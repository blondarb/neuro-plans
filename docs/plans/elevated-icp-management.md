---
title: "Elevated Intracranial Pressure Management"
description: "Clinical decision support for elevated intracranial pressure (icp) / intracranial hypertension diagnosis and management"
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

# Elevated Intracranial Pressure Management

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Elevated Intracranial Pressure (ICP) / Intracranial Hypertension

**ICD-10:** G93.2 (Benign intracranial hypertension [IIH]), G93.5 (Compression of brain), G93.6 (Cerebral edema), G91.1 (Obstructive hydrocephalus), G91.2 (Normal pressure hydrocephalus), S06.1X (Traumatic cerebral edema)

**CPT CODES:** 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 82947 (Blood glucose), 85610 (PT/INR), 83930 (Serum osmolality), 82803 (Arterial blood gas (ABG)), 83605 (Lactate), 86900 (Type and screen), 84484 (Troponin), 82533 (Cortisol (AM, random)), 84443 (TSH), 82140 (Ammonia), 80307 (Toxicology screen), 70450 (CT head without contrast), 70496 (CT angiography (CTA) head), 70553 (MRI brain with and without contrast), 71046 (Chest X-ray), 93886 (Transcranial Doppler (TCD)), 95700 (Continuous EEG monitoring), 62270 (LP with opening pressure)

**SYNONYMS:** Elevated intracranial pressure, elevated ICP, intracranial hypertension, raised ICP, high ICP, cerebral edema, brain swelling, herniation syndrome, increased intracranial pressure, ICP crisis

**SCOPE:** Emergency evaluation and management of elevated intracranial pressure in adults. Covers recognition of elevated ICP (Cushing triad, papilledema, declining GCS), emergent interventions (osmotherapy, hyperventilation, sedation, CSF drainage), ICP monitoring indications, surgical decompression, and specific etiology-based management. Includes management across etiologies: traumatic brain injury, stroke (ischemic/hemorrhagic), tumor, infection, hydrocephalus, and idiopathic intracranial hypertension. Excludes pediatric ICP management (different thresholds/approaches).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Infection workup; anemia (reduced O2 carrying capacity); thrombocytopenia (bleeding risk); baseline | Normal; leukocytosis → infection; thrombocytopenia → hemorrhage risk |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolytes (sodium critical for osmotherapy); renal function (contrast, mannitol); glucose; hepatic function | Normal; track sodium closely (goal varies by treatment); avoid hyponatremia |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Hyperglycemia worsens outcomes in brain injury; hypoglycemia mimics neurologic deterioration | 140-180 mg/dL target in critically ill; <180 in general |
| PT/INR (CPT 85610), aPTT (CPT 85730) | STAT | STAT | - | STAT | Coagulopathy (hemorrhagic causes); ICP monitor placement safety; surgical candidacy | Normal; INR <1.4 for ICP monitor placement |
| Serum osmolality (CPT 83930) | STAT | STAT | - | STAT | **CRITICAL for osmotherapy monitoring**; baseline before mannitol/hypertonic saline; target for therapy | 280-295 mOsm/kg baseline; therapeutic target 300-320 (do not exceed 320) |
| Sodium | STAT | STAT | - | STAT | **CRITICAL**; hypertonic saline therapy monitoring; cerebral salt wasting vs. SIADH; target for ICP management | 135-145 mEq/L baseline; therapeutic hypernatremia target 145-155 mEq/L (with hypertonic saline) |
| Arterial blood gas (ABG) (CPT 82803) | STAT | STAT | - | STAT | Ventilation status (PaCO2 critical for ICP); oxygenation; pH; metabolic status | PaCO2 35-40 mmHg (normal); pH 7.35-7.45; PaO2 >80; for hyperventilation: target PaCO2 30-35 |
| Lactate (CPT 83605) | STAT | STAT | - | STAT | Tissue perfusion; systemic sepsis; prognostic | <2 mmol/L; elevated → hypoperfusion, sepsis |
| Type and screen (CPT 86900) | STAT | STAT | - | STAT | Surgical candidacy; potential for decompressive craniectomy or other neurosurgical intervention | On file |
| Troponin (CPT 84484) | STAT | STAT | - | STAT | Neurogenic cardiac injury (stress cardiomyopathy); particularly in SAH, TBI, ICH | Normal; elevated → neurogenic stress cardiomyopathy; obtain echo |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum osmolality (serial) | - | STAT | - | STAT | **q4-6h during osmotherapy**; osmolar gap calculation; prevent hyper-osmolar state | Maintain <320 mOsm/kg; osmolar gap >10-15 → accumulating mannitol |
| Sodium (serial) | - | STAT | - | STAT | **q2-6h during active ICP management**; hypertonic saline monitoring; avoid rapid correction | Target 145-155 mEq/L during active ICP crisis; avoid fluctuations >10 mEq/24h |
| Cortisol (AM, random) (CPT 82533) | - | ROUTINE | ROUTINE | ROUTINE | Adrenal insufficiency (pituitary injury in TBI, tumor); steroid responsiveness in tumor edema | >10 mcg/dL (AM); if low → cortisol stimulation test or empiric steroids |
| TSH (CPT 84443), free T4 (CPT 84439) | - | ROUTINE | ROUTINE | - | Pituitary injury (TBI, tumor, surgery); hypothyroidism | Normal |
| Ammonia (CPT 82140) | STAT | STAT | - | STAT | Hepatic encephalopathy differential; can cause cerebral edema and elevated ICP | <35 μmol/L; elevated → hepatic cause; lactulose, rifaximin |
| Toxicology screen (CPT 80307) | STAT | STAT | - | STAT | Intoxication as cause of altered mental status; drug-induced cerebral edema (rare) | Negative; specific toxin identification |
| CSF analysis (if LP/EVD performed) | - | STAT | - | STAT | Infection (meningitis); malignancy (leptomeningeal disease); subarachnoid hemorrhage (xanthochromia); IIH (elevated OP with normal composition) | Normal CSF composition with elevated opening pressure → IIH; abnormal composition → specific diagnosis |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CSF opening pressure (LP) | - | URGENT | ROUTINE | - | **IIH diagnosis**: OP >25 cm H2O (obese patients >28 cm); therapeutic in IIH; NOT indicated if mass lesion or obstructive hydrocephalus | IIH: OP >25 cm H2O with normal composition; if OP >40-50 → severe |
| Pentobarbital level | - | - | - | STAT | If barbiturate coma induced for refractory ICP; therapeutic monitoring; guide dosing; monitor for toxicity | Therapeutic: 30-50 mcg/mL (for burst suppression); higher may be needed |
| EEG (continuous) | - | STAT | - | STAT | Monitor for burst suppression during barbiturate coma; detect subclinical seizures (common in brain injury); guide sedation titration | Target: burst suppression pattern during barbiturate coma; no seizures |
| Jugular venous oxygen saturation (SjvO2) | - | - | - | EXT | Advanced cerebral metabolism monitoring; guide CPP management; detect ischemia or hyperemia | 55-75%; <55% = ischemia (increase CPP or reduce CMRO2); >75% = hyperemia |
| Brain tissue oxygen (PbtO2) | - | - | - | EXT | Direct brain oxygenation monitoring; guide therapy in severe TBI; multimodal monitoring | >20 mmHg; <15 mmHg = brain hypoxia → intervene |
| Cerebral microdialysis | - | - | - | EXT | Research/specialized centers; metabolic monitoring; lactate:pyruvate ratio; glucose; glutamate | Lactate:pyruvate ratio <40 (normal); elevated = metabolic crisis |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | **Immediate** — within minutes of suspected elevated ICP; before any intervention; determines etiology and guides treatment | Mass lesion (tumor, hematoma); midline shift (>5mm = significant); hydrocephalus; cerebral edema (effaced sulci, compressed ventricles); herniation signs (uncal, tonsillar); cisternal effacement | None for non-contrast CT; benefit always outweighs risk in emergency |
| CT angiography (CTA) head (CPT 70496) | STAT | STAT | - | STAT | If vascular etiology suspected (SAH, venous sinus thrombosis, AVM); concurrent with non-contrast CT | Aneurysm (SAH); venous sinus thrombosis (filling defect in dural sinuses); AVM; dissection | Contrast allergy (premedicate if critical); renal impairment (benefit may outweigh risk) |
| CT venography (CTV) | STAT | STAT | ROUTINE | STAT | If cerebral venous sinus thrombosis suspected (headache, papilledema, focal deficits, hypercoagulable state); can be done with CTA | Filling defect in dural sinuses (transverse, sigmoid, sagittal); "empty delta sign" on contrast CT; cord sign | Same as CTA |
| MRI brain with and without contrast (CPT 70553) | URGENT | URGENT | ROUTINE | URGENT | When clinically stable; superior for tumor characterization, infection, posterior fossa; MRV for venous thrombosis; DWI for ischemia | Tumor; abscess; encephalitis; venous sinus thrombosis; ischemic stroke; PRES; herniation; meningeal enhancement | MRI-incompatible implants; hemodynamic instability |
| Chest X-ray (CPT 71046) | STAT | STAT | - | STAT | ETT position confirmation; pulmonary complications (aspiration, ARDS); central line position | ETT position; no pulmonary infiltrate; line position | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MR venography (MRV) | - | URGENT | ROUTINE | URGENT | Cerebral venous sinus thrombosis confirmation; if CTV equivocal; can be done without contrast (TOF technique) | Venous sinus thrombosis; flow void absence | Same as MRI |
| Transcranial Doppler (TCD) (CPT 93886) | - | URGENT | - | URGENT | Non-invasive ICP estimation (pulsatility index); vasospasm detection (SAH); cerebral circulatory arrest (brain death) | Pulsatility index >1.4 suggests elevated ICP; MCA velocities for vasospasm; reverberating flow = no cerebral circulation | None; operator-dependent |
| Optic nerve sheath diameter (ONSD) ultrasound | STAT | STAT | - | STAT | Bedside non-invasive ICP estimation; ONSD >5-5.5 mm suggests ICP >20 mmHg; useful when formal monitoring not available | ONSD >5 mm (some use 5.5 mm) = elevated ICP | Limited accuracy; operator-dependent; not a substitute for invasive monitoring |
| CT perfusion (CPT 0042T) | - | URGENT | - | URGENT | Ischemic stroke workup; penumbra assessment; vasospasm evaluation | Perfusion deficits; core vs. penumbra; vasospasm patterns | Contrast requirements |
| Fundoscopic examination | STAT | STAT | ROUTINE | STAT | Papilledema detection (takes hours-days to develop); retinal hemorrhages (Terson syndrome in SAH); IIH evaluation | Papilledema (indicates chronically or subacutely elevated ICP); absent papilledema does NOT exclude acute ICP elevation; venous pulsations absent if ICP >180 mm H2O | None |
| Formal visual field testing | - | - | ROUTINE | - | IIH monitoring; chronic elevated ICP; document visual field loss for treatment decisions | Enlarged blind spot; peripheral constriction; nasal field loss | Patient cooperation required |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| ICP monitor placement (invasive) | - | STAT | - | STAT | **Gold standard for ICP measurement**; indications: GCS ≤8 with abnormal CT, or GCS ≤8 with normal CT + 2 of (age >40, SBP <90, motor posturing); also for hydrocephalus management; typically EVD or parenchymal monitor | Direct ICP measurement; normal <15 mmHg; elevated >20-22 mmHg; treatment threshold >22 mmHg (Brain Trauma Foundation 2016) | Coagulopathy (correct first); infection at insertion site; uncontrolled bleeding diathesis |
| External ventricular drain (EVD) | - | STAT | - | STAT | ICP monitoring + therapeutic CSF drainage; preferred in hydrocephalus; allows ICP waveform analysis | ICP measurement; CSF drainage; waveform analysis (P2 > P1 = decreased compliance) | Same as ICP monitor |
| Continuous EEG monitoring (CPT 95700) | - | STAT | - | STAT | Detect subclinical seizures (common in TBI, ICH, SAH — up to 20-30%); guide sedation; burst suppression monitoring during barbiturate coma | No seizures; appropriate sedation level; burst suppression if pentobarbital coma | None; resource availability |
| Nuclear medicine cerebral perfusion (SPECT/HMPAO) | - | - | - | EXT | Brain death confirmation (ancillary test); no cerebral blood flow | No uptake = brain death (if clinical criteria met and confounders excluded) | Limited availability |
| CT/MRI perfusion for brain death | - | - | - | EXT | Brain death confirmation; no cerebral perfusion | No perfusion = brain death | Same as standard CT/MRI |

### Lumbar Puncture

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP with opening pressure (CPT 62270) | - | URGENT | ROUTINE | - | **IIH diagnosis and treatment**: measure opening pressure → therapeutic CSF removal; **CONTRAINDICATED if mass lesion, obstructive hydrocephalus, or herniation risk**; imaging FIRST | Opening pressure: normal <20 cm H2O (obese <25); IIH: >25 cm H2O with normal CSF composition; high-volume tap (20-30 mL) for symptomatic relief in IIH | **ABSOLUTE CONTRAINDICATION**: Mass lesion with mass effect; obstructive hydrocephalus; impending herniation; posterior fossa mass; midline shift; anticoagulation/coagulopathy; skin infection at LP site |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Airway management / Intubation** | IV | - | 0.3 mg/kg :: IV :: - :: **GCS ≤8: Secure airway**; RSI with agents that do NOT raise ICP; preferred: etomidate 0.3 mg/kg OR propofol 1-2 mg/kg + rocuronium 1.2 mg/kg OR succinylcholine 1.5 mg/kg; AVOID ketamine in severe TBI (controversial — emerging data suggest may be safe); lidocaine 1.5 mg/kg IV 2-3 min before laryngoscopy (may blunt ICP spike — controversial benefit); avoid hypotension during RSI | - | Airway protection; ventilation control (PaCO2 management); GCS ≤8 cannot protect airway; avoid hypoxia (PaO2 <60) and hypotension (SBP <90) — both worsen outcomes | STAT | STAT | - | STAT |
| **Head of bed elevation** | - | - | **Elevate HOB 30°**; neutral head position (avoid neck flexion/rotation that impedes jugular venous drainage); avoid tight cervical collar if possible; reverse Trendelenburg if cervical spine immobilization required | - | Promotes venous drainage; reduces ICP by 3-5 mmHg; no evidence of reduced CPP with 30° elevation; simple and immediate intervention | STAT | STAT | - | STAT |
| **Hyperventilation (temporary)** | - | - | **Acute herniation ONLY (bridging therapy)**; target PaCO2 30-35 mmHg; induces cerebral vasoconstriction → reduced cerebral blood volume → reduced ICP; **Duration: <30 minutes ideally, maximum 2-4 hours**; taper gradually; avoid PaCO2 <25 (causes ischemia) | - | BTF Guidelines: Avoid prophylactic hyperventilation; use only for acute ICP crisis/herniation as bridge to definitive therapy; prolonged hyperventilation causes rebound vasodilation and ischemia; monitor with SjvO2 or PbtO2 if prolonged use needed | STAT | STAT | - | STAT |
| **Osmotherapy — Mannitol** | IV | - | 1-1.5 g/kg :: IV :: PRN :: **Mannitol 20%:** 1-1.5 g/kg IV bolus (e.g., 100g = 500 mL of 20% for 70 kg patient) over 15-20 minutes; repeat doses: 0.25-0.5 g/kg q4-6h PRN; **Hold if:** serum osmolality >320 mOsm/kg, osmolar gap >15-20; **Requires:** Foley catheter (massive diuresis); volume replacement; **Onset:** 15-30 min; **Duration:** 2-6 hours | - | Creates osmotic gradient → draws water from brain parenchyma; reduces brain volume; also improves blood rheology; BTF: Level II evidence; monitor for renal toxicity (ATN), hypovolemia, rebound edema | STAT | STAT | - | STAT |
| **Osmotherapy — Hypertonic Saline** | IV | - | 30 mL :: IV :: Continuous :: **23.4% NaCl:** 30 mL IV bolus over 15-20 min via central line (preferred for acute crisis); **3% NaCl:** 250-500 mL IV bolus over 30 min (can give peripherally); **Continuous infusion:** 3% NaCl at 30-50 mL/hr to maintain Na 145-155 mEq/L; **Target sodium:** 145-155 mEq/L; avoid >160; correct slowly if hypernatremia develops (no faster than 8-10 mEq/24h decrease) | - | Equivalent or superior to mannitol for ICP reduction; does NOT cause diuresis (better for hypovolemic patients); no osmolality ceiling (unlike mannitol); does not accumulate in injured brain (mannitol may); preferred in many centers; SAFE-TBI trial (2021): 20% mannitol = HTS for ICP control | STAT | STAT | - | STAT |
| **Sedation and analgesia** | - | - | 25-75 mcg/kg :: - :: - :: **Goal:** Reduce metabolic demand, prevent agitation-induced ICP spikes; **Propofol:** 25-75 mcg/kg/min (first-line; reduces CMRO2 and ICP; allows rapid awakening for neuro exams); **Fentanyl:** 25-100 mcg/hr (analgesia without histamine release); **Midazolam:** 0.05-0.2 mg/kg/hr (alternative to propofol); **Avoid:** Ketamine in severe ICP (controversial); prolonged propofol (PRIS syndrome >48-72h at high doses) | - | Agitation, pain, coughing raise ICP; sedation reduces cerebral metabolic rate; propofol has favorable ICP properties; daily sedation holiday for neuro assessment if stable | STAT | STAT | - | STAT |
| **Neuromuscular blockade** | IV | - | 0.1-0.2 mg/kg :: IV :: once :: For refractory ICP spikes with ventilator dyssynchrony, coughing, posturing; **Cisatracurium** 0.1-0.2 mg/kg bolus → 1-3 mcg/kg/min infusion (organ-independent metabolism); **Rocuronium** 0.6-1 mg/kg bolus → 0.6 mg/kg/hr; **Requires:** Concurrent sedation/analgesia; train-of-four monitoring; prevents detection of seizures (need cEEG) | - | Prevents ICP spikes from coughing, posturing; reduces intrathoracic pressure; use judiciously — obscures neuro exam and seizure detection; requires cEEG monitoring | - | STAT | - | STAT |
| **Seizure prophylaxis / treatment** | IV | - | 1000-1500 mg :: IV :: q12h :: **Prophylaxis (TBI):** Levetiracetam 1000-1500 mg IV load → 500-1000 mg q12h x 7 days (BTF: early seizure prophylaxis x 7 days for severe TBI); **Active seizure:** Lorazepam 0.1 mg/kg (max 4 mg) → Levetiracetam 60 mg/kg load (max 4500 mg) OR fosphenytoin 20 mg PE/kg; **Status epilepticus:** Per SE protocol | - | Seizures dramatically increase CMRO2 and ICP; early seizures occur in 10-15% of severe TBI; prophylaxis beyond 7 days NOT recommended (does not prevent late epilepsy); levetiracetam preferred (no drug interactions, IV/PO equivalent) | STAT | STAT | - | STAT |
| **Temperature control** | - | - | 650-1000 mg :: - :: - :: **Avoid fever aggressively**: fever increases CMRO2 by 10-13% per °C; target 36-37°C; acetaminophen 650-1000 mg q4-6h; cooling blankets; **Therapeutic hypothermia:** 32-35°C controversial; EUROTHERM (2015) showed harm from prophylactic hypothermia to 32-35°C in TBI; may use for refractory ICP as rescue | - | Fever worsens neurologic outcomes; aggressive normothermia is standard; therapeutic hypothermia is rescue therapy only (not prophylactic); if used: 32-35°C, avoid shivering (increases CMRO2), slow rewarming | STAT | STAT | - | STAT |
| **Blood pressure / CPP management** | IV | - | **Target CPP 60-70 mmHg** (CPP = MAP - ICP); avoid CPP <60 (ischemia) and >70 (BTF: avoid aggressive CPP >70 due to ARDS risk); **If hypotensive:** IV fluids (isotonic crystalloid; avoid hypotonic fluids); vasopressors (norepinephrine first-line); **If hypertensive with ICP crisis:** Treat ICP first (osmotherapy, sedation); avoid precipitously lowering BP (reduces CPP) | - | CPP is the primary determinant of cerebral perfusion; BTF 2016: target CPP 60-70; lower threshold 60 mmHg; aggressive CPP >70 increases ARDS risk without outcome benefit; individualized based on autoregulation status | STAT | STAT | - | STAT |

### 3B. Definitive/Targeted Treatment (Tier 2 — Moderate ICP Elevation)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **ICP monitor / EVD placement** | - | - | **Indications (BTF 2016):** GCS ≤8 + abnormal CT; OR GCS ≤8 + normal CT + ≥2 of: age >40, SBP <90, motor posturing; **EVD preferred if:** Hydrocephalus; need for CSF drainage; **Parenchymal monitor if:** No hydrocephalus; cannot drain CSF; **Target ICP:** <22 mmHg (BTF 2016); some centers use <20 | - | Invasive ICP monitoring guides therapy; EVD allows therapeutic CSF drainage; parenchymal monitors cannot drain; infection risk ~5-10%; ventriculostomy is both diagnostic and therapeutic | - | STAT | - | STAT |
| **CSF drainage (via EVD)** | - | - | 5-10 mL :: - :: Continuous :: **Continuous drainage:** Set drain to maintain ICP <22 mmHg; drain 5-10 mL CSF if ICP spike; **Intermittent drainage:** Drain for ICP >22, then clamp to re-measure; **Typical:** Remove 5-20 mL for ICP crisis; **Rate:** Avoid draining >20 mL/hour (risk of over-drainage, collapse of ventricles, hemorrhage) | - | Immediate ICP reduction; removes volume (CSF) from closed cranial compartment; critical for hydrocephalus; risk: infection, hemorrhage, over-drainage | - | STAT | - | STAT |
| **Repeat osmotherapy dosing** | - | - | 0.25-0.5 g/kg :: - :: PRN :: Scheduled or PRN osmotherapy based on ICP readings; **Mannitol:** 0.25-0.5 g/kg q4-6h; **HTS 3%:** 30 mL/hr continuous or 250 mL bolus PRN; **Monitor:** Serum osm q4-6h (hold mannitol if >320); serum Na q2-4h (target 145-155 with HTS) | - | Sustained osmotherapy for sustained ICP elevation; alternating mannitol and HTS may extend treatment window; monitor for accumulation | - | STAT | - | STAT |
| **Decompressive craniectomy** | - | - | **Indications:** Refractory ICP despite maximal medical therapy; malignant MCA stroke (large hemispheric infarct with edema); large ICH with mass effect; traumatic brain injury with refractory ICP; **Timing:** TBI: DECRA trial (2011) — early DC did not improve 6-mo outcomes but reduced ICP/ICU stay; RESCUEicp (2016) — late rescue DC improved survival but increased severe disability; **Stroke:** DESTINY/DECIMAL/HAMLET — DC improves survival in malignant MCA stroke age <60 (NNT=2); must discuss goals of care | - | Removes skull to allow brain expansion; definitive ICP reduction; increases survival but may increase proportion surviving with severe disability; requires extensive goals of care discussion; timing and patient selection critical | - | STAT | - | - |
| **Dexamethasone (tumor/vasogenic edema)** | IV | - | 10 mg :: IV :: q6h :: **ONLY for vasogenic edema from tumor or abscess**; **NOT for TBI, stroke, or cytotoxic edema** (steroids worsen outcomes in TBI — CRASH trial); **Dose:** 10 mg IV load → 4 mg IV q6h; **Duration:** Until definitive tumor treatment; taper over 1-2 weeks after radiation/surgery; GI prophylaxis with PPI | - | Reduces vasogenic edema around tumors; inhibits VEGF; dramatic effect within 24-48h; CRASH trial: steroids HARMFUL in TBI — avoid; no benefit in stroke | - | STAT | ROUTINE | STAT |
| **Surgical evacuation of mass lesion** | - | - | 30 mL :: - :: - :: **Epidural hematoma:** Emergent if >30 mL, >15mm thickness, or >5mm midline shift, or GCS deterioration; **Subdural hematoma:** Emergent if >10mm thickness, >5mm midline shift, or GCS decrease >2 points; **ICH:** Consider if lobar >30 mL and deteriorating; cerebellar >3cm or hydrocephalus; **Tumor:** Resection or debulking for mass effect | - | Removes compressive mass → immediate ICP reduction; life-saving for epidural hematoma; subdural and ICH outcomes less clearly improved by surgery but indicated for mass effect and herniation | - | STAT | - | - |

### 3C. Refractory ICP Management (Tier 3 — Rescue Therapies)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Pentobarbital coma** | IV | - | 5-10 mg/kg :: IV :: Continuous :: **LAST RESORT for refractory ICP**; **Protocol:** Pentobarbital 5-10 mg/kg IV load over 30 min → 1-3 mg/kg/hr infusion; titrate to ICP <22 mmHg or burst suppression on EEG; **Target:** Burst suppression (3-10 second bursts with 10-20 second suppression); **Monitor:** Continuous EEG; drug levels (30-50 mcg/mL); hemodynamics (causes hypotension — often need vasopressors); **Duration:** 24-48h then attempt to wean; may need 3-5 days | - | Reduces CMRO2 to minimal levels; dramatic ICP reduction; causes severe hypotension (need vasopressors); immunosuppression; ileus; prolonged sedation; no proven mortality benefit but reduces ICP; requires ICU expertise | - | - | - | STAT |
| **Therapeutic hypothermia (rescue)** | - | - | **For refractory ICP only** (NOT prophylactic); **Target:** 32-35°C; **Method:** Surface cooling (Arctic Sun) or intravascular cooling catheter; **Duration:** 24-72h; **Rewarming:** Slow — 0.25°C/hour (rapid rewarming causes ICP rebound); **Complications:** Shivering (treat with paralysis, buspirone, meperidine), coagulopathy, infection, arrhythmia | - | Reduces CMRO2 and ICP; EUROTHERM (2015): prophylactic hypothermia HARMFUL in TBI; rescue hypothermia for refractory ICP still used but evidence weak; prevents fever spikes; requires expertise | - | - | - | STAT |
| **Lumbar CSF drainage** | - | - | 5-10 mL/h :: - :: - :: **ONLY if:** Communicating hydrocephalus; ICP refractory to EVD drainage; no mass lesion or obstructive hydrocephalus; basal cisterns visible; **Method:** Lumbar drain at 10-15 cm H2O; drain 5-10 mL/hour; **Risk:** Tonsillar herniation if used inappropriately; overdrainage | - | Drains CSF from lumbar space; reduces overall CSF volume; effective adjunct in communicating hydrocephalus; must NOT be used with obstructive hydrocephalus or significant mass effect | - | - | - | STAT |
| **High-dose hypertonic saline (23.4%)** | IV | - | 30 mL :: IV :: once :: **For refractory ICP crisis**; 30 mL IV bolus via central line; can repeat; target sodium up to 155-160 mEq/L in refractory cases (with close monitoring); **Risk:** Central pontine myelinolysis if rapid sodium changes (maintain stable elevated sodium; do not rapidly correct back to normal) | - | Potent osmotherapy; can achieve higher sodium targets than 3% NaCl; reserved for refractory cases; requires central line access | - | - | - | STAT |
| **Decompressive craniectomy (rescue)** | - | - | 26.9% :: - :: - :: As above; indicated for refractory ICP after failure of all medical therapies; must discuss survival with potential severe disability (RESCUEicp: DC improved survival from 26.9% to 48.9% but increased severe disability); goals of care critical | - | RESCUEicp (2016): More patients survived with DC but at cost of more survivors with severe disability; DECRA (2011): Early prophylactic DC did not improve functional outcomes; decision requires extensive patient/family discussion | - | STAT | - | - |

### 3D. Etiology-Specific Management

| Etiology | Specific Treatment |
|----------|-------------------|
| **Traumatic Brain Injury (TBI)** | ICP monitoring if GCS ≤8; CPP 60-70; avoid hypoxia (PaO2 <60), hypotension (SBP <90), hyperventilation (except acute herniation), hyperglycemia (>180), hyperthermia; seizure prophylaxis x 7 days; surgical evacuation of hematomas per criteria; decompressive craniectomy for refractory ICP |
| **Malignant MCA Stroke** | Decompressive craniectomy (hemicraniectomy) if age <60, within 48h; DESTINY/DECIMAL/HAMLET: NNT=2 for survival; discuss functional outcomes (many survive with hemiplegia, aphasia); no benefit from steroids; osmotherapy as bridge |
| **Intracerebral Hemorrhage (ICH)** | BP control (target SBP <140 per INTERACT2/ATACH-2); reverse anticoagulation; surgical evacuation if cerebellar >3cm, lobar >30mL with deterioration; EVD for hydrocephalus; no steroids |
| **Subarachnoid Hemorrhage (SAH)** | Secure aneurysm (clip/coil); nimodipine 60 mg q4h x 21 days; EVD for hydrocephalus; monitor for vasospasm (TCD, clinical); treat vasospasm (induced hypertension, intra-arterial therapy); euvolemia; avoid hypotension |
| **Brain Tumor** | Dexamethasone 10 mg IV then 4 mg q6h (for vasogenic edema); PPI while on steroids; surgical resection/debulking for mass effect; radiation/chemotherapy as appropriate; no osmotherapy needed if steroids effective |
| **Brain Abscess** | Antibiotics (empiric then targeted); surgical drainage (aspiration or excision) if >2.5 cm or refractory; dexamethasone for edema (controversial — may impair antibiotic penetration and immune response but used for severe edema); treat source |
| **Meningitis** | Antibiotics (empiric then targeted); dexamethasone 0.15 mg/kg q6h x 4 days for bacterial meningitis (give before or with first antibiotic dose — reduces inflammation); ICP management as above; EVD for hydrocephalus |
| **Hydrocephalus** | EVD (emergent temporizing measure); VP shunt (definitive for communicating); ETV (endoscopic third ventriculostomy for obstructive); treat underlying cause (tumor, hemorrhage, infection) |
| **Idiopathic Intracranial Hypertension (IIH)** | Weight loss (most important long-term intervention); acetazolamide 250 mg BID → titrate to 1-2 g/day (reduces CSF production); topiramate (weight loss + ICP reduction); furosemide (adjunct); serial LP (therapeutic drainage); optic nerve sheath fenestration (for vision loss); VP shunt or transverse sinus stenting (refractory) |
| **Cerebral Venous Sinus Thrombosis (CVST)** | Anticoagulation (heparin → warfarin or DOAC) even if hemorrhagic; ICP management as above; treat underlying hypercoagulable state; endovascular thrombectomy for refractory cases |
| **Hepatic Encephalopathy / Acute Liver Failure** | Lactulose; rifaximin; treat precipitant; avoid sedatives; ICP monitoring in acute liver failure (cerebral edema common); mannitol; moderate hypothermia (33-34°C); liver transplant evaluation |

### 3E. Medications to AVOID

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Corticosteroids in TBI | - | - | - | - | - | - | - | - | - |
| Corticosteroids in ischemic stroke | - | - | - | - | - | - | - | - | - |
| Hypotonic fluids (D5W, 0.45% NaCl) | - | - | - | - | - | - | - | - | - |
| Prolonged aggressive hyperventilation | - | - | - | - | - | - | - | - | - |
| Ketamine (traditionally) | - | - | - | - | - | - | - | - | - |
| Nitroprusside | - | - | - | - | - | - | - | - | - |
| Propofol infusion syndrome (prolonged high-dose propofol) | - | - | - | - | - | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Neurosurgery consultation — EMERGENT | STAT | STAT | - | STAT | All patients with elevated ICP need neurosurgical evaluation; ICP monitor/EVD placement; surgical decompression decisions; hematoma evacuation |
| Neuro-ICU admission | - | STAT | - | STAT | All patients with elevated ICP requiring intervention should be in Neuro-ICU or equivalent; 24/7 neuro-trained nursing; ICP monitoring capability; rapid imaging access |
| Continuous ICP monitoring (invasive) | - | STAT | - | STAT | If GCS ≤8 with abnormal CT; or GCS ≤8 with normal CT + risk factors; guides all ICP-directed therapy; allows CPP calculation |
| Continuous EtCO2 / frequent ABG | - | STAT | - | STAT | Ventilated patients: EtCO2 monitoring (correlate with ABG); target PaCO2 35-40; avoid hyperventilation except for acute crisis |
| Serial neurologic examination | STAT | STAT | - | STAT | q1-2h in unstable patients; pupil reactivity; GCS; motor response; detect early herniation; any decline → immediate intervention |
| HOB elevation 30° / midline head | STAT | STAT | - | STAT | Simple intervention; promotes venous drainage; reduces ICP |
| Avoid Valsalva / ICP-raising maneuvers | STAT | STAT | - | STAT | Prevent coughing during suctioning (pre-oxygenate, lidocaine); avoid tight cervical collar; avoid constipation; stool softeners |
| Normothermia | STAT | STAT | - | STAT | Treat fever aggressively; acetaminophen; cooling; each °C fever increases CMRO2 10-13% |
| Euvolemia | STAT | STAT | - | STAT | Avoid both hypovolemia (reduces CPP) and fluid overload (may worsen edema); isotonic fluids; monitor CVP/volume status |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Ophthalmology consultation | - | URGENT | ROUTINE | - | Fundoscopy for papilledema; IIH management; visual field testing; optic nerve sheath fenestration evaluation |
| Neurology consultation | - | URGENT | ROUTINE | URGENT | Seizure management; EEG interpretation; IIH management; stroke management |
| Physiatry / Rehabilitation | - | ROUTINE | ROUTINE | - | Early rehab evaluation; prognosis; disposition planning |
| Palliative care / Ethics | - | ROUTINE | ROUTINE | ROUTINE | Goals of care for poor prognosis patients; decompressive craniectomy discussions (survival vs. disability); brain death evaluation |
| Social work | - | ROUTINE | ROUTINE | - | Family support; long-term care planning; financial resources |
| Clinical neurophysiology / EEG | - | STAT | - | STAT | Continuous EEG for subclinical seizures; burst suppression monitoring; guide sedation |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Multimodal neuromonitoring | - | - | - | EXT | PbtO2 (brain tissue oxygen); SjvO2 (jugular venous saturation); cerebral microdialysis; optimize individual patient physiology; research/specialized centers |
| Targeted temperature management | - | - | - | EXT | 32-35°C for refractory ICP; slow rewarming; prevent fever; requires specialized cooling devices |
| Brain death evaluation | - | - | - | ROUTINE | If clinical brain death suspected; formal evaluation protocol; apnea testing; ancillary tests if confounders present |
| VP shunt / CSF diversion (long-term) | - | ROUTINE | ROUTINE | - | Definitive hydrocephalus management; IIH refractory to medical therapy; post-hemorrhagic hydrocephalus |
| Transverse sinus stenting (IIH) | - | - | ROUTINE | - | For IIH with venous sinus stenosis; reduces ICP; emerging therapy; specialized centers |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Causes of Elevated ICP

| Category | Etiologies | Key Features |
|----------|-----------|--------------|
| **Traumatic** | Traumatic brain injury (TBI); epidural hematoma; subdural hematoma; contusions; diffuse axonal injury | History of trauma; CT findings; mechanism of injury |
| **Vascular** | Ischemic stroke (malignant edema); intracerebral hemorrhage; subarachnoid hemorrhage; cerebral venous sinus thrombosis | Sudden onset; focal deficits; CT/MRI findings; angiography for vascular lesions |
| **Neoplastic** | Primary brain tumor; metastatic disease; leptomeningeal carcinomatosis | Subacute progressive; known cancer history; MRI with contrast |
| **Infectious** | Meningitis; encephalitis; brain abscess; subdural empyema | Fever; meningismus; CSF analysis; ring-enhancing lesion |
| **Hydrocephalus** | Obstructive (tumor, hemorrhage, aqueductal stenosis); communicating (post-infectious, post-hemorrhagic); normal pressure hydrocephalus | Ventricular enlargement on imaging; gait disturbance, dementia, incontinence (NPH triad) |
| **Idiopathic Intracranial Hypertension (IIH)** | Pseudotumor cerebri | Young obese women; headache; papilledema; pulsatile tinnitus; normal imaging; elevated OP on LP |
| **Metabolic** | Hepatic encephalopathy; hypertensive encephalopathy (PRES); hyponatremia (cerebral edema); hypoxic-ischemic injury | Metabolic derangement; toxic screen; liver function; blood pressure |
| **Other** | High altitude cerebral edema (HACE); post-operative; radiation necrosis; posterior reversible encephalopathy syndrome (PRES) | Exposure history; post-procedural; imaging pattern (PRES: posterior white matter edema) |

### Signs of Elevated ICP and Herniation

| Sign | Indication |
|------|-----------|
| **Cushing Triad** | Hypertension, bradycardia, irregular respirations — LATE and ominous sign of severely elevated ICP; indicates impending herniation |
| **Declining GCS** | Increasing ICP affecting reticular activating system |
| **Pupil asymmetry (unilateral dilation)** | Uncal herniation — compression of CN III; IPSILATERAL to lesion; dilated, fixed, "blown" pupil; emergent intervention needed |
| **Bilateral fixed pupils** | Late brainstem herniation; very poor prognosis |
| **Posturing (decerebrate/decorticate)** | Decorticate (flexion): midbrain/diencephalon dysfunction; Decerebrate (extension): pons/midbrain dysfunction; indicates progression |
| **Papilledema** | Chronically or subacutely elevated ICP (takes hours-days to develop); fundoscopy; absent papilledema does NOT exclude acutely elevated ICP |
| **Headache (worse lying down, morning)** | Increased ICP in recumbent position; chronic elevated ICP |
| **Nausea/vomiting (projectile)** | Brainstem compression; elevated ICP |
| **CN VI palsy** | "False localizing sign"; elevated ICP causes CN VI stretch along clivus; bilateral possible |

### Herniation Syndromes

| Syndrome | Anatomic Lesion | Clinical Features | Emergency Action |
|----------|----------------|-------------------|-----------------|
| **Uncal (transtentorial)** | Temporal lobe mass | Ipsilateral pupil dilation (CN III); contralateral hemiparesis; decreased LOC; then bilateral pupil dilation, decerebrate posturing | Osmotherapy STAT; hyperventilation; emergent surgical decompression |
| **Central (transtentorial)** | Bilateral supratentorial mass effect | Bilateral small pupils → bilateral fixed midpoint → bilateral dilated; progressive decrease in LOC; Cheyne-Stokes → central hyperventilation → ataxic breathing | Same as above; worse prognosis than uncal |
| **Subfalcine (cingulate)** | Unilateral hemisphere mass | Contralateral leg weakness (ACA compression); may progress to transtentorial herniation | Osmotherapy; surgical decompression of mass |
| **Tonsillar (cerebellar)** | Posterior fossa mass; severe supratentorial pressure | Neck stiffness; decreased LOC → respiratory arrest (medullary compression); rapid deterioration | EXTREME EMERGENCY; osmotherapy; emergent posterior fossa decompression; cardiopulmonary arrest imminent |
| **Upward (cerebellar)** | Posterior fossa mass with relief of supratentorial pressure | Pinpoint pupils; loss of upgaze; rapid coma | Posterior fossa decompression; avoid LP |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (ICU)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| ICP (if monitored) | Continuous | <22 mmHg (BTF 2016); some centers <20 | Tiered therapy escalation (osmotherapy → sedation → CSF drainage → hyperventilation → DC) |
| CPP (MAP - ICP) | Continuous (calculated) | 60-70 mmHg | If low: IV fluids, vasopressors; if high (>70) and ICP elevated: focus on ICP reduction |
| Neurologic exam (GCS, pupils, motor) | q1h initially; q2-4h when stable | Stable or improving | Decline: STAT CT; escalate ICP therapy; surgical evaluation |
| Serum sodium | q2-4h during active osmotherapy | 135-155 mEq/L (target varies); avoid rapid changes | Adjust osmotherapy; correct slowly if needed |
| Serum osmolality | q4-6h during mannitol therapy | <320 mOsm/kg (some use <315) | Hold mannitol if >320; switch to HTS |
| ABG / PaCO2 | q4-6h; more frequent if adjusting ventilation | 35-40 mmHg (normocapnia); 30-35 only for acute crisis | Adjust ventilator; avoid hyperventilation except for crisis |
| Temperature | Continuous | 36-37°C; strict normothermia | Aggressive cooling; acetaminophen; treat infection source |
| Blood glucose | q4-6h | 140-180 mg/dL | Insulin titration |
| Urine output | Hourly | 0.5-1 mL/kg/hr | Assess volume status; diuresis from mannitol expected (replace losses) |
| Hemodynamics (MAP) | Continuous | MAP to maintain CPP 60-70 | Vasopressors; volume |

### ICP Waveform Analysis

| Waveform | Interpretation |
|----------|---------------|
| Normal waveform | Three peaks: P1 (percussion) > P2 (tidal) > P3 (dicrotic); indicates normal intracranial compliance |
| Abnormal waveform | P2 > P1 ("rounded" waveform) = decreased intracranial compliance; indicates elevated ICP even if absolute value normal |
| Lundberg A waves (plateau waves) | Sustained ICP elevation to 50-100 mmHg for 5-20 min; indicates severely impaired compliance; ominous |
| Lundberg B waves | Oscillating ICP 20-50 mmHg at 0.5-2/min; indicates impaired compliance; precursor to A waves |
| Lundberg C waves | Oscillating ICP at 4-8/min; corresponds to arterial BP variations; normal |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| Neuro-ICU | Any patient requiring ICP monitoring; GCS ≤8; signs of herniation; requiring osmotherapy, sedation, or mechanical ventilation for ICP; post-operative after decompressive craniectomy or hematoma evacuation; status epilepticus; hemodynamic instability |
| Step-down / Intermediate care | Stable ICP; improving neurologically; EVD weaning; transitioning off invasive monitoring; stable post-operative |
| General neurology/neurosurgery floor | Stable IIH on medical therapy; post-VP shunt; stable post-operative without ICP concerns |

### Discharge Criteria

| Criterion | Details |
|-----------|---------|
| ICP normalized | ICP consistently <15-20 mmHg without intervention; EVD clamped successfully x 24-48h |
| Neurologic stability | Stable or improving neurologic exam; no new deficits; able to follow commands |
| Off ICP-lowering medications | Or transitioned to stable outpatient regimen (e.g., acetazolamide for IIH) |
| EVD removed / VP shunt functioning | CSF diversion resolved or definitive shunt placed |
| Seizure control | No seizures; stable AED regimen |
| Able to mobilize safely | PT/OT clearance; appropriate level of care for deficits |
| Follow-up arranged | Neurosurgery (1-2 weeks); neurology (as appropriate); ophthalmology (IIH); rehabilitation |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| [Guidelines for the Management of Severe Traumatic Brain Injury](https://pubmed.ncbi.nlm.nih.gov/27654000/) | Brain Trauma Foundation (BTF) | 2016 (4th ed) | ICP threshold 22 mmHg; CPP 60-70 mmHg; avoid prophylactic hyperventilation; avoid steroids; early seizure prophylaxis x 7 days |
| Malignant MCA Stroke Guidelines | AHA/ASA | 2019 | Decompressive craniectomy recommended for patients age <60 with malignant MCA stroke within 48h; discuss goals of care |
| ICH Guidelines | AHA/ASA | 2022 | BP target SBP <140 (intensive reduction); reversal of anticoagulation; surgery for cerebellar hemorrhage >3cm |
| SAH Guidelines | AHA/ASA | 2023 | Secure aneurysm early; nimodipine; EVD for hydrocephalus; euvolemia; monitor/treat vasospasm |
| IIH Guidelines | British Consensus Guidelines | 2018 | Weight loss; acetazolamide; serial LP; optic nerve fenestration for vision loss; VP shunt for refractory |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [BTF Guidelines (2016)](https://pubmed.ncbi.nlm.nih.gov/27654000/) | ICP threshold changed from 20 to 22 mmHg; CPP target 60-70 (avoid >70); Level IIA evidence for ICP monitoring improving outcomes | Standard of care for TBI ICP management |
| [CRASH Trial (2004)](https://pubmed.ncbi.nlm.nih.gov/15474134/) | Corticosteroids HARMFUL in TBI — 14-day mortality increased (25.7% vs. 22.3%, RR 1.15); 6-month mortality increased | Steroids absolutely contraindicated in TBI |
| [DECRA Trial (2011)](https://pubmed.ncbi.nlm.nih.gov/21434843/) | Early decompressive craniectomy (within 72h) for refractory ICP in TBI did NOT improve 6-month functional outcome (though reduced ICP and ICU stay) | Questioned early prophylactic DC; did not stop DC but informed timing decisions |
| [RESCUEicp Trial (2016)](https://pubmed.ncbi.nlm.nih.gov/27602507/) | Late/rescue DC for refractory ICP in TBI improved survival (48.9% vs. 26.9%) but increased proportion with severe disability; similar rates of favorable outcome | DC is life-saving but increases survival with disability; requires goals of care discussion |
| [DESTINY/DECIMAL/HAMLET (pooled)](https://pubmed.ncbi.nlm.nih.gov/17303527/) | DC for malignant MCA stroke <60 years within 48h reduces mortality (NNT=2); higher survival with moderate-severe disability (mRS 4); DC should be offered | Standard of care for malignant MCA stroke in appropriate patients |
| [EUROTHERM (2015)](https://pubmed.ncbi.nlm.nih.gov/26444221/) | Prophylactic hypothermia (32-35°C) in TBI HARMFUL — worse outcomes; trial stopped early | Hypothermia NOT recommended prophylactically; rescue use only for refractory ICP |
| [INTERACT2](https://pubmed.ncbi.nlm.nih.gov/23713578/) / [ATACH-2](https://pubmed.ncbi.nlm.nih.gov/27276234/) (ICH) | Intensive BP lowering (SBP <140) safe in ICH; modest benefit in INTERACT2; no benefit in ATACH-2 | SBP <140 within 6h is current recommendation for ICH |
| SAFE-TBI (2021) | 20% mannitol vs. hypertonic saline (various concentrations): no significant difference in ICP control or outcomes | Either osmotic agent acceptable; hypertonic saline may be preferred in hypovolemia |

### ICP and CPP Targets Summary

| Parameter | Target | Evidence Level |
|-----------|--------|---------------|
| ICP | <22 mmHg | BTF Level IIB |
| CPP | 60-70 mmHg | BTF Level IIB (avoid CPP <60; avoid >70 due to ARDS risk) |
| PaCO2 | 35-40 mmHg (normocapnia) | BTF Level IIB |
| PaCO2 (hyperventilation crisis) | 30-35 mmHg (brief, <30 min) | BTF Level III |
| Temperature | 36-37°C (normothermia) | BTF Level IIB |
| Glucose | 140-180 mg/dL | General critical care consensus |
| SBP (avoid hypotension) | >100 mmHg (or >110 for TBI age 50-69) | BTF Level III |

---

## APPENDICES

### Appendix A: Tiered ICP Management Algorithm

```
ELEVATED ICP SUSPECTED OR CONFIRMED
               │
    TIER 0: GENERAL MEASURES (all patients)
    • HOB 30°, midline head position
    • Avoid hyperthermia (target 36-37°C)
    • Avoid hypoxia (PaO2 >60), hypotension (SBP >90-100)
    • Adequate sedation and analgesia
    • Avoid constipation/Valsalva
    • Treat seizures
               │
    ICP >22 mmHg despite Tier 0?
               │
    TIER 1: FIRST-LINE MEDICAL THERAPY
    • CSF drainage via EVD (if available)
    • Osmotherapy: Mannitol 0.5-1 g/kg OR
                   HTS 3% 250mL or 23.4% 30mL
    • Ensure adequate sedation
    • Brief hyperventilation if acute crisis (PaCO2 30-35)
               │
    ICP >22 mmHg despite Tier 1?
               │
    TIER 2: ESCALATED THERAPY
    • Repeat osmotherapy dosing
    • Optimize CPP (vasopressors if needed)
    • Neuromuscular blockade
    • Moderate hyperventilation with monitoring (SjvO2 or PbtO2)
    • Consider surgical evacuation of mass lesion
               │
    ICP >22 mmHg despite Tier 2?
               │
    TIER 3: RESCUE THERAPY (discuss goals of care)
    • Pentobarbital coma (target burst suppression)
    • Therapeutic hypothermia (32-35°C)
    • Decompressive craniectomy
    • High-dose hypertonic saline (Na target 155-160)
```

### Appendix B: Osmotherapy Quick Reference

| Agent | Dose | Onset | Duration | Max Threshold | Administration | Monitoring |
|-------|------|-------|----------|--------------|----------------|------------|
| **Mannitol 20%** | 1-1.5 g/kg bolus; 0.25-0.5 g/kg repeat | 15-30 min | 2-6 hr | Serum osm >320 | Peripheral or central IV; filter; warm | Serum osm q4-6h; BMP q6h; Foley (massive diuresis) |
| **HTS 23.4%** | 30 mL over 15-20 min | 5-15 min | 2-4 hr | Na >160 (relative) | **Central line only** | Na q2-4h; avoid rapid Na changes |
| **HTS 3%** | 250-500 mL bolus or 30-50 mL/hr continuous | 15-30 min | 2-4 hr | Na >160 (relative) | Peripheral OK (central preferred) | Na q2-4h |
| **HTS 2%** | 500-1000 mL bolus or continuous | 30 min | 2-4 hr | Na >160 (relative) | Peripheral OK | Na q4-6h |

**Key differences:**
- Mannitol: Causes diuresis → may worsen hypovolemia; accumulates in brain with BBB disruption; renal toxicity with prolonged use; osmolar gap monitoring
- Hypertonic saline: No diuresis → better for hypovolemic patients; no osmolar gap ceiling; does not accumulate in brain; no renal toxicity; requires Na monitoring

### Appendix C: Herniation Emergency Protocol

```
SIGNS OF ACUTE HERNIATION
(Pupil dilation, posturing, Cushing triad, rapidly declining GCS)
                    │
    IMMEDIATE ACTIONS (within minutes):
    1. Call for help (neurosurgery STAT, airway team)
    2. HOB to 30° (or reverse Trendelenburg if C-spine)
    3. Hyperventilation if intubated: target PaCO2 30-35
       (bag at 20 breaths/min; avoid PaCO2 <25)
    4. Osmotherapy STAT:
       • Mannitol 1-1.5 g/kg IV push (100g = 500 mL of 20%)
         OR
       • 23.4% NaCl 30 mL IV via central line over 10-15 min
         OR
       • 3% NaCl 500 mL rapid infusion if no central access
    5. STAT CT head (if not already done)
    6. Prepare for emergent surgical intervention
                    │
    THESE ARE BRIDGE THERAPIES
    Definitive treatment = surgical decompression
    (hematoma evacuation, DC, tumor resection, EVD)
```

### Appendix D: IIH (Pseudotumor Cerebri) Management

| Intervention | Details |
|--------------|---------|
| **Weight loss** | Most important long-term intervention; 5-10% weight loss can significantly reduce ICP; bariatric surgery in morbid obesity |
| **Acetazolamide** | First-line medical therapy; 250 mg BID → titrate to 1-2 g/day (or max tolerated); carbonic anhydrase inhibitor reduces CSF production; side effects: paresthesias, fatigue, taste alteration, metabolic acidosis |
| **Topiramate** | Alternative to acetazolamide; also promotes weight loss; 50-100 mg BID; cognitive side effects |
| **Furosemide** | Adjunct to acetazolamide; 20-40 mg daily; less effective than acetazolamide alone |
| **Serial LP** | Therapeutic CSF removal; 20-30 mL per session; temporary relief; bridge to definitive treatment |
| **Optic nerve sheath fenestration** | Surgical; for progressive visual loss; protects optic nerve; may not reduce headache |
| **VP shunt** | Definitive CSF diversion; for refractory ICP or disabling headaches; shunt revision rates high |
| **Venous sinus stenting** | For patients with transverse sinus stenosis (common finding in IIH); emerging therapy; reduces ICP by improving venous outflow; specialized centers |

### Appendix E: Medications Affecting ICP

| Increases ICP | Decreases ICP |
|--------------|---------------|
| Ketamine (controversial — may be safe in controlled ventilation) | Propofol |
| Volatile anesthetics (at high concentrations) | Barbiturates (thiopental, pentobarbital) |
| Nitroprusside | Etomidate |
| Succinylcholine (transient) | Benzodiazepines (mild) |
| Hypercapnia | Fentanyl, remifentanil |
| Hypoxia | Mannitol, hypertonic saline |
| Fever | Hypothermia |
| Seizures | Neuromuscular blockers (by preventing ICP spikes from posturing/coughing) |
| Valsalva, coughing, straining | Hyperventilation (transient — use with caution) |

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
