# Neuro Plans - Claude Code Instructions

Clinical decision support templates for neurological diagnoses. MkDocs site auto-deploys from `main` via GitHub Actions. v1.0 live on App Store. Status: Maintenance.

## Key Files

| File | Purpose |
|------|---------|
| `docs/drafts/queue.md` | Plans awaiting review |
| `docs/plans/index.md` | Approved plans index |
| `docs/data/plans.json` | JSON data for clinical tool |
| `docs/data/medications.json` | Central medication database (936 meds) |
| `docs/clinical/index.html` | Interactive clinical tool (consumes plans.json) |
| `mkdocs.yml` | Site navigation |

## Skills

| Skill | File |
|-------|------|
| Builder | `skills/neuro-builder-SKILL.md` |
| Checker | `skills/neuro-checker-SKILL.md` |
| Rebuilder | `skills/neuro-rebuilder-SKILL.md` |
| Citation Verifier | `docs/skills/neuro-citation-verifier-skill.md` |
| CPT/Synonym Enricher | `docs/skills/neuro-cpt-synonym-enricher-skill.md` |
| Style Guide | `docs/skills/style-guide.md` |

## Workflow

**Draft Pipeline:** Check `docs/drafts/queue.md` for `pending` → claim (`in_progress`) → run checker → rebuilder → validate → generate JSON → citations → CPT/synonyms → mark `completed`, commit/push.

**Approval:** Copy draft to `docs/plans/`, update frontmatter (`status: approved`), add to `index.md` + `mkdocs.yml`, move in queue, regenerate JSON (`--merge` then `--check-parity`), commit/push/PR.

## JSON Schema (Critical)

```json
{ "Plan Name": { "id": "", "title": "", "version": "1.0", "icd10": [], "scope": "",
    "notes": [], "sections": {}, "differential": [], "evidence": [], "monitoring": [], "disposition": [] } }
```

`notes` = array (never string). `sections` = object (never array).

## Medication Format (v3.0)

10-column treatment tables: `| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |`

Structured dosing: `[dose] :: [route] :: [frequency] :: [full_instructions]`. Use `::` not `|`.

## Table Layout Detection

`docs/assets/js/table-layout.js` adds `data-venue-pos` attributes. Three patterns: `last4` (venue cols last 4), `mid` (positions 2-5), `mid3` (positions 2-4). See `docs/skills/style-guide.md`.

## Quality Targets

- **90%+ score** (54/60) on checker. All C-codes resolved. All meds: individual rows, structured dosing.

## On-Demand Reference

| Area | Read first |
|------|-----------|
| CLI commands | `docs/COMMANDS.md` |
| Guideline maintenance | `docs/GUIDELINE_MAINTENANCE.md` |
| Roadmap | `docs/ROADMAP.md` |
| Handoff | `docs/HANDOFF.md` |
| QA | `qa/TEST_RUNBOOK.md` |

## Deploy

Auto-deploys from `main` via GitHub Actions. CI: `scripts/build.py` → `mkdocs build` → GitHub Pages.

*Last updated: April 9, 2026*
