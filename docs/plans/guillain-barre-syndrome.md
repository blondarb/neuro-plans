---
title: "Guillain-Barré Syndrome (GBS)"
description: "Clinical decision support for guillain-barré syndrome (gbs) diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - epilepsy
  - headache
  - movement-disorders
  - demyelinating
  - infectious
---

# Guillain-Barré Syndrome (GBS)

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Guillain-Barré Syndrome (GBS)

**ICD-10:** G61.0 (Guillain-Barré syndrome)

**CPT CODES:** 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 83735 (Magnesium), 84100 (Phosphorus), 85652 (ESR), 82947 (Blood glucose), 81003 (Urinalysis), 85610 (PT/INR), 86900 (Type and screen), 86255 (Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b)), 80074 (Hepatitis B surface antigen, anti-HBc), 87389 (HIV 1/2 antigen/antibody), 84443 (TSH), 82607 (B12), 86334 (Serum protein electrophoresis (SPEP) with immunofixation), 72156 (MRI spine with and without contrast (whole spine)), 95907-95913 (Nerve conduction studies), 71046 (Chest X-ray), 93000 (ECG (12-lead)), 70553 (MRI brain with and without contrast), 71260 (CT chest with contrast), 93306 (Echocardiogram), 94010 (Pulmonary function testing (formal)), 89051 (Cell count (tubes 1 and 4)), 84157 (Protein), 82945 (Glucose with serum glucose), 88104 (Cytology), 86592 (VDRL (CSF)), 83916 (Oligoclonal bands), 96365 (IVIG (intravenous immunoglobulin)), 36514 (Plasmapheresis (PLEX))

**SYNONYMS:** Guillain-Barré syndrome, GBS, acute inflammatory demyelinating polyneuropathy, AIDP, acute motor axonal neuropathy, AMAN, acute motor-sensory axonal neuropathy, AMSAN, ascending paralysis, Landry's paralysis, post-infectious polyneuropathy

**SCOPE:** Acute inflammatory polyradiculoneuropathy including AIDP, AMAN, AMSAN, and Miller Fisher syndrome (MFS) variants. Covers acute diagnosis, respiratory monitoring, immunotherapy (IVIG/PLEX), autonomic dysfunction management, pain control, and rehabilitation planning. Excludes CIDP (chronic inflammatory demyelinating polyneuropathy — separate template), tick paralysis, and chronic neuropathies.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; infection screen; exclude hematologic causes | Normal; leukocytosis suggests infection trigger |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolyte abnormalities (hyponatremia from SIADH), renal/hepatic function for IVIG dosing | Normal |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia worsens weakness; arrhythmia risk | >1.8 mg/dL |
| Phosphorus (CPT 84100) | STAT | ROUTINE | ROUTINE | STAT | Hypophosphatemia causes weakness (mimic) | >2.5 mg/dL |
| ESR (CPT 85652) / CRP (CPT 86140) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory markers; infection screen | Mildly elevated (non-specific) |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Diabetes as comorbidity; hyperglycemia management | Normal |
| Urinalysis (CPT 81003) | STAT | ROUTINE | ROUTINE | STAT | UTI as precipitant; baseline | Normal |
| Pregnancy test (β-hCG) | STAT | STAT | ROUTINE | STAT | Affects IVIG formulation choice; imaging considerations | Document result |
| PT/INR (CPT 85610), aPTT (CPT 85730) | STAT | ROUTINE | - | STAT | Coagulation status before procedures (LP, central line) | Normal |
| Type and screen (CPT 86900) | STAT | ROUTINE | - | STAT | Potential need for PLEX | On file |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b) (CPT 86255) | - | ROUTINE | ROUTINE | ROUTINE | GM1: AMAN; GQ1b: Miller Fisher; GD1a: AMAN; helps confirm diagnosis and subtype | Positive supports diagnosis (negative does not exclude) |
| Anti-GQ1b antibody | - | ROUTINE | ROUTINE | - | Miller Fisher syndrome (ataxia, ophthalmoplegia, areflexia) | Positive in >90% MFS |
| Campylobacter jejuni serology (IgM, IgG) | - | ROUTINE | ROUTINE | - | Most common infectious trigger (30%); AMAN variant association | Positive IgM suggests recent infection |
| Mycoplasma pneumoniae IgM | - | ROUTINE | ROUTINE | - | Common triggering infection | Positive IgM suggests recent infection |
| CMV IgM | - | ROUTINE | ROUTINE | - | Triggering infection; associated with severe demyelinating GBS | Positive IgM |
| EBV panel (VCA IgM, EBNA) | - | ROUTINE | ROUTINE | - | Triggering infection | Positive VCA IgM |
| Hepatitis B surface antigen, anti-HBc (CPT 80074) | - | ROUTINE | ROUTINE | - | Screen before IVIG; reactivation risk | Negative |
| Hepatitis C antibody (CPT 80074) | - | ROUTINE | ROUTINE | - | Cryoglobulinemia-associated neuropathy (differential) | Negative |
| HIV 1/2 antigen/antibody (CPT 87389) | - | ROUTINE | ROUTINE | - | HIV-associated neuropathy; acute HIV can mimic GBS | Negative |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Thyroid dysfunction can cause weakness | Normal |
| B12 (CPT 82607), methylmalonic acid (CPT 83921) | - | ROUTINE | ROUTINE | - | B12 deficiency neuropathy (differential) | Normal |
| Serum protein electrophoresis (SPEP) with immunofixation (CPT 86334) | - | ROUTINE | ROUTINE | - | Paraproteinemia-associated neuropathy (differential); POEMS | Normal |
| IgA level (quantitative) | - | ROUTINE | - | ROUTINE | IgA deficiency contraindicates standard IVIG (anaphylaxis risk); check BEFORE IVIG if possible | Normal (>7 mg/dL) |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Zika virus serology/PCR | - | EXT | EXT | - | Endemic areas; associated with GBS outbreaks | Negative |
| Influenza A/B PCR | - | EXT | - | EXT | Triggering infection; seasonal | Negative |
| COVID-19 PCR/antigen | - | ROUTINE | - | ROUTINE | Post-COVID GBS association reported | Document result |
| Lyme serology (ELISA, Western blot) | - | EXT | EXT | - | Lyme-associated polyradiculopathy (differential); endemic areas | Negative |
| Paraneoplastic panel (serum) (CPT 86255) | - | EXT | EXT | - | If atypical features or poor response to treatment | Negative |
| Heavy metals (lead, arsenic, thallium) | - | EXT | EXT | - | Toxic neuropathy mimic; occupational exposure | Normal |
| Porphyrins (urine ALA, PBG) | - | EXT | EXT | - | Acute intermittent porphyria mimic (motor predominant, autonomic dysfunction) | Normal |
| Anti-MAG antibody (CPT 86255) | - | EXT | EXT | - | MAG-associated neuropathy (differential; chronic presentation) | Negative |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI spine with and without contrast (whole spine) (CPT 72156) | URGENT | URGENT | ROUTINE | URGENT | Within 24h of presentation | Nerve root enhancement (anterior roots in AIDP); exclude compressive myelopathy, spinal cord lesion, epidural abscess | Pacemaker, metallic implants |
| Nerve conduction studies (CPT 95907-95913) / EMG (CPT 95886) (NCS/EMG) | - | URGENT | ROUTINE | URGENT | Ideally within 3-5 days of symptom onset (may be normal in first 48h); repeat at 2-3 weeks if initially non-diagnostic | Demyelinating pattern: prolonged distal latencies, conduction block, temporal dispersion, prolonged F-waves, absent H-reflex. Axonal pattern (AMAN): reduced CMAP amplitudes with normal velocities | None significant; avoid anticoagulated patients for EMG needle exam |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | On admission | Aspiration, atelectasis, baseline for ventilator management | None significant |
| ECG (12-lead) (CPT 93000) | URGENT | ROUTINE | - | URGENT | On admission and PRN | Arrhythmias (sinus tachycardia, bradycardia, AV block); autonomic dysfunction | None |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) | - | ROUTINE | ROUTINE | ROUTINE | If Miller Fisher variant suspected or cranial nerve involvement | Cranial nerve enhancement (especially CN III, VI, VII); exclude central lesion | Same as MRI |
| CT chest with contrast (CPT 71260) | - | EXT | EXT | - | If paraneoplastic etiology suspected; thymoma screen if MG in differential | Mass lesion | Contrast allergy, renal impairment |
| Repeat NCS/EMG | - | ROUTINE | ROUTINE | - | At 2-4 weeks if initial study non-diagnostic or to assess prognosis | Evolution of findings; axonal degeneration predicts slower recovery | Same as initial |
| Echocardiogram (CPT 93306) | - | ROUTINE | - | ROUTINE | If autonomic instability or new murmur | Cardiac function; Takotsubo in severe autonomic GBS | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Nerve ultrasound (high-resolution) | - | EXT | EXT | - | If diagnosis uncertain | Nerve enlargement in CIDP (helps differentiate); some enlargement reported in GBS | None |
| Pulmonary function testing (formal) (CPT 94010) | - | ROUTINE | ROUTINE | - | If borderline respiratory function | Full spirometry for outpatient monitoring | Unable to cooperate |

### LUMBAR PUNCTURE

**Indication:** Diagnostic confirmation of GBS; albuminocytologic dissociation is classic finding

**Timing:** URGENT in ED or within first 24h of admission; may be normal in first 48h — repeat at 1 week if initially normal

**Volume Required:** 10-15 mL (standard diagnostic)

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | URGENT | ROUTINE | ROUTINE | Rule out elevated ICP | 10-20 cm H2O (normal) |
| Cell count (tubes 1 and 4) (CPT 89051) | URGENT | ROUTINE | ROUTINE | Albuminocytologic dissociation | WBC <10 cells/µL (if >50 WBC, reconsider diagnosis — HIV, Lyme, sarcoidosis, lymphoma) |
| Protein (CPT 84157) | URGENT | ROUTINE | ROUTINE | Classic finding: elevated protein with normal WBC | Elevated >45 mg/dL (often >100 mg/dL; may be normal in first week) |
| Glucose with serum glucose (CPT 82945) | URGENT | ROUTINE | ROUTINE | Normal in GBS; low in infectious/malignant meningitis | Normal (>60% serum) |
| Gram stain and culture | URGENT | ROUTINE | ROUTINE | Exclude bacterial meningitis | No organisms |
| Cytology (CPT 88104) | - | ROUTINE | ROUTINE | Exclude leptomeningeal lymphoma/carcinomatosis | Negative |
| VDRL (CSF) (CPT 86592) | - | ROUTINE | ROUTINE | Neurosyphilis can mimic | Negative |
| Oligoclonal bands (CPT 83916), IgG index | - | ROUTINE | ROUTINE | Differentiate from MS; may be positive in GBS (non-specific) | Negative or low titer |

**Special Handling:** Standard processing. Cell count and protein are the critical values.

**Contraindications:** Elevated ICP without imaging (CT first), coagulopathy (INR >1.5, platelets <50K), skin infection at LP site. Anticoagulation should be held.

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IVIG (intravenous immunoglobulin) (CPT 96365) | IV | - | 0.4 g/kg :: IV :: daily x 5 days :: 0.4 g/kg/day IV x 5 days (total 2 g/kg); infuse over 4-8h per dose; slow initial rate and increase per protocol. Start within 2 weeks of symptom onset for maximum benefit | IgA deficiency (use IgA-depleted product); acute renal failure; anaphylaxis to immunoglobulin | Vital signs q15min during first infusion, then q30min; renal function (BUN, Cr) before and during; headache (aseptic meningitis); thrombotic events; hemolysis (haptoglobin, LDH, direct Coombs if symptoms) | - | STAT | - | STAT |
| Plasmapheresis (PLEX) (CPT 36514) | - | - | N/A :: - :: once :: 5 exchanges over 7-14 days (typically every other day); each exchange 1-1.5 plasma volumes; use albumin replacement. Start within 4 weeks of symptom onset | Hemodynamic instability, severe sepsis, active bleeding, heparin allergy (for circuit anticoagulation), poor vascular access | BP and HR continuous during exchange; calcium (citrate toxicity: tingling, cramping); fibrinogen; CBC; electrolytes; line site infection | - | STAT | - | STAT |
| Intubation and mechanical ventilation | - | - | 20 mL/kg :: - :: - :: Indications (20/30/40 rule): FVC <20 mL/kg, NIF weaker than -30 cmH2O, >30% decline in FVC from baseline, or clinical respiratory distress. Use non-depolarizing agents (avoid succinylcholine — hyperkalemia risk). RSI with rocuronium preferred | N/A (life-saving) | Ventilator settings per ICU protocol; sedation; daily spontaneous breathing trial when improving | STAT | STAT | - | STAT |
| DVT prophylaxis: Enoxaparin | SC | - | 40 mg :: SC :: daily :: 40 mg SC daily; start on admission | Active bleeding, platelets <50K, CrCl <30 (use UFH) | Platelets q3 days; anti-Xa if renal impairment | - | ROUTINE | - | ROUTINE |
| DVT prophylaxis: Heparin SC (alternative) | SC | - | 5000 units :: SC :: - :: 5000 units SC q8-12h | Active bleeding, HIT | Platelets q3 days | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | - | N/A :: - :: continuous :: Apply bilaterally on admission; continue until ambulatory | Acute DVT, severe PVD | Skin checks daily | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Gabapentin | PO | Neuropathic pain (very common in GBS — 55-89%) | 300 mg :: PO :: qHS :: Start 300 mg PO qHS; increase by 300 mg/day every 1-3 days; target 900-1800 mg TID; max 3600 mg/day | Severe renal impairment (dose adjust); oversedation | Sedation, dizziness; adjust for renal function | - | ROUTINE | ROUTINE | ROUTINE |
| Pregabalin | PO | Neuropathic pain (alternative) | 75 mg :: PO :: BID :: Start 75 mg PO BID; increase to 150 mg BID after 3-7 days; max 300 mg BID | Renal impairment (dose adjust) | Sedation, weight gain, peripheral edema | - | ROUTINE | ROUTINE | ROUTINE |
| Carbamazepine | PO | Neuropathic pain (alternative) | 100 mg :: PO :: BID :: Start 100 mg PO BID; increase by 100 mg/day q3-7 days; target 400-800 mg/day in divided doses; max 1200 mg/day | AV block, bone marrow suppression, HLA-B*1502 (Asian descent — screen before starting) | CBC, LFTs, sodium at baseline and 2-4 weeks; drug level | - | ROUTINE | ROUTINE | - |
| Amitriptyline | PO | Neuropathic pain, insomnia | 10-25 mg :: PO :: qHS :: Start 10-25 mg PO qHS; increase by 10-25 mg q1-2 weeks; max 150 mg/day | Arrhythmia, urinary retention, angle-closure glaucoma, recent MI | ECG if cardiac risk; anticholinergic side effects | - | ROUTINE | ROUTINE | - |
| Acetaminophen | PO | Musculoskeletal pain, headache | 650-1000 mg :: PO :: q6h :: 650-1000 mg PO q6h; max 4g/day (2g hepatic impairment) | Severe liver disease | LFTs if prolonged | STAT | ROUTINE | ROUTINE | STAT |
| Morphine IV | IV | Severe pain unresponsive to above | 2-4 mg :: IV :: PRN :: 2-4 mg IV q3-4h PRN; use with caution — respiratory depression risk especially with respiratory compromise | Respiratory failure (relative — monitor closely), ileus | RR, SpO2, sedation scale; bowel function | - | URGENT | - | URGENT |
| Oxycodone | PO | Moderate-severe pain (if able to swallow) | 5-10 mg :: PO :: PRN :: 5-10 mg PO q4-6h PRN | Same as morphine | Same as morphine | - | ROUTINE | ROUTINE | - |
| Metoclopramide | IV | Gastroparesis, nausea (autonomic dysfunction) | 10 mg :: IV :: q6h :: 10 mg IV/PO q6h PRN; max 40 mg/day; limit duration to <12 weeks | Seizure history, Parkinson disease, GI obstruction | Tardive dyskinesia with prolonged use | - | ROUTINE | - | ROUTINE |
| Docusate sodium | PO | Constipation (immobility + opioids) | 100 mg :: PO :: BID :: 100 mg PO BID | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | ROUTINE |
| Senna | PO | Constipation | 8.6-17.2 mg :: PO :: qHS :: 8.6-17.2 mg PO qHS | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | - |
| Polyethylene glycol (MiraLAX) | PO | Constipation (if docusate insufficient) | 17 g :: PO :: daily :: 17 g PO daily in 8 oz water | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | - |
| Melatonin | PO | Insomnia (ICU delirium prevention) | 3-5 mg :: PO :: qHS :: 3-5 mg PO qHS | None significant | Sleep quality | - | ROUTINE | - | ROUTINE |
| Lorazepam | IV | Anxiety, autonomic crisis | 0.5-1 mg :: IV :: PRN :: 0.5-1 mg IV/PO q6-8h PRN | Respiratory compromise (use with extreme caution) | RR, sedation | - | URGENT | - | URGENT |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Second course IVIG | PO | - | 0.4 g/kg :: PO :: daily x 5 days :: 0.4 g/kg/day x 5 days; consider if progressive deterioration after initial treatment or treatment-related fluctuation (TRF) | Same as initial IVIG | Same as initial IVIG | - | URGENT | - | URGENT |
| PLEX after IVIG failure | - | - | N/A :: - :: per protocol :: 5 exchanges over 7-14 days; wait ≥2 weeks after IVIG to avoid washing out immunoglobulin | Same as initial PLEX | Same as initial PLEX | - | URGENT | - | URGENT |
| IV methylprednisolone (NOT standard of care) (CPT 96365) | IV | - | 500 mg :: IV :: daily :: 500 mg IV daily x 5 days; evidence does NOT support steroids alone; may be considered in combination with IVIG per some centers for refractory cases | Active infection, uncontrolled diabetes | Glucose, BP, GI prophylaxis | - | EXT | - | EXT |

### 3D. Disease-Modifying or Chronic Therapies

*Not applicable for GBS (acute monophasic illness). If recurrent or chronic course (>8 weeks), reconsider diagnosis — evaluate for CIDP.*

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology consultation | STAT | STAT | - | STAT | All suspected GBS; diagnostic confirmation, treatment initiation |
| Pulmonology / Critical care | URGENT | URGENT | - | STAT | Declining respiratory function; intubation decision; ventilator management |
| Physical therapy (PT) | - | URGENT | ROUTINE | URGENT | Early passive ROM to prevent contractures; gradual mobilization as tolerated; gait training |
| Occupational therapy (OT) | - | URGENT | ROUTINE | URGENT | Upper extremity function, ADLs, adaptive equipment |
| Speech-language pathology (SLP) | - | URGENT | ROUTINE | URGENT | Dysphagia evaluation (bulbar weakness); aspiration prevention |
| Rehabilitation medicine (physiatry) | - | ROUTINE | ROUTINE | - | Rehabilitation planning; disposition (inpatient rehab vs SNF) |
| Pain management | - | ROUTINE | ROUTINE | ROUTINE | Refractory neuropathic pain |
| Social work | - | ROUTINE | ROUTINE | - | Discharge planning, family support, financial resources |
| Psychology / Psychiatry | - | ROUTINE | ROUTINE | - | Anxiety, depression, PTSD (common in ICU patients) |
| Respiratory therapy | - | STAT | - | STAT | Bedside spirometry (FVC, NIF); pulmonary toilet; ventilator weaning |
| Nutrition / Dietitian | - | ROUTINE | - | ROUTINE | Enteral feeding plan if intubated; caloric needs during recovery |
| Infectious disease | - | ROUTINE | - | - | If triggering infection unclear or atypical presentation |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED / Call 911 if: increasing difficulty breathing, new swallowing difficulty, rapid worsening of weakness, inability to walk, chest pain, or lightheadedness | STAT | STAT | ROUTINE |
| GBS is typically a self-limited illness; most patients recover substantially but recovery may take months to years | - | ROUTINE | ROUTINE |
| Do NOT drive until strength and reflexes have recovered and neurology clears | - | ROUTINE | ROUTINE |
| Comply with physical therapy exercises as prescribed between sessions | - | ROUTINE | ROUTINE |
| Pain is normal in GBS and will be managed with medications; report if pain is inadequately controlled | - | ROUTINE | ROUTINE |
| Inform future healthcare providers about GBS history (vaccine considerations, anesthesia precautions) | - | ROUTINE | ROUTINE |
| Fall prevention: use assistive devices (walker, cane) as recommended; remove tripping hazards at home | - | ROUTINE | ROUTINE |
| Monitor for signs of blood clots: leg swelling, redness, chest pain, shortness of breath | - | ROUTINE | ROUTINE |
| Follow-up with neurology in 2-4 weeks after discharge; NCS/EMG may be repeated at 3-6 months | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Gradual return to activity as tolerated; avoid overexertion during recovery | - | ROUTINE | ROUTINE |
| Balanced nutrition for nerve recovery (adequate protein, B vitamins) | - | ROUTINE | ROUTINE |
| Smoking cessation (impairs nerve healing) | - | ROUTINE | ROUTINE |
| Adequate sleep (promotes neurologic recovery) | - | ROUTINE | ROUTINE |
| Mental health support (depression and anxiety common during recovery) | - | ROUTINE | ROUTINE |
| Flu vaccination: generally safe after GBS; discuss with neurologist (6 weeks post-onset minimum; risk-benefit individualized) | - | - | ROUTINE |
| COVID-19 vaccination: discuss risk-benefit with neurologist; most experts recommend vaccination after recovery | - | - | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Transverse myelitis | Sensory level, upper motor neuron signs (hyperreflexia, Babinski), bladder involvement early, MRI spinal cord lesion | MRI spine (cord signal change); LP (pleocytosis more common); NCS/EMG (normal peripheral nerves) |
| Myasthenia gravis | Fatigable weakness, ptosis, diplopia, intact reflexes, fluctuating symptoms, no sensory involvement | AChR antibodies, repetitive nerve stimulation (decremental), edrophonium test |
| Botulism | Descending paralysis (cranial nerves first), pupil involvement, GI prodrome, toxin exposure | Stool/serum botulinum toxin assay; NCS (incremental response at high-rate repetitive stimulation) |
| Tick paralysis | Ascending paralysis similar to GBS; tick found on exam; rapid recovery after tick removal | Physical exam (search for tick, especially scalp); NCS may show reduced CMAPs; CSF normal |
| Spinal cord compression | Back pain, sensory level, upper motor neuron signs below level, bladder dysfunction | MRI spine (compressive lesion) |
| Acute intermittent porphyria | Abdominal pain, psychiatric symptoms, autonomic dysfunction, motor predominant neuropathy, dark urine | Urine ALA and PBG (elevated during attack) |
| Poliomyelitis / West Nile virus | Asymmetric flaccid paralysis, fever, anterior horn cell pattern, CSF pleocytosis | CSF (elevated WBC); viral PCR; MRI (anterior horn signal) |
| CIDP | Similar to GBS but progression >8 weeks, relapsing-remitting course, may respond to steroids | NCS/EMG (demyelinating); temporal course >8 weeks; steroid response |
| Critical illness myopathy/neuropathy | ICU setting, prolonged ventilation, steroid/neuromuscular blocker exposure | NCS/EMG; CK (elevated in myopathy); clinical context |
| Hypokalemia | Diffuse weakness, cardiac arrhythmia, normal reflexes or hyporeflexia | Serum potassium; ECG; rapid improvement with replacement |
| Conversion disorder (FND) | Non-physiologic weakness pattern, Hoover sign, give-way weakness, psychiatric history | Normal NCS/EMG; normal LP; clinical exam |
| Diphtheria | Pharyngeal membrane, palatal weakness, sensorimotor neuropathy weeks after infection | Throat culture; clinical history |
| HIV-associated neuropathy | Progressive, often sensory predominant; CSF pleocytosis distinguishes from GBS | HIV testing; CSF (WBC >50 suggests HIV, not classic GBS) |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Forced Vital Capacity (FVC) | STAT | STAT | ROUTINE | STAT | q4-6h in hospital (q2h if declining); q1-2h in ICU if concerning trend | FVC >20 mL/kg (approximately >1.5L for 75kg adult) | If FVC <20 mL/kg or declining >30% from baseline → elective intubation; transfer to ICU |
| Negative Inspiratory Force (NIF/MIP) | STAT | STAT | ROUTINE | STAT | q4-6h with FVC | NIF more negative than -30 cmH2O (e.g., -40 is better than -20) | If NIF weaker than -30 cmH2O → prepare for intubation |
| Peak Cough Flow | - | ROUTINE | - | ROUTINE | q4-6h with FVC | >270 L/min (effective cough) | Airway clearance interventions; suction; assisted cough |
| Single Breath Count | STAT | STAT | - | STAT | q4h (bedside screening) | Count to ≥20 on single breath | If <10-15 → declining respiratory function, correlate with FVC |
| Oxygen saturation (SpO2) | STAT | STAT | - | STAT | Continuous in ICU; q4h on floor | ≥94% | Late finding — do NOT rely on SpO2 alone; FVC is more sensitive |
| Blood pressure | STAT | STAT | - | STAT | q4h on floor; continuous in ICU | Stable; watch for lability (autonomic) | If BP lability (swings >20 mmHg): short-acting agents only; avoid long-acting antihypertensives; telemetry |
| Heart rate and rhythm (telemetry) | STAT | STAT | - | STAT | Continuous x 48h minimum; longer if autonomic symptoms | HR 60-100; sinus rhythm | Bradycardia: atropine ready; Tachycardia: volume, pain control; AV block: consider temporary pacing |
| Neurologic exam (strength, reflexes) | STAT | STAT | ROUTINE | STAT | q4-8h; Hughes GBS disability scale daily | Stable or improving | Worsening → repeat FVC/NIF; consider additional immunotherapy |
| Swallowing function | URGENT | STAT | ROUTINE | STAT | Daily assessment; formal SLP if bulbar symptoms | Safe oral intake | NPO if unsafe; NG or PEG for nutrition |
| Pain assessment (NRS 0-10) | STAT | STAT | ROUTINE | STAT | q4h with vitals | NRS <4 | Adjust pain regimen |
| Bowel function | - | ROUTINE | ROUTINE | ROUTINE | Daily | Regular bowel movements | Bowel program; avoid ileus (autonomic dysfunction) |
| Bladder function | - | ROUTINE | ROUTINE | ROUTINE | I/O monitoring; post-void residual if needed | Adequate output; PVR <200 mL | Bladder scan; intermittent catheterization if retention |
| Renal function (BUN, Cr) | - | ROUTINE | - | ROUTINE | Daily during IVIG; q48h otherwise | Stable creatinine | Hold IVIG if rising Cr; hydration |
| Sodium | - | ROUTINE | - | ROUTINE | Daily | Normal (135-145 mEq/L) | SIADH workup if <130; fluid restriction |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Mild GBS (ambulatory without assistance, Hughes 0-2), stable respiratory function (FVC >60% predicted), adequate pain control on oral medications, safe swallowing, reliable outpatient follow-up, family/caregiver support |
| Admit to floor (monitored bed preferred) | Any GBS requiring treatment; unable to ambulate independently; FVC 20-30 mL/kg with no downward trend; mild bulbar symptoms; needs IVIG or PLEX |
| Admit to ICU | FVC <20 mL/kg or declining rapidly; NIF weaker than -30 cmH2O; intubated or imminent intubation; autonomic instability (BP lability, arrhythmia); severe bulbar weakness with aspiration risk; unable to protect airway |
| Transfer to higher level of care | Need for PLEX not available on-site; need for ICU with neurology expertise; rapidly progressive course |
| Inpatient rehabilitation | Significant motor deficits (unable to walk independently; Hughes 3-4); able to participate in 3h/day therapy; medically stable |
| Skilled nursing facility | Unable to tolerate intensive rehabilitation; requires ongoing nursing care; severe deconditioning |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IVIG 0.4 g/kg/day x 5 days | Class I, Level A | [Dutch GBS Study Group, NEJM 1992](https://pubmed.ncbi.nlm.nih.gov/1552913/); [Cochrane Review, Hughes 2014](https://pubmed.ncbi.nlm.nih.gov/25238327/) |
| PLEX (5 exchanges) equivalent to IVIG | Class I, Level A | [French Cooperative Group, Ann Neurol 1987](https://pubmed.ncbi.nlm.nih.gov/2893583/); North American GBS Study |
| IVIG + PLEX combination NOT superior to either alone | Class I, Level A | [PE/Sandoglobulin GBS Trial Group, Lancet 1997](https://pubmed.ncbi.nlm.nih.gov/9014908/) |
| Corticosteroids alone NOT effective for GBS | Class I, Level A | [Cochrane Review, Hughes 2016](https://pubmed.ncbi.nlm.nih.gov/27775812/) |
| IVIG + IV methylprednisolone may shorten recovery (weak evidence) | Class IIb, Level B | [Dutch GBS Study Group, Lancet 2004](https://pubmed.ncbi.nlm.nih.gov/14738791/) |
| Bedside FVC and NIF for respiratory monitoring | Class I, Level B | [Lawn et al. Arch Neurol 2001](https://pubmed.ncbi.nlm.nih.gov/11405803/) |
| 20/30/40 rule for intubation | Class IIa, Level C | Expert consensus; [Wijdicks & Borel, Neurology 1998](https://pubmed.ncbi.nlm.nih.gov/9443451/) |
| Avoid succinylcholine in GBS | Class III (Harm) | Risk of hyperkalemia from denervated muscle |
| Neuropathic pain management (gabapentin, carbamazepine) | Class IIa, Level B | [Pandey et al. Anesth Analg 2002](https://pubmed.ncbi.nlm.nih.gov/12456446/); Cochrane Review |
| Early rehabilitation improves outcomes | Class I, Level B | [Khan & Amatya, Eur J Phys Rehabil Med 2012](https://pubmed.ncbi.nlm.nih.gov/22820829/); GBS-CIDP Foundation recommendations |
| DVT prophylaxis | Class I, Level C | Standard of care for immobilized patients |
| Anti-ganglioside antibodies (diagnostic, not required) | Class IIa, Level B | Diagnostic sensitivity varies by subtype |
| Brighton criteria for GBS diagnosis | Class IIa, Level C | [Brighton Collaboration, Vaccine 2011](https://pubmed.ncbi.nlm.nih.gov/20600491/) |
| IgA level before IVIG | Class I, Level C | Standard safety measure |
| LP with albuminocytologic dissociation | Class I, Level B | Classic diagnostic finding; may be normal in first week |

---

**APPENDIX: HUGHES GBS DISABILITY SCALE**

| Grade | Description |
|-------|-------------|
| 0 | Healthy |
| 1 | Minor symptoms or signs, able to run |
| 2 | Able to walk ≥10m without assistance but unable to run |
| 3 | Able to walk ≥10m with assistance (walker, cane, person) |
| 4 | Chairbound or bedbound |
| 5 | Requiring assisted ventilation |
| 6 | Dead |

**APPENDIX: BRIGHTON CRITERIA (DIAGNOSTIC CERTAINTY)**

| Level | Requirements |
|-------|-------------|
| Level 1 (Highest) | Bilateral flaccid weakness + decreased/absent reflexes + electrophysiology consistent + CSF protein elevated with WBC <50 + no alternative diagnosis |
| Level 2 | Bilateral flaccid weakness + decreased/absent reflexes + CSF or electrophysiology consistent + no alternative diagnosis |
| Level 3 | Bilateral flaccid weakness + decreased/absent reflexes + no alternative diagnosis |

**APPENDIX: IVIG INFUSION PROTOCOL (TYPICAL)**

| Step | Rate |
|------|------|
| Initial 30 min | 0.5 mL/kg/h |
| If tolerated, increase q30min | 1.0 → 2.0 → 3.0 → 4.0 mL/kg/h |
| Maximum rate | 4.0-8.0 mL/kg/h (product-specific) |
| Pre-medication | Acetaminophen 650 mg + diphenhydramine 25-50 mg PO 30 min before; hydration 500 mL NS |

**APPENDIX: 20/30/40 INTUBATION RULE**

| Parameter | Threshold for Intubation |
|-----------|-------------------------|
| FVC | <20 mL/kg |
| NIF (MIP) | Weaker than -30 cmH2O |
| FVC decline | >30% from baseline |
| Additional clinical signs | Inability to count to 20 on single breath, paradoxical breathing, use of accessory muscles, tachypnea >30, weak cough |
