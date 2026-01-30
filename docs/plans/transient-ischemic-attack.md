---
title: "Transient Ischemic Attack (TIA)"
description: "Clinical decision support for transient ischemic attack (tia) diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
---

# Transient Ischemic Attack (TIA)

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Transient Ischemic Attack (TIA)

**ICD-10:** G45.9 (Transient cerebral ischemic attack, unspecified), G45.0 (Vertebro-basilar artery syndrome), G45.1 (Carotid artery syndrome)

**SYNONYMS:** Transient ischemic attack, TIA, mini-stroke, warning stroke, transient stroke, pre-stroke, temporary stroke symptoms, reversible ischemic neurological deficit

**SCOPE:** Acute evaluation and secondary prevention after transient ischemic attack in adults. Covers risk stratification (ABCD2), urgent workup (MRI with DWI, vascular imaging, cardiac evaluation), dual antiplatelet therapy initiation, and rapid secondary prevention. TIA is a medical emergency — 90-day stroke risk is 10-15% without intervention, highest in first 48h. Excludes completed ischemic stroke (see Acute Ischemic Stroke template), hemorrhagic stroke, and TIA mimics.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Point-of-care glucose | STAT | STAT | STAT | - | Hypoglycemia mimics TIA; must rule out immediately | >60 mg/dL |
| CBC with differential | STAT | STAT | ROUTINE | - | Thrombocytosis or thrombocytopenia; polycythemia; anemia; infection | Normal |
| CMP (BMP + LFTs) | STAT | STAT | ROUTINE | - | Electrolytes; renal function for contrast; hepatic function | Normal |
| PT/INR | STAT | STAT | ROUTINE | - | Anticoagulant use; coagulopathy assessment | Normal |
| Lipid panel (fasting or non-fasting) | STAT | STAT | ROUTINE | - | LDL target <70 mg/dL; statin initiation | LDL <70 |
| HbA1c | STAT | STAT | ROUTINE | - | Diabetes screening; cardiovascular risk factor | <7.0% |
| Troponin | STAT | STAT | - | - | Concurrent ACS; cardiac embolic source | Normal |
| Blood glucose (fasting) | - | ROUTINE | ROUTINE | - | Diabetes screening | <126 mg/dL |
| TSH | - | ROUTINE | ROUTINE | - | Hyperthyroidism → atrial fibrillation | Normal |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| ESR / CRP | URGENT | ROUTINE | ROUTINE | - | Vasculitis screen; giant cell arteritis (age >50 with TIA); inflammatory markers | Normal |
| Homocysteine | - | ROUTINE | ROUTINE | - | Elevated homocysteine as independent stroke risk factor | Normal (<15 µmol/L) |
| Urine drug screen | URGENT | ROUTINE | - | - | Cocaine/amphetamine-associated TIA/stroke | Negative |
| RPR/VDRL | - | ROUTINE | ROUTINE | - | Syphilitic vasculitis | Non-reactive |
| HIV 1/2 antigen/antibody | - | ROUTINE | ROUTINE | - | HIV-associated vasculopathy | Negative |
| Pregnancy test (β-hCG) | STAT | STAT | ROUTINE | - | Affects imaging and treatment decisions | Document result |
| Magnesium | URGENT | ROUTINE | ROUTINE | - | Electrolyte management | Normal |

### 1C. Rare/Specialized (Young TIA or Cryptogenic)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Hypercoagulable panel (Protein C, S, antithrombin III, Factor V Leiden, prothrombin gene mutation) | - | EXT | ROUTINE | - | Young patient (<50); cryptogenic TIA; personal/family history of thrombosis | Normal |
| Antiphospholipid antibodies (lupus anticoagulant, anticardiolipin, β2-glycoprotein I) | - | ROUTINE | ROUTINE | - | Young TIA; recurrent TIA; systemic lupus; recurrent pregnancy loss | Negative |
| ANA, dsDNA | - | EXT | ROUTINE | - | Lupus cerebritis; vasculitis | Negative |
| ANCA (c-ANCA, p-ANCA) | - | EXT | EXT | - | CNS vasculitis | Negative |
| Hemoglobin electrophoresis | - | EXT | EXT | - | Sickle cell disease (young patients, African descent) | Normal |
| JAK2 mutation | - | EXT | EXT | - | Polycythemia vera; myeloproliferative disorders | Negative |
| Lipoprotein(a) | - | ROUTINE | ROUTINE | - | Independent cardiovascular risk factor; elevated in 20% of population | <50 mg/dL |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with DWI | STAT | STAT | URGENT | - | Within 24h (ideally <6h). DWI-positive in 30-50% of clinical TIA — these patients are at HIGHEST stroke risk and may be reclassified as minor stroke | DWI restriction = acute ischemia (even if symptoms resolved, this upgrades risk and may change to minor stroke diagnosis); FLAIR changes; prior infarcts | Pacemaker, metallic implants, severe claustrophobia |
| CT head without contrast | STAT | STAT | - | - | Immediate (if MRI unavailable or contraindicated); excludes hemorrhage and mass | No hemorrhage; no mass; may show old infarcts | Pregnancy (relative) |
| CTA head and neck (OR MRA head and neck) | STAT | STAT | URGENT | - | With initial imaging or within 24h. Evaluates extracranial AND intracranial vessels | Carotid stenosis (≥50% NASCET); intracranial stenosis; vertebral stenosis; dissection | Contrast allergy; renal impairment (for CTA). MRA: pacemaker |
| ECG (12-lead) | STAT | STAT | ROUTINE | - | Immediately | Atrial fibrillation (detected in 5-10% on initial ECG); atrial flutter; acute MI; LVH; old infarct | None |
| Continuous cardiac monitoring (telemetry) | STAT | STAT | - | - | Minimum 24h in ED/hospital; ideally 48-72h | Paroxysmal atrial fibrillation (detected in additional 5-7% with monitoring) | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Transthoracic echocardiogram (TTE) | - | ROUTINE | ROUTINE | - | Within 24-48h | LV thrombus; PFO; valvular disease; cardiomyopathy; akinetic segments | None significant |
| Transesophageal echocardiogram (TEE) with bubble study | - | ROUTINE | ROUTINE | - | If TTE nondiagnostic; cryptogenic TIA; young patient | PFO with right-to-left shunt; atrial septal aneurysm; LAA thrombus; aortic arch atheroma (≥4mm) | Esophageal pathology |
| Carotid duplex ultrasound | URGENT | URGENT | URGENT | - | Within 24h (may be obtained instead of or in addition to CTA/MRA) | Carotid stenosis ≥50%; plaque characterization; hemodynamic significance | None significant |
| Extended cardiac monitoring (Holter 30-day or implantable loop recorder) | - | ROUTINE | ROUTINE | - | Arrange before discharge; especially if cryptogenic TIA | Paroxysmal AF (detected in 12-30% with prolonged monitoring in cryptogenic cases) | None significant |
| Transcranial Doppler (TCD) with bubble study | - | ROUTINE | ROUTINE | - | If PFO evaluation needed (alternative to TEE bubble); also for intracranial stenosis and microembolic signals | Right-to-left shunt; intracranial stenosis; microembolic signals | Absent temporal bone window |
| CT perfusion | - | EXT | - | - | If diagnosis uncertain; evaluate for persistent hypoperfusion despite symptom resolution | Perfusion deficits suggesting ongoing ischemic risk | Contrast allergy; renal impairment |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Conventional cerebral angiography (DSA) | - | EXT | EXT | - | If intracranial stenosis suspected on CTA/MRA; vasculitis workup; Moyamoya | Beading (vasculitis); intimal flap (dissection); Moyamoya collaterals; intracranial stenosis quantification | Contrast allergy; coagulopathy |
| MRI vessel wall imaging | - | EXT | EXT | - | Intracranial stenosis characterization; vasculitis evaluation | Vessel wall enhancement (active inflammation, unstable plaque) | Standard MRI contraindications |
| Fat-saturated MRI neck | - | ROUTINE | ROUTINE | - | If cervical dissection suspected (neck pain, Horner syndrome, young patient) | Intramural hematoma (crescent sign) | Standard MRI contraindications |
| PET-CT | - | - | EXT | - | If occult malignancy suspected (Trousseau syndrome) | Malignancy | Pregnancy |

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Aspirin (loading dose) | PO | - | 325 mg :: PO :: load :: 325 mg PO loading dose immediately upon TIA diagnosis (give in ED). Do NOT delay antiplatelet therapy | Active GI bleed; true aspirin allergy; thrombocytopenia <50K | GI symptoms; bleeding | STAT | STAT | STAT | - |
| Clopidogrel (loading dose for DAPT) | PO | - | 300 mg :: PO :: load :: 300 mg PO loading dose (give with aspirin for DAPT). DAPT is standard for high-risk TIA (ABCD2 ≥4) or minor stroke per CHANCE and POINT trials | Active bleeding; severe hepatic impairment | Bleeding; CBC | STAT | STAT | STAT | - |
| Dual antiplatelet therapy (DAPT maintenance): Aspirin + Clopidogrel | - | - | 81 mg :: - :: daily :: Aspirin 81 mg daily + Clopidogrel 75 mg daily x 21 days (CHANCE protocol) or x 90 days (POINT protocol — higher bleeding risk with longer duration). Then transition to single antiplatelet (typically clopidogrel 75 mg or aspirin 81 mg monotherapy) | Major bleeding risk; planned surgery | Bleeding signs; CBC monthly | - | STAT | STAT | - |
| Dual antiplatelet therapy (alternative): Aspirin + Ticagrelor | PO | - | 81 mg :: PO :: daily :: Aspirin 81 mg daily + Ticagrelor 90 mg BID x 30 days (THALES trial; for minor stroke NIHSS ≤5). Then single antiplatelet | Intracranial hemorrhage history; high bleeding risk; hepatic impairment | Bleeding; dyspnea (common side effect); avoid strong CYP3A4 inhibitors | - | STAT | STAT | - |
| High-intensity statin | PO | - | 80 mg :: PO :: daily :: Atorvastatin 80 mg PO daily (or Rosuvastatin 20-40 mg). Start immediately regardless of baseline LDL | Active liver disease; pregnancy | LFTs at 12 weeks; lipid panel at 4-12 weeks; CK if myalgia | STAT | STAT | STAT | - |
| Blood pressure management (acute) | - | - | 25% :: - :: - :: If SBP >220 or DBP >120 in ED: lower gently (15-25% in first 24h). If lower BP levels: permissive hypertension in first 24-48h unless end-organ damage. Avoid precipitous drops | Carotid stenosis with hemodynamic TIA: do NOT aggressively lower BP (may worsen symptoms) | Neuro checks with each change; BP q1h acutely | STAT | STAT | - | - |

### 3B. Secondary Prevention (Initiate Urgently)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Antihypertensive therapy (chronic) | PO | - | 10-20 mg :: PO :: daily :: Target BP <130/80 mmHg. Start/restart 24-48h after TIA once stable. Agent choice per comorbidities: ACE-I/ARB first-line. Consider: Lisinopril 10-20 mg daily, Amlodipine 5-10 mg, Losartan 50-100 mg, Chlorthalidone 12.5-25 mg | Bilateral renal artery stenosis (ACE-I/ARB); pregnancy | Home BP monitoring; Cr and K+ at 1-2 weeks | - | ROUTINE | ROUTINE | - |
| Anticoagulation (if atrial fibrillation detected) | PO | - | 5 mg :: - :: BID :: Start DOAC within 1-3 days for TIA (can start earlier than stroke). Preferred: Apixaban 5 mg BID (2.5 mg BID if criteria met). Alternative: Rivaroxaban 20 mg daily; Dabigatran 150 mg BID. Discontinue antiplatelet when anticoagulant started (do NOT combine long-term unless specific indication) | Active bleeding; mechanical valve (use warfarin); severe renal impairment | Renal function q6-12 months; bleeding signs | - | ROUTINE | ROUTINE | - |
| Carotid endarterectomy (CEA) | Surgery | - | 50% :: - :: - :: For symptomatic carotid stenosis ≥50% (NASCET criteria); ideally performed within 2 weeks of TIA (maximum benefit). NNT = 6 for 70-99% stenosis; NNT = 22 for 50-69% stenosis | Near-occlusion (controversial); life expectancy <5 years; severe cardiac comorbidity | Post-op: BP monitoring; neuro checks q1h x 24h; wound hematoma; cranial nerve injury | - | URGENT | URGENT | - |
| Carotid artery stenting (CAS) | Endovascular | - | Alternative to CEA if: high surgical risk, prior neck radiation, prior CEA with restenosis, surgically inaccessible. Requires DAPT (aspirin + clopidogrel) post-stenting | Severe aortic arch tortuosity; fresh thrombus | Post-procedure: BP management; neuro checks; DAPT compliance; restenosis surveillance | - | ROUTINE | ROUTINE | - |
| PFO closure | Procedure | - | For cryptogenic TIA/stroke age 18-60 with PFO and right-to-left shunt. Reduces recurrent stroke vs medical therapy alone (CLOSE, RESPECT, REDUCE trials). Requires 3-6 months DAPT then aspirin indefinitely | Anatomic constraints; active infection | Echo at 6-12 months; aspirin long-term | - | - | ROUTINE | - |
| Ezetimibe | PO | - | 10 mg :: PO :: daily :: 10 mg PO daily; add if LDL not at goal on max statin | LFTs; lipid panel | - | - | ROUTINE | ROUTINE | - |
| PCSK9 inhibitor (evolocumab or alirocumab) | SC | - | 140 mg :: SC :: monthly :: Evolocumab 140 mg SC q2 weeks or 420 mg monthly; if LDL not at goal on statin + ezetimibe | Lipid panel q4-12 weeks; injection site | - | - | - | ROUTINE | - |
| Diabetes management (optimize) | PO/SC | - | 7% :: - :: - :: Target HbA1c <7% (individualized); GLP-1 agonists and SGLT2 inhibitors have cardiovascular benefit | Per agent | HbA1c q3 months; renal function | - | ROUTINE | ROUTINE | - |

### 3C. Medications for Specific Etiologies

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Anticoagulation (warfarin) | - | Mechanical heart valve + TIA | Warfarin to target INR 2.5-3.5; bridge with heparin | - | INR weekly then monthly | - | - | - | - |
| DAPT long-term (aspirin + clopidogrel) | - | Intracranial stenosis 70-99% (SAMMPRIS trial: medical > stenting) | 325 mg :: PO :: daily :: Aspirin 325 mg + clopidogrel 75 mg daily x 90 days; then single antiplatelet + aggressive risk factor management | - | Bleeding; MRA q6-12 months | - | - | - | - |
| Anticoagulation | - | Cervical artery dissection | Antiplatelet or anticoagulation (both equally effective per CADISS trial); typically 3-6 months | - | Repeat vascular imaging at 3-6 months | - | - | - | - |
| Colchicine | PO | Residual inflammatory risk (LoDoCo2 / COLCOT trials support in ACS — emerging data for stroke prevention) | 0.5 mg :: PO :: daily :: 0.5 mg PO daily | - | GI symptoms; CBC | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology (stroke team) | STAT | STAT | URGENT | - | All TIA patients; risk stratification; workup direction; secondary prevention |
| Vascular surgery | - | URGENT | URGENT | - | Symptomatic carotid stenosis ≥50% for CEA; ideally within 2 weeks |
| Neurointerventional / Endovascular | - | ROUTINE | ROUTINE | - | Carotid stenting; intracranial stenosis management; PFO closure referral |
| Cardiology | - | ROUTINE | ROUTINE | - | Newly detected AF; PFO evaluation; anticoagulation management; cardiac optimization |
| Electrophysiology | - | ROUTINE | ROUTINE | - | Extended cardiac monitoring arrangement; AF management |
| Primary care (expedited) | - | ROUTINE | ROUTINE | - | Risk factor management; medication titration; chronic disease management |
| Smoking cessation program | - | ROUTINE | ROUTINE | - | Active smokers |
| Nutrition / Dietitian | - | ROUTINE | ROUTINE | - | Mediterranean/DASH diet counseling; weight management |
| Diabetes educator | - | - | ROUTINE | - | If new or uncontrolled diabetes |
| Social work | - | ROUTINE | ROUTINE | - | Medication assistance; transportation; caregiver support |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| TIA is a WARNING — risk of full stroke is HIGHEST in first 48h; take this very seriously | STAT | STAT | ROUTINE |
| Call 911 IMMEDIATELY if any symptom recurs: sudden weakness, numbness, speech difficulty, vision changes, severe headache, loss of balance (F.A.S.T.) | STAT | STAT | ROUTINE |
| Take all medications EXACTLY as prescribed; do NOT stop aspirin, clopidogrel, or statin without medical guidance | STAT | STAT | ROUTINE |
| Do NOT drive for at least 2 weeks (state laws vary; some require neurologist clearance) | URGENT | URGENT | ROUTINE |
| Return for follow-up within 1-2 weeks with neurology; primary care within 2-4 weeks | - | ROUTINE | ROUTINE |
| Blood pressure monitoring at home daily; keep log; target per physician guidance (<130/80) | - | ROUTINE | ROUTINE |
| Report any bleeding (bruising, blood in stool/urine, nosebleed) while on DAPT | - | ROUTINE | ROUTINE |
| Carry updated medication list at all times | - | ROUTINE | ROUTINE |
| Notify all providers of TIA history (dental, surgical, emergency) | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Smoking cessation (ABSOLUTE — doubles stroke risk) | - | ROUTINE | ROUTINE |
| Blood pressure target <130/80 mmHg | - | ROUTINE | ROUTINE |
| LDL target <70 mg/dL (high-intensity statin) | - | ROUTINE | ROUTINE |
| Mediterranean or DASH diet | - | ROUTINE | ROUTINE |
| Sodium restriction <2.3 g/day (ideally <1.5 g) | - | ROUTINE | ROUTINE |
| Regular aerobic exercise: 40 min moderate intensity, 3-4 days/week (after medical clearance) | - | - | ROUTINE |
| Weight management (BMI 18.5-24.9) | - | ROUTINE | ROUTINE |
| Alcohol limitation: ≤1 drink/day women, ≤2 drinks/day men | - | ROUTINE | ROUTINE |
| HbA1c target <7% (individualized) | - | ROUTINE | ROUTINE |
| OSA screening (STOP-BANG); CPAP if diagnosed | - | ROUTINE | ROUTINE |
| Depression / anxiety screening (PHQ-9) | - | - | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Migraine with aura | Gradual onset ("marching" symptoms over minutes); visual aura (scintillating scotoma); headache follows; younger; history of migraine | Normal MRI DWI; clinical history; gradual onset differentiates from sudden TIA |
| Seizure with Todd's paralysis | Witnessed seizure; post-ictal confusion; resolves in hours; focal weakness post-seizure | EEG; MRI DWI negative; clinical history |
| Hypoglycemia | Glucose <60; diaphoresis; tremor; confusion; resolves with glucose | POC glucose |
| Peripheral vertigo (BPPV, vestibular neuritis) | Isolated vertigo without other neurologic deficits; positive HINTS (peripheral pattern); nystagmus characteristics | HINTS exam; MRI DWI negative; normal CTA |
| Multiple sclerosis exacerbation | Young patient; symptoms disseminated in space and time; prior episodes; weeks duration | MRI brain (periventricular/juxtacortical lesions); oligoclonal bands |
| Brain tumor | Subacute progressive symptoms; headache; may have transient symptoms from seizure or compression | MRI with contrast (enhancing mass) |
| Conversion disorder / FND | Non-anatomic deficit distribution; Hoover sign; give-way weakness; psychological stressor | Normal MRI; normal vascular imaging; clinical exam |
| Syncope / Pre-syncope | Loss of consciousness; lightheadedness; no focal neurologic deficit | Orthostatic vitals; ECG; echo; tilt table |
| Labyrinthine infarction | Isolated sudden hearing loss + vertigo (AICA territory); may be a TIA equivalent | Audiometry (sensorineural hearing loss); MRI DWI (may show pontine or cerebellar infarct) |
| Subdural hematoma | Fluctuating symptoms; trauma history or anticoagulation; subacute | CT (extra-axial collection) |
| Transient global amnesia | Isolated anterograde amnesia lasting hours; no motor or speech deficit; age >50; benign | Clinical presentation; MRI DWI (may show small hippocampal DWI lesions) |
| Metabolic encephalopathy | Bilateral, non-focal; confusion predominant; abnormal labs | BMP; ammonia; LFTs; TSH |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Neurologic exam (deficit recurrence) | STAT | STAT | ROUTINE | - | q1h x 6h, then q4h in hospital; each outpatient visit | No recurrence of symptoms | If symptoms recur: STAT MRI DWI; may need admission; upgrade to stroke protocol if persistent >24h or DWI+ |
| Blood pressure | STAT | STAT | ROUTINE | - | q1h x 6h in ED; q4h in hospital; daily at home | Acute: avoid precipitous drop; Chronic: <130/80 | Antihypertensive titration; avoid SBP <100 if carotid stenosis |
| Heart rhythm (telemetry) | STAT | STAT | - | - | Continuous x 24-72h minimum | Sinus rhythm; detect paroxysmal AF | If AF detected: anticoagulation; discontinue antiplatelet |
| Blood glucose | STAT | ROUTINE | ROUTINE | - | q6h in hospital; HbA1c at follow-up | 140-180 (acute); HbA1c <7% | Diabetes management |
| Lipid panel | - | ROUTINE | ROUTINE | - | Baseline; repeat at 4-12 weeks on statin | LDL <70 mg/dL | Intensify statin; add ezetimibe or PCSK9i |
| Renal function (Cr) | - | ROUTINE | ROUTINE | - | At baseline; after starting ACE-I/ARB | Stable | Dose adjust medications |
| CBC | - | ROUTINE | ROUTINE | - | Baseline; at 1 month on DAPT | Normal | Monitor for bleeding on DAPT |
| ABCD2 Score (at presentation) | STAT | - | - | - | Once (risk stratification) | Score determines urgency and disposition | ≥4: admit or rapid TIA clinic within 24h; <4: may discharge with 24-48h follow-up if imaging complete |
| Extended cardiac monitoring | - | ROUTINE | ROUTINE | - | 30-day Holter or ILR post-discharge (especially cryptogenic) | Detect AF | Anticoagulation if AF detected |
| Carotid imaging follow-up | - | - | ROUTINE | - | After CEA/CAS: duplex at 1 month, 6 months, then annually | No restenosis | Repeat intervention if significant restenosis |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Admit to hospital (preferred for high-risk) | ABCD2 ≥4; crescendo TIA (recurrent within 24h); large vessel stenosis identified; atrial fibrillation detected; DWI-positive on MRI; incomplete workup that cannot be completed within 24h as outpatient |
| Rapid TIA clinic / 24-48h outpatient workup | ABCD2 <4; symptoms fully resolved; no large vessel disease on imaging; no AF on ECG; MRI/CTA completed and negative; reliable follow-up; medications started |
| Discharge from ED (with next-day follow-up) | Low risk (ABCD2 0-3); all imaging completed and normal (MRI DWI negative, CTA normal, ECG sinus); medications started; reliable patient; follow-up within 24-48h guaranteed |
| Admit to ICU | Rarely needed; consider if hemodynamic TIA with critical stenosis; malignant hypertension; crescendo TIA progressing to stroke |
| Transfer to stroke center | If vascular imaging, MRI, or neurology consultation not available within 24h |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| DAPT (aspirin + clopidogrel 21 days) for minor stroke / high-risk TIA | Class I, Level A | CHANCE trial (Wang et al. NEJM 2013) |
| DAPT (aspirin + clopidogrel 90 days) for minor stroke / high-risk TIA | Class IIa, Level B | POINT trial (Johnston et al. NEJM 2018); higher ICH risk than 21 days |
| Aspirin + ticagrelor x 30 days for minor stroke (NIHSS ≤5) | Class IIa, Level B | THALES trial (Johnston et al. NEJM 2020) |
| High-intensity statin for TIA secondary prevention | Class I, Level A | SPARCL trial (Amarenco et al. NEJM 2006); AHA/ASA 2021 |
| LDL target <70 mg/dL | Class I, Level A | TST trial (Amarenco et al. NEJM 2020) |
| BP target <130/80 for secondary prevention | Class I, Level A | SPS3 trial; PROGRESS; AHA/ASA 2021 |
| CEA within 2 weeks for symptomatic stenosis ≥50% | Class I, Level A | NASCET (NEJM 1991); ECST; Rothwell et al. (Lancet 2004) — maximum benefit if performed within 2 weeks |
| DOACs preferred over warfarin for AF-related TIA/stroke | Class I, Level A | RE-LY, ROCKET-AF, ARISTOTLE, ENGAGE AF |
| Extended cardiac monitoring for cryptogenic TIA | Class IIa, Level B | CRYSTAL-AF (Sanna et al. NEJM 2014); EMBRACE (Gladstone et al. NEJM 2014) |
| PFO closure for cryptogenic stroke/TIA age 18-60 | Class IIa, Level B | CLOSE, RESPECT, REDUCE trials |
| MRI DWI within 24h (DWI+ = higher stroke risk) | Class I, Level B | AHA/ASA Guidelines; Coutts et al. (Stroke 2012) |
| ABCD2 score for risk stratification | Class IIa, Level B | Johnston et al. (Lancet 2007); useful but imperfect; imaging adds value |
| Rapid TIA evaluation reduces 90-day stroke risk | Class I, Level B | EXPRESS trial (Rothwell et al. Lancet 2007); SOS-TIA (Lavallée et al. Lancet Neurol 2007) |
| Medical therapy superior to stenting for intracranial stenosis | Class I, Level A | SAMMPRIS trial (Chimowitz et al. NEJM 2011) |
| OSA screening and CPAP | Class IIa, Level B | AHA/ASA 2021 Guidelines |

---

**APPENDIX: ABCD2 SCORE (TIA RISK STRATIFICATION)**

| Component | Points |
|-----------|--------|
| **A**ge ≥60 | 1 |
| **B**P ≥140/90 at presentation | 1 |
| **C**linical features: Unilateral weakness | 2 |
| **C**linical features: Speech impairment without weakness | 1 |
| **D**uration ≥60 min | 2 |
| **D**uration 10-59 min | 1 |
| **D**iabetes | 1 |
| **Total possible** | **7** |

| Score | 2-Day Stroke Risk | 90-Day Stroke Risk | Recommendation |
|-------|-------------------|--------------------|--------------------|
| 0-3 (Low) | 1.0% | 3.1% | Rapid outpatient workup within 24-48h; may discharge from ED if workup complete |
| 4-5 (Moderate) | 4.1% | 9.8% | Admit or ensure <24h follow-up; start DAPT |
| 6-7 (High) | 8.1% | 17.8% | Admit; aggressive workup and treatment |

**Note:** ABCD2 is imperfect as a stand-alone tool. DWI-positive MRI, large vessel stenosis, and AF detection independently predict stroke risk regardless of ABCD2 score.

**APPENDIX: SECONDARY PREVENTION CHECKLIST**

| Risk Factor | Target | Intervention |
|-------------|--------|-------------|
| Blood pressure | <130/80 | ACE-I/ARB + lifestyle |
| LDL cholesterol | <70 mg/dL | High-intensity statin + ezetimibe ± PCSK9i |
| Diabetes (HbA1c) | <7.0% | Metformin; GLP-1/SGLT2 (CV benefit) |
| Antiplatelet | DAPT x 21-90 days → monotherapy | Aspirin + clopidogrel → single agent |
| Anticoagulation (if AF) | DOAC | Apixaban preferred |
| Carotid stenosis ≥50% | Revascularization | CEA within 2 weeks; or CAS |
| Smoking | Cessation | Counseling + pharmacotherapy |
| Exercise | 40 min, 3-4x/week | Cardiac clearance first |
| Diet | Mediterranean/DASH | Dietitian referral |
| BMI | 18.5-24.9 | Comprehensive lifestyle |
| Sleep apnea | Screening; CPAP if positive | STOP-BANG; sleep study |
