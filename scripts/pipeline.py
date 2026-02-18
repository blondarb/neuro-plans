#!/usr/bin/env python3
"""
Pipeline orchestrator for neuro-plans.

Chains all validation, generation, and build steps together in the correct
order so that nothing is forgotten (e.g., regenerating JSON after updating
citations, or rebuilding the iOS bundle after JSON changes).

Usage:
    python3 scripts/pipeline.py                    # Full pipeline
    python3 scripts/pipeline.py --dry-run          # Validate only, no file changes
    python3 scripts/pipeline.py --skip-verify      # Skip PubMed API calls
    python3 scripts/pipeline.py --skip-build       # Skip Xcode build
    python3 scripts/pipeline.py --verbose          # Show subprocess output

Pipeline steps:
    1. Link landmark citations       (non-gate)
    2. Verify citations via PubMed   (GATE)
    3. Validate ICD-10 codes         (GATE)
    4. Validate medications           (non-gate)
    5. Generate JSON                  (GATE)
    6. Parity check                   (GATE)
    7. Enrich unlinked citations      (non-gate, PubMed API)
    8. Validate enriched citations    (non-gate)
    9. Copy plans.json to iOS bundle  (non-gate)
   10. Generate changelog             (non-gate, internal)
   11. Xcode build                    (GATE)

Gate steps halt the pipeline on failure. Non-gate steps log warnings
but allow the pipeline to continue.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Repo detection
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

# Walk up to find repo root (look for docs/plans/ as anchor)
_candidate = SCRIPT_DIR
for _ in range(10):
    if (_candidate / "docs" / "plans").is_dir():
        REPO_ROOT = _candidate
        break
    _candidate = _candidate.parent

PLANS_JSON = REPO_ROOT / "docs" / "data" / "plans.json"
IOS_PLANS_JSON = REPO_ROOT / "ios" / "NeuroPlans" / "NeuroPlans" / "Resources" / "plans.json"
CHANGELOG_JSON = REPO_ROOT / "docs" / "data" / "changelog.json"
IOS_CHANGELOG_JSON = REPO_ROOT / "ios" / "NeuroPlans" / "NeuroPlans" / "Resources" / "changelog.json"
XCODEPROJ = REPO_ROOT / "ios" / "NeuroPlans" / "NeuroPlans.xcodeproj"


# ---------------------------------------------------------------------------
# ANSI colour helpers
# ---------------------------------------------------------------------------

class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def _supports_color():
    """Return True when stdout is a terminal that likely supports ANSI."""
    if os.environ.get("NO_COLOR"):
        return False
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


USE_COLOR = _supports_color()


def c(code, text):
    """Wrap *text* in an ANSI colour code if the terminal supports it."""
    if USE_COLOR:
        return f"{code}{text}{Color.RESET}"
    return text


# ---------------------------------------------------------------------------
# Snapshot / changelog helpers
# ---------------------------------------------------------------------------

def snapshot_plans(path):
    """Read plans.json and return {plan_id: title} mapping."""
    if not path.is_file():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        result = {}
        for key, plan in data.items():
            plan_id = plan.get("id", key)
            title = plan.get("title", key)
            result[plan_id] = title
        return result
    except (json.JSONDecodeError, OSError):
        return {}


def generate_changelog(before, after, output_path, ios_path=None):
    """Compare before/after plan snapshots and write changelog JSON.

    Returns the changelog dict for display purposes.
    """
    before_ids = set(before.keys())
    after_ids = set(after.keys())

    new_ids = sorted(after_ids - before_ids)
    removed_ids = sorted(before_ids - after_ids)
    common_ids = before_ids & after_ids

    updated_ids = sorted(
        pid for pid in common_ids if before[pid] != after[pid]
    )

    changelog = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total_plans": len(after_ids),
            "new": len(new_ids),
            "updated": len(updated_ids),
            "removed": len(removed_ids),
            "unchanged": len(common_ids) - len(updated_ids),
        },
        "new": [{"id": pid, "title": after[pid]} for pid in new_ids],
        "updated": [
            {"id": pid, "old_title": before[pid], "new_title": after[pid]}
            for pid in updated_ids
        ],
        "removed": [{"id": pid, "title": before[pid]} for pid in removed_ids],
    }

    # Write changelog JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(changelog, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Copy to iOS bundle if target directory exists
    if ios_path and ios_path.parent.is_dir():
        shutil.copy2(output_path, ios_path)

    return changelog


# ---------------------------------------------------------------------------
# Step runner
# ---------------------------------------------------------------------------

# Status constants
PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"
SKIP = "SKIP"


def run_step(cmd, cwd, verbose=False):
    """Run a command as a subprocess, returning (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=600,  # 10-minute timeout per step
        )
        if verbose:
            if result.stdout.strip():
                print(result.stdout)
            if result.stderr.strip():
                print(result.stderr, file=sys.stderr)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        msg = f"Command not found: {cmd[0]}"
        if verbose:
            print(msg, file=sys.stderr)
        return 127, "", msg
    except subprocess.TimeoutExpired:
        msg = f"Step timed out after 600 seconds"
        if verbose:
            print(msg, file=sys.stderr)
        return 124, "", msg
    except OSError as exc:
        msg = f"OS error running step: {exc}"
        if verbose:
            print(msg, file=sys.stderr)
        return 1, "", msg


# ---------------------------------------------------------------------------
# Pipeline definition
# ---------------------------------------------------------------------------

def build_steps(args):
    """Return the ordered list of pipeline steps based on CLI flags.

    Each step is a dict with keys:
        num      - display number
        name     - human-readable label
        cmd      - list[str] command (None for internal steps)
        gate     - bool, whether failure halts the pipeline
        skip     - bool, whether this step should be skipped
        internal - str label for internal (non-subprocess) steps
    """
    dry = args.dry_run

    steps = []

    # 1 — Link landmark citations
    if dry:
        cmd1 = ["python3", "scripts/link_landmark_citations.py", "--all", "--report"]
    else:
        cmd1 = ["python3", "scripts/link_landmark_citations.py", "--all", "--apply"]
    steps.append({
        "num": 1,
        "name": "Link citations",
        "cmd": cmd1,
        "gate": False,
        "skip": False,
    })

    # 2 — Verify citations (PubMed API)
    steps.append({
        "num": 2,
        "name": "Verify citations",
        "cmd": ["python3", "scripts/verify_citations.py", "--all", "--verify"],
        "gate": True,
        "skip": args.skip_verify,
    })

    # 3 — Validate ICD-10 codes
    steps.append({
        "num": 3,
        "name": "Validate ICD-10",
        "cmd": ["python3", "scripts/validate_icd10.py", "--all"],
        "gate": True,
        "skip": False,
    })

    # 4 — Validate medications
    steps.append({
        "num": 4,
        "name": "Validate medications",
        "cmd": ["python3", "scripts/validate_medication.py", "--all"],
        "gate": False,
        "skip": False,
    })

    # 5 — Generate JSON
    if dry:
        cmd5 = ["python3", "scripts/generate_json.py", "--all", "--validate-only"]
    else:
        cmd5 = ["python3", "scripts/generate_json.py", "--all", "--merge"]
    steps.append({
        "num": 5,
        "name": "Generate JSON",
        "cmd": cmd5,
        "gate": True,
        "skip": False,
    })

    # 6 — Parity check
    steps.append({
        "num": 6,
        "name": "Parity check",
        "cmd": [
            "python3", "scripts/generate_json.py",
            "--all", "--check-parity", "--fail-on-parity",
        ],
        "gate": True,
        "skip": dry,  # parity check is meaningless in dry-run (JSON wasn't regenerated)
    })

    # 7 — Enrich unlinked citations (PubMed API)
    #     Runs after JSON generation so it can add PubMed links to plans.json.
    #     Non-gate: enrichment failures shouldn't block the build.
    #     Skipped in dry-run and when --skip-verify (both imply no API calls).
    if dry:
        cmd7 = ["python3", "scripts/enrich_json_citations.py", "--quiet"]
    else:
        cmd7 = ["python3", "scripts/enrich_json_citations.py", "--apply", "--quiet"]
    steps.append({
        "num": 7,
        "name": "Enrich citations",
        "cmd": cmd7,
        "gate": False,
        "skip": dry or args.skip_verify,
    })

    # 8 — Validate enriched citations (topic mismatch check)
    #     Quick post-enrichment sanity check — catches wrong-topic PMIDs.
    #     Report-only (--check), doesn't modify data.
    steps.append({
        "num": 8,
        "name": "Validate enrichment",
        "cmd": ["python3", "scripts/validate_enriched_citations.py", "--check"],
        "gate": False,
        "skip": dry or args.skip_verify,
    })

    # 9 — Copy plans.json to iOS bundle
    steps.append({
        "num": 9,
        "name": "Copy to iOS bundle",
        "cmd": None,  # handled internally (file copy)
        "gate": False,
        "skip": dry,
        "internal": "copy_plans",
    })

    # 10 — Generate changelog (internal diff)
    steps.append({
        "num": 10,
        "name": "Generate changelog",
        "cmd": None,
        "gate": False,
        "skip": dry,
        "internal": "changelog",
    })

    # 11 — Xcode build
    steps.append({
        "num": 11,
        "name": "Xcode build",
        "cmd": [
            "xcodebuild", "build",
            "-project", str(XCODEPROJ),
            "-scheme", "NeuroPlans",
            "-destination", "generic/platform=iOS Simulator",
            "-quiet",
        ],
        "gate": True,
        "skip": args.skip_build or dry,
    })

    return steps


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run the full neuro-plans pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate only — do not modify files or build",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help="Skip citation verification (PubMed API calls)",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Skip the Xcode build step",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print subprocess stdout/stderr in real time",
    )
    args = parser.parse_args()

    # -----------------------------------------------------------------------
    # Banner
    # -----------------------------------------------------------------------
    mode_parts = []
    if args.dry_run:
        mode_parts.append("dry-run")
    if args.skip_verify:
        mode_parts.append("skip-verify")
    if args.skip_build:
        mode_parts.append("skip-build")
    mode_label = f" ({', '.join(mode_parts)})" if mode_parts else ""

    print()
    print(c(Color.BOLD, f"=== Neuro-Plans Pipeline{mode_label} ==="))
    print(f"    Repo root: {REPO_ROOT}")
    print()

    # Sanity check — make sure we're in the right repo
    if not (REPO_ROOT / "docs" / "plans").is_dir():
        print(c(Color.RED, "ERROR: Cannot find docs/plans/ — are you in the right repo?"))
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Snapshot plans.json BEFORE generation (for changelog)
    # -----------------------------------------------------------------------
    plans_before = snapshot_plans(PLANS_JSON)

    # -----------------------------------------------------------------------
    # Run steps
    # -----------------------------------------------------------------------
    steps = build_steps(args)
    results = []  # list of (step_dict, status, duration, detail)
    failed_gate = False

    for step in steps:
        num = step["num"]
        name = step["name"]
        is_gate = step["gate"]

        # Already halted?
        if failed_gate:
            results.append((step, SKIP, 0.0, "skipped (earlier gate failed)"))
            continue

        # Explicitly skipped?
        if step["skip"]:
            label = c(Color.CYAN, f"[SKIP]")
            print(f"  {label}  Step {num}: {name}")
            results.append((step, SKIP, 0.0, "skipped by flag"))
            continue

        print(f"  {c(Color.DIM, '[....]')}  Step {num}: {name} ...", end="", flush=True)
        t0 = time.monotonic()

        # --- Internal steps ------------------------------------------------
        internal = step.get("internal")
        if internal == "copy_plans":
            # Copy plans.json to iOS bundle
            if PLANS_JSON.is_file() and IOS_PLANS_JSON.parent.is_dir():
                try:
                    shutil.copy2(PLANS_JSON, IOS_PLANS_JSON)
                    exit_code, detail = 0, "copied"
                except OSError as exc:
                    exit_code, detail = 1, str(exc)
            elif not PLANS_JSON.is_file():
                exit_code, detail = 1, f"plans.json not found at {PLANS_JSON}"
            else:
                exit_code, detail = 1, f"iOS Resources dir missing: {IOS_PLANS_JSON.parent}"
            elapsed = time.monotonic() - t0

        elif internal == "changelog":
            # Generate changelog by diffing before/after snapshots
            plans_after = snapshot_plans(PLANS_JSON)
            try:
                cl = generate_changelog(
                    plans_before, plans_after, CHANGELOG_JSON, IOS_CHANGELOG_JSON
                )
                stats = cl["stats"]
                detail = (
                    f"{stats['total_plans']} plans | "
                    f"+{stats['new']} new, ~{stats['updated']} updated, "
                    f"-{stats['removed']} removed"
                )
                exit_code = 0
            except OSError as exc:
                exit_code, detail = 1, str(exc)
            elapsed = time.monotonic() - t0

        # --- Subprocess steps ----------------------------------------------
        else:
            exit_code, stdout, stderr = run_step(
                step["cmd"], cwd=REPO_ROOT, verbose=args.verbose
            )
            elapsed = time.monotonic() - t0
            # Build a short detail string from the last non-empty output line
            output_lines = (stdout + stderr).strip().splitlines()
            detail = output_lines[-1].strip() if output_lines else ""
            # Truncate long detail for the summary
            if len(detail) > 120:
                detail = detail[:117] + "..."

        # --- Record result -------------------------------------------------
        if exit_code == 0:
            status = PASS
            tag = c(Color.GREEN, "[PASS]")
        elif is_gate:
            status = FAIL
            tag = c(Color.RED, "[FAIL]")
            failed_gate = True
        else:
            status = WARN
            tag = c(Color.YELLOW, "[WARN]")

        # Overwrite the "[....]" progress marker
        print(f"\r  {tag}  Step {num}: {name}  ({elapsed:.1f}s)")
        if status == FAIL and not args.verbose:
            # Print the last few lines of output for context
            if detail:
                for line in detail.splitlines()[-3:]:
                    print(f"         {c(Color.RED, line)}")

        results.append((step, status, elapsed, detail))

    # -----------------------------------------------------------------------
    # Summary table
    # -----------------------------------------------------------------------
    print()
    print(c(Color.BOLD, "--- Pipeline Summary ---"))
    print()

    col_num = 4
    col_status = 6
    col_gate = 5
    col_name = 24
    col_time = 8

    header = (
        f"  {'#':>{col_num}}  "
        f"{'Status':<{col_status}}  "
        f"{'Gate?':<{col_gate}}  "
        f"{'Step':<{col_name}}  "
        f"{'Time':>{col_time}}"
    )
    print(c(Color.DIM, header))
    print(c(Color.DIM, "  " + "-" * (col_num + col_status + col_gate + col_name + col_time + 12)))

    for step, status, elapsed, detail in results:
        # Colour the status
        if status == PASS:
            s = c(Color.GREEN, status)
        elif status == FAIL:
            s = c(Color.RED, status)
        elif status == WARN:
            s = c(Color.YELLOW, status)
        else:
            s = c(Color.CYAN, status)

        gate_label = "yes" if step["gate"] else ""
        time_str = f"{elapsed:.1f}s" if elapsed > 0 else "-"
        name = step["name"]

        # Pad status accounting for ANSI escape codes
        raw_status_len = len(status)
        status_padding = col_status - raw_status_len
        padded_status = s + " " * status_padding

        print(
            f"  {step['num']:>{col_num}}  "
            f"{padded_status}  "
            f"{gate_label:<{col_gate}}  "
            f"{name:<{col_name}}  "
            f"{time_str:>{col_time}}"
        )

    # -----------------------------------------------------------------------
    # Final verdict
    # -----------------------------------------------------------------------
    total_time = sum(r[2] for r in results)
    n_pass = sum(1 for r in results if r[1] == PASS)
    n_fail = sum(1 for r in results if r[1] == FAIL)
    n_warn = sum(1 for r in results if r[1] == WARN)
    n_skip = sum(1 for r in results if r[1] == SKIP)

    print()
    parts = []
    if n_pass:
        parts.append(c(Color.GREEN, f"{n_pass} passed"))
    if n_fail:
        parts.append(c(Color.RED, f"{n_fail} failed"))
    if n_warn:
        parts.append(c(Color.YELLOW, f"{n_warn} warnings"))
    if n_skip:
        parts.append(c(Color.CYAN, f"{n_skip} skipped"))
    summary_line = ", ".join(parts)

    print(f"  {summary_line}  ({total_time:.1f}s total)")
    print()

    if n_fail:
        print(c(Color.RED, "  PIPELINE FAILED — fix errors above and re-run."))
        print()
        sys.exit(1)
    elif n_warn:
        print(c(Color.YELLOW, "  Pipeline completed with warnings."))
        print()
        sys.exit(0)
    else:
        print(c(Color.GREEN, "  Pipeline completed successfully."))
        print()
        sys.exit(0)


if __name__ == "__main__":
    main()
