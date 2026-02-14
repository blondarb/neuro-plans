#!/usr/bin/env python3
"""
Guideline freshness checker for neuro-plans.

Checks whether guidelines and trials in landmark_pmids.json have been
superseded, retracted, or have newer versions available. Uses PubMed
E-utilities (free, no API key needed) for all lookups.

Designed to run monthly to keep a paid subscription product current.

Features:
  - PMID health check (retraction/erratum detection)
  - Newer version search (PubMed ESearch by org + topic)
  - Age-tier flagging (guidelines >5 years old flagged for periodic review)
  - Plan cross-referencing (shows which plan files cite each guideline)

Usage:
    python scripts/check_guideline_freshness.py
    python scripts/check_guideline_freshness.py --cache
    python scripts/check_guideline_freshness.py --guidelines-only --json report.json
    python scripts/check_guideline_freshness.py --quiet

Modes:
    (default)         Check all entries in landmark_pmids.json
    --guidelines-only Check only guidelines (skip trials)
    --trials-only     Check only trials (skip guidelines)
    --cache           Use/update local PMID cache (docs/data/pmid-cache.json)
    --json FILE       Write full report to JSON
    --markdown FILE   Write human-readable summary
    --quiet           Only show flagged items
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
LOOKUP_FILE = SCRIPT_DIR / "landmark_pmids.json"
PLANS_DIR = SCRIPT_DIR.parent / "docs" / "plans"
CACHE_FILE = SCRIPT_DIR.parent / "docs" / "data" / "pmid-cache.json"

# Age-tier thresholds (years since publication)
AGE_TIER_REVIEW = 5     # ≥5 years old → "review recommended"
AGE_TIER_STALE = 8      # ≥8 years old → "aging — prioritize review"

ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# NCBI requires tool + email for polite access. Rate limit: 3 req/sec.
API_PARAMS = {
    "tool": "neuro-plans-freshness-checker",
    "email": "neuro-plans@example.com",
}

RATE_LIMIT_DELAY = 0.5  # seconds between API calls
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2


# ---------------------------------------------------------------------------
# Organization → PubMed Corporate Author mapping
# Used for "newer version" searches
# ---------------------------------------------------------------------------

ORG_TO_CORPORATE_AUTHOR = {
    "AHA/ASA": '"American Heart Association"[Corporate Author]',
    "AHA": '"American Heart Association"[Corporate Author]',
    "AAN": '"American Academy of Neurology"[Corporate Author]',
    "IDSA": '"Infectious Diseases Society of America"[Corporate Author]',
    "NCS": '"Neurocritical Care Society"[Affiliation]',
    "AES": '"American Epilepsy Society"[Corporate Author]',
    "EFNS": '"European Federation of Neurological Societies"[Corporate Author]',
    "EFNS/PNS": '"European Federation of Neurological Societies"[Corporate Author]',
    "EAN": '"European Academy of Neurology"[Corporate Author]',
    "ESO": '"European Stroke Organisation"[Corporate Author]',
    "WHO": '"World Health Organization"[Corporate Author]',
    "CDC": '"Centers for Disease Control and Prevention"[Corporate Author]',
    "ACOG": '"American College of Obstetricians and Gynecologists"[Corporate Author]',
    "AASLD": '"American Association for the Study of Liver Diseases"[Corporate Author]',
    "EASL": '"European Association for the Study of the Liver"[Corporate Author]',
    "AAOS": '"American Academy of Orthopaedic Surgeons"[Corporate Author]',
    "ASAM": '"American Society of Addiction Medicine"[Corporate Author]',
    "AANEM": '"American Association of Neuromuscular"[Affiliation]',
    "MAGNIMS": '"MAGNIMS"[Affiliation]',
    "NASS": '"North American Spine Society"[Affiliation]',
}

# Topic keywords to extract from guideline entry names
# Maps common short terms to PubMed search terms
TOPIC_KEYWORDS = {
    "stroke": "stroke",
    "SAH": "subarachnoid hemorrhage",
    "ICH": "intracerebral hemorrhage",
    "CVT": "cerebral venous thrombosis",
    "seizure": "seizure",
    "epilepsy": "epilepsy",
    "status epilepticus": "status epilepticus",
    "tremor": "tremor",
    "trigeminal": "trigeminal neuralgia",
    "meningitis": "meningitis",
    "encephalitis": "encephalitis",
    "neuropathy": "neuropathy",
    "Bell": "Bell palsy",
    "dementia": "dementia",
    "MCI": "mild cognitive impairment",
    "MS ": "multiple sclerosis",
    "migraine": "migraine",
    "ALS": "amyotrophic lateral sclerosis",
    "dystonia": "dystonia",
    "Tourette": "Tourette",
    "Wilson": "Wilson disease",
    "Lyme": "Lyme disease",
    "brain death": "brain death",
    "concussion": "concussion",
    "radiculopathy": "radiculopathy",
    "carpal tunnel": "carpal tunnel",
    "alcohol withdrawal": "alcohol withdrawal",
    "eclampsia": "preeclampsia",
    "endocarditis": "endocarditis",
    "GBS": "Guillain-Barre",
    "SUDEP": "sudden unexpected death epilepsy",
    "myotonic": "myotonic dystrophy",
    "MMN": "multifocal motor neuropathy",
    "CIDP": "chronic inflammatory demyelinating",
    "lumbar stenosis": "lumbar stenosis",
    "aspergillosis": "aspergillosis",
    "coccidioidomycosis": "coccidioidomycosis",
    "neurocysticercosis": "neurocysticercosis",
    "STI": "sexually transmitted",
    "TB": "tuberculosis",
    "neuroprognostication": "neuroprognostication",
    "rehab": "rehabilitation",
}


# ---------------------------------------------------------------------------
# API helpers (matching verify_citations.py patterns)
# ---------------------------------------------------------------------------

class APIError(Exception):
    """Raised when the PubMed API is unreachable."""
    pass


def _api_get(url: str, params: dict) -> dict:
    """Make a GET request to NCBI E-utilities with retry logic."""
    all_params = {**API_PARAMS, **params}
    query = "&".join(
        f"{k}={urllib.request.quote(str(v))}" for k, v in all_params.items()
    )
    full_url = f"{url}?{query}"

    last_error = None
    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # Rate limited — back off more aggressively
                wait = RETRY_BACKOFF_BASE ** (attempt + 2)
                time.sleep(wait)
                last_error = e
                continue
            last_error = e
        except (urllib.error.URLError, TimeoutError) as e:
            last_error = e

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_BACKOFF_BASE ** (attempt + 1))

    raise APIError(f"PubMed API failed after {MAX_RETRIES} retries: {last_error}")


def esummary_batch(pmids) -> dict:
    """
    Look up metadata for a batch of PMIDs via ESummary.
    Returns dict of {pmid: metadata_dict}.
    """
    results = {}
    # ESummary supports up to 200 IDs per request
    for i in range(0, len(pmids), 200):
        batch = pmids[i:i + 200]
        data = _api_get(ESUMMARY_URL, {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "json",
        })
        time.sleep(RATE_LIMIT_DELAY)

        result_data = data.get("result", {})
        for pmid in batch:
            meta = result_data.get(pmid, {})
            if "error" in meta:
                results[pmid] = {"exists": False, "error": meta["error"]}
            else:
                results[pmid] = {
                    "exists": True,
                    "title": meta.get("title", ""),
                    "first_author": meta.get("sortfirstauthor", ""),
                    "journal_abbrev": meta.get("source", ""),
                    "year": meta.get("pubdate", "")[:4],
                    "pubtype": meta.get("pubtype", []),
                    "doi": meta.get("elocationid", ""),
                }

    return results


def esearch(query: str, retmax: int = 10):
    """Search PubMed and return list of PMIDs."""
    try:
        data = _api_get(ESEARCH_URL, {
            "db": "pubmed",
            "term": query,
            "retmax": str(retmax),
            "retmode": "json",
        })
        time.sleep(RATE_LIMIT_DELAY)
        return data.get("esearchresult", {}).get("idlist", [])
    except APIError:
        return []


# ---------------------------------------------------------------------------
# Cache helpers (same format as verify_citations.py)
# ---------------------------------------------------------------------------

def load_cache() -> dict:
    """Load the verified PMID cache from disk."""
    if CACHE_FILE.exists():
        try:
            data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "pmids" in data:
                return data
        except (json.JSONDecodeError, ValueError):
            pass
    return {"version": 1, "pmids": {}}


def save_cache(cache: dict):
    """Save the verified PMID cache to disk."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Core freshness logic
# ---------------------------------------------------------------------------

def load_landmark_entries() -> tuple[dict, dict]:
    """Load trials and guidelines from landmark_pmids.json."""
    with open(LOOKUP_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("trials", {}), data.get("guidelines", {})


def extract_year(citation: str):
    """Extract a 4-digit year from citation text."""
    match = re.search(r'\b((?:19|20)\d{2})\b', citation)
    return int(match.group(1)) if match else None


def detect_org(entry_name: str):
    """Detect which organization issued this guideline from the entry name."""
    for org_key in sorted(ORG_TO_CORPORATE_AUTHOR.keys(), key=len, reverse=True):
        if org_key in entry_name:
            return org_key
    return None


def extract_topic(entry_name: str):
    """Extract a clinical topic from a guideline entry name."""
    for keyword, search_term in TOPIC_KEYWORDS.items():
        if keyword.lower() in entry_name.lower():
            return search_term
    return None


def classify_age_tier(pub_year: int, current_year: int) -> str:
    """Classify a guideline by age into review tiers."""
    if pub_year is None:
        return "unknown"
    age = current_year - pub_year
    if age >= AGE_TIER_STALE:
        return "aging"
    elif age >= AGE_TIER_REVIEW:
        return "review_recommended"
    return "current"


def scan_plan_references() -> dict:
    """
    Scan all plan .md files and build a map of which plans reference
    each guideline/trial from landmark_pmids.json.

    Returns dict: {entry_name: [list of plan file stems]}
    """
    if not PLANS_DIR.exists():
        return {}

    # Load landmark entries for matching
    with open(LOOKUP_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Build search patterns: entry_name → list of strings to search for
    search_map = {}
    for section in ("trials", "guidelines"):
        for name, info in data.get(section, {}).items():
            patterns = [name]
            patterns.extend(info.get("match_patterns", []))
            # Also search for PMID in link form
            pmid = info.get("pmid", "")
            if pmid:
                patterns.append(pmid)
            search_map[name] = patterns

    # Scan plan files
    ref_map = {name: [] for name in search_map}
    plan_files = sorted(PLANS_DIR.glob("*.md"))
    for plan_path in plan_files:
        try:
            content = plan_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        plan_stem = plan_path.stem
        content_lower = content.lower()

        for name, patterns in search_map.items():
            for pattern in patterns:
                if pattern.lower() in content_lower:
                    if plan_stem not in ref_map[name]:
                        ref_map[name].append(plan_stem)
                    break  # found in this plan, move to next entry

    return ref_map


def check_pmid_health(pmid: str, metadata: dict) -> dict:
    """
    Check a single PMID's health status.
    Returns a status dict with retraction/erratum info.
    """
    if not metadata.get("exists"):
        return {
            "status": "not_found",
            "detail": metadata.get("error", "PMID not found in PubMed"),
        }

    pubtypes = [pt.lower() for pt in metadata.get("pubtype", [])]
    issues = []

    if any("retract" in pt for pt in pubtypes):
        issues.append("retracted")
    if any("errat" in pt for pt in pubtypes):
        issues.append("has_erratum")

    if issues:
        return {"status": "flagged", "detail": "; ".join(issues)}

    return {"status": "ok"}


def search_newer_version(
    entry_name: str, entry_info: dict, current_year: int
):
    """
    Search PubMed for a newer version of a guideline.
    Returns candidate info dict if found, else None.
    """
    org = detect_org(entry_name)
    topic = extract_topic(entry_name)
    pub_year = extract_year(entry_info.get("citation", ""))

    if not org or not topic or not pub_year:
        return None

    corporate_author = ORG_TO_CORPORATE_AUTHOR.get(org, "")
    if not corporate_author:
        return None

    # Search for newer publications from same org on same topic
    # Include "guideline" OR "practice parameter" in title
    query = (
        f'{corporate_author} AND "{topic}"[Title] AND '
        f'("guideline"[Title] OR "practice parameter"[Title] OR '
        f'"practice guideline"[Title] OR "clinical practice"[Title]) AND '
        f'{pub_year + 1}:{current_year}[Date - Publication]'
    )

    pmids = esearch(query, retmax=5)
    if not pmids:
        return None

    # Get metadata for candidates
    candidates = esummary_batch(pmids)

    # Filter to actual guidelines (not commentaries, letters, etc.)
    guideline_types = {"guideline", "practice guideline", "consensus development conference"}
    for candidate_pmid, meta in candidates.items():
        if not meta.get("exists"):
            continue

        # Skip if it's the same PMID we already have
        if candidate_pmid == entry_info.get("pmid"):
            continue

        title = meta.get("title", "").lower()
        pubtypes = [pt.lower() for pt in meta.get("pubtype", [])]

        # Check if it looks like a guideline (by pub type or title)
        is_guideline = (
            any(gt in pt for pt in pubtypes for gt in guideline_types)
            or "guideline" in title
            or "practice parameter" in title
        )

        if is_guideline:
            return {
                "pmid": candidate_pmid,
                "title": meta.get("title", ""),
                "year": meta.get("year", ""),
                "journal": meta.get("journal_abbrev", ""),
                "first_author": meta.get("first_author", ""),
            }

    return None


def run_freshness_check(
    trials: dict,
    guidelines: dict,
    check_trials: bool = True,
    check_guidelines: bool = True,
    use_cache: bool = False,
    quiet: bool = False,
) -> dict:
    """
    Run the full freshness check.
    Returns a report dict with summary and per-entry results.
    """
    current_year = datetime.now().year
    cache = load_cache() if use_cache else {"version": 1, "pmids": {}}
    entries = []

    # Collect all entries to check
    if check_guidelines:
        for name, info in guidelines.items():
            entries.append(("guideline", name, info))
    if check_trials:
        for name, info in trials.items():
            entries.append(("trial", name, info))

    # Scan plan files for cross-references
    if not quiet:
        print("Scanning plan files for guideline references...")
    plan_refs = scan_plan_references()

    if not quiet:
        print(f"Checking {len(entries)} entries ({sum(1 for e in entries if e[0] == 'guideline')} guidelines, "
              f"{sum(1 for e in entries if e[0] == 'trial')} trials)")
        print()

    # Phase 1: PMID health check (batch)
    all_pmids = list(set(info["pmid"] for _, _, info in entries))
    uncached = [p for p in all_pmids if p not in cache.get("pmids", {})]

    if not quiet:
        print(f"Phase 1: PMID health check ({len(all_pmids)} unique PMIDs, "
              f"{len(all_pmids) - len(uncached)} cached)")

    metadata = {}
    if uncached:
        try:
            metadata = esummary_batch(uncached)
        except APIError as e:
            print(f"  ✖ {e}", file=sys.stderr)
            return {"error": str(e)}

    # Merge cache into metadata
    for pmid in all_pmids:
        if pmid in cache.get("pmids", {}):
            cached = cache["pmids"][pmid]
            metadata[pmid] = {
                "exists": True,
                "title": cached.get("title", ""),
                "first_author": cached.get("first_author", ""),
                "journal_abbrev": cached.get("journal_abbrev", ""),
                "year": cached.get("year", ""),
                "pubtype": [],  # cache doesn't store pubtypes
            }

    # Update cache with new lookups
    if use_cache and metadata:
        for pmid, meta in metadata.items():
            if meta.get("exists") and pmid not in cache["pmids"]:
                cache["pmids"][pmid] = {
                    "title": meta.get("title", ""),
                    "first_author": meta.get("first_author", ""),
                    "journal_abbrev": meta.get("journal_abbrev", ""),
                    "year": meta.get("year", ""),
                    "verified_date": time.strftime("%Y-%m-%d"),
                }
        save_cache(cache)

    # Phase 2: Newer version search (guidelines only)
    results = []
    stats = {
        "total_checked": len(entries),
        "current": 0,
        "flagged_newer_available": 0,
        "flagged_health": 0,
        "not_found": 0,
        "skipped_no_search": 0,
        "aging_guidelines": 0,
        "review_recommended_guidelines": 0,
    }

    guideline_entries = [(t, n, i) for t, n, i in entries if t == "guideline"]
    trial_entries = [(t, n, i) for t, n, i in entries if t == "trial"]

    if guideline_entries and not quiet:
        print(f"\nPhase 2: Searching for newer guideline versions "
              f"({len(guideline_entries)} guidelines)...")

    for entry_type, name, info in entries:
        pmid = info["pmid"]
        meta = metadata.get(pmid, {})
        health = check_pmid_health(pmid, meta)
        pub_year = extract_year(info.get("citation", ""))
        age_tier = classify_age_tier(pub_year, current_year) if entry_type == "guideline" else None
        affected_plans = plan_refs.get(name, [])

        entry_result = {
            "name": name,
            "type": entry_type,
            "pmid": pmid,
            "citation": info.get("citation", ""),
            "year": pub_year,
            "health": health["status"],
            "age_tier": age_tier,
            "affected_plans": affected_plans,
        }

        # Track age tier stats for guidelines
        if entry_type == "guideline" and age_tier == "aging":
            stats["aging_guidelines"] += 1
        elif entry_type == "guideline" and age_tier == "review_recommended":
            stats["review_recommended_guidelines"] += 1

        if health["status"] == "not_found":
            entry_result["status"] = "error"
            entry_result["detail"] = health["detail"]
            stats["not_found"] += 1
            if not quiet:
                print(f"  ✖ {name}: PMID {pmid} not found")
        elif health["status"] == "flagged":
            entry_result["status"] = "flagged_health"
            entry_result["detail"] = health["detail"]
            stats["flagged_health"] += 1
            if not quiet:
                print(f"  ⚠ {name}: {health['detail']}")
        else:
            # Only search for newer versions of guidelines, not trials
            if entry_type == "guideline":
                newer = search_newer_version(name, info, current_year)
                if newer:
                    entry_result["status"] = "newer_available"
                    entry_result["newer_candidate"] = newer
                    stats["flagged_newer_available"] += 1
                    if not quiet:
                        print(f"  🔄 {name} ({pub_year}): "
                              f"newer version found → PMID {newer['pmid']} "
                              f"({newer['year']})")
                else:
                    org = detect_org(name)
                    topic = extract_topic(name)
                    if not org or not topic:
                        entry_result["status"] = "current"
                        entry_result["note"] = "no search performed (missing org or topic)"
                        stats["skipped_no_search"] += 1
                    else:
                        entry_result["status"] = "current"
                        stats["current"] += 1
            else:
                # Trials: just health check, no newer version search
                entry_result["status"] = "current"
                stats["current"] += 1

        results.append(entry_result)

    report = {
        "run_date": datetime.now().strftime("%Y-%m-%d"),
        "summary": stats,
        "entries": results,
    }

    return report


def format_markdown_report(report: dict) -> str:
    """Format the freshness report as a human-readable markdown document."""
    lines = []
    lines.append("# Guideline Freshness Report")
    lines.append(f"\n**Run date:** {report['run_date']}")

    s = report["summary"]
    lines.append("\n## Summary\n")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total checked | {s['total_checked']} |")
    lines.append(f"| Current | {s['current']} |")
    lines.append(f"| Newer version available | {s['flagged_newer_available']} |")
    lines.append(f"| Health issues (retracted/erratum) | {s['flagged_health']} |")
    lines.append(f"| PMID not found | {s['not_found']} |")
    lines.append(f"| Skipped (no org/topic match) | {s['skipped_no_search']} |")
    lines.append(f"| Guidelines aging (≥{AGE_TIER_STALE}yr, no newer found) | {s['aging_guidelines']} |")
    lines.append(f"| Guidelines for review (≥{AGE_TIER_REVIEW}yr) | {s['review_recommended_guidelines']} |")

    # Show flagged items (newer available, health issues)
    flagged = [e for e in report["entries"]
               if e["status"] in ("newer_available", "flagged_health", "error")]

    if flagged:
        lines.append("\n## ⚠ Items Requiring Review\n")
        for entry in flagged:
            status_icon = {
                "newer_available": "🔄",
                "flagged_health": "⚠️",
                "error": "✖",
            }.get(entry["status"], "?")

            lines.append(f"### {status_icon} {entry['name']}")
            lines.append(f"- **Type:** {entry['type']}")
            lines.append(f"- **Current PMID:** {entry['pmid']}")
            lines.append(f"- **Citation:** {entry.get('citation', '')}")
            lines.append(f"- **Year:** {entry.get('year', 'unknown')}")
            lines.append(f"- **Status:** {entry['status']}")

            if entry.get("newer_candidate"):
                nc = entry["newer_candidate"]
                lines.append(f"- **Newer candidate:** PMID {nc['pmid']} ({nc.get('year', '?')})")
                lines.append(f"  - Title: {nc.get('title', '')}")
                lines.append(f"  - Journal: {nc.get('journal', '')}")
                lines.append(f"  - PubMed: https://pubmed.ncbi.nlm.nih.gov/{nc['pmid']}/")

            if entry.get("detail"):
                lines.append(f"- **Detail:** {entry['detail']}")

            plans = entry.get("affected_plans", [])
            if plans:
                lines.append(f"- **Affected plans ({len(plans)}):** {', '.join(plans)}")
            else:
                lines.append(f"- **Affected plans:** none (not referenced in any plan)")

            lines.append("")
    else:
        lines.append("\n## ✅ No newer versions or health issues detected\n")

    # Age-tier section: guidelines that are old even if no newer version was found
    aging = [e for e in report["entries"]
             if e.get("age_tier") in ("aging", "review_recommended")
             and e["status"] == "current"]

    if aging:
        lines.append(f"\n## 📅 Guidelines by Age (Periodic Review Needed)\n")
        lines.append("These guidelines are current (no newer PubMed version found) but are "
                      f"≥{AGE_TIER_REVIEW} years old. They may still be the authoritative "
                      "source, but should be periodically verified against society websites.\n")

        # Split into aging (≥8yr) and review (≥5yr)
        tier_aging = sorted(
            [e for e in aging if e.get("age_tier") == "aging"],
            key=lambda e: e.get("year") or 9999
        )
        tier_review = sorted(
            [e for e in aging if e.get("age_tier") == "review_recommended"],
            key=lambda e: e.get("year") or 9999
        )

        if tier_aging:
            lines.append(f"### 🔴 Aging (≥{AGE_TIER_STALE} years old) — Prioritize Review\n")
            lines.append("| Guideline | Year | Age | Affected Plans |")
            lines.append("|-----------|------|-----|----------------|")
            for e in tier_aging:
                age = (datetime.now().year - e["year"]) if e.get("year") else "?"
                plans = ", ".join(e.get("affected_plans", [])) or "none"
                lines.append(f"| {e['name']} | {e.get('year', '?')} | {age}yr | {plans} |")
            lines.append("")

        if tier_review:
            lines.append(f"### 🟡 Review Recommended (≥{AGE_TIER_REVIEW} years old)\n")
            lines.append("| Guideline | Year | Age | Affected Plans |")
            lines.append("|-----------|------|-----|----------------|")
            for e in tier_review:
                age = (datetime.now().year - e["year"]) if e.get("year") else "?"
                plans = ", ".join(e.get("affected_plans", [])) or "none"
                lines.append(f"| {e['name']} | {e.get('year', '?')} | {age}yr | {plans} |")
            lines.append("")

    # Show current items
    current = [e for e in report["entries"] if e["status"] == "current"]
    if current:
        lines.append(f"\n## Current ({len(current)} entries)\n")
        lines.append("| Name | Type | PMID | Year |")
        lines.append("|------|------|------|------|")
        for entry in sorted(current, key=lambda e: e["name"]):
            lines.append(
                f"| {entry['name']} | {entry['type']} | "
                f"{entry['pmid']} | {entry.get('year', '?')} |"
            )

    return "\n".join(lines)


def print_summary(report: dict):
    """Print a console summary of the freshness check."""
    s = report["summary"]
    print()
    print("=" * 60)
    print("  GUIDELINE FRESHNESS REPORT")
    print("=" * 60)
    print(f"  Run date:          {report['run_date']}")
    print(f"  Total checked:     {s['total_checked']}")
    print(f"  Current:           {s['current']}")
    print(f"  Newer available:   {s['flagged_newer_available']}")
    print(f"  Health issues:     {s['flagged_health']}")
    print(f"  PMID errors:       {s['not_found']}")
    print(f"  Skipped (no match):{s['skipped_no_search']}")
    print(f"  Aging (≥{AGE_TIER_STALE}yr):      {s['aging_guidelines']}")
    print(f"  Review (≥{AGE_TIER_REVIEW}yr):     {s['review_recommended_guidelines']}")
    print("=" * 60)

    total_flagged = s["flagged_newer_available"] + s["flagged_health"] + s["not_found"]
    total_aging = s["aging_guidelines"] + s["review_recommended_guidelines"]

    if total_flagged == 0 and total_aging == 0:
        print("\n  ✅ All entries appear current. No action needed.")
    else:
        if total_flagged > 0:
            print(f"\n  ⚠ {total_flagged} item(s) need immediate review (newer/health).")
        if total_aging > 0:
            print(f"  📅 {total_aging} guideline(s) are ≥{AGE_TIER_REVIEW}yr old — periodic review recommended.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Check freshness of guideline and trial citations",
        epilog="Designed to run monthly. Uses PubMed E-utilities (free, no API key).",
    )
    parser.add_argument(
        "--guidelines-only", action="store_true",
        help="Check only guidelines (skip trials)",
    )
    parser.add_argument(
        "--trials-only", action="store_true",
        help="Check only trials (skip guidelines)",
    )
    parser.add_argument(
        "--cache", action="store_true",
        help="Use/update local PMID cache (docs/data/pmid-cache.json)",
    )
    parser.add_argument(
        "--json", metavar="FILE",
        help="Write full report to JSON file",
    )
    parser.add_argument(
        "--markdown", metavar="FILE",
        help="Write human-readable summary to markdown file "
             "(default: docs/data/freshness-report.md)",
    )
    parser.add_argument(
        "--quiet", "-q", action="store_true",
        help="Only show flagged items",
    )

    args = parser.parse_args()

    # Load entries
    trials, guidelines = load_landmark_entries()

    check_trials = not args.guidelines_only
    check_guidelines = not args.trials_only

    if not check_trials and not check_guidelines:
        parser.error("Cannot use --guidelines-only and --trials-only together")

    # Run the check
    report = run_freshness_check(
        trials=trials,
        guidelines=guidelines,
        check_trials=check_trials,
        check_guidelines=check_guidelines,
        use_cache=args.cache,
        quiet=args.quiet,
    )

    if "error" in report:
        print(f"\n✖ Freshness check failed: {report['error']}", file=sys.stderr)
        sys.exit(1)

    # Print summary
    print_summary(report)

    # Write JSON report
    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"\nJSON report saved to {args.json}")

    # Write markdown report
    md_path = args.markdown or "docs/data/freshness-report.md"
    Path(md_path).parent.mkdir(parents=True, exist_ok=True)
    Path(md_path).write_text(format_markdown_report(report), encoding="utf-8")
    if not args.quiet:
        print(f"Markdown report saved to {md_path}")


if __name__ == "__main__":
    main()
