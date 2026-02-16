# Clinical Plans Template — Design Document

**Date:** 2026-02-15
**Status:** Approved
**Goal:** Create a reusable template repo from Neuro Plans that can be cloned and customized for any medical specialty (starting with cardiology).

---

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Repo strategy | Template repo (clone per specialty) | Independent App Store submissions, no merge conflicts, supports future collaborators |
| Content pipeline | Include Markdown-to-JSON toolchain | Faster authoring at scale, built-in validators catch errors before they reach the app |
| Backend | Shared Supabase project | One place for domain whitelisting, institutions get cross-specialty access naturally |
| Priority | Template first, then cardiology | Proves the template works before committing specialty content |

---

## 1. Template Repo Structure

The template repo (`clinical-plans-template`) is a clean copy of the Neuro Plans iOS app with all neurology-specific content replaced by placeholders and configuration points.

### What gets templated (edit per specialty)

- **`SpecialtyConfig.swift`** — single file containing app name, bundle ID, brand color, StoreKit product ID, error report email, Supabase credentials, specialty identifier, disclaimer text
- **`Category.swift`** — plan categories (e.g., "Heart Failure", "Arrhythmias" for cardiology)
- **`CalculatorEngine.swift`** — calculator formula implementations
- **`Reference.swift`** — reference category registries (scale, exam, tool categories)
- **`Resources/*.json`** — clinical data files (plans, scales, exams, tools)
- **`Assets.xcassets`** — app icon

### What stays unchanged

- All Views (entire UI shell)
- PlanStore, ReferenceStore, PlanBuilder, StopwatchService, UserPreferences
- EntitlementService, SubscriptionService (read config from SpecialtyConfig)
- SupabaseService (read config from SpecialtyConfig)
- ClinicalErrorService (read config from SpecialtyConfig)
- Theme structure (brand color comes from SpecialtyConfig)
- Plan.swift, all item type models
- PrivacyInfo.xcprivacy, entitlements
- QA framework (runbook, test cases, bug templates)
- Content pipeline (Python scripts, validators)

---

## 2. SpecialtyConfig.swift

Centralizes all specialty-specific values that are currently scattered across multiple files:

```swift
enum SpecialtyConfig {
    static let appName = "Cardio Plans"           // or "Neuro Plans", etc.
    static let specialty = "cardiology"            // identifier for Supabase
    static let bundleId = "com.cardioplans.app"
    static let brandColorHex = "#DC2626"           // red for cardiology
    static let storeKitProductId = "com.cardioplans.annual"
    static let errorReportEmail = "errors@cardioplans.app"
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "..."
    static let disclaimerText = "..."
}
```

All services and views reference this config instead of hardcoded values.

---

## 3. Shared Supabase Backend

### Table changes

**`whitelisted_domains`** — add `specialties` column (text array):
- `["all"]` — institution has access to every specialty app
- `["neurology", "cardiology"]` — institution has access to specific apps
- Existing rows default to `["all"]` during migration

**`verified_emails`** — add `specialty` column (text):
- Tracks which app a verification came from
- Existing rows default to `"neurology"`

### App behavior

The app passes `SpecialtyConfig.specialty` when:
- Checking domain whitelist (filter where `specialties` contains the specialty OR `"all"`)
- Recording email verifications (set `specialty` column)

### RLS policy update

The INSERT policy on `verified_emails` already restricts to own email. The SELECT on `whitelisted_domains` remains open to authenticated users (they only see domain names, not emails).

---

## 4. Content Pipeline

Included in the template:

- `scripts/generate_json.py` — Markdown-to-JSON converter
- `scripts/validate_icd10.py` — ICD-10 code validator
- `scripts/validate_citations.py` — citation link validator
- `docs/data/medications.json` — 936-medication cross-specialty database
- `docs/plans/` — empty, with one sample `.md` showing the authoring format
- `CONTENT_GUIDE.md` — how to author plans, scales, exams, and tools

### Data schema

The four-section plan structure is universal across specialties:
- Laboratory Workup
- Imaging & Studies
- Treatment
- Other Recommendations

The four venue priorities (ED, HOSP, OPD, ICU) are universal.

Reference content types (scales, exams, tools with calculators/protocols/tables) are universal.

---

## 5. QA Framework

Included in the template:

- `qa/TEST_RUNBOOK.md` — smoke tests adapted with placeholder app name/URLs
- `qa/TEST_CASES.yaml` — generic test cases
- `qa/BUG_TEMPLATE.md` — bug report template (unchanged)
- `qa/RELEASE_CHECKLIST.md` — pre/post deploy checks (unchanged)
- Unit test stubs for PlanStore, CalculatorEngine, EntitlementService, ClinicalErrorService

---

## 6. Setup Workflow

To spin up a new specialty:

1. Clone `clinical-plans-template` into a new repo (e.g., `cardio-plans`)
2. Edit `SpecialtyConfig.swift` — set name, color, bundle ID, product ID, email
3. Define plan categories in `Category.swift`
4. Define reference categories in `Reference.swift`
5. Author clinical content:
   - Plans as Markdown in `docs/plans/`, run pipeline to generate `plans.json`
   - Scales, exams, tools as JSON directly in `Resources/`
6. Implement calculator formulas in `CalculatorEngine.swift`
7. Update app icon in `Assets.xcassets`
8. Create App Store Connect entry and StoreKit subscription product
9. Run QA runbook
10. Submit to App Store

A `SETUP_GUIDE.md` in the template root documents each step in detail.

---

## 7. Backport to Neuro Plans

After the template is created, Neuro Plans itself should adopt `SpecialtyConfig.swift` so it follows the same pattern. This is a non-breaking refactor — extract hardcoded values into the config, no behavior change.

---

## 8. Future Specialties

The same template supports any inpatient/outpatient clinical specialty:
- Cardiology, Pulmonology, Nephrology, Gastroenterology, Rheumatology, Infectious Disease, Endocrinology, Hematology/Oncology, etc.

The data schema, venue system, and UI are universal. Only the clinical content and branding change.
