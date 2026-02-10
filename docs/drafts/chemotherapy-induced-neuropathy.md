---
title: "Chemotherapy-Induced Peripheral Neuropathy (CIPN)"
description: "Clinical decision support for chemotherapy-induced peripheral neuropathy diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - neuropathy
  - chemotherapy
  - CIPN
  - neurotoxicity
  - outpatient
  - neuromuscular
---

<div class="draft-warning-banner" style="background:#fff3cd;border:2px solid #ffc107;border-radius:8px;padding:16px;margin:16px 0;text-align:center;">
<strong>⚠️ DRAFT — NOT FOR CLINICAL USE</strong><br>
This template is under review and has not been physician-approved.
</div>

# Chemotherapy-Induced Peripheral Neuropathy (CIPN)

**VERSION:** 1.0
**CREATED:** February 9, 2026
**REVISED:** February 9, 2026
**STATUS:** Draft — Awaiting physician review

---

**DIAGNOSIS:** Chemotherapy-Induced Peripheral Neuropathy (CIPN)

**ICD-10:** G62.0 (Drug-induced polyneuropathy), T45.1X5A (Adverse effect of antineoplastic and immunosuppressive drugs, initial encounter), G62.9 (Polyneuropathy, unspecified)

**CPT CODES:** 95907 (NCS, 1-2 nerves), 95909 (NCS, 5-6 nerves), 95913 (NCS, 9-10 nerves), 95886 (Needle EMG, each extremity), 88305 (Skin biopsy pathology — IENFD), 85025 (CBC), 80048 (BMP), 82728 (Ferritin), 82607 (Vitamin B12), 84443 (TSH), 82947 (Glucose), 83036 (HbA1c), 82784 (IgG/IgA/IgM), 86235 (ANA), 84295 (Sodium), 84132 (Potassium)

**SYNONYMS:** CIPN, chemotherapy neuropathy, chemo neuropathy, neurotoxic neuropathy, taxane neuropathy, platinum neuropathy, vinca alkaloid neuropathy, bortezomib neuropathy, thalidomide neuropathy, drug-induced polyneuropathy, cancer treatment-related neuropathy

**SCOPE:** Evaluation and management of peripheral neuropathy caused by or attributed to chemotherapy agents in adults. Includes identification of causative agents, grading severity, dose modification guidance, symptomatic treatment, and long-term monitoring. Covers outpatient screening and management during active chemotherapy, inpatient evaluation for acute neurotoxicity, and post-treatment chronic neuropathy. Excludes radiation-induced neuropathy and paraneoplastic neuropathy as separate entities (addressed in differential).

---

**DEFINITIONS:**
- **CIPN:** Peripheral neuropathy directly caused by neurotoxic chemotherapy agents; predominantly sensory, length-dependent, affecting hands and feet
- **Coasting:** Worsening of neuropathy symptoms for weeks to months after discontinuation of the offending chemotherapy agent; characteristic of platinum compounds (oxaliplatin, cisplatin)
- **Acute oxaliplatin neuropathy:** Transient cold-triggered paresthesias and pharyngolaryngeal dysesthesia occurring within hours of oxaliplatin infusion; resolves within days; distinct from chronic cumulative CIPN
- **CTCAE grading (v5.0):** Grade 1 = asymptomatic, clinical/diagnostic observation only; Grade 2 = moderate symptoms limiting instrumental ADLs; Grade 3 = severe symptoms limiting self-care ADLs; Grade 4 = life-threatening (rare in CIPN)
- **NCI-CTCAE Sensory Neuropathy:** Grade 1 = asymptomatic/loss of deep tendon reflexes or paresthesia; Grade 2 = moderate symptoms limiting instrumental ADLs; Grade 3 = severe symptoms limiting self-care ADLs
- **Total Neuropathy Score (TNS):** Validated composite measure of sensory, motor, and autonomic neuropathy severity used in CIPN clinical trials

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (Exclude Concurrent Neuropathy Etiologies)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Diabetes is most common concurrent cause of neuropathy in cancer patients; must exclude as contributor | <6.5%; if elevated, concurrent diabetic neuropathy likely contributing |
| Fasting glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Screen for diabetes; steroid-induced hyperglycemia common in chemo regimens | <126 mg/dL fasting |
| Vitamin B12 (CPT 82607) | - | ROUTINE | ROUTINE | - | B12 deficiency common in cancer patients (poor nutrition, metformin use); worsens neuropathy | >300 pg/mL; if 200-400, check methylmalonic acid |
| CBC (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; macrocytosis (B12/folate deficiency); chemotherapy-related cytopenias | Normal indices; adequate counts |
| BMP (CPT 80048) | STAT | STAT | ROUTINE | STAT | Renal function (cisplatin nephrotoxicity); electrolytes (hypomagnesemia, hypokalemia worsening neuropathy) | Normal creatinine; Mg >1.8 mg/dL; K >3.5 mEq/L |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Hypothyroidism causes neuropathy and is common in cancer patients (checkpoint inhibitor thyroiditis) | Normal (0.4-4.0 mIU/L) |
| Magnesium | STAT | STAT | ROUTINE | STAT | Cisplatin and cetuximab cause renal magnesium wasting; hypomagnesemia exacerbates neuropathy and neurotoxicity | >1.8 mg/dL |

### 1B. Extended Labs (When CIPN Diagnosis Uncertain)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| SPEP/UPEP with immunofixation (CPT 82784) | - | - | ROUTINE | - | Screen for paraproteinemia (myeloma patients on bortezomib may have paraprotein-associated neuropathy as well) | No M-spike; normal free light chains |
| Folate | - | ROUTINE | ROUTINE | - | Deficiency in cancer patients with poor nutrition; contributes to neuropathy and macrocytosis | >5.9 ng/mL |
| Methylmalonic acid | - | - | ROUTINE | - | Confirm B12 deficiency if borderline B12 level (200-400 pg/mL) | Normal (<0.4 nmol/L) |
| Copper, serum | - | - | EXT | - | Copper deficiency neuropathy from zinc supplementation or malabsorption in cancer patients | Normal (70-140 mcg/dL) |
| ESR/CRP | - | ROUTINE | ROUTINE | - | Inflammatory process; vasculitic neuropathy in differential | Normal |
| ANA (CPT 86235) | - | - | EXT | - | Autoimmune neuropathy; checkpoint inhibitor-induced autoimmunity | Negative |
| Hepatitis B/C | - | - | EXT | - | Hepatitis-associated neuropathy; reactivation during immunosuppression | Negative |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-neuronal antibodies (Hu, CV2/CRMP5, amphiphysin) | - | - | EXT | - | Paraneoplastic neuropathy mimicking CIPN; especially if neuropathy precedes or is disproportionate to chemotherapy exposure | Negative; positive suggests paraneoplastic etiology |
| Ganglioside antibodies (anti-MAG, anti-GM1) | - | - | EXT | - | Autoimmune neuropathy; especially if demyelinating features on EMG not expected from chemotherapy type | Negative |
| Platinum levels (urine or serum) | - | - | EXT | - | Document platinum accumulation in refractory cases; research tool primarily | Correlate with cumulative dose and symptom severity |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| EMG/NCS (CPT 95907-95913, 95886) | - | - | ROUTINE | - | Baseline before chemotherapy (ideal); at onset of symptoms; monitor serially during treatment | Reduced SNAP amplitudes (axonal sensory neuropathy); normal or mildly reduced NCV; denervation if motor involvement; pattern consistent with agent type | None significant (relative: thrombocytopenia for needle EMG — platelet count >20K) |
| CIPN screening questionnaire (EORTC QLQ-CIPN20 or FACT/GOG-Ntx) | - | ROUTINE | ROUTINE | - | Each chemotherapy cycle; standardized patient-reported outcome measure | Score trending; identify grade >=2 symptoms early for dose modification | None |

### 2B. Extended Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Skin biopsy (IENFD — intraepidermal nerve fiber density) (CPT 88305) | - | - | ROUTINE | - | If small fiber neuropathy suspected (normal EMG/NCS with symptoms); quantify small fiber damage | Reduced IENFD below age/sex-specific norms at distal leg (confirms small fiber neuropathy) | Coagulopathy (platelets <50K); infection at biopsy site |
| Quantitative sensory testing (QST) | - | - | EXT | - | Research and clinical quantification of thermal and vibration thresholds; serial monitoring | Elevated thermal/vibration detection thresholds; correlate with clinical severity | Cognitive impairment limiting cooperation |
| MRI spine (cervical/lumbar) | - | - | EXT | - | If myelopathy or radiculopathy suspected; metastatic disease as alternative cause of neurologic symptoms | No cord compression, metastatic disease, or radiation-induced changes | MRI contraindications |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Sural nerve biopsy | - | - | EXT | - | Rarely indicated; vasculitic neuropathy suspected; atypical presentation not explained by chemotherapy | Axonal degeneration pattern; vasculitis on biopsy if present | Permanent sensory loss at biopsy site; coagulopathy |
| Corneal confocal microscopy | - | - | EXT | - | Non-invasive small fiber assessment; research tool for CIPN monitoring | Reduced corneal nerve fiber density and length correlating with CIPN severity | None |

---

## 3. TREATMENT

### 3A. Acute Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Dose reduction of offending chemotherapy | Protocol | Grade 2 CIPN (moderate symptoms limiting instrumental ADLs) | Per protocol :: Protocol :: per cycle :: Reduce offending agent dose by 25-50% per institutional guidelines; specific agent protocols vary (e.g., oxaliplatin: 25% reduction for grade 2, discontinue for grade 3) | Oncology team decision balancing neuropathy risk vs cancer treatment efficacy | CTCAE grading each cycle; symptom questionnaire; functional assessment | - | ROUTINE | ROUTINE | - |
| Discontinuation of offending chemotherapy | Protocol | Grade 3 CIPN (severe symptoms limiting self-care ADLs); persistent grade 2 despite dose reduction | Discontinue :: Protocol :: per cycle :: Stop offending agent; consider alternative non-neurotoxic regimen; oncology decision weighing risk-benefit | None (oncology team decision) | Symptom monitoring for coasting phenomenon (platinum agents); cancer treatment response | - | ROUTINE | ROUTINE | - |
| Calcium/magnesium infusion (for oxaliplatin acute neuropathy) | IV | Acute cold-triggered paresthesias during/after oxaliplatin infusion | 1 g calcium gluconate + 1 g magnesium sulfate :: IV :: per infusion :: 1 g calcium gluconate + 1 g MgSO4 in 100 mL NS IV over 30 min before and after oxaliplatin infusion; reduces acute neurotoxicity | Hypercalcemia; hypermagnesemia; renal failure (dose adjust Mg) | Calcium level; magnesium level; renal function | - | ROUTINE | ROUTINE | - |
| Warming measures (oxaliplatin) | Physical | Acute cold-triggered dysesthesia during oxaliplatin infusion | Avoid cold :: Physical :: per infusion :: Avoid cold drinks, cold foods, and cold air exposure for 3-5 days after infusion; wear gloves for refrigerator; warm beverages only | None | Patient education compliance | - | ROUTINE | ROUTINE | - |
| Magnesium supplementation | IV/PO | Cisplatin or cetuximab-induced hypomagnesemia exacerbating neuropathy | 400-800 mg :: PO :: daily :: Magnesium oxide 400-800 mg daily PO; or MgSO4 2 g IV over 1 hour for severe deficiency (<1.2 mg/dL) | Renal failure (dose adjust); heart block | Serum Mg q1-4 weeks; renal function; bowel habits (diarrhea) | STAT | ROUTINE | ROUTINE | STAT |

### 3B. Symptomatic Treatment (First-Line)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Duloxetine | PO | Neuropathic pain from CIPN; only agent with RCT evidence specifically for CIPN (ASCO recommended) | 30 mg :: PO :: daily :: Start 30 mg daily for 1 week; increase to 60 mg daily; trial 4-8 weeks at therapeutic dose; max 120 mg/day; taper when discontinuing | Severe hepatic impairment; concurrent MAOIs; uncontrolled narrow-angle glaucoma; CrCl <30 | BP (hypertension risk); hepatic function; serotonin syndrome; discontinuation syndrome; suicidality monitoring | - | ROUTINE | ROUTINE | - |
| Gabapentin | PO | Neuropathic pain; burning/tingling; first-line alternative to duloxetine | 300 mg :: PO :: TID :: Start 100-300 mg qHS; titrate by 300 mg q3-7 days; target 300-600 mg TID; max 3600 mg/day; dose adjust for renal impairment | Severe renal impairment (dose adjust); concurrent opioid use increases respiratory depression risk | Sedation; dizziness; peripheral edema; renal function for dose adjustment | - | ROUTINE | ROUTINE | - |
| Pregabalin | PO | Neuropathic pain; alternative to gabapentin with more predictable pharmacokinetics | 75 mg :: PO :: BID :: Start 50-75 mg BID; titrate to 150-300 mg BID; max 600 mg/day; dose adjust for renal impairment | Renal impairment (dose adjust); angioedema history | Weight gain; peripheral edema; sedation; renal dosing | - | ROUTINE | ROUTINE | - |
| Topical capsaicin 8% patch (Qutenza) | Topical | Localized neuropathic pain; feet predominantly; patients intolerant of systemic medications | 1 patch :: Topical :: q3 months :: Applied by healthcare professional to affected area for 30-60 minutes; may repeat q3 months; pre-treat with topical lidocaine | Open wounds; mucosal surfaces | Skin reaction at application site (burning, erythema); BP monitoring during application (transient increase) | - | - | ROUTINE | - |

### 3C. Second-Line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Venlafaxine | PO | CIPN pain refractory to duloxetine; some evidence for acute oxaliplatin neuropathy prevention | 37.5 mg :: PO :: daily :: Start 37.5 mg daily; titrate to 75-150 mg daily; extended release preferred; taper when discontinuing | Same as duloxetine | BP; serotonin syndrome; discontinuation syndrome; QTc if high dose | - | - | ROUTINE | - |
| Amitriptyline (low-dose) | PO | Neuropathic pain; sleep disruption from neuropathy; adjunct therapy | 10 mg :: PO :: qHS :: Start 10 mg qHS; titrate by 10 mg q1-2 weeks; max 50 mg qHS for neuropathic pain; avoid in elderly | Cardiac arrhythmia; recent MI; concurrent MAOIs; urinary retention; narrow-angle glaucoma; elderly (anticholinergic burden) | ECG if dose >50 mg or cardiac risk; anticholinergic effects; sedation; orthostatic BP | - | - | EXT | - |
| Topical lidocaine 5% patch | Topical | Localized neuropathic pain; allodynia on feet; adjunct therapy | 1-3 patches :: Topical :: 12h on/12h off :: Apply to affected area 12 hours on, 12 hours off; max 3 patches simultaneously | Allergy to amide local anesthetics; severe hepatic disease | Skin reaction; systemic absorption unlikely with topical use | - | - | ROUTINE | - |
| Scrambler therapy (MC5-A) | Physical | Refractory CIPN pain; emerging evidence; non-pharmacologic | Daily for 10 sessions :: Physical :: daily x10 :: Cutaneous electrostimulation device applied to pain area; 10 consecutive daily sessions of 30-45 minutes each | Implanted cardiac devices (pacemaker, defibrillator); epilepsy; skin lesions at electrode site | Pain scores pre/post treatment; functional measures | - | - | EXT | - |
| Acupuncture | Physical | Adjunctive treatment for CIPN pain; moderate evidence for symptom improvement | 2x/week for 8 weeks :: Physical :: 2x/week :: Electroacupuncture or manual acupuncture; 8-12 week course; standardized point selection protocols available | Coagulopathy (platelets <20K); neutropenia (<500); infection at needle sites | Pain scores; functional measures; adverse events (rare) | - | - | EXT | - |

### 3D. Neuroprotective Agents (Limited Evidence)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Exercise therapy (aerobic and resistance) | Physical | All CIPN patients; emerging evidence for neuroprotection and symptom improvement; improves balance | 30 min 3-5x/week :: Physical :: 3-5x/week :: Moderate-intensity aerobic exercise (walking, cycling) plus balance and resistance training; supervised initially; improves nerve function and reduces fall risk | Bone metastases (modify loading); severe cytopenias; hemodynamic instability | Functional capacity; fall risk; compliance; pain levels | - | ROUTINE | ROUTINE | - |
| Alpha-lipoic acid | PO | Antioxidant; limited evidence for CIPN; may reduce oxidative nerve damage | 600 mg :: PO :: daily :: 600 mg daily; trial 8-12 weeks; evidence from diabetic neuropathy trials; CIPN-specific evidence mixed | GI intolerance (nausea) | Blood glucose (may lower glucose); GI tolerance | - | - | EXT | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation for electrodiagnostic testing (EMG/NCS), CIPN confirmation, and to rule out concurrent neuropathy etiologies (diabetic, B12, paraneoplastic) | - | ROUTINE | ROUTINE | - |
| Physical therapy for balance training, fall prevention, gait assessment, and exercise program — fall risk is elevated in CIPN patients | - | ROUTINE | ROUTINE | - |
| Occupational therapy for hand function assessment, adaptive devices, and fine motor rehabilitation if hand involvement affects ADLs | - | - | ROUTINE | - |
| Pain management specialist for refractory CIPN pain not responding to duloxetine/gabapentin; multimodal approach | - | - | ROUTINE | - |
| Oncology discussion regarding dose modification, alternative regimens, and treatment goals when CIPN reaches grade 2 or higher | - | ROUTINE | ROUTINE | - |
| Podiatry referral for foot care, custom orthotics, and fall prevention assessment — sensory loss increases foot injury risk | - | - | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Report numbness, tingling, or burning in hands or feet to the oncology team before each chemotherapy cycle — early detection allows dose adjustment to prevent irreversible damage | - | ROUTINE | ROUTINE | - |
| For oxaliplatin patients: avoid cold drinks, cold food, cold air, and touching cold surfaces for 3-5 days after each infusion; use gloves when opening the refrigerator or freezer | - | ROUTINE | ROUTINE | - |
| Use fall prevention measures: wear well-fitting shoes with non-slip soles; use nightlights; remove loose rugs; install grab bars in bathroom; use handrails on stairs | ROUTINE | ROUTINE | ROUTINE | - |
| Inspect feet daily for cuts, blisters, or injuries — reduced sensation means you may not feel foot injuries; diabetic-type foot care reduces complications | - | ROUTINE | ROUTINE | - |
| Avoid alcohol which has its own neurotoxic effects and can worsen chemotherapy-induced neuropathy | - | ROUTINE | ROUTINE | - |
| Understand that some neuropathy symptoms may worsen ("coasting") for weeks to months after stopping chemotherapy (especially platinum drugs) before stabilizing — this is expected and not a sign of cancer progression | - | ROUTINE | ROUTINE | - |
| Exercise regularly (walking, cycling, swimming) as tolerated — exercise has been shown to improve nerve function, balance, and quality of life in CIPN patients | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Maintain adequate nutrition: balanced diet with B vitamins, folate, and protein to support nerve health during chemotherapy | - | ROUTINE | ROUTINE | - |
| Optimize glucose control if diabetic (HbA1c <7%) — uncontrolled diabetes significantly worsens CIPN severity and recovery | - | ROUTINE | ROUTINE | - |
| Replace magnesium and electrolyte deficiencies promptly — cisplatin and cetuximab deplete magnesium which exacerbates neurotoxicity | - | ROUTINE | ROUTINE | - |
| Engage in regular moderate exercise (30 min, 3-5x/week) during and after chemotherapy — emerging evidence supports exercise as both neuroprotective and therapeutic for CIPN | - | ROUTINE | ROUTINE | - |
| Smoking cessation — smoking impairs nerve repair and worsens neuropathy outcomes | - | ROUTINE | ROUTINE | - |
| Use assistive devices as needed (buttoning aids, grip enhancers, adapted utensils) to maintain independence during hand neuropathy | - | - | ROUTINE | - |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Diabetic peripheral neuropathy | Pre-existing diabetes; symptoms may predate chemotherapy; symmetric length-dependent; HbA1c elevated | HbA1c; glucose tolerance test; pre-chemo EMG baseline (if available) |
| B12 deficiency neuropathy | Macrocytosis; subacute combined degeneration if severe; may coexist with CIPN | Serum B12; methylmalonic acid; MRI spine if myelopathy |
| Paraneoplastic neuropathy (anti-Hu, anti-CV2) | Subacute onset; may precede cancer diagnosis; asymmetric or sensory ganglionopathy pattern; ataxia prominent | Paraneoplastic antibody panel; CSF analysis; pattern may not be length-dependent |
| Radiation-induced neuropathy/plexopathy | History of radiation field involving nerves/plexus; delayed onset (months-years post-radiation); myokymia on EMG | EMG showing myokymia (suggests radiation); MRI of affected plexus; temporal relationship to radiation field |
| Chronic inflammatory demyelinating polyneuropathy (CIDP) | Demyelinating pattern on EMG (prolonged distal latencies, conduction block); proximal and distal weakness; CSF protein elevated | EMG/NCS showing demyelinating features; CSF protein; response to IVIg/steroids |
| Vasculitic neuropathy | Asymmetric (mononeuritis multiplex); painful; elevated ESR/CRP; systemic vasculitis features | ESR/CRP; ANCA; nerve biopsy showing vasculitis; skin/renal involvement |
| Hereditary neuropathy (CMT) | Family history; pes cavus; high arched feet; slowly progressive; very slow NCV; present before chemotherapy | Genetic testing; family history; EMG showing very slow uniform NCV |
| Medication-induced neuropathy (non-chemo) | Temporal relationship to other medications: metformin, statins, colchicine, isoniazid, linezolid | Medication reconciliation; improvement with drug withdrawal |
| Alcohol-related neuropathy | History of chronic alcohol use; nutritional deficiency; may coexist | Alcohol use history; nutritional labs (thiamine, B12, folate); liver function |
| Lumbosacral or cervical radiculopathy | Dermatomal pattern; unilateral; spine pain; motor and sensory deficit in specific root distribution | MRI spine; EMG showing radicular pattern (not length-dependent) |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| CIPN screening questionnaire (EORTC QLQ-CIPN20 or FACT/GOG-Ntx) | Before each chemo cycle | Stable or improving scores; identify grade >=2 early | Dose reduce or discontinue chemotherapy per protocol; intensify symptom management | - | ROUTINE | ROUTINE | - |
| CTCAE neuropathy grading | Before each chemo cycle | Grade <=1 | Grade 2: dose reduce 25-50%; Grade 3: hold or discontinue; discuss with oncology | - | ROUTINE | ROUTINE | - |
| Neurologic exam (strength, sensation, reflexes, gait, Romberg) | Each oncology visit; each neurology visit | No progression of motor deficit; stable sensory exam | Adjust chemotherapy; add symptomatic treatment; PT referral for balance | ROUTINE | ROUTINE | ROUTINE | - |
| EMG/NCS (serial) | Baseline (pre-chemo ideal); at onset of symptoms; q6-12 months during treatment | Stable SNAP amplitudes; no new denervation | SNAP amplitude drop >50% → consider dose modification; new denervation → urgent oncology discussion | - | - | ROUTINE | - |
| Fall risk assessment | Each visit during active CIPN | Low fall risk; no falls | PT referral; home safety evaluation; assistive device assessment; reduce sedating medications | - | ROUTINE | ROUTINE | - |
| Serum magnesium (cisplatin/cetuximab patients) | Each chemo cycle; weekly during cisplatin | Mg >1.8 mg/dL | Replace IV MgSO4 if <1.2; oral supplementation if 1.2-1.8; dose may need to be held | - | ROUTINE | ROUTINE | STAT |
| Renal function (cisplatin patients) | Each chemo cycle | GFR >60 mL/min | Cisplatin dose adjustment per renal function; hold if significant decline | - | ROUTINE | ROUTINE | STAT |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge from ED | Acute CIPN exacerbation with stable neurologic exam; pain controlled with oral medications; no fall-related injuries requiring admission; neurology/oncology follow-up arranged |
| Observation | Acute neurologic decline requiring serial exams; fall with injury needing workup; severe electrolyte derangement (hypomagnesemia, hypokalemia) requiring IV replacement |
| Admit to floor | Severe (grade 3) CIPN with inability to perform self-care; cisplatin nephrotoxicity with electrolyte crisis; fall with injury requiring inpatient management; acute chemotherapy reaction requiring monitoring |
| Admit to ICU | Rare; only if concurrent chemotherapy toxicity (severe nephrotoxicity, sepsis in neutropenic patient); respiratory compromise from vinca alkaloid-induced autonomic/motor neuropathy |
| Outpatient follow-up (oncology) | Before each chemotherapy cycle: CIPN screening; dose modification decisions; ongoing monitoring during active treatment |
| Outpatient follow-up (neurology) | Initial evaluation: 2-4 weeks after symptom onset; EMG/NCS baseline; follow-up q3-6 months during treatment; post-treatment monitoring for coasting q3 months for 1 year |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Duloxetine is the only agent with RCT evidence for CIPN pain treatment (ASCO recommended) | Class I, Level A | [Smith EML et al. JAMA 2013](https://pubmed.ncbi.nlm.nih.gov/23549581/) |
| ASCO Clinical Practice Guideline on Prevention and Management of CIPN | Guideline | [Loprinzi CL et al. J Clin Oncol 2020 (update)](https://pubmed.ncbi.nlm.nih.gov/32663120/) |
| No agent has proven efficacy for CIPN prevention (ASCO 2020 guideline conclusion) | Class I, Level A | [Loprinzi CL et al. J Clin Oncol 2020](https://pubmed.ncbi.nlm.nih.gov/32663120/) |
| Exercise during chemotherapy may reduce CIPN incidence and severity | Class IIa, Level B | [Kleckner IR et al. Support Care Cancer 2018](https://pubmed.ncbi.nlm.nih.gov/29243164/) |
| Calcium/magnesium infusions may reduce oxaliplatin acute neurotoxicity | Class IIb, Level B | [Grothey A et al. J Clin Oncol 2011](https://pubmed.ncbi.nlm.nih.gov/21189381/) |
| Coasting phenomenon in platinum compounds (worsening after discontinuation) | Class IIa, Level C | [Cavaletti G, Marmiroli P. Nat Rev Neurol 2010](https://pubmed.ncbi.nlm.nih.gov/21060341/) |
| Skin biopsy (IENFD) detects small fiber damage in early CIPN when EMG/NCS normal | Class IIa, Level B | [Lauria G et al. Eur J Neurol 2010](https://pubmed.ncbi.nlm.nih.gov/20642627/) |
| Taxane CIPN: predominantly sensory, axonal, dose-dependent | Class IIa, Level B | [Argyriou AA et al. Eur J Cancer 2012](https://pubmed.ncbi.nlm.nih.gov/23304163/) |
| Capsaicin 8% patch shows benefit for localized CIPN pain | Class IIa, Level B | [Anand P, Bley K. Br J Anaesth 2011](https://pubmed.ncbi.nlm.nih.gov/21903638/) |

---

## NOTES

- CIPN affects 30-70% of patients receiving neurotoxic chemotherapy, depending on agent, dose, and duration
- Most common offending agents: taxanes (paclitaxel, docetaxel), platinum compounds (cisplatin, oxaliplatin, carboplatin), vinca alkaloids (vincristine), proteasome inhibitors (bortezomib), thalidomide/lenalidomide
- CIPN pattern by agent: taxanes → predominantly sensory, length-dependent, numbness/tingling; platinums → sensory ganglionopathy (dorsal root ganglion damage), coasting; vincristine → sensorimotor with autonomic features; bortezomib → painful small fiber neuropathy, often reversible
- Coasting is unique to platinum compounds: symptoms may worsen for 2-6 months after discontinuation before stabilizing
- There is NO proven neuroprotective agent — ASCO 2020 guidelines recommend against routine use of any supplement or medication for prevention
- Duloxetine 60 mg daily is the only pharmacologic treatment with ASCO recommendation based on RCT evidence (Smith 2013)
- Gabapentin/pregabalin are widely used but lack strong CIPN-specific RCT evidence; extrapolated from general neuropathic pain trials
- Baseline EMG/NCS before chemotherapy is ideal but often impractical; document baseline neurologic exam at minimum
- Always screen for concurrent causes of neuropathy (diabetes, B12 deficiency, alcohol) as these compound CIPN risk and severity
- Fall risk is significantly elevated in CIPN — proactive balance assessment and fall prevention are essential
- Exercise is emerging as both preventive and therapeutic — recommend supervised exercise programs during chemotherapy

---

## CHANGE LOG

**v1.0 (February 9, 2026)**
- Initial template creation
- Comprehensive coverage of CIPN across common chemotherapy classes (taxanes, platinums, vinca alkaloids, proteasome inhibitors)
- Agent-specific acute management (oxaliplatin cold precautions, calcium/magnesium infusions)
- Duloxetine as evidence-based first-line treatment per ASCO 2020 guidelines
- Dose modification framework using CTCAE grading system
- Evidence references including Smith 2013 (duloxetine RCT) and Loprinzi 2020 (ASCO guideline)
