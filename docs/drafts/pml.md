---
title: "Progressive Multifocal Leukoencephalopathy (PML)"
description: "Clinical decision support for diagnosis and management of PML"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - demyelinating
  - infection
  - immunocompromised
  - JC-virus
  - leukoencephalopathy
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Progressive Multifocal Leukoencephalopathy (PML)

**VERSION:** 1.1
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Draft — Revised per checker feedback

---

**DIAGNOSIS:** Progressive Multifocal Leukoencephalopathy (PML)

**ICD-10:** A81.2 (Progressive multifocal leukoencephalopathy)

**CPT CODES:** 85025 (CBC), 80053 (CMP), 86703 (HIV antibody), 87536 (HIV viral load), 86360 (CD4 count), 87798 (CSF JCV PCR), 89050 (CSF cell count), 84157 (CSF protein), 70553 (MRI brain with/without contrast), 88305 (Brain biopsy pathology), 95816 (EEG)

**SYNONYMS:** progressive multifocal leukoencephalopathy, PML, JC virus encephalopathy, JC virus leukoencephalopathy, natalizumab-associated PML, immune reconstitution PML, PML-IRIS, John Cunningham virus brain infection

**SCOPE:** Diagnosis and management of PML in all clinical contexts: HIV-associated, natalizumab-associated, other immunosuppression-associated, and rare immunocompetent PML. Covers CSF JCV PCR testing, MRI features, immune reconstitution strategies, PML-IRIS management, and supportive care. Excludes other causes of leukoencephalopathy as primary diagnosis but includes in differential.

---

**DEFINITIONS:**
- **PML:** Demyelinating disease caused by JC virus (JCV) reactivation in immunocompromised individuals; progressive destruction of oligodendrocytes leading to multifocal white matter injury
- **JC virus (JCV):** Polyomavirus; seroprevalence 50-70% in adults; remains latent in kidneys and bone marrow; reactivates with immunosuppression
- **PML-IRIS (Immune Reconstitution Inflammatory Syndrome):** Paradoxical worsening of PML during immune recovery (ART initiation in HIV, natalizumab cessation); contrast enhancement and edema on MRI; inflammatory CSF
- **Natalizumab-associated PML:** PML occurring in MS patients on natalizumab; risk factors: JCV antibody index >1.5, prior immunosuppression, treatment duration >24 months

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (All Patients)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Lymphopenia assessment; immunosuppression degree; baseline | Lymphocyte count >1000/μL |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal/hepatic function; metabolic baseline | Normal |
| HIV antibody/antigen (4th gen) (CPT 86703) | STAT | STAT | ROUTINE | STAT | HIV is most common cause of PML; must test all patients | Negative |
| HIV viral load (CPT 87536) | STAT | STAT | - | STAT | If HIV positive: quantify viral burden; guide ART initiation | Undetectable if on ART |
| CD4 count (CPT 86360) | STAT | STAT | ROUTINE | STAT | Degree of immunosuppression; PML typically occurs with CD4 <200 in HIV; also useful in non-HIV immunosuppression | CD4 >500 (PML risk highest <200 in HIV) |
| JCV antibody index (serum) | - | ROUTINE | ROUTINE | - | Risk stratification; high index (>1.5) associated with greater PML risk in natalizumab patients; documents JCV exposure | Negative or low index (<0.9 lower risk) |
| Immunoglobulin levels (IgG, IgA, IgM) | - | ROUTINE | ROUTINE | - | Hypogammaglobulinemia as contributing immunodeficiency | Normal |

### 1B. Extended Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Absolute lymphocyte subsets (CD4, CD8, CD19, NK cells) | - | ROUTINE | ROUTINE | - | Characterize immune deficiency; guide immune reconstitution strategy | Normal ranges for all subsets |
| Quantitative immunoglobulins | - | ROUTINE | ROUTINE | - | Hypogammaglobulinemia from rituximab or other B-cell depleting therapy | Normal IgG >600 mg/dL |
| ESR / CRP | - | ROUTINE | ROUTINE | - | Inflammatory markers; elevated in PML-IRIS | Normal in PML; elevated in IRIS |
| LDH | - | ROUTINE | ROUTINE | - | Prognostic marker; elevated associated with worse outcomes | Normal |
| Liver function tests | - | ROUTINE | ROUTINE | - | Baseline before any hepatotoxic treatment; hepatic disease contributing to immunodeficiency | Normal |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum JCV viral load (quantitative PCR) | - | EXT | EXT | - | Research use; viremia may precede PML; limited clinical utility currently | Negative |
| Flow cytometry for lymphocyte activation markers | - | - | EXT | - | Assess immune reconstitution; guide treatment in PML-IRIS | Normal activation markers |
| BK virus PCR (urine) | - | - | EXT | - | Related polyomavirus; BK viruria suggests polyomavirus reactivation context | Negative |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with/without contrast (CPT 70553) | STAT | STAT | ROUTINE | STAT | Immediate; critical for diagnosis | Multifocal, bilateral, asymmetric subcortical/juxtacortical white matter T2/FLAIR hyperintensities; typically NO enhancement and NO mass effect (distinguishes from tumors); involves subcortical U-fibers; posterior fossa common | MRI-incompatible devices |
| CT head without contrast | STAT | - | - | STAT | Only if MRI not immediately available | Hypodense white matter lesions; less sensitive than MRI | None |

### 2B. Extended Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain follow-up (q4-8 weeks) | - | - | ROUTINE | - | Serial monitoring for progression or IRIS; every 4-8 weeks initially | Stabilization or improvement of lesions; new enhancement suggests PML-IRIS | MRI-incompatible devices |
| MR spectroscopy | - | EXT | EXT | - | Differentiate PML from other white matter diseases | Reduced NAA (neuronal loss); elevated choline (demyelination); elevated myo-inositol | MRI-incompatible devices |
| EEG (CPT 95816) | - | ROUTINE | ROUTINE | ROUTINE | If seizures occur; encephalopathy assessment; outpatient monitoring for subclinical seizures | Focal or diffuse slowing; epileptiform activity at lesion borders | None |

### LUMBAR PUNCTURE

**Indication:** Essential for diagnosis; CSF JCV PCR is the cornerstone diagnostic test
**Timing:** Urgent; critical for definitive diagnosis
**Volume Required:** 10-15 cc; dedicate sufficient volume for JCV PCR (sensitivity is volume-dependent)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| JCV PCR (quantitative) (CPT 87798) | DEFINITIVE diagnostic test; sensitivity 72-92%; specificity ~99%; quantitative load correlates with disease severity | Negative (positive confirms PML in appropriate clinical/imaging context); higher copy numbers = worse prognosis | URGENT | STAT | ROUTINE | URGENT |
| Cell count with differential | Typically normal in PML; elevated WBC suggests IRIS or alternative diagnosis | Normal (<5 WBC); elevated with lymphocytic predominance suggests PML-IRIS | URGENT | STAT | - | URGENT |
| Protein | Mildly elevated or normal | Normal or mildly elevated (typically <100 mg/dL); markedly elevated suggests alternative | URGENT | STAT | - | URGENT |
| Glucose with serum glucose | Exclude infection | Normal (>60% serum) | URGENT | STAT | - | URGENT |
| Oligoclonal bands | MS evaluation if natalizumab patient; baseline | Variable; may be present from underlying MS | - | ROUTINE | - | - |
| Cytology | Exclude lymphoma (may mimic PML on imaging) | Negative for malignant cells | - | ROUTINE | - | - |

**Special Handling:** JCV PCR is the critical test; ensure adequate volume (≥1 mL dedicated to JCV); if initial PCR negative but clinical suspicion high, repeat LP in 2-4 weeks (sensitivity improves with repeat testing)
**Contraindications:** Significant mass effect; coagulopathy

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Antiretroviral therapy (ART) initiation (HIV-PML) | PO | HIV-associated PML; ART is the ONLY proven effective treatment; immune reconstitution allows immune clearance of JCV | Per HIV guidelines :: PO :: daily :: Initiate ART as soon as possible; integrase inhibitor-based regimen preferred (dolutegravir + tenofovir/emtricitabine); rapid ART start; coordinate with HIV specialist | None (benefit outweighs all risks in PML) | CD4 count q4-8wk; HIV viral load q4wk until undetectable; hepatic/renal function; IRIS monitoring | STAT | STAT | ROUTINE | STAT |
| Natalizumab cessation + PLEX (natalizumab-PML) | Apheresis | Natalizumab-associated PML; remove drug to allow immune reconstitution; PLEX accelerates natalizumab clearance | 5 exchanges :: Apheresis :: every other day :: Discontinue natalizumab immediately; 5 plasma exchanges over 10 days to accelerate drug clearance (natalizumab half-life ~16 days; PLEX reduces to days) | Hemodynamic instability; coagulopathy | IRIS monitoring (typically occurs 1-5 weeks after PLEX); MRI q2-4wk; clinical exam q1-2 days | - | STAT | - | STAT |
| Discontinue causative immunosuppression (other-PML) | - | PML from rituximab, mycophenolate, fludarabine, or other immunosuppressants | Discontinue immediately :: - :: - :: Stop the causative immunosuppressant; no PLEX equivalent for most drugs; immune reconstitution occurs over weeks-months depending on drug | Balance with underlying disease management | CD4 and lymphocyte counts q2-4wk; MRI q4-8wk; clinical monitoring for IRIS | - | STAT | ROUTINE | STAT |
| Methylprednisolone (PML-IRIS) | IV | Fulminant PML-IRIS with severe cerebral edema and herniation risk | 1000 mg daily x 3-5 days :: IV :: daily x 3-5 days :: 1000 mg IV daily for 3-5 days for life-threatening IRIS; follow with oral steroid taper | Mass effect with herniation (may need neurosurgical intervention first) | ICP; neurological exam; MRI; blood glucose; BP | - | STAT | - | STAT |
| Dexamethasone (PML-IRIS) | IV/PO | Moderate-severe PML-IRIS with significant edema, mass effect, or clinical deterioration from inflammation | 4-8 mg q6h :: IV/PO :: q6h :: Start 4-8 mg IV q6h for severe IRIS; taper over 2-6 weeks based on clinical response; shortest effective course to avoid further immunosuppression | Active untreated infection (relative); recognize that steroids also suppress beneficial immune response against JCV | Clinical exam; MRI q2-4wk for edema/enhancement resolution; steroid side effects; balance IRIS suppression vs JCV clearance | - | URGENT | - | URGENT |
| Dexamethasone (cerebral edema) | IV | Cerebral edema from PML lesions or IRIS causing mass effect | 10 mg load then 4 mg q6h :: IV :: q6h :: 10 mg IV load, then 4 mg q6h; taper as edema resolves; use shortest effective course | Active untreated infection | Blood glucose; BP; GI protection; clinical response | URGENT | URGENT | - | URGENT |
| Levetiracetam (acute seizures) | IV/PO | Acute seizure management in PML (seizures common with cortical lesions) | 1000 mg load :: IV :: load then BID :: 1000 mg IV load, then 500 mg IV/PO BID; titrate to 1000-1500 mg BID; adjust for renal function | Severe renal impairment (dose adjust) | Mood changes; sedation; renal function | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levetiracetam (maintenance) | PO | Ongoing seizure prophylaxis/treatment (seizures common in PML, especially with cortical lesions) | 500 mg BID :: PO :: BID :: Start 500 mg BID; titrate to 1000-1500 mg BID; adjust for renal function; continue indefinitely if seizures occurred | Severe renal impairment (dose adjust) | Mood changes; irritability; sedation; renal function | - | ROUTINE | ROUTINE | ROUTINE |
| Lacosamide | PO/IV | Seizure management; alternative or adjunct to levetiracetam; favorable side effect profile | 50 mg BID :: PO :: BID :: Start 50 mg BID; increase by 50 mg/dose weekly; target 100-200 mg BID; max 400 mg/day | PR prolongation; 2nd/3rd degree AV block; severe hepatic impairment | ECG at baseline; PR interval; dizziness; diplopia | - | ROUTINE | ROUTINE | ROUTINE |
| Valproic acid | PO/IV | Seizure management; broad-spectrum option for focal or generalized seizures in PML | 250 mg BID :: PO :: BID :: Start 250 mg BID; titrate to 500-750 mg BID; target level 50-100 mcg/mL; adjust for hepatic function | Hepatic disease; urea cycle disorders; pregnancy (teratogenic); mitochondrial disease (POLG mutation) | LFTs baseline and periodically; CBC; ammonia if encephalopathy; drug level; pancreatitis risk | - | ROUTINE | ROUTINE | ROUTINE |
| Gabapentin | PO | Neuropathic pain; paresthesias from white matter lesions | 300 mg qHS :: PO :: qHS :: Start 300 mg qHS; increase by 300 mg every 1-3 days; target 900-1800 mg TID; max 3600 mg/day | Renal impairment (adjust dose per CrCl) | Sedation; dizziness; peripheral edema | - | ROUTINE | ROUTINE | - |
| Pregabalin | PO | Neuropathic pain; alternative to gabapentin | 75 mg BID :: PO :: BID :: Start 75 mg BID; increase to 150 mg BID after 1 week; max 300 mg BID | Renal impairment (adjust dose per CrCl) | Sedation; weight gain; peripheral edema | - | ROUTINE | ROUTINE | - |
| Baclofen | PO | Spasticity from white matter and corticospinal tract involvement | 5 mg TID :: PO :: TID :: Start 5 mg TID; increase by 5 mg/dose every 3 days; max 80 mg/day in divided doses | Renal impairment (reduce dose) | Sedation; weakness; do NOT stop abruptly (withdrawal risk) | - | ROUTINE | ROUTINE | ROUTINE |
| Tizanidine | PO | Spasticity; alternative to baclofen | 2 mg qHS :: PO :: qHS :: Start 2 mg qHS or TID; increase by 2-4 mg every 3-4 days; max 36 mg/day in 3 divided doses | Hepatic impairment; concurrent ciprofloxacin or fluvoxamine (CYP1A2 inhibitors) | LFTs at baseline, 1, 3, 6 months; sedation; hypotension | - | ROUTINE | ROUTINE | ROUTINE |
| Sertraline | PO | Depression; anxiety; mood disturbance related to PML diagnosis and disability | 50 mg daily :: PO :: daily :: Start 50 mg daily; increase by 25-50 mg every 1-2 weeks; max 200 mg daily | Concurrent MAOIs; pimozide | Suicidality monitoring (especially weeks 1-4); serotonin syndrome; QTc at high doses | - | ROUTINE | ROUTINE | - |
| Escitalopram | PO | Depression; anxiety; alternative to sertraline | 10 mg daily :: PO :: daily :: Start 10 mg daily; may increase to 20 mg after 1 week; max 20 mg daily | Concurrent MAOIs; pimozide; QT prolongation | QTc if risk factors or dose >10 mg; suicidality monitoring | - | ROUTINE | ROUTINE | - |
| Mirtazapine (symptomatic) | PO | Depression with insomnia; appetite stimulation in wasting; also theoretical anti-JCV activity via 5-HT2A antagonism | 15 mg qHS :: PO :: qHS :: Start 15 mg qHS; titrate to 30-45 mg qHS; dual benefit as antidepressant and possible anti-JCV agent | Concurrent MAOIs | Sedation; weight gain (may be beneficial in cachectic patients); dry mouth; agranulocytosis (rare) | - | ROUTINE | ROUTINE | - |
| Modafinil | PO | Fatigue; cognitive slowing; excessive daytime somnolence | 100 mg daily :: PO :: daily :: Start 100 mg every morning; may increase to 200 mg; max 400 mg/day | Cardiac arrhythmia; LV hypertrophy; hepatic impairment | BP; HR; may reduce efficacy of hormonal contraception; Schedule IV | - | - | ROUTINE | - |
| Methylphenidate | PO | Fatigue; cognitive slowing; apathy; adjunct for attention deficits | 5 mg BID :: PO :: BID :: Start 5 mg BID (morning and noon); increase by 5-10 mg weekly; max 60 mg/day | Marked anxiety; glaucoma; tics/Tourette; concurrent MAOIs | BP; HR; mood; appetite; weight; Schedule II | - | - | ROUTINE | - |
| Donepezil | PO | Cognitive impairment; memory deficits from white matter injury | 5 mg daily :: PO :: daily :: Start 5 mg daily; may increase to 10 mg daily after 4-6 weeks; take in evening | Bradycardia; sick sinus syndrome; GI obstruction | HR; GI symptoms (nausea, diarrhea); vivid dreams; weight loss | - | - | ROUTINE | - |
| Memantine | PO | Cognitive impairment; moderate-severe cognitive deficits; may be combined with donepezil | 5 mg daily :: PO :: daily :: Start 5 mg daily; increase by 5 mg weekly; target 10 mg BID; max 20 mg/day | Severe renal impairment (dose adjust if CrCl <30) | Dizziness; headache; constipation; confusion | - | - | ROUTINE | - |
| Omeprazole | PO | GI prophylaxis during corticosteroid therapy | 20 mg daily :: PO :: daily :: 20-40 mg daily during steroid treatment | PPI allergy | None routine; long-term: magnesium, B12, bone density | - | ROUTINE | ROUTINE | ROUTINE |

### 3C. Maintenance/Chronic Therapies

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Antiretroviral therapy (ongoing, HIV-PML) | PO | Lifelong ART for HIV-associated PML; continuous immune reconstitution required for JCV clearance and prevention of relapse | Per HIV guidelines :: PO :: daily :: Continue integrase inhibitor-based regimen (dolutegravir + tenofovir/emtricitabine or equivalent); do NOT interrupt ART; optimize regimen with HIV specialist | None (benefit always outweighs risk in HIV-PML) | CD4 count q3 months; HIV viral load q3 months; renal function; LFTs; metabolic panel annually | - | ROUTINE | ROUTINE | ROUTINE |
| Mirtazapine (adjunctive anti-JCV) | PO | Long-term adjunctive therapy; 5-HT2A receptor antagonist may block JCV entry into glial cells; commonly used despite limited clinical evidence given favorable safety profile | 30-45 mg qHS :: PO :: qHS :: Continue 30-45 mg qHS long-term; theoretical benefit from 5-HT2A blockade preventing JCV cell entry | Concurrent MAOIs | Sedation; weight gain; dry mouth; metabolic monitoring annually | - | ROUTINE | ROUTINE | - |
| Maraviroc (IRIS adjunct) | PO | Adjunctive PML-IRIS treatment during taper period; CCR5 antagonist may reduce inflammatory infiltrate; limited evidence | 300 mg BID :: PO :: BID :: 300 mg PO BID; used as adjunct to steroids for IRIS; continue through IRIS resolution; case reports/series suggest benefit | Severe hepatic impairment; concurrent strong CYP3A4 inhibitors (dose adjust) | LFTs; clinical response; hepatotoxicity; postural hypotension | - | ROUTINE | ROUTINE | - |
| Dexamethasone taper (chronic IRIS) | PO | Prolonged IRIS requiring slow steroid taper over weeks to months | Variable taper :: PO :: daily :: Taper from 4-8 mg/day by 1-2 mg every 1-2 weeks guided by clinical response and MRI; may require months; balance IRIS suppression vs JCV clearance | Concurrent active infection; brittle diabetes | Blood glucose; BP; bone density if prolonged; weight; mood; adrenal insufficiency during taper | - | ROUTINE | ROUTINE | - |

### 3D. Investigational/Immune Reconstitution Therapies (Limited Evidence)

*These therapies function as disease-modifying approaches for PML. All require specialist supervision and informed consent given limited evidence.*

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Pembrolizumab | IV | PD-1 checkpoint inhibitor; immune reconstitution approach; emerging evidence in non-HIV PML; restores T-cell function against JCV | 2 mg/kg q4-6wk :: IV :: q4-6wk :: 2 mg/kg IV every 4-6 weeks; limited case series; risk of autoimmune complications and severe IRIS; informed consent essential | Baseline thyroid function; LFTs; renal function; chest imaging; confirm not organ transplant recipient | Autoimmune disease; organ transplant recipients (rejection risk); severe IRIS already present; active autoimmune condition | Immune-related adverse events (thyroid q6wk, LFTs q2-4wk, colitis symptoms, pneumonitis); IRIS monitoring; clinical response; JCV PCR q4-8wk | - | EXT | EXT | - |
| Cidofovir | IV | Antiviral with in vitro activity against JCV; clinical trials have NOT shown clear benefit; not recommended routinely; consider only when no other options | 5 mg/kg q1-2wk :: IV :: q1-2wk :: 5 mg/kg IV weekly x 2 then every 2 weeks; must give with probenecid and IV hydration; nephrotoxic; CLINICAL TRIALS HAVE NOT SHOWN BENEFIT | Baseline renal function; urinalysis; CBC; adequate hydration protocol | Renal insufficiency (Cr >1.5); concurrent nephrotoxins; dehydration | Renal function (Cr before each dose); proteinuria; neutrophil count; limited evidence of efficacy; ocular toxicity | - | EXT | - | - |
| Nivolumab | IV | PD-1 checkpoint inhibitor; alternative to pembrolizumab for non-HIV PML; similar mechanism of immune reconstitution | 3 mg/kg q2wk :: IV :: q2wk :: 3 mg/kg IV every 2 weeks; case reports of benefit; risk of IRIS and autoimmune adverse events | Baseline thyroid function; LFTs; renal function; chest imaging; confirm not organ transplant recipient | Autoimmune disease; organ transplant recipients (rejection risk); severe IRIS already present; active autoimmune condition | Immune-related adverse events (thyroid q6wk, LFTs q2-4wk, colitis symptoms, pneumonitis); IRIS monitoring; clinical response; JCV PCR q4-8wk | - | EXT | EXT | - |
| Interleukin-7 (IL-7) | SC | Investigational; promotes T-cell expansion and immune reconstitution; early-phase clinical data | 10-20 mcg/kg weekly :: SC :: weekly :: 10-20 mcg/kg SC weekly for 3 weeks; investigational; limited availability; clinical trial enrollment preferred | Baseline lymphocyte subsets; exclude active autoimmune disease | Active autoimmune disease; concurrent immunosuppression (relative) | CD4/CD8 counts q1-2wk; clinical response; IRIS monitoring; cytokine levels | - | EXT | EXT | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation for PML diagnosis confirmation, IRIS management, and serial monitoring | STAT | STAT | ROUTINE | STAT |
| Infectious disease consultation for HIV-PML (ART optimization) and non-HIV immunosuppression management | STAT | STAT | ROUTINE | STAT |
| Neuroradiology review for MRI pattern characterization and serial imaging comparison | URGENT | ROUTINE | ROUTINE | URGENT |
| Physical therapy for motor rehabilitation, mobility assessment, and adaptive equipment | - | ROUTINE | ROUTINE | ROUTINE |
| Occupational therapy for ADL assessment, adaptive strategies for visual and motor deficits | - | ROUTINE | ROUTINE | - |
| Speech therapy for aphasia, dysarthria, and dysphagia assessment | - | ROUTINE | ROUTINE | - |
| Neuropsychology referral for formal cognitive assessment and rehabilitation planning | - | ROUTINE | ROUTINE | - |
| Palliative care for goals of care discussion, symptom management, and advance care planning given poor prognosis in many cases | - | ROUTINE | ROUTINE | ROUTINE |
| Social work consult for insurance navigation, disability resources, home care coordination, and support services | - | ROUTINE | ROUTINE | - |
| Neurosurgery consultation only if brain biopsy needed for diagnosis (CSF JCV PCR negative with high clinical suspicion) | - | EXT | - | EXT |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Return to ED immediately for rapid neurological decline (new weakness, vision loss, speech difficulty, sudden confusion, seizures), as PML can progress rapidly and treatment adjustments may be needed | STAT | ROUTINE | ROUTINE | - |
| Do NOT stop antiretroviral therapy (if HIV-positive) under any circumstances; ART is the single most important treatment for HIV-PML; missed doses reduce effectiveness | STAT | ROUTINE | ROUTINE | - |
| Understand that worsening after starting ART (HIV) or stopping natalizumab may represent IRIS — a paradoxical inflammatory response that is expected and treatable; do not stop ART if this occurs | - | ROUTINE | ROUTINE | - |
| Seizure precautions: avoid driving until seizure risk assessed by neurology; do not swim or bathe alone; remove sharp/hard hazards from home; fall precautions | ROUTINE | ROUTINE | ROUTINE | - |
| Take all anti-seizure medications as prescribed; do not skip doses or stop abruptly; missed doses increase seizure risk | - | ROUTINE | ROUTINE | - |
| Follow-up appointments and MRIs are critical — do not miss scheduled imaging, as PML requires close monitoring for progression and IRIS | - | ROUTINE | ROUTINE | - |
| Report any new fever, headache, or worsening symptoms during steroid taper, as this may indicate IRIS flare requiring dose adjustment | - | ROUTINE | ROUTINE | - |
| Carry a medical identification card or bracelet listing PML diagnosis, current medications, and emergency contact for neurology | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| For patients on natalizumab: JCV antibody index monitoring q6 months; discuss treatment switch with MS specialist if JCV index >1.5 and treatment duration >24 months | - | ROUTINE | ROUTINE | - |
| Maximize antiretroviral adherence to maintain immune function and prevent PML recurrence/progression; use pill organizers, alarms, or directly observed therapy if needed | - | ROUTINE | ROUTINE | - |
| Home safety modifications for visual field deficits, weakness, and cognitive impairment: remove trip hazards, improve lighting, install grab bars, consider stair gates | - | ROUTINE | ROUTINE | - |
| Advance care planning discussions early given variable but often poor prognosis; designate healthcare proxy; document code status and treatment preferences | - | ROUTINE | ROUTINE | - |
| Infection avoidance: hand hygiene, avoid sick contacts, avoid raw/undercooked foods; immunocompromised patients at higher risk for opportunistic infections | - | ROUTINE | ROUTINE | - |
| Nutrition optimization: adequate protein and caloric intake; consult dietitian if weight loss or poor appetite; address swallowing difficulties if present | - | ROUTINE | ROUTINE | - |
| Caregiver education: teach recognition of seizures, IRIS symptoms, and neurological decline; ensure caregiver knows when to call 911 vs. neurology clinic | - | ROUTINE | ROUTINE | - |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| CNS lymphoma (primary) | Periventricular enhancing lesions; homogeneous enhancement; may be multifocal; immunocompromised patients at risk for both | MRI (PML: no enhancement; lymphoma: enhancing); CSF cytology/flow cytometry; brain biopsy |
| HIV encephalopathy | Diffuse white matter changes; symmetric; no focal lesions; more gradual cognitive decline | MRI (diffuse vs multifocal); CSF JCV PCR negative; clinical course (slower); HIV viral load correlation |
| MS (new or breakthrough) | In natalizumab patients; new MS lesions vs PML; MS lesions typically periventricular, smaller, enhance | MRI pattern (MS: periventricular, enhancing; PML: subcortical U-fibers, no enhancement); CSF JCV PCR |
| Posterior reversible encephalopathy syndrome (PRES) | Posterior-predominant vasogenic edema; hypertension; seizures; reversible | MRI (posterior vasogenic edema on ADC; PML: restricted diffusion); clinical context; BP |
| Acute disseminated encephalomyelitis (ADEM) | Post-infectious; encephalopathy; large lesions; enhancing; monophasic; responds to steroids | CSF JCV PCR negative; clinical context (post-infectious); MRI (enhancing lesions); steroid-responsive |
| Natalizumab-associated IRIS without PML | Inflammatory MRI changes on natalizumab cessation without true PML; JCV PCR negative | CSF JCV PCR negative; MRI may show enhancement but no typical PML lesion pattern |
| Toxoplasmosis (CNS) | Ring-enhancing lesions; mass effect; CD4 usually <100; anti-Toxoplasma IgG positive | MRI (ring enhancement, mass effect — not typical of PML); Toxoplasma IgG; response to empiric treatment |
| CMV encephalitis | Periventricular enhancement; cranial neuropathies; polyradiculopathy; CD4 <50 | CSF CMV PCR; periventricular enhancement pattern; ependymal involvement |
| Cerebral small vessel disease | Chronic symmetric white matter hyperintensities; vascular risk factors; non-progressive or slowly progressive | MRI (symmetric, chronic-appearing); clinical context (vascular risk factors); no JCV in CSF |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| MRI brain with/without contrast | Q4-8 weeks during active disease; then q3 months | Stabilization or improvement of lesions; no new lesions; resolution of IRIS enhancement | Adjust immune reconstitution strategy; treat IRIS if new enhancement with edema; consider biopsy if atypical | - | ROUTINE | ROUTINE | - |
| CSF JCV PCR (quantitative) | Repeat at 2-4 weeks if initially negative with high suspicion; q3 months if positive | Declining or undetectable JCV copies | If rising, assess immune reconstitution adequacy; consider more aggressive approach | - | ROUTINE | ROUTINE | - |
| CD4 count (HIV patients) | Q4-8 weeks after ART initiation; then q3 months | Rising CD4; target >200 | Optimize ART; check resistance; ID consultation | - | ROUTINE | ROUTINE | - |
| HIV viral load | Q4 weeks until undetectable; then q3 months | Undetectable (<50 copies/mL) | Assess adherence; resistance testing; regimen change | - | ROUTINE | ROUTINE | - |
| Neurological examination | Q1-2 days inpatient; each outpatient visit | Stable or improving | Treat IRIS if worsening with inflammation; reassess management if worsening without IRIS (progressive PML) | STAT | ROUTINE | ROUTINE | STAT |
| Blood glucose (during steroids) | Q6h during IV steroids; daily during oral taper | <180 mg/dL | Insulin sliding scale; endocrine consult if persistent >250 | STAT | ROUTINE | ROUTINE | STAT |
| Blood pressure | Q shift during steroids; each outpatient visit | <160/100 mmHg | Antihypertensives PRN; dose adjustment if sustained hypertension | STAT | ROUTINE | ROUTINE | STAT |
| Seizure monitoring | Daily inpatient; each outpatient visit | No seizures | Adjust anticonvulsant dosing; obtain EEG; neurology reassessment | STAT | ROUTINE | ROUTINE | STAT |
| Cognitive function (formal) | Each visit; formal neuropsychological testing q3-6 months | Stable or improving on serial assessments | Neuropsychological referral; cognitive rehabilitation; consider donepezil/memantine | - | ROUTINE | ROUTINE | - |
| Lymphocyte subsets (CD4, CD8) | Q2-4 weeks during active IRIS; then q3 months | Normalizing counts; CD4 >200 in HIV | Adjust immune reconstitution; reassess immunosuppression discontinuation timeline | - | ROUTINE | ROUTINE | - |
| LFTs (if on maraviroc, mirtazapine, or ART) | Baseline; q2-4 weeks initially; then q3 months | Normal ALT/AST | Hold hepatotoxic medications; dose adjust; hepatology consultation if severe | - | ROUTINE | ROUTINE | - |
| Renal function (if on cidofovir or tenofovir) | Before each cidofovir dose; q3 months on ART | Cr <1.5; stable GFR | Hold cidofovir if Cr >1.5; adjust tenofovir; nephrology referral | - | ROUTINE | ROUTINE | - |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Admit to floor | All new PML diagnoses; ART initiation/optimization; natalizumab cessation with PLEX; serial neurological monitoring; IRIS management |
| Admit to ICU | Severe cerebral edema with herniation risk; status epilepticus; severe IRIS with mass effect; respiratory compromise |
| Discharge from hospital | Neurologically stable or improving; on appropriate immune reconstitution therapy; seizures controlled; safe home environment; close outpatient follow-up arranged (neurology q2-4 weeks; ID for HIV) |
| Outpatient follow-up (neurology) | All patients: q2-4 weeks during active disease; MRI q4-8 weeks; transition to q3 months when stable |
| Outpatient follow-up (ID/HIV) | HIV patients: q2-4 weeks for ART optimization; viral load and CD4 monitoring |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| CSF JCV PCR is the definitive diagnostic test for PML; sensitivity 72-92% | Class I, Level B | [Berger JR et al. Ann Neurol 2013](https://pubmed.ncbi.nlm.nih.gov/23526723/) |
| ART is the primary treatment for HIV-PML; immune reconstitution improves survival | Class I, Level B | [Marzocchetti A et al. Neurology 2009](https://pubmed.ncbi.nlm.nih.gov/19564582/) |
| Natalizumab-associated PML: PLEX accelerates drug clearance and immune reconstitution | Class IIa, Level C | [Clifford DB et al. Neurology 2010](https://pubmed.ncbi.nlm.nih.gov/20975054/) |
| PML-IRIS occurs in ~15-25% of HIV-PML patients starting ART; corticosteroids are standard treatment | Class IIa, Level C | [Tan K et al. J Neurovirol 2009](https://pubmed.ncbi.nlm.nih.gov/19370545/) |
| Mirtazapine as adjunctive therapy (5-HT2A antagonism blocks JCV entry): limited clinical evidence | Class IIb, Level C | [Elphick GF et al. Science 2004](https://pubmed.ncbi.nlm.nih.gov/15528448/) |
| Pembrolizumab (anti-PD-1) for non-HIV PML: case series showing potential benefit | Class IIb, Level C | [Cortese I et al. N Engl J Med 2019](https://pubmed.ncbi.nlm.nih.gov/31050378/) |
| JCV antibody index stratifies natalizumab-PML risk | Class IIa, Level B | [Plavina T et al. Ann Neurol 2014](https://pubmed.ncbi.nlm.nih.gov/25164539/) |
| AAN practice guideline on PML risk stratification with natalizumab | Guideline | [McGuigan C et al. Neurology 2016](https://pubmed.ncbi.nlm.nih.gov/26764028/) |

---

## NOTES

- PML carries significant mortality: ~50% in HIV (improved with ART); up to 30-50% in natalizumab-PML; highly variable in other immunosuppression
- JCV PCR sensitivity is ~72-92%; a NEGATIVE CSF JCV PCR does NOT exclude PML — repeat LP in 2-4 weeks if clinical suspicion remains high
- Brain biopsy remains the gold standard but is reserved for cases where CSF JCV PCR is repeatedly negative with high clinical suspicion
- Classic MRI: multifocal, bilateral, asymmetric subcortical white matter T2/FLAIR lesions involving U-fibers; NO enhancement (enhancement suggests IRIS); NO mass effect
- PML-IRIS: paradoxical worsening 1-5 weeks after immune reconstitution; contrast enhancement and edema appear on MRI; inflammatory CSF; treat with corticosteroids
- The balance between treating IRIS (steroids = immunosuppression) and allowing immune clearance of JCV is the central management challenge
- Natalizumab-PML: risk factors are JCV antibody index >1.5, prior immunosuppression, and treatment duration >24 months; monitoring JCV index q6 months is essential
- Mirtazapine is commonly used despite limited evidence because of favorable safety profile and theoretical mechanism (5-HT2A receptor blockade prevents JCV cell entry)
- Cidofovir has NOT shown clinical benefit in controlled studies despite in vitro activity; not routinely recommended
- Pembrolizumab (anti-PD-1) is emerging for non-HIV PML but carries risks of IRIS and autoimmune complications; use in selected patients with informed consent
- Survivors often have significant residual neurological disability; early rehabilitation is important

---

## CHANGE LOG

**v1.1 (February 11, 2026)**
- Restructured Section 3 to standard subsection format: 3A Acute/Emergent, 3B Symptomatic, 3C Maintenance/Chronic, 3D Investigational/Immune Reconstitution
- Expanded 3B Symptomatic from 2 meds to 16 meds covering seizures (levetiracetam, lacosamide, valproic acid), neuropathic pain (gabapentin, pregabalin), spasticity (baclofen, tizanidine), mood (sertraline, escitalopram, mirtazapine), fatigue (modafinil, methylphenidate), cognitive (donepezil, memantine), GI prophylaxis (omeprazole)
- Added 3C Maintenance/Chronic section with ongoing ART, mirtazapine adjunctive, maraviroc, dexamethasone taper
- Restructured 3D as Investigational/Immune Reconstitution with Pre-Treatment Requirements column; added nivolumab and IL-7
- Moved PML-IRIS steroids and cerebral edema management into 3A Acute
- Added acute levetiracetam loading to 3A
- Enhanced 4A Referrals: added neuropsychology, social work; improved ED/ICU coverage for neuroradiology, palliative care, neurosurgery
- Enhanced 4B Patient Instructions from 5 to 8 items: added medication adherence, IRIS flare warning, medical ID recommendation
- Enhanced 4C Lifestyle from 4 to 7 items: added infection avoidance, nutrition optimization, caregiver education
- Expanded Section 6 Monitoring from 7 to 13 parameters: added blood glucose, BP, lymphocyte subsets, LFTs, renal function monitoring
- Fixed setting coverage gaps: added ED tags for neuroradiology, added ICU tags for palliative care and physical therapy

**v1.0 (February 11, 2026)**
- Initial template creation
- Covers HIV-PML, natalizumab-PML, and other immunosuppression-associated PML
- IRIS management protocol
- CSF JCV PCR as cornerstone diagnostic test
- Evidence references with PubMed links
