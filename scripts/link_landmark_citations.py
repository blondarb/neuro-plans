#!/usr/bin/env python3
"""
Link landmark trial names and guideline references to PubMed.

Uses a curated lookup (landmark_pmids.json) to find unlinked mentions of
well-known clinical trials and guidelines in plan evidence tables, then
replaces them with markdown PubMed links.

Usage:
    # Report mode — show what would change without modifying files
    python3 scripts/link_landmark_citations.py --all --report

    # Apply mode — write links into plan files
    python3 scripts/link_landmark_citations.py --all --apply

    # Single plan
    python3 scripts/link_landmark_citations.py docs/plans/acute-ischemic-stroke.md --apply

    # Save report to JSON
    python3 scripts/link_landmark_citations.py --all --report --json docs/data/landmark-report.json
"""

import argparse
import glob
import json
import os
import re
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
PLANS_DIR = os.path.join(REPO_ROOT, "docs", "plans")
LOOKUP_FILE = os.path.join(SCRIPT_DIR, "landmark_pmids.json")

# Trial names that are also common English words — require the word "trial"
# nearby or other contextual clues to confirm they refer to the clinical trial
AMBIGUOUS_NAMES = {
    "REDUCE", "CLOSE", "PROGRESS", "POINT", "CHANCE", "PATCH",
    "EXPAND", "ESCAPE", "ADAPT", "PHOENIX", "SMART", "FIRST",
    "LATE", "START", "DAWN",
}

# Context clues that confirm a word is being used as a trial name
TRIAL_CONTEXT_WORDS = {"trial", "trials", "study", "studies"}


def load_lookup():
    """Load the curated trial/guideline → PMID mapping.

    Returns (trials_dict, guidelines_dict) separately so they can use
    different matching strategies.
    """
    with open(LOOKUP_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    trials = {}
    for name, info in data.get("trials", {}).items():
        trials[name] = info

    guidelines = {}
    for name, info in data.get("guidelines", {}).items():
        guidelines[name] = info

    return trials, guidelines


def pubmed_url(pmid):
    """Build a PubMed URL from a PMID."""
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def is_inside_markdown_link(text, start, end):
    """Check if position start..end is already inside a markdown link."""
    before = text[:start]
    after = text[end:]

    # Check if we're inside the display text of a link: [... MATCH ...](url)
    bracket_open = before.rfind("[")
    bracket_close = before.rfind("]")
    if bracket_open > bracket_close:
        # We're inside an open [ ... check if there's a ](url) after
        paren_pattern = re.compile(r"^[^\]]*\]\([^)]+\)")
        if paren_pattern.match(after) or paren_pattern.match(text[end:]):
            return True

    # Also check if preceded by ]( — meaning we're inside a URL
    if "](http" in before[max(0, start - 200):start]:
        url_region = before[before.rfind("]("):]
        if ")" not in url_region:
            return True

    return False


def has_trial_context(text, trial_name, start, end):
    """Check if an ambiguous trial name appears in a trial-like context.

    Returns True if:
    - The word "trial" or "study" appears near the match
    - The match appears in a comma/semicolon list with other ALL-CAPS words
      (suggesting a list of trial abbreviations)
    - The match is immediately followed by " trial" or " study"
    """
    full_lower = text.lower()

    # Check for "trial" or "study" within 60 chars of the match
    window_start = max(0, start - 60)
    window_end = min(len(text), end + 60)
    window = full_lower[window_start:window_end]
    for word in TRIAL_CONTEXT_WORDS:
        if word in window:
            return True

    # Check if surrounded by other ALL-CAPS abbreviations (trial list pattern)
    # e.g., "CLOSE, RESPECT, REDUCE" or "RE-LY, ROCKET-AF, ARISTOTLE"
    nearby = text[max(0, start - 40):min(len(text), end + 40)]
    caps_words = re.findall(r"\b[A-Z][A-Z0-9-]{2,}\b", nearby)
    # If there are at least 2 other ALL-CAPS words nearby, it's a trial list
    other_caps = [w for w in caps_words if w != trial_name]
    if len(other_caps) >= 1:
        return True

    return False


def find_trial_mentions(text, trial_name):
    """Find all unlinked mentions of a trial name in a line of text.

    Returns list of (start, end, matched_text) that are NOT inside existing
    links and pass contextual checks for ambiguous names.
    """
    mentions = []

    # Build regex: match the trial name at word boundaries
    escaped = re.escape(trial_name)
    # Allow flexible whitespace for multi-word names
    escaped = escaped.replace(r"\ ", r"\s+")
    # Use word boundaries — \b handles most cases cleanly
    pattern = re.compile(r"(?<!\w)" + escaped + r"(?!\w)", re.IGNORECASE)

    is_ambiguous = trial_name.upper() in AMBIGUOUS_NAMES

    for match in pattern.finditer(text):
        start, end = match.start(), match.end()

        # Skip if inside an existing markdown link
        if is_inside_markdown_link(text, start, end):
            continue

        # For ambiguous names, require trial context
        if is_ambiguous:
            # Only match if it appears as uppercase (trial names are caps)
            matched = match.group()
            if not matched[0].isupper():
                continue
            if not has_trial_context(text, trial_name, start, end):
                continue

        mentions.append((start, end, match.group()))

    return mentions


def find_guideline_mentions(text, guideline_name, info):
    """Find all unlinked mentions of a guideline using its match_patterns.

    Guidelines use flexible pattern matching because they appear in many
    textual variations (e.g., "AHA/ASA 2019 Guidelines", "AHA/ASA 2019").

    Returns list of (start, end, matched_text) sorted by match length
    (longest first) to prefer more specific patterns.
    """
    mentions = []
    patterns = info.get("match_patterns", [])
    if not patterns:
        # Fall back to key-based matching like trials
        patterns = [guideline_name]

    # Sort patterns by length (longest first) to prefer specific matches
    patterns_sorted = sorted(patterns, key=len, reverse=True)

    seen_positions = set()  # Avoid duplicate matches from overlapping patterns

    for pattern_text in patterns_sorted:
        escaped = re.escape(pattern_text)
        # Allow flexible whitespace
        escaped = escaped.replace(r"\ ", r"\s+")
        # Match at word-ish boundaries but be more lenient for guidelines
        # since they often start with org abbreviations like "AHA/ASA"
        regex = re.compile(escaped, re.IGNORECASE)

        for match in regex.finditer(text):
            start, end = match.start(), match.end()

            # Skip if this position was already claimed by a longer pattern
            if any(start >= s and start < e for s, e in seen_positions):
                continue

            # Skip if inside an existing markdown link
            if is_inside_markdown_link(text, start, end):
                continue

            mentions.append((start, end, match.group()))
            seen_positions.add((start, end))

    return mentions


def process_plan(filepath, trials, guidelines, apply=False):
    """Process a single plan file, finding and optionally replacing landmarks.

    Returns a dict with results for this plan.
    """
    plan_name = os.path.splitext(os.path.basename(filepath))[0]

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find evidence table section (section 8)
    in_evidence = False
    evidence_start = None
    evidence_end = None
    for i, line in enumerate(lines):
        if re.match(r"^##?\s*8[.\s]+", line, re.IGNORECASE):
            in_evidence = True
            evidence_start = i
            continue
        if in_evidence and re.match(r"^##?\s*\d+[.\s]+", line) and not re.match(r"^##?\s*8[.\s]+", line, re.IGNORECASE):
            evidence_end = i
            break

    if evidence_start is None:
        return {"plan": plan_name, "found": [], "skipped": "no evidence section"}

    if evidence_end is None:
        evidence_end = len(lines)

    # Process only evidence table rows (lines starting with |)
    found = []
    modified_lines = list(lines)

    for i in range(evidence_start, evidence_end):
        line = lines[i]
        if not line.startswith("|"):
            continue

        # Split into cells
        cells = line.split("|")
        if len(cells) < 4:
            continue

        # Source is typically the last meaningful cell (3rd column)
        source_cell = cells[3] if len(cells) > 3 else cells[-2]

        # Collect all mentions for this line
        line_mentions = []

        # 1. Trial matching (exact name, with ambiguity handling)
        for trial_name, info in trials.items():
            mentions = find_trial_mentions(source_cell, trial_name)
            if not mentions:
                continue
            for start, end, matched_text in mentions:
                found.append({
                    "trial": trial_name,
                    "matched": matched_text,
                    "pmid": info["pmid"],
                    "citation": info["citation"],
                    "line": i + 1,
                    "type": "trial",
                    "context": source_cell.strip()[:120],
                })
                line_mentions.append((start, end, matched_text, info))

        # 2. Guideline matching (pattern-based)
        for guideline_name, info in guidelines.items():
            mentions = find_guideline_mentions(
                source_cell, guideline_name, info
            )
            if not mentions:
                continue
            for start, end, matched_text in mentions:
                # Check this doesn't overlap with an existing trial mention
                overlaps = False
                for ms, me, _, _ in line_mentions:
                    if start < me and end > ms:
                        overlaps = True
                        break
                if overlaps:
                    continue

                found.append({
                    "trial": guideline_name,
                    "matched": matched_text,
                    "pmid": info["pmid"],
                    "citation": info["citation"],
                    "line": i + 1,
                    "type": "guideline",
                    "context": source_cell.strip()[:120],
                })
                line_mentions.append((start, end, matched_text, info))

        if apply and line_mentions:
            # Sort by position (rightmost first) to preserve offsets
            line_mentions.sort(key=lambda x: x[0], reverse=True)

            # Remove overlapping mentions (keep the longer/earlier one)
            filtered = []
            for mention in line_mentions:
                overlap = False
                for kept in filtered:
                    if mention[0] < kept[1] and mention[1] > kept[0]:
                        overlap = True
                        break
                if not overlap:
                    filtered.append(mention)

            new_cell = source_cell
            for start, end, matched_text, info in filtered:
                link = f"[{matched_text}]({pubmed_url(info['pmid'])})"
                new_cell = new_cell[:start] + link + new_cell[end:]

            cells[3] = new_cell
            modified_lines[i] = "|".join(cells)

    if apply and found:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)

    return {"plan": plan_name, "found": found, "count": len(found)}


def main():
    parser = argparse.ArgumentParser(description="Link landmark trials to PubMed")
    parser.add_argument("files", nargs="*", help="Plan files to process")
    parser.add_argument("--all", action="store_true", help="Process all plans")
    parser.add_argument("--apply", action="store_true", help="Write links to files")
    parser.add_argument("--report", action="store_true", help="Report mode (default)")
    parser.add_argument("--json", metavar="PATH", help="Save results to JSON")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")
    args = parser.parse_args()

    # Default to report mode
    if not args.apply:
        args.report = True

    # Collect files
    if args.all:
        files = sorted(glob.glob(os.path.join(PLANS_DIR, "*.md")))
    elif args.files:
        files = args.files
    else:
        parser.error("Specify plan files or use --all")

    trials, guidelines = load_lookup()
    if not args.quiet:
        print(f"Loaded {len(trials)} trials + {len(guidelines)} guidelines")
        print(f"Processing {len(files)} plan files...")
        if args.apply:
            print("MODE: APPLY (writing links to files)")
        else:
            print("MODE: REPORT (no files modified)")
        print()

    results = []
    total_found = 0
    plans_with_links = 0

    for filepath in files:
        result = process_plan(filepath, trials, guidelines, apply=args.apply)
        results.append(result)
        if result["found"]:
            plans_with_links += 1
            total_found += len(result["found"])
            if not args.quiet:
                print(f"  {result['plan']}: {len(result['found'])} links")
                for item in result["found"]:
                    print(f"    → {item['trial']} → PMID {item['pmid']} ({item['citation']})")

    if not args.quiet:
        print()
        print(f"TOTAL: {total_found} landmark links across {plans_with_links} plans")
        if args.apply:
            print(f"Applied to {plans_with_links} plan files")

    # Save JSON report
    if args.json:
        report = {
            "total_found": total_found,
            "plans_with_links": plans_with_links,
            "mode": "apply" if args.apply else "report",
            "lookup_size": len(trials) + len(guidelines),
            "results": results,
        }
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if not args.quiet:
            print(f"Report saved to {args.json}")


if __name__ == "__main__":
    main()
