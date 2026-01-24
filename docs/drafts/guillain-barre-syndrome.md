---
title: Guillain-Barré Syndrome
description: Acute inflammatory demyelinating polyradiculoneuropathy - evaluation, respiratory monitoring, IVIg/PLEX, and ICU management.
version: "1.0"
setting: ED, HOSP, ICU
status: draft
tags:
  - neuromuscular
  - emergency
  - weakness
  - neuropathy
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Guillain-Barré Syndrome

**VERSION:** 1.0
**CREATED:** January 24, 2026
**REVISED:** January 24, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Guillain-Barré Syndrome (GBS)

**ICD-10:** G61.0 (Guillain-Barré syndrome)

**SCOPE:** Evaluation and management of acute Guillain-Barré Syndrome in adults, including all major variants (AIDP, AMAN, AMSAN, Miller Fisher). Covers respiratory monitoring protocols, immunotherapy (IVIg and plasmapheresis), autonomic dysfunction management, and ICU care. Excludes CIDP (chronic inflammatory demyelinating polyneuropathy) and pediatric GBS.

**CLINICAL SYNONYMS:** Acute inflammatory demyelinating polyradiculoneuropathy (AIDP), Landry's ascending paralysis, acute motor axonal neuropathy (AMAN), acute motor-sensory axonal neuropathy (AMSAN), Miller Fisher syndrome (MFS)

---

**KEY CLINICAL FEATURES:**
- Acute onset ascending weakness (proximal and distal)
- Areflexia or hyporeflexia
- Sensory symptoms (paresthesias, pain) often precede weakness
- Antecedent infection 1-4 weeks prior (Campylobacter, CMV, EBV, Zika, COVID-19)
- Nadir typically reached within 2-4 weeks
- **Critical:** 20-30% require mechanical ventilation

**VARIANTS:**
| Variant | Features | Antibody |
|---------|----------|----------|
| AIDP | Classic ascending weakness, areflexia | — |
| AMAN | Pure motor, preserved reflexes early | Anti-GM1, anti-GD1a |
| AMSAN | Severe motor + sensory axonal | Anti-GM1 |
| Miller Fisher | Ophthalmoplegia, ataxia, areflexia | Anti-GQ1b (>90%) |

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

!!! danger "⚡ RESPIRATORY FAILURE WARNING"
    **30% of GBS patients require intubation.** Monitor FVC and NIF every 4-6 hours. See [20/30/40 Rule](#respiratory-monitoring-2030-40-rule) for intubation criteria.

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential | Baseline, infection screen | Normal or mild leukocytosis | STAT | STAT | — | STAT |
| CMP (BMP + LFTs) | Electrolytes, renal function for IVIg | Normal | STAT | STAT | — | STAT |
| Magnesium | Hypomagnesemia worsens weakness | >1.8 mg/dL | STAT | STAT | — | STAT |
| Phosphorus | Hypophosphatemia causes weakness | >2.5 mg/dL | STAT | STAT | — | STAT |
| ESR, CRP | Inflammatory markers | May be mildly elevated | STAT | ROUTINE | — | STAT |
| Urinalysis | UTI as trigger | Document | STAT | ROUTINE | — | STAT |
| Blood glucose | Hyperglycemia worsens outcomes | <180 mg/dL | STAT | STAT | — | STAT |
| TSH | Thyroid myopathy in differential | Normal | URGENT | ROUTINE | — | URGENT |
| CPK | Myopathy in differential | Normal or mildly elevated | URGENT | ROUTINE | — | URGENT |
| PT/INR, PTT | Pre-LP, pre-PLEX | Normal | URGENT | ROUTINE | — | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b) | Variant classification, prognosis | Document positivity | — | ROUTINE | — | ROUTINE |
| Campylobacter jejuni serology | Most common trigger | Document if positive | — | ROUTINE | — | ROUTINE |
| CMV IgM/IgG | Viral trigger | Document if positive | — | ROUTINE | — | ROUTINE |
| EBV panel | Viral trigger | Document if positive | — | ROUTINE | — | ROUTINE |
| Mycoplasma pneumoniae IgM | Bacterial trigger | Document if positive | — | ROUTINE | — | ROUTINE |
| HIV | HIV-associated GBS | Negative | — | ROUTINE | — | ROUTINE |
| Hepatitis B surface antigen | Pre-IVIg screening | Negative | — | URGENT | — | URGENT |
| Hepatitis C antibody | Pre-PLEX screening | Negative | — | URGENT | — | URGENT |
| COVID-19 PCR/antigen | COVID-associated GBS | Document | STAT | STAT | — | STAT |
| Quantitative immunoglobulins | IgA deficiency (IVIg contraindication) | IgA >7 mg/dL | — | URGENT | — | URGENT |
| Type and screen | Pre-PLEX | Available | — | URGENT | — | STAT |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Zika virus serology | Travel to endemic area | Negative | — | EXT | — | EXT |
| West Nile virus serology | Endemic area, summer months | Negative | — | EXT | — | EXT |
| Lyme serology | Endemic area, tick exposure | Negative | — | EXT | — | EXT |
| Porphyrins (urine) | Motor neuropathy with abdominal pain | Normal | — | EXT | — | EXT |
| Heavy metals (lead, arsenic, thallium) | Toxic neuropathy differential | Normal | — | EXT | — | EXT |
| Serum protein electrophoresis | Paraproteinemic neuropathy | Normal | — | EXT | — | EXT |
| Anti-acetylcholine receptor antibodies | MG in differential | Negative | — | EXT | — | EXT |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Chest X-ray | On admission | Aspiration, atelectasis | None | STAT | STAT | — | STAT |
| ECG | On admission | Autonomic dysfunction (arrhythmia) | None | STAT | STAT | — | STAT |
| Forced vital capacity (FVC) | Serial q4-6h | FVC >20 mL/kg (stable) | Facial weakness limiting seal | STAT | STAT | — | STAT |
| Negative inspiratory force (NIF) | Serial q4-6h | NIF more negative than -30 cmH2O | Facial weakness | STAT | STAT | — | STAT |
| Nerve conduction studies/EMG | Within 48-72 hours | Demyelination, conduction block | None | — | URGENT | — | URGENT |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| MRI spine with contrast | If diagnostic uncertainty | Nerve root enhancement (spinal roots) | Pacemaker, hemodynamic instability | — | ROUTINE | — | ROUTINE |
| MRI brain with contrast | Miller Fisher variant | Cranial nerve enhancement | Pacemaker | — | ROUTINE | — | ROUTINE |
| Swallow evaluation | If bulbar weakness | Aspiration risk | None | — | URGENT | — | URGENT |
| Echocardiogram | If autonomic instability | Takotsubo, cardiac dysfunction | None | — | ROUTINE | — | ROUTINE |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Repetitive nerve stimulation | If MG suspected | Normal (vs decrement in MG) | None | — | EXT | — | EXT |
| Autonomic function testing | Persistent dysautonomia | Abnormal heart rate variability | Unstable patient | — | EXT | — | EXT |

### LUMBAR PUNCTURE

**Indication:** Confirm diagnosis (albuminocytologic dissociation); exclude infection if febrile

**Timing:** URGENT; may be normal in first 48-72 hours (sensitivity improves after day 3-5)

**Volume Required:** 10-15 mL standard

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure | Exclude elevated ICP | Normal (10-20 cmH2O) | URGENT | STAT | — | STAT |
| Cell count (tubes 1 and 4) | Albuminocytologic dissociation | WBC <10 (usually <5) | URGENT | STAT | — | STAT |
| Protein | Elevated in GBS | Elevated (>45 mg/dL; often >100) | URGENT | STAT | — | STAT |
| Glucose | Exclude infection | Normal | URGENT | STAT | — | STAT |
| Gram stain and culture | Exclude bacterial meningitis | Negative | URGENT | STAT | — | STAT |
| Cytology | If malignancy suspected | Negative | — | ROUTINE | — | ROUTINE |
| Oligoclonal bands | Atypical cases | Usually negative (positive in <10%) | — | ROUTINE | — | ROUTINE |

**Special Handling:** Cell count within 1 hour. Refrigerate cytology.

**Contraindications:** Coagulopathy (INR >1.5, platelets <50K), skin infection at LP site.

**NOTE:** CSF may be normal in first 48-72 hours. Elevated protein with normal cell count (albuminocytologic dissociation) is classic but not required for diagnosis.

---

## 3. TREATMENT

**CRITICAL:** GBS is a neurological emergency. Early immunotherapy improves outcomes. Respiratory monitoring is paramount.

### Respiratory Monitoring: 20/30/40 Rule

**Intubation Criteria (any ONE of):**
- FVC <20 mL/kg (or <1 L in average adult)
- NIF weaker than -30 cmH2O (closer to 0)
- >30% decline in FVC from baseline
- Oxygen desaturation <92%
- Clinical respiratory distress

**Other Warning Signs:**
- Rapid progression (<7 days from onset to nadir)
- Bulbar dysfunction (dysarthria, dysphagia)
- Bilateral facial weakness
- Autonomic instability

### 3A. Acute/Emergent - Respiratory Support

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Supplemental oxygen | INH | Hypoxemia | 2-6 L/min NC; 15 L/min NRB :: INH :: PRN :: Titrate to O2 sat >94%; escalate to high-flow if needed | None | O2 sat, RR | STAT | STAT | — | STAT |
| Endotracheal intubation | — | Respiratory failure | N/A :: — :: :: Intubate if FVC <20 mL/kg, NIF >-30 cmH2O, or clinical deterioration; avoid succinylcholine (hyperkalemia risk) | — | ETT position, ventilator settings | STAT | STAT | — | STAT |
| Mechanical ventilation | — | Respiratory failure | N/A :: — :: :: Lung-protective ventilation; TV 6-8 mL/kg IBW; PEEP 5-8 cmH2O | — | ABG, ventilator parameters | — | — | — | STAT |

### 3B. Immunotherapy - First-line

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (immune globulin IV) - 5-day protocol | IV | Primary immunotherapy | 0.4 g/kg/day x 5 days :: IV :: daily x 5 days :: 0.4 g/kg/day IV for 5 days (total 2 g/kg); infuse slowly day 1 (start 0.5-1 mL/kg/hr, advance to max 4 mL/kg/hr) | IgA deficiency (<7 mg/dL) with anti-IgA antibodies; severe renal impairment | Renal function, headache, infusion reactions; pre-medicate with acetaminophen/diphenhydramine | — | STAT | — | STAT |
| IVIg (immune globulin IV) - 2-day protocol | IV | Primary immunotherapy | 1 g/kg/day x 2 days :: IV :: daily x 2 days :: 1 g/kg/day IV for 2 days (total 2 g/kg); alternative accelerated protocol; same total dose | IgA deficiency (<7 mg/dL) with anti-IgA antibodies; severe renal impairment | Renal function, headache, infusion reactions; higher daily dose may increase infusion reactions | — | STAT | — | STAT |
| Plasmapheresis (PLEX) | — | Primary immunotherapy | 5 exchanges over 1-2 weeks :: — :: QOD x 5 :: 5 exchanges (200-250 mL/kg per exchange) over 7-14 days; typically QOD | Hemodynamic instability; severe sepsis; IV access issues | BP, electrolytes (Ca, Mg, K), coagulation, fibrinogen | — | STAT | — | STAT |

**IVIg vs PLEX Selection:**
- **IVIg preferred:** Hemodynamic instability, autonomic dysfunction, difficult IV access
- **PLEX preferred:** IgA deficiency, severe renal disease, cost considerations
- **Efficacy:** Equivalent when started within 2-4 weeks of symptom onset
- **Do NOT combine:** IVIg + PLEX not more effective; PLEX removes IVIg

### 3C. Autonomic Dysfunction Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Normal saline | IV | Hypotension | 250 mL; 500 mL; 1000 mL :: IV :: bolus PRN :: 250-500 mL bolus for SBP <90; avoid overhydration | Heart failure | BP, I/O, JVD | STAT | STAT | — | STAT |
| Phenylephrine | IV | Refractory hypotension | 100-200 mcg bolus; 0.5-2 mcg/kg/min :: IV :: infusion :: Start 0.5 mcg/kg/min; titrate to MAP >65 | Severe bradycardia | Continuous BP, HR | — | — | — | STAT |
| Esmolol | IV | Hypertensive crisis | 500 mcg/kg load; 50-200 mcg/kg/min :: IV :: infusion :: Load 500 mcg/kg over 1 min, then 50-200 mcg/kg/min; short-acting preferred in GBS | Bradycardia, heart block, decompensated HF | HR, BP | — | — | — | STAT |
| Atropine | IV | Symptomatic bradycardia | 0.5 mg; 1 mg :: IV :: PRN :: 0.5-1 mg IV push for HR <50 with symptoms; may repeat q3-5min; max 3 mg | Tachycardia | HR, rhythm | STAT | STAT | — | STAT |
| Temporary pacing | — | Complete heart block | N/A :: — :: :: Transcutaneous or transvenous pacing for refractory bradycardia/asystole | — | Continuous telemetry | — | — | — | STAT |
| Fludrocortisone | PO | Orthostatic hypotension | 0.1 mg daily; 0.2 mg daily :: PO :: daily :: 0.1-0.2 mg PO daily for persistent orthostatic hypotension | Hypertension, heart failure | BP (supine and standing), edema, K+ | — | ROUTINE | — | ROUTINE |
| Midodrine | PO | Orthostatic hypotension | 2.5 mg TID; 5 mg TID; 10 mg TID :: PO :: TID :: Start 2.5-5 mg TID; max 10 mg TID; avoid evening dose | Supine hypertension, urinary retention | BP (supine and standing) | — | ROUTINE | — | ROUTINE |

### 3D. Symptomatic/Supportive Care

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Gabapentin | PO | Neuropathic pain | 300 mg qHS; 300 mg TID; 600 mg TID; 900 mg TID :: PO :: TID :: Start 300 mg qHS; titrate by 300 mg/day q1-3d; max 3600 mg/day in 3 divided doses | Severe renal impairment (adjust dose) | Sedation, dizziness; reduce dose if CrCl <60 | — | ROUTINE | — | ROUTINE |
| Pregabalin | PO | Neuropathic pain | 75 mg BID; 150 mg BID; 300 mg BID :: PO :: BID :: Start 75 mg BID; may increase to 150 mg BID after 1 week; max 600 mg/day | Severe renal impairment (adjust dose) | Sedation, edema, weight gain | — | ROUTINE | — | ROUTINE |
| Morphine | IV | Severe pain | 2 mg q4h PRN; 4 mg q4h PRN :: IV :: q4h PRN :: 2-4 mg IV q4h PRN for severe pain; use cautiously with respiratory compromise | Respiratory depression | RR, sedation, O2 sat | STAT | STAT | — | STAT |
| Enoxaparin | SC | DVT prophylaxis | 40 mg daily; 30 mg BID :: SC :: daily :: 40 mg SC daily (BMI <40) or 30 mg BID (BMI >40); hold if CrCl <30; **HOLD if LP planned within 12 hours** | Active bleeding, HIT, CrCl <30 (use UFH), pending LP | Platelet count, signs of bleeding | — | STAT | — | STAT |
| Heparin (UFH) | SC | DVT prophylaxis (renal impairment) | 5000 units q8h; 5000 units q12h :: SC :: q8-12h :: 5000 units SC q8-12h if CrCl <30; **HOLD if LP planned within 4-6 hours** | Active bleeding, HIT, pending LP | Platelet count, signs of bleeding | — | STAT | — | STAT |
| SCDs (sequential compression devices) | — | DVT prophylaxis | N/A :: — :: continuous :: Bilateral lower extremity SCDs; use in addition to pharmacologic prophylaxis | Acute DVT in that extremity | Skin integrity | STAT | STAT | — | STAT |
| Bisacodyl | PO/PR | Constipation (autonomic) | 10 mg daily; 10 mg suppository :: PO/PR :: daily PRN :: 10 mg PO or PR daily as needed | Bowel obstruction | Bowel movements | — | ROUTINE | — | ROUTINE |
| Polyethylene glycol | PO | Constipation (autonomic) | 17 g daily; 17 g BID :: PO :: daily-BID :: 17 g (1 capful) PO daily-BID; titrate to 1-2 BMs daily | Bowel obstruction | Bowel movements | — | ROUTINE | — | ROUTINE |
| Metoclopramide | IV/PO | Gastroparesis | 10 mg q6h AC :: IV/PO :: q6h AC :: 10 mg IV/PO before meals and at bedtime; max 40 mg/day; limit to 5 days | Parkinson disease, GI obstruction | EPS, tardive dyskinesia | — | ROUTINE | — | ROUTINE |
| Ondansetron | IV/PO | Nausea | 4 mg q6h PRN; 8 mg q8h PRN :: IV/PO :: q6h PRN :: 4-8 mg IV/PO q6-8h PRN | QT prolongation | QTc if repeated dosing | STAT | STAT | — | STAT |
| Acetaminophen | PO/IV | Fever, mild pain | 650 mg q6h; 1000 mg q6h :: PO/IV :: q6h :: 650-1000 mg PO/IV q6h; max 4 g/day (3 g if hepatic impairment) | Severe hepatic impairment | LFTs if prolonged use | STAT | STAT | — | STAT |

### 3E. Treatment of GBS Variants

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (Miller Fisher) | IV | Miller Fisher syndrome | 0.4 g/kg/day x 5 days :: IV :: daily x 5 days :: Same as standard GBS; benefit less clear for pure MFS without weakness | IgA deficiency | Renal function, infusion reactions | — | URGENT | — | URGENT |
| Observation only (MFS) | — | Pure MFS (mild) | N/A :: — :: :: Consider observation without immunotherapy for pure MFS with mild symptoms and no limb weakness | If weakness present, treat | Serial neuro exam, FVC | — | ROUTINE | — | ROUTINE |

### 3F. Refractory/Treatment Failure

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Second course IVIg | IV | Treatment-related fluctuation | 0.4 g/kg/day x 5 days :: IV :: daily x 5 days :: Consider if deterioration during/after IVIg or PLEX; typically 2-3 weeks after first course | IgA deficiency | Renal function | — | URGENT | — | URGENT |
| PLEX after IVIg failure | — | IVIg non-response | 5 exchanges over 1-2 weeks :: — :: QOD x 5 :: Consider if no improvement 2-4 weeks post-IVIg; wait at least 2 weeks after IVIg completion | Hemodynamic instability | BP, coagulation | — | URGENT | — | URGENT |

**Note:** Corticosteroids are NOT effective in GBS and should NOT be used as primary treatment. They do not improve outcomes and may delay recovery.

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | Indication | ED | HOSP | OPD | ICU |
|----------------|------------|:--:|:----:|:---:|:---:|
| Neurology consult | All suspected GBS | STAT | STAT | — | STAT |
| Pulmonology consult | Respiratory compromise | URGENT | URGENT | — | STAT |
| Critical care consult | FVC <30 mL/kg or declining | URGENT | STAT | — | STAT |
| Physical therapy consult | Mobility assessment, fall prevention | — | STAT | — | STAT |
| Occupational therapy consult | ADL assessment, adaptive equipment | — | URGENT | — | URGENT |
| Speech therapy consult | Bulbar weakness, dysphagia | — | URGENT | — | URGENT |
| Respiratory therapy | Airway clearance, ventilator management | STAT | STAT | — | STAT |
| Pain management consult | Refractory neuropathic pain | — | ROUTINE | — | ROUTINE |
| Physiatry/PM&R | Rehabilitation planning | — | ROUTINE | — | ROUTINE |
| Social work | Discharge planning, support resources | — | ROUTINE | — | ROUTINE |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return if worsening weakness or shortness of breath | STAT | — | STAT |
| Fall precautions due to weakness | STAT | STAT | STAT |
| Do not drive until cleared by neurology | STAT | STAT | STAT |
| Physical therapy exercises as prescribed | — | STAT | STAT |
| Expect gradual recovery over weeks to months | — | ROUTINE | ROUTINE |
| Report fevers, severe headache, or new symptoms | STAT | STAT | STAT |
| GBS Foundation resources (www.gbs-cidp.org) | — | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Aspiration precautions if bulbar weakness | STAT | STAT | — |
| DVT prevention: early mobilization when safe | — | STAT | — |
| Skin breakdown prevention: frequent repositioning | — | STAT | STAT |
| Bladder care: monitor for retention | — | STAT | — |
| Energy conservation techniques | — | ROUTINE | ROUTINE |
| Gradual return to activities as tolerated | — | — | ROUTINE |
| Avoid vaccinations during acute illness (discuss timing with neurologist for future) | — | ROUTINE | ROUTINE |

---

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Myasthenia gravis | Fatigable weakness, ptosis, diplopia; reflexes preserved | AChR/MuSK antibodies, repetitive nerve stimulation, edrophonium test |
| Transverse myelitis | Sensory level, bowel/bladder dysfunction early, UMN signs | MRI spine with contrast, CSF |
| Spinal cord compression | Sensory level, UMN signs below lesion, back pain | MRI spine emergent |
| Botulism | Descending paralysis, pupil involvement, GI symptoms | Stool/serum toxin assay, EMG (incremental response) |
| Poliomyelitis/West Nile | Asymmetric weakness, fever, CSF pleocytosis | CSF PCR, serology |
| Tick paralysis | Recent tick exposure, ascending paralysis | Physical exam (find tick), rapid improvement with tick removal |
| Critical illness polyneuropathy | ICU setting, sepsis, prolonged weakness | EMG/NCS, clinical context |
| Hypokalemic periodic paralysis | Episodic weakness, low K+ during attacks | Serum K+ during attack, genetic testing |
| Acute porphyria | Abdominal pain, psychiatric symptoms, motor neuropathy | Urine porphyrins, ALA, PBG |
| Heavy metal poisoning | Exposure history, other systemic symptoms | Heavy metal levels |
| Diphtheria | Pharyngitis, palatal weakness, cardiac involvement | Throat culture, toxin assay |
| HIV-associated neuropathy | Risk factors, may have CSF pleocytosis | HIV testing |
| CIDP | Chronic course (>8 weeks), relapsing | Clinical course, EMG/NCS, CSF |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Forced vital capacity (FVC) | q4-6h initially; q2h if declining | >20 mL/kg | Intubate if <20 mL/kg or >30% decline | STAT | STAT | — | STAT |
| Negative inspiratory force (NIF) | q4-6h initially; q2h if declining | More negative than -30 cmH2O | Intubate if weaker than -30 cmH2O | STAT | STAT | — | STAT |
| Oxygen saturation | Continuous | >94% | Supplement oxygen, consider intubation | STAT | STAT | — | STAT |
| Heart rate | Continuous | 60-100 bpm | Treat bradycardia <50 or tachy >120 | STAT | STAT | — | STAT |
| Blood pressure | q1-4h | SBP 100-160 | Treat hypo/hypertension | STAT | STAT | — | STAT |
| Neurological exam (strength) | q4-8h | Stability or improvement | Escalate care if worsening | STAT | STAT | ROUTINE | STAT |
| Swallow function | Daily if bulbar symptoms | Safe swallow | NPO, NG tube if unsafe | — | STAT | — | STAT |
| Urine output | q4-8h | >0.5 mL/kg/hr | Bladder scan, catheterize if needed | — | STAT | — | STAT |
| Renal function | Daily during IVIg | Cr stable | Hold IVIg, hydrate if rising | — | STAT | — | STAT |
| Skin integrity | q shift | Intact | Reposition, pressure relief | — | ROUTINE | — | ROUTINE |
| Bowel function | Daily | Regular BMs | Bowel regimen if constipated | — | ROUTINE | — | ROUTINE |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **ICU admission** | FVC <30 mL/kg; NIF weaker than -40 cmH2O; rapid progression; autonomic instability; bulbar dysfunction; need for intubation |
| **Step-down/telemetry** | Stable FVC >30 mL/kg; improving or stable exam; no autonomic instability; on telemetry monitoring |
| **General floor** | Mild weakness (ambulatory); stable FVC >40 mL/kg; no bulbar symptoms; no autonomic dysfunction |
| **Acute rehabilitation** | Medically stable; significant residual weakness requiring intensive therapy; FVC stable >25 mL/kg |
| **Discharge home** | Ambulatory or near-ambulatory; stable >48-72 hours; adequate home support; outpatient PT arranged; no respiratory compromise |
| **Skilled nursing facility** | Unable to participate in intensive rehab; requires ongoing nursing care; medically stable |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IVIg or PLEX equally effective for GBS | Class I, Level A | [Hughes et al. Cochrane 2014](https://pubmed.ncbi.nlm.nih.gov/25238327/) |
| IVIg 0.4 g/kg x 5 days standard dosing | Class I, Level A | [van der Meché et al. NEJM 1992](https://pubmed.ncbi.nlm.nih.gov/1557426/) |
| PLEX effective within 4 weeks of onset | Class I, Level A | [Raphaël et al. Cochrane 2012](https://pubmed.ncbi.nlm.nih.gov/22786476/) |
| Combined IVIg + PLEX not superior | Class I, Level A | [Plasma Exchange/Sandoglobulin GBS Trial Group 1997](https://pubmed.ncbi.nlm.nih.gov/9008066/) |
| Corticosteroids ineffective in GBS | Class I, Level A | [Hughes et al. Cochrane 2016](https://pubmed.ncbi.nlm.nih.gov/27749928/) |
| FVC and NIF for respiratory monitoring | Class II, Level B | [Lawn et al. Ann Neurol 2001](https://pubmed.ncbi.nlm.nih.gov/11456310/) |
| Anti-GQ1b associated with Miller Fisher | Class II, Level B | [Chiba et al. Ann Neurol 1992](https://pubmed.ncbi.nlm.nih.gov/1637140/) |
| Campylobacter most common antecedent | Class II, Level B | [Jacobs et al. Neurology 1998](https://pubmed.ncbi.nlm.nih.gov/9710014/) |
| Early IVIg (within 2 weeks) improves outcomes | Class II, Level B | [van Koningsveld et al. Lancet Neurol 2004](https://pubmed.ncbi.nlm.nih.gov/15261607/) |
| 20/30/40 rule for intubation | Class III, Level C | [Wijdicks & Lawn. Neurology 1999](https://pubmed.ncbi.nlm.nih.gov/10591488/) |

---

## CHANGE LOG

**v1.0 (January 24, 2026)**
- Initial template creation
- Includes all GBS variants (AIDP, AMAN, AMSAN, Miller Fisher)
- Structured dosing format for immunotherapy and supportive care
- Respiratory monitoring protocol with 20/30/40 rule
- Autonomic dysfunction management
- DVT prophylaxis and supportive care

---

## APPENDIX A: Erasmus GBS Respiratory Insufficiency Score (EGRIS)

**Predicts need for mechanical ventilation within 1 week of admission**

| Parameter | Points |
|-----------|--------|
| **Days from onset to admission** | |
| >7 days | 0 |
| 4-7 days | 1 |
| ≤3 days | 2 |
| **Facial and/or bulbar weakness at admission** | |
| Absent | 0 |
| Present | 1 |
| **MRC sum score at admission** | |
| 60-51 | 0 |
| 50-41 | 1 |
| 40-31 | 2 |
| 30-21 | 3 |
| ≤20 | 4 |

**Interpretation:**
| EGRIS Score | Risk of MV |
|-------------|------------|
| 0-2 | Low (4%) |
| 3-4 | Intermediate (24%) |
| 5-7 | High (65%) |

**MRC Sum Score:** Sum of MRC grades (0-5) for 6 muscle groups bilaterally: shoulder abduction, elbow flexion, wrist extension, hip flexion, knee extension, ankle dorsiflexion. Maximum = 60.

---

## APPENDIX B: Hughes GBS Disability Scale

| Grade | Description |
|-------|-------------|
| 0 | Healthy |
| 1 | Minor symptoms or signs, able to run |
| 2 | Able to walk 10 meters without assistance but unable to run |
| 3 | Able to walk 10 meters with assistance (walker, cane, or support) |
| 4 | Bed-bound or chair-bound (unable to walk) |
| 5 | Requiring assisted ventilation |
| 6 | Death |

**Clinical Use:** Document at admission and serially to track progression/recovery. Grade ≥3 typically warrants immunotherapy.

---

## APPENDIX C: IVIg Administration Protocol

**Pre-treatment checklist:**
- [ ] Check IgA level (deficiency is contraindication)
- [ ] Document renal function (Cr, BUN)
- [ ] Assess hydration status
- [ ] Verify no recent live vaccines (wait 3 months post-IVIg)

**Infusion protocol:**
1. **Day 1:** Start at 0.5-1 mL/kg/hr for first 30 minutes
2. If tolerated, increase to 2 mL/kg/hr for 30 minutes
3. If tolerated, increase to 4 mL/kg/hr (max rate)
4. **Days 2-5:** Can start at higher rate if day 1 tolerated

**Premedication:**
- Acetaminophen 650-1000 mg PO
- Diphenhydramine 25-50 mg PO or IV
- Consider hydration with NS 250-500 mL pre-infusion

**Common reactions and management:**
| Reaction | Management |
|----------|------------|
| Headache | Slow infusion, acetaminophen, consider IVIg-induced aseptic meningitis if severe |
| Flushing, chills | Slow or pause infusion, acetaminophen, diphenhydramine |
| Hypertension | Slow infusion, monitor; usually transient |
| Nausea | Ondansetron 4 mg IV |
| Anaphylaxis (rare) | Stop infusion, epinephrine, supportive care |
| Renal dysfunction | Monitor Cr daily; hydrate; consider PLEX instead |

**Post-infusion:**
- Monitor for delayed reactions (headache, rash) for 24 hours
- Recheck renal function 24-48 hours after completion
