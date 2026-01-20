# Neuro Plans - Claude Code Instructions

This repository contains clinical decision support templates for neurological diagnoses. When starting a session, follow the workflow below.

## Automatic Workflow

### Step 1: Check the Queue

Read `docs/drafts/queue.md` to find plans awaiting review. Look for plans with status `pending` or `in_progress`.

### Step 2: Claim a Plan

If a plan is `pending`, update its status to `in_progress` and add your session ID. This prevents other sessions from working on the same plan.

### Step 3: Run the Skills Pipeline

For each plan, execute these steps in order:

#### 3a. Checker (Validation)
1. Read `skills/neuro-checker-SKILL.md` for validation instructions
2. Read the target plan from `docs/drafts/<plan>.md`
3. Validate against the 6 quality domains (target: 90%+)
4. Output a structured checker report with:
   - Scores for each domain
   - Critical issues (C-codes)
   - Setting coverage issues (S-codes)
   - Medication issues (M-codes)
   - Recommended revisions (R-codes)
   - Verification items (V-codes)

#### 3b. Review Findings
Present the checker report to the user. Ask which revisions to approve:
- All revisions
- Specific revisions (by code)
- Modified revisions

#### 3c. Rebuilder (Apply Fixes)
1. Read `skills/neuro-rebuilder-SKILL.md` for rebuilder instructions
2. Apply approved revisions systematically
3. Update version number and change log
4. Save the updated plan

#### 3d. Re-validate
Run the checker again to confirm improvements. Iterate until score >= 90%.

#### 3e. Generate JSON
```bash
python scripts/generate_json.py docs/drafts/<plan>.md --validate-only
python scripts/generate_json.py docs/drafts/<plan>.md --merge
```

### Step 4: Update Queue

Mark the plan as `completed` in `docs/drafts/queue.md`.

### Step 5: Commit and Push

Commit all changes with a descriptive message and push to the branch.

---

## Physician Approval Workflow

When the physician approves a plan (moves from `completed` to `approved`), execute ALL of the following steps:

### Step 6: Move Plan to Approved

#### 6a. Copy Plan File
```bash
cp docs/drafts/<plan>.md docs/plans/<plan>.md
```

#### 6b. Update Plan Metadata
Edit `docs/plans/<plan>.md`:
1. Change frontmatter `status: draft` → `status: approved`
2. Remove the draft warning banner (`<div class="admonition warning">...</div>`)
3. Update `STATUS:` line from "Draft - Pending Review" to "Approved"

#### 6c. Update Approved Plans Index
Edit `docs/plans/index.md`:
- Add the plan to the appropriate category table with setting coverage and status

#### 6d. Update Site Navigation
Edit `mkdocs.yml`:
- Move the plan from "Drafts for Review" section to "Approved Plans" section
- Update the file path from `drafts/<plan>.md` to `plans/<plan>.md`

#### 6e. Update Queue
Edit `docs/drafts/queue.md`:
- Remove plan from the Queue table
- Add plan to the "Approved" table with approved date and final score

#### 6f. Regenerate JSON
```bash
python scripts/generate_json.py docs/plans/<plan>.md --merge
```

#### 6g. Run Parity Check
```bash
python scripts/generate_json.py docs/plans/<plan>.md --check-parity
```
Verify output shows: `✅ PARITY CHECK PASSED`

#### 6h. Commit and Push
Commit all changes with message like:
```
Move <plan> to approved plans

- Copied from drafts to plans directory
- Updated status to approved
- Updated navigation and indexes
- Parity check passed
```

#### 6i. Merge to Main (Deploy)
The live site is built from the `main` branch. After pushing to your feature branch:
1. Create a Pull Request to merge into `main`
2. Merge the PR via GitHub
3. Wait 1-2 minutes for GitHub Pages to rebuild
4. Verify the plan loads in the clinical tool

---

## JSON Schema Requirements

The clinical tool (`docs/clinical/index.html`) expects a specific JSON structure. **If the structure is wrong, plans won't load.**

### Required Structure

```json
{
  "Plan Name": {
    "id": "plan-id",
    "title": "Plan Name",
    "version": "1.0",
    "icd10": ["G40.901"],
    "scope": "Description string...",
    "notes": [],           // MUST be array, NOT string
    "sections": {          // MUST be object/dict, NOT array
      "Section Name": {
        "Subsection Name": [
          {
            "item": "Item name",
            "ED": "STAT",
            "HOSP": "STAT",
            "OPD": "ROUTINE",
            "ICU": "STAT"
          }
        ]
      }
    },
    "differential": [],    // Top-level array
    "evidence": [],        // Top-level array
    "monitoring": [],      // Top-level array (optional)
    "disposition": []      // Top-level array (optional)
  }
}
```

### Critical Requirements

| Field | Type | Notes |
|-------|------|-------|
| `notes` | `array` | Must be `[]` or list of strings. **Never a string!** |
| `sections` | `object` | Must be `{name: {subsection: [items]}}`. **Never an array!** |
| `differential` | `array` | Top-level, not inside sections |
| `evidence` | `array` | Top-level, not inside sections |

### Verification

After generating JSON, verify the structure:
```bash
python3 -c "
import json
with open('docs/data/plans.json') as f:
    data = json.load(f)
plan = data['Plan Name']
print('notes type:', type(plan.get('notes')))      # Should be: <class 'list'>
print('sections type:', type(plan.get('sections'))) # Should be: <class 'dict'>
"
```

---

## Quick Reference

### Key Files

| File | Purpose |
|------|---------|
| `docs/drafts/queue.md` | Plans awaiting review |
| `docs/plans/index.md` | Approved plans index |
| `docs/data/plans.json` | JSON data for clinical tool |
| `mkdocs.yml` | Site navigation structure |
| `skills/neuro-checker-SKILL.md` | Validation instructions |
| `skills/neuro-rebuilder-SKILL.md` | Revision instructions |
| `scripts/generate_json.py` | Markdown to JSON converter + parity checker |

### Quality Targets

- **90%+ overall score** (54/60 points)
- All critical issues (C-codes) must be resolved
- All medications must have individual rows with complete dosing

### Commands

```bash
# Validate a plan (check structure, no output)
python scripts/generate_json.py docs/drafts/<plan>.md --validate-only

# Generate and merge JSON into plans.json
python scripts/generate_json.py docs/drafts/<plan>.md --merge

# Check parity between markdown and JSON (run after approval)
python scripts/generate_json.py docs/plans/<plan>.md --check-parity

# Build the site
python scripts/build.py
mkdocs build
```

---

## Manual Override

If you want to work on a specific plan regardless of the queue, just tell Claude:

> "Run the checker on docs/drafts/new-onset-seizure.md"

or

> "Skip the queue and work on the MS plan"
