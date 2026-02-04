---
title: "HSV Encephalitis"
description: "Clinical decision support for herpes simplex virus encephalitis diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - epilepsy
  - cerebrovascular
  - headache
  - neurodegenerative
  - movement-disorders
---

# HSV Encephalitis

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Herpes Simplex Virus Encephalitis

**ICD-10:** B00.4 (Herpesviral encephalitis), G05.1 (Encephalitis in diseases classified elsewhere)

**CPT CODES:** 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 87040 (Blood cultures x2), 82947 (Blood glucose (paired with CSF)), 84145 (Procalcitonin), 86140 (CRP), 83930 (Serum osmolality), 86900 (Type and screen), 84443 (TSH), 82140 (Ammonia), 84484 (Troponin), 80307 (Toxicology screen (urine)), 80320 (Blood alcohol level), 86255 (Autoimmune encephalitis panel (serum) — NMDAR, LGI1, CASPR2), 70450 (CT head without contrast), 70553 (MRI brain with and without contrast), 95816 (EEG (routine or continuous)), 93000 (ECG (12-lead)), 95700 (Continuous EEG (cEEG) monitoring), 71046 (Chest X-ray), 78816 (PET-CT brain), 89051 (Cell count with differential (tubes 1 and 4)), 84157 (Protein), 82945 (Glucose with paired serum), 87529 (HSV-1/2 PCR (CSF)), 87483 (BioFire FilmArray ME Panel), 83916 (Oligoclonal bands, IgG index), 88104 (Cytology), 87116 (AFB smear and culture), 86592 (VDRL (CSF)), 96365 (Acyclovir IV)

**SYNONYMS:** HSV encephalitis, HSE, herpes encephalitis, herpes simplex encephalitis, viral encephalitis, limbic encephalitis, temporal lobe encephalitis, brain infection, encephalitis

**SCOPE:** Acute HSV-1 encephalitis in adults — the most common cause of sporadic fatal encephalitis. Covers emergent empiric acyclovir, LP with HSV PCR, MRI findings, seizure management, and monitoring for complications (cerebral edema, SIADH, refractory status epilepticus). Excludes neonatal HSV, HSV-2 meningitis (Mollaret), CMV/EBV/VZV encephalitis, and autoimmune encephalitis (though post-HSV autoimmune encephalitis is addressed).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | - | STAT | Baseline; infection markers; lymphopenia may be present | Normal or mild leukocytosis |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | - | STAT | Renal function for acyclovir dosing (nephrotoxic); electrolytes (SIADH); hepatic function | Normal; watch Na and Cr |
| Blood cultures x2 (CPT 87040) | STAT | STAT | - | STAT | Exclude bacterial meningitis; concurrent bacteremia | No growth |
| Coagulation panel (PT/INR, aPTT) (CPT 85610+85730) | STAT | STAT | - | STAT | Before LP; coagulopathy workup if DIC suspected | Normal |
| Blood glucose (paired with CSF) (CPT 82947) | STAT | STAT | - | STAT | CSF:serum glucose ratio interpretation | Document paired with LP |
| Procalcitonin (CPT 84145) | URGENT | ROUTINE | - | URGENT | Low procalcitonin argues against bacterial meningitis | Low (<0.5 ng/mL favors viral) |
| CRP (CPT 86140) | URGENT | ROUTINE | - | URGENT | Inflammatory marker; lower in viral than bacterial | Mild elevation |
| Serum sodium | STAT | STAT | - | STAT | SIADH is common complication of HSV encephalitis | 135-145 mEq/L; watch for hyponatremia |
| Serum osmolality (CPT 83930) | URGENT | ROUTINE | - | URGENT | SIADH evaluation | 280-295 mOsm/kg |
| Type and screen (CPT 86900) | STAT | ROUTINE | - | STAT | Potential surgical intervention for mass effect | On file |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| HSV-1/2 IgG and IgM (serum) | - | ROUTINE | ROUTINE | - | Seroconversion supports diagnosis; IgG positive in most adults (not diagnostic alone); IgM suggests acute infection | Rising titers on paired sera (acute + convalescent at 2-4 weeks) |
| HIV 1/2 antigen/antibody | - | ROUTINE | ROUTINE | - | Immunocompromise affects prognosis and treatment duration | Document result |
| Urine osmolality and sodium | - | ROUTINE | - | ROUTINE | SIADH confirmation (urine osm >100, urine Na >40 with low serum Na) | Evaluate if hyponatremic |
| TSH (CPT 84443) | - | ROUTINE | - | - | Thyroid dysfunction in encephalopathy differential | Normal |
| Ammonia (CPT 82140) | URGENT | ROUTINE | - | URGENT | Hepatic encephalopathy in differential | Normal |
| Troponin (CPT 84484) | URGENT | ROUTINE | - | URGENT | Stress cardiomyopathy; myocarditis in systemic viral illness | Normal |
| Toxicology screen (urine) (CPT 80307) | URGENT | ROUTINE | - | URGENT | Altered mental status differential | Negative |
| Blood alcohol level (CPT 80320) | URGENT | - | - | URGENT | Altered mental status differential | Negative |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Autoimmune encephalitis panel (serum) — NMDAR, LGI1, CASPR2 (CPT 86255) | - | ROUTINE | ROUTINE | ROUTINE | Post-HSV autoimmune encephalitis occurs in 20-27% (especially anti-NMDAR); also primary differential | Negative initially; recheck at 2-4 weeks if relapse |
| Paraneoplastic panel (serum) (CPT 86255) | - | EXT | EXT | - | If atypical features or oncologic history | Negative |
| VZV IgG/IgM (serum) | - | ROUTINE | ROUTINE | - | VZV encephalitis in differential (especially immunocompromised) | Negative |
| Arboviral serologies (West Nile, EEE, St. Louis) | - | EXT | EXT | - | Geographic/seasonal risk; summer-fall encephalitis | Negative |
| Rabies antibodies | - | EXT | EXT | - | Animal exposure history with rapidly progressive encephalitis | Negative |
| Bartonella serology | - | EXT | EXT | - | Cat exposure; neuroretinitis | Negative |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediate — before LP to exclude mass effect; CT may be NORMAL early in HSV encephalitis | Temporal lobe hypodensity, edema, hemorrhage (late); may be normal in first 48-72h | Pregnancy (relative) |
| MRI brain with and without contrast (CPT 70553) | STAT | STAT | - | STAT | Within 24h; STAT if available. MOST SENSITIVE imaging study — abnormal in >90% within 48h | T2/FLAIR hyperintensity in medial temporal lobes (unilateral or bilateral), insular cortex, inferior frontal gyri, cingulate gyrus. DWI restriction in acute phase. Hemorrhagic transformation. Leptomeningeal enhancement | Pacemaker, metallic implants |
| EEG (routine or continuous) (CPT 95816) | URGENT | URGENT | - | STAT | Within 24h; continuous EEG if altered consciousness | Periodic lateralizing epileptiform discharges (PLEDs/LPDs) from temporal region — highly suggestive of HSV encephalitis; focal slowing; electrographic seizures; diffuse slowing | None significant |
| ECG (12-lead) (CPT 93000) | URGENT | ROUTINE | - | URGENT | On admission | Baseline; myocarditis screen; QTc for medication interactions | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with MRA/MRV | - | ROUTINE | - | ROUTINE | If vascular complication suspected | Venous sinus thrombosis; vasculopathy; large vessel occlusion | Same as MRI |
| Repeat MRI brain | - | ROUTINE | - | ROUTINE | At 48-72h if initial MRI negative but suspicion high; at 7-14 days to assess extent of damage | Evolving temporal changes; hemorrhagic transformation; extent of necrosis | Same as MRI |
| Continuous EEG (cEEG) monitoring (CPT 95700) | - | URGENT | - | STAT | 24-72h minimum if altered consciousness, seizures, or post-ictal state | Non-convulsive seizures, non-convulsive status epilepticus (NCSE), PLEDs | None |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | On admission | Aspiration; baseline for ventilator management | None |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Brain biopsy | - | - | - | EXT | Only if: PCR negative, MRI atypical, no response to acyclovir, alternative diagnosis likely | Cowdry type A inclusions; viral culture; PCR on tissue | Neurosurgical risk; coagulopathy |
| PET-CT brain (CPT 78816) | - | - | EXT | - | If autoimmune encephalitis relapse suspected post-HSV | Mesial temporal hypermetabolism (seizure focus) or hypometabolism | Pregnancy |
| ICP monitoring (EVD) | - | - | - | URGENT | If clinical signs of elevated ICP; declining GCS despite treatment | ICP <22 mmHg; CPP >60 | Coagulopathy |

### LUMBAR PUNCTURE

**Indication:** Diagnostic — ALL patients with suspected encephalitis. Do NOT delay acyclovir for LP.

**Timing:** STAT. Start acyclovir BEFORE LP if any delay anticipated.

**Volume Required:** 15-20 mL (extra for PCR, cytology, autoimmune panel)

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | STAT | ROUTINE | - | Elevated in some cases; monitor for ICP issues | Normal or mildly elevated (usually <300 mm H2O) |
| Cell count with differential (tubes 1 and 4) (CPT 89051) | STAT | ROUTINE | - | Lymphocytic pleocytosis typical; RBCs may be present (hemorrhagic encephalitis); tube comparison for traumatic tap | WBC 10-500 cells/µL (lymphocyte predominant); RBC may be elevated (hemorrhagic necrosis) |
| Protein (CPT 84157) | STAT | ROUTINE | - | Mildly to moderately elevated | Elevated (50-200 mg/dL typical; can be higher) |
| Glucose with paired serum (CPT 82945) | STAT | ROUTINE | - | Usually NORMAL in HSV (distinguishes from bacterial/TB/fungal) | Normal (>60% serum glucose ratio); low glucose argues against HSV |
| HSV-1/2 PCR (CSF) (CPT 87529) | STAT | ROUTINE | - | GOLD STANDARD diagnostic test; sensitivity 96-98%, specificity ~99%. May be NEGATIVE in first 72h — if clinical suspicion high and initial PCR negative, REPEAT at 3-7 days | Positive (HSV-1 in >90% adult cases; HSV-2 in neonatal/meningitis) |
| Gram stain and bacterial culture (CPT 87205+87070) | STAT | ROUTINE | - | Exclude bacterial meningitis | No organisms |
| BioFire FilmArray ME Panel (CPT 87483) | STAT | ROUTINE | - | Rapid multiplex PCR — includes HSV-1/2, VZV, enterovirus, CMV, HHV-6, and bacterial pathogens; result in ~1 hour | HSV-1 detected (or other pathogen identified) |
| VZV PCR (CSF) | URGENT | ROUTINE | - | VZV encephalitis in differential; especially immunocompromised and elderly | Negative (positive → VZV encephalitis — treat with IV acyclovir) |
| CMV PCR (CSF) | - | ROUTINE | - | If immunocompromised (HIV/transplant) | Negative |
| EBV PCR (CSF) | - | ROUTINE | - | If immunocompromised; CNS lymphoma differential | Negative |
| HHV-6 PCR (CSF) | - | ROUTINE | - | Post-transplant encephalitis; temporal lobe involvement similar to HSV | Negative |
| Enterovirus PCR | - | ROUTINE | - | Viral meningitis differential | Negative |
| Autoimmune encephalitis panel (CSF) — NMDAR, LGI1, CASPR2, GABA-B | - | ROUTINE | ROUTINE | Primary differential diagnosis; also detect post-HSV autoimmune encephalitis | Negative initially; recheck if relapse |
| Oligoclonal bands, IgG index (CPT 83916) | - | ROUTINE | ROUTINE | Intrathecal antibody production; MS differential | May be positive (non-specific) |
| Cytology (CPT 88104) | - | ROUTINE | - | Exclude leptomeningeal malignancy | Negative |
| AFB smear and culture (CPT 87116) | - | ROUTINE | - | TB meningitis if subacute or basilar | Negative |
| VDRL (CSF) (CPT 86592) | - | ROUTINE | - | Neurosyphilis screen | Negative |

**Special Handling:** HSV PCR sample can be refrigerated; do NOT freeze. Process CSF rapidly for cell count. Save extra CSF (frozen at -80°C) for future studies if needed.

**Repeat LP indications:** If initial HSV PCR negative but clinical suspicion high → repeat at 3-7 days. Also repeat if clinical deterioration at 2-4 weeks (relapse → send autoimmune encephalitis panel).

---

## 3. TREATMENT

### ⚠️ CRITICAL: START ACYCLOVIR IMMEDIATELY

**Do NOT wait for LP, imaging, or PCR results. Every hour of delay increases mortality and morbidity. Start acyclovir on clinical suspicion alone.**

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Acyclovir IV (CPT 96365) | IV | - | 10 mg/kg :: IV :: q8h :: 10 mg/kg IV q8h (infuse over 1h). Base on IDEAL body weight (IBW). Duration: minimum 14-21 days. Dose adjust for renal impairment: CrCl 25-50: 10 mg/kg q12h; CrCl 10-25: 10 mg/kg q24h; HD: 10 mg/kg after each dialysis session | True acyclovir allergy (extremely rare). Renal impairment — dose adjust, do NOT withhold | Renal function (BUN, Cr) daily; ensure adequate hydration (1-1.5 mL/kg/h IV fluids); urine output; acyclovir crystal nephropathy (maintain urine output); CBC (rare neutropenia); LFTs | STAT | STAT | - | STAT |
| IV normal saline (aggressive hydration) | IV | - | 1-1.5 mL/kg :: - :: continuous :: 1-1.5 mL/kg/h continuous to prevent acyclovir nephrotoxicity; bolus 500-1000 mL if dehydrated | Volume overload, CHF | I/O; Cr daily; urine output >0.5 mL/kg/h | STAT | STAT | - | STAT |
| Empiric antibiotics (vancomycin + ceftriaxone) | - | - | N/A :: - :: per protocol :: Standard meningitis dosing. Continue until bacterial meningitis excluded by CSF results (Gram stain negative, BioFire negative, cultures negative at 48-72h). See Bacterial Meningitis template for dosing | See Bacterial Meningitis template | Standard | STAT | STAT | - | STAT |
| Dexamethasone | IV | - | 0.15 mg/kg :: IV :: q6h :: 0.15 mg/kg IV q6h x 4 days — give empirically with antibiotics until bacterial meningitis excluded. Discontinue when bacterial excluded. Role in HSV encephalitis itself is CONTROVERSIAL — some evidence for reducing edema but no clear mortality benefit; not standard of care for isolated HSV | Uncontrolled infection (relative) | Glucose; GI prophylaxis | STAT | STAT | - | STAT |
| Levetiracetam (if seizures) | IV | - | 1000-1500 mg :: IV :: BID :: 1000-1500 mg IV load; then 500-1000 mg IV/PO BID; max 3000 mg/day. Seizures occur in 40-60% of HSV encephalitis | Severe renal impairment (dose adjust) | Renal function; behavioral side effects | STAT | STAT | - | STAT |
| Lorazepam (seizure rescue) | IV | - | 0.1 mg/kg :: IV :: - :: 0.1 mg/kg IV (max 4 mg); repeat x1 in 5 min if needed | Respiratory depression | RR, SpO2; airway equipment ready | STAT | STAT | - | STAT |
| Supplemental oxygen | - | - | 94% :: - :: - :: If SpO2 <94% or intubated | N/A | SpO2 target ≥94% | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Acetaminophen | IV | Fever (temperature goal <38°C); headache | 650-1000 mg :: IV :: q6h :: 650-1000 mg PO/IV q6h; max 4g/day | Severe hepatic disease | Temperature; LFTs | STAT | STAT | ROUTINE | STAT |
| Mannitol 20% | IV | Cerebral edema / elevated ICP | 1-1.5 g/kg :: IV :: once :: 1-1.5 g/kg IV bolus; then 0.25-0.5 g/kg q4-6h | Anuria | Serum osm <320; renal function; I/O | STAT | - | - | STAT |
| Hypertonic saline 23.4% | IV | Acute herniation | 30 mL :: IV :: - :: 30 mL IV via central line over 10-20 min | No central access | Na (target 145-155); osmolality | - | - | - | STAT |
| Hypertonic saline 3% infusion | - | ICP management (less acute) | 0.5-1 mL/kg :: - :: continuous :: 0.5-1 mL/kg/h continuous; target Na 145-155 | Hypernatremia | Na q4-6h; osmolality | - | - | - | STAT |
| Phenytoin/Fosphenytoin | IV | Refractory seizures (second-line after levetiracetam) | 20 mg :: IV :: q8h :: Fosphenytoin 20 mg PE/kg IV at 150 mg PE/min; maintenance 100 mg PE q8h; target level 10-20 µg/mL | Bradycardia, heart block, hypotension (infusion rate-related) | Continuous telemetry during load; free phenytoin level; LFTs | STAT | STAT | - | STAT |
| Lacosamide | IV | Seizure management (adjunctive) | 200 mg :: IV :: BID :: 200 mg IV/PO load; then 100-200 mg BID; max 400 mg/day | PR prolongation, AV block | ECG; PR interval | - | ROUTINE | ROUTINE | ROUTINE |
| Ondansetron | IV | Nausea/vomiting | 4 mg :: IV :: q6h :: 4 mg IV/PO q6h PRN | QT prolongation | QTc | STAT | ROUTINE | - | STAT |
| Pantoprazole | IV | GI prophylaxis (if steroids or critical illness) | 40 mg :: IV :: daily :: 40 mg IV/PO daily | C. diff risk long-term | GI symptoms | - | ROUTINE | - | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis | 40 mg :: SC :: daily :: 40 mg SC daily (start when not actively seizing and no hemorrhagic transformation) | Active bleeding, hemorrhagic transformation, coagulopathy, platelets <50K | Platelets q3 days | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | DVT prophylaxis | N/A :: - :: continuous :: Apply bilaterally on admission | Acute DVT | Skin checks | STAT | STAT | - | STAT |
| Fluid restriction | - | SIADH management | 1-1.2 L :: - :: per protocol :: 1-1.2 L/day if Na <130 with clinical SIADH | Dehydration (balance with acyclovir hydration needs) | Na q6-8h; urine osm/Na; I/O | - | ROUTINE | - | ROUTINE |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Foscarnet IV (acyclovir-resistant HSV) | IV | - | 60 mg/kg :: IV :: q8h :: 60 mg/kg IV q8h or 90 mg/kg IV q12h; infuse over 1-2h with aggressive hydration. For proven or suspected acyclovir resistance (immunocompromised, HIV) | Renal failure (major nephrotoxin); electrolyte abnormalities | Cr daily; Ca, Mg, K, PO4 BID (causes severe electrolyte wasting); hydration 1-2 L NS before each dose | - | EXT | - | EXT |
| Decompressive craniectomy | - | - | N/A :: - :: once :: For malignant cerebral edema with impending herniation, unresponsive to medical ICP management; consider if age appropriate and prognosis not already dismal | Bilateral massive necrosis; moribund patient | Post-op neuro checks; ICP monitoring; wound care | - | - | - | STAT |
| Immunotherapy for post-HSV autoimmune encephalitis | IV | - | 1g/day :: IV :: daily x 5 days :: If relapse at 2-6 weeks with new anti-NMDAR antibodies: IV methylprednisolone 1g/day x 5 days + IVIG 0.4 g/kg/day x 5 days; second-line: rituximab | Active HSV infection (ensure viral replication controlled) | NMDAR antibody titers; clinical response; viral PCR to confirm HSV not reactivated | - | URGENT | ROUTINE | URGENT |

### 3D. Duration of Treatment and Discontinuation

| Scenario | Duration | Criteria to Stop |
|----------|----------|-----------------|
| Confirmed HSV encephalitis (PCR positive) | 14-21 days IV acyclovir | Clinical improvement; repeat LP at end of treatment — if HSV PCR still positive, continue additional 7 days |
| Suspected HSV, PCR negative x2 | Consider stopping at 7-10 days if: two negative HSV PCRs (initial + repeat at 3-7 days), MRI not consistent with HSV, alternative diagnosis established | Clinical stability; alternative diagnosis confirmed |
| Immunocompromised patients | 21 days minimum | Repeat LP with PCR before stopping; ensure negative PCR before discontinuation |
| Transition to oral | Oral valacyclovir 1g PO TID x 3-6 months after IV course is INVESTIGATIONAL; some centers use for immunocompromised; not standard of care | Expert guidance |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology consultation | STAT | STAT | - | STAT | All suspected encephalitis; seizure management; EEG interpretation; post-HSV autoimmune evaluation |
| Infectious disease consultation | STAT | STAT | - | STAT | Antimicrobial management; acyclovir-resistant HSV; duration of therapy |
| Neurosurgery consultation | - | URGENT | - | STAT | Cerebral edema with mass effect; ICP monitoring (EVD placement); decompressive craniectomy |
| Critical care/ICU | STAT | STAT | - | STAT | Altered consciousness (GCS <12); respiratory failure; ICP management; status epilepticus |
| Speech-language pathology (SLP) | - | URGENT | ROUTINE | URGENT | Dysphagia evaluation; aphasia assessment (temporal lobe involvement); cognitive-communication evaluation |
| Physical therapy (PT) | - | URGENT | ROUTINE | URGENT | Early mobilization; prevent deconditioning; gait/balance training |
| Occupational therapy (OT) | - | URGENT | ROUTINE | URGENT | ADL assessment; cognitive rehabilitation; memory aids |
| Neuropsychology | - | ROUTINE | ROUTINE | - | Cognitive assessment (memory deficits common with temporal lobe damage); rehabilitation planning |
| Psychiatry | - | ROUTINE | ROUTINE | - | Behavioral changes; depression; anxiety; personality changes (frontal/temporal damage) |
| Rehabilitation medicine (physiatry) | - | ROUTINE | ROUTINE | - | Rehabilitation planning; disposition (inpatient rehab, SNF) |
| Social work | - | ROUTINE | ROUTINE | - | Family support; discharge planning; long-term care needs |
| Epilepsy specialist | - | ROUTINE | ROUTINE | - | Post-encephalitis epilepsy management; temporal lobe epilepsy |
| Palliative care | - | ROUTINE | - | ROUTINE | Goals of care for severe cases; prognostication |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED if: new confusion, seizure, fever recurrence, worsening headache, personality change, speech difficulty, new weakness | STAT | STAT | ROUTINE |
| HSV encephalitis can cause long-term memory and cognitive deficits; rehabilitation is important | - | ROUTINE | ROUTINE |
| Seizures may develop weeks to months after infection; report any episodic symptoms (staring, jerking, déjà vu, loss of awareness) | - | ROUTINE | ROUTINE |
| Post-HSV autoimmune encephalitis can occur 2-6 weeks later with new psychiatric/neurologic symptoms — report immediately | - | ROUTINE | ROUTINE |
| Take all medications as prescribed; do NOT stop antiepileptic drugs without neurologist guidance | - | ROUTINE | ROUTINE |
| Follow-up with neurology in 2-4 weeks; neuropsychology testing at 3-6 months | - | ROUTINE | ROUTINE |
| Cognitive rehabilitation and therapy are critical for recovery | - | ROUTINE | ROUTINE |
| Driving restrictions until seizure-free per state law (typically 3-12 months) | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| HSV encephalitis is NOT contagious in the traditional sense; no isolation needed | - | ROUTINE | ROUTINE |
| Long-term suppressive antiviral therapy is NOT standard after encephalitis (unlike genital HSV) | - | ROUTINE | ROUTINE |
| Cognitive rehabilitation: memory strategies, organizational tools, speech therapy | - | ROUTINE | ROUTINE |
| Seizure safety: avoid heights, swimming alone, operating heavy machinery until seizure-free | - | ROUTINE | ROUTINE |
| Mental health support (depression, anxiety, PTSD common after encephalitis) | - | ROUTINE | ROUTINE |
| Adequate sleep and stress management | - | ROUTINE | ROUTINE |
| Gradual return to work/school with accommodations as needed | - | - | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Autoimmune encephalitis (anti-NMDAR) | Subacute; psychiatric symptoms (psychosis, agitation); orofacial dyskinesias; seizures; young women; often post-HSV | Anti-NMDAR antibody (CSF > serum); MRI may be normal or temporal; ovarian teratoma screen |
| Bacterial meningitis | Fever + meningismus; CSF neutrophilic pleocytosis with low glucose; more acute; no temporal preference on imaging | CSF Gram stain, culture, BioFire; procalcitonin elevated; CSF glucose low |
| Viral meningitis (enterovirus) | Headache + fever + meningismus; LESS confusion/focal deficits; CSF lymphocytic but fewer WBC; MRI normal | Enterovirus PCR (CSF); BioFire panel; normal MRI |
| VZV encephalitis | Immunocompromised; may have rash (but not always); vasculopathy pattern on MRI; cranial neuropathies | VZV PCR (CSF); VZV IgG intrathecal antibody |
| Temporal lobe seizures / Status epilepticus | Seizures may cause MRI signal change in temporal lobes mimicking encephalitis; fever if convulsive SE | EEG; HSV PCR negative; MRI DWI pattern; clinical course |
| Limbic encephalitis (paraneoplastic: LGI1, GABA-B) | Subacute memory loss, seizures, psychiatric changes; often >40 years; associated malignancy | Antibody panel (serum + CSF); CT chest/abdomen/pelvis; PET-CT |
| Cerebral venous thrombosis | Headache, seizures, focal deficits; papilledema; risk factors (OCPs, hypercoagulable) | MRV; CT venogram; D-dimer |
| Brain abscess | Focal symptoms + fever; ring-enhancing lesion; subacute | MRI with contrast (ring enhancement, restricted DWI centrally); blood cultures |
| Acute disseminated encephalomyelitis (ADEM) | Post-infectious; multifocal white matter lesions; children > adults | MRI (multifocal white matter); clinical context |
| Tuberculosis meningitis | Subacute (weeks); basilar meningitis; CSF low glucose, lymphocytic, very high protein | AFB culture; TB PCR; ADA; chest imaging |
| Neurosyphilis | Subacute; psychiatric symptoms; pupillary abnormalities; history of STI | CSF VDRL; FTA-ABS; RPR |
| Primary CNS lymphoma | Immunocompromised; progressive focal deficits; periventricular enhancing lesion | MRI with contrast; CSF cytology; EBV PCR (CSF); brain biopsy |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| GCS / Neurologic exam | STAT | STAT | ROUTINE | STAT | q1h x 24h, then q2h x 48h, then q4h | Improving or stable GCS | If declining: STAT CT; ICP assessment; consider EVD |
| Temperature | STAT | STAT | - | STAT | q4h (q1h if febrile) | <38°C | Acetaminophen; cooling measures; reassess if persistent fever >72h on acyclovir |
| Serum sodium | STAT | STAT | ROUTINE | STAT | q6-8h x 48h, then q12h | 135-145 mEq/L | If <130: SIADH → fluid restriction (balance with acyclovir hydration); if <120: 3% saline |
| Serum creatinine | STAT | ROUTINE | ROUTINE | STAT | Daily (twice daily if rising) | Stable; within normal | If rising: increase hydration; consider dose adjustment; hold if severe (rare); monitor urine output |
| BUN | - | ROUTINE | - | ROUTINE | Daily | Normal | Dehydration; renal impairment |
| Urine output | STAT | STAT | - | STAT | q1h in ICU; q4h shift on floor | >0.5 mL/kg/h (critical for acyclovir clearance) | Increase IV fluids; if oliguria: renal assessment |
| Seizure monitoring (EEG) | - | URGENT | - | STAT | cEEG 24-72h if altered consciousness; routine EEG daily if improving | No seizure activity | If seizures: load/adjust AEDs; if NCSE: aggressive treatment per SE protocol |
| Blood pressure | STAT | STAT | - | STAT | q1-4h based on severity | Stable; MAP >60 | Fluids; vasopressors if septic |
| Oxygen saturation | STAT | STAT | - | STAT | Continuous in ICU; q4h on floor | ≥94% | Supplemental O2; intubation if respiratory failure |
| Repeat MRI brain | - | ROUTINE | ROUTINE | ROUTINE | At 48-72h (evolution); day 7-14 (extent of damage); 3-6 months (chronic changes) | Stable or improving | If worsening edema: ICP management; neurosurgery consult |
| Repeat LP (HSV PCR) | - | ROUTINE | - | ROUTINE | At end of treatment (day 14-21) to confirm PCR negativity; earlier if clinical suspicion of treatment failure | HSV PCR negative | If still positive: extend acyclovir 7+ more days; consider resistance |
| Autoimmune antibodies (follow-up) | - | ROUTINE | ROUTINE | - | Recheck at 2-4 weeks if relapse or new psychiatric/neurologic symptoms | Negative | If positive (especially NMDAR): immunotherapy protocol |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | NOT appropriate directly from ED for suspected HSV encephalitis — always admit. Discharge from hospital when: completing IV acyclovir course (or transitioned to monitoring); improved consciousness (GCS 15); no active seizures; stable neurologic exam; safe swallowing; rehabilitation arranged; follow-up confirmed |
| Admit to floor (monitored bed) | Mild encephalitis (GCS 13-15); stable; low seizure burden; able to cooperate with neuro checks |
| Admit to ICU / Neuro-ICU | GCS <13; active seizures or status epilepticus; need for continuous EEG; respiratory compromise; signs of elevated ICP; hemodynamic instability |
| Transfer to higher level | Need for neuro-ICU not available; need for neurosurgery (decompressive craniectomy); continuous EEG not available |
| Inpatient rehabilitation | Moderate-severe cognitive deficits (memory impairment, aphasia); motor deficits; able to participate in 3h/day therapy |
| Skilled nursing facility | Unable to tolerate intensive rehabilitation; requires ongoing nursing care |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IV acyclovir 10 mg/kg q8h x 14-21 days | Class I, Level A | [Whitley et al. (NEJM 1986)](https://pubmed.ncbi.nlm.nih.gov/3001520/) — acyclovir vs placebo landmark trial; reduced mortality from 70% to 20% |
| Start acyclovir empirically; do NOT delay for diagnostics | Class I, Level A | IDSA Encephalitis Guidelines ([Tunkel et al. CID 2008](https://pubmed.ncbi.nlm.nih.gov/18582201/)); every hour of delay worsens outcomes |
| CSF HSV PCR as gold standard (sensitivity 96-98%) | Class I, Level A | [Lakeman & Whitley (JID 1995)](https://pubmed.ncbi.nlm.nih.gov/7706811/) |
| Repeat HSV PCR if initially negative with high clinical suspicion | Class I, Level B | False negative rate ~5% in first 72h; Roullet (2007) |
| MRI with DWI is most sensitive imaging | Class I, Level A | Sensitivity >90% within 48h; temporal lobe predilection |
| EEG showing PLEDs supports diagnosis | Class IIa, Level B | Periodic lateralizing discharges in ~80% of HSV encephalitis |
| Post-HSV autoimmune encephalitis (anti-NMDAR) in 20-27% | Class IIa, Level B | [Armangue et al. (Ann Neurol 2014)](https://pubmed.ncbi.nlm.nih.gov/24318406/); [Prüss et al. (Ann Neurol 2012)](https://pubmed.ncbi.nlm.nih.gov/23280840/) |
| Dexamethasone for HSV encephalitis: NOT standard of care | Class IIb, Level C | DexEnceph trial (ongoing); animal data supportive; no clear human mortality benefit |
| Foscarnet for acyclovir-resistant HSV | Class IIa, Level C | Expert consensus; primarily in immunocompromised |
| Aggressive hydration to prevent acyclovir nephrotoxicity | Class I, Level B | Well-established; crystal nephropathy prevention |
| Empiric bacterial coverage until excluded | Class I, Level A | Standard practice; cannot clinically distinguish bacterial meningitis from encephalitis at presentation |
| Repeat LP at end of treatment to confirm PCR negativity | Class IIa, Level C | Expert consensus; immunocompromised patients especially |
| 14-day treatment minimum; 21 days for severe/immunocompromised | Class I, Level B | IDSA Guidelines; relapse rate higher with <14 days |

---

**APPENDIX: CLASSIC MRI FINDINGS IN HSV ENCEPHALITIS**

| Feature | Description |
|---------|-------------|
| Location | Medial temporal lobes (hippocampus, amygdala), insular cortex, inferior frontal gyri, cingulate gyrus |
| Pattern | Unilateral initially; may become bilateral (asymmetric) |
| T2/FLAIR | Hyperintensity in affected regions |
| DWI | Restricted diffusion (bright on DWI, dark on ADC) in acute phase |
| Hemorrhage | SWI/GRE may show hemorrhagic necrosis (petechial or confluent) |
| Enhancement | Variable; leptomeningeal or cortical enhancement possible |
| Sparing | Typically spares basal ganglia and thalami (unlike autoimmune encephalitis which may involve these) |

**APPENDIX: POST-HSV AUTOIMMUNE ENCEPHALITIS**

| Feature | Details |
|---------|---------|
| Timing | 2-6 weeks after HSV encephalitis (range 1 week to 3 months) |
| Prevalence | 20-27% of HSV encephalitis cases |
| Antibody | Most commonly anti-NMDAR; less commonly others |
| Presentation | New psychiatric symptoms (psychosis, agitation), movement disorders (orofacial dyskinesias, choreoathetosis), seizures, autonomic instability, decreased consciousness |
| Diagnosis | Anti-NMDAR antibody in CSF; HSV PCR NEGATIVE (distinguishes from viral relapse) |
| Treatment | Immunotherapy: IV methylprednisolone + IVIG; second-line: rituximab; ensure HSV PCR negative before immunosuppression |
| Prognosis | Generally good with treatment; better than primary autoimmune encephalitis |
