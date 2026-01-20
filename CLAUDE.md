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

## Quick Reference

### Key Files

| File | Purpose |
|------|---------|
| `docs/drafts/queue.md` | Plans awaiting review |
| `skills/neuro-checker-SKILL.md` | Validation instructions |
| `skills/neuro-rebuilder-SKILL.md` | Revision instructions |
| `scripts/generate_json.py` | Markdown to JSON converter |

### Quality Targets

- **90%+ overall score** (54/60 points)
- All critical issues (C-codes) must be resolved
- All medications must have individual rows with complete dosing

### Commands

```bash
# Validate a plan
python scripts/generate_json.py docs/drafts/<plan>.md --validate-only

# Generate and merge JSON
python scripts/generate_json.py docs/drafts/<plan>.md --merge

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
