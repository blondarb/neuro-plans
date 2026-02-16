# Neuro Plans Handoff — February 15, 2026

## Audience
Next Claude Code session or developer working on the Neuro Plans iOS app post-approval.

## Current State
- **Build/Deploy status**: v1.0 (Build 1) submitted to App Store — **Waiting for Review** as of Feb 15, 2026
- **App ID**: 6759209586
- **Bundle ID**: com.neuroplans.app
- **Branch**: `main` @ `23c9c27` (Add App Store metadata draft for submission)
- **Uncommitted changes**: Yes — see table below. Nothing has been committed or pushed.
- **Xcode**: 26.3 (Build 17C519)
- **Simulators**: iPhone 17 Pro (DA33D2DA-72AE-4907-A226-22B09B425A8C), iPad (B8F3E138-357B-4BF6-8395-3AC1C12B193D)
- **Supabase project**: `cyaginuvsqcbvyeuizlu` (neuroplans) — ACTIVE_HEALTHY

## Work Completed This Session

### 1. Steel Man Test (Adversarial Quality Analysis)
- Ran comprehensive 4-phase steel-man test on the entire iOS app
- Phase 0: Reconnaissance — mapped codebase, docs, architecture
- Phase 1: PRD analysis — identified the app has no iOS-specific PRD
- Phase 2: Deep code review — 32 findings across 10 categories (1 S0, 6 S1, 11 S2, 17 S3, 12 S4)
- Phase 3: Live product testing — app launches clean, dark mode/Dynamic Type work, zero crashes
- Phase 4: Competitive assessment — compared against MDCalc, Medscape, UpToDate, NeuroLogicMD

### 2. Supabase RLS Audit
- Verified RLS is enabled on both tables (`whitelisted_domains`, `verified_emails`)
- `whitelisted_domains`: Properly configured — public can only SELECT active domains
- `verified_emails`: **SECURITY ISSUE FOUND** — INSERT policy is overly permissive (`WITH CHECK (true)`). Any authenticated user can insert any email. Supabase security advisor flagged this.
- **Fix NOT applied** — awaiting user approval (remote write operation)

### 3. iOS App PRD
- Created comprehensive 15-section PRD at `ios/NeuroPlans/docs/PRD.md`
- Covers: product overview, 5 user personas, all features, user flows, data model, subscription model, tech architecture, content strategy, privacy/security, accessibility requirements, performance targets, success metrics, roadmap, limitations, competitive landscape

### 4. PrivacyInfo.xcprivacy
- Created Apple privacy manifest file at `ios/NeuroPlans/NeuroPlans/PrivacyInfo.xcprivacy`
- Declares UserDefaults API usage with reason CA92.1
- No tracking, no collected data types
- **Must be added to Xcode target** before next build (not yet in project.pbxproj)

### 5. Unit Test Files
- Created 4 test files with 119 total tests in `ios/NeuroPlans/NeuroPlansTests/`:
  - `CalculatorEngineTests.swift` (44 tests) — clinical calculator accuracy
  - `PlanStoreTests.swift` (22 tests) — data loading, search, favorites, recents
  - `EntitlementServiceTests.swift` (24 tests) — trial logic, access levels, domain validation
  - `ClinicalErrorServiceTests.swift` (29 tests) — error reporting, reward eligibility, report management
- **Test target not yet added in Xcode** — files are ready but need a test target created in the project

### 6. Post-Approval Sprint Plan
- Created prioritized fix plan at `docs/SPRINT_PLAN_POST_APPROVAL.md`
- Sprint 1 (v1.0.1, ~2.5 hrs): fatalError fix, PrivacyInfo, error UI, RLS fix
- Sprint 2 (v1.1, ~11 hrs): Keychain migration, scenePhase, logging, retry logic
- Sprint 3 (v1.2, ~14.5 hrs): Accessibility, test target, memory handling, plans.json optimization
- Backlog: quality of life items and competitive features (v2.0+)

## Uncommitted Files

| File | Status | Description |
|------|--------|-------------|
| `ios/NeuroPlans/NeuroPlans.xcodeproj/project.pbxproj` | Modified | Previous session changes (entitlements, scheme) |
| `ios/NeuroPlans/NeuroPlans/Assets.xcassets/AppIcon.appiconset/AppIcon.png` | Modified | App icon fix from previous session |
| `ios/NeuroPlans/PUBLISHING_GUIDE.md` | Modified | Submission log from previous session |
| `docs/SPRINT_PLAN_POST_APPROVAL.md` | New | Post-approval fix priority plan |
| `ios/NeuroPlans/NeuroPlans.xcodeproj/xcshareddata/` | New | Xcode shared scheme data |
| `ios/NeuroPlans/NeuroPlans/NeuroPlans.entitlements` | New | App entitlements file |
| `ios/NeuroPlans/NeuroPlans/PrivacyInfo.xcprivacy` | New | Apple privacy manifest |
| `ios/NeuroPlans/NeuroPlansTests/` | New | 4 test files + Info.plist (119 tests) |
| `ios/NeuroPlans/Screenshots/` | New | App Store screenshots from previous session |
| `ios/NeuroPlans/docs/PRD.md` | New | Comprehensive iOS app PRD |
| `qa/STEEL-MAN-2026-02-15.md` | New | Steel man adversarial test report |

## What Was NOT Done
- **RLS policy fix** — Requires applying a Supabase migration to restrict `verified_emails` INSERT to authenticated user's own email. Awaiting user approval.
- **Xcode test target creation** — Test files are written but the test target must be created in Xcode (File > New > Target > Unit Testing Bundle, then add the 4 .swift files)
- **PrivacyInfo.xcprivacy added to Xcode target** — File exists but must be added to the NeuroPlans build target in Xcode
- **No code fixes applied** — Intentionally deferred per user's decision to wait for Apple's approval/denial before modifying the app
- **No git commit** — All new files are untracked; user hasn't requested a commit

## Known Risks / Watch Items

1. **fatalError() in ReferenceStore.swift (S0)** — Lines 115 and 125 will crash the app if bundled JSON files are missing or corrupted. Highest priority fix for v1.0.1.
2. **Supabase verified_emails RLS is overly permissive** — Any authenticated user can insert any email. Should be fixed ASAP (server-side, doesn't require app update).
3. **10.1 MB plans.json loaded entirely into memory** — Works fine now but will become problematic as content grows. Monitor.
4. **Zero accessibility labels in entire codebase** — May affect App Store review if Apple tests with VoiceOver. More importantly, excludes users with disabilities.
5. **Trial system stored in unprotected UserDefaults** — Trivially bypassable by reinstalling the app. Move to Keychain in Sprint 2.
6. **No PrivacyInfo.xcprivacy in the submitted build** — Apple may not reject v1.0 for this, but future submissions may require it.

## Required Next Steps (Priority Order)

1. **Wait for Apple's App Store Review decision** — Either approval or rejection
2. **If approved**: Start Sprint 1 from `docs/SPRINT_PLAN_POST_APPROVAL.md`
3. **If rejected**: Address rejection reason first, then incorporate Sprint 1 fixes
4. **Apply Supabase RLS fix** (can do anytime, independent of app): Drop and recreate the `verified_emails` INSERT policy to restrict to `email = auth.jwt() ->> 'email'`
5. **Add test target in Xcode** and run the 119 tests to verify they pass
6. **Add PrivacyInfo.xcprivacy to Xcode target** for next build
7. **Commit all uncommitted work** when ready (user should review first)

## Files to Review First
- `qa/STEEL-MAN-2026-02-15.md` — Full adversarial test report with all 47 findings
- `docs/SPRINT_PLAN_POST_APPROVAL.md` — Prioritized fix plan for post-approval update
- `ios/NeuroPlans/docs/PRD.md` — Comprehensive product requirements document
- `ios/NeuroPlans/NeuroPlans/PrivacyInfo.xcprivacy` — Apple privacy manifest (verify before adding to target)

## Supabase RLS Fix (Ready to Apply)

When approved by user, apply this migration to project `cyaginuvsqcbvyeuizlu`:

```sql
-- Drop overly permissive INSERT policy
DROP POLICY "Authenticated insert verified emails" ON public.verified_emails;

-- Create restricted INSERT policy (users can only insert their own email)
CREATE POLICY "Authenticated insert own verified email"
  ON public.verified_emails
  FOR INSERT
  TO authenticated
  WITH CHECK (email = auth.jwt() ->> 'email');
```

## Key Reference IDs
- App ID: 6759209586
- Bundle ID: com.neuroplans.app
- Subscription Apple ID: 6759209768
- Team ID: 92YUSSM83T
- Supabase Project: cyaginuvsqcbvyeuizlu
- iPhone Simulator: DA33D2DA-72AE-4907-A226-22B09B425A8C
- iPad Simulator: B8F3E138-357B-4BF6-8395-3AC1C12B193D
