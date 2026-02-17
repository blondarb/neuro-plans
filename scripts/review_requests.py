#!/usr/bin/env python3
"""
Monthly plan request review script.

Pulls pending plan requests from Supabase, groups similar requests,
checks against existing plans, and produces a ranked demand report.
Optionally approves specific requests and generates a monthly work list.

Uses only Python stdlib (no external dependencies). Connects to the
Supabase REST API directly via urllib.

Usage:
    python scripts/review_requests.py --report
    python scripts/review_requests.py --approve abc123,def456,ghi789
    python scripts/review_requests.py --report --specialty cardiology
    python scripts/review_requests.py --approve abc123 --specialty all

Flags:
    --report            Read-only mode; print demand report without updating Supabase
    --approve IDs       Comma-separated request IDs to mark as approved
    --specialty NAME    Filter by specialty (cardiology|neurology|all); default: auto-detect

Environment:
    SUPABASE_SERVICE_ROLE_KEY   Service-role key for admin access
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

SUPABASE_URL = "https://cyaginuvsqcbvyeuizlu.supabase.co"
REST_BASE = f"{SUPABASE_URL}/rest/v1"

PLANS_JSON = REPO_ROOT / "docs" / "data" / "plans.json"
WORK_LIST_JSON = REPO_ROOT / "docs" / "data" / "monthly-work-list.json"
SPECIALTY_CONFIG = (
    REPO_ROOT / "ios" / "NeuroPlans" / "NeuroPlans" / "SpecialtyConfig.swift"
)

SIMILARITY_THRESHOLD = 0.7  # SequenceMatcher ratio for "same request"
PLAN_MATCH_THRESHOLD = 0.7  # SequenceMatcher ratio for "already exists"


# ---------------------------------------------------------------------------
# Supabase REST helpers
# ---------------------------------------------------------------------------

def _get_service_key() -> str:
    """Return the service-role key from the environment, or exit."""
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    if not key:
        print("ERROR: Environment variable SUPABASE_SERVICE_ROLE_KEY is not set.")
        print("       Export it before running this script.")
        sys.exit(1)
    return key


def _headers(key: str) -> dict:
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def _ssl_context() -> ssl.SSLContext:
    """Return a default SSL context for HTTPS requests."""
    return ssl.create_default_context()


def supabase_get(table: str, params: dict, key: str) -> list[dict]:
    """GET rows from a Supabase table via the REST API."""
    query = urllib.parse.urlencode(params)
    url = f"{REST_BASE}/{table}?{query}"
    req = urllib.request.Request(url, headers=_headers(key), method="GET")
    try:
        with urllib.request.urlopen(req, context=_ssl_context(), timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"ERROR: Supabase GET {table} returned {exc.code}: {body}")
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"ERROR: Could not reach Supabase: {exc.reason}")
        sys.exit(1)


def supabase_patch(table: str, match_params: dict, body: dict, key: str) -> list[dict]:
    """PATCH (update) rows in a Supabase table via the REST API."""
    query = urllib.parse.urlencode(match_params)
    url = f"{REST_BASE}/{table}?{query}"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=_headers(key), method="PATCH")
    try:
        with urllib.request.urlopen(req, context=_ssl_context(), timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        resp_body = exc.read().decode("utf-8", errors="replace")
        print(f"ERROR: Supabase PATCH {table} returned {exc.code}: {resp_body}")
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"ERROR: Could not reach Supabase: {exc.reason}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Specialty detection
# ---------------------------------------------------------------------------

def detect_specialty() -> str:
    """Auto-detect specialty from SpecialtyConfig.swift, or default to 'all'."""
    if not SPECIALTY_CONFIG.exists():
        return "all"
    try:
        text = SPECIALTY_CONFIG.read_text(encoding="utf-8")
        match = re.search(r'static\s+let\s+specialty\s*=\s*"(\w+)"', text)
        if match:
            return match.group(1).lower()
    except OSError:
        pass
    return "all"


# ---------------------------------------------------------------------------
# Plans loading and fuzzy matching
# ---------------------------------------------------------------------------

def load_plans() -> dict[str, str]:
    """Load plan ID -> title mapping from plans.json.

    Returns an empty dict if the file is missing or malformed.
    """
    if not PLANS_JSON.exists():
        print(f"  WARNING: {PLANS_JSON} not found — skipping existing-plan matching")
        return {}
    try:
        data = json.loads(PLANS_JSON.read_text(encoding="utf-8"))
        return {pid: entry.get("title", pid) for pid, entry in data.items()}
    except (json.JSONDecodeError, AttributeError) as exc:
        print(f"  WARNING: Could not parse plans.json — {exc}")
        return {}


def normalize(text: str) -> str:
    """Lowercase, strip, collapse whitespace."""
    return re.sub(r"\s+", " ", text.strip().lower())


def fuzzy_match_plan(request_text: str, plans: dict[str, str]) -> str | None:
    """Return the plan ID whose title best matches request_text, or None.

    Uses SequenceMatcher on normalised strings. Both the plan title and the
    plan ID (with hyphens replaced by spaces) are tested.
    """
    norm_req = normalize(request_text)
    best_id: str | None = None
    best_ratio = 0.0

    for plan_id, plan_title in plans.items():
        # Compare against title
        ratio_title = difflib.SequenceMatcher(
            None, norm_req, normalize(plan_title)
        ).ratio()
        # Compare against id (hyphens -> spaces)
        ratio_id = difflib.SequenceMatcher(
            None, norm_req, plan_id.replace("-", " ")
        ).ratio()
        ratio = max(ratio_title, ratio_id)

        if ratio > best_ratio:
            best_ratio = ratio
            best_id = plan_id

    if best_ratio >= PLAN_MATCH_THRESHOLD:
        return best_id
    return None


# ---------------------------------------------------------------------------
# Request clustering
# ---------------------------------------------------------------------------

def cluster_requests(requests: list[dict]) -> list[list[dict]]:
    """Group requests by textual similarity.

    Returns a list of clusters (each cluster is a list of request dicts).
    Two requests land in the same cluster when their normalised request_text
    has a SequenceMatcher ratio >= SIMILARITY_THRESHOLD.
    """
    clusters: list[list[dict]] = []

    for req in requests:
        norm_text = normalize(req.get("request_text", ""))
        placed = False
        for cluster in clusters:
            representative = normalize(cluster[0].get("request_text", ""))
            ratio = difflib.SequenceMatcher(None, norm_text, representative).ratio()
            if ratio >= SIMILARITY_THRESHOLD:
                cluster.append(req)
                placed = True
                break
        if not placed:
            clusters.append([req])

    # Sort by cluster size descending, then alphabetically by representative
    clusters.sort(key=lambda c: (-len(c), normalize(c[0].get("request_text", ""))))
    return clusters


# ---------------------------------------------------------------------------
# Report printing
# ---------------------------------------------------------------------------

def print_report(
    existing_matches: list[tuple[dict, str]],
    new_clusters: list[list[dict]],
    total_pending: int,
    specialty: str,
) -> None:
    """Print the formatted monthly review report."""
    now = datetime.now()
    month_label = now.strftime("%B %Y")

    bar = "\u2550" * 47  # box-drawing double horizontal
    print()
    print(bar)
    print(f"MONTHLY PLAN REQUEST REVIEW \u2014 {month_label}")
    if specialty != "all":
        print(f"Specialty: {specialty}")
    print(bar)

    # -- Already exist --
    print()
    if existing_matches:
        print("ALREADY EXIST (auto-declined):")
        for req, plan_id in existing_matches:
            text = req.get("request_text", "(empty)")
            print(f'  \u2022 "{text}" \u2192 matches: {plan_id}')
    else:
        print("ALREADY EXIST (auto-declined): (none)")

    # -- New requests ranked by demand --
    print()
    if new_clusters:
        print("NEW REQUESTS (ranked by demand):")
        for rank, cluster in enumerate(new_clusters, start=1):
            count = len(cluster)
            label = "request" if count == 1 else "requests"
            representative = cluster[0].get("request_text", "(empty)")
            # Align numbers nicely
            print(f'  {rank:>2}. [{count} {label}] {" " if count < 10 else ""}"{representative}"')
    else:
        print("NEW REQUESTS (ranked by demand): (none)")

    # -- Summary --
    n_exist = len(existing_matches)
    n_new_requests = sum(len(c) for c in new_clusters)
    n_unique = len(new_clusters)

    print()
    print(
        f"Summary: {total_pending} pending \u2192 "
        f"{n_exist} already exist, "
        f"{n_new_requests} genuinely new ({n_unique} unique)"
    )
    print(bar)
    print()


# ---------------------------------------------------------------------------
# Approve workflow
# ---------------------------------------------------------------------------

def approve_requests(
    ids: list[str],
    pending: list[dict],
    key: str,
) -> list[dict]:
    """Mark the given request IDs as approved in Supabase.

    Returns the list of approved request dicts (for the work list).
    """
    pending_by_id = {r["id"]: r for r in pending}
    approved: list[dict] = []

    for rid in ids:
        if rid not in pending_by_id:
            print(f"  WARNING: Request ID '{rid}' is not in the pending set — skipping")
            continue

        result = supabase_patch(
            "plan_requests",
            {"id": f"eq.{rid}"},
            {
                "status": "approved",
                "reviewed_at": datetime.utcnow().isoformat() + "Z",
                "review_notes": "Approved via review_requests.py",
            },
            key,
        )

        if result:
            req = pending_by_id[rid]
            approved.append(req)
            print(f'  Approved: "{req.get("request_text", rid)}"')
        else:
            print(f"  WARNING: PATCH returned empty for {rid}")

    return approved


def mark_existing(
    matches: list[tuple[dict, str]],
    key: str,
) -> None:
    """Mark requests that match existing plans as status='exists'."""
    for req, plan_id in matches:
        supabase_patch(
            "plan_requests",
            {"id": f"eq.{req['id']}"},
            {
                "status": "exists",
                "matched_plan_id": plan_id,
                "reviewed_at": datetime.utcnow().isoformat() + "Z",
                "review_notes": f"Auto-matched to existing plan: {plan_id}",
            },
            key,
        )


# ---------------------------------------------------------------------------
# Work list generation
# ---------------------------------------------------------------------------

def generate_work_list(
    approved: list[dict],
    clusters: list[list[dict]],
    specialty: str,
) -> None:
    """Write docs/data/monthly-work-list.json with approved items."""
    # Build demand counts from clusters
    demand_map: dict[str, int] = {}
    for cluster in clusters:
        for req in cluster:
            demand_map[req["id"]] = len(cluster)

    items = []
    for req in approved:
        items.append({
            "request_id": req["id"],
            "text": req.get("request_text", ""),
            "demand": demand_map.get(req["id"], 1),
        })

    payload = {
        "generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
        "specialty": specialty,
        "approved": items,
    }

    WORK_LIST_JSON.parent.mkdir(parents=True, exist_ok=True)
    WORK_LIST_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"  Work list written to {WORK_LIST_JSON.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Monthly plan request review — pull, cluster, match, report",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Read-only mode: print report without updating Supabase",
    )
    parser.add_argument(
        "--approve",
        metavar="IDs",
        help="Comma-separated request IDs to mark as approved",
    )
    parser.add_argument(
        "--specialty",
        choices=["cardiology", "neurology", "all"],
        default=None,
        help="Filter by specialty (default: auto-detect from repo)",
    )

    args = parser.parse_args()

    # Must specify at least one action
    if not args.report and not args.approve:
        parser.error("Specify --report, --approve, or both")

    # Resolve specialty
    specialty = args.specialty or detect_specialty()
    print(f"Specialty: {specialty}")

    # Service key
    key = _get_service_key()

    # ------------------------------------------------------------------
    # 1. Fetch pending requests from Supabase
    # ------------------------------------------------------------------
    print("Fetching pending requests from Supabase...")

    params: dict[str, str] = {
        "status": "eq.pending",
        "select": "*",
        "order": "created_at.asc",
    }
    if specialty != "all":
        params["specialty"] = f"eq.{specialty}"

    pending = supabase_get("plan_requests", params, key)

    if not pending:
        print("No pending requests found. Nothing to do.")
        sys.exit(0)

    print(f"  Found {len(pending)} pending request(s)")

    # ------------------------------------------------------------------
    # 2. Load existing plans
    # ------------------------------------------------------------------
    plans = load_plans()
    print(f"  Loaded {len(plans)} existing plan(s) from plans.json")

    # ------------------------------------------------------------------
    # 3. Match requests against existing plans
    # ------------------------------------------------------------------
    existing_matches: list[tuple[dict, str]] = []  # (request, matched_plan_id)
    unmatched: list[dict] = []

    for req in pending:
        text = req.get("request_text", "")
        matched_plan_id = fuzzy_match_plan(text, plans) if plans else None
        if matched_plan_id:
            existing_matches.append((req, matched_plan_id))
        else:
            unmatched.append(req)

    # ------------------------------------------------------------------
    # 4. Cluster unmatched requests by similarity
    # ------------------------------------------------------------------
    clusters = cluster_requests(unmatched)

    # ------------------------------------------------------------------
    # 5. Print report
    # ------------------------------------------------------------------
    if args.report:
        print_report(existing_matches, clusters, len(pending), specialty)

    # ------------------------------------------------------------------
    # 6. Mark existing matches in Supabase (unless --report only)
    # ------------------------------------------------------------------
    if not args.report and existing_matches:
        print("Marking existing-plan matches in Supabase...")
        mark_existing(existing_matches, key)
        print(f"  Marked {len(existing_matches)} request(s) as 'exists'")

    # If --report AND --approve, still mark existing but inform user
    if args.report and args.approve:
        print("NOTE: --report mode — existing-plan matches are NOT updated in Supabase")

    # ------------------------------------------------------------------
    # 7. Approve specific requests
    # ------------------------------------------------------------------
    if args.approve:
        if args.report:
            print("\nWARNING: --report flag is set — approvals will NOT be written to Supabase")
            print("         Remove --report to actually approve requests")
        else:
            ids = [i.strip() for i in args.approve.split(",") if i.strip()]
            if not ids:
                print("ERROR: --approve requires at least one request ID")
                sys.exit(1)

            print(f"\nApproving {len(ids)} request(s)...")
            approved = approve_requests(ids, pending, key)

            if approved:
                print(f"\nGenerating monthly work list...")
                generate_work_list(approved, clusters, specialty)
            else:
                print("  No requests were approved (check IDs)")


if __name__ == "__main__":
    main()
