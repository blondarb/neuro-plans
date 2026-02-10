# UI Audit — Neuro Clinical Plans

**Date:** February 2026
**Scope:** Visual design, typography, color system, layout, and component audit
**Auditor:** Claude Code (automated)

---

## 1. Color System

### 1.1 Current Palette

The site uses a teal-centric palette with no CSS custom properties in the main stylesheet. All values are hardcoded hex codes.

**Primary Colors:**

| Token | Hex | Usage |
|-------|-----|-------|
| Primary | `#0d9488` | Links, buttons, header accents, nav highlights |
| Primary Hover | `#0f766e` | Button hover, link hover |
| Primary Dark | `#115e59` | Table header text, dark accents |
| Primary Light | `#ccfbf1` | Venue column headers, subtle backgrounds |
| Primary BG | `#f0fdfa` | Table row stripes, table headers, nav hover |

**Priority Badge Colors:**

| Priority | Background | Text | Border |
|----------|-----------|------|--------|
| STAT | `#fee2e2` | `#991b1b` | `#fca5a5` |
| URGENT | `#ffedd5` | `#9a3412` | `#fed7aa` |
| ROUTINE | `#dbeafe` | `#1e40af` | `#93c5fd` |
| EXT | `#f3e8ff` | `#6b21a8` | `#d8b4fe` |
| N/A | `#f3f4f6` | `#6b7280` | `#d1d5db` |

**Neutral / Text Colors:**

| Purpose | Light Mode | Dark Mode |
|---------|-----------|-----------|
| Text primary | `#1e293b` | `#f1f5f9` |
| Text secondary | `#64748b` | `#94a3b8` |
| Text body | `#334155` | `#cbd5e1` |
| Background | `#ffffff` | `#1e293b` |
| Background alt | `#f8fafc` / `#f9fafb` | `#334155` |
| Border | `#e2e8f0` | `#334155` |

**Status Colors:**

| Status | Color | Usage |
|--------|-------|-------|
| Draft | `#f59e0b` (amber) | Draft warning banner, draft badges |
| Approved | `#10b981` (green) | Approved status badges |
| Error/Delete | `#dc2626` (red) | Delete buttons, error messages |

### 1.2 Color Issues

- **UI-C1 — No CSS custom properties in `custom.css`:** Every color is a hardcoded hex value. This makes theming impossible and maintenance error-prone. The Clinical Tool HTML, by contrast, uses CSS custom properties correctly.
- **UI-C2 — Inconsistent color usage:** The same conceptual "secondary text" appears as `#64748b`, `#6b7280`, and `#475569` in different contexts.
- **UI-C3 — Dark mode coverage is incomplete:** Dark mode styles exist for comments, tables, and navigation, but many elements (priority badges, status pills, loading states) use light-mode-only colors.
- **UI-C4 — No semantic color naming:** Colors are used by hex value, not by purpose. There is no `--color-danger`, `--color-success`, `--color-warning` system.

---

## 2. Typography

### 2.1 Font Stack

| Context | Font | Source |
|---------|------|--------|
| Body text | Inter | Google Fonts (via MkDocs Material config) |
| Code | Roboto Mono | Google Fonts (via MkDocs Material config) |
| Clinical Tool | System font stack | `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` |

### 2.2 Font Sizing

| Element | Size | Context |
|---------|------|---------|
| Table body text | `0.8rem` | Plan tables (desktop) |
| Table body text | `0.75rem` | Plan tables (<1219px) |
| Venue column text | `0.65rem` | ED/HOSP/OPD/ICU columns |
| Priority badges | `0.55rem` – `0.65rem` | Varies by breakpoint |
| Comment body | `0.9rem` | Comment section |
| Inline popup text | `0.85rem` | Section comments |
| TOC items | `0.65rem` | Right sidebar (>1220px) |
| Delete dialog text | `0.95rem` | Confirmation overlay |

### 2.3 Typography Issues

- **UI-T1 — Table text is very small:** At `0.8rem` base (roughly 12.8px) and `0.65rem` for venue columns (roughly 10.4px), the plan tables are at the lower limit of readability, especially for clinicians who may be older or using the site in challenging environments (bright ORs, dim on-call rooms).
- **UI-T2 — No typographic scale:** Font sizes are arbitrary values rather than following a consistent modular scale.
- **UI-T3 — Font mismatch between MkDocs site and Clinical Tool:** The documentation uses Inter (Google Fonts) while the Clinical Tool uses the system font stack. This creates a subtle but noticeable inconsistency.
- **UI-T4 — No `font-display: swap`:** If Google Fonts CDN is slow, there could be a flash of invisible text (FOIT). MkDocs Material handles this internally, but it is worth noting.

---

## 3. Layout & Spacing

### 3.1 Page Structure

**Documentation Pages:**
```
┌─────────────────────────────────────────────┐
│ Header (MkDocs Material)                     │
├───────┬─────────────────────────┬───────────┤
│ Left  │ Content Area            │ Right TOC │
│ Nav   │ (plan tables)           │ (h2 list) │
│ 240px │ flexible                │ 11rem     │
├───────┴─────────────────────────┴───────────┤
│ Comments Section                             │
└─────────────────────────────────────────────┘
```

**Clinical Tool:**
```
┌─────────────────────────────────────────────┐
│ Sticky Header (back button + logo)           │
├─────────────────────────────────────────────┤
│ Controls (plan selector, venue tabs, legend) │
├────────────────────────┬────────────────────┤
│ Plan Sections          │ Selected Items     │
│ (checkable items)      │ Sidebar (380px)    │
│ flexible               │                    │
└────────────────────────┴────────────────────┘
```

### 3.2 Responsive Breakpoints

| Breakpoint | Behavior |
|-----------|----------|
| >1400px | Full layout: left nav + content + right TOC |
| 1220–1400px | TOC sidebar narrows to 11rem, table fonts compact |
| 769–1219px | Table fonts reduce further to 0.75rem |
| ≤768px | Mobile: column constraints relaxed, text wrapping |
| ≤1024px | Clinical Tool: single column (sidebar below content) |

### 3.3 Layout Issues

- **UI-L1 — No 375px (small phone) breakpoint:** The responsive system stops at 768px. On an iPhone SE or similar small device (375px wide), plan tables with 10 columns are still very cramped.
- **UI-L2 — Table column width is not optimized:** Venue columns (ED/HOSP/OPD/ICU) use `min-width: 28px` which is extremely tight. On some screens, the text "STAT" inside a 28px column overflows.
- **UI-L3 — Comment section has no max-width:** On ultrawide displays (>1400px), comments stretch to full content width, which reduces readability (line lengths exceed 80-100 characters).
- **UI-L4 — No spacing system:** Padding and margins use arbitrary values (6px, 8px, 10px, 12px, 16px, 20px, 24px, 32px) rather than a consistent spacing scale.
- **UI-L5 — Clinical Tool sidebar is fixed 380px:** On 1025-1200px screens, the sidebar takes up too much proportional space.

---

## 4. Component Audit

### 4.1 Priority Badges

```
Current: Rounded rectangles with colored background/text
Style: padding 2px 6px, border-radius 3px, font-weight 600
States: STAT (red), URGENT (orange), ROUTINE (blue), EXT (purple), N/A (gray)
```

**Issues:**
- **UI-B1 — Badge sizing varies by breakpoint but inconsistently:** At <1400px, badges shrink to `0.55rem` with `1px 3px` padding, which is nearly illegible.
- **UI-B2 — No hover state or interactive affordance:** Badges are static text, but some users might expect them to be filterable.

### 4.2 Tables

```
Current: Standard Markdown tables rendered by MkDocs
Headers: Teal background (#f0fdfa), dark teal text (#115e59)
Rows: Alternating stripes (#f0fdfa on even rows)
Venue columns: Lighter teal (#ccfbf1) header background
```

**Issues:**
- **UI-TAB1 — Tables have no sticky headers:** When scrolling long treatment tables, the column headers (Item, ED, HOSP, OPD, ICU, Rationale, etc.) disappear, requiring users to scroll back up to remember what each column is.
- **UI-TAB2 — No row hover highlight:** There is no hover state on table rows, making it hard to track which row you are reading across many columns.
- **UI-TAB3 — No responsive table strategy:** Tables are simply overflow-scrollable on mobile. A better approach would be card-based layout or column hiding on small screens.
- **UI-TAB4 — Row stripe color is very subtle:** `#f0fdfa` is barely distinguishable from white (`#ffffff`), reducing the effectiveness of the striping.

### 4.3 Navigation

```
Current: MkDocs Material left sidebar with collapsible sections
Active state: Left teal border (3px solid #0d9488)
Hover: Background #f0fdfa, text color #0d9488
Clinical Tool link: Gradient teal background with 🔧 prefix
```

**Issues:**
- **UI-N1 — Active state is subtle:** A 3px left border is the only indicator of the current page. In a sidebar with 144 items, this is easy to miss.
- **UI-N2 — Clinical Tool link styling breaks consistency:** The gradient background with emoji prefix makes it look like an ad or external link rather than a core feature.
- **UI-N3 — No section counts:** Category headers don't show how many plans they contain, which would help with orientation.

### 4.4 Comment System Components

```
Components: Comment form, comment list, vote buttons, inline comment triggers,
            section popup, delete confirmation dialog, toast notifications,
            nav badges
```

**Issues:**
- **UI-CM1 — Comment form is visually separated from plan content:** There is a significant visual break between the plan content and the comment section, making comments feel like an afterthought.
- **UI-CM2 — Vote buttons are small (14px text):** The 👍/👎 icons are small and the vote count text is `0.8rem`, which is hard to tap on mobile.
- **UI-CM3 — Inline comment buttons conflict with heading styles:** The 💬 buttons appended to h2 headings add visual noise to the content hierarchy.
- **UI-CM4 — Toast notifications lack dark mode support:** The toast system uses hardcoded white background with shadow, which looks jarring in dark mode.

### 4.5 Status Indicators

```
Draft: Amber warning banner with icon, draft badge in nav
Approved: Green badge, "STATUS: Approved" line
```

**Issues:**
- **UI-S1 — Draft warning banner is visually heavy:** The full-width amber banner at the top of draft plans takes up significant space and may alarm users unnecessarily.
- **UI-S2 — No visual difference between approved plan versions:** There is no indication when a plan was last updated or if it has been revised since initial approval.

---

## 5. Dark Mode Assessment

### 5.1 Implementation

Dark mode uses MkDocs Material's `[data-md-color-scheme="slate"]` attribute selector. Custom dark mode overrides are applied for:
- Comment system (backgrounds, text, borders)
- Table headers and row stripes
- Navigation hover states
- Inline comment popups
- TOC badges
- Status badges
- Delete confirmation dialog

### 5.2 Dark Mode Issues

- **UI-DM1 — Priority badges have no dark mode overrides:** STAT (red), URGENT (orange), etc. use light-mode colors in dark mode, which can be too bright and lose contrast.
- **UI-DM2 — Clinical Tool has no dark mode:** The standalone HTML page has its own CSS with no dark mode support at all.
- **UI-DM3 — Some borders are invisible in dark mode:** The `#e2e8f0` border color becomes nearly invisible against `#1e293b` backgrounds. Dark mode overrides address some but not all instances.
- **UI-DM4 — Loading spinner color is hardcoded:** The spinner uses `border-top: 3px solid #0d9488` which works in both modes, but the accompanying text color may not.

---

## 6. Consistency Analysis

### 6.1 Design Tokens Comparison

| Property | custom.css | Clinical Tool | Match? |
|----------|-----------|---------------|--------|
| Primary color | `#0d9488` | `var(--primary): #0d9488` | ✅ Yes |
| Primary dark | `#0f766e` | `var(--primary-dark): #0f766e` | ✅ Yes |
| Primary light | `#ccfbf1` | `var(--primary-light): #ccfbf1` | ✅ Yes |
| STAT color | `#991b1b` text | `var(--stat): #dc2626` | ❌ Different |
| Border color | `#e2e8f0` | `var(--border): #e5e7eb` | ❌ Different |
| Body font | Inter (Google Fonts) | System font stack | ❌ Different |
| Spacing | arbitrary | arbitrary | ⚠️ Both inconsistent |
| Border radius | 3px (badges), 4px (nav), 8px (popup) | 6px–12px | ❌ Different |

### 6.2 Consistency Issues

- **UI-CON1 — Two separate design systems:** The MkDocs site and Clinical Tool have evolved independently. They share primary teal but diverge on everything else.
- **UI-CON2 — Border radius varies wildly:** Values range from 3px to 12px across components with no pattern.
- **UI-CON3 — Box shadow styles are inconsistent:** At least 4 different shadow values are used (`0 1px 3px rgba(0,0,0,0.1)`, `0 1px 4px rgba(0,0,0,0.06)`, `0 4px 20px rgba(0,0,0,0.15)`, `0 25px 50px -12px rgba(0,0,0,0.25)`).
- **UI-CON4 — No icon system:** The site uses a mix of Material Design icons (via MkDocs), emoji (🔧💬👍👎), and text-only states.

---

## 7. Interaction Patterns

### 7.1 Hover & Focus States

| Element | Hover | Focus | Keyboard |
|---------|-------|-------|----------|
| Nav links | ✅ bg change + color | ✅ (Material default) | ✅ |
| Table rows | ❌ None | ❌ None | N/A |
| Priority badges | ❌ None | ❌ None | N/A |
| Comment vote buttons | Partial (opacity) | ❌ None | ❌ Not focusable |
| Inline comment buttons | ✅ Scale + color | ❌ None | ❌ Not focusable |
| Clinical Tool venue tabs | ✅ Border color | ❌ None | ❌ Not focusable |
| Clinical Tool checkboxes | ✅ Row highlight | ❌ None | ❌ Not standard |

### 7.2 Animation & Transitions

| Animation | Duration | Easing | Concern |
|-----------|----------|--------|---------|
| Loading spinner | 0.8s | linear | No reduced-motion |
| Nav link transitions | Not specified | — | No transition applied |
| Comment popup appearance | Not specified | — | Appears instantly |
| Toast notification | Not specified | — | Appears/disappears instantly |
| Inline comment button scale | Not specified | — | Implied by `:hover` transform |

**Issue:** Most state changes are instant with no transition, which feels abrupt. The few animations that exist don't respect `prefers-reduced-motion`.

---

## 8. Summary of UI Issues by Severity

### Critical (Visual functionality broken)
| ID | Issue | Impact |
|----|-------|--------|
| UI-TAB3 | No responsive table strategy | Tables are unreadable on mobile devices |
| UI-C1 | No CSS variables in custom.css | Maintenance nightmare, no theming |

### High (Significant visual quality gap)
| ID | Issue | Impact |
|----|-------|--------|
| UI-CON1 | Two separate design systems | Inconsistent experience between MkDocs and Clinical Tool |
| UI-DM1 | Priority badges not dark-mode-aware | Bright colors in dark mode hurt readability |
| UI-DM2 | Clinical Tool has no dark mode | Jarring white screen for dark mode users |
| UI-T1 | Table text too small | Readability concern for primary content |
| UI-TAB1 | No sticky table headers | Users lose column context on long tables |

### Medium (Polish / consistency)
| ID | Issue | Impact |
|----|-------|--------|
| UI-C2 | Inconsistent secondary text colors | Visual inconsistency |
| UI-L1 | No 375px breakpoint | Small phone experience is cramped |
| UI-CON2 | Border radius varies wildly | Visual inconsistency |
| UI-B1 | Badges too small at compact breakpoint | Legibility concern |
| UI-N1 | Active nav state is subtle | Disorientation in large nav |

### Low (Refinement)
| ID | Issue | Impact |
|----|-------|--------|
| UI-T3 | Font mismatch (Inter vs system) | Subtle inconsistency |
| UI-L4 | No spacing system | Developer experience |
| UI-CM3 | Inline comment buttons add noise | Minor visual clutter |
| UI-TAB4 | Row stripe too subtle | Barely visible differentiation |

---

*End of UI Audit. See also: [UX Audit](UX_AUDIT.md) | [Design System](DESIGN_SYSTEM.md) | [Roadmap](ROADMAP.md)*
