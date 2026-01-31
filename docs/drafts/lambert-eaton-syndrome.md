---
title: Lambert-Eaton Myasthenic Syndrome (LEMS)
description: Clinical decision support for Lambert-Eaton myasthenic syndrome diagnosis and management including paraneoplastic evaluation, symptomatic treatment, and immunotherapy.
version: "1.1"
setting: ED, HOSP, OPD, ICU
status: draft
tags:
  - neuromuscular
  - paraneoplastic
  - autoimmune
  - neuromuscular-junction
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Lambert-Eaton Myasthenic Syndrome (LEMS)

**VERSION:** 1.1
**CREATED:** January 30, 2026
**REVISED:** January 30, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Lambert-Eaton Myasthenic Syndrome (LEMS)

**ICD-10:** G73.1 (Lambert-Eaton syndrome), C34.90 (Malignant neoplasm of unspecified part of unspecified bronchus or lung - for paraneoplastic LEMS), G70.80 (Other specified myoneural disorders)

**SYNONYMS:** Lambert-Eaton myasthenic syndrome, LEMS, Lambert-Eaton syndrome, Eaton-Lambert syndrome, paraneoplastic Lambert-Eaton syndrome, autoimmune Lambert-Eaton syndrome, VGCC antibody syndrome, P/Q-type calcium channel antibody syndrome, presynaptic neuromuscular junction disorder, paraneoplastic neuromuscular junction disorder, voltage-gated calcium channel antibody disease, myasthenic syndrome

**SCOPE:** Diagnosis and management of Lambert-Eaton myasthenic syndrome in adults, including both paraneoplastic (P-LEMS, ~60% associated with small cell lung cancer) and autoimmune (A-LEMS) subtypes. Covers VGCC antibody testing, DELTA-P score calculation for paraneoplastic risk stratification, electrodiagnostic evaluation (repetitive nerve stimulation), cancer screening protocols, symptomatic treatment with 3,4-diaminopyridine, immunotherapy, and long-term monitoring. Excludes myasthenia gravis (separate template), botulism, and congenital myasthenic syndromes.

---

**DEFINITIONS:**
- **P-LEMS:** Paraneoplastic LEMS, associated with underlying malignancy (~60% SCLC)
- **A-LEMS:** Autoimmune LEMS, no associated malignancy (non-paraneoplastic)
- **VGCC:** Voltage-gated calcium channel (P/Q-type antibodies are diagnostic)
- **DELTA-P Score:** Dutch-English LEMS Tumor Association Prediction score for paraneoplastic risk
- **Lambert sign:** Hyporeflexia that improves or normalizes after brief maximal voluntary contraction (post-exercise facilitation)
- **CMAP facilitation:** >100% increment in compound muscle action potential amplitude after high-frequency (50 Hz) repetitive nerve stimulation or after 10-second maximal voluntary contraction

---

**DELTA-P SCORE (Paraneoplastic Risk Stratification):**

| Feature | Points |
|---------|:------:|
| **D** - Dysarthria or Dysphagia at onset | 1 |
| **E** - Erectile dysfunction (males) | 1 |
| **L** - Loss of weight (>5% in 6 months) | 1 |
| **T** - Tobacco use (current or recent) | 1 |
| **A** - Age at onset >50 years | 1 |
| **P** - Positive bulbar involvement | 1 |

**Interpretation:**
- Score 0-1: Low risk of malignancy (~0-2%); likely autoimmune LEMS
- Score 2: Intermediate risk (~15-25%); cancer screening recommended
- Score >=3: High risk of malignancy (~83-96%); intensive cancer screening mandatory; SCLC most common

*Note: DELTA-P score >=3 has sensitivity ~96% and specificity ~99% for paraneoplastic LEMS (Titulaer et al. J Neurol Neurosurg Psychiatry 2011).*

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline before immunotherapy; infection screen; paraneoplastic cytopenias | Normal |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal/hepatic function baseline; electrolytes; pre-treatment assessment | Normal |
| P/Q-type VGCC antibody (CPT 86255) | URGENT | URGENT | ROUTINE | URGENT | Primary diagnostic test; positive in ~85-90% of LEMS (both P-LEMS and A-LEMS); sensitivity highest for P/Q-type | Negative (<0.02 nmol/L); positive confirms LEMS in appropriate clinical context |
| N-type VGCC antibody | URGENT | URGENT | ROUTINE | URGENT | May be co-positive with P/Q-type; less specific but supportive | Negative |
| SOX1 antibody | URGENT | URGENT | ROUTINE | URGENT | Paraneoplastic marker highly specific for SCLC (~64% sensitivity in P-LEMS); helps distinguish P-LEMS from A-LEMS | Negative (positive strongly suggests underlying SCLC) |
| ESR (CPT 85652) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory/autoimmune screen; cancer screening | Normal |
| CRP (CPT 86140) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory marker; infection screen | Normal |
| TSH (CPT 84443) | URGENT | ROUTINE | ROUTINE | URGENT | Thyroid disease as autoimmune comorbidity; hypothyroidism worsens weakness | Normal |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Pre-steroid baseline; autonomic dysfunction assessment | Normal |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Glycemic status before corticosteroid initiation | <5.7% |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia worsens neuromuscular transmission | Normal (1.7-2.2 mg/dL) |
| Calcium (CPT 82310) | STAT | STAT | ROUTINE | STAT | Calcium channel function directly relevant to LEMS pathophysiology | Normal (8.5-10.5 mg/dL) |
| Phosphorus (CPT 84100) | STAT | STAT | ROUTINE | STAT | Baseline electrolyte panel | Normal |
| PT/INR (CPT 85610) | STAT | STAT | - | STAT | Coagulation baseline before procedures | Normal |
| Urinalysis (CPT 81003) | STAT | ROUTINE | ROUTINE | STAT | Infection screen; baseline | Negative |
| LDH (CPT 83615) | URGENT | ROUTINE | ROUTINE | URGENT | Tumor marker; baseline before immunotherapy | Normal |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| AChR binding antibody (CPT 86235) | - | URGENT | ROUTINE | - | MG overlap screen; ~15% of LEMS patients have concurrent MG antibodies | Negative |
| AChR modulating antibody (CPT 86235) | - | URGENT | ROUTINE | - | MG overlap; increases sensitivity for coexistent MG | Negative |
| GAD65 antibody | - | ROUTINE | ROUTINE | - | Autoimmune overlap (stiff person syndrome, cerebellar ataxia, type 1 diabetes) | Negative |
| ANNA-1 (anti-Hu) antibody | - | ROUTINE | ROUTINE | - | Paraneoplastic marker for SCLC; sensory neuropathy overlap | Negative |
| CRMP-5 (anti-CV2) antibody | - | ROUTINE | ROUTINE | - | Paraneoplastic marker; associated with SCLC, chorea, neuropathy | Negative |
| Amphiphysin antibody | - | ROUTINE | ROUTINE | - | Paraneoplastic marker; stiff person spectrum; breast/lung cancer | Negative |
| Anti-Zic4 antibody | - | ROUTINE | ROUTINE | - | Paraneoplastic marker; cerebellar degeneration with SCLC | Negative |
| ANA (CPT 86235) | - | ROUTINE | ROUTINE | - | Autoimmune overlap screen (SLE, Sjogren) | Negative or low titer |
| Hepatitis B surface antigen (CPT 80074) | - | ROUTINE | ROUTINE | - | Screen before rituximab/immunosuppression (reactivation risk) | Negative |
| Hepatitis B core antibody | - | ROUTINE | ROUTINE | - | Screen for prior HBV before rituximab | Negative |
| Hepatitis C antibody (CPT 80074) | - | ROUTINE | ROUTINE | - | Screen before immunosuppression | Negative |
| HIV (CPT 87389) | - | ROUTINE | ROUTINE | - | Screen before immunosuppression | Negative |
| Quantitative immunoglobulins (IgG, IgA, IgM) | - | ROUTINE | ROUTINE | - | Baseline before IVIg; monitor on immunosuppression | Normal |
| TB test (QuantiFERON-Gold or PPD) | - | ROUTINE | ROUTINE | - | Screen before immunosuppression | Negative |
| Vitamin D (25-OH) (CPT 82306) | - | ROUTINE | ROUTINE | - | Immune modulation; deficiency common in autoimmune disease | >30 ng/mL |
| PSA (males >50) (CPT 84153) | - | ROUTINE | ROUTINE | - | Malignancy screen in paraneoplastic workup | Normal |
| CEA (CPT 82378) | - | ROUTINE | ROUTINE | - | Tumor marker screen; lung and GI malignancies | Normal (<5 ng/mL) |
| NSE (neuron-specific enolase) | - | ROUTINE | ROUTINE | - | SCLC tumor marker; elevated in ~60% of SCLC | Normal |
| ProGRP (pro-gastrin-releasing peptide) | - | ROUTINE | ROUTINE | - | SCLC-specific tumor marker; more specific than NSE | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| VGKC-complex antibody (LGI1, CASPR2) | - | EXT | EXT | - | Autoimmune encephalitis overlap; if cognitive or autonomic features prominent | Negative |
| Paraneoplastic antibody comprehensive panel | - | EXT | EXT | - | If initial antibodies negative but paraneoplastic syndrome suspected | Negative |
| SPEP with immunofixation (CPT 86334) | - | ROUTINE | EXT | - | Paraproteinemic neuropathy screen in atypical cases | Normal |
| Free light chains (serum) | - | EXT | EXT | - | Light chain disease screen | Normal ratio |
| Ganglionic AChR antibody | - | EXT | EXT | - | Autoimmune autonomic ganglionopathy if prominent autonomic features | Negative |
| Anti-Purkinje cell antibody (PCA-Tr/DNER) | - | EXT | EXT | - | Paraneoplastic cerebellar degeneration overlap with LEMS | Negative |
| Muscle biopsy | - | EXT | EXT | - | If diagnosis uncertain; rule out inflammatory myopathy | Normal |
| Genetic testing (CACNA1A, CACNB4) | - | - | EXT | - | Familial hemiplegic migraine/episodic ataxia with calcium channelopathy overlap; very rare | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT chest with contrast (CPT 71260) | URGENT | URGENT | ROUTINE | URGENT | Within 24-48h of diagnosis; primary malignancy screen | No lung mass, mediastinal lymphadenopathy, or thymoma | Contrast allergy, renal insufficiency |
| Chest X-ray (PA and lateral) (CPT 71046) | STAT | STAT | ROUTINE | STAT | Immediate; initial screen for lung mass | No mass lesion, no hilar adenopathy | None significant |
| PET/CT (FDG) (CPT 78816) | - | URGENT | ROUTINE | - | Within 1-2 weeks of diagnosis; most sensitive for occult SCLC if CT chest negative; recommended for all LEMS patients | No FDG-avid lesion; SCLC can be very small and CT-occult | Uncontrolled diabetes (glucose >200); pregnancy |
| ECG (12-lead) (CPT 93000) | STAT | ROUTINE | ROUTINE | STAT | At presentation; autonomic dysfunction assessment | Normal sinus rhythm; no QTc prolongation | None |

### 2B. Electrodiagnostic & Specialized Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Repetitive nerve stimulation (RNS) - low rate (2-3 Hz) (CPT 95937) | - | URGENT | ROUTINE | - | During workup; test multiple nerves including proximal muscles | Decremental response >10% at 2-3 Hz (similar to MG but typically more pronounced; test hand and shoulder muscles) | Pacemaker (relative) |
| Repetitive nerve stimulation (RNS) - high rate (20-50 Hz) (CPT 95937) | - | URGENT | ROUTINE | - | Immediately after low-rate RNS; DIAGNOSTIC hallmark of LEMS | Incremental response >100% (often >200%) at high-frequency stimulation; this distinguishes LEMS from MG | Pacemaker (relative); painful - consider post-exercise facilitation instead |
| Post-exercise facilitation testing (CPT 95937) | - | URGENT | ROUTINE | - | 10 seconds of maximal voluntary contraction then immediate repeat CMAP; preferred over high-rate RNS (less painful) | >100% increment in CMAP amplitude post-exercise; characteristic of presynaptic NMJ disorder | None significant |
| Baseline CMAP amplitude assessment | - | URGENT | ROUTINE | - | Before RNS; record resting CMAP amplitudes in multiple nerves | Low resting CMAP amplitudes (typically <5 mV in hand muscles); hallmark of LEMS | None |
| Standard EMG/NCS (CPT 95886, 95907-95913) | - | ROUTINE | ROUTINE | - | Complete electrodiagnostic evaluation; rule out concurrent neuropathy/myopathy | Low CMAP amplitudes at rest; normal sensory responses; no active denervation (unless cancer-related neuropathy) | None significant |
| Single-fiber EMG (SFEMG) (CPT 95872) | - | ROUTINE | ROUTINE | - | If RNS non-diagnostic; increased jitter with improvement at higher firing rates (opposite of MG pattern) | Increased jitter that improves with increased firing rate (presynaptic pattern) | Requires experienced electromyographer |
| Autonomic function testing (CPT 95921-95924) | - | ROUTINE | ROUTINE | - | If autonomic symptoms present; quantifies autonomic involvement | Abnormal sudomotor, cardiovagal, or adrenergic responses; supports LEMS diagnosis | None significant |

### 2C. Cancer Screening Protocol

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Notes |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------|
| CT chest/abdomen/pelvis with contrast | - | URGENT | ROUTINE | - | If initial CT chest negative and clinical suspicion high (DELTA-P >=2) | No occult malignancy | Annual screening required for at least 2 years |
| PET/CT (repeat if initial negative) | - | - | ROUTINE | - | Every 6 months for 2 years if DELTA-P >=3 and initial PET negative | No FDG-avid lesion | SCLC may be delayed in presentation; continuous vigilance |
| CT chest (low-dose screening) | - | - | ROUTINE | - | Every 6 months for 2 years from diagnosis; then annually for 2 more years (total 4 years screening) | No new lung nodules or mass | Per EFNS/PNS guidelines; P-LEMS risk persists for years |
| MRI brain with contrast (CPT 70553) | - | ROUTINE | ROUTINE | - | If neurological symptoms suggest brain metastases or paraneoplastic cerebellar degeneration | No metastases; no cerebellar atrophy | Gadolinium allergy, GFR <30, pacemaker |
| Bronchoscopy with biopsy | - | ROUTINE | - | - | If CT/PET shows suspicious pulmonary lesion | Tissue diagnosis; SCLC vs NSCLC | Coagulopathy; severe respiratory compromise |
| Mammography (females) | - | - | ROUTINE | - | As part of comprehensive malignancy screen | No malignancy | Per age-appropriate screening guidelines |
| Colonoscopy (age-appropriate) | - | - | ROUTINE | - | If no lung cancer found; screen for other malignancies | No malignancy | Bowel prep; coagulopathy |

*Note: Cancer screening protocol based on Titulaer et al. recommendations. If initial comprehensive screening is negative, repeat CT chest every 6 months for 2 years. If DELTA-P score >=3, repeat PET/CT at 3-6 months. ~3-5% of patients initially classified as A-LEMS are later diagnosed with cancer, usually within 2 years.*

### 2D. Bedside Clinical Tests

| Test | ED | HOSP | OPD | ICU | Timing | Target Finding | Notes |
|------|:--:|:----:|:---:|:---:|--------|----------------|-------|
| Deep tendon reflex testing (pre- and post-exercise) | STAT | STAT | ROUTINE | STAT | Initial exam; Lambert sign assessment | Hyporeflexia or areflexia at rest that improves after 10 sec maximal contraction (Lambert sign); pathognomonic for LEMS | Compare reflexes before and after 10-second isometric contraction |
| Manual muscle testing (proximal emphasis) | STAT | STAT | ROUTINE | STAT | Initial exam | Proximal weakness legs > arms; hip flexors and quadriceps most affected; may improve briefly with initial contraction | Use MRC grading scale; document post-exercise augmentation |
| Grip strength testing (pre- and post-exercise) | STAT | STAT | ROUTINE | STAT | Serial assessment | Reduced grip at baseline; may improve after initial maximal effort (post-exercise facilitation) | Dynamometer preferred for objective measurement |
| Forced vital capacity (FVC) | STAT | STAT | - | STAT | At presentation and serially if respiratory symptoms | >20 mL/kg (>1.5 L) | Respiratory failure rare in LEMS but can occur, especially with cancer treatment or crisis |
| Negative inspiratory force (NIF/MIP) | STAT | STAT | - | STAT | At presentation and serially | More negative than -40 cm H2O | Monitor if worsening weakness or peri-treatment |
| Orthostatic vital signs | STAT | STAT | ROUTINE | STAT | Initial assessment; autonomic dysfunction quantification | No orthostatic hypotension (drop >20 systolic or >10 diastolic on standing) | Common in LEMS due to autonomic involvement |
| Pupillary examination | STAT | STAT | ROUTINE | STAT | Initial exam | Normal pupillary responses; sluggish pupils may suggest autonomic involvement | Distinguish from botulism (fixed dilated pupils) |
| Dry mouth assessment (visual analog scale) | - | ROUTINE | ROUTINE | - | Each visit; autonomic symptom tracking | No xerostomia | Dry mouth is one of the earliest and most common autonomic features |

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (intravenous immunoglobulin) (CPT 96365) | IV | Acute LEMS exacerbation with significant functional impairment; rapid symptom control; pre-treatment or perioperative optimization | 0.4 g/kg :: IV :: daily x 5 days :: 0.4 g/kg/day IV x 5 days (total 2 g/kg) OR 1 g/kg/day x 2 days; infuse over 4-6 hours; slow initial rate per protocol | IgA deficiency (check IgA level first); recent thrombotic event; renal failure (use sucrose-free formulation) | Pre-infusion: IgA level, renal function, CBC; during: vital signs q15 min first hour then q1h; headache; aseptic meningitis; thrombosis risk; renal function post-infusion | STAT | STAT | - | STAT |
| Plasma exchange (PLEX) (CPT 36514) | IV | Acute LEMS exacerbation; alternative to IVIg; LEMS crisis with respiratory compromise; pre-thymectomy optimization if concurrent thymoma | 1-1.5 plasma volumes :: IV :: every other day x 5-7 exchanges :: 5-7 exchanges over 10-14 days; exchange 1-1.5 plasma volumes per session every other day; albumin replacement preferred | Hemodynamic instability; sepsis; central line contraindication; heparin allergy | BP during exchange; electrolytes (Ca, K, Mg); coagulation studies; fibrinogen; line site infection; hypotension | STAT | STAT | - | STAT |
| Normal saline IV | IV | Volume resuscitation for orthostatic hypotension from autonomic dysfunction | 500-1000 mL :: IV :: bolus then maintenance :: 500-1000 mL NS bolus then 75-125 mL/hr maintenance as needed for orthostatic symptoms | Heart failure; volume overload | I/O; BP; orthostatic vitals; weight | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| 3,4-Diaminopyridine (amifampridine/Firdapse) | PO | First-line symptomatic treatment for LEMS; enhances presynaptic acetylcholine release by blocking potassium channels; improves strength and autonomic symptoms | 5 mg :: PO :: TID :: Start 5 mg TID; increase by 5 mg per dose every 3-5 days; usual effective dose 15-20 mg TID-QID; max 80 mg/day (max 20 mg per single dose); take with food | Seizure history (lowers seizure threshold); concurrent use of drugs that lower seizure threshold; QT prolongation | ECG at baseline and after dose changes; seizure precautions; QTc monitoring; paresthesias (perioral, digital); GI upset | URGENT | URGENT | ROUTINE | URGENT |
| 3,4-Diaminopyridine phosphate (Ruzurgi) | PO | Alternative formulation of amifampridine for LEMS; enhances presynaptic acetylcholine release by blocking potassium channels; improves strength and autonomic symptoms | 5 mg :: PO :: TID :: Start 5 mg TID; increase by 5 mg per dose every 3-5 days; usual effective dose 15-20 mg TID-QID; max 80 mg/day (max 20 mg per single dose); take with food | Seizure history (lowers seizure threshold); concurrent use of drugs that lower seizure threshold; QT prolongation | ECG at baseline and after dose changes; seizure precautions; QTc monitoring; paresthesias (perioral, digital); GI upset | URGENT | URGENT | ROUTINE | URGENT |
| Pyridostigmine (Mestinon) | PO | Adjunctive symptomatic treatment; enhances postsynaptic acetylcholine effect; less effective in LEMS than in MG but may provide modest additional benefit when combined with 3,4-DAP | 30 mg :: PO :: TID :: Start 30 mg TID; increase by 30 mg per dose every 2-3 days; usual effective dose 60 mg q4-6h; max 120 mg per dose; less effective as monotherapy in LEMS than MG | Mechanical GI/GU obstruction; uncontrolled asthma | Cholinergic side effects: diarrhea, cramping, salivation, bradycardia | - | ROUTINE | ROUTINE | - |
| Guanfacine | PO | Refractory dry mouth from autonomic dysfunction not responsive to 3,4-DAP; off-label use | 1 mg :: PO :: daily :: Start 1 mg daily; may increase to 2 mg daily; used off-label for autonomic dry mouth | Hypotension; bradycardia; renal impairment | BP; HR; sedation | - | - | ROUTINE | - |
| Midodrine | PO | Orthostatic hypotension from autonomic dysfunction in LEMS | 2.5 mg :: PO :: TID :: Start 2.5 mg TID; titrate by 2.5 mg per dose every 1-2 weeks; max 10 mg TID; avoid dosing within 4 hours of bedtime | Supine hypertension; urinary retention; severe organic heart disease; pheochromocytoma | Supine BP (check 1 hour after first dose); avoid supine position for 4h after dosing | - | ROUTINE | ROUTINE | - |
| Fludrocortisone | PO | Orthostatic hypotension refractory to midodrine; volume expansion | 0.1 mg :: PO :: daily :: Start 0.1 mg daily; may increase to 0.2 mg daily; max 0.3 mg daily | Heart failure; hypertension; edema | Electrolytes (hypokalemia); weight; BP; edema; supine hypertension | - | ROUTINE | ROUTINE | - |
| Polyethylene glycol 3350 (MiraLAX) | PO | Constipation from autonomic dysfunction in LEMS | 17 g :: PO :: daily :: 17 g (1 capful) dissolved in 8 oz liquid once daily; adjust frequency to bowel response | Known bowel obstruction | Bowel habits; electrolytes if prolonged use | - | ROUTINE | ROUTINE | - |
| Senna | PO | Constipation from autonomic dysfunction; adjunct to osmotic laxative | 8.6 mg :: PO :: qHS :: 8.6-17.2 mg PO qHS; may increase to BID if needed; max 34.4 mg/day | Bowel obstruction; acute abdominal pain | Bowel habits; avoid long-term use if possible | - | ROUTINE | ROUTINE | - |
| Artificial tears/saliva substitutes | TOP | Dry eyes and dry mouth from autonomic dysfunction | 1-2 drops :: TOP :: q2-4h PRN :: Artificial tears q2-4h PRN for dry eyes; saliva substitute spray or lozenges PRN for dry mouth | None significant | Symptom relief assessment | - | ROUTINE | ROUTINE | - |
| Sildenafil | PO | Erectile dysfunction from autonomic dysfunction in LEMS | 25 mg :: PO :: PRN :: Start 25 mg PO 1 hour before sexual activity; may increase to 50-100 mg; max 100 mg/day | Concurrent nitrates (CONTRAINDICATED); severe cardiovascular disease; recent stroke/MI within 6 months | BP; cardiac status; vision changes; priapism | - | - | ROUTINE | - |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Prednisone | PO | Autoimmune LEMS (A-LEMS) with inadequate response to 3,4-DAP alone; bridge to steroid-sparing agent; NOT first-line for P-LEMS (treat cancer first) | 10-20 mg :: PO :: daily :: Start 10-20 mg daily; increase by 10 mg every 5-7 days to 0.5-1 mg/kg/day; maintain 4-8 weeks then taper by 5-10 mg/month to lowest effective dose | Active untreated infection; uncontrolled diabetes; psychosis history | Glucose; BP; mood/sleep; weight; bone density; GI prophylaxis | - | ROUTINE | ROUTINE | - |
| IVIg (maintenance) | IV | Chronic immunomodulation for LEMS with ongoing functional impairment despite 3,4-DAP and oral immunotherapy | 1 g/kg :: IV :: every 4 weeks :: 1 g/kg IV every 4 weeks (may adjust to 0.4-1 g/kg based on response); infuse over 4-6 hours | IgA deficiency; recent thrombotic event; renal failure | Renal function; IgA level; vital signs during infusion; headache; thrombosis risk | - | ROUTINE | ROUTINE | ROUTINE |
| Plasma exchange (maintenance) | IV | Chronic LEMS refractory to IVIg and oral immunotherapy | 1 plasma volume :: IV :: every 2-4 weeks :: Single volume exchange every 2-4 weeks; adjust frequency based on clinical response and antibody levels; albumin replacement | Hemodynamic instability; line complications | BP; electrolytes; coagulation; line site | - | ROUTINE | - | - |

### 3D. Disease-Modifying / Immunosuppressive Therapies

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Azathioprine (Imuran) | PO | Steroid-sparing agent for A-LEMS; long-term immunosuppression to reduce VGCC antibody production; onset 6-18 months | 50 mg :: PO :: daily :: Start 50 mg daily; increase by 50 mg every 1-2 weeks to target 2-3 mg/kg/day (typically 150-250 mg/day); onset 6-18 months | TPMT genotype/activity BEFORE starting (mandatory); CBC; LFTs; hepatitis B/C screen; TB test | TPMT deficiency (homozygous); concurrent allopurinol (reduce dose by 75%); pregnancy (relative); active infection | TPMT genotype before starting; CBC q1-2 weeks during titration then monthly; LFTs monthly; amylase/lipase if abdominal pain; lymphocyte count target 600-1000 | - | ROUTINE | ROUTINE | - |
| Mycophenolate mofetil (CellCept) | PO | Steroid-sparing agent for A-LEMS; alternative to azathioprine; onset 6-12 months | 500 mg :: PO :: BID :: Start 500 mg BID; increase to 1000 mg BID after 2 weeks; target 2000-3000 mg/day; onset 6-12 months | CBC; LFTs; hepatitis B/C screen; pregnancy test (females); TB test | Pregnancy (Category D - teratogenic); concurrent azathioprine; active infection | CBC q2 weeks x 3 months then monthly; LFTs; GI side effects (diarrhea, nausea); lymphopenia; REMS pregnancy prevention | - | ROUTINE | ROUTINE | - |
| Rituximab (Rituxan) | IV | Refractory A-LEMS not responding to conventional immunosuppressants; may be used earlier in severe cases; less evidence than in MG but reported efficacy | 375 mg/m2 :: IV :: weekly x 4 weeks :: 375 mg/m2 IV weekly x 4 weeks; OR 1000 mg IV x 2 doses 14 days apart; re-dose when CD19/CD20 recover or clinical worsening; onset 3-6 months | HBV serology (HBsAg, anti-HBc, anti-HBs); hepatitis C screen; HIV test; CBC; immunoglobulins; TB test; vaccinations up to date | Active hepatitis B; active infection; severe immunodeficiency; PML history | CD19/CD20 counts q3-6 months; immunoglobulins q6 months; PML risk (very rare); infusion reactions (premedicate with acetaminophen, diphenhydramine, methylprednisolone) | - | ROUTINE | ROUTINE | - |
| Cyclosporine (Sandimmune/Neoral) | PO | Alternative steroid-sparing agent for A-LEMS; faster onset than azathioprine (2-6 months) | 2-3 mg/kg/day :: PO :: BID :: Start 2-3 mg/kg/day divided BID; target trough 100-150 ng/mL; onset 2-6 months | Renal function; BP; electrolytes; hepatitis screen; TB test | Uncontrolled hypertension; renal impairment; concurrent nephrotoxic drugs | Trough levels; renal function q2 weeks then monthly; BP; electrolytes (K, Mg); lipids; gingival hyperplasia; hirsutism | - | - | ROUTINE | - |
| Cyclophosphamide | IV | Severe refractory LEMS not responding to other immunosuppressants; reserved for life-threatening or disabling disease | 500-1000 mg/m2 :: IV :: monthly x 6 months :: Pulse IV 500-1000 mg/m2 monthly x 6 months; OR oral 1-2 mg/kg/day; reserved for refractory cases; MESNA uroprotection with IV dosing | CBC; renal function; hepatitis screen; pregnancy test; fertility counseling | Pregnancy; active infection; bone marrow suppression; hemorrhagic cystitis history | CBC weekly during treatment; urinalysis (hemorrhagic cystitis); fertility counseling; malignancy risk | - | EXT | EXT | EXT |
| Oncology-directed chemotherapy (cisplatin/etoposide) | IV | Standard first-line for SCLC in P-LEMS; treatment of underlying malignancy is the primary therapy for paraneoplastic LEMS; neurological symptoms often improve with cancer treatment | Per oncology protocol :: IV :: per oncology :: Cisplatin 60-80 mg/m2 day 1 + etoposide 100-120 mg/m2 days 1-3 q21d x 4-6 cycles; defer to oncology for specific regimen | Oncology staging; LEMS diagnosis confirmation; LEMS-specific caution: avoid neuromuscular blocking agents if surgery needed | Per oncology assessment | Neuromuscular function during treatment; FVC if respiratory symptoms; electrolytes; renal function; myelosuppression | - | ROUTINE | ROUTINE | - |
| Radiation therapy (SCLC) | EXT | Limited-stage SCLC with or without concurrent chemotherapy; palliative radiation for extensive-stage | Per radiation oncology protocol :: EXT :: per oncology :: Concurrent chemoradiation for limited stage; palliative for extensive stage; prophylactic cranial irradiation per oncology | Radiation oncology staging; treatment planning | Per radiation oncology assessment | Neurological function; esophagitis; pneumonitis | - | ROUTINE | ROUTINE | - |
| Immune checkpoint inhibitors (with extreme caution) | IV | SCLC maintenance (atezolizumab, durvalumab); CRITICAL WARNING: may worsen LEMS or trigger myasthenic crisis; only under joint neuro-oncology management | Per oncology protocol :: IV :: per oncology :: Per oncology; MUST be administered with close neuromuscular monitoring; have IVIg/PLEX available | Baseline FVC; neuromuscular assessment; joint neuro-oncology plan | Pre-existing myasthenic crisis; uncontrolled LEMS; use only with neuromuscular specialist co-management | FVC before each cycle; MG-ADL equivalent assessment; creatine kinase; troponin (myocarditis); monitor for rapid neurological deterioration | - | EXT | EXT | EXT |

*Note: Treatment of underlying malignancy is the most important therapy in P-LEMS. LEMS symptoms often improve significantly with successful cancer treatment. Immunosuppressive therapy (azathioprine, mycophenolate, rituximab) should be used cautiously in P-LEMS as it may impair anti-tumor immunity. Immune checkpoint inhibitors may paradoxically worsen paraneoplastic neurological syndromes.*

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neuromuscular specialist referral for diagnosis confirmation, treatment planning, and long-term management of LEMS | URGENT | URGENT | ROUTINE | URGENT |
| Oncology referral for cancer screening and management in all LEMS patients (mandatory given ~60% paraneoplastic association) | URGENT | URGENT | ROUTINE | URGENT |
| Pulmonology referral for respiratory function monitoring if FVC declining or significant weakness | - | ROUTINE | ROUTINE | URGENT |
| Thoracic surgery referral if lung mass identified on imaging | - | URGENT | ROUTINE | - |
| Radiation oncology referral if SCLC confirmed for treatment planning | - | ROUTINE | ROUTINE | - |
| Speech-language pathology for swallow evaluation if dysphagia or bulbar symptoms present | - | URGENT | ROUTINE | URGENT |
| Physical therapy for proximal strengthening, gait training, and fall prevention given proximal leg weakness | - | ROUTINE | ROUTINE | ROUTINE |
| Occupational therapy for ADL adaptation and energy conservation strategies | - | ROUTINE | ROUTINE | - |
| Urology referral for erectile dysfunction management if not responsive to first-line treatment | - | - | ROUTINE | - |
| Gastroenterology referral for refractory constipation from autonomic dysfunction | - | - | ROUTINE | - |
| Psychiatry/Psychology referral for depression, anxiety, and adjustment to chronic diagnosis with cancer risk | - | ROUTINE | ROUTINE | - |
| Social work consult for insurance navigation, disability evaluation, and cancer support resources | - | ROUTINE | ROUTINE | - |
| Pain management referral for chronic pain from sustained weakness or paraneoplastic neuropathy | - | - | EXT | - |
| Palliative care referral for P-LEMS with advanced malignancy for goals of care discussion and symptom management | - | ROUTINE | ROUTINE | ROUTINE |
| Infusion center coordination for IVIg or rituximab scheduling | - | ROUTINE | ROUTINE | - |
| Smoking cessation program referral given strong association between LEMS and SCLC in tobacco users | - | ROUTINE | ROUTINE | - |
| Cardiology referral if autonomic dysfunction includes cardiac arrhythmias or significant orthostatic hypotension | - | ROUTINE | ROUTINE | URGENT |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED immediately if difficulty breathing, worsening weakness preventing walking, or inability to swallow (may indicate LEMS crisis or cancer progression) | ✓ | ✓ | ✓ |
| Return to ED if new severe weakness, falls, or inability to rise from chair (proximal weakness progression) | ✓ | ✓ | ✓ |
| Take 3,4-diaminopyridine (amifampridine) exactly as prescribed; do NOT exceed 20 mg per single dose or 80 mg/day (seizure risk) | ✓ | ✓ | ✓ |
| Take 3,4-diaminopyridine with food to reduce GI side effects (nausea, abdominal discomfort) | - | ✓ | ✓ |
| Report any seizures, tingling around the mouth, or numbness in fingers immediately (may indicate 3,4-DAP toxicity) | ✓ | ✓ | ✓ |
| Carry LEMS medical alert identification at all times (anesthesia and medication precautions critical) | ✓ | ✓ | ✓ |
| Provide LEMS medication list to ALL healthcare providers (emergency, dental, surgical) - many medications worsen neuromuscular junction disorders | ✓ | ✓ | ✓ |
| Attend ALL scheduled cancer screening appointments even if feeling well (cancer may develop years after LEMS diagnosis) | - | ✓ | ✓ |
| Report any new cough, weight loss, fatigue, chest pain, or hemoptysis immediately (may indicate lung cancer) | ✓ | ✓ | ✓ |
| Rise slowly from sitting or lying position to avoid falls from orthostatic hypotension (stand at bed/chair edge for 30 seconds before walking) | - | ✓ | ✓ |
| Increase fluid and salt intake to help manage orthostatic hypotension from autonomic dysfunction (unless restricted by other conditions) | - | ✓ | ✓ |
| Plan activities for times of best strength; use energy conservation techniques; rest between tasks | - | ✓ | ✓ |
| Do NOT stop immunosuppressant medications abruptly without physician guidance (disease flare risk) | - | ✓ | ✓ |
| Avoid extreme heat, hot baths, and saunas (may worsen weakness) | - | ✓ | ✓ |
| Report excessive dry mouth, constipation, or urinary symptoms to neurologist (autonomic dysfunction may require treatment adjustment) | - | ✓ | ✓ |
| Avoid alcohol (potentiates weakness and interacts with medications) | - | ✓ | ✓ |
| Understand that LEMS symptoms may improve if underlying cancer is successfully treated (for P-LEMS patients) | - | ✓ | ✓ |
| Stop smoking immediately if current smoker (reduces cancer risk and may slow disease progression) | ✓ | ✓ | ✓ |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Smoking cessation mandatory given strong association between LEMS, SCLC, and tobacco use (reduces ongoing cancer risk) | ✓ | ✓ | ✓ |
| Low-impact exercise (swimming, stationary bike, yoga) to maintain strength and mobility without overexertion given proximal weakness | - | ✓ | ✓ |
| Energy conservation with scheduled rest periods to manage fatigue and optimize function throughout the day | - | ✓ | ✓ |
| Home safety evaluation to remove fall hazards given proximal leg weakness and orthostatic hypotension (secure rugs, install grab bars, adequate lighting) | - | ✓ | ✓ |
| Compression stockings (waist-high, 30-40 mmHg) for orthostatic hypotension management from autonomic dysfunction | - | ✓ | ✓ |
| Elevate head of bed 10-20 degrees to reduce nocturnal supine hypertension while managing orthostatic hypotension | - | ✓ | ✓ |
| Increase dietary fluid intake to 2-3 L/day and liberal salt intake (unless contraindicated) for orthostatic hypotension | - | ✓ | ✓ |
| High-fiber diet with adequate hydration for constipation management from autonomic dysfunction | - | ✓ | ✓ |
| Regular dental care and oral hygiene given xerostomia (dry mouth) from autonomic dysfunction (increased caries risk) | - | - | ✓ |
| Vitamin D supplementation if deficient (1000-2000 IU daily) to support immune function and bone health, especially if on chronic steroids | - | ✓ | ✓ |
| Calcium supplementation (1000-1200 mg daily) if on chronic corticosteroids for bone protection | - | ✓ | ✓ |
| Annual influenza vaccination (inactivated form) and COVID-19 vaccination as recommended; avoid live vaccines if on immunosuppression | - | ✓ | ✓ |
| Aspiration precautions including thickened liquids and chin tuck positioning if dysphagia present from bulbar involvement | - | ✓ | ✓ |

### 4D. Medications to Avoid or Use with Caution in LEMS

| Medication/Class | Risk Level | Details | Safe Alternative (if applicable) |
|------------------|:----------:|---------|----------------------------------|
| **NEUROMUSCULAR BLOCKING AGENTS** |
| Succinylcholine | HIGH | Unpredictable response in LEMS; may have prolonged block | Non-depolarizing agents at markedly reduced dose with sugammadex available |
| Non-depolarizing NM blockers (vecuronium, rocuronium, pancuronium) | HIGH | Exaggerated and prolonged response; use 1/10 to 1/5 normal dose if absolutely necessary | Sugammadex for reversal of rocuronium; neuromuscular monitoring with TOF mandatory |
| **ANTIBIOTICS** |
| Aminoglycosides (gentamicin, tobramycin, amikacin) | HIGH | Impair presynaptic ACh release; can precipitate respiratory failure | Non-aminoglycoside antibiotics based on culture sensitivity |
| Fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin) | HIGH | NMJ blocking effect; FDA warning for neuromuscular disorders | Beta-lactams, cephalosporins (generally safe) |
| Macrolides (azithromycin, erythromycin) | MODERATE | Reports of NMJ worsening | Penicillins, cephalosporins |
| Polymyxins (colistin) | HIGH | Strong NMJ blocking effect | Alternative per culture sensitivity |
| **CARDIOVASCULAR** |
| Beta-blockers (propranolol, metoprolol) | MODERATE | May worsen weakness; impair NMJ transmission; worsen orthostatic hypotension | ACE inhibitors, ARBs |
| Calcium channel blockers (verapamil, diltiazem) | HIGH | Directly antagonize VGCC; may significantly worsen LEMS by further reducing calcium influx at nerve terminal | Amlodipine (lower risk); ACE inhibitors; avoid verapamil/diltiazem specifically |
| Magnesium sulfate IV | HIGH | Inhibits presynaptic ACh release; can precipitate crisis | Avoid except life-threatening hypomagnesemia; ICU monitoring required |
| **ANESTHETIC** |
| Volatile anesthetics (isoflurane, sevoflurane) | MODERATE | May potentiate NMJ blockade | TIVA (total intravenous anesthesia) preferred |
| **IMMUNE/CHECKPOINT** |
| Immune checkpoint inhibitors (nivolumab, pembrolizumab, ipilimumab) | HIGH | May worsen paraneoplastic neurological syndromes; can trigger myasthenic crisis; use only with joint neuro-oncology management | If required for cancer treatment, close neuromuscular monitoring mandatory |
| **OTHER** |
| Botulinum toxin | HIGH | Blocks presynaptic ACh release; CONTRAINDICATED in LEMS | Physical therapy; oral medications for spasticity |
| Quinine/tonic water | MODERATE | NMJ blocking effect | Avoid quinine-containing beverages |

*Note: LEMS patients are exquisitely sensitive to neuromuscular blocking agents due to presynaptic defect. ALL anesthesia providers must be informed of LEMS diagnosis before any surgical procedure. Calcium channel blockers (especially verapamil and diltiazem) are particularly dangerous in LEMS as they directly worsen the underlying pathophysiology.*

---

═══════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Myasthenia Gravis (MG) | Fatigable weakness that WORSENS with exertion (opposite of LEMS); ptosis and diplopia prominent (rare in LEMS); normal or brisk reflexes; no autonomic dysfunction; no cancer association (except thymoma) | AChR/MuSK antibodies positive; RNS shows decrement at low-rate WITHOUT significant increment at high-rate; CMAP amplitudes normal at rest |
| Botulism | Acute onset descending paralysis; dilated/fixed pupils; recent ingestion of contaminated food or wound; autonomic dysfunction present; NO prior NMJ disease | Stool/serum botulinum toxin assay; EMG shows BSAP pattern with incremental response similar to LEMS but acute onset |
| Polymyositis/Dermatomyositis | Proximal weakness without fatigability; elevated CK (often >1000); skin findings in DM (heliotrope rash, Gottron papules); no autonomic dysfunction; no NMJ abnormalities on RNS | CK; myositis antibody panel; EMG shows myopathic pattern (no NMJ findings); muscle biopsy |
| Inclusion Body Myositis (IBM) | Slowly progressive; finger flexor and quadriceps weakness (asymmetric); no autonomic dysfunction; older males; no NMJ findings | CK mildly elevated; EMG shows mixed myopathic/neurogenic pattern; muscle biopsy (rimmed vacuoles); anti-cN1A antibody |
| Motor Neuron Disease (ALS) | Progressive weakness with fasciculations; UMN signs (hyperreflexia, Babinski); no autonomic dysfunction; no fatigability pattern; EMG shows active denervation | EMG/NCS: active denervation, fasciculations, normal NMJ studies; no VGCC antibodies |
| Chronic Inflammatory Demyelinating Polyneuropathy (CIDP) | Progressive proximal and distal weakness; hyporeflexia/areflexia (but NO post-exercise facilitation); sensory involvement prominent; elevated CSF protein | NCS: demyelinating pattern; CSF protein elevated; no VGCC antibodies; no RNS increment |
| Guillain-Barre Syndrome (GBS) | Acute ascending weakness; areflexia; post-infectious; no autonomic facilitation; respiratory failure more common | CSF albuminocytologic dissociation; NCS: demyelinating or axonal pattern; no VGCC antibodies |
| Hypothyroid myopathy | Proximal weakness with myalgias; delayed relaxation of reflexes (NOT facilitation); fatigue; weight gain; cold intolerance | TSH elevated; free T4 low; CK may be elevated; EMG non-specific; no NMJ findings |
| Addison disease | Fatigue and weakness; orthostatic hypotension; hyperpigmentation; electrolyte abnormalities (hyperkalemia, hyponatremia); weight loss | Morning cortisol; ACTH stimulation test; electrolytes; no NMJ findings |
| Primary autonomic failure (MSA, PAF) | Prominent autonomic dysfunction; orthostatic hypotension; urinary dysfunction; NO proximal weakness pattern; NO NMJ findings on RNS | Autonomic function testing; brain MRI (MSA: hot cross bun sign); no VGCC antibodies; normal RNS |
| Congenital Myasthenic Syndromes (CMS) | Childhood onset; family history; seronegative; specific gene mutations; may have presynaptic, synaptic, or postsynaptic defect | Genetic testing (CMS gene panel); no VGCC antibodies; specific RNS patterns depend on CMS type |
| Spinal muscular atrophy (SMA) | Proximal weakness; areflexia; childhood or adult onset; fasciculations; no autonomic dysfunction; no NMJ findings | Genetic testing (SMN1 deletion); EMG shows anterior horn cell disease pattern; no VGCC antibodies |
| Paraneoplastic cerebellar degeneration | Ataxia rather than proximal weakness; may coexist with LEMS in ~15% of cases; anti-Purkinje cell antibodies | PCA-Tr/DNER, Yo, Hu antibodies; brain MRI showing cerebellar atrophy; VGCC may be positive (overlap) |
| Drug-induced neuromuscular blockade | Temporal correlation with offending medication (aminoglycosides, calcium channel blockers); reversible on drug withdrawal | Drug history review; NMJ studies normalize after drug discontinuation; no VGCC antibodies |

---

## 6. MONITORING PARAMETERS

### 6A. Acute Monitoring (ED / Inpatient / ICU)

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Forced vital capacity (FVC) | Q4-6h in acute; Q shift if stable | >20 mL/kg (>1.5 L) | If <15 mL/kg or <1 L: ICU transfer and prepare for intubation; respiratory failure less common in LEMS than MG but can occur | STAT | STAT | - | STAT |
| Negative inspiratory force (NIF/MIP) | Q4-6h in acute; Q shift if stable | More negative than -40 cm H2O | If weaker than -20 cm H2O: intubation consideration; ICU monitoring | STAT | STAT | - | STAT |
| Oxygen saturation (SpO2) | Continuous in acute | >94% | Supplemental O2; BiPAP; intubation if declining | STAT | STAT | - | STAT |
| Orthostatic vital signs | Q shift; daily when stable | No drop >20 systolic or >10 diastolic | Increase IV fluids; add midodrine; compression stockings; hold offending medications | STAT | ROUTINE | - | STAT |
| Blood pressure | Q shift; more frequent during PLEX | <160/100 mmHg | Antihypertensives PRN; adjust autonomic medications | STAT | ROUTINE | - | STAT |
| Neurologic exam (LEMS-specific: proximal strength, reflexes with post-exercise check) | Q shift inpatient; BID in ICU | Stable or improving strength; document Lambert sign | If worsening: reassess 3,4-DAP dose; consider IVIg/PLEX; evaluate for cancer progression | STAT | ROUTINE | - | STAT |
| Swallow function assessment | Daily; each meal if bulbar symptoms | Safe oral intake | NPO if aspiration risk; modified diet; SLP consult | URGENT | URGENT | - | URGENT |
| ECG monitoring | At baseline; after 3,4-DAP dose changes | QTc <500 ms; no arrhythmia | Hold 3,4-DAP if QTc prolongation; cardiology consult for arrhythmia | STAT | ROUTINE | - | STAT |
| Blood glucose | Q6h during IV/high-dose steroids | <180 mg/dL | Insulin sliding scale | STAT | ROUTINE | - | STAT |
| Electrolytes (K, Mg, Ca, Phos) | Daily while acute | Normal ranges | Replace aggressively; calcium homeostasis especially important in LEMS | STAT | ROUTINE | - | STAT |
| Temperature | Q shift | Afebrile | Infection workup if febrile (infection can worsen LEMS) | STAT | ROUTINE | - | STAT |
| I/O and daily weight | Daily (inpatient) | Euvolemic | Adjust fluids; consider autonomic contribution to dysregulation | - | ROUTINE | - | ROUTINE |

### 6B. Chronic/Outpatient Monitoring

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| VGCC antibody titer | Every 6-12 months | Declining or stable titer | Rising titer: reassess cancer screening; consider treatment escalation | - | - | ROUTINE | - |
| CT chest (cancer screening) | Every 6 months for 2 years; then annually for 2 more years | No new lesion or mass | Immediate oncology referral; biopsy; staging workup | - | - | ROUTINE | - |
| PET/CT (if DELTA-P >=3 and initial negative) | Every 6 months for 2 years | No FDG-avid lesion | Oncology referral; biopsy | - | - | ROUTINE | - |
| Proximal muscle strength testing (MRC grading) | Each clinic visit | Stable or improving | Treatment escalation; reassess 3,4-DAP dose; consider immunotherapy adjustment | - | - | ROUTINE | - |
| Autonomic symptom assessment (dry mouth, constipation, orthostasis, ED) | Each clinic visit | Stable or improving symptoms | Adjust symptomatic medications; consider 3,4-DAP dose optimization | - | - | ROUTINE | - |
| Orthostatic vital signs | Each clinic visit | No significant orthostatic drop | Adjust midodrine/fludrocortisone; increase fluids/salt; compression stockings | - | - | ROUTINE | - |
| FVC (office spirometry) | Each visit initially; q3-6 months when stable | >80% predicted | Pulmonology referral if declining; reassess treatment | - | - | ROUTINE | - |
| ECG (QTc monitoring) | At baseline; after 3,4-DAP dose changes; annually | QTc <500 ms | Hold/reduce 3,4-DAP if QTc prolonging; cardiology consult | - | - | ROUTINE | - |
| CBC with differential | Q2-4 weeks during immunosuppressant titration; then q3 months | WBC >3000; ANC >1500 | Hold/reduce immunosuppressant if cytopenic | - | - | ROUTINE | - |
| LFTs | Q2-4 weeks during immunosuppressant titration; then q3 months | AST/ALT <3x ULN | Reduce or hold offending agent; hepatology referral if persistent | - | - | ROUTINE | - |
| Renal function (BUN/Cr) | Q3 months on cyclosporine; q6 months otherwise | Normal eGFR | Dose adjustment; avoid nephrotoxins | - | - | ROUTINE | - |
| Fasting glucose / HbA1c | Q3 months while on steroids | HbA1c <7% | Endocrinology referral; steroid dose reduction | - | - | ROUTINE | - |
| DEXA scan (bone density) | Baseline if starting chronic steroids; repeat q2 years | T-score > -1.0 | Bisphosphonate; calcium/vitamin D | - | - | ROUTINE | - |
| Immunoglobulin levels (IgG, IgA, IgM) | Q6 months if on rituximab/chronic immunosuppression | IgG >400 mg/dL | IVIg replacement if symptomatic hypogammaglobulinemia | - | - | ROUTINE | - |
| CD19/CD20 B-cell counts (if on rituximab) | Q3-6 months | Depleted B-cells; monitor recovery | Redose rituximab when B-cells recover and symptoms worsen | - | - | ROUTINE | - |
| Weight monitoring | Each clinic visit | Stable weight; no unexplained loss | Unexplained weight loss >5%: repeat cancer screening urgently | - | - | ROUTINE | - |
| Depression/anxiety screening (PHQ-9, GAD-7) | Each clinic visit | Minimal symptoms | Psychiatry referral; consider SSRI (safe in LEMS) | - | - | ROUTINE | - |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **Discharge home** | Mild symptoms; stable on 3,4-DAP; adequate oral intake; no respiratory compromise (FVC >60% predicted); cancer screening plan in place; reliable follow-up within 1-2 weeks; understands return precautions |
| **Admit to floor (general neurology)** | New diagnosis requiring expedited workup; moderate proximal weakness limiting ambulation; initiating IVIg or immunotherapy; significant autonomic dysfunction requiring stabilization; new cancer diagnosis requiring coordination |
| **Admit to step-down/telemetry** | Declining FVC or NIF trending toward danger zone; moderate-severe orthostatic hypotension with syncope; starting PLEX; cardiac arrhythmias from autonomic dysfunction |
| **Admit to ICU** | FVC <30% predicted or <1 L; NIF weaker than -25 cm H2O; progressive respiratory failure; severe autonomic instability (symptomatic bradycardia, sustained hypotension); concurrent SCLC with acute complications; myasthenic crisis-like presentation |
| **Transfer to higher level** | Neuromuscular specialist not available; PLEX needed but unavailable; ICU capability needed; oncology expertise needed for SCLC management |
| **Discharge from hospital** | FVC stable and improving; adequate oral intake; stable on oral medications; cancer screening/treatment plan in place; outpatient follow-up scheduled within 1-2 weeks; patient and family educated on LEMS management and cancer screening importance |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| P/Q-type VGCC antibodies diagnostic for LEMS (~85-90% sensitivity) | Class I | Lennon VA et al. N Engl J Med 1995; 332:1467-1474 |
| LEMS association with SCLC (~60% paraneoplastic) | Class II | Titulaer MJ et al. J Clin Oncol 2011; 29:902-908 |
| DELTA-P score for paraneoplastic risk stratification | Class II | Titulaer MJ et al. J Neurol Neurosurg Psychiatry 2011; 82:1222-1228 |
| SOX1 antibody as SCLC biomarker in LEMS (~64% sensitivity) | Class II | Titulaer MJ et al. J Neuroimmunol 2009; 210:78-82 |
| Repetitive nerve stimulation: >100% increment at high-rate diagnostic for presynaptic NMJ disorder | Class I | Oh SJ et al. Muscle Nerve 2005; 32:549-556 |
| Low resting CMAP amplitudes as hallmark of LEMS | Class I | Sanders DB. Ann N Y Acad Sci 2003; 998:500-508 |
| Post-exercise facilitation (>100% CMAP increment) equivalent to high-rate RNS | Class II | Oh SJ et al. Muscle Nerve 2005; 32:549-556 |
| 3,4-Diaminopyridine as first-line symptomatic treatment for LEMS | Class I, Level A | Wirtz PW et al. Neurology 2009; 73:1849-1854 |
| 3,4-DAP improves strength and autonomic symptoms in LEMS (randomized controlled trial) | Class I | Oh SJ et al. Muscle Nerve 2009; 40:795-800 |
| Amifampridine (Firdapse) FDA approval for LEMS | Regulatory | FDA approval November 2018; NDA 208078 |
| Pyridostigmine as adjunctive therapy in LEMS (less effective than in MG) | Class III | Tim RW, Sanders DB. Semin Neurol 2004; 24:49-57 |
| IVIg effective for LEMS acute exacerbation | Class I | Bain PG et al. J Neurol Neurosurg Psychiatry 1996; 61:510-515 |
| Plasma exchange for LEMS exacerbation | Class II | Newsom-Davis J, Murray NM. Neurology 1984; 34:480-485 |
| Cancer treatment improves neurological symptoms in P-LEMS | Class II | Chalk CH et al. Neurology 1990; 40:1644-1645 |
| Cancer screening every 6 months for 2 years in LEMS | Consensus | Titulaer MJ et al. J Neurol Neurosurg Psychiatry 2011; 82:1222-1228 |
| PET/CT more sensitive than CT alone for detecting occult SCLC in LEMS | Class II | Titulaer MJ et al. Chest 2011; 139:1187-1193 |
| Azathioprine as steroid-sparing agent in autoimmune LEMS | Class III | Newsom-Davis J. Muscle Nerve 1998; 21:1762-1768 |
| Rituximab for refractory autoimmune LEMS (case series) | Class IV | Maddison P et al. Neurology 2011; 76:474-476 |
| Lambert sign (post-exercise facilitation of reflexes) as clinical hallmark | Class II | Lambert EH, Eaton LM, Rooke ED. Am J Physiol 1956; 187:612-613 |
| Autonomic dysfunction in LEMS (dry mouth, constipation, erectile dysfunction) | Class II | O'Neill JH et al. Brain 1988; 111:577-596 |
| EFNS/PNS guidelines for LEMS management | Consensus | Titulaer MJ et al. Eur J Neurol 2011; 18:486-490 |
| Immune checkpoint inhibitors may worsen paraneoplastic syndromes | Class III | Guidon AC et al. Neurology 2021; 97:e234-e245 |
| Calcium channel blockers particularly dangerous in LEMS (direct pathophysiologic antagonism) | Class III | Sanders DB et al. Neurology 2000; 54:2163-2167 |
| Neuromuscular blocking agent sensitivity in LEMS (1/10 normal dose) | Class II | Baraka A. Can J Anaesth 1992; 39:817-819 |
| FVC and NIF monitoring for respiratory assessment in neuromuscular disease | Class I, Level B | Thomas CE et al. Neurology 1997; 48:1253-1260 |
| Midodrine for orthostatic hypotension management | Class I | Low PA et al. JAMA 1997; 277:1046-1051 |
| 3,4-DAP seizure risk and QTc monitoring requirement | Class II | FDA prescribing information for Firdapse (amifampridine) 2018 |

---

## CHANGE LOG

**v1.1 (January 30, 2026)**
- Standardized all treatment table dosing to structured 4-field format: [dose] :: [route] :: [frequency] :: [full_instructions]
- Fixed PLEX route from "-" to "IV" in sections 3A and 3C (enables order sentence generation)
- Eliminated cross-references in Ruzurgi row ("Same as Firdapse") -- each row now self-contained with full contraindications, monitoring, and indication
- Merged Section 3E (Cancer-Directed Treatment) into Section 3D with Pre-Treatment Requirements column for consistency with standard 3A-3D structure
- Cleaned medication names in Treatment column (removed parenthetical descriptors from column, moved to Indication)
- Fixed dose-tier listings (e.g., "5 mg TID; 10 mg TID; 15 mg TID") to single starting dose in structured format with titration in full_instructions field

**v1.0 (January 30, 2026)**
- Initial creation
- Section 1: 43 laboratory tests across 3 tiers (16 core, 19 extended, 8 rare/specialized)
  - P/Q-type VGCC antibody, SOX1 antibody, N-type VGCC as core diagnostics
  - Comprehensive paraneoplastic antibody panel (ANNA-1, CRMP-5, amphiphysin, Zic4)
  - Tumor markers (NSE, ProGRP, CEA, PSA) for malignancy screening
- Section 2: Imaging and studies across 4 tiers plus bedside tests
  - 2A: CT chest, CXR, PET/CT, ECG as essential
  - 2B: RNS (low-rate and high-rate), post-exercise facilitation, baseline CMAP, EMG/NCS, SFEMG, autonomic testing
  - 2C: Cancer screening protocol (serial CT, PET/CT, bronchoscopy, mammography, colonoscopy)
  - 2D: Bedside tests (Lambert sign, proximal strength, grip, FVC, NIF, orthostatic vitals, pupillary exam, dry mouth)
- Section 3: Treatment across 4 subsections
  - 3A: Acute/emergent (IVIg, PLEX, IV fluids)
  - 3B: Symptomatic (3,4-DAP/amifampridine, pyridostigmine, midodrine, fludrocortisone, GI treatments, artificial tears/saliva, sildenafil)
  - 3C: Second-line (prednisone, maintenance IVIg, maintenance PLEX)
  - 3D: Disease-modifying/immunosuppressive + cancer-directed (azathioprine, mycophenolate, rituximab, cyclosporine, cyclophosphamide, chemotherapy, radiation, checkpoint inhibitors) with Pre-Treatment Requirements
- Section 4: Recommendations across 4 subsections
  - 4A: 17 referrals including oncology, smoking cessation, palliative care
  - 4B: 18 patient instructions with cancer screening emphasis
  - 4C: 13 lifestyle modifications including orthostatic management
  - 4D: Medications to avoid table organized by drug class with LEMS-specific risks
- Section 5: 14 differential diagnoses including MG, botulism, inflammatory myopathies, CIDP, ALS
- Section 6: Monitoring parameters
  - 6A: 12 acute monitoring parameters
  - 6B: 17 chronic monitoring parameters including cancer screening schedule
- Section 7: Disposition criteria (6 levels)
- Section 8: 28 evidence citations
- DELTA-P score reference table included
- LEMS-specific medication avoidance table (calcium channel blockers highlighted as particularly dangerous)
