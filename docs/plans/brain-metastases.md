---
title: "Brain Metastases"
description: "Clinical decision support for brain metastases diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - epilepsy
  - cerebrovascular
  - headache
  - neurodegenerative
  - demyelinating
---

# Brain Metastases

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Brain Metastases

**ICD-10:** C79.31 (Secondary malignant neoplasm of brain), C79.32 (Secondary malignant neoplasm of cerebral meninges), C79.49 (Secondary malignant neoplasm of other parts of nervous system), G93.6 (Cerebral edema due to neoplasm)

**CPT CODES:** 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 82947 (Blood glucose), 84484 (Troponin), 84703 (Pregnancy test (β-hCG)), 83615 (LDH), 87389 (HIV, hepatitis B/C), 82533 (Cortisol (AM)), 88104 (CSF cytology / flow cytometry), 70450 (CT head without contrast), 70553 (MRI brain with and without contrast (gadolinium)), 93000 (ECG (12-lead)), 71046 (Chest X-ray), 78816 (PET/CT (FDG)), 70496 (CT angiography (head)), 62270 (LP), 96374 (Dexamethasone (vasogenic edema))

**SYNONYMS:** Brain metastases, brain mets, cerebral metastases, brain metastasis, metastatic brain tumor, secondary brain tumor, secondary brain cancer, metastatic brain disease, brain tumor from cancer, metastatic disease to brain, brain lesions, CNS metastases

**SCOPE:** Management of newly diagnosed or progressive brain metastases in adults. Covers initial stabilization, vasogenic edema management with corticosteroids, seizure management, imaging evaluation, molecular/histopathologic workup, treatment modalities (surgery, stereotactic radiosurgery, whole-brain radiation, systemic therapy with CNS penetration), and disposition. Excludes primary brain tumors (separate template), leptomeningeal carcinomatosis (partially addressed), and spinal metastases (separate template).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; chemotherapy planning; leukocytosis/infection; thrombocytopenia (bleeding risk, treatment candidacy) | WBC, platelets within normal limits; ALC (absolute lymphocyte count) for immunotherapy eligibility |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal function for contrast imaging; hepatic function for chemotherapy dosing; electrolytes (SIADH from brain lesions); glucose (steroid hyperglycemia) | Normal; anticipate glucose elevation with dexamethasone |
| PT/INR, aPTT (CPT 85610+85730) | STAT | STAT | ROUTINE | STAT | Coagulopathy assessment; surgical candidacy; hemorrhagic metastases (melanoma, RCC, choriocarcinoma, thyroid) | Normal |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Steroid-induced hyperglycemia; baseline before dexamethasone | <180 mg/dL; start insulin if persistently elevated |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Cardiac evaluation if syncope or neurogenic cardiac injury | Normal |
| Pregnancy test (β-hCG) (CPT 84703) | STAT | STAT | ROUTINE | STAT | Treatment planning; β-hCG-secreting tumors (choriocarcinoma, germ cell); radiation contraindication in pregnancy | Negative; if elevated consider choriocarcinoma or germ cell tumor |
| LDH (CPT 83615) | STAT | ROUTINE | ROUTINE | STAT | Melanoma staging; tumor burden marker; prognostic | Normal; elevated in melanoma, lymphoma |
| TSH, free T4 (CPT 84443+84439) | - | ROUTINE | ROUTINE | - | Thyroid primary (thyroid cancer with brain metastases); fatigue/cognitive symptoms differential | Normal; abnormal may indicate thyroid primary |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Tumor markers (CEA, CA 19-9, CA 125, CA 15-3, AFP, β-hCG) (CPT 82378, 86301, 86304, 82105, 84703) | - | ROUTINE | ROUTINE | - | Unknown primary: CEA (lung, GI, breast), CA 19-9 (pancreatic, GI), CA 125 (ovarian), CA 15-3 (breast), AFP (hepatocellular, germ cell), β-hCG (choriocarcinoma, germ cell) | Elevations guide primary site evaluation |
| PSA (males) | - | ROUTINE | ROUTINE | - | Prostate cancer with brain metastases (rare but occurs) | Normal; elevated guides prostate workup |
| Serum protein electrophoresis (SPEP) | - | ROUTINE | ROUTINE | - | Lymphoma/myeloma differential for CNS mass lesion | No monoclonal protein |
| HIV, hepatitis B/C (CPT 87389) | - | ROUTINE | ROUTINE | - | Primary CNS lymphoma (PCNSL) differential; immunosuppression assessment; treatment implications | Negative |
| ESR / CRP (CPT 85652+86140) | - | ROUTINE | ROUTINE | - | Infection differential (abscess vs. metastasis); inflammatory markers | Normal |
| Cortisol (AM) (CPT 82533) | - | ROUTINE | ROUTINE | - | If pituitary metastasis suspected; before initiating dexamethasone if possible | Normal (>10 mcg/dL AM) |
| Prolactin | - | ROUTINE | ROUTINE | - | Pituitary metastasis differential | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CSF cytology / flow cytometry (CPT 88104) | - | EXT | EXT | - | Leptomeningeal carcinomatosis evaluation; diagnostic if positive (sensitivity ~50% single LP, ~80% with repeat) | Negative; positive = leptomeningeal disease |
| CSF protein, glucose, cell count (CPT 84157+82945+89051) | - | EXT | EXT | - | Leptomeningeal disease (elevated protein, low glucose, lymphocytic pleocytosis) | Normal; elevated protein and low glucose suggest LMD |
| Circulating tumor DNA (ctDNA) / liquid biopsy | - | EXT | EXT | - | Unknown primary; molecular profiling when tissue biopsy not feasible; monitor treatment response | Detectable mutations guide therapy |
| Next-generation sequencing (NGS) - blood | - | EXT | EXT | - | Identify actionable mutations (EGFR, ALK, BRAF, HER2, KRAS, ROS1) when tissue insufficient | Actionable driver mutations |
| Paraneoplastic antibody panel | - | EXT | EXT | - | If clinical presentation suggests paraneoplastic syndrome mimicking or coexisting with metastatic disease | Negative; positive changes management |
| Methylmalonic acid, B12, folate | - | EXT | ROUTINE | - | Cognitive decline differential | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediate in ED for acute presentation; identifies hemorrhage, mass effect, hydrocephalus | Mass lesion(s), hemorrhage, edema, midline shift, hydrocephalus; hemorrhagic metastases suggest melanoma, RCC, choriocarcinoma, thyroid | Pregnancy (benefit outweighs risk) |
| MRI brain with and without contrast (gadolinium) (CPT 70553) | STAT | STAT | URGENT | STAT | Within 24h of presentation; GOLD STANDARD for brain metastases; thin-cut (≤1mm) 3D T1 post-contrast | Number/size/location of metastases; ring-enhancement pattern; hemorrhagic component; leptomeningeal enhancement; dural-based vs. parenchymal | MRI-incompatible implants; GFR <30 (gadolinium risk); severe claustrophobia |
| CT chest/abdomen/pelvis with contrast (CPT 71260+74178) | URGENT | URGENT | ROUTINE | - | Within 24-48h if unknown primary; staging for known primary | Primary tumor identification; staging; additional metastatic disease | Contrast allergy; renal impairment |
| ECG (12-lead) (CPT 93000) | STAT | STAT | - | STAT | Baseline; pre-treatment; QTc for anti-emetics/targeted therapies | Normal | None |
| Chest X-ray (CPT 71046) | STAT | STAT | - | STAT | Lung primary (most common source of brain metastases); pulmonary metastases; aspiration if obtunded | Lung mass; effusion; lymphadenopathy | Pregnancy (shield) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| PET/CT (FDG) (CPT 78816) | - | ROUTINE | ROUTINE | - | Outpatient or during hospitalization; staging; unknown primary identification; ~85% sensitivity for primary site | Primary tumor; additional metastatic disease; lymph node involvement; treatment response assessment | Uncontrolled diabetes (glucose >200 impairs uptake); pregnancy |
| CT angiography (head) (CPT 70496) | URGENT | URGENT | - | URGENT | If hemorrhagic metastasis to evaluate vascularity; pre-surgical planning | Tumor vascularity; relationship to major vessels | Contrast allergy; renal impairment |
| MR spectroscopy (MRS) | - | ROUTINE | ROUTINE | - | Differentiating tumor from abscess or radiation necrosis; elevated choline:creatine ratio in tumor; lipid/lactate peak in necrosis | Elevated choline, reduced NAA in tumor; elevated lipid/lactate in necrosis | Same as MRI |
| MR perfusion (DSC or DCE) | - | ROUTINE | ROUTINE | - | Differentiating tumor recurrence from radiation necrosis; elevated rCBV in tumor | Elevated rCBV (>1.5-2.0) suggests tumor; low rCBV suggests radiation necrosis | Same as MRI |
| MRI spine (whole) with contrast (CPT 72156+72157+72158) | - | URGENT | ROUTINE | - | If spinal symptoms or leptomeningeal disease suspected; staging for drop metastases | Spinal metastases; leptomeningeal enhancement; cord compression | Same as MRI |
| Mammography / breast MRI (females) | - | ROUTINE | ROUTINE | - | Breast cancer is 2nd most common source of brain metastases in women | Breast mass or abnormality | Breast implants (mammography may be limited) |
| Stereotactic biopsy planning MRI | - | URGENT | ROUTINE | - | If tissue diagnosis needed and surgical resection not planned; fiducial/frameless navigation sequences | Biopsy trajectory planning; avoidance of eloquent cortex and vasculature | Same as MRI |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Thallium SPECT or FET-PET | - | - | EXT | - | Differentiating recurrent tumor vs. radiation necrosis when MR perfusion/spectroscopy equivocal | Increased uptake = tumor; decreased uptake = necrosis | Pregnancy |
| Functional MRI (fMRI) | - | - | EXT | - | Pre-surgical planning for metastases near eloquent cortex (motor, language areas) | Motor/language cortex mapping relative to lesion | Same as MRI |
| Diffusion tensor imaging (DTI) / Tractography | - | - | EXT | - | Pre-surgical planning; white matter tract relationship to tumor | Tract displacement vs. infiltration | Same as MRI |
| CT-guided biopsy (extracranial) | - | ROUTINE | ROUTINE | - | Biopsy accessible extracranial metastatic site rather than brain (safer, easier tissue acquisition) | Histopathologic diagnosis; molecular profiling | Coagulopathy; site-specific risks |

### Lumbar Puncture (if indicated)

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP (CPT 62270) with CSF cytology, flow cytometry, protein, glucose, cell count | - | URGENT | EXT | URGENT | If leptomeningeal disease suspected (cranial neuropathies, radiculopathy, headache, altered mentation without adequate parenchymal lesion to explain); MUST ensure no obstructive hydrocephalus or significant mass effect first | Cytology: malignant cells (50% sensitivity single LP; repeat improves to ~80%); elevated opening pressure; elevated protein (>50 mg/dL); low glucose (<40 mg/dL or <60% serum); lymphocytic pleocytosis | CONTRAINDICATED if significant mass effect, large posterior fossa lesion, obstructive hydrocephalus, midline shift >5mm (herniation risk); coagulopathy; local infection at LP site |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Dexamethasone (vasogenic edema)** (CPT 96374) | IV | - | 10 mg :: IV :: q6h :: **Symptomatic edema:** 10 mg IV loading dose, then 4 mg IV/PO q6h; **Moderate symptoms:** 4-8 mg/day; **Severe/impending herniation:** 10 mg IV bolus then 4-8 mg IV q6h (up to 16-24 mg/day); Taper as soon as clinically feasible over 2-4 weeks; GI prophylaxis with PPI (omeprazole 20 mg daily) while on steroids; Monitor glucose q6h initially | - | Dexamethasone is preferred corticosteroid (minimal mineralocorticoid effect, long half-life); symptomatic improvement in 24-72h; reduces vasogenic edema via BBB stabilization; no benefit in asymptomatic patients without edema (AVOID routine prophylactic use) | STAT | STAT | URGENT | STAT |
| **Seizure management (acute)** | IV | - | 0.1 mg/kg :: IV :: - :: **Active seizure:** Lorazepam 0.1 mg/kg IV (max 4 mg), may repeat x1 in 5 min; **Then:** Levetiracetam 1000-1500 mg IV load (preferred - no drug interactions with chemotherapy) OR valproic acid 20-30 mg/kg IV load (avoid with hepatic metastases); Phenytoin/fosphenytoin only if above unavailable (interacts with many chemotherapies and targeted agents) | - | Levetiracetam preferred: no hepatic enzyme induction (does NOT reduce efficacy of steroids, chemotherapy, or targeted agents), renal elimination, broad spectrum; AAN guidelines do NOT recommend prophylactic AEDs in brain tumor patients without seizures | STAT | STAT | - | STAT |
| **No prophylactic anticonvulsants** | - | - | N/A :: - :: per protocol :: Do NOT start AEDs prophylactically in patients with brain metastases who have NOT had seizures; Applicable even peri-operatively (surgical prophylaxis may be used 7 days only per institutional protocol) | - | AAN Practice Parameter (Glantz et al., 2000; reaffirmed): No evidence supporting prophylactic AED use in brain tumor patients; side effects outweigh benefits; ASCO guideline concordant | STAT | STAT | ROUTINE | STAT |
| **Airway/ICP management (obtunded patient)** | IV | - | 1-1.5 g/kg :: IV :: once :: **GCS ≤8:** Intubation; elevate HOB 30°; **Acute herniation:** Mannitol 1-1.5 g/kg IV bolus OR hypertonic saline (23.4% NaCl 30 mL via central line over 15 min or 3% NaCl 250 mL over 30 min); maintain PaCO2 30-35 mmHg (brief hyperventilation only as bridge to definitive treatment); Emergent neurosurgery consult for decompression | - | ICP management as bridge to definitive treatment (surgery/radiation); prolonged hyperventilation causes cerebral ischemia; osmotherapy reduces cerebral edema | STAT | - | - | STAT |
| **DVT prophylaxis** | SC | - | 40 mg :: SC :: q8h :: SCDs (sequential compression devices) immediately on admission; Pharmacologic prophylaxis: enoxaparin 40 mg SQ daily or heparin 5000 units SQ q8h - START within 24-48h unless hemorrhagic metastasis or planned surgery within 24h; Post-craniotomy: restart pharmacologic DVT ppx within 24-48h per neurosurgery guidance | - | Brain tumor patients have 20-30% VTE risk; mechanical prophylaxis alone insufficient; pharmacologic prophylaxis does NOT significantly increase intracranial hemorrhage risk (Perry et al., 2009; AVERT trial) | - | STAT | - | STAT |
| **Stress ulcer prophylaxis** | PO | - | 20 mg :: PO :: daily :: PPI (omeprazole 20 mg daily or pantoprazole 40 mg daily) while on dexamethasone; continue throughout steroid course | - | Combined corticosteroid + critical illness increases GI bleed risk | STAT | STAT | ROUTINE | STAT |

### 3B. Definitive/Targeted Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Surgical resection** | - | - | 60% :: - :: - :: **Indications:** Single (or limited ≤3) accessible metastasis; need for tissue diagnosis; symptomatic mass effect not responding to steroids; large lesion (>3-4 cm) not suitable for SRS alone; good performance status (KPS ≥70); controlled systemic disease; life expectancy >3 months; **Post-op:** MRI within 24-48h to assess residual; SRS to cavity within 2-4 weeks to reduce local recurrence (50-60% → 15-20%) | - | Patchell et al. (1990): Surgery + WBRT > WBRT alone for single brain metastasis (median survival 40 vs. 15 weeks); Cavity SRS post-resection: Mahajan et al. (2017): local control improved with cavity SRS vs. observation | - | URGENT | - | - |
| **Stereotactic radiosurgery (SRS)** | - | - | N/A :: - :: once :: **Indications:** 1-4 metastases (most centers), up to 10-15 in select cases (JLGK0901); size ≤3-4 cm; **Dose:** Single fraction 15-24 Gy (dose based on size: ≤2cm: 20-24 Gy, 2.1-3cm: 18 Gy, 3.1-4cm: 15 Gy) OR fractionated SRS (3-5 fractions for larger lesions or eloquent location); **Timing:** Within 2-4 weeks of diagnosis; Serial MRI q2-3 months post-SRS | - | Yamamoto et al. (JLGK0901): SRS alone for 2-10 metastases non-inferior to 2-4 for survival; SRS vs. WBRT: better cognitive preservation (NCCTG N0574, Brown et al., 2016); SRS + HA-WBRT vs SRS alone per NRG-CC003 | - | URGENT | ROUTINE | - |
| **Whole-brain radiation therapy (WBRT)** | - | - | 20 mg :: - :: daily :: **Indications:** >10-15 metastases; leptomeningeal disease; poor surgical/SRS candidates; miliary/diffuse pattern; **Standard:** 30 Gy in 10 fractions (or 20 Gy in 5 fractions for poor prognosis); **Hippocampal avoidance (HA-WBRT):** Preferred when technically feasible (no metastases within 5mm of hippocampus): 30 Gy in 10 fractions with hippocampal sparing + memantine 20 mg daily starting with WBRT x 6 months | - | HA-WBRT + memantine (NRG-CC001, Brown et al., 2020): significantly less cognitive deterioration vs. standard WBRT + memantine at 4 and 6 months; Memantine alone (RTOG 0614): trend toward better cognitive function | - | URGENT | ROUTINE | - |
| **Systemic therapy with CNS activity** | - | - | 80 mg :: - :: daily :: **NSCLC with EGFR mutation:** Osimertinib 80 mg daily (CNS response rate 91%); **NSCLC with ALK rearrangement:** Lorlatinib 100 mg daily (intracranial response 82%) or alectinib 600 mg BID (CNS response 81%); **NSCLC with ROS1:** Lorlatinib; **Melanoma with BRAF V600:** Dabrafenib + trametinib (intracranial response 58%) or encorafenib + binimetinib; **Melanoma (any):** Ipilimumab + nivolumab (intracranial response 46-57% in asymptomatic); **HER2+ breast:** Tucatinib + trastuzumab + capecitabine (HER2CLIMB: intracranial response 47%); **Breast (HR+):** Abemaciclib (some CNS activity); **RCC:** Nivolumab + ipilimumab or cabozantinib | - | CNS-penetrant systemic therapy increasingly used as upfront or adjunct to SRS; may defer radiation in asymptomatic patients with actionable mutations and small metastases; Always coordinate with medical oncology | - | ROUTINE | ROUTINE | - |
| **Corticosteroid taper** | - | - | 2 mg :: - :: once :: Begin taper once definitive treatment initiated and symptoms improving; **Taper schedule:** Reduce by 2 mg every 3-5 days (from 16 mg/day: 16→12→8→6→4→2→1→off); Slower taper if symptoms recur; Monitor for adrenal insufficiency if >3 weeks of steroid use | - | Prolonged steroids cause significant morbidity: hyperglycemia, myopathy (steroid myopathy can be debilitating), immunosuppression, osteoporosis, PJP risk, insomnia, psychiatric effects, GI bleeding | - | ROUTINE | ROUTINE | - |

### 3C. Adjunctive Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Levetiracetam (post-seizure maintenance)** | IV | - | 500-1500 mg :: IV :: BID :: 500-1500 mg PO/IV BID (start 500 mg BID, titrate to seizure control); Renal dosing if GFR <50; No drug interactions with chemotherapy, targeted therapy, or steroids | - | Preferred AED in brain tumor patients due to no CYP enzyme induction; does not reduce efficacy of dexamethasone, temozolomide, or targeted agents | - | STAT | ROUTINE | STAT |
| **PJP prophylaxis** | PO | - | 20 mg :: PO :: daily :: If dexamethasone >20 mg/week AND concomitant temozolomide or immunosuppression: TMP-SMX 1 DS tablet 3x/week (Mon/Wed/Fri) OR atovaquone 1500 mg daily if sulfa allergic | - | Risk of Pneumocystis with prolonged corticosteroids + additional immunosuppression | - | ROUTINE | ROUTINE | - |
| **Glucose management (steroid-induced)** | - | - | 180 mg :: - :: q6h :: Fingerstick glucose q6h while on dexamethasone; Sliding scale insulin initially; Basal-bolus insulin if persistently >180 mg/dL; Anticipate glucose elevation typically 4-8 hours after steroid dose; May need 2-3x baseline insulin requirements | - | Dexamethasone causes significant hyperglycemia in 50-60% of patients; uncontrolled hyperglycemia worsens outcomes | STAT | STAT | ROUTINE | STAT |
| **Calcium/Vitamin D** | PO | - | 1000-1200 mg :: PO :: daily :: Calcium 1000-1200 mg + Vitamin D 800-1000 IU daily while on prolonged steroids (>2 weeks) | - | Steroid-induced osteoporosis prevention | - | ROUTINE | ROUTINE | - |
| **Anti-emetics (for radiation/chemotherapy)** | IV | - | 4-8 mg :: IV :: q8h :: Ondansetron 4-8 mg IV/PO q8h PRN; Dexamethasone itself is anti-emetic; Avoid metoclopramide in brain metastases patients (extrapyramidal effects) | - | Nausea common with elevated ICP and with radiation therapy | - | ROUTINE | ROUTINE | - |
| **Memantine (with WBRT)** | - | - | 5 mg :: - :: daily :: 5 mg daily x1 week → 5 mg BID x1 week → 10 mg AM + 5 mg PM x1 week → 10 mg BID; Continue for 6 months total; Start day 1 of WBRT | - | RTOG 0614 and NRG-CC001: cognitive protection during WBRT; NMDA receptor antagonist reduces excitotoxic neuronal injury from radiation | - | ROUTINE | ROUTINE | - |

### 3D. Medications to AVOID or Use with Caution

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Prophylactic anticonvulsants (in patients without seizures) | - | - | - | - | - | - | - | - | - | - |
| Phenytoin / Carbamazepine / Phenobarbital (enzyme-inducing AEDs) | - | - | - | - | - | - | - | - | - | - |
| Bevacizumab (concurrent with surgery) | - | - | - | - | - | - | - | - | - | - |
| Anticoagulation (full-dose, peri-operative) | - | - | - | - | - | - | - | - | - | - |
| Methotrexate (high-dose, with brain radiation) | - | - | - | - | - | - | - | - | - | - |
| Live vaccines (while on dexamethasone or chemotherapy) | - | - | - | - | - | - | - | - | - | - |
| Lumbar puncture (with large posterior fossa lesion / significant mass effect) | - | - | - | - | - | - | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Neurosurgery consultation | STAT | STAT | ROUTINE | STAT | For surgical candidacy evaluation (single/oligometastases, mass effect, tissue diagnosis need); emergency for herniation/acute hydrocephalus |
| Radiation oncology consultation | - | URGENT | ROUTINE | - | SRS vs. WBRT vs. HA-WBRT decision; coordinate with surgery (post-resection cavity SRS within 2-4 weeks) |
| Medical oncology consultation | - | URGENT | ROUTINE | - | Systemic therapy options; molecular profiling for targeted agents; staging; prognosis; clinical trial eligibility |
| Multidisciplinary tumor board | - | URGENT | ROUTINE | - | Brain metastases management requires coordinated neurosurgery, radiation oncology, medical oncology, neuroradiology input; optimal sequencing of treatments |
| Goals of care discussion | - | URGENT | ROUTINE | URGENT | Discuss prognosis, treatment intent (curative vs. palliative), quality of life, code status; especially important for patients with limited systemic options or poor functional status (KPS <50) |
| Pathology review with molecular profiling | - | URGENT | ROUTINE | - | Confirm tissue diagnosis; molecular testing (NGS panel for EGFR, ALK, ROS1, BRAF, HER2, KRAS G12C, NTRK, RET, MET); PD-L1 (TPS and CPS); hormone receptors (breast); BRAF V600 (melanoma) |
| Fall precautions | STAT | STAT | ROUTINE | STAT | Brain metastases patients at high risk for falls (focal deficits, seizures, steroid myopathy, cognitive impairment); Remove fall hazards; PT/OT evaluation |
| Driving restrictions | - | ROUTINE | ROUTINE | - | Advise against driving if seizures, visual field deficits, significant cognitive impairment, or posterior fossa lesions affecting coordination; State-specific reporting requirements |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Palliative care consultation | - | ROUTINE | ROUTINE | - | Symptom management; goals of care facilitation; advance care planning; coordination of hospice if appropriate |
| Neuropsychology evaluation | - | - | ROUTINE | - | Baseline cognitive assessment before radiation treatment; monitor cognitive decline; guide rehabilitation |
| Physical/occupational therapy | - | ROUTINE | ROUTINE | - | Functional assessment; mobility training; ADL assistance; steroid myopathy mitigation (exercise program) |
| Speech-language pathology | - | ROUTINE | ROUTINE | - | If aphasia, dysarthria, dysphagia from metastasis location; swallow evaluation if posterior fossa lesion or obtunded |
| Social work / case management | - | ROUTINE | ROUTINE | - | Insurance authorization for SRS/radiation; transportation; caregiver support; disability paperwork |
| Genetic counseling | - | - | ROUTINE | - | If young patient or cancer predisposition syndrome suspected (Li-Fraumeni, BRCA, Lynch) |
| Clinical trials evaluation | - | ROUTINE | ROUTINE | - | Active brain metastases trials (immunotherapy combinations, targeted agents, radiosensitizers); NCI clinical trials database; institutional trials |
| Ophthalmology consultation | - | ROUTINE | ROUTINE | - | If visual complaints, papilledema, metastasis near visual pathways; formal visual fields testing |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Repeat biopsy / resection | - | URGENT | ROUTINE | - | If radiation necrosis vs. recurrence unclear after advanced imaging (MR perfusion, MRS, PET); tissue diagnosis changes management |
| Ommaya reservoir placement | - | ROUTINE | ROUTINE | - | Recurrent leptomeningeal disease requiring intrathecal chemotherapy; avoids repeated lumbar punctures |
| Intrathecal chemotherapy | - | ROUTINE | ROUTINE | - | Leptomeningeal carcinomatosis: methotrexate 12 mg IT or cytarabine (liposomal) 50 mg IT q2 weeks; via Ommaya reservoir; limited efficacy data |
| Laser interstitial thermal therapy (LITT) | - | ROUTINE | ROUTINE | - | MRI-guided laser ablation for recurrent metastases in deep or eloquent locations; radiation necrosis treatment |
| Re-irradiation (SRS for recurrence) | - | - | ROUTINE | - | SRS for recurrent metastases after prior SRS or WBRT; consider cumulative dose to normal brain; risk of radiation necrosis increases |
| Bevacizumab for radiation necrosis | - | ROUTINE | ROUTINE | - | 7.5 mg/kg IV q3 weeks for symptomatic radiation necrosis refractory to steroids; significant improvement in ~65% of patients (Levin et al., 2011) |
| Hospice referral | - | ROUTINE | ROUTINE | - | Poor prognosis (DS-GPA <1.0), declining functional status, exhausted treatment options, patient/family preference for comfort-focused care |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Primary Differential Diagnoses

| Diagnosis | Key Differentiating Features | Distinguishing Studies |
|-----------|------------------------------|----------------------|
| Primary brain tumor (GBM, astrocytoma) | Usually single; irregular enhancement; often involves corpus callosum (butterfly GBM); no known systemic cancer; infiltrative margins; surrounding FLAIR/T2 more extensive; restricted diffusion at tumor margins | MRI pattern; MR spectroscopy (elevated choline:creatine, reduced NAA); biopsy (IDH, MGMT, 1p19q); no systemic disease on staging CT/PET |
| Primary CNS lymphoma (PCNSL) | Periventricular location; homogeneously enhancing; restricted diffusion; may be multifocal; immunocompromised patients; responds dramatically to corticosteroids (may "disappear" = ghost tumor); typically does NOT ring-enhance unless HIV | MRI with diffusion restriction; AVOID steroids before biopsy if possible (may render biopsy non-diagnostic); CSF flow cytometry; vitreous biopsy if ocular involvement; HIV testing; slit lamp exam |
| Brain abscess | Ring-enhancing lesion with restricted diffusion on DWI (bright on DWI, dark on ADC in the cavity — metastases typically do NOT show central restricted diffusion); fever, elevated WBC; recent sinusitis/otitis/dental procedure/endocarditis; thin smooth enhancing rim; satellite lesions | DWI: central restricted diffusion is KEY distinguishing feature; MR spectroscopy: amino acid peaks (succinate, acetate, lactate); blood cultures; echocardiogram; source identification |
| Toxoplasmosis (immunocompromised) | HIV/AIDS (CD4 <100); multiple ring-enhancing lesions; basal ganglia predilection; eccentric target sign; edema/mass effect | Toxoplasma IgG (serum); CD4 count; empiric treatment trial (response in 10-14 days supports diagnosis); if no response → biopsy; Thallium SPECT (increased uptake = lymphoma, not toxoplasmosis) |
| Demyelinating disease (tumefactive MS, ADEM) | Incomplete ring enhancement (open ring sign); younger patients; clinical dissemination in time/space; less mass effect relative to lesion size; leading edge enhancement | MRI: open ring enhancement, T2/FLAIR lesions in MS-typical locations; CSF: oligoclonal bands; MOG/AQP4 antibodies; clinical response to steroids |
| Radiation necrosis | History of prior brain radiation (typically 6-24 months post-treatment but can occur later); enhancing lesion at site of prior radiation; difficult to distinguish from recurrent tumor on conventional MRI | MR perfusion: LOW rCBV (vs. tumor with HIGH rCBV); MR spectroscopy: elevated lipid/lactate, low choline; PET: low FDG uptake (vs. tumor with high uptake); biopsy if equivocal |
| Neurocysticercosis | Travel/residence in endemic area (Latin America, sub-Saharan Africa, Southeast Asia); cystic lesions with scolex (dot within cyst); often calcified in chronic phase; seizure is common presentation | MRI: cystic lesion with scolex; CT: calcified granulomas; serology (cysticercosis antibodies); stool ova/parasites |
| Cerebral infarct (subacute) | Vascular territory distribution; ring enhancement at 1-4 weeks post-stroke (luxury perfusion); clinical history of acute onset; DWI abnormalities conforming to vascular territory | Timing of enhancement (subacute strokes enhance transiently); vascular territory distribution; DWI/ADC map evolution; clinical history of acute onset |

### Red Flags Requiring Urgent Reassessment

| Red Flag | Concern | Action |
|----------|---------|--------|
| Rapid neurologic decline | Hemorrhage into metastasis; acute hydrocephalus; herniation | STAT CT head; neurosurgery STAT; consider intubation |
| New seizure (first-time) | Peri-tumoral irritation; hemorrhage; edema worsening; leptomeningeal spread | CT head (rule out hemorrhage); start AED (levetiracetam); re-image with MRI |
| Worst headache of life / thunderclap | Hemorrhagic metastasis (especially melanoma, RCC); pituitary apoplexy from pituitary metastasis | STAT CT head; CT angiography if SAH pattern |
| Fever + mental status changes | Brain abscess (metastasis can be misdiagnosed as abscess and vice versa); infection in immunocompromised patient; central fever from brain lesion | Blood cultures; CT head; LP if safe; broad-spectrum antibiotics if infection suspected |
| Acute vision loss | Pituitary metastasis with apoplexy; optic nerve/chiasm compression | STAT MRI; ophthalmology/neurosurgery STAT |
| Progressive bilateral leg weakness | Spinal cord compression from spinal metastases; leptomeningeal disease affecting cauda equina | STAT MRI whole spine; dexamethasone 10 mg IV; neurosurgery/radiation oncology STAT |
| Cushing syndrome features (steroid complications) | Prolonged dexamethasone; immunosuppression; hyperglycemia; myopathy; osteoporosis | Taper steroids; manage complications; alternative edema management (bevacizumab for radiation necrosis) |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (First 72h)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic checks (GCS, pupil reactivity, motor exam, speech) | q1-2h in ICU; q2-4h on floor | Stable or improving exam | Stat CT head if decline; neurosurgery alert; consider increasing dexamethasone or osmotherapy |
| Blood glucose | q6h (q1h if insulin drip) | 140-180 mg/dL | Sliding scale → basal-bolus insulin; typically requires 2-3x baseline insulin on dexamethasone |
| Blood pressure | Continuous in ICU; q4h on floor | SBP <160 (avoid hypertensive hemorrhage into metastasis) | Antihypertensives PRN; avoid excessive hypotension (SBP >100 to maintain cerebral perfusion) |
| Fluid balance / I&O | q8h | Euvolemia | Hyponatremia common (SIADH, cerebral salt wasting); free water restriction if SIADH |
| Sodium | q6-8h initially | 135-145 mEq/L | If <130: fluid restrict; if <125 or symptomatic: 3% NaCl; if rapidly dropping: urgent sodium correction |
| Seizure monitoring | Continuous observation; consider cEEG if altered mental status | No seizures; no subclinical seizures | AED initiation/adjustment; neurology consultation; continuous EEG monitoring |
| Pain assessment | q4h | NRS <4/10 | Acetaminophen 650-1000 mg q6h; dexamethasone (reduces headache from edema); opioids PRN for moderate-severe |

### Subacute/Outpatient Monitoring

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| MRI brain with contrast | q2-3 months for first year post-treatment, then q3-4 months year 2, then q6 months | Stable/decreasing lesion size; no new metastases | New/progressive lesions: repeat multidisciplinary discussion; salvage SRS, surgery, systemic therapy change |
| Neurologic examination | Each clinic visit (q2-4 weeks during treatment, q1-3 months maintenance) | Stable or improved | New deficits: urgent MRI; consider tumor progression vs. radiation necrosis vs. new metastasis |
| KPS / ECOG performance status | Each visit | KPS ≥70 / ECOG 0-2 for active treatment | KPS <50 / ECOG ≥3: reassess goals of care; transition to supportive/palliative care |
| Steroid taper progress | Each visit | Off dexamethasone or minimal dose | Steroid-dependent edema: consider bevacizumab, re-irradiation, or resection to enable taper |
| Blood glucose (while on steroids) | Daily fingerstick; HbA1c monthly | Fasting <130; random <180 | Insulin titration; endocrine consultation if difficult to control |
| CBC (if on chemotherapy) | Per chemotherapy cycle protocol; typically q2-3 weeks | ANC >1500, platelets >100,000 | Hold/dose-reduce chemotherapy; growth factor support |
| Hepatic/renal function | Monthly during systemic therapy | Normal | Dose adjustment; drug-specific monitoring per protocol |
| Neurocognitive screening | q3-6 months; MoCA or formal neuropsychological testing | Stable cognitive function | Cognitive rehabilitation; medication review; assess for depression; differentiate radiation injury vs. progression |
| Depression/anxiety screening (PHQ-9) | Each visit | PHQ-9 <5 | SSRI (avoid CYP interactions); psychology referral; supportive care |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| ICU admission | GCS ≤12; signs of herniation (pupil asymmetry, posturing, Cushing triad); acute hemorrhage into metastasis with neurologic decline; post-craniotomy (first 24h); status epilepticus; respiratory compromise requiring intubation; hemodynamic instability |
| General neurology/neurosurgery floor | New diagnosis requiring workup and treatment planning; symptomatic edema requiring IV dexamethasone; post-seizure requiring monitoring and AED optimization; post-craniotomy (step-down from ICU); functional decline requiring inpatient rehabilitation planning |
| Observation (≤24h) | Known brain metastases with mild symptom change; MRI revealing progression but patient clinically stable; steroid dose adjustment with monitoring |

### Discharge Criteria

| Criterion | Details |
|-----------|---------|
| Neurologic stability | Stable or improving neurologic exam for ≥24h on current steroid dose; no new deficits |
| Seizure control | Seizure-free ≥24h on oral AED; no breakthrough seizures; AED levels therapeutic if applicable |
| Steroid plan | Oral dexamethasone regimen established with clear taper schedule; glucose management plan in place |
| Pain control | Headache adequately controlled on oral medications |
| Treatment plan established | Multidisciplinary plan documented (surgery, radiation, systemic therapy); appointments scheduled within 1-2 weeks |
| Functional safety | Safe ambulation (with or without assistive device); safe swallowing; able to perform basic ADLs or adequate caregiver support |
| VTE plan | Transition to pharmacologic prophylaxis or therapeutic anticoagulation plan if VTE occurred |
| Follow-up arranged | Neurosurgery (1-2 weeks if post-op), radiation oncology (1-2 weeks for SRS/WBRT planning), medical oncology (1-2 weeks), PCP (1 week for steroid monitoring); MRI brain scheduled at appropriate interval |
| Patient/family education | Understanding of diagnosis, treatment plan, steroid side effects, seizure precautions, when to return to ED (acute headache, new weakness, seizure, vision changes, fever) |

### Discharge Prescriptions Checklist

| Medication | Details |
|-----------|---------|
| Dexamethasone | Taper schedule clearly documented (e.g., 4 mg q6h x 3 days → 4 mg q8h x 3 days → 4 mg q12h x 3 days → 4 mg daily x 3 days → 2 mg daily x 3 days → stop) |
| PPI | Omeprazole 20 mg daily or pantoprazole 40 mg daily while on steroids |
| AED (if seizure occurred) | Levetiracetam dose and frequency; DO NOT start if no seizure history |
| Insulin (if needed) | Sliding scale or basal-bolus regimen for steroid-induced hyperglycemia; glucometer and supplies |
| Calcium + Vitamin D | If steroids >2 weeks anticipated |
| DVT prophylaxis (if applicable) | Enoxaparin transition plan if VTE occurred |
| Analgesics | Acetaminophen; limited opioid prescription if needed |
| TMP-SMX (if applicable) | If on high-dose steroids + chemotherapy (PJP prophylaxis) |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| Management of Brain Metastases | Congress of Neurological Surgeons (CNS) / AANS Systematic Review | 2019 | Surgery for single accessible metastasis with mass effect; SRS for limited brain metastases (1-4); WBRT for multiple (>10-15) or leptomeningeal disease; avoid prophylactic AEDs |
| Brain Metastases Molecular Testing | NCCN Central Nervous System Cancers | v1.2025 | Comprehensive molecular profiling for actionable targets (EGFR, ALK, ROS1, BRAF, HER2, KRAS G12C, NTRK, RET, MET, PD-L1); guide systemic therapy selection |
| Prophylactic Anticonvulsants | [AAN Practice Parameter (Glantz et al.)](https://pubmed.ncbi.nlm.nih.gov/41456935/) | 2000 (reaffirmed) | Routine prophylactic AEDs NOT recommended in brain tumor patients without seizures |
| Hippocampal Avoidance WBRT | [NRG-CC001 (Brown et al.)](https://pubmed.ncbi.nlm.nih.gov/32058845/) | 2020 | HA-WBRT + memantine superior to standard WBRT + memantine for cognitive preservation |
| SRS for Multiple Brain Metastases | [JLGK0901 (Yamamoto et al.)](https://pubmed.ncbi.nlm.nih.gov/24621620/) | 2014 | SRS for 5-10 metastases non-inferior to 2-4 for overall survival |
| Cognitive Outcomes SRS vs. WBRT | [NCCTG N0574 (Brown et al.)](https://pubmed.ncbi.nlm.nih.gov/27458945/) | 2016 | SRS alone superior to SRS + WBRT for cognitive preservation; no overall survival difference |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [Patchell et al. (1990)](https://pubmed.ncbi.nlm.nih.gov/2405271/) | Surgery + WBRT vs. WBRT alone for single brain metastasis: median survival 40 vs. 15 weeks; lower recurrence at original site (20% vs. 52%) | Established surgery as standard for single brain metastasis |
| [Patchell et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9809728/) | Post-operative WBRT reduced brain recurrence (18% vs. 70%) but no survival benefit; improved neurologic death | Supported adjuvant radiation after surgery; now often SRS to cavity instead of WBRT |
| [Mahajan et al. (2017) - MD Anderson](https://pubmed.ncbi.nlm.nih.gov/28687375/) | SRS to surgical cavity vs. observation: 12-month local recurrence 28% vs. 59% (HR 0.46) | Established post-operative cavity SRS as standard of care |
| [Brown et al. (2016) - NCCTG N0574](https://pubmed.ncbi.nlm.nih.gov/27458945/) | SRS alone vs. SRS + WBRT: cognitive deterioration at 3 months 64% vs. 92%; no OS difference | Shifted practice toward SRS alone with surveillance MRI rather than WBRT |
| [Yamamoto et al. (2014) - JLGK0901](https://pubmed.ncbi.nlm.nih.gov/24621620/) | SRS for 5-10 vs. 2-4 brain metastases: similar overall survival (10.8 vs. 10.8 months) | Expanded SRS indications to higher numbers of metastases |
| [Brown et al. (2020) - NRG-CC001](https://pubmed.ncbi.nlm.nih.gov/32058845/) | HA-WBRT + memantine vs. WBRT + memantine: less cognitive deterioration at 4 months (59% vs. 68%) and 6 months; less decline in executive function and memory | HA-WBRT + memantine = new standard when WBRT indicated |
| [Tawbi et al. (2018) - CheckMate 204](https://pubmed.ncbi.nlm.nih.gov/30134131/) | Ipilimumab + nivolumab in melanoma brain metastases: intracranial response 57% in asymptomatic patients | Established immunotherapy as upfront option for melanoma brain metastases |
| [Reungwetwattana et al. (2018) - FLAURA CNS analysis](https://pubmed.ncbi.nlm.nih.gov/30153097/) | Osimertinib CNS response rate 91% in EGFR-mutant NSCLC with brain metastases vs. 68% standard EGFR TKI | Established osimertinib as preferred first-line for EGFR+ NSCLC with brain metastases |
| [Murthy et al. (2020) - HER2CLIMB](https://pubmed.ncbi.nlm.nih.gov/31825569/) | Tucatinib + trastuzumab + capecitabine: intracranial response 47%; CNS-PFS 9.9 vs. 4.2 months; OS benefit in brain metastases subgroup | Established tucatinib combination as standard for HER2+ breast cancer brain metastases |
| [Perry et al. (2010) - PRODIGE](https://pubmed.ncbi.nlm.nih.gov/20598077/) | Dalteparin vs. placebo in malignant glioma: no increase in intracranial hemorrhage with anticoagulation; VTE reduction | Supported pharmacologic DVT prophylaxis in brain tumor patients |
| [Levin et al. (2011)](https://pubmed.ncbi.nlm.nih.gov/20399573/) | Bevacizumab for radiation necrosis: significant radiographic and clinical improvement in ~65% of patients | Established bevacizumab as treatment option for symptomatic radiation necrosis refractory to steroids |

### Grading Scales

**Diagnosis-Specific Graded Prognostic Assessment (DS-GPA)**

| Component | Score = 0 | Score = 0.5 | Score = 1.0 |
|-----------|-----------|-------------|-------------|
| Age (years) | >60 | 50-60 | <50 |
| KPS | <70 | 70-80 | 90-100 |
| Number of CNS metastases | >3 | 2-3 | 1 |
| Extracranial metastases | Present | - | Absent |

*Note: DS-GPA varies by primary tumor type. The above is the general framework. Lung-molGPA incorporates molecular markers (EGFR, ALK). Melanoma-molGPA incorporates BRAF status. Breast-GPA incorporates receptor status (HR/HER2). Always use the disease-specific GPA tool.*

| DS-GPA Score (general) | Median Survival |
|------------------------|----------------|
| 0-1.0 | 2.6 months |
| 1.5-2.0 | 4.4 months |
| 2.5-3.0 | 9.4 months |
| 3.5-4.0 | 14.8 months |

**Recursive Partitioning Analysis (RPA) Classification (RTOG)**

| Class | Criteria | Median Survival |
|-------|----------|----------------|
| Class I | KPS ≥70, age <65, controlled primary, no extracranial metastases | 7.1 months |
| Class II | All other patients | 4.2 months |
| Class III | KPS <70 | 2.3 months |

**Karnofsky Performance Status (KPS)**

| Score | Description |
|-------|-------------|
| 100 | Normal, no complaints |
| 90 | Able to carry on normal activity; minor signs/symptoms |
| 80 | Normal activity with effort; some signs/symptoms |
| 70 | Cares for self; unable to carry on normal activity or active work |
| 60 | Requires occasional assistance but cares for most needs |
| 50 | Requires considerable assistance and frequent medical care |
| 40 | Disabled; requires special care and assistance |
| 30 | Severely disabled; hospitalization indicated, death not imminent |
| 20 | Very sick; active supportive treatment needed |
| 10 | Moribund |

---

## APPENDICES

### Appendix A: Most Common Primary Sites of Brain Metastases

| Primary Cancer | Approximate Frequency | Typical MRI Features | Key Molecular Targets |
|---------------|----------------------|---------------------|----------------------|
| Lung (NSCLC) | 40-50% of brain metastases | Multiple; any location; may hemorrhage; often ring-enhancing | EGFR, ALK, ROS1, BRAF V600E, KRAS G12C, MET, RET, NTRK, PD-L1 |
| Lung (SCLC) | 10-15% | Multiple; tend to be small; prophylactic cranial irradiation (PCI) standard in limited-stage SCLC with response | PD-L1; limited targeted options |
| Breast | 15-25% | HER2+ and triple-negative most commonly metastasize to brain; may be hemorrhagic; dural-based possible | HER2 (tucatinib, T-DXd), HR+ (CDK4/6 inhibitors — limited CNS data), PD-L1 (triple-negative) |
| Melanoma | 5-15% | Hemorrhagic (T1-hyperintense on pre-contrast MRI due to melanin and blood); multiple; any location | BRAF V600 (dabrafenib + trametinib), PD-1 + CTLA-4 (ipilimumab + nivolumab) |
| Renal cell carcinoma | 5-10% | Highly vascular; hemorrhagic; large lesions; significant surrounding edema | TKIs (cabozantinib), immunotherapy (ipilimumab + nivolumab) |
| Colorectal | 3-5% | Posterior fossa predilection; typically late in disease | KRAS, BRAF, MSI-H/dMMR (pembrolizumab) |
| Unknown primary | 5-10% | Variable | Comprehensive molecular profiling essential |

### Appendix B: Hemorrhagic Brain Metastases — High-Risk Primaries

Mnemonic: **"MR CT"** — Melanoma, Renal cell carcinoma, Choriocarcinoma, Thyroid

| Primary | Hemorrhage Risk | Management Considerations |
|---------|----------------|--------------------------|
| Melanoma | Very high (40-50% hemorrhagic) | T1 hyperintense from melanin + blood; SRS preferred over surgery when feasible (hemorrhage risk during resection); immunotherapy may be used upfront |
| Renal cell carcinoma | High (30-40% hemorrhagic) | Highly vascular; pre-operative embolization considered; hemorrhage may be presenting symptom |
| Choriocarcinoma | Very high | β-hCG markedly elevated; chemotherapy highly effective; hemorrhage may be initial presentation |
| Thyroid (papillary/follicular) | Moderate | Often indolent; radioactive iodine does NOT treat brain metastases (insufficient BBB penetration); surgery or SRS needed |
| Lung (NSCLC on anticoagulation) | Moderate | Stop anticoagulation if hemorrhagic metastasis; reverse if on warfarin/DOACs |

### Appendix C: CNS-Penetrant Systemic Therapies — Quick Reference

| Cancer Type | Drug | CNS Response Rate | Key Trial |
|-------------|------|-------------------|-----------|
| NSCLC, EGFR+ | Osimertinib 80 mg daily | 91% | FLAURA (Reungwetwattana 2018) |
| NSCLC, ALK+ | Lorlatinib 100 mg daily | 82% | CROWN (Shaw 2020) |
| NSCLC, ALK+ | Alectinib 600 mg BID | 81% | ALEX (Peters 2017) |
| NSCLC, ROS1+ | Lorlatinib 100 mg daily | ~60% | Phase II data |
| Melanoma, BRAF+ | Dabrafenib 150 mg BID + trametinib 2 mg daily | 58% | COMBI-MB (Davies 2017) |
| Melanoma, any | Ipilimumab 3 mg/kg + nivolumab 1 mg/kg | 46-57% | CheckMate 204 (Tawbi 2018) |
| HER2+ breast | Tucatinib + trastuzumab + capecitabine | 47% | HER2CLIMB (Murthy 2020) |
| HER2+ breast | Trastuzumab deruxtecan (T-DXd) | 63.9% | DESTINY-Breast03 (Cortés 2022) |
| Triple-negative breast | Sacituzumab govitecan | Limited CNS data | ASCENT (exploratory) |
| RCC | Cabozantinib 60 mg daily | ~55% (retrospective) | Retrospective series |
| RCC | Ipilimumab + nivolumab | ~28% (brain met subgroup) | CheckMate 214 (subgroup) |

### Appendix D: Treatment Algorithm — Decision Framework

```
BRAIN METASTASES DIAGNOSED
         │
         ├── Acute presentation (symptomatic edema, obtundation, herniation)?
         │         YES → Dexamethasone 10 mg IV → ICU if herniation → Emergent neurosurgery
         │         NO → Dexamethasone only if symptomatic edema present
         │
         ├── Number of metastases?
         │         │
         │         ├── 1 (single)
         │         │     ├── Surgically accessible + mass effect → Surgery → Cavity SRS
         │         │     ├── Not surgical candidate → SRS (single fraction or fractionated)
         │         │     └── With actionable mutation → Consider systemic first (e.g., osimertinib, ipi/nivo)
         │         │
         │         ├── 2-4 (oligometastases)
         │         │     ├── All ≤3-4 cm → SRS (each lesion)
         │         │     ├── 1 large + others small → Surgery for large + SRS for others
         │         │     └── With actionable mutation → Systemic + SRS
         │         │
         │         ├── 5-15
         │         │     ├── Select patients → SRS (JLGK0901 data supports up to 10-15)
         │         │     ├── Good systemic options → Systemic therapy + SRS
         │         │     └── Poor SRS candidate → HA-WBRT + memantine
         │         │
         │         └── >15 or miliary/diffuse
         │               └── HA-WBRT + memantine (if hippocampus-sparing feasible)
         │                   OR standard WBRT + memantine
         │
         ├── Molecular profiling?
         │         ├── EGFR+ NSCLC → Osimertinib (may defer radiation for small, asymptomatic)
         │         ├── ALK+ NSCLC → Lorlatinib or alectinib
         │         ├── BRAF+ melanoma → Dabrafenib + trametinib ± SRS
         │         ├── Melanoma (any) → Ipilimumab + nivolumab ± SRS
         │         ├── HER2+ breast → Tucatinib combo or T-DXd ± SRS
         │         └── No actionable target → Radiation + standard systemic
         │
         └── Surveillance post-treatment
                   └── MRI brain q2-3 months year 1 → q3-4 months year 2 → q6 months ongoing
                       New/progressive lesion → Salvage SRS, surgery, or systemic change
                       Suspected radiation necrosis → Advanced imaging → Bevacizumab if confirmed
```

### Appendix E: Steroid Dosing and Taper Guide

| Clinical Scenario | Initial Dexamethasone Dose | Duration Before Taper | Taper Schedule |
|-------------------|---------------------------|----------------------|----------------|
| Mild symptoms, small edema | 4 mg/day (2 mg BID) | 3-5 days | Reduce by 1 mg every 3-5 days |
| Moderate symptoms | 8-12 mg/day (4 mg q6-8h) | 5-7 days | Reduce by 2 mg every 3-5 days |
| Severe edema / mass effect | 16 mg/day (4 mg q6h) | 7-14 days | Reduce by 2-4 mg every 3-5 days |
| Impending herniation | 10 mg IV bolus → 4-8 mg q6h (up to 24 mg/day) | Until definitive treatment | Taper after surgery/radiation with clinical monitoring |
| Post-SRS | 4-8 mg/day starting day of SRS | 3-7 days | Rapid taper over 5-7 days if no worsening |
| Steroid-dependent (cannot taper) | Minimum effective dose | Ongoing | Consider bevacizumab, re-irradiation, or resection to enable taper |

**Key steroid complications to monitor:** Hyperglycemia (50-60%), insomnia, myopathy (proximal weakness — may mimic disease progression), immunosuppression (PJP risk), GI bleeding, osteoporosis, psychiatric effects (mania, psychosis — usually dose-related), adrenal suppression (if >3 weeks — taper slowly, do not abruptly stop).

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
