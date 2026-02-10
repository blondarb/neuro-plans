# Design System — Neuro Clinical Plans

**Date:** February 2026
**Status:** Proposed (derived from UI/UX Audit findings)

---

## 1. Design Principles

1. **Clinical clarity first** — Every design decision should optimize for fast, accurate clinical decision-making under time pressure.
2. **Scan, don't read** — Clinicians scan tables and lists for relevant items. Visual hierarchy, badges, and color coding should support scanning, not require reading.
3. **Setting-aware** — The interface should adapt to the care setting context (ED urgency vs outpatient thoroughness).
4. **Accessible by default** — All custom components must meet WCAG 2.1 AA. Color is never the sole information channel.
5. **Consistent across surfaces** — The MkDocs documentation site, Clinical Tool, and any future mobile experience should feel like one product.

---

## 2. Color Tokens

### 2.1 Proposed Token System

Replace all hardcoded hex values with CSS custom properties. Define tokens at three levels: primitive, semantic, and component.

**Primitive Colors (base palette):**

```css
:root {
  /* Teal scale */
  --color-teal-50: #f0fdfa;
  --color-teal-100: #ccfbf1;
  --color-teal-200: #99f6e4;
  --color-teal-300: #5eead4;
  --color-teal-400: #2dd4bf;
  --color-teal-500: #14b8a6;
  --color-teal-600: #0d9488;
  --color-teal-700: #0f766e;
  --color-teal-800: #115e59;
  --color-teal-900: #134e4a;

  /* Neutral scale */
  --color-slate-50: #f8fafc;
  --color-slate-100: #f1f5f9;
  --color-slate-200: #e2e8f0;
  --color-slate-300: #cbd5e1;
  --color-slate-400: #94a3b8;
  --color-slate-500: #64748b;
  --color-slate-600: #475569;
  --color-slate-700: #334155;
  --color-slate-800: #1e293b;
  --color-slate-900: #0f172a;

  /* Priority scale */
  --color-red-50: #fef2f2;
  --color-red-100: #fee2e2;
  --color-red-200: #fca5a5;
  --color-red-500: #ef4444;
  --color-red-700: #b91c1c;
  --color-red-800: #991b1b;

  --color-orange-50: #fff7ed;
  --color-orange-100: #ffedd5;
  --color-orange-200: #fed7aa;
  --color-orange-500: #f97316;
  --color-orange-700: #c2410c;
  --color-orange-800: #9a3412;

  --color-blue-50: #eff6ff;
  --color-blue-100: #dbeafe;
  --color-blue-200: #93c5fd;
  --color-blue-500: #3b82f6;
  --color-blue-700: #1d4ed8;
  --color-blue-800: #1e40af;

  --color-purple-50: #faf5ff;
  --color-purple-100: #f3e8ff;
  --color-purple-200: #d8b4fe;
  --color-purple-500: #a855f7;
  --color-purple-700: #7e22ce;
  --color-purple-800: #6b21a8;

  --color-amber-500: #f59e0b;
  --color-amber-600: #d97706;
  --color-green-500: #10b981;
  --color-green-600: #059669;
}
```

**Semantic Tokens (purpose-driven):**

```css
:root {
  /* Surfaces */
  --surface-primary: var(--color-slate-50);
  --surface-secondary: #ffffff;
  --surface-elevated: #ffffff;

  /* Text */
  --text-primary: var(--color-slate-800);
  --text-secondary: var(--color-slate-500);
  --text-tertiary: var(--color-slate-400);
  --text-inverse: #ffffff;

  /* Borders */
  --border-default: var(--color-slate-200);
  --border-strong: var(--color-slate-300);
  --border-focus: var(--color-teal-600);

  /* Interactive */
  --interactive-primary: var(--color-teal-600);
  --interactive-primary-hover: var(--color-teal-700);
  --interactive-primary-active: var(--color-teal-800);
  --interactive-primary-subtle: var(--color-teal-50);

  /* Status */
  --status-danger: var(--color-red-500);
  --status-danger-bg: var(--color-red-50);
  --status-warning: var(--color-amber-500);
  --status-warning-bg: var(--color-orange-50);
  --status-success: var(--color-green-500);
  --status-success-bg: var(--color-teal-50);
  --status-info: var(--color-blue-500);
  --status-info-bg: var(--color-blue-50);

  /* Priority badges */
  --priority-stat-bg: var(--color-red-100);
  --priority-stat-text: var(--color-red-800);
  --priority-stat-border: var(--color-red-200);

  --priority-urgent-bg: var(--color-orange-100);
  --priority-urgent-text: var(--color-orange-800);
  --priority-urgent-border: var(--color-orange-200);

  --priority-routine-bg: var(--color-blue-100);
  --priority-routine-text: var(--color-blue-800);
  --priority-routine-border: var(--color-blue-200);

  --priority-ext-bg: var(--color-purple-100);
  --priority-ext-text: var(--color-purple-800);
  --priority-ext-border: var(--color-purple-200);

  --priority-na-bg: var(--color-slate-100);
  --priority-na-text: var(--color-slate-500);
  --priority-na-border: var(--color-slate-300);
}

/* Dark mode overrides */
[data-md-color-scheme="slate"] {
  --surface-primary: var(--color-slate-900);
  --surface-secondary: var(--color-slate-800);
  --surface-elevated: var(--color-slate-700);

  --text-primary: var(--color-slate-100);
  --text-secondary: var(--color-slate-400);
  --text-tertiary: var(--color-slate-500);

  --border-default: var(--color-slate-700);
  --border-strong: var(--color-slate-600);

  --interactive-primary: var(--color-teal-400);
  --interactive-primary-hover: var(--color-teal-300);

  /* Priority badges in dark mode - softer backgrounds */
  --priority-stat-bg: rgba(239, 68, 68, 0.15);
  --priority-stat-text: var(--color-red-200);
  --priority-urgent-bg: rgba(249, 115, 22, 0.15);
  --priority-urgent-text: var(--color-orange-200);
  --priority-routine-bg: rgba(59, 130, 246, 0.15);
  --priority-routine-text: var(--color-blue-200);
  --priority-ext-bg: rgba(168, 85, 247, 0.15);
  --priority-ext-text: var(--color-purple-200);
  --priority-na-bg: rgba(148, 163, 184, 0.1);
  --priority-na-text: var(--color-slate-400);
}
```

---

## 3. Typography Scale

### 3.1 Proposed Scale (based on 1rem = 16px)

| Token | Size | Line Height | Weight | Usage |
|-------|------|------------|--------|-------|
| `--text-xs` | 0.75rem (12px) | 1.33 | 400 | Badges, labels, footnotes |
| `--text-sm` | 0.875rem (14px) | 1.43 | 400 | Table cells, secondary text |
| `--text-base` | 1rem (16px) | 1.5 | 400 | Body text, comments |
| `--text-lg` | 1.125rem (18px) | 1.56 | 500 | Section subheadings |
| `--text-xl` | 1.25rem (20px) | 1.4 | 600 | Section headings |
| `--text-2xl` | 1.5rem (24px) | 1.33 | 700 | Page titles |

### 3.2 Minimum Sizes

- **Table body text:** Never below `0.875rem` (14px) — current `0.8rem` is too small
- **Priority badges:** Never below `0.6875rem` (11px) — current `0.55rem` is illegible
- **Venue columns:** Never below `0.75rem` (12px) — current `0.65rem` is too small

### 3.3 Font Stack

Unify all surfaces on Inter:

```css
:root {
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'Roboto Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
}
```

---

## 4. Spacing Scale

### 4.1 Base-4 Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight padding (inside badges) |
| `--space-2` | 8px | Standard inner padding |
| `--space-3` | 12px | Component internal spacing |
| `--space-4` | 16px | Standard element gap |
| `--space-5` | 20px | Section inner padding |
| `--space-6` | 24px | Section gap |
| `--space-8` | 32px | Large section separation |
| `--space-10` | 40px | Page-level vertical spacing |
| `--space-12` | 48px | Major section breaks |

---

## 5. Border Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 4px | Badges, small elements |
| `--radius-md` | 8px | Cards, inputs, buttons |
| `--radius-lg` | 12px | Dialogs, popovers |
| `--radius-full` | 9999px | Pills, circular elements |

---

## 6. Shadow Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elevation (cards) |
| `--shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.1)` | Standard elevation (popups) |
| `--shadow-lg` | `0 10px 15px -3px rgba(0,0,0,0.1)` | High elevation (dialogs) |
| `--shadow-xl` | `0 20px 25px -5px rgba(0,0,0,0.1)` | Overlay elevation (modals) |

---

## 7. Responsive Breakpoints

### 7.1 Proposed Breakpoint System

| Token | Value | Rationale |
|-------|-------|-----------|
| `--bp-sm` | 375px | iPhone SE, small phones |
| `--bp-md` | 768px | iPad portrait, large phones landscape |
| `--bp-lg` | 1024px | iPad landscape, small laptops |
| `--bp-xl` | 1280px | Standard laptops |
| `--bp-2xl` | 1536px | Large monitors |

### 7.2 Mobile-First Strategy

Styles should be written mobile-first, adding complexity at wider breakpoints:

```css
/* Base: mobile (< 375px) */
.plan-table { font-size: var(--text-sm); }

/* Small phone and up */
@media (min-width: 375px) { ... }

/* Tablet and up */
@media (min-width: 768px) { ... }

/* Laptop and up */
@media (min-width: 1024px) { ... }

/* Desktop and up */
@media (min-width: 1280px) { ... }
```

---

## 8. Component Specifications

### 8.1 Priority Badge

```
Padding: var(--space-1) var(--space-2)     [4px 8px]
Border-radius: var(--radius-sm)             [4px]
Font-size: var(--text-xs)                   [12px]
Font-weight: 600
Letter-spacing: 0.02em
Text-transform: uppercase
Min-width: 48px (centered text)
```

### 8.2 Clinical Table

```
Header:
  Background: var(--interactive-primary-subtle)
  Text: var(--interactive-primary-active)
  Font-weight: 600
  Font-size: var(--text-sm)
  Padding: var(--space-2) var(--space-3)

Body cell:
  Font-size: var(--text-sm) minimum
  Padding: var(--space-2) var(--space-3)
  Border-bottom: 1px solid var(--border-default)

Row hover:
  Background: var(--color-teal-50)

Row stripe:
  Even rows: var(--surface-primary)

Sticky header (new):
  position: sticky; top: 0; z-index: 10;
```

### 8.3 Comment Card

```
Background: var(--surface-secondary)
Border: 1px solid var(--border-default)
Border-radius: var(--radius-md)
Padding: var(--space-4)
Margin-bottom: var(--space-3)

Vote button:
  Min-size: 44x44px (touch target)
  Font-size: var(--text-base)
  Border-radius: var(--radius-sm)
```

### 8.4 Venue Tab (Clinical Tool)

```
Padding: var(--space-2) var(--space-5)
Border: 2px solid var(--border-default)
Border-radius: var(--radius-md)
Font-weight: 500
Min-height: 44px (touch target)

Active state:
  Background: var(--interactive-primary)
  Border-color: var(--interactive-primary)
  Color: var(--text-inverse)
```

---

## 9. Accessibility Requirements

### 9.1 Color Contrast

All text must meet WCAG 2.1 AA contrast ratios:
- **Normal text (< 18px):** 4.5:1 minimum
- **Large text (≥ 18px or ≥ 14px bold):** 3:1 minimum
- **UI components:** 3:1 minimum against adjacent colors

### 9.2 Focus Indicators

All interactive elements must have visible focus indicators:
```css
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}
```

### 9.3 Touch Targets

Minimum 44x44px touch target for all interactive elements on mobile.

### 9.4 Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 9.5 ARIA Requirements

All custom interactive components must include:
- `role` attribute (button, tab, tabpanel, dialog, etc.)
- `aria-label` or `aria-labelledby` for non-text elements
- `aria-expanded` for collapsible sections
- `aria-live="polite"` for dynamic content (toasts, vote counts)
- `aria-current="page"` for active navigation items

---

## 10. Migration Path

### Phase 1: Token Foundation (Quick Win)
1. Add all CSS custom properties to the top of `custom.css`
2. Replace hardcoded hex values with token references (search-and-replace)
3. Add dark mode token overrides

### Phase 2: Component Updates
1. Update priority badges to use tokens and meet minimum sizes
2. Add sticky table headers
3. Add row hover states
4. Increase minimum font sizes

### Phase 3: Clinical Tool Alignment
1. Import shared token CSS into Clinical Tool
2. Add dark mode support to Clinical Tool
3. Unify font stack (Inter everywhere)

### Phase 4: Accessibility
1. Add ARIA attributes to comment system
2. Add ARIA attributes to Clinical Tool
3. Add focus management for dynamic content
4. Add `prefers-reduced-motion` support

---

*End of Design System. See also: [UX Audit](UX_AUDIT.md) | [UI Audit](UI_AUDIT.md) | [Roadmap](ROADMAP.md)*
