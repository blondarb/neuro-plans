# Neuro Plans - Claude Code Instructions

Clinical decision support templates for neurological diagnoses.

## Key Files

| File | Purpose |
|------|---------|
| `docs/drafts/queue.md` | Plans awaiting review |
| `docs/plans/index.md` | Approved plans index |
| `docs/data/plans.json` | JSON data for clinical tool |
| `mkdocs.yml` | Site navigation |
| `scripts/generate_json.py` | Markdown-to-JSON converter |
| `scripts/verify_citations.py` | PubMed citation verifier and PMID repair |
| `scripts/validate_icd10.py` | ICD-10-CM code validation (lint + NLM API) |
| `scripts/validate_medication.py` | RxNorm/OpenFDA medication validation |
| `scripts/medication_resolver.py` | Central medication DB lookup |
| `scripts/extract_medications.py` | Extract medications from plan files |
| `scripts/harvest_medications.py` | Harvest meds from plans into central DB |
| `scripts/generate_treatment_row.py` | Generate 10-column treatment table rows |
| `scripts/build.py` | Extracts plan metadata, generates index (runs during CI) |
| `scripts/convert_to_structured_dosing.py` | Normalize dosing to `::` format |
| `scripts/fix_dosing_frequency.py` | Fill missing frequency fields |
| `scripts/expand_dose_options.py` | Generate dose option ranges for clinical tool |
| `docs/data/medications.json` | Central medication database (936 meds) |
| `docs/clinical/index.html` | Interactive clinical tool (consumes plans.json) |
| `docs/ROADMAP.md` | Medication format & feature roadmap |
| `docs/HANDOFF.md` | Developer handoff & support guide |

## Skills

| Skill | File |
|-------|------|
| Builder | `skills/neuro-builder-SKILL.md` |
| Checker | `skills/neuro-checker-SKILL.md` |
| Rebuilder | `skills/neuro-rebuilder-SKILL.md` |
| Citation Verifier | `docs/skills/neuro-citation-verifier-skill.md` |
| CPT/Synonym Enricher | `docs/skills/neuro-cpt-synonym-enricher-skill.md` |
| Comment Review | `skills/neuro-comment-review-SKILL.md` |
| Style Guide | `docs/skills/style-guide.md` |

## Workflow

### Draft Pipeline
1. Check `docs/drafts/queue.md` for `pending` plans
2. Claim plan (set `in_progress`)
3. Run skills: checker -> rebuilder -> re-validate -> generate JSON -> citations -> CPT/synonyms
4. Mark `completed` in queue, commit and push

### Approval (Physician approves a completed plan)
1. Copy `docs/drafts/<plan>.md` to `docs/plans/<plan>.md`
2. Update metadata: frontmatter `status: approved`, remove draft banner, set STATUS line
3. Add to `docs/plans/index.md` and `mkdocs.yml` nav
4. Move from Queue to Approved table in `queue.md`
5. Regenerate JSON: `python -X utf8 scripts/generate_json.py docs/plans/<plan>.md --merge`
6. Parity check: `python -X utf8 scripts/generate_json.py docs/plans/<plan>.md --check-parity`
7. Commit, push, create PR, provide compare URL for mobile review

## JSON Schema (Critical)

```json
{
  "Plan Name": {
    "id": "plan-id", "title": "Plan Name", "version": "1.0",
    "icd10": [], "scope": "...",
    "notes": [],        // MUST be array
    "sections": {},     // MUST be object
    "differential": [], "evidence": [], "monitoring": [], "disposition": []
  }
}
```

`notes` = array (never string). `sections` = object (never array).

## Medication Format (v3.0)

All treatment tables use 10 columns:
```
| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
```

Structured dosing: `[dose] :: [route] :: [frequency] :: [full_instructions]`
Use `::` not `|`. First field = starting dose only.

## Table Layout Detection

`docs/assets/js/table-layout.js` detects venue column positions by reading header text and adds `data-venue-pos` attributes. CSS targets these attributes instead of column count. Three patterns:

- `last4` — venue cols are last 4 (treatment tables, some workup tables)
- `mid` — 4 venue cols at positions 2-5 (workup/imaging with ICU)
- `mid3` — 3 venue cols at positions 2-4 (LP/workup without ICU)

See `docs/skills/style-guide.md` for supported column layouts.

## Commands

```bash
# JSON generation & validation
python -X utf8 scripts/generate_json.py docs/drafts/<plan>.md --validate-only
python -X utf8 scripts/generate_json.py docs/drafts/<plan>.md --merge
python -X utf8 scripts/generate_json.py docs/plans/<plan>.md --check-parity

# Citation verification (requires internet for --verify)
python -X utf8 scripts/verify_citations.py docs/plans/<plan>.md --verify
python -X utf8 scripts/verify_citations.py docs/plans/<plan>.md --verify --repair --apply

# ICD-10 code validation
python -X utf8 scripts/validate_icd10.py docs/drafts/<plan>.md --lint
python -X utf8 scripts/validate_icd10.py docs/drafts/<plan>.md --verify
python -X utf8 scripts/validate_icd10.py --all --lint --quiet
python -X utf8 scripts/validate_icd10.py --all --verify --save-report docs/data/icd10-report.md

# Medication validation (requires internet)
python3 scripts/validate_medication.py --validate-db
python3 scripts/validate_medication.py --batch-from-plans --save-report docs/data/full-validation-report.md

# Medication harvest (expand central DB from plan data)
python -X utf8 scripts/harvest_medications.py --stats
python -X utf8 scripts/harvest_medications.py --preview
python -X utf8 scripts/harvest_medications.py --merge

# Treatment row generation (from central DB)
python -X utf8 scripts/generate_treatment_row.py <med-name> --header
python -X utf8 scripts/generate_treatment_row.py <med-name> --context <context-id>
python -X utf8 scripts/generate_treatment_row.py --indication "neuropathic pain"
```

Always use `-X utf8` flag on Windows.

## Quality Targets

- **90%+ score** (54/60) on checker
- All C-codes (critical issues) resolved
- All medications: individual rows, structured dosing, complete columns

## QA & Testing

All testing docs live in `/qa`. Do not duplicate test procedures elsewhere.

| Doc | Purpose |
|-----|---------|
| `qa/TEST_RUNBOOK.md` | Smoke, regression, role-based test procedures |
| `qa/TEST_CASES.yaml` | Structured test cases with IDs, steps, expected results |
| `qa/BUG_TEMPLATE.md` | Bug report template |
| `qa/RELEASE_CHECKLIST.md` | Pre-deploy and post-deploy checks |
| `qa/runs/RUN_TEMPLATE.md` | Per-release run log (copy for each run) |

**Rules:**
- Run smoke tests (SMK-01 through SMK-07) after every deploy to main
- Use `qa/RELEASE_CHECKLIST.md` for every PR merge
- File bugs using `qa/BUG_TEMPLATE.md` with a TEST_CASES.yaml reference
- Do not rewrite the runbook each release -- write a short mission brief in `qa/runs/`
- **Planner** (VS Code / Claude Code): selects test cases, writes mission brief
- **Executor** (Claude Code for Chrome): runs test cases against live site

## Git & Deploy

- Site auto-deploys from `main` via GitHub Actions (`.github/workflows/deploy.yml`)
- CI pipeline: `scripts/build.py` (generates index) → `mkdocs build` → GitHub Pages
- Always work on feature branches, merge via PR
- Use `gh pr create` and `gh pr merge` for PRs
- Provide `https://github.com/blondarb/neuro-plans/compare/main...<branch>` for mobile review
- Use `-X utf8` for all Python commands on Windows

## Clinical Tool & Comments

- **Clinical tool** (`docs/clinical/index.html`): Interactive plan viewer consuming `docs/data/plans.json`
- **Comment system** (`docs/assets/js/comments.js`): Firebase-backed inline comments for physician review
- **Data directory** (`docs/data/`): Source files (plans.json, medications.json) + auto-generated artifacts (.medication_cache.json, validation reports)

## Manual Override

> "Run the checker on docs/drafts/new-onset-seizure.md"
> "Skip the queue and work on the MS plan"
