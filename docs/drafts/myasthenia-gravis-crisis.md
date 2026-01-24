---
title: Myasthenia Gravis - Exacerbation/Crisis
description: Acute myasthenic exacerbation and crisis management - respiratory monitoring, IVIg/PLEX, medication safety, and ICU care.
version: "1.0"
setting: ED, HOSP, ICU
status: draft
tags:
  - neuromuscular
  - emergency
  - weakness
  - autoimmune
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Myasthenia Gravis - Exacerbation/Crisis

**VERSION:** 1.0
**CREATED:** January 24, 2026
**REVISED:** January 24, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Myasthenia Gravis - Exacerbation/Crisis

**ICD-10:** G70.00 (Myasthenia gravis without exacerbation), G70.01 (Myasthenia gravis with exacerbation), G70.1 (Toxic myoneural disorders)

**SCOPE:** Evaluation and management of acute myasthenic exacerbation and myasthenic crisis in adults. Covers respiratory monitoring, immunotherapy (IVIg and plasmapheresis), medications to avoid, and ICU management. Excludes new diagnosis workup, chronic maintenance therapy, Lambert-Eaton myasthenic syndrome (LEMS), and congenital myasthenic syndromes.

**CLINICAL SYNONYMS:** MG crisis, myasthenic crisis, MG exacerbation, acute MG flare, myasthenia gravis flare

---

**KEY DEFINITIONS:**
- **MG Exacerbation:** Worsening weakness requiring medication adjustment or immunotherapy but NOT requiring intubation
- **Myasthenic Crisis:** Respiratory failure requiring mechanical ventilation OR FVC <15-20 mL/kg
- **Cholinergic Crisis:** Excess acetylcholinesterase inhibitors causing weakness with muscarinic symptoms (SLUDGE: Salivation, Lacrimation, Urination, Defecation, GI distress, Emesis)

**KEY CLINICAL FEATURES:**
- Fatigable weakness (worsens with activity, improves with rest)
- Ptosis and diplopia (ocular MG or generalized with ocular involvement)
- Bulbar weakness: dysarthria, dysphagia, facial weakness
- Limb weakness (proximal > distal, arms > legs)
- Respiratory weakness: dyspnea, orthopnea, weak cough
- **Crisis triggers:** Infection, surgery, medication changes, pregnancy, stress

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

!!! danger "⚡ RESPIRATORY FAILURE WARNING"
    **15-20% of MG exacerbations progress to crisis.** Monitor FVC and NIF every 4-6 hours. Intubate if FVC <15 mL/kg or NIF weaker than -20 cmH2O.

!!! warning "⚠️ MEDICATION SAFETY"
    Many common medications worsen MG. See [Medications to AVOID](#medications-to-avoid) section before prescribing.

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential | Infection as trigger, baseline | Normal or elevated WBC if infected | STAT | STAT | — | STAT |
| CMP (BMP + LFTs) | Electrolytes, renal/hepatic function | Normal; hypokalemia worsens weakness | STAT | STAT | — | STAT |
| Magnesium | Hypomagnesemia worsens NMJ transmission | >1.8 mg/dL | STAT | STAT | — | STAT |
| Phosphorus | Hypophosphatemia causes weakness | >2.5 mg/dL | STAT | STAT | — | STAT |
| TSH | Thyroid disease common comorbidity | Normal | URGENT | ROUTINE | — | URGENT |
| Blood glucose | Hyperglycemia worsens outcomes | <180 mg/dL | STAT | STAT | — | STAT |
| Urinalysis | UTI as trigger | Negative for infection | STAT | ROUTINE | — | STAT |
| Blood cultures | If febrile or sepsis suspected | Negative | STAT | STAT | — | STAT |
| Procalcitonin | Differentiate infection vs non-infectious flare | <0.5 ng/mL if non-infectious | URGENT | ROUTINE | — | URGENT |
| ABG or VBG | Respiratory status, CO2 retention | PaCO2 <45 mmHg, pH >7.35 | STAT | STAT | — | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| AChR (acetylcholine receptor) antibody | Confirm diagnosis if unknown | Document if positive (~85% of generalized MG) | — | ROUTINE | — | ROUTINE |
| MuSK antibody | If AChR negative | Document if positive (~40% of AChR-negative) | — | ROUTINE | — | ROUTINE |
| LRP4 antibody | If AChR and MuSK negative | Document if positive | — | EXT | — | EXT |
| Anti-striated muscle antibody | Thymoma association | If positive, CT chest | — | ROUTINE | — | ROUTINE |
| Hepatitis B surface antigen | Pre-IVIg screening | Negative | — | URGENT | — | URGENT |
| Quantitative immunoglobulins | IgA deficiency (IVIg contraindication) | IgA >7 mg/dL | — | URGENT | — | URGENT |
| PT/INR, PTT | Pre-PLEX | Normal | — | URGENT | — | STAT |
| Type and screen | Pre-PLEX | Available | — | URGENT | — | STAT |
| Fibrinogen | Pre-PLEX baseline | Normal | — | URGENT | — | STAT |
| Troponin | Cardiac involvement, stress | Normal | URGENT | ROUTINE | — | STAT |
| BNP/NT-proBNP | Heart failure assessment | Normal | URGENT | ROUTINE | — | STAT |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Cortisol (random or AM) | Adrenal insufficiency if on chronic steroids | Normal stress response | — | ROUTINE | — | ROUTINE |
| Acetylcholinesterase inhibitor level | Cholinergic crisis concern (if available) | Therapeutic range | — | EXT | — | EXT |
| Paraneoplastic panel | Occult malignancy | Negative | — | EXT | — | EXT |
| Respiratory viral panel | Viral trigger | Document if positive | — | ROUTINE | — | ROUTINE |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Chest X-ray | On admission | Aspiration, atelectasis, pneumonia | None | STAT | STAT | — | STAT |
| ECG | On admission | Arrhythmia, QT prolongation | None | STAT | STAT | — | STAT |
| Forced vital capacity (FVC) | Serial q4-6h (q2h if declining) | FVC >15-20 mL/kg | Facial weakness limiting seal | STAT | STAT | — | STAT |
| Negative inspiratory force (NIF) | Serial q4-6h (q2h if declining) | NIF more negative than -20 cmH2O | Facial weakness | STAT | STAT | — | STAT |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT chest with contrast | If thymoma not previously evaluated | Thymoma or thymic hyperplasia | Contrast allergy, renal impairment | — | ROUTINE | — | ROUTINE |
| CT chest without contrast | Thymoma evaluation (if contrast contraindicated) | Thymic abnormality | None | — | ROUTINE | — | ROUTINE |
| Swallow evaluation | Bulbar symptoms | Aspiration risk | None | — | URGENT | — | URGENT |
| Repetitive nerve stimulation | If diagnosis uncertain | Decremental response >10% | None | — | ROUTINE | — | ROUTINE |
| Single-fiber EMG | If RNS negative but MG suspected | Increased jitter, blocking | None | — | EXT | — | EXT |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| PET-CT | Occult thymoma or malignancy | Tumor identification | Hemodynamic instability | — | EXT | — | EXT |
| Ice pack test | Bedside diagnostic (ptosis) | Improvement with cooling | None | STAT | STAT | — | STAT |

---

## 3. TREATMENT

**CRITICAL:** Myasthenic crisis is a medical emergency. Secure airway early if deteriorating. Do NOT delay intubation.

### Crisis vs Cholinergic Crisis Differentiation

| Feature | Myasthenic Crisis | Cholinergic Crisis |
|---------|-------------------|-------------------|
| Pupils | Normal or mydriasis | Miosis |
| Secretions | Normal or dry | Excessive (SLUDGE) |
| Fasciculations | Absent | Present |
| Heart rate | Normal or tachy | Bradycardia |
| Response to edrophonium | Improvement | Worsening |
| Management | IVIg/PLEX, stop AChEI temporarily | Stop AChEI, supportive care |

### 3A. Acute/Emergent - Airway and Respiratory Support

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Supplemental oxygen | INH | Hypoxemia | 2-6 L/min NC; 15 L/min NRB :: INH :: PRN :: Titrate to O2 sat >94%; escalate as needed | None | O2 sat, RR | STAT | STAT | — | STAT |
| Endotracheal intubation | — | Respiratory failure | N/A :: — :: :: Intubate if FVC <15 mL/kg, NIF >-20 cmH2O, or clinical deterioration; AVOID succinylcholine (may have prolonged block); use rocuronium (may need higher dose) | — | ETT position, ventilator settings | STAT | STAT | — | STAT |
| Non-invasive ventilation (BiPAP) | — | Bridge to intubation or mild hypoventilation | IPAP 10-15; EPAP 5 :: — :: continuous :: BiPAP may temporize; NOT a substitute for intubation in true crisis | Severe respiratory failure, inability to protect airway | RR, TV, O2 sat, CO2 | STAT | STAT | — | STAT |
| Mechanical ventilation | — | Respiratory failure | N/A :: — :: :: Lung-protective ventilation; expect prolonged wean; daily SBT when improved | — | ABG, ventilator parameters | — | — | — | STAT |

### 3B. Immunotherapy - First-line for Crisis/Severe Exacerbation

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IVIg (immune globulin IV) | IV | Myasthenic crisis or severe exacerbation | 0.4 g/kg/day x 5 days; 1 g/kg/day x 2 days :: IV :: daily x 5 days :: 0.4 g/kg/day IV for 5 days (preferred) OR 1 g/kg/day x 2 days; infuse slowly day 1 | IgA deficiency with anti-IgA antibodies; severe renal impairment; recent MI/stroke (thrombosis risk) | Renal function daily, headache, infusion reactions; pre-medicate | — | STAT | — | STAT |
| Plasmapheresis (PLEX) | — | Myasthenic crisis or severe exacerbation | 5 exchanges over 7-14 days :: — :: QOD x 5 :: 5 exchanges (1-1.5 plasma volumes per exchange) over 7-14 days; typically QOD | Hemodynamic instability, severe sepsis, poor IV access | BP, electrolytes, coagulation, fibrinogen | — | STAT | — | STAT |

**IVIg vs PLEX Selection:**
- **IVIg preferred:** Hemodynamic instability, autonomic dysfunction, difficult vascular access, outpatient
- **PLEX preferred:** Severe/rapidly worsening crisis (faster onset), IgA deficiency, MuSK-positive MG (may respond better), preparation for thymectomy
- **Efficacy:** Both effective; PLEX may work faster (days) vs IVIg (5-7 days)
- **Duration:** Effects last 3-6 weeks; bridge to chronic immunotherapy

### 3C. Cholinesterase Inhibitors

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Pyridostigmine | PO | Symptomatic treatment | 30 mg TID; 60 mg TID; 60 mg QID; 90 mg QID :: PO :: TID-QID :: Start 30-60 mg TID; titrate by 30 mg/dose q2-3d; max ~120 mg q4h; usual maintenance 60-90 mg q4-6h | Mechanical bowel/bladder obstruction | Cholinergic symptoms (SLUDGE), HR | — | ROUTINE | — | ROUTINE |
| Pyridostigmine (in crisis) | — | During crisis | HOLD or reduce :: — :: :: HOLD pyridostigmine in intubated patients or suspected cholinergic crisis; restart at low dose when improving | Cholinergic crisis | Secretions, HR | — | STAT | — | STAT |
| Neostigmine | IV/IM | If NPO and needs AChEI | 0.5 mg IV q3h; 1.5 mg IM q3h :: IV/IM :: q3h :: 0.5 mg IV or 1.5 mg IM roughly equivalent to 60 mg PO pyridostigmine; use ONLY if cannot take PO and essential | Cholinergic toxicity | HR, secretions | — | URGENT | — | URGENT |
| Glycopyrrolate | PO/IV | Cholinergic side effects | 1 mg PO TID; 0.2 mg IV PRN :: PO/IV :: TID :: 1-2 mg PO TID for secretions/GI effects; 0.2 mg IV PRN; does not cross BBB | Glaucoma, severe cardiac disease | HR, urinary retention | — | ROUTINE | — | ROUTINE |

### 3D. Corticosteroids (Use with CAUTION)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Prednisone (low-dose start) | PO | Moderate exacerbation | 10 mg daily; 20 mg daily :: PO :: daily :: Start LOW (10-20 mg daily) and increase slowly by 10 mg q5-7d to target 1 mg/kg/day; HIGH-DOSE INITIATION CAN WORSEN MG | Active infection (relative), brittle MG | Glucose, BP, K+; WATCH FOR TRANSIENT WORSENING days 5-10 | — | ROUTINE | — | — |
| Methylprednisolone | IV | Severe exacerbation (with IVIg/PLEX cover) | 500 mg daily x 3-5 days; 1000 mg daily x 3-5 days :: IV :: daily x 3-5 days :: 500-1000 mg IV daily x 3-5 days; ONLY with IVIg/PLEX coverage due to risk of transient worsening | Active untreated infection | Glucose, BP, K+, psychiatric effects | — | URGENT | — | URGENT |

**⚠️ STEROID WARNING:** High-dose corticosteroids can cause transient worsening of MG (typically days 5-10). Only initiate high-dose steroids with IVIg or PLEX cover, or in ICU setting with close respiratory monitoring.

### 3E. Medications to AVOID

**CRITICAL:** The following medications can worsen myasthenia gravis and should be avoided or used with extreme caution:

| Category | Medications to AVOID | Alternative |
|----------|---------------------|-------------|
| **Antibiotics** | Aminoglycosides (gentamicin, tobramycin, amikacin), fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin), macrolides (azithromycin, erythromycin), telithromycin | Penicillins, cephalosporins, carbapenems generally safer |
| **Cardiac** | Beta-blockers (all), calcium channel blockers (verapamil, diltiazem), procainamide, quinidine, lidocaine | Use with caution; cardiology consult |
| **Neuromuscular blockers** | Succinylcholine (prolonged block), non-depolarizing agents (prolonged) | If needed, use reduced dose rocuronium with sugammadex available |
| **Psychiatric** | Lithium, phenothiazines, benzodiazepines (high dose) | SSRIs generally safe |
| **Anticonvulsants** | Phenytoin, gabapentin (rare reports) | Levetiracetam, valproate safer |
| **Other** | Magnesium IV (high dose), D-penicillamine, botulinum toxin, quinine, chloroquine, iodinated contrast (caution) | Avoid if possible |

### 3F. Supportive Care

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Enoxaparin | SC | DVT prophylaxis | 40 mg daily; 30 mg BID :: SC :: daily :: 40 mg SC daily; 30 mg BID if BMI >40; hold if CrCl <30 | Active bleeding, HIT | Platelet count, bleeding | — | STAT | — | STAT |
| Heparin (UFH) | SC | DVT prophylaxis (renal impairment) | 5000 units q8h; 5000 units q12h :: SC :: q8-12h :: 5000 units SC q8-12h if CrCl <30 | Active bleeding, HIT | Platelet count | — | STAT | — | STAT |
| Famotidine | IV/PO | Stress ulcer prophylaxis (if on steroids) | 20 mg BID; 40 mg daily :: IV/PO :: BID :: 20 mg IV/PO BID or 40 mg daily | None significant | None | — | ROUTINE | — | ROUTINE |
| Insulin (regular) | IV/SC | Steroid-induced hyperglycemia | Sliding scale; basal-bolus :: IV/SC :: per protocol :: Sliding scale or basal-bolus; target glucose <180 mg/dL | Hypoglycemia | Glucose q4-6h | — | ROUTINE | — | STAT |
| Acetaminophen | PO/IV | Fever, mild pain | 650 mg q6h; 1000 mg q6h :: PO/IV :: q6h :: 650-1000 mg q6h; max 4 g/day | Severe hepatic impairment | LFTs if prolonged | STAT | STAT | — | STAT |
| SCDs (sequential compression devices) | — | DVT prophylaxis | N/A :: — :: continuous :: Bilateral lower extremity SCDs | DVT in that extremity | Skin integrity | STAT | STAT | — | STAT |

### 3G. Long-term Immunosuppression (Initiate/Continue as Indicated)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Azathioprine | PO | Steroid-sparing agent | 50 mg daily; 100 mg daily; 150 mg daily :: PO :: daily :: Start 50 mg daily; increase by 50 mg q2-4wk to 2-3 mg/kg/day; check TPMT before starting | TPMT deficiency, pregnancy | CBC weekly x 4, then monthly; LFTs monthly | — | ROUTINE | — | — |
| Mycophenolate mofetil | PO | Steroid-sparing agent | 500 mg BID; 1000 mg BID; 1500 mg BID :: PO :: BID :: Start 500 mg BID; increase to 1000-1500 mg BID over 2-4 weeks | Pregnancy, hypersensitivity | CBC q2wk x 2mo, then monthly; LFTs | — | ROUTINE | — | — |
| Rituximab | IV | Refractory MG, MuSK-positive MG | 375 mg/m² weekly x 4 weeks; 1000 mg q2wk x 2 :: IV :: weekly x 4 or q2wk x 2 :: 375 mg/m² weekly x 4 OR 1000 mg x 2 doses (2 weeks apart); pre-medicate with methylpred, acetaminophen, diphenhydramine | Active infection, HBV (screen first) | Infusion reactions, CD19/CD20, immunoglobulins | — | EXT | — | EXT |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | Indication | ED | HOSP | OPD | ICU |
|----------------|------------|:--:|:----:|:---:|:---:|
| Neurology consult | All MG exacerbations | STAT | STAT | — | STAT |
| Pulmonology consult | Respiratory compromise, ventilator wean | URGENT | URGENT | — | STAT |
| Critical care consult | FVC <20 mL/kg, impending crisis | URGENT | STAT | — | STAT |
| Thoracic surgery consult | Thymoma identified, thymectomy planning | — | ROUTINE | — | ROUTINE |
| Speech therapy consult | Bulbar symptoms, dysphagia | — | URGENT | — | URGENT |
| Physical therapy consult | Mobility, fall prevention | — | URGENT | — | URGENT |
| Occupational therapy consult | ADL assessment, energy conservation | — | ROUTINE | — | ROUTINE |
| Respiratory therapy | Airway clearance, pulmonary toilet | STAT | STAT | — | STAT |
| Pharmacy consult | Medication safety review | — | URGENT | — | URGENT |
| Social work | Support resources, discharge planning | — | ROUTINE | — | ROUTINE |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return immediately for worsening weakness or breathing difficulty | STAT | — | STAT |
| Do not skip or suddenly stop immunosuppressive medications | STAT | STAT | STAT |
| Carry MG medical alert card listing medications to avoid | — | STAT | STAT |
| Take pyridostigmine 30-60 minutes before meals if dysphagia | — | ROUTINE | ROUTINE |
| Report fever or signs of infection promptly | STAT | STAT | STAT |
| Avoid extreme heat (worsens symptoms) | — | ROUTINE | ROUTINE |
| Get adequate rest, avoid overexertion | — | ROUTINE | ROUTINE |
| Do not drive if diplopia or ptosis impairs vision | STAT | STAT | STAT |
| Myasthenia Gravis Foundation resources (www.myasthenia.org) | — | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Aspiration precautions if bulbar weakness | STAT | STAT | — |
| Fall precautions for all MG patients | STAT | STAT | STAT |
| Medication reconciliation before any new prescription | STAT | STAT | STAT |
| Vaccinations: avoid live vaccines on immunosuppression; flu and pneumococcal recommended | — | ROUTINE | ROUTINE |
| Stress management (stress can trigger exacerbation) | — | ROUTINE | ROUTINE |
| Sleep hygiene | — | ROUTINE | ROUTINE |
| Energy conservation techniques | — | ROUTINE | ROUTINE |

---

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Guillain-Barré syndrome | Ascending weakness, areflexia, no fluctuation | CSF (albuminocytologic dissociation), EMG/NCS |
| Lambert-Eaton syndrome | Proximal weakness, autonomic symptoms, reflexes improve with exercise | VGCC antibodies, EMG (incremental response) |
| Botulism | Descending weakness, pupil involvement, GI symptoms | Stool/serum toxin, EMG |
| Brainstem stroke | Acute onset, crossed findings, other cranial nerve signs | MRI brain |
| Multiple sclerosis | CNS symptoms, sensory involvement, different time course | MRI brain/spine, CSF |
| Thyroid eye disease | Thyroid dysfunction, proptosis, restrictive ophthalmopathy | TFTs, orbital imaging |
| Oculopharyngeal muscular dystrophy | Older onset, slowly progressive, no fluctuation | Genetic testing, muscle biopsy |
| Mitochondrial myopathy | Progressive, elevated lactate, other organ involvement | Lactate, muscle biopsy, genetic testing |
| Drug-induced MG | Recent D-penicillamine, checkpoint inhibitors | Medication history, antibodies |
| Cholinergic crisis | SLUDGE symptoms, miosis, bradycardia | Clinical, response to stopping AChEI |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Forced vital capacity (FVC) | q4-6h; q2h if declining | >15-20 mL/kg | Intubate if <15 mL/kg | STAT | STAT | — | STAT |
| Negative inspiratory force (NIF) | q4-6h; q2h if declining | More negative than -20 cmH2O | Intubate if weaker than -20 cmH2O | STAT | STAT | — | STAT |
| Oxygen saturation | Continuous | >94% | Supplement O2, consider intubation | STAT | STAT | — | STAT |
| Neurological exam (strength) | q4-8h | Stable or improving | Escalate therapy if worsening | STAT | STAT | ROUTINE | STAT |
| Swallow function | Daily if bulbar symptoms | Safe swallow | NPO, NG tube if unsafe | — | STAT | — | STAT |
| Blood glucose | q6h if on steroids | <180 mg/dL | Insulin adjustment | — | ROUTINE | — | STAT |
| Renal function | Daily during IVIg | Cr stable | Hold IVIg, hydrate if rising | — | STAT | — | STAT |
| Electrolytes (K+, Mg) | Daily | K+ >3.5, Mg >1.8 | Replete aggressively | STAT | STAT | — | STAT |
| Heart rate/rhythm | Continuous | Sinus rhythm, HR 60-100 | Evaluate for autonomic dysfunction | STAT | STAT | — | STAT |
| Blood pressure | q4h | SBP 100-160 | Evaluate for autonomic dysfunction | STAT | STAT | — | STAT |
| Cholinergic symptoms | Each dose of pyridostigmine | Absent | Reduce dose, consider cholinergic crisis | — | ROUTINE | — | ROUTINE |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **ICU admission** | FVC <20 mL/kg or declining; NIF weaker than -30 cmH2O; rapid progression; bulbar dysfunction with aspiration risk; need for intubation/BiPAP |
| **Step-down/telemetry** | Stable FVC >20 mL/kg; improving or stable exam; receiving IVIg/PLEX; no bulbar symptoms |
| **General floor** | Mild exacerbation; FVC >30 mL/kg and stable; no bulbar symptoms; stable on oral medications |
| **Discharge home** | Stable or improved x 24-48 hours; FVC stable >30 mL/kg; adequate oral intake; medications optimized; outpatient follow-up arranged |
| **Acute rehabilitation** | Significant residual weakness after crisis; requires intensive therapy; medically stable |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IVIg and PLEX equally effective for MG exacerbation | Class I, Level A | [Gajdos et al. Cochrane 2012](https://pubmed.ncbi.nlm.nih.gov/23235604/) |
| IVIg 2 g/kg total dose standard | Class I, Level A | [Zinman et al. Lancet Neurol 2007](https://pubmed.ncbi.nlm.nih.gov/17706563/) |
| PLEX effective for MG crisis | Class I, Level A | [Gajdos et al. Cochrane 2012](https://pubmed.ncbi.nlm.nih.gov/23235604/) |
| FVC and NIF for respiratory monitoring | Class II, Level B | [Rabinstein & Wijdicks. Neurology 2003](https://pubmed.ncbi.nlm.nih.gov/12654988/) |
| Pyridostigmine for symptomatic treatment | Class I, Level A | [Mehndiratta et al. Cochrane 2014](https://pubmed.ncbi.nlm.nih.gov/25304970/) |
| Corticosteroids can cause initial worsening | Class II, Level B | [Palace et al. Lancet Neurol 2012](https://pubmed.ncbi.nlm.nih.gov/22305458/) |
| Azathioprine as steroid-sparing agent | Class I, Level B | [Palace et al. NEJM 1998](https://pubmed.ncbi.nlm.nih.gov/9771070/) |
| Rituximab effective in refractory/MuSK+ MG | Class II, Level C | [Nowak et al. Neurology 2022](https://pubmed.ncbi.nlm.nih.gov/34986310/) |
| Medications to avoid in MG | Class III, Level C | [Juel. Semin Neurol 2004](https://pubmed.ncbi.nlm.nih.gov/15257515/) |
| Thymectomy beneficial in generalized MG | Class I, Level B | [Wolfe et al. NEJM 2016 (MGTX Trial)](https://pubmed.ncbi.nlm.nih.gov/27509102/) |

---

## CHANGE LOG

**v1.0 (January 24, 2026)**
- Initial template creation
- Includes respiratory monitoring protocol
- IVIg and PLEX protocols for crisis
- Comprehensive medications to avoid list
- Cholinergic vs myasthenic crisis differentiation
- Steroid initiation guidance with worsening warning

---

## APPENDIX A: Myasthenia Gravis Foundation of America (MGFA) Clinical Classification

| Class | Description |
|-------|-------------|
| **I** | Ocular weakness only (ptosis, diplopia) |
| **II** | Mild generalized weakness ± ocular |
| **IIa** | Predominantly limb/axial |
| **IIb** | Predominantly oropharyngeal/respiratory |
| **III** | Moderate generalized weakness ± ocular |
| **IIIa** | Predominantly limb/axial |
| **IIIb** | Predominantly oropharyngeal/respiratory |
| **IV** | Severe generalized weakness ± ocular |
| **IVa** | Predominantly limb/axial |
| **IVb** | Predominantly oropharyngeal/respiratory |
| **V** | Intubation required (with or without mechanical ventilation) |

**Clinical Use:** Document at admission and track progression. Class IIb, IIIb, IVb (bulbar predominant) and any Class IV/V require ICU monitoring.

---

## APPENDIX B: Quantitative Myasthenia Gravis (QMG) Score

Standardized 13-item scoring system for disease severity. Each item scored 0-3 (total 0-39).

| Item | Assessment |
|------|------------|
| Diplopia | Lateral gaze duration |
| Ptosis | Upward gaze duration |
| Facial muscles | Eye closure strength |
| Swallowing | 4 oz water |
| Speech | Counting to 50 |
| Right arm extended | 90° duration |
| Left arm extended | 90° duration |
| FVC | % predicted |
| Right hand grip | Dynamometer |
| Left hand grip | Dynamometer |
| Head lift | Supine, 45° duration |
| Right leg extended | Supine, 45° duration |
| Left leg extended | Supine, 45° duration |

**Interpretation:**
- 0-9: Mild
- 10-19: Moderate
- ≥20: Severe

---

## APPENDIX C: IVIg vs PLEX Quick Reference

| Factor | IVIg | PLEX |
|--------|------|------|
| **Onset of action** | 5-7 days | 2-3 days |
| **Duration of effect** | 3-6 weeks | 3-6 weeks |
| **Administration** | Peripheral IV possible | Central line usually required |
| **Sessions** | Daily x 5 days (or x2 days) | QOD x 5 (over ~2 weeks) |
| **Hemodynamic tolerance** | Better | Fluid shifts, hypotension risk |
| **In pregnancy** | Safe | Safe but challenging |
| **Renal impairment** | Caution (risk AKI) | Preferred |
| **IgA deficiency** | Contraindicated | Safe |
| **MuSK+ MG** | May be less effective | May be preferred |
| **Before thymectomy** | Either | Often preferred |
| **Cost** | Higher | Lower |
| **Outpatient feasible** | Yes | Difficult |
