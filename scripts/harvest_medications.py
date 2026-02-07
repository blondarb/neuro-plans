#!/usr/bin/env python3
"""Harvest medications from approved plan JSON data into the central medication database.

Reads docs/data/plans.json, extracts all treatment items with valid routes,
deduplicates by normalized name, and merges into docs/data/medications.json.

Existing validated entries are preserved (merge, don't overwrite).

Usage:
    python -X utf8 scripts/harvest_medications.py --preview   # Show what would be harvested
    python -X utf8 scripts/harvest_medications.py --stats     # Show counts and coverage
    python -X utf8 scripts/harvest_medications.py --merge     # Harvest and merge into medications.json
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


# --- Normalization (reused from extract_medications.py) ---

def normalize_med_name(name):
    """Normalize medication name for deduplication."""
    name = name.lower().strip()
    name = re.sub(r'\*+', '', name)           # Remove bold markers
    name = re.sub(r'~~[^~]*~~', '', name)     # Remove strikethrough
    name = re.sub(r'\([^)]*\)', '', name)     # Remove (Brand Name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def make_id(name):
    """Convert a normalized name into a hyphenated ID."""
    return re.sub(r'[^a-z0-9]+', '-', name).strip('-')


def make_context_id(indication):
    """Convert an indication string into a context ID."""
    s = indication.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    # Truncate to reasonable length
    return s[:60]


# --- Skipping logic ---

SKIP_ROUTES = {
    '-', 'N/A', 'External', 'Diet', 'Implant', '', 'Consult', 'Procedure',
    'Surgical', 'surgical', 'Surgery', 'Fluoroscopic', 'Endovascular', 'endovascular',
    'surgical/endovascular', 'Surgical/Endovascular', 'Behavioral', 'In-person',
    'Ventilator', 'Device', 'device', 'External programming', 'External/Internal',
    'external', 'Visual', 'Mechanical', 'Referral', 'Outpatient surgery',
    'Inpatient surgery', 'Percutaneous', 'External beam', 'XRT',
    'external/IV', 'Extracorporeal', 'Obstetric',
}

def is_medication_item(item):
    """Determine if a treatment item is an actual medication (not a procedure/assessment)."""
    route = item.get('route', '-')

    # Check dosing route too
    dosing = item.get('dosing', {})
    if isinstance(dosing, dict):
        dosing_route = dosing.get('route', '')
        if dosing_route and dosing_route not in SKIP_ROUTES:
            route = dosing_route

    if route in SKIP_ROUTES:
        return False

    # Skip items that look like procedures/assessments
    item_name = item.get('item', '')
    skip_patterns = [
        r'^(?:physical therapy|occupational therapy|speech therapy)',
        r'^(?:consult|referral|evaluation|assessment|monitoring)',
        r'^(?:ECG|EEG|MRI|CT |LP |lumbar puncture)',
        r'^(?:surgical|surgery|procedure|biopsy)',
        r'^(?:diet|nutrition|exercise|activity)',
    ]
    normalized = normalize_med_name(item_name)
    for pattern in skip_patterns:
        if re.match(pattern, normalized, re.IGNORECASE):
            return False

    return True


# --- Harvesting ---

def harvest_from_plans(plans_json_path):
    """Extract all medication items from plans.json."""
    with open(plans_json_path, 'r', encoding='utf-8') as f:
        plans = json.load(f)

    all_meds = []

    for plan_name, plan_data in plans.items():
        sections = plan_data.get('sections', {})
        if not isinstance(sections, dict):
            continue

        for section_name, section_data in sections.items():
            # Only treatment sections
            if 'treatment' not in section_name.lower():
                continue

            if isinstance(section_data, dict):
                # Nested subsections
                for subsection_name, items in section_data.items():
                    if isinstance(items, list):
                        for item in items:
                            if isinstance(item, dict) and is_medication_item(item):
                                all_meds.append({
                                    'plan': plan_name,
                                    'section': section_name,
                                    'subsection': subsection_name,
                                    **extract_fields(item)
                                })
            elif isinstance(section_data, list):
                for item in section_data:
                    if isinstance(item, dict) and is_medication_item(item):
                        all_meds.append({
                            'plan': plan_name,
                            'section': section_name,
                            'subsection': None,
                            **extract_fields(item)
                        })

    return all_meds


def extract_fields(item):
    """Extract relevant fields from a treatment item."""
    dosing = item.get('dosing', {})
    if not isinstance(dosing, dict):
        dosing = {}

    # Get route from item or dosing
    route = item.get('route', '-')
    dosing_route = dosing.get('route', '')
    if dosing_route and dosing_route not in SKIP_ROUTES:
        route = dosing_route

    return {
        'name': item.get('item', '').strip(),
        'normalized': normalize_med_name(item.get('item', '')),
        'route': route,
        'indication': item.get('indication', '-'),
        'doseOptions': dosing.get('doseOptions', []),
        'instructions': dosing.get('instructions', ''),
        'contraindications': item.get('contraindications', '-'),
        'monitoring': item.get('monitoring', '-'),
        'ED': item.get('ED', '-'),
        'HOSP': item.get('HOSP', '-'),
        'OPD': item.get('OPD', '-'),
        'ICU': item.get('ICU', '-'),
    }


# --- Deduplication and merging ---

def deduplicate(all_meds):
    """Group by normalized name and merge contexts."""
    groups = defaultdict(list)
    for med in all_meds:
        groups[med['normalized']].append(med)

    medications = {}

    for normalized_name, occurrences in groups.items():
        # Use the most common display name (prefer non-bold)
        name_counts = defaultdict(int)
        for occ in occurrences:
            clean_name = re.sub(r'\*+', '', occ['name']).strip()
            name_counts[clean_name] += 1
        display_name = max(name_counts, key=name_counts.get)

        med_id = make_id(normalized_name)

        # Collect unique routes
        routes = sorted(set(
            occ['route'] for occ in occurrences
            if occ['route'] and occ['route'] not in SKIP_ROUTES
        ))

        # Build contexts from unique indication + settings combos
        contexts = {}
        seen_indications = {}  # normalized indication -> context_id

        for occ in occurrences:
            indication = occ['indication']
            if not indication or indication == '-':
                indication = 'general'

            ind_normalized = indication.lower().strip()

            if ind_normalized not in seen_indications:
                ctx_id = make_context_id(indication)
                # Ensure unique context IDs
                base_ctx_id = ctx_id
                counter = 2
                while ctx_id in contexts:
                    ctx_id = f"{base_ctx_id}-{counter}"
                    counter += 1

                seen_indications[ind_normalized] = ctx_id

                contexts[ctx_id] = {
                    'indication': indication if indication != 'general' else '-',
                    'doseOptions': occ['doseOptions'],
                    'startingDose': '',
                    'maxDose': '',
                    'titration': '',
                    'notes': occ['instructions'],
                    'settings': {
                        'ED': occ['ED'],
                        'HOSP': occ['HOSP'],
                        'OPD': occ['OPD'],
                        'ICU': occ['ICU'],
                    },
                    '_sourcePlans': [occ['plan']]
                }
            else:
                # Same indication from a different plan — add source plan
                ctx_id = seen_indications[ind_normalized]
                if occ['plan'] not in contexts[ctx_id]['_sourcePlans']:
                    contexts[ctx_id]['_sourcePlans'].append(occ['plan'])

                # Merge settings (keep highest priority)
                existing = contexts[ctx_id]['settings']
                for venue in ('ED', 'HOSP', 'OPD', 'ICU'):
                    if existing[venue] == '-' and occ[venue] != '-':
                        existing[venue] = occ[venue]

                # Merge dose options if the existing context has fewer
                if len(occ['doseOptions']) > len(contexts[ctx_id]['doseOptions']):
                    contexts[ctx_id]['doseOptions'] = occ['doseOptions']

        # Build contraindications from all occurrences
        all_contras = set()
        for occ in occurrences:
            c = occ['contraindications']
            if c and c != '-':
                # Split on semicolons
                for part in c.split(';'):
                    part = part.strip()
                    if part and part != '-':
                        all_contras.add(part)

        # Build monitoring from all occurrences
        all_monitoring = set()
        for occ in occurrences:
            m = occ['monitoring']
            if m and m != '-':
                for part in m.split(';'):
                    part = part.strip()
                    if part and part != '-':
                        all_monitoring.add(part)

        medications[med_id] = {
            'id': med_id,
            'name': display_name,
            'genericName': '',
            'brandNames': [],
            'drugClass': '',
            'mechanisms': [],
            'routes': routes,
            'formulations': [],
            'contexts': contexts,
            'safety': {
                'blackBoxWarnings': [],
                'contraindications': sorted(all_contras),
                'precautions': [],
                'drugInteractions': [],
                'pregnancyCategory': '',
                'lactation': ''
            },
            'renalAdjustment': {'required': False, 'tiers': []},
            'hepaticAdjustment': {'required': False, 'notes': ''},
            'monitoring': {
                'baseline': [],
                'ongoing': sorted(all_monitoring),
                'frequency': ''
            },
            'patientCounseling': [],
            '_harvested': True,
            '_sourceCount': len(occurrences),
            '_sourcePlans': sorted(set(occ['plan'] for occ in occurrences))
        }

    return medications


def merge_into_db(harvested, db_path):
    """Merge harvested medications into existing database, preserving validated entries."""
    # Load existing DB
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = {'_metadata': {}, 'medications': {}}

    existing_meds = existing.get('medications', {})

    merged_count = 0
    new_count = 0
    preserved_count = 0

    for med_id, harvested_med in harvested.items():
        if med_id in existing_meds:
            # Existing validated entry — don't overwrite, but merge new contexts
            existing_med = existing_meds[med_id]
            existing_contexts = existing_med.get('contexts', {})
            harvested_contexts = harvested_med.get('contexts', {})

            for ctx_id, ctx_data in harvested_contexts.items():
                if ctx_id not in existing_contexts:
                    # Add settings to existing contexts that lack them
                    existing_contexts[ctx_id] = ctx_data
                    merged_count += 1
                elif 'settings' not in existing_contexts[ctx_id]:
                    # Add settings field to existing context
                    existing_contexts[ctx_id]['settings'] = ctx_data.get('settings', {})

            existing_med['contexts'] = existing_contexts
            preserved_count += 1
        else:
            # New medication — add it
            existing_meds[med_id] = harvested_med
            new_count += 1

    # Update metadata
    from datetime import date
    existing['_metadata']['lastUpdated'] = str(date.today())
    existing['_metadata']['version'] = '2.0.0'
    existing['_metadata']['description'] = (
        'Central medication database for Neuro Plans - '
        'single source of truth for all medication data. '
        f'Contains {len(existing_meds)} medications harvested from {len(set(p for m in harvested.values() for p in m.get("_sourcePlans", [])))} plans.'
    )
    existing['medications'] = dict(sorted(existing_meds.items()))

    # Write back
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
        f.write('\n')

    return new_count, merged_count, preserved_count


# --- CLI ---

def main():
    plans_json = Path('docs/data/plans.json')
    db_path = Path('docs/data/medications.json')

    if not plans_json.exists():
        print(f"Error: {plans_json} not found", file=sys.stderr)
        sys.exit(1)

    print(f"\nHarvesting medications from {plans_json}...")
    all_meds = harvest_from_plans(plans_json)
    print(f"  Found {len(all_meds)} total medication items")

    medications = deduplicate(all_meds)
    print(f"  Deduplicated to {len(medications)} unique medications")

    # Load existing DB for comparison
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            existing_db = json.load(f)
            existing_count = len(existing_db.get('medications', {}))
    except (FileNotFoundError, json.JSONDecodeError):
        existing_count = 0

    if '--stats' in sys.argv:
        print(f"\n{'=' * 60}")
        print(f"  MEDICATION HARVEST STATS")
        print(f"{'=' * 60}")
        print(f"  Total treatment items found: {len(all_meds)}")
        print(f"  Unique medications: {len(medications)}")
        print(f"  Currently in DB: {existing_count}")
        print(f"  New medications: {len(medications) - existing_count}")

        # Count by route
        route_counts = defaultdict(int)
        for med in medications.values():
            for r in med['routes']:
                route_counts[r] += 1
        print(f"\n  By route:")
        for route, count in sorted(route_counts.items(), key=lambda x: -x[1]):
            print(f"    {route}: {count}")

        # Count by number of contexts
        ctx_counts = defaultdict(int)
        for med in medications.values():
            ctx_counts[len(med['contexts'])] += 1
        print(f"\n  By context count:")
        for count, n in sorted(ctx_counts.items()):
            print(f"    {count} context(s): {n} medications")

        # Count by source plans
        plan_counts = defaultdict(int)
        for med in medications.values():
            plan_counts[len(med['_sourcePlans'])] += 1
        print(f"\n  By plan coverage:")
        for count, n in sorted(plan_counts.items(), reverse=True)[:10]:
            print(f"    Appears in {count} plan(s): {n} medications")

        # Top 20 most-used medications
        top_meds = sorted(medications.values(), key=lambda m: -m['_sourceCount'])[:20]
        print(f"\n  Top 20 most-used medications:")
        for med in top_meds:
            print(f"    {med['name']:<40} ({med['_sourceCount']}x in {len(med['_sourcePlans'])} plans)")

        return

    if '--preview' in sys.argv:
        print(f"\n{'=' * 60}")
        print(f"  HARVEST PREVIEW (first 30 medications)")
        print(f"{'=' * 60}\n")

        sorted_meds = sorted(medications.values(), key=lambda m: -m['_sourceCount'])
        for med in sorted_meds[:30]:
            ctx_list = list(med['contexts'].keys())
            print(f"  {med['name']}")
            print(f"    ID: {med['id']}")
            print(f"    Routes: {', '.join(med['routes'])}")
            print(f"    Contexts: {', '.join(ctx_list[:3])}{'...' if len(ctx_list) > 3 else ''}")
            print(f"    Contraindications: {len(med['safety']['contraindications'])} items")
            print(f"    From {len(med['_sourcePlans'])} plans ({med['_sourceCount']} occurrences)")
            print()

        if len(medications) > 30:
            print(f"  ... and {len(medications) - 30} more medications")
        print(f"\n  Run with --merge to write to {db_path}")
        return

    if '--merge' in sys.argv:
        new, merged, preserved = merge_into_db(medications, db_path)
        print(f"\n{'=' * 60}")
        print(f"  MERGE COMPLETE")
        print(f"{'=' * 60}")
        print(f"  New medications added: {new}")
        print(f"  Existing entries preserved: {preserved}")
        print(f"  New contexts merged: {merged}")
        print(f"  Total in database: {existing_count + new}")
        print(f"\n  Written to: {db_path}")
        return

    # Default: show help
    print(f"\nUsage:")
    print(f"  python -X utf8 scripts/harvest_medications.py --preview")
    print(f"  python -X utf8 scripts/harvest_medications.py --stats")
    print(f"  python -X utf8 scripts/harvest_medications.py --merge")


if __name__ == '__main__':
    main()
