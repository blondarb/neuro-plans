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

    # Section patterns - made more generic to handle various plan structures
    SECTION_PATTERNS = {
        'labs_core': r'###?\s*1A[.\s]+',
        'labs_extended': r'###?\s*1B[.\s]+',
        'labs_rare': r'###?\s*1C[.\s]+',
        'imaging_essential': r'###?\s*2A[.\s]+',
        'imaging_extended': r'###?\s*2B[.\s]+',
        'imaging_rare': r'###?\s*2C[.\s]+',
        'lumbar_puncture': r'###?\s*LUMBAR PUNCTURE|###?\s*LP Studies',
        'treatment_3a': r'###?\s*3A[.\s]+',
        'treatment_3b': r'###?\s*3B[.\s]+',
        'treatment_3c': r'###?\s*3C[.\s]+',
        'treatment_3d': r'###?\s*3D[.\s]+',
        'treatment_3e': r'###?\s*3E[.\s]+',
        'treatment_3f': r'###?\s*3F[.\s]+',
        'treatment_3g': r'###?\s*3G[.\s]+',
        'referrals': r'###?\s*4A[.\s]+',
        'patient_instructions': r'###?\s*4B[.\s]+',
        'lifestyle': r'###?\s*4C[.\s]+',
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
            'scope': self._extract_scope(),
            'notes': self._extract_notes(),  # Must be a list for clinical tool JS
            'sections': {}
        }

        # Parse main sections (for clinical tool)
        result['sections'] = self._parse_all_sections()

        # Parse top-level arrays (for reference sections in clinical tool)
        differential = self._parse_differential_section()
        if differential:
            result['differential'] = differential

        evidence = self._parse_evidence_section()
        if evidence:
            result['evidence'] = evidence

        monitoring = self._parse_monitoring_section()
        if monitoring:
            result['monitoring'] = monitoring

        disposition = self._parse_disposition_section()
        if disposition:
            result['disposition'] = disposition

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

    def _extract_notes(self) -> list:
        """Extract clinical notes as a list.

        Looks for a dedicated Clinical Notes section or returns empty list.
        Note: SCOPE is stored separately via _extract_scope().
        """
        notes = []

        # Look for Clinical Notes or Clinical Pearls section
        notes_match = re.search(
            r'(?:Clinical Notes|Clinical Pearls|KEY POINTS):\s*\n((?:[-•*]\s*.+\n?)+)',
            self.content, re.IGNORECASE
        )
        if notes_match:
            notes_text = notes_match.group(1)
            for line in notes_text.split('\n'):
                line = line.strip()
                if line and line[0] in '-•*':
                    notes.append(line.lstrip('-•* ').strip())

        return notes

    def _extract_scope(self) -> str:
        """Extract scope/description of the plan."""
        scope_match = re.search(r'SCOPE:\s*(.+)', self.content)
        if scope_match:
            return scope_match.group(1).strip()
        return ''

    def _parse_all_sections(self) -> dict:
        """Parse all sections from the markdown.

        Returns a dict with section names as keys and subsection dicts as values.
        This format is required by the clinical tool JavaScript.
        """
        sections = {}

        # Laboratory Workup
        lab_sections = self._parse_lab_sections()
        if lab_sections:
            sections['Laboratory Workup'] = self._subsections_to_dict(lab_sections)

        # Imaging & Studies
        imaging_sections = self._parse_imaging_sections()
        if imaging_sections:
            sections['Imaging & Studies'] = self._subsections_to_dict(imaging_sections)

        # Note: Lumbar Puncture is now a subsection under Laboratory Workup (not its own section)

        # Treatment
        treatment_sections = self._parse_treatment_sections()
        if treatment_sections:
            sections['Treatment'] = self._subsections_to_dict(treatment_sections)

        # Other Recommendations
        other_sections = self._parse_other_sections()
        if other_sections:
            sections['Other Recommendations'] = self._subsections_to_dict(other_sections)

        return sections

    def _subsections_to_dict(self, subsections_list: list) -> dict:
        """Convert list of subsections to dict format for clinical tool."""
        result = {}
        for subsection in subsections_list:
            title = subsection.get('title', 'Unknown')
            items = subsection.get('items', [])
            result[title] = items
        return result

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

        # Lumbar Puncture / CSF Studies (logically part of lab workup)
        # Note: LP appears under Labs in the clinical tool, even though it may be
        # positioned after Imaging in the markdown file for historical reasons
        lp_items = self._parse_table_section('lumbar_puncture', 'treatment_3a')
        if lp_items:
            subsections.append({'title': 'Lumbar Puncture', 'items': lp_items})

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

        # Note: Lumbar Puncture is now a subsection under Laboratory Workup

        return subsections

    def _parse_treatment_sections(self) -> list:
        """Parse treatment sections dynamically."""
        subsections = []

        # Define the treatment section sequence with their boundaries
        treatment_keys = [
            ('treatment_3a', 'treatment_3b'),
            ('treatment_3b', 'treatment_3c'),
            ('treatment_3c', 'treatment_3d'),
            ('treatment_3d', 'treatment_3e'),
            ('treatment_3e', 'treatment_3f'),
            ('treatment_3f', 'treatment_3g'),
            ('treatment_3g', 'referrals'),
        ]

        for start_key, end_key in treatment_keys:
            start_idx = self._find_section_start(start_key)
            if start_idx is None:
                continue

            # Extract the title from the actual markdown line
            title = self._extract_section_title(start_idx)

            items = self._parse_table_section(start_key, end_key)
            if items:
                subsections.append({'title': title, 'items': items})

        return subsections

    def _extract_section_title(self, line_idx: int) -> str:
        """Extract the section title from a markdown heading line."""
        line = self.lines[line_idx].strip()
        # Remove markdown heading markers and section numbers
        # Match patterns like "### 3A. Title" or "### 3B. Title"
        match = re.search(r'###?\s*\d[A-Z][.\s]+(.+)', line, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        # Fallback: remove leading # and return
        return re.sub(r'^#+\s*', '', line).strip()

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

    def _parse_differential_section(self) -> list:
        """Parse differential diagnosis section."""
        items = []
        start_idx = self._find_section_start('differential')
        end_idx = self._find_section_start('monitoring')

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
                if len(cells) >= 2 and cells[0] and not cells[0].lower().startswith('alternative'):
                    items.append({
                        'diagnosis': cells[0],
                        'features': cells[1] if len(cells) > 1 else '',
                        'tests': cells[2] if len(cells) > 2 else ''
                    })
                in_table = True
            elif in_table and not line.startswith('|'):
                break

        return items

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
        """Count items in each markdown section by parsing tables.

        This method carefully tracks section boundaries to avoid counting:
        - Appendix tables (algorithm timelines, etc.)
        - Change log entries
        - Notes sections
        - Timeline/overview tables that aren't actionable items
        """
        counts = {}
        content = self.markdown_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        # Track current section
        current_subsection = None
        in_table = False
        item_count = 0
        in_valid_section = False  # Track if we're in a countable section
        skip_next_table = False   # For skipping timeline tables

        # Patterns for sections we want to count (Sections 1-8)
        # Each pattern extracts the section title dynamically from the heading
        section_patterns = [
            # Main sections (## headers)
            (r'##?\s*1[.\s]+LABORATORY', 'Laboratory Workup'),
            (r'##?\s*2[.\s]+DIAGNOSTIC', 'Diagnostic Imaging'),
            (r'##?\s*3[.\s]+TREATMENT', 'Treatment'),
            (r'##?\s*4[.\s]+OTHER', 'Other Recommendations'),
            (r'##?\s*5[.\s]+DIFFERENTIAL', 'Differential Diagnosis'),
            (r'##?\s*6[.\s]+MONITORING', 'Monitoring Parameters'),
            (r'##?\s*7[.\s]+DISPOSITION', 'Disposition Criteria'),
            (r'##?\s*8[.\s]+EVIDENCE', 'Evidence & References'),
            # Subsections (### headers) - extract title dynamically
            (r'###\s*1A[.\s]+(.+)', None),  # Will use captured group
            (r'###\s*1B[.\s]+(.+)', None),
            (r'###\s*1C[.\s]+(.+)', None),
            (r'###\s*2A[.\s]+(.+)', None),
            (r'###\s*2B[.\s]+(.+)', None),
            (r'###\s*2C[.\s]+(.+)', None),
            (r'###\s*LUMBAR\s*PUNCTURE', 'Lumbar Puncture'),
            (r'###\s*3A[.\s]+(.+)', None),
            (r'###\s*3B[.\s]+(.+)', None),
            (r'###\s*3C[.\s]+(.+)', None),
            (r'###\s*3D[.\s]+(.+)', None),
            (r'###\s*3E[.\s]+(.+)', None),
            (r'###\s*3F[.\s]+(.+)', None),
            (r'###\s*3G[.\s]+(.+)', None),
            (r'###\s*4A[.\s]+(.+)', None),
            (r'###\s*4B[.\s]+(.+)', None),
            (r'###\s*4C[.\s]+(.+)', None),
        ]

        # Patterns that indicate we should STOP counting (end of main content)
        stop_patterns = [
            r'##?\s*APPENDIX',
            r'##?\s*NOTES\s*$',
            r'##?\s*CHANGE\s*LOG',
            r'##?\s*---\s*$',  # Horizontal rule often separates sections
        ]

        # Patterns for subsection headers within NORSE that we should skip counting
        # These are overview/timeline tables, not treatment items
        skip_table_patterns = [
            r'####?\s*Timeline-Based Protocol',
        ]

        for i, line in enumerate(lines):
            # Check if we hit a stop pattern (end of countable content)
            for pattern in stop_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Save current count before stopping
                    if current_subsection and item_count > 0:
                        counts[current_subsection] = counts.get(current_subsection, 0) + item_count
                    in_valid_section = False
                    current_subsection = None
                    item_count = 0
                    break

            if not in_valid_section and current_subsection is None:
                # Check if we're entering a valid section
                pass

            # Check for skip-table patterns (like Timeline-Based Protocol)
            for pattern in skip_table_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    skip_next_table = True
                    break

            # Check for section headers
            matched_section = False
            for pattern, section_name in section_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    # Save previous subsection count
                    if current_subsection and item_count > 0:
                        counts[current_subsection] = counts.get(current_subsection, 0) + item_count

                    # If section_name is None, extract from captured group or full match
                    if section_name is None:
                        if match.groups():
                            # Use the captured group (title after the section number)
                            current_subsection = match.group(1).strip()
                        else:
                            # Fall back to the full match
                            current_subsection = match.group(0).strip()
                    else:
                        current_subsection = section_name

                    item_count = 0
                    in_table = False
                    in_valid_section = True
                    skip_next_table = False  # Reset skip flag on new section
                    matched_section = True
                    break

            if matched_section:
                continue

            # Check for sub-subsection headers (#### First-Line Immunotherapy, etc.)
            # These indicate a new table is coming - reset skip flag if it's a treatment table
            if re.match(r'####\s+(?:First-Line|Second-Line)\s+Immunotherapy', line, re.IGNORECASE):
                skip_next_table = False  # These ARE treatment tables, don't skip

            # Skip reference tables (like "**ASM Therapeutic Level Reference:**")
            if re.match(r'\*\*.*Reference.*:\*\*', line, re.IGNORECASE):
                skip_next_table = True
                continue

            # Count table rows (items) only if we're in a valid section
            if in_valid_section and current_subsection and line.strip().startswith('|'):
                # Check if this is a new table after a skip pattern
                if skip_next_table:
                    # Check if we've moved past the table (non-table line encountered)
                    # For now, just skip until we see a new subsection header
                    continue

                cells = [c.strip() for c in line.split('|')[1:-1]]
                # Skip header rows and separator rows
                if cells and not all(set(c) <= {'-', ':', ' '} for c in cells):
                    # Skip rows where first cell is a header-like word
                    first_cell = cells[0].lower() if cells else ''
                    header_words = ['test', 'study', 'treatment', 'medication', 'recommendation',
                                   'parameter', 'disposition', 'alternative diagnosis', 'diagnosis',
                                   'timing', 'intervention']  # Added timing/intervention for timeline tables
                    if first_cell and first_cell not in header_words and not first_cell.startswith('---'):
                        # Additional check: skip timeline entries like "Day 0-3", "Day 7", etc.
                        if not re.match(r'\*?\*?day\s+\d', first_cell, re.IGNORECASE):
                            item_count += 1
                            in_table = True
            elif in_table and not line.strip().startswith('|') and line.strip():
                # End of table
                skip_next_table = False  # Reset after table ends

        # Save final subsection
        if current_subsection and item_count > 0:
            counts[current_subsection] = counts.get(current_subsection, 0) + item_count

        return counts

    def _count_json_items(self) -> dict:
        """Count items in each JSON section."""
        counts = {}

        if not self.plans_json_path.exists():
            return counts

        with open(self.plans_json_path, 'r', encoding='utf-8') as f:
            plans_data = json.load(f)

        # First, try to get the actual title from the markdown file
        # This is the most reliable way to match
        md_title = None
        md_content = self.markdown_path.read_text(encoding='utf-8')

        # Try frontmatter title first
        import re
        frontmatter_match = re.search(r'^---\s*\n.*?title:\s*["\']?([^"\'\n]+)["\']?\s*\n.*?---',
                                       md_content, re.DOTALL)
        if frontmatter_match:
            md_title = frontmatter_match.group(1).strip()

        # Fall back to DIAGNOSIS line
        if not md_title:
            diagnosis_match = re.search(r'DIAGNOSIS:\s*(.+)', md_content)
            if diagnosis_match:
                md_title = diagnosis_match.group(1).strip()

        # Find the plan by matching title from markdown
        plan_data = None
        if md_title and md_title in plans_data:
            plan_data = plans_data[md_title]

        # Try different name formats as fallback
        if not plan_data:
            plan_name = self.markdown_path.stem.replace('-', ' ').title()
            for key in plans_data:
                if key.lower().replace(' ', '-') == self.markdown_path.stem.lower():
                    plan_data = plans_data[key]
                    break
                if key.lower() == plan_name.lower():
                    plan_data = plans_data[key]
                    break

        if not plan_data:
            return counts

        # Count items in sections (accumulate for duplicate subsection names)
        sections = plan_data.get('sections', {})

        # Handle list-based sections structure (new format)
        if isinstance(sections, list):
            for section in sections:
                section_title = section.get('title', '')

                # Count items directly in section
                if 'items' in section and isinstance(section['items'], list):
                    counts[section_title] = counts.get(section_title, 0) + len(section['items'])

                # Count items in subsections
                if 'subsections' in section and isinstance(section['subsections'], list):
                    for subsection in section['subsections']:
                        subsection_title = subsection.get('title', '')
                        if 'items' in subsection and isinstance(subsection['items'], list):
                            counts[subsection_title] = counts.get(subsection_title, 0) + len(subsection['items'])

        # Handle dict-based sections structure (legacy format)
        elif isinstance(sections, dict):
            for section_name, section_data in sections.items():
                if isinstance(section_data, dict):
                    for subsection_name, items in section_data.items():
                        if isinstance(items, list):
                            # Accumulate counts for subsections with same name
                            counts[subsection_name] = counts.get(subsection_name, 0) + len(items)
                elif isinstance(section_data, list):
                    counts[section_name] = counts.get(section_name, 0) + len(section_data)

        # Also check top-level arrays
        for key in ['differential', 'evidence', 'notes', 'definitions', 'monitoring', 'disposition']:
            if key in plan_data and isinstance(plan_data[key], list):
                counts[key.title()] = len(plan_data[key])

        return counts

    def _normalize_section_name(self, name: str) -> str:
        """Normalize section names for comparison."""
        # Common variations to standardize
        normalizations = {
            # Status Epilepticus specific
            'stabilization/acute': 'stabilization',
            'first-line/emergent': 'first-line benzodiazepines',
            'first-line (benzodiazepines)': 'first-line benzodiazepines',
            'second-line asm': 'second-line asms',
            'refractory se': 'refractory se (anesthetics)',
            'super-refractory': 'super-refractory se',
            'norse/immunotherapy': 'norse immunotherapy',
            'norse/fires first-line immunotherapy': 'norse immunotherapy',
            'norse/fires second-line immunotherapy': 'norse immunotherapy',
            'norse first-line immunotherapy': 'norse immunotherapy',
            'norse second-line immunotherapy': 'norse immunotherapy',
            'supportive care': 'symptomatic/supportive icu care',

            # General section name mappings
            'essential/core labs': 'core labs',
            'core labs': 'core labs',
            'extended workup': 'extended workup',
            'extended workup (second-line)': 'extended workup',
            'rare/specialized': 'rare/specialized',
            'rare/specialized (refractory or atypical)': 'rare/specialized',
            'essential imaging': 'essential imaging',
            'essential/first-line': 'essential imaging',
            'extended imaging': 'extended imaging',
            'extended': 'extended imaging',
            'rare/specialized imaging': 'rare/specialized imaging',
            'rare/specialized labs': 'rare/specialized',
            'specialized': 'rare/specialized',
            'lumbar puncture': 'lumbar puncture',

            # Treatment sections
            'acute/emergent': 'acute/emergent',
            'symptomatic treatments': 'symptomatic treatments',
            'second-line/refractory': 'second-line/refractory',

            # Other recommendations
            'referrals & consults': 'referrals',
            'referrals': 'referrals',
            'consults': 'referrals',
            'patient instructions': 'patient instructions',
            'education': 'patient instructions',
            'lifestyle & prevention': 'lifestyle',
            'lifestyle': 'lifestyle',
            'prevention': 'lifestyle',

            # Reference sections
            'differential diagnosis': 'differential',
            'differential': 'differential',
            'evidence & references': 'evidence',
            'evidence': 'evidence',
            'monitoring parameters': 'monitoring',
            'monitoring': 'monitoring',
            'continuous monitoring': 'monitoring',
            'intermittent monitoring': 'monitoring',
            'monitoring continuous': 'monitoring',
            'monitoring intermittent': 'monitoring',
            'disposition criteria': 'disposition',
            'criteria': 'disposition',
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

    # Sections expected in the 'sections' dict
    REQUIRED_SECTIONS = [
        'Laboratory Workup',
        'Imaging & Studies',
        'Treatment',
        'Other Recommendations',
    ]

    # Top-level arrays (not in 'sections' dict)
    REQUIRED_TOP_LEVEL_ARRAYS = [
        'monitoring',
        'disposition',
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
        self._validate_clinical_tool_structure()
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

    def _validate_clinical_tool_structure(self):
        """Validate JSON structure is compatible with clinical tool.

        The clinical tool JavaScript expects:
        - sections: dict/object (NOT list)
        - notes: list/array (NOT string)
        - differential, evidence: lists at top level
        """
        # Check sections is a dict
        sections = self.data.get('sections')
        if sections is not None and not isinstance(sections, dict):
            self.result.errors.append(
                f"CRITICAL: 'sections' must be a dict/object, got {type(sections).__name__}. "
                "Clinical tool will fail to load this plan!"
            )
            self.result.passed = False

        # Check notes is a list (or missing)
        notes = self.data.get('notes')
        if notes is not None and not isinstance(notes, list):
            self.result.errors.append(
                f"CRITICAL: 'notes' must be a list/array, got {type(notes).__name__}. "
                "Clinical tool will crash when loading this plan!"
            )
            self.result.passed = False

        # Check top-level arrays are actually arrays
        for field in ['differential', 'evidence', 'monitoring', 'disposition']:
            value = self.data.get(field)
            if value is not None and not isinstance(value, list):
                self.result.errors.append(
                    f"'{field}' must be a list/array, got {type(value).__name__}"
                )
                self.result.passed = False

    def _validate_sections(self):
        """Check that required sections exist."""
        sections = self.data.get('sections', {})

        # Handle dict-based format (new format for clinical tool)
        if isinstance(sections, dict):
            section_titles = list(sections.keys())
        # Handle list-based format (legacy)
        elif isinstance(sections, list):
            section_titles = [s.get('title', '') for s in sections]
        else:
            section_titles = []

        for required in self.REQUIRED_SECTIONS:
            if required not in section_titles:
                self.result.warnings.append(f"Missing section: {required}")

        # Check top-level arrays (monitoring, disposition)
        for required in self.REQUIRED_TOP_LEVEL_ARRAYS:
            if required not in self.data or not self.data[required]:
                self.result.warnings.append(f"Missing top-level array: {required}")

    def _validate_items(self):
        """Validate individual items have required fields."""
        total_items = 0
        items_with_priorities = 0
        sections = self.data.get('sections', {})

        # Handle dict-based format (new format for clinical tool)
        if isinstance(sections, dict):
            for section_name, subsections in sections.items():
                if isinstance(subsections, dict):
                    for subsection_name, items in subsections.items():
                        if isinstance(items, list):
                            for item in items:
                                total_items += 1
                                if self._has_priority_fields(item):
                                    items_with_priorities += 1

        # Handle list-based format (legacy)
        elif isinstance(sections, list):
            for section in sections:
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

        sections = self.data.get('sections', {})

        # Handle dict-based format (new format for clinical tool)
        if isinstance(sections, dict):
            treatment_subsections = sections.get('Treatment', {})
            if isinstance(treatment_subsections, dict):
                for subsection_name, items in treatment_subsections.items():
                    if subsection_name in self.MEDICATION_SECTIONS and isinstance(items, list):
                        for item in items:
                            meds_total += 1
                            item_name = item.get('item', item.get('treatment', 'Unknown'))

                            if item.get('dosing'):
                                meds_with_dosing += 1
                            else:
                                meds_missing_dosing.append(item_name)

                            if item.get('contraindications'):
                                meds_with_contraindications += 1
                            else:
                                meds_missing_contraindications.append(item_name)

        # Handle list-based format (legacy)
        elif isinstance(sections, list):
            for section in sections:
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
        sections = self.data.get('sections', {})

        # Handle dict-based format
        if isinstance(sections, dict):
            self.result.stats['sections_count'] = len(sections)
            subsection_count = sum(
                len(subsections) if isinstance(subsections, dict) else 0
                for subsections in sections.values()
            )
        # Handle list-based format
        elif isinstance(sections, list):
            self.result.stats['sections_count'] = len(sections)
            subsection_count = sum(len(section.get('subsections', [])) for section in sections)
        else:
            self.result.stats['sections_count'] = 0
            subsection_count = 0

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
