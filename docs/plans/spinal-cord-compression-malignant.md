---
title: "Spinal Cord Compression (Malignant)"
description: "Clinical decision support for malignant spinal cord compression (mscc) / metastatic epidural spinal cord compression (mescc) diagnosis and management"
version: "1.0"
setting: "HOSP, OPD, ICU"
---

# Spinal Cord Compression (Malignant)

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Malignant Spinal Cord Compression (MSCC) / Metastatic Epidural Spinal Cord Compression (MESCC)

**ICD-10:** G95.20 (Unspecified cord compression), C79.49 (Secondary malignant neoplasm of other parts of nervous system), C79.51 (Secondary malignant neoplasm of bone), M49.50 (Collapsed vertebra in diseases classified elsewhere), G82.20 (Paraplegia, unspecified)

**SYNONYMS:** Malignant spinal cord compression, MSCC, metastatic epidural spinal cord compression, MESCC, cord compression, spinal metastases, spinal tumor compression, epidural metastases, cancer spine compression, vertebral metastases with cord compression

**SCOPE:** Emergency evaluation and management of malignant (metastatic) spinal cord compression in adults. Covers dexamethasone protocols, emergent imaging, surgical decompression criteria (Patchell criteria), radiation therapy, vertebral body assessment, functional prognostication, and disposition. Excludes non-malignant compressive myelopathy (disc herniation, epidural abscess — separate templates), primary spinal cord tumors (intramedullary), and cauda equina syndrome from malignancy (partially overlaps — see separate template for CES).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; surgical candidacy; chemotherapy effects; infection (epidural abscess differential) | Normal; leukocytosis may suggest infection; thrombocytopenia affects surgical/procedural candidacy |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal function (contrast, medications); electrolytes (hypercalcemia of malignancy); hepatic function (chemotherapy dosing, metastatic disease) | Normal; calcium >10.5 mg/dL → assess for hypercalcemia of malignancy |
| PT/INR, aPTT (CPT 85610, 85730) | STAT | STAT | ROUTINE | STAT | Coagulopathy assessment; surgical candidacy; anticoagulation reversal if emergent surgery needed | Normal; INR <1.5 for surgery |
| ESR / CRP (CPT 85652, 86140) | STAT | STAT | ROUTINE | STAT | Epidural abscess differential (highly elevated ESR >30-50 typically); inflammatory markers for malignancy | Normal-mildly elevated in malignancy; markedly elevated ESR/CRP → strongly consider abscess |
| Blood cultures (x2 sets) (CPT 87040) | STAT | STAT | - | STAT | Epidural abscess differential; bacteremia if febrile | Negative; positive → epidural abscess more likely than tumor |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Baseline before high-dose dexamethasone; steroid hyperglycemia | <180 mg/dL; anticipate significant hyperglycemia with high-dose steroids |
| Type and screen (CPT 86900) | STAT | STAT | - | STAT | Surgical candidacy; blood product availability | On file |
| Calcium (ionized or corrected) (CPT 82310) | STAT | STAT | ROUTINE | STAT | Hypercalcemia of malignancy (present in 10-30% of cancer patients); can cause confusion, weakness mimicking cord compression progression | Corrected Ca <10.5 mg/dL; if elevated → IV fluids, calcitonin, bisphosphonate |
| LDH | STAT | ROUTINE | ROUTINE | STAT | Tumor burden marker; lymphoma (very high LDH); prognostic | Normal; very high → lymphoma, aggressive malignancy |
| Urinalysis (CPT 81003) | STAT | STAT | - | STAT | Urinary retention (neurogenic bladder from cord compression); UTI (fever differential); baseline renal function | Normal; retention with high post-void residual expected in cord compression |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Tumor markers (PSA, CEA, CA 19-9, CA 125, CA 15-3, AFP, β-hCG) | - | ROUTINE | ROUTINE | - | Unknown primary cancer; PSA (prostate — most common spinal metastasis), CEA (GI, lung), CA 15-3 (breast), etc. | Elevations guide primary site identification |
| SPEP / UPEP with immunofixation (CPT 86334) | - | ROUTINE | ROUTINE | - | Multiple myeloma (common cause of vertebral compression/cord compression); M-protein, light chains | No monoclonal protein; if present → myeloma workup |
| Free light chains (kappa/lambda ratio) | - | ROUTINE | ROUTINE | - | Myeloma; light chain disease | Normal ratio (0.26-1.65); abnormal suggests myeloma |
| Serum protein electrophoresis (CPT 86334) | - | ROUTINE | ROUTINE | - | Myeloma; lymphoma | No M-spike |
| Alkaline phosphatase (bone-specific) | - | ROUTINE | ROUTINE | - | Osteoblastic metastases (prostate, breast); Paget's disease differential | Normal; elevated suggests bone turnover |
| Phosphate (CPT 84100) | - | ROUTINE | ROUTINE | - | Hypercalcemia workup; oncologic emergency assessment | Normal |
| Uric acid | - | ROUTINE | - | ROUTINE | Tumor lysis syndrome risk (lymphoma, rapidly proliferating tumors); pre-treatment assessment | Normal |
| Procalcitonin (CPT 84145) | STAT | STAT | - | STAT | If infection/abscess differential is high; more specific than CRP for bacterial infection | <0.25 ng/mL (low probability bacterial); >0.5 → consider abscess/infection |
| TSH, free T4 (CPT 84443, 84439) | - | ROUTINE | ROUTINE | - | Thyroid cancer metastases (follicular thyroid cancer has bony tropism) | Normal |
| Vitamin D (25-OH) (CPT 82306) | - | ROUTINE | ROUTINE | - | Bone health; pathologic fracture risk; supplement if deficient | >30 ng/mL |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Flow cytometry (peripheral blood) | - | EXT | EXT | - | Lymphoma/leukemia presenting as epidural mass | Abnormal lymphocyte population = lymphoproliferative disorder |
| Bone marrow biopsy | - | EXT | EXT | - | Myeloma; lymphoma; unknown primary with bone marrow involvement | Normal; abnormal → specific diagnosis |
| Paraneoplastic antibody panel | - | EXT | EXT | - | If myelopathy features atypical for compression (e.g., subacute progressive without clear structural compression) | Negative; positive changes diagnosis from compression to paraneoplastic myelopathy |
| AQP4-IgG (NMO antibody) | - | EXT | EXT | - | If imaging shows longitudinal intramedullary lesion rather than epidural compression → NMOSD differential | Negative; positive → NMOSD not metastatic compression |
| CT-guided biopsy of vertebral lesion | - | URGENT | ROUTINE | - | Unknown primary; tissue diagnosis needed before treatment; lymphoma requires tissue for definitive diagnosis (sensitive to steroids — obtain tissue BEFORE steroids if possible in suspected lymphoma) | Histopathologic diagnosis |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI entire spine with and without contrast (gadolinium) (CPT 72156+72157+72158) | STAT | STAT | URGENT | STAT | **Within 4 hours of presentation (24h max)**; GOLD STANDARD; must image ENTIRE spine (multifocal metastases in 30-40%) | Epidural mass with cord compression; level(s) of compression; Bilsky grade (0-3); vertebral body involvement; number of levels; intramedullary vs. extramedullary-intradural vs. epidural; cord signal change (T2 hyperintensity = edema/myelopathy — poor prognostic sign); paraspinal soft tissue extension | MRI-incompatible implants; severe claustrophobia (sedate); GFR <30 (gadolinium risk — benefit outweighs risk in emergency) |
| Plain radiographs (spine, targeted) | STAT | STAT | - | STAT | Immediate while awaiting MRI; identifies vertebral collapse, pathologic fracture, alignment; 70% sensitivity for vertebral metastases (30% miss rate) | Vertebral body collapse; pedicle erosion ("winking owl sign" on AP); pathologic fracture; kyphosis; alignment | Pregnancy (shield) |
| CT chest/abdomen/pelvis with contrast (CPT 71260, 74178) | URGENT | URGENT | ROUTINE | - | Within 24-48h; staging; primary identification; lung is most common primary | Primary tumor; staging of metastatic disease; lymphadenopathy; visceral metastases | Contrast allergy; renal impairment |
| CT spine (targeted level) without contrast | STAT | STAT | - | STAT | If MRI contraindicated or unavailable; pre-operative planning for bone assessment; vertebral body stability (SINS score); CT myelogram if MRI not possible | Bone destruction pattern (lytic vs. blastic vs. mixed); posterior element involvement; fracture; canal compromise; vertebral body collapse >50% | Pregnancy (risk vs. benefit) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT myelogram (CPT 72132) | STAT | STAT | - | STAT | If MRI contraindicated (pacemaker, implant); intrathecal contrast via LP → CT; demonstrates level of block | Complete or partial subarachnoid block; level of compression; multiple levels of disease | LP contraindicated if complete block above puncture site (risk of neurologic deterioration); coagulopathy |
| PET/CT (FDG) (CPT 78816) | - | ROUTINE | ROUTINE | - | Staging; primary identification; assessing treatment response; distinguishing active tumor from treated/necrotic bone | Active metastatic disease; primary tumor identification | Uncontrolled diabetes; pregnancy |
| Bone scan (Tc-99m) (CPT 78300) | - | ROUTINE | ROUTINE | - | Skeletal staging; identifies additional osseous metastases; blastic > lytic sensitivity; useful for prostate, breast | Additional bone metastases; may miss purely lytic lesions (renal, thyroid, myeloma) | Pregnancy |
| MRI brain with contrast (CPT 70552) | - | URGENT | ROUTINE | - | If lung primary or melanoma (high brain metastasis risk); symptoms suggesting intracranial disease | Brain metastases (concurrent in 10-30% of patients with MSCC) | Same as MRI |
| CT-guided biopsy (vertebral/paraspinal) | - | URGENT | ROUTINE | - | Tissue diagnosis if unknown primary; CRITICAL for suspected lymphoma (radiosensitive — may not need surgery); obtain BEFORE steroids if lymphoma suspected (steroids can render biopsy non-diagnostic) | Histopathologic diagnosis; molecular profiling | Coagulopathy; inaccessible lesion |
| DEXA scan | - | - | ROUTINE | - | Baseline bone density if prolonged steroids anticipated; osteoporosis risk | T-score; fracture risk assessment | None significant |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Spinal angiography | - | EXT | EXT | - | If highly vascular tumor suspected (RCC, thyroid) — pre-operative embolization to reduce surgical bleeding | Tumor vascularity; feeding vessels; embolization candidacy | Contrast allergy; renal impairment; coagulopathy |
| Pre-operative embolization | - | URGENT | - | - | Highly vascular metastases (RCC, thyroid); 24-48h before surgery to reduce intraoperative blood loss | Reduction of tumor blood supply | Contrast allergy; tumor supplying anterior spinal artery (risk of cord infarction) |
| Dynamic flexion-extension radiographs | - | - | ROUTINE | - | Post-treatment stability assessment; if clinical instability suspected | Mechanical instability (translation, angulation) | Acute cord compression (do NOT flex/extend if acute neurologic deficit) |
| Nuclear medicine thyroid scan | - | - | EXT | - | If thyroid primary suspected (follicular thyroid cancer has high bone tropism) | Thyroid nodule; functional assessment | Recent iodinated contrast (wait 4-6 weeks) |

### Lumbar Puncture

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP — Generally NOT indicated | - | - | - | - | LP is NOT routinely indicated in MSCC; CSF cytology only if leptomeningeal disease suspected AND no complete block; CT myelogram if MRI not available (different indication) | N/A — LP is diagnostic adjunct only in specific situations | CONTRAINDICATED with complete spinal block above LP level (risk of neurologic deterioration/coning); coagulopathy; local infection |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Dexamethasone (high-dose for MSCC)** (CPT 96374) | IV | - | 10 mg :: IV :: q6h :: **Standard loading dose:** 10 mg IV bolus STAT; **Then:** 4 mg IV/PO q6h (16 mg/day); **High-dose (severe deficits or rapidly progressive):** 96 mg IV bolus (controversial — see evidence) → 24 mg q6h x 3 days → rapid taper; **Moderate deficits / ambulatory:** 10 mg IV → 4 mg q6h; **Begin taper after definitive treatment initiated;** GI prophylaxis: PPI while on steroids; Monitor glucose q6h | - | Sorensen et al. (1994): Dexamethasone + radiation vs. radiation alone → 81% vs. 63% ambulatory at treatment end; High-dose (96 mg) vs. standard (10 mg): Vecht et al. (1989) — higher response rate at 1 week but more side effects; MOST centers now use moderate dose (10 mg load → 16 mg/day); Begin within 6h of diagnosis | STAT | STAT | URGENT | STAT |
| **Spinal precautions / immobilization** | - | - | Strict log-roll precautions; flat bed transport; cervical collar if cervical spine involved; thoracolumbar brace (TLSO) if thoracolumbar; avoid flexion/extension; transfer on spine board if unstable fracture suspected | - | Unstable pathologic fracture may worsen cord compression with movement; SINS score guides instability assessment | STAT | STAT | - | STAT |
| **Bladder management** | - | - | 200 mL :: - :: - :: Assess for urinary retention (cord compression causes neurogenic bladder); straight catheterize if retention → place Foley if residual >200 mL or ongoing retention; monitor I&O strictly | - | Urinary retention is a common presenting feature and may be the first sign of cord compression; bladder function correlates with motor recovery prognosis | STAT | STAT | - | STAT |
| **DVT prophylaxis** | SC | - | 40 mg :: SC :: daily :: SCDs immediately; pharmacologic prophylaxis (enoxaparin 40 mg SQ daily) within 24-48h unless surgery imminent; spinal cord compression patients have VERY HIGH VTE risk (up to 25-50% without prophylaxis) | - | Cancer + immobility + spinal cord injury = extremely high VTE risk; mechanical prophylaxis alone insufficient | STAT | STAT | - | STAT |
| **Pain management** | IV | - | 650-1000 mg :: IV :: q6h :: Back pain often severe; acetaminophen 650-1000 mg q6h scheduled + opioids PRN (morphine 2-4 mg IV q3h PRN or oxycodone 5-10 mg PO q4h PRN); NSAIDs cautiously (renal function, bleeding risk); dexamethasone itself reduces pain from edema/inflammation; neuropathic pain: gabapentin 300 mg TID (titrate) or pregabalin 75 mg BID | - | Pain is the presenting symptom in 83-95% of patients; median 7 weeks before diagnosis; adequate analgesia essential for function and quality of life | STAT | STAT | ROUTINE | STAT |
| **Bowel regimen** | - | - | 100 mg :: - :: BID :: Neurogenic bowel from cord compression + opioid constipation; docusate 100 mg BID + senna 2 tabs HS; bisacodyl suppository PRN; monitor for ileus | - | Bowel dysfunction common; proactive management prevents complications | STAT | STAT | ROUTINE | STAT |
| **Glucose monitoring** | - | - | Fingerstick q6h on high-dose dexamethasone; insulin sliding scale → basal-bolus if persistent >180; anticipate glucose will rise significantly within hours of steroid initiation | - | High-dose dexamethasone causes severe hyperglycemia in majority of patients | STAT | STAT | ROUTINE | STAT |

### 3B. Definitive/Targeted Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Surgical decompression + stabilization** | - | - | **Indications (Patchell criteria + expanded):** (1) Single site of compression, (2) Paraplegia ≤48h, (3) Not radiosensitive tumor (not lymphoma, myeloma, SCLC, germ cell), (4) Life expectancy >3 months, (5) ECOG ≤2 / able to tolerate surgery, (6) Mechanical instability (SINS ≥7), (7) Neurologic deterioration during radiation; **Approach:** Posterior decompressive laminectomy ± instrumented stabilization; anterior corpectomy with cage/cement for anterior compression with instability; **Timing:** Within 24h of presentation (ideally <12h); Followed by radiation within 2-4 weeks post-op | - | **Patchell et al. (2005) — LANDMARK:** Surgery + radiation vs. radiation alone: ambulatory rate 84% vs. 57% (p=0.001); maintained ambulation longer (122 vs. 13 days); more patients regained ambulation (62% vs. 19%); surgery retained continence longer; survival trend (126 vs. 100 days) | - | STAT | - | - |
| **External beam radiation therapy (EBRT)** | - | - | **Primary modality if:** Radiosensitive tumor (lymphoma, myeloma, SCLC, seminoma), surgical contraindication, multiple noncontiguous levels, life expectancy <3 months, poor surgical candidate; **Standard:** 30 Gy in 10 fractions (2 weeks) or 20 Gy in 5 fractions (1 week); **Short course (poor prognosis):** 8 Gy single fraction; **Begin within 24h of diagnosis**; Can start same day as dexamethasone; Radiation field covers 1-2 vertebral bodies above and below involved segment | - | Rades et al. (2008): No significant difference between 30 Gy/10 vs. 20 Gy/5 for motor function recovery or local control; 8 Gy single fraction appropriate for poor prognosis (life expectancy <6 months) | - | STAT | ROUTINE | - |
| **Stereotactic body radiation therapy (SBRT) / Spine SRS** | - | - | **Indications:** Previously irradiated segment (re-irradiation); radioresistant histology (RCC, melanoma, sarcoma); oligometastatic disease; post-operative; **Dose:** 16-24 Gy single fraction or 24-30 Gy in 3 fractions; **Requires:** Spinal cord dose constraints (max cord dose 10-14 Gy single fraction); MRI-based planning; **Timing:** As soon as technically feasible | - | RTOG 0631 and multiple institutional series: High local control (85-95%) for radioresistant histologies; superior to conventional EBRT for RCC, melanoma; separation surgery + SBRT emerging as preferred approach for radioresistant tumors | - | URGENT | ROUTINE | - |
| **Separation surgery + SBRT** | - | - | **Indication:** Epidural tumor compressing cord from radioresistant primary (RCC, melanoma, sarcoma); goal is NOT gross total resection — goal is to decompress cord and create ≥2mm separation between tumor and cord to enable safe SBRT delivery; Followed by SBRT within 2-4 weeks | - | Laufer et al. (2013): Separation surgery + SBRT: 90% local control at 1 year for radioresistant tumors; allows definitive radiation dose to tumor while respecting cord tolerance | - | URGENT | - | - |
| **Vertebroplasty / Kyphoplasty** | - | - | **Indications:** Painful pathologic compression fracture; vertebral body instability; post-radiation pain; NO epidural extension compressing cord (cement leak risk into canal); **SINS 7-12 (indeterminate stability):** Consider as adjunct; **Procedure:** Percutaneous PMMA cement injection into vertebral body | - | Pain relief in 70-90% within 24-48h; structural support; does NOT address epidural disease; risk of cement leak into epidural space (1-5%) | - | URGENT | ROUTINE | - |
| **Systemic chemotherapy** | - | - | **Radiosensitive tumors as primary/adjunct therapy:** Lymphoma (R-CHOP or equivalent); myeloma (bortezomib-based); SCLC (cisplatin/etoposide); germ cell (BEP); **Other primaries:** Per disease-specific guidelines after stabilization; coordinate with medical oncology | - | Chemosensitive tumors (lymphoma, myeloma, germ cell, SCLC) may respond rapidly to systemic therapy; may be used as primary treatment with radiation or as consolidation post-radiation | - | ROUTINE | ROUTINE | - |
| **Hormonal therapy (if applicable)** | - | - | Prostate cancer: ADT (LHRH agonist/antagonist) + enzalutamide/abiraterone/darolutamide; Breast cancer: anti-estrogen/AI per receptor status; Thyroid: levothyroxine suppression + RAI (spine metastases do NOT concentrate RAI well — external radiation preferred) | - | Prostate and breast cancer spinal metastases may respond to hormonal manipulation; adjunct to radiation | - | ROUTINE | ROUTINE | - |

### 3C. Adjunctive Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Steroid taper** | - | - | 2-4 mg :: - :: once :: Begin taper once definitive treatment (surgery/radiation) initiated and neurologic status stable/improving; **Taper schedule:** Reduce by 2-4 mg every 3-5 days; typical: 16→12→8→6→4→2→off over 2-3 weeks; slower taper if symptoms recur; monitor for adrenal insufficiency if >2-3 weeks of steroids | - | Prolonged high-dose steroids cause significant morbidity; steroid myopathy (proximal weakness — may mimic neurologic progression); PJP risk; hyperglycemia; GI bleed | - | ROUTINE | ROUTINE | - |
| **PPI (stress ulcer/GI prophylaxis)** | PO | - | 20 mg :: PO :: daily :: Omeprazole 20 mg daily or pantoprazole 40 mg daily while on dexamethasone | - | Steroid + critical illness increases GI bleed risk | STAT | STAT | ROUTINE | STAT |
| **Calcium + Vitamin D** | PO | - | 1000-1200 mg :: PO :: daily :: Calcium 1000-1200 mg + Vitamin D 800-1000 IU daily during steroid course and beyond (bone health in cancer patients) | - | Steroid-induced osteoporosis prevention; already compromised bone integrity | - | ROUTINE | ROUTINE | - |
| **Bone-modifying agents** | IV | - | 4 mg :: IV :: - :: Zoledronic acid 4 mg IV q4 weeks OR denosumab 120 mg SQ q4 weeks; reduces skeletal-related events (SRE); dental clearance before starting (ONJ risk); renal adjustment for zoledronic acid (hold if GFR <35) | - | Zoledronic acid: Rosen et al. (2003) — reduced SRE by 48% in bone metastases; denosumab: Fizazi et al. (2011) — superior to zoledronic acid for SRE reduction in bone metastases (prostate trial) | - | ROUTINE | ROUTINE | - |
| **Neuropathic pain management** | - | - | 300 mg :: - :: TID :: Gabapentin 300 mg TID → titrate to 600-900 mg TID; OR pregabalin 75 mg BID → titrate to 150-300 mg BID; duloxetine 30-60 mg daily as alternative; amitriptyline 10-25 mg HS (anticholinergic caution with urinary retention) | - | Radicular and central neuropathic pain common in cord compression; adjuvant analgesics reduce opioid requirements | - | STAT | ROUTINE | STAT |
| **Rehabilitation (inpatient)** | - | - | PT/OT evaluation within 24h of admission; early mobilization when cleared by spine surgery; adaptive equipment; wheelchair assessment if paraparetic/paraplegic; ROM exercises; strengthening; transfer training | - | Early rehabilitation improves functional outcomes; cancer rehabilitation is evidence-based; patients with MSCC benefit from structured rehab programs | - | URGENT | ROUTINE | - |
| **Skin care / pressure ulcer prevention** | - | - | Turn q2h; pressure-reducing mattress; heel protectors; skin assessment with Braden scale; nutrition optimization | - | Immobile patients with cord compression at very high risk for pressure injuries; prevention is critical | - | STAT | - | STAT |

### 3D. Medications to AVOID or Use with Caution

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| NSAIDs (prolonged use) | - | - | - | - | - | - | - | - | - | - |
| Methotrexate (high-dose, with spinal radiation) | - | - | - | - | - | - | - | - | - | - |
| Intrathecal chemotherapy (with spinal block) | IT | - | - | - | - | - | - | - | - | - |
| Anticoagulation (full-dose, peri-operative) | - | - | - | - | - | - | - | - | - | - |
| Steroids in suspected lymphoma (BEFORE biopsy) | - | - | - | - | - | - | - | - | - | - |
| Bevacizumab (peri-operative) | - | - | - | - | - | - | - | - | - | - |
| Bisphosphonates (if GFR <35 for zoledronic acid) | - | - | - | - | - | - | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Neurosurgery / Spine surgery consultation — EMERGENT | STAT | STAT | - | STAT | Surgical candidacy assessment; Patchell criteria evaluation; SINS score; stabilization; ALL patients with MSCC need spine surgery consultation even if radiation is primary treatment (assess stability) |
| Radiation oncology consultation — EMERGENT | STAT | STAT | ROUTINE | STAT | Within hours of diagnosis; concurrent with neurosurgery evaluation; EBRT planning; SBRT candidacy; begin radiation within 24h if non-surgical |
| Medical oncology consultation | - | URGENT | ROUTINE | - | Systemic therapy options; primary identification; staging; prognosis; clinical trial eligibility; coordinate bone-modifying agents |
| Multidisciplinary spine tumor board | - | URGENT | ROUTINE | - | Neurosurgery, radiation oncology, medical oncology, interventional radiology, pathology; optimal treatment sequencing; NOMS framework application |
| Goals of care discussion | - | URGENT | ROUTINE | URGENT | Prognosis (Tokuhashi score, Tomita score); functional goals; code status; palliative vs. aggressive treatment; quality of life; patient values and preferences |
| Physical medicine & rehabilitation | - | URGENT | ROUTINE | - | PT/OT; functional assessment; rehabilitation candidacy; inpatient rehab planning if motor deficits present; assistive devices |
| Foley catheter management | STAT | STAT | - | STAT | If urinary retention: Foley placement with monitoring; intermittent catheterization if partial function; urology consult if prolonged retention anticipated |
| Social work / case management | - | ROUTINE | ROUTINE | - | Equipment needs (wheelchair, hospital bed); caregiver training; home safety assessment; insurance authorization; hospice if appropriate |
| Pain management / palliative care | - | STAT | ROUTINE | STAT | If pain refractory to standard analgesics; assist with goals of care; symptom management; advance care planning |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Interventional radiology consultation | - | URGENT | ROUTINE | - | Pre-operative embolization (RCC, thyroid metastases); vertebroplasty/kyphoplasty; CT-guided biopsy for tissue diagnosis |
| Orthotics / bracing | - | ROUTINE | ROUTINE | - | Custom TLSO (thoracolumbar) or cervical collar based on level; post-operative stabilization; external support for non-surgical patients |
| Wound care (post-operative) | - | ROUTINE | ROUTINE | - | Irradiated tissue heals poorly; monitor surgical wound closely; avoid radiation to fresh surgical wound for 2-3 weeks (coordinate timing) |
| Nutrition / dietitian | - | ROUTINE | ROUTINE | - | Cancer cachexia assessment; steroid-induced appetite changes; adequate protein for wound healing (if surgical); calcium/vitamin D optimization |
| Psychology / psychiatry | - | ROUTINE | ROUTINE | - | Depression, anxiety, adjustment disorder common with acute paralysis/paresis and cancer diagnosis; screening with PHQ-9; support for functional loss |
| Urology consultation | - | ROUTINE | ROUTINE | - | If persistent neurogenic bladder; intermittent catheterization training; long-term bladder management plan |
| Home health referral | - | ROUTINE | ROUTINE | - | Nursing visits; PT/OT in home; wound care; medication management; caregiver education |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Re-irradiation (spine) | - | ROUTINE | ROUTINE | - | Recurrent MSCC at previously irradiated site; SBRT preferred for re-irradiation (better dose targeting, cord sparing); cumulative cord dose must be calculated; re-irradiation feasible if >6 months since prior radiation |
| Repeat surgery | - | URGENT | ROUTINE | - | Hardware failure; recurrent compression at operated level; progressive neurologic decline despite radiation; infection at surgical site |
| Intrathecal drug delivery | - | - | EXT | - | Refractory pain; intrathecal morphine or ziconotide pump; palliative care indication |
| Cement augmentation (post-radiation) | - | ROUTINE | ROUTINE | - | Persistent pain or progressive collapse after radiation; vertebroplasty/kyphoplasty as pain control adjunct |
| Hospice referral | - | ROUTINE | ROUTINE | - | Exhausted treatment options; life expectancy <6 months; patient preference for comfort-focused care; poor functional status (ECOG 3-4) |
| Clinical trial enrollment | - | ROUTINE | ROUTINE | - | Novel radiosensitizers; immunotherapy combinations; spine-specific SBRT protocols |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Primary Differential Diagnoses

| Diagnosis | Key Differentiating Features | Distinguishing Studies |
|-----------|------------------------------|----------------------|
| Spinal epidural abscess | Fever (present in 50-66%); IV drug use, recent procedure, immunosuppression; rapidly progressive; ESR >20 (sensitivity 94%); CRP markedly elevated; ring-enhancing epidural collection on MRI; restricted diffusion in abscess; spine pain with percussion tenderness; leukocytosis | MRI: T2-hyperintense epidural collection with rim enhancement; restricted diffusion (DWI bright, ADC dark) within abscess; blood cultures (positive in 60%); ESR/CRP markedly elevated; procalcitonin >0.5 |
| Degenerative spinal stenosis (cervical/lumbar) | Chronic progressive symptoms; myelopathic signs insidious onset; no cancer history; disc/osteophyte complex on imaging; NO destructive bone lesion; congenital canal narrowing | MRI: disc-osteophyte complex; ligamentum flavum hypertrophy; NO bone destruction; NO contrast enhancement of epidural mass; chronic degenerative changes |
| Primary spinal cord tumor (intramedullary) | Intramedullary (within cord parenchyma); ependymoma, astrocytoma; cord expansion with central lesion; no vertebral body destruction; slow progression; syrinx may be present | MRI: cord expansion with intramedullary enhancing lesion; no epidural mass; no vertebral body involvement; ependymoma: central location, hemosiderin cap; astrocytoma: eccentric, irregular |
| Vertebral compression fracture (osteoporotic) | No cancer history; older patient with osteoporosis; acute back pain after minor trauma/lifting; no neurologic deficits (usually); vertebral body collapsed but NO epidural mass; NO posterior element involvement | MRI: vertebral body edema (T1 low, STIR high) WITHOUT epidural mass or posterior element involvement; CT: no bone destruction beyond fracture; DEXA: osteoporosis; if ambiguous → biopsy |
| Multiple myeloma | Older adult; bone pain; anemia, renal insufficiency, hypercalcemia ("CRAB"); diffuse lytic lesions; monoclonal protein on SPEP; punched-out skull lesions; responsive to chemotherapy AND radiation | SPEP: M-protein; UPEP: Bence Jones protein; free light chains: abnormal ratio; bone marrow biopsy: >10% plasma cells; CT/MRI: multiple lytic lesions; biopsy: plasmacytoma; KEY: myeloma is RADIOSENSITIVE — radiation first-line |
| Lymphoma (epidural) | May present as isolated epidural mass; radiosensitive; responds dramatically to steroids (may "melt" before biopsy); younger patients; constitutional symptoms (B symptoms); elevated LDH | MRI: epidural mass; homogeneous enhancement; may be paraspinal; CT: lymphadenopathy; LDH elevated; flow cytometry; KEY: obtain biopsy BEFORE steroids if possible; radiation is primary treatment |
| Transverse myelitis / NMOSD | Intramedullary T2 lesion on MRI (NOT epidural mass); autoimmune history; AQP4/MOG antibodies; longitudinally extensive (≥3 segments in NMOSD); responds to IV steroids/PLEX; no bone lesion | MRI: intramedullary T2 hyperintensity, NOT epidural mass; AQP4-IgG or MOG-IgG positive; CSF: pleocytosis; no vertebral body destruction |
| Spinal epidural hematoma | Acute onset, often on anticoagulation; post-procedural (LP, epidural injection); acute neurogenic deficit; hyperacute T1 signal on MRI (blood) | MRI: epidural collection with blood signal characteristics (T1 hyperintense in subacute phase); history of anticoagulation or procedure; coagulation studies abnormal; neurosurgical emergency |

### Red Flags Requiring Urgent Reassessment

| Red Flag | Concern | Action |
|----------|---------|--------|
| Progressive motor weakness despite treatment | Increasing cord compression; treatment failure; hematoma; instability | STAT MRI; neurosurgery re-evaluation; consider surgical salvage; dose-escalate steroids |
| New/complete loss of bowel or bladder function | Progressing to complete cord injury; cauda equina involvement | STAT MRI; emergent surgical evaluation if within 48h window; Foley placement |
| Ascending sensory level | Rostral progression of compression; edema expansion; additional metastatic levels | STAT MRI entire spine; escalate dexamethasone; emergent neurosurgery |
| Saddle anesthesia (new) | Conus medullaris or cauda equina involvement | STAT MRI; emergent surgical evaluation |
| Fever after steroid initiation | Masked infection (steroids suppress fever); abscess; post-operative infection; UTI | Blood cultures; UA; CRP; imaging; broaden antibiotics; consider pausing immunosuppressive therapy |
| Acute hypotension + bradycardia | Neurogenic shock (spinal cord injury with loss of sympathetic tone) | IV fluids; vasopressors (norepinephrine or phenylephrine preferred); atropine for symptomatic bradycardia; ICU transfer |
| Bilateral leg DVT / PE symptoms | High VTE risk in MSCC; pulmonary embolism can be fatal | STAT CT angiography (PE); bilateral lower extremity duplex US (DVT); therapeutic anticoagulation (weigh against surgical planning) |
| Respiratory compromise | High cervical cord compression affecting diaphragm (C3-5); pulmonary embolism; pneumonia in immobilized patient | Bedside spirometry; ABG; CT angiography; intubation if needed; phrenic nerve pacing consideration |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (First 72h)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic examination (motor strength, sensory level, rectal tone, reflexes) | q4h x 48h → q6h | Stable or improving motor function; stable sensory level; preserved rectal tone | If declining: STAT MRI; escalate dexamethasone to 24 mg/day; emergent neurosurgery |
| Blood glucose | q6h (q4h if on insulin drip) | 140-180 mg/dL | Sliding scale → basal-bolus insulin; endocrine consult if refractory |
| Pain score (NRS) | q4h | NRS <4/10 | Escalate analgesics; add neuropathic agents; palliative care consultation |
| Blood pressure | q4h (continuous if neurogenic shock) | SBP >90 (avoid hypotension — cord perfusion); MAP >65-70 | IV fluids; vasopressors if neurogenic shock; avoid excessive hypertension (post-operative bleeding risk) |
| Bladder function (I&O, post-void residual) | q shift; post-void residual daily | Volitional voiding; PVR <200 mL | Foley if retention; intermittent catheterization if PVR 200-500 |
| Bowel function | Daily | Bowel movement within 48-72h | Aggressive bowel regimen; rectal exam; abdominal X-ray if distended |
| Skin integrity (Braden scale) | q shift | No pressure injuries; Braden ≥18 | Turn q2h; specialty mattress; heel protectors; wound care if injury develops |
| Temperature | q4h | Afebrile | If febrile: blood cultures, UA, chest imaging; consider abscess vs. tumor fever |
| Respiratory function (if cervical/high thoracic) | q4h; bedside spirometry daily | FVC >15 mL/kg; stable respiratory rate | If FVC declining: ICU transfer; prepare for intubation; consider phrenic nerve involvement |

### Subacute/Outpatient Monitoring

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| MRI spine (affected region) with contrast | 6-8 weeks post-treatment, then q3 months x 1 year, then q6 months | Tumor regression or stability; improved cord compression; resolution of edema | Progression: multidisciplinary re-evaluation; re-irradiation, surgery, systemic therapy change |
| Neurologic examination | Each clinic visit (q2-4 weeks initially, then q1-3 months) | Stable or improving motor function; improving or stable pain | New deficits: urgent MRI; consider disease progression, hardware failure, radiation myelopathy |
| Steroid taper progress | Each visit | Off steroids or minimum effective dose | Steroid-dependent: attempt taper after each treatment milestone |
| Bone-modifying agent monitoring | Monthly during treatment; dental exam q6 months | No skeletal-related events; stable calcium; no ONJ symptoms | Hold zoledronic acid if GFR <35; dental referral if jaw pain/exposed bone |
| Functional status (ECOG / KPS) | Each visit | Stable or improving | Declining function: reassess treatment goals; rehabilitation intensification; palliative care |
| Calcium, renal function | Monthly during bisphosphonate therapy | Ca >8.5; GFR >35 (for zoledronic acid) | Supplement calcium; switch to denosumab if renal decline |
| Spinal stability assessment | Each visit; dynamic imaging if clinical concern | Stable alignment; no hardware migration | Orthotics adjustment; re-fixation surgery if hardware failure |
| Depression/adjustment screening | Each visit | PHQ-9 <5 | Psychology referral; SSRI; support groups |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| ICU admission | Neurogenic shock (hypotension + bradycardia from spinal cord injury); respiratory compromise from high cervical lesion; post-operative monitoring (first 24h after major spine surgery); acute paraplegia/quadriplegia requiring close monitoring; hemodynamic instability |
| General neurology/neurosurgery/oncology floor | New MSCC diagnosis requiring workup and treatment planning; surgical candidate awaiting decompression; radiation therapy initiation; motor deficits requiring monitoring and rehabilitation; pain management; high-dose steroid initiation |
| Observation | Known metastatic disease with new pain but preserved neurologic function; MRI showing compression without cord signal change; stable neurologic exam |

### Discharge Criteria

| Criterion | Details |
|-----------|---------|
| Neurologic stability | Stable or improving neurologic exam for ≥24-48h; clear trend of improvement or plateau |
| Definitive treatment initiated | Surgery completed and recovering; radiation started or completed; systemic therapy plan in place |
| Pain controlled | Adequate pain control on oral medications; able to participate in PT/OT |
| Steroid regimen established | Oral dexamethasone with documented taper schedule; glucose management plan; PPI prescribed |
| Bladder function assessed | Voiding spontaneously OR clean intermittent catheterization teaching completed OR Foley with urology follow-up |
| Bowel regimen | Having regular bowel movements on established regimen |
| Mobility assessment | PT/OT clearance; safe with appropriate assistive device; OR inpatient rehab transfer planned |
| VTE plan | Pharmacologic DVT prophylaxis transition plan (enoxaparin at home or DOACs if indicated) |
| Spine stability | Bracing/orthotic fitted if indicated; activity restrictions clearly documented |
| Follow-up arranged | Neurosurgery (1-2 weeks), radiation oncology (as per treatment schedule), medical oncology (1-2 weeks), PM&R (outpatient rehab), PCP (steroid monitoring); MRI spine at 6-8 weeks |
| Patient/family education | Spinal precautions; steroid side effects; when to return to ED (new weakness, loss of bladder/bowel, severe pain, fever); caregiver training for mobility |
| Equipment ordered | Wheelchair, walker, hospital bed, shower chair, commode — as appropriate per functional assessment |

### Discharge Prescriptions Checklist

| Medication | Details |
|-----------|---------|
| Dexamethasone | Taper schedule clearly documented (e.g., 4 mg q6h → taper per schedule over 2-3 weeks) |
| PPI | While on steroids |
| Analgesics | Opioids with taper plan; gabapentin/pregabalin for neuropathic pain |
| Bowel regimen | Docusate + senna; PRN bisacodyl |
| DVT prophylaxis | Enoxaparin 40 mg SQ daily (if continued DVT prophylaxis indicated); duration per oncology recommendation |
| Bone-modifying agent | Zoledronic acid or denosumab (outpatient schedule) |
| Calcium + Vitamin D | If on steroids or bisphosphonates |
| Insulin (if needed) | For steroid-induced hyperglycemia with glucometer/supplies |
| Antiemetics PRN | If on chemotherapy or persistent nausea |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| MSCC Management | NICE Clinical Guideline CG75 (updated) | 2008/2023 | MRI within 24h (urgent within 4h if progressive deficit); dexamethasone 16 mg/day; surgical decompression within 24h if indicated; definitive treatment within 24h; multidisciplinary team approach |
| Spinal Metastases | NCCN Clinical Practice Guidelines | 2025 | NOMS framework (Neurologic, Oncologic, Mechanical instability, Systemic disease) for treatment decision-making; multidisciplinary approach; SINS scoring |
| Bone-Modifying Agents | ASCO Clinical Practice Guideline | 2017 | Zoledronic acid or denosumab recommended for all patients with bone metastases from solid tumors; start within 3 months of bone metastasis diagnosis |
| MSCC Radiation | Cochrane Systematic Review (George et al.) | 2015 | No significant difference between short-course (1-2 fractions) and longer-course (5-10 fractions) for motor outcomes in poor prognosis patients |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [Patchell et al. (2005) — Lancet](https://pubmed.ncbi.nlm.nih.gov/16112300/) | Direct decompressive surgery + radiation vs. radiation alone for MSCC: ambulatory 84% vs. 57% (p=0.001); regained ambulation 62% vs. 19%; maintained ambulation 122 vs. 13 days; maintained continence longer | LANDMARK study establishing surgery + radiation as superior to radiation alone for single-level MSCC in non-radiosensitive tumors with life expectancy >3 months |
| [Sorensen et al. (1994)](https://pubmed.ncbi.nlm.nih.gov/8142159/) | Dexamethasone + radiation vs. radiation alone: ambulation 81% vs. 63% at end of treatment; 59% vs. 33% at 3 months | Established dexamethasone as standard adjunct to radiation in MSCC |
| [Vecht et al. (1989)](https://pubmed.ncbi.nlm.nih.gov/2771077/) | High-dose (96 mg) vs. standard (10 mg) dexamethasone: faster initial response with high-dose but similar outcomes at 1 week; more side effects with high-dose | Most centers now use moderate dose (10 mg load → 16 mg/day) due to side effect profile |
| [Rades et al. (2008)](https://pubmed.ncbi.nlm.nih.gov/18539406/) | Short-course (20 Gy/5 fractions) vs. standard (30 Gy/10 fractions): no significant difference in motor function improvement for patients with poor prognosis | Short-course radiation appropriate for patients with limited life expectancy |
| [Laufer et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23339593/) | Separation surgery + SBRT for radioresistant MSCC: 90% local control at 1 year; enabled delivery of effective radiation doses to previously radioresistant tumors | Established separation surgery + SBRT paradigm for RCC, melanoma, sarcoma spinal metastases |
| [Rosen et al. (2003)](https://pubmed.ncbi.nlm.nih.gov/14534891/) | Zoledronic acid reduced skeletal-related events by 48% compared to placebo in bone metastases from breast cancer and myeloma | Standard bone-modifying therapy for cancer-related bone disease |
| [Fizazi et al. (2011)](https://pubmed.ncbi.nlm.nih.gov/21353695/) | Denosumab superior to zoledronic acid in reducing SRE in prostate cancer bone metastases (HR 0.82, p=0.008) | Denosumab as alternative/preferred bone-modifying agent; no renal adjustment needed |

### Grading Scales

**Spinal Instability Neoplastic Score (SINS)**

| Component | Score |
|-----------|-------|
| **Location** | |
| Junctional (occiput-C2, C7-T2, T11-L1, L5-S1) | 3 |
| Mobile (C3-C6, L2-L4) | 2 |
| Semi-rigid (T3-T10) | 1 |
| Rigid (S2-S5) | 0 |
| **Pain** | |
| Mechanical (movement-related) | 3 |
| Non-mechanical / occasional | 1 |
| Pain-free | 0 |
| **Bone lesion quality** | |
| Lytic | 2 |
| Mixed (lytic/blastic) | 1 |
| Blastic | 0 |
| **Spinal alignment** | |
| Subluxation/translation | 4 |
| De novo deformity (kyphosis/scoliosis) | 2 |
| Normal alignment | 0 |
| **Vertebral body collapse** | |
| >50% collapse | 3 |
| <50% collapse | 2 |
| No collapse with >50% body involved | 1 |
| None of the above | 0 |
| **Posterolateral involvement** | |
| Bilateral | 3 |
| Unilateral | 1 |
| None | 0 |

| SINS Total Score | Interpretation | Action |
|-----------------|----------------|--------|
| 0-6 | Stable | Non-surgical management appropriate |
| 7-12 | Indeterminate (potentially unstable) | Surgical consultation recommended |
| 13-18 | Unstable | Surgical stabilization recommended |

**Bilsky Epidural Spinal Cord Compression Scale**

| Grade | Description |
|-------|-------------|
| 0 | Bone-only disease |
| 1a | Epidural impingement without deformation of thecal sac |
| 1b | Thecal sac deformation without cord abutment |
| 1c | Thecal sac deformation with cord abutment, no compression |
| 2 | Cord compression with visible CSF around cord |
| 3 | Cord compression without visible CSF around cord |

**Tokuhashi Revised Scoring System (Prognosis)**

| Parameter | Score 0 | Score 1 | Score 2 |
|-----------|---------|---------|---------|
| General condition (KPS) | Poor (10-40%) | Moderate (50-70%) | Good (80-100%) |
| Number of extraspinal bone metastases | ≥3 | 1-2 | 0 |
| Number of vertebral body metastases | ≥3 | 2 | 1 |
| Metastases to major organs | Unremovable | Removable | None |
| Primary tumor site | Lung, osteosarcoma, stomach, bladder, esophagus, pancreas | Liver, gallbladder, unidentified | Thyroid, breast, prostate, renal (carcinoid treated as thyroid) |
| Neurologic deficit (Frankel) | Complete (A/B) | Incomplete (C/D) | None (E) |

| Tokuhashi Score | Predicted Survival | Recommended Treatment |
|-----------------|-------------------|----------------------|
| 0-8 | <6 months | Palliative/conservative (short-course radiation) |
| 9-11 | 6-12 months | Palliative or excisional surgery depending on factors |
| 12-15 | >12 months | Excisional surgery; aggressive treatment justified |

**NOMS Decision Framework (Memorial Sloan Kettering)**

| Factor | Assessment | Treatment Implications |
|--------|-----------|----------------------|
| **N**eurologic | Degree of cord compression (Bilsky grade); functional status; myelopathy | High-grade compression (Bilsky 2-3) → surgical decompression; low-grade → radiation alone may suffice |
| **O**ncologic | Radiosensitivity; expected tumor response to radiation | Radiosensitive (lymphoma, myeloma, SCLC) → radiation primary; Radioresistant (RCC, melanoma, sarcoma) → surgery + SBRT |
| **M**echanical instability | SINS score | SINS ≥7 → surgical consultation for stabilization |
| **S**ystemic disease | Extent of metastatic burden; medical comorbidities; life expectancy | Widespread disease, poor prognosis → palliative approach; oligometastatic → aggressive local treatment |

---

## APPENDICES

### Appendix A: Most Common Primary Cancers Causing Spinal Metastases

| Primary Cancer | Frequency | Typical Pattern | Treatment Sensitivity |
|---------------|-----------|-----------------|----------------------|
| Breast | 20-25% | Lytic, blastic, or mixed; thoracic predilection; hormonal status guides therapy | Moderately radiosensitive; hormone-responsive |
| Lung (NSCLC) | 15-20% | Lytic; any level; molecular markers (EGFR, ALK) guide systemic therapy | Moderately radiosensitive; targeted therapy if driver mutation |
| Prostate | 15-20% | Blastic (sclerotic); lumbar/sacral predilection; PSA monitoring | Moderately radiosensitive; very hormone-responsive |
| Renal cell carcinoma | 10-15% | Highly lytic; vascular (hemorrhage risk at surgery); may be solitary | Radioresistant → SBRT preferred; pre-op embolization; immunotherapy (ipi/nivo) |
| Multiple myeloma | 5-10% | Lytic (punched-out); diffuse involvement; vertebral compression fractures | Highly radiosensitive; chemotherapy-responsive |
| Lymphoma | 3-5% | Epidural mass; may be paraspinal; dramatic steroid response | Highly radiosensitive; chemotherapy-responsive |
| Thyroid (follicular) | 3-5% | Lytic; vascular; may present years after thyroidectomy | Radioresistant → SBRT or surgery; RAI does NOT work well in bone |
| Melanoma | 2-5% | Lytic; may be hemorrhagic; rapidly progressive | Radioresistant → surgery + SBRT; immunotherapy (ipi/nivo, anti-PD1) |
| Colorectal | 2-3% | Lytic; late-stage finding; sacral predilection | Moderately radiosensitive |
| Unknown primary | 5-10% | Variable; biopsy essential | Depends on histology; empiric radiation if urgent |

### Appendix B: Emergency MSCC Algorithm

```
SUSPECTED MALIGNANT SPINAL CORD COMPRESSION
              │
              ├── Neurologic deficit? (weakness, sensory level, bladder/bowel dysfunction)
              │         YES → EMERGENT pathway
              │         NO → URGENT pathway
              │
    EMERGENT PATHWAY                      URGENT PATHWAY
         │                                      │
    Dexamethasone 10mg IV STAT             Dexamethasone 4-10mg IV
         │                                      │
    MRI whole spine STAT                   MRI whole spine <24h
    (within 4h)                                 │
         │                                 Plan treatment based
         │                                 on MRI findings
    CONFIRMED MSCC on MRI
         │
         ├── Radiosensitive tumor?
         │     (lymphoma, myeloma, SCLC, germ cell)
         │         YES → Radiation within 24h
         │                (± chemotherapy)
         │         NO ↓
         │
         ├── Surgical candidate?
         │     (Patchell criteria met)
         │         • Single level compression
         │         • Paraplegia <48h
         │         • Life expectancy >3 months
         │         • ECOG ≤2
         │         • Not radiosensitive
         │
         │    YES → Surgery within 24h → Post-op radiation (2-4 weeks)
         │    NO  → Radiation within 24h
         │
         ├── Mechanically unstable? (SINS ≥7)
         │         YES → Spine surgery for stabilization
         │               (even if radiation is primary treatment)
         │
         └── Radioresistant + not ideal surgical candidate?
                   → Consider separation surgery + SBRT
                   → Or SBRT alone if no high-grade compression
```

### Appendix C: Ambulatory Status and Prognosis

| Pre-treatment Status | Likelihood of Post-treatment Ambulation | Key Prognostic Factor |
|---------------------|----------------------------------------|----------------------|
| Ambulatory at presentation | 80-90% maintain ambulation | MOST IMPORTANT predictor — early detection is critical |
| Paraparetic (some motor function) | 40-60% regain ambulation | Timing critical: better outcomes if treated within 24-48h of deficit onset |
| Paraplegic <24h | 30-40% may regain ambulation | Emergency surgery offers best chance; radiation alone less effective |
| Paraplegic 24-48h | 10-20% may regain some function | Surgery if feasible; diminishing returns after 48h |
| Paraplegic >48h | <5% regain functional ambulation | Goals of care discussion; pain control; prevent secondary complications |
| Complete loss >72h | Very unlikely to recover | Palliative focus; comfort measures; rehabilitation for adaptation |

**Key message: Ambulatory status at time of treatment is the single most important prognostic factor. Early diagnosis and treatment within 24h of symptom onset is critical.**

### Appendix D: Dexamethasone Dosing Summary for MSCC

| Clinical Scenario | Loading Dose | Maintenance | Taper |
|-------------------|-------------|-------------|-------|
| Mild deficit, ambulatory | 10 mg IV | 4 mg PO q6h (16 mg/day) | Start taper after radiation begins; reduce 2 mg q3-5 days |
| Moderate deficit, paraparetic | 10 mg IV | 4 mg PO q6h (16 mg/day) | Taper once improving; 2 mg reduction q3-5 days |
| Severe/complete deficit, rapidly progressive | 96 mg IV (controversial) OR 10 mg IV | 24 mg PO q6h → taper to 16 mg/day within 48h | Aggressive but systematic taper; 4 mg reduction q3-5 days |
| Post-operative / post-radiation (improving) | N/A | Continue at current dose until stable | Taper over 2-3 weeks once treatment response confirmed |
| Side effect management | GI: PPI; Glucose: insulin; Sleep: dose dexamethasone before 4 PM; Myopathy: minimize duration | | |

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
