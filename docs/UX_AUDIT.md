# UX Audit — Neuro Clinical Plans

**Date:** February 2026
**Scope:** Full UX evaluation of blondarb.github.io/neuro-plans
**Auditor:** Claude Code (automated)

---

## 1. Tech Stack Summary

| Layer | Technology | Version / Notes |
|-------|-----------|-----------------|
| Static Site Generator | MkDocs | Material for MkDocs theme |
| Theme | Material for MkDocs | Teal primary/accent, Inter font, Roboto Mono code font |
| Hosting | GitHub Pages → Vercel | Deployed from `main` branch |
| CSS | Single custom file (`custom.css`, 1 398 lines) | No preprocessor, no CSS variables in custom sheet |
| JavaScript | Vanilla JS (2 files) | `table-layout.js` (80 lines), `comments.js` (1 001 lines) |
| Comment System | Firebase Firestore | Anonymous voting, inline section comments |
| Interactive Tool | Standalone HTML (`clinical/index.html`) | Vanilla JS, inline CSS with CSS custom properties |
| Data Layer | JSON (`docs/data/plans.json`) + per-plan `.json` files | 144 plan JSONs + merged aggregate |
| Build Scripts | Python 3.12 (14 scripts) | Approval automation, JSON generation, ICD-10/citation validation |
| AI Pipeline | 4 LLM skills (Builder, Checker, Rebuilder, Comment Reviewer) | Markdown-based prompts in `/skills/` |
| Navigation | 20+ clinical categories, tabs, instant navigation, search | Defined in `mkdocs.yml` nav section (252 lines) |
| Plugins | `search`, `tags` | No social cards, no git-revision-date, no minification |

### Architecture Diagram

```
User → Vercel CDN → MkDocs Material (static HTML)
                       ├── 144 plan pages (Markdown → HTML)
                       ├── Interactive Clinical Tool (standalone HTML/JS)
                       ├── Comment System (Firebase Firestore)
                       └── JSON data layer (plans.json)
```

---

## 2. Content Inventory

| Content Type | Count | Format |
|-------------|-------|--------|
| Approved clinical plans | 144 | Markdown + JSON pairs |
| Draft plans | ~113 Markdown files in `/docs/drafts/` | Markdown (various states) |
| Clinical categories | 21 nav sections | Defined in mkdocs.yml |
| Reference pages | 2 (LP Reference, Template Tracker) | Markdown |
| Interactive tools | 1 (Clinical Plan Builder) | Standalone HTML |
| Index/landing pages | 3 (Home, Plans Index, Queue) | Markdown |

---

## 3. UX Audit — Information Architecture

### 3.1 Navigation Structure

**Strengths:**
- Logical clinical grouping by disease category (Seizures, Stroke, Neuromuscular, etc.)
- Tab-based top navigation separates Home, Clinical Tool, Plans, Drafts, References
- MkDocs instant navigation provides fast page transitions
- Left sidebar with collapsible sections for browsing by category
- Right TOC sidebar for within-page navigation (h2 depth)
- Search with suggest and highlight enabled

**Issues:**
- **IA-1 — Flat category list is overwhelming:** 21 navigation sections in the sidebar with 144 plans creates a very long scroll. No visual hierarchy differentiates "big" categories (Neuromuscular with 22 plans) from small ones (Intracranial Pressure with 1 plan).
- **IA-2 — No cross-referencing between related plans:** A user viewing "Parkinson's Disease" cannot easily discover related plans like "Parkinson's — Motor Fluctuations" or "Parkinson's — Psychosis" without scrolling the sidebar.
- **IA-3 — Drafts and approved plans are siloed:** The drafts queue is a separate nav section. Users cannot see which conditions are "coming soon" alongside approved plans.
- **IA-4 — Clinical Tool is disconnected from plan pages:** The interactive builder is a standalone HTML page outside the MkDocs template. Users lose the site navigation, search, and dark mode when they enter it.
- **IA-5 — No "recently viewed" or "favorites" mechanism:** Clinicians tend to use a small subset of plans repeatedly. There is no way to bookmark frequently used plans within the site.
- **IA-6 — Home page stats are stale:** The home page still says "124 Approved Plans" when there are actually 144 approved.

### 3.2 Search & Discovery

**Strengths:**
- MkDocs Material search with autocomplete and highlighting
- ICD-10 codes in plan metadata enable code-based search
- Synonym field in each plan improves search hit rate

**Issues:**
- **SD-1 — No search within the Clinical Tool:** The standalone HTML tool has its own dropdown selector but no type-ahead search.
- **SD-2 — No filter by care setting on the Plans Index:** Users cannot quickly find all ED-relevant or ICU-relevant plans from the index page.
- **SD-3 — No tag-based browsing:** Although the `tags` plugin is enabled, there is no visible tags page or tag cloud for browsing by clinical concept.

### 3.3 User Flows

**Primary Flow — Look up a plan for a specific diagnosis:**

```
Home → Plans Index → Scroll to category → Click plan → Read plan
                                                  or
Home → Search → Type diagnosis → Click result → Read plan
```

**Assessment:** The search path works well. The browse path requires too much scrolling through 21 categories.

**Secondary Flow — Use the interactive clinical tool:**

```
Home → Click "Open Clinical Plan Builder" → Select plan from dropdown →
  Choose venue tab → Check items → View sidebar → Copy/Export
```

**Assessment:** This flow works but requires leaving the MkDocs environment entirely. There is no way to go from a plan page directly to that plan in the clinical tool.

**Tertiary Flow — Leave feedback on a plan:**

```
Plan page → Scroll to comments → Type comment → Submit
                    or
Plan page → Click section comment button (on h2) → Type → Submit
```

**Assessment:** The comment system works but has no authentication, making it difficult to track feedback quality or follow up with commenters.

---

## 4. UX Audit — Usability

### 4.1 Plan Page Usability

**Strengths:**
- Consistent 8-section structure across all plans (Labs, Imaging, Treatment, Recommendations, DDx, Monitoring, Disposition, References)
- Priority badges (STAT/URGENT/ROUTINE/EXT) provide immediate visual triage
- 4-venue columns (ED/HOSP/OPD/ICU) allow setting-specific guidance at a glance
- Clear metadata block at top (ICD-10, Synonyms, Scope, Definitions)

**Issues:**
- **US-1 — Table-heavy layout is hard to scan on mobile:** Plans are structured as Markdown tables with 6-10 columns. On mobile, these tables become horizontally scrollable, making it very difficult to read.
- **US-2 — No "quick summary" or "key actions" section:** Plans jump directly into detailed tables. A busy clinician needs a 30-second summary before diving into full tables.
- **US-3 — Treatment dosing is dense:** Medication rows contain `dose :: route :: frequency :: instructions` in a single cell, which is information-dense and hard to parse quickly.
- **US-4 — References section is not interactive:** Citations are listed as plain text with PMIDs but are not hyperlinked to PubMed or DOI.
- **US-5 — No print-optimized layout:** Clinicians may want to print a plan for bedside use. There are no `@media print` styles.
- **US-6 — No "copy plan" or "share plan" quick action:** There is no easy way to copy a plan URL or share it via email/messaging.

### 4.2 Clinical Tool Usability

**Strengths:**
- Progressive disclosure with icon tooltips (rationale, indication, timing, target, contraindications, monitoring)
- Click-to-select items into sidebar
- Editable items in sidebar before export
- Venue tab filtering
- Clean, focused interface

**Issues:**
- **CT-1 — Single-page app outside MkDocs:** No back button to return to the plan page, no dark mode, no search integration.
- **CT-2 — No keyboard navigation:** All interactions are click-based. No keyboard shortcuts for power users.
- **CT-3 — No save/resume capability:** Selected items are lost on page refresh. No way to save a partially built plan.
- **CT-4 — Export is copy-only:** No option to export as PDF, structured note, or EHR-compatible format.
- **CT-5 — No multi-plan support:** Cannot combine items from multiple plans into a single clinical note (e.g., patient with stroke AND seizure).

### 4.3 Comment System Usability

**Strengths:**
- Low friction (anonymous, no login required)
- Upvote/downvote for community curation
- Section-level inline comments on h2 headings
- Nav badges show comment counts per page

**Issues:**
- **CM-1 — No moderation workflow:** Anonymous comments with no approval queue mean spam or inappropriate content could appear.
- **CM-2 — No notification for plan authors:** When a comment is left, there is no way to notify the physician who wrote the plan.
- **CM-3 — Delete requires no authentication:** The delete confirmation dialog exists but anyone can delete any comment.
- **CM-4 — No threading or replies:** Comments are flat, not threaded. Conversations are difficult to follow.

---

## 5. UX Audit — Accessibility

### 5.1 Automated Accessibility Assessment

**Critical Finding: Zero `aria-*` attributes in custom code.** A grep across the entire `docs/` directory found 0 instances of `aria-` and 0 instances of `role=`. All accessibility relies entirely on MkDocs Material's built-in semantics.

**Issues:**
- **A11Y-1 — No ARIA labels on comment system elements:** The comment form, vote buttons, delete buttons, and inline comment popups have no ARIA labels, roles, or live regions.
- **A11Y-2 — No ARIA labels on Clinical Tool:** The standalone HTML tool's buttons, tabs, checkboxes, sidebar, and export functionality have no ARIA markup.
- **A11Y-3 — No skip links in Clinical Tool:** The standalone page has no skip-to-content link.
- **A11Y-4 — Color-only priority indicators:** Priority badges use color alone (red for STAT, orange for URGENT, etc.) without sufficient text contrast or alternative indicators for colorblind users. The text labels ("STAT", "URGENT") help, but the venue column color coding (teal backgrounds) has no text alternative.
- **A11Y-5 — No focus management for dynamic content:** When comments load, inline popups open, or items are added to the sidebar, focus is not programmatically moved. Screen reader users would not be notified of these state changes.
- **A11Y-6 — Emoji-based icon system in Clinical Tool:** The progressive disclosure icons (ℹ️💊⏱🎯⚠️📊) rely on emoji, which have inconsistent screen reader support.
- **A11Y-7 — No reduced-motion preference:** The loading spinner animation and hover transitions do not respect `prefers-reduced-motion`.

### 5.2 Keyboard Navigation

- MkDocs Material provides reasonable keyboard navigation for the documentation site
- The Clinical Tool has no keyboard support for venue tabs, item selection, or sidebar management
- Comment vote buttons and inline comment triggers are likely not keyboard-focusable (they use `<span>` elements styled as buttons)

### 5.3 Screen Reader Support

- Plan content renders as standard HTML tables, which screen readers can navigate
- Dynamic content (comments, clinical tool interactions) has no live region announcements
- Toast notifications in the comment system are visual-only

---

## 6. UX Audit — Performance

### 6.1 Page Load

- **Static site advantage:** MkDocs generates static HTML, so initial page loads are fast
- **Firebase SDK loaded on every page:** The comments.js file loads Firebase SDK (firebase 10.7.1) via CDN on every plan page, even if the user never scrolls to the comments section
- **No lazy loading of comment system:** Comments and Firebase are initialized immediately on page load
- **plans.json is loaded entirely by the Clinical Tool:** The merged JSON file contains all 144 plans. As the library grows, this will become a performance concern.

### 6.2 Navigation Performance

- MkDocs instant navigation provides SPA-like transitions
- The comment system reinitializes on every navigation event using 7 different detection methods (popstate, document$, hashchange, click listener, MutationObserver, setInterval, title observer) — this is over-engineered and could cause performance issues or race conditions.

---

## 7. Summary of UX Issues by Priority

### Critical (Blocks core use cases)
| ID | Issue | Impact |
|----|-------|--------|
| US-1 | Tables unusable on mobile | Clinicians on phones cannot read plans |
| A11Y-1/2 | No ARIA in custom components | Accessibility violation for screen reader users |

### High (Significantly degrades experience)
| ID | Issue | Impact |
|----|-------|--------|
| IA-1 | 21-category flat nav is overwhelming | Hard to find plans by browsing |
| CT-1 | Clinical Tool is disconnected from site | Context switching, no dark mode, no search |
| CT-3 | No save/resume in Clinical Tool | Lost work on refresh |
| IA-6 | Stale home page stats | Trust/credibility concern |

### Medium (Noticeable friction)
| ID | Issue | Impact |
|----|-------|--------|
| US-2 | No quick summary on plan pages | Busy clinicians need 30-second overview |
| SD-1 | No search in Clinical Tool | Dropdown with 144 items is slow to browse |
| US-4 | References not hyperlinked | Extra steps to verify citations |
| A11Y-4 | Color-only priority indicators | Accessibility for colorblind users |
| IA-5 | No favorites or recent plans | Repeat users cannot quickly access their usual plans |

### Low (Polish / future enhancement)
| ID | Issue | Impact |
|----|-------|--------|
| US-5 | No print styles | Minor — most clinicians use screens |
| CM-4 | No comment threading | Minor — comment volume is low |
| CT-4 | Export is copy-only | Nice to have — PDF/EHR integration |
| A11Y-7 | No reduced-motion respect | Niche accessibility concern |

---

*End of UX Audit. See also: [UI Audit](UI_AUDIT.md) | [Design System](DESIGN_SYSTEM.md) | [Roadmap](ROADMAP.md)*
