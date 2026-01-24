---
title: Bacterial Meningitis
description: Acute bacterial meningitis - empiric antibiotics, dexamethasone, LP diagnostic criteria, and ICU management.
version: "1.0"
setting: ED, HOSP, ICU
status: draft
tags:
  - infection
  - emergency
  - meningitis
  - neurocritical-care
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Bacterial Meningitis

**VERSION:** 1.0
**CREATED:** January 24, 2026
**REVISED:** January 24, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Bacterial Meningitis

**ICD-10:** G00.9 (Bacterial meningitis, unspecified), G00.0 (Hemophilus meningitis), G00.1 (Pneumococcal meningitis), G00.2 (Streptococcal meningitis), G00.3 (Staphylococcal meningitis), G00.8 (Other bacterial meningitis), G01 (Meningitis in bacterial diseases classified elsewhere), G03.9 (Meningitis, unspecified)

**SCOPE:** Evaluation and empiric treatment of acute community-acquired bacterial meningitis in adults. Covers empiric antibiotic selection by age/risk, dexamethasone adjunctive therapy, lumbar puncture interpretation, and ICU management. Excludes neonatal meningitis, healthcare-associated/post-neurosurgical meningitis, tuberculous meningitis, and fungal meningitis.

**CLINICAL SYNONYMS:** Acute bacterial meningitis, pyogenic meningitis, purulent meningitis, community-acquired meningitis

---

**KEY CLINICAL FEATURES:**
- **Classic triad:** Fever, headache, neck stiffness (present in <50% of cases)
- **Additional features:** Altered mental status (most sensitive sign), photophobia, nausea/vomiting
- **Physical exam:** Kernig sign, Brudzinski sign (low sensitivity), petechial/purpuric rash (meningococcal)
- **Red flags:** Rapid deterioration, seizures, focal deficits, papilledema

**COMMON PATHOGENS BY AGE:**

| Age/Risk | Most Common Organisms |
|----------|----------------------|
| 16-50 years | *Streptococcus pneumoniae*, *Neisseria meningitidis* |
| >50 years | *S. pneumoniae*, *N. meningitidis*, *Listeria monocytogenes*, aerobic GNR |
| Immunocompromised | *Listeria*, GNR, *S. pneumoniae*, fungi |
| Alcoholism | *S. pneumoniae*, *Listeria* |
| Post-neurosurgery | Staphylococci, GNR, *P. aeruginosa* |
| CSF shunt | *S. epidermidis*, *S. aureus*, GNR |

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

!!! danger "⚡ TIME-CRITICAL EMERGENCY"
    **Do NOT delay antibiotics for LP or imaging.** Give empiric antibiotics within 1 hour of presentation. Every hour of delay increases mortality by 12.6%.

!!! warning "⚠️ DEXAMETHASONE TIMING"
    Give dexamethasone **BEFORE or WITH** the first dose of antibiotics. No benefit if given >4 hours after antibiotics.

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Blood cultures (2 sets) | Identify organism (positive in 50-80%) | Organism identification | STAT | STAT | — | STAT |
| CBC with differential | Leukocytosis, left shift; baseline | Elevated WBC; bandemia | STAT | STAT | — | STAT |
| CMP (BMP + LFTs) | Renal/hepatic function for antibiotic dosing | Normal or evidence of sepsis | STAT | STAT | — | STAT |
| Lactate | Sepsis severity marker | <2 mmol/L (elevated indicates sepsis) | STAT | STAT | — | STAT |
| Procalcitonin | Bacterial vs viral differentiation | Elevated (>0.5 ng/mL suggests bacterial) | STAT | STAT | — | STAT |
| PT/INR, PTT | Pre-LP coagulation status | INR <1.5, PTT normal | STAT | STAT | — | STAT |
| Platelet count | Pre-LP, DIC screening | >50,000/μL for safe LP | STAT | STAT | — | STAT |
| Blood glucose | Compare with CSF glucose | Document for CSF ratio | STAT | STAT | — | STAT |
| Urinalysis | Infection source if UTI | Document | STAT | ROUTINE | — | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CRP | Inflammatory marker, follow response | Elevated; trend with treatment | URGENT | ROUTINE | — | URGENT |
| D-dimer, fibrinogen | DIC screening (meningococcal) | Normal (elevated = DIC) | URGENT | ROUTINE | — | STAT |
| Type and screen | Anticipate transfusion if DIC | Available | URGENT | ROUTINE | — | STAT |
| Cortisol (random) | Adrenal insufficiency (Waterhouse-Friderichsen) | Normal stress response | URGENT | ROUTINE | — | URGENT |
| HIV antibody/antigen | Immunocompromise screen | Document status | — | ROUTINE | — | ROUTINE |
| BNP/troponin | Cardiac involvement, septic cardiomyopathy | Normal or elevated | URGENT | ROUTINE | — | STAT |
| ABG or VBG | Respiratory status, acid-base | Normal or compensated | STAT | STAT | — | STAT |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Serum cryptococcal antigen | If immunocompromised | Negative | — | ROUTINE | — | ROUTINE |
| Histoplasma/Blastomyces antigen | Endemic area, immunocompromised | Negative | — | EXT | — | EXT |
| Quantiferon/T-SPOT | TB risk factors | Negative | — | ROUTINE | — | ROUTINE |
| Complement levels (C3, C4, CH50) | Recurrent Neisseria infection | Normal | — | EXT | — | EXT |
| Immunoglobulin levels | Recurrent infections | Normal | — | EXT | — | EXT |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast | BEFORE LP if criteria met (see below) | Exclude mass, herniation, hydrocephalus | None in emergency | STAT | STAT | — | STAT |
| Chest X-ray | On admission | Pneumonia (source), aspiration | None | STAT | STAT | — | STAT |

**CT Before LP Criteria (any ONE = get CT first):**

- Immunocompromised state
- History of CNS disease (mass, stroke, infection)
- New onset seizure (within 1 week)
- Papilledema
- Altered level of consciousness
- Focal neurological deficit

**If NO criteria → proceed directly to LP (do not delay for CT)**

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| MRI brain with contrast | If complications suspected | Abscess, ventriculitis, infarct, subdural empyema | Hemodynamic instability | — | URGENT | — | URGENT |
| CT venogram | If venous sinus thrombosis suspected | Sinus thrombosis | Contrast allergy | — | URGENT | — | URGENT |
| EEG | If seizures or altered mental status | Seizure activity, encephalopathy | None | — | URGENT | — | URGENT |
| Echocardiogram | If endocarditis suspected | Vegetation | None | — | ROUTINE | — | ROUTINE |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT/MRI spine | If spinal epidural abscess suspected | Epidural collection | Hemodynamic instability | — | URGENT | — | URGENT |

### LUMBAR PUNCTURE

**Indication:** ALL suspected bacterial meningitis (unless contraindicated)

**Timing:** STAT - Do NOT delay antibiotics for LP. If LP will be delayed (CT, coagulopathy), give empiric antibiotics first.

**Volume Required:** 10-15 mL minimum (for all studies)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | Elevated in bacterial meningitis | 10-20 cmH2O normal; often >30 in bacterial | STAT | STAT | — | STAT |
| Cell count with differential (tubes 1 and 4) | Pleocytosis pattern | WBC >1000/μL typical; PMN predominant (>80%) | STAT | STAT | — | STAT |
| Protein | Elevated in bacterial infection | >100 mg/dL (often >200-500) | STAT | STAT | — | STAT |
| Glucose with serum glucose | Low in bacterial meningitis | <40 mg/dL or CSF:serum ratio <0.4 | STAT | STAT | — | STAT |
| Gram stain | Rapid organism identification | Positive in 60-90% untreated | STAT | STAT | — | STAT |
| Bacterial culture | Definitive organism identification | Positive in 70-85% untreated | STAT | STAT | — | STAT |
| BioFire FilmArray Meningitis/Encephalitis Panel | Rapid multiplex PCR (14 pathogens) | Organism identification within 1 hour | STAT | STAT | — | STAT |
| Latex agglutination (if available) | Rapid antigen detection | Organism-specific antigens | URGENT | URGENT | — | URGENT |
| HSV PCR | Exclude HSV encephalitis | Negative | STAT | STAT | — | STAT |
| Procalcitonin (CSF) | Bacterial vs aseptic | Elevated in bacterial | — | ROUTINE | — | ROUTINE |

**CSF Findings Comparison:**

| Parameter | Bacterial | Viral | TB/Fungal |
|-----------|-----------|-------|-----------|
| Opening pressure | Elevated (>30 cmH2O) | Normal/mild ↑ | Elevated |
| WBC count | >1000 (often >1000-10,000) | 10-500 | 100-500 |
| Cell type | PMN predominant (>80%) | Lymphocyte predominant | Lymphocyte predominant |
| Protein | >100 mg/dL (often >200) | 50-100 mg/dL | >100 mg/dL |
| Glucose | <40 mg/dL or <0.4 ratio | Normal | Low |
| Gram stain | Positive 60-90% | Negative | Usually negative |

**Special Handling:** Gram stain and culture STAT. BioFire Panel STAT. Cell count within 1 hour.

**Contraindications:** Signs of herniation, papilledema with mass effect, severe coagulopathy (INR >1.5, platelets <50K), skin infection at LP site. Get CT first if any criteria above.

**NOTE:** A negative Gram stain does NOT rule out bacterial meningitis. Continue empiric antibiotics until cultures finalize.

---

## 3. TREATMENT

**CRITICAL:** Antibiotics within 1 hour. Dexamethasone before or with first antibiotic dose. Do NOT wait for LP or CT if they will delay treatment.

### 3A. Empiric Antibiotic Therapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Ceftriaxone | IV | Empiric coverage (all ages) | 2 g q12h :: IV :: q12h :: 2 g IV q12h; meningeal dosing required | Severe cephalosporin allergy | Renal function | STAT | STAT | — | STAT |
| Vancomycin | IV | DRSP coverage (all patients) | 15-20 mg/kg q8-12h; 25-30 mg/kg load :: IV :: q8-12h :: Load 25-30 mg/kg IV, then 15-20 mg/kg q8-12h (target trough 15-20 mcg/mL); adjust for renal function | Renal impairment (adjust dose) | Trough levels, renal function, ototoxicity | STAT | STAT | — | STAT |
| Ampicillin | IV | Listeria coverage (age ≥50-60, immunocompromised, alcoholism) | 2 g q4h :: IV :: q4h :: 2 g IV q4h; required for Listeria coverage in at-risk patients; **NOTE: guidelines vary (≥50 vs >60) - use lower threshold if any additional risk factors** | Penicillin allergy (use TMP-SMX) | Renal function | STAT | STAT | — | STAT |
| Dexamethasone | IV | Adjunctive therapy (BEFORE/WITH antibiotics) | 0.15 mg/kg q6h x 4 days :: IV :: q6h x 4 days :: 0.15 mg/kg IV (typically 10 mg) q6h x 4 days; give 15-20 min BEFORE or WITH first antibiotic dose; see immunocompromised guidance below | GI bleed (relative), see immunocompromised guidance | Glucose, GI bleeding | STAT | STAT | — | STAT |

**Age-Based Empiric Regimen:**

| Age/Risk | Empiric Regimen |
|----------|-----------------|
| **16-50 years (healthy)** | Ceftriaxone + Vancomycin |
| **≥50 years** (some guidelines use >60) | Ceftriaxone + Vancomycin + Ampicillin |
| **Immunocompromised** | Ceftriaxone + Vancomycin + Ampicillin |
| **Alcoholism** | Ceftriaxone + Vancomycin + Ampicillin |
| **Severe penicillin allergy** | Meropenem + Vancomycin (or chloramphenicol + TMP-SMX) |

**Note:** Age threshold for Listeria coverage varies between guidelines (≥50 vs >60). Use lower threshold (≥50) when additional risk factors present (diabetes, malnutrition, chronic disease).

### 3B. Organism-Directed Therapy (After Culture/Sensitivity)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Penicillin G | IV | Penicillin-sensitive pneumococcus, meningococcus | 4 million units q4h :: IV :: q4h :: 4 million units IV q4h; can de-escalate if susceptible | Penicillin allergy | Renal function | — | STAT | — | STAT |
| Ceftriaxone (continued) | IV | Pneumococcus (intermediate), meningococcus, H. flu | 2 g q12h :: IV :: q12h :: Continue 2 g IV q12h if organism susceptible | Cephalosporin allergy | Renal function | — | STAT | — | STAT |
| Ampicillin (continued) | IV | Listeria monocytogenes | 2 g q4h :: IV :: q4h :: 2 g IV q4h x 21 days for Listeria | Penicillin allergy | Renal function | — | STAT | — | STAT |
| TMP-SMX | IV | Listeria (penicillin-allergic) | 5 mg/kg TMP q6h :: IV :: q6h :: 5 mg/kg (TMP component) IV q6h; alternative for Listeria | Sulfa allergy, severe renal impairment | Renal function, K+, rash | — | STAT | — | STAT |
| Meropenem | IV | Resistant GNR, penicillin allergy | 2 g q8h :: IV :: q8h :: 2 g IV q8h; meningeal dosing | Carbapenem allergy | Renal function, seizures | — | STAT | — | STAT |

### 3C. Treatment Duration by Organism

| Organism | Duration |
|----------|----------|
| *Neisseria meningitidis* | 7 days |
| *Haemophilus influenzae* | 7 days |
| *Streptococcus pneumoniae* | 10-14 days |
| *Group B Streptococcus* | 14-21 days |
| *Listeria monocytogenes* | ≥21 days |
| *Gram-negative bacilli* | 21 days |
| Unknown organism | 10-14 days (minimum) |

### 3D. Dexamethasone Guidance

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Dexamethasone (continue) | IV | Proven pneumococcal meningitis | 0.15 mg/kg q6h x 4 days :: IV :: q6h x 4 days :: Continue full 4-day course if S. pneumoniae confirmed | See below | Glucose, GI bleed | — | STAT | — | STAT |
| Dexamethasone (discontinue) | — | Non-pneumococcal meningitis | N/A :: — :: :: DISCONTINUE dexamethasone if organism other than S. pneumoniae (benefit unproven) | — | — | — | STAT | — | STAT |

**Dexamethasone Notes:**
- **Greatest benefit:** Pneumococcal meningitis (reduces mortality and hearing loss)
- **Timing critical:** Must be given BEFORE or WITH first antibiotic dose; no benefit if started >4 hours after antibiotics
- **Continue if:** S. pneumoniae confirmed
- **Discontinue if:** Other organism confirmed, prior antibiotics given
- **Caution:** May reduce CSF penetration of vancomycin (controversial; continue vancomycin anyway)

**Dexamethasone in Immunocompromised Patients:**
- **HIV:** Limited evidence of benefit in HIV-positive patients; meta-analyses show uncertain benefit. Use clinical judgment.
- **CRITICAL - Rule out cryptococcal/TB first:** Dexamethasone is **contraindicated** in HIV-associated cryptococcal meningitis (increased mortality shown in trials). TB meningitis benefit in HIV+ patients is uncertain.
- **Practical approach:** If HIV status unknown, give dexamethasone empirically but send cryptococcal antigen and evaluate for TB; discontinue if cryptococcal or TB confirmed.
- **Other immunocompromise:** Benefit unproven in transplant, chemotherapy, biologics; weigh risks vs benefits.

### 3E. Supportive Care

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Normal saline | IV | Fluid resuscitation, maintenance | 30 mL/kg bolus; 125 mL/hr maintenance :: IV :: bolus then maintenance :: 30 mL/kg bolus for sepsis; avoid over-hydration (cerebral edema risk) | Cerebral edema (restrict fluids) | I/O, Na+, mental status | STAT | STAT | — | STAT |
| Norepinephrine | IV | Septic shock | 0.1-0.5 mcg/kg/min; 2-30 mcg/min :: IV :: infusion :: Start 2-5 mcg/min; titrate to MAP ≥65 | — | Continuous BP, lactate | — | — | — | STAT |
| Phenytoin | IV | Seizure prophylaxis (if seizures occur) | 20 mg/kg load; 100 mg q8h :: IV :: load then q8h :: 20 mg/kg IV load (max rate 50 mg/min), then 100 mg IV q8h; NOT recommended routinely for prophylaxis | Bradycardia, heart block | Cardiac monitoring during load, levels | STAT | STAT | — | STAT |
| Levetiracetam | IV | Seizure treatment/prophylaxis | 1000 mg BID; 1500 mg BID :: IV :: BID :: 1000-1500 mg IV BID; preferred for seizure prophylaxis if indicated | Severe renal impairment (adjust) | Renal function | STAT | STAT | — | STAT |
| Acetaminophen | IV/PO | Fever, headache | 650 mg q6h; 1000 mg q6h :: IV/PO :: q6h :: 650-1000 mg q6h; max 4 g/day | Severe hepatic impairment | Temperature | STAT | STAT | — | STAT |
| Mannitol | IV | Elevated ICP | 0.5-1 g/kg bolus :: IV :: PRN :: 0.5-1 g/kg IV bolus over 15-20 min; may repeat q6h PRN; target serum osm <320 | Renal failure, hypotension | Serum osm, Na+, renal function | — | STAT | — | STAT |
| Hypertonic saline (3%) | IV | Elevated ICP | 250 mL bolus :: IV :: PRN :: 250 mL (or 30 mL of 23.4%) bolus for acute herniation; target Na 145-155 | — | Na+, serum osm | — | STAT | — | STAT |
| Enoxaparin | SC | DVT prophylaxis (after stabilization) | 40 mg daily :: SC :: daily :: 40 mg SC daily; start after 48-72h if no hemorrhagic complications | Active bleeding, recent LP, coagulopathy | Platelet count | — | ROUTINE | — | ROUTINE |
| Famotidine | IV | Stress ulcer prophylaxis | 20 mg BID :: IV :: BID :: 20 mg IV BID if on steroids or intubated | None significant | GI bleeding | — | ROUTINE | — | ROUTINE |

### 3F. Chemoprophylaxis for Close Contacts

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Rifampin | PO | Meningococcal prophylaxis | 600 mg BID x 2 days :: PO :: BID x 2 days :: 600 mg PO q12h x 4 doses (2 days); for household/close contacts | Pregnancy, liver disease | Orange secretions warning | — | ROUTINE | — | — |
| Ciprofloxacin | PO | Meningococcal prophylaxis | 500 mg single dose :: PO :: once :: 500 mg PO x 1 dose; alternative to rifampin | Pregnancy, children (relative) | Tendon warning | — | ROUTINE | — | — |
| Ceftriaxone | IM | Meningococcal prophylaxis | 250 mg single dose :: IM :: once :: 250 mg IM x 1 dose; safe in pregnancy | Cephalosporin allergy | None | — | ROUTINE | — | — |
| Rifampin (H. flu) | PO | H. influenzae prophylaxis | 20 mg/kg daily x 4 days :: PO :: daily x 4 days :: 20 mg/kg (max 600 mg) PO daily x 4 days; for household contacts if unvaccinated child <4 yo present | Pregnancy, liver disease | Orange secretions warning | — | ROUTINE | — | — |

**Contact Prophylaxis Indications:**
- **Meningococcal:** Household contacts, daycare contacts, anyone exposed to respiratory secretions (kissing, mouth-to-mouth, intubation without mask)
- **H. influenzae type b:** Household contacts if unvaccinated child <4 years present
- **Pneumococcal:** No prophylaxis indicated

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | Indication | ED | HOSP | OPD | ICU |
|----------------|------------|:--:|:----:|:---:|:---:|
| Infectious disease consult | All bacterial meningitis | URGENT | STAT | — | STAT |
| Neurology consult | Seizures, focal deficits, complications | URGENT | URGENT | — | STAT |
| Critical care consult | Septic shock, need for pressors, intubation | STAT | STAT | — | STAT |
| Neurosurgery consult | Hydrocephalus, abscess, elevated ICP | — | URGENT | — | STAT |
| ENT consult | Hearing evaluation (post-meningitis) | — | ROUTINE | — | ROUTINE |
| Audiology | Hearing test before discharge | — | ROUTINE | — | ROUTINE |
| Infection control | Isolation, contact tracing (meningococcal) | STAT | STAT | — | STAT |
| Public health notification | Meningococcal disease (reportable) | STAT | STAT | — | STAT |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return immediately for worsening headache, fever, confusion, or seizures | STAT | — | STAT |
| Complete full antibiotic course even if feeling better | — | STAT | STAT |
| Hearing test recommended after recovery | — | ROUTINE | ROUTINE |
| Close contacts should receive prophylaxis if meningococcal | STAT | STAT | — |
| Report persistent headaches, hearing changes, or cognitive difficulties | — | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Respiratory isolation (meningococcal) until 24h of effective antibiotics | STAT | STAT | — |
| Meningococcal vaccination for close contacts and patient (after recovery) | — | ROUTINE | ROUTINE |
| Pneumococcal vaccination if not up to date | — | ROUTINE | ROUTINE |
| Hand hygiene education | — | ROUTINE | ROUTINE |
| Avoid sharing utensils, drinks during active infection | STAT | STAT | — |

---

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Viral meningitis | Milder course, lymphocytic CSF, normal glucose | CSF profile, viral PCR |
| HSV encephalitis | Altered mental status, temporal lobe findings, seizures | MRI brain, CSF HSV PCR |
| Tuberculous meningitis | Subacute course, basilar enhancement, low glucose | CSF AFB, adenosine deaminase, PCR |
| Fungal meningitis | Immunocompromised, indolent course | CSF fungal culture, cryptococcal antigen |
| Subarachnoid hemorrhage | Thunderclap headache, xanthochromia | CT head, LP (xanthochromia, RBCs) |
| Brain abscess | Focal deficits, ring-enhancing lesion | MRI brain with contrast |
| Subdural empyema | Post-sinusitis/otitis, focal deficits | MRI brain with contrast |
| Autoimmune encephalitis | Subacute, psychiatric symptoms, movement disorder | Autoimmune panel (serum/CSF) |
| Carcinomatous meningitis | Cancer history, cranial neuropathies | CSF cytology, MRI |
| Drug-induced meningitis | NSAIDs, IVIG, TMP-SMX exposure | Temporal relationship, improvement off drug |
| Endocarditis with CNS embolization | Heart murmur, embolic phenomena | Echocardiogram, blood cultures |
| Septic dural sinus thrombosis | Headache, papilledema, focal signs | CT/MR venography |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Neurological exam (GCS) | q1-2h initially, then q4h | GCS stable or improving | Head CT, consider ICP monitoring | STAT | STAT | — | STAT |
| Temperature | q4h | Afebrile by 48-72h | Reassess antibiotic coverage | STAT | STAT | — | STAT |
| Blood pressure | q1-4h | MAP ≥65 | Vasopressors if septic shock | STAT | STAT | — | STAT |
| Heart rate | Continuous | 60-100 bpm | Evaluate for sepsis, arrhythmia | STAT | STAT | — | STAT |
| Oxygen saturation | Continuous | >94% | Supplement O2, consider intubation | STAT | STAT | — | STAT |
| Urine output | q4h | >0.5 mL/kg/hr | Fluid resuscitation | — | STAT | — | STAT |
| Serum sodium | q6-12h | 135-145 mEq/L | Evaluate for SIADH, cerebral salt wasting | STAT | STAT | — | STAT |
| Lactate | q6-12h until normal | <2 mmol/L | Optimize resuscitation | STAT | STAT | — | STAT |
| Vancomycin trough | Before 4th dose | 15-20 mcg/mL | Dose adjustment | — | STAT | — | STAT |
| Renal function | Daily | Cr stable | Adjust antibiotic doses | STAT | STAT | — | STAT |
| Glucose | q6h if on steroids | <180 mg/dL | Insulin | — | ROUTINE | — | STAT |
| Hearing assessment | Before discharge | Normal | Audiology referral | — | ROUTINE | — | ROUTINE |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **ICU admission** | GCS <12; hemodynamic instability (septic shock); respiratory failure; seizures; signs of elevated ICP; DIC; rapidly worsening |
| **Step-down/telemetry** | Stable but requiring close monitoring; improving mental status; weaning vasopressors |
| **General floor** | Stable; GCS 15; hemodynamically stable; no seizures; improving on antibiotics |
| **Discharge home** | NOT recommended for acute bacterial meningitis; requires IV antibiotics |
| **Transfer to higher level** | Need for neurosurgical intervention; refractory elevated ICP; ECMO candidacy |

**Typical Hospital Course:** 10-21 days depending on organism

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Dexamethasone before antibiotics improves outcomes in pneumococcal meningitis | Class I, Level A | [de Gans et al. NEJM 2002](https://pubmed.ncbi.nlm.nih.gov/12432045/) |
| Antibiotics within 1 hour reduce mortality | Class II, Level B | [Proulx et al. QJM 2005](https://pubmed.ncbi.nlm.nih.gov/15728404/) |
| CT before LP only if criteria met | Class II, Level B | [Hasbun et al. NEJM 2001](https://pubmed.ncbi.nlm.nih.gov/11742046/) |
| Vancomycin + ceftriaxone empiric for DRSP | Class II, Level B | [Tunkel et al. IDSA Guidelines Clin Infect Dis 2004](https://pubmed.ncbi.nlm.nih.gov/15494903/) |
| Ampicillin for Listeria coverage in at-risk | Class II, Level B | [IDSA Guidelines 2004](https://pubmed.ncbi.nlm.nih.gov/15494903/) |
| BioFire Panel for rapid diagnosis | Class II, Level B | [Leber et al. J Clin Microbiol 2016](https://pubmed.ncbi.nlm.nih.gov/27335149/) |
| Rifampin or ciprofloxacin prophylaxis for meningococcal contacts | Class I, Level A | [CDC MMWR Recommendations](https://pubmed.ncbi.nlm.nih.gov/23486021/) |
| Antibiotic duration by organism | Class II, Level B | [Tunkel et al. IDSA Guidelines](https://pubmed.ncbi.nlm.nih.gov/15494903/) |
| Delay in antibiotics increases mortality | Class II, Level B | [Auburtin et al. Crit Care Med 2006](https://pubmed.ncbi.nlm.nih.gov/16940475/) |

---

## CHANGE LOG

**v1.0 (January 24, 2026)**
- Initial template creation
- Age-based empiric antibiotic selection
- Dexamethasone timing guidance
- CSF interpretation table
- Contact prophylaxis protocols
- Treatment duration by organism

---

## APPENDIX A: CT Before LP Decision Algorithm

```
Suspected Bacterial Meningitis
         │
         ▼
Any of the following?
• Immunocompromised
• History of CNS disease
• New onset seizure (<1 week)
• Papilledema
• Altered consciousness (GCS <14)
• Focal neurological deficit
         │
    ┌────┴────┐
    │         │
   YES        NO
    │         │
    ▼         ▼
CT Head    Proceed directly
  STAT     to LP
    │         │
    ▼         │
No mass/    ─┘
herniation?
    │
   YES
    │
    ▼
Proceed to LP

**CRITICAL: Do NOT delay antibiotics for CT or LP**
Give empiric antibiotics + dexamethasone immediately if meningitis suspected
```

---

## APPENDIX B: Empiric Antibiotic Quick Reference

| Patient Type | Regimen | Key Points |
|--------------|---------|------------|
| **16-50 yo, healthy** | Ceftriaxone 2g q12h + Vancomycin | No Listeria coverage needed |
| **>50 yo** | Ceftriaxone 2g q12h + Vancomycin + Ampicillin 2g q4h | Add Listeria coverage |
| **Immunocompromised** | Ceftriaxone 2g q12h + Vancomycin + Ampicillin 2g q4h | Broader coverage |
| **Alcoholism** | Ceftriaxone 2g q12h + Vancomycin + Ampicillin 2g q4h | High Listeria risk |
| **Severe PCN allergy** | Meropenem 2g q8h + Vancomycin | Or chloramphenicol + TMP-SMX |
| **Post-neurosurgery** | Vancomycin + Cefepime 2g q8h (or Meropenem) | Cover Staph, Pseudomonas |

**ALL patients also receive:**
- Dexamethasone 0.15 mg/kg (or 10 mg) IV q6h x 4 days
- Give dexamethasone 15-20 min BEFORE or WITH first antibiotic dose

---

## APPENDIX C: CSF Parameters Quick Reference

| Parameter | Normal | Bacterial | Viral | TB/Fungal |
|-----------|--------|-----------|-------|-----------|
| **Opening pressure** | 10-20 cmH2O | >30 cmH2O | Normal/↑ | ↑↑ |
| **WBC** | <5/μL | 1,000-10,000 | 10-500 | 100-500 |
| **Differential** | — | >80% PMNs | Lymphs | Lymphs |
| **Protein** | 15-45 mg/dL | >200 mg/dL | 50-100 | >100 |
| **Glucose** | 45-80 mg/dL | <40 | Normal | <40 |
| **CSF:Serum glucose** | >0.6 | <0.4 | >0.6 | <0.4 |
| **Gram stain** | Negative | + in 60-90% | Negative | Usually - |
| **Lactate** | <3.5 mmol/L | >4 mmol/L | <3.5 | Variable |
