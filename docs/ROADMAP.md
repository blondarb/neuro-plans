# Neuro Plans - Development Roadmap

**Version:** 1.0
**Created:** January 24, 2026
**Status:** Active Development

---

## Overview

This roadmap outlines planned improvements to the clinical plan generation system, with a focus on medication handling, clickable dosing, and overall standardization before scaling to additional neurological topics.

---

## Phase 1: Medication Format Standardization (Foundation)

**Goal:** Create a consistent, parseable medication format across all treatment sections.

**Priority:** HIGH - Must complete before building new topics

### 1.1 Standardize Treatment Table Columns

| Current Problem | Solution |
|-----------------|----------|
| Section 3A/3B/3C have inconsistent columns | Standardize ALL treatment sections to same column order |
| Route only in Section 3D (DMTs) | Add Route column to ALL treatment sections |
| Column order varies | Fixed order: Treatment → Route → Indication → Dosing → Contraindications → Monitoring → ED → HOSP → OPD → ICU |

**New Standard Treatment Table Format (All Sections):**
```markdown
| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
```

### 1.2 Structured Dosing Format

**Current Problem:** Dosing is unstructured text that can't be parsed into order sentences.

**Example of current format:**
```
Start 5 mg TID; increase by 5 mg/dose every 3 days; max 80 mg/day
```

**New structured dosing format (double-colon delimited fields within dosing cell):**
```
5 mg :: PO :: TID :: Start 5 mg TID, titrate by 5 mg q3d, max 80 mg/day
```

**Format:** `dose :: route :: frequency :: full_instructions`

**Note:** We use `::` instead of `|` because `|` conflicts with markdown table syntax.

This allows the clinical tool to:
1. Generate order sentences: "Baclofen 5 mg PO TID"
2. Display full dosing guidance on hover/click
3. Support future weight-based calculations

### 1.3 Files to Update

| File | Changes |
|------|---------|
| `skills/neuro-builder-SKILL.md` | New table format, structured dosing spec |
| `skills/neuro-checker-SKILL.md` | Validation rules for new format |
| `skills/neuro-rebuilder-SKILL.md` | Update pattern matching for new columns |
| `scripts/generate_json.py` | Parse structured dosing into separate JSON fields |

---

## Phase 2: Clickable Dosing (Clinical Tool Enhancement)

**Goal:** Make medication dosing interactive with copy-ready order sentences.

**Priority:** HIGH - Key UX improvement

### 2.1 JSON Schema Enhancement

Add structured dosing fields to medication items:

```json
{
  "item": "Baclofen",
  "route": "PO",
  "indication": "Spasticity",
  "dosing": {
    "dose": "5 mg",
    "route": "PO",
    "frequency": "TID",
    "instructions": "Start 5 mg TID, titrate by 5 mg/dose q3d, max 80 mg/day",
    "orderSentence": "Baclofen 5 mg PO TID"
  },
  "contraindications": "Renal impairment (reduce dose)",
  "monitoring": "Sedation, weakness; do NOT stop abruptly",
  "ED": "-",
  "HOSP": "ROUTINE",
  "OPD": "ROUTINE",
  "ICU": "ROUTINE"
}
```

### 2.2 Clinical Tool UI Changes

| Feature | Behavior |
|---------|----------|
| Dosing badge click | Copies order sentence to clipboard with visual feedback |
| Dosing badge tooltip | Shows full dosing instructions on hover |
| Selected items sidebar | Displays order sentence format for medications |
| Copy all selected | Includes order sentences (not full instructions) |

### 2.3 Order Sentence Format

Standard order sentence pattern:
```
[Drug Name] [Dose] [Route] [Frequency] [Duration if applicable] [PRN indication if applicable]
```

**Examples:**
- `Baclofen 5 mg PO TID`
- `Methylprednisolone 1000 mg IV daily x 5 days`
- `Lorazepam 4 mg IV push PRN seizure`
- `Levetiracetam 1000 mg IV load, then 500 mg IV q12h`

---

## Phase 3: Common Dosing Regimens (Future Enhancement)

**Goal:** Pre-built dosing options for medications with common titration schedules.

**Priority:** MEDIUM - Nice to have after core functionality

### 3.1 Regimen Templates

For medications with standard titration protocols, offer selectable regimens:

```json
{
  "item": "Gabapentin",
  "regimens": [
    {
      "name": "Conservative Start",
      "orderSentence": "Gabapentin 100 mg PO TID",
      "instructions": "Start 100 mg TID, increase by 100 mg/dose q3d as tolerated"
    },
    {
      "name": "Standard Start",
      "orderSentence": "Gabapentin 300 mg PO TID",
      "instructions": "Start 300 mg TID, may increase to 600 mg TID"
    },
    {
      "name": "Rapid Titration (Inpatient)",
      "orderSentence": "Gabapentin 300 mg PO TID, titrate to 600 mg TID over 3 days",
      "instructions": "Day 1: 300 TID, Day 2: 400 TID, Day 3+: 600 TID"
    }
  ]
}
```

### 3.2 UI for Regimen Selection

- Dropdown or accordion under medication when clicked
- Shows regimen name + order sentence preview
- Click to select and copy

---

## Phase 4: Other Improvements

### 4.1 Medication Interaction Checking (Future)

- Flag potential interactions when multiple medications selected
- Use structured drug data to identify concerns
- Display warning icon in sidebar

### 4.2 Weight-Based Dosing Calculator (Future)

- For medications with mg/kg dosing
- Input patient weight → calculate dose
- Update order sentence automatically

### 4.3 Renal/Hepatic Dose Adjustments (Future)

- Flag medications needing adjustment
- Show alternative dosing for impaired organ function

---

## Implementation Priority

| Phase | Items | Priority | Estimated Effort |
|-------|-------|----------|------------------|
| 1.1 | Standardize columns | HIGH | Medium |
| 1.2 | Structured dosing format | HIGH | Medium |
| 1.3 | Update skills | HIGH | Medium |
| 2.1 | JSON schema | HIGH | Low |
| 2.2 | Clinical tool UI | HIGH | Medium |
| 2.3 | Order sentence logic | HIGH | Low |
| 3.x | Regimen templates | MEDIUM | High |
| 4.x | Future enhancements | LOW | High |

---

## Quality Gates Before Topic Generation

Before generating new clinical topics at scale, ensure:

- [ ] Phase 1 complete (standardized format)
- [ ] Phase 2 complete (clickable dosing works)
- [ ] Existing approved plans updated to new format
- [ ] generate_json.py handles new format
- [ ] Checker validates new format requirements
- [ ] At least one plan tested end-to-end with new format

---

## Change Log

**v1.0 (January 24, 2026)**
- Initial roadmap creation
- Defined Phase 1-4 improvements
- Specified structured dosing format
- Outlined clinical tool enhancements
