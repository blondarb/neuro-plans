#!/usr/bin/env python3
"""Fix missing frequency fields in structured dosing columns.

Scans plan markdown files for treatment table rows where the dosing column
uses the format `dose :: route :: :: instructions` (empty 3rd field) and
fills in the frequency by extracting it from the dose or instructions text.
"""

import re
import sys
from pathlib import Path


# Common frequency patterns to look for in dose/instruction text
# Order matters: more specific patterns first
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
    # Named frequencies (case-insensitive matching handled by re.IGNORECASE)
    (r'\bTID[-–]QID\b', lambda m: "TID-QID"),
    (r'\bQID\b', lambda m: "QID"),
    (r'\bTID\b', lambda m: "TID"),
    (r'\bBID\b', lambda m: "BID"),
    (r'\bQHS\b', lambda m: "QHS"),
    (r'\bqHS\b', lambda m: "QHS"),
    # Daily variants
    (r'\bonce daily\b', lambda m: "daily"),
    (r'\bdaily\b', lambda m: "daily"),
    # Continuous infusion markers
    (r'\bcontinuous\b', lambda m: "continuous"),
    (r'\bcontinuous infusion\b', lambda m: "continuous"),
    (r'\b\d+[\.\d]* m(?:g|cg|L)/(?:h|hr|hour|min)\b', lambda m: "continuous"),
    # Single dose/administration
    (r'\bsingle dose\b', lambda m: "once"),
    (r'\bsingle spray\b', lambda m: "once PRN"),
    (r'\bone dose\b', lambda m: "once"),
    (r'\bIV push\b', lambda m: "once"),
    (r'\bIM(?:\s|;|$)', lambda m: "once"),
    (r'\bonce\b', lambda m: "once"),
    # PRN
    (r'\bPRN\b', lambda m: "PRN"),
    # Other intervals
    (r'\bweekly\b', lambda m: "weekly"),
    (r'\bmonthly\b', lambda m: "monthly"),
    # dose/day divided patterns
    (r'\b(?:mg|g|mcg)/(?:kg/)?day\s+divided\b', lambda m: "divided doses"),
    (r'\bdivided\s+(?:TID|QID|BID)\b', lambda m: m.group().split()[-1]),
    # "with each X dose" patterns
    (r'\bwith each\b', lambda m: "with each dose"),
]


def extract_frequency(dose_text, instructions_text):
    """Extract the most appropriate frequency from dose and instructions text."""
    # First check dose text (before first ::) — often has the freq directly
    # Priority order matters: check more specific patterns first

    # Check dose field first
    for pattern, formatter in FREQ_PATTERNS:
        match = re.search(pattern, dose_text, re.IGNORECASE)
        if match:
            return formatter(match)

    # Then check instructions field
    for pattern, formatter in FREQ_PATTERNS:
        match = re.search(pattern, instructions_text, re.IGNORECASE)
        if match:
            return formatter(match)

    # Special cases for surgical/procedural/protocol entries
    combined = dose_text + ' ' + instructions_text
    if 'surgical' in dose_text.lower() or 'N/A' in dose_text:
        return "once"
    if 'stimulation' in dose_text.lower() or 'device' in dose_text.lower():
        return "once"
    if 'per protocol' in combined.lower() or 'per specific' in dose_text.lower():
        return "per protocol"
    if dose_text.lower().startswith('per ') or dose_text.lower().startswith('see appendix'):
        return "per protocol"
    if 'home dose' in dose_text.lower():
        return "per home regimen"
    if 'individualized' in dose_text.lower() or 'individualized' in instructions_text.lower():
        return "per protocol"
    # Check for x/day or per day patterns
    if re.search(r'\b(\d+)/day\b', combined):
        return "daily"
    # Low-GI or dietary entries
    if re.search(r'\bg(?:\s+net)?\s+carbs?\b', combined, re.IGNORECASE):
        return "daily"
    if re.search(r'\bfat-to-\b', combined, re.IGNORECASE):
        return "daily"
    # Patch/24hr patterns
    if re.search(r'\b\d+\s*(?:mg|mcg)/24hr\b', combined) or 'patch' in combined.lower():
        return "daily"
    # "at birth" patterns
    if 'at birth' in instructions_text.lower():
        return "once"
    # Units total (e.g., botox)
    if re.search(r'\bunits?\s+total\b', combined, re.IGNORECASE):
        return "per session"
    # Loading dose patterns
    if re.search(r'\bloading?\b', combined, re.IGNORECASE) and 'over' in instructions_text.lower():
        return "once"
    # "over X min" = single dose administration
    if re.search(r'\bover \d+[-–]?\d*\s*min\b', combined, re.IGNORECASE) and not re.search(r'\bthen\b', instructions_text[:50]):
        return "once"
    # "based on weight" rescue dosing
    if 'based on weight' in dose_text.lower():
        return "once PRN"
    # "1 vial" or single unit doses
    if re.search(r'^\d+\s+vials?\b', dose_text, re.IGNORECASE):
        return "once"
    # IV bolus then maintenance
    if re.search(r'\bIV\s+bolus\b', combined, re.IGNORECASE) or re.search(r'\bmL/kg\b', dose_text):
        return "once"
    # PE/kg (phenytoin equivalent loading)
    if re.search(r'\bPE/kg\b', dose_text):
        return "once"
    # SC dose escalation (apomorphine etc)
    if re.search(r'\d+\s*mg\s+SC;\s*\d+\s*mg\s+SC', dose_text):
        return "PRN"
    # hydralazine/labetalol repeat dosing
    if re.search(r'\d+\s*mg\s+IV;\s*\d+\s*mg\s+IV', dose_text):
        return "PRN"
    # low-GI carbs/day
    if 'carbs' in combined.lower() or 'carbohydrate' in combined.lower():
        return "daily"

    return None


def fix_file(filepath, dry_run=False):
    """Fix empty frequency fields in a single plan file."""
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    changes = []
    new_lines = []

    # Regex to find: dose :: route :: :: instructions (empty 3rd field)
    # Uses a regex that captures the dose, route, and instructions parts
    empty_freq_re = re.compile(r'([^|]*?) :: ([A-Za-z/,. -]+?) :: :: (.*?)(?=\|)')

    for i, line in enumerate(lines):
        if ' :: :: ' in line and '|' in line:
            match = empty_freq_re.search(line)
            if match:
                dose_text = match.group(1).strip()
                route_text = match.group(2).strip()
                instructions_text = match.group(3).strip()

                # Extract dose_text from the last pipe-delimited segment
                # (dose_text may include earlier table cells)
                if '|' in dose_text:
                    dose_text = dose_text.rsplit('|', 1)[-1].strip()

                freq = extract_frequency(dose_text, instructions_text)
                if freq:
                    old_str = f' :: {route_text} :: :: '
                    new_str = f' :: {route_text} :: {freq} :: '
                    new_line = line.replace(old_str, new_str, 1)
                    if new_line != line:
                        changes.append({
                            'line': i + 1,
                            'freq': freq,
                            'dose': dose_text[:60],
                        })
                        line = new_line
                else:
                    changes.append({
                        'line': i + 1,
                        'freq': '??? COULD NOT DETERMINE',
                        'dose': dose_text[:60],
                    })

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
        print("Usage: python scripts/fix_dosing_frequency.py --all [--dry-run]")
        print("       python scripts/fix_dosing_frequency.py docs/plans/file.md [--dry-run]")
        sys.exit(1)

    total_fixes = 0
    total_unfixed = 0

    for filepath in files:
        changes = fix_file(filepath, dry_run=dry_run)
        if changes:
            fixed = [c for c in changes if '???' not in c['freq']]
            unfixed = [c for c in changes if '???' in c['freq']]
            total_fixes += len(fixed)
            total_unfixed += len(unfixed)

            if fixed or unfixed:
                print(f"\n  {filepath.name}: {len(fixed)} fixed, {len(unfixed)} unresolved")
                for c in fixed:
                    print(f"    Line {c['line']}: → {c['freq']}  ({c['dose']})")
                for c in unfixed:
                    print(f"    Line {c['line']}: ??? COULD NOT DETERMINE  ({c['dose']})")

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'=' * 60}")
    print(f"  {mode}: {total_fixes} frequencies filled, {total_unfixed} unresolved")
    print(f"{'=' * 60}")

    if total_unfixed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
