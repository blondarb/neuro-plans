---
title: "Thunderclap Headache Evaluation"
description: "Clinical decision support for emergency evaluation of thunderclap headache"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - headache
  - emergency
  - stroke-vascular
  - subarachnoid-hemorrhage
  - evaluation
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Thunderclap Headache Evaluation

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Revised per checker/rebuilder validation (v1.1)

---

**DIAGNOSIS:** Thunderclap Headache Evaluation

**ICD-10:** R51.9 (Headache, unspecified), G44.1 (Vascular headache, not elsewhere classified), I60.9 (Nontraumatic subarachnoid hemorrhage, unspecified), I67.6 (Nonpyogenic thrombosis of intracranial venous system — cerebral venous thrombosis), I67.841 (Reversible cerebrovascular vasoconstriction syndrome), I67.0 (Dissection of cerebral arteries, non-ruptured), E23.6 (Other disorders of pituitary gland — pituitary apoplexy), I63.9 (Cerebral infarction, unspecified)

**CPT CODES:** 70450 (CT head without contrast), 70460 (CT head with contrast), 70496 (CTA head), 70498 (CTA neck), 70547 (MRA head without contrast), 70549 (MRA head with/without contrast), 70553 (MRI brain with/without contrast), 70544 (MRA head without contrast), 70557 (MRI brain functional), 62270 (lumbar puncture), 89050 (CSF cell count), 89051 (CSF differential), 89060 (CSF crystal/xanthochromia), 85025 (CBC), 80053 (CMP), 85610 (PT/INR), 85730 (aPTT), 84484 (troponin), 93000 (ECG), 93886 (transcranial Doppler), 36224 (cerebral angiography/DSA)

**SYNONYMS:** Thunderclap headache, thunderclap headache evaluation, sudden severe headache, worst headache of life, sentinel headache, explosive headache, acute severe headache, hyperacute headache, crash headache, sudden-onset severe headache, peracute headache, TCH, thunderclap cephalgia

**SCOPE:** Emergency evaluation of thunderclap headache (TCH) in adults, defined as a severe headache reaching peak intensity within 60 seconds of onset. Covers the systematic diagnostic algorithm to identify or exclude life-threatening secondary causes: subarachnoid hemorrhage (SAH), cerebral venous thrombosis (CVT), reversible cerebral vasoconstriction syndrome (RCVS), cervical artery dissection, pituitary apoplexy, hypertensive emergency, meningitis, and cerebral infarction. Emphasizes the CT-then-LP algorithm, indications for CTA/MRA/MRV, time-sensitive workup, and disposition. Excludes ongoing management of specific diagnoses once identified (see individual templates: SAH, CVT, RCVS, cervical artery dissection, bacterial meningitis, etc.). This is a diagnostic evaluation template, not a disease management plan.

---

**DEFINITIONS:**
- **Thunderclap Headache (TCH):** Severe headache reaching maximum intensity within 60 seconds of onset — often described as "the worst headache of my life." Any thunderclap headache is a neurological emergency until a secondary cause is excluded.
- **Sentinel Headache:** A warning headache days-to-weeks before a major SAH; may represent a small "warning leak." Missed in up to 25-50% of cases.
- **Xanthochromia:** Yellow discoloration of CSF supernatant from breakdown of hemoglobin to bilirubin; develops ≥6h after SAH and persists up to 2-4 weeks. Most reliable CSF marker for SAH.
- **Perimesencephalic SAH:** Benign SAH pattern with blood confined to cisterns anterior to the brainstem; CTA/DSA negative for aneurysm; excellent prognosis.
- **Must-Exclude Diagnoses:** SAH, CVT, RCVS, cervical artery dissection, pituitary apoplexy — all require emergent identification and carry high morbidity/mortality if missed.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | URGENT | STAT | Baseline; infection screen (elevated WBC in meningitis); thrombocytopenia (CVT risk); leukocytosis | Normal; elevated WBC raises concern for meningitis |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | URGENT | STAT | Electrolytes; renal function (contrast planning for CTA); hepatic function; glucose | Normal |
| PT/INR (CPT 85610), aPTT (CPT 85730) | STAT | STAT | URGENT | STAT | Coagulopathy assessment; pre-LP safety; anticoagulant use (CVT workup); baseline for potential heparin | Normal |
| ESR (CPT 85652) | STAT | STAT | URGENT | STAT | Giant cell arteritis (age >50); vasculitis screen | <30 mm/h (age-adjusted) |
| CRP (CPT 86140) | STAT | STAT | URGENT | STAT | Inflammatory marker; infection; vasculitis | <1.0 mg/dL |
| Blood glucose (CPT 82947) | STAT | STAT | - | STAT | Hyperglycemia worsens outcomes in stroke; compare with CSF glucose if LP performed | Normal |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Neurogenic stunned myocardium in SAH (20-30%); concurrent ACS with hypertensive crisis | Normal (elevated in SAH-neurogenic) |
| Pregnancy test (β-hCG) (CPT 84703) | STAT | STAT | URGENT | STAT | Affects imaging decisions (contrast, radiation); pregnancy-related causes (CVT, eclampsia, pituitary apoplexy) | Document result |
| Type and screen (CPT 86900) | STAT | STAT | - | STAT | If SAH confirmed or suspected; potential surgical intervention | On file |
| D-dimer (CPT 85379) | URGENT | URGENT | URGENT | URGENT | Elevated in CVT (sensitivity ~97%, poor specificity); negative D-dimer has high NPV for CVT | <0.5 µg/mL (negative essentially excludes CVT in low-probability cases) |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Fibrinogen (CPT 85384) | URGENT | URGENT | - | URGENT | Coagulopathy; DIC screen; pre-procedure | >150 mg/dL |
| Lactate (CPT 83605) | URGENT | ROUTINE | - | URGENT | Perfusion status; sepsis (meningitis concern) | <2 mmol/L |
| Blood cultures (CPT 87040) | URGENT | URGENT | - | URGENT | If febrile or meningitis suspected | No growth |
| Procalcitonin (CPT 84145) | URGENT | ROUTINE | - | URGENT | Differentiate infectious from non-infectious etiology if febrile | <0.5 ng/mL |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Pituitary apoplexy may present with acute hypopituitarism | Normal |
| AM cortisol (CPT 82533) | URGENT | URGENT | - | URGENT | If pituitary apoplexy suspected — acute adrenal insufficiency is life-threatening | >18 µg/dL |
| Prolactin (CPT 84146) | URGENT | URGENT | ROUTINE | URGENT | Elevated in pituitary apoplexy (compression of remaining gland) or baseline stalk effect | Document |
| Toxicology screen (urine) (CPT 80307) | STAT | ROUTINE | - | STAT | Cocaine, amphetamines — sympathomimetic-associated SAH, RCVS, dissection | Negative |
| Lipid panel (CPT 80061) | - | ROUTINE | ROUTINE | - | Cardiovascular risk; vascular etiology risk stratification | Document |
| Magnesium (CPT 83735) | STAT | STAT | - | STAT | Hypomagnesemia increases vasospasm risk if SAH; needed for general ICU management | >2.0 mg/dL |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Thrombophilia panel (Factor V Leiden, prothrombin mutation, protein C/S, antithrombin III) | - | EXT | EXT | - | Young patient with CVT and no clear risk factor; hypercoagulable state | Normal |
| Antiphospholipid antibodies (lupus anticoagulant, anticardiolipin, anti-beta-2 glycoprotein) | - | EXT | EXT | - | CVT or stroke in young patient; antiphospholipid syndrome | Negative |
| Pituitary hormone panel (GH, IGF-1, LH, FSH, free T4, ACTH) | - | EXT | EXT | - | Suspected pituitary apoplexy; assess degree of hypopituitarism | Variable; document deficiencies |
| Urine catecholamines/metanephrines | - | EXT | EXT | - | Pheochromocytoma as cause of hypertensive headache crisis | Normal |
| Connective tissue disorder workup | - | - | EXT | - | Young patient with dissection or aneurysm; Ehlers-Danlos, Marfan, fibromuscular dysplasia features | Clinical + genetic |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | STAT | STAT | IMMEDIATE — door-to-CT target <25 min. This is the FIRST test for ALL thunderclap headaches. Sensitivity for SAH: ~98-100% within 6h of onset; ~93% at 12h; ~85% at 24h; declines significantly after 3-5 days | Hyperdense blood in basal cisterns, Sylvian fissure, interhemispheric fissure (SAH); parenchymal hemorrhage; hydrocephalus; mass (pituitary apoplexy); hypodensity (infarct) | None significant — no reason to delay |
| CT angiography (CTA) head and neck (CPT 70496, 70498) | STAT | STAT | URGENT | STAT | Obtain simultaneously with or immediately after non-contrast CT. Essential to identify: aneurysm (SAH), segmental vasoconstriction (RCVS), dissection (vertebral or carotid), venous thrombosis (if CT venogram protocol included) | Aneurysm (location, size, morphology); "string of beads" vasoconstriction (RCVS); intimal flap or pseudoaneurysm (dissection); vessel occlusion | Contrast allergy (premedicate if time allows; benefit usually outweighs risk in emergency); renal impairment (relative — do not delay for Cr in acute thunderclap) |
| ECG (12-lead) (CPT 93000) | STAT | STAT | - | STAT | Immediately — within minutes of arrival | Deep T-wave inversions ("cerebral T waves"), ST changes, QT prolongation (SAH); arrhythmia; hypertensive emergency findings | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with/without contrast (CPT 70553) | URGENT | URGENT | URGENT | URGENT | Within 24h if CT negative and diagnosis uncertain. FLAIR detects subacute blood (SAH >12h); DWI detects ischemia (infarct, vasospasm); T1 with contrast for pituitary mass; SWI/GRE for microhemorrhages | FLAIR hyperintensity in sulci (subacute SAH); DWI restriction (stroke); pituitary mass with hemorrhage; cortical/convexity SAH (RCVS) | Pacemaker/ICD (conditional devices may be scanned); hemodynamic instability; agitation (sedation may be needed) |
| MRA head (CPT 70544/70547) | URGENT | URGENT | URGENT | URGENT | With MRI; alternative to CTA if contrast contraindicated or for follow-up | Aneurysm; segmental vasoconstriction (RCVS — may be normal early in course); dissection | Standard MRI contraindications |
| MRV head (MR venography) (CPT 70547) | URGENT | URGENT | URGENT | URGENT | If CVT suspected (headache + risk factors: OCP use, pregnancy/postpartum, thrombophilia, dehydration); or CT venogram unavailable | Absent flow signal in dural sinuses/cortical veins (thrombosis) | Standard MRI contraindications |
| CT venography (CTV) (CPT 70496) | URGENT | URGENT | - | URGENT | Obtained with CTA using delayed-phase protocol; preferred in ED for speed if CVT suspected | Filling defect in dural sinus; "empty delta sign" (superior sagittal sinus thrombosis) | Contrast allergy; renal impairment (relative) |
| Conventional cerebral angiography (DSA) (CPT 36224) | - | URGENT | - | URGENT | GOLD STANDARD for aneurysm detection if CTA negative but clinical suspicion remains high; also detects RCVS vasoconstriction (may require repeat at 2-3 weeks if initially normal); diagnoses vasculitis | Aneurysm missed by CTA; segmental vasoconstriction (RCVS); vasculitis (irregular vessel narrowing); dissection | Contrast allergy; renal impairment; coagulopathy (correct first); hemodynamic instability |
| Repeat DSA (if initial negative) | - | ROUTINE | - | ROUTINE | 7-14 days if initial DSA negative and non-perimesencephalic SAH pattern; also repeat at 2-4 weeks for suspected RCVS (vasoconstriction may develop delayed) | Previously missed aneurysm; interval development of vasoconstriction | Same as initial DSA |
| Transcranial Doppler (TCD) (CPT 93886) | - | URGENT | - | URGENT | If SAH confirmed — begin daily from post-bleed day 3 through day 14 (vasospasm window); also detects elevated flow velocities in RCVS | MCA mean velocity >120 cm/s concerning; >200 cm/s severe vasospasm; Lindegaard ratio >3 | Absent temporal bone window (~10%) |
| MRI sella (dedicated pituitary protocol) (CPT 70553) | - | URGENT | URGENT | URGENT | If pituitary apoplexy suspected (headache + visual field cut + ophthalmoplegia + known pituitary adenoma) | Hemorrhagic or necrotic pituitary mass; sellar expansion; optic chiasm compression | Standard MRI contraindications |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | On admission if SAH or meningitis; neurogenic pulmonary edema in SAH | Neurogenic pulmonary edema; aspiration; widened mediastinum (aortic dissection with headache) | None |
| Echocardiogram (TTE) (CPT 93306) | - | ROUTINE | - | ROUTINE | If SAH confirmed — neurogenic stunned myocardium (20-30%); if embolic cause suspected | Takotsubo; regional wall motion abnormalities; valvular vegetation; PFO | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| 3D rotational angiography | - | EXT | - | EXT | During DSA for complex aneurysm anatomy | Detailed aneurysm morphology | Same as DSA |
| CT perfusion (CTP) (CPT 0042T) | - | URGENT | - | URGENT | If vasospasm suspected in confirmed SAH (post-bleed days 4-14); also detects perfusion deficit in RCVS with stroke | Perfusion deficits; mismatch (reversible ischemia) | Contrast allergy; renal impairment |
| Spinal MRI | - | EXT | EXT | - | If spinal SAH suspected (back/leg pain with meningismus; intracranial imaging negative) | Spinal subarachnoid blood; spinal vascular malformation | Standard MRI contraindications |
| Conventional spinal angiography | - | EXT | - | EXT | If spinal SAH with suspected vascular malformation | Spinal AVM/AVF | Same as DSA |

### LUMBAR PUNCTURE

**Indication:** CT head is NEGATIVE but clinical suspicion for SAH or other secondary cause remains. LP (CPT 62270) is MANDATORY if CT does not explain the thunderclap headache. Also indicated if meningitis is suspected regardless of CT findings.

**Timing:** URGENT. For SAH detection, ideally wait ≥6h (preferably 12h) from headache onset to allow xanthochromia to develop. However, do NOT delay LP if meningitis is a concern — perform immediately.

**Pre-LP Checklist:**
- Platelet count >50,000 and INR <1.5 (or correct first)
- No evidence of mass lesion or midline shift on CT (herniation risk)
- Document time of headache onset (essential for interpreting xanthochromia results)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure (CPT 89060) | Elevated in SAH, CVT, meningitis; low in spontaneous intracranial hypotension (SIH) | Normal: 6-20 cm H2O. Elevated: >20 cm H2O (SAH, CVT, meningitis). Low: <6 cm H2O (SIH — different mechanism) | URGENT | ROUTINE | ROUTINE | URGENT |
| Cell count (tubes 1 AND 4) (CPT 89050) | Distinguish SAH from traumatic tap: SAH = RBC count does NOT clear significantly between tube 1 and tube 4 | SAH: RBCs in tube 4 ≥ tube 1 (no clearing). Traumatic tap: tube 4 << tube 1 (clearing >25%) | URGENT | ROUTINE | ROUTINE | URGENT |
| Xanthochromia (visual and/or spectrophotometry) (CPT 89060) | Most reliable CSF test for SAH; develops >6h post-bleed from RBC breakdown (bilirubin); spectrophotometry more sensitive than visual inspection | Present = SAH (sensitivity >95% at 12h-2 weeks). Absent at >12h from onset = essentially excludes SAH | URGENT | ROUTINE | ROUTINE | URGENT |
| Protein (CPT 89060) | Elevated in SAH, meningitis, CVT | Normal 15-45 mg/dL; elevated in SAH and infection | URGENT | ROUTINE | ROUTINE | URGENT |
| Glucose (CPT 89060) | Low CSF:serum glucose ratio (<0.4) suggests bacterial meningitis; normal in SAH | Normal >60% of serum glucose | URGENT | ROUTINE | ROUTINE | URGENT |
| Gram stain and culture (CPT 87070, 87040) | Exclude bacterial meningitis (meningeal signs overlap with SAH) | No organisms | URGENT | ROUTINE | ROUTINE | URGENT |
| CSF WBC with differential | Neutrophilic pleocytosis (bacterial meningitis); lymphocytic (viral/fungal); mild pleocytosis in SAH (reactive) | SAH: mild pleocytosis (reactive). Meningitis: significant pleocytosis | URGENT | ROUTINE | ROUTINE | URGENT |

**Special Handling:** Xanthochromia sample must be protected from light (wrap tube in foil); centrifuge immediately; spectrophotometry if available (more sensitive than visual inspection). Label tube with exact time of LP and time of headache onset. In ICU patients, LP may require lateral decubitus positioning or fluoroscopic guidance if patient is intubated or sedated.

**Key Interpretation:**
- CT negative + LP negative (no xanthochromia, no excess RBCs at ≥12h) = SAH effectively excluded
- CT negative + xanthochromia present = SAH until proven otherwise → proceed to CTA/DSA
- CT negative + elevated opening pressure + normal CSF = evaluate for CVT → proceed to MRV/CTV
- CT negative + LP with pleocytosis and low glucose = initiate meningitis workup
- CT negative + low opening pressure (<6 cm H2O) = evaluate for SIH → obtain MRI + CT myelography

---

## 3. TREATMENT

### CRITICAL PRIORITIES — THUNDERCLAP HEADACHE ALGORITHM
1. **ABCs** — Secure airway if GCS ≤8; stabilize blood pressure
2. **Immediate CT head** — Within 25 minutes of arrival (door-to-CT)
3. **CT positive for blood?** → Activate SAH protocol; STAT CTA; neurosurgery consult
4. **CT negative?** → LP (wait ≥6h from onset if feasible); CTA head/neck
5. **Identify the cause** — SAH, CVT, RCVS, dissection, pituitary apoplexy, meningitis, hypertensive emergency
6. **Time is critical** — Missed SAH has 40% case fatality if re-bleeding occurs; CVT requires urgent anticoagulation; dissection needs antithrombotic therapy

### 3A. Acute/Emergent — Stabilization & Symptom Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Nicardipine IV (CPT 96365) | IV | Hypertensive emergency (SBP >180); SAH with SBP >160; hypertensive crisis with thunderclap | 5 mg/h :: IV :: continuous :: 5 mg/h IV; titrate by 2.5 mg/h q5-15min; max 15 mg/h. Target SBP <160 if SAH suspected (until aneurysm secured). For hypertensive emergency: reduce MAP by 20-25% in first hour | Severe aortic stenosis | Continuous arterial BP; neuro checks q1h | STAT | STAT | - | STAT |
| Labetalol IV (CPT 96374) | IV | Alternative to nicardipine for BP control | 10-20 mg :: IV :: q10-20min :: 10-20 mg IV q10-20min; max 300 mg. Alternative first-line for hypertensive emergency | Heart block; severe bradycardia; asthma; cocaine use (relative — unopposed alpha) | HR; BP continuous | STAT | STAT | - | STAT |
| Acetaminophen IV (CPT 96374) | IV | First-line pain control for thunderclap headache during evaluation; avoid masking exam | 1000 mg :: IV :: q6h :: 1000 mg IV q6h; max 4g/day. Safe first-line — does not affect coagulation or mask pupillary exam | Hepatic impairment (reduce dose); <50 kg (weight-based dosing) | Pain score; hepatic function if repeat dosing | STAT | STAT | - | STAT |
| Ketorolac IV (CPT 96374) | IV | Moderate-severe headache pain; use ONLY after SAH excluded or deemed unlikely (affects platelet function) | 15-30 mg :: IV :: once :: 15-30 mg IV once; max 120 mg/day. Do NOT use if SAH suspected (platelet inhibition increases re-bleed risk); do NOT use if LP planned within 24h (relative) | SAH suspected; active bleeding; renal impairment; coagulopathy; GI bleed | Renal function; GI symptoms | URGENT | URGENT | - | URGENT |
| Ondansetron (CPT 96374) | IV | Nausea/vomiting (common with thunderclap headache and elevated ICP) | 4 mg :: IV :: q6h PRN :: 4 mg IV q6h PRN | QT prolongation; severe hepatic impairment | QTc if repeated dosing | STAT | STAT | - | STAT |
| Metoclopramide (CPT 96374) | IV | Alternative antiemetic; also has analgesic properties for headache | 10 mg :: IV :: once :: 10 mg IV over 15 min; may repeat once. Avoid in patients with Parkinson's or dystonic reactions | Parkinson's disease; bowel obstruction; pheochromocytoma; seizure history (relative) | Dystonic reactions; akathisia | STAT | STAT | - | STAT |
| IV isotonic fluids (CPT 96360) | IV | Volume resuscitation and hydration; dehydration worsens headache and may worsen CVT | 1-1.5 mL/kg/h :: IV :: continuous :: NS at 1-1.5 mL/kg/h; goal euvolemia. Essential for pre-contrast hydration (CTA) and general resuscitation | Volume overload; CHF | I/O; serum Na | STAT | STAT | - | STAT |
| Levetiracetam (CPT 96374) | IV | ONLY if SAH confirmed or seizure occurs; not routine for undifferentiated thunderclap headache | 1000 mg :: IV :: once :: 1000 mg IV load; then 500-1000 mg IV/PO BID. Use short-term (3-7 days) in confirmed SAH per AHA guidelines | Renal impairment (dose adjust) | Seizure activity; renal function | STAT | STAT | - | STAT |
| Intubation / Airway protection | - | GCS ≤8; inability to protect airway; respiratory failure; clinical herniation | - :: - :: once :: Rapid sequence intubation per institutional protocol; use hemodynamically neutral agents; avoid succinylcholine if hyperkalemia risk | Difficult airway (prepare backup plan) | Avoid hypotension during RSI; maintain BP goals; continuous SpO2; ETCO2 | STAT | STAT | - | STAT |

### 3B. Cause-Specific Initial Treatment (Start While Awaiting Definitive Management)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Nimodipine (if SAH confirmed) | PO | SAH confirmed — vasospasm prevention (CORNERSTONE therapy) | 60 mg :: PO :: q4h :: 60 mg PO/NG q4h x 21 days. START within 96h of SAH. If hypotension: 30 mg q2h. Do NOT give IV — oral only | Hypotension (SBP <90 — reduce dose) | BP with each dose; ensure enteral route only | - | STAT | - | STAT |
| Nimodipine (if RCVS confirmed) | PO | RCVS — empiric calcium channel blocker; off-label but widely used | 60 mg :: PO :: q4h :: 60 mg PO q4h; duration 4-12 weeks until vasoconstriction resolves on follow-up imaging | Hypotension | BP with each dose | - | STAT | ROUTINE | STAT |
| Heparin IV (if CVT confirmed) (CPT 96365) | IV | Cerebral venous thrombosis — anticoagulation is standard even with hemorrhagic venous infarct | 80 units/kg :: IV :: bolus :: 80 units/kg IV bolus; then 18 units/kg/h infusion. Target aPTT 1.5-2.5x control. Transition to LMWH or warfarin | Active major hemorrhage (ICH from CVT is NOT a contraindication per guidelines); HIT | aPTT q6h until therapeutic; platelets q3 days; neuro checks | STAT | STAT | - | STAT |
| Aspirin (if cervical artery dissection confirmed) | PO | Cervical artery dissection — antiplatelet therapy (equivalent to anticoagulation per CADISS trial) | 325 mg :: PO :: daily :: Aspirin 325 mg PO daily x 3-6 months. Preferred in patients with large infarct or hemorrhagic transformation | Active hemorrhagic stroke; allergy | Neuro checks; GI symptoms | STAT | STAT | ROUTINE | STAT |
| Heparin then warfarin (if cervical artery dissection confirmed — anticoagulation option) | IV/PO | Cervical artery dissection — anticoagulation alternative (equivalent to antiplatelet per CADISS trial) | 80 units/kg :: IV :: bolus :: 80 units/kg IV bolus; then 18 units/kg/h infusion; transition to warfarin (INR 2-3) x 3-6 months. Preferred if recurrent ischemic events on antiplatelet | Active hemorrhagic stroke; massive infarct; HIT | INR; aPTT q6h until therapeutic; neuro checks | STAT | STAT | ROUTINE | STAT |
| Hydrocortisone (if pituitary apoplexy with hemodynamic instability) | IV | Acute adrenal crisis in pituitary apoplexy | 100 mg :: IV :: bolus :: 100 mg IV bolus; then 50 mg IV q8h until endocrine evaluation complete. Life-saving — do not wait for cortisol results if clinical suspicion high | None in acute crisis | BP; glucose; electrolytes; cortisol levels | STAT | STAT | - | STAT |
| Ceftriaxone (if bacterial meningitis suspected) | IV | Febrile thunderclap headache with meningeal signs — empiric gram-negative and pneumococcal coverage | 2 g :: IV :: q12h :: Ceftriaxone 2 g IV q12h. Do NOT delay antibiotics for LP or imaging | Cephalosporin allergy (use meropenem or chloramphenicol) | CSF culture results; clinical response; renal function | STAT | STAT | - | STAT |
| Vancomycin (if bacterial meningitis suspected) | IV | Empiric MRSA and resistant pneumococcal coverage in meningitis | 15-20 mg/kg :: IV :: q8-12h :: 15-20 mg/kg IV q8-12h; target trough 15-20 mcg/mL. Administer with ceftriaxone for empiric coverage | Vancomycin allergy (use linezolid) | Vancomycin trough; renal function; ototoxicity | STAT | STAT | - | STAT |
| Dexamethasone (if bacterial meningitis suspected) | IV | Reduce inflammation and improve outcomes in bacterial meningitis (especially pneumococcal) | 0.15 mg/kg :: IV :: q6h :: 0.15 mg/kg IV q6h x 4 days. Give 15-20 min before or with first antibiotic dose | GI bleeding (relative); immunocompromised (relative) | Blood glucose; GI symptoms | STAT | STAT | - | STAT |
| Remove vasoconstrictor triggers (if RCVS suspected) | - | Immediately discontinue all potential triggers: triptans, ergotamines, SSRIs/SNRIs, cannabis, cocaine, amphetamines, nasal decongestants, nicotine patches | - :: - :: immediate :: Discontinue all vasoconstrictor agents immediately upon suspicion of RCVS; document all discontinued medications | None | Document all discontinued medications; headache frequency decreases after trigger removal | STAT | STAT | ROUTINE | STAT |

### 3C. Headache-Specific Red Flag Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Pneumatic compression devices (DVT prophylaxis) | External | All admitted thunderclap headache patients (immobilized during workup; many diagnoses carry VTE risk) | - :: External :: continuous :: Apply bilateral sequential compression devices on admission; maintain until patient is ambulatory | Acute DVT in affected limb | Skin checks; device compliance | STAT | STAT | - | STAT |
| Pantoprazole (stress ulcer prophylaxis) | IV | ICU admission or steroid use | 40 mg :: IV :: daily :: 40 mg IV/PO daily | C. diff risk (long-term) | GI symptoms | - | ROUTINE | - | ROUTINE |
| Docusate (stool softener) | PO | Avoid Valsalva/straining (may increase ICP; re-bleed risk in SAH) | 100 mg :: PO :: BID :: 100 mg PO BID | Bowel obstruction | Bowel movements | - | ROUTINE | - | ROUTINE |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology / Vascular neurology — ALL thunderclap headaches; diagnostic guidance; RCVS management; CVT management; dissection | STAT | STAT | URGENT | STAT |
| Neurosurgery — SAH confirmed or suspected; aneurysm securing; EVD for hydrocephalus; pituitary apoplexy (transsphenoidal approach) | STAT | STAT | - | STAT |
| Interventional neuroradiology / Neuroendovascular — aneurysm coiling; intra-arterial vasospasm treatment; thrombectomy for CVT (refractory); stenting for dissection | STAT | STAT | - | STAT |
| Neurocritical care / Neurointensivist — SAH ICU management; deteriorating patient; vasospasm monitoring | STAT | STAT | - | STAT |
| Ophthalmology — pituitary apoplexy (visual field assessment); papilledema evaluation; Terson syndrome (vitreous hemorrhage in SAH) | URGENT | URGENT | URGENT | URGENT |
| Endocrinology — pituitary apoplexy hormone replacement; long-term pituitary monitoring | - | URGENT | ROUTINE | URGENT |
| Hematology — CVT with thrombophilia; coagulopathy management | - | ROUTINE | ROUTINE | - |
| Infectious disease — meningitis confirmed or atypical CSF findings | - | URGENT | - | URGENT |
| Headache specialist / Neurology outpatient — negative workup; primary thunderclap headache; migraine variant; follow-up for recurrence | - | ROUTINE | ROUTINE | - |
| Social work / Case management — family support; disposition planning | - | ROUTINE | - | - |

### 4B. Patient / Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Thunderclap headache is a neurological emergency — every episode requires evaluation until a cause is identified or excluded | STAT | ROUTINE | ROUTINE |
| Call 911 immediately if: sudden severe headache ("worst headache of life"), loss of consciousness, seizure, new weakness, vision changes, fever with stiff neck | STAT | ROUTINE | ROUTINE |
| Do NOT take aspirin, ibuprofen, or blood thinners before evaluation is complete (may worsen bleeding if SAH) | STAT | ROUTINE | ROUTINE |
| Avoid triggers: cocaine, amphetamines, triptans, heavy exertion, Valsalva until diagnosis is confirmed | STAT | ROUTINE | ROUTINE |
| If discharged after negative workup: return immediately if headache recurs with same severity, if new symptoms develop (weakness, vision changes, confusion), or if fever develops | STAT | ROUTINE | ROUTINE |
| Report any recurrent thunderclap headaches over days-to-weeks to the treating team immediately — recurrence indicates RCVS and requires follow-up imaging even if initial workup is negative | - | ROUTINE | ROUTINE |
| Follow up with neurology within 1-2 weeks after discharge; return sooner if symptoms recur | - | ROUTINE | ROUTINE |
| First-degree relatives of SAH patients: undergo aneurysm screening if 2 or more family members are affected | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Stop all cocaine and amphetamine use immediately (strongly associated with SAH, RCVS, and dissection) | STAT | ROUTINE | ROUTINE |
| Stop smoking (strongest modifiable risk factor for aneurysm formation) | - | ROUTINE | ROUTINE |
| Maintain blood pressure control (<130/80 mmHg long-term) | - | ROUTINE | ROUTINE |
| Avoid vasoconstrictor medications (triptans, ergotamines, decongestants) until RCVS excluded | STAT | ROUTINE | ROUTINE |
| Limit alcohol intake (heavy drinking increases SAH risk) | - | ROUTINE | ROUTINE |
| Maintain adequate hydration (dehydration may contribute to CVT risk) | - | ROUTINE | ROUTINE |
| Discontinue oral contraceptives if CVT diagnosed; use non-estrogen alternatives (oral contraceptives increase CVT risk) | - | ROUTINE | ROUTINE |
| Avoid extreme exertion or Valsalva maneuvers during the acute evaluation period | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Subarachnoid hemorrhage (SAH) | Sudden severe headache; loss of consciousness in 50%; meningismus; may have focal deficits; up to 25% present with sentinel headache days before rupture | CT head (blood in basal cisterns); LP (xanthochromia, non-clearing RBCs); CTA (aneurysm) |
| Reversible cerebral vasoconstriction syndrome (RCVS) | Recurrent thunderclap headaches over 1-3 weeks; triggered by exertion, Valsalva, sexual activity, showering, emotional stress; vasoconstrictor exposure history; may have convexity SAH; no aneurysm | CTA/MRA (multifocal segmental narrowing — may be normal in first week); MRI (convexity SAH, PRES overlap, stroke); resolves on follow-up imaging at 12 weeks |
| Cerebral venous thrombosis (CVT) | Headache (may be thunderclap or progressive); seizures; focal deficits; risk factors: OCP, pregnancy/postpartum, thrombophilia, dehydration; may have hemorrhagic venous infarct | MRV or CTV (absent flow in dural sinuses); CT may show "cord sign" (hyperdense sinus); D-dimer elevated |
| Cervical artery dissection (carotid or vertebral) | Headache/neck pain (ipsilateral); Horner syndrome (carotid); may have stroke; history of minor trauma, chiropractic manipulation, or connective tissue disorder | CTA neck (intimal flap, pseudoaneurysm, string sign); MRI neck (crescent sign — intramural hematoma on fat-sat T1) |
| Pituitary apoplexy | Sudden headache + visual field defect (bitemporal hemianopia) + ophthalmoplegia (CN III, IV, VI); known pituitary adenoma (often undiagnosed); may have signs of acute adrenal crisis (hypotension, hyponatremia) | MRI sella (hemorrhagic/necrotic pituitary mass with sellar expansion); hormone panel (cortisol, TSH, prolactin); visual field testing |
| Hypertensive emergency | Severely elevated BP (>180/120) with headache and end-organ damage (encephalopathy, renal failure, retinal hemorrhages); no blood on CT; may overlap with PRES | CT (no blood; may show PRES features); BP measurement; end-organ evaluation; MRI (posterior white matter edema in PRES) |
| Bacterial meningitis | Fever + headache + nuchal rigidity + altered mental status (classic triad in ~50%); may have rash (meningococcemia); progresses rapidly | LP (neutrophilic pleocytosis, low glucose, high protein, positive gram stain/culture); blood cultures; procalcitonin elevated; CT typically normal |
| Primary intracerebral hemorrhage | Focal deficits with headache; parenchymal hematoma on CT with minimal subarachnoid blood; hypertensive basal ganglia/thalamic location | CT (parenchymal hemorrhage, not cisternal pattern); CTA (no aneurysm unless hemorrhage extends into subarachnoid space) |
| Posterior reversible encephalopathy syndrome (PRES) | Headache, seizures, visual disturbance, altered mental status; hypertension; often overlaps with RCVS or eclampsia | MRI (posterior white matter vasogenic edema on FLAIR/T2); CT may be normal early; usually reversible with BP control |
| Ischemic stroke | Sudden onset focal deficits; headache present in 25% of strokes; basilar artery occlusion may present with thunderclap headache and rapid deterioration | CT (early signs of infarct; may be normal within 6h); CTA (large vessel occlusion); MRI DWI (acute restricted diffusion) |
| Primary (benign) thunderclap headache | Diagnosis of EXCLUSION after complete negative workup; mimics SAH presentation; may recur; some may represent undiagnosed RCVS | Normal CT, LP, CTA, MRI/MRA; clinical follow-up |
| Spontaneous intracranial hypotension (SIH) / CSF leak | Orthostatic headache (worse upright, better supine); may present acutely with thunderclap; may have subdural hygromas | MRI (diffuse pachymeningeal enhancement, brain sagging); LP (low opening pressure <6 cm H2O); CT myelography for leak localization |
| Colloid cyst of third ventricle | Positional thunderclap headache with transient obstruction of foramen of Monro; may cause acute hydrocephalus; rare but dangerous | CT/MRI (hyperdense/enhancing cyst at foramen of Monro; acute hydrocephalus if obstructing) |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Blood pressure | STAT | STAT | ROUTINE | STAT | Continuous in ED and ICU. q1h on floor. SAH: SBP <160 until aneurysm secured. Hypertensive emergency: reduce MAP 20-25% in first hour | SBP <160 (if SAH); MAP reduction 20-25% (if hypertensive emergency); SBP <140 (CVT/RCVS) | Titrate antihypertensives; arterial line if labile |
| GCS / Neurologic exam | STAT | STAT | ROUTINE | STAT | q1h x 12h; then q2h x 24h; then q4h. Document GCS, pupillary response, motor exam, speech | Stable or improving | If declining: STAT repeat CT; reassess diagnosis; escalate care |
| Headache severity (pain scale 0-10) | STAT | STAT | ROUTINE | STAT | q2-4h; with each assessment | Improving trend | If worsening or new thunderclap recurrence: repeat imaging; RCVS likely if recurrent |
| Temperature | STAT | STAT | - | STAT | q4h (q1h if febrile) | <37.5 C | If febrile: infection workup (blood cultures, UA, CXR); LP if not yet performed; antibiotics if meningitis suspected |
| Serum sodium | STAT | STAT | - | STAT | q8h (q6h if SAH confirmed — hyponatremia common) | 135-145 mEq/L | If <135: differentiate CSW vs SIADH (if SAH); fluid/salt management |
| Blood glucose | STAT | STAT | - | STAT | q6h | 140-180 mg/dL | Insulin if hyperglycemic; avoid <60 |
| ICP (if EVD placed for SAH/hydrocephalus) | - | - | - | STAT | Continuous; record q1h | ICP <22 mmHg; CPP 60-70 mmHg | CSF drainage; osmotherapy; surgical decompression |
| Troponin / BNP | STAT | ROUTINE | - | ROUTINE | Troponin q8h x 24h; then daily if SAH | Trending | If rising: echo; cardiology consult |
| aPTT (if on heparin for CVT or dissection) | STAT | STAT | - | STAT | q6h until therapeutic, then daily | aPTT 1.5-2.5x control (or per institutional protocol) | Adjust heparin dose; assess for bleeding |
| Repeat CT head | STAT | STAT | - | STAT | Repeat if neurologic change; at 24h if SAH; post-LP if concern for herniation | Stable | New hemorrhage or infarct: escalate to appropriate pathway |
| Transcranial Doppler (if SAH confirmed) | - | STAT | - | STAT | Daily from day 3 through day 14 | MCA <120 cm/s; Lindegaard ratio <3 | If velocities rising: CTA/CTP; induced hypertension if symptomatic |
| Cortisol / pituitary hormones (if apoplexy) | - | URGENT | ROUTINE | URGENT | At diagnosis; repeat at 48-72h; long-term outpatient monitoring | Cortisol >18 µg/dL | Replacement therapy; endocrinology follow-up |
| Visual fields (if pituitary apoplexy) | - | URGENT | ROUTINE | URGENT | At presentation; daily if visual deficits present | Stable or improving | Neurosurgical decompression if worsening |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home from ED (negative workup) | Complete negative evaluation: normal CT head, normal CTA head/neck, normal LP (performed ≥6h from onset with no xanthochromia, no excess RBCs, normal opening pressure). Stable neurologic exam. Patient understands return precautions. Neurology follow-up arranged within 1-2 weeks. Obtain outpatient MRI/MRA if not performed in ED |
| Admit to observation / inpatient neurology | Inconclusive workup (LP pending, CTA pending, awaiting MRI); persistent severe headache requiring IV analgesia; recurrent thunderclap headaches (RCVS likely); new neurologic deficit; abnormal labs requiring monitoring |
| Admit to Neuro-ICU | Confirmed SAH (all cases — minimum 14-21 days ICU monitoring); CVT with hemorrhagic infarct or declining GCS; pituitary apoplexy with hemodynamic instability; large territorial stroke from dissection or RCVS; any thunderclap headache patient with GCS ≤12 or declining exam |
| Transfer to comprehensive stroke center | SAH confirmed and no neurosurgery or interventional neuroradiology available on-site — TRANSFER IMMEDIATELY; suspected CVT or dissection requiring endovascular intervention not available locally |
| Outpatient follow-up (after negative ED evaluation) | Neurology within 1-2 weeks; outpatient MRI/MRA if not done; repeat CTA/MRA at 4-6 weeks if RCVS suspected (vasoconstriction may develop delayed); aneurysm screening for family members if SAH |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| CT head sensitivity ~98-100% within 6h for SAH | Class I, Level A | [Perry et al. (BMJ 2011)](https://pubmed.ncbi.nlm.nih.gov/21768192/) — Prospective cohort; 3132 patients; sensitivity 100% (95% CI 97-100%) for CT within 6h |
| LP mandatory if CT negative but clinical suspicion for SAH persists | Class I, Level B | [AHA/ASA SAH Guidelines (Connolly et al. Stroke 2012)](https://pubmed.ncbi.nlm.nih.gov/22556195/) |
| Xanthochromia by spectrophotometry is gold standard CSF test for SAH | Class I, Level B | [UK National SAH Guidelines (Edlow et al. Stroke 2016)](https://pubmed.ncbi.nlm.nih.gov/27217503/); sensitivity >95% at 12h-2 weeks |
| CTA sensitivity 95-100% for aneurysms >3mm | Class I, Level A | [White PM et al. (Radiology 2003)](https://pubmed.ncbi.nlm.nih.gov/14500398/) — Meta-analysis of CTA for intracranial aneurysm detection; [Defined et al. (Stroke 2006)](https://pubmed.ncbi.nlm.nih.gov/16902176/) — requires full author verification |
| Anticoagulation for CVT even with hemorrhagic infarct | Class I, Level A | [EFNS Guidelines (Ferro et al. Eur J Neurol 2017)](https://pubmed.ncbi.nlm.nih.gov/28128773/); [AHA/ASA CVT Guidelines (Saposnik et al. Stroke 2011)](https://pubmed.ncbi.nlm.nih.gov/21293023/) |
| Nimodipine 60 mg PO q4h x 21 days for SAH vasospasm prevention | Class I, Level A | [Pickard et al. (BMJ 1989)](https://pubmed.ncbi.nlm.nih.gov/2496789/) |
| RCVS: calcium channel blockers (nimodipine/verapamil) for headache and vasoconstriction | Class IIa, Level C | [Ducros et al. (Brain 2007)](https://pubmed.ncbi.nlm.nih.gov/17468116/); [Singhal et al. (Neurology 2011)](https://pubmed.ncbi.nlm.nih.gov/21383328/) |
| RCVS: vasoconstriction resolves within 12 weeks — follow-up imaging to confirm | Class I, Level B | [Calabrese et al. (Ann Intern Med 2007)](https://pubmed.ncbi.nlm.nih.gov/17210890/) |
| Cervical artery dissection: antiplatelet vs anticoagulation equivalent | Class I, Level B | [CADISS trial (Markus et al. Lancet Neurol 2015)](https://pubmed.ncbi.nlm.nih.gov/25987284/) |
| Pituitary apoplexy: emergent corticosteroid replacement is life-saving | Class I, Level C | [UK Pituitary Apoplexy Guidelines (Rajasekaran et al. Clin Endocrinol 2011)](https://pubmed.ncbi.nlm.nih.gov/20550536/) |
| D-dimer sensitivity ~97% for CVT; negative D-dimer has high NPV | Class IIa, Level B | [Kosinski et al. (Stroke 2004)](https://pubmed.ncbi.nlm.nih.gov/15243148/) |
| Ottawa SAH Rule: 100% sensitivity for ruling out SAH in ED (validated clinical decision rule) | Class IIa, Level B | [Perry et al. (JAMA 2013)](https://pubmed.ncbi.nlm.nih.gov/24065012/) |
| Recurrent thunderclap headaches over days suggest RCVS over SAH | Class IIa, Level C | [Ducros et al. (Brain 2007)](https://pubmed.ncbi.nlm.nih.gov/17468116/) |
| Primary thunderclap headache is a diagnosis of exclusion only | Class I, Level C | [ICHD-3 (Headache Classification Committee, Cephalalgia 2018)](https://pubmed.ncbi.nlm.nih.gov/29368949/) |
| SBP <160 until aneurysm secured in SAH | Class I, Level B | [AHA/ASA SAH Guidelines (Connolly et al. Stroke 2012)](https://pubmed.ncbi.nlm.nih.gov/22556195/) |
| Early aneurysm securing (<24h) improves outcomes | Class I, Level B | [AHA/ASA SAH Guidelines 2012](https://pubmed.ncbi.nlm.nih.gov/22556195/); [de Gans et al. (Neurosurgery 2002)](https://pubmed.ncbi.nlm.nih.gov/11844269/) |

---

## CHANGE LOG

**v1.1 (February 2, 2026) — Checker/Rebuilder Pipeline**
- Fixed placeholder "Defined et al." reference: corrected first CTA citation to White PM et al. (Radiology 2003, PMID 14500398); flagged second CTA citation (PMID 16902176) as requiring full author verification (C1/R1)
- Reordered LP table columns to place venue columns last per style guide: Study | Rationale | Target Finding | ED | HOSP | OPD | ICU (C2/R3)
- Restructured Section 4A (Referrals) from 6-column to 5-column format (Recommendation | ED | HOSP | OPD | ICU); merged indication text into Recommendation column (C3/R2)
- Split antithrombotic for dissection into two separate rows: Aspirin and Heparin/warfarin (M2/R4)
- Split empiric meningitis coverage into three separate rows: Ceftriaxone, Vancomycin, Dexamethasone (M3/R5)
- Fixed vasoconstrictor trigger row dosing field: changed "N/A" to "-" for consistency (M1)
- Replaced non-directive language in LP Key Interpretation: "consider CVT" → "evaluate for CVT"; "Consider MRI/MRA" → "Obtain MRI/MRA"; added SIH interpretation line (R6)
- Replaced non-directive language in Disposition: "Consider MRI/MRA outpatient" → "Obtain outpatient MRI/MRA" (R6)
- Removed "⚠️" emoji from Critical Priorities heading for consistency (R7)
- Updated treatment table column headers to match standardized format (Treatment | Route | Indication | Dosing | ...) (R7)
- Removed redundant labels from Treatment column (e.g., "Blood pressure control:" prefix, "Analgesic:" prefix) (R7)
- Updated version to 1.1; updated STATUS line to "Revised per checker/rebuilder validation (v1.1)" (R8)

**v1.0 (February 2, 2026)**
- Initial template creation
- Comprehensive thunderclap headache evaluation covering the diagnostic algorithm (CT → LP → CTA/MRA), must-exclude diagnoses (SAH, CVT, RCVS, dissection, pituitary apoplexy), cause-specific initial treatments, and disposition criteria
- Structured dosing format for all medications
- Full 12-item differential diagnosis table including SAH, RCVS, CVT, dissection, pituitary apoplexy, hypertensive emergency, meningitis, PRES, ischemic stroke, SIH, and colloid cyst
- Evidence table with PubMed links for all major recommendations

---

## APPENDIX A: THUNDERCLAP HEADACHE DIAGNOSTIC ALGORITHM

```
THUNDERCLAP HEADACHE (peak intensity <60 seconds)
│
├── STEP 1: Immediate CT Head (without contrast)
│   ├── CT POSITIVE (blood seen)
│   │   ├── SAH pattern → STAT CTA → Neurosurgery + Neuro-ICU
│   │   ├── Parenchymal hemorrhage → ICH pathway
│   │   └── Pituitary hemorrhage → MRI sella + Endocrine + Neurosurgery
│   │
│   └── CT NEGATIVE (no blood)
│       ├── STEP 2: CTA Head/Neck (if not already done)
│       │   ├── Aneurysm found → SAH protocol (LP + Neurosurgery)
│       │   ├── Vasoconstriction → RCVS protocol
│       │   ├── Dissection → Antithrombotic + Vascular neurology
│       │   └── Normal → Proceed to LP
│       │
│       └── STEP 3: Lumbar Puncture (≥6h from onset if possible)
│           ├── Xanthochromia PRESENT → SAH → DSA
│           ├── RBCs non-clearing → SAH → DSA
│           ├── Elevated OP + normal CSF → Evaluate for CVT → MRV/CTV
│           ├── Pleocytosis + low glucose → Meningitis workup
│           ├── Normal LP → Obtain MRI/MRA (if not done)
│           │   ├── Vasoconstriction → RCVS
│           │   ├── CVT → Anticoagulation
│           │   ├── Pituitary mass → Apoplexy pathway
│           │   ├── PRES features → BP management
│           │   └── Normal → Primary TCH (dx of exclusion)
│           └── Low OP (<6 cm H2O) → SIH → MRI + CT myelography
```

---

## APPENDIX B: OTTAWA SAH RULE

**Application:** For patients ≥15 years old presenting with acute non-traumatic headache reaching peak intensity within 1 hour.

**High-risk criteria (any ONE = investigate for SAH):**

| Criterion | Description |
|-----------|-------------|
| 1. Age ≥40 | Older age increases SAH risk |
| 2. Neck pain or stiffness | Meningeal irritation from subarachnoid blood |
| 3. Witnessed loss of consciousness | Transient increase in ICP at time of rupture |
| 4. Onset during exertion | Valsalva or physical exertion triggers rupture |
| 5. Thunderclap headache (instant peak) | Classic SAH presentation |
| 6. Limited neck flexion on exam | Meningismus |

**Sensitivity:** 100% (95% CI 97-100%) for SAH in validation study.
**Specificity:** 15% — low specificity means most positives are not SAH, but the rule safely identifies ALL SAH patients.

**Clinical Use:** If ALL six criteria are ABSENT, SAH is extremely unlikely. However, the rule was designed to identify which headache patients need CT — it does NOT replace LP in CT-negative cases with clinical suspicion.

---

## APPENDIX C: CAUSES OF THUNDERCLAP HEADACHE — MUST NOT MISS

| Diagnosis | Frequency | Key Feature | Initial Test |
|-----------|-----------|-------------|--------------|
| Subarachnoid hemorrhage (SAH) | Most common dangerous cause (~10-25% of TCH presentations) | Sudden onset; may have LOC; meningismus | CT head → LP → CTA |
| Reversible cerebral vasoconstriction syndrome (RCVS) | Common; increasingly recognized | RECURRENT thunderclap headaches over days-weeks; triggers (sex, exertion, drugs) | CTA/MRA (may be normal early); clinical + follow-up |
| Cerebral venous thrombosis (CVT) | Uncommon but serious | Risk factors (OCPs, pregnancy); seizures; hemorrhagic infarct | MRV/CTV; D-dimer |
| Cervical artery dissection | Uncommon | Neck pain + ipsilateral headache; Horner syndrome; stroke | CTA neck; MRI neck (fat-sat T1) |
| Pituitary apoplexy | Rare | Visual field cut + ophthalmoplegia + headache; hemodynamic instability | MRI sella; cortisol; hormone panel |
| Bacterial meningitis | Uncommon with TCH onset | Fever; meningismus; rapid deterioration | LP; blood cultures |
| Intracerebral hemorrhage | Common | Focal deficits dominant; blood on CT | CT head |
| Hypertensive emergency | Common | Very high BP; end-organ damage | BP; CT; renal function |
| PRES | Uncommon | Seizures; visual changes; hypertension; posterior edema on MRI | MRI (FLAIR) |
| Ischemic stroke (basilar) | Uncommon with isolated TCH | Rapid deterioration; brainstem signs; vertigo | CT/CTA; MRI DWI |
| Spontaneous intracranial hypotension | Uncommon | Orthostatic component (better supine) | LP (low OP); MRI (pachymeningeal enhancement) |
| Colloid cyst (3rd ventricle) | Rare | Positional TCH; acute hydrocephalus | CT/MRI (foramen of Monro mass) |

---

## APPENDIX D: XANTHOCHROMIA INTERPRETATION GUIDE

| Timing from Headache Onset | CT Sensitivity for SAH | Xanthochromia Development | Clinical Implication |
|----------------------------|----------------------|--------------------------|---------------------|
| <6 hours | ~98-100% | Not yet developed | CT alone may suffice if clearly negative (some guidelines); LP less informative (no xanthochromia yet) |
| 6-12 hours | ~93% | Developing (sensitivity rising) | LP recommended; xanthochromia sensitivity increasing |
| 12 hours - 2 weeks | ~85% at 24h; declines further | Fully developed (>95% sensitivity) | LP most informative; xanthochromia is the key finding |
| >2 weeks | Very low (<50%) | May still be present but declining | LP may still show xanthochromia; MRI FLAIR may detect subacute blood |

**Key Points:**
- Spectrophotometry is more sensitive than visual inspection for xanthochromia
- Protect CSF from light (bilirubin degrades under light → false negative)
- A truly negative LP at ≥12 hours from onset (no xanthochromia by spectrophotometry, no excess RBCs) effectively excludes SAH
- Traumatic tap: RBCs clearing from tube 1 to tube 4 by >25%; xanthochromia absent; ratio of WBC:RBC in CSF similar to peripheral blood
