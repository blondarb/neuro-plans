---
title: "Myasthenia Gravis - Exacerbation/Crisis"
description: "Clinical decision support for myasthenia gravis - exacerbation/crisis diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
---

# Myasthenia Gravis - Exacerbation/Crisis

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Myasthenia Gravis - Exacerbation/Crisis

**ICD-10:** G70.01 (Myasthenia gravis with exacerbation)

**SYNONYMS:** Myasthenic crisis, MG crisis, MG exacerbation, myasthenia exacerbation, myasthenic respiratory failure, acute MG, worsening myasthenia, cholinergic crisis, myasthenia gravis crisis

**SCOPE:** Acute exacerbation and myasthenic crisis in adults with known or suspected myasthenia gravis. Covers respiratory monitoring, emergent immunotherapy (IVIG/PLEX), cholinesterase inhibitor management, distinguishing myasthenic from cholinergic crisis, and medications to avoid. Excludes new diagnosis workup (see MG - New Diagnosis template), Lambert-Eaton syndrome, and chronic stable management.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; infection screen (common trigger); leukocytosis suggests infection | Normal |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolytes, renal/hepatic function for medication dosing; hypokalemia worsens weakness | Normal |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia worsens NMJ transmission; CONTRAINDICATED to give IV Mg in MG crisis | Confirm normal BEFORE any magnesium replacement |
| TSH (CPT 84443) | URGENT | ROUTINE | ROUTINE | URGENT | Thyroid disease coexists in 10-15% of MG; thyrotoxicosis precipitates crisis | Normal |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Steroid-induced hyperglycemia management | Normal |
| Urinalysis (CPT 81003) + urine culture | STAT | ROUTINE | ROUTINE | STAT | UTI as precipitant for exacerbation | Negative |
| Blood cultures x2 (CPT 87040) | STAT | STAT | - | STAT | If febrile; infection is #1 trigger for crisis | No growth |
| Pregnancy test (β-hCG) | STAT | STAT | ROUTINE | STAT | Affects treatment choices; MG can fluctuate in pregnancy | Document result |
| PT/INR (CPT 85610), aPTT (CPT 85730) | STAT | ROUTINE | - | STAT | Coagulation before procedures; PLEX circuit anticoagulation | Normal |
| ABG (CPT 82803) or VBG (CPT 82800) | STAT | STAT | - | STAT | Respiratory failure assessment; hypercapnia is LATE finding — do not wait for this | Normal; rising pCO2 = imminent failure |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| AChR binding antibody (CPT 86235) | - | ROUTINE | ROUTINE | - | Confirm diagnosis if not previously tested; positive in 85% generalized MG | Positive supports MG diagnosis |
| AChR modulating antibody (CPT 86235) | - | ROUTINE | ROUTINE | - | Additional sensitivity when binding Ab equivocal | Positive supports diagnosis |
| AChR blocking antibody (CPT 86235) | - | ROUTINE | ROUTINE | - | Part of full AChR panel | Positive supports diagnosis |
| MuSK antibody (CPT 86235) | - | ROUTINE | ROUTINE | - | If AChR negative; MuSK-positive MG has different treatment implications (poor response to pyridostigmine, PLEX preferred over IVIG) | Check if AChR negative |
| Anti-striated muscle antibody (anti-titin) | - | ROUTINE | ROUTINE | - | Associated with thymoma; especially in young patients | If positive, image for thymoma |
| Procalcitonin (CPT 84145) | URGENT | ROUTINE | - | URGENT | Differentiate bacterial infection trigger from other causes of decompensation | <0.5 ng/mL |
| Chest X-ray (CPT 71046) | STAT | ROUTINE | - | STAT | Aspiration pneumonia, atelectasis; baseline for ventilator | Clear lungs |
| Lactate (CPT 83605) | URGENT | ROUTINE | - | URGENT | Sepsis screen if febrile | Normal (<2 mmol/L) |
| Drug level of immunosuppressant (if applicable) | - | ROUTINE | ROUTINE | - | Check azathioprine metabolites (6-TGN), mycophenolate levels, tacrolimus levels if on these agents | Therapeutic range |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| LRP4 antibody | - | EXT | EXT | - | Triple-seronegative MG (AChR-/MuSK-/LRP4+) | Check if double seronegative |
| Agrin antibody | - | EXT | EXT | - | Emerging biomarker in seronegative MG | Research use |
| Anti-Kv1.4 antibody | - | EXT | EXT | - | Associated with myocarditis in MG; cardiac risk stratification | Check if cardiac symptoms |
| Complement levels (C3, C4) | - | EXT | EXT | - | Complement-mediated MG pathophysiology; pre-eculizumab evaluation | Baseline |
| Quantitative immunoglobulins (IgG, IgA, IgM) | - | ROUTINE | ROUTINE | - | Hypogammaglobulinemia from rituximab or chronic IVIG; IgA deficiency before IVIG | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Chest X-ray (CPT 71046) | STAT | ROUTINE | - | STAT | Immediate in ED | Pneumonia, aspiration, atelectasis, mediastinal mass (thymoma) | None significant |
| ECG (12-lead) (CPT 93000) | STAT | ROUTINE | - | STAT | On admission | Arrhythmia, myocarditis (rare but reported in MG, especially anti-Kv1.4+) | None |
| Bedside spirometry (FVC and NIF) (CPT 94010) | STAT | STAT | ROUTINE | STAT | Immediately on presentation; serial monitoring | FVC >20 mL/kg; NIF more negative than -30 cmH2O | Patient cooperation required |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT chest with contrast (CPT 71260) | - | ROUTINE | ROUTINE | - | During admission if not recently done | Thymoma (present in 10-15%); thymic hyperplasia | Contrast allergy, renal impairment |
| MRI chest (alternative to CT) | - | ROUTINE | ROUTINE | - | If CT contraindicated | Thymoma evaluation | Pacemaker, metallic implants |
| Repetitive nerve stimulation (RNS) (CPT 95937) | - | ROUTINE | ROUTINE | - | If diagnosis not confirmed; avoid during acute crisis (deferred to stable phase) | Decremental response >10% at 2-3 Hz in affected muscle | None significant |
| Single-fiber EMG (SFEMG) (CPT 95872) | - | - | ROUTINE | - | Most sensitive test (95-99%); defer to outpatient stable phase | Increased jitter, blocking | Patient cooperation |
| CT head (CPT 70450) | URGENT | ROUTINE | - | URGENT | If altered mental status to rule out other causes | Normal (MG does not affect brain parenchyma) | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| PET-CT (CPT 78816) | - | EXT | EXT | - | If thymoma on CT; staging | Metabolic activity, metastatic disease | Pregnancy |
| Echocardiogram (CPT 93306) | - | ROUTINE | ROUTINE | ROUTINE | If cardiac symptoms or anti-Kv1.4 positive | Myocarditis, cardiomyopathy | None significant |
| Pulmonary function tests (formal) (CPT 94010) | - | - | ROUTINE | - | Outpatient baseline after recovery | FVC baseline for future comparisons | Patient cooperation |

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IVIG (intravenous immunoglobulin) (CPT 96365) | IV | - | 0.4 g/kg :: IV :: daily x 5 days :: 0.4 g/kg/day IV x 5 days (total 2 g/kg) OR 1 g/kg/day x 2 days (faster option). Start within 24h of crisis recognition | IgA deficiency (anaphylaxis risk — use IgA-depleted product); renal failure; thrombotic risk | Vital signs q15min first infusion; renal function daily; headache (aseptic meningitis); thrombotic events | - | STAT | - | STAT |
| Plasmapheresis (PLEX) (CPT 36514) | - | - | 5 exchanges over 10-14 days (every other day); 1-1.5 plasma volumes per exchange. PREFERRED for MuSK-positive MG. Faster onset than IVIG (days vs 1-2 weeks) | Hemodynamic instability, severe sepsis, heparin allergy, poor vascular access | BP continuous during exchange; Ca2+ (citrate toxicity); fibrinogen; electrolytes; line infection | - | STAT | - | STAT |
| Intubation and mechanical ventilation | - | - | 20 mL/kg :: - :: - :: Indications: FVC <20 mL/kg, NIF >-30 cmH2O (weaker), >30% FVC decline, clinical distress, inability to handle secretions. Use NON-DEPOLARIZING agents at REDUCED DOSE (MG patients are sensitive). Avoid succinylcholine (unpredictable response) | N/A (life-saving) | Ventilator per ICU protocol; daily SBT when improving | STAT | STAT | - | STAT |
| Hold pyridostigmine during crisis | - | - | HOLD cholinesterase inhibitors during intubation/crisis — excess cholinergic stimulation increases secretions and complicates ventilator management. Resume at reduced dose during weaning | N/A | Secretion management; restart when extubation approaching | STAT | STAT | - | STAT |
| Supplemental oxygen | - | - | 94% :: - :: - :: As needed for SpO2 <94% | N/A | SpO2 monitoring | STAT | STAT | - | STAT |
| IV fluids (isotonic) | IV | - | NS maintenance; hydration for IVIG renal protection | Volume overload | I/O, electrolytes | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Pyridostigmine (when stable/recovering) | PO | Symptomatic weakness improvement | 30 mg :: PO :: q4h :: Resume at 30 mg PO TID during recovery; titrate by 30 mg/dose q3-5 days to 60 mg PO q4-6h; max 120 mg q4h (rarely needed). Take 30-60 min before meals for dysphagia | Cholinergic crisis (excessive dosing), mechanical bowel obstruction | GI symptoms (diarrhea, cramping, salivation = cholinergic excess); reduce dose if muscarinic symptoms | - | ROUTINE | ROUTINE | ROUTINE |
| Glycopyrrolate | IV | Cholinergic side effects of pyridostigmine | 1-2 mg :: IV :: BID :: 1-2 mg PO BID-TID; or 0.2 mg IV PRN for excessive secretions | Angle-closure glaucoma, urinary retention, tachycardia | Heart rate; urinary retention; dry mouth | - | ROUTINE | ROUTINE | ROUTINE |
| Acetaminophen | PO | Headache (IVIG-related or general) | 650-1000 mg :: PO :: q6h :: 650-1000 mg PO q6h; max 4g/day | Severe liver disease | LFTs if prolonged | STAT | ROUTINE | ROUTINE | STAT |
| Ondansetron | IV | Nausea (IVIG-related) | 4 mg :: IV :: q6h :: 4 mg IV/PO q6h PRN | QT prolongation | QTc monitoring | - | ROUTINE | - | ROUTINE |
| Diphenhydramine | IV | IVIG premedication | 25-50 mg :: IV :: - :: 25-50 mg IV/PO 30 min before IVIG infusion | Angle-closure glaucoma; avoid in elderly (anticholinergic) | Sedation | - | ROUTINE | - | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis | 40 mg :: SC :: daily :: 40 mg SC daily | Active bleeding, CrCl <30 (use UFH) | Platelets q3 days | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | DVT prophylaxis | Apply bilaterally on admission | Acute DVT | Skin checks | STAT | STAT | - | STAT |
| Pantoprazole | IV | GI prophylaxis (if on steroids) | 40 mg :: IV :: daily :: 40 mg IV/PO daily | Prolonged use risks (C. diff, osteoporosis) | GI symptoms | - | ROUTINE | ROUTINE | ROUTINE |
| Insulin sliding scale | - | Steroid-induced hyperglycemia | 140-180 mg :: - :: - :: Per institutional protocol; target glucose 140-180 mg/dL | Hypoglycemia | Blood glucose q6h or more frequent | - | ROUTINE | - | ROUTINE |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IV methylprednisolone (CPT 96365) | IV | - | 1000 mg :: IV :: daily :: 1000 mg IV daily x 3-5 days. CAUTION: steroids can transiently worsen MG in first 5-10 days — only initiate in monitored setting with respiratory support available. Some centers use slow oral prednisone uptitration instead | Uncontrolled diabetes (relative), active infection (relative) | FVC/NIF closely; glucose q6h; BP; GI prophylaxis | - | URGENT | - | URGENT |
| Prednisone (oral uptitration) | PO | - | 10-20 mg :: PO :: daily :: Start 10-20 mg PO daily; increase by 10 mg every 3-5 days to target 1 mg/kg/day (max 60-80 mg); maintain for 4-8 weeks, then slow taper over months | Active infection, uncontrolled DM (relative) | Glucose, BP, weight, bone density, mood; GI prophylaxis; PJP prophylaxis if prolonged high-dose | - | ROUTINE | ROUTINE | - |
| Second course IVIG or PLEX | - | - | Repeat standard dosing if inadequate response to first course; wait 2-4 weeks between courses | Same as initial | Same as initial | - | URGENT | - | URGENT |
| Eculizumab | IV | - | 900 mg :: IV :: - :: 900 mg IV q1 week x 4 weeks, then 1200 mg IV q2 weeks; for AChR-positive refractory generalized MG | Unresolved Neisseria meningitidis infection; must vaccinate ≥2 weeks before starting | Meningococcal infection; complement levels; CBC | - | EXT | ROUTINE | - |
| Efgartigimod (Vyvgart) | IV | - | 10 mg/kg :: IV :: - :: 10 mg/kg IV weekly x 4 weeks per cycle; repeat cycles based on clinical response; for AChR-positive generalized MG | Active infection, IgG <2 g/L | IgG levels (target reduction); infection signs; CBC | - | EXT | ROUTINE | - |
| Rituximab | IV | - | 375 mg/m2 :: IV :: - :: 375 mg/m2 IV weekly x 4 weeks OR 1000 mg IV x 2 doses 2 weeks apart; especially effective in MuSK-positive MG | Active infection, hepatitis B (reactivation risk — screen first) | CD20 count, immunoglobulins q3 months; hepatitis B screening; PML risk (rare) | - | EXT | ROUTINE | - |

### 3D. Disease-Modifying or Chronic Therapies

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Azathioprine | PO | - | 50 mg :: PO :: daily :: Start 50 mg PO daily; increase by 50 mg every 1-2 weeks to target 2-3 mg/kg/day; onset of effect 6-12 months | - | TPMT deficiency; pregnancy; concurrent allopurinol (dose reduce by 75%) | CBC weekly x 4 weeks, then biweekly x 2 months, then monthly; LFTs monthly x 3, then q3 months | - | ROUTINE | ROUTINE | - |
| Mycophenolate mofetil | PO | - | 500 mg :: PO :: BID :: Start 500 mg PO BID; increase to 1000 mg PO BID after 2 weeks; max 1500 mg BID; onset 6-12 months | - | Pregnancy (Category D), breastfeeding | CBC q1 week x 1 month, then biweekly x 2 months, then monthly; LFTs q3 months | - | ROUTINE | ROUTINE | - |
| Tacrolimus | PO | - | 3 mg :: PO :: daily :: 3 mg PO daily in 2 divided doses; target trough 5-10 ng/mL; onset 3-6 months | - | Renal failure, uncontrolled hypertension | Trough level q1 week initially, then monthly; Cr, K+, glucose, BP; drug interactions (CYP3A4) | - | - | ROUTINE | - |
| Cyclosporine | PO | - | 2-3 mg/kg :: PO :: - :: Start 2-3 mg/kg/day PO in 2 divided doses; target trough 100-200 ng/mL; onset 3-6 months | - | Renal failure, uncontrolled HTN, malignancy | Trough levels, Cr, BP, Mg, lipids monthly | - | - | ROUTINE | - |

---

## ⚠️ MEDICATIONS TO AVOID IN MYASTHENIA GRAVIS

| Drug Category | Specific Agents | Risk |
|---------------|-----------------|------|
| **Aminoglycosides** | Gentamicin, tobramycin, amikacin, streptomycin | NMJ blockade; can precipitate crisis |
| **Fluoroquinolones** | Ciprofloxacin, levofloxacin, moxifloxacin | NMJ blockade; FDA black box warning for MG |
| **Macrolides** | Azithromycin, erythromycin, clarithromycin | NMJ blockade (less than aminoglycosides but still risky) |
| **Beta-blockers** | Propranolol, metoprolol, atenolol (all) | Worsen NMJ transmission; can precipitate crisis |
| **Calcium channel blockers** | Verapamil (worst); diltiazem | Impair NMJ transmission |
| **Magnesium** (IV) | Magnesium sulfate | Directly blocks NMJ; can precipitate respiratory failure. Do NOT give IV Mg in MG unless life-threatening hypomagnesemia with close monitoring |
| **Telithromycin** | Ketek | Severe exacerbation; contraindicated |
| **D-Penicillamine** | Cuprimine | Can induce autoimmune MG |
| **Neuromuscular blockers** | Succinylcholine (unpredictable), non-depolarizing agents (prolonged effect at standard doses) | Use reduced doses of non-depolarizing agents if intubation required |
| **Botulinum toxin** | Botox, Dysport | Systemic weakness risk |
| **Statins** | All (rare) | Reported to unmask or worsen MG (rare; benefit usually outweighs risk) |
| **Immune checkpoint inhibitors** | Nivolumab, pembrolizumab, ipilimumab | Can trigger or exacerbate MG (potentially fatal); oncology must coordinate with neurology |
| **Quinine/Quinidine** | Antimalarials, antiarrhythmics | NMJ blockade |
| **Phenytoin** | Dilantin | Can worsen MG (mechanism unclear) |
| **Lithium** | Mood stabilizer | May worsen NMJ transmission |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neurology consultation (neuromuscular specialist if available) | STAT | STAT | - | STAT | All myasthenic crisis; treatment decisions; medication management |
| Pulmonology / Critical care | URGENT | URGENT | - | STAT | Declining respiratory function; ventilator management |
| Thoracic surgery | - | ROUTINE | ROUTINE | - | Thymoma evaluation; thymectomy planning (if not previously done) |
| Respiratory therapy | STAT | STAT | - | STAT | Bedside FVC/NIF monitoring; pulmonary toilet |
| Speech-language pathology (SLP) | URGENT | STAT | ROUTINE | URGENT | Dysphagia evaluation; aspiration prevention (bulbar weakness common in crisis) |
| Physical therapy (PT) | - | URGENT | ROUTINE | ROUTINE | Prevent deconditioning; safe mobilization; fall prevention |
| Occupational therapy (OT) | - | URGENT | ROUTINE | ROUTINE | ADL assessment; energy conservation techniques; adaptive equipment |
| Pharmacy (clinical pharmacist) | STAT | STAT | - | STAT | Medication reconciliation — review ALL medications for MG-unsafe drugs |
| Social work | - | ROUTINE | ROUTINE | - | Discharge planning; support resources; insurance for IVIG/PLEX |
| Palliative care | - | ROUTINE | - | ROUTINE | Goals of care discussion for refractory or elderly patients |
| Infectious disease | - | ROUTINE | - | - | If infection trigger unclear or complex; immunosuppressed patient management |
| Endocrinology | - | ROUTINE | ROUTINE | - | If concurrent thyroid disease; steroid-induced diabetes management |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Call 911 / Return to ED if: increasing difficulty breathing, trouble swallowing, choking on food or saliva, unable to hold head up, rapidly worsening weakness | STAT | STAT | ROUTINE |
| Carry MG crisis card / MedicAlert bracelet at all times | - | ROUTINE | ROUTINE |
| Bring complete medication list to every medical visit; alert ALL providers about MG diagnosis | - | ROUTINE | ROUTINE |
| NEVER take antibiotics, pain medications, or new prescriptions without checking with neurology | - | ROUTINE | ROUTINE |
| Take pyridostigmine 30-60 minutes before meals for best swallowing function | - | ROUTINE | ROUTINE |
| Avoid extreme heat (worsens weakness), overexertion, and sleep deprivation | - | ROUTINE | ROUTINE |
| Report any new medication prescribed by other providers to your neurologist | - | ROUTINE | ROUTINE |
| Infection prevention: hand hygiene, avoid sick contacts, up-to-date vaccinations (inactivated only if immunosuppressed; NO live vaccines) | - | ROUTINE | ROUTINE |
| Follow-up with neurology 1-2 weeks post-discharge; sooner if symptoms worsen | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Infection avoidance (number one trigger for crisis) | - | ROUTINE | ROUTINE |
| Influenza vaccination annually (inactivated) | - | - | ROUTINE |
| Pneumococcal vaccination | - | - | ROUTINE |
| COVID-19 vaccination (inactivated/mRNA; coordinate timing with immunosuppression cycle) | - | - | ROUTINE |
| NO live vaccines if on immunosuppression (MMR, varicella, live zoster, yellow fever) | - | ROUTINE | ROUTINE |
| Adequate sleep (fatigue worsens MG) | - | ROUTINE | ROUTINE |
| Stress management (emotional stress triggers exacerbation) | - | ROUTINE | ROUTINE |
| Moderate exercise as tolerated; avoid overexertion; rest periods during activity | - | ROUTINE | ROUTINE |
| Heat avoidance (hot weather, hot tubs, saunas worsen NMJ transmission) | - | ROUTINE | ROUTINE |
| Smoking cessation | - | ROUTINE | ROUTINE |
| Alcohol limitation (alcohol worsens weakness) | - | ROUTINE | ROUTINE |
| Eye protection (sunglasses, patching for diplopia; artificial tears for incomplete lid closure) | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Cholinergic crisis | EXCESSIVE pyridostigmine; salivation, lacrimation, urination, diarrhea, emesis (SLUDE); miosis; fasciculations; weakness WORSENS with additional pyridostigmine | Hold pyridostigmine — if strength improves, cholinergic; if worsens, myasthenic crisis. Clinical distinction is key |
| Guillain-Barré syndrome | Ascending paralysis, areflexia, albuminocytologic dissociation, preceding infection, no fatigability | NCS/EMG (demyelinating neuropathy vs NMJ); LP (elevated protein); no response to pyridostigmine |
| Lambert-Eaton myasthenic syndrome | Proximal weakness IMPROVES with repeated use; autonomic dysfunction (dry mouth); associated with small cell lung cancer; hyporeflexia | VGCC antibodies; NCS (incremental response with high-rate repetitive stimulation — opposite of MG) |
| Botulism | Descending paralysis (cranial → limbs); dilated pupils; foodborne or wound exposure; autonomic dysfunction | Stool/serum botulinum toxin; NCS (incremental); clinical history |
| ALS | Progressive weakness without fluctuation; upper AND lower motor neuron signs; no fatigability pattern; fasciculations | NCS/EMG (denervation); no response to IVIG/PLEX; no AChR antibodies |
| Brainstem stroke | Acute onset; cranial nerve findings; crossed findings (ipsilateral cranial nerve + contralateral limb); no fatigability | MRI DWI (restricted diffusion); CTA |
| MS exacerbation | CNS symptoms (optic neuritis, sensory level, cerebellar ataxia); dissemination in space and time; no NMJ findings | MRI brain/spine; LP (oligoclonal bands); no AChR antibodies |
| Thyroid storm | Severe weakness, tachycardia, fever, agitation, lid lag; thyroid hormone excess | TSH (suppressed), free T4 (elevated) |
| Periodic paralysis (hypo/hyperkalemic) | Episodic weakness triggered by meals, exercise, rest; normal between attacks | Serum potassium during attack; genetic testing |
| Conversion disorder / FND | Non-physiologic weakness; Hoover sign; distractible; no fatigable pattern | Normal NCS/EMG; normal antibodies; clinical exam |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Forced Vital Capacity (FVC) | STAT | STAT | ROUTINE | STAT | q4-6h on floor; q2-4h in ICU; q1-2h if declining | >20 mL/kg | If <20 mL/kg → intubate electively; if declining >30% → prepare for intubation |
| Negative Inspiratory Force (NIF) | STAT | STAT | ROUTINE | STAT | With FVC measurements | More negative than -30 cmH2O | If weaker than -30 → intubate |
| Single breath count | STAT | STAT | - | STAT | q4h as screening | Count to >20 | If <15 → correlate with FVC; if <10 → imminent failure |
| Oxygen saturation | STAT | STAT | - | STAT | Continuous in ICU; q4h on floor | ≥94% | LATE finding; do not rely on alone |
| Blood pressure | STAT | STAT | ROUTINE | STAT | q4h on floor; continuous in ICU | Stable | Autonomic dysregulation possible (less common than GBS) |
| Heart rate and rhythm | STAT | STAT | - | STAT | Continuous telemetry in ICU; q4h on floor | Normal sinus | Arrhythmia: cardiology consult |
| Neurologic exam (strength, bulbar function) | STAT | STAT | ROUTINE | STAT | q4-8h; MGFA post-intervention status at discharge | Improving or stable | If worsening → re-evaluate treatment; consider repeat IVIG/PLEX |
| Swallowing assessment | URGENT | STAT | ROUTINE | STAT | Daily | Safe oral intake | NPO; NG tube; modified diet |
| Blood glucose | - | ROUTINE | ROUTINE | ROUTINE | q6h if on steroids; BID if stable | <180 mg/dL | Insulin; reduce steroid if possible |
| Renal function (Cr, BUN) | - | ROUTINE | - | ROUTINE | Daily during IVIG; q48h otherwise | Stable | Hold IVIG; hydration |
| CBC | - | ROUTINE | ROUTINE | ROUTINE | Weekly during immunosuppression initiation; q3 months chronic | Normal | Dose adjust or hold immunosuppressant |
| LFTs | - | ROUTINE | ROUTINE | - | Monthly x3 for azathioprine/mycophenolate, then q3 months | Normal | Dose adjust or hold |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Exacerbation resolved; FVC >60% predicted and stable; able to swallow safely; adequate oral medications; no respiratory distress; stable immunotherapy regimen; follow-up within 1-2 weeks |
| Admit to floor (monitored bed) | Moderate exacerbation; FVC 20-30 mL/kg; requires IVIG or PLEX; dysphagia requiring modified diet; unable to maintain medications orally |
| Admit to ICU | Myasthenic crisis; FVC <20 mL/kg or declining rapidly; intubated; bulbar weakness with aspiration risk; post-operative thymectomy with respiratory concerns |
| Transfer to higher level | Need for PLEX not available; neuromuscular specialist consultation; need for ICU with neurology expertise |
| Inpatient rehabilitation | Significant weakness; unable to perform ADLs independently; able to tolerate 3h/day therapy |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| IVIG (2 g/kg over 2-5 days) for myasthenic crisis | Class I, Level A | [Zinman et al. (2007)](https://pubmed.ncbi.nlm.nih.gov/17353471/); [Gajdos et al. Cochrane (2012)](https://pubmed.ncbi.nlm.nih.gov/23235588/) |
| PLEX (5 exchanges) for myasthenic crisis | Class I, Level A | Cortese et al. (2011); Cochrane Review |
| IVIG and PLEX are equivalent for crisis | Class I, Level A | [Barth et al. (2011)](https://pubmed.ncbi.nlm.nih.gov/21562253/) |
| PLEX preferred for MuSK-positive MG | Class IIa, Level C | Expert consensus; [Evoli et al. (2003)](https://pubmed.ncbi.nlm.nih.gov/12821509/) |
| Hold pyridostigmine during intubation/crisis | Class IIa, Level C | Expert consensus |
| Avoid aminoglycosides, fluoroquinolones in MG | Class III (Harm) | FDA safety communication; multiple case reports |
| Avoid IV magnesium in MG | Class III (Harm) | NMJ blockade; case reports of respiratory failure |
| Steroids can transiently worsen MG (monitor closely when initiating) | Class IIa, Level B | Multiple observational studies |
| Thymectomy benefit in non-thymomatous MG | Class I, Level B | MGTX trial ([Wolfe et al. NEJM 2016](https://pubmed.ncbi.nlm.nih.gov/27509100/)) |
| Eculizumab for refractory AChR+ generalized MG | Class I, Level A | REGAIN trial ([Howard et al. Lancet Neurol 2017](https://pubmed.ncbi.nlm.nih.gov/29066163/)) |
| Efgartigimod for AChR+ generalized MG | Class I, Level A | ADAPT trial ([Howard et al. Lancet Neurol 2021](https://pubmed.ncbi.nlm.nih.gov/34146511/)) |
| Rituximab for MuSK-positive MG | Class IIa, Level B | [Hehir et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/28801338/); [Díaz-Manera et al. (2012)](https://pubmed.ncbi.nlm.nih.gov/22218276/) |
| 20/30/40 rule for intubation | Class IIa, Level C | Wijdicks & Klein (2017) |
| Bedside FVC superior to ABG for monitoring | Class I, Level B | Multiple studies; ABG changes are LATE findings |
| Azathioprine as first-line steroid-sparing | Class I, Level B | [Palace et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9633727/) |
| Mycophenolate as steroid-sparing | Class II, Level B | Mixed trial results but widely used |

---

**APPENDIX: MYASTHENIC vs CHOLINERGIC CRISIS**

| Feature | Myasthenic Crisis | Cholinergic Crisis |
|---------|-------------------|-------------------|
| Cause | Undertreated MG; infection trigger | Excessive pyridostigmine |
| Pupils | Normal | Miosis (constricted) |
| Secretions | Normal or decreased | Excessive salivation, tearing, bronchorrhea |
| Fasciculations | Absent | Present |
| GI symptoms | Absent | Diarrhea, nausea, vomiting, cramping |
| Response to pyridostigmine | Improves | Worsens |
| Treatment | IVIG/PLEX; increase immunotherapy | HOLD pyridostigmine; supportive care |

**APPENDIX: MGFA CLINICAL CLASSIFICATION**

| Class | Description |
|-------|-------------|
| I | Ocular weakness only; may have weakness of eye closure. All other muscle strength is normal |
| II | Mild weakness affecting muscles other than ocular; may also have ocular weakness of any severity |
| IIa | Predominantly limb, axial muscles, or both; may have lesser involvement of oropharyngeal muscles |
| IIb | Predominantly oropharyngeal, respiratory muscles, or both; may have lesser or equal involvement of limb, axial muscles |
| III | Moderate weakness affecting muscles other than ocular; may also have ocular weakness of any severity |
| IIIa | Predominantly limb, axial muscles |
| IIIb | Predominantly oropharyngeal, respiratory muscles |
| IV | Severe weakness affecting muscles other than ocular |
| IVa | Predominantly limb, axial muscles |
| IVb | Predominantly oropharyngeal, respiratory (can include feeding tube, without intubation) |
| V | Intubation required to maintain airway (with or without mechanical ventilation) = MYASTHENIC CRISIS |
