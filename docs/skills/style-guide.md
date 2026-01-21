---
title: Style Guide
---

# Clinical Plan Style Guide

Guidelines for creating and maintaining clinical decision support templates.

## Core Principles

1. **Evidence-Based** - Recommendations should be grounded in current guidelines and literature
2. **Actionable** - Each item should be a clear, specific action
3. **Setting-Aware** - Consider applicability across ED, Hospital, Outpatient, and ICU settings
4. **Safe** - Include contraindications, monitoring requirements, and safety checks
5. **No PHI** - Never include patient-identifiable information

## Document Structure

All plans follow an 8-section format:

### Section A: Action Items (Primary)

1. **Laboratory Workup** (1A Core, 1B Extended, 1C Specialized)
2. **Diagnostic Imaging & Studies** (2A Essential, 2B Extended, 2C Specialized)
3. **Treatment** (3A Acute, 3B Symptomatic, 3C Maintenance, 3D Disease-Modifying)
4. **Other Recommendations** (4A Referrals, 4B Patient Instructions, 4C Lifestyle)

### Section B: Reference (Supporting)

5. **Differential Diagnosis**
6. **Monitoring Parameters**
7. **Disposition Criteria**
8. **Evidence & References**

## Table Format

Use the multi-column setting-priority format. **IMPORTANT:** Venue columns (ED, HOSP, OPD, ICU) must be the **last 4 columns** for CSS styling to work correctly.

### Labs/Studies Table

```markdown
| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC  | Infection screen | Normal | STAT | STAT | ROUTINE | STAT |
```

### Treatment Table

```markdown
| Treatment | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Drug Name | 10 mg PO daily | Allergy | LFTs | STAT | STAT | ROUTINE | STAT |
```

> ⚠️ **Column Order Matters:** The CSS applies narrow column widths to the last 4 columns, expecting them to be ED/HOSP/OPD/ICU. Incorrect column order will cause rendering issues.

### Lumbar Puncture Section

**IMPORTANT:** Lumbar Puncture appears under **Laboratory Workup** in the clinical tool (CSF analysis IS laboratory work). In the markdown file, place it as `### LUMBAR PUNCTURE` after the imaging subsections (2A/2B/2C) - the JSON generator will position it correctly under Labs.

```markdown
### LUMBAR PUNCTURE

**Indication:** [Clinical indication for LP]
**Timing:** URGENT if [condition]; ROUTINE for [condition]
**Volume Required:** 10-15 mL (standard diagnostic)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | Rule out elevated ICP | 10-20 cm H2O | URGENT | ROUTINE | ROUTINE | - |
| Cell count (tubes 1 and 4) | Inflammation, infection | WBC <5, RBC 0 | URGENT | ROUTINE | ROUTINE | - |

**Special Handling:** [Notes about transport, timing]
**Contraindications:** [List contraindications]
```

> **Clinical Tool Display:** When LP studies are selected in the clinical tool, they appear grouped under "Laboratory Workup > Lumbar Puncture" alongside other lab sections.

## Priority Levels

| Priority | Meaning | When to Use |
|----------|---------|-------------|
| STAT | Immediate | Time-critical actions |
| URGENT | Within hours | Important but not emergent |
| ROUTINE | Standard timing | Scheduled/non-urgent |
| EXT | Extended/atypical | Specialized or second-line |
| - | Not applicable | Setting doesn't apply |

## Writing Guidelines

### Be Specific

- **Good:** "Levetiracetam 500 mg PO BID, titrate to 1500 mg BID over 2 weeks"
- **Bad:** "Start anti-seizure medication"

### One Drug Per Row

Each medication gets its own table row with complete dosing information.

### Include Contraindications

Always note absolute and relative contraindications.

### Use Plain Language for Patient Instructions

Section 4B should be understandable by patients and families.

## Medication Formatting

- Include: Generic name, route, dose, frequency, titration schedule, maximum dose
- Include: Contraindications, monitoring requirements
- Example: "Gabapentin 300 mg PO TID; titrate by 300 mg/day every 3-5 days to 1800-3600 mg/day divided TID | CrCl adjustment required | Monitor sedation, edema"

## Quality Standards

- Target validation score: 90%+ (54/60 across 6 domains)
- All plans require physician review before clinical use
- Update plans when new guidelines are published

## Version Control

- Use semantic versioning (v1.0, v1.1, v2.0)
- Minor changes: +0.1 (typos, clarifications)
- Major changes: +1.0 (new sections, significant clinical updates)
- Document all changes in the Change Log section

## YAML Frontmatter

All plan files require frontmatter:

```yaml
---
title: "Diagnosis Name"
description: "Brief description of what the plan covers"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
tags:
  - category
  - subcategory
---
```
