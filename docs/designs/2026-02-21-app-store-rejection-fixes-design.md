# App Store Rejection Fixes — Design Document

**Date:** 2026-02-21
**Status:** Approved
**Context:** NeuroPlans v1.0 rejected for Guidelines 3.1.1, 4.3, 5.1.1

---

## Problem

NeuroPlans v1.0 was rejected on Feb 15, 2026 for three guideline violations:

| Guideline | Issue |
|-----------|-------|
| 3.1.1 (Subscriptions) | Hardcoded price/period, missing legal text |
| 4.3 (Spam/Duplicates) | Neuro Plans and Cardio Plans too similar |
| 5.1.1 (Privacy) | Privacy manifest incomplete, debug print() statements |

The fix branch from the previous session was never pushed. This design covers implementing all fixes on `main`.

---

## Approach: Config Arrays in SpecialtyConfig

Add static arrays to `SpecialtyConfig.swift` for paywall features, quick actions, and header icon. This keeps the existing "edit one file per specialty" pattern intact without adding JSON loading or new models.

---

## Files to Modify (8)

### 1. SpecialtyConfig.swift
Add new config properties:
- `headerIcon: String` — SF Symbol for paywall/disclaimer header (`"brain.head.profile"` for neuro)
- `paywallFeatures: [(icon: String, title: String, description: String)]` — 6 features shown on paywall
- `quickActions: [(id: String, title: String, icon: String, planId: String)]` — 3-4 specialty shortcuts for home screen
- `supportEmail: String` — for settings/support contact

Neuro quick actions: Stroke Alert, Status Epilepticus, Acute Meningitis
Cardio quick actions (commented, for future): STEMI Alert, Acute PE, AFib

### 2. PaywallView.swift
- Replace hardcoded `Image(systemName: "brain.head.profile")` with `SpecialtyConfig.headerIcon`
- Replace 6 hardcoded `FeatureRow(...)` calls with `ForEach` over `SpecialtyConfig.paywallFeatures`

### 3. HomeView.swift
- Add horizontal scroll quick actions bar below SettingPicker, above section ForEach
- Each action shows icon + title in a tappable chip
- Tapping navigates to the linked plan via `planId`

### 4. PrivacyInfo.xcprivacy
Add collected data types to `NSPrivacyCollectedDataTypes`:
- Email Address — App Functionality, Not Linked, Not Tracking
- Purchase History — App Functionality, Not Linked, Not Tracking
- Device ID — App Functionality, Not Linked, Not Tracking

### 5. ReferenceStore.swift (lines 115, 127)
Replace `print(msg)` with `import os` + `Logger.warning(msg)`

### 6. ExamToolsView.swift (line 283)
Replace `print("Flash error: \(error)")` with `Logger.error("Flash error: \(error)")`

### 7. Configuration.storekit
- Add 14-day free trial introductory offer to annual subscription
- Update `_developerTeamID` from `"XXXXXXXXXX"` to `"92YUSSM83T"`
- Update `_applicationInternalID` from `"1234567890"` to `"6759209586"`
- Add subscription group localization for English (US)

### 8. Xcode scheme (verify only)
Confirm `Configuration.storekit` is wired into the run scheme (already confirmed: line 43 of NeuroPlans.xcscheme).

---

## Files to Create (2)

### 9. ios/scripts/ios-preflight.sh
Pre-submission validation script. Checks:
- No `print()` calls in Swift source (excluding tests)
- PrivacyInfo.xcprivacy exists and has NSPrivacyCollectedDataTypes entries
- SpecialtyConfig.swift has all required fields (headerIcon, paywallFeatures, quickActions)
- Legal URLs (terms, privacy) are reachable (curl check)
- No hardcoded price strings (e.g., "$12.99") in PaywallView.swift
- Configuration.storekit has non-placeholder team/app IDs
- Configuration.storekit has introductoryOffer configured
- Build number check (informational)

Exit with count of FAIL items. 0 = ready to submit.

### 10. ios/NeuroPlans/APP_STORE_DIFFERENTIATION.md
Documents how Neuro Plans differs from future Cardio Plans across:
- App icon and branding (brain vs heart, teal vs red)
- Header icon on paywall/disclaimer
- Paywall feature list (neuro-specific vs cardio-specific)
- Quick actions (Stroke Alert vs STEMI Alert)
- Exam tools (penlight, OKN stripes vs ECG, stethoscope)
- Clinical scales and calculators
- Categories and plan content
- Separate support email and legal docs

---

## Manual Steps (Post-Code, App Store Connect)

1. Update App Privacy labels: declare Email, Purchase History, Device ID
2. Configure introductory offer: 14-day free trial on annual subscription
3. Complete Agreements, Tax, and Banking
4. Create sandbox tester account
5. Test full purchase flow on device
6. Update review notes from APP_STORE_METADATA.md
7. Verify neuroplans.app/privacy and neuroplans.app/terms load
8. Archive build 1.0.0 (build 2), upload
9. Run ios-preflight.sh (must pass with 0 FAIL)
10. Submit for review

---

## Testing Plan

### Automated (preflight script)
- All checks listed in ios-preflight.sh section above

### Manual (simulator)
1. Launch app with StoreKit config active
2. Verify paywall shows dynamic price from StoreKit (not hardcoded)
3. Tap Subscribe Now → StoreKit purchase sheet appears
4. Complete purchase → paywall dismisses, full access granted
5. Kill/relaunch → subscription persists
6. Test Restore Purchases button
7. Verify quick actions on home screen navigate to correct plans
8. Verify no console print() output during normal use

---

## What We're NOT Changing (YAGNI)

These are Task 2 (CardioPlans) scope, not needed for resubmission:
- Category.swift (hardcoded neuro categories)
- Reference.swift (hardcoded neuro reference categories)
- ExamToolsView.swift tool list (hardcoded neuro exam tools)
- CalculatorEngine.swift (hardcoded neuro calculators)
