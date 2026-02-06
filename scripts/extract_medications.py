#!/usr/bin/env python3
"""Extract all unique medications from plan JSON files.

This script analyzes all plan files to identify unique medications,
their contexts (indications), and current dosing information.
Used to build the central medication database.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def normalize_med_name(name):
    """Normalize medication name for comparison."""
    name = name.lower()
    name = re.sub(r'\*+', '', name)  # Remove bold markers
    name = re.sub(r'\([^)]*\)', '', name)  # Remove (Brand Name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def extract_medications(json_path):
    """Extract medications from a single plan JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"  Error reading {json_path.name}: {e}", file=sys.stderr)
        return []

    medications = []
    plan_name = json_path.stem

    sections = data.get('sections', {})
    if not isinstance(sections, dict):
        return []

    for section_name, section_data in sections.items():
        # Look for treatment sections
        if 'treatment' not in section_name.lower():
            continue

        if isinstance(section_data, dict):
            # Nested subsections
            for subsection_name, items in section_data.items():
                if isinstance(items, list):
                    for item in items:
                        if isinstance(item, dict):
                            med_info = extract_med_from_item(item, plan_name, section_name, subsection_name)
                            if med_info:
                                medications.append(med_info)
        elif isinstance(section_data, list):
            for item in section_data:
                if isinstance(item, dict):
                    med_info = extract_med_from_item(item, plan_name, section_name, None)
                    if med_info:
                        medications.append(med_info)

    return medications


def extract_med_from_item(item, plan_name, section_name, subsection_name):
    """Extract medication info from a treatment item."""
    item_name = item.get('item', '')
    if not item_name:
        return None

    # Skip non-medication items
    route = item.get('route', '')
    if route in ('-', 'N/A', 'External', 'Diet', 'Implant', ''):
        # Check if dosing has route
        dosing = item.get('dosing', {})
        if isinstance(dosing, dict):
            route = dosing.get('route', route)
        if route in ('-', 'N/A', 'External', 'Diet', 'Implant', ''):
            return None

    dosing = item.get('dosing', {})
    if not isinstance(dosing, dict):
        return None

    return {
        'name': item_name,
        'normalized': normalize_med_name(item_name),
        'plan': plan_name,
        'section': section_name,
        'subsection': subsection_name,
        'route': route or dosing.get('route', ''),
        'indication': item.get('indication', ''),
        'instructions': dosing.get('instructions', ''),
        'contraindications': item.get('contraindications', ''),
        'monitoring': item.get('monitoring', ''),
        'doseOptions': dosing.get('doseOptions', [])
    }


def main():
    plans_dir = Path('docs/plans')
    if not plans_dir.exists():
        print(f"Error: {plans_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    all_medications = []

    # Collect all medications
    for json_file in sorted(plans_dir.glob('*.json')):
        # Skip non-plan files
        if any(x in json_file.name for x in ['report', 'citation', 'cpt-synonym', 'icd-synonym']):
            continue

        meds = extract_medications(json_file)
        all_medications.extend(meds)

    # Group by normalized name
    med_groups = defaultdict(list)
    for med in all_medications:
        med_groups[med['normalized']].append(med)

    # Output analysis
    print(f"\n{'=' * 70}")
    print(f"  MEDICATION EXTRACTION REPORT")
    print(f"{'=' * 70}")
    print(f"\n  Total medications found: {len(all_medications)}")
    print(f"  Unique medications: {len(med_groups)}")

    # Sort by frequency (most common first)
    sorted_meds = sorted(med_groups.items(), key=lambda x: -len(x[1]))

    print(f"\n  Top 50 most common medications:")
    print(f"  {'-' * 60}")

    for i, (name, occurrences) in enumerate(sorted_meds[:50], 1):
        plans = set(o['plan'] for o in occurrences)
        indications = set(o['indication'] for o in occurrences if o['indication'] and o['indication'] != '-')
        print(f"  {i:3}. {name[:40]:<40} ({len(occurrences):2}x in {len(plans):2} plans)")
        if indications:
            for ind in list(indications)[:2]:
                print(f"       - {ind[:60]}")

    # Output JSON for further processing
    if '--json' in sys.argv:
        output = {}
        for name, occurrences in sorted_meds:
            plans = list(set(o['plan'] for o in occurrences))
            indications = list(set(o['indication'] for o in occurrences if o['indication'] and o['indication'] != '-'))
            routes = list(set(o['route'] for o in occurrences if o['route']))

            output[name] = {
                'count': len(occurrences),
                'plans': plans,
                'indications': indications,
                'routes': routes
            }

        print(json.dumps(output, indent=2))

    # Output full details
    if '--full' in sys.argv:
        print(f"\n\n  ALL MEDICATIONS BY NAME:")
        print(f"  {'=' * 60}")

        for name, occurrences in sorted_meds:
            print(f"\n  {name}")
            print(f"  {'-' * 50}")
            for o in occurrences:
                print(f"    Plan: {o['plan']}")
                print(f"    Indication: {o['indication'][:60] if o['indication'] else '-'}")
                print(f"    Route: {o['route']}")
                print()

    # List medications not yet in central database
    if '--missing' in sys.argv:
        try:
            with open('docs/data/medications.json', 'r', encoding='utf-8') as f:
                central_db = json.load(f)
                existing_meds = set(central_db.get('medications', {}).keys())
        except FileNotFoundError:
            existing_meds = set()

        print(f"\n\n  MEDICATIONS NOT IN CENTRAL DATABASE:")
        print(f"  {'=' * 60}")

        missing = []
        for name, occurrences in sorted_meds:
            if name not in existing_meds:
                missing.append((name, occurrences))

        print(f"  Missing: {len(missing)} medications\n")

        for name, occurrences in missing[:100]:
            plans = set(o['plan'] for o in occurrences)
            print(f"    {name[:40]:<40} ({len(occurrences)}x in {len(plans)} plans)")


if __name__ == '__main__':
    main()
