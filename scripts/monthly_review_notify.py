#!/usr/bin/env python3
"""
Monthly review notification for Clinical Plans.

Checks for pending plan requests in Supabase and guideline freshness,
then sends a macOS notification reminding the developer to run the
monthly review workflow.

Designed to run on the 1st of each month via launchd.

Usage:
    python3 scripts/monthly_review_notify.py
"""

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

SUPABASE_URL = "https://cyaginuvsqcbvyeuizlu.supabase.co"
PENDING_REQUESTS_ENDPOINT = (
    SUPABASE_URL + "/rest/v1/plan_requests?status=eq.pending&select=id"
)

FRESHNESS_SCRIPT = os.path.join(SCRIPT_DIR, "check_guideline_freshness.py")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(message: str):
    """Print a timestamped log line to stdout."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}")


def get_pending_request_count() -> tuple[int | None, str]:
    """Query Supabase for the number of pending plan requests.

    Returns (count, error_message).  count is None on failure.
    """
    api_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not api_key:
        return None, "Could not check requests (missing API key)"

    headers = {
        "apikey": api_key,
        "Authorization": f"Bearer {api_key}",
        "Prefer": "count=exact",
    }

    req = urllib.request.Request(PENDING_REQUESTS_ENDPOINT, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content_range = resp.headers.get("content-range", "")
            # content-range looks like "0-9/42" or "*/0"
            if "/" in content_range:
                count_str = content_range.split("/")[-1]
                try:
                    return int(count_str), ""
                except ValueError:
                    pass
            # Fallback: parse the JSON body and count rows
            body = json.loads(resp.read().decode("utf-8"))
            if isinstance(body, list):
                return len(body), ""
            return 0, ""
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return None, f"Could not check requests ({exc})"


def get_stale_guideline_count() -> tuple[int, str]:
    """Run check_guideline_freshness.py --json and count stale entries.

    Returns (stale_count, note).  note is non-empty on failure.
    """
    if not os.path.isfile(FRESHNESS_SCRIPT):
        return 0, "freshness script not found"

    try:
        result = subprocess.run(
            [sys.executable, FRESHNESS_SCRIPT, "--json", "/dev/stdout",
             "--guidelines-only", "--quiet"],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        return 0, f"freshness check failed ({exc})"

    if result.returncode != 0:
        return 0, "freshness check exited non-zero"

    # The --json flag writes to a file, but we asked for /dev/stdout
    # so the JSON report will be in stdout.  The script may also print
    # progress lines; try to find the JSON object in the output.
    stdout = result.stdout.strip()
    # Try parsing from the last '{' that starts a top-level object
    json_start = stdout.rfind('\n{"')
    if json_start == -1:
        json_start = stdout.find('{"')
    if json_start == -1:
        # Fallback: try parsing the markdown output from stdout for counts
        return 0, "could not parse freshness output"

    try:
        report = json.loads(stdout[json_start:])
    except json.JSONDecodeError:
        return 0, "could not parse freshness JSON"

    summary = report.get("summary", {})
    stale = (
        summary.get("flagged_newer_available", 0)
        + summary.get("flagged_health", 0)
        + summary.get("aging_guidelines", 0)
    )
    return stale, ""


def send_notification(title: str, message: str):
    """Send a macOS notification via osascript."""
    # Escape double-quotes inside the strings for AppleScript
    safe_title = title.replace('"', '\\"')
    safe_message = message.replace('"', '\\"')
    script = (
        f'display notification "{safe_message}" '
        f'with title "{safe_title}"'
    )
    try:
        subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError) as exc:
        log(f"WARNING: osascript failed — {exc}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log("Monthly review notification starting")

    # 1. Pending request count
    pending, req_error = get_pending_request_count()

    # 2. Guideline freshness
    stale, freshness_note = get_stale_guideline_count()

    # 3. Build notification message
    parts = []
    if req_error:
        parts.append(req_error)
    elif pending is not None and pending > 0:
        parts.append(f"{pending} plan request{'s' if pending != 1 else ''} pending")
    elif pending == 0:
        parts.append("No pending requests")

    if freshness_note:
        parts.append(f"0 guidelines need updating ({freshness_note})")
    elif stale > 0:
        parts.append(f"{stale} guideline{'s' if stale != 1 else ''} need{'s' if stale == 1 else ''} updating")
    else:
        parts.append("All guidelines current")

    # If everything is clean, say so explicitly
    if (pending is not None and pending == 0
            and stale == 0 and not req_error and not freshness_note):
        message = "No pending requests. All guidelines current."
    else:
        message = ". ".join(parts) + ". Run: python3 scripts/review_requests.py"

    # 4. Send notification
    send_notification("Clinical Plans Monthly Review", message)

    # 5. Log results
    log(f"Pending requests: {pending if pending is not None else 'unknown'}")
    if req_error:
        log(f"  Note: {req_error}")
    log(f"Stale guidelines: {stale}")
    if freshness_note:
        log(f"  Note: {freshness_note}")
    log(f"Notification: {message}")
    log("Done")


if __name__ == "__main__":
    main()
