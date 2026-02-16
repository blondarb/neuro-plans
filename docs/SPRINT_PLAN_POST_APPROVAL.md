# Post-Approval Sprint Plan

**Created:** 2026-02-15
**Source:** Steel Man Test Report (`qa/STEEL-MAN-2026-02-15.md`)
**Context:** v1.0 submitted to App Store — Waiting for Review. This plan organizes fixes for the first post-approval update (v1.0.1 or v1.1).

---

## Sprint 1: Critical Fixes (v1.0.1 — Ship Within 1 Week of Approval)

**Goal:** Eliminate the crash risk and the most exploitable security gaps.

| # | Task | Severity | File(s) | Est. Effort | Notes |
|---|------|----------|---------|-------------|-------|
| 1 | Replace `fatalError()` with graceful error handling | S0 | `ReferenceStore.swift:115,125` | 30 min | Return empty arrays + show error UI |
| 2 | Add `PrivacyInfo.xcprivacy` to Xcode project | S1 | New file (already created locally) | 15 min | Add to Xcode target, verify in build |
| 3 | Add error UI for `plans.json` load failure | S1 | `PlanStore.swift:52-67` | 1 hr | Show retry/error view instead of blank screen |
| 4 | Fix `verified_emails` RLS policy | S1 | Supabase migration | 15 min | Already identified — restrict INSERT to own email |
| 5 | Verify all Supabase RLS policies are correct | S1 | Supabase dashboard | 30 min | ✅ Done — whitelisted_domains is properly locked |

**Sprint 1 Total:** ~2.5 hours of coding + testing

---

## Sprint 2: Security Hardening (v1.1 — Within 2 Weeks)

**Goal:** Move sensitive data to Keychain, close entitlement bypasses.

| # | Task | Severity | File(s) | Est. Effort | Notes |
|---|------|----------|---------|-------------|-------|
| 6 | Move `trialStartDate` to Keychain | S1 | `EntitlementService.swift:13-16` | 2 hr | Migrate existing UserDefaults value on first launch |
| 7 | Move `verifiedEmail` to Keychain | S1 | `EntitlementService.swift:21` | 1 hr | Same migration pattern |
| 8 | Move `hasEarnedFreeYear` + `freeYearEarnedDate` to Keychain | S1 | `ClinicalErrorService.swift:32-40` | 1 hr | Same migration pattern |
| 9 | Add `@Environment(\.scenePhase)` handling | S2 | `NeuroPlansApp.swift` | 1.5 hr | Refresh entitlements on foreground, pause stopwatch on background |
| 10 | Add structured logging with `os_log` | S2 | All `Services/` files | 2 hr | Replace 5 `print()` calls, add log categories |
| 11 | Differentiate OTP error types | S2 | `EntitlementService.swift:238-239` | 1 hr | Network vs expired vs invalid vs rate-limited |
| 12 | Add network retry with exponential backoff | S2 | All network calls | 2 hr | Create shared retry utility |
| 13 | Configure URLSession timeouts (15s) | S2 | `SupabaseService.swift` | 30 min | Custom configuration |

**Sprint 2 Total:** ~11 hours

---

## Sprint 3: Accessibility & Testing (v1.2 — Within 1 Month)

**Goal:** Make the app accessible and establish testing infrastructure.

| # | Task | Severity | File(s) | Est. Effort | Notes |
|---|------|----------|---------|-------------|-------|
| 14 | Add accessibility labels to all interactive elements | S1 | All Views | 4 hr | Navigation, tabs, plan items, buttons, calculators |
| 15 | Add accessibility hints for non-obvious controls | S1 | Key Views | 2 hr | Stopwatch, builder, scale scoring |
| 16 | Run Accessibility Inspector audit | S2 | N/A | 1 hr | Verify VoiceOver navigation flow |
| 17 | Add test target to Xcode project | S2 | `project.pbxproj` | 30 min | Link test files already written |
| 18 | Run and fix initial unit tests | S2 | `NeuroPlansTests/` | 2 hr | CalculatorEngine, PlanStore, EntitlementService |
| 19 | Add memory warning handler | S2 | `NeuroPlansApp.swift` | 1 hr | Release non-visible plan data under pressure |
| 20 | Handle `plans.json` memory footprint | S1 | `PlanStore.swift` | 4 hr | Lazy loading or split into category files |

**Sprint 3 Total:** ~14.5 hours

---

## Backlog: Quality of Life (v1.x — Ongoing)

| # | Task | Severity | Est. Effort | Notes |
|---|------|----------|-------------|-------|
| 21 | Cache sorted computed properties | S3 | 1 hr | `allPlans`, `allScales`, `allExams`, `allTools` |
| 22 | Reduce stopwatch timer to 10Hz | S3 | 30 min | Users can't perceive 10ms precision |
| 23 | Persist Plan Builder state | S3 | 2 hr | Save selections to UserDefaults for crash recovery |
| 24 | Add calculator input range warnings | S3 | 3 hr | Clinical out-of-bounds alerts |
| 25 | Read version from bundle | S3 | 15 min | `CFBundleShortVersionString` instead of hardcoded "1.0.0" |
| 26 | Read data version from metadata | S3 | 30 min | Derive from plans.json or build date |
| 27 | Add feedback send mechanism | S3 | 2 hr | Currently just accumulates in UserDefaults |
| 28 | Limit UserDefaults data growth | S3 | 1 hr | Max entries for feedback, error reports |
| 29 | Improve email validation | S3 | 30 min | Use NSDataDetector or proper regex |
| 30 | Stop creating orphaned Supabase Auth users | S3 | 30 min | Set `shouldCreateUser: false` |

---

## Backlog: Competitive Features (v2.0+)

| # | Feature | Priority | Est. Effort | Rationale |
|---|---------|----------|-------------|-----------|
| 31 | Drug interaction checker | High | 40+ hr | Table-stakes for apps listing medications |
| 32 | Evidence grading system | High | 8 hr | GRADE or AAN Class I-IV on each recommendation |
| 33 | Editorial transparency | Medium | 4 hr | Show author, review date, methodology per plan |
| 34 | CME credit integration | Medium | 20+ hr | Major retention and engagement driver |
| 35 | Server-side receipt validation | Medium | 8 hr | Detect refund abuse, remote revocation |
| 36 | User accounts / cloud sync | Low | 40+ hr | Sync favorites, builder, preferences across devices |
| 37 | Collaborative plan sharing | Low | 20+ hr | Share custom builder plans with colleagues |

---

## Definition of Done (per sprint)

- [ ] All code changes have unit tests where applicable
- [ ] Accessibility Inspector audit passes (Sprint 3+)
- [ ] No new `print()` statements — use `os_log` (Sprint 2+)
- [ ] Dark mode verified for new UI elements
- [ ] Dynamic Type verified at XL and AXXXL sizes
- [ ] No `fatalError()`, `preconditionFailure()`, or force unwraps on user data
- [ ] UserDefaults data validated (no unbounded growth)
- [ ] Build succeeds with zero warnings

---

## Key Metrics to Track Post-Launch

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Crash-free rate | >99.5% | App Store Connect / TestFlight |
| App launch time | <2 seconds | Xcode Instruments |
| Memory at launch | <100 MB | Xcode Instruments |
| Accessibility audit | 0 critical issues | Accessibility Inspector |
| Test coverage | >60% of Services | Xcode coverage report |
| App Store rating | >4.5 stars | App Store Connect |
| Trial → subscription | >5% | StoreKit analytics |
| Daily active users | Track baseline | Supabase analytics |
