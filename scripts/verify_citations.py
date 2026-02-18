#!/usr/bin/env python3
"""
Citation verification script for neuro-plans.

Extracts PMIDs from plan files and verifies them against the PubMed API.
Uses NCBI E-utilities (ESummary) for deterministic, 100% accurate lookups.
No external dependencies — uses only Python stdlib (urllib, json, xml).

Usage:
    python scripts/verify_citations.py docs/plans/migraine.md
    python scripts/verify_citations.py docs/plans/migraine.md --verify
    python scripts/verify_citations.py --all --verify
    python scripts/verify_citations.py --all --verify --fix
    python scripts/verify_citations.py --all --verify --json report.json
    python scripts/verify_citations.py --all --repair --json repair-report.json
    python scripts/verify_citations.py --all --repair --apply
    python scripts/verify_citations.py --all --lint          # offline format check
    python scripts/verify_citations.py --all --verify --cache # use/update cache

Modes:
    (default)   Extract and list citations with PMIDs
    --verify    Look up each PMID via PubMed API and check for mismatches
    --fix       Auto-correct citation text to match PubMed metadata (implies --verify)
    --repair    Find correct PMIDs for mismatched citations via PubMed search (implies --verify)
    --apply     Apply found corrections to markdown files (implies --repair)
    --lint      Offline PMID format/range validation (no API needed)
    --cache     Use local cache for verified PMIDs (reads + writes cache file)
    --json FILE Write verification/repair results to JSON file
    --quiet     Suppress per-citation output, show only summary
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.request
import urllib.error
from pathlib import Path


# ---------------------------------------------------------------------------
# PubMed API helpers (stdlib only — no requests dependency)
# ---------------------------------------------------------------------------

ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# NCBI requires tool + email for polite access. Rate limit: 3 req/sec without key.
API_PARAMS = {
    "tool": "neuro-plans-citation-verifier",
    "email": "neuro-plans@example.com",
}

# Seconds between API calls (3 req/sec without API key; use 0.5 for safety margin)
RATE_LIMIT_DELAY = 0.5

# Retry settings for transient API failures
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2  # seconds — exponential: 2, 4, 8

# Cache file for verified PMIDs
CACHE_FILE = Path("docs/data/pmid-cache.json")


# ---------------------------------------------------------------------------
# PMID format/range validation (offline — no API needed)
# ---------------------------------------------------------------------------

# Valid PMID range as of early 2026. PubMed IDs are sequential integers.
# First PMID: 1 (1946). As of Feb 2026, highest is ~41,700,000.
PMID_MIN = 1
PMID_MAX = 42_000_000  # generous upper bound; update periodically


# Approximate mapping of publication year to expected PMID range.
# Used for offline cross-reference validation.
# Source: PubMed sequential numbering; values are approximate bounds.
YEAR_TO_PMID_RANGE = {
    1990: (1_000_000, 3_000_000),
    1995: (3_000_000, 9_000_000),
    2000: (9_000_000, 12_000_000),
    2005: (14_000_000, 17_000_000),
    2010: (19_000_000, 22_000_000),
    2012: (21_000_000, 24_500_000),
    2015: (24_500_000, 27_500_000),
    2017: (27_000_000, 30_500_000),
    2018: (28_500_000, 31_500_000),
    2019: (30_000_000, 33_000_000),
    2020: (31_500_000, 34_000_000),
    2021: (33_000_000, 35_500_000),
    2022: (34_500_000, 37_000_000),
    2023: (36_000_000, 39_000_000),
    2024: (37_500_000, 40_500_000),
    2025: (39_500_000, 42_500_000),
    2026: (41_000_000, 44_000_000),
}


def _expected_pmid_range_for_year(year_str: str) -> tuple:
    """
    Return (min_pmid, max_pmid) expected for a given publication year.
    Returns None if year is not in our lookup table.
    Uses generous margins (±3M) to avoid false positives.
    """
    try:
        year = int(year_str)
    except (ValueError, TypeError):
        return None

    # Direct lookup
    if year in YEAR_TO_PMID_RANGE:
        lo, hi = YEAR_TO_PMID_RANGE[year]
        return (max(1, lo - 3_000_000), hi + 3_000_000)

    # Interpolate for years between known points
    years = sorted(YEAR_TO_PMID_RANGE.keys())
    if year < years[0] or year > years[-1]:
        return None

    for i in range(len(years) - 1):
        if years[i] <= year <= years[i + 1]:
            lo_year, hi_year = years[i], years[i + 1]
            lo_range = YEAR_TO_PMID_RANGE[lo_year]
            hi_range = YEAR_TO_PMID_RANGE[hi_year]
            frac = (year - lo_year) / (hi_year - lo_year)
            est_min = int(lo_range[0] + frac * (hi_range[0] - lo_range[0]))
            est_max = int(lo_range[1] + frac * (hi_range[1] - lo_range[1]))
            return (max(1, est_min - 3_000_000), est_max + 3_000_000)

    return None


def validate_pmid_format(pmid: str, citation_text: str = "") -> list[str]:
    """
    Validate PMID format offline (no API call).
    Returns list of issue strings; empty list = valid format.

    If citation_text is provided, cross-references the claimed year
    against the expected PMID range for that year.
    """
    issues = []

    # Must be all digits
    if not pmid.isdigit():
        issues.append(f"PMID '{pmid}' contains non-digit characters")
        return issues

    pmid_int = int(pmid)

    # Length check (valid PMIDs are 1-8 digits)
    if len(pmid) > 8:
        issues.append(f"PMID {pmid} has {len(pmid)} digits (max 8)")

    # Range check
    if pmid_int < PMID_MIN:
        issues.append(f"PMID {pmid} is below minimum valid range")
    elif pmid_int > PMID_MAX:
        issues.append(f"PMID {pmid} exceeds known PubMed range (>{PMID_MAX})")

    # Year-vs-PMID cross-reference: if the citation claims a specific year,
    # the PMID should be in the expected range for that year.
    # This catches the most common hallucination: a real paper title with a
    # fabricated PMID that is wildly out of range for the publication year.
    if citation_text:
        year_match = re.search(r'\b((?:19|20)\d{2})\b', citation_text)
        if year_match:
            claimed_year = year_match.group(1)
            expected = _expected_pmid_range_for_year(claimed_year)
            if expected:
                lo, hi = expected
                if pmid_int < lo or pmid_int > hi:
                    issues.append(
                        f"PMID {pmid} is outside expected range for year "
                        f"{claimed_year} (expected ~{lo:,}–{hi:,})"
                    )

    return issues


def lint_pmids(plan_citations: dict) -> dict:
    """
    Run offline PMID format/range validation on all extracted citations.
    Returns dict of {plan: [{"pmid": ..., "issues": [...], "citation": ...}]}.
    """
    results = {}
    total_checked = 0
    total_issues = 0

    for plan in sorted(plan_citations.keys()):
        plan_issues = []
        for cit in plan_citations[plan]:
            pmid = cit["pmid"]
            total_checked += 1
            issues = validate_pmid_format(pmid, cit["citation"])
            if issues:
                total_issues += len(issues)
                plan_issues.append({
                    "pmid": pmid,
                    "citation": cit["citation"],
                    "line": cit.get("line"),
                    "issues": issues,
                })

        if plan_issues:
            results[plan] = plan_issues

    print(f"\n{'='*70}")
    print(f"  PMID LINT RESULTS (offline format check)")
    print(f"{'='*70}")
    print(f"  PMIDs checked:  {total_checked}")
    print(f"  Issues found:   {total_issues}")
    print(f"  Plans affected: {len(results)}")
    print(f"{'='*70}")

    if results:
        for plan, issues in results.items():
            print(f"\n  {plan}:")
            for item in issues:
                for issue in item["issues"]:
                    print(f"    ⚠  PMID {item['pmid']}: {issue}")
                    print(f"       Citation: {item['citation'][:80]}")
    else:
        print("\n  ✅ All PMIDs pass format/range checks.")

    return results


# ---------------------------------------------------------------------------
# Verified PMID cache
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
    CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


def update_cache_from_metadata(cache: dict, metadata: dict) -> int:
    """
    Add verified PMIDs to cache. Only caches PMIDs confirmed to exist.
    Returns number of new entries added.
    """
    added = 0
    for pmid, meta in metadata.items():
        if meta.get("exists") and pmid not in cache["pmids"]:
            cache["pmids"][pmid] = {
                "title": meta.get("title", ""),
                "first_author": meta.get("first_author", ""),
                "journal_abbrev": meta.get("journal_abbrev", ""),
                "year": meta.get("year", ""),
                "verified_date": time.strftime("%Y-%m-%d"),
            }
            added += 1
    return added


# ---------------------------------------------------------------------------
# API connectivity and request handling
# ---------------------------------------------------------------------------

def check_api_connectivity() -> bool:
    """
    Quick connectivity check against NCBI E-utilities.
    Tests with a single well-known PMID (NINDS rt-PA trial, PMID 7477192).
    Returns True if API is reachable and responding correctly.
    """
    test_pmid = "7477192"
    try:
        params = {**API_PARAMS, "db": "pubmed", "id": test_pmid, "retmode": "json"}
        query = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in params.items())
        url = f"{ESUMMARY_URL}?{query}"
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            # Verify we got a real response
            result = data.get("result", {}).get(test_pmid, {})
            if result and "error" not in result:
                return True
            print("  ⚠ API returned unexpected response format", file=sys.stderr)
            return False
    except urllib.error.HTTPError as e:
        print(f"  ✖ PubMed API HTTP error: {e.code} {e.reason}", file=sys.stderr)
        return False
    except urllib.error.URLError as e:
        print(f"  ✖ PubMed API unreachable: {e.reason}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  ✖ PubMed API check failed: {e}", file=sys.stderr)
        return False


class APIError(Exception):
    """Raised when the PubMed API is unreachable (distinct from PMID not found)."""
    pass


def _api_get(url: str, params: dict) -> dict:
    """
    Make a GET request to NCBI E-utilities and return parsed JSON.
    Retries on transient failures with exponential backoff.
    Raises APIError on persistent network failures.
    """
    all_params = {**API_PARAMS, **params}
    query = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in all_params.items())
    full_url = f"{url}?{query}"

    last_error = None
    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(full_url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # Rate limited — wait longer and retry
                wait = RETRY_BACKOFF_BASE ** (attempt + 1)
                print(f"  Rate limited (429), retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                last_error = e
                continue
            elif e.code >= 500:
                # Server error — retry
                wait = RETRY_BACKOFF_BASE ** (attempt + 1)
                print(f"  Server error ({e.code}), retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                last_error = e
                continue
            else:
                # Client error (400, 403, etc.) — don't retry
                last_error = e
                break
        except urllib.error.URLError as e:
            wait = RETRY_BACKOFF_BASE ** (attempt + 1)
            if attempt < MAX_RETRIES - 1:
                print(f"  Network error, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            last_error = e
            continue
        except Exception as e:
            last_error = e
            break

    # All retries exhausted — raise instead of silently returning {}
    raise APIError(f"PubMed API request failed after {MAX_RETRIES} attempts: {last_error}")


def fetch_pmid_metadata(pmids: list[str], cache: dict = None) -> dict:
    """
    Batch-fetch metadata for a list of PMIDs via ESummary.
    Returns dict keyed by PMID with title, authors, journal, year, doi.
    Handles up to 200 PMIDs per request.

    If cache is provided, returns cached results for known-good PMIDs
    and only queries the API for uncached ones.

    Raises APIError if the API is unreachable.
    """
    results = {}

    # Phase 1: Serve from cache where possible
    uncached_pmids = list(pmids)
    if cache:
        cached_pmids = cache.get("pmids", {})
        uncached_pmids = []
        for pmid in pmids:
            if pmid in cached_pmids:
                entry = cached_pmids[pmid]
                results[pmid] = {
                    "exists": True,
                    "title": entry.get("title", ""),
                    "authors": [],
                    "first_author": entry.get("first_author", ""),
                    "last_author": "",
                    "journal": "",
                    "journal_abbrev": entry.get("journal_abbrev", ""),
                    "year": entry.get("year", ""),
                    "volume": "",
                    "issue": "",
                    "pages": "",
                    "doi": None,
                    "from_cache": True,
                }
            else:
                uncached_pmids.append(pmid)

        if results:
            print(f"  Cache: {len(results)} PMIDs from cache, "
                  f"{len(uncached_pmids)} need API lookup")

    if not uncached_pmids:
        return results

    # Phase 2: Fetch uncached PMIDs from API
    batch_size = 200

    for i in range(0, len(uncached_pmids), batch_size):
        batch = uncached_pmids[i:i + batch_size]
        data = _api_get(ESUMMARY_URL, {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "json",
        })

        result_data = data.get("result", {})
        for pmid in batch:
            record = result_data.get(pmid, {})
            if "error" in record or not record:
                results[pmid] = {"exists": False}
            else:
                # Extract DOI
                doi = None
                for aid in record.get("articleids", []):
                    if aid.get("idtype") == "doi":
                        doi = aid.get("value")
                        break

                # Extract authors
                authors = [a.get("name", "") for a in record.get("authors", [])]

                results[pmid] = {
                    "exists": True,
                    "title": record.get("title", ""),
                    "authors": authors,
                    "first_author": authors[0] if authors else "",
                    "last_author": record.get("lastauthor", ""),
                    "journal": record.get("fulljournalname", ""),
                    "journal_abbrev": record.get("source", ""),
                    "year": record.get("pubdate", "")[:4],
                    "volume": record.get("volume", ""),
                    "issue": record.get("issue", ""),
                    "pages": record.get("pages", ""),
                    "doi": doi,
                }

        # Rate limit between batches
        if i + batch_size < len(uncached_pmids):
            time.sleep(RATE_LIMIT_DELAY)

    return results


def search_pubmed(author: str = "", journal: str = "", year: str = "",
                  title_words: str = "", max_results: int = 5) -> list[str]:
    """Search PubMed by author/journal/year/title. Returns list of PMIDs.
    Raises APIError if the API is unreachable."""
    parts = []
    if author:
        parts.append(f"{author}[Author]")
    if journal:
        parts.append(f"{journal}[Journal]")
    if year:
        parts.append(f"{year}[Date - Publication]")
    if title_words:
        parts.append(f"{title_words}[Title]")

    if not parts:
        return []

    term = " AND ".join(parts)
    data = _api_get(ESEARCH_URL, {
        "db": "pubmed",
        "term": term,
        "retmax": str(max_results),
        "retmode": "json",
    })

    return data.get("esearchresult", {}).get("idlist", [])


# ---------------------------------------------------------------------------
# Citation extraction from markdown
# ---------------------------------------------------------------------------

def extract_citations(file_path: Path) -> list[dict]:
    """
    Extract all citations with PubMed links from a markdown file.
    Searches the entire file (not just Evidence section) for PubMed URLs.
    """
    content = file_path.read_text(encoding="utf-8")
    citations = []
    seen_pmids = set()

    # Pattern: [Citation text](https://pubmed.ncbi.nlm.nih.gov/12345678/)
    # Can appear in table cells or inline text
    pattern = r'\[([^\]]+)\]\(https?://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/?\)'

    for match in re.finditer(pattern, content):
        citation_text = match.group(1).strip()
        pmid = match.group(2)

        # Find the line number and surrounding context
        start = match.start()
        line_num = content[:start].count("\n") + 1

        # Try to extract the evidence claim from the table row
        line = content[content.rfind("\n", 0, start) + 1:content.find("\n", start)]
        evidence = ""
        if "|" in line:
            cells = [c.strip() for c in line.split("|")]
            # First non-empty cell is usually the evidence claim
            for cell in cells:
                if cell and cell != citation_text and "pubmed" not in cell.lower():
                    evidence = cell
                    break

        citations.append({
            "citation": citation_text,
            "pmid": pmid,
            "line": line_num,
            "evidence": evidence[:120] if evidence else "",
            "match_text": match.group(0),
        })

    return citations


def extract_unlinked_citations(file_path: Path) -> list[dict]:
    """Find citations in the Evidence section that don't have PubMed links."""
    content = file_path.read_text(encoding="utf-8")
    unlinked = []

    evidence_section = re.search(r'## 8\. EVIDENCE.*?(?=\n## |\Z)', content, re.DOTALL)
    if not evidence_section:
        return unlinked

    section = evidence_section.group(0)
    for line in section.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 4:
            continue

        # Last substantive cell is usually the source
        source_cell = cells[-2] if cells[-1] == "" else cells[-1]

        # Skip header/separator rows
        if source_cell.startswith("---") or source_cell == "Source":
            continue

        # Check if this row has a PubMed link
        if "pubmed.ncbi.nlm.nih.gov" not in line and source_cell:
            # Has text but no PubMed link
            if len(source_cell) > 5 and not source_cell.startswith("---"):
                unlinked.append({
                    "source_text": source_cell,
                    "evidence": cells[1] if len(cells) > 2 else "",
                })

    return unlinked


# ---------------------------------------------------------------------------
# Citation comparison / matching
# ---------------------------------------------------------------------------

def _strip_diacritics(text: str) -> str:
    """Remove diacritics/accents for fuzzy matching (e.g., Wickström → Wickstrom)."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


# Words/phrases that indicate a guideline, consensus, or trial citation.
# These are commonly cited by organization name rather than first author.
GUIDELINE_INDICATORS = [
    "guideline", "guidelines", "consensus", "practice parameter",
    "recommendation", "recommendations", "position statement",
    "advisory", "scientific statement", "white paper",
    "evidence assessment", "evidence-based", "standards of care",
    "expert opinion", "task force", "working group",
    # Organization acronyms
    "aha", "aha/asa", "aan", "aes", "ncs", "ilae", "ichd", "ean",
    "efns", "who", "nice", "sign", "acr", "aans", "cns",
    "ers", "aasm", "acns", "naemsp",
    "ahs", "ihs", "ens", "wfn", "abpn", "acep",
    # Trial names (commonly cited by trial name, not lead author)
    "trial", "study group", "investigators",
    "esett", "rampart", "preempt", "arise", "dawn", "defuse",
    "escape", "extend-ia", "mr clean", "revascat", "swift prime",
    "clots", "interact", "atach", "mistie", "clear",
    "isat", "brat", "coss", "sampris",
]


def compare_citation(citation_text: str, pubmed_meta: dict) -> dict:
    """
    Compare claimed citation text against actual PubMed metadata.
    Returns a result dict with match status and any issues found.

    Uses Unicode normalization for author matching and relaxed rules
    for guideline/consensus/trial citations.
    """
    if not pubmed_meta.get("exists"):
        return {
            "status": "NOT_FOUND",
            "issues": ["PMID does not exist in PubMed"],
        }

    issues = []
    ct = _strip_diacritics(citation_text).lower()
    first_author = pubmed_meta.get("first_author", "")
    last_author = pubmed_meta.get("last_author", "")
    journal = pubmed_meta.get("journal", "")
    journal_abbrev = pubmed_meta.get("journal_abbrev", "")
    year = pubmed_meta.get("year", "")

    # Detect guideline/consensus/trial citations early — these follow
    # different conventions (org name instead of first author, etc.)
    is_guideline = any(gw in ct for gw in GUIDELINE_INDICATORS)

    # --- Author check ---
    # For guidelines, skip author matching entirely — they cite by org name
    if not is_guideline:
        first_author_last = first_author.split()[0] if first_author else ""
        last_author_last = last_author.split()[0] if last_author else ""

        # Normalize author names too (handle diacritics in PubMed data)
        fa_norm = _strip_diacritics(first_author_last).lower()
        la_norm = _strip_diacritics(last_author_last).lower()

        author_found = False
        if fa_norm and fa_norm in ct:
            author_found = True
        elif la_norm and la_norm in ct:
            author_found = True

        # Also check first 5 co-author surnames
        if not author_found:
            for author in pubmed_meta.get("authors", [])[:5]:
                surname = author.split()[0] if author else ""
                surname_norm = _strip_diacritics(surname).lower()
                if surname_norm and len(surname_norm) > 2 and surname_norm in ct:
                    author_found = True
                    break

        if not author_found and first_author_last:
            issues.append(f"Author: expected '{first_author}', not found in citation text")

    # --- Year check ---
    if year and year not in citation_text:
        issues.append(f"Year: expected '{year}', not found in citation text")

    # --- Journal check (fuzzy — abbreviations vary widely) ---
    jl = _strip_diacritics(journal).lower()
    jal = _strip_diacritics(journal_abbrev).lower()

    # Common journal abbreviation mappings
    journal_aliases = {
        "the new england journal of medicine": ["nejm", "n engl j med"],
        "the lancet": ["lancet"],
        "the lancet. neurology": ["lancet neurol"],
        "the lancet neurology": ["lancet neurol"],
        "jama neurology": ["jama neurol"],
        "annals of neurology": ["ann neurol"],
        "neurology": ["neurology"],
        "epilepsia": ["epilepsia"],
        "cephalalgia": ["cephalalgia"],
        "stroke": ["stroke"],
        "brain": ["brain"],
        "journal of neurology, neurosurgery, and psychiatry": ["j neurol neurosurg psychiatry", "jnnp"],
        "annals of emergency medicine": ["ann emerg med"],
        "academic emergency medicine": ["acad emerg med"],
        "critical care medicine": ["crit care med"],
        "neurocritical care": ["neurocrit care"],
        "journal of neuroimmunology": ["j neuroimmunol"],
        "movement disorders": ["mov disord"],
        "headache": ["headache"],
        "journal of neurosurgery": ["j neurosurg"],
        "neurosurgery": ["neurosurgery"],
        "journal of stroke and cerebrovascular diseases": ["j stroke cerebrovasc dis"],
        "journal of the neurological sciences": ["j neurol sci"],
        "multiple sclerosis": ["mult scler"],
        "archives of neurology": ["arch neurol"],
        "current neurology and neuroscience reports": ["curr neurol neurosci rep"],
        "seizure": ["seizure"],
        "epilepsy & behavior": ["epilepsy behav"],
        "journal of clinical neuroscience": ["j clin neurosci"],
        "frontiers in neurology": ["front neurol"],
        "nature reviews. neurology": ["nat rev neurol"],
        "lancet neurology": ["lancet neurol"],
    }

    journal_found = False
    if jal and jal in ct:
        journal_found = True
    elif jl and jl in ct:
        journal_found = True
    else:
        for full_name, abbrevs in journal_aliases.items():
            if jl.startswith(full_name) or full_name.startswith(jl):
                for abbr in abbrevs:
                    if abbr in ct:
                        journal_found = True
                        break
            if journal_found:
                break

    # Don't flag journal mismatch for guidelines (commonly cited by org name)
    if not journal_found and journal and not is_guideline:
        issues.append(f"Journal: expected '{journal_abbrev or journal}', not found in citation text")

    # --- Determine status ---
    if not issues:
        status = "VERIFIED"
    elif len(issues) == 1 and "Journal" in issues[0]:
        status = "PARTIAL"  # Journal name mismatches are often just abbreviation differences
    else:
        status = "MISMATCH"

    return {
        "status": status,
        "issues": issues,
        "pubmed": {
            "title": pubmed_meta.get("title", ""),
            "first_author": first_author,
            "journal": journal_abbrev or journal,
            "year": year,
            "doi": pubmed_meta.get("doi", ""),
        },
    }


# ---------------------------------------------------------------------------
# Citation text parser — extract author, journal, year from citation text
# ---------------------------------------------------------------------------

# Map common abbreviations used in citation text to PubMed-searchable journal names
JOURNAL_SEARCH_MAP = {
    "nejm": "N Engl J Med",
    "n engl j med": "N Engl J Med",
    "lancet": "Lancet",
    "lancet neurol": "Lancet Neurol",
    "jama neurol": "JAMA Neurol",
    "ann neurol": "Ann Neurol",
    "neurology": "Neurology",
    "epilepsia": "Epilepsia",
    "cephalalgia": "Cephalalgia",
    "stroke": "Stroke",
    "brain": "Brain",
    "headache": "Headache",
    "jnnp": "J Neurol Neurosurg Psychiatry",
    "j neurol neurosurg psychiatry": "J Neurol Neurosurg Psychiatry",
    "ann emerg med": "Ann Emerg Med",
    "acad emerg med": "Acad Emerg Med",
    "crit care med": "Crit Care Med",
    "neurocrit care": "Neurocrit Care",
    "j neuroimmunol": "J Neuroimmunol",
    "mov disord": "Mov Disord",
    "j neurosurg": "J Neurosurg",
    "neurosurgery": "Neurosurgery",
    "cochrane": "Cochrane Database Syst Rev",
    "cochrane review": "Cochrane Database Syst Rev",
    "muscle nerve": "Muscle Nerve",
    "j neurol sci": "J Neurol Sci",
    "mult scler": "Mult Scler",
    "arch neurol": "Arch Neurol",
    "seizure": "Seizure",
    "epilepsy behav": "Epilepsy Behav",
    "front neurol": "Front Neurol",
    "nat rev neurol": "Nat Rev Neurol",
    "semin neurol": "Semin Neurol",
    "j clin neurosci": "J Clin Neurosci",
    "curr neurol neurosci rep": "Curr Neurol Neurosci Rep",
    "jama": "JAMA",
    "bmj": "BMJ",
    "ann intern med": "Ann Intern Med",
    "n engl j med": "N Engl J Med",
    "j neurol": "J Neurol",
    "eur j neurol": "Eur J Neurol",
    "j clin neurophysiol": "J Clin Neurophysiol",
    "clin neurophysiol": "Clin Neurophysiol",
    "j stroke cerebrovasc dis": "J Stroke Cerebrovasc Dis",
    "int j stroke": "Int J Stroke",
    "cerebrovasc dis": "Cerebrovasc Dis",
    "parkinsonism relat disord": "Parkinsonism Relat Disord",
    "j parkinsons dis": "J Parkinsons Dis",
    "amyotroph lateral scler": "Amyotroph Lateral Scler",
    "j peripher nerv syst": "J Peripher Nerv Syst",
    "autoimmun rev": "Autoimmun Rev",
    "mult scler relat disord": "Mult Scler Relat Disord",
    "j neuroophthalmol": "J Neuroophthalmol",
    "neurol clin": "Neurol Clin",
    "neurol clin pract": "Neurol Clin Pract",
    "ther adv neurol disord": "Ther Adv Neurol Disord",
    "expert rev neurother": "Expert Rev Neurother",
    "continuum": "Continuum (Minneap Minn)",
    "pract neurol": "Pract Neurol",
    "curr opin neurol": "Curr Opin Neurol",
    "j child neurol": "J Child Neurol",
    "dev med child neurol": "Dev Med Child Neurol",
    "j headache pain": "J Headache Pain",
    "j emerg med": "J Emerg Med",
    "emerg med clin north am": "Emerg Med Clin North Am",
    "crit care": "Crit Care",
    "intensive care med": "Intensive Care Med",
    "j intensive care med": "J Intensive Care Med",
    "chest": "Chest",
    "mayo clin proc": "Mayo Clin Proc",
    "ther clin risk manag": "Ther Clin Risk Manag",
    "drugs": "Drugs",
    "cns drugs": "CNS Drugs",
    "clin infect dis": "Clin Infect Dis",
    "j infect dis": "J Infect Dis",
    "j antimicrob chemother": "J Antimicrob Chemother",
    "j neurovirol": "J Neurovirol",
    "j neuropathol exp neurol": "J Neuropathol Exp Neurol",
    "acta neuropathol": "Acta Neuropathol",
    "acta neurol scand": "Acta Neurol Scand",
    "j neurooncol": "J Neurooncol",
    "neuro oncol": "Neuro Oncol",
    "cancer": "Cancer",
    "j clin oncol": "J Clin Oncol",
}


def parse_citation_text(text: str) -> dict:
    """
    Parse citation text into searchable components.

    Handles patterns like:
      "Author et al. Journal Year;vol:pages"
      "Author, Author2. Journal Year"
      "Author. Journal Year"
      "Org Guidelines Year"
      "PubMed: 12345678"

    Returns dict with keys: author, journal, year, is_guideline
    """
    result = {"author": "", "journal": "", "year": "", "is_guideline": False}

    # Skip bare PMID references
    if re.match(r'^PubMed:\s*\d+$', text.strip()):
        return result

    # Extract year — use the LAST year in the citation, not the first.
    # Citations like "NASCET 1991 (updated analysis 2005)" should use 2005.
    # If the structured paren-citation regex fires later, it overrides this.
    all_years = re.findall(r'\b((?:19|20)\d{2})\b', text)
    if all_years:
        result["year"] = all_years[-1]

    # Check if guideline-style citation
    ct_lower = _strip_diacritics(text).lower()
    result["is_guideline"] = any(gw in ct_lower for gw in GUIDELINE_INDICATORS)

    # Check for "TRIAL (Author et al. JOURNAL YEAR)" format BEFORE stripping parens
    # This is a common clinical citation format
    paren_citation = re.search(
        r'\(([A-Z][a-zA-Zéèêëàâäùûüïîôöç\' -]+?)\s+et\s+al\.?\s*[.,]?\s*'
        r'([A-Z][A-Za-z .]+?)\s+((?:19|20)\d{2})\)',
        text
    )
    if paren_citation:
        result["author"] = paren_citation.group(1).strip().rstrip(',')
        result["journal"] = paren_citation.group(2).strip().rstrip('.')
        result["year"] = paren_citation.group(3)
        return result

    # Remove trial name in parens, volume/pages, DOI
    clean = re.sub(r'\([^)]*\)', '', text)        # Remove (REGAIN), (CHAMPION-MG)
    clean = re.sub(r';\s*\d+[^,]*$', '', clean)   # Remove ;337:689-695
    clean = re.sub(r'\bdoi:?\s*\S+', '', clean, flags=re.IGNORECASE)
    clean = clean.strip().rstrip('.')

    # Extract author - everything before "et al.", "&", "and", or first period
    author = ""
    remainder = clean

    # Pattern 1: "Author et al. Journal Year"
    et_al_match = re.match(r'(.+?)\s+et\s+al\.?\s*[.,]?\s*', clean)
    if et_al_match:
        author = et_al_match.group(1).strip().rstrip(',')
        remainder = clean[et_al_match.end():].strip().rstrip('.')
    else:
        # Pattern 2: "Author1 & Author2. Journal Year" or "Author1 and Author2. Journal Year"
        amp_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?)\s*(?:&|and)\s*[A-Z].+?\.\s*(.+)', clean)
        if amp_match:
            author = amp_match.group(1).strip()
            remainder = amp_match.group(2).strip().rstrip('.')
        else:
            # Pattern 3: "Author1, Author2. Journal Year" (two named authors, may have Jr/Sr)
            two_auth_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?(?:\s+(?:Jr|Sr|III?|IV))?),\s*[A-Z][a-zA-Z\'-]+(?:\s+[A-Z]{1,3})?(?:\s+(?:Jr|Sr|III?|IV))?\.\s*(.+)', clean)
            if two_auth_match:
                author = two_auth_match.group(1).strip()
                remainder = two_auth_match.group(2).strip().rstrip('.')
            else:
                # Pattern 4: "Author. Journal Year" (single author)
                dot_match = re.match(r'([A-Z][a-zA-Zéèêëàâäùûüïîôöç\'-]+(?:\s+[A-Z]{1,3})?)\.\s*(.+)', clean)
                if dot_match:
                    author = dot_match.group(1).strip()
                    remainder = dot_match.group(2).strip().rstrip('.')

    # Fallback: check for parenthetical author — "Trial Name (Author et al.)"
    if not author:
        paren_match = re.search(r'\(([A-Z][a-zA-Z\'-]+)\s+et\s+al\.?\)', text)
        if paren_match:
            author = paren_match.group(1).strip()

    result["author"] = author

    # Extract journal from remainder (strip year and extra whitespace)
    if result["year"] and remainder:
        journal = remainder.replace(result["year"], "").strip().rstrip('.').strip()
        # Remove leading/trailing punctuation
        journal = journal.strip('.,;: ')
        if journal:
            result["journal"] = journal
    elif remainder and not author:
        # Entire text might be like "NCS Guidelines 2012" — journal = ""
        pass
    elif remainder:
        result["journal"] = remainder.strip('.,;: ')

    return result


def _resolve_journal_for_search(journal_hint: str) -> str:
    """Convert a journal abbreviation from citation text to PubMed-searchable form."""
    if not journal_hint:
        return ""
    hint_lower = journal_hint.lower().strip()
    # Direct lookup
    if hint_lower in JOURNAL_SEARCH_MAP:
        return JOURNAL_SEARCH_MAP[hint_lower]
    # Try without trailing period
    hint_clean = hint_lower.rstrip('.')
    if hint_clean in JOURNAL_SEARCH_MAP:
        return JOURNAL_SEARCH_MAP[hint_clean]
    # Return as-is (PubMed may still recognize it)
    return journal_hint


def find_correct_pmid(citation_text: str, wrong_pmid: str) -> dict:
    """
    Search PubMed to find the correct PMID for a mismatched citation.

    Tries multiple search strategies:
    1. Author + Journal + Year (most specific)
    2. Author + Year (broader — journal abbreviation might not match)
    3. Author + Journal (no year — date might be off by 1)

    Returns dict: {pmid, confidence, method, metadata} or {pmid: None, ...}
    """
    parsed = parse_citation_text(citation_text)
    author = parsed["author"]
    journal_hint = parsed["journal"]
    year = parsed["year"]

    if not author and not year:
        return {"pmid": None, "confidence": "none", "method": "no_searchable_info",
                "citation": citation_text}

    journal_search = _resolve_journal_for_search(journal_hint)

    # Extract author surname for search (e.g., "Mayo-Smith MF" → "Mayo-Smith")
    author_surname = ""
    if author:
        # Handle "Last First" or "Last FM" format
        parts = author.split()
        if parts:
            author_surname = _strip_diacritics(parts[0]).rstrip(',')

    strategies = []

    # Strategy 1: Author + Journal + Year (most specific)
    if author_surname and journal_search and year:
        strategies.append({
            "name": "author+journal+year",
            "author": author_surname,
            "journal": journal_search,
            "year": year,
        })

    # Strategy 2: Author + Year (broader)
    if author_surname and year:
        strategies.append({
            "name": "author+year",
            "author": author_surname,
            "journal": "",
            "year": year,
        })

    # Strategy 3: Author + Journal (year might be off by 1)
    if author_surname and journal_search:
        strategies.append({
            "name": "author+journal",
            "author": author_surname,
            "journal": journal_search,
            "year": "",
        })

    # Strategy 4: Just author surname (last resort for uncommon names)
    if author_surname and len(author_surname) > 5:
        strategies.append({
            "name": "author_only",
            "author": author_surname,
            "journal": "",
            "year": "",
        })

    for strategy in strategies:
        time.sleep(RATE_LIMIT_DELAY)

        results = search_pubmed(
            author=strategy["author"],
            journal=strategy["journal"],
            year=strategy["year"],
            max_results=5,
        )

        if not results:
            continue

        # Filter out the known-wrong PMID
        candidates = [r for r in results if r != wrong_pmid]
        if not candidates:
            continue

        # If we got exactly 1 candidate, high confidence
        if len(candidates) == 1:
            return {
                "pmid": candidates[0],
                "confidence": "high",
                "method": strategy["name"],
                "citation": citation_text,
                "all_candidates": candidates,
            }

        # Multiple candidates — fetch metadata and pick the best match
        time.sleep(RATE_LIMIT_DELAY)
        candidate_meta = fetch_pmid_metadata(candidates[:5])

        best = None
        best_score = -1

        for cand_pmid in candidates[:5]:
            meta = candidate_meta.get(cand_pmid, {})
            if not meta.get("exists"):
                continue

            score = _score_candidate(citation_text, parsed, meta)
            if score > best_score:
                best_score = score
                best = cand_pmid

        if best and best_score >= 2:
            confidence = "high" if best_score >= 3 else "medium"
            return {
                "pmid": best,
                "confidence": confidence,
                "method": strategy["name"],
                "citation": citation_text,
                "score": best_score,
                "all_candidates": candidates[:5],
            }

    return {"pmid": None, "confidence": "none", "method": "exhausted",
            "citation": citation_text}


def _score_candidate(citation_text: str, parsed: dict, meta: dict) -> int:
    """Score how well a PubMed record matches the citation text. Higher = better."""
    score = 0
    ct = _strip_diacritics(citation_text).lower()

    # Author match (+2 for first author, +1 for any author)
    # Use word-boundary regex to prevent short surnames ("li", "ma", "an")
    # from matching inside unrelated words ("likelier", "manage", "analysis")
    first_author = meta.get("first_author", "")
    if first_author:
        fa_surname = _strip_diacritics(first_author.split()[0]).lower() if first_author.split() else ""
        if fa_surname and len(fa_surname) > 1 and re.search(r'\b' + re.escape(fa_surname) + r'\b', ct):
            score += 2
        else:
            # Check any of the first 5 authors
            for auth in meta.get("authors", [])[:5]:
                surname = _strip_diacritics(auth.split()[0]).lower() if auth.split() else ""
                if surname and len(surname) > 2 and re.search(r'\b' + re.escape(surname) + r'\b', ct):
                    score += 1
                    break

    # Year match (+1)
    year = meta.get("year", "")
    if year and year in citation_text:
        score += 1

    # Journal match (+1)
    journal_abbrev = _strip_diacritics(meta.get("journal_abbrev", "")).lower()
    journal_full = _strip_diacritics(meta.get("journal", "")).lower()
    journal_hint = parsed.get("journal", "").lower()
    if journal_abbrev and journal_abbrev in ct:
        score += 1
    elif journal_full and journal_full in ct:
        score += 1
    elif journal_hint:
        resolved = _resolve_journal_for_search(journal_hint).lower()
        if resolved and (resolved in journal_abbrev or journal_abbrev in resolved
                         or resolved in journal_full or journal_full in resolved):
            score += 1

    # Title keyword match (+1 if 2+ meaningful words from citation appear
    # in the PubMed article title, or vice versa). This catches matches
    # where author+year is right but journal parsing failed.
    title = _strip_diacritics(meta.get("title", "")).lower()
    if title:
        # Extract meaningful words from citation (skip author, year, journal, stopwords)
        citation_words = set()
        for w in ct.split():
            w_clean = w.strip('.,;:()[]')
            if (len(w_clean) > 4 and w_clean.isalpha()
                    and w_clean not in {"trial", "study", "group", "their",
                                        "these", "those", "which", "about",
                                        "other", "after", "before", "during",
                                        "first", "second", "level", "class",
                                        "based", "using", "review", "between"}):
                citation_words.add(w_clean)
        # Count how many citation words appear in the article title
        # Use word-boundary check to avoid "cardiac" matching "pericardial"
        title_matches = sum(1 for w in citation_words
                            if re.search(r'\b' + re.escape(w) + r'\b', title))
        if title_matches >= 2:
            score += 1

    return score


def repair_mismatches(plan_citations: dict, metadata: dict, quiet: bool = False) -> dict:
    """
    For all MISMATCH citations, attempt to find correct PMIDs via PubMed search.
    Returns dict keyed by plan stem, each containing list of repair results.
    """
    repairs = {}
    total_mismatches = 0
    total_found = 0
    total_high = 0
    total_medium = 0

    # Pre-count mismatches per plan for progress display
    plans_with_mismatches = []
    for plan in sorted(plan_citations.keys()):
        count = 0
        for cit in plan_citations[plan]:
            pmid = cit["pmid"]
            meta = metadata.get(pmid, {"exists": False})
            result = compare_citation(cit["citation"], meta)
            if result["status"] in ("MISMATCH", "NOT_FOUND"):
                count += 1
        if count > 0:
            plans_with_mismatches.append((plan, count))

    total_plans = len(plans_with_mismatches)
    total_expected = sum(c for _, c in plans_with_mismatches)

    for plan_idx, (plan, _) in enumerate(plans_with_mismatches, 1):
        citations = plan_citations[plan]
        plan_repairs = []

        # Progress: always show which plan we're on
        print(f"  [{plan_idx}/{total_plans}] {plan}...", end="", flush=True)

        for cit in citations:
            pmid = cit["pmid"]
            meta = metadata.get(pmid, {"exists": False})
            result = compare_citation(cit["citation"], meta)

            if result["status"] not in ("MISMATCH", "NOT_FOUND"):
                continue

            total_mismatches += 1
            repair = find_correct_pmid(cit["citation"], pmid)
            repair["old_pmid"] = pmid
            repair["line"] = cit.get("line")
            repair["match_text"] = cit.get("match_text", "")

            if repair["pmid"]:
                total_found += 1
                if repair["confidence"] == "high":
                    total_high += 1
                else:
                    total_medium += 1

            plan_repairs.append(repair)

        if plan_repairs:
            repairs[plan] = plan_repairs
            found_count = sum(1 for r in plan_repairs if r["pmid"])
            print(f" {found_count}/{len(plan_repairs)} found "
                  f"(total: {total_found}/{total_mismatches})", flush=True)
        else:
            print(" no mismatches", flush=True)

    print(f"\n{'='*70}")
    print(f"  REPAIR SUMMARY")
    print(f"{'='*70}")
    print(f"  Total mismatches processed: {total_mismatches}")
    print(f"  Correct PMIDs found:        {total_found} "
          f"({total_found/total_mismatches*100:.0f}%)" if total_mismatches else "")
    print(f"    High confidence:           {total_high}")
    print(f"    Medium confidence:          {total_medium}")
    print(f"  Not found:                   {total_mismatches - total_found}")
    print(f"{'='*70}")

    return repairs


def apply_pmid_repairs(md_files: list, repairs: dict, confidence_threshold: str = "high") -> int:
    """
    Apply PMID corrections to markdown files.
    Only applies repairs at or above the confidence threshold.
    Returns total number of fixes applied.
    """
    min_confidence = {"high": 2, "medium": 1, "low": 0}
    threshold = min_confidence.get(confidence_threshold, 2)
    confidence_rank = {"high": 2, "medium": 1, "low": 0, "none": -1}

    total_fixes = 0

    for plan, plan_repairs in repairs.items():
        md_path = next((f for f in md_files if f.stem == plan), None)
        if not md_path:
            continue

        content = md_path.read_text(encoding="utf-8")
        fixes_in_plan = 0

        for repair in plan_repairs:
            if not repair.get("pmid"):
                continue
            if confidence_rank.get(repair["confidence"], -1) < threshold:
                continue

            old_pmid = repair["old_pmid"]
            new_pmid = repair["pmid"]

            # Replace the PubMed URL, preserving the citation text
            old_url = f"https://pubmed.ncbi.nlm.nih.gov/{old_pmid}/"
            new_url = f"https://pubmed.ncbi.nlm.nih.gov/{new_pmid}/"

            # Also handle URLs without trailing slash
            old_url_noslash = f"https://pubmed.ncbi.nlm.nih.gov/{old_pmid}"

            if old_url in content:
                content = content.replace(old_url, new_url)
                fixes_in_plan += 1
            elif old_url_noslash in content:
                content = content.replace(old_url_noslash, new_url)
                fixes_in_plan += 1

        if fixes_in_plan > 0:
            md_path.write_text(content, encoding="utf-8")
            print(f"  ✏️  Fixed {fixes_in_plan} PMID(s) in {md_path.name}")
            total_fixes += fixes_in_plan

    return total_fixes


# ---------------------------------------------------------------------------
# Fix mode — update citation text in markdown
# ---------------------------------------------------------------------------

def build_corrected_citation(pubmed_meta: dict) -> str:
    """Build a corrected citation string from PubMed metadata."""
    first_author = pubmed_meta.get("first_author", "Unknown")
    journal = pubmed_meta.get("journal_abbrev", "") or pubmed_meta.get("journal", "")
    year = pubmed_meta.get("year", "")
    title = pubmed_meta.get("title", "")

    # Shorten title for display
    if len(title) > 80:
        title = title[:77] + "..."

    # Format: "Author et al. Journal Year"
    num_authors = len(pubmed_meta.get("authors", []))
    if num_authors > 2:
        author_str = f"{first_author} et al."
    elif num_authors == 2:
        second = pubmed_meta["authors"][1]
        author_str = f"{first_author}, {second}"
    else:
        author_str = first_author

    parts = [author_str]
    if journal:
        parts.append(journal)
    if year:
        parts.append(year)

    return " ".join(parts)


def apply_fixes(file_path: Path, citations: list[dict], metadata: dict) -> int:
    """Update citation text in the file to match PubMed metadata. Returns fix count."""
    content = file_path.read_text(encoding="utf-8")
    fixes = 0

    for cit in citations:
        pmid = cit["pmid"]
        meta = metadata.get(pmid, {})
        if not meta.get("exists"):
            continue

        result = compare_citation(cit["citation"], meta)
        if result["status"] == "MISMATCH":
            corrected = build_corrected_citation(meta)
            old_link = f'[{cit["citation"]}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)'
            new_link = f'[{corrected}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)'
            if old_link in content:
                content = content.replace(old_link, new_link, 1)
                fixes += 1

    if fixes > 0:
        file_path.write_text(content, encoding="utf-8")

    return fixes


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

SYMBOLS = {
    "VERIFIED": "✅",
    "PARTIAL": "⚠️",
    "MISMATCH": "❌",
    "NOT_FOUND": "💀",
}


def print_plan_report(plan_name: str, citations: list[dict], metadata: dict,
                      unlinked: list[dict], quiet: bool = False):
    """Print verification report for a single plan."""
    if not citations and not unlinked:
        return

    counts = {"VERIFIED": 0, "PARTIAL": 0, "MISMATCH": 0, "NOT_FOUND": 0}
    results = []

    for cit in citations:
        pmid = cit["pmid"]
        meta = metadata.get(pmid, {"exists": False})
        result = compare_citation(cit["citation"], meta)
        counts[result["status"]] += 1
        results.append((cit, result))

    total = len(citations)
    verified_pct = (counts["VERIFIED"] + counts["PARTIAL"]) / total * 100 if total else 0

    print(f"\n{'='*70}")
    print(f"  {plan_name}")
    print(f"{'='*70}")
    print(f"  Linked citations: {total}   |   "
          f"✅ {counts['VERIFIED']}  ⚠️  {counts['PARTIAL']}  "
          f"❌ {counts['MISMATCH']}  💀 {counts['NOT_FOUND']}   |   "
          f"{verified_pct:.0f}% verified")

    if unlinked:
        print(f"  Unlinked citations: {len(unlinked)}")

    if quiet and counts["MISMATCH"] == 0 and counts["NOT_FOUND"] == 0:
        return counts  # Skip detail output but still return counts

    # Print issues
    for cit, result in results:
        if result["status"] in ("MISMATCH", "NOT_FOUND"):
            sym = SYMBOLS[result["status"]]
            print(f"\n  {sym} PMID {cit['pmid']}: {result['status']}")
            print(f"     Claimed:  {cit['citation']}")
            if result.get("pubmed"):
                pm = result["pubmed"]
                print(f"     Actual:   {pm.get('first_author', '?')} — "
                      f"{pm.get('journal', '?')} {pm.get('year', '?')}")
                print(f"     Title:    {pm.get('title', '?')[:90]}")
            for issue in result.get("issues", []):
                print(f"     → {issue}")

        elif result["status"] == "PARTIAL" and not quiet:
            sym = SYMBOLS[result["status"]]
            print(f"\n  {sym}  PMID {cit['pmid']}: {result['status']}")
            print(f"     Claimed:  {cit['citation']}")
            for issue in result.get("issues", []):
                print(f"     → {issue}")

    return counts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Verify PubMed citations in neuro-plan templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("markdown_file", nargs="*",
                        help="Path to one or more plan markdown files")
    parser.add_argument("--all", action="store_true",
                        help="Process all plans in docs/plans/")
    parser.add_argument("--verify", action="store_true",
                        help="Verify PMIDs against PubMed API")
    parser.add_argument("--fix", action="store_true",
                        help="Auto-correct mismatched citation text (implies --verify)")
    parser.add_argument("--repair", action="store_true",
                        help="Find correct PMIDs for mismatched citations (implies --verify)")
    parser.add_argument("--apply", action="store_true",
                        help="Apply PMID corrections to files (implies --repair)")
    parser.add_argument("--lint", action="store_true",
                        help="Offline PMID format/range validation (no API needed)")
    parser.add_argument("--cache", action="store_true",
                        help="Use local cache for verified PMIDs (reads + writes)")
    parser.add_argument("--confidence", choices=["high", "medium"],
                        default="high",
                        help="Minimum confidence for --apply (default: high)")
    parser.add_argument("--json", metavar="FILE",
                        help="Write results to JSON file")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Only show plans with issues")

    args = parser.parse_args()

    if args.apply:
        args.repair = True
    if args.repair:
        args.verify = True
    if args.fix:
        args.verify = True

    # Determine files
    if args.all:
        plans_dir = Path("docs/plans")
        md_files = sorted(plans_dir.glob("*.md"))
        md_files = [f for f in md_files
                    if f.name != "index.md" and "-report-" not in f.name]
    elif args.markdown_file:
        md_files = [Path(f) for f in args.markdown_file]
    else:
        parser.print_help()
        sys.exit(1)

    # Phase 1: Extract all PMIDs from all files
    plan_citations = {}  # plan_stem -> list of citation dicts
    plan_unlinked = {}   # plan_stem -> list of unlinked citations
    all_pmids = set()

    for md_path in md_files:
        if not md_path.exists():
            print(f"File not found: {md_path}", file=sys.stderr)
            continue

        citations = extract_citations(md_path)
        unlinked = extract_unlinked_citations(md_path)
        plan_citations[md_path.stem] = citations
        plan_unlinked[md_path.stem] = unlinked

        for c in citations:
            all_pmids.add(c["pmid"])

    total_citations = sum(len(v) for v in plan_citations.values())
    total_unlinked = sum(len(v) for v in plan_unlinked.values())

    print(f"\nExtracted {total_citations} linked citations "
          f"({len(all_pmids)} unique PMIDs) from {len(plan_citations)} plans")
    if total_unlinked:
        print(f"Found {total_unlinked} unlinked citations (no PubMed URL)")

    # --lint mode: offline format/range validation (no API needed)
    if args.lint:
        lint_results = lint_pmids(plan_citations)
        if args.json:
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump({"lint": lint_results}, indent=2, ensure_ascii=False, fp=f)
            print(f"\nLint results written to {args.json}")
        if lint_results:
            sys.exit(1)  # Non-zero exit for CI gating
        return

    if not args.verify:
        # Extract-only mode — just list what we found
        for plan, citations in sorted(plan_citations.items()):
            if not citations:
                continue
            print(f"\n{'='*60}")
            print(f"PLAN: {plan}")
            print(f"{'='*60}")
            for i, c in enumerate(citations, 1):
                print(f"  {i}. PMID {c['pmid']}: {c['citation']}")

        pmids_sorted = sorted(all_pmids)
        print(f"\nUnique PMIDs ({len(pmids_sorted)}):")
        print(", ".join(pmids_sorted))
        return

    # ---------------------------------------------------------------
    # Connectivity pre-check (fail fast if API is unreachable)
    # ---------------------------------------------------------------
    print("\nChecking PubMed API connectivity...")
    api_available = check_api_connectivity()

    if not api_available:
        print("\n" + "=" * 70)
        print("  ERROR: PubMed API is not reachable!")
        print("=" * 70)
        print("  Cannot verify PMIDs without API access.")
        print("  Possible causes:")
        print("    - Network/firewall/proxy blocking NCBI E-utilities")
        print("    - NCBI servers temporarily down")
        print("    - Rate limiting (too many recent requests)")
        print()
        print("  Available offline alternatives:")
        print("    --lint     Run format/range validation (no API)")
        print("    --cache    Use cached results from a previous run")
        print()

        # If cache is available, offer to use it
        if args.cache:
            cache = load_cache()
            cached_count = len(cache.get("pmids", {}))
            if cached_count > 0:
                print(f"  Cache contains {cached_count} verified PMIDs "
                      f"(last updated: {cache.get('updated', 'unknown')})")
                print("  Proceeding with cached data only...\n")
                # Build metadata from cache only
                metadata = {}
                for pmid in sorted(all_pmids):
                    cached = cache["pmids"].get(pmid)
                    if cached:
                        metadata[pmid] = {
                            "exists": True,
                            "title": cached.get("title", ""),
                            "authors": [],
                            "first_author": cached.get("first_author", ""),
                            "last_author": "",
                            "journal": "",
                            "journal_abbrev": cached.get("journal_abbrev", ""),
                            "year": cached.get("year", ""),
                            "from_cache": True,
                        }
                    else:
                        metadata[pmid] = {"exists": False, "api_unavailable": True}

                cached_hits = sum(1 for v in metadata.values() if v.get("exists"))
                uncached = len(all_pmids) - cached_hits
                print(f"  Cache hits: {cached_hits}/{len(all_pmids)} "
                      f"({uncached} PMIDs not in cache — shown as NOT_FOUND)")
            else:
                print("  Cache is empty. Run with API access first to populate it.")
                sys.exit(1)
        else:
            print("  Tip: Run with --cache to use/build a local cache,")
            print("       or --lint for offline format checks.")
            sys.exit(1)
    else:
        print("  ✓ PubMed API is reachable\n")

        # Load cache if requested
        cache = load_cache() if args.cache else None

        # Phase 2: Batch-verify all PMIDs via PubMed API
        print(f"Verifying {len(all_pmids)} unique PMIDs against PubMed API...")
        pmid_list = sorted(all_pmids)

        try:
            metadata = fetch_pmid_metadata(pmid_list, cache=cache)
        except APIError as e:
            print(f"\n  ✖ API failed during verification: {e}", file=sys.stderr)
            print("  Try again later, or use --lint for offline checks.")
            sys.exit(1)

        found = sum(1 for v in metadata.values() if v.get("exists"))
        not_found = sum(1 for v in metadata.values() if not v.get("exists"))
        print(f"  API results: {found} found, {not_found} not found\n")

        # Update cache with new results
        if args.cache and cache is not None:
            added = update_cache_from_metadata(cache, metadata)
            if added:
                save_cache(cache)
                print(f"  Cache updated: +{added} new PMIDs "
                      f"({len(cache['pmids'])} total cached)\n")

    # Phase 3: Compare and report
    grand_totals = {"VERIFIED": 0, "PARTIAL": 0, "MISMATCH": 0, "NOT_FOUND": 0}
    json_results = {}
    total_fixes = 0

    for plan in sorted(plan_citations.keys()):
        citations = plan_citations[plan]
        unlinked = plan_unlinked.get(plan, [])
        if not citations:
            continue

        counts = print_plan_report(plan, citations, metadata, unlinked, args.quiet)
        if counts:
            for k in grand_totals:
                grand_totals[k] += counts.get(k, 0)

        # Fix mode
        if args.fix:
            md_path = next((f for f in md_files if f.stem == plan), None)
            if md_path:
                fixes = apply_fixes(md_path, citations, metadata)
                if fixes:
                    print(f"  ✏️  Fixed {fixes} citation(s) in {md_path.name}")
                    total_fixes += fixes

        # Build JSON output
        if args.json:
            plan_results = []
            for cit in citations:
                pmid = cit["pmid"]
                meta = metadata.get(pmid, {"exists": False})
                result = compare_citation(cit["citation"], meta)
                plan_results.append({
                    "pmid": pmid,
                    "claimed": cit["citation"],
                    "line": cit.get("line"),
                    "status": result["status"],
                    "issues": result.get("issues", []),
                    "pubmed": result.get("pubmed"),
                })
            json_results[plan] = {
                "linked": plan_results,
                "unlinked": unlinked,
            }

    # Grand summary
    grand_total = sum(grand_totals.values())
    verified_pct = (grand_totals["VERIFIED"] + grand_totals["PARTIAL"]) / grand_total * 100 if grand_total else 0

    print(f"\n{'='*70}")
    print(f"  VERIFICATION SUMMARY")
    print(f"{'='*70}")
    print(f"  Plans checked:       {len([p for p in plan_citations if plan_citations[p]])}")
    print(f"  Citations verified:  {grand_total}")
    print(f"  ✅ Verified:          {grand_totals['VERIFIED']}")
    print(f"  ⚠️  Partial match:    {grand_totals['PARTIAL']}")
    print(f"  ❌ Mismatch:          {grand_totals['MISMATCH']}")
    print(f"  💀 Not found:         {grand_totals['NOT_FOUND']}")
    print(f"  Accuracy:            {verified_pct:.1f}%")
    if total_unlinked:
        print(f"  Unlinked citations:  {total_unlinked}")
    if total_fixes:
        print(f"  Auto-fixed:          {total_fixes}")
    print(f"{'='*70}")

    if grand_totals["NOT_FOUND"] > 0:
        print(f"\n⚠️  {grand_totals['NOT_FOUND']} PMID(s) do not exist in PubMed!")

    # Phase 4: Repair — find correct PMIDs for mismatches
    repairs = {}
    total_pmid_fixes = 0
    if args.repair and (grand_totals["MISMATCH"] + grand_totals["NOT_FOUND"]) > 0:
        mismatch_count = grand_totals["MISMATCH"] + grand_totals["NOT_FOUND"]
        print(f"\n{'='*70}")
        print(f"  REPAIR PHASE — searching for correct PMIDs ({mismatch_count} mismatches)")
        print(f"{'='*70}\n")

        try:
            repairs = repair_mismatches(plan_citations, metadata, quiet=args.quiet)
        except APIError as e:
            print(f"\n  ✖ API failed during repair phase: {e}", file=sys.stderr)
            print("  Verification results above are still valid.")
            repairs = {}

        # Apply corrections if requested
        if args.apply and repairs:
            print(f"\nApplying corrections (confidence >= {args.confidence})...\n")
            total_pmid_fixes = apply_pmid_repairs(md_files, repairs,
                                                  confidence_threshold=args.confidence)
            if total_pmid_fixes:
                print(f"\n  Total PMIDs corrected: {total_pmid_fixes}")
            else:
                print("  No corrections met the confidence threshold.")

    # Write JSON
    if args.json:
        json_output = {
            "summary": {
                "total_citations": grand_total,
                "verified": grand_totals["VERIFIED"],
                "partial": grand_totals["PARTIAL"],
                "mismatch": grand_totals["MISMATCH"],
                "not_found": grand_totals["NOT_FOUND"],
                "accuracy_pct": round(verified_pct, 1),
                "unlinked": total_unlinked,
                "pmids_corrected": total_pmid_fixes,
            },
            "plans": json_results,
        }
        if repairs:
            # Add repair results to JSON
            repair_json = {}
            for plan, plan_repairs in repairs.items():
                repair_json[plan] = [
                    {
                        "citation": r["citation"],
                        "old_pmid": r["old_pmid"],
                        "new_pmid": r.get("pmid"),
                        "confidence": r.get("confidence", "none"),
                        "method": r.get("method", ""),
                        "line": r.get("line"),
                    }
                    for r in plan_repairs
                ]
            json_output["repairs"] = repair_json

        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(json_output, f, indent=2, ensure_ascii=False)
        print(f"\nResults written to {args.json}")


if __name__ == "__main__":
    main()
