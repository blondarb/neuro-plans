#!/usr/bin/env python3
"""
Build script for neuro-clinical-plans site.

This script:
1. Syncs plans from /plans to docs/plans (if using separate source)
2. Generates/updates the plans index page
3. Extracts metadata from YAML frontmatter
"""

import argparse
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime

# Paths
ROOT = Path(__file__).parent.parent
PLANS_DIR = ROOT / "docs" / "plans"
INDEX_FILE = PLANS_DIR / "index.md"

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match YAML frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}

def get_first_heading(filepath):
    """Extract first H1 heading from markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return filepath.stem.replace('-', ' ').title()

def generate_plans_index():
    """Generate the plans index page from available plan files."""
    plans = []

    # Scan for plan files
    for filepath in PLANS_DIR.glob("*.md"):
        if filepath.name == "index.md":
            continue

        meta = extract_frontmatter(filepath)
        title = meta.get('title') or get_first_heading(filepath)
        description = meta.get('description', '')
        version = meta.get('version', '')
        setting = meta.get('setting', '')
        tags = meta.get('tags', [])

        plans.append({
            'filename': filepath.stem,
            'title': title,
            'description': description,
            'version': version,
            'setting': setting,
            'tags': tags
        })

    # Sort by title
    plans.sort(key=lambda x: x['title'])

    return plans

def categorize_plans(plans):
    """Group plans by category based on tags."""
    categories = {
        'Seizure & Epilepsy': [],
        'Stroke & Cerebrovascular': [],
        'Headache': [],
        'Demyelinating Diseases': [],
        'Neuromuscular Disorders': [],
        'Neuropathy': [],
        'Movement Disorders': [],
        'Dementia & Cognitive Disorders': [],
        'CNS Infections': [],
        'Neuro-Oncology': [],
        'Spinal Cord Disorders': [],
        'Autoimmune & Inflammatory': [],
        'Functional & Psychiatric': [],
        'Neurocritical Care': [],
        'Other': []
    }

    tag_to_category = {
        'seizure': 'Seizure & Epilepsy',
        'epilepsy': 'Seizure & Epilepsy',
        'stroke': 'Stroke & Cerebrovascular',
        'cerebrovascular': 'Stroke & Cerebrovascular',
        'headache': 'Headache',
        'migraine': 'Headache',
        'demyelinating': 'Demyelinating Diseases',
        'multiple-sclerosis': 'Demyelinating Diseases',
        'neuromuscular': 'Neuromuscular Disorders',
        'neuropathy': 'Neuropathy',
        'movement': 'Movement Disorders',
        'parkinson': 'Movement Disorders',
        'dementia': 'Dementia & Cognitive Disorders',
        'cognitive': 'Dementia & Cognitive Disorders',
        'infection': 'CNS Infections',
        'meningitis': 'CNS Infections',
        'encephalitis': 'CNS Infections',
        'oncology': 'Neuro-Oncology',
        'tumor': 'Neuro-Oncology',
        'spinal': 'Spinal Cord Disorders',
        'myelopathy': 'Spinal Cord Disorders',
        'autoimmune': 'Autoimmune & Inflammatory',
        'functional': 'Functional & Psychiatric',
        'neurocritical-care': 'Neurocritical Care',
        'emergency': 'Neurocritical Care',
    }

    for plan in plans:
        categorized = False
        for tag in plan['tags']:
            tag_lower = tag.lower()
            if tag_lower in tag_to_category:
                category = tag_to_category[tag_lower]
                if plan not in categories[category]:
                    categories[category].append(plan)
                    categorized = True
                    break

        if not categorized:
            categories['Other'].append(plan)

    return categories

def validate_frontmatter(plans):
    """Check that all plans have required frontmatter fields.

    Returns a list of (filename, missing_fields) tuples for plans with issues.
    """
    required = ['title', 'version']
    errors = []
    for plan in plans:
        missing = [f for f in required if not plan.get(f)]
        if missing:
            errors.append((plan['filename'], missing))
    return errors


def main():
    """Main build function."""
    parser = argparse.ArgumentParser(description='Build neuro-clinical-plans site')
    parser.add_argument('--strict', action='store_true',
                        help='Exit non-zero if any plan is missing required frontmatter')
    args = parser.parse_args()

    print("Building neuro-clinical-plans site...")

    # Generate plans data
    plans = generate_plans_index()
    print(f"Found {len(plans)} plans")

    # Strict mode: validate required frontmatter
    if args.strict:
        errors = validate_frontmatter(plans)
        if errors:
            print(f"\nERROR: {len(errors)} plan(s) missing required frontmatter:")
            for filename, missing in errors:
                print(f"  {filename}.md — missing: {', '.join(missing)}")
            sys.exit(1)
        else:
            print("Frontmatter validation passed")

    # Categorize plans
    categories = categorize_plans(plans)

    # Print summary
    for category, cat_plans in categories.items():
        if cat_plans:
            print(f"  {category}: {len(cat_plans)} plans")

    print("Build complete!")

if __name__ == "__main__":
    main()
