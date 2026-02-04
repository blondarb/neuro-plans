---
title: "Acute Ischemic Stroke"
description: "Clinical decision support for acute ischemic stroke diagnosis and management"
version: "1.0"
setting: "HOSP, OPD, ICU"
status: approved
---

# Acute Ischemic Stroke

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Acute Ischemic Stroke

**ICD-10:** I63.9 (Cerebral infarction, unspecified), I63.50 (Cerebral infarction due to unspecified occlusion or stenosis of unspecified cerebral artery), I63.30 (Cerebral infarction due to thrombosis of unspecified cerebral artery), I63.40 (Cerebral infarction due to embolism of unspecified cerebral artery), G45.9 (Transient cerebral ischemic attack, unspecified)

**SYNONYMS:** Acute ischemic stroke, AIS, stroke, brain attack, cerebral infarction, CVA, cerebrovascular accident, thrombotic stroke, embolic stroke, ischemic CVA, ischemic stroke, code stroke

**SCOPE:** Acute ischemic stroke in adults — covers initial stabilization, thrombolytic therapy (IV alteplase/tenecteplase), endovascular thrombectomy criteria, blood pressure management, stroke etiology workup, secondary prevention initiation, and early rehabilitation. Excludes hemorrhagic stroke (see Intracerebral Hemorrhage template), transient ischemic attack (see TIA template), pediatric stroke, and chronic post-stroke management.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Point-of-care glucose (CPT 82962) | STAT | STAT | - | STAT | Hypoglycemia mimics stroke; must rule out before tPA | >60 mg/dL |
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; thrombocytopenia contraindicates tPA if <100K | Platelets >100,000 |
| BMP (Na, K, Cr, glucose, BUN) (CPT 80048) | STAT | STAT | ROUTINE | STAT | Electrolyte abnormalities, renal function for contrast/medication dosing | Normal |
| PT/INR (CPT 85610) | STAT | STAT | - | STAT | Anticoagulant use; INR >1.7 contraindicates tPA | INR ≤1.7 for tPA eligibility |
| aPTT (CPT 85730) | STAT | STAT | - | STAT | Heparin use; elevated aPTT contraindicates tPA | Normal range |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Acute MI can cause cardioembolic stroke; stress cardiomyopathy | Normal |
| Type and screen (CPT 86900) | STAT | ROUTINE | - | STAT | Potential need for blood products, surgical intervention | On file |
| Lipid panel (fasting or non-fasting) (CPT 80061) | - | ROUTINE | ROUTINE | - | Baseline for statin therapy; cardiovascular risk assessment | LDL target <70 mg/dL |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Diabetes screening/management; cardiovascular risk factor | <7.0% (individualized) |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Hepatic function panel (AST, ALT, albumin) (CPT 80076) | URGENT | ROUTINE | ROUTINE | URGENT | Liver disease affects anticoagulation, medication metabolism | Normal |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Thyroid dysfunction as cardiovascular risk factor; atrial fibrillation workup | Normal |
| ESR (CPT 85652) / CRP (CPT 86140) | - | ROUTINE | ROUTINE | - | Vasculitis screen, inflammatory stroke etiology | Normal |
| Urine drug screen (CPT 80307) | URGENT | ROUTINE | - | URGENT | Cocaine/amphetamine-associated vasospasm or stroke | Negative |
| Pregnancy test (β-hCG) (CPT 84703) | STAT | STAT | ROUTINE | STAT | Affects treatment decisions (tPA risk-benefit), imaging choices | Negative |
| Blood alcohol level (CPT 80320) | URGENT | - | - | URGENT | Intoxication as stroke mimic; affects exam reliability | Correlate with clinical picture |
| Magnesium (CPT 83735) | URGENT | ROUTINE | ROUTINE | URGENT | Hypomagnesemia associated with arrhythmia, vascular risk | Normal (>1.8 mg/dL) |
| Phosphorus (CPT 84100) | - | ROUTINE | ROUTINE | - | Refeeding risk if malnourished; metabolic panel | Normal |
| Prealbumin | - | ROUTINE | - | ROUTINE | Nutritional status for rehabilitation planning | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Hypercoagulable panel (protein C, protein S, antithrombin III, Factor V Leiden, prothrombin gene mutation) | - | EXT | EXT | - | Young stroke (<50), cryptogenic stroke, venous thrombosis history | Normal |
| Antiphospholipid antibody panel (lupus anticoagulant, anticardiolipin, β2-glycoprotein I) | - | EXT | EXT | - | Young stroke, recurrent stroke, systemic lupus | Negative |
| Homocysteine (CPT 83090) | - | ROUTINE | ROUTINE | - | Elevated homocysteine as independent stroke risk factor | Normal (<15 µmol/L) |
| RPR/VDRL (CPT 86592) | - | ROUTINE | ROUTINE | - | Syphilitic vasculitis | Negative |
| HIV (CPT 87389) | - | ROUTINE | ROUTINE | - | HIV-associated vasculopathy | Negative |
| ANA (CPT 86235), dsDNA | - | EXT | EXT | - | Lupus cerebritis, vasculitis | Negative |
| ANCA (c-ANCA, p-ANCA) | - | EXT | EXT | - | CNS vasculitis | Negative |
| Complement levels (C3, C4) | - | EXT | EXT | - | Complement-mediated vasculitis | Normal |
| Hemoglobin electrophoresis | - | EXT | EXT | - | Sickle cell disease (young patients, African descent) | Normal (HbAA) |
| JAK2 mutation | - | EXT | EXT | - | Polycythemia vera, myeloproliferative disorders | Negative |
| Fibrinogen (CPT 85384) | URGENT | ROUTINE | - | URGENT | DIC screen, coagulopathy evaluation | Normal (200-400 mg/dL) |
| D-dimer (CPT 85379) | URGENT | ROUTINE | - | URGENT | DIC, paradoxical embolism through PFO, cancer-associated | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Door-to-CT <25 minutes | Exclude hemorrhage; may show early ischemic changes (loss of gray-white differentiation, sulcal effacement) | Pregnancy (relative) |
| CT angiography head and neck (CTA) (CPT 70496, 70498) | STAT | STAT | - | STAT | With initial CT; door-to-CTA <25 min | Large vessel occlusion (LVO) for thrombectomy; carotid/vertebral stenosis or dissection | Contrast allergy (premedicate), eGFR <30 (benefit outweighs risk in acute setting) |
| CT perfusion (CTP) (CPT 0042T) | STAT | URGENT | - | STAT | With CTA if extended window (6-24h) or wake-up stroke | Ischemic penumbra (mismatch between core infarct and hypoperfused tissue); target mismatch ratio >1.8 | Same as CTA |
| MRI brain with DWI (diffusion-weighted imaging) (CPT 70553) | URGENT | URGENT | ROUTINE | URGENT | Within 24h; STAT if diagnosis uncertain | Acute ischemic infarct (restricted diffusion); stroke location and extent; ASPECTS scoring | Pacemaker, metallic implants, severe claustrophobia |
| ECG (12-lead) (CPT 93000) | STAT | STAT | ROUTINE | STAT | Immediate | Atrial fibrillation, acute MI, LVH, ST changes | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRA head and neck (CPT 70544, 70547) | - | URGENT | ROUTINE | URGENT | Within 24-48h | Intracranial stenosis, vertebrobasilar disease, dissection | Same as MRI |
| Transthoracic echocardiogram (TTE) (CPT 93306) | - | ROUTINE | ROUTINE | ROUTINE | Within 24-48h | LV thrombus, PFO, valvular disease, cardiomyopathy, akinetic segments | None significant |
| Transesophageal echocardiogram (TEE) (CPT 93312) with bubble study | - | ROUTINE | ROUTINE | - | Within 48-72h if TTE nondiagnostic or cryptogenic stroke | PFO with right-to-left shunt, atrial septal aneurysm, left atrial appendage thrombus, aortic arch atheroma | Esophageal pathology, uncooperative patient |
| Carotid duplex ultrasound (CPT 93880) | - | ROUTINE | ROUTINE | - | Within 24-48h | Carotid stenosis ≥50%, plaque characterization | None significant |
| Transcranial Doppler (TCD) (CPT 93886) | - | ROUTINE | ROUTINE | - | Within 24-48h | Intracranial stenosis, vasospasm, microembolic signals, right-to-left shunt (bubble study) | Absent temporal bone window (~10% patients) |
| Continuous cardiac telemetry (CPT 93228) | STAT | STAT | - | STAT | Minimum 24h; ideally ≥48-72h | Paroxysmal atrial fibrillation, other arrhythmias | None |
| Extended cardiac monitoring (Holter 30-day or implantable loop recorder) | - | ROUTINE | ROUTINE | - | Arrange before discharge if cryptogenic stroke | Paroxysmal atrial fibrillation (detected in 12-30% with prolonged monitoring) | None significant |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | Within 24h | Cardiomegaly, pulmonary edema, aspiration pneumonia | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Conventional cerebral angiography (DSA) (CPT 36224) | - | EXT | EXT | EXT | If vasculitis, dissection, or Moyamoya suspected | Beading pattern (vasculitis), intimal flap (dissection), Moyamoya collaterals | Contrast allergy, severe renal impairment, coagulopathy |
| MRI vessel wall imaging | - | EXT | EXT | - | If intracranial stenosis or vasculitis suspected | Vessel wall enhancement (vasculitis, unstable plaque), dissection | Same as MRI |
| Fat-saturated MRI neck | - | EXT | EXT | - | If cervical dissection suspected | Intramural hematoma (crescent sign) | Same as MRI |
| Cardiac MRI | - | EXT | EXT | - | If cardiomyopathy or cardiac mass suspected | Myocardial fibrosis, thrombus, tumor | Same as MRI |
| PET-CT | - | - | EXT | - | If occult malignancy suspected (Trousseau syndrome) | Occult cancer, hypercoagulable etiology | Pregnancy, uncontrolled diabetes |

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IV alteplase (tPA) (CPT 96365) | IV | - | 0.9 mg/kg :: IV :: once :: 0.9 mg/kg IV (max 90 mg); 10% as bolus over 1 min, remaining 90% infused over 60 min. Door-to-needle target <45 min | >4.5h from last known well (relative 3-4.5h window with additional exclusions); BP >185/110 despite treatment; platelets <100K; INR >1.7; active bleeding; recent surgery <14 days; recent stroke <3 months; intracranial hemorrhage history | Neuro checks q15min during infusion, q30min x 6h, then q1h x 18h; BP q15min x 2h, q30min x 6h, then q1h; hold anticoagulants/antiplatelets 24h | STAT | STAT | - | STAT |
| Tenecteplase IV (CPT 96374) (if available) | IV | - | 0.25 mg/kg :: IV :: once :: 0.25 mg/kg IV single bolus (max 25 mg); preferred if LVO planned for thrombectomy | Same as alteplase | Same as alteplase | STAT | STAT | - | STAT |
| Endovascular thrombectomy | - | - | N/A :: - :: once :: For LVO (ICA, M1, M1-M2 junction, basilar); within 24h if eligible per DAWN/DEFUSE-3 criteria. 0-6h: NIHSS ≥6, ASPECTS ≥6. 6-24h: clinical-core mismatch on perfusion imaging | Large established infarct core (ASPECTS <6 in 0-6h window); no LVO; poor premorbid function (mRS >2 relative); life expectancy <6 months | Continuous monitoring in neuro-ICU post-procedure; groin check; BP per post-thrombectomy protocol | STAT | STAT | - | STAT |
| Aspirin | PO | - | 325 mg :: PO :: daily :: 325 mg PO/PR load (give within 24-48h of onset); if tPA given, wait 24h and obtain CT before starting. Maintenance: 81-325 mg daily | Active GI bleed, true aspirin allergy, within 24h of tPA (wait for post-tPA CT) | GI symptoms, bleeding signs | STAT | STAT | - | STAT |
| Blood pressure management PRE-tPA: Labetalol IV (CPT 96374) | IV | - | 10-20 mg :: IV :: once :: 10-20 mg IV over 1-2 min; may repeat once; target BP <185/110 before tPA | Heart block (2nd/3rd degree), severe bradycardia, decompensated HF, asthma/severe COPD | Heart rate, BP continuous | STAT | STAT | - | STAT |
| Blood pressure management PRE-tPA: Nicardipine IV (CPT 96365) | IV | - | 5 mg/h :: IV :: - :: 5 mg/h IV infusion; increase by 2.5 mg/h q5-15min; max 15 mg/h; target BP <185/110 | Severe aortic stenosis | BP continuous monitoring | STAT | STAT | - | STAT |
| Blood pressure management PRE-tPA: Clevidipine IV (CPT 96365) | IV | - | 1-2 mg/h :: IV :: - :: 1-2 mg/h IV; titrate by doubling q90sec initially; max 32 mg/h | Soy/egg allergy, severe lipid disorders, defective lipid metabolism | BP continuous monitoring | STAT | STAT | - | STAT |
| Blood pressure management POST-tPA (24h) | IV | - | N/A :: IV :: continuous :: Target BP <180/105 x 24h post-tPA; use nicardipine or labetalol drip as above | See individual agents above | Neuro checks with each BP check; hold if SBP <100 | - | STAT | - | STAT |
| Permissive hypertension (no tPA given) | - | - | 15% :: - :: - :: Allow BP up to 220/120; treat only if >220/120 or end-organ damage (ACS, aortic dissection, hypertensive encephalopathy). Lower by 15% in first 24h | N/A | Neuro checks; avoid precipitous drops | STAT | STAT | - | STAT |
| IV normal saline | IV | - | N/A :: IV :: per protocol :: Isotonic fluids; avoid dextrose-containing solutions (hyperglycemia worsens outcomes); avoid hypotonic solutions (cerebral edema risk) | Volume overload | I/O, electrolytes | STAT | STAT | - | STAT |
| Supplemental oxygen | - | - | 94% :: - :: - :: Only if SpO2 <94%; nasal cannula or mask as needed | N/A | SpO2 target ≥94%; avoid routine supplemental O2 if normoxic | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Acetaminophen | PO | Fever (temp >38°C worsens outcomes) | 650-1000 mg :: PO :: q6h :: 650-1000 mg PO/PR q6h; max 4g/day (2g if hepatic impairment) | Severe hepatic disease | Temperature q4h; LFTs if prolonged use | STAT | STAT | - | STAT |
| Insulin (regular) | IV | Hyperglycemia (glucose >180 worsens outcomes) | 140-180 mg :: IV :: - :: Sliding scale or insulin drip for persistent hyperglycemia; target glucose 140-180 mg/dL; avoid hypoglycemia (<60 mg/dL) | Hypoglycemia risk | BG q1h if drip; q6h if sliding scale | STAT | STAT | - | STAT |
| Ondansetron | IV | Nausea/vomiting (posterior circulation stroke) | 4 mg :: IV :: q6h :: 4 mg IV/PO q6h PRN | QT prolongation, serotonin syndrome risk | QTc if risk factors | URGENT | ROUTINE | ROUTINE | URGENT |
| Enoxaparin | SC | DVT prophylaxis | 40 mg :: SC :: daily :: 40 mg SC daily; start within 24-48h if not receiving therapeutic anticoagulation; after post-tPA imaging clears hemorrhage | Active bleeding, platelets <50K, CrCl <30 (use UFH 5000u SC q8-12h) | Platelets q3 days; renal function | - | ROUTINE | - | ROUTINE |
| Heparin (unfractionated) SC | SC | DVT prophylaxis (alternative) | 5000 units :: SC :: - :: 5000 units SC q8-12h | Active bleeding, HIT | Platelets q3 days | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | DVT prophylaxis (non-pharmacologic) | N/A :: - :: continuous :: Apply to both legs immediately on admission; use in addition to or instead of pharmacologic prophylaxis | Acute DVT, severe peripheral vascular disease | Skin checks daily | STAT | STAT | - | STAT |
| Pantoprazole | IV | GI prophylaxis (stress ulcer) | 40 mg :: IV :: daily :: 40 mg IV/PO daily | C. difficile risk with prolonged use | GI symptoms | - | ROUTINE | - | ROUTINE |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Dual antiplatelet therapy (DAPT): Aspirin + Clopidogrel | - | - | 81 mg :: - :: daily :: Aspirin 81 mg + Clopidogrel 75 mg daily x 21 days (minor stroke NIHSS ≤3 or high-risk TIA ABCD2 ≥4); then single antiplatelet long-term. Load clopidogrel 300 mg if not previously on it | Major stroke (NIHSS >3), high bleeding risk, planned surgery | Bleeding signs; CBC | - | URGENT | URGENT | - |
| Dual antiplatelet therapy: Aspirin + Ticagrelor | PO | - | 81 mg :: PO :: daily :: Aspirin 81 mg daily + Ticagrelor 90 mg BID x 30 days (THALES trial: minor stroke NIHSS ≤5); then single antiplatelet | Intracranial stenosis (may use), high bleeding risk, hepatic impairment | Bleeding signs; dyspnea (common side effect) | - | URGENT | URGENT | - |
| Heparin IV drip (therapeutic) | IV | - | 60-80 units/kg :: IV :: once :: Bolus 60-80 units/kg (max 5000u); infusion 12-18 units/kg/h; target aPTT 1.5-2.5x control. Use for: cardiac source with high re-embolization risk, arterial dissection, crescendo TIA, free-floating thrombus | Large infarct (hemorrhagic transformation risk), uncontrolled BP, within 24h of tPA | aPTT q6h until stable, then q12-24h; platelets q3 days; neuro checks | - | URGENT | - | URGENT |
| Decompressive craniectomy (malignant MCA infarct) | - | - | 50% :: - :: - :: For malignant MCA syndrome with >50% MCA territory infarct, age <60 preferred; within 48h of onset; reduces mortality from 70-80% to ~20% | Age >60 (relative — DESTINY II showed benefit up to age 80 but with higher disability); bilateral infarcts; hemorrhagic transformation | Post-operative neuro checks, ICP monitoring, wound care | - | - | - | STAT |
| Osmotherapy: Mannitol 20% | IV | - | 1-1.5 g/kg :: IV :: once :: 1-1.5 g/kg IV bolus for acute herniation; 0.25-0.5 g/kg q4-6h maintenance | Anuria, severe dehydration | Serum osmolality (hold if >320 mOsm/kg), osmolar gap, renal function, I/O | - | - | - | STAT |
| Osmotherapy: Hypertonic saline 23.4% | IV | - | 30 mL :: IV :: once :: 30 mL IV bolus via central line over 10-20 min for acute herniation | No central access for 23.4%; hypokalemia | Serum sodium (target 145-155 mEq/L), osmolality, central line integrity | - | - | - | STAT |
| Hypertonic saline 3% infusion | IV | - | 150-500 mL :: IV :: continuous :: 150-500 mL IV bolus or continuous infusion 0.5-1 mL/kg/h; target Na 145-155 | Hypernatremia, volume overload | Serum sodium q4-6h, osmolality | - | - | - | STAT |

### 3D. Disease-Modifying / Chronic Therapies

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Atorvastatin | PO | - | 80 mg :: PO :: daily :: 80 mg PO daily (high-intensity); start within 24-48h regardless of baseline LDL | - | Active liver disease, pregnancy, breastfeeding | LFTs at 12 weeks then annually; lipid panel at 4-12 weeks; CK if myalgia | - | STAT | ROUTINE | STAT |
| Rosuvastatin | PO | - | 20-40 mg :: PO :: daily :: 20-40 mg PO daily (high-intensity alternative) | - | Active liver disease, pregnancy, CrCl <30 for 40mg | Same as atorvastatin | - | STAT | ROUTINE | STAT |
| Apixaban | PO | - | 5 mg :: PO :: BID :: 5 mg PO BID (2.5 mg BID if ≥2 of: age ≥80, weight ≤60kg, Cr ≥1.5); start 4-14 days post-stroke for AF (timing based on infarct size). Preferred DOAC per guidelines | - | Renal function; bleeding signs; CBC | - | - | ROUTINE | ROUTINE | - |
| Rivaroxaban | PO | - | 20 mg :: PO :: daily :: 20 mg PO daily with evening meal (15 mg daily if CrCl 15-50); start 4-14 days post-stroke for AF | - | Renal function q6-12 months; bleeding signs | - | - | ROUTINE | ROUTINE | - |
| Dabigatran | PO | - | 150 mg :: PO :: BID :: 150 mg PO BID (75 mg BID if CrCl 15-30); start 4-14 days post-stroke for AF | - | Renal function q6-12 months; bleeding signs; GI side effects | - | - | ROUTINE | ROUTINE | - |
| Warfarin | PO | - | 5 mg :: PO :: daily :: 5 mg PO daily initial (2-3 mg if elderly, low weight, or interacting drugs); target INR 2.0-3.0 for AF; 2.5-3.5 for mechanical valve. Bridge with heparin | - | INR daily until stable, then weekly, then monthly; diet counseling (vitamin K) | - | - | ROUTINE | ROUTINE | - |
| Lisinopril | PO | - | 5-10 mg :: PO :: daily :: Start 5-10 mg PO daily; titrate to 20-40 mg daily; target BP <130/80 after acute phase | - | Cr and K+ at 1-2 weeks after initiation; BP | - | - | ROUTINE | ROUTINE | - |
| Amlodipine | PO | - | 5 mg :: PO :: daily :: Start 5 mg PO daily; max 10 mg daily | - | BP, peripheral edema | - | - | ROUTINE | ROUTINE | - |
| Losartan | PO | - | 50 mg :: PO :: daily :: Start 50 mg PO daily; max 100 mg daily | - | Cr, K+, BP | - | - | ROUTINE | ROUTINE | - |
| Metoprolol succinate | PO | - | 25 mg :: PO :: daily :: Start 25 mg PO daily; titrate to 200 mg daily | - | HR, BP | - | - | ROUTINE | ROUTINE | - |
| Ezetimibe | PO | - | 10 mg :: PO :: daily :: 10 mg PO daily; add if LDL not at goal on max statin | - | LFTs, lipid panel | - | - | ROUTINE | ROUTINE | - |
| PCSK9 inhibitor (evolocumab) | SC | - | 140 mg :: SC :: monthly :: 140 mg SC q2 weeks or 420 mg SC monthly; if LDL not at goal on max statin + ezetimibe | - | Lipid panel q4-12 weeks; injection site reactions | - | - | - | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology consultation (stroke team) | STAT | STAT | - | STAT | All acute stroke presentations; tPA decision; stroke workup |
| Neurointerventional/endovascular consultation | STAT | STAT | - | STAT | Large vessel occlusion on CTA for thrombectomy |
| Neurosurgery consultation | URGENT | URGENT | - | STAT | Malignant MCA edema, posterior fossa stroke with hydrocephalus, hemorrhagic transformation requiring intervention |
| Cardiology consultation | - | ROUTINE | ROUTINE | ROUTINE | Newly detected atrial fibrillation, acute MI, cardiomyopathy, PFO evaluation |
| Vascular surgery consultation | - | ROUTINE | ROUTINE | - | Symptomatic carotid stenosis ≥50% (NASCET) for endarterectomy; ideally within 2 weeks |
| Speech-language pathology (SLP) | URGENT | STAT | ROUTINE | URGENT | Dysphagia screening before any PO intake; aphasia evaluation; cognitive-communication assessment |
| Physical therapy (PT) | - | URGENT | ROUTINE | URGENT | Early mobilization within 24-48h (AVERT trial: avoid very early aggressive mobilization <24h); gait and balance training |
| Occupational therapy (OT) | - | URGENT | ROUTINE | URGENT | ADL assessment, upper extremity function, adaptive equipment, cognitive rehabilitation |
| Rehabilitation medicine (physiatry) | - | ROUTINE | ROUTINE | - | Determine rehabilitation disposition (inpatient rehab, SNF, home health, outpatient) |
| Social work | - | ROUTINE | ROUTINE | - | Discharge planning, insurance, DME, caregiver support, advance directives |
| Nutrition/dietitian | - | ROUTINE | ROUTINE | - | Dysphagia diet recommendations, cardiovascular risk diet (Mediterranean, DASH) |
| Palliative care | - | ROUTINE | - | ROUTINE | Large territory stroke with poor prognosis, goals of care discussion |
| Smoking cessation counseling | - | ROUTINE | ROUTINE | - | Active smokers |
| Case management | - | ROUTINE | ROUTINE | - | Rehabilitation placement, follow-up coordination |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Call 911 immediately if new symptoms: sudden weakness, numbness, vision changes, speech difficulty, severe headache, loss of balance | STAT | STAT | ROUTINE |
| Do NOT drive until cleared by neurology (minimum 2 weeks; state-specific laws apply) | URGENT | URGENT | ROUTINE |
| Take all medications as prescribed; do NOT stop antiplatelet or anticoagulant without medical advice | URGENT | URGENT | ROUTINE |
| Swallowing precautions per SLP recommendations (sit upright 90° for meals, specific diet texture) | URGENT | URGENT | ROUTINE |
| Fall prevention: clear pathways, use assistive devices, adequate lighting, non-slip surfaces | - | URGENT | ROUTINE |
| Blood pressure monitoring at home (target <130/80 per physician guidance) | - | ROUTINE | ROUTINE |
| Stroke signs education for patient and family: F.A.S.T. (Face drooping, Arm weakness, Speech difficulty, Time to call 911) | URGENT | ROUTINE | ROUTINE |
| Medication list: carry updated list including all prescriptions, OTC, and supplements | - | ROUTINE | ROUTINE |
| Follow-up appointment with neurology in 1-2 weeks; primary care in 2-4 weeks | - | ROUTINE | ROUTINE |
| Report any bleeding (bruising, blood in stool/urine, gum bleeding) if on anticoagulation | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Smoking cessation (absolute) | - | ROUTINE | ROUTINE |
| Blood pressure target <130/80 mmHg | - | ROUTINE | ROUTINE |
| Mediterranean or DASH diet | - | ROUTINE | ROUTINE |
| Sodium restriction <2.3 g/day (ideally <1.5 g if hypertensive) | - | ROUTINE | ROUTINE |
| Regular aerobic exercise: 40 min moderate intensity, 3-4 days/week (after medical clearance) | - | - | ROUTINE |
| Weight management (BMI 18.5-24.9) | - | ROUTINE | ROUTINE |
| Alcohol limitation: ≤1 drink/day women, ≤2 drinks/day men; cessation if heavy use | - | ROUTINE | ROUTINE |
| Glycemic control target HbA1c <7% (individualized) | - | ROUTINE | ROUTINE |
| LDL target <70 mg/dL (high-intensity statin) | - | ROUTINE | ROUTINE |
| Obstructive sleep apnea screening (Berlin questionnaire or STOP-BANG); CPAP if diagnosed | - | ROUTINE | ROUTINE |
| Stress management and emotional support (depression common post-stroke) | - | ROUTINE | ROUTINE |
| Influenza and pneumococcal vaccination | - | - | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Hypoglycemia | Glucose <60; symptoms resolve with dextrose; diaphoresis, tremor | POC glucose STAT |
| Seizure with Todd's paralysis | Witnessed seizure, post-ictal confusion, resolves within 24h; may have known epilepsy | EEG, clinical observation, MRI (DWI negative) |
| Complicated migraine (hemiplegic) | Headache history, aura preceding deficit, gradual onset ("marching"), younger patient, family history | MRI DWI (negative), clinical history |
| Intracerebral hemorrhage | CT shows hemorrhage; more severe headache, rapid progression, vomiting | CT head without contrast |
| Brain tumor/mass | Subacute onset over days-weeks, progressive symptoms, headache worse in morning | MRI with contrast (enhancing mass) |
| Subdural hematoma | History of trauma or anticoagulation; subacute confusion, headache, fluctuating symptoms | CT head (crescent-shaped extra-axial collection) |
| Hypertensive encephalopathy / PRES | Severely elevated BP, headache, confusion, visual changes, seizures; typically posterior involvement | MRI FLAIR (posterior white matter edema), BP >220/120 |
| CNS infection (abscess, meningitis) | Fever, meningismus, subacute course, immunocompromise | MRI with contrast, LP, blood cultures |
| Conversion disorder / functional neurological disorder | Non-anatomic distribution, Hoover sign positive, give-way weakness, distractible exam findings | Normal imaging, clinical exam findings |
| Peripheral vertigo (for posterior circulation symptoms) | Isolated vertigo, positive HINTS peripheral pattern, no other neurologic deficits | HINTS exam, MRI DWI |
| Multiple sclerosis exacerbation | Young patient, prior episodes, symptoms disseminated in space and time | MRI (periventricular/juxtacortical lesions), oligoclonal bands |
| Metabolic encephalopathy | Bilateral, non-focal exam (usually); abnormal metabolic labs; confusion predominates | BMP, ammonia, TSH, LFTs, UDS |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| NIHSS (NIH Stroke Scale) | STAT | STAT | ROUTINE | STAT | q1h x 24h (post-tPA: q15min x 2h, q30min x 6h, q1h x 16h), then q4h x 48h, then q shift | Stable or improving | If NIHSS increases ≥4 points: STAT CT head, call stroke team; consider hemorrhagic transformation, re-occlusion, or new stroke |
| Blood pressure | STAT | STAT | ROUTINE | STAT | Post-tPA: q15min x 2h, q30min x 6h, q1h x 16h; non-tPA: q1h x 24h, then q4h | Pre-tPA: <185/110; Post-tPA: <180/105 x 24h; Chronic: <130/80 | Titrate antihypertensives; avoid SBP <100 (hypoperfusion risk) |
| Heart rate and rhythm (telemetry) | STAT | STAT | - | STAT | Continuous x 48-72h minimum | Detect paroxysmal atrial fibrillation, arrhythmias | Cardiology consult; anticoagulation if AF |
| Temperature | STAT | STAT | - | STAT | q4h x 48h, then q8h | Target <37.5°C (normothermia) | Acetaminophen; cooling measures; infection workup if >38°C |
| Blood glucose | STAT | STAT | ROUTINE | STAT | q6h x 48h (q1h if insulin drip) | 140-180 mg/dL; avoid <60 mg/dL | Insulin; D50W for hypoglycemia |
| Oxygen saturation (SpO2) | STAT | STAT | - | STAT | Continuous x 24h, then q4h | ≥94% | Supplemental O2; if <90% consider intubation for large strokes |
| Neurologic exam (level of consciousness, pupils) | STAT | STAT | - | STAT | q1-4h depending on severity | Alert, equal reactive pupils | Declining LOC: STAT CT, ICP management |
| Swallowing screen | URGENT | STAT | - | URGENT | Before any PO intake | Pass screening (water swallow test) | NPO until formal SLP evaluation |
| INR (if on warfarin) | - | ROUTINE | ROUTINE | - | Daily until stable, then per protocol | 2.0-3.0 for AF; 2.5-3.5 for mechanical valve | Dose adjustment |
| Renal function (Cr, BUN) | - | ROUTINE | ROUTINE | - | q24-48h if contrast given or on new medications | Stable | Hydration; hold nephrotoxic agents |
| Lipid panel | - | ROUTINE | ROUTINE | - | Fasting within 24-48h; repeat at 4-12 weeks on statin | LDL <70 mg/dL | Intensify statin; add ezetimibe or PCSK9i |
| Depression screening (PHQ-9) | - | - | ROUTINE | - | At 1 month, 3 months, annually | PHQ-9 <5 | SSRI initiation; psychology/psychiatry referral |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Minor stroke (NIHSS 0-3) with stable exam, adequate support at home, able to perform ADLs or with home health, completed workup or reliable outpatient follow-up arranged, medications filled |
| Admit to stroke unit/floor | Moderate stroke (NIHSS 4-15), requires IV medications or ongoing monitoring, incomplete workup, dysphagia requiring NPO/modified diet, new atrial fibrillation requiring anticoagulation initiation |
| Admit to ICU/neuro-ICU | Post-tPA monitoring (first 24h), post-thrombectomy, large territory infarct with edema risk, posterior fossa stroke with herniation risk, unstable BP requiring IV antihypertensives, declining neurologic exam, respiratory compromise |
| Transfer to higher level of care | LVO needing thrombectomy (transfer to comprehensive stroke center), need for neurosurgical intervention not available, need for neuro-ICU not available |
| Inpatient rehabilitation | Moderate-severe deficits (NIHSS >4), able to participate in 3h/day therapy, expected to benefit from intensive rehab, medically stable |
| Skilled nursing facility (SNF) | Unable to tolerate 3h/day rehab, needs skilled nursing care, medically complex requiring ongoing monitoring |
| Home with outpatient therapy | Mild deficits, safe home environment, reliable follow-up, family support available |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IV alteplase within 4.5h | Class I, Level A | [AHA/ASA 2019 Guidelines (Powers et al.)](https://pubmed.ncbi.nlm.nih.gov/31662037/); [NINDS trial (NEJM 1995)](https://pubmed.ncbi.nlm.nih.gov/7477192/); [ECASS III (Hacke et al. NEJM 2008)](https://pubmed.ncbi.nlm.nih.gov/18815396/) |
| Tenecteplase non-inferior to alteplase for LVO | Class IIa, Level B-R | [AcT trial (Menon et al. Lancet 2022)](https://pubmed.ncbi.nlm.nih.gov/35779553/); EXTEND-IA TNK |
| Thrombectomy for LVO 0-6h | Class I, Level A | [MR CLEAN (Berkhemer et al. NEJM 2015)](https://pubmed.ncbi.nlm.nih.gov/25517348/), ESCAPE, EXTEND-IA, SWIFT-PRIME, REVASCAT |
| Thrombectomy for LVO 6-24h (selected patients) | Class I, Level A | [DAWN trial (Nogueira et al. NEJM 2018)](https://pubmed.ncbi.nlm.nih.gov/29129157/); [DEFUSE-3 (Albers et al. NEJM 2018)](https://pubmed.ncbi.nlm.nih.gov/29364767/) |
| DAPT 21 days for minor stroke/high-risk TIA | Class I, Level A | [CHANCE trial (Wang et al. NEJM 2013)](https://pubmed.ncbi.nlm.nih.gov/23803136/); POINT trial |
| Aspirin + ticagrelor 30 days for minor stroke | Class IIa, Level B-R | THALES trial |
| High-intensity statin therapy | Class I, Level A | [SPARCL trial (Amarenco et al. NEJM 2006)](https://pubmed.ncbi.nlm.nih.gov/16899775/); AHA/ASA 2021 |
| Anticoagulation for AF-related stroke | Class I, Level A | RE-LY, ROCKET-AF, ARISTOTLE, ENGAGE AF |
| BP target <130/80 for secondary prevention | Class I, Level A | SPS3 trial; AHA/ASA 2021 |
| Early mobilization (24-48h, not aggressive) | Class IIa, Level B-R | AVERT trial (very early <24h aggressive mobilization harmful) |
| Decompressive craniectomy for malignant MCA | Class I, Level A (age <60) | DESTINY, DECIMAL, HAMLET pooled analysis |
| Extended cardiac monitoring for cryptogenic stroke | Class IIa, Level B-R | CRYSTAL-AF, EMBRACE trials |
| Dysphagia screening before PO intake | Class I, Level B-NR | AHA/ASA 2019 Guidelines |
| Carotid endarterectomy for symptomatic stenosis ≥50% | Class I, Level A | NASCET, ECST trials |
| PFO closure for cryptogenic stroke age 18-60 | Class IIa, Level B-R | CLOSE, RESPECT, REDUCE trials |
| Permissive hypertension (up to 220/120 if no tPA) | Class I, Level B-R | AHA/ASA 2019 Guidelines |
| Target glucose 140-180 mg/dL | Class I, Level C | AHA/ASA 2019 Guidelines |
| DVT prophylaxis within 24-48h | Class I, Level A | AHA/ASA 2019 Guidelines |
| Depression screening post-stroke | Class I, Level B-NR | AHA/ASA 2019 Guidelines |
| Normothermia maintenance | Class I, Level C | AHA/ASA 2019 Guidelines |

---

**APPENDIX: ACUTE STROKE TIME TARGETS**

| Metric | Target |
|--------|--------|
| Door-to-physician | ≤10 minutes |
| Door-to-CT completion | ≤25 minutes |
| Door-to-CT interpretation | ≤45 minutes |
| Door-to-needle (tPA) | ≤45 minutes (target), ≤60 minutes (acceptable) |
| Door-to-groin puncture (thrombectomy) | ≤90 minutes (if on-site), ≤120 minutes (if transfer) |
| Last known well to tPA | ≤4.5 hours |
| Last known well to thrombectomy | ≤24 hours (with perfusion imaging selection for 6-24h) |

**APPENDIX: NIHSS QUICK REFERENCE**

| Score Range | Severity | General Prognosis |
|-------------|----------|-------------------|
| 0 | No deficit | Excellent |
| 1-4 | Minor stroke | Good; consider DAPT |
| 5-15 | Moderate stroke | Consider tPA; may need rehab |
| 16-20 | Moderate-severe | tPA + thrombectomy if LVO; likely inpatient rehab |
| 21-42 | Severe | High mortality/morbidity; goals of care discussion |

**APPENDIX: ASPECTS (Alberta Stroke Program Early CT Score)**

| Score | Interpretation |
|-------|---------------|
| 10 | Normal CT |
| 7-9 | Small infarct; favorable for intervention |
| 6 | Threshold for thrombectomy eligibility (0-6h window) |
| <6 | Large established infarct; higher hemorrhagic transformation risk |
| 0 | Complete MCA territory infarct |
