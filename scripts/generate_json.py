#!/usr/bin/env python3
"""
Neuro Clinical Plans - Markdown to JSON Generator

Parses markdown clinical plan templates and generates JSON for the Clinical Plan Builder.
Includes built-in validation to ensure parity between markdown and JSON.

Usage:
    python scripts/generate_json.py docs/plans/status-epilepticus.md
    python scripts/generate_json.py docs/plans/status-epilepticus.md --validate-only
    python scripts/generate_json.py docs/plans/status-epilepticus.md --check-parity
    python scripts/generate_json.py docs/plans/status-epilepticus.md --output custom.json
    python scripts/generate_json.py --all  # Process all plans in docs/plans/

Pipeline position: Run LAST after all other skills complete
    Builder → Checker → Rebuilder → Citation Verifier → ICD/Synonym Enricher → JSON Generator

Parity Validation:
    The --check-parity flag compares markdown item counts against existing JSON in plans.json.
    This catches discrepancies before deployment and prevents content from going missing
    in the Clinical Plan Builder.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """Stores validation results for reporting."""
    passed: bool = True
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    stats: dict = field(default_factory=dict)


class MarkdownParser:
    """Parses markdown clinical plan templates into structured data."""

    # Section patterns
    SECTION_PATTERNS = {
        'labs_core': r'###?\s*1A[.\s]+Essential|###?\s*1A[.\s]+Core',
        'labs_extended': r'###?\s*1B[.\s]+Extended',
        'labs_rare': r'###?\s*1C[.\s]+Rare|###?\s*1C[.\s]+Specialized',
        'imaging_essential': r'###?\s*2A[.\s]+Essential|###?\s*2A[.\s]+First-line',
        'imaging_extended': r'###?\s*2B[.\s]+Extended',
        'imaging_rare': r'###?\s*2C[.\s]+Rare|###?\s*2C[.\s]+Specialized',
        'lumbar_puncture': r'###?\s*LUMBAR PUNCTURE|###?\s*LP Studies',
        'treatment_acute': r'###?\s*3A[.\s]+Acute|###?\s*3A[.\s]+Emergent',
        'treatment_symptomatic': r'###?\s*3B[.\s]+Symptomatic|###?\s*3B[.\s]+First-line',
        'treatment_secondline': r'###?\s*3C[.\s]+Second-line|###?\s*3C[.\s]+Refractory',
        'treatment_dmt': r'###?\s*3D[.\s]+Disease-Modifying|###?\s*3D[.\s]+Chronic',
        'treatment_super_refractory': r'###?\s*3E[.\s]+Super-Refractory',
        'treatment_immunotherapy': r'###?\s*3F[.\s]+Immunotherapy|###?\s*3F[.\s]+NORSE',
        'treatment_supportive': r'###?\s*3G[.\s]+Supportive|###?\s*3G[.\s]+Symptomatic.*ICU',
        'referrals': r'###?\s*4A[.\s]+Referrals|###?\s*4A[.\s]+Consults',
        'patient_instructions': r'###?\s*4B[.\s]+Patient',
        'lifestyle': r'###?\s*4C[.\s]+Lifestyle|###?\s*4C[.\s]+Prevention',
        'differential': r'##?\s*5[.\s]+DIFFERENTIAL',
        'monitoring': r'##?\s*6[.\s]+MONITORING',
        'disposition': r'##?\s*7[.\s]+DISPOSITION',
        'evidence': r'##?\s*8[.\s]+EVIDENCE',
    }

    # Priority values
    VALID_PRIORITIES = {'STAT', 'URGENT', 'ROUTINE', 'EXT', '-'}

    def __init__(self, markdown_path: Path):
        self.markdown_path = markdown_path
        self.content = markdown_path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')

    def parse(self) -> dict:
        """Parse the markdown file into a structured dictionary."""
        result = {
            'id': self._extract_id(),
            'title': self._extract_title(),
            'version': self._extract_version(),
            'icd10': self._extract_icd10(),
            'notes': self._extract_notes(),
            'sections': []
        }

        # Parse each section type
        result['sections'] = self._parse_all_sections()

        return result

    def _extract_id(self) -> str:
        """Extract plan ID from filename."""
        return self.markdown_path.stem

    def _extract_title(self) -> str:
        """Extract title from frontmatter or first heading."""
        # Try frontmatter first
        frontmatter_match = re.search(r'^---\s*\n.*?title:\s*["\']?([^"\'\n]+)["\']?\s*\n.*?---',
                                       self.content, re.DOTALL)
        if frontmatter_match:
            return frontmatter_match.group(1).strip()

        # Fall back to DIAGNOSIS line
        diagnosis_match = re.search(r'DIAGNOSIS:\s*(.+)', self.content)
        if diagnosis_match:
            return diagnosis_match.group(1).strip()

        # Fall back to first H1
        h1_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()

        return self.markdown_path.stem.replace('-', ' ').title()

    def _extract_version(self) -> str:
        """Extract version from frontmatter or change log."""
        # Try frontmatter
        version_match = re.search(r'version:\s*["\']?([^"\'\n]+)["\']?', self.content)
        if version_match:
            return version_match.group(1).strip()

        # Try change log - find the first version entry
        changelog_match = re.search(r'\*\*v(\d+\.\d+)', self.content)
        if changelog_match:
            return changelog_match.group(1)

        return '1.0'

    def _extract_icd10(self) -> list:
        """Extract ICD-10 codes."""
        icd_match = re.search(r'ICD-10:\s*(.+)', self.content)
        if icd_match:
            codes = icd_match.group(1).strip()
            return [c.strip() for c in re.split(r'[,;]', codes)]
        return []

    def _extract_notes(self) -> str:
        """Extract clinical notes/scope."""
        scope_match = re.search(r'SCOPE:\s*(.+)', self.content)
        if scope_match:
            return scope_match.group(1).strip()
        return ''

    def _parse_all_sections(self) -> list:
        """Parse all sections from the markdown."""
        sections = []

        # Laboratory Workup
        lab_sections = self._parse_lab_sections()
        if lab_sections:
            sections.append({
                'title': 'Laboratory Workup',
                'subsections': lab_sections
            })

        # Imaging & Studies
        imaging_sections = self._parse_imaging_sections()
        if imaging_sections:
            sections.append({
                'title': 'Diagnostic Imaging & Studies',
                'subsections': imaging_sections
            })

        # Treatment
        treatment_sections = self._parse_treatment_sections()
        if treatment_sections:
            sections.append({
                'title': 'Treatment',
                'subsections': treatment_sections
            })

        # Other Recommendations
        other_sections = self._parse_other_sections()
        if other_sections:
            sections.append({
                'title': 'Other Recommendations',
                'subsections': other_sections
            })

        # Monitoring Parameters
        monitoring_items = self._parse_monitoring_section()
        if monitoring_items:
            sections.append({
                'title': 'Monitoring Parameters',
                'items': monitoring_items
            })

        # Disposition Criteria
        disposition_items = self._parse_disposition_section()
        if disposition_items:
            sections.append({
                'title': 'Disposition Criteria',
                'items': disposition_items
            })

        # Evidence & References
        evidence_items = self._parse_evidence_section()
        if evidence_items:
            sections.append({
                'title': 'Evidence & References',
                'items': evidence_items
            })

        return sections

    def _parse_lab_sections(self) -> list:
        """Parse laboratory workup sections."""
        subsections = []

        # Core Labs
        core_items = self._parse_table_section('labs_core', 'labs_extended')
        if core_items:
            subsections.append({'title': 'Essential/Core Labs', 'items': core_items})

        # Extended Labs
        extended_items = self._parse_table_section('labs_extended', 'labs_rare')
        if extended_items:
            subsections.append({'title': 'Extended Workup', 'items': extended_items})

        # Rare/Specialized Labs
        rare_items = self._parse_table_section('labs_rare', 'imaging_essential')
        if rare_items:
            subsections.append({'title': 'Rare/Specialized', 'items': rare_items})

        return subsections

    def _parse_imaging_sections(self) -> list:
        """Parse imaging sections."""
        subsections = []

        # Essential Imaging
        essential_items = self._parse_table_section('imaging_essential', 'imaging_extended')
        if essential_items:
            subsections.append({'title': 'Essential/First-line', 'items': essential_items})

        # Extended Imaging
        extended_items = self._parse_table_section('imaging_extended', 'imaging_rare')
        if extended_items:
            subsections.append({'title': 'Extended', 'items': extended_items})

        # Rare/Specialized Imaging
        rare_items = self._parse_table_section('imaging_rare', 'lumbar_puncture')
        if rare_items:
            subsections.append({'title': 'Rare/Specialized', 'items': rare_items})

        # Lumbar Puncture
        lp_items = self._parse_table_section('lumbar_puncture', 'treatment_acute')
        if lp_items:
            subsections.append({'title': 'Lumbar Puncture', 'items': lp_items})

        return subsections

    def _parse_treatment_sections(self) -> list:
        """Parse treatment sections."""
        subsections = []

        # Acute/Emergent
        acute_items = self._parse_table_section('treatment_acute', 'treatment_symptomatic')
        if acute_items:
            subsections.append({'title': 'Acute/Emergent', 'items': acute_items})

        # Symptomatic
        symptomatic_items = self._parse_table_section('treatment_symptomatic', 'treatment_secondline')
        if symptomatic_items:
            subsections.append({'title': 'Symptomatic Treatments', 'items': symptomatic_items})

        # Second-line/Refractory
        secondline_items = self._parse_table_section('treatment_secondline', 'treatment_dmt')
        if secondline_items:
            subsections.append({'title': 'Second-line/Refractory', 'items': secondline_items})

        # Disease-Modifying
        dmt_items = self._parse_table_section('treatment_dmt', 'treatment_super_refractory')
        if dmt_items:
            subsections.append({'title': 'Disease-Modifying', 'items': dmt_items})

        # Super-Refractory
        super_items = self._parse_table_section('treatment_super_refractory', 'treatment_immunotherapy')
        if super_items:
            subsections.append({'title': 'Super-Refractory', 'items': super_items})

        # Immunotherapy
        immuno_items = self._parse_table_section('treatment_immunotherapy', 'treatment_supportive')
        if immuno_items:
            subsections.append({'title': 'Immunotherapy', 'items': immuno_items})

        # Supportive/ICU Care
        supportive_items = self._parse_table_section('treatment_supportive', 'referrals')
        if supportive_items:
            subsections.append({'title': 'Supportive/ICU Care', 'items': supportive_items})

        return subsections

    def _parse_other_sections(self) -> list:
        """Parse other recommendations sections."""
        subsections = []

        # Referrals
        referral_items = self._parse_table_section('referrals', 'patient_instructions')
        if referral_items:
            subsections.append({'title': 'Referrals & Consults', 'items': referral_items})

        # Patient Instructions
        instruction_items = self._parse_table_section('patient_instructions', 'lifestyle')
        if instruction_items:
            subsections.append({'title': 'Patient Instructions', 'items': instruction_items})

        # Lifestyle
        lifestyle_items = self._parse_table_section('lifestyle', 'differential')
        if lifestyle_items:
            subsections.append({'title': 'Lifestyle & Prevention', 'items': lifestyle_items})

        return subsections

    def _parse_monitoring_section(self) -> list:
        """Parse monitoring parameters section."""
        return self._parse_table_section('monitoring', 'disposition')

    def _parse_disposition_section(self) -> list:
        """Parse disposition criteria section."""
        items = []
        start_idx = self._find_section_start('disposition')
        end_idx = self._find_section_start('evidence')

        if start_idx is None:
            return items

        if end_idx is None:
            end_idx = len(self.lines)

        # Look for table rows
        in_table = False
        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if len(cells) >= 2 and cells[0] and not cells[0].lower().startswith('disposition'):
                    items.append({
                        'disposition': cells[0],
                        'criteria': cells[1] if len(cells) > 1 else ''
                    })
                in_table = True
            elif in_table and not line.startswith('|'):
                break

        return items

    def _parse_evidence_section(self) -> list:
        """Parse evidence & references section."""
        items = []
        start_idx = self._find_section_start('evidence')

        if start_idx is None:
            return items

        # Find end (next major section or appendix or end of file)
        end_idx = len(self.lines)
        for i in range(start_idx + 1, len(self.lines)):
            line = self.lines[i].strip()
            if line.startswith('## ') and 'APPENDIX' not in line.upper():
                end_idx = i
                break
            if line.startswith('---') and i > start_idx + 5:
                end_idx = i
                break

        # Parse table rows
        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if len(cells) >= 3 and cells[0] and not cells[0].lower().startswith('recommendation'):
                    items.append({
                        'recommendation': cells[0],
                        'evidenceLevel': cells[1] if len(cells) > 1 else '',
                        'source': cells[2] if len(cells) > 2 else ''
                    })

        return items

    def _find_section_start(self, section_key: str) -> int | None:
        """Find the starting line index of a section."""
        pattern = self.SECTION_PATTERNS.get(section_key)
        if not pattern:
            return None

        for i, line in enumerate(self.lines):
            if re.search(pattern, line, re.IGNORECASE):
                return i

        return None

    def _find_next_section(self, after_key: str) -> int | None:
        """Find the next section after the given one."""
        # Get ordered list of section keys
        keys = list(self.SECTION_PATTERNS.keys())
        try:
            current_idx = keys.index(after_key)
        except ValueError:
            return None

        # Search for subsequent sections
        for key in keys[current_idx + 1:]:
            idx = self._find_section_start(key)
            if idx is not None:
                return idx

        return None

    def _parse_table_section(self, start_key: str, end_key: str = None) -> list:
        """Parse a table section between two section markers."""
        items = []
        start_idx = self._find_section_start(start_key)

        if start_idx is None:
            return items

        # Find end boundary
        if end_key:
            end_idx = self._find_section_start(end_key)
        else:
            end_idx = self._find_next_section(start_key)

        if end_idx is None:
            # Look for next ## heading
            for i in range(start_idx + 1, len(self.lines)):
                if self.lines[i].strip().startswith('## '):
                    end_idx = i
                    break
            if end_idx is None:
                end_idx = len(self.lines)

        # Parse table
        header_cols = []
        in_table = False

        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if not line.startswith('|'):
                if in_table:
                    break
                continue

            cells = [c.strip() for c in line.split('|')[1:-1]]

            # Skip separator row
            if all(set(c) <= {'-', ':', ' '} for c in cells):
                continue

            # Detect header row
            if not in_table:
                header_cols = [c.lower() for c in cells]
                in_table = True
                continue

            # Parse data row
            if len(cells) > 0 and cells[0]:
                item = self._parse_table_row(cells, header_cols)
                if item:
                    items.append(item)

        return items

    def _parse_table_row(self, cells: list, headers: list) -> dict | None:
        """Parse a single table row into an item dictionary."""
        if not cells or not cells[0]:
            return None

        item = {}

        for i, header in enumerate(headers):
            if i >= len(cells):
                break

            value = cells[i].strip()
            if not value:
                continue

            # Map header to JSON field
            field = self._map_header_to_field(header)
            if field:
                item[field] = value

        return item if item else None

    def _map_header_to_field(self, header: str) -> str | None:
        """Map a table header to a JSON field name."""
        header = header.lower().strip()

        mappings = {
            'test': 'item',
            'study': 'item',
            'treatment': 'item',
            'medication': 'item',
            'drug': 'item',
            'recommendation': 'item',
            'parameter': 'item',
            'ed': 'ED',
            'hosp': 'HOSP',
            'opd': 'OPD',
            'icu': 'ICU',
            'rationale': 'rationale',
            'indication': 'indication',
            'timing': 'timing',
            'target': 'target',
            'target finding': 'target',
            'contraindications': 'contraindications',
            'contraindication': 'contraindications',
            'monitoring': 'monitoring',
            'dosing': 'dosing',
            'dose': 'dosing',
            'frequency': 'frequency',
            'action if abnormal': 'action',
            'threshold': 'threshold',
            'priority': 'priority',
        }

        return mappings.get(header, None)


class ParityChecker:
    """Checks parity between markdown content and existing JSON in plans.json."""

    def __init__(self, markdown_path: Path, plans_json_path: Path = None):
        self.markdown_path = markdown_path
        self.plans_json_path = plans_json_path or Path('docs/data/plans.json')
        self.discrepancies = []
        self.md_counts = {}
        self.json_counts = {}

    def check(self) -> tuple[bool, list]:
        """
        Check parity between markdown and JSON.
        Returns (parity_ok, discrepancies_list)
        """
        # Count items in markdown
        self.md_counts = self._count_markdown_items()

        # Count items in JSON
        self.json_counts = self._count_json_items()

        # Compare
        self._compare_counts()

        parity_ok = len(self.discrepancies) == 0
        return parity_ok, self.discrepancies

    def _count_markdown_items(self) -> dict:
        """Count items in each markdown section by parsing tables."""
        counts = {}
        content = self.markdown_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        # Track current section
        current_section = None
        current_subsection = None
        in_table = False
        item_count = 0

        section_patterns = [
            (r'##?\s*1[.\s]+LABORATORY', 'Laboratory Workup'),
            (r'###?\s*1A', 'Core Labs'),
            (r'###?\s*1B', 'Extended Workup'),
            (r'###?\s*1C', 'Rare/Specialized Labs'),
            (r'##?\s*2[.\s]+DIAGNOSTIC', 'Diagnostic Imaging'),
            (r'###?\s*2A', 'Essential Imaging'),
            (r'###?\s*2B', 'Extended Imaging'),
            (r'###?\s*2C', 'Rare/Specialized Imaging'),
            (r'###?\s*LUMBAR', 'Lumbar Puncture'),
            (r'##?\s*3[.\s]+TREATMENT', 'Treatment'),
            (r'###?\s*3A', 'Stabilization/Acute'),
            (r'###?\s*3B', 'First-Line/Emergent'),
            (r'###?\s*3C', 'Second-Line ASM'),
            (r'###?\s*3D', 'Refractory SE'),
            (r'###?\s*3E', 'Super-Refractory'),
            (r'###?\s*3F', 'NORSE/Immunotherapy'),
            (r'###?\s*3G', 'Supportive Care'),
            (r'##?\s*4[.\s]+OTHER', 'Other Recommendations'),
            (r'###?\s*4A', 'Referrals'),
            (r'###?\s*4B', 'Patient Instructions'),
            (r'###?\s*4C', 'Lifestyle'),
            (r'##?\s*5[.\s]+DIFFERENTIAL', 'Differential Diagnosis'),
            (r'##?\s*6[.\s]+MONITORING', 'Monitoring Parameters'),
            (r'##?\s*7[.\s]+DISPOSITION', 'Disposition Criteria'),
            (r'##?\s*8[.\s]+EVIDENCE', 'Evidence & References'),
        ]

        for line in lines:
            # Check for section headers
            for pattern, section_name in section_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Save previous subsection count
                    if current_subsection and item_count > 0:
                        counts[current_subsection] = item_count
                    current_subsection = section_name
                    item_count = 0
                    in_table = False
                    break

            # Count table rows (items)
            if line.strip().startswith('|'):
                cells = [c.strip() for c in line.split('|')[1:-1]]
                # Skip header rows and separator rows
                if cells and not all(set(c) <= {'-', ':', ' '} for c in cells):
                    # Skip rows where first cell is a header-like word
                    first_cell = cells[0].lower() if cells else ''
                    header_words = ['test', 'study', 'treatment', 'medication', 'recommendation',
                                   'parameter', 'disposition', 'alternative diagnosis', 'diagnosis']
                    if first_cell and first_cell not in header_words and not first_cell.startswith('---'):
                        item_count += 1
                        in_table = True
            elif in_table and not line.strip().startswith('|') and line.strip():
                # End of table - but keep counting if next table
                pass

        # Save final subsection
        if current_subsection and item_count > 0:
            counts[current_subsection] = item_count

        return counts

    def _count_json_items(self) -> dict:
        """Count items in each JSON section."""
        counts = {}

        if not self.plans_json_path.exists():
            return counts

        with open(self.plans_json_path, 'r', encoding='utf-8') as f:
            plans_data = json.load(f)

        # Find the plan by matching filename
        plan_name = self.markdown_path.stem.replace('-', ' ').title()

        # Try different name formats
        plan_data = None
        for key in plans_data:
            if key.lower().replace(' ', '-') == self.markdown_path.stem.lower():
                plan_data = plans_data[key]
                break
            if key.lower() == plan_name.lower():
                plan_data = plans_data[key]
                break

        if not plan_data:
            # Try Status Epilepticus specifically
            if 'Status Epilepticus' in plans_data:
                plan_data = plans_data['Status Epilepticus']

        if not plan_data:
            return counts

        # Count items in sections
        sections = plan_data.get('sections', {})
        if isinstance(sections, dict):
            for section_name, section_data in sections.items():
                if isinstance(section_data, dict):
                    for subsection_name, items in section_data.items():
                        if isinstance(items, list):
                            counts[subsection_name] = len(items)
                elif isinstance(section_data, list):
                    counts[section_name] = len(section_data)

        # Also check top-level arrays
        for key in ['differential', 'evidence', 'notes', 'definitions']:
            if key in plan_data and isinstance(plan_data[key], list):
                counts[key.title()] = len(plan_data[key])

        return counts

    def _normalize_section_name(self, name: str) -> str:
        """Normalize section names for comparison."""
        # Common variations to standardize
        normalizations = {
            'stabilization/acute': 'stabilization',
            'first-line/emergent': 'first-line benzodiazepines',
            'first-line (benzodiazepines)': 'first-line benzodiazepines',
            'second-line asm': 'second-line asms',
            'refractory se': 'refractory se (anesthetics)',
            'super-refractory': 'super-refractory se',
            'norse/immunotherapy': 'norse immunotherapy',
            'norse/fires first-line immunotherapy': 'norse immunotherapy',  # Combine NORSE sections
            'norse/fires second-line immunotherapy': 'norse immunotherapy',  # Combine NORSE sections
            'norse first-line immunotherapy': 'norse immunotherapy',
            'norse second-line immunotherapy': 'norse immunotherapy',
            'supportive care': 'symptomatic/supportive icu care',
            'essential imaging': 'essential',
            'extended imaging': 'extended',
            'rare/specialized imaging': 'rare/specialized',
            'rare/specialized labs': 'rare/specialized',  # Combine rare labs
            'specialized': 'rare/specialized',
            'differential diagnosis': 'differential',
            'evidence & references': 'evidence',
            'monitoring parameters': 'monitoring',
            'disposition criteria': 'criteria',
            'continuous monitoring': 'monitoring',  # Combine monitoring
            'intermittent monitoring': 'monitoring',  # Combine monitoring
            'monitoring continuous': 'monitoring',
            'monitoring intermittent': 'monitoring',
            'patient instructions': 'education',
            'lifestyle': 'prevention',
            'referrals': 'consults',
        }
        lower = name.lower().strip()
        return normalizations.get(lower, lower)

    # Sections that exist only in JSON and are expected (not errors)
    JSON_ONLY_SECTIONS = {'definitions', 'notes', 'treatment'}

    def _compare_counts(self):
        """Compare markdown and JSON counts, recording discrepancies."""
        # Normalize all section names
        normalized_md = {}
        for section, count in self.md_counts.items():
            norm_name = self._normalize_section_name(section)
            normalized_md[norm_name] = normalized_md.get(norm_name, 0) + count

        normalized_json = {}
        for section, count in self.json_counts.items():
            norm_name = self._normalize_section_name(section)
            normalized_json[norm_name] = normalized_json.get(norm_name, 0) + count

        all_sections = set(normalized_md.keys()) | set(normalized_json.keys())

        for section in sorted(all_sections):
            # Skip sections that only exist in JSON by design
            if section in self.JSON_ONLY_SECTIONS:
                continue

            md_count = normalized_md.get(section, 0)
            json_count = normalized_json.get(section, 0)

            if md_count != json_count:
                diff = md_count - json_count
                direction = "missing from JSON" if diff > 0 else "extra in JSON"
                self.discrepancies.append({
                    'section': section,
                    'markdown_count': md_count,
                    'json_count': json_count,
                    'difference': abs(diff),
                    'direction': direction
                })

        # Update counts with normalized versions for reporting
        self.md_counts = normalized_md
        self.json_counts = normalized_json


def print_parity_report(parity_ok: bool, discrepancies: list, md_counts: dict, json_counts: dict):
    """Print a formatted parity report."""
    print(f"\n{'='*70}")
    print("PARITY CHECK REPORT")
    print('='*70)

    # Summary table
    print(f"\n{'Section':<35} {'Markdown':>10} {'JSON':>10} {'Status':>12}")
    print('-'*70)

    all_sections = sorted(set(md_counts.keys()) | set(json_counts.keys()))
    for section in all_sections:
        md = md_counts.get(section, 0)
        js = json_counts.get(section, 0)
        if md == js:
            status = "✅ OK"
        elif md > js:
            status = f"❌ -{md-js} missing"
        else:
            status = f"⚠️ +{js-md} extra"
        print(f"{section:<35} {md:>10} {js:>10} {status:>12}")

    print('-'*70)

    # Totals
    md_total = sum(md_counts.values())
    json_total = sum(json_counts.values())
    print(f"{'TOTAL':<35} {md_total:>10} {json_total:>10}")

    # Discrepancy details
    if discrepancies:
        print(f"\n❌ DISCREPANCIES FOUND ({len(discrepancies)}):")
        print("-"*70)
        for d in discrepancies:
            print(f"  • {d['section']}: {d['difference']} items {d['direction']}")
            print(f"    Markdown: {d['markdown_count']}, JSON: {d['json_count']}")

    # Overall status
    print(f"\n{'='*70}")
    if parity_ok:
        print("✅ PARITY CHECK PASSED - Markdown and JSON are in sync")
    else:
        print("❌ PARITY CHECK FAILED - Fix discrepancies before deployment")
        print("\nTo fix: Run 'python scripts/generate_json.py <file> --merge' to regenerate JSON")
    print('='*70 + '\n')


class JSONValidator:
    """Validates generated JSON for completeness and correctness."""

    REQUIRED_SECTIONS = [
        'Laboratory Workup',
        'Diagnostic Imaging & Studies',
        'Treatment',
        'Other Recommendations',
        'Monitoring Parameters',
        'Disposition Criteria',
    ]

    MEDICATION_SECTIONS = [
        'Acute/Emergent',
        'Symptomatic Treatments',
        'Second-line/Refractory',
        'Disease-Modifying',
        'Super-Refractory',
        'Immunotherapy',
        'Supportive/ICU Care',
    ]

    def __init__(self, json_data: dict, markdown_path: Path = None):
        self.data = json_data
        self.markdown_path = markdown_path
        self.result = ValidationResult()

    def validate(self) -> ValidationResult:
        """Run all validation checks."""
        self._validate_required_fields()
        self._validate_sections()
        self._validate_items()
        self._validate_medications()
        self._calculate_stats()

        return self.result

    def _validate_required_fields(self):
        """Check required top-level fields."""
        required = ['id', 'title', 'version', 'sections']

        for field in required:
            if field not in self.data or not self.data[field]:
                self.result.errors.append(f"Missing required field: {field}")
                self.result.passed = False

    def _validate_sections(self):
        """Check that required sections exist."""
        section_titles = []
        for section in self.data.get('sections', []):
            section_titles.append(section.get('title', ''))

        for required in self.REQUIRED_SECTIONS:
            if required not in section_titles:
                self.result.warnings.append(f"Missing section: {required}")

    def _validate_items(self):
        """Validate individual items have required fields."""
        total_items = 0
        items_with_priorities = 0

        for section in self.data.get('sections', []):
            items = section.get('items', [])
            subsections = section.get('subsections', [])

            for item in items:
                total_items += 1
                if self._has_priority_fields(item):
                    items_with_priorities += 1

            for subsection in subsections:
                for item in subsection.get('items', []):
                    total_items += 1
                    if self._has_priority_fields(item):
                        items_with_priorities += 1

        self.result.stats['total_items'] = total_items
        self.result.stats['items_with_priorities'] = items_with_priorities

        if total_items == 0:
            self.result.errors.append("No items found in any section")
            self.result.passed = False

    def _has_priority_fields(self, item: dict) -> bool:
        """Check if item has at least one priority field."""
        priority_fields = ['ED', 'HOSP', 'OPD', 'ICU']
        return any(field in item for field in priority_fields)

    def _validate_medications(self):
        """Check that medications have required safety fields."""
        meds_total = 0
        meds_with_dosing = 0
        meds_with_contraindications = 0
        meds_missing_dosing = []
        meds_missing_contraindications = []

        for section in self.data.get('sections', []):
            if section.get('title') != 'Treatment':
                continue

            for subsection in section.get('subsections', []):
                if subsection.get('title') in self.MEDICATION_SECTIONS:
                    for item in subsection.get('items', []):
                        meds_total += 1
                        item_name = item.get('item', 'Unknown')

                        if item.get('dosing'):
                            meds_with_dosing += 1
                        else:
                            meds_missing_dosing.append(item_name)

                        if item.get('contraindications'):
                            meds_with_contraindications += 1
                        else:
                            meds_missing_contraindications.append(item_name)

        self.result.stats['medications_total'] = meds_total
        self.result.stats['medications_with_dosing'] = meds_with_dosing
        self.result.stats['medications_with_contraindications'] = meds_with_contraindications

        if meds_missing_dosing:
            self.result.warnings.append(
                f"Medications missing dosing ({len(meds_missing_dosing)}): {', '.join(meds_missing_dosing[:5])}"
                + ('...' if len(meds_missing_dosing) > 5 else '')
            )

        if meds_missing_contraindications:
            self.result.warnings.append(
                f"Medications missing contraindications ({len(meds_missing_contraindications)}): {', '.join(meds_missing_contraindications[:5])}"
                + ('...' if len(meds_missing_contraindications) > 5 else '')
            )

    def _calculate_stats(self):
        """Calculate summary statistics."""
        self.result.stats['sections_count'] = len(self.data.get('sections', []))

        # Count subsections
        subsection_count = 0
        for section in self.data.get('sections', []):
            subsection_count += len(section.get('subsections', []))
        self.result.stats['subsections_count'] = subsection_count


def generate_json(markdown_path: Path, output_path: Path = None, validate_only: bool = False) -> tuple[dict, ValidationResult]:
    """Generate JSON from markdown and optionally validate."""

    # Parse markdown
    parser = MarkdownParser(markdown_path)
    json_data = parser.parse()

    # Validate
    validator = JSONValidator(json_data, markdown_path)
    validation = validator.validate()

    # Write output unless validate-only
    if not validate_only and output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

    return json_data, validation


def print_validation_report(validation: ValidationResult, plan_title: str):
    """Print a formatted validation report."""
    print(f"\n{'='*60}")
    print(f"VALIDATION REPORT: {plan_title}")
    print('='*60)

    # Stats
    stats = validation.stats
    print(f"\nStatistics:")
    print(f"  Sections: {stats.get('sections_count', 0)}")
    print(f"  Subsections: {stats.get('subsections_count', 0)}")
    print(f"  Total items: {stats.get('total_items', 0)}")
    print(f"  Items with priorities: {stats.get('items_with_priorities', 0)}")

    if stats.get('medications_total', 0) > 0:
        print(f"\nMedications:")
        print(f"  Total: {stats.get('medications_total', 0)}")
        print(f"  With dosing: {stats.get('medications_with_dosing', 0)}/{stats.get('medications_total', 0)}")
        print(f"  With contraindications: {stats.get('medications_with_contraindications', 0)}/{stats.get('medications_total', 0)}")

    # Errors
    if validation.errors:
        print(f"\n❌ ERRORS ({len(validation.errors)}):")
        for error in validation.errors:
            print(f"  - {error}")

    # Warnings
    if validation.warnings:
        print(f"\n⚠️  WARNINGS ({len(validation.warnings)}):")
        for warning in validation.warnings:
            print(f"  - {warning}")

    # Overall status
    print(f"\n{'='*60}")
    if validation.passed and not validation.warnings:
        print("✅ PASSED - All validations successful")
    elif validation.passed:
        print("⚠️  PASSED with warnings")
    else:
        print("❌ FAILED - Fix errors before deployment")
    print('='*60 + '\n')


def merge_into_plans_json(new_plan: dict, plans_json_path: Path):
    """Merge a new plan into the existing plans.json file."""

    # Load existing plans.json
    if plans_json_path.exists():
        with open(plans_json_path, 'r', encoding='utf-8') as f:
            plans_data = json.load(f)
    else:
        plans_data = {}

    # Add or update the plan
    plan_key = new_plan.get('title', new_plan.get('id', 'Unknown'))
    plans_data[plan_key] = new_plan

    # Write back
    with open(plans_json_path, 'w', encoding='utf-8') as f:
        json.dump(plans_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Merged '{plan_key}' into {plans_json_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate JSON from markdown clinical plan templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        'markdown_file',
        nargs='?',
        help='Path to markdown template file'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all markdown files in docs/plans/'
    )

    parser.add_argument(
        '--output', '-o',
        help='Output JSON file path (default: same name as input with .json extension)'
    )

    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate existing markdown, do not generate JSON'
    )

    parser.add_argument(
        '--merge',
        action='store_true',
        help='Merge output into docs/data/plans.json instead of separate file'
    )

    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress validation report output'
    )

    parser.add_argument(
        '--check-parity',
        action='store_true',
        help='Check parity between markdown and existing JSON in plans.json'
    )

    parser.add_argument(
        '--fail-on-parity',
        action='store_true',
        help='Exit with error code if parity check fails (useful for CI)'
    )

    args = parser.parse_args()

    # Determine files to process
    if args.all:
        # Find all markdown files in docs/plans/
        plans_dir = Path('docs/plans')
        if not plans_dir.exists():
            print(f"Error: Directory {plans_dir} not found")
            sys.exit(1)
        markdown_files = list(plans_dir.glob('*.md'))
        if not markdown_files:
            print(f"No markdown files found in {plans_dir}")
            sys.exit(1)
    elif args.markdown_file:
        markdown_files = [Path(args.markdown_file)]
    else:
        parser.print_help()
        sys.exit(1)

    # Process each file
    all_passed = True
    parity_failed = False

    for md_path in markdown_files:
        if not md_path.exists():
            print(f"Error: File not found: {md_path}")
            all_passed = False
            continue

        # Parity check mode
        if args.check_parity:
            checker = ParityChecker(md_path)
            parity_ok, discrepancies = checker.check()

            if not args.quiet:
                print_parity_report(parity_ok, discrepancies, checker.md_counts, checker.json_counts)

            if not parity_ok:
                parity_failed = True

            continue  # Skip generation in parity-check mode

        # Determine output path
        if args.output and len(markdown_files) == 1:
            output_path = Path(args.output)
        elif args.merge:
            output_path = None  # Will merge instead
        else:
            output_path = md_path.with_suffix('.json')

        # Generate and validate
        json_data, validation = generate_json(
            md_path,
            output_path if not args.merge else md_path.with_suffix('.json'),
            validate_only=args.validate_only
        )

        # Print report
        if not args.quiet:
            print_validation_report(validation, json_data.get('title', md_path.stem))

        # Merge if requested
        if args.merge and not args.validate_only:
            plans_json_path = Path('docs/data/plans.json')
            merge_into_plans_json(json_data, plans_json_path)

        if not validation.passed:
            all_passed = False

    # Exit codes
    if args.check_parity:
        if args.fail_on_parity and parity_failed:
            sys.exit(1)
        sys.exit(0)

    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
