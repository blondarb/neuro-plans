#!/usr/bin/env python3
"""Convert unstructured dosing entries to structured :: format.

Scans plan markdown files for treatment table rows where the Dosing column
does not use the structured `[dose] :: [route] :: [frequency] :: [instructions]`
format, and converts them.

Skips:
- Rows where ALL columns are `-` (avoid/contraindicated items)
- Non-treatment tables (tables without `| Treatment |` and `| Dosing |` headers)
- Rows where the Dosing column is just `-` (dosing not applicable)
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Frequency extraction patterns (reused from fix_dosing_frequency.py)
# ---------------------------------------------------------------------------
FREQ_PATTERNS = [
    # q-interval with PRN
    (r'\bq(\d+)[-–](\d+)h\s+PRN\b', lambda m: f"q{m.group(1)}-{m.group(2)}h PRN"),
    (r'\bq(\d+)h\s+PRN\b', lambda m: f"q{m.group(1)}h PRN"),
    # q-interval frequencies
    (r'\bq(\d+)[-–](\d+)h\b', lambda m: f"q{m.group(1)}-{m.group(2)}h"),
    (r'\bq(\d+)h\b', lambda m: f"q{m.group(1)}h"),
    (r'\bq(\d+)[-–](\d+)min\b', lambda m: f"q{m.group(1)}-{m.group(2)}min"),
    (r'\bq(\d+)min\b', lambda m: f"q{m.group(1)}min"),
    (r'\bq(\d+)wk\b', lambda m: f"q{m.group(1)}wk"),
    (r'\bq(\d+)d\b', lambda m: f"q{m.group(1)}d"),
    # every N units
    (r'\bevery (\d+) weeks?\b', lambda m: f"q{m.group(1)}wk"),
    (r'\bevery (\d+) months?\b', lambda m: f"q{m.group(1)}mo"),
    (r'\bevery (\d+) hours?\b', lambda m: f"q{m.group(1)}h"),
    (r'\bevery (\d+) days?\b', lambda m: f"q{m.group(1)}d"),
    # Named frequencies
    (r'\bTID[-–]QID\b', lambda m: "TID-QID"),
    (r'\bQID\b', lambda m: "QID"),
    (r'\bTID\b', lambda m: "TID"),
    (r'\bBID\b', lambda m: "BID"),
    (r'\bQHS\b', lambda m: "QHS"),
    (r'\bqHS\b', lambda m: "QHS"),
    (r'\b5[×x]\s*daily\b', lambda m: "5x daily"),
    (r'\b4[×x]\s*daily\b', lambda m: "QID"),
    (r'\b3[×x]\s*daily\b', lambda m: "TID"),
    (r'\b2[×x]\s*daily\b', lambda m: "BID"),
    # Daily variants
    (r'\bonce daily\b', lambda m: "daily"),
    (r'\b\d+ times?\s*/?\s*day\b', lambda m: "daily"),
    (r'\bdaily\b', lambda m: "daily"),
    # Continuous
    (r'\bcontinuous infusion\b', lambda m: "continuous"),
    (r'\bcontinuously\b', lambda m: "continuous"),
    (r'\bcontinuous\b', lambda m: "continuous"),
    # Single dose/administration
    (r'\bsingle dose\b', lambda m: "once"),
    (r'\bone dose\b', lambda m: "once"),
    (r'\bIV push\b', lambda m: "once"),
    (r'\bonce\b', lambda m: "once"),
    # PRN
    (r'\bas needed\b', lambda m: "PRN"),
    (r'\bPRN\b', lambda m: "PRN"),
    # Other intervals
    (r'\bweekly\b', lambda m: "weekly"),
    (r'\bmonthly\b', lambda m: "monthly"),
    # Divided doses
    (r'\bdivided\s+(?:TID|QID|BID)\b', lambda m: m.group().split()[-1]),
]

# ---------------------------------------------------------------------------
# Dose extraction pattern
# ---------------------------------------------------------------------------
DOSE_UNIT_RE = re.compile(
    r'^(\*?\*?)'                              # optional bold markers
    r'([\d.,]+\s*[-–/]\s*[\d.,]+|[\d.,]+)'   # numeric part (range or single)
    r'\s*'
    r'(million\s+units?|'
    r'mg/kg/day|mg/kg/min|mg/kg/hr|mg/kg/h|mg/kg|'
    r'mcg/kg/min|mcg/kg/hr|mcg/kg|µg/kg/min|µg/kg|'
    r'mL/kg/hr|mL/kg/h|mL/kg|'
    r'g/kg/day|g/kg|'
    r'mEq/L|mEq|'
    r'PE/kg|mg/m2|'
    r'units?/kg/hr|units?/kg|units?|IU|'
    r'mg/(?:hr|h|hour|min|day)|'
    r'mcg/(?:hr|h|hour|min)|'
    r'µg/(?:hr|h|hour|min)|'
    r'mL/(?:hr|h|hour|min)|'
    r'drops?|'
    r'mg|g|mcg|µg|mL|L|mmol|'
    r'%'
    r')',
    re.IGNORECASE
)

# "1 strip/spray/puff/tab" pattern
DOSE_UNIT_ALT_RE = re.compile(
    r'^(\d+)\s+(strips?|sprays?|puffs?|tabs?|caps?|tablets?|capsules?|patches?|vials?)',
    re.IGNORECASE
)


# ---------------------------------------------------------------------------
# Treatment-name keyword categories for frequency inference
# ---------------------------------------------------------------------------
SURGICAL_KW = [
    'surgical', 'surgery', 'craniectomy', 'craniotomy', 'decompression',
    'laminectomy', 'laminoplasty', 'discectomy', 'microdiscectomy',
    'implant', 'graft', 'anastomosis', 'tarsorrhaphy',
    'sling', 'nerve section', 'labyrinthectomy', 'fasciotomy', 'fixation',
    'ablation', 'shunt', 'biopsy', 'resection', 'embolization', 'clipping',
    'fenestration', 'fundoplication', 'fusion', 'instrumentation',
    'intratympanic', 'endolymphatic', 'catheter ablation',
    'valve replacement', 'revascularization', 'drainage', 'aspiration',
    'picc line', 'icp monitor', 'evd placement', 'evd ',
    'evacuation', 'hematoma evacuation', 'thrombectomy', 'endovascular',
    'corpectomy', 'foraminotomy', 'rhizotomy', 'cordotomy',
    'injection', 'nerve block', 'gon block', 'spg block', 'lumbar puncture',
    'plasmapheresis', 'plasma exchange', 'plex',
    'intubation', 'mechanical ventilation', 'tracheostomy',
    'external ventricular', 'ventriculostomy',
    'skin biopsy', 'muscle biopsy', 'nerve biopsy',
]

DEVICE_KW = [
    'pacemaker', 'icd ', 'implantable cardioverter', 'defibrillator',
    'telemetry', 'compression stocking', 'compression garment', 'brace',
    'bracing', 'orthosis', 'collar', 'eye patch', 'moisture chamber',
    'glasses', 'sunglasses', 'tape eyelid', 'abdominal binder',
    'head of bed', 'hob ', 'elevate head', 'trendelenburg',
    'elevate hob', 'scd', 'sequential compression',
    'pneumatic compression', 'compression device', 'scds',
    'stimulation', 'stimulator', 'nerve stimulat',
    'vagus nerve', 'deep brain', 'spinal cord stimulat',
    'hearing aid', 'cochlear',
    'wrist splint', 'splint', 'cast',
    'cervical collar', 'halo vest',
    'bipap', 'cpap', 'non-invasive ventilat',
]

MANEUVER_KW = [
    'maneuver', 'repositioning', 'roll', 'brandt-daroff', 'epley',
    'semont', 'bbq roll', 'dix-hallpike', 'counter-pressure',
    'valsalva', 'jaw thrust', 'chin lift', 'heimlich',
    'log roll',
]

EDUCATION_KW = [
    'education', 'reassurance', 'post-treatment instructions',
    'counseling', 'goals of care', 'advance directive',
    'substance abuse counseling', 'psychological support',
    'social work', 'palliative', 'hospice',
    'family meeting', 'code status', 'informed consent',
]

LIFESTYLE_KW = [
    'diet', 'lifestyle', 'modification', 'trigger avoidance', 'sleep hygiene',
    'dietary', 'salt intake', 'fluid intake', 'sodium',
    'migraine lifestyle', 'avoid tight collar',
    'weight loss', 'weight management', 'caloric',
    'smoking cessation', 'alcohol cessation',
    'hydration', 'increased fluid',
]

EXERCISE_KW = [
    'exercise', 'rehabilitation', 'vestibular rehab', 'physiotherapy',
    'physical therapy', 'facial exercise', 'massage', 'retraining',
    'tilt training', 'neuromuscular retraining', 'gait training',
    'early vestibular', 'early mobilization', 'occupational therapy',
    'speech therapy', 'swallow', 'cognitive rehabilitation',
    'range of motion', 'stretching', 'aquatic therapy',
]

MONITORING_KW = [
    'telemetry monitoring', 'icp monitor', 'blood pressure management',
    'cpp management', 'glucose control', 'temperature management',
    'bp management', 'hemodynamic',
]

PROTOCOL_KW = [
    'protocol', 'treat underlying', 'correct reversible', 'treat precipitant',
    'secondary prevention', 'anticoagulation', 'duration of antibiotic',
    'medical management', 'outpatient parenteral', 'opat',
    'nutritional optimization', 'diabetes optimization',
    'identify', 'discontinue offending', 'volume repletion',
    'stroke protocol', 'sepsis', 'resuscitation',
    'disease-modifying', 'anti-tb', 'ripe ', 'empiric',
    'bowel management', 'bladder management', 'urinary',
    'nutrition consult', 'refeeding', 'gradual refeed',
    'non-operative', 'conservative management',
    'fluid restriction', 'restrict',
    'treat structural', 'treat arrhythmia',
    'no prophylactic', 'hyperventilat', 'hypothermia',
    'targeted antibiotic', 'oral antibiotic transition',
    'combination ', 'concomitant ',
]

PROTECT_KW = [
    'protect patient', 'administer home', 'rule out',
    'iv access', 'iv fluid', 'iv normal saline',
    'normal saline', 'crystalloid', 'fluid bolus',
]

AVOID_KW = [
    'avoid vestibular', 'avoid ',
]

DRUG_NAME_KW = [
    'artificial tear', 'lubricating', 'lacri-lube', 'ointment',
    'multivitamin', 'thiamine before', 'vitamin',
    'botulinum', 'onabotulinumtoxin', 'botox',
    'scig ', 'ivig',
    'electroconvulsive therapy',
]


def extract_starting_dose(text):
    """Extract the starting dose from dosing text."""
    clean = text.lstrip('*').strip()

    # Skip if text starts with non-dose words (instructions, not doses)
    skip_starters = [
        'for ', 'if ', 'apply ', 'start ', 'target ', 'per ', 'see ',
        'use ', 'avoid ', 'do not', 'standard ', 'alternative ',
        'patient ', 'refer ', 'surgical ', 'minimally ',
        'establish', 'legs ', 'treat ', 'review ', 'identify',
        'benign ', 'progressive ', 'waist', 'aortic',
        'sick ', 'ventricular ', 'arrhythmia', 'refeeding',
        'foley', 'calorie', 'endocrinology', 'always ',
        'only ', 'not ', 'candidates', 'requirements',
        'bowel ', 'rsi:', 'isotonic',
    ]
    clean_lower = clean.lower()
    if any(clean_lower.startswith(s) for s in skip_starters):
        return None

    # Try "N million units" pattern first (e.g., "18-24 million units/day")
    m = re.match(
        r'^([\d.,]+\s*[-–]\s*[\d.,]+|[\d.,]+)\s+(million\s+units?)',
        clean, re.IGNORECASE
    )
    if m:
        return (m.group(1) + ' ' + m.group(2)).strip()

    # Try "N MU" abbreviation (e.g., "3-4 MU q4h")
    m = re.match(r'^([\d.,]+\s*[-–]\s*[\d.,]+|[\d.,]+)\s+MU\b', clean)
    if m:
        return m.group(1) + ' million units'

    # Try standard numeric+unit pattern
    m = DOSE_UNIT_RE.match(clean)
    if m:
        dose = (m.group(2) + ' ' + m.group(3)).strip()
        # Reject gauge numbers (e.g., "18G" = catheter gauge)
        if re.match(r'^\d+\s*G$', dose):
            return None
        # Reject percentages that aren't concentrations (e.g., "30%" from "20-30% of cases")
        if dose.endswith('%') and not re.search(r'solution|concentration|saline|dextrose', clean, re.IGNORECASE):
            return None
        return dose

    # Try "N strips/sprays" pattern
    m = DOSE_UNIT_ALT_RE.match(clean)
    if m:
        return (m.group(1) + ' ' + m.group(2)).strip()

    return None


def extract_frequency(text):
    """Extract frequency from text using common patterns."""
    for pattern, formatter in FREQ_PATTERNS:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            return formatter(m)
    return None


def categorize_treatment(treatment_name):
    """Categorize a treatment entry based on its name."""
    name = treatment_name.lower().replace('*', '').strip()

    # Order matters: check more specific categories first
    if any(kw in name for kw in DRUG_NAME_KW):
        return 'drug'
    if any(kw in name for kw in SURGICAL_KW):
        return 'surgical'
    if any(kw in name for kw in MANEUVER_KW):
        return 'maneuver'
    if any(kw in name for kw in EDUCATION_KW):
        return 'education'
    if any(kw in name for kw in EXERCISE_KW):
        return 'exercise'
    if any(kw in name for kw in DEVICE_KW):
        return 'device'
    if any(kw in name for kw in LIFESTYLE_KW):
        return 'lifestyle'
    if any(kw in name for kw in MONITORING_KW):
        return 'monitoring'
    if any(kw in name for kw in PROTOCOL_KW):
        return 'protocol'
    if any(kw in name for kw in PROTECT_KW):
        return 'protocol'
    if any(kw in name for kw in AVOID_KW):
        return 'avoid'
    return 'unknown'


# Default frequencies by category
CATEGORY_FREQ = {
    'surgical': 'once',
    'maneuver': 'per session',
    'education': 'once',
    'exercise': 'daily',
    'device': 'continuous',
    'lifestyle': 'daily',
    'monitoring': 'continuous',
    'protocol': 'per protocol',
    'drug': 'per protocol',
    'avoid': 'N/A',
    'unknown': 'per protocol',
}


def infer_frequency(treatment_name, dosing_text):
    """Infer frequency from treatment category and dosing text context."""
    dosing_lower = dosing_text.lower()
    category = categorize_treatment(treatment_name)

    # For non-drug categories, prefer category defaults over text extraction
    # (text may mention frequencies in monitoring/instruction context, not dosing)
    if category in ('surgical', 'maneuver', 'education', 'device', 'avoid'):
        # Still check text for some clear patterns
        freq = extract_frequency(dosing_text)
        if freq and category == 'device':
            return freq  # devices might have real frequencies
        return CATEGORY_FREQ[category]

    # Try text-based extraction first for drugs and protocols
    freq = extract_frequency(dosing_text)
    if freq:
        return freq

    # Check for infusion rate patterns → continuous
    if re.search(r'\b\d+[\d.]*\s*(?:µg|mcg|mg|mL|units?)/(?:kg/)?(?:min|hr|h|hour)\b', dosing_lower):
        return 'continuous'
    if 'infusion' in dosing_lower or 'drip' in dosing_lower:
        return 'continuous'

    # Context clues in dosing text
    if 'at night' in dosing_lower or 'at bedtime' in dosing_lower or 'bedtime' in dosing_lower:
        return 'QHS'
    if 'per session' in dosing_lower:
        return 'per session'
    if 'before meals' in dosing_lower or 'with meals' in dosing_lower:
        return 'TID'
    if re.search(r'\b\d+\s*mg\s+AM\b', dosing_text):
        return 'daily'
    if re.search(r'\bmg/day\b', dosing_lower) or re.search(r'\bg/day\b', dosing_lower):
        return 'daily'
    if re.search(r'\bx\s*\d+\s*(?:days?|weeks?|months?)\b', dosing_lower):
        return 'daily'
    if re.search(r'\b\d+[-–]\d+\s*(?:weeks?|months?)\b', dosing_lower):
        return 'per protocol'
    if 'per arrhythmia' in dosing_lower or 'per condition' in dosing_lower:
        return 'per protocol'
    if 'per ' in dosing_lower[:15] and 'per protocol' not in dosing_lower[:25]:
        return 'per protocol'
    if 'if ' in dosing_lower[:10]:
        return 'per protocol'

    # Fall back to category default
    return CATEGORY_FREQ.get(category, 'per protocol')


def convert_entry(treatment_name, route_col, dosing_text):
    """Convert a plain-text dosing entry to structured format."""
    # Extract dose
    dose = extract_starting_dose(dosing_text)
    if not dose:
        dose = 'N/A'

    # Use route from the Route column
    route = route_col if route_col and route_col not in ('-', '') else '-'

    # Determine frequency
    freq = infer_frequency(treatment_name, dosing_text)

    return f"{dose} :: {route} :: {freq} :: {dosing_text}"


def is_treatment_table_header(line):
    """Check if a line is a standard treatment table header with Dosing column."""
    return ('| Treatment' in line or '| Treatment' in line.replace('**', '')) \
        and '| Dosing' in line


def parse_header_columns(header_line):
    """Parse a header line and return column name → index mapping."""
    cells = [c.strip() for c in header_line.split('|')]
    # Remove empty cells from leading/trailing pipes
    if cells and cells[0] == '':
        cells = cells[1:]
    if cells and cells[-1] == '':
        cells = cells[:-1]
    return {name: idx for idx, name in enumerate(cells)}


def fix_file(filepath, dry_run=False):
    """Fix unstructured dosing entries in a single plan file."""
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    in_treatment_table = False
    col_map = {}
    changes = []
    new_lines = []

    for i, line in enumerate(lines):
        # Check for treatment table header
        if is_treatment_table_header(line):
            in_treatment_table = True
            col_map = parse_header_columns(line)
            new_lines.append(line)
            continue

        # Separator row (---|---|...)
        if in_treatment_table and line.strip().startswith('|') and '---' in line:
            new_lines.append(line)
            continue

        # End of table: blank line or non-pipe line
        if in_treatment_table and (not line.strip() or not line.strip().startswith('|')):
            in_treatment_table = False
            col_map = {}
            new_lines.append(line)
            continue

        # Process table data row
        if in_treatment_table and 'Dosing' in col_map and line.strip().startswith('|'):
            cells = line.split('|')
            # cells[0] is empty (before first pipe), cells[-1] is empty (after last pipe)
            # Data cells are cells[1:-1]
            data_cells = cells[1:-1] if len(cells) > 2 else cells

            dosing_idx = col_map.get('Dosing')
            treatment_idx = col_map.get('Treatment')
            route_idx = col_map.get('Route')

            if dosing_idx is not None and dosing_idx < len(data_cells):
                dosing = data_cells[dosing_idx].strip()

                # Skip if already structured, empty, or just a dash
                if '::' in dosing or dosing in ('-', '', 'N/A'):
                    new_lines.append(line)
                    continue

                treatment = data_cells[treatment_idx].strip() if treatment_idx is not None and treatment_idx < len(data_cells) else ''
                route = data_cells[route_idx].strip() if route_idx is not None and route_idx < len(data_cells) else '-'

                structured = convert_entry(treatment, route, dosing)

                # Replace the dosing cell content
                data_cells[dosing_idx] = ' ' + structured + ' '

                # Reconstruct line
                new_line = '|' + '|'.join(data_cells) + '|'
                changes.append({
                    'line': i + 1,
                    'treatment': treatment.replace('**', '').strip()[:50],
                    'old_dosing': dosing[:80],
                    'new_dosing': structured[:100],
                    'category': categorize_treatment(treatment),
                })
                line = new_line

        new_lines.append(line)

    if changes and not dry_run:
        path.write_text('\n'.join(new_lines), encoding='utf-8')

    return changes


def main():
    dry_run = '--dry-run' in sys.argv
    files = []

    if '--all' in sys.argv:
        plans_dir = Path('docs/plans')
        files = sorted(plans_dir.glob('*.md'))
    else:
        for arg in sys.argv[1:]:
            if not arg.startswith('--'):
                files.append(Path(arg))

    if not files:
        print("Usage: python scripts/convert_to_structured_dosing.py --all [--dry-run]")
        print("       python scripts/convert_to_structured_dosing.py docs/plans/file.md [--dry-run]")
        sys.exit(1)

    total_converted = 0
    all_changes = []

    for filepath in files:
        changes = fix_file(filepath, dry_run=dry_run)
        if changes:
            total_converted += len(changes)
            all_changes.extend([(filepath.name, c) for c in changes])
            print(f"\n  {filepath.name}: {len(changes)} entries converted")
            for c in changes:
                print(f"    Line {c['line']}: [{c['category']}] {c['treatment']}")
                print(f"      OLD: {c['old_dosing']}")
                print(f"      NEW: {c['new_dosing']}")

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'=' * 70}")
    print(f"  {mode}: {total_converted} entries converted across {len(set(f for f, _ in all_changes))} files")
    print(f"{'=' * 70}")

    # Summary by category
    if all_changes:
        cats = {}
        for _, c in all_changes:
            cat = c['category']
            cats[cat] = cats.get(cat, 0) + 1
        print("\n  By category:")
        for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
            print(f"    {cat}: {count}")


if __name__ == '__main__':
    main()
