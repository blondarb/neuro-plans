#!/usr/bin/env python3
"""
Extract all unlinked trial names and guideline references from evidence tables
in neuro-plans markdown files.

Scans Section 8 (Evidence & References) tables for Source column entries that
are NOT wrapped in markdown links [text](url).
"""

import os
import re
import glob
from collections import Counter

PLANS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "plans")

# Guideline patterns: organization abbreviations + "Guidelines" or "Practice Parameter" etc.
GUIDELINE_PATTERN = re.compile(
    r'('
    # Org abbreviation(s) + year + Guidelines/Recommendations/etc.
    r'(?:[A-Z]{2,}(?:/[A-Z]{2,})*\s+\d{4}\s+(?:Guidelines?|Recommendations?|Practice\s+Parameters?|Consensus|Statement|Update))'
    r'|'
    # Org abbreviation(s) + Guidelines/Practice Parameter (without year)
    r'(?:[A-Z]{2,}(?:/[A-Z]{2,})*\s+(?:Guidelines?|Recommendations?|Practice\s+Parameters?|Consensus|Statement))'
    r'|'
    # "XYZ Guidelines YEAR" pattern
    r'(?:[A-Z]{2,}(?:/[A-Z]{2,})*\s+(?:Guidelines?|Recommendations?)\s+\d{4})'
    r'|'
    # Descriptive guidelines: "Cochrane Review(s)", "Brighton Collaboration"
    r'(?:Cochrane\s+Reviews?)'
    r'|'
    r'(?:Brighton\s+Collaboration)'
    r'|'
    # "Expert consensus" (common unlinked pattern)
    r'(?:[Ee]xpert\s+consensus)'
    r')',
    re.IGNORECASE
)

# Markdown link pattern: [text](url)
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\([^)]*\)')

# ============================================================================
# EXCLUSION LISTS
# ============================================================================

# Known journal abbreviations (NOT trial names)
JOURNAL_NAMES = {
    'NEJM', 'BMJ', 'JAMA', 'LANCET',
    'CID',   # Clinical Infectious Diseases
    'AJNR',  # American Journal of Neuroradiology
    'BMC',   # BMC (journal publisher)
    'CMAJ',  # Canadian Medical Association Journal
    'QJM',   # QJM: An International Journal of Medicine
    'NPV',   # Not a trial
}

# Organization abbreviations (used in guideline refs, not trial names themselves)
ORGANIZATION_ABBREVS = {
    'AHA', 'ASA', 'AAN', 'AHS',
    'IDSA', 'CDC', 'WHO', 'NIH', 'FDA',
    'EFNS', 'EANO', 'NCCN', 'RANO',
    'AANEM', 'AASLD', 'EASL', 'ESC',
    'APA', 'ADA', 'ATS', 'ACCP', 'ACR', 'ACOG',
    'AAP', 'AASM', 'ATA', 'RTOG', 'EORTC',
    'ERC', 'ESICM', 'ESPEN', 'ACCF',
    'ILCOR', 'IPMSSG', 'IPCG', 'ICBD', 'IBTPP',
    'NASS', 'NRG', 'USPSTF',
    'ACC',  # American College of Cardiology
}

# Common medical/clinical abbreviations (NOT trial names)
MEDICAL_ABBREVS = {
    'PO', 'IV', 'IM', 'SC', 'SQ', 'SL', 'PR', 'ET', 'OR', 'AND', 'FOR',
    'THE', 'NOT', 'NIF', 'FVC', 'DVT', 'GBS', 'GCS', 'ICU', 'OPD', 'ED',
    'CT', 'LP', 'MRI', 'MRA', 'CTA', 'EEG', 'EMG', 'NCS', 'CSF', 'CBC',
    'BMP', 'CMP', 'LFT', 'TSH', 'HBA', 'INR', 'PTT', 'ESR', 'CRP', 'ANA',
    'SSA', 'SSB', 'BID', 'TID', 'QID', 'PRN', 'QHS', 'ICD', 'CPT',
    'IGA', 'MOH', 'IVIG', 'PLEX', 'HARM',
    'CLASS', 'LEVEL', 'RCT', 'RCTS', 'MD', 'DO', 'PHD',
    'II', 'III', 'IIA', 'IIB', 'NR',
    'MG', 'MS', 'ALS', 'TBI', 'ICP', 'SAH', 'ICH', 'TIA',
    'AF', 'BP', 'HR', 'RR', 'SBP', 'DBP', 'MAP',
    'OP', 'LVO', 'MCA', 'PFO', 'CEA', 'CAS',
    'NULL', 'NONE', 'NA', 'TBD',
    'SE', 'EPC', 'NMS', 'DBS', 'VNS', 'RNS',
    'CIDP', 'ADEM', 'NMOSD', 'MOG', 'CNS', 'PNS',
    'HIV', 'HSV', 'VZV', 'CMV', 'EBV', 'JCV', 'PML',
    'RA', 'SLE', 'GCA', 'PMR',
    'PT', 'OT', 'ST', 'SNF',
    'TO', 'IN', 'OF', 'AT', 'ON', 'IS', 'IT', 'AS', 'BY', 'AN', 'UP',
    'BE', 'DO', 'NO', 'SO', 'IF', 'HE', 'WE', 'AM', 'PM', 'VS',
    'REM', 'NREM',
    'TX', 'RX', 'DX', 'HX', 'FX',
    'QOL', 'ADL', 'ROM', 'BMI',
    'UPDRS', 'MMSE', 'MOCA',
    'ICA', 'ECA', 'CCA',
    'DM', 'DWI', 'PCR', 'PMID',
    'TB', 'TBM', 'SCI', 'CSM', 'DNR', 'NMJ', 'ABG',
    'ABI', 'RPD', 'UTI', 'PRES', 'TCD', 'STEMI',
    'RIPE',  # TB drug regimen, not a trial
    'EITB',  # Enzyme-linked immunoelectrotransfer blot
    'NCC',   # Neurocysticercosis abbreviation
    'REMS',  # Risk Evaluation and Mitigation Strategy
    'MMWR',  # Morbidity and Mortality Weekly Report
    'RCVS',  # Reversible cerebral vasoconstriction syndrome
}

# Combine all exclusions
EXCLUDE_WORDS = JOURNAL_NAMES | ORGANIZATION_ABBREVS | MEDICAL_ABBREVS

# Author initial patterns: exactly 2 uppercase letters (like "JJ", "SJ", "DB")
# These appear as "LastName AB" patterns in citation text
AUTHOR_INITIAL_PATTERN = re.compile(r'^[A-Z]{2}$')

# Known legitimate trial names (to keep even if they overlap with other patterns)
KNOWN_TRIALS = {
    'THALES', 'RE-LY', 'NASCET', 'AVERT', 'DESTINY', 'MR CLEAN',
    'ESCAPE', 'EXTEND-IA', 'SWIFT-PRIME', 'REVASCAT', 'DAWN',
    'DEFUSE-3', 'CHANCE', 'POINT', 'SPARCL', 'CRYSTAL-AF', 'EMBRACE',
    'CLOSE', 'RESPECT', 'REDUCE', 'ARISTOTLE', 'ROCKET-AF', 'ENGAGE AF',
    'SPS3', 'DECIMAL', 'HAMLET', 'ECST', 'INTERACT2', 'ATACH-2',
    'STICH', 'STICH II', 'MISTIE III', 'INCH', 'TICH-2', 'PATCH',
    'ENRICH', 'ANNEXA-4', 'RE-VERSE AD', 'MASH-2', 'HIMALAIA',
    'ISAT', 'IIHTT', 'CADISS', 'ESETT', 'FIRES',
    'FIRST', 'MONEAD', 'ADAGIO', 'TEMPO', 'EXPRESS',
    'ADAPT', 'LATE', 'MGTX', 'REGAIN',
    'DCCT', 'EDIC', 'APOLLO', 'ATTR-ACT', 'NEURO-TTR',
    'ORATORIO', 'EXPAND', 'SOLAR', 'CHOLINE',
    'PREEMPT', 'AVERT',
    'PRODIGE', 'NOA-08', 'AMBITION',
    'PROGRESS', 'ISSUE-3', 'NNIPPS', 'PHOENIX',
    'PRECIS', 'PROPAC', 'TTM',
    'SMART', 'START',
    'STRIVE', 'WTX101-301', 'RCVS2',
    'EXTEND-IA TNK', 'ALS FTD', 'WHO CNS5', 'WHO MDR-TB',
    'TTM EEG', 'CDC STI', 'CDC MMWR',
    'NPDPSC',
    'GBS-CIDP', 'TB-IRIS', 'ICD-10 F07', 'ICHD-3',
    'FDA REMS',
}

# Minimum length for trial name candidates
MIN_TRIAL_LENGTH = 3  # Require at least 3 chars to avoid 2-letter author initials


def remove_links(text):
    """Remove markdown links and return (cleaned_text, set_of_linked_text)."""
    linked_texts = set()
    for m in LINK_PATTERN.finditer(text):
        linked_texts.add(m.group(1).strip())
    cleaned = LINK_PATTERN.sub(' __LINK__ ', text)
    return cleaned, linked_texts


def extract_source_column(line):
    """Extract the Source column (3rd column) from a table row."""
    parts = line.split('|')
    if len(parts) >= 4:
        return parts[3].strip()
    return None


def find_evidence_tables(filepath):
    """Find all evidence table rows in a file and return Source column values."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sources = []
    in_evidence = False
    header_found = False
    separator_found = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect evidence section header
        if re.match(r'^##\s+8\.\s+EVIDENCE', stripped, re.IGNORECASE):
            in_evidence = True
            header_found = False
            separator_found = False
            continue

        # Detect any new section header (exit evidence)
        if in_evidence and re.match(r'^##\s+(?!8\.)', stripped):
            in_evidence = False
            continue

        # Also exit on --- separator after data rows
        if in_evidence and separator_found and stripped == '---':
            in_evidence = False
            continue

        if not in_evidence:
            continue

        # Look for table header row
        if not header_found and 'Recommendation' in stripped and 'Evidence Level' in stripped and 'Source' in stripped:
            header_found = True
            continue

        # Skip separator row
        if header_found and not separator_found and re.match(r'^\|[\s\-:|]+\|', stripped):
            separator_found = True
            continue

        # Data rows
        if header_found and separator_found and stripped.startswith('|') and not stripped.startswith('|---'):
            source = extract_source_column(stripped)
            if source:
                sources.append((source, os.path.basename(filepath)))

    return sources


def is_author_initials(name):
    """Check if a name looks like author initials (2 uppercase letters)."""
    return bool(AUTHOR_INITIAL_PATTERN.match(name))


def is_likely_trial_name(name):
    """Heuristic: does this look like a clinical trial name?"""
    # Known trials always pass
    if name in KNOWN_TRIALS:
        return True

    # Exclude pure author initials (2 letters)
    if is_author_initials(name):
        return False

    # Exclude if in any exclusion list
    if name in EXCLUDE_WORDS:
        return False

    # For single words: require minimum 3 characters
    words = name.split()
    if len(words) == 1 and len(name) < MIN_TRIAL_LENGTH:
        return False

    # For multi-word: check that not ALL words are excluded
    if len(words) > 1:
        non_excluded = [w for w in words if w not in EXCLUDE_WORDS and not is_author_initials(w)]
        if not non_excluded:
            return False

    # Must contain at least 2 uppercase letters total
    upper_count = sum(1 for c in name if c.isupper())
    if upper_count < 2:
        return False

    # Looks like a Cochrane ID (CD followed by digits) -- keep these as they may need linking
    if re.match(r'^CD\d+$', name):
        return True

    # Looks like a clinical trial registry number (NCT followed by digits) -- keep
    if re.match(r'^NCT\d+$', name):
        return True

    # Reject things that look like "PMID: 12345" fragments
    if name.startswith('PMID'):
        return False

    # Reject very short single-word entries that are likely abbreviations
    # but not in our known trial list
    if len(words) == 1 and len(name) <= 3 and name not in KNOWN_TRIALS:
        return False

    return True


def extract_unlinked_references(source_text):
    """Extract trial names and guideline references that are NOT inside markdown links."""
    references = []

    # Remove markdown links to get only unlinked text
    cleaned_text, linked_texts = remove_links(source_text)

    # Extract guideline references from unlinked text
    for m in GUIDELINE_PATTERN.finditer(cleaned_text):
        ref = m.group(0).strip()
        if ref and '__LINK__' not in ref:
            references.append(('guideline', ref))

    # Extract trial names from unlinked text
    # Split by semicolons and commas to process segments
    segments = re.split(r'[;,]', cleaned_text)

    for segment in segments:
        segment = segment.strip()
        if '__LINK__' in segment:
            parts = segment.split('__LINK__')
            for part in parts:
                part = part.strip()
                if part:
                    _extract_trial_names(part, references)
        else:
            _extract_trial_names(segment, references)

    return references


def _extract_trial_names(text, references):
    """Extract trial name candidates from a text segment."""
    # First try multi-word trial names (e.g., "MR CLEAN", "EXTEND-IA TNK")
    multi_word = re.finditer(
        r'\b([A-Z][A-Z0-9]*(?:[-][A-Z0-9]+)*(?:\s+[A-Z][A-Z0-9]*(?:[-][A-Z0-9]+)*)+)\b',
        text
    )
    found_spans = set()
    for m in multi_word:
        name = m.group(1).strip()
        if is_likely_trial_name(name):
            references.append(('trial', name))
            found_spans.add((m.start(), m.end()))

    # Single-word trial names
    single_word = re.finditer(r'\b([A-Z][A-Z0-9]*(?:[-][A-Z0-9]+)*)\b', text)
    for m in single_word:
        name = m.group(1).strip()
        # Skip if this position was already captured as part of a multi-word name
        if any(m.start() >= s and m.end() <= e for s, e in found_spans):
            continue
        if is_likely_trial_name(name):
            references.append(('trial', name))


def clean_reference(ref_type, name):
    """Clean and normalize a reference name."""
    name = name.strip()
    name = re.sub(r'[\s;,\.]+$', '', name)
    name = re.sub(r'^[\s;,\.]+', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name


def main():
    plan_files = sorted(glob.glob(os.path.join(PLANS_DIR, "*.md")))
    plan_files = [f for f in plan_files if not f.endswith('index.md')]

    print(f"Scanning {len(plan_files)} plan files...\n")

    all_references = Counter()
    reference_files = {}

    files_with_evidence = 0
    total_source_cells = 0

    for filepath in plan_files:
        sources = find_evidence_tables(filepath)
        if sources:
            files_with_evidence += 1

        for source_text, filename in sources:
            total_source_cells += 1
            refs = extract_unlinked_references(source_text)

            for ref_type, name in refs:
                cleaned = clean_reference(ref_type, name)
                if cleaned and len(cleaned) >= 2:
                    key = (ref_type, cleaned)
                    all_references[key] += 1
                    if key not in reference_files:
                        reference_files[key] = set()
                    reference_files[key].add(filename)

    sorted_refs = sorted(all_references.items(), key=lambda x: (-x[1], x[0][1]))

    # Print summary
    trial_refs = [(k, v) for k, v in sorted_refs if k[0] == 'trial']
    guideline_refs = [(k, v) for k, v in sorted_refs if k[0] == 'guideline']

    print(f"Files scanned: {len(plan_files)}")
    print(f"Files with evidence tables: {files_with_evidence}")
    print(f"Total source cells processed: {total_source_cells}")
    print(f"Unique unlinked references found: {len(sorted_refs)}")
    print(f"  - Trial names: {len(trial_refs)}")
    print(f"  - Guideline references: {len(guideline_refs)}")
    print()

    print("=" * 90)
    print(f"UNLINKED TRIAL NAMES ({len(trial_refs)} unique)")
    print("=" * 90)
    print(f"{'Count':<8} {'Trial Name':<45} {'Files'}")
    print("-" * 90)
    for (ref_type, name), count in sorted_refs:
        if ref_type == 'trial':
            files = sorted(reference_files[(ref_type, name)])
            files_str = ', '.join(f.replace('.md', '') for f in files[:5])
            if len(files) > 5:
                files_str += f' (+{len(files)-5} more)'
            print(f"{count:<8} {name:<45} {files_str}")

    print()
    print("=" * 90)
    print(f"UNLINKED GUIDELINE REFERENCES ({len(guideline_refs)} unique)")
    print("=" * 90)
    print(f"{'Count':<8} {'Guideline Reference':<55} {'Files'}")
    print("-" * 90)
    for (ref_type, name), count in sorted_refs:
        if ref_type == 'guideline':
            files = sorted(reference_files[(ref_type, name)])
            files_str = ', '.join(f.replace('.md', '') for f in files[:5])
            if len(files) > 5:
                files_str += f' (+{len(files)-5} more)'
            print(f"{count:<8} {name:<55} {files_str}")

    # Combined summary
    print()
    print("=" * 90)
    print("COMBINED LIST (sorted by frequency)")
    print("=" * 90)
    print(f"{'Count':<8} {'Type':<12} {'Reference'}")
    print("-" * 90)
    for (ref_type, name), count in sorted_refs:
        print(f"{count:<8} {ref_type:<12} {name}")

    # Grand total
    total_instances = sum(v for v in all_references.values())
    print(f"\nTOTAL: {total_instances} unlinked reference instances across {len(sorted_refs)} unique names")


if __name__ == '__main__':
    main()
