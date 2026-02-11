---
title: "Acute Disseminated Encephalomyelitis (ADEM)"
description: "Clinical decision support for diagnosis and management of ADEM"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - demyelinating
  - autoimmune
  - encephalitis
  - pediatric
  - post-infectious
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Acute Disseminated Encephalomyelitis (ADEM)

**VERSION:** 1.0
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Draft

---

**DIAGNOSIS:** Acute Disseminated Encephalomyelitis (ADEM)

**ICD-10:** G04.81 (Other encephalitis and encephalomyelitis), G04.00 (Acute disseminated encephalitis and encephalomyelitis, unspecified)

**CPT CODES:** 85025 (CBC), 80053 (CMP), 86255 (MOG-IgG antibody), 86235 (ANA), 86021 (AQP4-IgG/NMO antibody), 89050 (CSF cell count), 89051 (CSF differential), 84157 (CSF protein), 84662 (CSF glucose), 86325 (CSF oligoclonal bands), 87070 (CSF culture), 87798 (CSF PCR panel), 70553 (MRI brain with/without contrast), 72156 (MRI cervical spine), 72158 (MRI thoracic spine), 95816 (EEG)

**SYNONYMS:** acute disseminated encephalomyelitis, ADEM, post-infectious encephalomyelitis, post-vaccination encephalomyelitis, para-infectious encephalomyelitis, perivenous encephalomyelitis, acute demyelinating encephalomyelitis, multiphasic disseminated encephalomyelitis, MDEM

**SCOPE:** Diagnosis and acute management of ADEM in children and adults. Covers IPMSSG diagnostic criteria, distinction from first MS attack, MOGAD-associated ADEM, CSF analysis, immunotherapy (high-dose steroids, IVIg, PLEX), and monitoring for recurrence. Includes multiphasic ADEM (MDEM) considerations. Excludes other causes of acute encephalitis unless as differential diagnosis.

---

**DEFINITIONS:**
- **ADEM:** Acute monophasic inflammatory demyelinating CNS event with encephalopathy (altered consciousness or behavioral change) and multifocal neurological deficits; preceded by infection or vaccination in most cases
- **Encephalopathy (required for ADEM diagnosis):** Altered consciousness ranging from lethargy to coma, OR behavioral change unexplained by fever/systemic illness/postictal state
- **Multiphasic ADEM (MDEM):** Second ADEM event ≥3 months after first, with new clinical and MRI findings not attributable to original event; if ≥2 relapses, consider MS or MOGAD
- **MOG-IgG associated ADEM:** ADEM with MOG-IgG antibodies; distinct from MS; higher relapse risk; better prognosis than AQP4-positive disease
- **IPMSSG criteria:** International Pediatric MS Study Group diagnostic criteria for ADEM (2013 revision)

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (All Patients)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Infection screen; leukocytosis; baseline before immunotherapy | Normal; mild leukocytosis may be present |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolytes, renal/hepatic function; metabolic encephalopathy exclusion | Normal |
| Blood cultures (x2) | STAT | STAT | - | STAT | Exclude bacteremia/sepsis before empiric steroids | No growth |
| ESR / CRP | STAT | STAT | ROUTINE | STAT | Inflammatory marker; may be elevated in ADEM | Variable; mild elevation expected |
| MOG-IgG antibody (cell-based assay) (CPT 86255) | URGENT | STAT | ROUTINE | STAT | MOG-associated ADEM; positive in 30-60% of ADEM cases (especially children); prognostic implications | Negative (positive = MOG-associated ADEM; better prognosis but relapse risk) |
| AQP4-IgG (NMO-IgG) antibody (CPT 86021) | URGENT | STAT | ROUTINE | STAT | Exclude NMOSD which may present like ADEM; treatment implications | Negative (positive = NMOSD, not ADEM) |
| Urinalysis | STAT | ROUTINE | - | STAT | Infection screen | Normal |

### 1B. Extended Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| ANA (CPT 86235) | - | ROUTINE | ROUTINE | - | Autoimmune disease screening (SLE cerebritis, neurosarcoidosis) | Negative |
| HIV antibody | - | ROUTINE | ROUTINE | - | HIV-associated CNS disease | Negative |
| Mycoplasma IgM/IgG | - | ROUTINE | ROUTINE | - | Mycoplasma pneumoniae-associated ADEM (common trigger) | Negative |
| EBV panel (VCA IgM, EBNA IgG) | - | ROUTINE | ROUTINE | - | EBV-triggered ADEM | Negative for acute infection |
| Respiratory viral panel | STAT | ROUTINE | - | STAT | Identify triggering infection | Identifies trigger but does not change ADEM management |
| ACE level | - | ROUTINE | ROUTINE | - | Neurosarcoidosis in differential | Normal |
| Quantitative immunoglobulins | - | ROUTINE | ROUTINE | - | IgA deficiency before IVIg; baseline immunoglobulin levels | Normal; check IgA |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum anti-NMDAR antibodies | - | ROUTINE | EXT | - | Anti-NMDA receptor encephalitis may mimic ADEM (especially with psychiatric symptoms and seizures) | Negative |
| Paraneoplastic antibody panel | - | - | EXT | - | Paraneoplastic encephalitis in adults; especially if atypical age or course | Negative |
| Mitochondrial DNA studies | - | - | EXT | - | Mitochondrial leukoencephalopathy (MELAS) if atypical presentation | No pathogenic variant |
| Biotinidase level | - | - | EXT | - | Biotinidase deficiency causing leukoencephalopathy (treatable) | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with/without contrast (CPT 70553) | STAT | STAT | ROUTINE | STAT | Immediate; critical for diagnosis | Large (>1-2 cm), poorly demarcated, bilateral, asymmetric white matter lesions; deep gray matter (thalami, basal ganglia) involvement common in ADEM; may enhance with contrast | MRI-incompatible devices |
| MRI total spine with/without contrast (CPT 72156, 72158) | URGENT | STAT | ROUTINE | URGENT | Within 24 hours; assess for concurrent myelitis | Large, longitudinally extensive, intramedullary T2 lesions (often ≥3 segments); may enhance | MRI-incompatible devices |
| CT head without contrast | STAT | - | - | STAT | Only if MRI not immediately available; exclude mass, hemorrhage, hydrocephalus | No acute hemorrhage or mass; may show subtle white matter hypodensity | None |

### 2B. Extended Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| EEG (CPT 95816) | - | ROUTINE | - | ROUTINE | If seizures suspected; encephalopathy assessment | Diffuse or focal slowing without epileptiform activity; epileptiform discharges if seizures | None |
| MRI brain follow-up (3-6 months) | - | - | ROUTINE | - | Document lesion resolution (ADEM lesions should partially or fully resolve); new lesions suggest MS or MOGAD relapse | Resolution or significant improvement of lesions; no new lesions | MRI-incompatible devices |
| Visual evoked potentials (VEP) | - | - | EXT | - | If optic neuritis component suspected | Normal or prolonged P100 latency | None |
| MR spectroscopy | - | EXT | EXT | - | Differentiate demyelination from tumor (choline/NAA ratios) | Elevated choline, reduced NAA in acute lesion; no mass-like spectral pattern | MRI-incompatible devices |

### LUMBAR PUNCTURE

**Indication:** All patients with suspected ADEM; essential to exclude CNS infection and support diagnosis
**Timing:** Urgent; before or shortly after starting empiric steroids (do not delay steroids for LP)
**Volume Required:** Standard 10-15 cc

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | Elevated ICP assessment | Normal (10-20 cm H2O); may be mildly elevated | URGENT | STAT | - | URGENT |
| Cell count with differential (tubes 1 and 4) | Infection vs inflammation; ADEM often has mild pleocytosis | Mild-moderate pleocytosis (typically <100 WBC, lymphocytic); high WBC or neutrophilic predominance suggests infection | URGENT | STAT | - | URGENT |
| Protein | Elevated in inflammatory/infectious conditions | Normal to mildly elevated (often 50-100 mg/dL in ADEM); markedly elevated suggests GBS or infection | URGENT | STAT | - | URGENT |
| Glucose with serum glucose | Low CSF glucose suggests bacterial/TB/fungal infection | Normal (>60% serum glucose) | URGENT | STAT | - | URGENT |
| Gram stain and bacterial culture | Exclude bacterial meningitis | No organisms; no growth | URGENT | STAT | - | URGENT |
| HSV PCR | Exclude HSV encephalitis (critical mimic) | Negative | URGENT | STAT | - | URGENT |
| CSF meningitis/encephalitis PCR panel (BioFire or equivalent) | Broad viral/bacterial screen; exclude treatable infections | Negative for all pathogens | URGENT | STAT | - | URGENT |
| Oligoclonal bands (CSF and serum) | Absent in most ADEM (present in MS); important for MS differentiation | Absent in ADEM (present in >90% of MS); if positive, raises concern for MS | - | ROUTINE | - | - |
| MOG-IgG (CSF) | MOG-associated ADEM; CSF MOG-IgG may be positive even if serum is negative | Negative (positive supports MOG-ADEM) | - | ROUTINE | - | - |
| Cytology | Exclude leptomeningeal malignancy/lymphoma | Negative for malignant cells | - | EXT | - | - |

**Special Handling:** CSF should be processed promptly; hold 2-3 mL frozen for additional studies if needed
**Contraindications:** Mass lesion with midline shift; coagulopathy (correct first); skin infection at puncture site

---

## 3. TREATMENT

### 3A. First-Line Immunotherapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IV Methylprednisolone | IV | First-line for ADEM; begin as soon as CNS infection reasonably excluded; do NOT delay for LP results if clinical suspicion high | 30 mg/kg/day (peds, max 1000 mg); 1000 mg daily (adults) x 3-5 days :: IV :: daily x 3-5 days :: Pediatric: 30 mg/kg/day (max 1000 mg) IV daily x 3-5 days; Adult: 1000 mg IV daily x 3-5 days; infuse over 1 hour | Active untreated bacterial/fungal infection; uncontrolled diabetes (relative) | Blood glucose Q6H; BP; mood/sleep; GI symptoms; electrolytes | STAT | STAT | - | STAT |
| Oral Prednisone taper | PO | Following IV methylprednisolone; prevents rebound | 1 mg/kg daily (max 60 mg); taper over 4-6 weeks :: PO :: daily with taper :: Start 1 mg/kg/day (max 60 mg) after IV pulse; taper by 5-10 mg q3-5d over 4-6 weeks; do NOT taper faster than 4 weeks (risk of relapse) | Active untreated infection | Blood glucose; BP; mood; weight; GI protection (PPI) | - | ROUTINE | ROUTINE | - |
| Acyclovir (empiric) | IV | Empiric coverage for HSV encephalitis until PCR results return; ADEM and HSV can present similarly | 10 mg/kg q8h :: IV :: q8h :: 10 mg/kg IV q8h; continue until HSV PCR confirmed negative (typically 48-72h); ensure adequate hydration | Hypersensitivity | Renal function (Cr); adequate hydration (prevent crystalluria); CBC | STAT | STAT | - | STAT |

### 3B. Second-Line Immunotherapy (Steroid-Refractory)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (Intravenous Immunoglobulin) | IV | Steroid-refractory ADEM (no improvement after 3-5 days of IV steroids); contraindication to steroids | 2 g/kg :: IV :: over 2-5 days :: 2 g/kg divided over 2-5 days (0.4 g/kg/day x 5 days); premedicate with acetaminophen and diphenhydramine | IgA deficiency with anti-IgA antibodies; recent thromboembolic event; uncompensated HF | Renal function; headache; infusion reactions; BP; HR; thrombotic events | - | URGENT | - | URGENT |
| Plasma Exchange (PLEX) | Apheresis | Steroid-refractory and IVIg-refractory ADEM; severe fulminant ADEM | 5-7 exchanges :: Apheresis :: every other day :: 5-7 exchanges over 10-14 days; 1-1.5 plasma volumes per session; albumin replacement | Hemodynamic instability; severe coagulopathy; poor vascular access | Coagulation studies; electrolytes (calcium, potassium); fibrinogen; BP; hemodynamic monitoring | - | URGENT | - | URGENT |

### 3C. Acute Seizure Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levetiracetam | IV/PO | Seizures in ADEM; preferred first-line due to fewer drug interactions | 20 mg/kg IV load; 500 mg BID; 1000 mg BID :: IV/PO :: BID :: Loading dose 20-30 mg/kg IV (max 3000 mg); then 500-1000 mg BID; adjust for renal function | Severe renal impairment (dose adjust) | Mood changes; sedation; renal function | STAT | STAT | ROUTINE | STAT |
| Lorazepam | IV | Acute seizure termination | 0.1 mg/kg IV (max 4 mg); 4 mg IV :: IV :: PRN :: 0.1 mg/kg IV (max 4 mg) over 2 min; may repeat x1 in 5 min | Severe respiratory depression without ventilator support | Respiratory status; sedation; BP | STAT | STAT | - | STAT |

### 3D. Symptomatic/Supportive

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Famotidine | IV/PO | GI prophylaxis during high-dose steroid therapy | 20 mg BID :: PO :: BID :: 20 mg PO BID during steroid therapy and taper | Severe renal impairment (dose adjust) | GI symptoms | - | ROUTINE | ROUTINE | - |
| Insulin sliding scale | SQ | Steroid-induced hyperglycemia | Per protocol :: SQ :: per protocol :: Monitor blood glucose Q6H during IV steroid pulse; sliding scale insulin per hospital protocol | Hypoglycemia | Blood glucose Q6H; transition to scheduled insulin if persistent hyperglycemia | - | ROUTINE | - | ROUTINE |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation for ADEM diagnosis confirmation, immunotherapy management, and MS/MOGAD/NMOSD differentiation | STAT | STAT | ROUTINE | STAT |
| Neuroradiology review of MRI for ADEM vs MS lesion pattern characterization | - | ROUTINE | ROUTINE | - |
| Infectious disease consultation if infection cannot be confidently excluded or if unusual pathogen suspected | URGENT | ROUTINE | - | URGENT |
| Physical therapy for motor recovery, gait training, and rehabilitation planning | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL assessment and adaptive strategies during recovery | - | ROUTINE | ROUTINE | - |
| Speech therapy for dysphagia assessment and communication if brainstem/cerebellar involvement | - | ROUTINE | - | ROUTINE |
| Neuropsychology follow-up for cognitive assessment (cognitive deficits may persist especially in children) | - | - | ROUTINE | - |
| Ophthalmology if optic neuritis component present for visual acuity monitoring | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| ADEM is usually a monophasic illness with good recovery expected over weeks to months; most patients recover fully or near-fully | - | ROUTINE | ROUTINE | - |
| Return immediately if new neurological symptoms develop (weakness, vision changes, confusion, seizures) after discharge, as this may indicate relapse or alternative diagnosis | STAT | - | ROUTINE | - |
| Complete the full oral steroid taper as prescribed; do NOT stop abruptly (risk of disease rebound and adrenal crisis) | - | ROUTINE | ROUTINE | - |
| Follow-up MRI at 3-6 months is essential to confirm lesion resolution and rule out MS (new lesions on follow-up MRI would suggest MS rather than ADEM) | - | - | ROUTINE | - |
| Report any new visual symptoms, limb weakness, numbness, or balance problems even after recovery, as these may indicate a second attack (MDEM or MS transition) | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Adequate rest during acute recovery; gradual return to school/work activities as neurological function improves | - | ROUTINE | ROUTINE | - |
| Vaccination review: ADEM can rarely be triggered by vaccines; this does NOT contraindicate future vaccination in most cases; discuss with neurologist and immunologist on case-by-case basis | - | - | ROUTINE | - |
| Seizure precautions if seizures occurred during acute phase; anticonvulsant taper guided by neurology (usually can be discontinued if EEG normalizes) | - | ROUTINE | ROUTINE | - |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| First attack of multiple sclerosis | No encephalopathy (key distinction); well-demarcated periventricular lesions; Dawson fingers; OCBs positive; lesions disseminated in time and space | MRI (periventricular, juxtacortical, Dawson fingers); CSF OCBs (positive in >90% MS); follow-up MRI showing new lesions at 3-6 months |
| MOGAD (MOG antibody disease) | Overlap with ADEM especially in children; MOG-IgG positive; may relapse (unlike monophasic ADEM); optic neuritis and myelitis common | MOG-IgG (cell-based assay); clinical course (relapses suggest MOGAD vs monophasic ADEM) |
| NMOSD (neuromyelitis optica spectrum disorder) | AQP4-IgG positive; area postrema syndrome; longitudinally extensive TM; optic neuritis; less commonly encephalopathy | AQP4-IgG antibody; MRI pattern (LETM, area postrema); clinical features |
| HSV encephalitis | Temporal lobe predilection; hemorrhagic lesions; rapid deterioration; CSF lymphocytic pleocytosis with RBCs | CSF HSV PCR (positive); MRI (temporal lobe T2 hyperintensity with hemorrhagic changes); EEG (PLEDs) |
| Autoimmune encephalitis (anti-NMDAR, anti-LGI1) | Psychiatric symptoms; seizures; movement disorder (faciobrachial dystonic seizures in LGI1); ovarian teratoma (NMDAR) | Autoimmune antibody panel (serum and CSF); MRI (may be normal or limbic involvement) |
| Acute viral encephalitis (non-HSV) | Direct viral invasion; more pronounced meningeal signs; CSF viral PCR positive; no demyelinating lesion pattern on MRI | CSF viral PCR panel; MRI pattern (cortical > white matter); clinical course |
| CNS vasculitis | Multifocal lesions but with vascular territory pattern; vessel wall enhancement on MRI; CSF pleocytosis | MR angiography; vessel wall MRI; conventional angiography; brain biopsy |
| CNS lymphoma | Periventricular enhancing mass(es); older adults; immunocompromised; homogeneous enhancement | MRI (homogeneous enhancement); CSF cytology and flow cytometry; brain biopsy |
| Acute hemorrhagic leukoencephalitis (AHLE/Weston Hurst) | Hyperacute fulminant variant of ADEM; hemorrhagic white matter necrosis; very high mortality | MRI (hemorrhagic component); brain biopsy (if diagnostic uncertainty); clinical course (fulminant) |
| Neurosarcoidosis | Leptomeningeal enhancement; cranial neuropathies; hilar lymphadenopathy; elevated ACE | ACE level; chest CT (hilar adenopathy); CSF (ACE, cell count); brain biopsy if needed |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Neurological examination (motor, sensory, cerebellar, mental status) | Q4-8h inpatient; each outpatient visit | Improving after treatment initiation | Escalate to IVIg or PLEX if no improvement after 3-5 days of IV steroids | STAT | ROUTINE | ROUTINE | STAT |
| GCS / level of consciousness | Q4h inpatient; Q1h if ICU | Improving; GCS ≥13 | Escalate treatment; consider intubation if GCS declining; ICU transfer | STAT | ROUTINE | - | STAT |
| Blood glucose | Q6H during IV steroid pulse | <200 mg/dL | Sliding scale insulin; scheduled insulin if persistent | - | ROUTINE | - | ROUTINE |
| MRI brain (follow-up) | 3-6 months after acute event | Resolution or significant improvement of lesions; NO new lesions | New lesions suggest MS or MOGAD relapse; refer for long-term DMT consideration | - | - | ROUTINE | - |
| MOG-IgG titer (follow-up) | 3-6 months; 12 months | Declining or negative | Persistent positivity increases relapse risk; consider longer steroid taper or maintenance therapy | - | - | ROUTINE | - |
| Cognitive assessment | 3-6 months; 12 months post-event | Return to baseline cognition | Neuropsychological referral; educational support for children | - | - | ROUTINE | - |
| Seizure monitoring | During hospitalization; follow-up EEG if seizures occurred | No recurrent seizures | Continue anticonvulsant; EEG monitoring; consider tapering anticonvulsant at 3-6 months if seizure-free | - | ROUTINE | ROUTINE | ROUTINE |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Admit to floor | All patients with confirmed or suspected ADEM; need for IV methylprednisolone; neurological monitoring; infection exclusion |
| Admit to ICU | Severe encephalopathy (GCS ≤12); respiratory compromise; status epilepticus; rapidly deteriorating neurological exam; AHLE variant |
| Discharge from hospital | Neurologically improving; tolerating oral prednisone taper; no seizures; adequate oral intake; safe for home environment; follow-up MRI and neurology appointments scheduled |
| Outpatient follow-up (neurology) | All patients: 2-4 weeks post-discharge; 3-month follow-up MRI; 6-month and 12-month visits to monitor for relapse; longer follow-up if MOG-IgG positive |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IPMSSG diagnostic criteria for ADEM (2013 revision) | Consensus | [Krupp LB et al. Neurology 2013](https://pubmed.ncbi.nlm.nih.gov/23530151/) |
| High-dose IV methylprednisolone as first-line treatment for ADEM | Class IIa, Level C | [Tenembaum S et al. Neurology 2007](https://pubmed.ncbi.nlm.nih.gov/17898335/) |
| IVIg for steroid-refractory ADEM | Class IIb, Level C | [Pohl D et al. Neurology 2004](https://pubmed.ncbi.nlm.nih.gov/15596748/) |
| PLEX for fulminant steroid-refractory ADEM | Class IIb, Level C | [Keegan M et al. Neurology 2002](https://pubmed.ncbi.nlm.nih.gov/11865132/) |
| MOG-IgG associated ADEM: clinical features and prognosis | Class IIa, Level B | [Hacohen Y et al. Brain 2015](https://pubmed.ncbi.nlm.nih.gov/26209313/) |
| ADEM vs MS differentiation: MRI and CSF features | Class IIa, Level B | [Callen DJ et al. Neurology 2009](https://pubmed.ncbi.nlm.nih.gov/19221297/) |
| Oral steroid taper of 4-6 weeks reduces relapse risk | Class IIa, Level C | Expert consensus; IPMSSG recommendations |
| Persistent MOG-IgG positivity associated with higher relapse risk | Class IIa, Level B | [Waters PJ et al. Lancet Neurol 2020](https://pubmed.ncbi.nlm.nih.gov/31708357/) |

---

## NOTES

- ADEM requires ENCEPHALOPATHY for diagnosis (altered consciousness or behavioral change) — this distinguishes it from a first MS attack
- More common in children (mean age 5-8 years) but can occur in adults; adult ADEM requires careful MS exclusion
- Typical MRI: large (>1-2 cm), bilateral, poorly demarcated T2/FLAIR white matter lesions; deep gray matter (thalami, basal ganglia) involvement favors ADEM over MS
- MOG-IgG is positive in 30-60% of ADEM cases (especially pediatric); MOG-positive ADEM has higher relapse risk than MOG-negative
- AQP4-IgG positivity essentially excludes ADEM and reclassifies as NMOSD
- CSF oligoclonal bands are typically ABSENT in ADEM (present in >90% of MS) — important diagnostic distinction
- Monophasic ADEM has excellent prognosis: >70% recover fully or near-fully; residual cognitive deficits possible
- Follow-up MRI at 3-6 months is ESSENTIAL: new lesions suggest MS rather than ADEM; ADEM lesions should be resolving
- If second attack occurs ≥3 months after first, consider MDEM, MOGAD, or MS depending on clinical and imaging features
- Empiric acyclovir should be started alongside steroids until HSV PCR returns negative — do not delay steroids waiting for all results
- Fulminant hemorrhagic variant (AHLE/Weston Hurst) has very high mortality; aggressive treatment with PLEX and immunosuppression indicated

---

## CHANGE LOG

**v1.0 (February 11, 2026)**
- Initial template creation
- Comprehensive coverage including IPMSSG criteria, MOG-IgG testing, LP protocol
- Escalation pathway: steroids → IVIg → PLEX
- MS vs ADEM differentiation emphasis
- Evidence references with PubMed links
