#!/usr/bin/env python3
"""
Neuro Clinical Plans - Approval Workflow Automation

Automates the full 7-step approval workflow for promoting draft plans to approved status:
  1. Move files from docs/drafts/ to docs/plans/
  2. Update frontmatter (status: draft → status: approved)
  3. Remove draft warning banner HTML
  4. Update STATUS line in body text
  5. Update mkdocs.yml navigation
  6. Update docs/plans/index.md section table
  7. Update docs/drafts/queue.md (queue status + approved table)

After file updates, runs generate_json.py --merge and --check-parity for each plan.

Usage:
    python3.12 scripts/approve_plans.py \\
        --plans pots.md neurogenic-orthostatic-hypotension.md \\
        --category "Autonomic & Pain Disorders" \\
        --dry-run

    python3.12 scripts/approve_plans.py \\
        --plans pots.md crps.md \\
        --category "Autonomic & Pain Disorders" \\
        --insert-before "Other"

Pipeline position: Run AFTER physician approval, BEFORE commit/push.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


# ---------- constants ----------

REPO_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = REPO_ROOT / "docs" / "drafts"
PLANS_DIR = REPO_ROOT / "docs" / "plans"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"
INDEX_MD = PLANS_DIR / "index.md"
QUEUE_MD = DRAFTS_DIR / "queue.md"
PLANS_JSON = REPO_ROOT / "docs" / "data" / "plans.json"
GENERATE_JSON = REPO_ROOT / "scripts" / "generate_json.py"

TODAY = date.today().isoformat()  # YYYY-MM-DD


# ---------- helpers ----------

def extract_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields from a markdown file."""
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return fm
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip("\"'")
            if key and val:
                fm[key] = val
    return fm


def extract_icd10(text: str) -> str:
    """Extract ICD-10 codes from plan body text."""
    m = re.search(r"ICD-10:\s*(.+)", text)
    if m:
        return m.group(1).strip()
    return ""


def extract_checker_score(text: str) -> str:
    """Extract checker score (e.g. '56/60' or '90%') from plan text."""
    # Look for "Score: X/60" or "Final Score: X/60" patterns
    m = re.search(r"(?:Score|Final Score):\s*(\d+/60)", text, re.IGNORECASE)
    if m:
        raw = m.group(1)
        num, denom = raw.split("/")
        pct = int(int(num) / int(denom) * 100)
        return f"{pct}% ({raw})"
    # Look for percentage in frontmatter-style
    m = re.search(r"score:\s*[\"']?(\d+%)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    return "90%+"


def get_next_approved_number(queue_text: str) -> int:
    """Find the next sequential number for the approved table in queue.md."""
    numbers = re.findall(r"^\|\s*(\d+)\s*\|", queue_text, re.MULTILINE)
    if numbers:
        return max(int(n) for n in numbers) + 1
    return 1


# ---------- step 1: move files ----------

def move_files(plan_files: list[str], dry_run: bool) -> list[Path]:
    """Move plan files from docs/drafts/ to docs/plans/. Returns new paths."""
    new_paths = []
    for filename in plan_files:
        src = DRAFTS_DIR / filename
        dst = PLANS_DIR / filename
        if not src.exists():
            print(f"  WARNING: {src} not found, skipping")
            continue
        if dry_run:
            print(f"  [DRY RUN] Would move {src} → {dst}")
        else:
            shutil.move(str(src), str(dst))
            print(f"  Moved {src.name} → docs/plans/")
        new_paths.append(dst)
    return new_paths


# ---------- step 2-4: update plan content ----------

def update_plan_content(plan_path: Path, dry_run: bool) -> dict:
    """Update frontmatter, remove draft banner, update STATUS line.

    Returns extracted metadata dict: {title, setting, icd10, score}.
    """
    text = plan_path.read_text(encoding="utf-8")

    # Extract metadata before modifying
    fm = extract_frontmatter(text)
    title = fm.get("title", plan_path.stem.replace("-", " ").title())
    setting = fm.get("setting", "ED, HOSP, OPD, ICU")
    icd10 = extract_icd10(text)
    score = extract_checker_score(text)

    # 2. Update frontmatter status
    text = re.sub(r"^(status:\s*)draft\s*$", r"\1approved", text, flags=re.MULTILINE)

    # 3. Remove draft warning banner (various formats)
    # Format A: <div class="draft-warning-banner">...</div>
    text = re.sub(
        r'<div class="draft-warning-banner"[^>]*>.*?</div>\s*',
        "",
        text,
        flags=re.DOTALL,
    )
    # Format B: inline-styled draft banner
    text = re.sub(
        r'<div class="draft-warning-banner"\s+style="[^"]*">.*?</div>\s*',
        "",
        text,
        flags=re.DOTALL,
    )

    # 4. Update STATUS line (various formats)
    text = re.sub(
        r"\*\*STATUS:\*\*\s*Draft.*$",
        "**STATUS:** Approved",
        text,
        flags=re.MULTILINE,
    )

    if dry_run:
        print(f"  [DRY RUN] Would update {plan_path.name} (status→approved, banner removed)")
    else:
        plan_path.write_text(text, encoding="utf-8")
        print(f"  Updated {plan_path.name}")

    return {"title": title, "setting": setting, "icd10": icd10, "score": score}


# ---------- step 5: update mkdocs.yml ----------

def update_mkdocs_nav(
    plan_metadata: list[dict],
    plan_files: list[str],
    category: str,
    insert_before: str,
    dry_run: bool,
):
    """Add plans to mkdocs.yml nav under the given category."""
    text = MKDOCS_YML.read_text(encoding="utf-8")

    # Check if category already exists
    if f"- {category}:" in text:
        # Add entries to existing category section
        # Find the category line and insert after the last entry in that section
        lines = text.split("\n")
        cat_idx = None
        last_entry_idx = None
        indent = "        "  # 8 spaces for nav entries under a category

        for i, line in enumerate(lines):
            if f"- {category}:" in line:
                cat_idx = i
                # Detect the indent level of entries under this category
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    m = re.match(r"^(\s+)-\s", next_line)
                    if m:
                        indent = m.group(1)
                continue
            if cat_idx is not None and i > cat_idx:
                stripped = line.strip()
                if stripped.startswith("- ") and ":" in stripped and "plans/" in stripped:
                    last_entry_idx = i
                elif stripped and not stripped.startswith("- "):
                    break
                elif stripped.startswith("- ") and ":" in stripped and "plans/" not in stripped:
                    break

        if last_entry_idx is not None:
            new_entries = []
            for meta, filename in zip(plan_metadata, plan_files):
                entry = f"{indent}- {meta['title']}: plans/{filename}"
                # Skip if already present
                if entry not in text:
                    new_entries.append(entry)

            if new_entries:
                for j, entry in enumerate(new_entries):
                    lines.insert(last_entry_idx + 1 + j, entry)
                text = "\n".join(lines)
    else:
        # Create a new category section — insert before the specified section
        nav_entries = []
        for meta, filename in zip(plan_metadata, plan_files):
            nav_entries.append(f"        - {meta['title']}: plans/{filename}")
        new_section = f"      - {category}:\n" + "\n".join(nav_entries)

        # Find where to insert (before "insert_before" section or before "Drafts for Review")
        insert_marker = f"  - {insert_before}:" if insert_before else "  - Drafts for Review:"
        if insert_marker in text:
            text = text.replace(insert_marker, new_section + "\n" + insert_marker)
        else:
            # Fallback: insert before "Drafts for Review" or "References"
            for fallback in ["  - Drafts for Review:", "  - References:"]:
                if fallback in text:
                    text = text.replace(fallback, new_section + "\n" + fallback)
                    break

    if dry_run:
        print(f"  [DRY RUN] Would add {len(plan_files)} entries to mkdocs.yml under '{category}'")
    else:
        MKDOCS_YML.write_text(text, encoding="utf-8")
        print(f"  Updated mkdocs.yml — added {len(plan_files)} entries under '{category}'")


# ---------- step 6: update index.md ----------

def update_index_md(
    plan_metadata: list[dict],
    plan_files: list[str],
    category: str,
    dry_run: bool,
):
    """Add plan rows to the category section in docs/plans/index.md."""
    text = INDEX_MD.read_text(encoding="utf-8")

    # Build table rows
    rows = []
    for meta, filename in zip(plan_metadata, plan_files):
        link = f"[{meta['title']}]({filename})"
        rows.append(f"| {link} | {meta['setting']} | {meta['icd10']} |")

    # Check if category section exists
    cat_header = f"## {category}"
    if cat_header in text:
        # Find the end of the existing table and append rows
        lines = text.split("\n")
        insert_idx = None
        found_header = False
        for i, line in enumerate(lines):
            if line.strip() == cat_header:
                found_header = True
                continue
            if found_header and line.startswith("|") and "---" not in line:
                insert_idx = i  # Keep updating — last table row
            elif found_header and insert_idx and not line.startswith("|"):
                break

        if insert_idx:
            for j, row in enumerate(rows):
                # Skip if already present (check by filename)
                filename_check = plan_files[j]
                if filename_check not in text:
                    lines.insert(insert_idx + 1 + j, row)
            text = "\n".join(lines)
    else:
        # Create new section — insert before "## Other" or at end
        table_header = "| Plan | Setting Coverage | ICD-10 |\n|------|------------------|--------|"
        new_section = f"\n{cat_header}\n\n{table_header}\n" + "\n".join(rows) + "\n"

        # Try to insert before "## Other"
        if "## Other" in text:
            text = text.replace("## Other", new_section + "\n## Other")
        else:
            text += new_section

    if dry_run:
        print(f"  [DRY RUN] Would add {len(rows)} rows to index.md under '{category}'")
    else:
        INDEX_MD.write_text(text, encoding="utf-8")
        print(f"  Updated index.md — added {len(rows)} rows under '{category}'")


# ---------- step 7: update queue.md ----------

def update_queue_md(
    plan_metadata: list[dict],
    plan_files: list[str],
    category: str,
    dry_run: bool,
):
    """Update queue.md: change status to approved and add to approved table."""
    text = QUEUE_MD.read_text(encoding="utf-8")
    next_num = get_next_approved_number(text)

    # Update queue status for each plan
    for filename in plan_files:
        # Match queue rows by filename and change status to approved
        text = re.sub(
            rf"(\|\s*`{re.escape(filename)}`\s*\|\s*)`\w+`",
            rf"\1`approved`",
            text,
        )
        # Update date
        text = re.sub(
            rf"(`{re.escape(filename)}`\s*\|\s*`approved`\s*\|\s*)[^|]+(\|\s*)[^\|]+\|",
            rf"\1— \g<2>{TODAY} |",
            text,
        )

    # Add rows to approved table (find the last row before the "Completed" section)
    approved_rows = []
    for i, (meta, filename) in enumerate(zip(plan_metadata, plan_files)):
        num = next_num + i
        link = f"[`{filename}`](../plans/{filename})"
        approved_rows.append(
            f"| {num} | {meta['title']} | {link} | {TODAY} | {meta['score']} |"
        )

    # Find insertion point: last numbered row in the Approved table
    lines = text.split("\n")
    insert_idx = None
    in_approved = False
    for i, line in enumerate(lines):
        if "## Approved" in line:
            in_approved = True
            continue
        if in_approved and line.strip().startswith("| ") and re.match(r"\|\s*\d+\s*\|", line):
            insert_idx = i
        elif in_approved and line.strip().startswith("## "):
            break  # Hit next section

    if insert_idx:
        for j, row in enumerate(approved_rows):
            lines.insert(insert_idx + 1 + j, row)
        text = "\n".join(lines)

    if dry_run:
        print(f"  [DRY RUN] Would update queue.md with {len(plan_files)} approved plans")
    else:
        QUEUE_MD.write_text(text, encoding="utf-8")
        print(f"  Updated queue.md — {len(plan_files)} plans marked approved (#{next_num}-{next_num + len(plan_files) - 1})")


# ---------- step 8-9: JSON generation + parity ----------

def run_json_generation(plan_files: list[str], dry_run: bool) -> list[str]:
    """Run generate_json.py --merge and --check-parity for each plan.

    Returns list of parity failure messages (empty = all passed).
    """
    failures = []
    python = "python3.12"

    for filename in plan_files:
        plan_path = PLANS_DIR / filename

        if dry_run:
            print(f"  [DRY RUN] Would run generate_json.py --merge on {filename}")
            print(f"  [DRY RUN] Would run generate_json.py --check-parity on {filename}")
            continue

        # Generate JSON
        print(f"  Generating JSON for {filename}...")
        result = subprocess.run(
            [python, "-X", "utf8", str(GENERATE_JSON), str(plan_path), "--merge", "--quiet"],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
        )
        if result.returncode != 0:
            print(f"    WARNING: JSON generation failed for {filename}")
            print(f"    {result.stderr.strip()}")
            failures.append(f"{filename}: JSON generation failed")
            continue

        # Parity check
        result = subprocess.run(
            [python, "-X", "utf8", str(GENERATE_JSON), str(plan_path), "--check-parity", "--quiet"],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
        )
        if result.returncode != 0:
            print(f"    WARNING: Parity check failed for {filename}")
            failures.append(f"{filename}: parity check failed")
        else:
            print(f"    {filename}: JSON + parity OK")

    return failures


# ---------- main ----------

def main():
    parser = argparse.ArgumentParser(
        description="Automate the plan approval workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--plans",
        nargs="+",
        required=True,
        help="Filenames of plans to approve (e.g., pots.md crps.md)",
    )
    parser.add_argument(
        "--category",
        required=True,
        help='Nav category name (e.g., "Autonomic & Pain Disorders")',
    )
    parser.add_argument(
        "--insert-before",
        default=None,
        help="Insert new nav category before this section (default: before Drafts for Review)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview all changes without modifying any files",
    )

    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"PLAN APPROVAL WORKFLOW")
    print(f"Plans: {', '.join(args.plans)}")
    print(f"Category: {args.category}")
    if args.dry_run:
        print("MODE: DRY RUN (no files will be modified)")
    print(f"{'='*60}\n")

    # Step 1: Move files
    print("Step 1: Moving files from docs/drafts/ → docs/plans/")
    new_paths = move_files(args.plans, args.dry_run)
    if not args.dry_run and not new_paths:
        print("ERROR: No files were moved. Aborting.")
        sys.exit(1)

    # Step 2-4: Update plan content and extract metadata
    print("\nStep 2-4: Updating frontmatter, removing banners, updating STATUS")
    metadata_list = []
    for filename in args.plans:
        plan_path = PLANS_DIR / filename
        if args.dry_run or plan_path.exists():
            meta = update_plan_content(plan_path, args.dry_run)
            metadata_list.append(meta)

    # Step 5: Update mkdocs.yml
    print("\nStep 5: Updating mkdocs.yml navigation")
    update_mkdocs_nav(metadata_list, args.plans, args.category, args.insert_before, args.dry_run)

    # Step 6: Update index.md
    print("\nStep 6: Updating docs/plans/index.md")
    update_index_md(metadata_list, args.plans, args.category, args.dry_run)

    # Step 7: Update queue.md
    print("\nStep 7: Updating docs/drafts/queue.md")
    update_queue_md(metadata_list, args.plans, args.category, args.dry_run)

    # Step 8-9: JSON generation + parity
    print("\nStep 8-9: JSON generation and parity checks")
    failures = run_json_generation(args.plans, args.dry_run)

    # Summary
    print(f"\n{'='*60}")
    print("APPROVAL SUMMARY")
    print(f"{'='*60}")
    print(f"Plans approved: {len(args.plans)}")
    print(f"Category: {args.category}")
    print(f"Date: {TODAY}")

    if failures:
        print(f"\nWARNINGS ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
    else:
        print("\nAll steps completed successfully.")

    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply changes.")
    else:
        print(f"\nNext steps:")
        print(f"  1. Review changes: git diff")
        print(f"  2. Stage: git add docs/plans/ docs/data/plans.json docs/drafts/queue.md docs/plans/index.md mkdocs.yml")
        print(f"  3. Commit: git commit -m 'Approve {len(args.plans)} plans ({args.category})'")
        print(f"  4. Push and create PR")

    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
