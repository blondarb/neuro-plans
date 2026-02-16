# Clinical Plans Template — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extract a reusable template repo from Neuro Plans so any medical specialty can be cloned, configured, and shipped as an independent iOS app.

**Architecture:** Clone Neuro Plans into a new `clinical-plans-template` repo. Introduce `SpecialtyConfig.swift` to centralize all specialty-specific values. Replace hardcoded references across 5 services and 3 views. Update shared Supabase tables with a `specialties` column. Include the content pipeline, QA framework, and a setup guide.

**Tech Stack:** Swift 5.9 / SwiftUI / iOS 17+ / Supabase / StoreKit 2 / Python 3 (content pipeline)

**Design doc:** `docs/designs/2026-02-15-clinical-plans-template-design.md`

---

## Phase 1: Refactor Neuro Plans (prep for extraction)

These tasks modify the Neuro Plans repo to use `SpecialtyConfig.swift`. This makes it easy to extract and also improves Neuro Plans itself.

---

### Task 1: Create SpecialtyConfig.swift

**Files:**
- Create: `ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift`

**Step 1: Create the config file**

```swift
import Foundation

/// All specialty-specific values in one place.
/// To create a new specialty app, clone this repo and edit only this file
/// (plus Category.swift, Reference.swift, and CalculatorEngine.swift for content).
enum SpecialtyConfig {
    // MARK: - Identity
    static let appName = "Neuro Plans"
    static let specialty = "neurology"
    static let bundleId = "com.neuroplans.app"

    // MARK: - Branding
    static let brandColorHex = "#0D9488"

    // MARK: - Subscription
    static let storeKitProductId = "com.neuroplans.annual"

    // MARK: - Error Reporting
    static let errorReportEmail = "errors@neuroplans.app"

    // MARK: - Supabase
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5YWdpbnV2c3FjYnZ5ZXVpemx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMDY5NjUsImV4cCI6MjA4NjU4Mjk2NX0.UGJN-vnfGy7eECbmT33g4-OXME-2bbwC9sm3ckOmpWA"

    // MARK: - Legal
    static let termsURL = "https://neuroplans.app/terms"
    static let privacyURL = "https://neuroplans.app/privacy"
    static let disclaimerTitle = "Neuro Plans"
}
```

**Step 2: Add to Xcode project**

Add `SpecialtyConfig.swift` to the Xcode project's `project.pbxproj` — add PBXFileReference, PBXBuildFile, PBXGroup (in the NeuroPlans root group, after `NeuroPlansApp.swift`), and PBXSourcesBuildPhase entries.

**Step 3: Build to verify**

Run: `xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet`
Expected: Build succeeds (file exists but nothing references it yet)

**Step 4: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift ios/NeuroPlans/NeuroPlans.xcodeproj/project.pbxproj
git commit -m "feat: add SpecialtyConfig.swift centralizing specialty-specific values"
```

---

### Task 2: Wire SupabaseService to SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Services/SupabaseService.swift`

**Step 1: Replace hardcoded URL and key**

In `SupabaseService.swift`, change:
```swift
static let client = SupabaseClient(
    supabaseURL: URL(string: "https://cyaginuvsqcbvyeuizlu.supabase.co")!,
    supabaseKey: "eyJhbG..."
)
```

To:
```swift
static let client = SupabaseClient(
    supabaseURL: URL(string: SpecialtyConfig.supabaseUrl)!,
    supabaseKey: SpecialtyConfig.supabaseAnonKey
)
```

**Step 2: Build to verify**

Run: `xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet`
Expected: Build succeeds

**Step 3: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/Services/SupabaseService.swift
git commit -m "refactor: wire SupabaseService to SpecialtyConfig"
```

---

### Task 3: Wire EntitlementService to SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Services/EntitlementService.swift`

**Step 1: Replace hardcoded product ID**

Change line 56:
```swift
static let annualSubscriptionID = "com.neuroplans.annual"
```

To:
```swift
static let annualSubscriptionID = SpecialtyConfig.storeKitProductId
```

**Step 2: Build and commit**

```bash
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
git add ios/NeuroPlans/NeuroPlans/Services/EntitlementService.swift
git commit -m "refactor: wire EntitlementService to SpecialtyConfig"
```

---

### Task 4: Wire ClinicalErrorService to SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Services/ClinicalErrorService.swift`

**Step 1: Replace hardcoded email**

Change line 117:
```swift
static let reportEmailAddress = "errors@neuroplans.app"
```

To:
```swift
static let reportEmailAddress = SpecialtyConfig.errorReportEmail
```

**Step 2: Update test expectation**

In `ios/NeuroPlans/NeuroPlansTests/ClinicalErrorServiceTests.swift`, update the test that checks the email address to reference `SpecialtyConfig.errorReportEmail` instead of the hardcoded string.

**Step 3: Build and commit**

```bash
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
git add ios/NeuroPlans/NeuroPlans/Services/ClinicalErrorService.swift ios/NeuroPlans/NeuroPlansTests/ClinicalErrorServiceTests.swift
git commit -m "refactor: wire ClinicalErrorService to SpecialtyConfig"
```

---

### Task 5: Wire Theme to SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Theme/Theme.swift`

**Step 1: Add a helper to parse hex color and use it for the brand color**

Add at the bottom of `Theme.swift`:
```swift
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let r, g, b: Double
        r = Double((int >> 16) & 0xFF) / 255.0
        g = Double((int >> 8) & 0xFF) / 255.0
        b = Double(int & 0xFF) / 255.0
        self.init(red: r, green: g, blue: b)
    }
}
```

Then change the brand color lines:
```swift
static let teal = Color(hex: SpecialtyConfig.brandColorHex)
```

Keep `tealDark` and `tealLight` as computed variants or leave them as-is (they are only used in a few places and a template user can adjust).

**Step 2: Build and commit**

```bash
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
git add ios/NeuroPlans/NeuroPlans/Theme/Theme.swift
git commit -m "refactor: wire Theme brand color to SpecialtyConfig"
```

---

### Task 6: Wire Views to SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Views/DisclaimerView.swift`
- Modify: `ios/NeuroPlans/NeuroPlans/Views/Subscription/PaywallView.swift`

**Step 1: Update DisclaimerView**

Change line 15:
```swift
Text("Neuro Plans")
```
To:
```swift
Text(SpecialtyConfig.appName)
```

**Step 2: Update PaywallView**

Change lines 238-239:
```swift
Link("Terms of Service", destination: URL(string: "https://neuroplans.app/terms")!)
Link("Privacy Policy", destination: URL(string: "https://neuroplans.app/privacy")!)
```
To:
```swift
Link("Terms of Service", destination: URL(string: SpecialtyConfig.termsURL)!)
Link("Privacy Policy", destination: URL(string: SpecialtyConfig.privacyURL)!)
```

**Step 3: Build and commit**

```bash
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
git add ios/NeuroPlans/NeuroPlans/Views/DisclaimerView.swift ios/NeuroPlans/NeuroPlans/Views/Subscription/PaywallView.swift
git commit -m "refactor: wire DisclaimerView and PaywallView to SpecialtyConfig"
```

---

### Task 7: Verify Neuro Plans still works end-to-end

**Step 1: Full build for device**

Run: `xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "id=00008140-0000146C0A53001C" -quiet`
Expected: Build succeeds

**Step 2: Install and launch on iPhone**

```bash
xcrun devicectl device install app --device 4A7995D3-2659-5A11-9BB3-08A43D34FDA7 <path-to-built-app>
xcrun devicectl device process launch --device 4A7995D3-2659-5A11-9BB3-08A43D34FDA7 com.neuroplans.app
```

**Step 3: Quick smoke test**

Verify: app launches, plans load, categories display, settings show subscription status, disclaimer shows app name correctly.

---

## Phase 2: Update Supabase for multi-specialty

---

### Task 8: Add specialty columns to Supabase tables

**Step 1: Apply migration to add `specialties` column to `whitelisted_domains`**

```sql
ALTER TABLE public.whitelisted_domains
  ADD COLUMN specialties text[] NOT NULL DEFAULT ARRAY['all'];
```

**Step 2: Apply migration to add `specialty` column to `verified_emails`**

```sql
ALTER TABLE public.verified_emails
  ADD COLUMN specialty text NOT NULL DEFAULT 'neurology';
```

**Step 3: Verify with Supabase security advisors**

Run security and performance advisors to confirm no new warnings.

**Step 4: Update SupabaseService.swift to pass specialty**

In `SupabaseService.swift`:

Update `fetchWhitelistedDomains()` to filter by specialty:
```swift
static func fetchWhitelistedDomains(for specialty: String) async throws -> [String] {
    let domains: [WhitelistedDomain] = try await client
        .from("whitelisted_domains")
        .select()
        .eq("is_active", value: true)
        .or("specialties.cs.{\(specialty)},specialties.cs.{all}")
        .execute()
        .value

    return domains.map { $0.domain }
}
```

Update `recordVerifiedEmail` to include specialty:
```swift
struct VerifiedEmailRecord: Encodable {
    let email: String
    let domain: String
    let isWhitelisted: Bool
    let specialty: String

    enum CodingKeys: String, CodingKey {
        case email, domain, specialty
        case isWhitelisted = "is_whitelisted"
    }
}

static func recordVerifiedEmail(email: String, domain: String, isWhitelisted: Bool) async throws {
    let record = VerifiedEmailRecord(
        email: email,
        domain: domain,
        isWhitelisted: isWhitelisted,
        specialty: SpecialtyConfig.specialty
    )
    try await client.from("verified_emails").insert(record).execute()
}
```

Update `EntitlementService.swift` to pass specialty when calling `fetchWhitelistedDomains`:
```swift
let domains = try await SupabaseService.fetchWhitelistedDomains(for: SpecialtyConfig.specialty)
```

**Step 5: Build, test, commit**

```bash
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
git add ios/NeuroPlans/NeuroPlans/Services/SupabaseService.swift ios/NeuroPlans/NeuroPlans/Services/EntitlementService.swift
git commit -m "feat: add multi-specialty support to Supabase integration"
```

---

## Phase 3: Create the template repo

---

### Task 9: Create the template repo on GitHub

**Step 1: Create new repo**

```bash
cd /Users/stevearbogast/dev/repos
gh repo create blondarb/clinical-plans-template --private --clone
```

**Step 2: Copy Neuro Plans into the template**

Copy the entire `neuro-plans/` structure into the new repo, preserving the directory layout. Exclude:
- `.git/` directory
- `docs/plans/*.md` and `docs/plans/*.json` (neurology content — keep only one sample plan)
- `docs/data/plans.json` (generated neurology plans)
- `qa/runs/` (neurology-specific test run logs)
- `qa/STEEL-MAN-2026-02-15.md` (neurology-specific report)
- `docs/HANDOFF_*.md` (session-specific)
- `docs/designs/` (neurology-specific design docs)

**Step 3: Commit the initial copy**

```bash
cd clinical-plans-template
git add -A
git commit -m "feat: initial template from Neuro Plans"
```

---

### Task 10: Replace neurology content with placeholders

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift` — replace with placeholder values
- Modify: `ios/NeuroPlans/NeuroPlans/Models/Category.swift` — replace with 3 sample categories
- Modify: `ios/NeuroPlans/NeuroPlans/Models/Reference.swift` — replace category registries with samples
- Modify: `ios/NeuroPlans/NeuroPlans/Services/CalculatorEngine.swift` — keep only 1 sample calculator (BMI)
- Replace: `ios/NeuroPlans/NeuroPlans/Resources/plans.json` — 3 sample plans
- Replace: `ios/NeuroPlans/NeuroPlans/Resources/scales.json` — 1 sample scale
- Replace: `ios/NeuroPlans/NeuroPlans/Resources/exams.json` — 1 sample exam
- Replace: `ios/NeuroPlans/NeuroPlans/Resources/tools.json` — 1 sample tool (BMI calculator)

**Step 1: Update SpecialtyConfig with placeholder values**

```swift
enum SpecialtyConfig {
    static let appName = "MY_SPECIALTY Plans"          // TODO: Replace
    static let specialty = "my_specialty"               // TODO: Replace
    static let bundleId = "com.myspecialty.plans"        // TODO: Replace
    static let brandColorHex = "#3B82F6"                // TODO: Pick a color
    static let storeKitProductId = "com.myspecialty.annual" // TODO: Replace
    static let errorReportEmail = "errors@myspecialty.app"  // TODO: Replace
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "..."                  // Shared Supabase project
    static let termsURL = "https://myspecialty.app/terms"   // TODO: Replace
    static let privacyURL = "https://myspecialty.app/privacy" // TODO: Replace
    static let disclaimerTitle = "MY_SPECIALTY Plans"     // TODO: Replace
}
```

**Step 2: Create sample data files**

Create minimal but valid JSON files with 1-3 items each that demonstrate the schema. Include comments in the setup guide explaining each field.

**Step 3: Replace Category.swift with sample categories**

Replace the 18 neurology categories with 3 generic samples:
```swift
static let all: [PlanCategory] = [
    PlanCategory(id: "category-1", name: "Category 1", icon: "heart.fill", color: "red", planIds: ["sample-plan-1"]),
    PlanCategory(id: "category-2", name: "Category 2", icon: "lungs.fill", color: "blue", planIds: ["sample-plan-2"]),
    PlanCategory(id: "category-3", name: "Category 3", icon: "brain.fill", color: "purple", planIds: ["sample-plan-3"]),
]
```

**Step 4: Build to verify template compiles**

Run: `xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet`

**Step 5: Commit**

```bash
git add -A
git commit -m "feat: replace neurology content with template placeholders"
```

---

### Task 11: Rename Xcode project references

**Step 1: Rename generic references**

The Xcode project folder is named `NeuroPlans` and the app entry point is `NeuroPlansApp.swift`. For the template, these should be renamed to `ClinicalPlans` or left as-is with a note in the setup guide to rename them.

**Recommendation:** Leave the folder/file names as `NeuroPlans` in the template and document the renaming process in `SETUP_GUIDE.md`. Renaming an Xcode project involves updating 20+ entries in `project.pbxproj` and is error-prone — the setup guide will explain how to do it in Xcode's UI (File > Rename Project) which handles all references automatically.

**Step 2: Commit** (if any changes made)

---

### Task 12: Write SETUP_GUIDE.md

**Files:**
- Create: `SETUP_GUIDE.md` (template repo root)

**Content outline:**

1. **Prerequisites** — Xcode 16+, Apple Developer account, Supabase account access, Python 3
2. **Clone and rename** — `gh repo create`, Xcode File > Rename Project
3. **Configure SpecialtyConfig.swift** — every field explained with examples
4. **Define categories** — how to edit `Category.swift` and `Reference.swift`
5. **Author clinical content** — link to `CONTENT_GUIDE.md`, explain the Markdown plan format, JSON schemas for scales/exams/tools
6. **Implement calculators** — how to add formulas to `CalculatorEngine.swift`
7. **Update app icon** — replace `Assets.xcassets/AppIcon`
8. **Configure App Store Connect** — create app entry, subscription product, screenshots
9. **Configure StoreKit** — update `Configuration.storekit` with new product ID
10. **Run QA** — reference `qa/TEST_RUNBOOK.md`
11. **Submit to App Store** — reference `PUBLISHING_GUIDE.md`

**Step 1: Write the guide**

**Step 2: Commit**

```bash
git add SETUP_GUIDE.md
git commit -m "docs: add setup guide for new specialty apps"
```

---

### Task 13: Write CONTENT_GUIDE.md

**Files:**
- Create: `CONTENT_GUIDE.md` (template repo root)

**Content outline:**

1. **Plan authoring format** — Markdown structure with 10-column treatment tables, section headers, ICD-10 codes
2. **JSON schemas** — documented schemas for plans.json, scales.json, exams.json, tools.json with field-by-field descriptions
3. **Content pipeline** — how to run `scripts/generate_json.py`, validators
4. **Quality checklist** — ICD-10 validation, citation verification, medication name checking
5. **Examples** — link to the sample plan in `docs/plans/`

**Step 1: Write the guide**

**Step 2: Commit**

```bash
git add CONTENT_GUIDE.md
git commit -m "docs: add content authoring guide"
```

---

### Task 14: Clean up template repo and create sample plan

**Files:**
- Create: `docs/plans/sample-acute-chest-pain.md` — one sample plan in Markdown format showing the authoring structure
- Verify: `scripts/generate_json.py` works on the sample plan
- Clean: remove any neurology-specific docs, handoff files, design docs

**Step 1: Create sample Markdown plan**

Write a simple, generic "Acute Chest Pain" sample plan that demonstrates all sections (labs, imaging, treatment, other recs, differential, monitoring, disposition, evidence) with 2-3 items each.

**Step 2: Run the pipeline**

```bash
python3 scripts/generate_json.py docs/plans/sample-acute-chest-pain.md
```

Verify it produces valid JSON.

**Step 3: Commit**

```bash
git add -A
git commit -m "feat: add sample plan and verify content pipeline"
```

---

### Task 15: Final template verification

**Step 1: Build the template from clean state**

```bash
cd /Users/stevearbogast/dev/repos/clinical-plans-template
xcodebuild build -project ios/NeuroPlans/NeuroPlans.xcodeproj -scheme NeuroPlans -destination "generic/platform=iOS Simulator" -quiet
```

Expected: Build succeeds with placeholder data.

**Step 2: Launch in simulator**

Install and launch in iOS Simulator. Verify:
- App launches with placeholder app name
- Sample plans display in the plan list
- Plan detail view shows all sections correctly
- Sample scale works (scoring components render)
- Sample calculator works (computes result)
- Settings tab shows trial status
- No crashes

**Step 3: Push to GitHub**

```bash
git push -u origin main
```

---

## Phase 4: Backport SpecialtyConfig to Neuro Plans

---

### Task 16: Cherry-pick or merge the SpecialtyConfig refactor back to Neuro Plans

The Phase 1 changes (Tasks 1-7) were made directly in the Neuro Plans repo, so they're already there. Verify that Neuro Plans still builds and runs correctly with the refactored config.

**Step 1: Run full QA smoke test on Neuro Plans**

Reference `qa/TEST_RUNBOOK.md`, execute SMK-01 through SMK-07.

**Step 2: Commit any remaining changes and push**

---

## Summary

| Phase | Tasks | Estimated Time | Description |
|-------|-------|----------------|-------------|
| Phase 1 | Tasks 1-7 | ~2 hours | Refactor Neuro Plans to use SpecialtyConfig |
| Phase 2 | Task 8 | ~30 min | Update Supabase for multi-specialty |
| Phase 3 | Tasks 9-15 | ~3-4 hours | Create and populate template repo |
| Phase 4 | Task 16 | ~30 min | Verify Neuro Plans still works |
| **Total** | **16 tasks** | **~6-7 hours** | |

After this plan is complete, the template is ready to clone for cardiology (or any specialty). The cardiology content authoring is a separate effort — estimated at 40-80 hours of clinical content creation depending on the number of plans.
