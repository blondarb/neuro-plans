#!/usr/bin/env python3
"""
Neuro Clinical Plans - Markdown to JSON Generator

Parses markdown clinical plan templates and generates JSON for the Clinical Plan Builder.
Includes built-in validation to ensure parity between markdown and JSON.

Usage:
    python scripts/generate_json.py docs/plans/status-epilepticus.md
    python scripts/generate_json.py docs/plans/status-epilepticus.md --validate-only
    python scripts/generate_json.py docs/plans/status-epilepticus.md --output custom.json
    python scripts/generate_json.py --all  # Process all plans in docs/plans/

Pipeline position: Run LAST after all other skills complete
    Builder → Checker → Rebuilder → Citation Verifier → ICD/Synonym Enricher → JSON Generator
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

    for md_path in markdown_files:
        if not md_path.exists():
            print(f"Error: File not found: {md_path}")
            all_passed = False
            continue

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

    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
