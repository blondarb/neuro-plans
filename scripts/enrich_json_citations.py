#!/usr/bin/env python3
"""
Enrich unlinked citations in plans.json with PubMed links.

Operates directly on the iOS plans.json bundle resource. Finds evidence items
whose recommendation field contains citation text but no PubMed URL, then:
  1. Checks landmark_pmids.json for instant matches (no API call)
  2. Classifies remaining citations (author, guideline, trial, skip)
  3. Searches PubMed using multi-strategy approach
  4. Validates every match inline before accepting
  5. Writes results back to plans.json + copies to docs/data/plans.json

Usage:
    python scripts/enrich_json_citations.py                    # Report mode (no changes)
    python scripts/enrich_json_citations.py --apply            # Apply changes
    python scripts/enrich_json_citations.py --apply --json report.json  # Apply + write report
    python scripts/enrich_json_citations.py --batch 1-50       # Only process first 50 unlinked
    python scripts/enrich_json_citations.py --skip-api         # Landmark matching only
    python scripts/enrich_json_citations.py --confidence high  # Only accept high confidence

Requires no external dependencies — uses Python stdlib only.
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Imports from sibling scripts
# ---------------------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).parent))
from verify_citations import (
    search_pubmed,
    fetch_pmid_metadata,
    load_cache,
    save_cache,
    update_cache_from_metadata,
    check_api_connectivity,
    _strip_diacritics,
    _resolve_journal_for_search,
    _score_candidate,
    parse_citation_text,
    validate_pmid_format,
    RATE_LIMIT_DELAY,
    JOURNAL_SEARCH_MAP,
    APIError,
)

from link_unlinked_citations import (
    classify_citation,
    search_for_author_citation,
    search_for_guideline,
    search_for_trial,
    ORG_JOURNAL_MAP,
    TRIAL_JOURNAL_MAP,
)

from validate_enriched_citations import is_clearly_wrong

# ---------------------------------------------------------------------------
# File paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
IOS_PLANS = REPO_ROOT / "ios" / "NeuroPlans" / "NeuroPlans" / "Resources" / "plans.json"
DOCS_PLANS = REPO_ROOT / "docs" / "data" / "plans.json"
LANDMARK_FILE = Path(__file__).parent / "landmark_pmids.json"

# Regex for existing Markdown PubMed links
MD_LINK_RE = re.compile(
    r'\[([^\]]+)\]\(https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?\)'
)


# ---------------------------------------------------------------------------
# Landmark matching (offline — no API calls)
# ---------------------------------------------------------------------------

def load_landmark_pmids() -> dict:
    """Load the landmark_pmids.json file. Returns empty structure if missing."""
    if not LANDMARK_FILE.exists():
        return {"trials": {}, "guidelines": {}}
    try:
        with open(LANDMARK_FILE, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(f"  Warning: Could not load {LANDMARK_FILE}: {e}", file=sys.stderr)
        return {"trials": {}, "guidelines": {}}


def match_landmark(citation_text: str, landmarks: dict) -> Optional[dict]:
    """
    Check if citation_text matches any landmark trial or guideline.

    Returns dict with pmid, citation, source on match, or None.
    """
    text_lower = _strip_diacritics(citation_text).lower()

    # Check trials: case-insensitive name match
    for trial_name, info in landmarks.get("trials", {}).items():
        trial_lower = trial_name.lower()
        if trial_lower in text_lower:
            return {
                "pmid": info["pmid"],
                "landmark_citation": info.get("citation", ""),
                "source": f"landmark:trial:{trial_name}",
            }

    # Check guidelines: use match_patterns if available, else name match
    for guideline_name, info in landmarks.get("guidelines", {}).items():
        patterns = info.get("match_patterns", [guideline_name])
        for pattern in patterns:
            if pattern.lower() in text_lower:
                return {
                    "pmid": info["pmid"],
                    "landmark_citation": info.get("citation", ""),
                    "source": f"landmark:guideline:{guideline_name}",
                }

    return None


# ---------------------------------------------------------------------------
# Collect unlinked citations from plans.json
# ---------------------------------------------------------------------------

def collect_unlinked(data: dict) -> list[dict]:
    """
    Scan all plans in data and return a list of unlinked evidence items.

    Each item is a dict with: plan_id, index, citation_text, evidence_context.
    """
    unlinked = []
    for plan_id, plan in data.items():
        for i, item in enumerate(plan.get("evidence", [])):
            rec = item.get("recommendation", "").strip()
            # Skip if already linked or too short to be a real citation
            if "pubmed.ncbi.nlm.nih.gov" in rec or len(rec) < 5:
                continue
            unlinked.append({
                "plan_id": plan_id,
                "index": i,
                "citation_text": rec,
                "evidence_context": item.get("evidenceLevel", ""),
            })
    return unlinked


def count_evidence_stats(data: dict) -> dict:
    """Count total, linked, and unlinked evidence items across all plans."""
    total = 0
    linked = 0
    for plan in data.values():
        for item in plan.get("evidence", []):
            total += 1
            rec = item.get("recommendation", "")
            if "pubmed.ncbi.nlm.nih.gov" in rec:
                linked += 1
    return {"total": total, "linked": linked, "unlinked": total - linked}


# ---------------------------------------------------------------------------
# Inline validation
# ---------------------------------------------------------------------------

def validate_match(pmid: str, citation_text: str, cache_dict: dict,
                   confidence: str, plan_topic: str = "") -> tuple:
    """
    Run inline validation on a candidate PMID match.

    Returns (accepted: bool, reason: str).

    Checks:
      1. PMID format/year-range lint
      2. Fetches metadata if not cached
      3. Topic validation via is_clearly_wrong()
      4. Confidence threshold (caller handles this separately)
    """
    # Step 1: PMID format and year-range validation
    lint_issues = validate_pmid_format(pmid, citation_text)
    if lint_issues:
        return False, f"PMID lint: {lint_issues[0]}"

    # Step 2: Fetch metadata if not already in cache
    try:
        cached_pmids = cache_dict.get("pmids", {})
        if pmid in cached_pmids:
            meta = cached_pmids[pmid]
            article_title = meta.get("title", "")
        else:
            meta_result = fetch_pmid_metadata([pmid], cache_dict)
            m = meta_result.get(pmid, {})
            if not m.get("exists"):
                return False, "PMID not found in PubMed"
            article_title = m.get("title", "")
            # Update cache with this metadata
            update_cache_from_metadata(cache_dict, meta_result)
    except APIError as e:
        return False, f"API error fetching metadata: {e}"

    # Step 3: Topic validation
    if article_title:
        wrong, reason = is_clearly_wrong(article_title, citation_text,
                                          plan_topic=plan_topic)
        if wrong:
            return False, f"Topic mismatch: {reason}"

    return True, "passed"


# ---------------------------------------------------------------------------
# Enrichment pipeline
# ---------------------------------------------------------------------------

def enrich_citations(
    data: dict,
    landmarks: dict,
    cache: dict,
    batch_range: Optional[tuple] = None,
    min_confidence: str = "medium",
    skip_api: bool = False,
    quiet: bool = False,
    apply: bool = False,
) -> dict:
    """
    Main enrichment pipeline. Processes unlinked citations and returns a report.

    Parameters:
        data            Plans dict (modified in-place if apply=True)
        landmarks       Landmark PMIDs dict
        cache           PMID cache dict
        batch_range     (start, end) 1-indexed range of unlinked citations to process
        min_confidence  Minimum confidence to accept: "high" or "medium"
        skip_api        If True, only do landmark matching (no PubMed API)
        quiet           Suppress per-citation output
        apply           If True, write links into data dict

    Returns report dict with counts and per-citation details.
    """
    # Collect all unlinked items
    unlinked = collect_unlinked(data)
    stats_before = count_evidence_stats(data)

    # Apply batch range filter
    if batch_range:
        start_idx, end_idx = batch_range
        # Convert 1-indexed to 0-indexed
        unlinked_to_process = unlinked[start_idx - 1:end_idx]
    else:
        unlinked_to_process = unlinked

    # Confidence levels for comparison
    conf_rank = {"high": 2, "medium": 1, "low": 0, "none": -1}
    min_conf_rank = conf_rank.get(min_confidence, 1)

    # Counters
    landmark_matches = 0
    api_matches = 0
    api_high = 0
    api_medium = 0
    rejected_validation = 0
    not_found = 0
    skipped_not_searchable = 0
    links_added = 0

    # Per-citation details for JSON report
    details = []

    total_to_process = len(unlinked_to_process)
    if not quiet:
        print(f"\n  Processing {total_to_process} unlinked citations...\n")

    for idx, item in enumerate(unlinked_to_process, 1):
        plan_id = item["plan_id"]
        ev_index = item["index"]
        citation_text = item["citation_text"]
        evidence_context = item["evidence_context"]

        # Progress indicator
        if not quiet and idx % 10 == 0:
            print(f"  [{idx}/{total_to_process}] ...", flush=True)
        elif not quiet:
            sys.stdout.write(".")
            sys.stdout.flush()

        detail = {
            "plan_id": plan_id,
            "index": ev_index,
            "citation_text": citation_text[:120],
            "result": None,
            "pmid": None,
            "confidence": "none",
            "method": None,
            "rejected_reason": None,
        }

        # ---- Step 2: Check landmark PMIDs first (no API) ----
        lm = match_landmark(citation_text, landmarks)
        if lm:
            pmid = lm["pmid"]
            # Validate even landmark matches
            accepted, reason = validate_match(
                pmid, citation_text, cache, "high", plan_topic=plan_id
            )
            if accepted:
                detail["result"] = "landmark"
                detail["pmid"] = pmid
                detail["confidence"] = "high"
                detail["method"] = lm["source"]
                landmark_matches += 1

                if apply:
                    evidence_list = data[plan_id]["evidence"]
                    evidence_list[ev_index]["recommendation"] = (
                        f"[{citation_text}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)"
                    )
                    links_added += 1

                if not quiet:
                    sys.stdout.write("+")
                    sys.stdout.flush()

                details.append(detail)
                continue
            else:
                detail["rejected_reason"] = reason
                if not quiet:
                    sys.stdout.write("x")
                    sys.stdout.flush()
                # Fall through to API search

        # ---- Step 3: Skip API if --skip-api ----
        if skip_api:
            if lm:
                # Landmark matched but validation failed
                detail["result"] = "rejected"
                rejected_validation += 1
            else:
                detail["result"] = "skipped_no_api"
                not_found += 1
            details.append(detail)
            continue

        # ---- Step 3: Classify and search PubMed ----
        category = classify_citation(citation_text)
        detail["category"] = category

        if category == "skip":
            detail["result"] = "skipped"
            skipped_not_searchable += 1
            details.append(detail)
            continue

        # Search PubMed based on category
        search_result = None
        try:
            if category == "trial":
                search_result = search_for_trial(
                    citation_text, cache,
                    evidence_context=evidence_context,
                    plan_topic=plan_id,
                )
            elif category == "guideline":
                search_result = search_for_guideline(
                    citation_text, cache,
                    evidence_context=evidence_context,
                    plan_topic=plan_id,
                )
            elif category == "author":
                search_result = search_for_author_citation(
                    citation_text, cache,
                    evidence_context=evidence_context,
                    plan_topic=plan_id,
                )
        except APIError as e:
            detail["result"] = "api_error"
            detail["rejected_reason"] = str(e)
            not_found += 1
            details.append(detail)
            if not quiet:
                sys.stdout.write("E")
                sys.stdout.flush()
            continue
        except Exception as e:
            detail["result"] = "error"
            detail["rejected_reason"] = str(e)
            not_found += 1
            details.append(detail)
            if not quiet:
                sys.stdout.write("E")
                sys.stdout.flush()
            continue

        if not search_result or not search_result.get("pmid"):
            detail["result"] = "not_found"
            detail["method"] = search_result.get("method", "") if search_result else ""
            not_found += 1
            details.append(detail)
            if not quiet:
                sys.stdout.write("-")
                sys.stdout.flush()
            continue

        pmid = search_result["pmid"]
        confidence = search_result.get("confidence", "none")

        # ---- Step 4: Inline validation ----

        # 4a. Confidence threshold
        if conf_rank.get(confidence, -1) < min_conf_rank:
            detail["result"] = "rejected_confidence"
            detail["pmid"] = pmid
            detail["confidence"] = confidence
            detail["method"] = search_result.get("method", "")
            detail["rejected_reason"] = (
                f"Confidence '{confidence}' below threshold '{min_confidence}'"
            )
            rejected_validation += 1
            details.append(detail)
            if not quiet:
                sys.stdout.write("c")
                sys.stdout.flush()
            continue

        # 4b. Validate PMID format, metadata, and topic
        accepted, reason = validate_match(pmid, citation_text, cache, confidence,
                                          plan_topic=plan_id)
        if not accepted:
            detail["result"] = "rejected_validation"
            detail["pmid"] = pmid
            detail["confidence"] = confidence
            detail["method"] = search_result.get("method", "")
            detail["rejected_reason"] = reason
            rejected_validation += 1
            details.append(detail)
            if not quiet:
                sys.stdout.write("x")
                sys.stdout.flush()
            continue

        # ---- Match accepted ----
        detail["result"] = "matched"
        detail["pmid"] = pmid
        detail["confidence"] = confidence
        detail["method"] = search_result.get("method", "")
        detail["pubmed_title"] = search_result.get("pubmed_title", "")[:120]
        api_matches += 1
        if confidence == "high":
            api_high += 1
        else:
            api_medium += 1

        if apply:
            evidence_list = data[plan_id]["evidence"]
            evidence_list[ev_index]["recommendation"] = (
                f"[{citation_text}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)"
            )
            links_added += 1

        if not quiet:
            sys.stdout.write("+" if confidence == "high" else "~")
            sys.stdout.flush()

        details.append(detail)

    if not quiet:
        print()  # End progress line

    stats_after = count_evidence_stats(data) if apply else stats_before

    report = {
        "stats_before": stats_before,
        "stats_after": stats_after,
        "total_unlinked": len(unlinked),
        "processed": total_to_process,
        "landmark_matches": landmark_matches,
        "api_matches": api_matches,
        "api_high": api_high,
        "api_medium": api_medium,
        "rejected_validation": rejected_validation,
        "not_found": not_found,
        "skipped_not_searchable": skipped_not_searchable,
        "links_added": links_added,
        "details": details,
    }

    return report


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_report(report: dict, apply: bool = False):
    """Print a human-readable summary report."""
    before = report["stats_before"]
    total_ev = before["total"]
    already_linked = before["linked"]
    total_unlinked = report["total_unlinked"]
    processed = report["processed"]

    new_links = report["links_added"]
    after_linked = already_linked + new_links if apply else already_linked
    after_pct = (after_linked / total_ev * 100) if total_ev else 0

    print()
    print("=" * 60)
    print("  Citation Enrichment Report")
    print("=" * 60)
    print()
    print(f"  Total evidence items:     {total_ev:,}")
    print(f"  Already linked:           {already_linked:,}")
    print(f"  Unlinked to process:      {processed:,}")
    if processed < total_unlinked:
        print(f"  (of {total_unlinked:,} total unlinked)")
    print()
    print(f"  Landmark matches:         {report['landmark_matches']}")
    print(f"  PubMed API matches:       {report['api_matches']}")
    print(f"  - High confidence:        {report['api_high']}")
    print(f"  - Medium confidence:      {report['api_medium']}")
    print(f"  Rejected (validation):    {report['rejected_validation']}")
    print(f"  Not found:                {report['not_found']}")
    print(f"  Skipped (not searchable): {report['skipped_not_searchable']}")
    print()
    if apply:
        print(f"  New links added:          {new_links}")
        print(f"  Total linked (after):     {after_linked:,} ({after_pct:.1f}%)")
    else:
        total_potential = (
            report["landmark_matches"] + report["api_matches"]
        )
        print(f"  Would add links:          {total_potential}")
        potential_linked = already_linked + total_potential
        potential_pct = (potential_linked / total_ev * 100) if total_ev else 0
        print(f"  Total linked (potential): {potential_linked:,} ({potential_pct:.1f}%)")
    print()
    print("=" * 60)


def print_detail_table(report: dict, quiet: bool = False):
    """Print per-citation details for non-quiet mode."""
    if quiet:
        return

    details = report.get("details", [])
    # Show rejected and matched items
    matched = [d for d in details if d["result"] in ("matched", "landmark")]
    rejected = [d for d in details if d["result"] and "rejected" in d["result"]]

    if matched:
        print(f"\n  ACCEPTED MATCHES ({len(matched)}):")
        for d in matched[:50]:
            src = "LM" if d["result"] == "landmark" else d["confidence"][:3].upper()
            print(f"    [{d['plan_id']}] PMID {d['pmid']} ({src}): "
                  f"{d['citation_text'][:80]}")
        if len(matched) > 50:
            print(f"    ... and {len(matched) - 50} more")

    if rejected:
        print(f"\n  REJECTED ({len(rejected)}):")
        for d in rejected[:30]:
            reason = d.get("rejected_reason", "unknown")[:60]
            print(f"    [{d['plan_id']}] {reason}: "
                  f"{d['citation_text'][:70]}")
        if len(rejected) > 30:
            print(f"    ... and {len(rejected) - 30} more")


def write_json_report(report: dict, output_path: str):
    """Write a detailed JSON report file."""
    json_report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total_evidence": report["stats_before"]["total"],
            "already_linked": report["stats_before"]["linked"],
            "unlinked_total": report["total_unlinked"],
            "processed": report["processed"],
            "landmark_matches": report["landmark_matches"],
            "api_matches": report["api_matches"],
            "api_high": report["api_high"],
            "api_medium": report["api_medium"],
            "rejected_validation": report["rejected_validation"],
            "not_found": report["not_found"],
            "skipped_not_searchable": report["skipped_not_searchable"],
            "links_added": report["links_added"],
        },
        "citations": report.get("details", []),
    }

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(json_report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n  JSON report written to {output_path}")


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

def load_plans() -> dict:
    """Load plans.json from the iOS bundle resource path."""
    if not IOS_PLANS.exists():
        print(f"Error: {IOS_PLANS} not found", file=sys.stderr)
        sys.exit(1)
    with open(IOS_PLANS, encoding="utf-8") as f:
        return json.load(f)


def save_plans(data: dict):
    """Write plans.json to both iOS and docs locations."""
    # Write to iOS bundle
    IOS_PLANS.parent.mkdir(parents=True, exist_ok=True)
    with open(IOS_PLANS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Written to {IOS_PLANS}")

    # Copy to docs/data/plans.json
    if DOCS_PLANS.parent.exists():
        with open(DOCS_PLANS, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Written to {DOCS_PLANS}")


def parse_batch_range(batch_str: str) -> tuple:
    """Parse a batch range string like '1-50' into (start, end) tuple."""
    try:
        parts = batch_str.split("-")
        if len(parts) == 2:
            start = int(parts[0])
            end = int(parts[1])
            if start < 1 or end < start:
                raise ValueError
            return (start, end)
        else:
            raise ValueError
    except ValueError:
        print(f"Error: --batch must be N-M (e.g., 1-50), got '{batch_str}'",
              file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Enrich unlinked citations in plans.json with PubMed links",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Write changes to plans.json (default is report-only)",
    )
    parser.add_argument(
        "--json", metavar="FILE",
        help="Write detailed JSON report to FILE",
    )
    parser.add_argument(
        "--batch", metavar="N-M",
        help="Only process unlinked citations N through M (1-indexed)",
    )
    parser.add_argument(
        "--confidence", choices=["high", "medium"], default="medium",
        help="Minimum confidence to accept (default: medium)",
    )
    parser.add_argument(
        "--skip-api", action="store_true",
        help="Only do landmark matching, skip PubMed API searches",
    )
    parser.add_argument(
        "--quiet", "-q", action="store_true",
        help="Suppress per-citation output",
    )

    args = parser.parse_args()

    # Parse batch range if provided
    batch_range = None
    if args.batch:
        batch_range = parse_batch_range(args.batch)

    # Load plans.json
    print("\nLoading plans.json...")
    data = load_plans()
    stats = count_evidence_stats(data)
    print(f"  Loaded {len(data)} plans, {stats['total']:,} evidence items")
    print(f"  Already linked: {stats['linked']:,} ({stats['linked']/stats['total']*100:.1f}%)")
    print(f"  Unlinked: {stats['unlinked']:,}")

    # Load landmark PMIDs
    landmarks = load_landmark_pmids()
    trial_count = len(landmarks.get("trials", {}))
    guideline_count = len(landmarks.get("guidelines", {}))
    print(f"  Landmark PMIDs: {trial_count} trials, {guideline_count} guidelines")

    # Load PMID cache
    cache = load_cache()
    print(f"  PMID cache: {len(cache.get('pmids', {}))} entries")

    # API connectivity check (unless --skip-api)
    if not args.skip_api:
        print("\nChecking PubMed API connectivity...")
        if not check_api_connectivity():
            print(
                "\n  PubMed API is not reachable.\n"
                "  Use --skip-api for landmark-only matching,\n"
                "  or check your network connection.",
                file=sys.stderr,
            )
            sys.exit(1)
        print("  PubMed API is reachable")

    # Run enrichment pipeline
    mode_label = "APPLYING" if args.apply else "REPORT ONLY"
    batch_label = f" (batch {args.batch})" if args.batch else ""
    conf_label = f" (min confidence: {args.confidence})"

    print(f"\n{'='*60}")
    print(f"  {mode_label}{batch_label}{conf_label}")
    print(f"{'='*60}")

    report = enrich_citations(
        data=data,
        landmarks=landmarks,
        cache=cache,
        batch_range=batch_range,
        min_confidence=args.confidence,
        skip_api=args.skip_api,
        quiet=args.quiet,
        apply=args.apply,
    )

    # Print summary report
    print_report(report, apply=args.apply)

    # Print detail table (unless quiet)
    if not args.quiet:
        print_detail_table(report, quiet=args.quiet)

    # Save results
    if args.apply and report["links_added"] > 0:
        print("\nSaving updated plans.json...")
        save_plans(data)

    # Save cache
    save_cache(cache)
    if not args.quiet:
        print(f"  Cache saved ({len(cache.get('pmids', {}))} entries)")

    # Write JSON report
    if args.json:
        write_json_report(report, args.json)

    # Final summary line
    if args.apply:
        after = report["stats_after"]
        pct = (after["linked"] / after["total"] * 100) if after["total"] else 0
        print(f"\n  Final: {after['linked']:,}/{after['total']:,} "
              f"citations linked ({pct:.1f}%)")
    else:
        potential = report["landmark_matches"] + report["api_matches"]
        if potential > 0:
            print(f"\n  Run with --apply to add {potential} links.")


if __name__ == "__main__":
    main()
