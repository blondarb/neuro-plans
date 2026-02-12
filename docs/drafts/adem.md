---
title: "Acute Disseminated Encephalomyelitis (ADEM)"
description: "Clinical decision support for diagnosis and management of ADEM"
version: "1.1"
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

**VERSION:** 1.1
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Draft — Revised per checker feedback

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

═══════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════

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

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IV Methylprednisolone | IV | First-line for ADEM; begin as soon as CNS infection reasonably excluded; do NOT delay for LP results if clinical suspicion high | 1000 mg :: IV :: daily x 3-5 days :: Pediatric: 30 mg/kg/day (max 1000 mg) IV daily x 3-5 days; Adult: 1000 mg IV daily x 3-5 days; infuse over 1 hour | Active untreated bacterial/fungal infection; uncontrolled diabetes (relative) | Blood glucose Q6H; BP; mood/sleep; GI symptoms; electrolytes | STAT | STAT | - | STAT |
| Oral Prednisone taper | PO | Following IV methylprednisolone; prevents rebound; do NOT taper faster than 4 weeks | 1 mg/kg :: PO :: daily with taper :: Start 1 mg/kg/day (max 60 mg) after IV pulse; taper by 5-10 mg q3-5d over 4-6 weeks; do NOT taper faster than 4 weeks (risk of relapse) | Active untreated infection | Blood glucose; BP; mood; weight; GI protection (PPI) | - | ROUTINE | ROUTINE | - |
| Acyclovir (empiric) | IV | Empiric coverage for HSV encephalitis until PCR results return; ADEM and HSV can present similarly | 10 mg/kg :: IV :: q8h :: 10 mg/kg IV q8h; continue until HSV PCR confirmed negative (typically 48-72h); ensure adequate hydration | Hypersensitivity | Renal function (Cr); adequate hydration (prevent crystalluria); CBC | STAT | STAT | - | STAT |
| Lorazepam | IV | Acute seizure termination in ADEM | 0.1 mg/kg :: IV :: PRN seizure :: 0.1 mg/kg IV (max 4 mg) over 2 min; may repeat x1 in 5 min; max 8 mg | Severe respiratory depression without ventilator support | Respiratory status; sedation; BP | STAT | STAT | - | STAT |
| Omeprazole | PO/IV | GI ulcer prophylaxis during high-dose steroid therapy | 40 mg :: PO :: daily :: 40 mg PO/IV daily during IV steroid course and oral taper | PPI allergy | None routine | URGENT | STAT | ROUTINE | STAT |
| Insulin sliding scale | SC | Steroid-induced hyperglycemia management | Per protocol :: SC :: PRN :: Per institutional protocol if glucose >200 mg/dL; sliding scale insulin per hospital protocol | Hypoglycemia risk | Blood glucose Q6H; transition to scheduled insulin if persistent hyperglycemia | - | ROUTINE | - | ROUTINE |

*Note: Empiric acyclovir should be started alongside steroids until HSV PCR returns negative. Do not delay steroids waiting for all results. If seizures occur, levetiracetam is preferred first-line anticonvulsant (see 3B).*

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levetiracetam | IV/PO | Seizures in ADEM; preferred first-line anticonvulsant due to fewer drug interactions and no hepatic metabolism | 500 mg :: IV/PO :: BID :: Loading dose 20-30 mg/kg IV (max 3000 mg); then 500-1000 mg BID; adjust for renal function; may taper after 3-6 months if seizure-free and EEG normalized | Severe renal impairment (dose adjust) | Mood changes (rage, irritability); sedation; suicidality screening; renal function | STAT | STAT | ROUTINE | STAT |
| Gabapentin | PO | Neuropathic pain from myelitis component; painful paresthesias | 300 mg :: PO :: TID :: Start 300 mg qHS; titrate by 300 mg q1-3d; target 300-900 mg TID; max 3600 mg/day divided TID | Renal impairment (adjust dose per CrCl) | Sedation; dizziness; edema; renal function | - | ROUTINE | ROUTINE | - |
| Acetaminophen | PO/IV | Pain control; headache from steroids or acute illness; fever management | 1000 mg :: PO :: q6h PRN :: 1000 mg PO/IV q6h PRN; max 3000 mg/day (2000 mg/day if liver disease); pediatric: 15 mg/kg q6h (max 75 mg/kg/day) | Severe hepatic impairment; allergy | LFTs if prolonged use | STAT | STAT | ROUTINE | STAT |
| Famotidine | PO/IV | GI prophylaxis during high-dose steroid therapy (alternative to PPI) | 20 mg :: PO :: BID :: 20 mg PO BID during steroid therapy and taper; IV 20 mg q12h if NPO | Severe renal impairment (dose adjust) | GI symptoms | ROUTINE | ROUTINE | ROUTINE | ROUTINE |
| Baclofen | PO | Spasticity from myelitis component; painful tonic spasms | 5 mg :: PO :: TID :: Start 5 mg TID; titrate by 5 mg/dose q3d; max 80 mg/day; do NOT discontinue abruptly (risk of seizures, hallucinations) | Seizure disorder (lower threshold); renal impairment | Sedation; weakness; abrupt withdrawal causes seizures/hallucinations | - | ROUTINE | ROUTINE | - |
| Oxybutynin | PO | Neurogenic bladder urgency/frequency from myelitis component | 5 mg :: PO :: BID :: Start 5 mg BID; max 5 mg TID | Uncontrolled narrow-angle glaucoma; urinary retention; GI obstruction | Anticholinergic effects; cognitive effects (especially elderly and children); dry mouth | - | ROUTINE | ROUTINE | - |
| Docusate sodium | PO | Constipation prevention during immobility or opioid use | 100 mg :: PO :: BID :: 100 mg PO BID | Intestinal obstruction | Bowel function | - | ROUTINE | ROUTINE | - |
| Polyethylene glycol 3350 (MiraLAX) | PO | Constipation from neurogenic bowel or immobility | 17 g :: PO :: daily :: 17 g (1 capful) dissolved in 8 oz water daily | Intestinal obstruction; bowel perforation | Bowel function; electrolytes if prolonged | - | ROUTINE | ROUTINE | - |
| Ondansetron | IV/PO | Nausea and vomiting during acute illness or steroid therapy | 4 mg :: IV :: q6h PRN :: 4 mg IV/PO q6h PRN; max 16 mg/day | QTc prolongation; severe hepatic impairment (max 8 mg/day) | QTc if repeated dosing; LFTs | STAT | ROUTINE | ROUTINE | STAT |
| Melatonin | PO | Insomnia and sleep disruption from high-dose steroid therapy | 3 mg :: PO :: qHS :: 3-5 mg PO qHS; use during steroid pulse and taper; non-habit-forming | None significant | Sedation; next-day drowsiness | - | ROUTINE | ROUTINE | - |
| Calcium + Vitamin D | PO | Bone protection during prolonged corticosteroid therapy (taper >4 weeks) | 1000 mg calcium + 2000 IU vitamin D :: PO :: daily :: Calcium 1000-1200 mg/day + Vitamin D 1000-2000 IU/day; start with steroid taper; continue for duration of steroid use | Hypercalcemia; kidney stones | 25-OH Vitamin D level; calcium; DEXA if steroid use >3 months | - | ROUTINE | ROUTINE | - |

### 3C. Second-line/Refractory (Steroid-Refractory)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (Intravenous Immunoglobulin) | IV | Steroid-refractory ADEM (no improvement after 3-5 days of IV steroids); contraindication to steroids | 0.4 g/kg :: IV :: daily x 5 days :: 2 g/kg total divided over 2-5 days (0.4 g/kg/day x 5 days); premedicate with acetaminophen and diphenhydramine; check IgA level before first dose | IgA deficiency with anti-IgA antibodies; recent thromboembolic event; uncompensated HF; renal failure | Renal function; headache (aseptic meningitis); infusion reactions; BP; HR; thrombotic events | - | URGENT | - | URGENT |
| Plasma Exchange (PLEX) | Extracorporeal | Steroid-refractory and IVIg-refractory ADEM; severe fulminant ADEM (AHLE variant) | 5-7 exchanges :: Extracorporeal :: every other day :: 5-7 exchanges over 10-14 days; 1-1.5 plasma volumes per session; albumin replacement | Hemodynamic instability; severe coagulopathy; poor vascular access; sepsis | Coagulation studies (fibrinogen); electrolytes (calcium, potassium, magnesium); BP; hemodynamic monitoring; line site | - | URGENT | - | URGENT |
| Repeat IV Methylprednisolone (extended course) | IV | Incomplete response to initial 3-5 day course; may extend to 7-10 days in severe cases | 1000 mg :: IV :: daily :: 1000 mg IV daily; extend course to 7-10 days total if partial response after initial 3-5 days | Active untreated infection; uncontrolled diabetes; steroid psychosis | Glucose q6h; BP; mood; infection surveillance; electrolytes | - | URGENT | - | URGENT |

*Note: For steroid-refractory ADEM, IVIg is typically first escalation. PLEX is reserved for IVIg-refractory or fulminant cases (AHLE). If using sequential PLEX followed by IVIg, begin IVIg at least 24 hours after last PLEX exchange. ADEM is typically monophasic -- long-term DMTs are NOT indicated unless reclassified as MOGAD or MS.*

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation for ADEM diagnosis confirmation, immunotherapy management, and MS/MOGAD/NMOSD differentiation | STAT | STAT | ROUTINE | STAT |
| Neuroradiology review of MRI for ADEM vs MS lesion pattern characterization | URGENT | ROUTINE | ROUTINE | URGENT |
| Infectious disease consultation if infection cannot be confidently excluded or if unusual pathogen suspected | URGENT | ROUTINE | - | URGENT |
| Physical therapy for motor recovery, gait training, and rehabilitation planning | - | ROUTINE | ROUTINE | ROUTINE |
| Occupational therapy for ADL assessment and adaptive strategies during recovery | - | ROUTINE | ROUTINE | ROUTINE |
| Speech-language pathology for dysphagia assessment and communication if brainstem/cerebellar involvement | - | ROUTINE | ROUTINE | ROUTINE |
| Neuropsychology follow-up for cognitive assessment (cognitive deficits may persist especially in children) | - | - | ROUTINE | - |
| Ophthalmology if optic neuritis component present for visual acuity monitoring and OCT baseline | - | ROUTINE | ROUTINE | - |
| Rehabilitation medicine for comprehensive inpatient rehabilitation if significant residual motor or cognitive deficits | - | ROUTINE | ROUTINE | - |
| Social work for family support, insurance navigation, school/work accommodations, and discharge planning | - | ROUTINE | ROUTINE | - |
| Pediatric neurology referral if pediatric patient (ADEM most common in children ages 5-8) | URGENT | URGENT | ROUTINE | URGENT |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| ADEM is usually a monophasic illness with good recovery expected over weeks to months; most patients (>70%) recover fully or near-fully | ROUTINE | ROUTINE | ROUTINE | - |
| Return to ED immediately if new neurological symptoms develop after discharge (new weakness, vision changes, confusion, seizures) as this may indicate relapse or alternative diagnosis (MS, MOGAD) | STAT | ROUTINE | ROUTINE | - |
| Complete the full oral steroid taper as prescribed; do NOT stop abruptly (risk of disease rebound and adrenal crisis) | - | ROUTINE | ROUTINE | - |
| Follow-up MRI at 3-6 months is essential to confirm lesion resolution and rule out MS (new lesions on follow-up MRI would suggest MS rather than ADEM) | - | ROUTINE | ROUTINE | - |
| Report any new visual symptoms, limb weakness, numbness, or balance problems even after recovery, as these may indicate a second attack (MDEM or MS transition) | ROUTINE | ROUTINE | ROUTINE | - |
| Report any signs of infection (fever >100.4F, cough, dysuria) while on steroid therapy, as steroids suppress immune function | - | ROUTINE | ROUTINE | - |
| Avoid driving and operating heavy machinery while on sedating medications (levetiracetam, gabapentin) until tolerance established | - | ROUTINE | ROUTINE | - |
| Children: inform school of diagnosis and potential cognitive recovery needs; request neuropsychological testing before return | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Adequate rest during acute recovery; gradual return to school/work activities as neurological function improves | - | ROUTINE | ROUTINE | - |
| Vaccination review: ADEM can rarely be triggered by vaccines; this does NOT contraindicate future vaccination in most cases; discuss with neurologist and immunologist on case-by-case basis | - | - | ROUTINE | - |
| Seizure precautions if seizures occurred during acute phase; anticonvulsant taper guided by neurology (usually can be discontinued if EEG normalizes and seizure-free for 3-6 months) | - | ROUTINE | ROUTINE | - |
| Balanced diet with adequate calcium and vitamin D intake during steroid therapy; monitor weight | - | ROUTINE | ROUTINE | - |
| Avoid contact sports and high-risk activities until neurological recovery is complete and cleared by neurology | - | ROUTINE | ROUTINE | - |
| Stress management and psychological support; ADEM diagnosis can be distressing for patients and families; consider counseling if adjustment difficulties | - | - | ROUTINE | - |

---

═══════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════

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

**v1.1 (February 11, 2026)**
- Restructured Section 3 to standard numbering: 3A Acute/Emergent, 3B Symptomatic, 3C Second-line/Refractory
- Moved lorazepam and omeprazole/insulin to 3A (acute); moved IVIg/PLEX to 3C (refractory)
- Added symptomatic medications: gabapentin (neuropathic pain), baclofen (spasticity), oxybutynin (neurogenic bladder), acetaminophen (pain/fever), docusate/MiraLAX (constipation), ondansetron (nausea), melatonin (steroid-induced insomnia), calcium/vitamin D (bone protection)
- Fixed structured dosing format across all treatment rows to consistent `dose :: route :: frequency :: instructions`
- Added Section A/B dividers (═══)
- Updated 4A Referrals: added rehabilitation medicine, social work, pediatric neurology; expanded ICU coverage for PT/OT/SLP
- Updated 4B Patient Instructions: added infection reporting, driving precautions, school accommodations; improved ED coverage
- Updated 4C Lifestyle: added diet/calcium, contact sports avoidance, stress management
- Fixed setting coverage gaps: added neuroradiology ED/ICU coverage; expanded PT/OT/SLP ICU coverage; added omeprazole ED coverage
- Upgraded levetiracetam monitoring (suicidality screening, behavioral changes)

**v1.0 (February 11, 2026)**
- Initial template creation
- Comprehensive coverage including IPMSSG criteria, MOG-IgG testing, LP protocol
- Escalation pathway: steroids → IVIg → PLEX
- MS vs ADEM differentiation emphasis
- Evidence references with PubMed links
