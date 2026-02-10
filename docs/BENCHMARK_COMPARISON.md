# Benchmark Comparison — Neuro Clinical Plans vs. Leading Clinical Reference Apps

**Date:** February 2026
**Purpose:** Compare Neuro Clinical Plans against industry-leading clinical decision support and reference applications to identify best practices and improvement opportunities.

---

## 1. Apps Benchmarked

| App | Category | Primary Audience | Platform |
|-----|----------|-----------------|----------|
| **UpToDate** (Wolters Kluwer) | Clinical reference | Physicians, residents | Web + iOS/Android |
| **Epocrates** | Drug/disease lookup | Physicians, NPs, PAs | Mobile-first + web |
| **DynaMed** (EBSCO) | Evidence-based reference | Physicians, librarians | Web + iOS/Android |
| **MDCalc** | Clinical calculators | ED/ICU physicians | Mobile-first + web + EHR |
| **Apple Health** | Consumer health | Patients | iOS native |

---

## 2. Dimension-by-Dimension Comparison

### 2.1 Layout & Content Strategy

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| Primary layout | Long-form doc + outline | Tabbed mobile sections | Outline + summary boxes | Single-purpose cards | Card dashboard | **Table-heavy Markdown** |
| Content density | Very high | Moderate | High (segmented) | Low per screen | Low-moderate | **Very high** |
| Progressive disclosure | Section collapse | Expandable rows | Overview box at top | Score → detail below | Summary → drill-in | **Partial (Clinical Tool only)** |
| Summary/quick-answer | Section headers | Structured cards | Overview & Recommendations | Calculator result | Glanceable cards | **❌ None** |

**Gap:** Neuro Plans lacks a quick-summary or "key actions" section at the top of each plan. DynaMed's "Overview and Recommendations" pattern is directly applicable — a summary box at the top of each plan page with the 3-5 most critical actions would dramatically improve utility for time-pressed clinicians.

### 2.2 Color & Visual Hierarchy

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| Primary brand color | Teal/green | Blue | Blue | Green | Multi-color | **Teal** |
| Evidence grading | Inline text (GRADE) | N/A | Color-coded boxes | Score bands | N/A | **Priority badges** |
| Color as information | Minimal | Moderate (warnings) | Strong (rec levels) | Strong (risk bands) | Very strong (categories) | **Strong (priorities)** |
| Dark mode | ✅ | ✅ | ✅ | ✅ | ✅ | **Partial** |
| CSS custom properties | Yes (modern web) | N/A (native) | Yes | Yes | N/A (native) | **❌ No (hardcoded)** |

**Gap:** The teal color system is appropriate for a clinical tool. However, the lack of CSS custom properties means the color system is unmaintainable. Additionally, dark mode support is incomplete — notably the Clinical Tool has no dark mode at all.

### 2.3 Mobile & Responsive Strategy

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| Mobile approach | Responsive + native | Mobile-first native | Responsive + native | Mobile-first native | Native iOS | **Responsive web** |
| Mobile breakpoints | Multiple | Native | Multiple | Native | Native | **768px only** |
| Small phone (375px) | ✅ Supported | ✅ Native | ✅ Supported | ✅ Native | ✅ Native | **❌ No breakpoint** |
| Offline access | Downloaded topics | Core drug data | Full offline | All calculators | Local data | **❌ None** |
| Touch target sizes | ≥44px | ≥44px | ≥44px | ≥44px | ≥44px | **❌ Some < 28px** |

**Gap:** This is the most significant gap. Every competitor has either a native mobile app or a thoroughly responsive web experience. Neuro Plans has only a single mobile breakpoint at 768px, no 375px small phone support, no offline access, and some interactive elements (venue column badges, vote buttons) are too small for touch. The 10-column tables are essentially unusable on phones.

### 2.4 Search & Navigation

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| Search prominence | Primary entry point | Primary entry point | Primary entry point | Primary entry point | Secondary | **Available (MkDocs)** |
| Type-ahead suggestions | ✅ Rich | ✅ Drug names | ✅ Categorized | ✅ Calculators | ✅ | **✅ (basic)** |
| Browse by specialty | ✅ | ✅ Tabs | ✅ | ✅ | ✅ Categories | **✅ Nav sections** |
| Recent/favorites | ✅ | ✅ | ✅ | ✅ | ✅ Pinned cards | **❌ None** |
| Cross-references | ✅ Rich linking | ✅ | ✅ | ✅ Related calcs | N/A | **❌ None** |
| Filter by setting | N/A | N/A | N/A | By specialty | N/A | **Clinical Tool only** |

**Gap:** Search works adequately via MkDocs Material's built-in search. The main gaps are: (1) no recent/favorites feature for repeat users, (2) no cross-referencing between related plans, and (3) no setting-based filtering on the plans index page.

### 2.5 Clinical Content Presentation

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| Content format | Narrative chapters | Concise cards | Structured outline | Calculator + context | Data + education | **Structured tables** |
| Actionability | Graded recommendations | Dosing tables | Recommendation boxes | Score → next steps | Reference ranges | **Priority-tagged items** |
| Evidence citations | Numbered, linked | Referenced | Linked + graded | Linked papers | N/A | **PMID (not linked)** |
| Treatment algorithms | Inline in text | Step-based | Flow diagrams | Decision trees | N/A | **Table rows by priority** |
| Drug dosing format | Within narrative | Structured tables | Structured | Calculator-driven | N/A | **dose::route::freq::inst** |

**Gap:** The structured table format with priority badges is actually a strong differentiator — it is more actionable than UpToDate's narrative approach and more comprehensive than Epocrates's brief cards. However, the drug dosing format (`dose :: route :: frequency :: instructions`) is dense and could benefit from better visual parsing. References should be hyperlinked to PubMed.

### 2.6 Accessibility & Compliance

| Dimension | UpToDate | Epocrates | DynaMed | MDCalc | Apple Health | **Neuro Plans** |
|-----------|---------|-----------|---------|--------|-------------|-----------------|
| WCAG compliance | ✅ AA | Partial | ✅ AA | Partial | ✅ AAA (Apple HIG) | **❌ Significant gaps** |
| Screen reader support | ✅ | Partial | ✅ | Partial | ✅ Full VoiceOver | **❌ No ARIA in custom code** |
| Keyboard navigation | ✅ | Native | ✅ | ✅ | Native | **MkDocs only, not custom** |
| Focus management | ✅ | Native | ✅ | ✅ | Native | **❌ None in custom code** |
| Reduced motion | ✅ | Native | ✅ | ✅ | Native | **❌ Not supported** |

**Gap:** Accessibility is the clearest compliance gap. Zero ARIA attributes in custom components (comments, clinical tool, inline popups) represents a significant accessibility failure. All competitors meet at least WCAG AA.

---

## 3. Feature Comparison Matrix

| Feature | UpToDate | Epocrates | DynaMed | MDCalc | **Neuro Plans** |
|---------|---------|-----------|---------|--------|-----------------|
| Search with type-ahead | ✅ | ✅ | ✅ | ✅ | ✅ |
| Category browsing | ✅ | ✅ | ✅ | ✅ | ✅ |
| Dark mode | ✅ | ✅ | ✅ | ✅ | ⚠️ Partial |
| Mobile app or PWA | ✅ | ✅ | ✅ | ✅ | ❌ |
| Offline access | ✅ | ✅ | ✅ | ✅ | ❌ |
| Favorites/bookmarks | ✅ | ✅ | ✅ | ✅ | ❌ |
| Recently viewed | ✅ | ✅ | ✅ | ✅ | ❌ |
| Setting/venue filtering | ❌ | ❌ | ❌ | ❌ | ✅ Unique |
| Priority-based triage | ❌ | ❌ | ❌ | ❌ | ✅ Unique |
| Interactive plan builder | ❌ | ❌ | ❌ | ✅ Calculators | ✅ Unique |
| Inline community comments | ❌ | ❌ | ❌ | ❌ | ❌ → ✅ Unique |
| Evidence grading | ✅ GRADE | ❌ | ✅ | ✅ Score-based | ⚠️ Priority only |
| EHR integration | ❌ | ❌ | ❌ | ✅ Epic/Cerner | ❌ |
| Print-optimized | ✅ | ❌ | ✅ | ✅ | ❌ |
| Quick summary box | ✅ Sections | ✅ Cards | ✅ Overview | ✅ Score | ❌ |
| Cross-referencing | ✅ | ✅ | ✅ | ✅ | ❌ |
| Hyperlinked citations | ✅ | ✅ | ✅ | ✅ | ❌ |

---

## 4. Competitive Advantages of Neuro Plans

1. **Setting-based filtering (ED/HOSP/OPD/ICU):** No competitor offers this. The 4-venue column system with priority badges is a unique differentiator that directly addresses the needs of neurohospitalists who work across settings.

2. **Priority-based triage (STAT/URGENT/ROUTINE/EXT):** The priority badge system provides immediate visual triage — something lacking in narrative-based references like UpToDate.

3. **Interactive plan builder:** The ability to select individual items from a plan and build a custom clinical note is unique in this space. MDCalc has calculators, but not full plan builders.

4. **Community feedback system:** Inline section-level comments with voting allow real-time clinical community input — unprecedented in clinical reference tools.

5. **Open source and free:** Unlike UpToDate ($500+/year), Epocrates (freemium), and DynaMed (institutional subscription), Neuro Plans is freely available.

---

## 5. Key Patterns to Adopt

### Must-Have (adopt immediately)
1. **Quick summary box** (from DynaMed) — Add an "At a Glance" or "Key Actions" summary at the top of each plan
2. **Hyperlinked citations** (universal) — Link PMIDs to PubMed
3. **Favorites/recent** (universal) — Add localStorage-based recent plans and favorites
4. **Small phone breakpoint** (universal) — Add 375px responsive support

### Should-Have (medium-term)
5. **Progressive disclosure on plan pages** (from all competitors) — Collapsible table sections so users can focus on relevant content
6. **Dark mode completion** (universal) — Full dark mode for Clinical Tool and all components
7. **Offline PWA** (from Epocrates/MDCalc mobile pattern) — Service worker for offline plan access
8. **Cross-referencing** (from UpToDate/DynaMed) — "Related Plans" links on each plan page

### Nice-to-Have (long-term)
9. **Score-linked guidance** (from MDCalc) — Integrate calculators into treatment recommendations
10. **EHR copy format** (from MDCalc) — Export as structured clinical note compatible with EHR paste

---

*End of Benchmark Comparison. See also: [UX Audit](UX_AUDIT.md) | [UI Audit](UI_AUDIT.md) | [Design System](DESIGN_SYSTEM.md) | [Roadmap](ROADMAP.md)*
