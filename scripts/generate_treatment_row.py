#!/usr/bin/env python3
"""Generate 10-column markdown treatment table rows from the central medication database.

Outputs ready-to-paste rows in the standard format:
| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |

Usage:
    # Single medication, specific context
    python -X utf8 scripts/generate_treatment_row.py gabapentin --context neuropathic-pain

    # Single medication, all contexts (one row per context)
    python -X utf8 scripts/generate_treatment_row.py gabapentin

    # Multiple medications
    python -X utf8 scripts/generate_treatment_row.py gabapentin pregabalin duloxetine

    # With table header
    python -X utf8 scripts/generate_treatment_row.py gabapentin --header

    # Search by indication (fuzzy match)
    python -X utf8 scripts/generate_treatment_row.py --indication "neuropathic pain"

    # List all available contexts for a medication
    python -X utf8 scripts/generate_treatment_row.py gabapentin --list-contexts
"""

import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from medication_resolver import MedicationResolver


def main():
    resolver = MedicationResolver()

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    # Parse arguments
    args = sys.argv[1:]
    context = None
    indication = None
    header = False
    list_contexts = False
    med_names = []

    i = 0
    while i < len(args):
        if args[i] == '--context':
            i += 1
            if i < len(args):
                context = args[i]
        elif args[i] == '--indication':
            i += 1
            if i < len(args):
                indication = args[i]
        elif args[i] == '--header':
            header = True
        elif args[i] == '--list-contexts':
            list_contexts = True
        elif args[i] == '--help':
            print(__doc__)
            sys.exit(0)
        elif not args[i].startswith('--'):
            med_names.append(args[i])
        i += 1

    # Search by indication
    if indication:
        resolver._load()
        print(f"\nMedications matching indication: \"{indication}\"\n")

        header_printed = False
        for med_id, med_data in sorted(resolver._medications.items()):
            for ctx_id, ctx_data in med_data.get('contexts', {}).items():
                ind_text = ctx_data.get('indication', '')
                if indication.lower() in ind_text.lower():
                    row = resolver.generate_treatment_row(
                        med_id,
                        context_id=ctx_id,
                        include_header=(header and not header_printed)
                    )
                    if row:
                        print(row)
                        header_printed = True
        return

    if not med_names:
        print("Error: Provide at least one medication name or use --indication", file=sys.stderr)
        sys.exit(1)

    # List contexts mode
    if list_contexts:
        for name in med_names:
            contexts = resolver.get_contexts(name)
            if not contexts:
                print(f"\n  '{name}' not found in database.")
                continue

            med = resolver.get_medication(name)
            print(f"\n  {med['name']} — Available contexts:")
            print(f"  {'—' * 50}")
            for ctx_id in contexts:
                ctx_data = med['contexts'][ctx_id]
                ind = ctx_data.get('indication', '-')
                n_doses = len(ctx_data.get('doseOptions', []))
                settings = ctx_data.get('settings', {})
                settings_str = ' '.join(
                    f"{k}={v}" for k, v in settings.items() if v != '-'
                ) if settings else ''
                print(f"    {ctx_id}")
                print(f"      Indication: {ind[:70]}")
                print(f"      Dose options: {n_doses}")
                if settings_str:
                    print(f"      Settings: {settings_str}")
                print()
        return

    # Generate rows
    header_printed = False
    for name in med_names:
        if context:
            # Single context
            row = resolver.generate_treatment_row(
                name,
                context_id=context,
                include_header=(header and not header_printed)
            )
            if row:
                print(row)
                header_printed = True
            else:
                print(f"# '{name}' not found or context '{context}' not available", file=sys.stderr)
        else:
            # All contexts
            rows = resolver.generate_treatment_rows(
                name,
                include_header=(header and not header_printed)
            )
            if rows:
                for row in rows:
                    print(row)
                header_printed = True
            else:
                print(f"# '{name}' not found in database", file=sys.stderr)


if __name__ == '__main__':
    main()
