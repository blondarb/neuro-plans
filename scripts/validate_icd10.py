#!/usr/bin/env python3
"""
ICD-10-CM code validation script for neuro-plans.

Extracts ICD-10 codes from plan files and validates them:
  - Offline: format validation (code structure, pattern checks)
  - Online: lookup against the NLM ICD-10-CM API for existence and HIPAA validity

Uses only Python stdlib (no external dependencies).

Usage:
    python scripts/validate_icd10.py docs/plans/migraine.md
    python scripts/validate_icd10.py docs/plans/migraine.md --verify
    python scripts/validate_icd10.py --all --lint
    python scripts/validate_icd10.py --all --verify
    python scripts/validate_icd10.py --all --verify --save-report report.md
    python scripts/validate_icd10.py --all --verify --json report.json

Modes:
    (default)   Extract and list ICD-10 codes from plan file(s)
    --lint      Offline format/structure validation (no API needed)
    --verify    Validate each code against NLM ICD-10-CM API
    --json FILE Write results to JSON file
    --save-report FILE  Write human-readable Markdown report

Flags:
    --all       Process all plans in docs/plans/ and docs/drafts/
    --quiet     Suppress per-code output, show only summary
    --drafts    Include docs/drafts/ in --all (default: plans only)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# ICD-10-CM format rules (offline validation)
# ---------------------------------------------------------------------------

# ICD-10-CM code structure:
# - Starts with a letter (A-Z, excluding U which is reserved)
# - Followed by 2 digits
# - Optionally followed by a decimal point and 1-4 alphanumeric characters
# - Total length: 3-7 characters (without dot), displayed as X00.XXXX
ICD10_PATTERN = re.compile(
    r'^[A-TV-Z]'       # First character: letter (A-T, V-Z; U reserved for new diseases)
    r'[0-9]{2}'        # Characters 2-3: digits
    r'(?:\.'           # Optional decimal portion:
    r'[A-Z0-9]{1,4}'   #   1-4 alphanumeric characters after the dot
    r')?$',            # End of string
    re.IGNORECASE
)

# Pattern to extract ICD-10 codes from plan markdown
# Matches the **ICD-10:** line and captures everything after it
ICD10_LINE_PATTERN = re.compile(
    r'\*\*ICD-10:\*\*\s*(.+?)(?:\n|$)',
    re.IGNORECASE
)

# Pattern to extract individual codes from the ICD-10 line
# Matches patterns like: G47.33 (description), G47.33, G47.33;
CODE_EXTRACT_PATTERN = re.compile(
    r'([A-Z][0-9]{2}(?:\.[A-Z0-9]{1,4})?)\s*'  # Code
    r'(?:\([^)]*\))?',                             # Optional (description)
    re.IGNORECASE
)


# ---------------------------------------------------------------------------
# NLM ICD-10-CM API
# ---------------------------------------------------------------------------

# CMS.gov ICD-10 API (no key required, public access)
# Alternate: https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search
NLM_SEARCH_URL = "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search"

# Rate limit: be polite (no official limit, but 2 req/sec is safe)
RATE_LIMIT_DELAY = 0.5

# Retry settings
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2


# ---------------------------------------------------------------------------
# Code extraction
# ---------------------------------------------------------------------------

def extract_icd10_from_file(filepath: Path) -> list[dict]:
    """
    Extract ICD-10 codes from a plan file.

    Returns list of dicts:
        {
            "code": "G47.33",
            "description": "Obstructive sleep apnea",
            "line_number": 25,
            "raw_text": "G47.33 (Obstructive sleep apnea)"
        }
    """
    results = []
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    for i, line in enumerate(lines, start=1):
        match = ICD10_LINE_PATTERN.search(line)
        if match:
            icd_text = match.group(1)
            # Extract individual codes from the line
            for code_match in CODE_EXTRACT_PATTERN.finditer(icd_text):
                code = code_match.group(1).upper()
                # Try to get the description in parentheses
                desc = ""
                desc_match = re.search(
                    re.escape(code_match.group(1)) + r'\s*\(([^)]+)\)',
                    icd_text,
                    re.IGNORECASE
                )
                if desc_match:
                    desc = desc_match.group(1).strip()

                results.append({
                    "code": code,
                    "description": desc,
                    "line_number": i,
                    "raw_text": code_match.group(0).strip(),
                })

    return results


# ---------------------------------------------------------------------------
# Offline format validation
# ---------------------------------------------------------------------------

def validate_format(code: str) -> list[str]:
    """
    Validate ICD-10-CM code format offline.
    Returns list of issue strings; empty = valid format.
    """
    issues = []

    # Basic pattern check
    if not ICD10_PATTERN.match(code):
        issues.append(f"Code '{code}' does not match ICD-10-CM format pattern")
        return issues

    # U-codes are reserved (WHO use only, not CM)
    if code[0] == 'U':
        issues.append(f"Code '{code}' starts with 'U' (reserved codes, not standard ICD-10-CM)")

    # Check for common format issues
    first_char = code[0].upper()
    digits = code[1:3]

    # Category headers (3 chars) are generally not billable
    if '.' not in code and len(code) == 3:
        issues.append(f"Code '{code}' is a 3-character category (may be header-only, not billable)")

    return issues


# ---------------------------------------------------------------------------
# Online API validation
# ---------------------------------------------------------------------------

def _api_request(url: str, params: dict) -> Optional[dict]:
    """Make an API request with retry logic."""
    query = urllib.parse.urlencode(params)
    full_url = f"{url}?{query}"

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(full_url)
            req.add_header("User-Agent", "neuro-plans-icd10-validator/1.0")
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                wait = RETRY_BACKOFF_BASE ** (attempt + 1)
                time.sleep(wait)
                continue
            return None
        except (urllib.error.URLError, TimeoutError):
            wait = RETRY_BACKOFF_BASE ** (attempt + 1)
            time.sleep(wait)
            continue

    return None


def verify_code_nlm(code: str) -> dict:
    """
    Verify a single ICD-10-CM code against NLM Clinical Tables API.

    Returns:
        {
            "exists": bool,
            "hipaa_valid": bool,
            "api_description": str or None,
            "error": str or None
        }
    """
    # NLM API: search for exact code match
    # The API returns [total_count, codes_array, extra, descriptions_array]
    params = {
        "sf": "code",
        "terms": code,
        "maxList": 10,
    }

    time.sleep(RATE_LIMIT_DELAY)
    result = _api_request(NLM_SEARCH_URL, params)

    if result is None:
        return {
            "exists": None,
            "hipaa_valid": None,
            "api_description": None,
            "error": "API request failed after retries",
        }

    try:
        total_count = result[0]
        codes_list = result[1]  # list of matching code strings
        descriptions_list = result[3]  # list of [code, description] pairs

        # Check for exact match
        exact_match = False
        api_desc = None

        for i, returned_code in enumerate(codes_list):
            if returned_code.upper() == code.upper():
                exact_match = True
                if i < len(descriptions_list):
                    api_desc = descriptions_list[i][1] if len(descriptions_list[i]) > 1 else None
                break

        # NLM API only returns billable codes, so if found, it's HIPAA valid
        return {
            "exists": exact_match,
            "hipaa_valid": exact_match,
            "api_description": api_desc,
            "error": None,
        }

    except (IndexError, KeyError, TypeError) as e:
        return {
            "exists": None,
            "hipaa_valid": None,
            "api_description": None,
            "error": f"Failed to parse API response: {e}",
        }


# ---------------------------------------------------------------------------
# Main validation logic
# ---------------------------------------------------------------------------

def validate_file(filepath: Path, verify: bool = False, quiet: bool = False) -> dict:
    """
    Validate all ICD-10 codes in a single file.

    Returns:
        {
            "file": str,
            "codes_found": int,
            "issues": [
                {"code": str, "severity": "error"|"warning"|"info", "message": str}
            ],
            "codes": [
                {"code": str, "description": str, "format_valid": bool,
                 "api_valid": bool|None, "api_description": str|None}
            ]
        }
    """
    codes = extract_icd10_from_file(filepath)
    result = {
        "file": str(filepath),
        "codes_found": len(codes),
        "issues": [],
        "codes": [],
    }

    if len(codes) == 0:
        result["issues"].append({
            "code": "",
            "severity": "warning",
            "message": "No ICD-10 codes found in file",
        })
        if not quiet:
            print(f"  ⚠  No ICD-10 codes found")
        return result

    seen_codes = set()
    for entry in codes:
        code = entry["code"]
        code_result = {
            "code": code,
            "description": entry["description"],
            "line_number": entry["line_number"],
            "format_valid": True,
            "api_valid": None,
            "api_description": None,
        }

        # Check for duplicates
        if code in seen_codes:
            result["issues"].append({
                "code": code,
                "severity": "info",
                "message": f"Duplicate code {code} in same file",
            })
        seen_codes.add(code)

        # Format validation (always runs)
        format_issues = validate_format(code)
        if format_issues:
            code_result["format_valid"] = False
            for issue in format_issues:
                severity = "warning" if "category" in issue.lower() else "error"
                result["issues"].append({
                    "code": code,
                    "severity": severity,
                    "message": issue,
                })
                if not quiet:
                    icon = "⚠ " if severity == "warning" else "✗"
                    print(f"  {icon} {code}: {issue}")

        # Online verification
        if verify:
            api_result = verify_code_nlm(code)
            code_result["api_valid"] = api_result["exists"]
            code_result["api_description"] = api_result["api_description"]

            if api_result["error"]:
                result["issues"].append({
                    "code": code,
                    "severity": "warning",
                    "message": f"API lookup failed: {api_result['error']}",
                })
                if not quiet:
                    print(f"  ⚠  {code}: API error — {api_result['error']}")

            elif not api_result["exists"]:
                result["issues"].append({
                    "code": code,
                    "severity": "error",
                    "message": f"Code {code} not found in NLM ICD-10-CM database "
                               f"(may be a category header or invalid code)",
                })
                if not quiet:
                    print(f"  ✗ {code}: NOT FOUND in NLM database")

            elif api_result["api_description"] and entry["description"]:
                # Check for description mismatch
                api_desc = api_result["api_description"].lower().strip()
                plan_desc = entry["description"].lower().strip()
                # Only flag if they're very different (not just abbreviation differences)
                if not _descriptions_similar(api_desc, plan_desc):
                    result["issues"].append({
                        "code": code,
                        "severity": "warning",
                        "message": f"Description mismatch for {code}: "
                                   f"plan says '{entry['description']}', "
                                   f"NLM says '{api_result['api_description']}'",
                    })
                    if not quiet:
                        print(f"  ⚠  {code}: description mismatch")
                        print(f"       Plan: {entry['description']}")
                        print(f"       NLM:  {api_result['api_description']}")
                else:
                    if not quiet:
                        print(f"  ✓ {code}: valid — {api_result['api_description']}")
            else:
                if not quiet:
                    desc = api_result["api_description"] or entry["description"] or code
                    print(f"  ✓ {code}: valid — {desc}")

        else:
            # Format-only mode
            if not format_issues and not quiet:
                print(f"  ✓ {code}: format OK — {entry['description'] or '(no description)'}")

        result["codes"].append(code_result)

    return result


def _descriptions_similar(a: str, b: str) -> bool:
    """
    Check if two ICD-10 descriptions are similar enough.
    Accounts for abbreviations, word reordering, etc.
    """
    # Normalize
    a = re.sub(r'[^a-z0-9\s]', '', a.lower())
    b = re.sub(r'[^a-z0-9\s]', '', b.lower())

    a_words = set(a.split())
    b_words = set(b.split())

    if not a_words or not b_words:
        return True  # Can't compare, don't flag

    # Check word overlap (Jaccard-like)
    overlap = len(a_words & b_words)
    total = len(a_words | b_words)

    # If more than 40% of words overlap, consider similar
    return (overlap / total) >= 0.35


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_markdown_report(results: list[dict]) -> str:
    """Generate a human-readable Markdown validation report."""
    lines = [
        "# ICD-10 Validation Report",
        "",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]

    total_codes = sum(r["codes_found"] for r in results)
    total_errors = sum(
        1 for r in results for i in r["issues"] if i["severity"] == "error"
    )
    total_warnings = sum(
        1 for r in results for i in r["issues"] if i["severity"] == "warning"
    )

    lines.extend([
        f"**Files scanned:** {len(results)}",
        f"**Total codes:** {total_codes}",
        f"**Errors:** {total_errors}",
        f"**Warnings:** {total_warnings}",
        "",
    ])

    # Errors section
    error_items = [
        (r["file"], i)
        for r in results
        for i in r["issues"]
        if i["severity"] == "error"
    ]
    if error_items:
        lines.extend(["## Errors", ""])
        lines.append("| File | Code | Issue |")
        lines.append("|------|------|-------|")
        for filepath, issue in error_items:
            fname = Path(filepath).name
            lines.append(f"| {fname} | `{issue['code']}` | {issue['message']} |")
        lines.append("")

    # Warnings section
    warning_items = [
        (r["file"], i)
        for r in results
        for i in r["issues"]
        if i["severity"] == "warning"
    ]
    if warning_items:
        lines.extend(["## Warnings", ""])
        lines.append("| File | Code | Issue |")
        lines.append("|------|------|-------|")
        for filepath, issue in warning_items:
            fname = Path(filepath).name
            lines.append(f"| {fname} | `{issue['code']}` | {issue['message']} |")
        lines.append("")

    # Summary by file
    lines.extend(["## Files Summary", ""])
    lines.append("| File | Codes | Errors | Warnings |")
    lines.append("|------|-------|--------|----------|")
    for r in sorted(results, key=lambda x: x["file"]):
        fname = Path(r["file"]).name
        errs = sum(1 for i in r["issues"] if i["severity"] == "error")
        warns = sum(1 for i in r["issues"] if i["severity"] == "warning")
        lines.append(f"| {fname} | {r['codes_found']} | {errs} | {warns} |")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def get_plan_files(include_drafts: bool = False) -> list[Path]:
    """Get all plan markdown files."""
    plans_dir = Path("docs/plans")
    drafts_dir = Path("docs/drafts")

    files = []
    if plans_dir.exists():
        files.extend(
            f for f in sorted(plans_dir.glob("*.md"))
            if f.name != "index.md"
        )
    if include_drafts and drafts_dir.exists():
        files.extend(
            f for f in sorted(drafts_dir.glob("*.md"))
            if f.name not in ("index.md", "queue.md")
        )

    return files


def main():
    parser = argparse.ArgumentParser(
        description="Validate ICD-10-CM codes in neuro-plans"
    )
    parser.add_argument(
        "files", nargs="*", help="Plan file(s) to validate"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Process all plans in docs/plans/"
    )
    parser.add_argument(
        "--drafts", action="store_true",
        help="Include docs/drafts/ when using --all"
    )
    parser.add_argument(
        "--lint", action="store_true",
        help="Offline format validation only (no API)"
    )
    parser.add_argument(
        "--verify", action="store_true",
        help="Verify codes against NLM ICD-10-CM API"
    )
    parser.add_argument(
        "--json", metavar="FILE",
        help="Write results to JSON file"
    )
    parser.add_argument(
        "--save-report", metavar="FILE",
        help="Write Markdown report to file"
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Suppress per-code output"
    )

    args = parser.parse_args()

    # Determine files to process
    if args.all:
        files = get_plan_files(include_drafts=args.drafts)
    elif args.files:
        files = [Path(f) for f in args.files]
    else:
        parser.error("Specify file(s) or use --all")
        return

    if not files:
        print("No plan files found.")
        sys.exit(1)

    verify = args.verify  # --lint implies no verify
    if args.lint:
        verify = False

    print(f"ICD-10 Validation — {len(files)} file(s)")
    print(f"Mode: {'API verify' if verify else 'format lint'}")
    print("=" * 60)

    all_results = []
    total_errors = 0
    total_warnings = 0

    for filepath in files:
        if not filepath.exists():
            print(f"\n✗ File not found: {filepath}")
            continue

        if not args.quiet:
            print(f"\n{filepath.name}:")

        result = validate_file(filepath, verify=verify, quiet=args.quiet)
        all_results.append(result)

        errs = sum(1 for i in result["issues"] if i["severity"] == "error")
        warns = sum(1 for i in result["issues"] if i["severity"] == "warning")
        total_errors += errs
        total_warnings += warns

    # Summary
    total_codes = sum(r["codes_found"] for r in all_results)
    print("\n" + "=" * 60)
    print(f"SUMMARY: {total_codes} codes across {len(all_results)} files")
    print(f"  Errors:   {total_errors}")
    print(f"  Warnings: {total_warnings}")

    if total_errors > 0:
        print(f"\n⚠  {total_errors} error(s) found — review and fix before approval")

    # Write reports
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        print(f"\nJSON report saved to {args.json}")

    if args.save_report:
        report = generate_markdown_report(all_results)
        with open(args.save_report, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Markdown report saved to {args.save_report}")

    # Exit code: non-zero if errors
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
