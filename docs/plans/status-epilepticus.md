---
title: Status Epilepticus
description: Management of convulsive and non-convulsive status epilepticus including staged treatment protocol, NORSE/FIRES immunotherapy, and rapid protocol for non-specialists.
version: "1.4"
setting: ED, HOSP, ICU
status: approved
tags:
  - seizure
  - epilepsy
  - emergency
  - neurocritical-care
---

<div class="approved-banner">
  <span class="icon">✅</span>
  <div class="content">
    <div class="title">APPROVED - Ready for Clinical Use</div>
    <div class="description">This plan has been reviewed and approved. Comments and suggestions are still welcome.</div>
  </div>
</div>

# Status Epilepticus

**VERSION:** 1.4
**CREATED:** January 15, 2026
**REVISED:** January 19, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Status Epilepticus

**ICD-10:** G40.901 (Epilepsy, unspecified, not intractable, with status epilepticus), G41.0 (Grand mal status epilepticus), G41.1 (Petit mal status epilepticus), G41.2 (Complex partial status epilepticus), G41.8 (Other status epilepticus), G41.9 (Status epilepticus, unspecified)

**SCOPE:** Management of convulsive status epilepticus (CSE) and non-convulsive status epilepticus (NCSE) in adults. Covers staged treatment protocol from emergent benzodiazepines through refractory and super-refractory phases. Includes diagnostic workup to identify underlying etiology and specific protocols for NORSE/FIRES. Excludes pediatric status epilepticus, neonatal seizures, and psychogenic non-epileptic status.

---

**DEFINITIONS:**
- **Status Epilepticus (SE):** Seizure lasting >5 minutes OR ≥2 seizures without return to baseline between episodes
- **Refractory SE (RSE):** SE continuing after adequate doses of initial benzodiazepine AND one second-line ASM
- **Super-Refractory SE (SRSE):** SE continuing ≥24 hours after anesthetic initiation, including cases that recur during anesthetic weaning
- **NORSE:** New-Onset Refractory Status Epilepticus - RSE without clear acute/active structural, toxic, or metabolic cause in a patient without prior epilepsy
- **FIRES:** Febrile Infection-Related Epilepsy Syndrome - subset of NORSE with febrile illness ≥24 hours before SE onset

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

!!! danger "⚡ RAPID PROTOCOL FOR NON-SPECIALISTS"
    **Need the quick "3 AM Protocol"?** Skip to [**APPENDIX C: Rapid Protocol**](#appendix-c-rapid-protocol-for-non-specialists) at the bottom of this document for a single default pathway with exact doses.

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Point-of-care glucose | STAT | STAT | - | STAT | Hypoglycemia is immediately reversible cause | >70 mg/dL |
| CBC with differential | STAT | STAT | - | STAT | Infection screen, baseline before ASMs | Normal |
| CMP (BMP + LFTs) | STAT | STAT | - | STAT | Electrolyte abnormalities, renal/hepatic function for ASM dosing | Normal |
| Magnesium | STAT | STAT | - | STAT | Hypomagnesemia lowers seizure threshold | >1.8 mg/dL |
| Calcium (ionized if available) | STAT | STAT | - | STAT | Hypocalcemia can cause seizures | Ionized 4.5-5.3 mg/dL |
| Phosphorus | STAT | STAT | - | STAT | Hypophosphatemia lowers seizure threshold | >2.5 mg/dL |
| Blood gas (ABG or VBG) | STAT | STAT | - | STAT | Acidosis, oxygenation, ventilation status | pH >7.2; correct severe acidosis |
| Lactate | STAT | STAT | - | STAT | Elevated in prolonged seizure; marker of severity | Will be elevated; trending useful |
| Urine drug screen | STAT | STAT | - | STAT | Illicit drugs, withdrawal states | Identify triggers |
| Blood alcohol level | STAT | STAT | - | STAT | Alcohol withdrawal common cause | Correlate with history |
| ASM levels (if on therapy) | STAT | STAT | - | STAT | Subtherapeutic levels as precipitant | Therapeutic range |
| Pregnancy test (women of childbearing age) | STAT | STAT | - | STAT | Eclampsia; affects ASM choice | Document status |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Ammonia | URGENT | STAT | - | STAT | Hepatic encephalopathy, valproate toxicity, urea cycle disorders | <35 μmol/L |
| TSH | URGENT | ROUTINE | - | URGENT | Thyroid storm/myxedema | Normal |
| Troponin | URGENT | ROUTINE | - | STAT | Cardiac stress from prolonged seizure | May be elevated |
| CPK/CK | URGENT | ROUTINE | - | STAT | Rhabdomyolysis from prolonged convulsions | Elevated; monitor trend |
| Cortisol (random) | URGENT | ROUTINE | - | URGENT | Adrenal insufficiency | Normal stress response |
| Serum osmolality | URGENT | ROUTINE | - | URGENT | Hypo/hyperosmolar states | 280-295 mOsm/kg |
| Procalcitonin | URGENT | ROUTINE | - | URGENT | CNS infection if suspected | <0.5 ng/mL |
| Coagulation panel (PT/INR, PTT) | URGENT | ROUTINE | - | STAT | Pre-LP, hemorrhage risk | Normal |
| Type and screen | URGENT | ROUTINE | - | STAT | Anticipate possible surgical intervention | Available |
| Urinalysis | URGENT | ROUTINE | - | URGENT | UTI as precipitant (especially elderly) | Negative |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Autoimmune encephalitis panel (serum) | - | URGENT | - | URGENT | Anti-NMDAR, LGI1, CASPR2 in NORSE | Negative |
| Paraneoplastic panel (serum) | - | URGENT | - | URGENT | Subacute onset, smoking history, weight loss | Negative |
| HIV | - | ROUTINE | - | ROUTINE | HIV-associated CNS disease | Negative |
| RPR/VDRL | - | ROUTINE | - | ROUTINE | Neurosyphilis | Negative |
| Ceruloplasmin, serum copper | - | EXT | - | EXT | Wilson disease (young patients) | Normal |
| Porphyrins (urine/serum) | - | EXT | - | EXT | Acute intermittent porphyria | Normal |
| Mitochondrial DNA testing | - | - | - | EXT | MELAS, other mitochondrial disorders | Normal |
| Pyridoxine trial (empiric) | - | - | - | URGENT | Pyridoxine-dependent seizures (rare, usually pediatric) | Response to treatment |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast | STAT | STAT | - | STAT | Immediately after stabilization | Mass, hemorrhage, stroke, herniation, hydrocephalus | None in emergency |
| Continuous EEG (cEEG) monitoring | STAT | STAT | - | STAT | As soon as available; mandatory in RSE/SRSE | Seizure burden, treatment response, NCSE detection | None significant |
| Chest X-ray | STAT | STAT | - | STAT | Aspiration risk, ETT placement confirmation | Aspiration, ETT position | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast | - | URGENT | - | URGENT | When stable; within 24-48h | Encephalitis, stroke, tumor, cortical injury from SE | Hemodynamic instability, pacemaker |
| CT angiography head/neck | URGENT | URGENT | - | URGENT | If stroke suspected | Large vessel occlusion, dissection | Contrast allergy, renal insufficiency |
| MRA/MRV brain | - | ROUTINE | - | ROUTINE | If vascular etiology suspected | Venous thrombosis, vascular malformation | Same as MRI |
| CT chest/abdomen/pelvis | - | ROUTINE | - | ROUTINE | If paraneoplastic suspected | Occult malignancy | Contrast allergy |
| Echocardiogram | - | ROUTINE | - | ROUTINE | If embolic stroke suspected, endocarditis | Vegetation, thrombus | None |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| PET-CT (whole body) | - | EXT | - | EXT | Occult malignancy workup | Tumor identification | Hemodynamic instability |
| Brain biopsy | - | EXT | - | EXT | Refractory cases, suspected encephalitis | Histopathologic diagnosis | Coagulopathy, critical location |

### LUMBAR PUNCTURE

**Indication:** Suspected CNS infection (meningitis, encephalitis), autoimmune encephalitis, NORSE/FIRES, or unknown etiology after initial workup

**Timing:** URGENT after CT excludes mass effect; do not delay empiric antibiotics/antivirals

**Volume Required:** 15-20 mL standard; 20-30 mL if autoimmune/malignancy suspected

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| Opening pressure | URGENT | STAT | - | STAT | Elevated ICP | 10-20 cm H2O |
| Cell count (tubes 1 and 4) | URGENT | STAT | - | STAT | Infection, inflammation | WBC <5; RBC 0 |
| Protein | URGENT | STAT | - | STAT | Elevated in infection, inflammation | 15-45 mg/dL |
| Glucose with serum glucose | URGENT | STAT | - | STAT | Low in bacterial/fungal meningitis | >60% serum |
| Gram stain and culture | URGENT | STAT | - | STAT | Bacterial meningitis | No organisms |
| BioFire FilmArray ME Panel | URGENT | STAT | - | STAT | Rapid pathogen identification | Negative |
| HSV-1/2 PCR | URGENT | STAT | - | STAT | HSV encephalitis | Negative |
| Autoimmune encephalitis panel (CSF) | - | URGENT | - | URGENT | NORSE, limbic encephalitis | Negative |
| Cytology | - | ROUTINE | - | ROUTINE | Carcinomatous meningitis | Negative |
| Oligoclonal bands | - | ROUTINE | - | ROUTINE | Demyelinating disease | Negative |

**Special Handling:** HSV PCR refrigerated. Cytology rapid transport (<1 hour). Cell count within 1 hour.

**Contraindications:** Signs of herniation, coagulopathy (INR >1.5, platelets <50K), skin infection at LP site. CT before LP if any concern for mass effect.

---

## 3. TREATMENT

**CRITICAL:** Status epilepticus requires STAGED, TIME-BASED management. Each medication must be on its own row with complete dosing.

**👉 FOR RAPID DEFAULT PATHWAY, SEE [APPENDIX C](#appendix-c-rapid-protocol-for-non-specialists) AT THE BOTTOM OF THIS DOCUMENT**

### TREATMENT STAGING OVERVIEW

| Stage | Time | Goal | Primary Agents |
|-------|------|------|----------------|
| **Stabilization** | 0-5 min | ABCs, glucose, thiamine | Supportive care |
| **Emergent (1st line)** | 0-5 min | Abort seizure | Benzodiazepines |
| **Urgent (2nd line)** | 5-20 min | Seizure control if BZD fails | Fosphenytoin, valproate, levetiracetam, lacosamide, or brivaracetam |
| **Refractory (3rd line)** | 20-60 min | Anesthetic coma if 2nd line fails | Midazolam, propofol, or ketamine infusion |
| **Super-refractory** | >24h on anesthetics | Seizure control | Additional agents, immunotherapy for NORSE |

### 3A. Stabilization (Time 0)

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Airway positioning/management | STAT | STAT | - | STAT | Head-tilt chin-lift, oral airway, prepare for intubation | None | O2 sat, airway patency |
| Supplemental oxygen | STAT | STAT | - | STAT | Non-rebreather 15 L/min or bag-valve-mask | None | O2 sat >94% |
| IV access (two large-bore) | STAT | STAT | - | STAT | 18G or larger x2 | None | IV patency |
| Cardiac monitoring | STAT | STAT | - | STAT | Continuous telemetry | None | Rhythm, HR, BP |
| Dextrose 50% IV | STAT | STAT | - | STAT | 50 mL IV push (25g) if glucose <70 or unknown | Document hyperglycemia | Glucose |
| Thiamine IV | STAT | STAT | - | STAT | 100-500 mg IV BEFORE or WITH glucose | None | None |
| Isotonic fluids | STAT | STAT | - | STAT | NS or LR wide open initially | Pulmonary edema | BP, I/O |

### 3B. Emergent/First-Line - Benzodiazepines (Time 0-5 min)

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Lorazepam IV | STAT | STAT | - | STAT | 0.1 mg/kg IV (max 4 mg/dose); may repeat x1 in 5 min if still seizing; total max 8 mg | Acute narrow-angle glaucoma | RR, O2 sat, BP, sedation; airway equipment ready |
| Midazolam IM | STAT | STAT | - | STAT | 10 mg IM (≥40 kg) or 0.2 mg/kg IM (if no IV access); single dose | Respiratory compromise | RR, O2 sat; prepare IV access |
| Midazolam IV | STAT | STAT | - | STAT | 0.2 mg/kg IV (max 10 mg); may repeat x1 | Same as lorazepam | RR, O2 sat, BP |
| Midazolam intranasal | STAT | STAT | - | STAT | 5 mg per nostril (10 mg total) if no IV/IM access | Nasal obstruction | RR, O2 sat |
| Midazolam buccal | STAT | STAT | - | STAT | 10 mg buccal (if available) | Oral trauma | RR, O2 sat |
| Diazepam IV | STAT | STAT | - | STAT | 0.15 mg/kg IV (max 10 mg); may repeat x1 in 5 min | Acute narrow-angle glaucoma | RR, O2 sat; short duration - requires follow-up ASM |
| Diazepam rectal | STAT | STAT | - | STAT | 0.2-0.5 mg/kg PR (max 20 mg); use rectal gel formulation | Rectal pathology | RR, O2 sat |

**NOTE:** If seizure continues after 2 adequate doses of benzodiazepine, immediately proceed to second-line agent. Do NOT give additional benzodiazepines.

### 3C. Urgent/Second-Line ASMs (Time 5-20 min)

**DOSING NOTE:** Levetiracetam dosing options reflect evolving evidence. ESETT trial used 60 mg/kg; some institutions use 40 mg/kg. Both are acceptable.

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Levetiracetam IV (ESETT dosing) | STAT | STAT | - | STAT | 60 mg/kg IV (max 4500 mg) over 10-15 min | None absolute; reduce if CrCl <50 | Generally well tolerated; agitation |
| Levetiracetam IV (conservative) | STAT | STAT | - | STAT | 40 mg/kg IV (max 4500 mg) over 10-15 min | None absolute; reduce if CrCl <50 | Generally well tolerated; agitation |
| Fosphenytoin IV | STAT | STAT | - | STAT | 20 mg PE/kg IV at 150 mg PE/min; may give additional 5-10 mg PE/kg if needed | 2nd/3rd degree AV block, sinus bradycardia, allergy | Continuous cardiac monitor, BP q5min during infusion |
| Valproate IV | STAT | STAT | - | STAT | 40 mg/kg IV (max 3000 mg) over 10 min | Pregnancy, hepatic disease, mitochondrial disease, urea cycle disorders, pancreatitis | Ammonia, LFTs; avoid in unknown pregnancy status |
| Lacosamide IV | STAT | STAT | - | STAT | 400 mg IV over 15 min (can give 200 mg over 5 min if urgent) | PR >200 ms, 2nd/3rd degree AV block, severe hepatic impairment | ECG for PR interval |
| Brivaracetam IV | STAT | STAT | - | STAT | 100-200 mg IV over 2-5 min; no titration needed | Hepatic impairment (reduce dose) | Faster onset than levetiracetam; fewer behavioral effects |
| Phenytoin IV | STAT | STAT | - | STAT | 20 mg/kg IV at max 50 mg/min (if fosphenytoin unavailable) | AV block, sinus bradycardia | Cardiac monitor; MUST use large vein, tissue necrosis risk |
| Phenobarbital IV | STAT | STAT | - | STAT | 15-20 mg/kg IV at 50-100 mg/min | Severe respiratory disease, porphyria | Respiratory depression; often requires intubation at this dose |

**NOTES:**
- Choose ONE second-line agent initially
- If first second-line agent fails, may try second agent OR proceed to anesthetics (do not delay >20 min)
- Levetiracetam, lacosamide, and brivaracetam have fewer drug interactions and hemodynamic effects
- Brivaracetam may have faster onset than levetiracetam; useful if patient already on levetiracetam at home
- Phenobarbital highly effective but significant respiratory depression - have airway ready
- **ESETT Trial (Kapur et al., NEJM 2019):** Levetiracetam 60 mg/kg, fosphenytoin 20 mg/kg PE, and valproate 40 mg/kg showed equivalent efficacy (~47% success)

### 3D. Refractory SE - Anesthetic Infusions (Time 20-60 min)

**INDICATION:** Seizures continue after benzodiazepine AND one second-line ASM at adequate doses

**SETTING:** ICU with continuous EEG monitoring, mechanical ventilation capability

**KETAMINE TIMING NOTE:** Emerging evidence supports earlier ketamine use. Ketamine is twice as effective when given early in RSE (64% efficacy) vs late/SRSE (32% efficacy). Consider ketamine as first-line anesthetic OR as adjunct to midazolam from the start of RSE. Earlier administration correlates with better outcomes.

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Midazolam infusion | URGENT | - | - | STAT | Load: 0.2 mg/kg IV bolus; Infusion: start 0.1 mg/kg/hr, titrate by 0.1 mg/kg/hr q15min to seizure suppression; max 2 mg/kg/hr; target burst suppression on cEEG | Hemodynamic instability (relative) | cEEG, BP (hypotension common), sedation scale |
| Propofol infusion | - | - | - | STAT | Load: 1-2 mg/kg IV bolus (may repeat x1); Infusion: start 20 mcg/kg/min, titrate by 10 mcg/kg/min q5min; max 200 mcg/kg/min; target burst suppression | Propofol infusion syndrome risk (limit to <48h at high dose), egg/soy allergy, pregnancy | cEEG, triglycerides q24-48h, CPK, metabolic acidosis, BP |
| Ketamine infusion | URGENT | - | - | STAT | Load: 1-2 mg/kg IV bolus; Infusion: start 1 mg/kg/hr, titrate by 0.5 mg/kg/hr q15-30min; max 5 mg/kg/hr | Uncontrolled hypertension, elevated ICP (relative - actually may be neuroprotective) | cEEG, BP (may increase), HR; less hypotension than other anesthetics |
| Ketamine + Midazolam (combination) | - | - | - | STAT | Ketamine load 1 mg/kg + Midazolam load 0.2 mg/kg; then dual infusions per above | Per individual agents | 2024 data: combination may reduce SE duration faster than midazolam alone |
| Pentobarbital infusion | - | - | - | STAT | Load: 5-15 mg/kg IV at 50 mg/min; Infusion: start 0.5-1 mg/kg/hr, titrate to burst suppression; max 5 mg/kg/hr | Severe cardiac dysfunction | cEEG, BP (significant hypotension - need pressors), cardiac output; longest half-life |

**NOTES:**
- Midazolam or propofol typically first choice; **consider ketamine early or in combination**
- Ketamine advantages: NMDA antagonism targets receptor changes in prolonged SE; less hypotension; potentially neuroprotective
- Pentobarbital most potent but worst hemodynamic effects; reserve for SRSE
- All require intubation and continuous EEG (exception: ketamine may be used without intubation in select cases per emerging data)
- Target: burst suppression or seizure suppression on cEEG for 24-48h before weaning

### 3E. Super-Refractory SE - Additional Agents

**DEFINITION:** SE continues or recurs ≥24 hours after anesthetic initiation

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Add second anesthetic | - | - | - | STAT | Combine midazolam + propofol, or add ketamine to either | Per agent | cEEG, hemodynamics |
| Topiramate (enteral) | - | - | - | URGENT | Load 300-400 mg via NGT; then 200-400 mg BID; max 1600 mg/day | Metabolic acidosis, kidney stones | Bicarbonate, renal function |
| Lacosamide (if not tried) | - | - | - | URGENT | 400 mg IV, then 200-400 mg BID | PR prolongation | ECG |
| Perampanel (enteral) | - | - | - | ROUTINE | 4-8 mg via NGT daily; titrate to 12 mg daily | None absolute | Aggression, sedation |
| Magnesium sulfate infusion | - | - | - | URGENT | 4-6 g IV over 20 min, then 1-2 g/hr infusion; target Mg 3.5-4 mg/dL | Renal failure (relative), myasthenia | Mg levels, reflexes, respiratory status |
| Pyridoxine (empiric trial) | - | - | - | URGENT | 100-500 mg IV; may try single dose empirically | None | Response to treatment |
| Ketogenic diet | - | - | - | URGENT | Initiate within 7 days per NORSE consensus; requires nutrition support | Pyruvate carboxylase deficiency, fatty acid oxidation disorders | Ketones, glucose, lipids |
| Hypothermia (32-35°C) | - | - | - | EXT | Targeted temperature management x 24-48h | Coagulopathy, severe infection | Temperature, coagulation, infection |
| Electroconvulsive therapy | - | - | - | EXT | If all else fails; requires anesthesia | Raised ICP, recent stroke | Per ECT protocol |
| Epilepsy surgery (emergent) | - | - | - | EXT | Resection if focal lesion identified | Eloquent cortex, multifocal | Per surgical team |

### 3F. NORSE/FIRES Immunotherapy Protocol

**INDICATION:** New-onset RSE without clear etiology after initial workup; suspect autoimmune/inflammatory cause

**REFERENCE:** International Consensus Recommendations (Wickström et al., Epilepsia 2022)

#### Timeline-Based Protocol

| Timing | Intervention | Dosing | Notes |
|--------|--------------|--------|-------|
| **Day 0-3** | First-line immunotherapy | See below | Start within 72 hours if no clear etiology |
| **Day 3-7** | Escalate if no response | Add remaining first-line agents | Do not delay |
| **Day 7** | Ketogenic diet | Initiate with nutrition support | One of few treatments with evidence in FIRES |
| **Day 7+** | Second-line immunotherapy | If first-line inadequate | Earlier may be better |

#### First-Line Immunotherapy (Start within 72 hours)

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Methylprednisolone IV | - | URGENT | - | STAT | 1000 mg IV daily × 3-5 days | Active untreated infection (relative) | Glucose q6h, BP, GI prophylaxis, infection signs |
| IVIG | - | URGENT | - | STAT | 0.4 g/kg/day IV × 5 days (total 2 g/kg); can give simultaneously with steroids | IgA deficiency (use IgA-depleted product), renal failure, thrombosis risk | Renal function, signs of aseptic meningitis, thrombosis |
| Plasmapheresis (PLEX) | - | ROUTINE | - | STAT | 5-7 exchanges over 10-14 days; 1-1.5 plasma volumes per exchange | Hemodynamic instability, line access issues | Hemodynamics, electrolytes (Ca, Mg), coagulation, fibrinogen |

**NOTES:**
- Steroids preferred as initial agent; can combine with IVIG from start
- Do not wait for autoimmune panel results to initiate treatment
- Sequential (steroids → IVIG → PLEX) or simultaneous approach acceptable

#### Second-Line Immunotherapy (If first-line fails by Day 7)

| Treatment | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Rituximab | - | - | - | ROUTINE | 375 mg/m² IV weekly × 4 doses | Active infection, hepatitis B (screen first) | Infusion reactions, infection, B-cell counts |
| Cyclophosphamide | - | - | - | ROUTINE | 750-1000 mg/m² IV monthly × 3-6 months | Severe cytopenias, active infection | CBC weekly, renal function, hemorrhagic cystitis (hydration + mesna) |
| Tocilizumab | - | - | - | EXT | 8 mg/kg IV q4 weeks (emerging option) | Active infection, hepatic impairment | LFTs, lipids, infection |
| Anakinra | - | - | - | EXT | 100 mg SC daily (may increase; used in FIRES) | Active infection | Injection site reactions, infection |

### 3G. Symptomatic/Supportive ICU Care

| Treatment | Indication | ED | HOSP | OPD | ICU | Dosing | Contraindications | Monitoring |
|-----------|------------|:--:|:----:|:---:|:---:|--------|-------------------|------------|
| Norepinephrine | Hypotension from anesthetics | - | - | - | STAT | Start 0.1 mcg/kg/min; titrate to MAP ≥65 | Hypovolemia (correct first) | Arterial line, MAP |
| Vasopressin | Adjunct pressor | - | - | - | STAT | 0.04 units/min fixed dose | Cardiac ischemia | MAP, cardiac status |
| Fentanyl infusion | Analgesia/sedation adjunct | - | - | - | ROUTINE | 25-100 mcg/hr; titrate to comfort | Hemodynamic instability | Pain scale, respiratory status |
| Propofol (sub-anesthetic) | Sedation during cEEG | - | - | - | ROUTINE | 5-50 mcg/kg/min | Same as anesthetic use | Sedation scale |
| Dexmedetomidine | Sedation, possible antiseizure | - | - | - | ROUTINE | 0.2-1.5 mcg/kg/hr | Bradycardia, heart block | HR, BP |
| Pantoprazole | Stress ulcer prophylaxis | - | ROUTINE | - | STAT | 40 mg IV daily | None significant | GI bleeding |
| Enoxaparin | DVT prophylaxis | - | ROUTINE | - | STAT | 40 mg SC daily (start when stable) | Active bleeding, recent LP | Platelets, bleeding |
| Insulin infusion | Stress hyperglycemia | URGENT | ROUTINE | - | STAT | Per ICU protocol; target glucose 140-180 mg/dL | Hypoglycemia | Glucose q1-4h |
| Bowel regimen | Constipation prophylaxis | - | ROUTINE | - | ROUTINE | Docusate 100 mg BID + senna 8.6 mg daily; escalate to bisacodyl or lactulose PRN | Bowel obstruction | Bowel movements |
| Skin care protocol | Pressure injury prevention | - | ROUTINE | - | STAT | Turn q2h, specialty mattress, moisture barrier, Braden scale assessment | None | Skin integrity daily |
| Eye care | Corneal protection | - | ROUTINE | - | STAT | Lubricating drops q4h, eyelid taping if incomplete closure | None | Corneal integrity |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology/Epilepsy STAT consult | STAT | STAT | - | STAT | All cases of SE |
| Neurocritical care consult | STAT | STAT | - | STAT | RSE/SRSE, need for anesthetic infusions |
| ICU admission | STAT | STAT | - | - | All SE requiring second-line agents or ongoing seizures |
| EEG technologist/cEEG initiation | STAT | STAT | - | STAT | Mandatory for RSE/SRSE; strongly recommended for all SE |
| Infectious disease consult | - | URGENT | - | URGENT | Suspected CNS infection |
| Rheumatology/Neuroimmunology consult | - | URGENT | - | URGENT | NORSE/FIRES, suspected autoimmune encephalitis |
| Pharmacy consult | - | ROUTINE | - | ROUTINE | Complex ASM dosing, drug interactions |
| Nutrition/Dietitian consult | - | ROUTINE | - | URGENT | Enteral feeding, ketogenic diet initiation (by Day 7 in NORSE) |
| Palliative care consult | - | - | - | ROUTINE | SRSE with poor prognosis, goals of care discussion |
| Social work consult | - | ROUTINE | ROUTINE | ROUTINE | Family support, discharge planning |
| Epilepsy surgery evaluation | - | - | EXT | EXT | Focal lesion on imaging, refractory to medical therapy |
| PT/OT/Speech evaluation | - | ROUTINE | ROUTINE | ROUTINE | Once stabilized; assess for deficits |
| Epilepsy outpatient follow-up | - | ROUTINE | ROUTINE | - | All SE survivors; ASM optimization, etiology workup |
| Outpatient video-EEG monitoring | - | - | ROUTINE | - | Characterization of seizure type, presurgical evaluation |
| Neuropsychology testing | - | - | ROUTINE | - | Cognitive assessment post-SE; baseline before surgery |

### 4B. Patient/Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Explain SE is a medical emergency requiring ICU care | STAT | STAT | - |
| Discuss prognosis based on etiology and duration of SE | - | URGENT | - |
| Educate on importance of ASM adherence (if applicable) | - | ROUTINE | - |
| Seizure first aid education for family | - | ROUTINE | - |
| Rescue medication training (rectal diazepam, nasal midazolam) | - | ROUTINE | - |
| Driving restrictions (minimum 3-6 months seizure-free, varies by state) | - | ROUTINE | - |
| Medical alert bracelet recommendation | - | ROUTINE | - |
| Seizure action plan development | - | ROUTINE | - |
| Discuss goals of care if SRSE with poor prognosis | - | - | ROUTINE (ICU) |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Medication adherence counseling | - | ROUTINE | - |
| Avoid abrupt ASM discontinuation (common SE precipitant) | - | ROUTINE | - |
| Alcohol cessation | - | ROUTINE | - |
| Sleep hygiene (sleep deprivation lowers threshold) | - | ROUTINE | - |
| Avoid known seizure triggers | - | ROUTINE | - |
| Drug interaction review (OTC, supplements) | - | ROUTINE | - |
| Pregnancy planning counseling (women of childbearing potential) | - | ROUTINE | - |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Psychogenic non-epileptic status | Preserved awareness, asynchronous movements, eye closure, pelvic thrusting, prolonged duration with minimal post-ictal period | Video EEG, normal cEEG during event |
| Convulsive syncope | Brief (< 30 sec), occurs with LOC, myoclonic jerks possible | History of prodrome, rapid recovery, normal EEG |
| Movement disorders (dystonia, chorea) | Non-rhythmic, preserved awareness, stereotyped pattern | EEG normal during movements |
| Rigors (sepsis, transfusion reaction) | Associated with fever/chills, rhythmic shaking, preserves awareness | Infectious workup, temperature, EEG normal |
| Decerebrate/decorticate posturing | Associated with structural brain injury, sustained posturing | Imaging, cEEG |
| Drug-induced dyskinesia | Medication history, stereotyped movements | Drug levels, history, EEG normal |
| Neuroleptic malignant syndrome | Rigidity, hyperthermia, AMS, autonomic instability | CPK, medication history |
| Serotonin syndrome | Hyperreflexia, clonus, agitation, fever | Medication history, clinical features |
| Tetanus | Sustained muscle contraction, trismus, opisthotonos | History of wound, vaccination status |
| Strychnine poisoning | Opisthotonus with preserved consciousness | Toxicology |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Continuous EEG | STAT | STAT | - | STAT | Continuous | No seizures; burst suppression if on anesthetics | Adjust ASMs/anesthetics |
| Cardiac telemetry | STAT | STAT | - | STAT | Continuous | Normal rhythm, HR 60-100 | Treat arrhythmia; assess ASM effect |
| Pulse oximetry | STAT | STAT | - | STAT | Continuous | O2 sat >94% | Increase O2, assess airway |
| Blood pressure | STAT | STAT | - | STAT | q5min during treatment, then q1h | MAP ≥65; avoid severe hypertension | Pressors or antihypertensives |
| Neurologic exam | STAT | STAT | - | STAT | q1-2h when off sedation | Return to baseline | Imaging, reassess etiology |
| Glucose | STAT | STAT | - | STAT | q1-4h | 140-180 mg/dL (ICU) | Insulin or dextrose |
| Electrolytes (Na, K, Mg, Ca, Phos) | STAT | STAT | - | STAT | q6-12h | Normal ranges | Replete deficiencies |
| ABG/VBG | STAT | ROUTINE | - | STAT | q4-6h (RSE), PRN | pH >7.25, CO2 35-45, PO2 >60 | Adjust ventilator, treat acidosis |
| Lactate | STAT | ROUTINE | - | STAT | q6-12h | Trending down | Treat underlying cause |
| ASM levels | URGENT | ROUTINE | - | URGENT | 24h after load, then PRN | Therapeutic range | Adjust dosing |
| Ammonia | URGENT | ROUTINE | - | STAT | q24h if on valproate | <35 μmol/L | Reduce/stop valproate |
| LFTs | URGENT | ROUTINE | - | ROUTINE | q24-48h | Normal | Adjust hepatically-metabolized ASMs |
| Renal function | URGENT | ROUTINE | - | STAT | q24h | Normal | Adjust renally-cleared ASMs |
| CPK | - | ROUTINE | - | STAT | q12-24h if prolonged convulsions | Trending down | Aggressive hydration, monitor renal |
| Triglycerides | - | - | - | ROUTINE | q24-48h if on propofol | <400 mg/dL | Reduce propofol dose |
| Temperature | STAT | STAT | - | STAT | q4h | 36-38°C | Infection workup; cooling if hyperthermic |
| ICP (if monitored) | - | - | - | STAT | Continuous | <20 mmHg | ICP management protocol |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| ICU admission (REQUIRED) | All SE requiring second-line ASMs; all RSE/SRSE; altered mental status; need for airway management; hemodynamic instability |
| Step-down/Telemetry | Seizures controlled x 24h, off anesthetics x 24h, stable neuro exam, no airway concerns |
| General floor | Seizures controlled, off continuous monitoring, stable on oral ASMs, resolved AMS |
| Discharge home | Seizures controlled, stable on oral ASM regimen, etiology identified and addressed, family educated, follow-up arranged |
| Transfer to higher level care | Need for services unavailable (cEEG, neurocritical care, epilepsy surgery evaluation) |
| Long-term care/Rehab | Persistent deficits after prolonged SE, need for ongoing rehabilitation |
| Palliative/Hospice | SRSE with irreversible brain injury, goals of care established |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Benzodiazepines first-line for SE | Class I, Level A | Neurocritical Care Society 2012; AES Guidelines 2016 |
| Lorazepam preferred IV benzodiazepine | Class I, Level A | Alldredge et al. NEJM 2001 |
| IM midazolam non-inferior to IV lorazepam | Class I, Level A | RAMPART Trial, Silbergleit et al. NEJM 2012 |
| Second-line agents (LEV, VPA, fPHT) equivalent efficacy | Class I, Level A | ESETT Trial, Kapur et al. NEJM 2019;381:2103-2113 |
| Levetiracetam 60 mg/kg dosing | Class I, Level A | ESETT Trial - higher than traditional 20-40 mg/kg |
| Levetiracetam 40 mg/kg may be adequate | Class II, Level B | Meta-analysis, pharmacokinetic modeling 2023-2024 |
| cEEG monitoring in RSE | Class I, Level B | NCS Guidelines 2012 |
| Burst suppression target for RSE | Class IIb, Level C | Expert consensus |
| Ketamine in RSE/SRSE | Class IIb, Level B | Multiple case series; 2024 systematic reviews |
| Earlier ketamine = better outcomes | Class II, Level B | 2024 two-center study; systematic reviews |
| Ketamine efficacy in RSE/SRSE | Class IIa, Level B | Systematic review: Rosati A et al., CNS Drugs 2018;32(11):997-1009 |
| Ketamine ± midazolam superiority over midazolam alone | Class II, Level B | Fletman et al., Clin Neurol Neurosurg 2024; Yan et al., J Neurol 2024 |
| NORSE first-line immunotherapy within 72h | Class IIa, Level C | International Consensus, Wickström et al. Epilepsia 2022 |
| Ketogenic diet by Day 7 in NORSE | Class IIa, Level C | International Consensus 2022; FIRES case series |
| Second-line immunotherapy by Day 7 if first-line fails | Class IIb, Level C | International Consensus 2022 |
| Brivaracetam for SE | Class IIb, Level C | Emerging evidence; case series |

---

## APPENDIX A: TIME-BASED TREATMENT ALGORITHM

```
TIME 0-5 MIN: STABILIZATION + EMERGENT TREATMENT
├── ABCs: Airway, Breathing, Circulation
├── Glucose check → Dextrose if low + Thiamine
├── IV access x 2
├── Lorazepam 0.1 mg/kg IV (max 4 mg) OR Midazolam 10 mg IM
└── May repeat BZD x1 in 5 min

TIME 5-20 MIN: URGENT/SECOND-LINE (if still seizing)
├── Choose ONE:
│   ├── Levetiracetam 40-60 mg/kg IV (max 4500 mg)
│   ├── Fosphenytoin 20 mg PE/kg IV at 150 mg PE/min
│   ├── Valproate 40 mg/kg IV (max 3000 mg) - avoid in pregnancy
│   ├── Lacosamide 400 mg IV
│   └── Brivaracetam 100-200 mg IV (if available)
├── Start cEEG monitoring
└── CT head if not done

TIME 20-60 MIN: REFRACTORY SE (if still seizing)
├── Requires ICU and intubation
├── Initiate anesthetic infusion:
│   ├── Midazolam: Load 0.2 mg/kg → 0.1-2 mg/kg/hr
│   ├── Propofol: Load 1-2 mg/kg → 20-200 mcg/kg/min
│   └── Ketamine: Load 1-2 mg/kg → 1-5 mg/kg/hr ← Consider EARLY
├── Target burst suppression on cEEG
└── Continue second-line ASM at maintenance doses

TIME >24 HOURS ON ANESTHETICS: SUPER-REFRACTORY SE
├── Add additional ASMs (topiramate, perampanel)
├── Combine anesthetics (midazolam + ketamine)
├── If NORSE/FIRES → See Appendix B
├── Consider ketogenic diet
├── Goals of care discussion
└── Epilepsy surgery evaluation if focal lesion
```

---

## APPENDIX B: NORSE/FIRES IMMUNOTHERAPY TIMELINE

```
DAY 0-3: FIRST-LINE IMMUNOTHERAPY
├── Methylprednisolone 1000 mg IV daily × 3-5 days
├── ± IVIG 0.4 g/kg/day × 5 days (can start simultaneously)
└── Continue ASMs and anesthetics as needed

DAY 3-7: ESCALATE IF NO RESPONSE
├── Add IVIG if not started
├── Consider PLEX (5-7 exchanges)
└── Do not wait for autoimmune results

DAY 7: KEY DECISION POINT
├── Initiate ketogenic diet
├── If first-line inadequate → Start second-line:
│   ├── Rituximab 375 mg/m² weekly × 4
│   └── OR Cyclophosphamide 750-1000 mg/m² monthly
└── Continue supportive care

DAY 7+: ONGOING MANAGEMENT
├── Continue second-line immunotherapy
├── Maintain ketogenic diet
├── Consider tocilizumab or anakinra if refractory
└── Goals of care discussion if no improvement
```

---

## NOTES

- SE is a medical emergency with ~20% mortality; rapid treatment is critical
- Every 5-minute delay in treatment associated with worse outcomes
- cEEG monitoring essential - up to 48% of patients have non-convulsive seizures after convulsive SE controlled
- **Levetiracetam dosing:** ESETT used 60 mg/kg; 40 mg/kg also acceptable per recent evidence. No head-to-head comparison exists.
- **Ketamine timing:** Earlier administration (in RSE, not just SRSE) correlates with better outcomes. Consider using early or in combination with midazolam.
- **NORSE/FIRES:** ~50% remain cryptogenic; start immunotherapy within 72 hours even without confirmed etiology. Ketogenic diet by Day 7.
- Propofol infusion syndrome: metabolic acidosis, rhabdomyolysis, cardiac failure - limit propofol to <48h at high doses
- Always have airway equipment ready; many second-line and all third-line agents cause respiratory depression

---

## CHANGE LOG

**v1.4 (January 19, 2026)**
- Moved Appendix C (Rapid Protocol) to bottom of document per standardized template format
- Added prominent link at top directing users to Appendix C
- All appendices now follow Section 8 and Change Log

**v1.3 (January 18, 2026)**
- Added OPD referrals for SE survivors: epilepsy outpatient follow-up, outpatient video-EEG monitoring, neuropsychology testing
- Added OPD priorities for social work, epilepsy surgery evaluation, PT/OT/Speech
- Added evidence citations: Rosati et al. CNS Drugs 2018, Fletman et al. 2024, Yan et al. J Neurol 2024
- Added supportive care items: bowel regimen, skin care protocol, eye care
- Added language option note (Spanish availability) and QR code placeholder to Quick Reference Card

**v1.2 (January 15, 2026)**
- Added Appendix C: Rapid Protocol for Non-Specialists ("3 AM Protocol")
  - Single default pathway with exact doses
  - Weight-based dosing table for levetiracetam
  - Decision branches for common scenarios (pregnancy, renal failure, cardiac disease, already on LEV)
  - Clear escalation triggers with checkboxes
  - "When to call for help" section
  - Critical safety reminders
  - Printable quick reference card

**v1.1 (January 15, 2026)**
- Added dual levetiracetam dosing options (40 mg/kg conservative vs 60 mg/kg ESETT-based)
- Added brivaracetam to second-line agents
- Added ketamine timing note emphasizing earlier use based on 2024 evidence
- Added ketamine + midazolam combination option
- Added comprehensive NORSE/FIRES immunotherapy protocol (Section 3F) per 2022 International Consensus
- Added second-line immunotherapy agents (rituximab, cyclophosphamide, tocilizumab, anakinra)
- Added "Avoid abrupt ASM discontinuation" to lifestyle recommendations
- Added ESETT citation with specific reference (Kapur J et al. NEJM 2019;381:2103-2113)
- Added Appendix B: NORSE/FIRES Immunotherapy Timeline
- Updated Evidence & References section with additional citations
- Fixed LP table OPD column for format consistency

**v1.0 (January 15, 2026)**
- Initial template creation

---

## APPENDIX C: RAPID PROTOCOL FOR NON-SPECIALISTS

**This is the "3 AM Protocol" - a single default pathway with exact doses. Follow this unless you have a specific reason to deviate. For comprehensive options and alternatives, see the full template above.**

---

### ✅ STEP 1: STABILIZATION (Time 0) - Do All Simultaneously

| Action | Dose/Details | ✓ |
|--------|--------------|---|
| Call for help | Page Neurology STAT; alert ICU | ☐ |
| Position patient | Recovery position if possible; protect head | ☐ |
| Oxygen | Non-rebreather 15 L/min | ☐ |
| IV access | Two large-bore IVs (18G or larger) | ☐ |
| Cardiac monitor | Attach telemetry | ☐ |
| Fingerstick glucose | If <70 or unknown → Dextrose 50% 50 mL IV + Thiamine 100 mg IV | ☐ |
| Labs | POC glucose, BMP, CBC, Mg, Ca, LFTs, VBG, lactate, tox screen, ASM levels | ☐ |

---

### ✅ STEP 2: FIRST-LINE - BENZODIAZEPINE (Time 0-5 min)

**PICK ONE based on IV access:**

| Situation | Drug | Exact Dose | ✓ |
|-----------|------|------------|---|
| **IV access available** | **Lorazepam IV** | **4 mg IV push over 2 min** | ☐ |
| No IV access | Midazolam IM | 10 mg IM (single injection, deltoid or thigh) | ☐ |
| No IV/IM access | Midazolam intranasal | 5 mg each nostril (10 mg total) | ☐ |

**⏱️ WAIT 5 MINUTES. Still seizing?**

| Action | Dose | ✓ |
|--------|------|---|
| Repeat benzodiazepine x1 | Lorazepam 4 mg IV (total max 8 mg) OR Midazolam 10 mg IM | ☐ |

**⏱️ WAIT 5 MORE MINUTES. Still seizing? → GO TO STEP 3 IMMEDIATELY**

🚫 **DO NOT give a third dose of benzodiazepine. Move to Step 3.**

---

### ✅ STEP 3: SECOND-LINE ASM (Time 5-20 min)

**DEFAULT CHOICE: Levetiracetam** (safest, fewest drug interactions, no cardiac monitoring needed)

| Weight | Levetiracetam Dose | Infusion Time | ✓ |
|--------|-------------------|---------------|---|
| 50 kg | 2500 mg IV | Over 10 min | ☐ |
| 60 kg | 3000 mg IV | Over 10 min | ☐ |
| 70 kg | 3500 mg IV | Over 10 min | ☐ |
| 80 kg | 4000 mg IV | Over 10 min | ☐ |
| ≥90 kg | **4500 mg IV (max)** | Over 10 min | ☐ |

**Quick calc: 50 mg/kg (or 60 mg/kg per ESETT), max 4500 mg**

---

#### 🔀 DECISION BRANCHES - Use Alternative If:

| Situation | Use Instead | Dose | Why |
|-----------|-------------|------|-----|
| **Patient already takes levetiracetam at home** | Fosphenytoin | 20 mg PE/kg IV at 150 mg PE/min (70 kg = 1400 mg PE) | Already on LEV; need different mechanism |
| **Patient already takes levetiracetam at home** | Brivaracetam | 200 mg IV over 2 min | Alternative SV2A agent with faster onset |
| **Pregnant or might be pregnant** | Levetiracetam | 50-60 mg/kg IV (max 4500 mg) | AVOID valproate (teratogenic) |
| **Known cardiac disease (heart block, bradycardia)** | Levetiracetam | 50-60 mg/kg IV (max 4500 mg) | AVOID fosphenytoin/lacosamide |
| **Severe renal impairment (CrCl <30)** | Fosphenytoin | 20 mg PE/kg IV at 150 mg PE/min | LEV requires dose reduction |
| **Severe liver disease** | Levetiracetam | 50-60 mg/kg IV (max 4500 mg) | Renally cleared |
| **Hypotensive (SBP <90)** | Levetiracetam | 50-60 mg/kg IV (max 4500 mg) | Least hemodynamic effect |

---

**⏱️ WAIT 10-15 MINUTES for infusion to complete. Still seizing?**

**Options:**
1. Try ONE more second-line agent (different class), OR
2. Proceed directly to Step 4 (RSE protocol)

**🚨 DO NOT delay beyond 20 minutes total. If still seizing at 20 min → Step 4.**

---

### ✅ STEP 4: REFRACTORY SE (Time 20+ min) - CALL ICU NOW

**🚨 STOP: This requires ICU admission, intubation capability, and continuous EEG. Call for help if not already done.**

**DEFAULT: Midazolam infusion** (most familiar to non-specialists, reversible)

| Action | Dose | ✓ |
|--------|------|---|
| **Intubate patient** | RSI with propofol or ketamine induction | ☐ |
| **Midazolam bolus** | 0.2 mg/kg IV (70 kg = 14 mg IV push) | ☐ |
| **Start midazolam infusion** | 0.1 mg/kg/hr (70 kg = 7 mg/hr) | ☐ |
| **Order continuous EEG** | STAT - mandatory | ☐ |
| **Start vasopressors if needed** | Norepinephrine if MAP <65 | ☐ |

**Titration:** Increase midazolam by 0.1 mg/kg/hr every 15 min until seizures stop on EEG. Max 2 mg/kg/hr.

---

#### 🔀 CONSIDER ADDING KETAMINE EARLY

**Emerging evidence supports adding ketamine at RSE onset (not waiting for SRSE):**

| Action | Dose | Rationale |
|--------|------|-----------|
| Ketamine bolus | 1-2 mg/kg IV (70 kg = 70-140 mg) | NMDA antagonism; less hypotension |
| Ketamine infusion | Start 1 mg/kg/hr, titrate to 5 mg/kg/hr | 2x more effective when given early |

**Ketamine can be used WITH midazolam from the start.**

---

### ✅ STEP 5: WHEN TO SUSPECT NORSE (No Clear Cause Found)

**If patient has RSE and initial workup is negative, consider NORSE:**

| Criteria | ✓ |
|----------|---|
| No prior epilepsy history | ☐ |
| No acute structural lesion on CT/MRI | ☐ |
| No toxic/metabolic cause identified | ☐ |
| No active infection explaining seizures | ☐ |

**If NORSE suspected → Start immunotherapy within 72 hours (don't wait for antibody results):**

| Day | Action | Dose |
|-----|--------|------|
| Day 1 | Methylprednisolone | 1000 mg IV daily |
| Day 1-5 | Continue steroids | 1000 mg IV daily × 5 days total |
| Day 1-5 | Consider adding IVIG | 0.4 g/kg/day × 5 days |
| Day 7 | Ketogenic diet consult | If still refractory |

---

### 📞 WHEN TO CALL FOR HELP

| Situation | Who to Call | Urgency |
|-----------|-------------|---------|
| Any SE | Neurology | STAT |
| SE not responding to first BZD | Neurology + ICU | STAT |
| SE not responding to second-line ASM | Neurocritical care | STAT |
| Need for intubation | Anesthesia/ICU | STAT |
| Suspected NORSE (no cause found) | Neuroimmunology | URGENT |
| Suspected CNS infection | Infectious Disease | URGENT |

---

### ⚠️ CRITICAL SAFETY REMINDERS

| Reminder | |
|----------|---|
| 🔴 **Airway first** - Have bag-valve-mask and intubation equipment at bedside before giving ANY medication | |
| 🔴 **Don't stack benzos** - Max 2 doses. More benzos = more respiratory depression, not more efficacy | |
| 🔴 **Time matters** - Every 5-minute delay worsens outcomes. Move fast through the protocol | |
| 🔴 **Valproate + Pregnancy = NO** - Always check pregnancy status before valproate | |
| 🔴 **Fosphenytoin + Heart block = NO** - Check ECG or avoid if unknown cardiac history | |
| 🔴 **Get EEG** - Up to 48% have non-convulsive seizures after convulsions stop. You need EEG to know. | |

---

### 🏥 DISPOSITION

| Seizure Status | Disposition |
|----------------|-------------|
| Resolved with first-line BZD only | May observe in ED; admit to telemetry if first seizure |
| Required second-line ASM | **ICU admission** |
| Required intubation/anesthetics | **ICU admission** |
| Any RSE/SRSE | **ICU admission** |

---

### 📋 QUICK REFERENCE CARD (Print This)

*Note: This protocol is available in Spanish (Español) - see your institution's translated materials or request from Pharmacy/Nursing Education.*

*For mobile access: Scan QR code [institutional link] or bookmark the online version for bedside reference.*

```
STATUS EPILEPTICUS - RAPID PROTOCOL
====================================

STEP 1: STABILIZE
• O2, 2 IVs, monitor, glucose check
• Labs: BMP, CBC, Mg, Ca, tox, ASM levels

STEP 2: BENZODIAZEPINE (Time 0-5 min)
• Lorazepam 4 mg IV push
• Wait 5 min → Repeat x1 if still seizing
• MAX 2 doses. Do NOT give 3rd dose.

STEP 3: SECOND-LINE (Time 5-20 min)
• Levetiracetam 50-60 mg/kg IV (max 4500 mg) over 10 min
  - 50 kg = 2500 mg
  - 70 kg = 3500 mg
  - 90+ kg = 4500 mg
• Alternatives: Fosphenytoin, Valproate, Lacosamide

STEP 4: RSE (Time 20+ min) - CALL ICU
• Intubate
• Midazolam 0.2 mg/kg bolus → 0.1 mg/kg/hr infusion
• ± Ketamine 1-2 mg/kg bolus → 1 mg/kg/hr infusion
• Continuous EEG - MANDATORY
• Target burst suppression

CALL NEUROLOGY FOR ALL SE
CALL ICU IF STEP 3 FAILS
====================================
```

---

<div id="comments-container"></div>
