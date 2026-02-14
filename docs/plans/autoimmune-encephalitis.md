---
title: "Autoimmune Encephalitis"
description: "Clinical decision support for autoimmune encephalitis diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - autoimmune
  - encephalitis
  - neuro-oncology
---

# Autoimmune Encephalitis

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial creation

---

**DIAGNOSIS:** Autoimmune Encephalitis

**ICD-10:** G04.81 (Other autoimmune encephalitis), G04.90 (Encephalitis and encephalomyelitis, unspecified)

**CPT CODES:** 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 84443 (TSH), 85652 (ESR), 86140 (CRP), 87040 (Blood cultures (x2 sets)), 82947 (Blood glucose), 83036 (HbA1c), 82140 (Ammonia), 83605 (Lactate), 83735 (Magnesium), 84100 (Phosphorus), 84145 (Procalcitonin), 84484 (Troponin), 82550 (CPK), 80307 (Urine drug screen), 80320 (Alcohol level), 81025 (Pregnancy test (females of childbearing age)), 83615 (LDH), 86255 (Anti-NMDAR antibody (serum AND CSF)), 86235 (Anti-LGI1 antibody (serum AND CSF)), 70450 (CT head without contrast), 70553 (MRI brain with and without contrast), 95816 (EEG (routine or continuous)), 93000 (ECG (12-lead)), 71046 (Chest X-ray), 78816 (FDG-PET/CT (whole body)), 89051 (Cell count with differential (tubes 1 and 4)), 84157 (Protein), 82945 (Glucose with paired serum glucose), 87529 (HSV 1/2 PCR), 87327 (Cryptococcal antigen), 86592 (VDRL (CSF)), 83916 (Oligoclonal bands (CSF AND paired serum)), 88104 (Cytology), 87116 (AFB culture and smear), 87102 (Fungal culture), 96365 (Methylprednisolone IV)

**SYNONYMS:** Autoimmune encephalitis, AE, anti-NMDA receptor encephalitis, anti-NMDAR encephalitis, limbic encephalitis, antibody-mediated encephalitis, paraneoplastic encephalitis, LGI1 encephalitis, CASPR2 encephalitis, rapid neurocognitive syndrome

**SCOPE:** Diagnostic workup, acute treatment, and long-term management of suspected or confirmed autoimmune encephalitis. Covers antibody-mediated encephalitis (anti-NMDAR, LGI1, CASPR2, GABA-B, AMPA, DPPX, IgLON5, GABA-A, GAD65), first-line immunotherapy, second-line escalation, seizure management, psychiatric symptom management, ICU considerations, tumor screening, and long-term immunosuppression. For infectious encephalitis, use "HSV Encephalitis" template. For paraneoplastic syndromes without encephalitis, use "Paraneoplastic Syndrome" template. For status epilepticus management, use "Status Epilepticus" template.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; infection screen; pre-immunotherapy | Normal |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Metabolic screen; renal/hepatic baseline for immunotherapy | Normal |
| TSH (CPT 84443) | URGENT | ROUTINE | ROUTINE | URGENT | Thyroid encephalopathy mimic; Hashimoto encephalopathy screen | Normal |
| ESR (CPT 85652) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory/vasculitis screen | Normal (<20 mm/hr) |
| CRP (CPT 86140) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory marker; infection screen | Normal |
| Urinalysis with culture (CPT 81003+87086) | STAT | STAT | ROUTINE | STAT | UTI as encephalopathy trigger | Negative |
| Blood cultures (x2 sets) (CPT 87040) | STAT | STAT | - | STAT | Rule out septic encephalopathy | No growth |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Metabolic encephalopathy screen; pre-steroid baseline | Normal |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Glycemic status before high-dose steroids | <5.7% |
| Ammonia (CPT 82140) | STAT | STAT | - | STAT | Hepatic encephalopathy mimic | Normal |
| Lactate (CPT 83605) | STAT | STAT | - | STAT | Sepsis screen; metabolic screen | Normal (<2.0 mmol/L) |
| PT/INR, aPTT (CPT 85610+85730) | STAT | STAT | - | STAT | Coagulopathy screen pre-LP; DIC screen | Normal |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Seizure threshold; metabolic screen | Normal |
| Phosphorus (CPT 84100) | STAT | STAT | - | STAT | Metabolic screen | Normal |
| Procalcitonin (CPT 84145) | URGENT | URGENT | - | URGENT | Distinguish bacterial vs autoimmune etiology | Normal (<0.1 ng/mL) |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Cardiac involvement; autonomic instability assessment | Normal |
| CPK (CPT 82550) | URGENT | URGENT | - | URGENT | Rhabdomyolysis from prolonged seizures/catatonia | Normal |
| Urine drug screen (CPT 80307) | STAT | STAT | - | STAT | Toxic/drug-induced encephalopathy mimic | Negative |
| Alcohol level (CPT 80320) | STAT | STAT | - | STAT | Alcohol-related encephalopathy | Negative |
| Pregnancy test (females of childbearing age) (CPT 81025) | STAT | STAT | ROUTINE | STAT | Eclampsia mimic; treatment planning (teratogenicity) | As applicable |
| Peripheral blood smear | URGENT | URGENT | - | URGENT | TTP/HUS screen if thrombocytopenia | Normal |
| LDH (CPT 83615) | URGENT | ROUTINE | ROUTINE | URGENT | Hemolysis screen; tumor marker | Normal |
| Uric acid | - | ROUTINE | ROUTINE | - | Tumor lysis risk if malignancy suspected | Normal |
| Lipase | STAT | STAT | - | STAT | Pancreatitis-related encephalopathy | Normal |

### 1B. Autoimmune Antibody Panel

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| **Anti-NMDAR antibody (serum AND CSF)** (CPT 86255) | URGENT | URGENT | ROUTINE | URGENT | Most common autoimmune encephalitis; CSF more sensitive than serum; cell-based assay (CBA) preferred | Negative |
| **Anti-LGI1 antibody (serum AND CSF)** (CPT 86235) | URGENT | URGENT | ROUTINE | URGENT | Limbic encephalitis; faciobrachial dystonic seizures (FBDS); hyponatremia | Negative |
| **Anti-CASPR2 antibody (serum AND CSF)** (CPT 86235) | URGENT | URGENT | ROUTINE | URGENT | Limbic encephalitis; Morvan syndrome; neuromyotonia; neuropathic pain | Negative |
| **Anti-GABA-B antibody (serum AND CSF)** | URGENT | URGENT | ROUTINE | URGENT | Limbic encephalitis with prominent seizures; 50% associated with SCLC | Negative |
| **Anti-AMPA antibody (serum AND CSF)** | URGENT | URGENT | ROUTINE | URGENT | Limbic encephalitis; relapsing course; associated with thymoma, lung, breast | Negative |
| **Anti-DPPX antibody (serum AND CSF)** | URGENT | URGENT | ROUTINE | URGENT | Encephalitis with hyperexcitability, GI symptoms, PERM | Negative |
| **Anti-IgLON5 antibody (serum AND CSF)** | - | URGENT | ROUTINE | URGENT | Sleep disorder, bulbar dysfunction, gait instability, tau pathology | Negative |
| **Anti-GABA-A antibody (serum AND CSF)** | - | URGENT | ROUTINE | URGENT | Refractory seizures/status epilepticus; often with thymoma | Negative |
| **Anti-GAD65 antibody (serum AND CSF)** | URGENT | URGENT | ROUTINE | URGENT | Limbic encephalitis, stiff-person spectrum, cerebellar ataxia; high titers (>20 nmol/L) significant | Negative or low titer |
| **Mayo Autoimmune Evaluation - Encephalopathy (serum)** | URGENT | URGENT | ROUTINE | URGENT | Comprehensive panel: NMDAR, LGI1, CASPR2, GABA-B, AMPA, DPPX | All negative |
| **Mayo Autoimmune Evaluation - Encephalopathy (CSF)** | URGENT | URGENT | ROUTINE | URGENT | CSF panel: NMDAR, LGI1, CASPR2, GABA-B, AMPA, DPPX | All negative |
| ANA (CPT 86235) | URGENT | ROUTINE | ROUTINE | URGENT | Lupus cerebritis screen | Negative or low titer |
| Anti-dsDNA | - | ROUTINE | ROUTINE | - | If ANA positive; lupus evaluation | Negative |
| Anti-SSA/SSB (Ro/La) | - | ROUTINE | ROUTINE | - | Sjogren syndrome with CNS involvement | Negative |
| Anti-TPO antibodies | URGENT | ROUTINE | ROUTINE | URGENT | Hashimoto encephalopathy (SREAT) | Negative |
| Anti-thyroglobulin antibodies | URGENT | ROUTINE | ROUTINE | URGENT | Hashimoto encephalopathy (SREAT) | Negative |
| AQP4-IgG (NMO antibody) | - | ROUTINE | ROUTINE | - | NMOSD overlap; cell-based assay preferred | Negative |
| MOG-IgG | - | ROUTINE | ROUTINE | - | MOGAD overlap; ADEM-like presentation | Negative |
| Complement C3, C4 | - | ROUTINE | ROUTINE | - | Lupus; complement-mediated disease | Normal |
| Quantitative immunoglobulins (IgG, IgA, IgM) | - | ROUTINE | ROUTINE | - | Baseline before immunotherapy; IgA deficiency (IVIG contraindication) | Normal |

*Note: ALWAYS send BOTH serum AND CSF for antibody testing. CSF is more sensitive for anti-NMDAR; serum is more sensitive for anti-LGI1 and anti-CASPR2. Cell-based assay (CBA) is gold standard -- avoid ELISA-only testing. Mayo panels preferred for comprehensive evaluation. Results may take 1-3 weeks; do NOT wait for results before starting empiric immunotherapy if clinical suspicion is high.*

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-neuronal nuclear antibody type 1 (ANNA-1/anti-Hu) | - | EXT | EXT | - | Paraneoplastic; SCLC, neuroblastoma | Negative |
| Anti-neuronal nuclear antibody type 2 (ANNA-2/anti-Ri) | - | EXT | EXT | - | Paraneoplastic; breast, SCLC | Negative |
| Anti-CV2/CRMP5 | - | EXT | EXT | - | Paraneoplastic; SCLC, thymoma | Negative |
| Anti-amphiphysin | - | EXT | EXT | - | Paraneoplastic; breast, SCLC; stiff-person overlap | Negative |
| Anti-Ma2/Ta | - | EXT | EXT | - | Paraneoplastic limbic encephalitis; testicular germ cell tumor | Negative |
| Anti-SOX1 | - | EXT | EXT | - | SCLC-associated; Lambert-Eaton overlap | Negative |
| Anti-Kelch-like protein 11 (KLHL11) | - | EXT | EXT | - | Testicular seminoma; brainstem/cerebellar syndrome | Negative |
| Anti-GlyR (glycine receptor) | - | EXT | EXT | - | Progressive encephalomyelitis with rigidity and myoclonus (PERM) | Negative |
| Anti-mGluR5 | - | EXT | EXT | - | Ophelia syndrome; Hodgkin lymphoma | Negative |
| Anti-mGluR1 | - | EXT | EXT | - | Cerebellar ataxia; Hodgkin lymphoma | Negative |
| Anti-neurexin-3-alpha | - | EXT | EXT | - | Rapid-onset encephalitis; seizures; confusion | Negative |
| Anti-D2R (dopamine-2 receptor) | - | EXT | EXT | - | Basal ganglia encephalitis; movement disorders | Negative |
| Paraneoplastic evaluation panel (comprehensive) | - | EXT | EXT | - | If standard panels negative and paraneoplastic suspected | All negative |
| 14-3-3 protein (CSF) | - | EXT | EXT | - | Prion disease mimic; rapidly progressive dementia | Negative |
| RT-QuIC (CSF) | - | EXT | EXT | - | Prion disease exclusion in rapidly progressive cases | Negative |
| Next-generation sequencing (CSF metagenomics) | - | EXT | EXT | - | Occult infection when standard testing negative | No pathogens detected |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediate (ED triage) | Rule out mass, hemorrhage, hydrocephalus | None significant |
| MRI brain with and without contrast (CPT 70553) | URGENT | URGENT | ROUTINE | URGENT | Within 24h | Mesial temporal T2/FLAIR hyperintensity (limbic encephalitis); cortical/subcortical signal changes; leptomeningeal enhancement | GFR <30, gadolinium allergy, pacemaker |
| EEG (routine or continuous) (CPT 95816) | URGENT | URGENT | ROUTINE | STAT | Within 24h; continuous if ICU or altered consciousness | Extreme delta brush (anti-NMDAR); focal/generalized slowing; epileptiform discharges; subclinical seizures | None significant |
| ECG (12-lead) (CPT 93000) | STAT | STAT | ROUTINE | STAT | Immediate | Autonomic dysfunction; arrhythmia; QTc prolongation (medication safety) | None |
| Chest X-ray (CPT 71046) | STAT | STAT | - | STAT | Immediate | Mediastinal mass (thymoma); pulmonary mass (SCLC) | Pregnancy (relative) |
| Continuous telemetry | - | STAT | - | STAT | Continuous in hospital | Arrhythmia from autonomic instability | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI spine (cervical and thoracic) with and without contrast | - | ROUTINE | ROUTINE | ROUTINE | Within 48-72h | Concurrent myelitis; overlap syndromes | GFR <30, gadolinium allergy |
| CT chest/abdomen/pelvis with contrast (CPT 71260+74178) | - | URGENT | ROUTINE | URGENT | Within 48h | Occult malignancy: thymoma, lung cancer, ovarian teratoma, lymphoma | Contrast allergy, renal insufficiency |
| Pelvic/transvaginal ultrasound (females) | - | URGENT | ROUTINE | URGENT | Within 48h | Ovarian teratoma (anti-NMDAR) | None significant |
| Testicular ultrasound (males <50) | - | URGENT | ROUTINE | URGENT | Within 48h | Testicular germ cell tumor (anti-Ma2, KLHL11) | None significant |
| FDG-PET/CT (whole body) (CPT 78816) | - | ROUTINE | ROUTINE | - | Within 1-2 weeks | Occult malignancy not seen on CT; FDG-avid tumor | Uncontrolled diabetes, pregnancy |
| Video-EEG monitoring (prolonged) | - | ROUTINE | ROUTINE | STAT | As needed | Characterize seizure semiology; subclinical seizures; extreme delta brush pattern | None |
| FDG-PET brain | - | EXT | EXT | - | Within 1-2 weeks | Mesial temporal hypermetabolism (early) or hypometabolism (late); cortical metabolic changes | Same as PET/CT |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with epilepsy protocol | - | EXT | EXT | - | If seizures refractory | Subtle cortical lesions; hippocampal sclerosis | Gadolinium contraindications |
| Brain biopsy | - | EXT | - | - | Last resort | Inflammatory infiltrate; exclusion of other pathology | Coagulopathy, inaccessible location |
| CT-guided biopsy (tumor) | - | EXT | EXT | - | After tumor identified | Histopathological confirmation | Coagulopathy, tumor location |
| Mammography/breast MRI | - | ROUTINE | ROUTINE | - | If AMPA, amphiphysin positive | Breast malignancy | Implants (relative for MRI) |
| Polysomnography | - | - | EXT | - | If IgLON5 suspected | REM/NREM parasomnias; sleep disordered breathing | None significant |

### LUMBAR PUNCTURE

**Indication:** Essential for diagnosis of autoimmune encephalitis; supports Graus 2016 criteria (CSF pleocytosis); CSF antibody testing more sensitive than serum for anti-NMDAR; rules out infectious encephalitis

**Timing:** STAT/URGENT -- perform as soon as safely possible after CT head; do NOT delay for MRI

**Volume Required:** 20-30 mL (large volume for comprehensive antibody and infectious testing)

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | URGENT | ROUTINE | ROUTINE | Elevated ICP assessment | 10-20 cm H2O |
| Cell count with differential (tubes 1 and 4) (CPT 89051) | STAT | STAT | ROUTINE | Lymphocytic pleocytosis supports autoimmune | WBC 5-80 (lymphocyte-predominant); RBC 0 |
| Protein (CPT 84157) | STAT | STAT | ROUTINE | Mildly elevated in autoimmune; markedly elevated suggests infection/GBS | Normal to mildly elevated (usually <100 mg/dL) |
| Glucose with paired serum glucose (CPT 82945) | STAT | STAT | ROUTINE | Low in infection/carcinomatous meningitis | Normal (>60% of serum) |
| Gram stain and bacterial culture (CPT 87205+87070) | STAT | STAT | ROUTINE | Rule out bacterial meningitis | No organisms |
| HSV 1/2 PCR (CPT 87529) | STAT | STAT | ROUTINE | Rule out HSV encephalitis (most important mimic) | Negative |
| VZV PCR | URGENT | URGENT | ROUTINE | Varicella encephalitis | Negative |
| EBV PCR | - | ROUTINE | ROUTINE | EBV-associated encephalitis; lymphoma screen | Negative |
| CMV PCR | - | ROUTINE | ROUTINE | Immunocompromised patients | Negative |
| HHV-6 PCR | - | ROUTINE | ROUTINE | Post-transplant; limbic encephalitis mimic | Negative |
| Enterovirus PCR | URGENT | URGENT | - | Viral meningitis/encephalitis | Negative |
| West Nile virus IgM/IgG | - | ROUTINE | - | Endemic areas; flaccid paralysis | Negative |
| Cryptococcal antigen (CPT 87327) | URGENT | ROUTINE | - | Immunocompromised; chronic meningitis | Negative |
| VDRL (CSF) (CPT 86592) | - | ROUTINE | ROUTINE | Neurosyphilis | Negative |
| Oligoclonal bands (CSF AND paired serum) (CPT 83916) | URGENT | ROUTINE | ROUTINE | Intrathecal IgG synthesis; MS/NMOSD overlap | May show CSF-specific bands |
| IgG index | URGENT | ROUTINE | ROUTINE | Intrathecal antibody synthesis | May be elevated |
| Cytology (CPT 88104) | - | ROUTINE | ROUTINE | Carcinomatous/lymphomatous meningitis | Negative |
| Flow cytometry | - | ROUTINE | ROUTINE | CNS lymphoma | Normal |
| **Autoimmune encephalitis antibody panel (CSF)** | URGENT | URGENT | ROUTINE | NMDAR, LGI1, CASPR2, GABA-B, AMPA, DPPX -- CBA method | All negative |
| **Anti-NMDAR IgG (CSF)** | URGENT | URGENT | ROUTINE | CSF more sensitive than serum for NMDAR | Negative |
| AFB culture and smear (CPT 87116) | - | ROUTINE | - | TB meningitis if risk factors | Negative |
| Fungal culture (CPT 87102) | - | ROUTINE | - | Immunocompromised | Negative |

**Special Handling:** Send minimum 2 mL CSF to each reference lab. Anti-NMDAR CSF testing is more sensitive than serum -- ALWAYS send CSF. Antibody results take 1-3 weeks. Cytology requires rapid transport (<1 hour). Store extra CSF (frozen at -20C) for future testing.

**Contraindications:** Elevated ICP without imaging (get CT first), coagulopathy (INR >1.5, platelets <50K), skin infection at LP site, posterior fossa mass with risk of herniation

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Empiric acyclovir IV (until HSV ruled out) | IV | Suspected viral encephalitis; HSV not yet excluded | 10 mg/kg :: IV :: q8h :: 10 mg/kg IV q8h; continue until HSV PCR negative x2 (48h apart) or alternative diagnosis confirmed | Renal impairment (adjust dose); adequate hydration required | Renal function daily; hydration status; crystal nephropathy prevention | STAT | STAT | - | STAT |
| Empiric antibiotics (if bacterial meningitis not excluded) | IV | Bacterial meningitis not yet excluded | 2g :: IV :: q12h :: Ceftriaxone 2g IV q12h + vancomycin 15-20 mg/kg IV q8-12h + dexamethasone 0.15 mg/kg q6h x 4 days | Per individual drug allergies | Cultures; clinical response; renal function; vancomycin troughs | STAT | STAT | - | STAT |
| Lorazepam (acute seizure) | IV | Active seizure; acute seizure termination | 0.1 mg/kg :: IV :: - :: 0.1 mg/kg IV (max 4 mg/dose); may repeat x1 in 5 minutes | Respiratory depression; acute narrow-angle glaucoma | Respiratory status; sedation level; airway patency | STAT | STAT | - | STAT |
| Midazolam (if no IV access) | IV | Active seizure; no IV access available | 10 mg :: IM :: - :: 10 mg IM (adults >40 kg) or 0.2 mg/kg intranasal | Respiratory depression | Same as lorazepam | STAT | STAT | - | STAT |
| Lorazepam (catatonia challenge) | IV | Suspected catatonia; diagnostic challenge test | 1-2 mg :: IV :: - :: 1-2 mg IV; observe 15-30 min for response; if improvement, continue 1-2 mg IV/PO q4-8h (up to 8-24 mg/day) | Respiratory compromise; prior paradoxical response | Bush-Francis Catatonia Rating Scale; respiratory status; sedation | STAT | STAT | - | STAT |

*Note: Initiate empiric acyclovir and antibiotics IMMEDIATELY. Do NOT delay antimicrobials for LP. Start immunotherapy as soon as autoimmune encephalitis is clinically suspected -- do NOT wait for antibody results.*

### 3B. First-Line Immunotherapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Methylprednisolone IV (CPT 96365) | IV | Suspected or confirmed autoimmune encephalitis; first-line immunotherapy | 1000 mg :: IV :: daily :: 1000 mg IV daily x 5 days; infuse over 1-2 hours | Active untreated infection; uncontrolled diabetes; psychosis from steroids | Glucose q6h (target <180); BP; mood/sleep; I/O; GI prophylaxis | URGENT | STAT | - | STAT |
| Omeprazole (GI prophylaxis during steroids) | IV | GI prophylaxis during high-dose IV steroids | 40 mg :: IV :: daily :: 40 mg IV/PO daily during steroid course | PPI allergy | None routine | URGENT | STAT | - | STAT |
| Insulin sliding scale | SC/IV | Steroid-induced hyperglycemia >180 mg/dL | 180 mg :: - :: - :: Per protocol if glucose >180 mg/dL | Hypoglycemia risk | Glucose q6h; adjust per response | URGENT | STAT | - | STAT |
| IVIG (intravenous immunoglobulin) (CPT 96365) | IV | Suspected or confirmed AE; first-line immunotherapy (with steroids) | 0.4 g/kg :: IV :: daily x 5 days :: 0.4 g/kg/day IV x 5 days (total 2 g/kg); infuse per weight-based protocol; premedicate with acetaminophen, diphenhydramine | IgA deficiency (anaphylaxis risk); recent thromboembolic event; renal failure | Renal function daily; headache (aseptic meningitis); thrombosis; volume overload; check IgA level before first dose | - | STAT | - | STAT |
| Plasmapheresis (PLEX) | - | Suspected or confirmed AE; first-line immunotherapy; rapid deterioration | N/A :: - :: once :: 5-7 exchanges over 10-14 days; 1-1.5 plasma volumes per exchange; albumin replacement | Hemodynamic instability; sepsis; coagulopathy; poor vascular access | BP during exchanges; electrolytes (Ca, K, Mg); coagulation (fibrinogen); line site; citrate reactions | - | STAT | - | STAT |

*Note: Methylprednisolone is typically started first (often in combination with IVIG or PLEX). IVIG and PLEX are considered equivalent first-line therapies and should be started concurrently or within days of steroids if clinical suspicion is high. For anti-NMDAR encephalitis, combination of all three first-line agents is common. PLEX may be preferred if rapid deterioration; IVIG may be preferred if hemodynamic instability or vascular access issues.*

### 3C. Second-Line Immunotherapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Rituximab | IV | AE refractory to first-line immunotherapy; anti-NMDAR encephalitis (early escalation) | 375 mg/m2 :: IV :: - :: 375 mg/m2 IV weekly x 4 doses OR 1000 mg IV x 2 doses (day 0 and day 14); premedicate with methylprednisolone 100 mg, acetaminophen, diphenhydramine | Active hepatitis B; severe active infection; live vaccines within 4 weeks | Hepatitis B serology (before first dose); CBC with differential q2-4 weeks; immunoglobulin levels q3 months; CD19/CD20 B-cell counts; infusion reactions; PML surveillance | - | URGENT | ROUTINE | URGENT |
| Cyclophosphamide | IV | AE refractory to first-line; alternative to rituximab | 750 mg/m2 :: IV :: monthly :: 750 mg/m2 IV monthly x 6 cycles; pre-hydrate with 1L NS; administer with MESNA (uroprotection) | Pregnancy; active infection; bone marrow failure; bladder outlet obstruction | CBC weekly x 4 weeks after each cycle (nadir day 10-14); urinalysis; BMP; LFTs; fertility counseling; hemorrhagic cystitis prevention | - | URGENT | ROUTINE | URGENT |
| Tocilizumab (third-line) | IV | Refractory AE failing rituximab/cyclophosphamide; third-line | 8 mg/kg :: IV :: - :: 8 mg/kg IV every 4 weeks (max 800 mg/dose) | Active infection; hepatic impairment (ALT >5x ULN); diverticulitis; concurrent live vaccines | CBC, LFTs, lipids q4-8 weeks; infection surveillance; GI perforation risk; neutropenia | - | EXT | EXT | EXT |
| Bortezomib (third-line) | IV | Refractory AE failing rituximab/cyclophosphamide; third-line | 1.3 mg/m2 :: IV :: - :: 1.3 mg/m2 SC/IV on days 1, 4, 8, 11 of 21-day cycles x 4-6 cycles | Severe hepatic impairment; peripheral neuropathy grade 2+ | CBC; peripheral neuropathy assessment (dose-reduce or hold if worsens); herpes zoster prophylaxis (acyclovir 400 mg BID) | - | EXT | EXT | EXT |
| Repeated IVIG or PLEX cycles | IV | Ongoing AE; maintenance or bridging to second-line agent | 0.4 g/kg :: PO :: daily x 5 days :: IVIG 0.4 g/kg/day x 5 days (repeat q4 weeks) or PLEX 5 exchanges (repeat as needed) | Same as first-line | Same as first-line | - | URGENT | ROUTINE | URGENT |
| Oral prednisone taper (following IV methylprednisolone) | PO | Post-IV methylprednisolone taper; ongoing immunosuppression | 1 mg/kg :: PO :: - :: 1 mg/kg/day (max 60 mg) x 2 weeks; taper by 10 mg/week to 20 mg; then taper by 5 mg/week to discontinuation OR low-dose maintenance | Active infection; uncontrolled diabetes; avascular necrosis | Glucose; BP; bone density if prolonged; mood; weight; adrenal insufficiency on taper | - | ROUTINE | ROUTINE | - |

*Note: Second-line therapy should be initiated if no improvement within 2 weeks of first-line therapy OR if clinically worsening despite first-line treatment. For anti-NMDAR encephalitis, early escalation to rituximab is associated with improved outcomes. Rituximab is generally preferred over cyclophosphamide given better safety profile. Third-line agents (tocilizumab, bortezomib) reserved for refractory cases failing rituximab/cyclophosphamide.*

### 3D. Seizure Management

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Levetiracetam (first-line ASM) | IV | Seizures in autoimmune encephalitis; first-line ASM | 1000-1500 mg :: IV :: BID :: Load: 1000-1500 mg IV; Maintenance: 500-1500 mg IV/PO BID (max 3000 mg/day) | - | Renal impairment (adjust dose per CrCl) | Behavioral changes (rage, irritability); suicidality; renal function | STAT | STAT | ROUTINE | STAT |
| Lacosamide (second-line ASM) | IV | Seizures refractory to levetiracetam; second-line ASM | 200-400 mg :: IV :: BID :: Load: 200-400 mg IV; Maintenance: 100-200 mg IV/PO BID (max 400 mg/day) | - | Second/third degree AV block; severe hepatic impairment | ECG (PR prolongation); dizziness; cardiac monitoring during load | URGENT | URGENT | ROUTINE | URGENT |
| Valproic acid | IV | Refractory seizures; broad-spectrum ASM | 20-40 mg/kg :: IV :: q8h :: Load: 20-40 mg/kg IV (max rate 6 mg/kg/min); Maintenance: 250-500 mg IV/PO q8h (target level 50-100 mcg/mL) | - | Pregnancy (teratogenic -- Category X); hepatic disease; urea cycle disorders; mitochondrial disease (POLG) | LFTs; ammonia; CBC (thrombocytopenia); drug level; pancreatitis | URGENT | URGENT | ROUTINE | URGENT |
| Brivaracetam | IV | Seizures refractory to levetiracetam; SV2A alternative | 100 mg :: IV :: BID :: Load: 100 mg IV; Maintenance: 50-100 mg IV/PO BID (max 200 mg/day) | - | Hepatic impairment (reduce dose) | Behavioral changes; sedation | - | URGENT | ROUTINE | URGENT |
| Clobazam | PO | Adjunctive seizure control; refractory focal seizures | 5-10 mg :: PO :: BID :: Start 5-10 mg BID; titrate to 20-40 mg/day in divided doses | - | Severe hepatic impairment; myasthenia gravis | Sedation; CYP2C19 poor metabolizers (reduce dose); tolerance; dependence | - | ROUTINE | ROUTINE | ROUTINE |
| Phenytoin/fosphenytoin (refractory) | IV | Refractory seizures; status epilepticus | 20 mg :: IV :: BID :: Fosphenytoin: 20 mg PE/kg IV (max rate 150 mg PE/min); Maintenance: 5-7 mg/kg/day divided BID-TID (target level 10-20 mcg/mL) | - | AV block; bradycardia | Continuous cardiac monitoring during load; drug level; purple glove syndrome (peripheral IV); gingival hyperplasia | STAT | STAT | - | STAT |
| Phenobarbital (refractory) | IV | Refractory seizures not responding to other ASMs | 15-20 mg/kg :: IV :: - :: Load: 15-20 mg/kg IV (max rate 60 mg/min); Maintenance: 1-3 mg/kg/day (target level 15-40 mcg/mL) | - | Severe respiratory depression; porphyria | Respiratory depression; sedation; hypotension; drug level | - | URGENT | - | URGENT |
| Midazolam infusion (refractory SE) | IV | Refractory status epilepticus requiring ICU | 0.2 mg/kg :: IV :: once :: Bolus: 0.2 mg/kg IV; Infusion: 0.1-2.0 mg/kg/hr; titrate to EEG burst suppression | - | Unprotected airway (requires intubation) | Continuous EEG; respiratory status; hemodynamics; tachyphylaxis | - | - | - | STAT |
| Propofol infusion (refractory SE) | IV | Refractory status epilepticus requiring ICU | 1-2 mg/kg :: IV :: once :: Bolus: 1-2 mg/kg IV; Infusion: 20-80 mcg/kg/min (max 5 mg/kg/hr to avoid PRIS) | - | Propofol infusion syndrome risk (prolonged use >48h at high doses); egg/soy allergy | Continuous EEG; triglycerides q48h; CPK; lactate; hemodynamics; PRIS surveillance | - | - | - | STAT |
| Ketamine infusion (super-refractory SE) | IV | Super-refractory status epilepticus | 1-3 mg/kg :: IV :: once :: Bolus: 1-3 mg/kg IV; Infusion: 0.5-5 mg/kg/hr | - | Uncontrolled hypertension; raised ICP (relative) | Continuous EEG; BP; HR; hepatic function; laryngospasm risk | - | - | - | STAT |

*Note: Seizures in autoimmune encephalitis are driven by antibody-mediated mechanisms -- immunotherapy is the definitive seizure treatment. ASMs control acute seizures but will not resolve the underlying cause. Avoid carbamazepine/oxcarbazepine in LGI1 encephalitis (may worsen hyponatremia). Levetiracetam and lacosamide are preferred first-line ASMs given favorable drug interaction profiles with immunotherapy.*

### 3E. Psychiatric Symptom Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Haloperidol (acute agitation) | IV | Acute severe agitation; psychosis requiring immediate control | 0.5-2 mg :: IV :: PRN :: 0.5-2 mg IV/IM q4-6h PRN (lowest effective dose); max 20 mg/day | QTc >500 ms; Parkinson disease; prior NMS | ECG (QTc); EPS; NMS surveillance; temperature; CPK if NMS suspected | STAT | STAT | - | STAT |
| Olanzapine (agitation/psychosis) | IM | Psychosis or agitation; oral/IM management | 2.5-5 mg :: IM :: BID :: 2.5-5 mg PO/IM BID (start low); max 20 mg/day | QTc prolongation; metabolic syndrome | Glucose; lipids; QTc; weight; sedation; EPS | - | ROUTINE | ROUTINE | ROUTINE |
| Quetiapine (psychosis/insomnia) | PO | Psychosis; insomnia with psychiatric features | 25-50 mg :: PO :: qHS :: Start 25-50 mg qHS; titrate to 200-400 mg/day in divided doses | QTc prolongation; severe hepatic impairment | QTc; metabolic parameters; orthostatic BP; sedation | - | ROUTINE | ROUTINE | - |
| Lorazepam (catatonia -- first-line) | IV | Catatonia (first-line treatment); agitation in AE | 1-2 mg :: IV :: - :: Start 1-2 mg IV/PO; if response, 1-2 mg q4-8h (escalate to 8-24 mg/day as needed for catatonia) | Respiratory compromise (high doses) | Bush-Francis Catatonia Rating Scale; respiratory rate; sedation; airway | STAT | STAT | ROUTINE | STAT |
| Dexmedetomidine (agitation in ICU) | IV | ICU agitation; non-GABAergic sedation | 1 mcg/kg :: IV :: - :: Load: 1 mcg/kg IV over 10 min (optional); Infusion: 0.2-0.7 mcg/kg/hr (max 1.5 mcg/kg/hr) | Severe bradycardia; advanced heart block | HR (bradycardia); BP (hypotension); sedation level (RASS) | - | - | - | STAT |
| Valproic acid (mood stabilization/agitation) | PO | Mood instability; agitation with concurrent seizure risk | 250-500 mg :: PO :: BID :: 250-500 mg PO BID; titrate to level 50-100 mcg/mL (dual benefit: mood + seizure) | Pregnancy; hepatic disease | LFTs; ammonia; CBC; drug level | - | ROUTINE | ROUTINE | ROUTINE |
| Melatonin (sleep-wake disturbance) | PO | Sleep-wake cycle disturbance; circadian disruption | 3-10 mg :: PO :: qHS :: 3-10 mg PO qHS | None significant | Sleep quality; no significant drug interactions | - | ROUTINE | ROUTINE | ROUTINE |
| Trazodone (insomnia) | PO | Insomnia refractory to melatonin | 25-100 mg :: PO :: qHS :: 25-100 mg PO qHS | Concurrent MAOIs; QTc prolongation | Orthostatic hypotension; priapism (rare); sedation | - | ROUTINE | ROUTINE | - |
| Electroconvulsive therapy (ECT) (refractory catatonia) | - | Refractory catatonia not responding to lorazepam | N/A :: - :: per protocol :: Per psychiatry protocol; typically 3x/week | Pheochromocytoma; raised ICP (relative) | Anesthesia monitoring; cognitive function; post-procedure seizure threshold | - | EXT | EXT | EXT |

*Note: CAUTION with antipsychotics in autoimmune encephalitis -- patients (especially anti-NMDAR) are highly susceptible to neuroleptic malignant syndrome (NMS) and EPS. Use LOWEST effective doses. Benzodiazepines (lorazepam) are first-line for catatonia and agitation. Catatonia may be present in up to 40% of anti-NMDAR cases. If catatonia does not respond to lorazepam, consider ECT before escalating antipsychotics. Psychiatric symptoms in AE are driven by antibody-mediated mechanisms -- immunotherapy is the definitive treatment.*

### 3F. ICU-Specific Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Intubation and mechanical ventilation | - | GCS ≤8; airway protection; central hypoventilation | N/A :: - :: once :: RSI: avoid succinylcholine if hyperkalemia risk; maintain normocapnia | As per standard airway management | Ventilator parameters; ABG; daily SBT when appropriate | - | - | - | STAT |
| Labetalol IV (autonomic hypertensive crisis) | IV | Autonomic hypertensive crisis; SBP >180 | 10-20 mg :: IV :: PRN :: 10-20 mg IV q10-15min PRN; or infusion 0.5-2 mg/min; target SBP <180 | Severe bradycardia; AV block; decompensated CHF; asthma | Continuous BP; HR; I/O | - | - | - | STAT |
| Esmolol IV (autonomic tachycardia) | IV | Autonomic tachycardia; HR >120 | 500 mcg/kg :: IV :: once :: Bolus: 500 mcg/kg over 1 min; Infusion: 50-200 mcg/kg/min | Severe bradycardia; decompensated CHF; cardiogenic shock | Continuous HR/BP; ECG | - | - | - | STAT |
| Atropine (autonomic bradycardia) | IV | Autonomic bradycardia; HR <50 with hemodynamic compromise | 0.5-1 mg :: IV :: - :: 0.5-1 mg IV q3-5min (max 3 mg total) | Tachycardia; thyrotoxicosis | HR; rhythm | - | - | - | STAT |
| Isoproterenol drip (severe autonomic bradycardia) | IV | Severe autonomic bradycardia refractory to atropine | 2-10 mcg :: IV :: - :: 2-10 mcg/min IV infusion; titrate to HR >60 | Tachyarrhythmia; digoxin toxicity | Continuous ECG; HR; BP | - | - | - | STAT |
| Temporary transvenous pacemaker | - | Refractory bradycardia; pacemaker-dependent rhythm | N/A :: - :: continuous :: Per cardiology if pharmacologic measures fail | Active infection at insertion site | Capture; sensing; threshold checks | - | - | - | STAT |
| Norepinephrine (autonomic hypotension) | IV | Autonomic hypotension; MAP <65 | 0.1-0.5 mcg/kg :: IV :: - :: 0.1-0.5 mcg/kg/min IV; titrate to MAP >65 | Peripheral ischemia risk at high doses | Arterial line; MAP; lactate; urine output | - | - | - | STAT |
| DVT prophylaxis (enoxaparin) | SC | Immobilized ICU patient; VTE prevention | 40 mg :: SC :: daily :: 40 mg SC daily (adjust for renal function: 30 mg SC daily if CrCl <30) | Active bleeding; HIT; severe thrombocytopenia | Platelet count; anti-Xa if renal impairment; bleeding signs | - | STAT | - | STAT |
| Temperature management (hyperthermia) | IV | Central hyperthermia; target normothermia | 1g :: IV :: q6h :: Targeted temperature: 36-37C; cooling blankets; acetaminophen 1g IV/PO q6h PRN | Avoid overcooling; avoid shivering (increases metabolic demand) | Continuous temperature; shivering assessment (BSAS) | - | - | - | STAT |
| Sodium correction (hyponatremia -- LGI1) | IV | Hyponatremia (Na <125); LGI1-associated SIADH | 100-150 mL :: IV :: - :: If Na <125: 3% NaCl 100-150 mL IV over 10-20 min (repeat up to 3x); Target correction: 4-6 mEq/L in first 6h, max 8 mEq/L in 24h | Avoid overcorrection (osmotic demyelination risk) | Sodium q2-4h during correction; urine output; neurologic status | URGENT | URGENT | ROUTINE | URGENT |
| Fludrocortisone (chronic hyponatremia -- LGI1) | PO | Chronic hyponatremia from SIADH (LGI1 encephalitis) | 0.05-0.2 mg :: PO :: daily :: 0.05-0.2 mg PO daily | CHF; hypertension | Sodium; potassium; BP; edema | - | ROUTINE | ROUTINE | - |
| Fluid restriction (SIADH-related hyponatremia) | - | SIADH-related hyponatremia; LGI1 encephalitis | N/A :: - :: per protocol :: Restrict to 1-1.2 L/day if SIADH suspected (LGI1) | Dehydration risk | Sodium; I/O; daily weight; urine osmolality | - | ROUTINE | - | ROUTINE |

*Note: Central hypoventilation occurs in anti-NMDAR encephalitis and may require prolonged mechanical ventilation (weeks to months). Autonomic instability (tachycardia/bradycardia alternating, blood pressure lability, central hyperthermia, cardiac dysrhythmias) is a hallmark of severe anti-NMDAR encephalitis. LGI1 encephalitis frequently causes SIADH-related hyponatremia. Do NOT over-correct sodium (risk of osmotic demyelination).*

### 3G. Long-Term Immunosuppression / Maintenance

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Mycophenolate mofetil (CellCept) | PO | Long-term immunosuppression; steroid-sparing maintenance | 500 mg :: PO :: BID :: Start 500 mg PO BID; increase to 1000 mg PO BID over 2-4 weeks (target 1500-3000 mg/day) | Pregnancy (Category D -- teratogenic); active infection | CBC q2 weeks x 3 months, then monthly; LFTs; GI symptoms; infection surveillance; pregnancy prevention | - | - | ROUTINE | - |
| Azathioprine (Imuran) | PO | Long-term immunosuppression; steroid-sparing alternative | 50 mg :: PO :: daily :: Start 50 mg PO daily; increase by 50 mg every 2 weeks to target 2-3 mg/kg/day | TPMT deficiency (check before starting); pregnancy (relative) | TPMT genotype/activity before starting; CBC q2 weeks x 2 months, then monthly; LFTs; pancreatitis | - | - | ROUTINE | - |
| Rituximab (maintenance) | IV | Relapse prevention; B-cell depletion maintenance | 500-1000 mg :: IV :: - :: 500-1000 mg IV every 6 months; re-dose based on CD19/CD20 B-cell repopulation or clinical relapse | Active hepatitis B; severe active infection | CD19/CD20 counts q3 months; immunoglobulin levels q3-6 months; hepatitis B surveillance; infection monitoring; PML surveillance | - | - | ROUTINE | - |
| Oral prednisone (low-dose maintenance) | PO | Low-dose bridge while transitioning to steroid-sparing agent | 5-10 mg :: PO :: daily :: 5-10 mg PO daily; aim to taper off within 3-6 months if on steroid-sparing agent | Poorly controlled diabetes; active infection; avascular necrosis | Glucose; BP; bone density (DEXA if >3 months); weight; mood; cataracts; adrenal assessment on taper | - | - | ROUTINE | - |
| IVIG (maintenance) | IV | Ongoing immunomodulation; relapse prevention | 0.4 g/kg :: IV :: - :: 0.4 g/kg IV every 4 weeks OR 1-2 g/kg IV every 4-6 weeks (adjust per response) | IgA deficiency; thromboembolic history | Renal function; headache; IgG trough levels; infusion reactions | - | - | ROUTINE | - |
| Calcium + Vitamin D (bone protection with steroids) | - | Bone protection during chronic steroid use | 1000-1200 mg/day :: PO :: - :: Calcium 1000-1200 mg/day + Vitamin D 1000-2000 IU/day | Hypercalcemia; kidney stones | 25-OH Vitamin D level; calcium; DEXA baseline if anticipated steroid use >3 months | - | ROUTINE | ROUTINE | - |

*Note: Long-term immunosuppression is guided by antibody subtype, relapse risk, and tumor status. Anti-NMDAR encephalitis has ~12-20% relapse rate. Rituximab maintenance is most commonly used for relapse prevention. Mycophenolate and azathioprine are steroid-sparing alternatives. Monitor for immunosuppression-related complications (infection, malignancy). Duration of maintenance therapy is individualized -- typically minimum 2 years; some patients require indefinite treatment.*

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology (autoimmune/neuroimmunology) | STAT | STAT | ROUTINE | STAT | All suspected autoimmune encephalitis cases; immunotherapy management |
| Epilepsy/EEG service | STAT | STAT | ROUTINE | STAT | Seizure management; continuous EEG monitoring; extreme delta brush interpretation |
| Psychiatry | URGENT | URGENT | ROUTINE | URGENT | Psychiatric manifestations (psychosis, catatonia, agitation); antipsychotic management; NMS risk |
| Critical care/ICU | URGENT | URGENT | - | - | Autonomic instability; respiratory failure; refractory status epilepticus; altered consciousness |
| Gynecologic oncology (females with anti-NMDAR) | - | URGENT | URGENT | URGENT | Ovarian teratoma screening and surgical resection |
| Oncology | - | URGENT | ROUTINE | URGENT | Any identified malignancy; tumor screening guidance; chemotherapy planning |
| Urology (males <50 with anti-Ma2/KLHL11) | - | URGENT | ROUTINE | - | Testicular germ cell tumor screening |
| Hematology/apheresis | - | URGENT | - | URGENT | PLEX coordination; catheter placement |
| Physical therapy | - | ROUTINE | ROUTINE | ROUTINE | Motor rehabilitation; gait training; fall prevention |
| Occupational therapy | - | ROUTINE | ROUTINE | ROUTINE | ADL assessment; cognitive rehabilitation; adaptive strategies |
| Speech-language pathology | - | ROUTINE | ROUTINE | ROUTINE | Swallowing evaluation; language/communication rehabilitation; cognitive-linguistic therapy |
| Neuropsychology | - | - | ROUTINE | - | Formal cognitive assessment; rehabilitation planning; serial monitoring |
| Social work | - | ROUTINE | ROUTINE | - | Family support; insurance navigation; disability resources; long-term care planning |
| Rehabilitation medicine | - | ROUTINE | ROUTINE | - | Comprehensive inpatient or outpatient rehab program coordination |
| Palliative care | - | EXT | EXT | EXT | Refractory cases; prolonged ICU stay; family support; goals of care discussion |
| Infectious disease | URGENT | URGENT | - | URGENT | Rule out infection; antimicrobial guidance; post-immunosuppression infection management |
| Endocrinology | - | ROUTINE | ROUTINE | - | Steroid-induced hyperglycemia management; thyroid evaluation if Hashimoto suspected |

### 4B. Patient/Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED immediately for new seizures, sudden behavioral changes, fever, difficulty breathing, or loss of consciousness | Y | Y | Y |
| Autoimmune encephalitis is a treatable condition -- recovery may be slow (months to years) but significant improvement is expected with appropriate immunotherapy | Y | Y | Y |
| Do NOT drive until seizure-free for state-mandated period AND cleared by neurology | Y | Y | Y |
| Keep seizure diary (date, time, type, duration, triggers) | - | Y | Y |
| Behavioral and psychiatric symptoms are part of the disease, not a primary psychiatric disorder -- immunotherapy is the treatment | Y | Y | Y |
| Report any signs of infection (fever >100.4F, cough, dysuria, rash) immediately while on immunotherapy | - | Y | Y |
| Avoid live vaccines while on immunosuppressive therapy (inform all physicians of immunosuppression status) | - | Y | Y |
| Do not stop anti-seizure medications abruptly | - | Y | Y |
| Avoid alcohol and recreational drugs (lower seizure threshold, interact with medications) | - | Y | Y |
| Pregnancy must be avoided during immunotherapy; discuss contraception with neurology and OB/GYN | - | Y | Y |
| Expect gradual improvement -- anti-NMDAR recovery typically occurs in reverse order of symptom onset (psychiatric symptoms resolve last) | - | Y | Y |
| Cognitive rehabilitation exercises as directed by speech and occupational therapy | - | Y | Y |
| Safety modifications at home (remove sharp objects, secure stairways, fall prevention) | - | Y | Y |
| Medical alert bracelet recommended (autoimmune encephalitis, seizure risk, immunosuppressed) | - | Y | Y |
| Follow-up appointments are critical -- relapse monitoring requires regular visits | - | Y | Y |

### 4C. Tumor Screening Protocols by Antibody

| Antibody | Associated Tumor(s) | Screening Protocol | Frequency |
|----------|---------------------|-------------------|-----------|
| Anti-NMDAR | Ovarian teratoma (females, especially 12-45 years); rarely other tumors | Pelvic MRI or transvaginal US; CT chest/abdomen/pelvis | At diagnosis; repeat q6 months x 2 years if initially negative |
| Anti-LGI1 | Thymoma (~5-10%) | CT chest with contrast | At diagnosis; repeat if relapse |
| Anti-CASPR2 | Thymoma (~20-30%) | CT chest with contrast | At diagnosis; repeat if relapse |
| Anti-GABA-B | Small cell lung cancer (~50%) | CT chest; FDG-PET/CT if CT negative | At diagnosis; q6 months x 4 years |
| Anti-AMPA | Thymoma, lung cancer, breast cancer | CT chest/abdomen/pelvis; mammography; FDG-PET/CT | At diagnosis; q6 months x 4 years |
| Anti-DPPX | B-cell lymphoma (rare) | CT chest/abdomen/pelvis; FDG-PET if suspected | At diagnosis |
| Anti-Ma2/Ta | Testicular germ cell tumor (young males); lung cancer (older patients) | Testicular US (males <50); CT chest; FDG-PET/CT | At diagnosis; q6 months x 4 years |
| Anti-Hu (ANNA-1) | Small cell lung cancer (>90%) | CT chest; FDG-PET/CT | At diagnosis; q6 months x 4 years |
| Anti-CV2/CRMP5 | SCLC; thymoma | CT chest; FDG-PET/CT | At diagnosis; q6 months x 4 years |
| Anti-amphiphysin | Breast cancer; SCLC | Mammography/breast MRI; CT chest | At diagnosis; q6 months x 4 years |
| Anti-KLHL11 | Testicular seminoma | Testicular US; FDG-PET/CT | At diagnosis; repeat if relapse |

*Note: Tumor resection is critical for treatment response -- immunotherapy alone may be insufficient if underlying tumor is not removed. If initial tumor screen is negative but paraneoplastic antibody is positive, repeat imaging q6 months x 4 years. Consider FDG-PET/CT if CT is negative and clinical suspicion remains high.*

---

═══════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| HSV encephalitis | Acute fever, temporal lobe hemorrhagic necrosis, CSF lymphocytic pleocytosis with RBCs | HSV PCR (CSF); MRI temporal lobe changes; often more acute onset |
| Other viral encephalitis (EBV, CMV, HHV-6, enterovirus, West Nile) | Fever, CSF pleocytosis, specific exposure/season, immunocompromised status | Specific viral PCR/serology; CSF studies |
| Bacterial meningitis/encephalitis | Acute fever, meningismus, CSF neutrophilic pleocytosis, low glucose | CSF Gram stain, culture, procalcitonin, bacterial PCR |
| Neurosyphilis | Cognitive decline, psychiatric symptoms, Argyll Robertson pupils, positive serology | RPR/VDRL; CSF VDRL; FTA-ABS |
| Prion disease (CJD) | Rapidly progressive dementia, myoclonus, akinetic mutism; cortical ribboning on MRI (DWI) | 14-3-3 protein; RT-QuIC; MRI DWI cortical ribboning; EEG periodic discharges |
| CNS lymphoma | Progressive encephalopathy, mass lesion, periventricular enhancement, immunocompromised | CSF cytology/flow cytometry; FDG-PET; brain biopsy |
| CNS vasculitis | Headache, stroke-like episodes, multifocal infarcts, elevated ESR/CRP | Angiography; brain/leptomeningeal biopsy; ESR/CRP |
| Neurosarcoidosis | Cranial neuropathies, hypothalamic dysfunction, leptomeningeal enhancement | ACE level; chest CT (hilar adenopathy); biopsy |
| Hashimoto encephalopathy (SREAT) | Encephalopathy with very high anti-TPO; steroid-responsive; diagnosis of exclusion | Anti-TPO; anti-thyroglobulin; dramatic steroid response |
| Acute disseminated encephalomyelitis (ADEM) | Post-infectious/post-vaccination, multifocal large white matter lesions, encephalopathy | MRI pattern; MOG-IgG; monophasic course |
| NMO spectrum disorder (NMOSD) | Optic neuritis, longitudinally extensive myelitis, area postrema syndrome | AQP4-IgG; MRI pattern |
| Drug/toxin-induced encephalopathy | Temporal correlation with drug exposure; resolves with discontinuation | Urine drug screen; medication review; drug levels |
| Metabolic encephalopathy | Hepatic, uremic, thyroid, electrolyte disturbances | CMP; LFTs; ammonia; TSH; specific metabolic panels |
| Psychiatric disorder (new-onset psychosis, catatonia) | No CSF pleocytosis; normal MRI/EEG; isolated psychiatric symptoms (caution: AE can present as pure psychiatric) | LP mandatory to differentiate; EEG; MRI; antibody testing before assuming primary psychiatric |
| Seizure-related encephalopathy (post-ictal/non-convulsive SE) | Prolonged post-ictal confusion; non-convulsive status on EEG | Continuous EEG monitoring; resolves with ASM treatment |
| Neuro-Behcet disease | Oral/genital ulcers; brainstem predominance; CSF neutrophilic pleocytosis | Clinical criteria; pathergy test; HLA-B51 |

---

## 6. MONITORING PARAMETERS

### 6A. Acute Phase Monitoring (Inpatient)

| Parameter | Frequency | Target/Threshold | Action if Abnormal |
|-----------|-----------|------------------|-------------------|
| Neurologic examination (GCS, orientation, cranial nerves, motor, reflexes) | Q4-6h (ICU); Q8-12h (floor) | Stable or improving | If worsening: urgent re-imaging; escalate immunotherapy; consider ICU transfer |
| Modified Rankin Scale (mRS) | Baseline, then weekly | Improvement over weeks-months | Document trajectory; guide treatment escalation; long-term disability tracking |
| Bush-Francis Catatonia Rating Scale | Daily if catatonia features | Score decreasing with treatment | If not responding to lorazepam: increase dose; consider ECT; escalate immunotherapy |
| Blood glucose | Q6h during IV steroids | <180 mg/dL | Insulin sliding scale; endocrine consult if persistent >250 |
| Blood pressure | Q1h (ICU); Q4h (floor) | SBP 100-180 mmHg; MAP >65 | Autonomic dysregulation: labetalol/esmolol for hypertension; norepinephrine for hypotension |
| Heart rate and rhythm | Continuous telemetry (ICU/floor) | HR 60-100; sinus rhythm | Autonomic instability: treat per protocol (3F); cardiology consult if sustained arrhythmia |
| Temperature | Q4h; continuous in ICU | 36.0-37.5 C | Central hyperthermia: cooling measures; acetaminophen; rule out infection |
| Respiratory rate and NIF | Q4h (ICU); Q shift (floor) | RR <20; NIF >-30 cm H2O | NIF worsening toward -20: intubation; ICU transfer; evaluate for neuromuscular respiratory failure |
| Seizure log | Continuous | Decreasing frequency/severity | If increasing: escalate ASMs; re-assess immunotherapy; continuous EEG |
| EEG (continuous) | 24-72h minimum; longer if ICU | Resolving extreme delta brush; no subclinical seizures | If persistent seizures: escalate per Section 3D |
| Sodium (Na) | Q6-12h (if LGI1 or hyponatremia) | Na >130 mEq/L | Correct per protocol (3F); fluid restriction if SIADH |
| I/O and daily weight | Daily | Euvolemic | Adjust fluids; diuretics if fluid overload; free water restriction if SIADH |
| Renal function (BUN/Cr) | Daily during IVIG; q48h otherwise | Stable | Hold IVIG if Cr rising; hydration; nephrology consult |
| CBC with differential | Q48h during immunotherapy; daily if on cyclophosphamide | WBC >3.0; ANC >1.5; Plt >100 | Hold immunotherapy if critically low; growth factor support; hematology consult |
| LFTs | Q48-72h during acute treatment | ALT/AST <3x ULN | Dose adjustment or hold hepatotoxic medications |
| Fibrinogen (during PLEX) | Before each exchange | >100 mg/dL | Hold PLEX if <100; FFP replacement |

### 6B. Outpatient/Long-Term Monitoring

| Parameter | Frequency | Target/Threshold | Action if Abnormal |
|-----------|-----------|------------------|-------------------|
| Neurologic examination (cognition, behavior, seizures, motor) | Monthly x 6 months; then q3 months x 2 years; then q6 months | Sustained improvement; no new symptoms | If relapse: repeat LP/MRI; resume or escalate immunotherapy; re-screen for tumor |
| Modified Rankin Scale (mRS) | Each visit | Improving toward mRS 0-1 | Document trajectory; adjust rehab goals; consider treatment escalation if plateau or decline |
| CASE score (Clinical Assessment Scale in Autoimmune Encephalitis) | Each visit | Improving score over time | Standardized outcome measure; guide treatment decisions |
| MRI brain with and without contrast | 3-6 months post-treatment; then annually x 3 years | Stable or improved signal changes | New/worsening lesions: relapse workup; repeat antibody testing; escalate treatment |
| EEG (routine) | 3-6 months post-treatment; as needed for seizure management | Improved background; no epileptiform activity | If persistent abnormality: continue/adjust ASMs; consider repeat immunotherapy |
| Serum antibody titers | q3-6 months x 2 years; then annually | Decreasing or negative | Rising titers may precede clinical relapse; increase surveillance; consider preemptive treatment |
| CBC with differential | Q2-4 weeks on mycophenolate/azathioprine; then monthly | WBC >3.0; ANC >1.5; Plt >100 | Hold/reduce immunosuppression; growth factor support |
| LFTs | Monthly x 3 months on azathioprine/mycophenolate; then q3 months | ALT/AST <3x ULN | Dose reduction or switch agent |
| Immunoglobulin levels (IgG, IgA, IgM) | Q3-6 months on rituximab or other B-cell depletion | IgG >400 mg/dL | Immunoglobulin replacement if recurrent infections with hypogammaglobulinemia |
| CD19/CD20 B-cell counts | Q3 months on rituximab | Depleted (<1% B-cells) during active treatment | Guide re-dosing interval; B-cell repopulation may trigger relapse |
| TPMT activity/genotype | Once before starting azathioprine | Normal enzyme activity | Dose reduce or avoid azathioprine if intermediate/low TPMT |
| Tumor surveillance (per antibody type -- Section 4C) | Per protocol: q6 months x 2-4 years | No tumor identified | If tumor found: urgent oncology referral and surgical resection |
| Neuropsychological testing | Baseline (when able); 6 months; 12 months; annually | Improving cognitive domains | Guide cognitive rehabilitation; inform return to work/school planning |
| DEXA scan (bone density) | Baseline if steroids >3 months; repeat q1-2 years | T-score >-2.5 | Bisphosphonate therapy; calcium/vitamin D optimization |
| ASM drug levels (if applicable) | Per drug-specific schedule; after dose changes | Therapeutic range | Adjust dose; assess adherence |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **Discharge home** | Mild symptoms; stable or improving on established immunotherapy; no active seizures; able to perform basic ADLs; reliable follow-up within 1-2 weeks; no significant autonomic instability; family/caregiver education completed; outpatient infusion arranged if needed |
| **Admit to floor (medical/neurology)** | New-onset encephalitis requiring workup and immunotherapy initiation; seizures requiring medication adjustment; moderate behavioral symptoms manageable on floor; needs IV steroids/IVIG; diagnostic uncertainty requiring expedited workup |
| **Admit to ICU** | Refractory status epilepticus; altered consciousness (GCS <12); severe autonomic instability (hemodynamic swings, arrhythmias, central hypoventilation); need for continuous EEG monitoring; requirement for mechanical ventilation; severe catatonia unresponsive to lorazepam; frequent or prolonged seizures requiring IV anesthetic infusions |
| **Transfer to higher level of care** | PLEX or continuous EEG not available; neurology/neuroimmunology specialist not available; need for tumor resection (gynecologic oncology for teratoma); requires ICU care not available at current facility |
| **Inpatient rehabilitation** | Medically stable; significant functional deficits requiring intensive therapy (cognitive, motor, speech); unable to safely return home; expected to benefit from structured rehabilitation program |
| **Long-term acute care (LTAC)** | Prolonged ventilator dependence (common in severe anti-NMDAR); medically complex care needs; ongoing immunotherapy requirements; unable to participate in intensive rehab |
| **Skilled nursing facility** | Stable but unable to perform ADLs independently; requires ongoing nursing care; awaiting rehabilitation bed; chronic disability |
| **Outpatient follow-up** | All discharged patients: neurology follow-up within 1-2 weeks; infusion center for ongoing immunotherapy; neuropsychology referral; rehab services; tumor surveillance per protocol |
| **Readmission criteria** | New seizures after period of control; behavioral/cognitive regression; fever or signs of infection on immunotherapy; suspected relapse (any new neurologic/psychiatric symptoms) |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Graus 2016 diagnostic criteria for autoimmune encephalitis | Expert Consensus, Class III | [Graus F et al. Lancet Neurol 2016;15:391-404](https://pubmed.ncbi.nlm.nih.gov/26906964/) |
| CSF antibody testing more sensitive than serum for anti-NMDAR | Class II | [Dalmau J et al. Lancet Neurol 2008;7:1091-1098](https://pubmed.ncbi.nlm.nih.gov/18851928/) |
| Cell-based assay (CBA) is gold standard for antibody detection | Class II | Waters P et al. J Neurol Neurosurg Psychiatry 2014 |
| First-line immunotherapy: IV steroids + IVIG or PLEX | Class III, Expert Consensus | [Titulaer MJ et al. Lancet Neurol 2013;12:157-165](https://pubmed.ncbi.nlm.nih.gov/23290630/) |
| Early immunotherapy improves outcomes | Class II | [Titulaer MJ et al. Lancet Neurol 2013;12:157-165](https://pubmed.ncbi.nlm.nih.gov/23290630/) |
| Rituximab as second-line therapy | Class III, Retrospective | [Lee WJ et al. Neurology 2016;86:1683-1691](https://pubmed.ncbi.nlm.nih.gov/27037228/) |
| Early second-line (rituximab) improves anti-NMDAR outcomes | Class III | [Titulaer MJ et al. Lancet Neurol 2013;12:157-165](https://pubmed.ncbi.nlm.nih.gov/23290630/) |
| Cyclophosphamide as second-line therapy | Class III, Expert Consensus | [Dalmau J & Graus F. N Engl J Med 2018;378:840-851](https://pubmed.ncbi.nlm.nih.gov/29490181/) |
| Tocilizumab for refractory autoimmune encephalitis | Class IV, Case Series | [Lee WJ et al. Neurotherapeutics 2016;13:824-832](https://pubmed.ncbi.nlm.nih.gov/27215218/) |
| Bortezomib for refractory autoimmune encephalitis | Class IV, Case Series | [Scheibe F et al. Neurology 2017;88:366-370](https://pubmed.ncbi.nlm.nih.gov/28003505/) |
| Ovarian teratoma resection is essential in anti-NMDAR | Class II | [Titulaer MJ et al. Lancet Neurol 2013](https://pubmed.ncbi.nlm.nih.gov/23290630/) |
| Tumor screening by antibody type | Expert Consensus | [Graus F et al. Lancet Neurol 2016](https://pubmed.ncbi.nlm.nih.gov/26906964/) |
| Extreme delta brush on EEG in anti-NMDAR | Class III | [Schmitt SE et al. Neurology 2012;79:1094-1100](https://pubmed.ncbi.nlm.nih.gov/22933737/) |
| Faciobrachial dystonic seizures precede LGI1 encephalitis | Class III | [Irani SR et al. Ann Neurol 2011;69:892-900](https://pubmed.ncbi.nlm.nih.gov/21416487/) |
| Hyponatremia in LGI1 encephalitis (SIADH mechanism) | Class III | [Lai M et al. Lancet Neurol 2010;9:776-785](https://pubmed.ncbi.nlm.nih.gov/20580615/) |
| GABA-B encephalitis and SCLC association (~50%) | Class III | [Lancaster E et al. Lancet Neurol 2010;9:67-76](https://pubmed.ncbi.nlm.nih.gov/19962348/) |
| Anti-NMDAR encephalitis staging and recovery pattern | Class II | [Dalmau J et al. Lancet Neurol 2019;18:1045-1057](https://pubmed.ncbi.nlm.nih.gov/31326280/) |
| Modified Rankin Scale for outcome tracking | Validated Scale | [van Swieten JC et al. Stroke 1988;19:604-607](https://pubmed.ncbi.nlm.nih.gov/3363593/) |
| CASE score for autoimmune encephalitis assessment | Validated Scale | [Lim JA et al. Ann Neurol 2019;85:352-358](https://pubmed.ncbi.nlm.nih.gov/30675918/) |
| Catatonia in anti-NMDAR encephalitis (~40%) | Class III | [Al-Diwani A et al. Lancet Psychiatry 2019;6:235-246](https://pubmed.ncbi.nlm.nih.gov/30765329/) |
| Lorazepam challenge for catatonia | Expert Consensus | [Bush G et al. Acta Psychiatr Scand 1996;93:129-136](https://pubmed.ncbi.nlm.nih.gov/8686483/) |
| NMS risk with antipsychotics in anti-NMDAR | Class IV, Case Reports | [Lejuste F et al. Neurol Neuroimmunol Neuroinflamm 2016;3:e280](https://pubmed.ncbi.nlm.nih.gov/27606355/) |
| Levetiracetam as preferred ASM in autoimmune encephalitis | Expert Consensus | [Britton J. Handb Clin Neurol 2016;133:219-245](https://pubmed.ncbi.nlm.nih.gov/27112680/) |
| Avoid carbamazepine in LGI1 (worsens hyponatremia) | Expert Consensus | [Irani SR et al. Brain 2010;133:2734-2748](https://pubmed.ncbi.nlm.nih.gov/20663977/) |
| Long-term rituximab maintenance prevents relapse | Class III | [Nosadini M et al. Expert Rev Neurother 2015;15:1391-1419](https://pubmed.ncbi.nlm.nih.gov/26559389/) |
| Anti-NMDAR relapse rate 12-20% | Class II | [Titulaer MJ et al. Lancet Neurol 2013](https://pubmed.ncbi.nlm.nih.gov/23290630/) |
| Mycophenolate as steroid-sparing agent | Class IV | Expert practice; no large trials |
| Autonomic instability management in anti-NMDAR | Expert Consensus | [Dalmau J & Graus F. N Engl J Med 2018](https://pubmed.ncbi.nlm.nih.gov/29490181/) |
| Repeat tumor screening q6 months x 2-4 years | Expert Consensus | [Graus F et al. Lancet Neurol 2016](https://pubmed.ncbi.nlm.nih.gov/26906964/) |
| Central hypoventilation in severe anti-NMDAR requiring prolonged ventilation | Class III | [Florance NR et al. Ann Neurol 2009;66:11-18](https://pubmed.ncbi.nlm.nih.gov/19670433/) |
| Neuropsychological recovery trajectory in autoimmune encephalitis | Class III | [Finke C et al. JAMA Neurol 2017;74:50-59](https://pubmed.ncbi.nlm.nih.gov/27893017/) |

---

## CLINICAL DECISION SUPPORT NOTES

### Graus 2016 Diagnostic Criteria -- Possible Autoimmune Encephalitis

All three of the following must be met:
- [ ] Subacute onset (rapid progression of <3 months) of working memory deficits, altered mental status, or psychiatric symptoms
- [ ] At least one of: (a) new focal CNS findings, (b) seizures not explained by prior seizure disorder, (c) CSF pleocytosis (WBC >5), (d) MRI features suggestive of encephalitis
- [ ] Reasonable exclusion of alternative causes

### Anti-NMDAR Encephalitis Clinical Staging

1. **Prodromal phase** (days to 2 weeks): Fever, headache, URI-like symptoms
2. **Psychiatric phase** (weeks 1-2): Psychosis, paranoia, agitation, bizarre behavior, hallucinations, anxiety, insomnia
3. **Unresponsive phase** (weeks 2-4): Decreased consciousness, catatonia, mutism
4. **Hyperkinetic phase** (weeks 2-8): Orofacial dyskinesias, choreoathetosis, dystonic posturing, autonomic instability
5. **Recovery phase** (months to years): Gradual improvement in reverse order of symptom onset; prolonged cognitive/behavioral deficits

### Red Flags for Autoimmune Encephalitis

- [ ] Young female with new-onset psychiatric symptoms + seizures (consider anti-NMDAR)
- [ ] Limbic encephalitis + hyponatremia (consider LGI1)
- [ ] Faciobrachial dystonic seizures (pathognomonic for LGI1)
- [ ] Refractory status epilepticus in young patient (consider GABA-A, GABA-B, NMDAR)
- [ ] Psychiatric presentation with CSF pleocytosis (encephalitis, NOT primary psychiatric)
- [ ] Encephalopathy + ovarian teratoma (consider anti-NMDAR)
- [ ] Extreme delta brush on EEG (pathognomonic for anti-NMDAR)
- [ ] Encephalopathy + movement disorder (orofacial dyskinesias) + autonomic instability
- [ ] New-onset refractory status epilepticus (NORSE/FIRES) -- screen for autoimmune etiology
- [ ] Rapidly progressive encephalopathy with seizures in a smoker (consider GABA-B + SCLC)

---

## CHANGE LOG

**v1.0 (January 27, 2026)**
- Initial creation
- Section 1: 24 core labs (1A), 20 antibody panel tests (1B), 16 rare/specialized tests (1C)
- Section 2: 6 essential imaging/studies (2A), 7 extended (2B), 5 rare (2C), 22 LP/CSF studies
- Section 3: Expanded to 7 subsections:
  - 3A: 5 acute/emergent treatments (empiric acyclovir, antibiotics, benzodiazepines, catatonia challenge)
  - 3B: 5 first-line immunotherapy agents (methylprednisolone, omeprazole, insulin, IVIG, PLEX)
  - 3C: 6 second-line immunotherapy agents (rituximab, cyclophosphamide, tocilizumab, bortezomib, repeated IVIG/PLEX, oral prednisone taper)
  - 3D: 10 anti-seizure medications including refractory/super-refractory status epilepticus protocols
  - 3E: 9 psychiatric symptom management agents (antipsychotics, lorazepam for catatonia, ICU sedation, mood stabilization, ECT)
  - 3F: 12 ICU-specific treatments (ventilation, autonomic instability, DVT prophylaxis, temperature management, sodium correction)
  - 3G: 6 long-term immunosuppression/maintenance agents (mycophenolate, azathioprine, rituximab maintenance, prednisone, IVIG maintenance, bone protection)
- Section 4: 17 referrals (4A), 15 patient/family instructions (4B), 11 tumor screening protocols by antibody type (4C)
- Section 5: 16 differential diagnoses with distinguishing features
- Section 6: 16 acute monitoring parameters (6A), 15 outpatient/long-term monitoring parameters (6B)
- Section 7: 9 disposition criteria
- Section 8: 30 evidence references with evidence levels
- Clinical Decision Support Notes: Graus 2016 diagnostic criteria checklist, anti-NMDAR clinical staging (5 phases), 10 red flags checklist
