---
title: Checker Skill
---

---
name: neuro-checker
description: Validates clinical decision support recommendations for neurological diagnoses. Scores content across six domains (completeness, accuracy, safety, objectivity, setting appropriateness, usability) and provides specific revision suggestions. Use after running neuro-builder to validate output quality, or when reviewing any clinical recommendation content for accuracy and safety.
---

# Neuro Clinical Recommendation Checker

Validate and score clinical decision support content across six quality domains. Provides structured feedback for iterative improvement.

## Expected Structure

Documents should have 8 sections in two groups:

**Section A: Action Items (Primary)**
1. Laboratory Workup (1A, 1B, 1C)
2. Diagnostic Imaging & Studies (2A, 2B, 2C)
3. Treatment (3A, 3B, 3C, 3D)
4. Other Recommendations (4A, 4B, 4C) Ã¢â€ Â **Must be diagnosis-specific**

**Section B: Reference (Supporting)**
5. Differential Diagnosis
6. Monitoring Parameters
7. Disposition Criteria
8. Evidence & References

## Expected Table Format (Option A Multi-Column)

Tables should use the multi-column setting-priority format:

**Labs/Studies:**
```
| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
```

**Treatments:**
```
| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
```

**Priority values:** STAT | URGENT | ROUTINE | EXT | - (not applicable)

## Validation Domains

Score each domain 0-10:

### 1. COMPLETENESS (0-10)
- Are all 8 sections present and populated?
- Are essential labs, imaging, and treatments included?
- Are there obvious gaps in the workup?
- Is the differential diagnosis comprehensive?
- **Setting Coverage:** Are all applicable settings (ED, HOSP, OPD, ICU) represented?
- **Medication Coverage:**
  - [ ] Each medication on its own row (not grouped)?
  - [ ] Complete dosing for each drug (start, titrate, max)?
  - [ ] Symptomatic treatments cover relevant categories (pain, spasticity, bladder, mood, fatigue)?
  - [ ] DMTs individually listed with pre-treatment requirements (if applicable)?
- **Section 4 Checklist:**
  - [ ] 4A (Referrals & Consults) present with Ã¢â€°Â¥5 relevant referrals?
  - [ ] 4B (Patient Instructions) present with Ã¢â€°Â¥5 actionable instructions?
  - [ ] 4C (Lifestyle & Prevention) present with Ã¢â€°Â¥3 recommendations?
  - [ ] All Section 4 content is diagnosis-specific (not generic)?

### 2. ACCURACY (0-10)
- Are drug dosages correct?
- Are diagnostic criteria accurately stated?
- Are contraindications complete?
- Any factual errors?
- Are priority levels appropriate for each setting?

### 3. SAFETY (0-10)
- Are critical contraindications noted?
- Are drug interactions or monitoring requirements included?
- Are red flags and escalation triggers clear?
- Any potentially dangerous omissions?
- **Section 4B Safety Check:** Are return precautions specific and actionable?

### 4. OBJECTIVITY (0-10)
- Are claims evidence-based or clearly labeled as expert opinion?
- Is language neutral (no promotional bias)?
- Are limitations of evidence acknowledged?

### 5. SETTING APPROPRIATENESS (0-10)
- **Are all four settings (ED, HOSP, OPD, ICU) appropriately covered?**
- Are priorities correct for each setting (STAT in ED, ROUTINE in OPD)?
- Is "-" used correctly (truly not applicable, not just "less common")?
- **Flag gaps:** Missing OPD labs? Missing ED treatments?
- Would recommendations be actionable in each tagged setting?

### 6. USABILITY (0-10)
- Is format consistent and parseable?
- Is the multi-column format correctly structured?
- Could this be directly converted to JSON for clinical tools?
- **Are recommendations written as directives (not suggestions)?**
- **Section 4 Usability:** Are patient instructions written in plain language?

## CRITICAL: Setting Coverage Validation

**This is the most important new check.** For each diagnosis, verify:

### Setting Coverage Checklist

| Section | ED Coverage | HOSP Coverage | OPD Coverage | ICU Coverage |
|---------|-------------|---------------|--------------|--------------|
| 1. Labs | Ã¢â€°Â¥3 tests? | Ã¢â€°Â¥3 tests? | Ã¢â€°Â¥3 tests? | If applicable? |
| 2. Imaging | If urgent needed? | Ã¢â€°Â¥1 study? | Ã¢â€°Â¥1 study? | If applicable? |
| 3. Treatment | Acute therapies? | Maintenance? | Maintenance? | Critical care? |
| 4A. Referrals | If applicable? | Ã¢â€°Â¥3 consults? | Ã¢â€°Â¥3 consults? | If applicable? |
| 4B. Instructions | Discharge teaching? | Discharge teaching? | All applicable? | N/A |

### Common Coverage Gaps to Flag

| Gap Type | Example | Impact |
|----------|---------|--------|
| **Missing OPD labs** | Seizure workup has no OPD-tagged labs | Outpatient neurologist can't order workup |
| **Missing OPD imaging** | MRI only tagged for ED/HOSP | Clinic-based imaging not supported |
| **Missing HOSP maintenance** | Only acute treatments tagged | Admitted patients don't get home meds continued |
| **Overuse of "-"** | OPD marked "-" for tests that CAN be done outpatient | Limits ambulatory care |
| **Missing ED consults** | Referrals only tagged OPD | Delays specialty input in emergencies |

### When "-" Is Appropriate

"-" means **truly not applicable**, not "less common" or "usually done elsewhere."

| Appropriate "-" | Inappropriate "-" |
|-----------------|-------------------|
| Prolactin for OPD (only useful <20 min post-ictal) | Basic metabolic panel for OPD |
| ICU-only monitoring for routine outpatient | MRI brain for OPD (can be ordered from clinic) |
| Emergent intubation meds for OPD | Maintenance AEDs for ED (may need to continue) |

## Output Format

```
DIAGNOSIS REVIEWED: [Name]
VERSION: [if applicable]

## SCORES

| Domain | Score | Notes |
|--------|-------|-------|
| Completeness | X/10 | [brief note] |
| Accuracy | X/10 | [brief note] |
| Safety | X/10 | [brief note] |
| Objectivity | X/10 | [brief note] |
| Setting Appropriateness | X/10 | [brief note] |
| Usability | X/10 | [brief note] |

**OVERALL SCORE: X/60 (X%)**

## SETTING COVERAGE ASSESSMENT

| Section | ED | HOSP | OPD | ICU | Gaps Identified |
|---------|:--:|:----:|:---:|:---:|-----------------|
| 1. Labs | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | [specific gaps] |
| 2. Imaging | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | [specific gaps] |
| 3. Treatment | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | [specific gaps] |
| 4. Other | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | Ã¢Å“â€œ/Ã¢Å“â€” | [specific gaps] |

## SECTION 4 ASSESSMENT

| Subsection | Present | Count | Diagnosis-Specific | Notes |
|------------|---------|-------|-------------------|-------|
| 4A Referrals | Y/N | X items | Y/N | [note] |
| 4B Patient Instructions | Y/N | X items | Y/N | [note] |
| 4C Lifestyle | Y/N | X items | Y/N | [note] |

## MEDICATION ASSESSMENT

| Criterion | Met? | Notes |
|-----------|------|-------|
| Each drug on individual row (not grouped) | Y/N | [note] |
| Complete dosing (start, titrate, max) | Y/N | [list any drugs missing dosing] |
| Contraindications listed for each drug | Y/N | [note] |
| Monitoring specified for each drug | Y/N | [note] |
| Symptomatic categories covered | Y/N | [list missing: pain, spasticity, bladder, mood, fatigue, etc.] |
| Section 3B has Indication column | Y/N | [note] |
| Section 3D has Route + Pre-Treatment columns | Y/N or N/A | [note] |

## SECTION 6 MONITORING ASSESSMENT

| Criterion | Met? | Notes |
|-----------|------|-------|
| Venue columns present (ED, HOSP, OPD, ICU) | Y/N | [Section 6 must have venue columns] |
| Frequency column present | Y/N | [note] |
| Target/threshold specified for each parameter | Y/N | [note] |
| Action if abnormal specified | Y/N | [note] |
| Critical safety monitoring included (if applicable) | Y/N | [e.g., respiratory function for GBS/MG] |
| Longitudinal monitoring has OPD coverage | Y/N | [note] |

## CRITICAL ISSUES (Must Fix)

[List any dangerous or major errors - these block approval]

C1. [Section] - [Description of critical issue]
C2. [Section] - [Description of critical issue]

## SETTING COVERAGE ISSUES

[List specific setting gaps - high priority]

S1. [Section] - [Setting gap: e.g., "Labs section has no OPD coverage - outpatient workup not possible"]
S2. [Section] - [Setting gap]

## MEDICATION ISSUES

[List medication comprehensiveness gaps - high priority]

M1. [Section] - [Medication issue: e.g., "Drugs grouped as 'SSRIs' instead of individual rows"]
M2. [Section] - [Medication issue: e.g., "Gabapentin missing titration schedule"]
M3. [Section] - [Medication issue: e.g., "No bladder dysfunction treatments included"]

## RECOMMENDED REVISIONS

[Specific suggestions ranked by priority]

R1. [Section] - [Specific revision with rationale]
R2. [Section] - [Specific revision with rationale]
...

## STRENGTHS

[What was done well - reinforces good patterns]

S1. [Description]
S2. [Description]

## VERIFICATION NEEDED

[Items requiring clinical expert verification]

V1. [Item needing physician confirmation]
V2. [Item needing physician confirmation]
```

## Checker Principles

1. **Prioritize patient safety above all** - Flag any potentially dangerous omissions or errors as CRITICAL
2. **Validate comprehensive setting coverage** - Flag gaps in ED, HOSP, OPD, or ICU coverage
3. **Flag unsupported claims** - Note where evidence is missing or weak
4. **Be specific in feedback** - Cite exact section/row needing revision
5. **Recommend verification when uncertain** - Don't assume error if unclear, flag for expert review
6. **Check for appropriate "-" usage** - Ensure "-" means truly not applicable
7. **Verify directive language** - Recommendations should be checkbox-ready, not suggestions
8. **Validate Section 4 specificity** - Flag generic or copy-paste content that doesn't fit the diagnosis

## Common Issues to Check

**Medication Comprehensiveness (NEW - HIGH PRIORITY):**
- Are all medications listed individually (not grouped as "SSRIs" or "beta-blockers")?
- Does each drug have complete dosing (start dose, titration, max dose)?
- Are contraindications listed for each medication?
- Is monitoring specified for each medication?
- For DMTs: Are pre-treatment requirements listed?
- Are relevant symptomatic treatment categories covered (pain, spasticity, bladder, mood, fatigue)?
- Does Section 3B include an "Indication" column?
- Does Section 3D include "Route" and "Pre-Treatment Requirements" columns (if DMTs apply)?

**Setting Coverage (HIGH PRIORITY):**
- Missing OPD coverage in Labs section
- Missing OPD coverage in Imaging section
- Overuse of "-" where tests/treatments ARE applicable
- Inconsistent priorities across settings
- Missing HOSP column for maintenance therapies

**Section 6 Monitoring (HIGH PRIORITY):**
- Missing venue columns (ED, HOSP, OPD, ICU) - all monitoring parameters need venue columns
- Missing critical safety monitoring (respiratory function for neuromuscular conditions)
- Missing longitudinal monitoring (OPD coverage for ongoing parameters)
- Venue interpretation: venue indicates where monitoring is ordered/initiated, not necessarily performed

**Safety:**
- Glucose monitoring during steroids
- Respiratory monitoring thresholds for myelitis
- Drug-drug interactions
- Contraindication completeness
- Escalation criteria clarity

**Accuracy:**
- Drug dosing (especially weight-based)
- Monitoring frequencies
- Evidence levels cited correctly
- ICD-10 codes
- Priority levels appropriate for setting

**Completeness:**
- Missing differential diagnoses
- Incomplete disposition criteria
- Missing evidence references
- Gaps in monitoring parameters
- Missing Section 4 subsections (4A, 4B, 4C)

**Objectivity:**
- Brand name bias
- Unsupported treatment preferences
- Missing alternative therapies

**Usability - Directive Language:**
Flag any recommendations that use weak/suggestive language:
- "Consider..." Ã¢â€ â€™ Rewrite as direct order
- "May benefit from..." Ã¢â€ â€™ Rewrite as direct order
- "Should be encouraged to..." Ã¢â€ â€™ Rewrite as direct instruction

## Setting Coverage Scoring Impact

| Issue | Scoring Impact |
|-------|----------------|
| One setting missing entirely from a section | Setting Appropriateness: -2 points |
| Multiple settings missing coverage | Setting Appropriateness: -3 to -4 points |
| Inappropriate use of "-" (should have coverage) | Setting Appropriateness: -1 point per instance |
| OPD completely missing from Labs | Completeness: -2 points; Setting: -2 points |
| Priorities incorrect for setting (e.g., STAT in OPD) | Accuracy: -1 point per instance |

## Scoring Guidelines

- **9-10:** Excellent, minimal or no changes needed
- **7-8:** Good, minor revisions only
- **5-6:** Acceptable, moderate revisions needed
- **3-4:** Significant issues, major revision required
- **0-2:** Unsafe or fundamentally flawed, rebuild required

**Overall thresholds:**
- Ã¢â€°Â¥54/60 (90%): Ready for clinical use pending physician sign-off
- 48-53/60 (80-89%): Revise and re-check
- <48/60 (<80%): Significant revision needed

## Change Log

**v2.2 (January 14, 2026)**
- Added Section 6 Monitoring Assessment table to output format
- Added venue column validation for Section 6 (ED, HOSP, OPD, ICU required)
- Added Section 6 Monitoring to Common Issues to Check
- Added critical safety monitoring validation (respiratory function for neuromuscular conditions)
- Section 6 venue interpretation: where monitoring is ordered/initiated, not necessarily performed

**v2.1 (January 13, 2026)**
- Added Medication Assessment table to output format
- Added M-codes for medication issues (M1, M2, M3, etc.)
- Added Medication Comprehensiveness checks to Common Issues section
- Updated Completeness domain with medication coverage checklist
- Checks for: individual drug rows, complete dosing, symptomatic categories, DMT columns

**v2.0 (January 13, 2026)**
- Added Setting Coverage Assessment table to output format
- Added Setting Coverage Issues section (S1, S2, etc.)
- Added comprehensive setting coverage validation checklist
- Added common coverage gaps to flag
- Added guidance on appropriate vs inappropriate "-" usage
- Added setting coverage scoring impact
- Updated all six domain descriptions for multi-column format
- Added format validation for Option A structure

**v1.0 (January 13, 2026)**
- Initial version
