#!/usr/bin/env python3
"""
Citation verification script for neuro-plans.
Extracts citations with PMIDs and outputs them for verification.
"""

import re
import sys
from pathlib import Path

def extract_citations(file_path: Path) -> list:
    """Extract all citations with PMIDs from a markdown file."""
    content = file_path.read_text(encoding='utf-8')

    # Pattern to match citations like:
    # [Author et al. Journal Year (study name)](https://pubmed.ncbi.nlm.nih.gov/12345678/)
    # | Evidence statement | Class/Level | [Citation](url) |

    citations = []

    # Find all lines in Evidence section
    evidence_section = re.search(r'## 8\. EVIDENCE.*?(?=\n## |\Z)', content, re.DOTALL)
    if evidence_section:
        section_content = evidence_section.group(0)

        # Pattern for table rows with citations
        # | Evidence text | Level | [Citation text](pubmed_url) |
        row_pattern = r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*\[([^\]]+)\]\((https://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?\))\s*\|'

        for match in re.finditer(row_pattern, section_content):
            evidence_text = match.group(1).strip()
            evidence_level = match.group(2).strip()
            citation_text = match.group(3).strip()
            pmid = match.group(5)

            citations.append({
                'evidence': evidence_text,
                'level': evidence_level,
                'citation': citation_text,
                'pmid': pmid
            })

    return citations

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_citations.py <markdown_file>")
        print("       python verify_citations.py --all  # Check all approved plans")
        sys.exit(1)

    if sys.argv[1] == '--all':
        plans_dir = Path('docs/plans')
        md_files = sorted(plans_dir.glob('*.md'))
        md_files = [f for f in md_files if f.stem not in ('index',) and 'report' not in f.stem]
    else:
        md_files = [Path(sys.argv[1])]

    all_citations = []

    for file_path in md_files:
        if not file_path.exists():
            print(f"File not found: {file_path}")
            continue

        citations = extract_citations(file_path)
        if citations:
            print(f"\n{'='*60}")
            print(f"PLAN: {file_path.stem}")
            print(f"{'='*60}")
            print(f"Found {len(citations)} citations with PMIDs\n")

            for i, c in enumerate(citations, 1):
                print(f"{i}. PMID: {c['pmid']}")
                print(f"   Claimed: {c['citation']}")
                print(f"   Supports: {c['evidence'][:80]}...")
                print()
                all_citations.append({**c, 'plan': file_path.stem})

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(all_citations)} total citations to verify")
    print(f"{'='*60}")

    # Output PMIDs for batch verification
    pmids = sorted(set(c['pmid'] for c in all_citations))
    print(f"\nUnique PMIDs ({len(pmids)}):")
    print(', '.join(pmids))

if __name__ == '__main__':
    main()
