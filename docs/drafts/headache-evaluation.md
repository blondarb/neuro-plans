---
title: "Headache Evaluation"
description: "Clinical decision support for systematic headache evaluation including red flag identification, primary vs secondary headache classification, and diagnostic workup algorithm"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - headache
  - headache-evaluation
  - diagnostic-workup
  - red-flags
  - emergency
  - outpatient
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Headache Evaluation

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Validated per checker pipeline

---

**DIAGNOSIS:** Headache Evaluation / Undifferentiated Headache

**ICD-10:** R51.9 (Headache, unspecified), R51.0 (Headache with orthostatic component), G44.1 (Vascular headache, not elsewhere classified), G44.209 (Tension-type headache, unspecified, not intractable), G44.89 (Other headache syndrome), G44.52 (New daily persistent headache), G43.909 (Migraine, unspecified, not intractable), G44.009 (Cluster headache syndrome, unspecified), G44.319 (Post-traumatic headache, unspecified, not intractable), R51 (Headache)

**CPT CODES:** 99281-99285 (ED E/M), 99202-99205 (New outpatient visit), 99212-99215 (Established outpatient visit), 99252-99255 (Inpatient consult), 70450 (CT head without contrast), 70551 (MRI brain without contrast), 70553 (MRI brain with and without contrast), 70544 (MRA head without contrast), 70496 (CTA head), 70498 (CTA neck), 62270 (Lumbar puncture, diagnostic), 85025 (CBC), 80053 (CMP), 85652 (ESR), 86140 (CRP)

**SYNONYMS:** Headache, cephalgia, cephalalgia, head pain, cranial pain, headache disorder, new headache, acute headache, worst headache of life, thunderclap headache, new-onset headache, chronic headache, daily headache, undifferentiated headache, headache workup, headache evaluation, secondary headache, primary headache, undiagnosed headache, red flag headache, emergent headache

**SCOPE:** Systematic evaluation and diagnostic workup of undifferentiated headache in adults. Covers red flag identification (SNOOP mnemonic), primary vs secondary headache classification, indications for neuroimaging and lumbar puncture, and initial symptomatic management during workup. This is a DIAGNOSTIC EVALUATION plan, not a treatment plan for a specific headache type. Once a specific diagnosis is established, transition to the appropriate condition-specific plan (migraine, cluster headache, SAH, meningitis, etc.).

---

**DEFINITIONS:**
- **Primary Headache:** Headache disorder without underlying structural, metabolic, or infectious cause (migraine, tension-type, cluster, other trigeminal autonomic cephalalgias)
- **Secondary Headache:** Headache attributable to an underlying disorder (SAH, meningitis, mass lesion, vascular dissection, venous thrombosis, medication overuse, etc.)
- **Thunderclap Headache:** Severe headache reaching maximum intensity within seconds to 1 minute; must be assumed to be subarachnoid hemorrhage until proven otherwise
- **SNOOP Mnemonic:** Red flag screening tool: **S**ystemic symptoms/secondary risk factors, **N**eurologic symptoms or abnormal signs, **O**nset sudden (thunderclap), **O**lder age (new onset >50 years), **P**revious headache history (first, worst, or change in pattern)
- **New Daily Persistent Headache (NDPH):** Headache occurring daily and unremitting from onset (or within 24 hours), with clear onset date recalled by patient

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC (CPT 85025) | Rule out anemia, infection, thrombocytopenia; baseline before LP | Normal WBC, Hgb, platelets | STAT | ROUTINE | ROUTINE | STAT |
| CMP (CPT 80053) | Electrolyte abnormalities, renal function, hepatic function; metabolic causes of headache | Normal | STAT | ROUTINE | ROUTINE | STAT |
| hCG (women of childbearing age) (CPT 84703) | Pregnancy status affects imaging choices (CT radiation) and treatment options | Document status | STAT | STAT | ROUTINE | STAT |
| ESR (CPT 85652) | Screen for giant cell arteritis if age >50, new headache, temporal tenderness | <20 mm/hr (age-adjusted: age/2 for men; (age+10)/2 for women) | STAT | ROUTINE | ROUTINE | STAT |
| CRP (CPT 86140) | Inflammatory marker; supports GCA evaluation; infection screen | <3.0 mg/L | STAT | ROUTINE | ROUTINE | STAT |
| Coagulation studies (PT/INR, PTT) (CPT 85610, 85730) | Baseline before LP; assess bleeding risk in suspected hemorrhage | Normal PT/INR, PTT | STAT | ROUTINE | - | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| TSH (CPT 84443) | Thyroid dysfunction can cause or exacerbate headache | 0.4-4.0 mIU/L | - | ROUTINE | ROUTINE | - |
| Magnesium (CPT 83735) | Low magnesium associated with headache disorders; may guide supplementation | >1.8 mg/dL | URGENT | ROUTINE | ROUTINE | URGENT |
| Vitamin D, 25-hydroxy (CPT 82306) | Deficiency associated with chronic headache disorders | >30 ng/mL | - | ROUTINE | ROUTINE | - |
| Procalcitonin (CPT 84145) | Differentiate bacterial vs viral etiology when meningitis suspected | <0.5 ng/mL | URGENT | URGENT | - | URGENT |
| Blood cultures x2 (CPT 87040) | If meningitis or systemic infection suspected; obtain before antibiotics | No growth | STAT | STAT | - | STAT |
| Lactate (CPT 83605) | Sepsis screen if infectious etiology suspected | <2.0 mmol/L | STAT | URGENT | - | STAT |
| Carboxyhemoglobin (CPT 82375) | Carbon monoxide poisoning can present as headache; especially with multiple household members affected | <3% (nonsmoker); <10% (smoker) | STAT | URGENT | - | STAT |

### 1C. Rare/Specialized

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| ANA (CPT 86235) | If vasculitis or autoimmune cause suspected | Negative | - | EXT | EXT | - |
| ANCA panel (CPT 86235, 86236) | If CNS vasculitis suspected | Negative | - | EXT | EXT | - |
| ACE level (CPT 82164) | If neurosarcoidosis suspected | Normal (8-52 U/L) | - | EXT | EXT | - |
| Hypercoagulability panel (CPT 85306, 85300, 85613, 86147) | If cerebral venous thrombosis suspected (young patient, risk factors) | Normal | - | EXT | EXT | - |
| Pheochromocytoma workup (plasma metanephrines) (CPT 83835) | Paroxysmal headache with hypertension, diaphoresis, palpitations | Normal | - | EXT | EXT | - |
| RPR/VDRL (CPT 86592) | If neurosyphilis suspected (risk factors, cranial neuropathies) | Nonreactive | - | EXT | EXT | - |
| HIV (CPT 87389) | If immunosuppression suspected; opportunistic CNS infections | Negative | - | EXT | ROUTINE | - |
| Lyme antibodies (CPT 86618) | If endemic area and cranial neuropathy, meningitis | Negative | - | EXT | EXT | - |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast (CPT 70450) | Immediate if: thunderclap headache, worst headache of life, focal neurologic deficits, altered mental status, papilledema, anticoagulated patient, trauma, immunocompromised, fever with meningismus | Rule out hemorrhage, mass, hydrocephalus, midline shift | None in emergency; pregnancy relative (discuss risk/benefit) | STAT | STAT | - | STAT |
| MRI brain without contrast (CPT 70551) | New headache pattern, progressive headache, persistent headache without clear primary diagnosis, abnormal neurologic exam without acute emergency | Rule out mass, demyelination, Chiari, structural cause | Pacemaker, ferromagnetic implants, severe claustrophobia | - | ROUTINE | ROUTINE | - |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| MRI brain with and without contrast (CPT 70553) | Suspected mass, infection, inflammation, leptomeningeal disease, pituitary pathology | Rule out enhancing lesion, abscess, meningeal enhancement | Contrast allergy, GFR <30, pregnancy | URGENT | ROUTINE | ROUTINE | URGENT |
| CTA head (CPT 70496) | Thunderclap headache with negative CT; suspected aneurysm, dissection, or vasculopathy | Rule out aneurysm, dissection, vasospasm | Contrast allergy, renal insufficiency | STAT | URGENT | - | STAT |
| CTA neck (CPT 70498) | Suspected cervical artery dissection (neck pain, Horner syndrome, young stroke) | Rule out dissection, stenosis | Contrast allergy, renal insufficiency | STAT | URGENT | - | STAT |
| MRA head (CPT 70544) | Suspected vasculopathy, aneurysm, vasculitis (non-emergent or contrast contraindicated) | Normal vasculature; no aneurysm, stenosis, or irregularity | Pacemaker, ferromagnetic implants | - | ROUTINE | ROUTINE | - |
| MRV (CPT 70546) or CT venogram (CPT 70496) | Suspected cerebral venous thrombosis (headache + papilledema, pregnancy/postpartum, hypercoagulable state, OCP use) | Patent venous sinuses | Per modality | URGENT | URGENT | ROUTINE | URGENT |
| MRA neck (CPT 70547) | Suspected cervical artery dissection (when CTA contraindicated) | Normal cervical vasculature | Pacemaker, ferromagnetic implants | - | ROUTINE | ROUTINE | - |
| CT head with contrast (CPT 70460) | If MRI unavailable and mass or infection suspected | Rule out enhancing lesion | Contrast allergy, renal insufficiency | URGENT | URGENT | - | URGENT |
| ECG (CPT 93000) | Before administering triptans, DHE, or antiemetics (QTc assessment) | Normal sinus rhythm, QTc <470 ms | None | STAT | STAT | ROUTINE | STAT |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Conventional cerebral angiography (CPT 36224) | Suspected CNS vasculitis with negative noninvasive imaging; confirmed aneurysm for intervention planning | Vessel wall irregularity, beading (vasculitis); aneurysm morphology | Contrast allergy (premedicate), renal insufficiency, coagulopathy | - | EXT | EXT | - |
| High-resolution vessel wall MRI | Suspected intracranial vasculitis, RCVS, or dissection when CTA/MRA inconclusive | Concentric enhancement (vasculitis) vs non-enhancing (RCVS) | Standard MRI contraindications | - | EXT | EXT | - |
| CT temporal bones (CPT 70480) | Headache with pulsatile tinnitus, suspected CSF leak, skull base pathology | Rule out tegmen dehiscence, mastoid disease | Pregnancy (relative) | - | EXT | EXT | - |
| Fundoscopic exam / Optic nerve sheath ultrasound | Screen for papilledema when fundoscopy unavailable or pupil dilation contraindicated | Optic nerve sheath diameter <5 mm (normal); >5.8 mm suggests elevated ICP | None | STAT | STAT | ROUTINE | STAT |

### LUMBAR PUNCTURE (CPT 62270)

**Indication:** Thunderclap headache with negative CT head (rule out SAH); suspected meningitis/encephalitis; suspected IIH (papilledema, visual obscurations); suspected CNS vasculitis; suspected leptomeningeal disease; new daily persistent headache of unclear etiology; headache with fever and meningismus

**Timing:** URGENT after CT head excludes mass effect. For suspected SAH: perform within 12 hours of headache onset for maximum xanthochromia sensitivity (peaks 12 hours post-bleed)

**Volume Required:** 10-15 mL standard diagnostic; 30-40 mL if therapeutic (IIH)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure (CPT 89050) | Diagnose elevated ICP (IIH) or low pressure (CSF leak/spontaneous intracranial hypotension) | 10-20 cm H2O (elevated >25 suggests IIH; <6 suggests low-pressure headache) | STAT | STAT | ROUTINE | STAT |
| Cell count (tubes 1 and 4) (CPT 89051) | Detect infection (WBC), hemorrhage (RBC); tube 1 vs 4 comparison for traumatic vs true hemorrhage | WBC <5/uL; RBC 0; clearing RBC count (traumatic tap) vs stable (SAH) | STAT | STAT | ROUTINE | STAT |
| Protein (CPT 84157) | Elevated in infection, inflammation, malignancy, GBS | 15-45 mg/dL | STAT | STAT | ROUTINE | STAT |
| Glucose with simultaneous serum glucose (CPT 82945) | Low CSF/serum ratio in bacterial meningitis, TB meningitis, malignancy | CSF glucose >60% of serum glucose | STAT | STAT | ROUTINE | STAT |
| Xanthochromia (visual or spectrophotometric) | Detect SAH when CT head negative; xanthochromia develops 2-12 hours after bleed | Negative (clear, colorless CSF) | STAT | STAT | - | STAT |
| Gram stain and culture (CPT 87205, 87070) | Identify bacterial pathogen in suspected meningitis | No organisms; no growth | STAT | STAT | - | STAT |
| CSF meningitis/encephalitis panel (BioFire) (CPT 87483) | Rapid multiplex PCR for bacterial, viral, fungal pathogens | Negative | URGENT | URGENT | - | URGENT |
| Cytology (CPT 88108) | Suspected leptomeningeal carcinomatosis (progressive headache, cranial neuropathies, known malignancy) | No malignant cells | - | URGENT | EXT | - |
| Oligoclonal bands (CPT 83916) | Suspected MS or other demyelinating disease | Absent (or matched to serum) | - | ROUTINE | ROUTINE | - |
| VDRL CSF (CPT 86593) | Suspected neurosyphilis | Nonreactive | - | EXT | EXT | - |
| AFB culture (CPT 87116) | Suspected TB meningitis (subacute headache, basilar meningitis, immunocompromised) | No growth | - | URGENT | EXT | - |
| Fungal culture (CPT 87102) / Cryptococcal antigen (CPT 87899) | Suspected fungal meningitis (immunocompromised, subacute course) | Negative | URGENT | URGENT | EXT | URGENT |

**Special Handling:** Xanthochromia sample must be protected from light and processed within 1 hour. Cell count requires tubes 1 AND 4 for traumatic tap vs SAH differentiation. Send CSF glucose with simultaneous serum glucose.

**Contraindications:** Mass effect on CT (risk of herniation), coagulopathy (INR >1.5, platelets <50,000), overlying skin infection at LP site, epidural abscess

---

## 3. TREATMENT

*Note: This section covers symptomatic management during diagnostic evaluation. Once a specific headache diagnosis is established, transition to the appropriate condition-specific treatment plan.*

### 3A. Acute Symptomatic Treatment - First-Line

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Acetaminophen | PO/IV | Mild-moderate headache pain during workup | 1000 mg :: PO :: once :: 1000 mg PO/IV once; may repeat q6h; max 3000 mg/day | Hepatic disease, chronic alcohol use (>3 drinks/day) | LFTs if frequent use | STAT | ROUTINE | ROUTINE | STAT |
| Ibuprofen | PO | Mild-moderate headache pain during workup | 400-800 mg :: PO :: once :: 400-800 mg PO once; may repeat q6h; max 2400 mg/day | Renal disease, GI bleeding history, aspirin allergy, third trimester pregnancy | Renal function, GI symptoms | STAT | ROUTINE | ROUTINE | - |
| Ketorolac | IV/IM | Moderate-severe headache pain during workup | 30 mg :: IV :: once :: 30 mg IV once (15 mg if >65y, CrCl <50, or weight <50 kg); max 2 doses in 24h | Renal disease (CrCl <30), active GI bleeding, anticoagulation, third trimester pregnancy | Renal function, bleeding | STAT | STAT | - | STAT |
| Naproxen sodium | PO | Mild-moderate headache pain during workup | 500-825 mg :: PO :: once :: 500-825 mg PO once; may repeat 250-500 mg in 6-8h; max 1250 mg first day | Renal disease, GI bleeding history, aspirin allergy, third trimester pregnancy | Renal function, GI symptoms | - | ROUTINE | ROUTINE | - |

### 3B. Acute Symptomatic Treatment - Antiemetics / Headache Cocktail

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Prochlorperazine (CPT 96374) | IV | Moderate-severe headache with nausea; dopamine-mediated headache relief | 10 mg :: IV :: once :: 10 mg IV slow push over 5-10 min; may repeat once in 30 min | QT prolongation, Parkinson disease, history of dystonic reaction | QTc, akathisia, dystonic reaction | STAT | STAT | - | STAT |
| Metoclopramide | IV | Moderate-severe headache with nausea; alternative to prochlorperazine | 10-20 mg :: IV :: once :: 10-20 mg IV over 15-30 min; may repeat once in 30 min | QT prolongation, Parkinson disease, seizure disorder, bowel obstruction | QTc, akathisia, dystonic reaction | STAT | STAT | - | STAT |
| Diphenhydramine | IV | Prevention of akathisia/dystonia from dopamine antagonist antiemetics | 25-50 mg :: IV :: once :: 25-50 mg IV push (co-administer with prochlorperazine or metoclopramide) | Glaucoma, urinary retention, elderly (increased sedation risk) | Sedation level | STAT | STAT | - | STAT |
| Ondansetron | IV/PO | Nausea/vomiting when dopamine antagonists contraindicated (Parkinson, QTc prolongation) | 4-8 mg :: IV :: once :: 4-8 mg IV/PO once; may repeat q8h | QT prolongation (dose-dependent), serotonin syndrome risk with concurrent serotonergic drugs | QTc | URGENT | ROUTINE | ROUTINE | URGENT |
| Dexamethasone | IV | Reduce headache recurrence; anti-inflammatory effect for suspected inflammatory etiology | 10 mg :: IV :: once :: 10 mg IV once (reduces 24-72h headache recurrence) | Active untreated infection, uncontrolled diabetes (relative), psychosis (relative) | Glucose, blood pressure | URGENT | URGENT | - | URGENT |

### 3C. IV Fluids and Supportive Care

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IV normal saline | IV | Dehydration contributing to headache; pre-procedure hydration (LP); NPO status | 1000 mL :: IV :: bolus then continuous :: NS 1L bolus over 1h, then 75-125 mL/hr maintenance | Decompensated heart failure, severe volume overload | Intake/output, daily weights if admitted | STAT | STAT | - | STAT |
| Magnesium sulfate (CPT 96365) | IV | Low magnesium; adjunctive headache treatment especially if migraine suspected | 2 g :: IV :: once :: 2 g IV in 100 mL NS over 20-30 min | Renal failure (GFR <30), myasthenia gravis, heart block | Magnesium level, deep tendon reflexes, respiratory status | URGENT | URGENT | - | URGENT |

### 3D. Empiric Treatment When Secondary Cause Suspected

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Ceftriaxone | IV | Empiric meningitis coverage pending CSF results (give BEFORE LP if delay anticipated) | 2 g :: IV :: q12h :: 2 g IV q12h (meningitis dosing); give STAT if bacterial meningitis suspected | Cephalosporin allergy (severe); adjust if PCN allergy documented | Renal function, rash, C. difficile | STAT | STAT | - | STAT |
| Vancomycin | IV | Empiric meningitis coverage for resistant organisms (give with ceftriaxone) | 15-20 mg/kg :: IV :: q8-12h :: 15-20 mg/kg IV q8-12h (target trough 15-20 mcg/mL); max 2 g/dose | Vancomycin allergy; red man syndrome (infuse over 1h minimum) | Trough levels, renal function, ototoxicity | STAT | STAT | - | STAT |
| Acyclovir | IV | Empiric HSV encephalitis coverage if fever, altered mental status, temporal lobe abnormalities | 10 mg/kg :: IV :: q8h :: 10 mg/kg IV q8h (based on ideal body weight); adjust for renal function | Renal insufficiency (dose adjust); ensure adequate hydration | Renal function q24h, urine output | STAT | STAT | - | STAT |
| Dexamethasone (for meningitis) | IV | Reduce inflammation and improve outcomes in bacterial meningitis (give BEFORE or with first antibiotic dose) | 0.15 mg/kg :: IV :: q6h :: 0.15 mg/kg IV q6h x 4 days (typically 10 mg q6h); start before or with first antibiotic dose | Active fungal infection; defer if viral meningitis confirmed | Glucose, blood pressure | STAT | STAT | - | STAT |
| Nimodipine | PO | Suspected SAH with vasospasm; RCVS | 60 mg :: PO :: q4h :: 60 mg PO q4h x 21 days; reduce to 30 mg q4h if hypotension | Hypotension (SBP <90); do NOT give IV (severe hypotension risk) | Blood pressure q1h initially, then q4h | STAT | STAT | - | STAT |
| Heparin drip | IV | Confirmed cerebral venous thrombosis (CVT) | 80 units/kg :: IV :: continuous :: 80 units/kg bolus, then 18 units/kg/hr; target PTT 60-80 sec | Active hemorrhagic infarction (relative; still often treated), uncontrolled bleeding | PTT q6h until stable, then q12h; platelet count | STAT | STAT | - | STAT |
| Mannitol | IV | Emergent ICP reduction in suspected mass lesion with herniation signs | 1-1.5 g/kg :: IV :: once :: 1-1.5 g/kg IV bolus over 15-20 min; may repeat 0.25-0.5 g/kg q6h | Anuria, severe dehydration, active intracranial hemorrhage (relative) | Serum osmolality (<320), electrolytes, urine output, neuro checks | STAT | - | - | STAT |
| Hypertonic saline (23.4%) | IV | Emergent ICP reduction; alternative to mannitol | 30 mL :: IV :: once :: 30 mL of 23.4% NaCl IV over 15-20 min via central line | Hypernatremia (Na >160) | Sodium q2-4h (target 145-155), osmolality | STAT | - | - | STAT |

### 3E. Empiric Treatment When Primary Headache Suspected

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Sumatriptan SC | SC | Suspected migraine or cluster headache with moderate-severe pain (after secondary causes excluded) | 6 mg :: SC :: once :: 6 mg SC once; may repeat in 2h; max 12 mg/24h | CAD, stroke/TIA, uncontrolled HTN, hemiplegic migraine, pregnancy, basilar migraine, within 24h of ergotamine | Chest tightness, BP | STAT | STAT | - | - |
| Sumatriptan PO | PO | Suspected migraine after secondary causes excluded; milder attacks | 50-100 mg :: PO :: once :: 50-100 mg PO once; may repeat in 2h; max 200 mg/24h | CAD, stroke/TIA, uncontrolled HTN, hemiplegic migraine, pregnancy, basilar migraine, within 24h of ergotamine | Chest tightness, BP | - | ROUTINE | ROUTINE | - |
| Oxygen (high-flow) | INH | Suspected cluster headache (unilateral periorbital pain with autonomic features) | 100% :: INH :: continuous x 15-20 min :: 100% O2 via non-rebreather mask at 12-15 L/min x 15-20 min | None | Oxygen saturation | STAT | STAT | - | STAT |
| Nerve block (greater occipital) | Local | Refractory headache during evaluation; suspected occipital neuralgia; adjunctive for migraine/cluster | 2-3 mL per side :: local injection :: once :: Lidocaine 1% or bupivacaine 0.25%, 2-3 mL per side at greater occipital nerve | Local anesthetic allergy, overlying skin infection, anticoagulation (relative) | Local reaction, vasovagal response | URGENT | ROUTINE | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consult for headache with focal neurologic deficits, abnormal imaging, or diagnostic uncertainty requiring urgent subspecialty input | STAT | URGENT | - | STAT |
| Neurosurgery consult for suspected SAH, acute hydrocephalus, or mass lesion with herniation risk requiring surgical evaluation | STAT | STAT | - | STAT |
| Ophthalmology consult for papilledema, visual loss, or suspected IIH requiring fundoscopic evaluation and visual field testing | URGENT | URGENT | ROUTINE | URGENT |
| Headache specialist referral for chronic or recurrent headache not responding to initial management within 4-6 weeks | - | ROUTINE | ROUTINE | - |
| Infectious disease consult for suspected CNS infection with unusual organism profile or immunocompromised host | URGENT | URGENT | - | URGENT |
| Rheumatology consult for suspected CNS vasculitis or giant cell arteritis requiring temporal artery biopsy coordination | - | URGENT | ROUTINE | - |
| Pain management referral for chronic refractory headache not responding to first-line and second-line therapies | - | - | ROUTINE | - |
| Behavioral health referral for comorbid anxiety or depression contributing to headache chronification | - | ROUTINE | ROUTINE | - |
| ENT referral for headache with sinus symptoms, pulsatile tinnitus, or suspected CSF leak from skull base | - | ROUTINE | ROUTINE | - |

### 4B. Patient/Family Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Return immediately if headache becomes the worst headache of your life, sudden thunderclap onset, or associated with fever, stiff neck, confusion, weakness, double vision, or seizure (these may indicate a life-threatening cause) | ROUTINE | ROUTINE | ROUTINE | - |
| Keep a headache diary documenting frequency, severity (0-10), location, duration, associated symptoms, triggers, and medications taken with response (essential for diagnosis and management) | ROUTINE | ROUTINE | ROUTINE | - |
| Do not drive or operate heavy machinery while headache is severe or if experiencing visual changes, dizziness, or sedation from medications | ROUTINE | ROUTINE | ROUTINE | - |
| Avoid medication overuse: limit acute headache medications to no more than 2-3 days per week to prevent medication overuse headache | - | ROUTINE | ROUTINE | - |
| Follow up with primary care or neurology within 1-2 weeks if headache is new or within 4-6 weeks if chronic, to review diagnostic results and establish ongoing management | ROUTINE | ROUTINE | ROUTINE | - |
| Bring a list of all medications (prescription and over-the-counter) to follow-up visits, including how often each headache medication is used per month | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Maintain regular sleep schedule (7-8 hours nightly at consistent times) as both sleep deprivation and oversleeping are common headache triggers | - | ROUTINE | ROUTINE | - |
| Stay well-hydrated (64+ oz water daily) as dehydration is a modifiable headache trigger | ROUTINE | ROUTINE | ROUTINE | - |
| Regular aerobic exercise (30 minutes, 5 days/week) to reduce headache frequency through endorphin release and stress reduction | - | ROUTINE | ROUTINE | - |
| Stress management techniques (progressive muscle relaxation, deep breathing, biofeedback, or cognitive behavioral therapy) to reduce stress-related headache triggers | - | ROUTINE | ROUTINE | - |
| Limit caffeine to consistent moderate intake (<200 mg/day) and avoid abrupt caffeine withdrawal which can trigger rebound headache | - | ROUTINE | ROUTINE | - |
| Screen for and address modifiable risk factors: obesity, poor sleep hygiene, excessive screen time, poor posture, jaw clenching/bruxism | - | - | ROUTINE | - |
| Smoking cessation to reduce vascular risk and improve overall headache outcomes | - | ROUTINE | ROUTINE | - |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Migraine | Unilateral, pulsating, 4-72h, nausea/vomiting, photo/phonophobia, aura in 25%, aggravated by activity | Clinical history (ICHD-3 criteria); diagnosis of exclusion; normal neuroimaging |
| Tension-type headache | Bilateral, pressing/tightening, mild-moderate, no nausea, no photo AND phonophobia together, not worsened by activity | Clinical history; no imaging needed if typical presentation |
| Cluster headache | Strictly unilateral periorbital, autonomic features (lacrimation, rhinorrhea, ptosis, miosis), 15-180 min attacks, circadian pattern, male predominance | Clinical pattern; MRI brain with pituitary views to rule out structural cause |
| Subarachnoid hemorrhage | Thunderclap onset (peak intensity <1 min), "worst headache of life," neck stiffness, loss of consciousness, sentinel leak | CT head (>95% sensitivity within 6h); LP with xanthochromia if CT negative within 6-12h; CTA for aneurysm |
| Bacterial meningitis | Fever, neck stiffness, altered mental status (classic triad in <50%); headache, photophobia, Kernig/Brudzinski signs | LP with CSF pleocytosis, elevated protein, low glucose; blood cultures; CSF Gram stain and culture |
| Viral meningitis/encephalitis | Fever, headache, photophobia, neck stiffness; encephalitis adds confusion, seizures, focal deficits | LP with lymphocytic pleocytosis, normal glucose; CSF PCR panel; MRI (temporal lobe in HSV) |
| Idiopathic intracranial hypertension (IIH) | Papilledema, visual obscurations, pulsatile tinnitus, worse supine, typically young obese women | LP with elevated opening pressure (>25 cm H2O); MRI with empty sella, optic nerve sheath distension; MRV to exclude CVT |
| Cerebral venous thrombosis | Progressive headache, seizures, focal deficits; risk factors (OCP, pregnancy/postpartum, hypercoagulable state) | MRV or CT venogram (filling defect in venous sinus); D-dimer (negative may exclude) |
| Giant cell arteritis | Age >50, new headache, jaw claudication, scalp tenderness, visual symptoms, polymyalgia rheumatica | ESR/CRP markedly elevated; temporal artery biopsy (gold standard); temporal artery ultrasound (halo sign) |
| Cervical artery dissection | Unilateral head/neck/face pain, partial Horner syndrome, pulsatile tinnitus; history of trauma, chiropractic manipulation, or connective tissue disorder | CTA neck or MRA neck with fat-sat; intimal flap, pseudoaneurysm, or string sign |
| RCVS (reversible cerebral vasoconstriction syndrome) | Recurrent thunderclap headaches over 1-4 weeks, may have triggers (vasoactive drugs, postpartum, exertion, Valsalva) | CTA/MRA with segmental vasoconstriction (beading); resolves within 3 months; catheter angiography if noninvasive negative |
| Brain tumor | Progressive headache, worse in morning or with Valsalva, new focal deficits, weight loss, seizures | MRI brain with contrast; CT if MRI unavailable |
| Spontaneous intracranial hypotension | Orthostatic headache (worse upright, better supine), may have subdural collections, pachymeningeal enhancement | LP with low opening pressure (<6 cm H2O); MRI with diffuse pachymeningeal enhancement, brain sagging; CT myelogram to localize CSF leak |
| Carbon monoxide poisoning | Headache with nausea, dizziness, confusion; multiple household members affected; worse in winter (heating systems) | Carboxyhemoglobin level (>3% nonsmoker); ABG |
| Medication overuse headache | Chronic daily headache (>15 days/month) in patient with pre-existing headache disorder using acute medications >10-15 days/month for >3 months | Medication diary; improves with withdrawal of offending agent (within 2 months) |
| Acute angle-closure glaucoma | Severe eye pain, headache, nausea/vomiting, mid-dilated fixed pupil, red eye, visual halos, elevated intraocular pressure | Intraocular pressure measurement; slit-lamp exam; gonioscopy |
| Hypertensive emergency | Severe headache with SBP >180 and/or DBP >120 with end-organ damage (encephalopathy, visual changes, AKI) | Blood pressure measurement; fundoscopy (papilledema, hemorrhages); renal function; CT head to exclude hemorrhage |
| Pituitary apoplexy | Sudden severe headache, visual field deficits (bitemporal hemianopia), ophthalmoplegia, altered mental status; history of pituitary adenoma | MRI with pituitary protocol; hormonal panel (cortisol, TSH, prolactin, GH) |

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Pain scale (0-10 NRS) | Per assessment; q1-2h in ED; q4h inpatient; each visit OPD | Decreasing trend; target <4/10 | Escalate analgesic regimen; reassess for secondary cause if not improving | STAT | ROUTINE | ROUTINE | STAT |
| Neurologic exam (mental status, cranial nerves, motor, sensory, coordination) | At presentation and with any change; q4h if admitted; each visit OPD | Stable or improving; no new focal deficits | Urgent imaging and neurology consult if new deficit; reassess differential | STAT | ROUTINE | ROUTINE | STAT |
| Vital signs (BP, HR, RR, T, SpO2) | Per assessment; q1h in ED/ICU; q4h inpatient | Normal vital signs; T <38.0C; SBP <180 | Address hypertensive urgency; fever workup if new; reassess for infection | STAT | ROUTINE | ROUTINE | STAT |
| GCS / level of consciousness | At presentation and q1-2h if declining; q4h if stable inpatient | GCS 15; no decline | Urgent imaging; ICU transfer if GCS declining; intubation if GCS <8 | STAT | ROUTINE | - | STAT |
| Pupil size and reactivity | At presentation and q2-4h if concern for elevated ICP | Equal, round, reactive 3-4 mm | Fixed dilated pupil = emergent imaging + neurosurgery; initiate herniation protocol | STAT | ROUTINE | - | STAT |
| Fundoscopic exam | At presentation; repeat if clinical change | No papilledema, no hemorrhages | If papilledema: urgent LP for opening pressure; MRV to exclude CVT; ophthalmology consult | URGENT | ROUTINE | ROUTINE | URGENT |
| Headache diary (frequency, severity, triggers, medications) | Each outpatient visit; daily inpatient | Decreasing frequency and severity over time | Adjust treatment plan; reassess diagnosis if not improving at 4-6 weeks | - | ROUTINE | ROUTINE | - |
| ECG (if using dopamine antagonists, triptans, or DHE) | Before first dose; repeat if symptoms | Normal sinus rhythm; QTc <470 ms | Hold QT-prolonging medications; cardiology consult if QTc >500 ms | STAT | STAT | ROUTINE | STAT |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge from ED | Pain controlled to tolerable level; able to tolerate PO; no red flags on history or exam; normal neurologic exam; CT head normal (if indicated); reliable patient with clear return precautions; follow-up arranged within 1-2 weeks |
| Admit to hospital floor | Headache unresponsive to ED treatment requiring IV medications; need for IV antibiotic therapy (suspected meningitis); diagnostic workup requiring inpatient monitoring (serial LPs, extended imaging); intractable nausea/vomiting with dehydration; new neurologic deficit under investigation |
| Admit to ICU | Suspected SAH with hemodynamic instability or declining mental status; confirmed bacterial meningitis with sepsis or altered consciousness; elevated ICP with risk of herniation; cerebral venous thrombosis with hemorrhagic conversion; status requiring continuous neuro monitoring; hypertensive emergency with neurologic symptoms |
| Transfer to higher level of care | Need for neurosurgical intervention not available (aneurysm clipping/coiling, VP shunt, tumor resection); need for interventional neuroradiology (embolization, thrombectomy); need for continuous EEG monitoring not available locally |
| Outpatient follow-up | New headache without red flags: PCP or neurology within 1-2 weeks; Chronic headache: neurology/headache specialist within 4-6 weeks; After hospitalization: neurology follow-up within 2-4 weeks; After normal ED workup: PCP within 1-2 weeks to review results |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| CT head within 6 hours has >95% sensitivity for SAH | Class I, Level A | [Perry et al. BMJ 2011](https://pubmed.ncbi.nlm.nih.gov/21791490/) |
| LP required if CT negative and SAH suspected (within 6-12h for xanthochromia) | Class I, Level B | [Edlow et al. Acad Emerg Med 2008](https://pubmed.ncbi.nlm.nih.gov/18616449/) |
| Ottawa SAH Rule for thunderclap headache risk stratification | Class II, Level B | [Perry et al. JAMA 2013](https://pubmed.ncbi.nlm.nih.gov/24065011/) |
| SNOOP mnemonic for headache red flags | Expert consensus | [Dodick. N Engl J Med 2006](https://pubmed.ncbi.nlm.nih.gov/16495396/); [Do et al. Lancet Neurol 2019](https://pubmed.ncbi.nlm.nih.gov/30497828/) |
| Prochlorperazine/metoclopramide effective for acute undifferentiated headache in ED | Class I, Level A | [Friedman et al. Ann Emerg Med 2008](https://pubmed.ncbi.nlm.nih.gov/18006188/); [Kelley and Tepper. Headache 2012](https://pubmed.ncbi.nlm.nih.gov/22946834/) |
| Dexamethasone reduces 24-72h headache recurrence | Class I, Level A | [Singh et al. Acad Emerg Med 2008](https://pubmed.ncbi.nlm.nih.gov/18976336/) |
| ACR Appropriateness Criteria for headache imaging | Expert consensus, Class II | [ACR Appropriateness Criteria: Headache 2019](https://pubmed.ncbi.nlm.nih.gov/31054741/) |
| AHS consensus statement: choosing wisely in headache medicine | Expert consensus | [Loder et al. Headache 2013](https://pubmed.ncbi.nlm.nih.gov/23808661/) |
| Neuroimaging not indicated for stable migraine pattern without red flags | Class II, Level B | [Sandrini et al. Neurol Sci 2004](https://pubmed.ncbi.nlm.nih.gov/15549530/); [AAN Practice Parameter, Frishberg 2000](https://pubmed.ncbi.nlm.nih.gov/10993987/) |
| Dexamethasone before antibiotics in bacterial meningitis improves outcomes | Class I, Level A | [de Gans and van de Beek. N Engl J Med 2002](https://pubmed.ncbi.nlm.nih.gov/12417547/) |
| ICHD-3 diagnostic criteria for primary headache disorders | Expert consensus (Gold Standard) | [ICHD-3. Cephalalgia 2018](https://pubmed.ncbi.nlm.nih.gov/29368949/) |
| High-flow oxygen effective for acute cluster headache | Class I, Level A | [Cohen et al. J Neurol Neurosurg Psychiatry 2009](https://pubmed.ncbi.nlm.nih.gov/19151014/) |
| ESR and CRP for GCA screening; sensitivity improves with combined testing | Class II, Level B | [Salvarani et al. N Engl J Med 2002](https://pubmed.ncbi.nlm.nih.gov/12140307/); [Costello et al. BMC Musculoskelet Disord 2020](https://pubmed.ncbi.nlm.nih.gov/32527251/) |
| CTA for aneurysm detection approaches sensitivity of conventional angiography | Class I, Level A | [White et al. Radiology 2000](https://pubmed.ncbi.nlm.nih.gov/10657181/) |
| MRV or CTV for cerebral venous thrombosis diagnosis | Class II, Level B | [Saposnik et al. Stroke 2011](https://pubmed.ncbi.nlm.nih.gov/21293023/) |

---

## NOTES

- This plan is a DIAGNOSTIC EVALUATION framework; once a specific headache diagnosis is made, transition to the appropriate condition-specific treatment plan
- The SNOOP mnemonic is the cornerstone of red flag identification: Systemic symptoms/secondary risk factors, Neurologic symptoms/abnormal signs, Onset sudden (thunderclap), Older age (new onset >50), Previous headache history change
- Thunderclap headache is SAH until proven otherwise; CT head within 6 hours is >95% sensitive; LP is still required if CT negative and clinical suspicion remains
- Do not image every headache: stable, typical migraine or tension-type headache pattern with normal neurologic exam does not require neuroimaging (AAN/AHS guidelines)
- In patients >50 with new headache, ALWAYS check ESR and CRP to screen for giant cell arteritis; temporal artery biopsy is the gold standard
- If bacterial meningitis is suspected, administer empiric antibiotics IMMEDIATELY; do not delay treatment for LP or imaging
- Medication overuse headache is the most common cause of chronic daily headache; screen for frequency of acute medication use in all chronic headache patients
- Pregnancy modifies the differential: consider cerebral venous thrombosis, pre-eclampsia/eclampsia, pituitary apoplexy, and RCVS; avoid CT if possible (MRI preferred); limit medication options

---

## CHANGE LOG

**v1.1 (February 2, 2026)**
- Added Section A / Section B dividers with ═══ format per template standard
- Added ICU column to Section 4B (Patient/Family Instructions) and Section 4C (Lifestyle & Prevention) tables for format consistency
- Standardized structured dosing format across all treatment tables (verified `[dose] :: [route] :: [frequency] :: [full_instructions]`)
- Fixed IV normal saline dosing field to use proper structured format (dose :: route :: frequency :: instructions)
- Fixed Heparin drip dosing field to use weight-based dose as first field instead of generic "weight-based"
- Removed "IV" suffix from Ketorolac and Prochlorperazine treatment names (route captured in Route column)
- Removed "IV" suffix from Magnesium sulfate, Metoclopramide, Diphenhydramine treatment names for consistency
- Fixed Sumatriptan PO contraindications (was "Same as sumatriptan SC" cross-reference; replaced with full contraindication list)
- Fixed Oxygen high-flow dosing frequency field from empty to "continuous x 15-20 min"
- Strengthened directive language in Section 6 (removed "consider" from GCS and pupil action items)
- Updated VERSION to 1.1, added REVISED date, updated STATUS to "Validated per checker pipeline"

**v1.0 (February 2, 2026)**
- Initial template creation
- Comprehensive diagnostic evaluation framework for undifferentiated headache
- SNOOP red flag screening framework
- Full differential diagnosis covering primary and secondary headache disorders
- Lumbar puncture section with complete CSF panel
- Empiric treatment sections for both suspected primary and secondary headache causes
- Evidence-based imaging indications and algorithm
- CPT codes for all tests, imaging, and procedures

---

## APPENDIX A: SNOOP Red Flag Mnemonic for Headache Evaluation

| Letter | Red Flag | Concern | Action |
|--------|----------|---------|--------|
| **S** | **S**ystemic symptoms (fever, weight loss, malignancy, HIV, immunosuppression) | Infection, malignancy, inflammatory disease | CBC, CRP, blood cultures; MRI with contrast; LP |
| **S** | **S**econdary risk factors (anticoagulation, pregnancy, postpartum) | CVT, hemorrhage, pre-eclampsia, pituitary apoplexy | Coagulation studies; MRV/CTV; blood pressure; urine protein |
| **N** | **N**eurologic symptoms or abnormal exam (focal deficits, papilledema, meningismus, altered mental status) | Mass, stroke, hemorrhage, meningitis, elevated ICP | STAT CT head; neurology consult; LP if safe |
| **O** | **O**nset sudden / thunderclap (peak intensity <1 minute) | SAH, CVT, dissection, RCVS, pituitary apoplexy | STAT CT head; LP if CT negative; CTA head/neck |
| **O** | **O**lder age at onset (new headache >50 years) | GCA, mass, hemorrhage | ESR/CRP; temporal artery biopsy; MRI brain |
| **P** | **P**attern change, positional, provoked by Valsalva, progressive, or precipitated by exertion/sex | IIH, Chiari, mass, low-pressure headache, SAH | MRI brain; LP with opening pressure; MRV |

## APPENDIX B: Headache Evaluation Decision Algorithm

**Step 1: Red Flag Screen (SNOOP)**

- If ANY red flag present --> Proceed to urgent evaluation (Step 2)
- If NO red flags + typical primary headache pattern --> Clinical diagnosis; no imaging needed; treat per condition-specific plan

**Step 2: Determine Acuity**

- **Thunderclap onset (<1 min to peak):** STAT CT head --> If negative, LP within 12h --> If negative, CTA head/neck for aneurysm/dissection/RCVS
- **Acute onset with fever + meningismus:** Blood cultures + empiric antibiotics STAT --> CT head --> LP
- **Acute onset with focal deficits:** STAT CT head --> MRI if CT negative --> Neurology consult
- **Subacute/progressive over days-weeks:** MRI brain with contrast --> Targeted workup based on findings

**Step 3: Targeted Workup Based on Suspicion**

| Clinical Suspicion | Primary Test | Confirmatory Test |
|--------------------|-------------|-------------------|
| SAH | CT head (within 6h) | LP (xanthochromia) --> CTA for aneurysm |
| Meningitis/Encephalitis | LP (CSF analysis + cultures + PCR panel) | MRI brain (encephalitis pattern) |
| IIH | LP (opening pressure >25 cm H2O) | MRV to exclude CVT; ophthalmology (visual fields) |
| CVT | MRV or CT venogram | Hypercoagulability workup |
| GCA | ESR + CRP | Temporal artery biopsy or ultrasound |
| Dissection | CTA neck or MRA neck with fat-sat | Conventional angiography (rarely needed) |
| Mass lesion | MRI brain with contrast | Neurosurgery consult; biopsy if indicated |
| RCVS | CTA/MRA (segmental vasoconstriction) | Repeat imaging at 12 weeks (should resolve) |
| Low-pressure headache | MRI brain (pachymeningeal enhancement, brain sagging) | CT myelogram (localize leak) |

**Step 4: Classify and Transition**

Once a specific diagnosis is established, transition to the appropriate condition-specific clinical plan for definitive management.
