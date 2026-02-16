# Neuro Plans / Clinical Plans Template Handoff — February 15, 2026

## Audience
Next Claude session or developer continuing template/Neuro Plans work.

## Current State

### Clinical Plans Template (`/Users/stevearbogast/dev/repos/clinical-plans-template/`)
- **Build status**: Compiles clean, launches in simulator without crashes
- **Branch**: `main` — 4 commits, all local (no remote yet)
- **Size**: 25MB (down from 250K+ lines of neurology content)
- **Status**: Ready to clone for any specialty

### Neuro Plans (`/Users/stevearbogast/dev/repos/neuro-plans/`)
- **Build status**: Compiles clean, launches in simulator without crashes
- **Branch**: `main` — up to date with `origin/main`
- **Uncommitted changes**: 13 modified files + 10 untracked files (Sprint 1 + Phase 1-2 work)
- **Status**: All Sprint 1 code changes work but have NOT been committed

### Environment
- Xcode: latest (building for iOS 17+ target)
- Simulator: iPhone 16 Pro (DA33D2DA-72AE-4907-A226-22B09B425A8C)
- Supabase project: cyaginuvsqcbvyeuizlu
- Python 3 (for content pipeline)

---

## Work Completed

### Sprint 1 Critical Fixes (in neuro-plans, uncommitted)
- Removed `fatalError()` calls from `ReferenceStore.swift` and `PlanStore.swift`
- Added error state handling in `PlanStore` and `ReferenceStore`
- Added error alert UI in `NeuroPlansApp.swift`
- Created `PrivacyInfo.xcprivacy` for App Store compliance

### Phase 1: Refactor Neuro Plans for SpecialtyConfig (Tasks 1-7, uncommitted)
| File | Change |
|------|--------|
| `SpecialtyConfig.swift` | NEW — centralizes app name, bundle ID, brand color, Supabase creds, legal URLs |
| `SupabaseService.swift` | Uses `SpecialtyConfig.supabaseUrl` and `.supabaseAnonKey` |
| `EntitlementService.swift` | Uses `SpecialtyConfig.storeKitProductId` |
| `ClinicalErrorService.swift` | Uses `SpecialtyConfig.errorReportEmail` |
| `Theme.swift` | Uses `SpecialtyConfig.brandColorHex` |
| `DisclaimerView.swift` | Uses `SpecialtyConfig.disclaimerTitle` |
| `PaywallView.swift` | Uses `SpecialtyConfig.appName` |
| `Plan.swift` | Added `CodingKeys` for JSON field mapping |
| `project.pbxproj` | Added SpecialtyConfig, PrivacyInfo, entitlements, test targets |

### Phase 2: Supabase Multi-Specialty (Task 8, applied to remote DB)
- Added `specialties text[]` column to `whitelisted_domains` table
- Added `specialty text` column to `verified_emails` table
- Updated RLS policies to filter by specialty
- Backfilled existing rows with `{neurology}`

### Phase 3: Template Repo (Tasks 9-15, committed locally)

| Commit | Description |
|--------|-------------|
| `cfccc24` | Initial template from Neuro Plans (120 files) |
| `070a621` | Replace neurology content with placeholders (259K lines removed, 379 added) |
| `e008846` | Setup guide and content authoring guide |
| `7920c8d` | Sample Markdown plan and pipeline verification |

Key template files:
| File | Purpose |
|------|---------|
| `SpecialtyConfig.swift` | TODO placeholders for new specialty |
| `Category.swift` | 3 sample categories (was 18 neurology) |
| `Reference.swift` | 1 sample per reference type |
| `CalculatorEngine.swift` | BMI calculator only (was 25+ calculators) |
| `Resources/plans.json` | 3 sample plans (was 250K lines) |
| `Resources/scales.json` | 1 sample scale |
| `Resources/exams.json` | 1 sample exam |
| `Resources/tools.json` | 1 BMI calculator |
| `SETUP_GUIDE.md` | 13-step setup guide |
| `CONTENT_GUIDE.md` | Full content authoring reference |
| `docs/plans/sample-acute-chest-pain.md` | Sample Markdown plan demonstrating all sections |

### Phase 4: Backport Verification (Task 16)
- Neuro Plans builds and launches with all SpecialtyConfig changes
- No crashes, graceful error handling confirmed

---

## What Was NOT Done
- **Neuro Plans changes not committed** — 13 modified + 10 untracked files need to be committed and pushed
- **Template repo has no remote** — needs `git remote add origin` and push to GitHub
- **Full QA runbook not executed** — plan called for SMK-01 through SMK-07; only build+launch verified
- **Xcode project not actually renamed** in template — documented in SETUP_GUIDE.md step 3 as manual step (plan specified "document only")

---

## Known Risks / Watch Items
1. **Supabase multi-specialty columns are live** — The `specialties` and `specialty` columns were added to the production DB. All existing rows backfilled with `{neurology}`. If new domains/emails are added without specifying specialty, they'll need the column populated.
2. **Template bundle ID** — The Xcode project still uses `com.neuroplans.app` as the build-time bundle ID. `SpecialtyConfig.bundleId` is a runtime reference. New specialty apps need to change the bundle ID in Xcode project settings (documented in SETUP_GUIDE.md).
3. **Validator warnings** — `generate_json.py` validation warns about missing "Diagnostic Imaging & Studies" (it expects that exact string vs "Imaging & Studies"). Cosmetic only — JSON structure is correct.

---

## Required Next Steps
1. **Commit Neuro Plans changes** — Stage and commit the Sprint 1 + Phase 1 changes (13 modified + 10 untracked files). Consider splitting into logical commits (Sprint 1 fixes, SpecialtyConfig refactor, docs/design files).
2. **Push Neuro Plans to origin** — After committing.
3. **Create GitHub repo for template** — `gh repo create blondarb/clinical-plans-template --private` then push.
4. **Run full QA smoke test** on Neuro Plans per `qa/TEST_RUNBOOK.md` (SMK-01 through SMK-07).
5. **Consider first specialty clone** — The template is ready for cardiology or any other specialty.

---

## Files to Review First
- `/Users/stevearbogast/dev/repos/neuro-plans/docs/designs/2026-02-15-clinical-plans-template-plan.md` — The 16-task implementation plan (all complete)
- `/Users/stevearbogast/dev/repos/clinical-plans-template/SETUP_GUIDE.md` — How to use the template
- `/Users/stevearbogast/dev/repos/clinical-plans-template/CONTENT_GUIDE.md` — How to author clinical content
- `/Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift` — The central config pattern
