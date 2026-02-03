---
title: "Neuromuscular Respiratory Failure"
description: "Clinical decision support for neuromuscular respiratory failure diagnosis and management"
version: "1.0"
setting: "HOSP, OPD, ICU"
status: approved
tags:
  - epilepsy
  - cerebrovascular
  - headache
  - demyelinating
  - infectious
---

# Neuromuscular Respiratory Failure

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Neuromuscular Respiratory Failure

**ICD-10:** G70.00 (Myasthenia gravis without exacerbation), G70.01 (Myasthenia gravis with exacerbation), G61.0 (Guillain-Barré syndrome), J96.00 (Acute respiratory failure, unspecified hypoxia/hypercapnia), G71.0 (Muscular dystrophy), G12.21 (Amyotrophic lateral sclerosis)

**CPT CODES:** 82803 (Arterial blood gas (ABG)), 85025 (CBC with differential), 80053 (CMP (BMP + LFTs)), 83735 (Magnesium), 84100 (Phosphorus), 82330 (Calcium (ionized)), 86235 (Acetylcholine receptor (AChR) antibodies), 84443 (TSH), 84145 (Procalcitonin), 86255 (Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b)), 95937 (Repetitive nerve stimulation (RNS)), 95872 (Single-fiber EMG (SFEMG)), 95907-95913 (Nerve conduction studies), 71260 (CT chest (with contrast)), 71046 (Chest X-ray), 94010 (Bedside spirometry (FVC)), 94799 (Negative inspiratory force (NIF/MIP)), 93000 (ECG (12-lead)), 93306 (Echocardiogram), 78816 (PET/CT), 62270 (LP), 96365 (IVIG (Intravenous Immunoglobulin)), 36514 (Plasma exchange (PLEX))

**SYNONYMS:** Neuromuscular respiratory failure, NMRF, respiratory failure from weakness, GBS respiratory failure, myasthenic respiratory failure, NIF less than 20, FVC less than 20, impending respiratory failure, neuromuscular ventilatory failure, ventilatory failure, diaphragmatic weakness

**SCOPE:** Emergency evaluation and management of respiratory failure from neuromuscular disorders in adults. Covers recognition of impending respiratory failure, monitoring parameters (FVC, NIF), indications for intubation, non-invasive ventilation (NIV) considerations, disease-specific treatments (myasthenia gravis crisis, GBS, ALS, muscular dystrophy, other myopathies), and weaning considerations. Excludes central causes of respiratory failure (brainstem stroke, sedative overdose) and primary pulmonary causes (pneumonia, ARDS, COPD exacerbation).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Arterial blood gas (ABG) (CPT 82803) | STAT | STAT | - | STAT | **CRITICAL**: Assess ventilation (PaCO2) and oxygenation (PaO2); hypercapnia (PaCO2 >45) indicates hypoventilation; respiratory acidosis = severe; PaO2/FiO2 ratio | Normal: pH 7.35-7.45, PaCO2 35-45, PaO2 >80; **Hypercapnia with respiratory acidosis = impending/current respiratory failure** — consider intubation |
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Infection (pneumonia as trigger or complication); baseline; anemia (reduces O2 carrying capacity) | Normal; leukocytosis → infection; anemia → correct |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolytes (K, Mg, Ca, Phos — all affect muscle function); renal function; glucose | Normal; hypokalemia, hypophosphatemia, hypomagnesemia, hypocalcemia can all worsen neuromuscular weakness |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia worsens neuromuscular junction transmission and muscle weakness | >2.0 mg/dL; replete if low |
| Phosphorus (CPT 84100) | STAT | STAT | ROUTINE | STAT | Hypophosphatemia causes profound muscle weakness including respiratory muscles | >2.5 mg/dL; replete if low (can cause respiratory failure at <1.0) |
| Calcium (ionized) (CPT 82330) | STAT | STAT | ROUTINE | STAT | Hypocalcemia increases neuromuscular excitability; hypercalcemia causes weakness | Normal ionized Ca |
| Acetylcholine receptor (AChR) antibodies (CPT 86235) | - | URGENT | ROUTINE | URGENT | **MG workup**: positive in 85% of generalized MG; 50% of ocular MG; confirms diagnosis | Positive = MG; negative does NOT exclude (check MuSK, LRP4) |
| Anti-MuSK antibodies (CPT 86235) | - | URGENT | ROUTINE | URGENT | If AChR negative but MG suspected clinically; MuSK-positive MG has distinct features (bulbar predominant, may not respond well to cholinesterase inhibitors) | Positive = MuSK MG |
| Anti-LRP4 antibodies | - | ROUTINE | ROUTINE | - | If both AChR and MuSK negative ("seronegative MG"); less commonly available | Positive = LRP4 MG (rare) |
| Creatine kinase (CK) | STAT | STAT | ROUTINE | STAT | Elevated in myopathies, muscular dystrophies; may be normal in MG, GBS, ALS | Normal in MG, GBS; elevated in myopathies, rhabdomyolysis; very high (>10,000) in inflammatory myopathies, dystrophies |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Thyroid dysfunction: hyperthyroidism worsens MG; hypothyroidism causes myopathy | Normal |
| Procalcitonin (CPT 84145) / CRP (CPT 86140) | STAT | STAT | - | STAT | Infection as trigger (pneumonia, UTI can precipitate MG crisis); distinguish infection from disease exacerbation | Normal; elevated → infection workup |
| Urine drug screen | STAT | - | - | STAT | Drugs affecting neuromuscular function; intoxication as mimicker | Negative |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Pyridostigmine level (if available) | - | ROUTINE | - | ROUTINE | Rarely available; assess for cholinergic crisis (too much pyridostigmine vs. myasthenic crisis) | Therapeutic range varies; clinical assessment more reliable |
| Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b) (CPT 86255) | - | URGENT | ROUTINE | URGENT | GBS workup; GQ1b positive in Miller Fisher syndrome | Positive supports GBS diagnosis; negative does NOT exclude |
| CSF analysis | - | URGENT | ROUTINE | - | GBS: albuminocytologic dissociation (elevated protein, normal cells — may not be present in first week); exclude infection | GBS: protein elevated (>45 mg/dL), WBC <10 (usually <5); may be normal early |
| Repetitive nerve stimulation (RNS) (CPT 95937) | - | URGENT | ROUTINE | - | **MG diagnosis**: decremental response at 3 Hz stimulation (>10% decrement) in proximal muscles | >10% decrement = neuromuscular junction defect (MG); no decrement does NOT exclude MG |
| Single-fiber EMG (SFEMG) (CPT 95872) | - | - | ROUTINE | - | **Most sensitive test for MG** (92-98%); increased jitter and blocking | Increased jitter = neuromuscular transmission defect |
| Nerve conduction studies (CPT 95907-95913) / EMG (CPT 95886) | - | URGENT | ROUTINE | URGENT | GBS: demyelinating pattern (prolonged F-waves, conduction block, temporal dispersion) or axonal (reduced amplitudes); ALS: widespread denervation; myopathy: myopathic units | GBS: demyelinating or axonal; ALS: diffuse denervation; myopathy: small, polyphasic MUPs |
| CT chest (with contrast) (CPT 71260) | - | URGENT | ROUTINE | - | **Thymoma screening in MG**: 10-15% of MG patients have thymoma; all MG patients need chest imaging | Thymoma (anterior mediastinal mass); thymic hyperplasia; normal thymus |
| Anti-striational (anti-titin, anti-RyR) antibodies | - | ROUTINE | ROUTINE | - | Associated with thymoma in MG; may indicate need for more aggressive thymoma search | Positive in older MG patients and thymoma-associated MG |
| Paraneoplastic antibody panel (CPT 86255) | - | ROUTINE | ROUTINE | - | Paraneoplastic neuromuscular syndromes (LEMS with anti-VGCC and small cell lung cancer); myositis with malignancy | Anti-VGCC (LEMS); anti-Hu, anti-CV2 (paraneoplastic) |
| Anti-VGCC antibodies | - | URGENT | ROUTINE | - | Lambert-Eaton myasthenic syndrome (LEMS); associated with SCLC in 50-60% | Positive = LEMS (check for underlying malignancy) |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Muscle biopsy | - | - | EXT | - | Inflammatory myopathy (dermatomyositis, polymyositis); muscular dystrophy; congenital myopathy | Inflammatory infiltrate; dystrophic changes; structural abnormalities |
| Genetic testing (muscular dystrophy panel) | - | - | EXT | - | Suspected hereditary myopathy/dystrophy; known family history; young patient with progressive weakness | Specific mutations (dystrophin, FSHD, myotonic dystrophy, etc.) |
| Myositis-specific antibodies (Jo-1, Mi-2, SRP, MDA5, etc.) | - | ROUTINE | ROUTINE | - | Inflammatory myopathy workup | Specific antibodies guide diagnosis and prognosis |
| Edrophonium (Tensilon) test | - | EXT | EXT | - | Rarely done now (replaced by serologic testing and SFEMG); bedside MG test; risk of cholinergic crisis; atropine must be at bedside | Transient improvement = positive (MG); false positives/negatives occur |
| Ice pack test | - | URGENT | ROUTINE | URGENT | Bedside test for ocular MG; apply ice pack to closed eyelid for 2 min; improvement in ptosis suggests MG | Improvement = positive; negative does NOT exclude |
| Spirometry with flow-volume loop | - | URGENT | ROUTINE | URGENT | Upper airway obstruction pattern (variable extrathoracic obstruction in vocal cord weakness); restrictive pattern in neuromuscular disease | Restrictive pattern; flattened inspiratory loop suggests extrathoracic obstruction |
| Polysomnography | - | - | ROUTINE | - | Sleep-disordered breathing in neuromuscular disease; nocturnal hypoventilation; assess need for nocturnal NIV | Hypoventilation; desaturations; REM-related hypopneas |
| Pulmonary function tests (full) | - | - | ROUTINE | - | Baseline and monitoring in chronic neuromuscular disease; FVC, MIP, MEP, SNIP | FVC; supine vs. upright FVC (>20% drop suggests diaphragm weakness) |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Chest X-ray (CPT 71046) | STAT | STAT | - | STAT | Immediate; assess for aspiration, pneumonia (trigger for crisis), atelectasis, elevated hemidiaphragm | Aspiration pneumonia; atelectasis (from weak cough); elevated hemidiaphragm (diaphragm weakness); anterior mediastinal mass (thymoma) | None |
| Bedside spirometry (FVC) (CPT 94010) | STAT | STAT | ROUTINE | STAT | **CRITICAL: q4-6h in unstable patients; q1-2h if rapidly declining**; most important monitoring parameter | FVC >20 mL/kg = adequate; FVC <15-20 mL/kg = consider intubation; FVC declining >30% from baseline = concerning | Patient cooperation required; cannot perform if intubated (use ventilator parameters) |
| Negative inspiratory force (NIF/MIP) (CPT 94799) | STAT | STAT | ROUTINE | STAT | **CRITICAL: Assess inspiratory muscle strength**; complement to FVC; easier for fatigued patients | NIF < -30 cm H2O = adequate; NIF > -20 to -25 cm H2O (less negative) = weak, consider intubation | Patient cooperation |
| Maximum expiratory pressure (MEP) | - | URGENT | ROUTINE | STAT | Assess cough strength; correlates with ability to clear secretions | MEP <40 cm H2O = weak cough; aspiration risk |
| ABG (arterial blood gas) (CPT 82803) | STAT | STAT | - | STAT | Assess ventilation and oxygenation; hypercapnia is late sign | PaCO2 >45 = hypoventilation; rising PaCO2 is ominous; PaO2 <60 = hypoxemia |
| ECG (12-lead) (CPT 93000) | STAT | STAT | - | STAT | Arrhythmia from autonomic dysfunction (GBS); cardiac involvement in muscular dystrophies; baseline for IVIG/PLEX | Arrhythmia; conduction abnormalities; cardiomyopathy (DMD, LGMD) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT chest with contrast (CPT 71260) | - | URGENT | ROUTINE | - | Within 24-48h for MG; thymoma screening; all newly diagnosed generalized MG | Thymoma (anterior mediastinal mass); thymic hyperplasia | Contrast allergy; renal impairment |
| MRI chest (non-contrast) | - | - | ROUTINE | - | If CT contraindicated or additional characterization needed | Thymoma; thymic abnormality | MRI-incompatible implants |
| Echocardiogram (CPT 93306) | - | URGENT | ROUTINE | URGENT | Cardiomyopathy screening in muscular dystrophies (DMD, BMD, LGMD2I, myotonic dystrophy); autonomic dysfunction in GBS; baseline before IVIG | Cardiomyopathy; reduced EF; conduction abnormalities (perform ECG first) | None |
| Diaphragm ultrasound | - | URGENT | ROUTINE | URGENT | Assess diaphragm excursion and thickness; non-invasive diaphragm function assessment; bedside | Reduced diaphragm excursion (<1.5 cm during tidal breathing, <4 cm during deep breath); paradoxical motion = diaphragm paralysis | Operator-dependent; obesity may limit views |
| CT angiography (pulmonary) | - | URGENT | - | URGENT | If pulmonary embolism suspected (immobile patients at high VTE risk) | PE | Contrast allergy; renal impairment |
| PET/CT (CPT 78816) | - | - | ROUTINE | - | If LEMS diagnosed to search for underlying malignancy (SCLC in 50-60%) | Lung mass; lymphadenopathy; occult malignancy | Uncontrolled diabetes |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Phrenic nerve conduction study | - | - | ROUTINE | - | Assess phrenic nerve function; bilateral phrenic neuropathy as cause of respiratory failure | Absent or reduced phrenic CMAP = phrenic neuropathy; prolonged latency | Pacemaker (relative) |
| Fluoroscopic sniff test | - | - | ROUTINE | - | Diaphragm function; "sniff test" — paradoxical upward diaphragm motion with sniff = paralysis | Paradoxical motion = diaphragm paralysis | Radiation exposure; pregnancy |
| Transdiaphragmatic pressure (Pdi) | - | - | EXT | - | Gold standard for diaphragm strength; requires esophageal and gastric balloon catheters; specialized centers | Reduced Pdi = diaphragm weakness | Invasive; specialized equipment |
| Polysomnography with capnography | - | - | ROUTINE | - | Nocturnal hypoventilation assessment; sleep-disordered breathing; guide NIV | Nocturnal hypoventilation (elevated PtcCO2); desaturations; REM-related events | Sleep lab availability |

### Lumbar Puncture

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP (CPT 62270) with CSF analysis | - | URGENT | ROUTINE | - | GBS diagnosis (albuminocytologic dissociation); may be normal in first week; NOT typically needed for MG diagnosis | GBS: elevated protein (often >100 mg/dL after first week), normal WBC (<10, usually <5); cytoalbuminous dissociation | Coagulopathy; skin infection at LP site; elevated ICP |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Airway assessment and monitoring** | - | - | 20 mL/kg :: - :: - :: **"20/30/40 Rule":** FVC <20 mL/kg, NIF > -30 cm H2O (less negative), MEP <40 cm H2O = HIGH RISK for respiratory failure; monitor q2-4h (or more frequently if declining); **INTUBATION THRESHOLD:** FVC <15-20 mL/kg, NIF > -20 to -25 cm H2O, rising PaCO2, or clinical distress | - | NMD respiratory failure is often predictable by serial FVC/NIF; intubate BEFORE crisis (controlled intubation is safer); ABG abnormalities are LATE signs | STAT | STAT | - | STAT |
| **Elective intubation (if criteria met)** | - | - | 15-20 mL/kg :: - :: - :: **Indications:** FVC <15-20 mL/kg (or <1 L); NIF > -20 to -25 cm H2O; PaCO2 rising or >50; clinical respiratory distress; inability to clear secretions; aspiration; fatigue; **RSI considerations:** AVOID succinylcholine in myopathies/muscular dystrophy (hyperkalemia), MG (resistance); use rocuronium (may need reduced dose in MG); can use sugammadex for reversal | - | Elective intubation is safer than emergent; neuromuscular patients are difficult to bag-mask ventilate; have difficult airway equipment ready; avoid neuromuscular blockers post-intubation if possible | STAT | STAT | - | STAT |
| **Non-invasive ventilation (NIV)** | - | - | **ROLE IS LIMITED IN ACUTE NMD RESPIRATORY FAILURE**; may be considered as bridge in: stable patients with nocturnal hypoventilation, mild hypercapnia without distress, secretion clearance ability preserved, no aspiration risk, patient can protect airway; **AVOID NIV if:** Bulbar dysfunction (aspiration risk), unable to clear secretions, severe hypercapnia (PaCO2 >60), acidosis, rapid decline, altered mental status | - | NIV (BiPAP) has lower threshold for failure in neuromuscular disease than COPD/CHF; bulbar weakness increases aspiration risk; low threshold for intubation; useful for chronic nocturnal hypoventilation | STAT | STAT | ROUTINE | STAT |
| **Supplemental oxygen** | - | - | 96% :: - :: - :: **Use CAUTIOUSLY**: Oxygen can mask hypoventilation (hypercapnia develops before desaturation); may eliminate hypoxic drive (though less relevant in NMD than COPD); titrate to SpO2 92-96%; **If hypoxemic + hypercapnic:** This indicates severe failure — intubate, do NOT rely on oxygen alone | - | Hypoxemia is a late finding in pure neuromuscular hypoventilation; if hypoxemic, consider aspiration, atelectasis, or imminent failure | STAT | STAT | - | STAT |
| **Secretion management** | - | - | Weak cough = poor secretion clearance; **Techniques:** Assisted cough (abdominal thrust during cough); mechanical insufflation-exsufflation (CoughAssist) — pressures +40/-40 cm H2O; aggressive pulmonary toilet; chest physiotherapy; suction PRN; **If unable to clear secretions:** Intubate | - | Aspiration pneumonia is leading cause of death in chronic NMD; weak cough (MEP <40) = high risk; mechanical cough assist is underutilized and highly effective | STAT | STAT | - | STAT |
| **Stop/avoid precipitating medications** | IV | - | **MG crisis precipitants (AVOID):** Aminoglycosides (gentamicin, tobramycin), fluoroquinolones (ciprofloxacin, levofloxacin — less risky but still caution), macrolides (azithromycin, erythromycin), beta-blockers, magnesium (IV), neuromuscular blockers, D-penicillamine, interferon-alpha, checkpoint inhibitors (nivolumab, pembrolizumab); **Full list in Appendix** | - | Many medications can worsen neuromuscular transmission; careful medication review essential; see comprehensive list in appendix | STAT | STAT | ROUTINE | STAT |
| **DVT prophylaxis** | SC | - | 40 mg :: SC :: daily :: SCDs immediately; pharmacologic prophylaxis (enoxaparin 40 mg SQ daily) once stable; immobile patients at very high VTE risk | - | High VTE risk in paralyzed/weak patients; balance with IVIG timing (hold anticoagulation during IVIG infusion in some protocols) | STAT | STAT | - | STAT |
| **Aspiration precautions** | - | - | HOB elevated 30-45°; NPO if significant bulbar weakness; speech-language pathology evaluation; modified diet or enteral feeding if prolonged weakness | - | Aspiration pneumonia is major complication; bulbar weakness (dysphagia, weak cough, voice changes) = high risk | STAT | STAT | ROUTINE | STAT |

### 3B. Disease-Specific Treatment

#### MYASTHENIA GRAVIS CRISIS

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **IVIG (Intravenous Immunoglobulin)** (CPT 96365) | IV | - | 2 g/kg :: - :: daily x 5 days :: **First-line for MG crisis (with PLEX):** 2 g/kg total divided over 2-5 days (400 mg/kg/day x 5 days OR 1 g/kg/day x 2 days); **Onset:** 2-5 days; **Duration:** 3-6 weeks; **Pre-treatment:** Check IgA (IgA deficiency = anaphylaxis risk); renal function; volume status | - | Efficacy equivalent to PLEX (RCTs); easier logistics than PLEX; side effects: headache (aseptic meningitis), renal failure (sucrose-containing products), thrombosis, hemolysis; slower onset than PLEX | - | STAT | - | STAT |
| **Plasma exchange (PLEX)** (CPT 36514) | - | - | **First-line for MG crisis (with IVIG):** 5-7 exchanges over 10-14 days (1-1.5 plasma volumes per exchange; typically 3-4 L); **Onset:** Faster than IVIG (improvement may begin after 2-3 exchanges); requires large-bore central venous access; **Caution:** Hypotension, citrate toxicity (hypocalcemia), infection | - | May work faster than IVIG; useful if rapid response needed; RCT showed PLEX and IVIG equivalent in MG exacerbation; PLEX preferred if IVIG contraindicated (IgA deficiency, renal failure) | - | STAT | - | STAT |
| **HOLD pyridostigmine (cholinesterase inhibitors)** | - | - | **In intubated MG crisis patients:** STOP pyridostigmine while intubated; excessive secretions worsen pulmonary toilet; cannot distinguish myasthenic from cholinergic crisis if on pyridostigmine; **Resume cautiously when extubation nearing** | - | Pyridostigmine increases secretions; in intubated patient, secretions worsen; hold until preparing for extubation; some restart at lower dose (30 mg q6h) and titrate | STAT | STAT | - | STAT |
| **Corticosteroids (delayed initiation)** | IV | - | 10-20 mg :: IV :: daily :: **CAUTION: Steroids can cause TRANSIENT WORSENING in MG (up to 50% of patients)**; **In crisis:** Start AFTER IVIG/PLEX initiated and patient stabilizing (days 3-5 or later); do NOT start steroids as initial therapy in crisis; **Protocol:** Prednisone 10-20 mg daily, increase by 10 mg every 3-5 days to 1 mg/kg/day (max 60-80 mg); OR IV methylprednisolone 1g daily x 3-5 days then oral | - | Steroids are maintenance therapy but can worsen MG acutely ("steroid dip"); always start with IVIG or PLEX first in crisis; steroid-sparing agents (azathioprine, mycophenolate) for long-term | - | URGENT | ROUTINE | URGENT |
| **Treat precipitant** | - | - | **Infection:** Most common trigger; treat aggressively but AVOID contraindicated antibiotics (see list); **Medication-induced:** Stop offending drug; **Surgery/anesthesia:** Stress can trigger crisis; **Tapering immunosuppression:** Restart or increase | - | 30-40% of MG crises have identifiable trigger; treating trigger may hasten recovery | STAT | STAT | - | STAT |

#### GUILLAIN-BARRÉ SYNDROME (GBS)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **IVIG** (CPT 96365) | - | - | 2 g/kg :: - :: daily x 5 days :: **First-line for GBS:** 2 g/kg total over 5 days (400 mg/kg/day x 5 days); start within 2-4 weeks of symptom onset for best efficacy; **Efficacy:** Equivalent to PLEX; faster recovery; fewer complications; **Onset:** Days to 1-2 weeks | - | RCTs show IVIG = PLEX; IVIG preferred due to availability and easier administration; start as soon as diagnosis confirmed (or highly likely); do NOT delay for CSF/EMG confirmation | - | STAT | - | STAT |
| **Plasma exchange (PLEX)** (CPT 36514) | - | - | 200-250 mL/kg :: - :: - :: **Alternative to IVIG:** 5 exchanges over 1-2 weeks (200-250 mL/kg total); start within 2-4 weeks of onset; **Consider PLEX if:** IVIG contraindicated; IVIG failure; severe/refractory | - | PLEX and IVIG equivalent; do NOT combine (no added benefit, more complications); PLEX if renal failure (IVIG risk) | - | STAT | - | STAT |
| **Corticosteroids — NOT effective in GBS** | - | - | **Do NOT use steroids for GBS**; no benefit; may cause harm | - | Multiple RCTs: steroids do NOT improve GBS outcomes; may delay recovery | - | - | - | - |
| **Autonomic monitoring** | - | - | 70% :: - :: - :: **GBS has significant autonomic dysfunction (up to 70%):** Cardiac monitoring (arrhythmias, heart block); BP monitoring (labile — hypertension and hypotension); ileus; urinary retention; treat arrhythmias; short-acting antihypertensives (avoid long-acting due to swings); pacing if bradycardia | - | Autonomic death is second leading cause of GBS mortality after respiratory failure; close cardiac monitoring; avoid medications that worsen autonomic dysfunction | - | STAT | - | STAT |
| **Pain management** | PO | - | 300 mg :: PO :: TID :: Pain in GBS is common (60-90%) and often severe; neuropathic pain; back pain; radicular pain; **Treatment:** Gabapentin 300 mg TID → titrate; pregabalin; opioids PRN; AVOID NSAIDs if renal concerns | - | Pain can be as debilitating as weakness; multimodal approach; gabapentinoids first-line | - | STAT | ROUTINE | STAT |

#### ALS / MOTOR NEURON DISEASE

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Goals of care discussion** | - | - | **CRITICAL:** ALS is progressive and fatal; respiratory failure is end-stage; discuss intubation, tracheostomy, long-term mechanical ventilation BEFORE crisis; many ALS patients choose comfort care / no intubation; **Advance directive** should be documented | - | Intubation in ALS often leads to chronic ventilator dependence (cannot wean); tracheostomy and home ventilation is option for some but significantly impacts QoL; respect patient autonomy | - | URGENT | ROUTINE | URGENT |
| **Non-invasive ventilation (NIV)** | - | - | 50% :: - :: - :: **Standard of care for ALS respiratory insufficiency:** Start NIV when FVC <50% predicted or symptoms of nocturnal hypoventilation; prolongs survival (median 7-11 months) and improves QoL; **Settings:** BiPAP S/T mode; IPAP 10-20, EPAP 4-6; titrate to comfort; initially nocturnal → extended daytime use as disease progresses | - | Cochrane review: NIV improves survival and QoL in ALS (especially with limb-onset); bulbar patients benefit less but still benefit; no evidence for invasive ventilation superiority over NIV with experienced teams | - | URGENT | ROUTINE | URGENT |
| **Mechanical insufflation-exsufflation (CoughAssist)** | - | - | 270 L/min :: - :: daily :: All ALS patients with weak cough (PCF <270 L/min or MEP <60); reduces respiratory infections; can be used with NIV; **Settings:** +40/-40 cm H2O; 4-5 cycles; several times daily | - | Improves secretion clearance; reduces pneumonia; can prolong NIV effectiveness; underutilized | - | URGENT | ROUTINE | URGENT |
| **Riluzole** | PO | - | 50 mg :: PO :: BID :: 50 mg PO BID; modestly prolongs survival (~2-3 months); neuroprotective; continue unless intolerant | - | Only FDA-approved disease-modifying drug for ALS with survival benefit (though modest); continue through respiratory failure unless goals of care dictate otherwise | - | ROUTINE | ROUTINE | - |
| **Edaravone (Radicava)** | IV | - | IV infusion or oral formulation; may slow functional decline; expensive; used in early ALS | - | Recent approval; modest benefit in selected patients; often continued if started | - | - | ROUTINE | - |
| **Symptomatic treatment** | - | - | Sialorrhea (glycopyrrolate, atropine drops, botulinum toxin to salivary glands); thick secretions (guaifenesin, N-acetylcysteine, hydration); pseudobulbar affect (dextromethorphan/quinidine); spasticity (baclofen, tizanidine); pain; depression | - | Palliative symptom management is cornerstone of ALS care; multidisciplinary team essential | - | ROUTINE | ROUTINE | STAT |
| **Comfort-focused care / Palliative care** | IV | - | 2-5 mg :: IV :: PRN :: If patient declines intubation or chronic mechanical ventilation; opioids for dyspnea (morphine 2-5 mg IV/SQ q2-4h PRN — does NOT hasten death and relieves suffering); anxiolytics (lorazepam); comfort measures; hospice referral | - | Dyspnea is the most distressing symptom at end of life; opioids are safe and effective; do not withhold for fear of "hastening death" | - | URGENT | ROUTINE | URGENT |

#### MUSCULAR DYSTROPHY / MYOPATHY

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Treat underlying cause (if treatable)** | - | - | 1 mg/kg :: - :: - :: **Inflammatory myopathy:** Corticosteroids (prednisone 1 mg/kg/day) + steroid-sparing agent (methotrexate, azathioprine, IVIG for dermatomyositis); **Hypothyroid myopathy:** Thyroid replacement; **Drug-induced myopathy (statins):** Stop drug; **Metabolic myopathy:** Specific treatment (enzyme replacement for Pompe disease) | - | Many myopathies are treatable; identify and treat cause; inflammatory myopathies are steroid-responsive | - | STAT | ROUTINE | STAT |
| **Nocturnal NIV** | - | - | 50% :: - :: - :: Chronic respiratory insufficiency in muscular dystrophy (DMD, BMD, LGMD, myotonic dystrophy); start when FVC <50%, symptoms, or nocturnal hypoventilation on PSG; prolongs survival in DMD | - | NIV is standard of care for chronic respiratory failure in MD; delays tracheostomy; improves survival and QoL | - | URGENT | ROUTINE | URGENT |
| **CoughAssist / Secretion management** | - | - | Same as ALS; weak cough universal in advanced MD; prevents pneumonia | - | Critical for preventing respiratory infections | - | URGENT | ROUTINE | URGENT |
| **Cardiac monitoring (DMD, BMD, LGMD2I, myotonic DM)** | - | - | Cardiomyopathy is common and can cause death; annual echocardiogram; ACE inhibitors / beta-blockers for cardiomyopathy; antiarrhythmics / pacemaker / ICD as indicated | - | Cardiac disease is leading cause of death in some muscular dystrophies; proactive cardiac management essential | - | STAT | ROUTINE | STAT |
| **Avoid succinylcholine** | - | - | **Absolute contraindication in muscular dystrophy and most myopathies**: Hyperkalemic cardiac arrest; use rocuronium (with sugammadex available for reversal) | - | Succinylcholine causes massive K+ release from dystrophic muscle; fatal hyperkalemia | STAT | STAT | - | STAT |

### 3C. Ventilator Management and Weaning

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Initial ventilator settings** | - | - | 6-8 mL/kg :: - :: - :: **Mode:** Volume-controlled (AC/VC) or Pressure-support (PS) during weaning; **Tidal volume:** 6-8 mL/kg IBW (lung-protective); **Rate:** 12-16 to achieve adequate minute ventilation; **PEEP:** 5 (higher if atelectasis or hypoxemia); **FiO2:** Titrate to SpO2 92-96%; **I:E ratio:** 1:2 or 1:3; avoid breath-stacking | - | NMD patients generally have healthy lungs; lung-protective ventilation still applies; goal is to support ventilation while disease-specific treatment works | - | STAT | - | STAT |
| **Weaning from mechanical ventilation** | - | - | 15 mL/kg :: - :: - :: **NMD weaning is often prolonged:** Disease-specific treatment must take effect (MG: IVIG/PLEX effect in 3-7 days; GBS: weeks); **Weaning trial criteria:** FVC >15 mL/kg; NIF < -25 cm H2O; adequate cough; secretions manageable; underlying disease improving; **SBT (spontaneous breathing trial):** T-piece or low PS (5-8 cm H2O) x 30-120 min; assess for fatigue, tachypnea, hypercapnia | - | Premature extubation leads to re-intubation; NMD patients may need longer ventilation than other ICU patients; patience; daily SBT when criteria met | - | ROUTINE | - | STAT |
| **Extubation criteria** | - | - | 15-20 mL/kg :: - :: - :: Pass SBT; FVC >15-20 mL/kg AND improving trajectory; NIF < -25 to -30 cm H2O; effective cough (able to clear secretions); alert and cooperative; bulbar function adequate (can swallow); no heavy sedation; consider cuff leak test | - | Higher threshold for extubation in NMD than general ICU patients; failed extubation is dangerous | - | - | - | STAT |
| **Tracheostomy (if prolonged ventilation anticipated)** | - | - | **Consider if:** Unable to wean after 2-3 weeks of optimal disease-specific treatment; ALS with decision for long-term ventilation; severe GBS; **Timing:** No firm consensus; typically discuss at 10-14 days if no progress; earlier in conditions with known prolonged course | - | Tracheostomy allows for weaning, reduces sedation needs, allows speech (with speaking valve), but has complications and care burden; goals of care discussion essential | - | ROUTINE | - | ROUTINE |
| **Post-extubation monitoring** | - | - | Close monitoring for 24-48h; serial FVC/NIF; watch for fatigue, stridor; have reintubation equipment ready; consider prophylactic NIV post-extubation in borderline cases | - | Re-intubation rates higher in NMD; close monitoring; low threshold for NIV support post-extubation | - | - | - | STAT |

### 3D. Medications to AVOID in Neuromuscular Disease

| Medication Class | Examples | Risk | Safer Alternative |
|-----------------|----------|------|-------------------|
| **Aminoglycosides** | Gentamicin, tobramycin, amikacin, streptomycin | Neuromuscular blockade; worsen MG, GBS | Beta-lactams, fluoroquinolones (with caution) |
| **Fluoroquinolones** | Ciprofloxacin, levofloxacin, moxifloxacin | Associated with MG exacerbation; FDA warning | Beta-lactams (cephalosporins, penicillins) |
| **Macrolides** | Azithromycin, erythromycin, clarithromycin | May worsen MG | Beta-lactams |
| **Beta-blockers** | Propranolol, metoprolol, etc. | Worsen MG; use with caution | Cardioselective (metoprolol) if essential |
| **Magnesium (IV high-dose)** | MgSO4 | Blocks neuromuscular transmission | Avoid unless life-threatening (e.g., eclampsia, torsades) |
| **Neuromuscular blockers** | Succinylcholine, rocuronium, vecuronium | Succinylcholine: hyperkalemia in myopathies; all NMBs: prolonged weakness in MG | Avoid if possible; if needed: rocuronium (reduced dose in MG) + sugammadex |
| **Calcium channel blockers** | Verapamil, diltiazem (less with dihydropyridines) | May worsen neuromuscular transmission | Dihydropyridines (amlodipine) if needed |
| **Botulinum toxin** | Botox, Dysport | Can worsen MG | Avoid in MG |
| **D-Penicillamine** | Cuprimine | Can induce MG (autoimmune) | Alternative for Wilson disease |
| **Checkpoint inhibitors** | Nivolumab, pembrolizumab, ipilimumab | Can trigger or worsen MG, myositis, GBS-like syndromes | Oncology risk-benefit discussion |
| **Statins** | Atorvastatin, simvastatin, etc. | Can cause myopathy; worsen pre-existing myopathy | Discontinue if causing myopathy |
| **Corticosteroids (acutely in MG)** | Prednisone, methylprednisolone | Can cause transient worsening of MG ("steroid dip") | Start AFTER IVIG/PLEX in MG crisis |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Neurology consultation — EMERGENT | STAT | STAT | ROUTINE | STAT | All patients with suspected neuromuscular respiratory failure; confirm diagnosis; guide disease-specific treatment (IVIG, PLEX, steroids) |
| Pulmonology / Critical Care consultation | STAT | STAT | - | STAT | Respiratory failure management; ventilator management; weaning protocols; NIV expertise |
| Serial FVC and NIF monitoring | STAT | STAT | - | STAT | **Most important monitoring parameter**; q4-6h initially; q1-2h if declining; trends are more important than absolute values; decline >30% is concerning |
| ICU admission | - | STAT | - | STAT | All patients with impending or established respiratory failure; FVC <25 mL/kg; declining trajectory; need for close monitoring |
| Speech-language pathology | - | URGENT | ROUTINE | URGENT | Dysphagia evaluation; aspiration risk assessment; safe diet recommendations; NPO if severe bulbar weakness |
| Medication review | STAT | STAT | ROUTINE | STAT | Review ALL medications for neuromuscular-impairing drugs; stop or substitute offending agents; see comprehensive list above |
| Goals of care discussion | - | URGENT | ROUTINE | URGENT | Especially important in ALS and progressive muscular dystrophies; discuss intubation, tracheostomy, long-term ventilation preferences EARLY |
| DVT prophylaxis | STAT | STAT | - | STAT | SCDs; pharmacologic prophylaxis (enoxaparin); immobile patients at very high risk |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Respiratory therapy | - | STAT | ROUTINE | STAT | CoughAssist; chest physiotherapy; secretion management; NIV setup and titration |
| Physical therapy | - | URGENT | ROUTINE | URGENT | Early mobilization when stable; prevent contractures; maintain function; ROM exercises |
| Occupational therapy | - | ROUTINE | ROUTINE | ROUTINE | ADL assessment; adaptive equipment; hand function preservation |
| Nutrition / Dietitian | - | ROUTINE | ROUTINE | ROUTINE | Caloric needs (often increased in NMD); dysphagia diet; enteral feeding if prolonged weakness; avoid overfeeding (increases CO2 production) |
| Social work | - | ROUTINE | ROUTINE | ROUTINE | Family support; discharge planning; long-term care needs; financial resources |
| Palliative care | - | ROUTINE | ROUTINE | ROUTINE | Symptom management; goals of care facilitation; especially important in ALS and progressive disorders |
| Cardiology | - | ROUTINE | ROUTINE | ROUTINE | If cardiomyopathy (DMD, LGMD, myotonic dystrophy); autonomic dysfunction (GBS) |
| Psychiatry / Psychology | - | ROUTINE | ROUTINE | - | Depression, anxiety common; ICU delirium; adjustment to chronic illness; ALS psychological support |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Repeat IVIG or PLEX | - | URGENT | ROUTINE | URGENT | If inadequate response to first course (MG, GBS); may need 2nd course of IVIG or PLEX; combination (IVIG + PLEX) not recommended (IVIG washed out by PLEX) |
| Rituximab (MG) | - | - | ROUTINE | - | Refractory MG; anti-CD20; especially useful in MuSK MG; onset weeks to months |
| Eculizumab (MG) | - | - | ROUTINE | - | Complement inhibitor; FDA-approved for refractory generalized AChR-positive MG; reduces exacerbations |
| Thymectomy (MG) | - | - | ROUTINE | - | Elective; for AChR-positive MG (benefit even without thymoma per MGTX trial); not in crisis; schedule when stable |
| Tracheostomy and long-term ventilation | - | ROUTINE | ROUTINE | ROUTINE | If unable to wean after 2-4 weeks; ALS patients who choose long-term ventilation; chronic NMD with respiratory failure |
| Home mechanical ventilation | - | - | ROUTINE | - | Transition from hospital/trach to home ventilation; requires extensive training; home nursing; sleep medicine / pulmonology follow-up |
| Diaphragm pacing | - | - | EXT | - | For high cervical spinal cord injury; some ALS patients; investigational in many settings |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Causes of Neuromuscular Respiratory Failure

| Category | Etiologies | Key Distinguishing Features |
|----------|-----------|---------------------------|
| **Neuromuscular junction** | Myasthenia gravis; Lambert-Eaton myasthenic syndrome (LEMS); botulism; organophosphate poisoning | MG: fatigable weakness, ptosis, diplopia, AChR Ab; LEMS: proximal weakness, autonomic symptoms, improves with repetition, anti-VGCC; Botulism: descending paralysis, dilated pupils, recent exposure; OP poisoning: miosis, salivation, bradycardia, cholinergic crisis |
| **Peripheral nerve** | Guillain-Barré syndrome; critical illness polyneuropathy (CIP); phrenic nerve injury (cardiac surgery); Charcot-Marie-Tooth (rare) | GBS: ascending weakness, areflexia, post-infectious, elevated CSF protein; CIP: ICU patient, sepsis, prolonged weakness; Phrenic injury: post-cardiac surgery, unilateral diaphragm paralysis |
| **Anterior horn cell** | ALS (amyotrophic lateral sclerosis); spinal muscular atrophy; poliomyelitis (rare) | ALS: UMN + LMN signs, progressive, fasciculations, no sensory involvement; SMA: childhood onset, proximal weakness |
| **Muscle** | Muscular dystrophies (DMD, BMD, LGMD, myotonic, FSHD); inflammatory myopathies (dermatomyositis, polymyositis, inclusion body myositis); critical illness myopathy; metabolic myopathies | DMD: young males, elevated CK, cardiac involvement; Myotonic: myotonia, cataracts, cardiac; Inflammatory: elevated CK, rash (DM), proximal weakness; CIM: ICU patient, prolonged steroids/NMB, flaccid weakness |
| **Respiratory muscle specific** | Bilateral diaphragm paralysis; diaphragmatic fatigue; isolated phrenic neuropathy | Orthopnea; paradoxical breathing; supine FVC drop >20%; fluoroscopy: paradoxical motion |

### Myasthenic Crisis vs. Cholinergic Crisis

| Feature | Myasthenic Crisis | Cholinergic Crisis |
|---------|------------------|-------------------|
| Cause | Worsening MG; undertreated; triggered by infection, medication, stress | Excessive cholinesterase inhibitor (pyridostigmine overdose) |
| Symptoms | Weakness, respiratory failure, ptosis, diplopia, dysphagia | Weakness PLUS: salivation, lacrimation, urination, defecation, GI upset, emesis (SLUDGE); miosis; bradycardia; fasciculations; bronchospasm |
| Pupils | Normal | Miotic (constricted) |
| Secretions | May be increased (from weak swallow) | Profusely increased |
| Response to edrophonium | Improves | Worsens |
| Treatment | IVIG/PLEX; hold pyridostigmine; supportive | Stop pyridostigmine; atropine for muscarinic symptoms; supportive |
| Clinical clue | Usually distinguishable clinically; cholinergic crisis is rare and usually obvious | Excessive secretions + diarrhea + small pupils + bradycardia |

### Red Flags for Imminent Respiratory Failure

| Red Flag | Action |
|----------|--------|
| FVC <20 mL/kg or declining >30% from baseline | Prepare for intubation; ICU transfer; increase monitoring frequency |
| NIF > -30 cm H2O (less negative) | Prepare for intubation |
| Rising PaCO2 (especially with respiratory acidosis) | Intubate — this is a LATE sign |
| Use of accessory muscles; tripoding | Impending failure |
| Tachypnea >30 with shallow breathing | Compensating; fatigue imminent |
| Paradoxical breathing (abdomen moves IN with inspiration) | Diaphragm fatigue/paralysis; intubate |
| Inability to count to 20 in one breath | Simple bedside test; very weak if cannot count to 10 |
| Weak cough; inability to clear secretions | Aspiration risk; may need intubation for airway protection |
| Orthopnea (cannot lie flat) | Diaphragm weakness; FVC drops supine |
| Altered mental status | Hypercapnia; severe — intubate immediately |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (ICU)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| FVC (forced vital capacity) | q4-6h initially; q1-2h if declining | >20 mL/kg safe; <15-20 mL/kg = intubation threshold | Declining trend or <15-20: prepare for intubation |
| NIF (negative inspiratory force) | q4-6h initially | < -30 cm H2O safe; > -20 to -25 = intubation threshold | Worsening (less negative): prepare for intubation |
| ABG | q6-8h or PRN; with any clinical change | PaCO2 35-45; pH 7.35-7.45 | Rising PaCO2 or acidosis: intubate |
| SpO2 | Continuous | >92% | Desaturation: assess for aspiration, atelectasis, failure; supplement O2 cautiously |
| Respiratory rate | Continuous | 12-20 | Tachypnea >30 with shallow breathing suggests fatigue |
| Neurologic exam (strength, bulbar function) | q4-8h | Stable or improving | Worsening weakness: reassess treatment; anticipate respiratory decline |
| Autonomic function (GBS) | Continuous (telemetry); q4h BP checks | Stable HR 60-100; BP 90-140 systolic | Arrhythmia: treat; wide BP swings: short-acting agents; bradycardia: atropine/pacing |
| Secretion assessment | q2-4h | Manageable; patient can cough | Excessive secretions + weak cough: aggressive pulmonary toilet; consider intubation |

### Weaning Phase Monitoring

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Daily SBT (spontaneous breathing trial) | Daily when criteria met | Pass SBT without distress | Fail: resume full support; reassess next day |
| FVC (pre-extubation) | Daily; before extubation | >15-20 mL/kg AND improving | Do not extubate if still declining |
| NIF (pre-extubation) | Daily | < -25 to -30 cm H2O | Weak NIF: high re-intubation risk |
| Cough strength / PCF | Daily | PCF >160 L/min for successful extubation; MEP >40 | Weak cough: high aspiration risk; continue CoughAssist; delay extubation |
| Bulbar function | Daily | Able to swallow saliva; protect airway | Severe bulbar weakness: aspiration risk; consider tracheostomy |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| ICU | FVC <25 mL/kg or declining; NIF > -40 cm H2O; any respiratory distress; autonomic instability (GBS); need for frequent monitoring (q1-4h); NIV initiation for acute failure; intubation anticipated or performed |
| Step-down / Intermediate | Stable but requires monitoring q4-6h; improving trajectory; stable on NIV; post-extubation observation |
| General floor | Stable respiratory function; FVC >30 mL/kg and stable; for diagnostic workup of mild exacerbation; initiation of immunotherapy without respiratory compromise |

### Discharge Criteria

| Criterion | Details |
|-----------|---------|
| Respiratory stability | FVC >25-30 mL/kg and stable/improving; off supplemental O2 or at baseline; able to clear secretions |
| Off mechanical ventilation (or stable on chronic NIV) | Extubated and stable x 24-48h; or established on home NIV with stable settings |
| Disease-specific treatment initiated and tolerated | IVIG/PLEX completed; oral immunosuppression started (MG); able to continue treatment outpatient |
| Adequate nutrition | Tolerating oral diet or enteral feeding established; swallowing safe per SLP |
| Functional mobility | PT/OT clearance; able to perform ADLs or adequate support |
| Follow-up arranged | Neurology (1-2 weeks); pulmonology (if chronic respiratory issues); PCP; cardiology (if applicable) |
| Education | Disease education; medication instructions; when to return to ED (worsening weakness, dyspnea, dysphagia); MedicAlert bracelet for MG; medication list (avoid contraindicated drugs) |
| Equipment | CoughAssist, suction machine, NIV (if prescribed); home nursing if tracheostomy/ventilator |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| Myasthenia Gravis Treatment Guidelines | AAN / MGFA | 2016/2021 | IVIG and PLEX are equivalent for MG exacerbation; thymectomy benefits AChR+ MG; corticosteroid caution (steroid dip); rituximab and eculizumab for refractory |
| Guillain-Barré Syndrome Guidelines | AAN | 2012 | IVIG or PLEX within 4 weeks of onset; equivalent efficacy; do NOT combine; steroids NOT effective |
| ALS Practice Parameters | AAN | 2009/Updates | NIV prolongs survival; CoughAssist; multidisciplinary care; riluzole modestly prolongs survival |
| Respiratory Management in NMD | ATS | 2004/Updates | NIV for chronic respiratory failure; FVC <50% threshold; CoughAssist; monitoring parameters |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [Plasma Exchange/Sandoglobulin GBS Trial (1997)](https://pubmed.ncbi.nlm.nih.gov/9014908/) | IVIG = PLEX for GBS; combination not better | Either IVIG or PLEX; no combination |
| [MG Thymectomy Trial (MGTX, 2016)](https://pubmed.ncbi.nlm.nih.gov/27509100/) | Thymectomy + prednisone > prednisone alone for AChR+ MG (even without thymoma); improved outcomes at 3 years | Thymectomy recommended for generalized AChR+ MG |
| [Radunovic et al. NIV in ALS (2017 Cochrane)](https://pubmed.ncbi.nlm.nih.gov/28982219/) | NIV prolongs survival in ALS (7-11 months) and improves QoL | NIV is standard of care for ALS respiratory insufficiency |
| [Lawn et al. Respiratory Failure in GBS (2001)](https://pubmed.ncbi.nlm.nih.gov/11405803/) | FVC <20 mL/kg or NIF > -30 cm H2O predicted need for intubation; "20/30/40 rule" | Established monitoring thresholds for MG crisis |
| [REGAIN Trial (Eculizumab in MG, 2017)](https://pubmed.ncbi.nlm.nih.gov/29066163/) | Eculizumab reduced exacerbations in refractory generalized MG | FDA approval of eculizumab for refractory AChR+ MG |

### The "20/30/40" Rule

| Parameter | Threshold | Interpretation |
|-----------|-----------|---------------|
| FVC | <20 mL/kg | Impending respiratory failure; consider intubation |
| NIF (MIP) | > -30 cm H2O (less negative) | Weak inspiratory muscles; impending failure |
| MEP | <40 cm H2O | Weak cough; unable to clear secretions; aspiration risk |

**Clinical Pearl:** These values suggest impending failure and need for intubation. Do NOT wait for PaCO2 elevation — this is a LATE sign. Trend is more important than absolute values.

---

## APPENDICES

### Appendix A: Medications to AVOID in Myasthenia Gravis (Comprehensive)

**ABSOLUTE CONTRAINDICATION / HIGH RISK:**
- Aminoglycosides (gentamicin, tobramycin, amikacin, streptomycin, neomycin)
- Botulinum toxin (Botox)
- D-Penicillamine (can induce MG)
- Magnesium (IV high-dose)
- Neuromuscular blocking agents (use reduced dose if essential; avoid succinylcholine)
- Telithromycin (Ketek)
- Quinine / Quinidine
- Procainamide

**USE WITH CAUTION / MODERATE RISK:**
- Fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin) — FDA warning
- Macrolides (azithromycin, erythromycin, clarithromycin)
- Beta-blockers (especially non-selective; propranolol > metoprolol)
- Calcium channel blockers (verapamil, diltiazem)
- Lithium
- Phenytoin
- Chloroquine / Hydroxychloroquine
- Interferon-alpha
- Checkpoint inhibitors (nivolumab, pembrolizumab, ipilimumab) — can trigger or worsen MG
- Statins (rare exacerbation)
- Iodinated contrast (rare)
- Corticosteroids (transient worsening — "steroid dip")

**GENERALLY SAFE:**
- Beta-lactams (penicillins, cephalosporins, carbapenems)
- Vancomycin
- TMP-SMX
- Metronidazole
- Doxycycline (though tetracycline class has theoretical risk — doxycycline generally safe)
- Acetaminophen
- NSAIDs
- Opioids
- Dihydropyridine calcium channel blockers (amlodipine)
- ACE inhibitors
- Most anticonvulsants (levetiracetam, valproate)

### Appendix B: RSI Considerations in Neuromuscular Disease

| Agent | Consideration |
|-------|--------------|
| **Succinylcholine** | **AVOID in myopathies/muscular dystrophies** — causes massive hyperkalemia and cardiac arrest; **AVOID in denervated patients (ALS, GBS)** — hyperkalemia; **MG patients:** Relative resistance — may need higher dose (but risk of prolonged effect) → generally avoid |
| **Rocuronium** | Preferred NMB in NMD; **MG patients:** Increased sensitivity — use 50% of usual dose (0.3-0.5 mg/kg instead of 0.6-1.2 mg/kg); have sugammadex available for reversal |
| **Sugammadex** | Reverses rocuronium; useful for failed intubation or when rapid reversal needed; standard dose 2-4 mg/kg; immediate reversal 16 mg/kg |
| **Etomidate** | Safe; no effect on neuromuscular transmission |
| **Propofol** | Safe; no NM effects |
| **Ketamine** | Safe from NM perspective; avoid in intracranial pathology |
| **Fentanyl** | Safe; useful for blunting response |
| **Lidocaine** | Safe; may reduce airway reactivity |

### Appendix C: Pulmonary Function Thresholds in Neuromuscular Disease

| Parameter | Normal | Abnormal | Critical / Intubation Threshold |
|-----------|--------|----------|--------------------------------|
| FVC | >80% predicted; >40-50 mL/kg | <50% predicted; <25-30 mL/kg | <15-20 mL/kg |
| Supine FVC | <10% drop from sitting | 10-20% drop | >25% drop (diaphragm weakness) |
| NIF (MIP) | < -80 cm H2O (more negative) | > -60 cm H2O | > -20 to -30 cm H2O |
| MEP | >80 cm H2O | <60 cm H2O | <40 cm H2O (weak cough) |
| Peak cough flow (PCF) | >360 L/min | <270 L/min | <160 L/min (inadequate secretion clearance) |
| PaCO2 | 35-45 mmHg | >45 mmHg (hypoventilation) | Rising PaCO2; >50-55 mmHg |
| SpO2 | >95% on room air | <92% on room air | Declining despite O2 (assess for aspiration, PE) |

### Appendix D: Neuromuscular Respiratory Failure Decision Algorithm

```
SUSPECTED NEUROMUSCULAR RESPIRATORY FAILURE
                │
    IMMEDIATE ASSESSMENT:
    • ABG (PaCO2, pH)
    • Bedside FVC and NIF
    • Secretion assessment / cough strength
    • Bulbar function (swallow, voice)
    • Vital signs, SpO2
                │
    RESPIRATORY STATUS?
         │
    ┌────┴────────┬───────────────┐
    │             │               │
  STABLE      BORDERLINE       FAILING
(FVC >25,    (FVC 15-25,     (FVC <15-20,
NIF < -40)   NIF -25 to -40) NIF > -20-25,
    │             │            rising PaCO2)
    │             │               │
Floor admission  ICU admission  INTUBATE
Serial q6h      Serial q2-4h   (RSI considerations)
monitoring       monitoring        │
    │             │               │
    │             │         ICU management
    │             │         Disease-specific Rx
    │             │               │
    └─────────────┴───────────────┘
                │
    DISEASE-SPECIFIC TREATMENT:
    • MG crisis → IVIG or PLEX; HOLD pyridostigmine
    • GBS → IVIG or PLEX (NOT both)
    • ALS → NIV; goals of care; palliative
    • Inflammatory myopathy → Corticosteroids + IVIG
    • Critical illness polyneuromyopathy → Supportive; treat sepsis
                │
    WEANING (when disease improving):
    • Daily SBT when FVC >15, NIF <-25
    • Extubate when: FVC >15-20 AND improving, effective cough, bulbar function intact
    • Monitor closely post-extubation
```

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
