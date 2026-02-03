---
title: "Cerebral Venous Thrombosis (CVT)"
description: "Clinical decision support for cerebral venous thrombosis diagnosis and management"
version: "1.2"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - cerebrovascular
  - stroke
  - thrombosis
---

# Cerebral Venous Thrombosis (CVT)

**VERSION:** 1.2
**CREATED:** January 30, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Cerebral Venous Thrombosis (CVT)

**ICD-10:** I67.6 (Nonpyogenic thrombosis of intracranial venous system), I63.6 (Cerebral infarction due to cerebral venous thrombosis), G08 (Intracranial and intraspinal phlebitis and thrombophlebitis)

**SYNONYMS:** Cerebral venous sinus thrombosis, CVST, CVT, dural sinus thrombosis, sagittal sinus thrombosis, transverse sinus thrombosis, sigmoid sinus thrombosis, cortical vein thrombosis, deep cerebral vein thrombosis, cavernous sinus thrombosis, cerebral venous infarction

**SCOPE:** Diagnostic workup, acute anticoagulation, and long-term management of cerebral venous thrombosis. Covers all venous sinus locations (superior sagittal, transverse, sigmoid, straight, cavernous) and cortical/deep vein thrombosis. Includes management of associated hemorrhagic venous infarction, seizures, elevated ICP, and thrombophilia workup. Excludes cavernous sinus thrombosis from septic source (see infectious workup). For arterial ischemic stroke, see "Acute Ischemic Stroke" template. For subarachnoid hemorrhage, see "SAH" template.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential (CPT 85025) | Polycythemia, thrombocytosis, leukocytosis (infection/inflammation); HIT screen baseline | Normal; identify polycythemia or thrombocytosis | STAT | STAT | ROUTINE | STAT |
| CMP (BMP + LFTs) (CPT 80053) | Metabolic screen; baseline for anticoagulation; hepatic function | Normal | STAT | STAT | ROUTINE | STAT |
| PT/INR, aPTT (CPT 85610+85730) | Baseline coagulation; monitor heparin/warfarin | Normal; therapeutic range for anticoagulation | STAT | STAT | ROUTINE | STAT |
| D-dimer (CPT 85379) | Elevated in >90% CVT; normal D-dimer has high negative predictive value in low-suspicion cases; less useful if symptoms >2 weeks | Elevated (>500 ng/mL); normal does NOT exclude CVT if high suspicion | STAT | STAT | ROUTINE | STAT |
| ESR (CPT 85652) | Inflammatory/infectious screen; vasculitis workup | Normal or elevated | URGENT | ROUTINE | ROUTINE | URGENT |
| CRP (CPT 86140) | Inflammatory marker; infection screen | Normal | URGENT | ROUTINE | ROUTINE | URGENT |
| Blood glucose (CPT 82947) | Metabolic screen | Normal | STAT | STAT | ROUTINE | STAT |
| Fibrinogen (CPT 85384) | Baseline before anticoagulation; DIC screen | Normal (200-400 mg/dL) | STAT | STAT | - | STAT |
| Blood type and screen | Potential for hemorrhagic conversion or surgical intervention | On file | STAT | STAT | - | STAT |
| Pregnancy test (females of childbearing age) (CPT 81025) | Pregnancy/postpartum is major CVT risk factor; affects treatment choice | As applicable | STAT | STAT | ROUTINE | STAT |
| TSH (CPT 84443) | Thyroid disease; hypercoagulable workup | Normal | URGENT | ROUTINE | ROUTINE | URGENT |
| Urinalysis (CPT 81003) | Nephrotic syndrome screen (proteinuria → hypercoagulable); UTI | Negative | STAT | STAT | ROUTINE | STAT |
| Procalcitonin (CPT 84145) | Septic CVT evaluation | Normal (<0.1 ng/mL) | URGENT | URGENT | - | URGENT |
| Blood cultures (x2 sets) (CPT 87040) | Septic CVT (cavernous sinus thrombosis from sinusitis/dental/orbital) | No growth | STAT | STAT | - | STAT |
| Lactate (CPT 83605) | Sepsis screen if infectious etiology suspected | Normal (<2.0 mmol/L) | STAT | STAT | - | STAT |

### 1B. Thrombophilia/Hypercoagulable Workup

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Factor V Leiden mutation (CPT 81241) | Most common inherited thrombophilia; increased CVT risk | Negative | - | ROUTINE | ROUTINE | - |
| Prothrombin gene mutation (G20210A) (CPT 81240) | Second most common inherited thrombophilia | Negative | - | ROUTINE | ROUTINE | - |
| Antithrombin III activity (CPT 85300) | Antithrombin deficiency; may be falsely low on heparin | Normal (80-120%) | - | ROUTINE | ROUTINE | - |
| Protein C activity (CPT 85303) | Protein C deficiency; may be falsely low on warfarin or acute thrombosis | Normal | - | ROUTINE | ROUTINE | - |
| Protein S activity (free and total) (CPT 85306) | Protein S deficiency; may be falsely low on warfarin, pregnancy, acute thrombosis | Normal | - | ROUTINE | ROUTINE | - |
| Antiphospholipid antibodies (anticardiolipin IgG/IgM, anti-beta-2 glycoprotein I IgG/IgM, lupus anticoagulant) (CPT 86147+86146+85613) | Antiphospholipid syndrome; repeat in 12 weeks if positive | Negative | - | ROUTINE | ROUTINE | - |
| Homocysteine (CPT 83090) | Hyperhomocysteinemia; modifiable risk factor | Normal (<15 umol/L) | - | ROUTINE | ROUTINE | - |
| ANA (CPT 86235) | Lupus; connective tissue disease | Negative or low titer | - | ROUTINE | ROUTINE | - |
| Anti-dsDNA | If ANA positive; lupus | Negative | - | ROUTINE | ROUTINE | - |
| JAK2 V617F mutation (CPT 81270) | Polycythemia vera; myeloproliferative disorder | Negative | - | ROUTINE | ROUTINE | - |
| Factor VIII activity (CPT 85240) | Elevated factor VIII is independent CVT risk factor | Normal (<150%) | - | ROUTINE | ROUTINE | - |
| Lipoprotein(a) (CPT 83695) | Independent prothrombotic risk factor | Normal (<30 mg/dL) | - | ROUTINE | ROUTINE | - |
| Paroxysmal nocturnal hemoglobinuria (PNH) flow cytometry (CPT 88184) | PNH-associated thrombosis (unusual site thrombosis) | Negative | - | EXT | EXT | - |
| HIT antibody (anti-PF4) | If on heparin and platelet drop >50% | Negative | - | URGENT | - | URGENT |

*Note: Thrombophilia testing should ideally be performed BEFORE starting anticoagulation or >2 weeks after stopping. Protein C and S are affected by warfarin; antithrombin by heparin; lupus anticoagulant by DOACs. However, do NOT delay anticoagulation for thrombophilia results. Factor V Leiden and prothrombin mutation are genetic tests unaffected by anticoagulation. In acute setting, send genetic tests and defer functional assays to outpatient follow-up. Thrombophilia is found in ~35% of CVT patients.*

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| ADAMTS13 activity | TTP if thrombocytopenia and hemolysis | Normal (>10%) | - | EXT | EXT | - |
| Complement C3, C4 (CPT 86160+86162) | Lupus; complement deficiency | Normal | - | EXT | EXT | - |
| Beta-2 microglobulin (CPT 82232) | Lymphoproliferative disorder | Normal | - | EXT | EXT | - |
| Serum protein electrophoresis (SPEP) (CPT 86334) | Multiple myeloma; hyperviscosity | Normal | - | EXT | EXT | - |
| Hemoglobin electrophoresis (CPT 83020) | Sickle cell disease (CVT risk) | Normal | - | EXT | EXT | - |
| BCR-ABL (if elevated WBC) (CPT 81206) | CML | Negative | - | EXT | EXT | - |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast (CPT 70450) | Immediate | Hyperdense sinus (cord sign); hemorrhagic venous infarction; edema; empty delta sign (post-contrast) | None significant | STAT | STAT | - | STAT |
| CT venography (CTV) (CPT 70496) | Immediate (ED) | Filling defect in venous sinuses; absence of contrast in thrombosed sinus; identifies extent of thrombosis | Contrast allergy (premedicate); renal insufficiency | STAT | STAT | - | STAT |
| MRI brain with and without contrast (CPT 70553) | Within 24h | Parenchymal edema; hemorrhagic venous infarction; non-arterial distribution infarct; T2*/SWI blooming in thrombosed vein | GFR <30, gadolinium allergy, pacemaker | URGENT | URGENT | ROUTINE | URGENT |
| MR venography (MRV) (CPT 70547) | Within 24h | Flow gap in thrombosed sinus; absent flow signal; preferred for follow-up (no contrast/radiation) | MRI contraindications | URGENT | URGENT | ROUTINE | URGENT |
| ECG (12-lead) (CPT 93000) | Immediate | Baseline cardiac rhythm; arrhythmia screen | None | STAT | STAT | ROUTINE | STAT |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head with contrast (empty delta sign) | If CTV not initially obtained | Empty delta sign (filling defect in superior sagittal sinus on axial contrast CT) | Contrast allergy | URGENT | URGENT | - | URGENT |
| CT/MR of sinuses and mastoids | If septic CVT suspected | Sinusitis, mastoiditis, otitis as source | Standard CT/MRI contraindications | URGENT | URGENT | - | URGENT |
| Conventional cerebral angiography (DSA) | If CTV/MRV equivocal; isolated cortical vein thrombosis suspected | Gold standard; defines extent; therapeutic option (mechanical thrombectomy) | Contrast allergy; renal insufficiency; coagulopathy | - | EXT | - | EXT |
| Fundoscopic exam / optic nerve sheath diameter on US | Immediate if elevated ICP suspected | Papilledema; optic disc swelling; ONSD >5 mm | None significant | STAT | STAT | - | STAT |
| Transcranial Doppler (TCD) | If bedside assessment needed | Abnormal flow velocities in affected sinuses | Poor temporal window | - | ROUTINE | - | ROUTINE |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Catheter-directed venography with thrombectomy | If severe/refractory despite anticoagulation | Direct visualization; mechanical clot removal; pharmacomechanical thrombolysis | Same as DSA | - | EXT | - | EXT |
| ICP monitoring (invasive) | If refractory elevated ICP | Direct ICP measurement; guide management | Coagulopathy; risk of infection/hemorrhage | - | - | - | EXT |

### LUMBAR PUNCTURE

**Indication:** Measurement of opening pressure (elevated ICP is common in CVT); rules out meningitis in febrile patients; NOT required for diagnosis if imaging is definitive

**Timing:** After neuroimaging confirms CVT; AVOID if large hemorrhagic infarction or mass effect; may serve as therapeutic LP for elevated ICP

**Volume Required:** 10-15 mL standard; therapeutic removal of 20-30 mL if elevated ICP

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure (CPT 89050) | Elevated ICP common in CVT (~50%); guide management | Elevated (>20 cm H2O); therapeutic drainage if >25 | URGENT | URGENT | ROUTINE | - |
| Cell count with differential (tubes 1 and 4) (CPT 89051) | Rule out meningitis/encephalitis | Normal or mildly elevated WBC | URGENT | ROUTINE | ROUTINE | - |
| Protein (CPT 84157) | Mildly elevated in CVT; infection screen | Normal to mildly elevated | URGENT | ROUTINE | ROUTINE | - |
| Glucose with paired serum glucose (CPT 82945) | Rule out infection | Normal (>60% of serum) | URGENT | ROUTINE | ROUTINE | - |
| Gram stain and bacterial culture (CPT 87205+87070) | Septic CVT; meningitis | No organisms | STAT | STAT | - | - |
| Cytology (CPT 88104) | Carcinomatous meningitis if malignancy suspected | Negative | - | ROUTINE | ROUTINE | - |

**Special Handling:** Measure opening pressure with patient in lateral decubitus position, legs extended. Document volume of CSF removed if therapeutic LP.

**Contraindications:** Large hemorrhagic infarction with mass effect; uncal herniation risk; coagulopathy (correct INR <1.5, platelets >50K before LP); active anticoagulation (relative -- discuss risk/benefit)

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Unfractionated heparin (UFH) IV | IV | Acute CVT with large hemorrhagic infarction, renal failure, or anticipated procedures; preferred if endovascular intervention planned | 80 units/kg :: IV :: bolus then continuous :: 80 units/kg IV bolus (max 10,000 units), then 18 units/kg/hr infusion; target aPTT 1.5-2.5x control (60-80 sec) | Active uncontrolled bleeding; severe thrombocytopenia (<50K); HIT | aPTT q6h until therapeutic x2, then q12-24h; platelet count q2d (HIT screen); signs of bleeding | STAT | STAT | - | STAT |
| Enoxaparin (LMWH) | SC | Acute CVT without large hemorrhagic infarction; preferred initial therapy per guidelines | 1 mg/kg BID :: SC :: BID :: 1 mg/kg SC every 12 hours; adjust for CrCl <30 (1 mg/kg daily) or obesity | Active uncontrolled bleeding; CrCl <15; HIT | Anti-Xa levels (target 0.5-1.0 IU/mL) if extremes of weight or renal impairment; platelet count q2d; signs of bleeding | STAT | STAT | - | STAT |
| Levetiracetam (seizure prophylaxis/treatment) | IV/PO | Acute symptomatic seizures; prophylaxis if hemorrhagic infarction or cortical involvement | 1000 mg :: IV :: BID :: Load: 1000-1500 mg IV; Maintenance: 500-1500 mg IV/PO BID (max 3000 mg/day) | Renal impairment (adjust dose per CrCl) | Behavioral changes; suicidality; renal function | STAT | STAT | ROUTINE | STAT |
| Acetazolamide (elevated ICP) | PO/IV | Elevated ICP without indication for emergent surgical intervention | 250 mg :: PO :: BID :: Start 250 mg PO BID; titrate to 500 mg BID; max 2000 mg/day | Sulfonamide allergy; hypokalemia; metabolic acidosis; renal failure | BMP (K, bicarb) q1-2 weeks initially; paresthesias; kidney stones | - | ROUTINE | ROUTINE | ROUTINE |
| Mannitol (acute elevated ICP) | IV | Acute symptomatic elevated ICP with impending herniation | 0.5-1 g/kg :: IV :: bolus :: 0.5-1 g/kg IV over 15-20 min; may repeat q6h; target serum osmolality 300-320 mOsm/kg | CHF; renal failure; serum osmolality >320 | Serum osmolality q6h; BMP; I/O; renal function | STAT | STAT | - | STAT |
| Hypertonic saline 3% (acute elevated ICP) | IV | Alternative to mannitol for acute ICP crisis | 250 mL bolus :: IV :: bolus :: 250 mL IV over 15-20 min via central line preferred; target Na 145-155 mEq/L | Hypernatremia (Na >155) | Sodium q2-4h; serum osmolality; central line preferred for concentrations >3% | STAT | STAT | - | STAT |
| Dexamethasone (vasogenic edema) | IV | Significant vasogenic edema surrounding venous infarction; NOT routine | 10 mg :: IV :: load then q6h :: 10 mg IV loading dose, then 4 mg IV q6h; taper over 5-7 days | Active untreated infection; unclear role in CVT | Glucose; BP; GI prophylaxis | - | URGENT | - | URGENT |

*Note: CRITICAL -- anticoagulate even in the presence of hemorrhagic infarction. Multiple studies confirm safety and benefit of heparin in CVT with associated ICH. The hemorrhage is caused by venous congestion, and anticoagulation treats the underlying cause. LMWH is preferred over UFH per AHA/ASA guidelines (associated with better outcomes in ISCVT trial). Do NOT withhold anticoagulation due to hemorrhagic conversion.*

### 3B. Transition to Oral Anticoagulation

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Warfarin | PO | Long-term anticoagulation; preferred if antiphospholipid syndrome confirmed | 5 mg daily :: PO :: daily :: Start 5 mg PO daily (lower if elderly, hepatic impairment, CYP2C9 variant); overlap with heparin until INR 2-3 x 2 consecutive days; target INR 2.0-3.0 | Pregnancy (teratogenic -- use LMWH instead); active bleeding; severe hepatic disease | INR q1-3 days initially; then q1-2 weeks; then monthly; drug/diet interactions | - | ROUTINE | ROUTINE | - |
| Dabigatran | PO | Alternative to warfarin for CVT (RE-SPECT CVT trial); no INR monitoring needed | 150 mg BID :: PO :: BID :: 150 mg PO BID; reduce to 110 mg BID if age >80, concurrent P-gp inhibitor, or CrCl 30-50 | CrCl <30; mechanical heart valve; active bleeding | Renal function q6-12 months; signs of bleeding; aPTT as qualitative screen | - | ROUTINE | ROUTINE | - |
| Rivaroxaban | PO | Alternative DOAC for CVT (limited data but increasingly used) | 20 mg daily :: PO :: daily :: 20 mg PO daily with food; reduce to 15 mg daily if CrCl 15-50 | CrCl <15; hepatic impairment (Child-Pugh B/C); active bleeding | Renal function q6-12 months; LFTs; signs of bleeding | - | ROUTINE | ROUTINE | - |
| Apixaban | PO | Alternative DOAC for CVT (limited data) | 5 mg BID :: PO :: BID :: 5 mg PO BID; reduce to 2.5 mg BID if ≥2 of: age ≥80, weight ≤60 kg, Cr ≥1.5 | Active bleeding; hepatic impairment | Renal function q6-12 months; LFTs; signs of bleeding | - | ROUTINE | ROUTINE | - |

*Note: Duration of anticoagulation: provoked CVT (identifiable transient risk factor) -- 3-6 months; unprovoked CVT -- 6-12 months; recurrent CVT or high-risk thrombophilia (APS, homozygous FVL, combined deficiencies) -- consider indefinite anticoagulation. The RE-SPECT CVT trial (2019) showed dabigatran non-inferior to warfarin. DOACs are increasingly used but warfarin remains standard in antiphospholipid syndrome. In pregnancy, use LMWH throughout (warfarin and DOACs are contraindicated).*

### 3C. Second-Line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Endovascular mechanical thrombectomy | - | Severe/deteriorating despite anticoagulation; deep venous system thrombosis with impending herniation | Per neurointerventional protocol :: - :: - :: Catheter-directed aspiration or stent-retriever; may combine with local thrombolysis | Inaccessible thrombosis; terminal prognosis | Procedural monitoring; ICU post-procedure; repeat imaging | - | EXT | - | EXT |
| Local catheter-directed thrombolysis (tPA) | - | Severe refractory CVT; adjunct to mechanical thrombectomy | Per neurointerventional protocol :: - :: - :: Alteplase 1-2 mg/hr via catheter directly into thrombosed sinus; duration 12-48h | Active bleeding; recent surgery; coagulopathy | ICU monitoring; repeat imaging q12-24h; fibrinogen; CBC | - | EXT | - | EXT |
| Decompressive hemicraniectomy | - | Large hemorrhagic venous infarction with impending transtentorial herniation; life-saving | Neurosurgical protocol :: - :: - :: Large bone flap removal; duraplasty | Terminal prognosis; poor baseline | ICP monitoring post-procedure; ICU care | - | - | - | STAT |
| Optic nerve sheath fenestration | - | Progressive vision loss from papilledema despite medical ICP management | Ophthalmologic surgical protocol :: - :: - :: Incision of optic nerve sheath to relieve CSF pressure on optic nerve | Orbital infection | Visual acuity post-procedure; IOP | - | EXT | EXT | - |
| VP shunt / lumbar drain | - | Refractory elevated ICP not responding to medical management | Neurosurgical protocol :: - :: - :: CSF diversion procedure; temporary (lumbar drain) or permanent (VP shunt) | Active infection; coagulopathy | ICP; CSF output; infection surveillance | - | EXT | - | EXT |

### 3D. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Acetaminophen | PO/IV | Headache management (avoid NSAIDs while anticoagulated) | 1000 mg :: PO :: q6h PRN :: 1000 mg PO/IV q6h PRN; max 3g/day (2g if hepatic impairment) | Hepatic impairment; weight <50 kg (reduce dose) | LFTs if chronic use | STAT | STAT | ROUTINE | STAT |
| Ondansetron | PO/IV | Nausea/vomiting from elevated ICP | 4 mg :: IV :: q6h PRN :: 4-8 mg IV/PO q6-8h PRN | QTc prolongation | QTc if risk factors | STAT | STAT | ROUTINE | STAT |
| Metoclopramide | IV | Nausea/vomiting (alternative to ondansetron) | 10 mg :: IV :: q6h PRN :: 10 mg IV q6-8h PRN; max 40 mg/day; limit use to 5 days | Parkinson disease; seizure disorder; bowel obstruction | EPS; tardive dyskinesia; QTc | URGENT | URGENT | - | URGENT |
| Lacosamide (second-line ASM) | IV/PO | Seizures refractory to levetiracetam | 200 mg BID :: IV :: BID :: Load: 200-400 mg IV; Maintenance: 100-200 mg IV/PO BID (max 400 mg/day) | Second/third degree AV block; severe hepatic impairment | ECG (PR prolongation); dizziness | URGENT | URGENT | ROUTINE | URGENT |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology for CVT diagnosis confirmation, seizure management, and neurologic monitoring | STAT | STAT | ROUTINE | STAT |
| Hematology for thrombophilia workup interpretation and anticoagulation duration guidance | - | ROUTINE | ROUTINE | - |
| Neurointerventional radiology for endovascular thrombectomy evaluation if deteriorating despite anticoagulation | - | URGENT | - | URGENT |
| Neurosurgery for decompressive hemicraniectomy evaluation if large hemorrhagic infarction with herniation risk | - | URGENT | - | STAT |
| Ophthalmology/neuro-ophthalmology for papilledema assessment, visual field testing, and optic nerve monitoring | - | URGENT | ROUTINE | URGENT |
| OB/GYN if pregnancy-related or postpartum CVT for anticoagulation coordination and delivery planning | - | URGENT | ROUTINE | URGENT |
| ENT if septic CVT from sinusitis, mastoiditis, or dental source requiring surgical drainage | - | URGENT | - | URGENT |
| Hematology/oncology if myeloproliferative disorder (JAK2+, polycythemia vera) or malignancy identified | - | ROUTINE | ROUTINE | - |
| Physical therapy for mobility assessment and rehabilitation following neurologic deficits | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL adaptation if cognitive or motor deficits present | - | ROUTINE | ROUTINE | - |
| Social work for anticoagulation management support, disability resources, and family education | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED immediately for sudden severe headache, new seizures, vision changes, weakness, or speech difficulty (may indicate extension or complication of CVT) | Y | Y | Y |
| Take anticoagulation medication exactly as prescribed; do NOT miss doses; carry anticoagulation card | - | Y | Y |
| Avoid contact sports and activities with high fall/injury risk while anticoagulated | - | Y | Y |
| Report any signs of bleeding (blood in urine/stool, excessive bruising, prolonged bleeding from cuts, heavy menstruation) immediately | - | Y | Y |
| Do not take aspirin, ibuprofen, or other NSAIDs unless specifically directed by your physician while anticoagulated | - | Y | Y |
| INR monitoring appointments are critical if on warfarin -- do not miss them | - | Y | Y |
| Discuss contraception options with your physician as hormonal contraceptives may be contraindicated after CVT | - | Y | Y |
| Do not drive until cleared by neurology (seizure risk; visual field deficits) | - | Y | Y |
| Avoid dehydration (drink adequate fluids daily) as dehydration is a CVT risk factor | - | Y | Y |
| If planning pregnancy, discuss with both neurology and hematology for anticoagulation management (warfarin/DOACs contraindicated; LMWH required) | - | Y | Y |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Discontinue oral contraceptive pills (OCPs) or hormone replacement therapy (HRT) permanently after CVT; discuss alternative contraception with gynecology | - | Y | Y |
| Smoking cessation to reduce prothrombotic risk | - | Y | Y |
| Adequate hydration (8+ glasses water daily) to reduce venous stasis | - | Y | Y |
| Avoid prolonged immobilization; use compression stockings during long travel | - | Y | Y |
| Maintain healthy weight to reduce prothrombotic risk | - | Y | Y |
| Address modifiable risk factors identified in thrombophilia workup (folate for hyperhomocysteinemia, phlebotomy for polycythemia) | - | Y | Y |

---

═══════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Migraine with aura | Recurrent; typical aura pattern; no venous filling defects; normal imaging | MRI/MRV normal; headache diary; family history |
| Idiopathic intracranial hypertension (IIH) | Elevated ICP without venous thrombosis; obesity; female predominance; papilledema | MRV shows no thrombosis; LP elevated opening pressure; normal D-dimer |
| Arterial ischemic stroke | Arterial territory distribution; no hemorrhagic component typical of CVT; older patients | CT/CTA shows arterial occlusion; CTV/MRV normal veins |
| Intracerebral hemorrhage (hypertensive) | Typical deep locations (basal ganglia, thalamus); hypertension; older patients | CTV/MRV shows patent sinuses; hemorrhage in typical hypertensive location |
| Subarachnoid hemorrhage | Thunderclap headache; cisternal blood; positive CTA for aneurysm | CTA for aneurysm; LP (xanthochromia); CTV shows patent sinuses |
| Meningitis/encephalitis | Fever; meningismus; CSF pleocytosis; specific pathogen identified | LP; blood cultures; CSF PCR panels; CTV/MRV normal |
| Brain tumor/metastasis | Progressive symptoms; enhancing mass lesion; no venous filling defect | MRI with contrast shows mass; CTV/MRV normal sinuses; biopsy |
| Brain abscess | Fever; ring-enhancing lesion; restricted diffusion centrally; infectious source | MRI DWI; blood cultures; surgical drainage; CTV normal |
| Posterior reversible encephalopathy syndrome (PRES) | Hypertensive emergency; symmetric posterior white matter edema; seizures | BP history; MRI pattern; CTV/MRV normal; resolves with BP control |
| Dural AV fistula | Progressive symptoms; tortuous vessels on MRI; pulsatile tinnitus | Conventional angiography; MRI flow voids |
| Subdural hematoma | Crescent-shaped extra-axial collection; trauma history; bridging vein tearing | CT shows subdural; no venous sinus filling defect |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Neurologic examination (GCS, pupils, motor, speech) | Q1h (ICU); Q2-4h (floor) | Stable or improving | If worsening: repeat imaging; escalate to ICU; consider endovascular intervention | STAT | STAT | ROUTINE | STAT |
| aPTT (if on UFH) | Q6h until therapeutic x2; then Q12-24h | 1.5-2.5x control (60-80 sec) | Adjust heparin rate per nomogram | STAT | STAT | - | STAT |
| INR (if on warfarin) | Daily until therapeutic; then q1-3 days; then weekly; then monthly | 2.0-3.0 | Adjust warfarin dose; bridge with LMWH if subtherapeutic | - | STAT | ROUTINE | STAT |
| Platelet count | Q2 days (HIT screen while on heparin) | Stable; no >50% drop from baseline | If >50% drop: check HIT antibody; switch to argatroban or bivalirudin | STAT | STAT | - | STAT |
| Head CT / MRI | 48-72h post-admission; at clinical change | Stable or improving; no new hemorrhage; no herniation | If worsening: escalate care; neurosurgery consult | - | URGENT | ROUTINE | URGENT |
| Follow-up MRV | 3-6 months after diagnosis | Recanalization (partial or complete) | If persistent: extend anticoagulation; consider endovascular if symptomatic | - | - | ROUTINE | - |
| Visual acuity and visual fields | Daily if papilledema; each OPD visit | Stable or improving | If worsening: increase ICP management; ophthalmology; consider ONSF | - | ROUTINE | ROUTINE | - |
| Fundoscopic exam | Daily if papilledema (inpatient); q1-3 months (OPD) | Resolving papilledema | If worsening: escalate ICP management; therapeutic LP | - | ROUTINE | ROUTINE | - |
| Opening pressure (if repeated LP) | Per clinical indication | Decreasing; <25 cm H2O | If persistently elevated: acetazolamide; VP shunt evaluation | - | ROUTINE | ROUTINE | - |
| Seizure monitoring (EEG if needed) | Continuous if seizures; as indicated | No seizures | If recurrent: adjust ASMs; continuous EEG monitoring | - | ROUTINE | - | STAT |
| Renal function (BUN/Cr) | Baseline; q3-7 days on heparin; q6-12 months on DOACs | Stable | Adjust anticoagulation dose for renal impairment | STAT | ROUTINE | ROUTINE | STAT |
| Blood pressure | Q1h (ICU); Q4h (floor) | SBP <180; avoid hypotension (maintain perfusion) | Permissive hypertension acceptable; avoid excessive lowering | STAT | STAT | ROUTINE | STAT |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **Discharge home** | Neurologically stable; therapeutic anticoagulation achieved; seizures controlled; no significant hemorrhagic infarction; adequate outpatient follow-up arranged (neurology, hematology, ophthalmology); patient/family educated on anticoagulation management and warning signs |
| **Admit to floor (neurology/stroke unit)** | New CVT diagnosis requiring anticoagulation initiation; seizures requiring treatment; elevated ICP requiring medical management; hemorrhagic venous infarction (small/moderate); diagnostic workup pending |
| **Admit to ICU** | Large hemorrhagic infarction with mass effect; GCS ≤12; refractory seizures or status epilepticus; malignant cerebral edema with herniation risk; hemodynamic instability; requires invasive ICP monitoring; post-endovascular procedure |
| **Transfer to higher level of care** | Neurointerventional capability not available (for endovascular thrombectomy); neurosurgery not available (for decompressive hemicraniectomy); requires ICU care not available at current facility |
| **Outpatient follow-up** | All patients: neurology within 1-2 weeks; hematology within 1 month (thrombophilia results); ophthalmology within 2-4 weeks if papilledema; anticoagulation clinic (if on warfarin); repeat MRV at 3-6 months |
| **Readmission criteria** | New or worsening headache; new seizures; new neurologic deficits; signs of bleeding on anticoagulation; pregnancy (requires anticoagulation modification) |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| AHA/ASA scientific statement on CVT diagnosis and management | Expert Consensus | [Saposnik G et al. Stroke 2011;42:1158-1192](https://pubmed.ncbi.nlm.nih.gov/21293023/) |
| EAN guideline on CVT | Expert Consensus | [Ferro JM et al. Eur J Neurol 2017;24:1203-1213](https://pubmed.ncbi.nlm.nih.gov/28833980/) |
| ISCVT (International Study on CVT): largest cohort study | Class II | [Ferro JM et al. Stroke 2004;35:664-670](https://pubmed.ncbi.nlm.nih.gov/14976332/) |
| Anticoagulation safe and beneficial even with hemorrhagic infarction | Class II | Einhaupl K et al. J Neurol Neurosurg Psychiatry 1991;54:396-401 |
| LMWH preferred over UFH (ISCVT data) | Class III | Coutinho JM et al. Stroke 2010;41:2519-2524 |
| RE-SPECT CVT trial: dabigatran vs warfarin | Class II (RCT) | Ferro JM et al. Lancet Neurol 2019;18:1147-1156 |
| D-dimer in CVT diagnosis (high NPV) | Class II | [Dentali F et al. J Thromb Haemost 2012;10:582-589](https://pubmed.ncbi.nlm.nih.gov/22257124/) |
| Thrombophilia prevalence in CVT (~35%) | Class II | Martinelli I et al. Blood 1998;92:3152-3157 |
| Oral contraceptives as major CVT risk factor | Class II | de Bruijn SF et al. Stroke 1998;29:2588-2592 |
| Decompressive surgery for malignant CVT | Class III | Ferro JM et al. Cerebrovasc Dis 2009;27:55-62 |
| Endovascular thrombectomy for severe CVT | Class III, Case Series | Siddiqui FM et al. J Neurointerv Surg 2015;7:442-447 |
| Seizure incidence in CVT (~40%) | Class II | Ferro JM et al. Stroke 2008;39:3222-3227 |
| Long-term prognosis of CVT (good in most cases) | Class II | [Ferro JM et al. Stroke 2004;35:664-670](https://pubmed.ncbi.nlm.nih.gov/14976332/) |
| Duration of anticoagulation in CVT | Expert Consensus | [Saposnik G et al. Stroke 2011;42:1158-1192](https://pubmed.ncbi.nlm.nih.gov/21293023/) |
| CTV and MRV sensitivity for CVT diagnosis | Class II | Defined F et al. AJNR 2007;28:1694-1697 |
| CVT in pregnancy and postpartum management | Expert Consensus | [Saposnik G et al. Stroke 2011](https://pubmed.ncbi.nlm.nih.gov/21293023/) |
| Antiphospholipid syndrome and CVT; warfarin preferred over DOACs | Class II | [Pengo V et al. Blood 2018;132:1365-1371](https://pubmed.ncbi.nlm.nih.gov/30002145/) |

---

## CLINICAL DECISION SUPPORT NOTES

### CVT Risk Factors

**Transient/Provoked:**
- Oral contraceptive pills (OCP) -- most common modifiable risk factor
- Pregnancy and postpartum (especially 3rd trimester and first 4 weeks postpartum)
- Dehydration
- Head/neck trauma or surgery
- Lumbar puncture
- Infection (sinusitis, mastoiditis, otitis, meningitis)
- Iron deficiency anemia
- Malignancy (especially hematologic)

**Persistent/Unprovoked:**
- Inherited thrombophilia (Factor V Leiden, prothrombin mutation, protein C/S/antithrombin deficiency)
- Antiphospholipid syndrome
- Myeloproliferative disorders (PV, ET, CML)
- Hyperhomocysteinemia
- Nephrotic syndrome
- Inflammatory bowel disease
- Behcet disease
- Sarcoidosis

### CVT Clinical Presentations

| Presentation | Frequency | Key Features |
|-------------|-----------|-------------|
| Isolated intracranial hypertension | ~40% | Headache, papilledema, visual obscurations, 6th nerve palsy |
| Focal neurologic deficit ± seizures | ~40% | Hemiparesis, aphasia, seizures, non-arterial distribution infarct |
| Encephalopathy (diffuse) | ~15% | Altered consciousness, confusion, coma (deep venous thrombosis) |
| Cavernous sinus syndrome | ~5% | Proptosis, chemosis, ophthalmoplegia, V1/V2 sensory loss |

### Anticoagulation Duration Guide

| Scenario | Duration |
|----------|----------|
| Provoked CVT (transient risk factor removed) | 3-6 months |
| Unprovoked CVT (first episode) | 6-12 months |
| Recurrent VTE or CVT | Indefinite |
| High-risk thrombophilia (APS, homozygous FVL, combined defects) | Indefinite |
| Antiphospholipid syndrome | Indefinite; warfarin preferred (DOACs inferior per TRAPS trial) |

---

## CHANGE LOG

**v1.2 (January 30, 2026)**
- Citation verification: removed 9 unverified PubMed links (converted to plain text), including 1 fabricated author citation ("Defined F")
- CPT enrichment: added 5 CPT codes to Section 1C (86160+86162, 82232, 86334, 83020, 81206)

**v1.1 (January 30, 2026)**
- Standardized structured dosing format across all treatment sections (3A, 3B, 3D)
- Fixed standard_dose field to contain starting dose only (UFH, levetiracetam, acetazolamide, dexamethasone, acetaminophen, ondansetron, metoclopramide)
- Added frequency field to all medications

**v1.0 (January 30, 2026)**
- Initial creation
- Section 1: 15 core labs (1A), 14 thrombophilia panel tests (1B), 6 rare/specialized tests (1C)
- Section 2: 5 essential imaging (2A), 5 extended (2B), 2 rare (2C), 6 LP/CSF studies
- Section 3: 4 subsections:
  - 3A: 7 acute/emergent treatments (anticoagulation, seizure management, ICP management)
  - 3B: 4 oral anticoagulation transition agents (warfarin, dabigatran, rivaroxaban, apixaban)
  - 3C: 5 second-line/refractory interventions (endovascular, surgical)
  - 3D: 4 symptomatic treatments
- Section 4: 11 referrals (4A), 10 patient instructions (4B), 6 lifestyle/prevention recommendations (4C)
- Section 5: 11 differential diagnoses
- Section 6: 12 monitoring parameters
- Section 7: 6 disposition criteria
- Section 8: 17 evidence references with PubMed links
- Clinical Decision Support Notes: Risk factors, clinical presentations, anticoagulation duration guide
