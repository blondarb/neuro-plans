# Test Runbook

**runbook_version:** 1.0
**Last updated:** 2026-01-30

---

## Overview

This runbook defines how to test the Neuro Plans site. It is a **stable baseline** -- do not rewrite it each release. Each release gets a short **mission brief** (see `runs/RUN_TEMPLATE.md`) that references specific test case IDs from `TEST_CASES.yaml`.

### Tooling Model

| Role | Tool | Responsibility |
|------|------|----------------|
| **Planner** | VS Code + Claude Code | Select test cases for the release, write mission brief, review results |
| **Executor** | Claude Code for Chrome | Run test cases against the live site, record pass/fail |

**Workflow:** Planner writes a mission brief listing test case IDs to run. Executor opens the brief, runs those cases, and fills in the run log.

---

## 1. Smoke Tests (Run Every Deploy)

Minimum viable checks. If any fail, block the release.

| ID | Check | How |
|----|-------|-----|
| SMK-01 | Site loads | Open `https://blondarb.github.io/neuro-plans/` -- page renders, no errors |
| SMK-02 | Plans index loads | Navigate to Clinical Plans -- table of plans visible |
| SMK-03 | Clinical tool loads | Open Interactive Clinical Tool -- plan dropdown populates |
| SMK-04 | Plan data loads | Select any plan in clinical tool -- sections render with items |
| SMK-05 | Navigation works | Click 3 different plans from nav sidebar -- each renders |
| SMK-06 | Mobile renders | Resize to 375px width (or phone) -- layout not broken, nav hamburger works |
| SMK-07 | Search works | Use search bar, type a plan name -- results appear |

---

## 2. Regression Tests

Run after content or code changes. Grouped by feature area. Reference `TEST_CASES.yaml` for detailed steps.

### 2A. Plan Content Integrity

- Plans display correct title, ICD-10, STATUS
- No draft banners on approved plans
- Draft banners present on draft plans
- All 8 sections render (Labs, Imaging, Treatment, Recommendations, Differential, Monitoring, Disposition, Evidence)

### 2B. Clinical Tool

- Setting filters (ED/HOSP/OPD/ICU) show/hide correct items
- Priority badges display correct colors (STAT=red, URGENT=orange, ROUTINE=blue)
- Medication dosing badge clickable -- copies order sentence to clipboard
- Icon tooltips display on hover (rationale, indication, contraindications, etc.)
- Selected Items sidebar populates when items are checked
- Export/copy functionality works
- Custom items can be added

### 2C. JSON Integrity

- `plans.json` is valid JSON
- Each plan has required fields: `id`, `title`, `sections` (object), `notes` (array)
- Plan count in JSON matches plan count on site
- No duplicate plan keys

### 2D. Navigation & Structure

- `mkdocs.yml` nav entries match actual files in `docs/plans/`
- `docs/plans/index.md` categories match nav categories
- All nav links resolve (no 404s)

---

## 3. Role-Based Flows

### 3A. Physician (Mobile-First)

1. Open site on phone (or 375px viewport)
2. Navigate to a plan via hamburger menu
3. Scroll through all 8 sections -- content readable, tables scroll horizontally
4. Open clinical tool -- select a plan, apply ED filter
5. Select 5+ items -- sidebar shows selections
6. Copy plan -- paste into Notes app (or equivalent)

### 3B. Claude Code Session (Content Author)

1. Create or edit a draft plan in `docs/drafts/`
2. Run `python -X utf8 scripts/generate_json.py docs/drafts/<plan>.md --validate-only`
3. Run `--merge` to add to `plans.json`
4. Verify plan appears in clinical tool
5. Run `--check-parity` after moving to `docs/plans/`

### 3C. Reviewer (PR-Based)

1. Open PR on GitHub -- diff is readable
2. Changed `.md` files show expected metadata updates
3. `plans.json` diff shows new/updated plan entry
4. `mkdocs.yml` and `index.md` updated if new plan approved

---

## 4. Mobile-First Checklist

Run on a real device or Chrome DevTools mobile emulation.

| Viewport | Check |
|----------|-------|
| 375px (iPhone SE) | Nav hamburger works, plan tables horizontally scroll, clinical tool usable |
| 768px (iPad) | Sidebar visible, tables render without overflow |
| 1024px+ (Desktop) | Full layout, sidebar and content side-by-side |

---

## 5. How to Add Tests

1. Add the test case to `TEST_CASES.yaml` with the next available ID in its group
2. Reference the ID in future mission briefs as needed
3. Do not modify this runbook unless changing the testing framework itself
