---
name: neuro-builder
description: Generates structured, evidence-based clinical decision support recommendations for neurological diagnoses. Use when creating clinical workup plans, treatment protocols, or diagnostic recommendations for neurologists. Triggers on requests for clinical recommendations, diagnostic workups, treatment plans for neurological conditions, or references to teleneurohospitalist content.
---

# Neuro Clinical Recommendation Builder

Generate comprehensive, structured clinical decision support content for neurological diagnoses across care settings (ED, Hospital, ICU, Outpatient, Rehab).

## Diagnosis Scoping Rules

Identify the clinical scenario from the diagnosis modifier:

| Modifier | Interpretation |
|----------|----------------|
| "[Condition] - Exacerbation" or "Acute [Condition]" | Focus on acute management; maintenance therapy mentioned but not detailed |
| "[Condition] - New Diagnosis" | Include full workup, differential, AND long-term treatment options |
| "[Condition] - Chronic/Maintenance" | Focus on long-term management, monitoring, lifestyle |
| "[Condition] - Refractory" | Include second-line and rare therapies prominently |

If modifier is ambiguous, generate for the most common clinical scenario AND note what would differ for other scenarios.

## CRITICAL: Comprehensive Setting Coverage

**Every recommendation must be evaluated for ALL applicable settings.** Patients with the same diagnosis may present to ED, hospital, outpatient clinic, or ICU. The plan must be complete and actionable regardless of where the patient is seen.

**For each test, study, or treatment, ask:**
1. Is this applicable in the ED? What priority?
2. Is this applicable on the hospital floor? What priority?
3. Is this applicable in outpatient clinic? What priority?
4. Is this applicable in ICU? What priority?

**Use "-" only when truly not applicable** (e.g., prolactin level only useful if drawn within 20 minutes of seizure Ã¢â€ â€™ "-" for OPD). Do NOT use "-" for "less common" or "usually done elsewhere."

**Common gaps to avoid:**
- Labs missing OPD tags (outpatient neurologists need to order workups too)
- Imaging missing OPD tags (MRI often ordered from clinic)
- Treatments missing HOSP tags (maintenance meds continue inpatient)
- Referrals missing ED tags (some consults start in ED)

## Output Structure

Generate output using this exact structure. **Sections 1-4 are primary action items; Sections 5-8 are reference/supporting information** (may be collapsed by default in clinical tools).

```
DIAGNOSIS: [Name]
ICD-10: [Code(s)]
SCOPE: [Brief statement of what this template covers and excludes]

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â
SECTION A: ACTION ITEMS
Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|

## 3. TREATMENT

**CRITICAL: Each medication must be on its own row with complete prescribing information. Do NOT group drugs together.**

**CRITICAL: NO CROSS-REFERENCES. Each row must be completely self-contained.**
- ❌ NEVER use "Same as [drug]", "See above", "Similar to [drug]", "As above"
- ✅ ALWAYS repeat the full content even if it's identical to another row
- **Why:** Users scan individual rows quickly. Cross-references force searching, slowing clinical workflow.

**Example - WRONG:**
```
| Nortriptyline | Same as amitriptyline | Same |
```

**Example - CORRECT:**
```
| Nortriptyline | Cardiac conduction abnormality; recent MI; urinary retention; glaucoma; elderly | ECG if dose >100 mg/day; anticholinergic effects |
```

**IMPORTANT:** All treatment tables use STANDARDIZED columns with **Route** and **Indication** for every medication. This enables:
- Order sentence generation (e.g., "Baclofen 5 mg PO TID")
- Teal pill icon (💊) on hover showing why this treatment is recommended
- Consistent parsing for the clinical tool

### Standard Treatment Table Format (ALL Sections)

```
| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
```

**Column Definitions:**
- **Treatment:** Drug name (generic preferred; include brand if commonly used)
- **Route:** PO, IV, IM, SC, PR, SL, INH, TOP, IT (intrathecal), or combination
- **Indication:** Why this drug is used for this condition (displays as 💊 icon)
- **Dosing:** Structured format (see Dosing Requirements below)
- **Contraindications:** Safety warnings (displays as ⚠️ icon)
- **Monitoring:** Required labs, vitals, or clinical monitoring (displays as 📊 icon)
- **ED/HOSP/OPD/ICU:** Priority in each setting (STAT, URGENT, ROUTINE, EXT, -)

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

### 3D. Disease-Modifying or Chronic Therapies (if applicable)

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|

## Treatment Section Guidance

### CRITICAL: Individual Drug Rows

**Every medication must be listed on its own row.** Do NOT group drugs together (e.g., "SSRIs" or "beta-blockers"). Each drug needs complete prescribing information with the standardized column format including Route.

Ã¢ÂÅ’ **Wrong:**
```
| SSRIs | Depression | Per drug | Various | Monitor mood | — | ROUTINE | ROUTINE | — |
```

Ã¢Å“â€¦ **Correct:**
```
| Sertraline | Depression | Start 50 mg daily; increase by 25-50 mg q1-2wk; max 200 mg | Concurrent MAOIs | Suicidality monitoring | — | ROUTINE | ROUTINE | — |
| Escitalopram | Depression | Start 10 mg daily; max 20 mg | Concurrent MAOIs; QT prolongation | QTc if risk factors | — | ROUTINE | ROUTINE | — |
```

### Dosing Requirements

**STRUCTURED DOSING FORMAT:** Use double-colon delimited fields to enable order sentence generation:

**Single Dose Format:**
```
[dose] [frequency] :: [route] :: :: [full_instructions]
```

**Multiple Dose Format (semicolon-separated options):**
```
[dose1 freq1]; [dose2 freq2]; [dose3 freq3] :: [route] :: :: [full_instructions]
```

**Note:** We use `::` instead of `|` because `|` conflicts with markdown table syntax.

**Single Dose Examples:**
```
5 mg TID :: PO :: :: Start 5 mg TID; titrate by 5 mg/dose q3d; max 80 mg/day
1000 mg daily x 5 days :: IV :: :: 1000 mg IV daily for 3-5 days; infuse over 1 hour
4 mg push PRN seizure :: IV :: :: 4 mg IV push over 2 min; may repeat x1 in 5 min; max 8 mg
```

**Multiple Dose Examples (PREFERRED for medications with standard titration):**
```
300 mg qHS; 300 mg TID; 600 mg TID; 900 mg TID :: PO :: :: Start 300 mg qHS; titrate by 300 mg q1-3d; max 3600 mg/day
75 mg BID; 150 mg BID; 300 mg BID :: PO :: :: Start 75 mg BID; may increase q1wk; max 600 mg/day
25 mg qHS; 50 mg qHS; 75 mg qHS :: PO :: :: Start 25 mg qHS; titrate q1wk; max 150 mg qHS
```

Each semicolon-separated option becomes a selectable order sentence in the clinical tool.

**Field Definitions:**
| Field | Purpose | Examples |
|-------|---------|----------|
| dose_options | One or more dose+frequency pairs | "5 mg TID" or "300 mg qHS; 300 mg TID; 600 mg TID" |
| route | Administration route | "PO", "IV", "IM", "SC", "SL", "PR", "INH", "TOP" |
| (empty) | Reserved field, leave empty | :: |
| full_instructions | Complete dosing guidance | Include start dose, titration, max dose, special instructions |

**Order Sentence Generation:**
The clinical tool generates clickable order sentences from dose options:
- Single: `5 mg TID :: PO :: :: ...` → "Baclofen 5 mg PO TID"
- Multiple: `300 mg qHS; 300 mg TID :: PO :: :: ...` → Dropdown with:
  - "Gabapentin 300 mg PO qHS"
  - "Gabapentin 300 mg PO TID"

**Full Instructions Must Include:**
| Element | Example |
|---------|---------|
| Starting dose | "Start 5 mg TID" or "Start 300 mg qHS" |
| Titration schedule | "titrate by 5 mg/dose q3d" or "increase by 300 mg q1-3d" |
| Target dose (if applicable) | "target 900-1800 mg TID" |
| Maximum dose | "max 80 mg/day" or "max 3600 mg/day" |
| Special instructions | "take with food", "avoid afternoon dosing", "exactly 12 hours apart" |

**PRN Medications:**
Include PRN indication with each dose option:
```
4 mg IV push PRN seizure; 2 mg IV push PRN seizure :: IV :: :: 4 mg IV push; may repeat x1 in 5 min; max 8 mg
10 mg q6h PRN; 20 mg q6h PRN :: PO :: :: 10-20 mg PO q6h as needed for pain; max 80 mg/day
```

**Loading + Maintenance Doses:**
Use separate dose options for load and maintenance:
```
1000 mg IV load; 500 mg IV q12h :: IV :: :: Load 1000 mg IV, then 500 mg IV q12h; adjust for renal function
20 mg/kg IV load; 5 mg/kg IV q12h :: IV :: :: 20 mg/kg IV load (max 1500 mg), then 5 mg/kg IV q12h
```

**Weight-Based Dosing:**
Include mg/kg with calculated examples:
```
0.15 mg/kg IV push; 0.1 mg/kg IV push :: IV :: :: 0.1-0.15 mg/kg IV (max 10 mg); repeat q5min PRN
4 mg IV; 0.1 mg/kg IV :: IV :: :: 4 mg or 0.1 mg/kg IV push; max 10 mg; for patients >40 kg use fixed dose
```

### Symptomatic Treatment Categories

For chronic neurological conditions, consider including treatments for these symptom categories where applicable:

| Category | Common in... | Example Drugs |
|----------|--------------|---------------|
| Spasticity | MS, stroke, SCI, TBI | Baclofen, tizanidine, dantrolene, botulinum toxin |
| Neuropathic pain | Neuropathy, MS, post-stroke | Gabapentin, pregabalin, duloxetine, amitriptyline, carbamazepine |
| Spasms/cramps | ALS, neuropathy | Baclofen, quinine (limited), mexiletine |
| Bladder urgency | MS, Parkinson, stroke | Oxybutynin, solifenacin, mirabegron |
| Urinary retention | MS, autonomic neuropathy | Tamsulosin, bethanechol |
| Constipation | Parkinson, neuropathy, opioid use | PEG 3350, senna, bisacodyl, lubiprostone |
| Fatigue | MS, myasthenia, post-stroke | Amantadine, modafinil, methylphenidate |
| Depression | Any chronic neuro condition | Sertraline, escitalopram, bupropion, venlafaxine |
| Anxiety | Any chronic neuro condition | SSRIs, buspirone, hydroxyzine |
| Insomnia | Parkinson, dementia, chronic pain | Trazodone, melatonin, mirtazapine |
| Tremor | MS, essential tremor, Parkinson | Propranolol, primidone, clonazepam (not for Parkinson resting tremor) |
| Sialorrhea | ALS, Parkinson | Glycopyrrolate, atropine drops, botulinum toxin |
| Pseudobulbar affect | ALS, MS, stroke, TBI | Dextromethorphan-quinidine |
| Cognitive impairment | Dementia, MS | Donepezil, memantine, rivastigmine |
| Orthostatic hypotension | Autonomic neuropathy, Parkinson | Midodrine, fludrocortisone, droxidopa |

### Disease-Modifying Therapy (DMT) Section

Use Section 3D with expanded columns when the diagnosis has chronic disease-modifying treatments:

**Applies to:** MS, myasthenia gravis, CIDP, neuromyelitis optica, autoimmune encephalitis, etc.

**Additional columns for DMTs:**
- **Route:** PO, SC, IM, IV, other
- **Pre-Treatment Requirements:** Labs, imaging, vaccinations, genetic testing, specialist clearances

**Each DMT row must include:**
- Specific brand and generic name
- Exact dosing with titration schedule (if any)
- Complete pre-treatment workup
- All contraindications
- Monitoring schedule with frequencies (e.g., "JCV antibody q6mo", "CBC monthly Ãƒâ€” 48 months")
- REMS program requirements where applicable

### Setting-Specific Treatment Notes

| Setting | Treatment Considerations |
|---------|-------------------------|
| **ED** | Acute treatments only; avoid initiating chronic therapies; can continue home meds |
| **HOSP** | Continue home meds; can initiate symptomatic treatments; DMTs typically NOT started inpatient |
| **OPD** | Primary setting for DMT initiation; chronic disease management; titration of symptomatic meds |
| **ICU** | Critical care interventions; may need to hold certain home meds; avoid drugs that worsen hemodynamics |

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | Indication | ED | HOSP | OPD | ICU |
|----------------|------------|:--:|:----:|:---:|:---:|

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|

Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â
SECTION B: REFERENCE (Expand as Needed)
Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|

## 6. MONITORING PARAMETERS

*Venue columns indicate where monitoring is typically ordered/initiated. Most monitoring continues in outpatient setting.*

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | [criteria] |
| Admit to floor | [criteria] |
| Admit to ICU | [criteria] |
| Transfer to higher level | [criteria] |

## 8. EVIDENCE & REFERENCES

**CRITICAL: All citations must include clickable PubMed links where available.** Use markdown format: `[Author et al. Journal Year](https://pubmed.ncbi.nlm.nih.gov/PMID/)`

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|

---

## CHANGE LOG

**v1.0 (Date)**
- Initial template creation

---

## APPENDIX A: [Title] (if needed)

[Appendix content - algorithms, dosing tables, quick reference cards, etc.]

## APPENDIX B: [Title] (if needed)

[Additional appendix content]
```

## Setting Definitions

| Setting | Definition | Typical Priorities |
|---------|------------|-------------------|
| **ED** | Emergency Department - acute presentation, limited time | STAT, URGENT |
| **HOSP** | Inpatient floor - admitted, can wait hours | STAT, URGENT, ROUTINE |
| **OPD** | Outpatient clinic - scheduled visit, days-weeks available | ROUTINE, EXT |
| **ICU** | Intensive Care Unit - critically ill, continuous monitoring | STAT, URGENT |

## Priority Definitions

| Priority | Timeframe | Use When |
|----------|-----------|----------|
| **STAT** | Immediate (minutes) | Life-threatening, time-sensitive |
| **URGENT** | Within hours | Important but not immediately life-threatening |
| **ROUTINE** | Standard timing (days) | Important but not time-sensitive |
| **EXT** | Extended workup | Atypical cases, refractory, specialized |
| **-** | Not applicable | Truly not relevant to this setting |

## Writing Style: Directive Language

All recommendations must be written as **checkbox-ready directives** - clear orders from one physician to another or to the patient. These will be selected and sent directly in clinical communications.

**DO NOT write:**
- "Consider physical therapy for balance issues"
- "Patient may benefit from neurology follow-up"
- "Smoking cessation should be encouraged"

**DO write:**
- "Physical therapy consult for gait and balance training"
- "Neurology follow-up in 2-4 weeks"
- "Smoking cessation"
- "Avoid driving until cleared by neurology"
- "Vitamin D 2000 IU daily"
- "MRI brain with and without contrast"

**Formatting rules:**
- Start with the action or service, not the rationale
- Use imperative verb forms or noun phrases
- Keep recommendations concise (aim for <10 words when possible)
- Rationale goes in the designated column, not the recommendation itself

## Section 4 Guidance: Diagnosis-Specific Content Required

**CRITICAL:** Section 4 content must be customized to the specific diagnosis. Do not copy generic content between templates. Each neurological condition has unique referral needs, patient education requirements, and lifestyle factors.

### 4A. Referrals & Consults

Include diagnosis-appropriate referrals. Common categories:

| Category | Examples |
|----------|----------|
| Rehabilitation | PT (gait, balance, strengthening), OT (ADLs, hand function), Speech (swallow, cognition, communication) |
| Subspecialty | Neuromuscular, neuro-ophthalmology, epilepsy, movement disorders, neuro-oncology |
| Medical specialties | Hematology/oncology, rheumatology, endocrinology, cardiology, pulmonology |
| Supportive | Pain management, psychiatry/psychology, social work, palliative care, genetic counseling |
| Primary care | PCP follow-up, podiatry, wound care, nutrition |

### 4B. Patient Instructions

Include actionable, diagnosis-specific instructions:

| Category | Content Type |
|----------|--------------|
| Return precautions | Specific symptoms requiring ED return |
| Activity guidance | Driving, work, exercise restrictions |
| Medication guidance | Titration expectations, what not to stop abruptly, timing |
| Self-monitoring | What to watch for, symptom diaries, when to call |
| Safety | Fall prevention, seizure precautions, heat/cold exposure |

### 4C. Lifestyle Modifications

Include modifiable risk factors and preventive measures specific to the condition:

| Category | Examples |
|----------|----------|
| Substance use | Alcohol cessation, smoking cessation |
| Metabolic | Glycemic control, blood pressure targets, lipid management |
| Activity | Exercise type and intensity, activity pacing |
| Diet/supplements | Specific vitamins, dietary modifications |
| Environmental | Heat avoidance, pressure point protection, home safety |
| Sleep | Sleep hygiene, CPAP compliance |

## Builder Principles

1. **Ensure comprehensive setting coverage** - every applicable setting must be tagged
2. **List each medication individually** - never group drugs; each drug gets its own row with complete dosing
3. **Include complete prescribing information** - starting dose, titration, max dose, contraindications, monitoring
4. Include evidence grading where available (Class I-III, Level A-C)
5. Note contraindications and monitoring requirements for all treatments
6. Be specific with dosing when standard protocols exist
7. Include red flags and escalation triggers
8. Acknowledge limitations of evidence where relevant
9. Maintain objectivity - no promotional language
10. Write all recommendations as directives, not suggestions
11. Include relevant referrals (PT, OT, Speech, subspecialty consults) and patient instructions
12. **Validate coverage:** Before finalizing, confirm each section has appropriate entries for ED, HOSP, OPD, and ICU where applicable
13. **Cover symptomatic treatments comprehensively** - include all symptom categories relevant to the diagnosis (pain, spasticity, bladder, mood, etc.)
14. **Include clickable citation links** - All references in Section 8 must include PubMed links where available (see Citation Link Requirements below)
15. **CRITICAL: Maintain JSON parity** - The `plans.json` file must contain ALL content from the markdown template. The Clinical Plan Builder reads from JSON only. See "JSON Parity Requirement" section below.

## Setting Coverage Checklist (Validate Before Output)

Before delivering the recommendation, verify:

**Labs:**
- [ ] Can this patient present to outpatient clinic? Ã¢â€ â€™ OPD labs included?
- [ ] Can this patient be admitted? Ã¢â€ â€™ HOSP labs appropriate?
- [ ] Can this be an emergency? Ã¢â€ â€™ ED labs with STAT priorities?

**Imaging:**
- [ ] Is outpatient imaging an option? Ã¢â€ â€™ OPD column populated?
- [ ] Urgent inpatient imaging needed? Ã¢â€ â€™ HOSP column populated?

**Treatments:**
- [ ] Maintenance meds applicable in hospital? Ã¢â€ â€™ HOSP column populated?
- [ ] Acute treatments applicable in ED? Ã¢â€ â€™ ED column with STAT/URGENT?

**Referrals:**
- [ ] Can consults be initiated from ED? Ã¢â€ â€™ ED column where appropriate?
- [ ] Outpatient follow-up referrals? Ã¢â€ â€™ OPD column populated?

**Monitoring (Section 6):**
- [ ] Venue columns included for all monitoring parameters?
- [ ] Critical safety monitoring (respiratory, cardiac) has ED/ICU coverage?
- [ ] Longitudinal monitoring has OPD coverage?

## Section 6 Monitoring Parameters Guidance

Section 6 uses venue columns differently than action sections. For monitoring, the venue indicates **where monitoring is typically ordered or initiated**, not where it is performed longitudinally.

| Venue | Meaning for Monitoring |
|-------|----------------------|
| **ED** | Check this parameter in ED if patient presents acutely |
| **HOSP** | Order/initiate during hospitalization |
| **OPD** | Order/continue in outpatient follow-up |
| **ICU** | Critical monitoring in intensive care |

### Examples

| Parameter Type | Typical Venues | Rationale |
|---------------|----------------|-----------|
| HbA1c | HOSP, OPD | Longitudinal; not urgent |
| Pain scores | ED, HOSP, OPD, ICU | Assess everywhere |
| Creatinine clearance | ED, HOSP, OPD, ICU | Critical for medication dosing |
| ECG (if on QT-prolonging drug) | ED, HOSP, OPD, ICU | Safety everywhere |
| Respiratory function (NIF, FVC) | ED, HOSP, ICU | Critical for GBS/myasthenic crisis |
| Annual screening tests | OPD only | Longitudinal care |

### Critical Safety Monitoring

Always include venue-appropriate critical monitoring for conditions with acute decompensation risk:

| Condition | Critical Monitoring | Must Include |
|-----------|--------------------|--------------| 
| GBS, CIDP, MG | Respiratory function (FVC, NIF) | ED: STAT, HOSP: STAT, ICU: STAT |
| Seizure | Seizure recurrence, mental status | ED: STAT, HOSP: ROUTINE, ICU: STAT |
| Stroke | Neuro checks, BP | ED: STAT, HOSP: STAT, ICU: STAT |
| High-dose steroids | Glucose, BP, mood | ED: STAT, HOSP: ROUTINE, ICU: STAT |


## Citation Link Requirements

**All citations in Section 8 (Evidence & References) must include clickable links** to enable one-click access to source literature in the Clinical Plan Builder interface.

### Link Format

Use markdown hyperlink syntax in the Source column:
```
| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Benzodiazepines first-line | Class I, Level A | [Alldredge et al. NEJM 2001](https://pubmed.ncbi.nlm.nih.gov/11547716/) |
```

### Link Priority (prefer earlier options)

| Source Type | Preferred Link | Example |
|-------------|----------------|---------|
| Journal articles | PubMed (PMID) | `https://pubmed.ncbi.nlm.nih.gov/12345678/` |
| Guidelines | Organization website or PubMed | `https://www.aan.com/Guidelines/...` |
| Clinical trials | ClinicalTrials.gov or PubMed | `https://clinicaltrials.gov/study/NCT01234567` |
| FDA labeling | DailyMed | `https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=...` |
| Consensus statements | PubMed or organization | Direct link to abstract |

### Multiple Sources

For rows with multiple sources, link each individually:
```
| Benzodiazepines first-line | Class I, Level A | [NCS 2012](https://pubmed.ncbi.nlm.nih.gov/22528274/); [AES 2016](https://pubmed.ncbi.nlm.nih.gov/26900382/) |
```

### When Links Are Not Available

- Expert consensus: No link needed, state "Expert consensus"
- Emerging evidence/case series: Link if PubMed indexed, otherwise state "Emerging evidence; case series"
- Textbooks: Link to publisher page if available online

### Verification

Run the **neuro-citation-verifier** skill after building to:
1. Verify all citations exist and are accurate
2. Add any missing PubMed links
3. Correct any hallucinated or inaccurate citations

## Appendices

When additional reference material, algorithms, or protocols are needed, place them at the **bottom of the document** after Section 8 (Evidence & References) and the Change Log.

```
## APPENDIX A: [Title]
[Content]

## APPENDIX B: [Title]
[Content]
```

**Appendix Placement Rules:**
- Appendices always go AFTER the main 8 sections and Change Log
- Use lettered appendices (A, B, C) in order of importance or logical flow
- Common appendix types:
  - Treatment algorithms/flowcharts
  - Dosing tables
  - Immunotherapy timelines
  - Quick reference cards for specific scenarios
- If an appendix is critical for acute situations (e.g., rapid protocol for non-specialists), include a prominent link/reference to it from the relevant treatment section

## Post-Pipeline Auto-Push Workflow

After completing the full skill pipeline (Builder → Checker → Rebuilder → Citation Verifier → ICD/Synonym Enricher), automatically push the draft to GitHub for review.

### Auto-Push Steps

1. **Verify draft is in correct location:**
   ```
   /docs/drafts/[condition-name].md
   ```

2. **Ensure draft has correct frontmatter:**
   ```yaml
   ---
   title: [Condition Name]
   description: [Brief description]
   version: "1.0"
   setting: [ED, HOSP, OPD, ICU as applicable]
   status: draft
   tags:
     - [relevant tags]
   ---
   ```

3. **Add draft warning banner after frontmatter:**
   ```markdown
   <div class="draft-warning-banner">
     <div class="icon">⚠️</div>
     <div class="content">
       <div class="title">DRAFT - Pending Review</div>
       <div class="description">This plan requires physician review before clinical use.</div>
     </div>
   </div>
   ```

4. **Update `/docs/drafts/index.md`** to add the new draft to the table

5. **Update `mkdocs.yml`** to add the draft to navigation under "Drafts for Review"

6. **Commit and push:**
   ```bash
   git add docs/drafts/[condition-name].md docs/drafts/index.md mkdocs.yml
   git commit -m "Add draft: [Condition Name] for review

   Pipeline completed: Builder → Checker → Rebuilder → Citation Verifier → ICD/Synonym Enricher
   Ready for physician review at [site-url]/drafts/[condition-name]/

   Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
   git push
   ```

7. **Notify user:**
   ```
   ✅ Draft published for review!

   View at: https://blondarb.github.io/neuro-plans/drafts/[condition-name]/

   When ready to approve, say: "Approve [Condition Name] and move to approved"
   ```

### Approval Workflow

When user approves a draft:

1. **Move file** from `/docs/drafts/` to `/docs/plans/`
2. **Update frontmatter** status from `draft` to `approved`
3. **Replace draft banner** with approved banner
4. **Update `/docs/drafts/index.md`** to remove from pending
5. **Update `/docs/plans/index.md`** to add to approved table
6. **Update `mkdocs.yml`** navigation
7. **Commit and push** with approval message
8. **Confirm to user** with link to approved plan

## Reference Examples

See `references/ms-exacerbation-v2.md` for a complete example of Builder output that has been validated through the Checker/Rebuilder workflow.

## Lumbar Puncture Guidance

**IMPORTANT:** Lumbar Puncture appears under **Laboratory Workup** in the clinical tool (CSF analysis IS laboratory work). This ensures LP studies display alongside other lab sections when selected by the clinician.

In the markdown file, place `### LUMBAR PUNCTURE` after the imaging subsections (2A/2B/2C). The JSON generator will automatically position it under "Laboratory Workup > Lumbar Puncture" in the clinical tool output.

Use this structure (note: venue columns ED/HOSP/OPD/ICU must be the last 4 columns):

```
### LUMBAR PUNCTURE

**Indication:** [Why LP is being done]
**Timing:** [Urgent vs routine, any prerequisites]
**Volume Required:** [Standard 10-15cc OR therapeutic 30-50cc for NPH]

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | [Why ordered] | 10-20 cm H2O | URGENT | ROUTINE | ROUTINE | - |
| Cell count (tubes 1 and 4) | [Why ordered] | WBC <5, RBC 0 | URGENT | ROUTINE | ROUTINE | - |
| Protein | [Why ordered] | Normal 15-45 mg/dL | URGENT | ROUTINE | ROUTINE | - |
| Glucose with serum glucose | [Why ordered] | Normal (>60% serum) | URGENT | ROUTINE | ROUTINE | - |
| Gram stain and culture | [Why ordered] | No organisms | URGENT | ROUTINE | ROUTINE | - |
| [Diagnosis-specific study] | [Rationale] | [Target] | [Priority] | [Priority] | [Priority] | [Priority] |

**Special Handling:** [Time-sensitive, temperature requirements]
**Contraindications:** [List contraindications]
```

See `references/lp-reference.md` for comprehensive LP panels organized by diagnosis, including:
- Core studies (always order)
- Diagnosis-specific panels (MS, meningitis, GBS, SAH, malignancy, autoimmune)
- Advanced molecular testing (BioFire ME Panel, mNGS/Delve Detect, CSF cfDNA for tumors)
- Therapeutic LP protocols (NPH, IIH)

## Clinical Tool JSON Schema

When converting plans to JSON format for the Clinical Plan Builder web interface, use this schema to ensure all metadata displays correctly with icons.

### Plan-Level Fields

```json
{
  "id": "condition-name",
  "title": "Condition Name",
  "version": "1.0",
  "notes": "Important clinical notes displayed in collapsible banner at top",
  "sections": [...]
}
```

### Section Structure

```json
{
  "title": "Section Title",
  "items": [...]
}
```

### Item Fields (Icons & Display)

Each item can include these fields. The Clinical Tool displays icons only for fields that exist:

| Field | Type | Icon | Color | Description |
|-------|------|------|-------|-------------|
| `item` | string | - | - | **Required.** The item name (test, drug, study, etc.) |
| `ED` | string | - | - | Priority for Emergency Department (STAT, URGENT, ROUTINE, EXT, -) |
| `HOSP` | string | - | - | Priority for Hospital/Inpatient |
| `OPD` | string | - | - | Priority for Outpatient |
| `ICU` | string | - | - | Priority for Intensive Care Unit |
| `dosing` | string | Badge | Blue | Medication dosing (displayed as badge AND in selected items sidebar) |
| `rationale` | string | ℹ️ | Blue | Clinical rationale or evidence basis |
| `timing` | string | ⏱ | Amber | When to perform/administer |
| `target` | string | 🎯 | Green | Target finding or expected result |
| `contraindications` | string | ⚠️ | Red (pulsing) | Safety warnings - CRITICAL for patient safety |
| `monitoring` | string | 📊 | Purple | Required monitoring parameters |

### Icon Display Behavior

- Icons only appear if the field has a value in JSON
- Hovering over an icon reveals a tooltip with the full text
- The contraindication icon (⚠️) pulses to draw attention to safety-critical information
- Multiple icons can appear for a single item

### Example Item with Full Metadata

```json
{
  "item": "Lorazepam IV",
  "ED": "STAT",
  "HOSP": "STAT",
  "OPD": "-",
  "ICU": "STAT",
  "dosing": "4 mg IV push over 2 min; may repeat x1 in 5 min; max 8 mg total",
  "rationale": "First-line if IV access available; Class I evidence from ESETT trial",
  "timing": "Administer within 5 min of seizure onset for best efficacy",
  "target": "Cessation of clinical and electrographic seizure activity",
  "contraindications": "Acute narrow-angle glaucoma; severe respiratory depression without ventilator support",
  "monitoring": "Respiratory status, BP, sedation level; have airway equipment ready"
}
```

### Example Item with Partial Metadata (Labs)

```json
{
  "item": "CBC with differential",
  "ED": "STAT",
  "HOSP": "STAT",
  "OPD": "ROUTINE",
  "ICU": "STAT",
  "rationale": "Assess for infection, anemia, thrombocytopenia"
}
```

### Safety-Critical Fields

**IMPORTANT:** For medications, always include these fields when applicable:

1. **`contraindications`** - Include ALL major contraindications, especially:
   - Pregnancy warnings (teratogenic drugs)
   - Organ dysfunction (hepatic, renal)
   - Drug interactions
   - Black box warnings

2. **`monitoring`** - Include for drugs requiring:
   - Lab monitoring (drug levels, organ function)
   - Vital sign monitoring
   - Syndrome surveillance (e.g., PROPOFOL INFUSION SYNDROME)

### Ensuring Icon Display

To ensure icons appear in the Clinical Tool:

1. **Include the field in JSON** - Icons only show if the field exists with a value
2. **Use descriptive text** - The tooltip shows the full text
3. **Highlight safety concerns** - Use ALL CAPS for critical warnings in contraindications/monitoring
4. **Be concise but complete** - Tooltips work best with 1-3 sentences

## JSON Parity Requirement

**CRITICAL: The JSON file (`docs/data/plans.json`) must contain ALL content from the markdown template.** The Clinical Plan Builder reads exclusively from `plans.json`, NOT from markdown files. Any content missing from JSON will not appear in the web interface.

### JSON Generation Checklist

After creating or updating a markdown template, verify the corresponding JSON entry includes:

**Section 1 - Laboratory Workup:**
- [ ] 1A: Essential/Core Labs
- [ ] 1B: Extended Workup (Second-line)
- [ ] 1C: Rare/Specialized (Refractory or Atypical)

**Section 2 - Diagnostic Imaging & Studies:**
- [ ] 2A: Essential/First-line
- [ ] 2B: Extended
- [ ] 2C: Rare/Specialized
- [ ] Lumbar Puncture subsection (if applicable)

**Section 3 - Treatment:**
- [ ] 3A: Acute/Emergent
- [ ] 3B: Symptomatic Treatments
- [ ] 3C: Second-line/Refractory
- [ ] 3D: Disease-Modifying (if applicable)
- [ ] 3E: Super-Refractory options (if applicable)
- [ ] 3F: Immunotherapy options (if applicable, e.g., NORSE/FIRES)
- [ ] 3G: Symptomatic/Supportive ICU Care (if applicable)

**Section 4 - Other Recommendations:**
- [ ] 4A: Referrals & Consults
- [ ] 4B: Patient Instructions
- [ ] 4C: Lifestyle & Prevention

**Section 5 - Differential Diagnosis:**
- [ ] All differential diagnoses with distinguishing features

**Section 6 - Monitoring Parameters:**
- [ ] Continuous monitoring items (EEG, telemetry, etc.)
- [ ] Intermittent monitoring items (labs, exams, etc.)

**Section 7 - Disposition Criteria:**
- [ ] ICU admission criteria
- [ ] Floor admission criteria
- [ ] Discharge criteria
- [ ] Transfer criteria

**Section 8 - Evidence & References:**
- [ ] All citations with PubMed links (handled separately via citations section in JSON)

### JSON Field Completeness

For each item in JSON, include ALL applicable metadata fields:
- `item`: Name (required)
- `ED`, `HOSP`, `OPD`, `ICU`: Priority flags
- `dosing`: For medications
- `rationale`: Clinical reasoning
- `timing`: When to perform
- `target`: Expected findings
- `contraindications`: Safety warnings
- `monitoring`: Required monitoring

### Validation Step

**Before considering a plan complete:**
1. Count total items in markdown template
2. Count total items in JSON entry
3. Verify counts match (or document why they differ)
4. Spot-check 3 random items from each section to confirm field completeness

### Common JSON Gaps to Avoid

| Gap | Impact | Prevention |
|-----|--------|------------|
| Missing subsections (1C, 2C, 3E-3G) | Advanced/rare options not visible | Follow section checklist |
| Missing monitoring section | Safety monitoring not displayed | Always include Section 6 |
| Missing disposition criteria | No admission/discharge guidance | Always include Section 7 |
| Incomplete item fields | Icons don't appear | Include all applicable metadata |
| Missing ICU-specific treatments | Incomplete critical care coverage | Review all 3E-3G subsections |

## Change Log

**v3.1 (January 24, 2026)** - Multiple Dose Options
- **Added multi-dose support**: Semicolon-separated dose options in structured dosing
- **New format**: `dose1 freq1; dose2 freq2; dose3 freq3 :: route :: :: full_instructions`
- Example: `300 mg qHS; 300 mg TID; 600 mg TID :: PO :: :: Start 300 mg qHS; titrate...`
- Each dose option generates a separate order sentence for dropdown selection
- Updated all dosing examples (PRN, loading/maintenance, weight-based)
- Clinical tool shows dropdown when multiple options available

**v3.0 (January 24, 2026)** - MAJOR: Clickable Medication Dosing
- **Standardized ALL treatment tables** to same column order: Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU
- **Added Route column to ALL sections** (3A, 3B, 3C) - previously only in 3D
- **Introduced structured dosing format**: `dose freq :: route :: :: full_instructions`
- This enables order sentence generation: clicking dosing badge copies "Baclofen 5 mg PO TID"
- Added detailed Dosing Requirements with examples for:
  - Standard dosing, PRN medications, loading + maintenance, weight-based dosing
- Updated examples throughout to use new format
- See docs/ROADMAP.md for full implementation plan

**v2.6 (January 19, 2026)**
- **Added JSON Parity Requirement section** - CRITICAL update requiring JSON to match markdown completely
- Added JSON Generation Checklist covering all 8 sections and subsections
- Added JSON Field Completeness requirements for item metadata
- Added Validation Step with item count verification
- Added Common JSON Gaps table to prevent missing content
- This addresses issue where Clinical Plan Builder showed incomplete content because JSON lacked parity with markdown

**v2.1 (January 13, 2026)**
- Added comprehensive Treatment Section Guidance
- Renamed Section 3B from "First-line Maintenance" to "Symptomatic Treatments" with Indication column
- Added requirement: each medication on individual row (no grouping)
- Added dosing requirements checklist (start, titrate, max, frequency)
- Added symptomatic treatment categories table with examples
- Added DMT section guidance with expanded columns (Route, Pre-Treatment Requirements)
- Added setting-specific treatment considerations
- Updated Section 3D template with Route and Pre-Treatment columns
- Updated Builder Principles (#2, #3, #13 for medication comprehensiveness)

**v2.0 (January 13, 2026)**
- Changed to Option A format: multi-column setting-priority matrix (ED | HOSP | OPD | ICU)
- Added comprehensive setting coverage requirements and validation checklist
- Added explicit instructions to avoid common coverage gaps
- Added setting and priority definition tables
- Reorganized for clarity and JSON conversion compatibility

**v1.0 (January 13, 2026)**
- Initial version

**v2.5 (January 19, 2026)**
- Added Clinical Tool JSON Schema section
- Documents all item fields that display as icons (rationale, timing, target, contraindications, monitoring)
- Includes icon colors, display behavior, and examples
- Safety-critical field guidance for medications

**v2.4 (January 19, 2026)**
- Added Post-Pipeline Auto-Push Workflow section
- Drafts automatically pushed to GitHub after pipeline completion
- Added Approval Workflow for moving drafts to approved status
- Includes frontmatter requirements, banner templates, and git commands

**v2.3 (January 19, 2026)**
- Added Appendices section with placement rules
- Appendices must go at BOTTOM of document, after Section 8 and Change Log
- Updated Output Structure to show Change Log and Appendix placement

**v2.2 (January 14, 2026)**
- Added venue columns (ED, HOSP, OPD, ICU) to Section 6 Monitoring Parameters template
- Added "Section 6 Monitoring Parameters Guidance" explaining venue interpretation for monitoring
- Added Monitoring checklist item to Setting Coverage Checklist
- Added Critical Safety Monitoring table for conditions with acute decompensation risk
- Venue for monitoring indicates where monitoring is ordered/initiated (not necessarily performed)
