---
title: Glioblastoma (GBM)
description: Comprehensive clinical decision support for glioblastoma (IDH-wildtype, WHO grade 4) including diagnosis, surgical management, Stupp protocol, and recurrence treatment.
version: "1.1"
setting: ED, HOSP, OPD, ICU
status: draft
tags:
  - neuro-oncology
  - brain-tumor
  - glioma
  - neurosurgery
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Glioblastoma (GBM)

**VERSION:** 1.1
**CREATED:** January 30, 2026
**REVISED:** January 30, 2026
**STATUS:** Draft - Revised per checker pipeline

---

**DIAGNOSIS:** Glioblastoma (GBM), IDH-wildtype, WHO Grade 4

**ICD-10:** C71.9 (Malignant neoplasm of brain, unspecified), C71.0 (Malignant neoplasm of cerebral lobe, frontal), C71.1 (Malignant neoplasm of cerebral lobe, temporal), C71.2 (Malignant neoplasm of cerebral lobe, parietal), C71.3 (Malignant neoplasm of cerebral lobe, occipital), C71.4 (Malignant neoplasm of cerebral ventricle), C71.5 (Malignant neoplasm of other parts of cerebrum), C71.6 (Malignant neoplasm of cerebellum), C71.7 (Malignant neoplasm of brainstem), C71.8 (Malignant neoplasm of overlapping sites of brain), D49.6 (Neoplasm of unspecified behavior of brain), G93.6 (Cerebral edema)

**SYNONYMS:** Glioblastoma, GBM, glioblastoma multiforme, grade 4 glioma, high-grade glioma, HGG, malignant glioma, IDH-wildtype glioblastoma, WHO grade 4 astrocytoma, primary brain tumor, primary malignant brain tumor, astrocytoma grade IV, anaplastic astrocytoma IDH-wildtype with molecular features of glioblastoma, gliosarcoma, giant cell glioblastoma, epithelioid glioblastoma, brain cancer, cerebral glioblastoma

**SCOPE:** Comprehensive management of newly diagnosed and recurrent glioblastoma (IDH-wildtype, WHO grade 4) in adults. Covers initial presentation and stabilization, neuroimaging evaluation (MRI with gadolinium, perfusion MRI, MR spectroscopy), histopathologic and molecular profiling (MGMT promoter methylation, TERT promoter mutation, EGFR amplification, +7/-10 chromosome changes), surgical planning (maximal safe resection, stereotactic biopsy), standard Stupp protocol (concurrent temozolomide + radiation followed by adjuvant temozolomide), tumor treating fields (TTFields/Optune), recurrence management (bevacizumab, lomustine, re-resection), supportive care (dexamethasone, seizure management), and palliative care integration. Excludes pediatric gliomas, IDH-mutant astrocytomas, oligodendrogliomas, and brain metastases (separate templates).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential (CPT 85025) | Baseline before surgery and chemotherapy; leukocytosis screen; platelet count for surgical candidacy and temozolomide eligibility | WBC, platelets within normal limits; ALC for treatment planning | STAT | STAT | ROUTINE | STAT |
| CMP (BMP + LFTs) (CPT 80053) | Renal function for contrast imaging; hepatic function for chemotherapy dosing; electrolytes (SIADH risk with brain lesions); glucose (steroid-induced hyperglycemia baseline) | Normal; anticipate glucose elevation with dexamethasone | STAT | STAT | ROUTINE | STAT |
| PT/INR, aPTT (CPT 85610+85730) | Coagulopathy assessment for surgical candidacy; glioblastoma patients have elevated VTE risk | Normal | STAT | STAT | ROUTINE | STAT |
| Blood glucose (CPT 82947) | Steroid-induced hyperglycemia baseline; pre-operative assessment | <180 mg/dL; start insulin if persistently elevated on steroids | STAT | STAT | ROUTINE | STAT |
| TSH (CPT 84443) | Fatigue and cognitive symptom differential; baseline before radiation therapy | Normal | - | ROUTINE | ROUTINE | - |
| Type and screen | Pre-operative; anticipate intraoperative blood loss during craniotomy | Available for crossmatch | STAT | STAT | - | STAT |
| Pregnancy test (women of childbearing age) (CPT 81025) | Temozolomide is teratogenic (Category D); radiation contraindicated in pregnancy | Negative | STAT | STAT | ROUTINE | STAT |
| HbA1c (CPT 83036) | Glycemic status before initiating prolonged dexamethasone; perioperative glucose optimization | <7.0% (ideal); higher values require aggressive insulin management | - | ROUTINE | ROUTINE | - |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| LDH (CPT 83615) | Tumor burden marker; prognostic significance | Elevated may indicate aggressive disease | - | ROUTINE | ROUTINE | - |
| Troponin (CPT 84484) | If syncope or seizure presentation; cardiac evaluation before surgery | Normal | STAT | STAT | - | STAT |
| CPK/CK (CPT 82550) | Post-seizure rhabdomyolysis screen | Normal; elevated after prolonged seizures | URGENT | ROUTINE | - | STAT |
| Cortisol (AM) (CPT 82533) | If hypothalamic/pituitary involvement suspected; baseline before dexamethasone | Normal (>10 mcg/dL AM) | - | ROUTINE | ROUTINE | - |
| Prealbumin / Albumin (CPT 84134) | Nutritional status for surgical planning and chemoradiation tolerance; steroid-induced catabolism | Normal; low values predict poor surgical outcomes | - | ROUTINE | ROUTINE | - |
| HIV (CPT 87389) | Primary CNS lymphoma differential; immunosuppression assessment | Negative | - | ROUTINE | ROUTINE | - |
| ESR / CRP (CPT 85652+86140) | Infection differential (abscess vs. tumor); inflammatory markers | Normal | - | ROUTINE | ROUTINE | - |
| Ammonia (CPT 82140) | If on valproic acid for seizures; altered mental status workup | <35 micromol/L | - | ROUTINE | - | STAT |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Paraneoplastic antibody panel (serum) | If clinical presentation suggests paraneoplastic syndrome coexisting with glioblastoma | Negative | - | EXT | EXT | - |
| BRCA1/2 germline testing | Consider in young patients (<40 years) or family history of cancer; may affect treatment options | Variable | - | - | EXT | - |
| Li-Fraumeni syndrome screening (TP53 germline) | Young patients with glioblastoma (<45 years), personal or family history of multiple cancers | Negative | - | - | EXT | - |
| Circulating tumor DNA (ctDNA) | Emerging biomarker for treatment response monitoring and early recurrence detection | Baseline and serial monitoring | - | - | EXT | - |
| EBV serology / CSF EBV PCR | Primary CNS lymphoma differential if tissue diagnosis unclear | Negative | - | EXT | EXT | - |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast (CPT 70450) | Immediately upon presentation; first-line for acute symptoms (seizure, headache, focal deficit, altered mental status) | Hypodense mass with surrounding edema, calcification (rare in GBM), hemorrhage, midline shift, hydrocephalus; classic ring-enhancing lesion not visible without contrast | None in emergency | STAT | STAT | - | STAT |
| MRI brain with and without contrast (gadolinium) (CPT 70553) | Within 24h of presentation; GOLD STANDARD for glioblastoma; thin-cut (1mm) 3D T1 post-contrast sequences | Ring-enhancing mass with central necrosis; irregular thick enhancing rim; significant surrounding T2/FLAIR edema; hemorrhagic components; butterfly pattern if crossing corpus callosum; multifocal in 2-5% | MRI-incompatible implants; GFR <30 (gadolinium risk); severe claustrophobia | STAT | STAT | URGENT | STAT |
| CT chest/abdomen/pelvis with contrast (CPT 71260+74178) | Within 48h; rule out metastatic disease to brain (brain metastasis is more common than GBM); staging | No extracranial primary malignancy | Contrast allergy; renal impairment | - | URGENT | ROUTINE | - |
| ECG (12-lead) (CPT 93000) | Pre-operative baseline; QTc for anti-emetics and targeted therapies | Normal | None | STAT | STAT | ROUTINE | STAT |
| Chest X-ray (CPT 71046) | Pre-operative clearance; lung primary exclusion (most common source of brain metastases) | No lung mass; no effusion | Pregnancy (shield) | STAT | STAT | ROUTINE | STAT |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| MR perfusion (DSC or DCE) (CPT 70553) | With diagnostic MRI or pre-operative; differentiates high-grade glioma from low-grade or lymphoma | Elevated rCBV (>1.75) in enhancing region = high-grade glioma; hot spot mapping for biopsy targeting | Same as MRI | - | URGENT | ROUTINE | - |
| MR spectroscopy (MRS) (CPT 76390) | With diagnostic MRI; differentiates tumor from abscess or radiation necrosis | Elevated choline (Cho), reduced N-acetylaspartate (NAA), elevated Cho/NAA ratio (>2.0), elevated Cho/Cr ratio; lipid/lactate peak suggests necrosis/high grade | Same as MRI | - | URGENT | ROUTINE | - |
| Diffusion tensor imaging (DTI) / Tractography | Pre-operative planning; white matter tract mapping relative to tumor | Motor tract (corticospinal tract), language pathways (arcuate fasciculus), visual pathways relative to tumor margins; guides extent of resection | Same as MRI | - | ROUTINE | ROUTINE | - |
| Functional MRI (fMRI) (CPT 70554) | Pre-operative; motor and language cortex mapping for tumors near eloquent areas | Motor cortex activation; language lateralization (Broca, Wernicke); visual cortex if occipital location | Same as MRI; requires patient cooperation | - | ROUTINE | ROUTINE | - |
| MRI spine (whole) with contrast (CPT 72156+72157+72158) | If spinal symptoms present; staging for drop metastases (rare in GBM but occurs) | Leptomeningeal enhancement; drop metastases | Same as MRI | - | ROUTINE | ROUTINE | - |
| PET/CT (FDG or amino acid-based: FET, FDOPA) (CPT 78816) | Differentiating tumor from treatment-related changes; FET-PET superior to FDG for brain tumors; biopsy target guidance | FET uptake TBR >1.6 suggests tumor; hot spot for biopsy targeting; useful in recurrence vs. pseudoprogression | Pregnancy; uncontrolled diabetes (FDG) | - | ROUTINE | ROUTINE | - |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Intraoperative MRI (iMRI) | During craniotomy at centers with iMRI capability | Real-time assessment of extent of resection; residual enhancing tumor identification; enables additional resection during same surgery | Same as MRI; equipment compatibility | - | EXT | - | - |
| Awake craniotomy mapping | For tumors in eloquent cortex (motor strip, language areas); requires patient cooperation | Direct cortical stimulation to define functional boundaries; enables maximal safe resection | Unable to cooperate; severe aphasia; anxiety precluding awake procedure | - | EXT | - | - |
| Magnetoencephalography (MEG) | Pre-operative functional mapping; alternative to fMRI when fMRI not feasible | Language and motor cortex localization; epileptogenic focus mapping | Metal implants (some); limited availability | - | - | EXT | - |
| Thallium SPECT | When MR perfusion/spectroscopy equivocal for recurrence vs. radiation necrosis | Increased uptake = viable tumor; decreased uptake = necrosis | Pregnancy | - | - | EXT | - |

### LUMBAR PUNCTURE (CPT 62270)

**Indication:** Not routinely indicated in glioblastoma. Perform if leptomeningeal dissemination suspected (cranial nerve palsies, radiculopathy, meningismus), or if primary CNS lymphoma is in the differential and tissue biopsy not yet performed

**Timing:** URGENT if CNS lymphoma suspected; otherwise ROUTINE

**Volume Required:** 10-15 mL standard diagnostic

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | Elevated ICP from mass effect | 10-20 cm H2O | - | URGENT | ROUTINE | - |
| Cell count (tubes 1 and 4) (CPT 89051) | Leptomeningeal dissemination; infection differential | WBC <5; RBC 0 | - | URGENT | ROUTINE | - |
| Protein (CPT 84157) | Elevated in leptomeningeal disease, infection | 15-45 mg/dL | - | URGENT | ROUTINE | - |
| Glucose with serum glucose (CPT 82945) | Low in infection, carcinomatous meningitis | Normal (>60% serum) | - | URGENT | ROUTINE | - |
| Cytology (CPT 88104) | Malignant cells from leptomeningeal spread | Negative; positive = leptomeningeal glioblastoma (poor prognosis) | - | URGENT | ROUTINE | - |
| Flow cytometry (CPT 88184) | Primary CNS lymphoma differential | No monoclonal B-cell population | - | URGENT | ROUTINE | - |
| Gram stain and culture (CPT 87205, 87070) | Infection differential (abscess vs. tumor) | No organisms | - | URGENT | ROUTINE | - |

**Special Handling:** Cytology requires rapid transport (<1 hour). Flow cytometry requires fresh specimen at room temperature.

**Contraindications:** Significant mass effect, midline shift >5 mm, obstructive hydrocephalus, posterior fossa mass effect (herniation risk); coagulopathy (INR >1.5, platelets <50K); skin infection at LP site. ALWAYS obtain CT/MRI before LP.

---

## 3. TREATMENT

**CRITICAL:** Glioblastoma management requires multidisciplinary coordination (neurosurgery, neuro-oncology, radiation oncology, neuropathology). Treatment decisions depend on molecular profiling (especially MGMT methylation), extent of resection, age, and functional status.

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Dexamethasone (vasogenic edema) | IV/PO | Vasogenic edema from tumor; symptomatic mass effect; reduce peritumoral edema to improve neurologic function | 10 mg :: IV :: load, then 4 mg q6h :: 10 mg IV loading dose, then 4 mg IV/PO q6h; moderate symptoms: 4-8 mg/day; severe edema/herniation: 10 mg IV bolus then 4-8 mg q6h (up to 16-24 mg/day); taper as soon as clinically feasible over 2-4 weeks; GI prophylaxis with PPI while on steroids; symptomatic improvement typically within 24-72h | Active untreated infection; uncontrolled diabetes (relative); psychosis history (relative) | Glucose q6h (target <180 mg/dL), BP, mood/sleep, GI symptoms, signs of infection | STAT | STAT | URGENT | STAT |
| Lorazepam (acute seizure) | IV | Acute seizure termination; 20-40% of GBM patients present with seizures | 4 mg :: IV :: PRN seizure :: 0.1 mg/kg IV (max 4 mg/dose); may repeat x1 in 5 min; max 8 mg total | Acute narrow-angle glaucoma; severe respiratory depression without ventilator | RR, O2 sat, BP, sedation level; airway equipment at bedside | STAT | STAT | - | STAT |
| Levetiracetam (seizure - loading) | IV | Anti-seizure medication loading for new seizures; preferred in brain tumor patients due to no CYP enzyme induction (does not reduce efficacy of steroids, chemotherapy, or targeted agents) | 1500 mg :: IV :: load, then 500-1500 mg BID :: 1000-1500 mg IV load, then 500-1500 mg PO/IV BID; renal dosing if GFR <50 | None absolute; reduce dose if CrCl <50 | Behavioral changes (agitation, irritability); generally well tolerated | STAT | STAT | - | STAT |
| Mannitol (elevated ICP) | IV | Acute elevated ICP with herniation signs; bridge to definitive surgical intervention | 1 g/kg :: IV :: bolus :: 1-1.5 g/kg IV bolus over 15-20 min; may repeat 0.25-0.5 g/kg q4-6h; maintain serum osmolality <320 mOsm/kg | Anuria; severe dehydration; active intracranial bleeding (relative) | Serum osmolality q6h, serum sodium, I/O, renal function | STAT | - | - | STAT |
| Hypertonic saline (elevated ICP) | IV | Acute elevated ICP; alternative to mannitol; may be preferred in hypotensive patients | 30 mL :: IV :: bolus (23.4% via central line) :: 23.4% NaCl 30 mL via central line over 15 min OR 3% NaCl 250 mL IV over 30 min; target Na 145-155 mEq/L | Severe hypernatremia (Na >160) | Sodium q4-6h, serum osmolality, I/O, central line required for 23.4% | STAT | - | - | STAT |
| Airway management (obtunded patient) | - | GCS <=8; impending herniation; respiratory compromise | Per RSI protocol :: - :: - :: Intubation per RSI protocol; elevate HOB 30 degrees; maintain PaCO2 30-35 mmHg (brief hyperventilation as bridge only) | None in emergency | O2 sat, ETCO2, hemodynamics | STAT | - | - | STAT |
| Enoxaparin (DVT prophylaxis) | SC | Brain tumor patients have 20-30% VTE risk; sequential compression devices immediately; pharmacologic prophylaxis within 24-48h post-operatively | 40 mg :: SC :: daily :: Enoxaparin 40 mg SC daily or heparin 5000 units SC q8h; start within 24-48h unless hemorrhagic or planned surgery within 24h; post-craniotomy restart per neurosurgery (typically 24-48h) | Active intracranial hemorrhage; planned surgery within 24h | Platelet count; signs of bleeding | - | STAT | - | STAT |
| Pantoprazole (stress ulcer prophylaxis) | PO/IV | GI bleed prevention while on dexamethasone; combined corticosteroid + critical illness increases risk | 40 mg :: IV :: daily :: Pantoprazole 40 mg IV/PO daily OR omeprazole 20 mg PO daily; continue throughout steroid course | PPI allergy | GI symptoms | STAT | STAT | ROUTINE | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levetiracetam (maintenance) | PO | Seizure prevention after first seizure; NO prophylactic AEDs in patients without seizures (AAN guideline) | 500 mg :: PO :: BID :: Start 500 mg BID; titrate by 500 mg/day q1-2 weeks to seizure control; max 3000 mg/day; renal dosing if GFR <50 | None absolute; reduce dose if CrCl <50 | Behavioral changes (agitation, depression, irritability), somnolence; generally well tolerated; no drug interactions with chemotherapy | - | STAT | ROUTINE | STAT |
| Lacosamide | PO/IV | Alternative or adjunct AED for seizures; minimal drug interactions with chemotherapy | 50 mg :: PO :: BID :: Start 50 mg BID; titrate by 50 mg/dose weekly; max 400 mg/day | PR interval >200 ms; 2nd/3rd degree AV block; severe hepatic impairment | ECG at baseline and with dose changes; PR interval monitoring | - | STAT | ROUTINE | STAT |
| Valproic acid | PO/IV | Second-line AED; some preclinical data suggesting synergy with temozolomide via HDAC inhibition (clinical significance uncertain) | 250 mg :: PO :: BID :: Start 250 mg BID; titrate by 250 mg q3-5 days to therapeutic level (50-100 mcg/mL); max 60 mg/kg/day | Hepatic disease; mitochondrial disorders (Alpers syndrome); pregnancy (teratogenic); urea cycle disorders; pancreatitis history | LFTs at baseline and periodically; ammonia if AMS; CBC (thrombocytopenia may limit chemotherapy); VPA level | - | ROUTINE | ROUTINE | ROUTINE |
| Ondansetron | IV/PO | Nausea/vomiting from elevated ICP, chemotherapy, or radiation | 4 mg :: IV :: q8h PRN :: 4-8 mg IV/PO q8h PRN nausea; max 24 mg/day | QT prolongation; concurrent use of QT-prolonging agents | QTc if risk factors; serotonin syndrome risk with SSRIs | STAT | STAT | ROUTINE | STAT |
| Acetaminophen | PO | Headache from elevated ICP; avoid NSAIDs peri-operatively due to bleeding risk | 1000 mg :: PO :: q6h PRN :: 650-1000 mg PO q6h PRN headache; max 3 g/day (2 g/day if hepatic impairment) | Severe hepatic impairment; allergy | LFTs if prolonged use | STAT | STAT | ROUTINE | STAT |
| Dexamethasone (taper) | PO | Transition from IV to PO; taper as soon as clinically feasible to minimize steroid side effects; taper after surgery and/or after radiation | 4 mg :: PO :: q6h, then taper :: Taper by 2 mg every 3-5 days (e.g., 16 to 12 to 8 to 6 to 4 to 2 to 1 to off); slower taper if symptoms recur; monitor for adrenal insufficiency if >3 weeks of use | Symptom recurrence (hold taper, reassess) | Glucose, BP, mood, steroid myopathy (proximal weakness may mimic disease progression), immunosuppression, osteoporosis | - | ROUTINE | ROUTINE | - |
| Insulin (steroid-induced hyperglycemia) | SC/IV | Glucose management while on dexamethasone; 50-60% of patients on dexamethasone develop hyperglycemia | Variable :: SC :: per sliding scale :: Fingerstick glucose q6h; sliding scale insulin initially; basal-bolus if persistently >180 mg/dL; may need 2-3x baseline insulin on dexamethasone; anticipate glucose elevation 4-8h after steroid dose | Hypoglycemia risk | Glucose q6h (q1h if insulin drip) | STAT | STAT | ROUTINE | STAT |
| TMP-SMX (PJP prophylaxis) | PO | Pneumocystis prophylaxis during concurrent temozolomide + radiation (Stupp protocol); lymphopenia risk | 1 DS tablet :: PO :: MWF :: TMP-SMX 1 DS tablet 3x/week (Mon/Wed/Fri) during concurrent chemoradiation and for 1 month after; continue if CD4 <200 or ALC <500 | Sulfa allergy (use atovaquone 1500 mg daily or dapsone 100 mg daily as alternatives); renal impairment | CBC; renal function; rash | - | ROUTINE | ROUTINE | - |
| Calcium + Vitamin D | PO | Steroid-induced osteoporosis prevention while on prolonged dexamethasone (>2 weeks) | 1000 mg Ca + 800 IU Vit D :: PO :: daily :: Calcium 1000-1200 mg + Vitamin D 800-1000 IU daily while on steroids | Hypercalcemia; renal stones (relative) | Calcium level; vitamin D level | - | ROUTINE | ROUTINE | - |
| Methylphenidate (cancer-related fatigue) | PO | Cancer-related fatigue; cognitive slowing from tumor or treatment; may improve alertness and concentration during chemoradiation | 5 mg :: PO :: BID (AM and noon) :: Start 5 mg PO BID (morning and noon); titrate by 5 mg/dose q3-7 days; max 40 mg/day; avoid evening dosing; reassess need monthly | Uncontrolled hypertension; tachyarrhythmia; severe anxiety; concurrent MAO inhibitors; glaucoma | Heart rate, BP, appetite, sleep quality, mood (agitation) | - | ROUTINE | ROUTINE | - |
| Memantine (neuroprotection during RT) | PO | Cognitive protection during radiation therapy; RTOG 0614 showed reduced cognitive decline at 24 weeks (emerging evidence; not yet standard of care) | 5 mg :: PO :: daily, titrate to 10 mg BID :: Start 5 mg PO daily; increase by 5 mg weekly (5 mg daily, 5 mg BID, 10 mg AM/5 mg PM, 10 mg BID); continue during and after radiation; max 20 mg/day | Severe renal impairment (CrCl <30); concurrent use of other NMDA antagonists | Renal function; dizziness; confusion; reassess benefit at 6 months | - | ROUTINE | ROUTINE | - |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Bevacizumab (Avastin) | IV | Recurrent glioblastoma; FDA-approved as monotherapy for recurrent GBM; anti-VEGF monoclonal antibody; reduces edema and may allow steroid taper; does not clearly improve overall survival but improves PFS and quality of life | 10 mg/kg :: IV :: q2 weeks :: 10 mg/kg IV every 2 weeks; infuse first dose over 90 min, then 60 min, then 30 min if tolerated; continue until progression or intolerable toxicity | Uncontrolled hypertension; recent (28 days) surgery or wound healing complications; active hemorrhage; bowel perforation risk; pregnancy; severe proteinuria (>3.5 g/24h) | BP each visit; urinalysis for proteinuria q2-4 weeks; wound healing assessment; CBC; signs of GI perforation, thromboembolism; hold 28 days before and after surgery | - | - | ROUTINE | - |
| Lomustine (CCNU) | PO | Recurrent glioblastoma; alkylating agent; can be combined with bevacizumab; single agent option for recurrence | 110 mg/m2 :: PO :: q6 weeks :: 110 mg/m2 PO as single dose every 6 weeks; reduce to 100 mg/m2 if prior myelosuppression; take on empty stomach; do not repeat until platelets >100K and WBC >4K | Severe myelosuppression; platelets <100K; WBC <4K; hepatic/renal impairment; pregnancy | CBC with differential weekly for 6 weeks after each dose (nadir at 4-6 weeks); LFTs; renal function; pulmonary function (cumulative pulmonary toxicity) | - | - | ROUTINE | - |
| Bevacizumab + Lomustine (combination) | IV/PO | Recurrent glioblastoma; EORTC 26101 trial showed PFS benefit (not OS) vs. lomustine alone; consider for good performance status patients | Bevacizumab 10 mg/kg q2wk + Lomustine 90 mg/m2 q6wk :: IV/PO :: per protocol :: Bevacizumab 10 mg/kg IV q2 weeks + Lomustine 90 mg/m2 PO q6 weeks (reduced dose when combined); monitor for combined toxicity | Per individual agents | Per individual agents; additional monitoring for combined myelosuppression | - | - | ROUTINE | - |
| Temozolomide rechallenge | PO | Recurrent GBM with prior temozolomide response; dose-dense or metronomic schedule; consider if long interval since initial treatment | 75 mg/m2 :: PO :: daily x 21/28 days :: Dose-dense: 75-150 mg/m2 PO daily x 21 days of 28-day cycle; metronomic: 50 mg/m2 PO daily continuous; take on empty stomach 1h before bed | Severe myelosuppression; prior temozolomide intolerance; hypersensitivity to dacarbazine | CBC weekly for first 2 cycles, then q2 weeks; LFTs monthly; watch for cumulative lymphopenia | - | - | ROUTINE | - |
| Re-resection (surgical) | - | Recurrent GBM amenable to resection; symptomatic mass effect not responsive to medical management; good performance status (KPS >=70) | Maximal safe resection :: - :: per neurosurgical assessment :: Maximal safe resection per neurosurgical assessment; consider 5-ALA fluorescence guidance; post-op MRI within 48h | Poor functional status (KPS <50); eloquent cortex involvement precluding safe resection; diffuse/multifocal recurrence | Post-op MRI within 48h; neurologic exams; wound monitoring | - | URGENT | - | - |
| Re-irradiation (SRS or fractionated) | - | Recurrent GBM; focal recurrence amenable to SRS; consider fractionated re-irradiation for larger volumes | 15 Gy :: - :: single fraction (SRS) :: SRS 12-18 Gy single fraction for focal lesions (<=3 cm); hypofractionated re-radiation (35 Gy in 10 fractions) for larger areas; consider cumulative brain dose constraints | Prior radiation dose limits exceeded; diffuse progression; brainstem tolerance | Radiation necrosis risk (advanced imaging with perfusion MRI q2-3 months); new neurologic deficits | - | - | ROUTINE | - |

### 3D. Disease-Modifying Therapies (Chemotherapy / Targeted / Adjuvant)

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Temozolomide - Concurrent with RT (Stupp Protocol Phase 1) | PO | Standard of care for newly diagnosed GBM; concurrent with focal radiation (60 Gy in 30 fractions); Stupp et al. NEJM 2005 demonstrated OS benefit (14.6 vs. 12.1 months) | 75 mg/m2 :: PO :: daily x 42 days :: 75 mg/m2 PO daily throughout radiation (42 consecutive days including weekends/holidays); take on empty stomach 1 hour before bedtime; antiemetic 30-60 min before (ondansetron 8 mg); PJP prophylaxis (TMP-SMX) mandatory | CBC with differential at baseline; weekly CBC during concurrent phase; hepatic function; renal function; MGMT methylation status (predicts response but treatment given regardless); negative pregnancy test; no active infection | ANC <1500; platelets <100K; severe hepatic/renal impairment; known hypersensitivity to temozolomide or dacarbazine; pregnancy/breastfeeding | CBC weekly during concurrent phase; if ANC <1000 or platelets <50K, hold temozolomide until recovery; LFTs q2 weeks; PJP prophylaxis; watch for severe lymphopenia (CD4 <200) | - | - | ROUTINE | - |
| Temozolomide - Adjuvant (Stupp Protocol Phase 2) | PO | Standard adjuvant chemotherapy following concurrent chemoradiation; 6 cycles of dose-dense temozolomide | 150 mg/m2 :: PO :: days 1-5 q28d :: Cycle 1: 150 mg/m2 PO days 1-5 of 28-day cycle; if tolerated (ANC >1500, platelets >100K), increase to 200 mg/m2 for cycles 2-6; take on empty stomach 1h before bedtime; antiemetic pre-medication; 6 cycles total | CBC on Day 22 of each cycle (nadir) and Day 1 of next cycle; hepatic function; renal function; adequate bone marrow recovery from concurrent phase | ANC <1500; platelets <100K on Day 1 of cycle; same as concurrent phase | CBC Day 1 and Day 22 of each cycle; LFTs monthly; MGMT methylation-positive patients have better response (median OS ~21 months vs. ~14 months); hold if ANC <1000 or platelets <50K until recovery; reduce dose by 50 mg/m2 for Grade 3-4 toxicity | - | - | ROUTINE | - |
| Radiation therapy (focal) | - | Standard of care concurrent with temozolomide; 60 Gy in 30 fractions to tumor bed + 2cm margin; for GBM in all age groups with good functional status | 60 Gy :: - :: 30 fractions (2 Gy/fraction) :: 60 Gy in 30 fractions over 6 weeks; begin within 3-6 weeks of surgery; concurrent with temozolomide 75 mg/m2 daily; MRI-based treatment planning with T1-post-contrast and FLAIR for target delineation | Simulation MRI within 2 weeks of starting RT; post-surgical MRI (within 48h of surgery) for planning; adequate wound healing; functional status assessment (KPS >=60) | Pregnancy; prior full-dose brain radiation (assess cumulative dose); very poor performance status (KPS <40) - consider hypofractionated or palliative | Weekly neurologic assessment during RT; MRI 4 weeks after RT completion (new baseline); then q2-3 months; watch for pseudoprogression (especially in MGMT methylated tumors) at 3-6 month post-RT MRI | - | - | ROUTINE | - |
| Radiation therapy (hypofractionated - elderly/poor KPS) | - | Alternative for elderly patients (>65-70 years) or poor functional status; Perry et al. NEJM 2017 showed benefit of adding temozolomide to hypofractionated RT in elderly | 40 Gy :: - :: 15 fractions (2.67 Gy/fraction) :: 40 Gy in 15 fractions (2.67 Gy/fraction) over 3 weeks; with or without concurrent temozolomide (75 mg/m2 daily); consider adjuvant temozolomide (6 cycles) if MGMT methylated | Post-surgical MRI for planning; functional status assessment | Same as standard RT; very poor KPS (<30) - consider temozolomide alone or best supportive care | Same as standard RT but with adjusted imaging schedule | - | - | ROUTINE | - |
| Tumor Treating Fields (TTFields / Optune) | TOP | FDA-approved for newly diagnosed GBM as adjuvant with temozolomide; alternating electric fields (200 kHz) disrupt mitosis; EF-14 trial: OS 20.9 vs. 16.0 months with temozolomide alone | Continuous :: TOP :: >=18 hours/day :: 4 transducer arrays applied to shaved scalp; continuous use >=18h/day for optimal benefit; worn during adjuvant temozolomide phase and beyond; continue until progression | Scalp measured and arrays prescribed by trained provider; head shaving; patient education and training session; compliance monitoring device built into system | Active implanted medical device in the brain (DBS, programmable shunt with metallic parts); skull defect with no bone flap replacement; sensitivity to conductive hydrogel; pregnancy | Compliance monitoring (>=18h/day target; <75% compliance reduces benefit); scalp skin assessment q2 weeks initially then monthly (contact dermatitis in ~16%); treat skin irritation with topical corticosteroids and array repositioning; quality of life assessment | - | - | ROUTINE | - |
| Temozolomide alone (elderly/poor KPS without RT) | PO | Elderly patients (>70) or poor functional status (KPS 30-60) who cannot tolerate radiation; consider if MGMT methylated (better response); Wick et al. Lancet Oncol 2012 (NOA-08) | 150 mg/m2 :: PO :: days 1-5 q28d :: Standard 5/28 day dosing (as per adjuvant protocol); MGMT methylation status guides decision: methylated = temozolomide preferred; unmethylated = consider RT alone or best supportive care | CBC baseline and Day 22; MGMT methylation status; hepatic/renal function | Same as concurrent/adjuvant temozolomide | Same as adjuvant temozolomide | - | - | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurosurgery STAT consultation for surgical candidacy evaluation, maximal safe resection planning, and ICP management for all patients with suspected high-grade glioma | STAT | STAT | ROUTINE | STAT |
| Neuro-oncology consultation for molecular profiling interpretation, Stupp protocol initiation, and long-term treatment planning | - | URGENT | ROUTINE | - |
| Radiation oncology consultation for treatment planning (60 Gy in 30 fractions or hypofractionated per age/KPS) to begin within 3-6 weeks post-surgery | - | URGENT | ROUTINE | - |
| Multidisciplinary tumor board presentation for coordinated treatment planning including neurosurgery, neuro-oncology, radiation oncology, neuropathology, and neuroradiology | - | URGENT | ROUTINE | - |
| Neuropathology consultation for comprehensive molecular profiling including IDH mutation, MGMT promoter methylation, TERT promoter mutation, EGFR amplification, +7/-10 chromosome status, and integrated WHO 2021 classification | - | URGENT | ROUTINE | - |
| Palliative care consultation for symptom management, goals of care discussion, and advance directive completion given median survival of 14-16 months | - | ROUTINE | ROUTINE | ROUTINE |
| Physical therapy for mobility assessment, fall prevention given steroid myopathy and neurologic deficits, and exercise program to mitigate deconditioning | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL assessment, cognitive compensation strategies, and home safety evaluation | - | ROUTINE | ROUTINE | - |
| Speech-language pathology for swallow evaluation if posterior fossa or brainstem involvement, and language assessment if dominant hemisphere tumor | - | ROUTINE | ROUTINE | - |
| Social work consultation for insurance authorization, disability paperwork, caregiver support, and community resource coordination | - | ROUTINE | ROUTINE | - |
| Neuropsychology evaluation for baseline cognitive assessment before radiation and chemotherapy to monitor treatment-related decline | - | - | ROUTINE | - |
| Genetic counseling if age <45 years, family history of cancer, or clinical suspicion for Li-Fraumeni or other cancer predisposition syndrome | - | - | ROUTINE | - |
| Psychiatry/psychology referral for depression, anxiety, and adjustment disorder management given diagnosis of malignant brain tumor | - | ROUTINE | ROUTINE | - |
| Ophthalmology consultation if visual field deficits, papilledema, or tumor near visual pathways | - | ROUTINE | ROUTINE | - |
| Endocrinology consultation if persistent steroid-induced hyperglycemia difficult to manage or hypothalamic/pituitary involvement | - | ROUTINE | ROUTINE | - |
| Clinical trials evaluation for eligible patients at all stages including newly diagnosed (novel combinations) and recurrence (immunotherapy, targeted agents, novel delivery) | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Return immediately for new or worsening headache, sudden weakness, vision changes, speech difficulty, or seizures (may indicate tumor progression, hemorrhage, or increased intracranial pressure) | STAT | STAT | ROUTINE | - |
| Do not drive until cleared by neurology and neurosurgery due to seizure risk, visual field deficits, and cognitive impairment | - | ROUTINE | ROUTINE | - |
| Do not stop dexamethasone abruptly as this may cause adrenal crisis; follow prescribed taper schedule exactly | - | ROUTINE | ROUTINE | - |
| Take temozolomide on empty stomach 1 hour before bedtime with antiemetic pre-medication to minimize nausea | - | ROUTINE | ROUTINE | - |
| Report any fever, unusual bruising, or signs of infection while on chemotherapy as this may indicate dangerous myelosuppression requiring urgent evaluation | - | ROUTINE | ROUTINE | - |
| For TTFields (Optune) users: maintain device use for at least 18 hours/day for optimal benefit; inspect scalp for skin irritation daily; contact device support team for technical issues | - | - | ROUTINE | - |
| Keep a symptom diary documenting headaches, seizures, weakness, cognitive changes, and mood to track treatment response | - | ROUTINE | ROUTINE | - |
| Discuss advance directive and healthcare proxy designation given diagnosis and expected disease course | - | ROUTINE | ROUTINE | - |
| Wear medical alert identification indicating brain tumor diagnosis and seizure risk | - | ROUTINE | ROUTINE | - |
| Avoid live vaccines during chemotherapy and steroid therapy due to immunosuppression | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Low-sodium diet while on dexamethasone to reduce fluid retention, edema, and hypertension | - | ROUTINE | ROUTINE | - |
| Blood sugar monitoring and diabetic diet while on steroids to prevent steroid-induced hyperglycemia complications | - | ROUTINE | ROUTINE | - |
| Regular low-impact exercise (walking, swimming, yoga) as tolerated to maintain strength, reduce steroid myopathy, and improve mood and quality of life | - | ROUTINE | ROUTINE | - |
| Fall precautions at home including removal of trip hazards, use of handrails, non-slip mats, and night lights given focal deficits, steroid myopathy, and seizure risk | - | ROUTINE | ROUTINE | - |
| Smoking cessation to optimize wound healing, radiation response, and reduce thrombotic risk | - | ROUTINE | ROUTINE | - |
| Alcohol avoidance during chemotherapy to prevent hepatotoxicity and avoid seizure threshold lowering | - | ROUTINE | ROUTINE | - |
| CPAP compliance if obstructive sleep apnea present to prevent nocturnal hypoxia which may worsen cerebral edema | - | ROUTINE | ROUTINE | - |
| Sun protection while on temozolomide due to photosensitivity risk | - | - | ROUTINE | - |
| Adequate hydration (2-3 L/day unless fluid restricted) during chemotherapy and steroid use to support renal function and prevent constipation | - | ROUTINE | ROUTINE | - |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Brain metastases | History of systemic malignancy; often multiple lesions (vs. GBM usually single); well-demarcated ring enhancement; located at gray-white junction; less infiltrative | CT chest/abdomen/pelvis; PET/CT for primary site; tissue biopsy (cytokeratin, TTF-1, melanoma markers); typically no IDH mutation, no GFAP expression |
| Primary CNS lymphoma (PCNSL) | Periventricular homogeneous enhancement (not ring-enhancing unless HIV); restricted diffusion on DWI; responds dramatically to corticosteroids ("ghost tumor"); immunocompromised patients | AVOID steroids before biopsy (may render non-diagnostic); DWI showing restricted diffusion; CSF flow cytometry; stereotactic biopsy; HIV testing; slit lamp exam for vitreous involvement |
| Brain abscess | Ring-enhancing with central restricted diffusion on DWI (bright DWI, dark ADC in cavity -- GBM does NOT show central restricted diffusion); thin smooth rim; fever, leukocytosis; recent ENT/dental/cardiac source | DWI is key differentiator (central restriction = abscess); MR spectroscopy (amino acid peaks: succinate, acetate); blood cultures; echocardiogram for endocarditis |
| IDH-mutant astrocytoma (WHO grade 2-4) | Younger patients (30-50 years); less aggressive imaging appearance; may lack ring enhancement; frontal lobe predilection; FLAIR mismatch sign in grade 2 | IDH1/2 mutation testing (positive); ATRX loss; p53 overexpression; no EGFR amplification; no +7/-10; prognosis significantly better than IDH-wildtype GBM |
| Oligodendroglioma (IDH-mutant, 1p/19q-codeleted) | "Fried egg" histology; calcifications common; cortical involvement; T2-FLAIR mismatch less common; typically younger patients | IDH mutation (positive); 1p/19q codeletion (defining feature); calcifications on CT; distinct molecular profile from GBM |
| Tumefactive multiple sclerosis | Younger patients; incomplete ring enhancement ("open ring sign"); less mass effect relative to size; clinical history of MS symptoms; other demyelinating lesions | MRI: open ring enhancement; CSF oligoclonal bands; MOG/AQP4 antibodies; clinical dissemination in time and space; response to corticosteroids with resolution |
| Toxoplasmosis (immunocompromised) | HIV/AIDS with CD4 <100; multiple ring-enhancing lesions; basal ganglia predilection; eccentric target sign | Toxoplasma IgG; CD4 count; empiric treatment trial (response in 10-14 days); if no response then biopsy; Thallium SPECT |
| Radiation necrosis | History of prior brain radiation (typically 6-24 months post-treatment); enhancing lesion at prior radiation site; challenging to distinguish from recurrent GBM on conventional MRI | MR perfusion (low rCBV in necrosis vs. high in tumor); MR spectroscopy (elevated lipid/lactate, low choline in necrosis); FET-PET; biopsy if equivocal |
| Cerebral infarct (subacute) | Vascular territory distribution; ring enhancement at 1-4 weeks post-stroke; clinical history of acute onset; DWI conforming to vascular territory | Vascular territory distribution; DWI/ADC map evolution; clinical history; MRA/CTA showing vascular occlusion |
| Gliomatosis cerebri pattern | Diffuse infiltration involving >=3 lobes; minimal or no enhancement; widespread T2/FLAIR abnormality; no discrete mass | MRI showing diffuse T2/FLAIR without focal enhancing mass; biopsy from most abnormal region; molecular profiling |

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Neurologic examination (motor, sensory, language, cognition, cranial nerves) | q2-4h inpatient; each clinic visit | Stable or improving; new deficits warrant urgent imaging | STAT MRI if decline; increase dexamethasone; neurosurgery alert if herniation | STAT | STAT | ROUTINE | STAT |
| Blood glucose | q6h while on dexamethasone (q1h if insulin drip) | <180 mg/dL | Sliding scale to basal-bolus insulin; endocrine consult if refractory | STAT | STAT | ROUTINE | STAT |
| CBC with differential | Weekly during concurrent chemoradiation; Day 1 and Day 22 of each adjuvant TMZ cycle | ANC >1500; platelets >100K; lymphocytes monitored for lymphopenia | Hold temozolomide if ANC <1000 or platelets <50K; PJP prophylaxis if CD4 <200 or ALC <500 | STAT | STAT | ROUTINE | STAT |
| Hepatic function (LFTs) | q2 weeks during concurrent TMZ; monthly during adjuvant TMZ | Normal | Dose reduce or hold temozolomide; hepatology consult if Grade 3-4 elevation | - | ROUTINE | ROUTINE | ROUTINE |
| Renal function (BUN/Cr) | Baseline; monthly during treatment | Normal | Adjust renally-cleared medications (levetiracetam, temozolomide) | STAT | STAT | ROUTINE | STAT |
| Serum sodium | q6-12h inpatient; each visit outpatient | 135-145 mEq/L | SIADH workup if <130; fluid restriction; hypertonic saline if <125 or symptomatic | STAT | STAT | ROUTINE | STAT |
| MRI brain with contrast | Post-op within 48h; 4 weeks post-RT (new baseline); then q2-3 months | Stable or decreasing enhancement; distinguish pseudoprogression from true progression | Tumor board discussion if progression suspected; advanced imaging (perfusion, spectroscopy, PET); rebiopsy if equivocal | - | URGENT | ROUTINE | - |
| Blood pressure | Continuous in ICU; q4h on floor; each clinic visit | SBP <160 | Antihypertensives; especially important if on bevacizumab (target <140/90) | STAT | STAT | ROUTINE | STAT |
| KPS / ECOG performance status | Each clinic visit | KPS >=60 for active treatment; KPS <50 reassess goals | KPS <40: consider transition to best supportive care/hospice | - | ROUTINE | ROUTINE | - |
| Seizure monitoring | Continuous inpatient; patient diary outpatient | No seizures | AED dose adjustment; consider cEEG if subclinical seizures suspected; verify medication compliance | STAT | STAT | ROUTINE | STAT |
| Body weight / nutritional status | Weekly inpatient; each clinic visit | Stable weight; adequate caloric intake | Dietitian referral; consider appetite stimulants; evaluate for steroid myopathy vs. cachexia | - | ROUTINE | ROUTINE | - |
| Depression / anxiety screening (PHQ-9) | Each clinic visit | PHQ-9 <5 | Psychiatry/psychology referral; SSRI initiation (avoid CYP interactions); supportive care | - | - | ROUTINE | - |
| TTFields compliance | Each clinic visit | >=18 hours/day usage | Patient education; troubleshoot barriers; scalp care for contact dermatitis | - | - | ROUTINE | - |
| Urinalysis (proteinuria) | q2-4 weeks if on bevacizumab | No proteinuria; <1+ | 24-hour urine if >2+; hold bevacizumab if nephrotic range (>3.5 g/24h) | - | - | ROUTINE | - |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| ICU admission | GCS <=12; signs of herniation (pupil asymmetry, posturing, Cushing triad); acute hemorrhage into tumor; status epilepticus; post-craniotomy (first 24h per institutional protocol); respiratory compromise requiring intubation; hemodynamic instability |
| General neurology/neurosurgery floor | New diagnosis requiring workup and stabilization; symptomatic edema requiring IV dexamethasone with close glucose monitoring; post-craniotomy step-down from ICU (typically POD 1-2); seizures requiring AED optimization and observation; functional decline requiring inpatient rehabilitation planning |
| Observation (<=24h) | Known GBM with mild symptom worsening on stable regimen; MRI showing possible progression requiring multidisciplinary discussion; steroid dose adjustment with monitoring |
| Discharge home | Neurologically stable for >=24h; seizure-free >=24h on oral AED; oral dexamethasone taper plan established with written instructions; glucose management plan in place; pain controlled on oral medications; treatment plan established with scheduled appointments (neurosurgery, neuro-oncology, radiation oncology within 1-2 weeks); safe ambulation and ADLs or adequate caregiver; patient/family education completed |
| Transfer to higher level care | Need for neurosurgical expertise not available; tumor board or neuro-oncology consultation not available; need for specialized intraoperative monitoring (iMRI, awake craniotomy); clinical trial access at tertiary center |
| Inpatient rehabilitation | Significant post-operative neurologic deficits (hemiparesis, aphasia, cognitive impairment) requiring intensive rehabilitation before outpatient treatment can begin; KPS 40-60 with rehabilitation potential |
| Palliative care / Hospice | End-stage GBM with progressive decline despite treatment; KPS <30; exhausted reasonable treatment options; patient/family goals aligned with comfort-focused care; no longer candidate for disease-directed therapy |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Maximal safe resection improves overall survival in GBM | Class II, Level B | Lacroix et al. J Neurosurg 2001; Sanai et al. J Neurosurg 2011 |
| 5-ALA fluorescence-guided surgery improves extent of resection | Class I, Level A | Stummer et al. Lancet Oncol 2006 |
| Concurrent temozolomide + radiation (Stupp protocol) standard of care for newly diagnosed GBM | Class I, Level A | Stupp et al. NEJM 2005; Stupp et al. Lancet Oncol 2009 (5-year data) |
| MGMT promoter methylation predicts temozolomide response and overall survival | Class I, Level A | Hegi et al. NEJM 2005 |
| Tumor Treating Fields (TTFields) with adjuvant temozolomide improves OS in newly diagnosed GBM | Class I, Level A | Stupp et al. JAMA 2017 (EF-14 trial) |
| Hypofractionated RT (40 Gy/15 fractions) + temozolomide beneficial in elderly GBM | Class I, Level A | Perry et al. NEJM 2017 |
| Temozolomide alone vs. RT alone in elderly GBM; treatment guided by MGMT status | Class I, Level A | Wick et al. Lancet Oncol 2012 (NOA-08); Malmstrom et al. Lancet Oncol 2012 (Nordic trial) |
| Bevacizumab for recurrent GBM: PFS benefit, no OS benefit | Class I, Level B | Friedman et al. J Clin Oncol 2009; Wick et al. Lancet Oncol 2017 (EORTC 26101) |
| Bevacizumab in newly diagnosed GBM: PFS benefit, no OS benefit | Class I, Level A | Chinot et al. NEJM 2014 (AVAglio); Gilbert et al. NEJM 2014 (RTOG 0825) |
| WHO 2021 classification: IDH-wildtype glioblastoma defined by molecular criteria | Expert Consensus | Louis et al. Neuro-Oncology 2021 (WHO CNS5) |
| TERT promoter mutation, EGFR amplification, +7/-10 as molecular diagnostic criteria for GBM | Expert Consensus | Louis et al. Neuro-Oncology 2021 (WHO CNS5) |
| Prophylactic AEDs NOT recommended in brain tumor patients without seizures | Class I, Level A | Glantz et al. Neurology 2000 (AAN Practice Parameter); reaffirmed |
| Levetiracetam preferred AED in brain tumor patients (no CYP enzyme induction) | Class II, Level B | Rosati et al. J Neurooncol 2010; RANO guidelines |
| DVT prophylaxis safe in brain tumor patients | Class II, Level B | Perry et al. Lancet 2010 (PRODIGE trial) |
| Dexamethasone for vasogenic edema; use minimum effective dose and taper | Class II, Level B | Ryken et al. J Neurooncol 2010 (CNS systematic review) |
| Pseudoprogression occurs in 20-30% of GBM patients post-chemoradiation, especially MGMT methylated | Class II, Level B | Brandsma et al. Lancet Oncol 2008; RANO criteria 2010 |
| RANO response criteria for glioblastoma clinical assessment | Expert Consensus | Wen et al. J Clin Oncol 2010 |
| Lomustine for recurrent GBM; combination with bevacizumab PFS benefit | Class I, Level B | Wick et al. Lancet Oncol 2017 (EORTC 26101) |
| PJP prophylaxis recommended during concurrent chemoradiation | Class II, Level C | Expert consensus; NCCN guidelines |
| Supratotal resection may improve outcomes beyond contrast-enhancing boundary | Class II, Level C | Li et al. World Neurosurg 2016; emerging evidence |
| MR spectroscopy and perfusion MRI differentiate tumor from treatment effects | Class II, Level B | Law et al. AJNR 2003; various meta-analyses |
| Memantine may reduce cognitive decline during brain radiation therapy | Class II, Level B | Brown et al. Neuro-Oncology 2013 (RTOG 0614) |
| Methylphenidate for cancer-related fatigue | Class II, Level B | Lower et al. Cancer 2009; Minton et al. J Clin Oncol 2013 (Cochrane review) |

---

## CHANGE LOG

**v1.1 (January 30, 2026)**
- Reordered all lab table columns (1A, 1B, 1C) to place venue columns last per style guide (R1)
- Reordered LP table columns to place venue columns last (R2)
- Reordered imaging table columns (2A, 2B, 2C) to place venue columns last
- Reordered Section 6 monitoring table columns to place venue columns last
- Standardized all treatment dosing fields to structured format: dose :: route :: frequency :: instructions (R3, C3)
- Renamed "DVT prophylaxis" to "Enoxaparin (DVT prophylaxis)" in Section 3A (R4, M2)
- Renamed "Stress ulcer prophylaxis" to "Pantoprazole (stress ulcer prophylaxis)" in Section 3A (R5, M3)
- Added methylphenidate for cancer-related fatigue in Section 3B (R6, M5)
- Added memantine for neuroprotection during radiation in Section 3B (R7, M6)
- Fixed insulin dosing to structured format in Section 3B (R8, M7)
- Fixed Calcium + Vitamin D dosing to structured format in Section 3B (R9, M8)
- Added ICU column to 4B and 4C tables (R10, S1, S2)
- Added ECG and CXR OPD coverage as ROUTINE for pre-operative clearance (S3)
- Added evidence references for memantine (RTOG 0614) and methylphenidate (Cochrane review)
- Updated version to 1.1

**v1.0 (January 30, 2026)**
- Initial template creation
- Comprehensive 8-section plan for glioblastoma (IDH-wildtype, WHO grade 4)
- Full molecular profiling criteria per WHO 2021 (CNS5) classification
- Stupp protocol with concurrent and adjuvant temozolomide dosing
- Tumor Treating Fields (TTFields/Optune) with compliance monitoring
- Hypofractionated RT option for elderly/poor KPS patients
- Recurrence management (bevacizumab, lomustine, re-resection, re-irradiation)
- MGMT methylation-guided treatment decision framework
- Comprehensive differential diagnosis including IDH-mutant astrocytoma, PCNSL, abscess
- Pseudoprogression monitoring guidance with advanced imaging
- 20+ evidence references with landmark trials

---

## APPENDIX A: STUPP PROTOCOL TIMELINE

```
WEEK 0: SURGERY (Maximal Safe Resection)
├── Post-op MRI within 48 hours
├── Pathology: IDH-wildtype, WHO grade 4
├── Molecular: MGMT methylation, TERT, EGFR, +7/-10
├── Start dexamethasone taper
└── Multidisciplinary tumor board

WEEKS 3-6: BEGIN CONCURRENT CHEMORADIATION
├── Radiation: 60 Gy in 30 fractions (6 weeks)
├── Temozolomide: 75 mg/m² PO daily × 42 days
├── PJP prophylaxis: TMP-SMX 1 DS MWF
├── CBC weekly (hold TMZ if ANC <1000 or plt <50K)
└── Antiemetic: ondansetron 8 mg before TMZ

WEEK 10 (4 WEEKS POST-RT): NEW BASELINE MRI
├── Distinguish pseudoprogression from true progression
├── Pseudoprogression more common in MGMT methylated (up to 30%)
└── If equivocal: repeat MRI in 4-8 weeks; do NOT change treatment

WEEKS 10-34: ADJUVANT TEMOZOLOMIDE (6 CYCLES)
├── Cycle 1: 150 mg/m² PO Days 1-5 of 28-day cycle
├── Cycles 2-6: 200 mg/m² PO Days 1-5 if Cycle 1 tolerated
├── CBC Day 1 and Day 22 of each cycle
├── MRI q2-3 months
├── Continue PJP prophylaxis if ALC <500 or CD4 <200
└── Consider TTFields (Optune) starting with adjuvant phase

ONGOING: SURVEILLANCE
├── MRI brain with contrast q2-3 months year 1
├── Then q3-4 months year 2
├── Then q4-6 months ongoing
├── Each visit: neuro exam, KPS, labs, symptom assessment
└── At recurrence: re-evaluate for surgery, re-irradiation,
    bevacizumab, lomustine, clinical trials
```

## APPENDIX B: MGMT-GUIDED TREATMENT DECISION FRAMEWORK

```
MGMT METHYLATION STATUS
         │
         ├── METHYLATED (~40% of GBM)
         │     ├── Standard Stupp Protocol (concurrent TMZ + RT → adjuvant TMZ)
         │     ├── Median OS: ~21 months (vs. ~14 unmethylated)
         │     ├── Higher pseudoprogression rate (up to 30%)
         │     ├── Elderly (>65): hypofractionated RT + TMZ (Perry 2017)
         │     ├── Poor KPS: TMZ alone may be considered (NOA-08)
         │     └── TTFields: additional benefit (EF-14)
         │
         ├── UNMETHYLATED (~60% of GBM)
         │     ├── Standard Stupp Protocol (still recommended — some benefit)
         │     ├── Median OS: ~14 months
         │     ├── Lower pseudoprogression rate
         │     ├── Elderly: consider RT alone if poor KPS (NOA-08, Nordic)
         │     ├── Clinical trials strongly encouraged (novel targets)
         │     └── TTFields: still beneficial regardless of MGMT
         │
         └── UNKNOWN / INDETERMINATE
               ├── Treat as standard Stupp Protocol
               ├── Repeat MGMT testing if tissue available
               └── Do NOT delay treatment for MGMT results
```

## APPENDIX C: PSEUDOPROGRESSION VS. TRUE PROGRESSION

```
POST-CHEMORADIATION MRI SHOWS INCREASED ENHANCEMENT
         │
         ├── TIMING: Within 3-6 months of completing RT?
         │     YES → Pseudoprogression more likely (20-30%)
         │     NO (>6 months) → True progression more likely
         │
         ├── MGMT STATUS: Methylated?
         │     YES → Higher pseudoprogression risk (~30%)
         │     NO → Lower pseudoprogression risk (~10-15%)
         │
         ├── CLINICAL STATUS:
         │     Stable/Improving → Favor pseudoprogression
         │     Declining → Favor true progression
         │
         ├── ADVANCED IMAGING:
         │     ├── MR Perfusion: Low rCBV → Pseudoprogression
         │     │                 High rCBV (>1.75) → True progression
         │     ├── MR Spectroscopy: Low Cho/NAA → Pseudoprogression
         │     │                     High Cho/NAA → True progression
         │     └── FET-PET: Low uptake → Pseudoprogression
         │                  High uptake (TBR >1.6) → True progression
         │
         └── MANAGEMENT:
               ├── If pseudoprogression suspected → Continue current treatment
               │    → Repeat MRI in 4-8 weeks
               ├── If true progression → Tumor board discussion
               │    → Consider re-resection, re-irradiation, bevacizumab,
               │       lomustine, clinical trial
               └── If equivocal → Biopsy for definitive diagnosis
```

## APPENDIX D: GBM MOLECULAR PROFILING — WHO 2021 (CNS5)

**Diagnostic Criteria for Glioblastoma, IDH-wildtype, WHO Grade 4:**

A diffuse astrocytic glioma is classified as glioblastoma, IDH-wildtype IF:

1. **Histologically** shows features of a diffuse astrocytic glioma, AND
2. **IDH1 and IDH2 are wildtype** (no mutation), AND
3. **At least ONE of the following molecular features:**
   - TERT promoter mutation (C228T or C250T)
   - EGFR gene amplification
   - Combined whole chromosome 7 gain and whole chromosome 10 loss (+7/-10)

**Additional Molecular Markers (prognostic/predictive, not diagnostic):**

| Marker | Clinical Significance | Testing Method |
|--------|-----------------------|----------------|
| **MGMT promoter methylation** | Predicts temozolomide response; methylated = better prognosis | Methylation-specific PCR or pyrosequencing |
| **TERT promoter mutation** | Diagnostic criterion; present in ~80% of GBM | Sanger sequencing or next-gen sequencing |
| **EGFR amplification** | Diagnostic criterion; present in ~40-50% of GBM | FISH, array CGH, or NGS |
| **+7/-10 (chromosome gains/losses)** | Diagnostic criterion; present in ~70% of GBM | Array CGH, SNP array, or NGS |
| **EGFRvIII variant** | Targeted therapy target (rindopepimut, CAR-T); present in ~30% of EGFR-amplified | RT-PCR, immunohistochemistry |
| **CDKN2A/B deletion** | Associated with worse prognosis; CDK4/6 inhibitor target | FISH or NGS |
| **TP53 mutation** | Common (~30%); no current therapeutic implication in GBM | Sequencing |
| **PTEN loss** | Common (~40%); PI3K pathway activation; emerging therapeutic target | IHC, FISH, or NGS |
| **PDL1 expression** | Immunotherapy biomarker (limited efficacy in GBM to date) | IHC (TPS, CPS) |

---

*This template has been validated through the checker pipeline v1.1 and requires physician review before clinical deployment.*
