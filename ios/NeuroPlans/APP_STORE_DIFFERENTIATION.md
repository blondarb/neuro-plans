# App Store Differentiation Strategy

## Problem

Apple App Store Guideline 4.3 (Spam) rejects apps that are near-identical clones
from the same developer. When both Neuro Plans and Cardio Plans were submitted,
Apple's review team flagged the shared codebase, identical UI structure, and
same developer account.

## Root Cause Analysis

Out of 48 Swift source files, **28 were byte-for-byte identical** between
the two apps. Only 6 files required code changes; the rest were either
identical or merely read a different value from `SpecialtyConfig`. Apple's
automated similarity scanning and manual review both catch this pattern.

### What Apple's Reviewer Sees (Before This Fix)

| Area | Neuro Plans | Cardio Plans | Identical? |
|------|-------------|--------------|------------|
| Home screen layout | Same | Same | YES |
| Tab bar (5 tabs) | Same | Same | YES |
| Disclaimer screen | brain icon, "Clinical Decision Support" | brain icon, "Clinical Decision Support" | YES |
| Paywall features | "NIHSS, mRS, GCS" hardcoded | "NIHSS, mRS, GCS" hardcoded | YES |
| Settings > About | "neurological diagnoses" hardcoded | "neurological diagnoses" hardcoded | YES |
| Exam tools | Penlight, OKN, Amsler Grid | Same (neuro tools in cardio app!) | YES |
| Emergency protocols | None | None | N/A |
| Brand color | Teal | Teal (default) | YES |
| Support email | support@neuroplans.app | support@neuroplans.app | YES |

## Changes Made (This PR)

### 1. Expanded SpecialtyConfig (`SpecialtyConfig.swift`)

Added new per-specialty customization points:

| Property | Purpose | Neuro Value | Cardio Should Be |
|----------|---------|-------------|------------------|
| `headerIcon` | SF Symbol for app identity | `brain.head.profile` | `heart.fill` |
| `tagline` | Subtitle on disclaimer | "Clinical Neurology Decision Support" | "Clinical Cardiology Decision Support" |
| `paywallFeatures` | Feature list on paywall | NIHSS, neuro exams, etc. | ESC, ECG guides, etc. |
| `aboutDescription` | Settings > About text | "neurological diagnoses" | "cardiovascular diagnoses" |
| `aboutIcon` | SF Symbol in About | `brain.fill` | `heart.text.square.fill` |
| `quickActions` | Emergency protocol buttons | Stroke Alert, Status Epilepticus | STEMI Alert, Acute PE, AFib |
| `supportEmail` | Contact email | support@neuroplans.app | support@cardioplans.app |

### 2. Views Now Read From Config (No Hardcoded Text)

| View | Before | After |
|------|--------|-------|
| `PaywallView` | Hardcoded "brain.head.profile" icon, 6 hardcoded feature rows | Reads `SpecialtyConfig.headerIcon`, iterates `SpecialtyConfig.paywallFeatures` |
| `SettingsView` | Hardcoded "brain.fill" icon and neuro description | Reads `SpecialtyConfig.aboutIcon` and `.aboutDescription` |
| `DisclaimerView` | Hardcoded "brain.head.profile" icon and generic subtitle | Reads `SpecialtyConfig.headerIcon` and `.tagline`, uses brand color |

### 3. Quick Actions Bar (New Feature)

Added a `QuickActionsBar` to the home screen that shows specialty-specific
emergency protocol shortcuts. This is the single most visible differentiator
because Apple's reviewer sees a different home screen on first launch.

- **Neuro Plans**: Stroke Alert, Status Epilepticus, Seizure Workup
- **Cardio Plans** (example): STEMI Alert, Acute PE Protocol, AFib Management

### 4. Fixed Cardio Plans Legal Docs

- `docs/cardio/privacy.md`: Changed support email from neuroplans.app to cardioplans.app
- `docs/cardio/terms.md`: Same fix

## Remaining Work for Full Differentiation

Before resubmission, the Cardio Plans clone needs these additional changes:

### Must Do (Required for 4.3 compliance)

1. **Replace `ExamToolsView.swift` enum** - Remove neuro tools (penlight, OKN stripes,
   pupil gauge, red desaturation). Add cardio tools (ECG rhythm identifier,
   stethoscope auscultation guide, pulse assessment, S1/S2 heart sound reference).

2. **Different brand color** - Set `brandColorHex` to a cardiology color
   (e.g., `#E74C3C` red or `#3498DB` blue). This changes the entire app theme.

3. **Different app icon** - Must be visually distinct (heart vs brain).

4. **Replace `Category.swift`** - Swap neurology categories for cardiology
   (ACS, Heart Failure, Arrhythmias, Valvular Disease, etc.).

5. **Replace `Reference.swift`** - Swap neuro scales/exams/tools for cardio
   equivalents (ESC scores, cardiac exam steps, cardio calculators).

6. **Add cardio-specific calculators** to `CalculatorEngine.swift` -
   EuroScore II, Framingham Risk Score, TIMI Risk Score, QTc calculation.

### Should Do (Strengthens differentiation)

7. **Different onboarding flow** - Add a first-launch specialty picker or
   welcome screen with cardiology-specific imagery.

8. **Different tab icons** - Use heart-related SF Symbols for Cardio Plans
   tab bar instead of the same generic icons.

9. **Unique "What's New" content** - Specialty-specific changelog entries.

10. **Different screenshots** - Cardio Plans App Store screenshots must show
    cardiology content, not generic UI.

### Technical Issues to Fix Before Resubmission

11. **Add `PrivacyInfo.xcprivacy`** to Xcode target (already in codebase since commit 1296611)
12. **Complete Agreements, Tax, and Banking** in App Store Connect
13. **Configure introductory offer** (14-day trial) after subscription approval
14. **Fix `fatalError()` calls** in `ReferenceStore.swift` (already fixed in codebase)
15. **Set up unique Supabase project** for Cardio Plans (separate anon key)

## Apple's Differentiation Checklist

For each resubmission, verify:

- [ ] Different app icon and brand color
- [ ] Different header icon on disclaimer and paywall screens
- [ ] Different tagline and about description
- [ ] Different paywall feature list (mentions specialty-specific content)
- [ ] Different quick actions on home screen
- [ ] Different exam tools (specialty-specific, not shared)
- [ ] Different clinical scales and calculators
- [ ] Different categories and plan content
- [ ] Separate support email and legal documents
- [ ] Unique screenshots showing specialty content
- [ ] App Review notes explain the specialty focus and how it differs
