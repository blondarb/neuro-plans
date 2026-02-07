# Developer Handoff & Support Guide

**Last Updated:** February 6, 2026
**Repository:** [github.com/blondarb/neuro-plans](https://github.com/blondarb/neuro-plans)
**Live Site:** [blondarb.github.io/neuro-plans](https://blondarb.github.io/neuro-plans/)

---

## Project Summary

Neuro Plans is a library of **124 evidence-based clinical decision support templates** for neurological diagnoses. Each plan provides structured recommendations for labs, imaging, treatments, monitoring, and disposition — organized by care setting (ED, Hospital, Outpatient, ICU) and priority level (STAT, URGENT, ROUTINE).

The site includes an **Interactive Clinical Plan Builder** that lets physicians filter, select, and export clinical items for patient care.

### By the Numbers

| Metric | Count |
|--------|-------|
| Approved plans | 124 |
| Clinical categories | 19 |
| Total clinical items | 12,784 |
| Medications with structured dosing | 3,507 |
| Evidence citations | 2,166 |
| Differential diagnoses | 1,666 |

---

## Architecture

### Stack

- **Static site:** MkDocs Material → GitHub Pages (auto-deploys from `main`)
- **Clinical tool:** Vanilla HTML/JS (`docs/clinical/index.html`) reading `docs/data/plans.json`
- **Comment system:** Firebase (section-specific inline comments)
- **Data pipeline:** Python scripts for markdown → JSON conversion, citation verification, and medication validation

### Key Directories

| Path | Purpose |
|------|---------|
| `docs/plans/` | 124 approved plan markdown files (source of truth) |
| `docs/plans/*.json` | Per-plan JSON files (generated, not hand-edited) |
| `docs/data/plans.json` | Combined JSON for the Clinical Plan Builder |
| `docs/drafts/` | Draft plans and `queue.md` tracking document |
| `docs/clinical/` | Interactive Clinical Plan Builder (HTML/JS) |
| `docs/skills/` | Public skill documentation and style guide |
| `skills/` | Source skill definitions (used by Claude Code) |
| `scripts/` | Python build/validation tools |
| `qa/` | Test runbook, test cases, release checklist, run logs |
| `references/` | Reference materials (LP guide, historical tracker) |
| `api-spec/` | API pipeline design docs (future capability) |

### Key Files

| File | Purpose |
|------|---------|
| `scripts/generate_json.py` | Markdown → JSON converter, validator, parity checker (~2,000 lines) |
| `scripts/verify_citations.py` | PubMed citation verifier and PMID repair tool (~1,260 lines) |
| `scripts/validate_medication.py` | RxNorm/OpenFDA medication validation (~820 lines) |
| `scripts/medication_resolver.py` | Central medication DB lookup and enrichment (~510 lines) |
| `scripts/extract_medications.py` | Extract unique medications from plan files (~200 lines) |
| `docs/data/medications.json` | Central medication database (936 medications; 11 fully validated, 925 harvested) |
| `docs/drafts/queue.md` | Canonical plan tracking (approval status, scores, dates) |
| `docs/plans/index.md` | Public index of all approved plans |
| `docs/ROADMAP.md` | Feature roadmap (medication format, clickable dosing) |
| `mkdocs.yml` | Site navigation and MkDocs configuration |
| `CLAUDE.md` | Claude Code instructions for this repo |

---

## How Plans Work

### Plan Structure (8 Sections)

Every plan follows this structure:

1. **Laboratory Workup** — Core labs, extended workup, specialized tests
2. **Diagnostic Imaging & Studies** — Essential and extended imaging
3. **Treatment** — Acute, maintenance, disease-modifying therapies (10-column tables)
4. **Other Recommendations** — Diagnosis-specific guidance
5. **Differential Diagnosis** — DDx with distinguishing features
6. **Monitoring Parameters** — What to track and when
7. **Disposition Criteria** — Admission, discharge, follow-up
8. **Evidence & References** — Citations with PubMed links

### Medication Format (v3.0)

All treatment tables use 10 columns:

```
| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
```

Dosing uses structured format: `[dose] :: [route] :: [frequency] :: [full_instructions]`

### JSON Schema

Each plan in `plans.json` follows this structure:

```json
{
  "plan-id": {
    "id": "plan-id",
    "title": "Plan Name",
    "version": "1.0",
    "icd10": [],
    "scope": "...",
    "notes": [],
    "sections": {},
    "differential": [],
    "evidence": [],
    "monitoring": [],
    "disposition": []
  }
}
```

Critical: `notes` must be an array (never string). `sections` must be an object (never array). Plans are keyed by `id` (not title).

---

## Common Operations

### Adding a New Plan

1. Create markdown in `docs/drafts/` following the style guide
2. Run the skill pipeline: Builder → Checker (≥90%) → Rebuilder → Citation Verifier → CPT/Synonym Enricher
3. Physician reviews and approves
4. Move file to `docs/plans/`
5. Add frontmatter `status: approved`
6. Add to `docs/plans/index.md` and `mkdocs.yml` nav
7. Update `docs/drafts/queue.md`
8. Generate JSON and verify:

```bash
python -X utf8 scripts/generate_json.py docs/plans/plan-name.md --merge
python -X utf8 scripts/generate_json.py docs/plans/plan-name.md --check-parity
```

### Regenerating All JSON

```bash
python -X utf8 scripts/generate_json.py --all --merge
python -X utf8 scripts/generate_json.py --all --check-parity
```

All 124 plans should pass parity.

### Verifying Citations

```bash
# Verify a single plan
python -X utf8 scripts/verify_citations.py docs/plans/plan-name.md --verify

# Verify all plans
python -X utf8 scripts/verify_citations.py --all --verify

# Find and fix wrong PMIDs
python -X utf8 scripts/verify_citations.py docs/plans/plan-name.md --verify --repair --apply

# Quiet mode with JSON report
python -X utf8 scripts/verify_citations.py --all --verify --quiet --json report.json
```

### Running Smoke Tests

See `qa/TEST_RUNBOOK.md`. Smoke tests (SMK-01 through SMK-07) are browser-based and should be run against the live site after every deploy to `main`.

### Deploying

The site auto-deploys via GitHub Pages when changes are pushed to `main`. There is no manual deploy step.

---

## Current State & Known Issues

### What's Working Well

- All 124 plans approved, JSON generated, parity verified
- Clinical Plan Builder functional with all plans
- Citation accuracy at 85.0% (1,054 verified + 417 partial out of 1,730)
- CPT codes and synonyms enriched across all plans
- Medication format v3.0: structured dosing across all plans (Roadmap Phases 1-3 complete)
- Medication validation: 1,048 entries validated against RxNorm/OpenFDA (417 confirmed drugs, 137 with black box warnings)
- Central medication database: 936 medications (11 API-validated with RxCUI provenance, 925 harvested from plans)
- QA framework v1.1 in place (56 test cases, 8 categories) with runbook, release checklist, and run logs

### Known Issues

| Issue | Severity | Details |
|-------|----------|---------|
| 256 citation mismatches remain | Low | Mostly bare "PubMed" citations with no author/journal/year (unsearchable). Plans affected: wilsons-disease, chronic-migraine, drug-induced-parkinsonism, neuro-behcets-disease, multiple-system-atrophy, low-pressure-headache, syncope, and others |
| 3 PMIDs don't exist in PubMed | Low | Likely retracted or removed articles |
| PubMed rate limiting | Operational | `verify_citations.py` uses 0.5s delay between API calls; large batch runs (50+ plans) may hit 429 errors. No API key configured — adding one would increase throughput (10 req/sec vs 3 req/sec) |
| `api-spec/` not yet implemented | Informational | API pipeline design docs exist but the automated generation API is not built yet — all plans are currently created through Claude Code sessions |

### Remaining Citation Work

The 256 remaining mismatches break down as:

- **~145 bare "PubMed" citations** — The citation text is just `[PubMed: 12345678](url)` with no author or journal info. These need the citation text enriched from PubMed metadata before they can be verified.
- **~11 guideline/trial citations** — Organization-authored citations (e.g., "AAN Guidelines 2019") where PubMed search by author doesn't work.
- **~100 search failures** — Author+journal+year was present but PubMed search returned no match. May be due to author name variations, journal name mismatches, or the paper genuinely not being in PubMed.

### Technical Debt

- `references/neuro-templates-tracker.md` is historical — `docs/drafts/queue.md` is the canonical tracker
- 107 draft files remain in `docs/drafts/` (mirrors of approved plans) — could be cleaned up
- No automated CI/CD tests — validation is manual via scripts
- Comment system (Firebase) credentials/config not documented in repo

---

## Scripts Reference

### `scripts/generate_json.py` (~2,000 lines)

The main data pipeline tool. Parses plan markdown into structured JSON.

| Flag | Purpose |
|------|---------|
| `--validate-only` | Check plan structure without generating output |
| `--merge` | Generate JSON and merge into `plans.json` |
| `--check-parity` | Verify markdown item counts match JSON |
| `--all` | Process all plans in `docs/plans/` |

Plans are keyed by `id` field in `plans.json` (not by title). This prevents duplicates when plan titles change.

Non-plan files (index.md, report files) are automatically filtered out.

### `scripts/verify_citations.py` (~1,260 lines)

PubMed citation verification and repair.

| Flag | Purpose |
|------|---------|
| `--verify` | Check each PMID against PubMed API metadata |
| `--repair` | Search PubMed for correct PMIDs when mismatches found |
| `--apply` | Write corrected PMIDs back to markdown files |
| `--confidence` | Minimum confidence for repairs: `high` (default) or `medium` |
| `--quiet` | Suppress per-plan detail, show only summary |
| `--json FILE` | Write results to JSON file |
| `--all` | Process all plans |

The verification compares citation text (author, journal, year) against PubMed ESummary data. The repair phase uses multi-strategy PubMed ESearch (author+journal+year → author+year → author+journal → author-only) to find correct PMIDs.

Rate limit: 0.5s between API calls (no API key). With an NCBI API key (set `NCBI_API_KEY` env var), throughput increases to 10 req/sec.

### `scripts/validate_medication.py` (~820 lines)

RxNorm/OpenFDA medication validation. Confirms drugs exist and checks for safety data.

| Flag | Purpose |
|------|---------|
| `--validate-db` | Validate medications in `medications.json` |
| `--batch-from-plans` | Validate all medications found in plan files |
| `--save-report FILE` | Save results to markdown report |
| `--quiet` | Suppress per-medication detail |

Uses RxNorm API (no key required, 20 req/sec limit) and OpenFDA API (no key required, 240 req/min limit).

### `scripts/medication_resolver.py` (~510 lines)

Central medication database lookup and enrichment. Resolves plan medication references against `docs/data/medications.json`.

### `scripts/extract_medications.py` (~200 lines)

Extracts unique medication names from all plan markdown files. Used by `validate_medication.py` for batch processing.

### Validating Medications

```bash
# Validate central DB (936 medications)
python3 scripts/validate_medication.py --validate-db

# Batch validate all plan medications (~1,048 unique entries, ~10 min)
python3 scripts/validate_medication.py --batch-from-plans --save-report docs/data/full-validation-report.md
```

---

## Quality Standards

- All plans require **90%+ validation score** (54/60) across 6 domains
- All C-codes (critical issues from checker) must be resolved
- All medications: individual rows, structured dosing, complete 10-column format
- Physician review required before clinical use
- Parity check must pass (markdown item counts = JSON item counts)

---

## Support Contacts & Resources

| Resource | Location |
|----------|----------|
| Style guide | `docs/skills/style-guide.md` |
| Workflow pipeline | `docs/skills/workflow.md` |
| Test runbook | `qa/TEST_RUNBOOK.md` |
| Test cases | `qa/TEST_CASES.yaml` |
| Release checklist | `qa/RELEASE_CHECKLIST.md` |
| Bug template | `qa/BUG_TEMPLATE.md` |
| Feature roadmap | `docs/ROADMAP.md` |
| Claude Code config | `CLAUDE.md` |
| Plan queue/tracking | `docs/drafts/queue.md` |
| Plans index | `docs/plans/index.md` |
| Medication validation handoff | `docs/data/MEDICATION_VALIDATION_HANDOFF.md` |
| Medication migration plan | `docs/data/MEDICATION_MIGRATION_PLAN.md` |
| Central medication DB | `docs/data/medications.json` |
| Sync handoff (latest) | `docs/data/SYNC_HANDOFF_2026-02-06.md` |

---

## Getting Started (New Developer)

1. Clone the repo: `git clone https://github.com/blondarb/neuro-plans.git`
2. Install MkDocs: `pip install mkdocs-material pyyaml`
3. Run local server: `mkdocs serve` (visit `http://localhost:8000`)
4. Read `CLAUDE.md` for workflow rules and conventions
5. Read `docs/skills/style-guide.md` for plan formatting
6. Read `qa/TEST_RUNBOOK.md` for testing procedures
7. Try generating JSON for one plan:
   ```bash
   python -X utf8 scripts/generate_json.py docs/plans/status-epilepticus.md --validate-only
   ```
8. Try verifying citations for one plan:
   ```bash
   python -X utf8 scripts/verify_citations.py docs/plans/status-epilepticus.md --verify
   ```
