---
title: "Intracerebral Hemorrhage"
description: "Clinical decision support for intracerebral hemorrhage (ich) diagnosis and management"
version: "1.0"
setting: "HOSP, OPD, ICU"
status: approved
tags:
  - epilepsy
  - cerebrovascular
  - headache
  - neurodegenerative
  - infectious
---

# Intracerebral Hemorrhage

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Intracerebral Hemorrhage (ICH)

**ICD-10:** I61.9 (Nontraumatic intracerebral hemorrhage, unspecified), I61.0 (ICH in hemisphere, subcortical), I61.1 (ICH in hemisphere, cortical), I61.2 (ICH in hemisphere, unspecified), I61.3 (ICH in brain stem), I61.4 (ICH in cerebellum), I61.5 (ICH, intraventricular), I61.6 (ICH, multiple localized), I62.9 (Nontraumatic intracranial hemorrhage, unspecified)

**CPT CODES:** 85025 (CBC with differential), 85610 (PT/INR), 85730 (aPTT), 85384 (Fibrinogen), 80053 (CMP (BMP + LFTs)), 82947 (Blood glucose), 86900 (Type and screen / crossmatch), 84484 (Troponin), 80320 (Blood alcohol level), 80307 (Urine drug screen), 84703 (Pregnancy test (β-hCG)), 80061 (Lipid panel), 83036 (HbA1c), 84443 (TSH), 85652 (ESR), 85379 (D-dimer), 83930 (Serum osmolality), 86235 (ANA), 70450 (CT head without contrast), 70496 (CT angiography (CTA) head), 93000 (ECG (12-lead)), 70553 (MRI brain with and without contrast), 36224 (Conventional cerebral angiography (DSA)), 93306 (Echocardiogram), 95700 (Continuous EEG (cEEG)), 71046 (Chest X-ray), 96365 (Blood pressure reduction: Nicardipine IV), 96374 (Blood pressure reduction: Labetalol IV)

**SYNONYMS:** Intracerebral hemorrhage, ICH, hemorrhagic stroke, brain bleed, cerebral hemorrhage, intraparenchymal hemorrhage, hypertensive hemorrhage, spontaneous ICH, bleeding in the brain, intracerebral bleed, cerebral bleed, hemorrhagic CVA

**SCOPE:** Spontaneous (non-traumatic) intracerebral hemorrhage in adults. Covers acute BP management, anticoagulant reversal, ICH score and prognosis, ICP management, surgical indications, etiology workup, and secondary prevention. Excludes traumatic ICH, subarachnoid hemorrhage (separate template), hemorrhagic transformation of ischemic stroke, and subdural/epidural hematomas.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | - | STAT | Baseline; thrombocytopenia as cause or complication; transfusion needs | Platelets >100,000 (>50,000 minimum for hemostasis) |
| PT/INR (CPT 85610) | STAT | STAT | - | STAT | Warfarin-related ICH requires emergent reversal; coagulopathy assessment | INR <1.4 target (if elevated: REVERSE IMMEDIATELY) |
| aPTT (CPT 85730) | STAT | STAT | - | STAT | Heparin-related ICH; coagulopathy | Normal |
| Fibrinogen (CPT 85384) | STAT | STAT | - | STAT | DIC; consumptive coagulopathy; tPA-related hemorrhage | >150 mg/dL (if <150: give cryoprecipitate) |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | - | STAT | Electrolytes; renal function for contrast/medication; hepatic function for coagulopathy | Normal |
| Blood glucose (CPT 82947) | STAT | STAT | - | STAT | Hyperglycemia worsens ICH outcomes; hypoglycemia mimics stroke | 140-180 mg/dL target |
| Type and screen / crossmatch (CPT 86900) | STAT | STAT | - | STAT | Potential need for blood products, surgery, reversal agents | On file; crossmatch if OR likely |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Neurogenic cardiac injury (stress cardiomyopathy); concurrent ACS | Normal |
| Blood alcohol level (CPT 80320) | STAT | - | - | STAT | Coagulopathy; exam reliability; alcoholism is ICH risk factor | Document result |
| Urine drug screen (CPT 80307) | STAT | - | - | STAT | Cocaine/amphetamine-associated ICH (sympathomimetic surge) | Negative |
| Pregnancy test (β-hCG) (CPT 84703) | STAT | STAT | - | STAT | Affects management (eclampsia differential; imaging) | Document result |
| Thrombin time (TT) and/or ecarin clotting time (ECT) | STAT | STAT | - | STAT | Dabigatran (direct thrombin inhibitor) detection; if patient on DOACs | Normal (prolonged = dabigatran present) |
| Anti-Xa level (calibrated for specific DOAC) | STAT | STAT | - | STAT | Rivaroxaban/apixaban/edoxaban detection; guides reversal need | Negative/undetectable (elevated = DOAC present and active) |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Lipid panel (CPT 80061) | - | ROUTINE | ROUTINE | - | Cardiovascular risk; statin decision (controversial post-ICH) | Document baseline |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Diabetes management | <7.0% |
| TSH (CPT 84443) | - | ROUTINE | - | - | Thyroid dysfunction | Normal |
| ESR (CPT 85652) / CRP (CPT 86140) | - | ROUTINE | ROUTINE | - | Vasculitis screen; inflammatory etiology | Normal |
| D-dimer (CPT 85379) | URGENT | ROUTINE | - | URGENT | DIC; venous thromboembolism | Normal |
| Serum osmolality (CPT 83930) | - | ROUTINE | - | ROUTINE | Monitor during osmotherapy (mannitol/hypertonic saline) | 280-320 mOsm/kg; hold osmotherapy if >320 |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Hypercoagulable panel | - | EXT | EXT | - | Young patient ICH without clear etiology; cerebral venous thrombosis with secondary hemorrhage | Normal |
| ANA (CPT 86235), ANCA | - | EXT | EXT | - | CNS vasculitis-related hemorrhage | Negative |
| Toxicology (expanded) | - | EXT | - | EXT | Sympathomimetic drug use; synthetic drug-associated hemorrhage | Negative |
| Amyloid-beta PET | - | - | EXT | - | Cerebral amyloid angiopathy (CAA) confirmation; research context | Positive amyloid deposition in lobar distribution |
| APOE genotype | - | - | EXT | - | CAA risk stratification; APOE ε2/ε4 associated with ICH | Document alleles |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Door-to-CT <25 minutes; determines ICH diagnosis, location, volume, IVH, hydrocephalus, midline shift | Hemorrhage location (deep: basal ganglia/thalamus = hypertensive; lobar: CAA, tumor, AVM), volume (ABC/2 method), intraventricular hemorrhage (IVH), hydrocephalus, midline shift >5mm | Pregnancy (benefit outweighs risk) |
| CT angiography (CTA) head (CPT 70496) | STAT | STAT | - | STAT | With initial CT; identify "spot sign" (active contrast extravasation = hematoma expansion risk), underlying vascular malformation (AVM, aneurysm) | Spot sign (30-50% risk of expansion); AVM; aneurysm; dural AV fistula; Moyamoya | Contrast allergy; renal impairment (benefit outweighs risk in emergency) |
| ECG (12-lead) (CPT 93000) | STAT | STAT | - | STAT | Baseline; neurogenic cardiac injury; arrhythmia; QTc prolongation risk | Normal; ST changes may be neurogenic | None |
| Repeat CT head (non-contrast) | - | STAT | - | STAT | At 6h and 24h OR any neurologic decline; assess for hematoma expansion (>33% or >6mL increase from baseline = significant expansion) | Stable hematoma size; no new hemorrhage; no hydrocephalus progression | Same as initial |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) (include GRE/SWI sequences) | - | URGENT | ROUTINE | URGENT | Within 24-72h when stable; or urgently if underlying mass/AVM suspected | Underlying tumor; cavernous malformation; microbleeds (CAA pattern: lobar; hypertensive: deep). SWI shows microhemorrhages | Pacemaker; hemodynamic instability; MRI-incompatible monitoring |
| MR venography (MRV) | - | ROUTINE | - | ROUTINE | If cerebral venous thrombosis (CVT) suspected as cause of hemorrhagic venous infarct | Venous sinus thrombosis | Same as MRI |
| Conventional cerebral angiography (DSA) (CPT 36224) | - | URGENT | EXT | URGENT | Young patient (<50) with lobar ICH and no clear etiology; suspected AVM/aneurysm where CTA inconclusive; negative initial CTA but high suspicion | AVM; aneurysm; dural AV fistula; Moyamoya; vasculitis | Contrast allergy; renal impairment; coagulopathy |
| Delayed DSA (if initial negative) | - | - | ROUTINE | - | Repeat at 3-6 months; small AVM may be compressed by acute hematoma and missed initially | Unmasked AVM/aneurysm | Same as initial DSA |
| Echocardiogram (CPT 93306) | - | ROUTINE | - | ROUTINE | Neurogenic cardiac injury; baseline cardiac function; endocarditis if mycotic aneurysm suspected | LV dysfunction; stress cardiomyopathy | None significant |
| Continuous EEG (cEEG) (CPT 95700) | - | URGENT | - | STAT | If altered consciousness disproportionate to hemorrhage size; suspected seizures | Non-convulsive seizures; NCSE (seen in 20-30% of ICH patients) | None |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | Aspiration; pulmonary edema (neurogenic); baseline for ventilator | Normal | None |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Brain biopsy | - | - | EXT | - | If underlying tumor, vasculitis, or amyloid angiopathy suspected and non-invasive workup inconclusive | Tumor; vasculitis; amyloid | Surgical risk |
| Amyloid PET scan | - | - | EXT | - | CAA diagnosis in lobar ICH with microbleeds | Amyloid deposition | Research/limited availability |

---

## 3. TREATMENT

### ⚠️ CRITICAL PRIORITIES IN ACUTE ICH (First 60 Minutes)
1. **ABCs** — airway, breathing, circulation
2. **Blood pressure reduction** — target SBP <140 mmHg within 1 hour (INTERACT2, ATACH-2)
3. **Anticoagulant reversal** — IMMEDIATELY if on anticoagulation
4. **Repeat CT** — assess for expansion

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Blood pressure reduction: Nicardipine IV (CPT 96365) | IV | SBP >150-220; target <140 per INTERACT2/AHA 2022 | 5 mg/h :: IV :: - :: 5 mg/h IV; increase by 2.5 mg/h q5-15min; max 15 mg/h. Target SBP 130-150 mmHg (INTERACT2: <140 safe; AHA 2022: <140 reasonable if presenting SBP 150-220) | Severe aortic stenosis; advanced HF | Continuous arterial line BP; neuro checks with each change; avoid SBP <110 (renal hypoperfusion) | STAT | STAT | - | STAT |
| Blood pressure reduction: Labetalol IV (CPT 96374) | IV | Alternative to nicardipine for BP reduction | 10-20 mg :: IV :: once :: 10-20 mg IV bolus over 1-2 min; may repeat or double q10min; max 300 mg. Alternative to nicardipine | Heart block (2nd/3rd degree); severe bradycardia; decompensated HF; asthma | HR; BP continuous | STAT | STAT | - | STAT |
| Blood pressure reduction: Clevidipine IV (CPT 96365) | IV | Ultra-short-acting alternative for BP control | 1-2 mg/h :: IV :: - :: 1-2 mg/h IV; titrate by doubling q90sec initially; max 32 mg/h | Soy/egg allergy; lipid disorders | BP continuous | STAT | STAT | - | STAT |
| Intubation and airway protection | - | GCS ≤8; airway protection; respiratory failure; impending herniation | N/A :: - :: once :: GCS ≤8; inability to protect airway; respiratory failure; impending herniation. Use non-depolarizing agents; avoid succinylcholine if elevated ICP (relative) | N/A | Ventilator; head of bed 30°; avoid hyperventilation unless herniation | STAT | STAT | - | STAT |
| Warfarin reversal: 4-factor PCC (Kcentra) (CPT 96374) | IV | Warfarin-associated ICH; INR >1.4; emergent reversal | 25-50 units/kg :: IV :: - :: 25-50 units/kg IV (dose based on INR: INR 2-4: 25 u/kg; INR 4-6: 35 u/kg; INR >6: 50 u/kg); infuse over 10-15 min. Reverses INR within 15-30 min. PREFERRED over FFP (faster, smaller volume) | Active DIC (relative); HIT (contains heparin traces) | INR 15 min after infusion; repeat if INR >1.4; thrombotic risk | STAT | STAT | - | STAT |
| Warfarin reversal: Vitamin K (phytonadione) | IV | Sustain INR correction after PCC (PCC is temporary) | 10 mg :: IV :: - :: 10 mg IV slow push (over 10 min) to sustain INR correction (PCC is temporary). ALWAYS give WITH PCC | Known severe allergic reaction (rare) | INR at 6h and 24h; anaphylaxis risk (rare with slow IV) | STAT | STAT | - | STAT |
| Warfarin reversal: FFP (if PCC unavailable) | IV | Warfarin reversal when PCC unavailable; slower alternative | 10-15 mL/kg :: IV :: - :: 10-15 mL/kg IV (typically 2-4 units). Slower than PCC; requires thawing and larger volume | Volume overload; transfusion reactions | INR; volume status | STAT | STAT | - | STAT |
| Dabigatran reversal: Idarucizumab (Praxbind) (CPT 96374) | IV | Dabigatran-associated ICH; specific reversal agent | 5 g :: IV :: - :: 5 g IV (two 2.5g boluses or infusions). Specific reversal agent for dabigatran. Reversal within minutes | None absolute | Thrombin time (TT), aPTT; clinical hemostasis | STAT | STAT | - | STAT |
| Factor Xa inhibitor reversal: Andexanet alfa (Andexxa) (CPT 96365) | IV | Rivaroxaban/apixaban-associated ICH; specific reversal agent | 400 mg :: IV :: once :: For rivaroxaban/apixaban. Low-dose: 400 mg IV bolus then 4 mg/min x 2h (last dose >8h ago). High-dose: 800 mg IV bolus then 8 mg/min x 2h (last dose <8h ago or unknown, or rivaroxaban) | Thrombotic risk (10-15% VTE in trials) | Anti-Xa levels; thrombosis monitoring; arterial line | STAT | STAT | - | STAT |
| Factor Xa inhibitor reversal: 4-factor PCC (if andexanet unavailable) | IV | Factor Xa inhibitor reversal when andexanet unavailable | 50 units/kg :: IV :: - :: 50 units/kg IV. Off-label but supported by guidelines if andexanet not available | Same as PCC | Anti-Xa levels; clinical hemostasis | STAT | STAT | - | STAT |
| Heparin reversal: Protamine sulfate | IV | Heparin-associated ICH; 1 mg per 100 units heparin given | 1 mg :: IV :: - :: 1 mg per 100 units of heparin given in last 2-3h; max 50 mg; give slow IV over 10 min | Fish/protamine allergy | aPTT; BP (hypotension with rapid infusion); anaphylaxis | STAT | STAT | - | STAT |
| Platelet transfusion | IV | Platelets <100K + active bleeding or pre-surgical; NOT routine per PATCH trial | 1 unit :: - :: - :: 1 unit apheresis platelets if platelet count <100,000 AND active bleeding or pre-surgical. For antiplatelet-associated ICH: PATCH trial showed NO benefit from routine platelet transfusion (do NOT transfuse if platelets >100K on antiplatelet therapy) | HIT; ITP (consult hematology) | Platelet count; clinical hemostasis | STAT | STAT | - | STAT |
| Tranexamic acid (TXA) | IV | Hematoma expansion; spot sign positive or early presentation | 1 g :: IV :: - :: 1 g IV over 10 min then 1 g IV over 8h. TICH-2 trial: did NOT reduce mortality but reduced hematoma expansion. Not routine; consider if spot sign positive or early presentation with active expansion | Active DVT/PE; hypercoagulable state | Thrombotic events; clinical hemostasis | STAT | STAT | - | STAT |
| ICP management: Head of bed elevation | - | All ICH patients; optimize venous drainage; reduce ICP | N/A :: - :: continuous :: HOB 30°; head in midline (optimize venous drainage); avoid neck flexion/compression | None | ICP if monitored | STAT | STAT | - | STAT |
| ICP management: Mannitol 20% | IV | Acute herniation; elevated ICP >22 mmHg | 1-1.5 g/kg :: IV :: once :: 1-1.5 g/kg IV bolus for acute herniation; 0.25-0.5 g/kg q4-6h maintenance | Anuria; serum osm >320 | Serum osm q4-6h; osmolar gap; Cr; I/O | STAT | - | - | STAT |
| ICP management: Hypertonic saline 23.4% | IV | Acute herniation; requires central line | 30 mL :: IV :: once :: 30 mL IV bolus via central line over 10-20 min for acute herniation | No central access | Na (target 145-155); osmolality | - | - | - | STAT |
| ICP management: Hypertonic saline 3% | IV | ICP reduction; target Na 145-155 mEq/L | 150-500 mL :: IV :: once :: 150-500 mL bolus or 0.5-1 mL/kg/h infusion; target Na 145-155 | Hypernatremia >160 | Na q4-6h; osmolality | - | - | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Levetiracetam | IV | Seizure treatment (NOT routine prophylaxis — AHA 2022 recommends against routine prophylaxis). Treat if clinical or electrographic seizures | 1000-1500 mg :: IV :: BID :: 1000-1500 mg IV load; then 500-1000 mg IV/PO BID | Severe renal impairment (dose adjust) | Seizure monitoring; cEEG; renal function | STAT | STAT | - | STAT |
| Acetaminophen | IV | Fever (target normothermia <37.5°C; fever worsens ICH outcomes) | 650-1000 mg :: IV :: q6h :: 650-1000 mg PO/IV q6h; max 4g/day | Severe hepatic disease | Temperature q4h; LFTs | STAT | STAT | - | STAT |
| Surface cooling / Arctic Sun | - | Refractory fever (targeted temperature management) | N/A :: - :: per protocol :: Target 36-37°C; avoid shivering (counterproductive) | N/A | Core temperature; shivering assessment (BSAS) | - | - | - | ROUTINE |
| Insulin (regular) | IV | Hyperglycemia (target 140-180 mg/dL) | N/A :: IV :: continuous :: Sliding scale or insulin drip | Hypoglycemia | BG q1h if drip; q6h if sliding scale | STAT | STAT | - | STAT |
| Pantoprazole | IV | GI prophylaxis (Cushing ulcer risk from elevated ICP) | 40 mg :: IV :: daily :: 40 mg IV/PO daily | C. diff risk | GI symptoms | - | ROUTINE | - | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis (start 24-48h after hemorrhage stabilizes; after repeat CT shows stability) | 40 mg :: SC :: daily :: 40 mg SC daily. AHA 2022: intermittent pneumatic compression devices on admission; pharmacologic prophylaxis after hemorrhage stable on repeat imaging | Active hemorrhagic expansion; within 24h of ICH onset; pre-surgical | Platelet count; repeat CT before starting | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | DVT prophylaxis (start IMMEDIATELY) | N/A :: - :: continuous :: Apply bilaterally on admission; ICH patients are HIGH VTE risk | Acute DVT | Skin checks | STAT | STAT | - | STAT |
| Ondansetron | IV | Nausea/vomiting (posterior fossa hemorrhage; elevated ICP) | 4 mg :: IV :: q6h :: 4 mg IV q6h PRN | QT prolongation | QTc | STAT | ROUTINE | - | STAT |

### 3C. Surgical Interventions

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| External ventricular drain (EVD) | - | IVH with acute hydrocephalus; GCS declining; need for ICP monitoring | N/A :: - :: once :: Neurosurgery places; allows CSF drainage and ICP monitoring; target ICP <22, CPP >60 | Coagulopathy (correct first); futile care | - | - | - | - | - |
| Intraventricular tPA via EVD | - | IVH with hydrocephalus (CLEAR III trial: reduced mortality in severe IVH but did NOT improve functional outcome) | 1 mg :: - :: q8h :: Alteplase 1 mg q8h via EVD; up to 12 doses; clamp EVD 1h after dosing then open to drain | Active systemic bleeding; coagulopathy | - | - | - | - | - |
| Surgical hematoma evacuation (craniotomy) | - | Lobar ICH >30 mL with deterioration; cerebellar hemorrhage >3 cm OR with brainstem compression/hydrocephalus (STRONGEST surgical indication). STICH/STICH-II: no clear benefit for supratentorial deep ICH | N/A :: - :: once :: Craniotomy or craniectomy for clot evacuation | Deep ICH (generally no benefit from open surgery); GCS 3-4 without brainstem reflexes (futile); severe coagulopathy | - | - | - | - | - |
| Minimally invasive surgery (MIS) — endoscopic or stereotactic aspiration | - | Supratentorial ICH >30 mL with stable or mild deficits (MISTIE III, ENRICH trials: emerging data; ENRICH showed benefit for lobar ICH) | N/A :: - :: once :: Stereotactic catheter-based aspiration or endoscopic evacuation with lower morbidity than craniotomy | Deep location (relative); coagulopathy | - | - | - | - | - |
| Decompressive craniectomy | - | Massive ICH with refractory elevated ICP; malignant cerebellar edema | N/A :: - :: once :: Bone flap removal to allow brain expansion | Futile prognosis; bilateral fixed dilated pupils | - | - | - | - | - |
| Suboccipital decompressive craniectomy | - | Cerebellar hemorrhage with brainstem compression | N/A :: - :: once :: Posterior fossa decompression; life-saving for cerebellar ICH with brainstem compression | Moribund patient | - | - | - | - | - |

### 3D. Secondary Prevention (After Acute Phase)

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Antihypertensive therapy (long-term) | PO | ALL ICH patients; BP is most important modifiable risk factor | N/A :: PO :: per protocol :: Target SBP <130 mmHg (SPS3 trial, PROGRESS trial); agent choice per comorbidities (ACE-I, ARB, CCB, thiazide) | - | - | Home BP monitoring; clinic BP | - | - | - | - |
| Statin (controversial post-ICH) | PO | Risk-benefit discussion; SPARCL showed small increased ICH risk with atorvastatin but overall cardiovascular benefit. AHA 2022: statin not contraindicated after ICH | N/A :: PO :: per protocol :: Per cardiovascular risk; individualize | - | - | Lipid panel | - | - | - | - |
| Anticoagulation restart (if AF or mechanical valve) | PO | Most controversial decision. AHA 2022: may restart anticoagulation at 4-8 weeks for patients with strong indication (AF with high CHA2DS2-VASc). Avoid in CAA-related lobar ICH if possible | N/A :: PO :: per protocol :: Apixaban preferred (APACHE-AF trial: lowest ICH recurrence). Timing: 4-8 weeks; individualized risk-benefit | - | - | Imaging stability; bleeding risk; CHA2DS2-VASc vs HAS-BLED | - | - | - | - |
| Antiplatelet restart | PO | RESTART trial: restarting antiplatelet after ICH is associated with LOWER risk of recurrent ICH; may restart at 2-4 weeks for patients with cardiovascular indication | 81 mg :: PO :: daily :: Aspirin 81 mg or clopidogrel 75 mg daily | - | - | Bleeding signs | - | - | - | - |
| Left atrial appendage occlusion (LAAO/Watchman) | Procedure | AF patients who cannot tolerate long-term anticoagulation post-ICH (lobar ICH, CAA) | N/A :: Procedure :: per protocol :: Interventional cardiology procedure; eliminates need for long-term anticoagulation in AF | - | - | Procedural risks | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurosurgery | STAT | STAT | - | STAT | ALL ICH patients; surgical decision for EVD, hematoma evacuation, decompression |
| Neurology / Neurocritical care | STAT | STAT | - | STAT | Medical management; BP optimization; ICP management; seizure management |
| Hematology | STAT | STAT | - | STAT | Anticoagulant reversal guidance; coagulopathy management; thrombocytopenia |
| Pharmacy (clinical pharmacist) | STAT | STAT | - | STAT | Reversal agent dosing; anticoagulant identification; drug interactions |
| Cardiology | - | ROUTINE | ROUTINE | ROUTINE | AF management; anticoagulation restart decision; LAAO evaluation; neurogenic cardiac injury |
| Speech-language pathology (SLP) | - | URGENT | ROUTINE | URGENT | Dysphagia screening before PO intake; aphasia assessment |
| Physical therapy (PT) | - | URGENT | ROUTINE | URGENT | Early mobilization (24-48h if stable); fall prevention; strength |
| Occupational therapy (OT) | - | URGENT | ROUTINE | URGENT | ADL assessment; cognitive rehabilitation; adaptive equipment |
| Rehabilitation medicine (physiatry) | - | ROUTINE | ROUTINE | - | Rehabilitation disposition; functional prognosis |
| Social work | - | ROUTINE | ROUTINE | - | Family support; advance directives; discharge planning |
| Palliative care | - | ROUTINE | - | ROUTINE | Goals of care discussion (especially ICH score ≥3); early palliative involvement improves care quality |
| Interventional neuroradiology | - | ROUTINE | - | ROUTINE | AVM/aneurysm treatment planning; dural AV fistula |

### 4B. Patient / Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| ICH is serious but outcomes vary; early aggressive treatment improves survival | STAT | ROUTINE | ROUTINE |
| Call 911 if: sudden headache, new weakness, speech changes, altered consciousness | - | ROUTINE | ROUTINE |
| Blood pressure control is the MOST IMPORTANT factor in preventing recurrence | - | ROUTINE | ROUTINE |
| Take all medications as prescribed; never stop blood pressure medications without physician guidance | - | ROUTINE | ROUTINE |
| Do NOT restart anticoagulation or antiplatelet without specific neurology/cardiology guidance | - | ROUTINE | ROUTINE |
| Home blood pressure monitoring daily; keep log; target per physician guidance | - | ROUTINE | ROUTINE |
| Follow-up with neurology in 2-4 weeks; neurosurgery if applicable | - | ROUTINE | ROUTINE |
| Do NOT drive until cleared | - | ROUTINE | ROUTINE |
| Fall prevention at home | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Blood pressure target <130/80 mmHg (most important) | - | ROUTINE | ROUTINE |
| Smoking cessation (doubles ICH risk) | - | ROUTINE | ROUTINE |
| Alcohol cessation or limitation (heavy drinking increases ICH risk) | - | ROUTINE | ROUTINE |
| Cocaine/amphetamine cessation (sympathomimetic ICH) | - | ROUTINE | ROUTINE |
| Avoid excessive anticoagulation (keep INR in range if on warfarin) | - | ROUTINE | ROUTINE |
| Regular exercise (moderate intensity after recovery) | - | - | ROUTINE |
| Weight management | - | ROUTINE | ROUTINE |
| DASH or Mediterranean diet | - | ROUTINE | ROUTINE |
| Depression screening (PHQ-9 at 1-3 months) | - | - | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Hemorrhagic transformation of ischemic stroke | Prior ischemic infarct on imaging; onset timing suggests ischemic → hemorrhagic evolution | CT/MRI timing; DWI changes preceding hemorrhage |
| Cerebral venous thrombosis (CVT) with hemorrhagic infarct | Headache, seizures, often young women (OCPs, pregnancy); hemorrhage doesn't respect arterial territory; parasagittal location | MRV/CT venography (thrombosed sinus); D-dimer |
| Brain tumor with hemorrhage | Subacute symptoms preceding hemorrhage; ring enhancement around hemorrhage; disproportionate edema | MRI with contrast (underlying enhancing mass); biopsy |
| Cerebral amyloid angiopathy (CAA) | Lobar location (NOT deep); age >55; recurrent lobar hemorrhages; cortical superficial siderosis; multiple lobar microbleeds on SWI | MRI SWI (lobar microbleeds, superficial siderosis); Boston criteria |
| Vascular malformation (AVM, cavernoma) | Younger patient; recurrent hemorrhages at same location; AVM on CTA/DSA; cavernoma on MRI (popcorn appearance) | CTA; DSA; MRI (especially SWI) |
| Ruptured aneurysm extending into parenchyma | Subarachnoid + intraparenchymal hemorrhage; near aneurysm location | CTA (aneurysm); DSA |
| Hypertensive ICH | Deep location (putamen, thalamus, pons, cerebellum); history of poorly controlled HTN | Clinical; typical location; no underlying lesion on workup |
| Moyamoya disease | Young adults or Asian patients; recurrent stroke; stenotic proximal vessels with collateral network | MRA (ICA/MCA stenosis with Moyamoya collaterals); DSA |
| Coagulopathy-related ICH | Multiple hemorrhages; known coagulopathy or anticoagulant use | Coagulation panel; medication history |
| Mycotic aneurysm | Endocarditis; distal vessel location; fever | Blood cultures; echocardiogram; CTA/DSA |
| Trauma | History of trauma; scalp laceration; subdural or epidural components | Clinical history; CT pattern |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Blood pressure (arterial line preferred in ICU) | STAT | STAT | ROUTINE | STAT | q5min x 2h during acute reduction; q15min x 6h; then q1h x 24h; then q4h | SBP 130-150 (acute); <130/80 (chronic) | Titrate antihypertensives; avoid SBP <110 |
| GCS / Neurologic exam | STAT | STAT | ROUTINE | STAT | q1h x 24h, then q2h x 24h, then q4h | Stable or improving GCS | If declining: STAT CT; ICP assessment; neurosurgery |
| ICP (if EVD in place) | - | - | - | STAT | Continuous; assess q1h | ICP <22 mmHg; CPP 60-70 mmHg | Tiered ICP management: drain CSF → osmotherapy → sedation → hypothermia → decompression |
| Repeat CT head | - | STAT | - | STAT | At 6h (routine); at 24h; and with ANY neurologic decline | Stable hematoma; no expansion (>33% or >6mL = expansion) | If expanding: re-evaluate BP; reversal; surgical consultation |
| Temperature | STAT | STAT | - | STAT | q4h; q1h if febrile | <37.5°C (normothermia) | Aggressive fever management; cooling devices; infection workup |
| Blood glucose | STAT | STAT | - | STAT | q6h (q1h if insulin drip) | 140-180 mg/dL | Insulin; avoid <60 |
| Serum sodium | - | ROUTINE | - | STAT | q6h during osmotherapy; q12h otherwise | 135-155 (higher range with osmotherapy) | Adjust osmotherapy |
| Serum osmolality | - | ROUTINE | - | STAT | q6h during mannitol | <320 mOsm/kg; osmolar gap <10 | Hold mannitol if >320 |
| INR (if on warfarin) | STAT | ROUTINE | - | STAT | 15 min after PCC; then q6h x 24h; then daily | INR <1.4 | Additional reversal agents |
| Hemoglobin | STAT | ROUTINE | - | ROUTINE | q6-12h x 48h | >7 g/dL (>10 if active bleeding or coronary disease) | Transfuse PRBCs |
| EEG / Seizure monitoring | - | URGENT | - | STAT | cEEG 24-48h minimum if altered consciousness | No seizure activity | AED loading; aggressive management |
| Swallowing screen | - | STAT | - | URGENT | Before any PO intake | Pass screening | NPO; SLP evaluation |
| ICH Score (calculate at admission) | STAT | - | - | STAT | Once (prognostic) | Lower is better | Goals of care discussion if score ≥3 |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Small ICH; stable exam; GCS 15; ambulatory; adequate home support; medications filled; BP controlled; follow-up arranged |
| Admit to stroke unit/floor (monitored) | Small-moderate ICH; GCS 13-15; no surgical indication; stable repeat CT; BP controlled on oral/IV medications |
| Admit to neuro-ICU | ALL moderate-large ICH; GCS <13 or declining; anticoagulant-related ICH; posterior fossa ICH; IVH with hydrocephalus; EVD in place; requiring arterial line and IV antihypertensives; post-surgical |
| Emergent surgery | Cerebellar ICH >3 cm with brainstem compression or hydrocephalus; deteriorating lobar ICH >30 mL; obstructive hydrocephalus needing EVD |
| Transfer to higher level | Need for neurosurgery not available; need for neuro-ICU; need for reversal agents not available; need for endovascular treatment |
| Inpatient rehabilitation | Significant deficits but able to participate in 3h/day therapy; medically stable |
| Comfort care / Hospice | ICH score ≥4; devastating ICH with poor prognosis after family goals of care discussion |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| SBP target <140 mmHg in acute ICH (presenting SBP 150-220) | Class I, Level A | INTERACT2 ([Anderson et al. NEJM 2013](https://pubmed.ncbi.nlm.nih.gov/23713578/)); AHA/ASA 2022 Guidelines |
| Intensive BP lowering safe but benefit on functional outcome modest | Class IIa, Level A | ATACH-2 ([Qureshi et al. NEJM 2016](https://pubmed.ncbi.nlm.nih.gov/27276234/)) — <140 vs <180 safe; no functional difference |
| 4-factor PCC preferred over FFP for warfarin reversal | Class I, Level B | INCH trial ([Steiner et al. Lancet Neurol 2016](https://pubmed.ncbi.nlm.nih.gov/27647638/)) |
| Idarucizumab for dabigatran reversal | Class I, Level B | RE-VERSE AD trial ([Pollack et al. NEJM 2017](https://pubmed.ncbi.nlm.nih.gov/28693366/)) |
| Andexanet alfa for factor Xa inhibitor reversal | Class IIa, Level B | ANNEXA-4 ([Connolly et al. NEJM 2019](https://pubmed.ncbi.nlm.nih.gov/30730782/)) |
| Platelet transfusion NOT beneficial for antiplatelet-associated ICH | Class III (No Benefit) | PATCH trial ([Baharoglu et al. Lancet 2016](https://pubmed.ncbi.nlm.nih.gov/27178479/)) |
| TXA reduces expansion but NOT mortality | Class IIb, Level B | TICH-2 ([Sprigg et al. Lancet 2018](https://pubmed.ncbi.nlm.nih.gov/29778325/)) |
| Surgical evacuation for cerebellar ICH with deterioration | Class I, Level B | AHA/ASA Guidelines; strong consensus |
| No benefit from routine supratentorial open surgery | Class III (No Benefit) | STICH ([Mendelow et al. Lancet 2005](https://pubmed.ncbi.nlm.nih.gov/15680453/)); STICH II (2013) |
| Minimally invasive surgery emerging benefit | Class IIb, Level B | MISTIE III ([Hanley et al. Lancet 2019](https://pubmed.ncbi.nlm.nih.gov/30739747/)); ENRICH (2024) |
| EVD for IVH with hydrocephalus | Class I, Level B | AHA/ASA Guidelines |
| Intraventricular tPA (CLEAR III) | Class IIb, Level B | [Hanley et al. (Lancet 2017)](https://pubmed.ncbi.nlm.nih.gov/28081952/) — reduced mortality but not functional outcome |
| Seizure prophylaxis NOT recommended routinely | Class III (No Benefit) | AHA/ASA 2022 — treat clinical/electrographic seizures; cEEG if altered |
| Anticoagulation restart 4-8 weeks for AF | Class IIb, Level B | AHA/ASA 2022; observational data |
| Antiplatelet restart appears safe (RESTART trial) | Class IIa, Level B | [RESTART trial (Lancet 2019)](https://pubmed.ncbi.nlm.nih.gov/31128924/) |
| DVT prophylaxis: pneumatic devices immediately; pharmacologic at 24-48h | Class I, Level B | AHA/ASA 2022 Guidelines |
| ICH Score for prognosis | Class IIa, Level B | [Hemphill et al. (Stroke 2001)](https://pubmed.ncbi.nlm.nih.gov/11283388/) |
| Normothermia improves outcomes | Class I, Level C | AHA/ASA Guidelines |
| Avoid self-fulfilling prophecy (DNR discussion timing) | Class I, Level C | AHA/ASA 2022: delay new DNR orders until at least 24h after admission |

---

**APPENDIX: ICH SCORE (PROGNOSIS)**

| Component | Points |
|-----------|--------|
| GCS 3-4 | 2 |
| GCS 5-12 | 1 |
| GCS 13-15 | 0 |
| ICH volume ≥30 mL | 1 |
| ICH volume <30 mL | 0 |
| IVH present | 1 |
| IVH absent | 0 |
| Infratentorial origin | 1 |
| Supratentorial origin | 0 |
| Age ≥80 | 1 |
| Age <80 | 0 |

| ICH Score | 30-Day Mortality |
|-----------|-----------------|
| 0 | 0% |
| 1 | 13% |
| 2 | 26% |
| 3 | 72% |
| 4 | 97% |
| 5 | 100% |

**APPENDIX: ABC/2 METHOD FOR ICH VOLUME**

Volume (mL) = (A × B × C) / 2
- A = largest diameter on slice with largest hemorrhage (cm)
- B = diameter perpendicular to A on same slice (cm)
- C = number of CT slices with hemorrhage × slice thickness (cm)

**APPENDIX: ANTICOAGULANT REVERSAL QUICK REFERENCE**

| Agent | Reversal | Dose | Onset |
|-------|----------|------|-------|
| Warfarin | 4-factor PCC + Vitamin K 10mg IV | Per INR (25-50 u/kg) | 15-30 min |
| Dabigatran | Idarucizumab (Praxbind) | 5g IV | Minutes |
| Rivaroxaban/Apixaban | Andexanet alfa (Andexxa) OR 4-factor PCC 50 u/kg | Per dosing protocol | 15-30 min |
| Edoxaban | Andexanet alfa OR 4-factor PCC 50 u/kg | Per protocol | 15-30 min |
| UFH | Protamine sulfate | 1mg per 100u heparin | Minutes |
| LMWH | Protamine sulfate (60% reversal) | 1mg per 1mg enoxaparin (within 8h) | Partial |
