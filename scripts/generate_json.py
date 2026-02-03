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
        'treatment_3h': r'###?\s*3H[.\s]+',
        'treatment_3i': r'###?\s*3I[.\s]+',
        'referrals': r'###?\s*4A[.\s]+',
        'patient_instructions': r'###?\s*4B[.\s]+',
        'lifestyle': r'###?\s*4C[.\s]+',
        'other_4d': r'###?\s*4D[.\s]+',
        'other_4e': r'###?\s*4E[.\s]+',
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
        # Try frontmatter first - handle quoted titles with apostrophes
        frontmatter_match = re.search(r'^---\s*\n.*?title:\s*"([^"\n]+)"',
                                       self.content, re.DOTALL)
        if frontmatter_match:
            return frontmatter_match.group(1).strip()

        # Try single-quoted frontmatter title
        frontmatter_match = re.search(r"^---\s*\n.*?title:\s*'([^'\n]+)'",
                                       self.content, re.DOTALL)
        if frontmatter_match:
            return frontmatter_match.group(1).strip()

        # Fall back to DIAGNOSIS line (strip bold markdown markers)
        diagnosis_match = re.search(r'DIAGNOSIS:\s*\*?\*?\s*(.+)', self.content)
        if diagnosis_match:
            title = diagnosis_match.group(1).strip()
            # Remove any trailing bold markers
            title = re.sub(r'^\*+\s*', '', title)
            return title

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

    # Default lab subsection title mapping (for generic names)
    LAB_TITLE_MAP = {
        'essential': 'Essential/Core Labs',
        'extended': 'Extended Workup',
    }

    def _parse_lab_sections(self) -> list:
        """Parse laboratory workup sections dynamically."""
        subsections = []

        lab_keys = [
            ('labs_core', 'labs_extended'),
            ('labs_extended', 'labs_rare'),
            ('labs_rare', 'imaging_essential'),
        ]

        for start_key, end_key in lab_keys:
            start_idx = self._find_section_start(start_key)
            if start_idx is None:
                continue

            # Extract actual title from the markdown heading
            title = self._extract_section_title(start_idx)

            # Map generic names to standard lab titles
            title_mapped = self.LAB_TITLE_MAP.get(title.lower(), title)

            items = self._parse_table_section(start_key, end_key)
            if items:
                subsections.append({'title': title_mapped, 'items': items})

        # Lumbar Puncture / CSF Studies (logically part of lab workup)
        lp_items = self._parse_table_section('lumbar_puncture', 'treatment_3a')
        if lp_items:
            subsections.append({'title': 'Lumbar Puncture', 'items': lp_items})

        return subsections

    # Default imaging subsection title mapping (for generic names)
    IMAGING_TITLE_MAP = {
        'essential': 'Essential/First-line',
        'extended': 'Extended',
    }

    def _parse_imaging_sections(self) -> list:
        """Parse imaging sections dynamically."""
        subsections = []

        # Ordered sequence of imaging boundaries; each section uses the next
        # existing boundary as its end-point.
        imaging_boundary_seq = [
            'imaging_essential', 'imaging_extended', 'imaging_rare',
            'lumbar_puncture', 'treatment_3a',
        ]

        imaging_keys = [
            ('imaging_essential', 'imaging_extended'),
            ('imaging_extended', 'imaging_rare'),
            ('imaging_rare', 'lumbar_puncture'),
        ]

        for start_key, end_key in imaging_keys:
            start_idx = self._find_section_start(start_key)
            if start_idx is None:
                continue

            # Extract actual title from the markdown heading
            title = self._extract_section_title(start_idx)

            # Map generic names to standard imaging titles
            title_mapped = self.IMAGING_TITLE_MAP.get(title.lower(), title)

            # Find the effective end boundary: if end_key doesn't exist,
            # walk forward through the boundary sequence to find the next
            # existing section that appears AFTER the start section.
            effective_end = end_key
            end_exists = self._find_section_start(end_key) is not None
            if end_exists and self._find_section_start(end_key) <= start_idx:
                end_exists = False  # End boundary is before start — invalid
            if not end_exists:
                bp = imaging_boundary_seq.index(end_key) if end_key in imaging_boundary_seq else -1
                if bp >= 0:
                    for candidate in imaging_boundary_seq[bp + 1:]:
                        cand_idx = self._find_section_start(candidate)
                        if cand_idx is not None and cand_idx > start_idx:
                            effective_end = candidate
                            end_exists = True
                            break

            # Use multi_table when we have a valid end boundary (prevents
            # bleeding into the next major section)
            items = self._parse_table_section(start_key, effective_end,
                                              multi_table=end_exists)
            if items:
                subsections.append({'title': title_mapped, 'items': items})

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
            ('treatment_3g', 'treatment_3h'),
            ('treatment_3h', 'treatment_3i'),
            ('treatment_3i', 'referrals'),
        ]

        for start_key, end_key in treatment_keys:
            start_idx = self._find_section_start(start_key)
            if start_idx is None:
                continue

            # Extract the title from the actual markdown line
            title = self._extract_section_title(start_idx)

            items = self._parse_table_section(start_key, end_key, multi_table=True)
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

    # Generic Other-Recommendations subsection names → standard titles
    OTHER_REC_TITLE_MAP = {
        'essential': 'Referrals & Consults',
        'extended': 'Patient Instructions',
        'atypical/refractory': 'Lifestyle & Prevention',
    }

    def _parse_other_sections(self) -> list:
        """Parse other recommendations sections dynamically.

        Scans for all 4X subsections (4A through 4E), extracts their titles,
        and uses natural subsection boundaries rather than assuming a fixed
        4A=Referrals, 4B=Patient Instructions, 4C=Lifestyle ordering.
        """
        subsections = []

        # Define the other-recommendations section sequence with boundaries
        other_keys = [
            ('referrals', 'patient_instructions'),      # 4A → 4B
            ('patient_instructions', 'lifestyle'),       # 4B → 4C
            ('lifestyle', 'other_4d'),                   # 4C → 4D
            ('other_4d', 'other_4e'),                    # 4D → 4E
            ('other_4e', 'differential'),                # 4E → Section 5
        ]

        for start_key, end_key in other_keys:
            start_idx = self._find_section_start(start_key)
            if start_idx is None:
                continue

            # Extract the actual title from the markdown heading
            title = self._extract_section_title(start_idx)

            # Map generic names (Essential, Extended, Atypical/Refractory)
            # to standard Other Recommendations titles
            title_mapped = self.OTHER_REC_TITLE_MAP.get(title.lower(), title)

            items = self._parse_table_section(start_key, end_key)
            if items:
                subsections.append({'title': title_mapped, 'items': items})

        return subsections

    # Header words to skip in differential/disposition/evidence tables
    DIFF_HEADER_WORDS = {
        'alternative diagnosis', 'diagnosis', 'condition', 'category', 'type',
        'nystagmus type', 'feature', 'red flag', 'criterion', 'letter',
        'drug', 'medication', 'level of care', 'level', 'setting',
        'step', 'procedure', 'test', 'study', 'treatment', 'parameter',
        'disposition', 'criteria', 'recommendation', 'evidence level',
        'source', 'features', 'tests', 'domain',
        'guideline', 'tool', 'subtype',
        'component', 'class', 'score',
        'antibody', 'pattern', 'tempo',
        'etiology', 'maneuver', 'disorder', 'precipitant', 'item',
        'organism', 'factor', 'grade', 'asm', 'phase',
        'sign', 'syndrome', 'finding',
    }

    # Prefix patterns for header detection (JSON parser)
    DIFF_HEADER_PREFIXES = [
        'alternative diagnosis', 'nystagmus type', 'level of care',
        'evidence level', 'test (', 'study (', 'treatment (', 'medication (',
        'primary tumor', 'major risk factors',
        'ds-gpa score', 'sins total score',
        'general condition (kps)',
        'tokuhashi score',
    ]

    @classmethod
    def _is_header_cell(cls, first_cell: str) -> bool:
        """Check if a table cell looks like a header."""
        lower = first_cell.lower().strip()
        if lower in cls.DIFF_HEADER_WORDS:
            return True
        return any(lower.startswith(prefix) for prefix in cls.DIFF_HEADER_PREFIXES)

    def _parse_differential_section(self) -> list:
        """Parse differential diagnosis section."""
        items = []
        start_idx = self._find_section_start('differential')
        end_idx = self._find_section_start('monitoring')

        if start_idx is None:
            return items

        if end_idx is None:
            end_idx = len(self.lines)

        # Look for table rows (supports multiple sub-tables within the section)
        in_table = False
        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                first_cell = cells[0].strip() if cells else ''
                # Skip header rows
                if self._is_header_cell(first_cell):
                    in_table = True
                    continue
                if len(cells) >= 2 and cells[0]:
                    items.append({
                        'diagnosis': cells[0],
                        'features': cells[1] if len(cells) > 1 else '',
                        'tests': cells[2] if len(cells) > 2 else ''
                    })
                in_table = True
            elif in_table and not line.startswith('|'):
                in_table = False  # Reset for potential next sub-table

        return items

    def _parse_monitoring_section(self) -> list:
        """Parse monitoring parameters section."""
        return self._parse_table_section('monitoring', 'disposition', multi_table=True)

    def _parse_disposition_section(self) -> list:
        """Parse disposition criteria section."""
        items = []
        start_idx = self._find_section_start('disposition')
        end_idx = self._find_section_start('evidence')

        if start_idx is None:
            return items

        if end_idx is None:
            end_idx = len(self.lines)

        # Look for table rows (supports multiple sub-tables within the section)
        in_table = False
        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                first_cell = cells[0].strip() if cells else ''
                # Skip header rows
                if self._is_header_cell(first_cell):
                    in_table = True
                    continue
                if len(cells) >= 2 and cells[0]:
                    items.append({
                        'disposition': cells[0],
                        'criteria': cells[1] if len(cells) > 1 else ''
                    })
                in_table = True
            elif in_table and not line.startswith('|'):
                in_table = False  # Reset for potential next sub-table

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

        # Parse table rows (supports multiple sub-tables within evidence section)
        in_table = False
        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                first_cell = cells[0].strip() if cells else ''
                # Skip header rows using shared header-word detection
                if self._is_header_cell(first_cell):
                    in_table = True
                    continue
                if len(cells) >= 2 and cells[0]:
                    items.append({
                        'recommendation': cells[0],
                        'evidenceLevel': cells[1] if len(cells) > 1 else '',
                        'source': cells[2] if len(cells) > 2 else ''
                    })
                in_table = True
            elif in_table and not line.startswith('|'):
                in_table = False  # Reset for potential next sub-table

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

    def _parse_table_section(self, start_key: str, end_key: str = None, multi_table: bool = False) -> list:
        """Parse a table section between two section markers.

        Args:
            start_key: Section pattern key for the start boundary
            end_key: Section pattern key for the end boundary
            multi_table: If True, continue past non-table lines to find additional
                         sub-tables within the section. If False (default), stop at
                         the first non-table line after a table is found.
        """
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

        # Patterns for reference/interpretation/timeline tables to skip in multi_table mode
        SKIP_TABLE_RE = re.compile(
            r'\*\*.*(?:Reference|Interpretation Guide|Interpretation Key).*:\*\*'
            r'|####?\s*Timeline-Based Protocol',
            re.IGNORECASE
        )

        # Parse table
        header_cols = []
        in_table = False
        skip_table = False
        in_skipped_table = False  # Track if we're inside a skipped table

        for i in range(start_idx, end_idx):
            line = self.lines[i].strip()

            if not line.startswith('|'):
                if in_table:
                    if multi_table:
                        in_table = False
                        skip_table = False
                        header_cols = []  # Reset for potential next sub-table
                    else:
                        break  # Single-table mode: stop at end of first table
                elif in_skipped_table:
                    # We've passed the skipped table — reset flags
                    in_skipped_table = False
                    skip_table = False
                # Check if next table should be skipped (reference/interpretation)
                if multi_table and SKIP_TABLE_RE.match(line):
                    skip_table = True
                continue

            # Skip tables flagged as reference/interpretation
            if skip_table:
                in_skipped_table = True
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

        # Fallback: if no fields matched standard mappings, use first cell as 'item'
        # and remaining cells with their header names as-is
        if not item and cells[0]:
            item['item'] = cells[0]
            for i, header in enumerate(headers[1:], 1):
                if i < len(cells) and cells[i].strip():
                    item[header] = cells[i].strip()

        # Parse structured dosing if present
        if 'dosing' in item and item.get('item'):
            dosing_data = self._parse_structured_dosing(
                item['dosing'],
                item['item'],
                item.get('route')
            )
            if dosing_data:
                # Replace simple dosing string with structured object
                item['dosing'] = dosing_data

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
            'subtype': 'item',
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
            'route': 'route',
            'frequency': 'frequency',
            'action if abnormal': 'action',
            'threshold': 'threshold',
            'priority': 'priority',
            'pre-treatment requirements': 'pretreatment',
            'pre-treatment': 'pretreatment',
        }

        # Try exact match first
        result = mappings.get(header)
        if result:
            return result

        # Try matching base word before parenthetical, e.g. "test (cpt)" -> "test"
        base = re.split(r'\s*[\(]', header)[0].strip()
        if base != header:
            return mappings.get(base)

        return None

    def _parse_structured_dosing(self, dosing_text: str, item_name: str, route: str = None) -> dict:
        """Parse structured dosing format into separate fields.

        Single dose format: "dose freq :: route :: :: full_instructions"
        Multi-dose format: "dose1 freq1; dose2 freq2 :: route :: :: full_instructions"

        Returns dict with:
        - doseOptions: array of {dose, frequency, orderSentence} for each option
        - route: "PO"
        - instructions: "Start 5 mg TID; titrate by 5 mg/dose q3d; max 80 mg/day"
        - orderSentence: first/default order sentence for backwards compatibility
        """
        if not dosing_text:
            return None

        # Check if it's the new structured format (contains :: delimiters)
        # Using :: instead of | because | conflicts with markdown table syntax
        parts = [p.strip() for p in dosing_text.split('::')]

        if len(parts) >= 3:
            # New structured format
            dose_field = parts[0]
            med_route = parts[1]
            # parts[2] is empty/reserved
            instructions = parts[3] if len(parts) > 3 else dosing_text

            # Parse dose options (may be single or multiple separated by semicolons)
            dose_options = []
            dose_items = [d.strip() for d in dose_field.split(';')]

            for dose_item in dose_items:
                if not dose_item:
                    continue
                # Generate order sentence for this option
                order_sentence = f"{item_name} {dose_item} {med_route}".strip()
                # Clean up any double spaces
                order_sentence = ' '.join(order_sentence.split())
                dose_options.append({
                    'text': dose_item,
                    'orderSentence': order_sentence
                })

            if dose_options:
                return {
                    'doseOptions': dose_options,
                    'route': med_route,
                    'instructions': instructions,
                    'orderSentence': dose_options[0]['orderSentence']  # Default to first option
                }

        # Legacy format (unstructured text) - keep as-is for backwards compatibility
        # Try to generate a basic order sentence if route is available
        order_sentence = None
        if route:
            order_sentence = f"{item_name} - {route} - see dosing"

        return {
            'instructions': dosing_text,
            'orderSentence': order_sentence
        }


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
        current_main_section = None  # Track parent section (e.g., 'Other Recommendations')
        in_table = False
        seen_table = False  # Whether we've seen at least one table in current subsection
        item_count = 0
        in_valid_section = False  # Track if we're in a countable section
        skip_next_table = False   # For skipping timeline tables

        # Generic "Other Recommendations" subsection names that need context-aware mapping
        # When 4A/4B/4C use these generic names, they map to standard Other Rec subsections
        OTHER_REC_GENERIC_NAMES = {
            'essential': 'referrals',
            'extended': 'patient instructions',
            'atypical/refractory': 'lifestyle',
        }

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
            (r'###\s*3H[.\s]+(.+)', None),
            (r'###\s*3I[.\s]+(.+)', None),
            (r'###\s*4A[.\s]+(.+)', None),
            (r'###\s*4B[.\s]+(.+)', None),
            (r'###\s*4C[.\s]+(.+)', None),
            (r'###\s*4D[.\s]+(.+)', None),
            (r'###\s*4E[.\s]+(.+)', None),
        ]

        # Patterns that indicate we should STOP counting (end of main content)
        stop_patterns = [
            r'##?\s*APPENDIX',
            r'^\*\*APPENDIX',              # Bold-text appendix (used in 11+ plans)
            r'##?\s*NOTES\s*$',
            r'##?\s*CHANGE\s*LOG',
            r'##?\s*CPT\s+CODE',           # CPT CODE QUICK REFERENCE sections
            r'^═{3,}',                     # Section dividers
            r'^---\s*$',                   # Bare horizontal rules
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

                    # Track main section for context-aware subsection naming
                    if section_name in ('Laboratory Workup', 'Diagnostic Imaging',
                                        'Treatment', 'Other Recommendations',
                                        'Differential Diagnosis', 'Monitoring Parameters',
                                        'Disposition Criteria', 'Evidence & References'):
                        current_main_section = section_name

                    # If section_name is None, extract from captured group or full match
                    if section_name is None:
                        if match.groups():
                            # Use the captured group (title after the section number)
                            extracted = match.group(1).strip()
                        else:
                            # Fall back to the full match
                            extracted = match.group(0).strip()

                        # Context-aware naming: generic names under Other Recommendations
                        # get mapped to standard subsection names (referrals, patient
                        # instructions, lifestyle) since the JSON parser uses those
                        if (current_main_section == 'Other Recommendations' and
                                extracted.lower() in OTHER_REC_GENERIC_NAMES):
                            current_subsection = OTHER_REC_GENERIC_NAMES[extracted.lower()]
                        else:
                            current_subsection = extracted
                    else:
                        current_subsection = section_name

                    item_count = 0
                    in_table = False
                    seen_table = False  # Reset sub-table tracking for new section
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

            # Skip reference/interpretation tables (not actionable items)
            if re.match(r'\*\*.*(?:Reference|Interpretation Guide|Interpretation Key).*:\*\*', line, re.IGNORECASE):
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
                    # Skip header row of sub-tables (not the first table in section)
                    # When in_table was reset to False (saw non-table content), the next
                    # table's first non-separator row is its header
                    if not in_table and seen_table:
                        # This is the header row of a subsequent sub-table; skip it
                        in_table = True
                    else:
                        # Check if it's a header via word matching
                        first_cell = cells[0].lower() if cells else ''
                        # Exact-match header words
                        exact_headers = {'test', 'study', 'treatment', 'medication', 'drug',
                                        'recommendation', 'parameter', 'disposition', 'diagnosis',
                                        'timing', 'intervention', 'guideline', 'type', 'feature',
                                        'criterion', 'level', 'letter', 'step', 'procedure',
                                        'condition', 'category', 'setting', 'domain', 'criteria',
                                        'source', 'tool', 'subtype', 'component', 'class',
                                        'score', 'red flag', 'red flags', 'antibody', 'pattern',
                                        'tempo', 'etiology', 'maneuver', 'disorder',
                                        'precipitant', 'item', 'organism', 'factor', 'grade',
                                        'asm', 'phase', 'sign', 'syndrome', 'finding',
                                        'scenario', 'medication class', 'medication/class',
                                        'intervention', 'location', 'population',
                                        'symptom', 'situation'}
                        # Prefix-match header words
                        prefix_headers = ['alternative diagnosis', 'nystagmus type',
                                         'level of care', 'evidence level', 'test (', 'study (',
                                         'treatment (', 'medication (',
                                         'medications to avoid/',
                                         'high-risk features', 'high risk features',
                                         'primary tumor', 'major risk factors',
                                         'ds-gpa score', 'sins total score',
                                         'general condition (kps)',
                                         'tokuhashi score']
                        is_header = (first_cell in exact_headers or
                                    any(first_cell.startswith(ph) for ph in prefix_headers))
                        if first_cell and not is_header and not first_cell.startswith('---'):
                            # Additional check: skip timeline entries
                            if not re.match(r'\*?\*?day\s+\d', first_cell, re.IGNORECASE):
                                item_count += 1
                        in_table = True
                        seen_table = True
            elif in_table and not line.strip().startswith('|') and line.strip():
                # End of table - reset for potential next sub-table
                in_table = False
                skip_next_table = False

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

        # Try to find the plan by id first (matches the id-keyed structure)
        plan_data = None
        md_id = self.markdown_path.stem
        if md_id in plans_data:
            plan_data = plans_data[md_id]

        # Fallback: search by id field within plan entries (for title-keyed data)
        if not plan_data:
            for key, value in plans_data.items():
                if isinstance(value, dict) and value.get('id') == md_id:
                    plan_data = value
                    break

        # Fallback: try matching by title from the markdown file
        if not plan_data:
            md_title = None
            md_content = self.markdown_path.read_text(encoding='utf-8')

            # Try frontmatter title first - handle quoted titles with apostrophes
            import re
            frontmatter_match = re.search(r'^---\s*\n.*?title:\s*"([^"\n]+)"',
                                           md_content, re.DOTALL)
            if frontmatter_match:
                md_title = frontmatter_match.group(1).strip()

            # Try single-quoted frontmatter title
            if not md_title:
                frontmatter_match = re.search(r"^---\s*\n.*?title:\s*'([^'\n]+)'",
                                               md_content, re.DOTALL)
                if frontmatter_match:
                    md_title = frontmatter_match.group(1).strip()

            # Fall back to DIAGNOSIS line (strip bold markdown markers)
            if not md_title:
                diagnosis_match = re.search(r'DIAGNOSIS:\s*\*?\*?\s*(.+)', md_content)
                if diagnosis_match:
                    md_title = diagnosis_match.group(1).strip()
                    # Remove any trailing bold markers
                    md_title = re.sub(r'^\*+\s*', '', md_title)

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
        """Normalize section names for comparison.

        Uses a two-phase approach:
        1. Exact match against known normalizations dict
        2. Pattern-based fallback for varied parenthetical qualifiers
        """
        # Common variations to standardize (exact match)
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
            'essential/core labs (reversible causes screen)': 'core labs',
            'core labs': 'core labs',
            'extended workup': 'extended workup',
            'extended workup (second-line)': 'extended workup',
            'autoimmune & exclusion panel': 'extended workup',
            'rare/specialized': 'rare/specialized',
            'rare/specialized (refractory or atypical)': 'rare/specialized',
            'rare/specialized (if red flags or refractory)': 'rare/specialized',
            'rare/advanced': 'rare/specialized',
            'essential imaging': 'essential imaging',
            'essential/first-line': 'essential imaging',
            'extended imaging': 'extended imaging',
            'extended': 'extended imaging',
            'rare/specialized imaging': 'rare/specialized imaging',
            'rare/specialized labs': 'rare/specialized',
            'specialized': 'rare/specialized',
            'specialized testing (selected patients)': 'rare/specialized',
            'neuropsychological testing': 'rare/specialized',
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
            'patient/family instructions': 'patient instructions',
            'patient / family instructions': 'patient instructions',
            'education': 'patient instructions',
            'lifestyle & prevention': 'lifestyle',
            'lifestyle': 'lifestyle',
            'prevention': 'lifestyle',
            "hashimoto's encephalopathy subtypes & clinical patterns": 'lifestyle',

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

            # Plan-specific exact mappings (unmappable by pattern)
            'foot care & ulcer prevention (critical)': 'patient instructions',
            'medication review (discontinue iih-associated drugs)': 'patient instructions',
            'legal, ethical & documentation': 'lifestyle',
            'infection control, safety & lifestyle': 'lifestyle',
            'close contacts prophylaxis (public health)': 'patient instructions',
            'csf analysis (diagnostic lp)': 'lumbar puncture',
            'ophthalmologic studies': 'rare/specialized',
            'iih mri findings (supportive but not diagnostic)': 'extended imaging',
            'mri findings in wernicke encephalopathy': 'extended imaging',
            'risk stratification (san francisco syncope rule, egsys, oesil, canadian syncope risk score)': 'patient instructions',
            'at-risk populations (prophylactic thiamine)': 'patient instructions',
            'duration of treatment and discontinuation': 'patient instructions',
            'non-pharmacologic considerations': 'lifestyle',
            'pre-procedure considerations': 'patient instructions',
            'prevention strategies': 'lifestyle',
            'driving & activity restrictions': 'lifestyle',
            'comorbidity management': 'lifestyle',
            'pregnancy considerations': 'pregnancy considerations',
            'vaccinations': 'vaccinations',
            'tumor screening protocols by antibody': 'rare/specialized',
            'medications to avoid or use with caution in lems': 'lifestyle',
            'medications to avoid in myasthenia gravis': 'lifestyle',

        }
        lower = name.lower().strip()

        # Phase 1: exact match
        if lower in normalizations:
            return normalizations[lower]

        # Phase 2: pattern-based fallback
        # Core labs variants (with parenthetical qualifiers)
        if (lower.startswith('core labs (') or
                lower.startswith('essential/core labs') or
                lower.startswith('baseline labs')):
            return 'core labs'

        # Extended workup variants
        if (lower.startswith('extended workup (') or
                lower.startswith('extended labs') or
                lower.endswith(' panel') or
                lower.endswith(' workup') or
                lower.startswith('autoimmune') and 'panel' in lower):
            return 'extended workup'

        # Rare/specialized variants
        if (lower.startswith('rare/specialized (') or
                lower.startswith('rare/specialized labs') or
                lower.startswith('rare/advanced') or
                lower.startswith('specialized studies') or
                lower.startswith('specialized testing') or
                lower.startswith('specialized protocols') or
                lower.startswith('specialized labs')):
            return 'rare/specialized'

        # Essential imaging variants
        if (lower.startswith('essential/first-line') or
                lower.startswith('essential imaging') or
                lower.startswith('neuroimaging')):
            return 'essential imaging'

        # Extended imaging variants
        if (lower.startswith('extended (') or
                lower.startswith('ancillary tests')):
            return 'extended imaging'

        # Patient instructions variants
        if (('patient' in lower and 'instruction' in lower) or
                lower.startswith('patient and family') or
                lower.startswith('patient/family') or
                lower.startswith('patient / family')):
            return 'patient instructions'

        # Lifestyle variants
        if (lower.startswith('lifestyle') or
                lower.startswith('medications that may worsen') or
                lower.startswith('medications to avoid')):
            return 'lifestyle'

        # Monitoring variants
        if lower.startswith('monitoring '):
            return 'monitoring'

        # Electrodiagnostic studies -> rare/specialized
        if lower.startswith('electrodiagnostic'):
            return 'rare/specialized'

        # Autonomic testing -> rare/specialized
        if lower.startswith('autonomic testing') or lower.startswith('autonomic function'):
            return 'rare/specialized'

        # Additional studies -> rare/specialized
        if lower == 'additional studies':
            return 'rare/specialized'

        # Cardiac studies -> rare/specialized
        if lower.startswith('cardiac stud') or lower.startswith('extended cardiac'):
            return 'rare/specialized'

        # Small fiber neuropathy assessment -> rare/specialized
        if lower.startswith('small fiber'):
            return 'rare/specialized'

        # Cancer screening -> rare/specialized
        if lower.startswith('cancer screening'):
            return 'rare/specialized'

        # Tumor screening -> rare/specialized
        if lower.startswith('tumor screening'):
            return 'rare/specialized'

        # Bedside clinical tests -> rare/specialized
        if lower.startswith('bedside clinical'):
            return 'rare/specialized'

        # No match - return as-is
        return lower

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
        meds_with_structured_dosing = 0
        meds_with_order_sentence = 0
        meds_with_contraindications = 0
        meds_with_route = 0
        meds_missing_dosing = []
        meds_missing_contraindications = []
        meds_missing_route = []

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

                            # Check for dosing
                            dosing = item.get('dosing')
                            if dosing:
                                meds_with_dosing += 1
                                # Check if structured dosing format
                                if isinstance(dosing, dict):
                                    meds_with_structured_dosing += 1
                                    if dosing.get('orderSentence'):
                                        meds_with_order_sentence += 1
                            else:
                                meds_missing_dosing.append(item_name)

                            # Check for route
                            if item.get('route'):
                                meds_with_route += 1
                            else:
                                meds_missing_route.append(item_name)

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
        self.result.stats['medications_with_structured_dosing'] = meds_with_structured_dosing
        self.result.stats['medications_with_order_sentence'] = meds_with_order_sentence
        self.result.stats['medications_with_route'] = meds_with_route
        self.result.stats['medications_with_contraindications'] = meds_with_contraindications

        if meds_missing_dosing:
            self.result.warnings.append(
                f"Medications missing dosing ({len(meds_missing_dosing)}): {', '.join(meds_missing_dosing[:5])}"
                + ('...' if len(meds_missing_dosing) > 5 else '')
            )

        if meds_missing_route:
            self.result.warnings.append(
                f"Medications missing route ({len(meds_missing_route)}): {', '.join(meds_missing_route[:5])}"
                + ('...' if len(meds_missing_route) > 5 else '')
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
        print(f"  With route: {stats.get('medications_with_route', 0)}/{stats.get('medications_total', 0)}")
        print(f"  With dosing: {stats.get('medications_with_dosing', 0)}/{stats.get('medications_total', 0)}")
        print(f"  With structured dosing: {stats.get('medications_with_structured_dosing', 0)}/{stats.get('medications_total', 0)}")
        print(f"  With order sentence: {stats.get('medications_with_order_sentence', 0)}/{stats.get('medications_total', 0)}")
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
    plan_key = new_plan.get('id', new_plan.get('title', 'Unknown'))
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
        all_md_files = list(plans_dir.glob('*.md'))
        # Filter out non-plan files
        markdown_files = []
        skipped_files = []
        for f in all_md_files:
            # Skip index.md
            if f.name == 'index.md':
                skipped_files.append(f.name)
                continue
            # Skip report files (e.g., *-report-*.md)
            if re.search(r'-report-', f.name):
                skipped_files.append(f.name)
                continue
            # Skip files without plan-like frontmatter (must have version: field)
            try:
                content = f.read_text(encoding='utf-8')
                if not re.search(r'^---\s*\n.*?version:\s*', content, re.DOTALL):
                    skipped_files.append(f.name)
                    continue
            except Exception:
                skipped_files.append(f.name)
                continue
            markdown_files.append(f)
        if skipped_files:
            print(f"Skipped {len(skipped_files)} non-plan file(s): {', '.join(sorted(skipped_files))}")
        if not markdown_files:
            print(f"No plan files found in {plans_dir}")
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
