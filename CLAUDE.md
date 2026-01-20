# Neuro Plans - Claude Code Instructions

This repository contains clinical decision support templates for neurological diagnoses. When starting a session, follow the workflow below.

## Automatic Workflow

### Step 1: Pull Latest Changes (CRITICAL)

**Before doing anything else**, pull the latest changes to see the current queue state:

```bash
git checkout main
git pull origin main
```

### Step 2: Check the Queue

Read `docs/drafts/queue.md` to find the **first** plan with status `pending`. Skip any plans marked `in_progress`.

### Step 3: Claim a Plan (ATOMIC - DO THIS IMMEDIATELY)

**You MUST commit and push your claim BEFORE starting any work.** This prevents race conditions.

```bash
# 1. Create your working branch
git checkout -b claude/review-<plan-name>-<session-id>

# 2. Edit docs/drafts/queue.md:
#    - Change your plan's status from "pending" to "in_progress"
#    - Add your session ID to the Session column
#    - Update the Last Updated date

# 3. Commit and push IMMEDIATELY
git add docs/drafts/queue.md
git commit -m "Claim <plan-name> for review"
git push -u origin claude/review-<plan-name>-<session-id>
```

**If push fails due to conflict:**
1. Run `git pull origin main --rebase`
2. Check queue.md again - your plan may have been claimed by another session
3. If claimed, pick the next `pending` plan and repeat

**Only proceed to Step 4 after your claim is pushed successfully.**

### Step 4: Run the Skills Pipeline

For each plan, execute these steps in order:

#### 4a. Checker (Validation)
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

#### 4b. Review Findings
Present the checker report to the user. Ask which revisions to approve:
- All revisions
- Specific revisions (by code)
- Modified revisions

#### 4c. Rebuilder (Apply Fixes)
1. Read `skills/neuro-rebuilder-SKILL.md` for rebuilder instructions
2. Apply approved revisions systematically
3. Update version number and change log
4. Save the updated plan

#### 4d. Re-validate
Run the checker again to confirm improvements. Iterate until score >= 90%.

#### 4e. Generate JSON
```bash
python scripts/generate_json.py docs/drafts/<plan>.md --validate-only
python scripts/generate_json.py docs/drafts/<plan>.md --merge
```

### Step 5: Update Queue

Mark the plan as `completed` in `docs/drafts/queue.md`. Update the Final Score column.

### Step 6: Commit and Push

Commit all changes with a descriptive message and push to the branch. Create a PR to merge into main.

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
