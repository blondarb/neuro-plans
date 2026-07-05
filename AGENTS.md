# Neuro Plans

- **What it is:** Evidence-based clinical decision-support template site for neurological diagnoses,
  with an interactive Clinical Plan Builder tool. Companion iOS app is live on the App Store (v1.0).
- **Type:** code repo
- **Stack / tools:** Python (mkdocs-material, pyyaml) content pipeline; MkDocs site (GitHub Pages,
  auto-deploys from `main` via GitHub Actions); static HTML/JS interactive clinical tool; a Swift/
  Xcode iOS app under `ios/NeuroPlans/`.
- **How to run / test:** TODO: no verified install/run command found beyond `requirements.txt`
  (mkdocs-material, pyyaml) and `mkdocs.yml`; presumably `pip install -r requirements.txt` then
  `mkdocs serve`. iOS app has its own `project.yml`/`.xcodeproj` — no build command confirmed here.
- **Key files / structure:**
  - `docs/drafts/queue.md` — plans awaiting review
  - `docs/plans/index.md` — approved plans index
  - `docs/data/plans.json`, `docs/data/medications.json` — structured clinical data (936 meds)
  - `docs/clinical/index.html` — interactive clinical tool
  - `ios/NeuroPlans/` — companion iOS app (Xcode project)
  - `scripts/` — Python pipeline scripts (build, checker, citation/CPT enrichment, validation)
- **Conventions:** See CLAUDE.md (Draft Pipeline: queue → claim → checker → rebuilder → validate →
  JSON → citations → CPT/synonyms → mark completed; Approval Pipeline: copy to `docs/plans/` → update
  frontmatter → index/mkdocs → regenerate JSON with `--merge`/`--check-parity`). JSON schema: `notes`
  is always an array, `sections` is always an object. Medications use 10-column structured-dosing
  format with `::` separators. Quality target: 90%+ checker score.
- **Current focus / handoff notes:** as of 2026-07-05, status is Maintenance per CLAUDE.md. Recent
  commits migrated the iOS app's data-API calls from Supabase to the v2 REST API (see sibling repo
  `neuro-plans-v2`, the new AWS-native website for this same specialty). This repo (v1) and
  `clinical-plans-template` share the original mkdocs + iOS-app lineage — `clinical-plans-template`
  is a fork of this repo used as the starting point for new specialty sites.

<!-- Read by Claude Code, Claude Cowork, and OpenAI Codex. Auto-generated 2026-07-05 (Fable run); edit freely. -->
