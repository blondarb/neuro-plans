# Neuro Plans - Claude Code Instructions

This repository contains clinical decision support templates for neurological diagnoses. When starting a session, follow the workflow below.

## Automatic Workflow

### Step 1: Check the Queue

Read `docs/drafts/queue.md` to find plans awaiting review. Look for plans with status `pending` or `in_progress`.

### Step 2: Claim a Plan

If a plan is `pending`, update its status to `in_progress` and add your session ID. This prevents other sessions from working on the same plan.

### Step 3: Run the Skills Pipeline

Execute these phases in order. Each phase has a quality gate that must pass before proceeding.

---

#### Phase 1: VALIDATE (Checker)

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

**Quality Gate:** Must achieve ≥90% (54/60) to proceed

##### If Score <90%: REBUILD

1. Present the checker report to the user
2. Ask which revisions to approve (all, specific codes, or modified)
3. Read `skills/neuro-rebuilder-SKILL.md` for rebuilder instructions
4. Apply approved revisions systematically
5. Update version number and change log
6. Re-validate until score ≥90%

---

#### Phase 2: VERIFY CITATIONS

1. Read `docs/skills/neuro-citation-verifier-skill.md` for instructions
2. Extract all citations from Section 8 (Evidence & References)
3. Prioritize by safety impact:
   - **HIGH:** Drug dosing, contraindications, safety warnings
   - **MEDIUM:** Diagnostic criteria, treatment protocols
   - **LOW:** Epidemiology, background information
4. Web search to verify each HIGH priority citation
5. Flag each citation:
   - ✅ Verified - Citation exists and supports claim
   - ⚠️ Partial Match - Citation exists but claim needs adjustment
   - ❌ Not Found - Citation doesn't exist or can't be located
   - ❌ Inaccurate - Citation exists but doesn't support claim
6. Present verification report to user
7. Correct any flagged citations

**Quality Gate:** All HIGH priority citations must be verified or corrected

---

#### Phase 3: ENRICH (CPT/Synonyms)

1. Read `docs/skills/neuro-cpt-synonym-enricher-skill.md` for instructions
2. Identify all codeable items:
   - Laboratory tests
   - Imaging studies
   - Procedures (LP, EEG, etc.)
   - Infusions and injections
3. Search and verify CPT/HCPCS codes for each item
4. Collect clinical synonyms:
   - Abbreviations (CBC, CMP, MRI)
   - Brand names (Keppra for levetiracetam)
   - Lay terms (blood test, brain scan)
5. Generate enrichment data for JSON output

**Quality Gate:** All common procedures should have verified codes

---

#### Phase 4: Generate JSON

```bash
python scripts/generate_json.py docs/drafts/<plan>.md --validate-only
python scripts/generate_json.py docs/drafts/<plan>.md --merge
```

---

### Step 4: Update Queue

Update `docs/drafts/queue.md`:
- Change status from `in_progress` to `completed`
- Record final score in Completed table
- Note which phases were completed

### Step 5: Commit and Push

Commit all changes with a descriptive message and push to the branch.

---

## Pipeline Status Tracking

When updating queue.md, track pipeline progress:

| Status | Meaning |
|--------|---------|
| `pending` | Not started |
| `in_progress` | Currently being processed |
| `validated` | Phase 1 complete (≥90% score) |
| `citations_verified` | Phase 2 complete |
| `enriched` | Phase 3 complete |
| `completed` | All phases complete, ready for physician review |
| `approved` | Physician approved, move to `docs/plans/` |

---

## Quick Reference

### Key Files

| File | Purpose |
|------|---------|
| `docs/drafts/queue.md` | Plans awaiting review |
| `skills/neuro-checker-SKILL.md` | Phase 1: Validation instructions |
| `skills/neuro-rebuilder-SKILL.md` | Phase 1: Revision instructions |
| `docs/skills/neuro-citation-verifier-skill.md` | Phase 2: Citation verification |
| `docs/skills/neuro-cpt-synonym-enricher-skill.md` | Phase 3: CPT/synonym enrichment |
| `docs/skills/workflow.md` | Full workflow documentation |
| `scripts/generate_json.py` | Markdown to JSON converter |

### Quality Targets

- **Phase 1:** 90%+ overall score (54/60 points)
- **Phase 2:** All HIGH priority citations verified
- **Phase 3:** Common procedures have CPT codes

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

## Physician Approval

When a physician is ready to approve a plan:

1. User says: "Approve [Plan Name] and move to approved"
2. Move file from `docs/drafts/` to `docs/plans/`
3. Update `mkdocs.yml` nav to move plan to "Approved Plans" section
4. Remove draft warning banner from the plan
5. Update `queue.md` status to `approved`
6. Commit and push changes

---

## Manual Override

To work on a specific plan regardless of the queue:

> "Run the checker on docs/drafts/new-onset-seizure.md"

> "Skip the queue and work on the MS plan"

> "Run citation verification on the seizure plan"

> "Skip to Phase 3 (enrichment) for the seizure plan"
