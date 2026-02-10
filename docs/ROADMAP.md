# Neuro Plans - Development Roadmap

**Version:** 2.0
**Created:** January 24, 2026
**Last Updated:** February 2026
**Status:** Phases 1-3 Complete, UI/UX Improvement Phases Defined

---

## Overview

This roadmap covers two workstreams:
1. **Clinical Content Pipeline** (Phases 1-4) — Medication handling, clickable dosing, and standardization
2. **UI/UX Improvements** (Phases 5-8) — Design system, mobile experience, and app transition

---

## Clinical Content Pipeline

### Phase 1: Medication Format Standardization — ✅ COMPLETE

**Completed:** January 24 – January 30, 2026

Standardized all treatment sections to consistent 10-column format with structured dosing (`dose :: route :: frequency :: instructions`). Updated builder, checker, and rebuilder skills.

### Phase 2: Clickable Dosing — ✅ COMPLETE

**Completed:** January 31, 2026

Made medication dosing interactive in the Clinical Tool. Dosing badge click copies order sentence to clipboard. Hover shows full instructions.

### Phase 3: Multiple Dose Options — ✅ COMPLETE

**Completed:** February 5, 2026

Expanded 1,321 medications to 2-6 clinically appropriate dose options. Dropdown selection in Clinical Tool for each medication.

### Phase 4: Future Clinical Enhancements — 🔮 PLANNED

| Feature | Priority | Effort |
|---------|----------|--------|
| Medication interaction checking | Medium | High |
| Weight-based dosing calculator | Medium | Medium |
| Renal/hepatic dose adjustments | Medium | High |

---

## UI/UX Improvement Roadmap

Based on comprehensive audit (see [UX Audit](UX_AUDIT.md), [UI Audit](UI_AUDIT.md), [Benchmark Comparison](BENCHMARK_COMPARISON.md), [Design System](DESIGN_SYSTEM.md), [App Strategy](APP_STRATEGY.md)).

### Phase 5: Quick Wins (CSS & Token Foundation) — 🔧 NEXT

**Effort:** 1-2 days
**Branch:** `ui-ux-improvements`
**Impact:** High — addresses multiple audit findings with low risk

| Item | Audit ID | Description |
|------|----------|-------------|
| CSS custom properties | UI-C1 | Add design tokens to top of `custom.css`, replace hardcoded hex values |
| Dark mode priority badges | UI-DM1 | Add `[data-md-color-scheme="slate"]` overrides for all priority badges |
| Sticky table headers | UI-TAB1 | Add `position: sticky; top: 0` to plan table headers |
| Row hover highlight | UI-TAB2 | Add hover state to table rows for better tracking |
| Row stripe contrast | UI-TAB4 | Increase stripe visibility from `#f0fdfa` to slightly more distinct shade |
| Minimum font sizes | UI-T1 | Increase table body minimum from `0.8rem` → `0.875rem`, venue columns from `0.65rem` → `0.75rem` |
| Badge minimum sizes | UI-B1 | Ensure priority badges never go below `0.6875rem` with `4px 8px` padding |
| Active nav visibility | UI-N1 | Strengthen active page indicator (background color + left border) |
| Home page stats | IA-6 | Update "124 Approved Plans" → "144 Approved Plans" |
| Hyperlink references | US-4 | Add PMID → PubMed URL auto-linking (CSS or JS) |
| Focus indicators | A11Y-2 | Add `:focus-visible` styles to all interactive custom elements |
| Reduced motion | A11Y-7 | Add `@media (prefers-reduced-motion: reduce)` to disable animations |
| Touch targets | Mobile | Ensure all interactive elements ≥44px touch target on mobile |
| 375px breakpoint | UI-L1 | Add small phone responsive styles |

### Phase 6: Mobile & Responsive — 📱 MEDIUM EFFORT

**Effort:** 1-2 weeks
**Depends on:** Phase 5 (tokens must be in place)

| Item | Audit ID | Description |
|------|----------|-------------|
| Responsive table strategy | UI-TAB3 | Card-based layout for tables on mobile (<768px) |
| Clinical Tool dark mode | UI-DM2 | Add dark mode support using shared design tokens |
| Clinical Tool integration | CT-1 | Add back-to-plan link, match site navigation |
| Comment ARIA attributes | A11Y-1 | Add roles, labels, and live regions to comment components |
| Clinical Tool ARIA | A11Y-2 | Add ARIA to venue tabs, checkboxes, sidebar, export |
| Collapsible plan sections | US-2 | Progressive disclosure for table sections (click to expand) |
| Quick summary box | Gap #1 | Add "Key Actions" summary at top of each plan page |
| Comment system lazy load | Perf | Defer Firebase SDK until user scrolls to comments |

### Phase 7: PWA & Offline — 📲 MEDIUM EFFORT

**Effort:** 1-2 weeks
**Depends on:** Phase 6 (mobile layout must be solid)

| Item | Audit ID | Description |
|------|----------|-------------|
| Service worker | App Strategy | Cache-first for plan pages, stale-while-revalidate |
| Web app manifest | App Strategy | Icons, theme color, standalone display mode |
| Offline fallback page | App Strategy | Graceful offline experience |
| Add to home screen | App Strategy | Install prompt for mobile users |
| JSON data splitting | Perf | Split plans.json by category for faster Clinical Tool load |

### Phase 8: Feature Parity & Polish — ✨ LARGER EFFORT

**Effort:** 2-4 weeks
**Depends on:** Phase 7

| Item | Audit ID | Description |
|------|----------|-------------|
| Favorites / recent plans | IA-5 | localStorage-based bookmarks and history |
| Cross-referencing | IA-2 | "Related Plans" links on each plan page |
| Search in Clinical Tool | SD-1 | Type-ahead search to replace dropdown |
| Multi-plan Clinical Tool | CT-5 | Combine items from multiple plans |
| Save/resume in Clinical Tool | CT-3 | Persist selected items in localStorage |
| Print styles | US-5 | `@media print` optimized layout |
| Comment moderation | CM-1 | Basic spam filtering, report button |
| Setting filter on index | SD-2 | Filter plans by care setting on the index page |
| Clinical Tool keyboard nav | CT-2 | Full keyboard support for power users |

---

## Priority Matrix

| Phase | Effort | Impact | Risk | Timeline |
|-------|--------|--------|------|----------|
| 5: Quick Wins | Low (1-2 days) | High | Very Low | Immediate |
| 6: Mobile & Responsive | Medium (1-2 wk) | Very High | Low | Next sprint |
| 7: PWA & Offline | Medium (1-2 wk) | High | Low | Month 2 |
| 8: Feature Parity | High (2-4 wk) | Medium | Medium | Month 2-3 |

---

## Quality Gates

### Before Phase 1-3 (Clinical Content) — ✅ ALL PASSED
- [x] Standardized medication format
- [x] Clickable dosing in Clinical Tool
- [x] 1,321 medications expanded to multi-dose
- [x] All 144 approved plans in new format
- [x] generate_json.py handles structured dosing

### Before Phase 5-6 (UI/UX) — TO VERIFY
- [ ] Design tokens defined in DESIGN_SYSTEM.md ✅
- [ ] UX Audit completed ✅
- [ ] UI Audit completed ✅
- [ ] Benchmark comparison completed ✅
- [ ] App strategy decided ✅

### Before Phase 7 (PWA)
- [ ] Mobile responsive tables working
- [ ] Dark mode complete across all surfaces
- [ ] ARIA attributes on all custom components
- [ ] Lighthouse PWA score ≥80

---

## Change Log

**v2.0 (February 2026)**
- Added UI/UX Improvement Roadmap (Phases 5-8)
- Linked to audit documents (UX_AUDIT, UI_AUDIT, DESIGN_SYSTEM, BENCHMARK_COMPARISON, APP_STRATEGY)
- Added priority matrix and quality gates for new phases
- Updated plan count to 144 (from 124)

**v1.1 (February 6, 2026)**
- Marked Phases 1-3 as COMPLETE with dates
- Updated quality gates (all passed)

**v1.0 (January 24, 2026)**
- Initial roadmap creation
- Defined Phase 1-4 improvements
