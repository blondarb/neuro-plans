---
title: "Progressive Multifocal Leukoencephalopathy (PML)"
description: "Clinical decision support for diagnosis and management of PML"
version: "1.0"
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

**VERSION:** 1.0
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Draft

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
| LDH | - | ROUTINE | - | - | Prognostic marker; elevated associated with worse outcomes | Normal |
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
| EEG (CPT 95816) | - | ROUTINE | - | ROUTINE | If seizures occur; encephalopathy assessment | Focal or diffuse slowing; epileptiform activity at lesion borders | None |

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

### 3A. Immune Reconstitution (Primary Strategy)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Antiretroviral therapy (ART) initiation (HIV-PML) | PO | HIV-associated PML; ART is the ONLY proven effective treatment; immune reconstitution allows immune clearance of JCV | Per HIV guidelines :: PO :: daily :: Initiate ART as soon as possible; integrase inhibitor-based regimen preferred (dolutegravir + tenofovir/emtricitabine); rapid ART start; coordinate with HIV specialist | None (benefit outweighs all risks in PML) | CD4 count q4-8wk; HIV viral load q4wk until undetectable; hepatic/renal function; IRIS monitoring | STAT | STAT | ROUTINE | STAT |
| Natalizumab cessation + PLEX (natalizumab-PML) | Apheresis | Natalizumab-associated PML; remove drug to allow immune reconstitution; PLEX accelerates natalizumab clearance | 5 exchanges :: Apheresis :: every other day :: Discontinue natalizumab immediately; 5 plasma exchanges over 10 days to accelerate drug clearance (natalizumab half-life ~16 days; PLEX reduces to days) | Hemodynamic instability; coagulopathy | IRIS monitoring (typically occurs 1-5 weeks after PLEX); MRI q2-4wk; clinical exam q1-2 days | - | STAT | - | STAT |
| Discontinue causative immunosuppression (other-PML) | - | PML from rituximab, mycophenolate, fludarabine, or other immunosuppressants | Discontinue immediately :: - :: - :: Stop the causative immunosuppressant; no PLEX equivalent for most drugs; immune reconstitution occurs over weeks-months depending on drug | Balance with underlying disease management | CD4 and lymphocyte counts q2-4wk; MRI q4-8wk; clinical monitoring for IRIS | - | STAT | ROUTINE | STAT |

### 3B. PML-IRIS Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Dexamethasone (PML-IRIS) | IV/PO | Moderate-severe PML-IRIS with significant edema, mass effect, or clinical deterioration from inflammation | 4 mg IV/PO q6h; 8 mg IV/PO q6h :: IV/PO :: q6h :: Start 4-8 mg IV q6h for severe IRIS; taper over 2-6 weeks based on clinical response; shortest effective course to avoid further immunosuppression | Active untreated infection (relative); recognize that steroids also suppress beneficial immune response against JCV | Clinical exam; MRI q2-4wk for edema/enhancement resolution; steroid side effects; balance IRIS suppression vs JCV clearance | - | URGENT | ROUTINE | URGENT |
| Methylprednisolone (PML-IRIS) | IV | Fulminant PML-IRIS with severe cerebral edema and herniation risk | 1000 mg daily x 3-5 days :: IV :: daily x 3-5 days :: 1000 mg IV daily for 3-5 days for life-threatening IRIS; follow with oral steroid taper | Mass effect with herniation (may need neurosurgical intervention first) | ICP; neurological exam; MRI; blood glucose; BP | - | STAT | - | STAT |
| Maraviroc | PO | Adjunctive PML-IRIS treatment; CCR5 antagonist may reduce inflammatory infiltrate; limited evidence | 300 mg BID :: PO :: BID :: 300 mg PO BID; used as adjunct to steroids for IRIS; limited evidence; case reports/series suggest benefit | Severe hepatic impairment; concurrent strong CYP3A4 inhibitors (dose adjust) | LFTs; clinical response; hepatotoxicity; postural hypotension | - | EXT | EXT | - |

### 3C. Investigational/Adjunctive Therapies (Limited Evidence)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Mirtazapine | PO | 5-HT2A receptor antagonist; may block JCV entry into glial cells; in vitro evidence; unproven clinically but commonly used given favorable safety profile | 15 mg qHS; 30 mg qHS; 45 mg qHS :: PO :: qHS :: Start 15 mg qHS; titrate to 30-45 mg qHS; 5-HT2A receptor used by JCV for cell entry; theoretical benefit; limited clinical evidence | Concurrent MAOIs | Sedation; weight gain; dry mouth | - | ROUTINE | ROUTINE | - |
| Cidofovir | IV | Antiviral with in vitro activity against JCV; clinical trials have NOT shown clear benefit; not recommended routinely | 5 mg/kg q1-2wk :: IV :: q1-2wk :: 5 mg/kg IV weekly x 2 then every 2 weeks; must give with probenecid and IV hydration; nephrotoxic; CLINICAL TRIALS HAVE NOT SHOWN BENEFIT | Renal insufficiency (Cr >1.5); concurrent nephrotoxins | Renal function (Cr before each dose); proteinuria; neutrophil count; limited evidence of efficacy | - | EXT | - | - |
| Pembrolizumab | IV | PD-1 checkpoint inhibitor; immune reconstitution approach; emerging evidence in non-HIV PML; restores T-cell function against JCV | 2 mg/kg q4-6wk :: IV :: q4-6wk :: 2 mg/kg IV every 4-6 weeks; limited case series; risk of autoimmune complications and severe IRIS; informed consent essential | Autoimmune disease; organ transplant recipients (rejection risk); severe IRIS already present | Immune-related adverse events (thyroid, hepatic, colitis, pneumonitis); IRIS; clinical response; JCV PCR | - | EXT | EXT | - |

### 3D. Supportive/Symptomatic

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levetiracetam | IV/PO | Seizure prophylaxis/treatment (seizures common in PML, especially with cortical lesions) | 500 mg BID; 1000 mg BID; 1500 mg BID :: PO :: BID :: Start 500 mg BID; titrate to 1000-1500 mg BID; adjust for renal function | Severe renal impairment (dose adjust) | Mood changes; sedation; renal function | STAT | ROUTINE | ROUTINE | STAT |
| Dexamethasone (cerebral edema) | IV | Cerebral edema from PML lesions or IRIS causing mass effect | 4 mg q6h; 10 mg load then 4 mg q6h :: IV :: q6h :: 10 mg IV load, then 4 mg q6h; taper as edema resolves; use shortest effective course | Active untreated infection | Blood glucose; BP; GI protection; clinical response | URGENT | URGENT | - | URGENT |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation for PML diagnosis confirmation, IRIS management, and serial monitoring | STAT | STAT | ROUTINE | STAT |
| Infectious disease consultation for HIV-PML (ART optimization) and non-HIV immunosuppression management | STAT | STAT | ROUTINE | STAT |
| Neuroradiology review for MRI pattern characterization and serial imaging comparison | - | ROUTINE | ROUTINE | - |
| Physical therapy for motor rehabilitation, mobility assessment, and adaptive equipment | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL assessment, adaptive strategies for visual and motor deficits | - | ROUTINE | ROUTINE | - |
| Speech therapy for aphasia, dysarthria, and dysphagia assessment | - | ROUTINE | ROUTINE | - |
| Palliative care for goals of care discussion, symptom management, and advance care planning given poor prognosis in many cases | - | ROUTINE | ROUTINE | - |
| Neurosurgery consultation only if brain biopsy needed for diagnosis (CSF JCV PCR negative with high clinical suspicion) | - | EXT | - | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Report any new neurological symptoms (weakness, vision changes, speech difficulty, confusion) immediately, as PML can progress rapidly and treatment adjustments may be needed | STAT | ROUTINE | ROUTINE | - |
| Do NOT stop antiretroviral therapy (if HIV-positive) under any circumstances; ART is the single most important treatment for HIV-PML | - | ROUTINE | ROUTINE | - |
| Understand that worsening after starting ART (HIV) or stopping natalizumab may represent IRIS — a paradoxical inflammatory response that is expected and treatable | - | ROUTINE | ROUTINE | - |
| Seizure precautions: avoid driving until seizure risk assessed; do not swim or bathe alone; fall precautions at home | - | ROUTINE | ROUTINE | - |
| Follow-up appointments and MRIs are critical — do not miss scheduled imaging, as PML requires close monitoring | - | - | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| For patients on natalizumab: JCV antibody monitoring q6 months; consider treatment switch if JCV index >1.5 and treatment duration >24 months | - | - | ROUTINE | - |
| Maximize antiretroviral adherence to maintain immune function and prevent PML recurrence/progression | - | ROUTINE | ROUTINE | - |
| Home safety modifications for visual field deficits, weakness, and cognitive impairment | - | ROUTINE | ROUTINE | - |
| Advance care planning discussions early given variable but often poor prognosis | - | ROUTINE | ROUTINE | - |

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
| MRI brain with/without contrast | Q4-8 weeks during active disease; then q3 months | Stabilization → improvement of lesions; no new lesions; resolution of IRIS enhancement | Adjust immune reconstitution strategy; treat IRIS if new enhancement with edema; consider biopsy if atypical | - | ROUTINE | ROUTINE | - |
| CSF JCV PCR (quantitative) | Repeat at 2-4 weeks if initially negative with high suspicion; q3 months if positive | Declining or undetectable JCV copies | If rising, assess immune reconstitution adequacy; consider more aggressive approach | - | ROUTINE | ROUTINE | - |
| CD4 count (HIV patients) | Q4-8 weeks after ART initiation; then q3 months | Rising CD4; target >200 | Optimize ART; check resistance; ID consultation | - | ROUTINE | ROUTINE | - |
| HIV viral load | Q4 weeks until undetectable; then q3 months | Undetectable (<50 copies/mL) | Assess adherence; resistance testing; regimen change | - | ROUTINE | ROUTINE | - |
| Neurological examination | Q1-2 days inpatient; each outpatient visit | Stable or improving | Treat IRIS if worsening with inflammation; reassess management if worsening without IRIS (progressive PML) | STAT | ROUTINE | ROUTINE | STAT |
| Seizure monitoring | Daily inpatient; each outpatient visit | No seizures | Adjust anticonvulsant; EEG monitoring | - | ROUTINE | ROUTINE | ROUTINE |
| Cognitive function | Each visit; formal testing q3-6 months | Stable or improving | Neuropsychological referral; rehabilitation | - | - | ROUTINE | - |

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

**v1.0 (February 11, 2026)**
- Initial template creation
- Covers HIV-PML, natalizumab-PML, and other immunosuppression-associated PML
- IRIS management protocol
- CSF JCV PCR as cornerstone diagnostic test
- Evidence references with PubMed links
