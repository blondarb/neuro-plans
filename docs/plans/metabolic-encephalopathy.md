---
title: "Metabolic Encephalopathy"
description: "Clinical decision support for metabolic encephalopathy diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: approved
tags:
  - metabolic
  - encephalopathy
  - hepatic
  - uremic
  - critical-care
---

# Metabolic Encephalopathy

**VERSION:** 1.0
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Metabolic Encephalopathy

**ICD-10:** G93.41 (Metabolic encephalopathy), K72.90 (Hepatic failure, unspecified without coma), K72.91 (Hepatic failure, unspecified with coma), N18.6 (End-stage renal disease), E87.0 (Hyperosmolality and hypernatremia), E87.1 (Hypo-osmolality and hyponatremia), E16.2 (Hypoglycemia, unspecified), E03.5 (Myxedema coma), E87.2 (Acidosis), E87.5 (Hyperkalemia), E83.52 (Hypercalcemia)

**CPT CODES:** 80053 (CMP), 82947 (Blood glucose), 82374 (CO2/bicarbonate), 84295 (Sodium), 84520 (BUN), 82565 (Creatinine), 82140 (Ammonia), 82803 (ABG), 84443 (TSH), 84439 (Free T4), 82533 (Cortisol), 83735 (Magnesium), 85610 (PT/INR), 82784 (Serum albumin), 84255 (Thiamine), 80307 (Urine drug screen), 87040 (Blood culture), 89050 (CSF cell count), 89051 (CSF differential), 86592 (RPR), 70450 (CT head without contrast), 70553 (MRI brain with and without contrast), 95819 (EEG routine), 95950 (Continuous EEG), 62270 (Lumbar puncture), 74178 (CT abdomen/pelvis with contrast), 76700 (Liver ultrasound), 76775 (Renal ultrasound)

**SYNONYMS:** Metabolic encephalopathy, toxic-metabolic encephalopathy, hepatic encephalopathy, uremic encephalopathy, electrolyte encephalopathy, hyponatremic encephalopathy, hepatic coma, portal-systemic encephalopathy, hyperammonemic encephalopathy, renal encephalopathy, myxedema coma, hypoglycemic encephalopathy

**SCOPE:** Evaluation and management of encephalopathy due to metabolic derangements in adults. Covers four major etiologies: (1) Hepatic encephalopathy, (2) Uremic encephalopathy, (3) Electrolyte-related encephalopathy (hyponatremia, hypercalcemia, hypernatremia), and (4) Endocrine/glucose-related encephalopathy (hypoglycemia, myxedema coma). Applies to ED, hospital, outpatient, and ICU settings. Excludes Wernicke encephalopathy (separate plan — nutritional/thiamine deficiency), hypertensive encephalopathy (separate plan — vascular mechanism), and drug-induced neurotoxicity (separate plan).

---

**DEFINITIONS:**
- **Hepatic Encephalopathy (HE):** Neuropsychiatric syndrome from liver failure; ranges from subclinical to coma; classified by West Haven criteria (Grade 0-4)
- **West Haven Criteria:** Grade 0 = subclinical (abnormal psychometrics); Grade 1 = mild confusion, sleep disturbance; Grade 2 = lethargy, moderate confusion; Grade 3 = somnolence, disorientation; Grade 4 = coma
- **Uremic Encephalopathy:** Altered mental status from accumulation of uremic toxins in renal failure; reversible with dialysis
- **Hyponatremic Encephalopathy:** Cerebral edema from acute hyponatremia (<120 mEq/L or rapid decline); risk of osmotic demyelination syndrome (ODS) with overcorrection
- **Myxedema Coma:** Life-threatening decompensated hypothyroidism with altered mental status, hypothermia, and multi-organ failure

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

!!! danger "IDENTIFY AND TREAT THE UNDERLYING METABOLIC CAUSE"
    Metabolic encephalopathy is a **reversible** condition if the underlying cause is identified and corrected. The CMP is the single most important lab — it screens for hepatic, renal, electrolyte, and glucose derangements simultaneously.

!!! warning "CRITICAL SAFETY ALERTS"
    - **Thiamine BEFORE glucose:** Always give thiamine before dextrose if nutritional deficiency is suspected — glucose without thiamine can precipitate or worsen Wernicke encephalopathy
    - **Hyponatremia correction rate:** Maximum 8 mEq/L in 24 hours — overcorrection causes irreversible osmotic demyelination syndrome (ODS)
    - **Ammonia correlation:** Ammonia levels correlate poorly with HE severity — do NOT withhold treatment based on normal ammonia

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential (CPT 85025) | Infection workup (precipitant of HE); anemia; thrombocytopenia (cirrhosis, DIC) | Normal WBC; platelets >50,000; no left shift | STAT | STAT | ROUTINE | STAT |
| CMP (BMP + LFTs) (CPT 80053) | THE key lab — renal function, hepatic function, electrolytes, glucose, calcium simultaneously; identifies hepatic, uremic, electrolyte, and glucose-related etiologies | Identify specific derangement(s) | STAT | STAT | STAT | STAT |
| Ammonia (venous) (CPT 82140) | Hepatic encephalopathy; collect on ice, analyze within 30 min; elevated >35 micromol/L suggestive of HE | <35 micromol/L (normal); note: correlates poorly with severity | STAT | STAT | ROUTINE | STAT |
| Blood glucose (CPT 82947) | Hypoglycemic encephalopathy; rapid bedside check followed by lab confirmation | >60 mg/dL (normal); <60 mg/dL = hypoglycemia requiring treatment | STAT | STAT | STAT | STAT |
| Serum sodium (CPT 84295) | Hyponatremic or hypernatremic encephalopathy; note rate of change matters more than absolute value | 136-145 mEq/L; <120 mEq/L = severe hyponatremia; >160 mEq/L = severe hypernatremia | STAT | STAT | STAT | STAT |
| BUN/Creatinine (CPT 84520, 82565) | Uremic encephalopathy; BUN >60-100 mg/dL correlates with neurologic symptoms | BUN <20; Cr <1.2 | STAT | STAT | STAT | STAT |
| Serum osmolality (CPT 83930) | Osmolar gap; osmotic demyelination risk assessment; hyperosmolar states | 280-295 mOsm/kg | STAT | STAT | ROUTINE | STAT |
| Lactate (CPT 83605) | Tissue perfusion assessment; metabolic acidosis; sepsis screening | <2 mmol/L | STAT | STAT | - | STAT |
| ABG/VBG (CPT 82803) | Acid-base status; respiratory compensation; identify metabolic acidosis/alkalosis | Normal pH 7.35-7.45; identify specific acid-base disorder | URGENT | URGENT | - | STAT |
| Calcium, ionized (CPT 82330) | Hypercalcemic encephalopathy; adjusted calcium >14 mg/dL causes severe neurologic symptoms | Ionized Ca 4.6-5.3 mg/dL; total Ca 8.5-10.5 mg/dL | STAT | STAT | ROUTINE | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| TSH (CPT 84443), Free T4 (CPT 84439) | Myxedema coma; severe hypothyroidism causing encephalopathy | TSH normal (0.5-4.5 mIU/L); very elevated TSH with low free T4 = myxedema | URGENT | URGENT | ROUTINE | URGENT |
| Cortisol, AM (CPT 82533) | Adrenal crisis; adrenal insufficiency can cause encephalopathy and mimic metabolic causes | >18 mcg/dL (normal stress response); <3 mcg/dL = adrenal insufficiency | URGENT | URGENT | ROUTINE | URGENT |
| Magnesium (CPT 83735) | Correct cofactor deficiencies; hypomagnesemia lowers seizure threshold; common in alcoholics and cirrhosis | >2.0 mg/dL | STAT | STAT | ROUTINE | STAT |
| Phosphorus (CPT 84100) | Hypophosphatemia (refeeding, alcoholism); hyperphosphatemia (renal failure) | 2.5-4.5 mg/dL | STAT | STAT | ROUTINE | STAT |
| PT/INR (CPT 85610) | Hepatic synthetic function; coagulopathy assessment; pre-LP safety | INR <1.5 | STAT | STAT | ROUTINE | STAT |
| Serum albumin (CPT 82784) | Correct calcium for hypoalbuminemia (adjusted Ca = total Ca + 0.8 x (4.0 - albumin)); nutritional status | >3.5 g/dL | ROUTINE | ROUTINE | ROUTINE | ROUTINE |
| Thiamine level (CPT 84255) | Exclude Wernicke encephalopathy; Wernicke often coexists with hepatic encephalopathy in alcoholics | >70 nmol/L (normal) | ROUTINE | ROUTINE | ROUTINE | ROUTINE |
| Urine drug screen (CPT 80307) | Exclude intoxication; drug-induced encephalopathy in differential | Negative | STAT | STAT | ROUTINE | STAT |
| Blood cultures (CPT 87040) x 2 sets | Infection is common precipitant of hepatic encephalopathy; septic encephalopathy in differential | No growth | STAT | STAT | - | STAT |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Urine sodium, urine osmolality (CPT 84300, 83935) | SIADH vs cerebral salt wasting; guide hyponatremia management | SIADH: urine Na >40, urine osm >100; CSW: urine Na >40, volume depleted | URGENT | URGENT | ROUTINE | URGENT |
| Ammonia (serial, q12-24h) (CPT 82140) | Track response to lactulose/rifaximin therapy; trend more useful than single value | Declining trend with treatment | - | URGENT | - | STAT |
| 24h urine copper (CPT 82525), Ceruloplasmin (CPT 82390) | Wilson disease in young patients (<40) with unexplained hepatic encephalopathy | Ceruloplasmin >20 mg/dL; 24h urine Cu <40 mcg/day | - | EXT | EXT | EXT |
| Serum protein electrophoresis (CPT 86235) | Paraproteinemia; myeloma-related renal failure | Normal pattern | - | EXT | EXT | - |
| Anti-thyroid peroxidase (TPO) antibodies | Hashimoto encephalopathy (SREAT) differential | Negative; if positive, consider steroid-responsive encephalopathy | - | EXT | EXT | EXT |
| Serum manganese level | Chronic hepatic encephalopathy; manganese deposition in basal ganglia | Elevated in chronic liver disease | - | EXT | EXT | - |

---

### LUMBAR PUNCTURE

**Indication:** Consider LP if meningitis or encephalitis is in the differential (fever, meningismus, altered consciousness not explained by identified metabolic derangement). LP is NOT routinely required for metabolic encephalopathy diagnosis.
**Timing:** URGENT if infection suspected; defer until metabolic correction initiated and imaging reviewed
**Volume Required:** 10-15 mL (standard diagnostic)

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure (CPT 89050) | Elevated ICP assessment; pseudotumor in differential | 10-20 cm H2O (normal or mildly elevated in metabolic encephalopathy) | URGENT | ROUTINE | - | URGENT |
| Cell count (tubes 1 and 4) (CPT 89050) | Rule out meningitis/encephalitis | WBC <5; RBC 0 | URGENT | ROUTINE | - | URGENT |
| Protein (CPT 89051) | Mild elevation may occur; significantly elevated suggests infection or inflammation | 15-45 mg/dL (normal or mildly elevated in metabolic encephalopathy) | URGENT | ROUTINE | - | URGENT |
| Glucose with serum glucose (CPT 89051) | Rule out infectious meningitis | >60% of serum glucose | URGENT | ROUTINE | - | URGENT |
| Gram stain and culture (CPT 87070) | Rule out bacterial meningitis | No organisms | URGENT | ROUTINE | - | URGENT |
| HSV PCR (CPT 87529) | Rule out HSV encephalitis if clinical suspicion | Negative | URGENT | ROUTINE | - | URGENT |

**Special Handling:** CSF must be sent promptly for culture; ammonia is NOT measured in CSF; hold extra tube for additional studies if needed
**Contraindications:** Space-occupying lesion with mass effect on imaging; uncorrected coagulopathy (INR >1.4 or platelets <50,000); hemodynamic instability; local skin infection at puncture site

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast (CPT 70450) | STAT on presentation | Exclude structural cause (hemorrhage, mass, hydrocephalus, herniation); CT has low sensitivity for metabolic encephalopathy | Pregnancy (benefit outweighs risk if clinically indicated) | STAT | STAT | - | STAT |
| MRI brain with FLAIR/DWI (CPT 70553) | Within 24-48h | **Hepatic:** bilateral globus pallidus T1 hyperintensity (manganese deposition); **Uremic:** cortical/subcortical T2/FLAIR edema; **Hyponatremic:** diffuse cerebral edema; **ODS:** central pontine and/or extrapontine T2/FLAIR hyperintensity; **Hypoglycemic:** bilateral hippocampal, basal ganglia DWI restriction | Hemodynamic instability; non-MRI-conditional devices | URGENT | URGENT | ROUTINE | URGENT |
| EEG (routine or continuous) (CPT 95819, 95950) | STAT if seizure suspected; URGENT otherwise | **Hepatic:** triphasic waves (bilateral, frontally predominant); **Uremic:** triphasic waves, diffuse slowing; **All metabolic:** diffuse theta/delta slowing; exclude NCSE | None | URGENT | URGENT | ROUTINE | STAT |

**MRI Findings by Etiology:**
- **Hepatic encephalopathy (chronic):** Bilateral symmetric T1 hyperintensity in globus pallidus (manganese deposition); may be normal in acute HE
- **Uremic encephalopathy:** Bilateral cortical and subcortical T2/FLAIR hyperintensity; may involve basal ganglia
- **Hyponatremic encephalopathy:** Diffuse cerebral edema on FLAIR; if ODS develops: central pontine and/or extrapontine myelinolysis on T2/FLAIR (appears 2-4 weeks after overcorrection)
- **Hypoglycemic encephalopathy:** DWI restriction in hippocampi, basal ganglia, cortex (severe cases)
- **Myxedema coma:** Usually normal; may show diffuse cerebral edema

**EEG Findings:**
- **Triphasic waves:** Classic but not specific — seen in hepatic encephalopathy, uremic encephalopathy, and other metabolic causes
- **Diffuse slowing:** Theta then delta predominance correlates with encephalopathy severity
- **NCSE:** Must exclude non-convulsive status epilepticus, which can mimic metabolic encephalopathy

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT abdomen/pelvis with contrast (CPT 74178) | URGENT if hepatic etiology undetermined | Cirrhosis; portal hypertension; hepatocellular carcinoma; ascites; splenomegaly | Contrast allergy; renal impairment (benefit outweighs risk) | - | URGENT | ROUTINE | URGENT |
| Liver ultrasound with Doppler (CPT 76700) | Within 24-48h for hepatic etiology | Portal hypertension; portal vein thrombosis; hepatic parenchymal disease; ascites | None significant | - | URGENT | ROUTINE | URGENT |
| Renal ultrasound (CPT 76775) | Within 48h for uremic etiology | Renal size (small = chronic kidney disease); hydronephrosis; obstruction | None significant | - | ROUTINE | ROUTINE | ROUTINE |
| Chest X-ray (CPT 71046) | URGENT if respiratory compromise or aspiration risk | Aspiration pneumonia; pulmonary edema; pleural effusion (hepatic hydrothorax) | None | URGENT | ROUTINE | - | URGENT |

---

## 3. TREATMENT

### CRITICAL PRIORITIES IN ACUTE METABOLIC ENCEPHALOPATHY (First 60 Minutes)
1. **ABCs** — Protect airway if GCS <=8; assess respiratory status
2. **Bedside glucose** — If <60 mg/dL: give thiamine FIRST, then D50W immediately
3. **CMP** — The single most important lab to identify the metabolic cause
4. **Identify and treat the underlying derangement** — Correction of the metabolic cause is the definitive treatment
5. **Identify precipitants** — Infection, medications, GI bleeding, dehydration, noncompliance

### 3A. Immediate Stabilization

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Airway management / Intubation | - | GCS <=8 or inability to protect airway; respiratory failure | RSI per institutional protocol :: - :: once :: Intubate if GCS <=8, declining mental status with aspiration risk, or respiratory failure; head of bed 30 degrees post-intubation | N/A | Ventilator settings; continuous SpO2; ETCO2; neuro checks | STAT | STAT | - | STAT |
| IV Thiamine (CPT 96374) | IV | Give BEFORE dextrose in suspected nutritional deficiency (alcoholism, malnutrition, chronic liver disease); prevents Wernicke encephalopathy | 500 mg :: IV :: once :: 500 mg IV over 30 min; give BEFORE glucose administration; may continue 500 mg IV q8h x 3 days if Wernicke suspected | Known hypersensitivity (rare) | Anaphylaxis (rare); vital signs during infusion | STAT | STAT | - | STAT |
| IV Dextrose (D50W) (CPT 96374) | IV | Hypoglycemic encephalopathy (glucose <60 mg/dL); give AFTER thiamine | 25-50 mL :: IV :: once :: 25-50 mL D50W (12.5-25 g dextrose) IV push; recheck glucose in 15 min; repeat if still <60 mg/dL; start D10W drip if recurrent hypoglycemia | Hyperglycemia; adequate glucose | Bedside glucose q15 min until >100 mg/dL; then q1-2h | STAT | STAT | - | STAT |
| IV Normal saline (0.9% NaCl) (CPT 96360) | IV | Volume resuscitation for dehydration; hepatic encephalopathy precipitated by dehydration; uremic encephalopathy | Rate per clinical status :: IV :: continuous :: Bolus 500-1000 mL if dehydrated; maintenance per clinical assessment; avoid hypotonic fluids in hyponatremia unless directed | Volume overload; decompensated heart failure; severe hyponatremia (use hypertonic saline instead) | Fluid balance; electrolytes q4-6h; urine output | STAT | STAT | - | STAT |
| Naloxone (CPT 96374) | IV | Suspected opioid intoxication contributing to altered mental status | 0.4-2 mg :: IV :: q2-3min PRN :: 0.4-2 mg IV; may repeat every 2-3 min up to 10 mg total; consider infusion if recurrent sedation | Known hypersensitivity | Respiratory status; sedation level; withdrawal symptoms | STAT | STAT | - | STAT |

### 3B. Hepatic Encephalopathy -- Specific Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Lactulose (CPT 96374 if IV route needed) | PO/NG | First-line treatment for acute hepatic encephalopathy; osmotic laxative reduces ammonia absorption; titrate to 2-3 bowel movements per day | 30 mL :: PO :: q1-2h :: 30 mL (20 g) PO q1-2h until first bowel movement, then titrate to 2-3 bowel movements per day; maintenance 15-30 mL PO BID-TID | Galactosemia; bowel obstruction | Bowel movement count; stool consistency; electrolytes (dehydration risk); abdominal distension; mental status | STAT | STAT | ROUTINE | STAT |
| Lactulose enema | PR | Unable to take PO; obtunded patient; ileus with rectal access | 300 mL in 700 mL NS :: PR :: q6-8h :: 300 mL lactulose mixed in 700 mL normal saline as retention enema; retain 30-60 min; repeat q6-8h PRN | Rectal perforation risk; rectal surgery | Bowel output; electrolytes; abdominal exam | STAT | STAT | - | STAT |
| Rifaximin (CPT 96374) | PO | Add to lactulose for secondary prophylaxis of recurrent hepatic encephalopathy; first-line for prevention of HE recurrence (Bass 2010) | 550 mg :: PO :: BID :: 550 mg PO BID; continue indefinitely for secondary prophylaxis; use in combination with lactulose | C. difficile infection (use with caution); known hypersensitivity | Hepatic function; C. difficile symptoms; mental status | - | STAT | ROUTINE | STAT |
| Identify and treat HE precipitants | - | Precipitant correction is essential; most common: infection/SBP, GI bleeding, constipation, electrolyte abnormalities, dehydration, medication noncompliance, sedative use | Treat specific precipitant :: - :: - :: Screen for: infection (blood/urine cultures, diagnostic paracentesis for SBP); GI bleeding (CBC, stool guaiac); constipation; electrolyte abnormalities; dehydration; medication noncompliance; sedative/opioid use | N/A | Per precipitant identified | STAT | STAT | ROUTINE | STAT |
| L-ornithine L-aspartate (LOLA) | IV | Alternative/adjunct for hepatic encephalopathy; reduces ammonia via urea cycle activation | 20 g :: IV :: daily :: 20 g IV infusion daily x 3-5 days; alternative to or adjunct with lactulose | Known hypersensitivity; severe renal failure | Ammonia levels; mental status; nausea/vomiting | - | URGENT | - | URGENT |
| Zinc sulfate | PO | Adjunct therapy; zinc deficiency is common in cirrhosis and impairs urea cycle function | 220 mg :: PO :: BID :: 220 mg PO BID (50 mg elemental zinc per dose); long-term supplementation | GI intolerance | Zinc levels; copper levels (chronic use may cause copper deficiency); GI side effects | - | ROUTINE | ROUTINE | ROUTINE |
| Albumin infusion (CPT 96365) | IV | If spontaneous bacterial peritonitis (SBP) is the precipitant of HE; reduces mortality in SBP | 1.5 g/kg Day 1, then 1 g/kg Day 3 :: IV :: per protocol :: 1.5 g/kg (max 150 g) on Day 1 of SBP diagnosis, then 1 g/kg (max 100 g) on Day 3 | Volume overload; decompensated heart failure | Volume status; renal function; respiratory status | - | STAT | - | STAT |
| Liver transplant evaluation referral | - | Recurrent or refractory hepatic encephalopathy despite maximal medical therapy; MELD score assessment | Hepatology referral :: - :: - :: Refer to hepatology/transplant center for evaluation if recurrent Grade 3-4 HE despite lactulose + rifaximin compliance | Active substance abuse (per center criteria); advanced malignancy; severe cardiopulmonary disease | MELD score; transplant candidacy assessment | - | URGENT | ROUTINE | URGENT |

**Important:** Protein restriction is NOT recommended per EASL/AASLD 2014 guidelines (outdated practice); maintain dietary protein intake of 1.2-1.5 g/kg/day. Protein restriction can worsen sarcopenia and nutritional status in cirrhosis.

### 3C. Uremic Encephalopathy -- Specific Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Urgent hemodialysis (CPT 90935) | - | Definitive treatment for uremic encephalopathy; improvement expected within 24-48h of initiation | Per nephrology :: - :: per protocol :: Urgent hemodialysis; initial session may be shorter duration (2-3h) to avoid dialysis disequilibrium syndrome; standard sessions 3-4h thereafter | Hemodynamic instability (consider CRRT); severe coagulopathy; lack of vascular access | BUN, Cr, electrolytes pre/post dialysis; neurologic status; hemodynamics; dialysis adequacy (Kt/V) | STAT | STAT | - | STAT |
| Continuous renal replacement therapy (CRRT) (CPT 90945) | - | Uremic encephalopathy with hemodynamic instability; cannot tolerate intermittent hemodialysis | Per nephrology :: - :: continuous :: CRRT (CVVHD or CVVHDF) for hemodynamically unstable patients; slower solute clearance reduces risk of dialysis disequilibrium | Severe coagulopathy (citrate anticoagulation option); lack of central venous access | Electrolytes q4-6h; fluid balance; hemodynamics; filter patency; anticoagulation | - | - | - | STAT |
| Correct electrolyte abnormalities | IV/PO | Potassium, calcium, magnesium, phosphorus derangements in renal failure | Per specific abnormality :: IV/PO :: per protocol :: Correct hyperkalemia urgently (calcium gluconate, insulin/dextrose, kayexalate); correct hypocalcemia, hypomagnesemia, hyperphosphatemia per standard protocols | Per specific correction | Electrolytes q4-6h; ECG for hyperkalemia; cardiac monitoring | STAT | STAT | ROUTINE | STAT |
| Levetiracetam (CPT 96374) | IV/PO | Seizure management in uremic encephalopathy; renally cleared — dose adjust for renal function; preferred ASM in renal failure | 500-1000 mg :: IV/PO :: BID :: 500-1000 mg IV or PO BID; reduce dose 50% if CrCl <30 mL/min; supplemental dose after hemodialysis (250-500 mg) | Known hypersensitivity | Seizure monitoring; renal function; behavioral side effects; post-dialysis supplemental dosing | STAT | STAT | ROUTINE | STAT |
| Avoid nephrotoxic medications | - | Medication review to discontinue or adjust nephrotoxins | Review and discontinue :: - :: - :: Discontinue or dose-adjust: NSAIDs, aminoglycosides, contrast dye, ACE inhibitors/ARBs (in acute setting), metformin, lithium; pharmacy consult for renal dosing of all medications | N/A | Renal function; medication levels where applicable | STAT | STAT | ROUTINE | STAT |

**Important:** Avoid phenytoin in uremic encephalopathy — highly protein-bound with unreliable levels in hypoalbuminemia and renal failure; use levetiracetam as preferred ASM.

### 3D. Electrolyte Encephalopathy -- Specific Treatment

**HYPONATREMIA:**

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Hypertonic saline (3% NaCl) (CPT 96365) | IV | Acute (<48h) or symptomatic hyponatremia with neurologic symptoms (seizures, altered consciousness, cerebral edema) | 100-150 mL :: IV :: over 20 min :: 100-150 mL 3% NaCl IV over 20 min; may repeat x2 if persistent severe symptoms (seizures); MAXIMUM correction 8 mEq/L in first 24 hours | Hypervolemic hyponatremia with volume overload (relative — benefit outweighs risk if symptomatic) | Serum Na q2h during active correction; neurologic exam; urine output; watch for overcorrection | STAT | STAT | - | STAT |
| Chronic hyponatremia management (>48h) | PO/IV | Chronic hyponatremia (>48h or unknown duration) — correct slowly to avoid ODS | Correct at <=0.5 mEq/L per hour :: IV/PO :: per protocol :: Fluid restriction (1-1.5 L/day) first-line; salt tablets 1-3 g PO TID if needed; isotonic saline if hypovolemic; MAXIMUM 8 mEq/L correction in 24h | Overcorrection (causes ODS) | Serum Na q2-4h; strict I&O; neuro checks q4h; daily weight | STAT | STAT | ROUTINE | STAT |
| Tolvaptan (CPT 96374) | PO | SIADH-associated hyponatremia; euvolemic hyponatremia refractory to fluid restriction | 15 mg :: PO :: daily :: 15 mg PO daily; initiate in hospital only; titrate to 30 mg then 60 mg at >=24h intervals if Na not rising; discontinue fluid restriction when starting; max 30 days per FDA label | Hypovolemic hyponatremia; inability to sense or respond to thirst; anuria; concomitant strong CYP3A4 inhibitors; liver disease | Serum Na q6h for first 24h; strict I&O; hepatic function (risk of hepatotoxicity); limit treatment to 30 days | - | STAT | - | STAT |
| Desmopressin rescue (CPT 96374) | IV | Overcorrection of hyponatremia (Na rising >8 mEq/L in 24h) — prevents osmotic demyelination syndrome | 2 mcg :: IV :: once :: 2 mcg IV if sodium correction exceeds 8 mEq/L in 24h; re-lower sodium to safe correction rate; may give D5W 3-6 mL/kg/h concurrently | Fluid overload (use with caution) | Serum Na q1-2h; urine output; fluid balance | STAT | STAT | - | STAT |

**HYPERCALCEMIA:**

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IV Normal saline aggressive hydration (CPT 96360) | IV | First-line treatment for hypercalcemic encephalopathy; volume expansion promotes calciuresis | 200-300 mL/h :: IV :: continuous :: 200-300 mL/h NS initially; adjust for volume status and cardiac function; target urine output 200-300 mL/h | Decompensated heart failure; severe volume overload | Fluid balance; urine output q1h; electrolytes q4-6h; calcium q6h; cardiac monitoring | STAT | STAT | - | STAT |
| Calcitonin (CPT 96372) | SC/IM | Rapid onset (hours) but temporary effect; bridge therapy while awaiting bisphosphonate onset | 4 IU/kg :: SC/IM :: q12h :: 4 IU/kg SC or IM q12h; onset 4-6h; tachyphylaxis develops within 48h; use as bridge to bisphosphonate effect | Known hypersensitivity; prior anaphylaxis | Calcium q6-12h; allergic reaction monitoring; effect wanes after 48h | STAT | STAT | - | STAT |
| Zoledronic acid (CPT 96365) | IV | Definitive treatment for moderate-severe hypercalcemia; onset 2-4 days, duration weeks | 4 mg :: IV :: once :: 4 mg IV over 15 min; onset 2-4 days; may repeat in 7 days if inadequate response; renal dose adjustment if CrCl <30 | Severe renal impairment (CrCl <35 mL/min — use with caution); pregnancy | Renal function (Cr at 48h and 1 week); calcium q24h; phosphorus; magnesium | - | URGENT | - | URGENT |
| Loop diuretics (Furosemide) | IV | ONLY after adequate hydration; promotes calciuresis; avoid if dehydrated | 20-40 mg :: IV :: q6-12h :: 20-40 mg IV q6-12h ONLY after adequate IV hydration established; avoid if volume depleted; monitor for electrolyte wasting | Volume depletion; hypokalemia; hypomagnesemia | Electrolytes q4-6h; urine output; fluid balance; potassium and magnesium replacement | - | URGENT | - | URGENT |

### 3E. Endocrine Encephalopathy -- Specific Treatment

**MYXEDEMA COMA:**

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Levothyroxine IV loading (CPT 96374) | IV | First-line thyroid hormone replacement for myxedema coma; IV route mandatory (PO absorption unreliable in myxedema) | 200-400 mcg :: IV :: loading :: 200-400 mcg IV loading dose, then 50-100 mcg IV daily until able to take PO; lower loading dose (200 mcg) in elderly or coronary artery disease; transition to PO when clinically improved | Uncorrected adrenal insufficiency (give hydrocortisone FIRST); acute MI; severe tachyarrhythmia | Heart rate; ECG; TSH and free T4 q24-48h; clinical response; watch for arrhythmia and myocardial ischemia | STAT | STAT | - | STAT |
| Hydrocortisone IV (CPT 96374) | IV | Empiric stress-dose steroids until adrenal insufficiency excluded; coexistent adrenal insufficiency common in myxedema; give BEFORE levothyroxine | 100 mg :: IV :: q8h :: 100 mg IV q8h; give BEFORE or concurrent with levothyroxine loading; continue until ACTH stimulation test excludes adrenal insufficiency; taper when stable | Active untreated infection (relative — benefit outweighs risk); GI hemorrhage (relative) | Blood glucose q6h; electrolytes; cortisol levels; signs of infection | STAT | STAT | - | STAT |
| Supportive care: Passive rewarming | - | Hypothermia management in myxedema coma; avoid active rewarming (causes vasodilation and cardiovascular collapse) | Passive rewarming only :: - :: continuous :: Warm blankets, warm IV fluids, warm humidified oxygen; avoid active external rewarming (heating blankets, warm bath) as it causes peripheral vasodilation and cardiovascular collapse | N/A | Core temperature q1-2h; hemodynamics; expect slow rise over 24-48h | STAT | STAT | - | STAT |
| Mechanical ventilation | - | Respiratory failure from hypoventilation; CO2 narcosis; inability to protect airway | Per institutional protocol :: - :: continuous :: Intubate for respiratory failure (common in myxedema coma — hypoventilation, hypercapnia); avoid sedatives if possible | N/A | Ventilator settings; ABG q4-6h; ETCO2; weaning readiness | STAT | STAT | - | STAT |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Hepatology/Gastroenterology for hepatic encephalopathy management, transplant evaluation, portal hypertension management | STAT | STAT | ROUTINE | STAT |
| Nephrology for uremic encephalopathy, dialysis initiation, renal replacement therapy planning | STAT | STAT | ROUTINE | STAT |
| Endocrinology for myxedema coma, adrenal crisis, complex endocrine derangements | URGENT | URGENT | ROUTINE | URGENT |
| Neurology for EEG interpretation, seizure management, differential diagnosis of encephalopathy, NCSE exclusion | URGENT | URGENT | ROUTINE | STAT |
| Critical Care / ICU for Grade 3-4 hepatic encephalopathy, myxedema coma, severe electrolyte emergencies requiring ICU-level monitoring | STAT | STAT | - | STAT |
| Pharmacy for medication reconciliation, renal dosing adjustments, drug interaction review, lactulose/rifaximin optimization | URGENT | URGENT | ROUTINE | URGENT |
| Nutrition/Dietetics for hepatic encephalopathy dietary planning (1.2-1.5 g/kg/day protein — NOT restricted); renal diet in uremia; fluid management | - | ROUTINE | ROUTINE | ROUTINE |
| Social work for discharge planning, medication access, substance abuse resources (if alcohol-related cirrhosis), dialysis transition support | - | ROUTINE | ROUTINE | - |
| Palliative care for refractory hepatic encephalopathy with advanced cirrhosis not transplant-eligible; goals of care discussion | - | ROUTINE | ROUTINE | ROUTINE |

### 4B. Patient / Family Instructions

**Hepatic Encephalopathy:**
- Lactulose adherence is critical — take as prescribed; titrate to 2-3 soft bowel movements per day
- Recognize early signs of recurrence: confusion, sleep disturbance, personality change — seek medical attention immediately
- Dietary protein is NOT restricted (common misconception) — maintain regular protein intake (1.2-1.5 g/kg/day)
- Avoid sedatives, opioids, benzodiazepines, and alcohol — these worsen encephalopathy
- Take rifaximin as prescribed for prevention of recurrence
- Keep all hepatology follow-up appointments; report any medication changes

**Uremic Encephalopathy:**
- Dialysis compliance is essential — do not skip or shorten dialysis sessions
- Report any confusion, excessive fatigue, muscle twitching, or seizures
- Medication review — avoid over-the-counter NSAIDs (ibuprofen, naproxen) and other nephrotoxins
- Follow dietary restrictions (fluid, potassium, phosphorus) as directed by your renal dietitian

**Hyponatremic Encephalopathy:**
- Fluid restriction education — understand daily fluid limit as prescribed
- Symptoms of overcorrection (ODS): difficulty speaking, swallowing, walking — these may develop days after treatment; report immediately
- Avoid excessive water intake; be cautious with diuretics
- Regular sodium monitoring as directed by your physician

**Myxedema Coma / Hypothyroidism:**
- Take levothyroxine daily as prescribed; do not discontinue without physician guidance
- Recognize symptoms of hypothyroidism: fatigue, cold intolerance, weight gain, constipation, cognitive slowing
- Follow-up thyroid function testing per endocrinology

### 4C. Lifestyle & Prevention

**Hepatic Encephalopathy:**
- Absolute alcohol cessation — alcohol worsens liver disease and precipitates HE
- Lactulose + rifaximin adherence for secondary prophylaxis
- SBP prophylaxis with daily norfloxacin or trimethoprim-sulfamethoxazole if indicated
- Vaccination: hepatitis A, hepatitis B, influenza, pneumococcal, COVID-19
- Avoid constipation — lactulose adherence; adequate hydration; dietary fiber
- Regular hepatology follow-up with MELD score monitoring

**Uremic Encephalopathy:**
- Dialysis compliance and adequacy monitoring (target Kt/V >=1.2)
- Fluid and dietary management per renal dietitian recommendations
- Nephrotoxin avoidance (NSAIDs, aminoglycosides, contrast dye when possible)
- Regular nephrology follow-up; transplant evaluation if eligible
- Blood pressure control to slow CKD progression

**Electrolyte Encephalopathy:**
- Regular electrolyte monitoring for patients on diuretics, SIADH management, or chronic hyponatremia
- Medication review to identify iatrogenic causes (thiazides, SSRIs, carbamazepine for hyponatremia)
- Adequate hydration; avoid extreme water restriction or water intoxication
- For hypercalcemia: treatment of underlying cause (malignancy, hyperparathyroidism); adequate hydration

---

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|-----------------------------|------------------------|
| Wernicke encephalopathy | Classic triad: confusion, ophthalmoplegia, ataxia; thiamine deficiency; often coexists with hepatic encephalopathy in alcoholics | Thiamine level; MRI (medial thalamic, mammillary body, periaqueductal changes); response to IV thiamine |
| Drug-induced neurotoxicity | Temporal relationship with medication initiation or dose change; medication history critical; serotonin syndrome, NMS, lithium toxicity | Drug levels; urine drug screen; medication reconciliation; specific drug levels (lithium, valproate, etc.) |
| Septic encephalopathy | Fever; hemodynamic instability; positive cultures; procalcitonin elevation; altered mental status with infection | Blood cultures; procalcitonin; lactate; CRP; imaging for infection source |
| CNS infection (meningitis/encephalitis) | Fever; meningismus; headache; focal neurologic signs; CSF pleocytosis | Lumbar puncture (elevated WBC, low glucose, elevated protein); CSF cultures; HSV PCR; MRI |
| Autoimmune encephalitis | Subacute onset; psychiatric symptoms; seizures; movement disorders; CSF antibodies | Autoimmune encephalitis panel (serum + CSF); MRI (temporal lobe FLAIR changes); EEG |
| Non-convulsive status epilepticus (NCSE) | Fluctuating altered consciousness; subtle motor signs (eye deviation, nystagmus, automatisms); may coexist with metabolic encephalopathy | Continuous EEG (definitive); trial of benzodiazepine with clinical and electrographic improvement |
| Posterior reversible encephalopathy syndrome (PRES) | Severe hypertension; seizures; visual changes; posterior predominant vasogenic edema on MRI | MRI (posterior white matter vasogenic edema); blood pressure assessment |
| Hepatic + Uremic combined | Hepatorenal syndrome patients may have combined metabolic causes | CMP; ammonia; BUN/Cr; address both liver and renal failure |
| Hypoxic-ischemic encephalopathy | History of cardiac arrest, respiratory failure, severe hypotension; DWI restriction on MRI | Clinical history; ABG; MRI brain (cortical ribbon, basal ganglia DWI restriction); EEG |
| Delirium (multifactorial) | Fluctuating attention; inattention as cardinal feature; often multifactorial in hospitalized elderly patients | CAM assessment; comprehensive metabolic workup; medication review; infection screen; environmental assessment |
| Structural lesion (stroke, tumor, SDH) | Focal neurologic deficits; asymmetric findings; acute onset (stroke) or progressive (tumor); unilateral imaging findings | CT head (hemorrhage, mass); MRI brain (stroke, tumor); CT angiography (large vessel occlusion) |

---

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|-------------------|---------------------|
| Neurologic exam (GCS, orientation, asterixis) | STAT | STAT | ROUTINE | STAT | q2-4h (acute); q shift (stable) | Improving or stable GCS; resolving asterixis | Escalate treatment; consider ICU if declining; repeat imaging |
| Ammonia (venous) | STAT | URGENT | ROUTINE | STAT | q12-24h during acute HE treatment | Declining trend (do not treat based on number alone) | Optimize lactulose; check for precipitants; rifaximin if not already on |
| Serum sodium | STAT | STAT | ROUTINE | STAT | q2h during active correction; q4-6h when stable | Correction rate <=8 mEq/L in 24h; target 130-135 mEq/L | Slow or stop correction if rate excessive; desmopressin rescue if overcorrection |
| BUN/Creatinine | STAT | STAT | ROUTINE | STAT | q12-24h; pre/post dialysis | Declining BUN with dialysis; Cr trending toward baseline | Adjust dialysis frequency; nephrology reassessment |
| Blood glucose | STAT | STAT | ROUTINE | STAT | q1h if on insulin drip; q4-6h otherwise | 100-180 mg/dL | Adjust insulin; D10W drip for recurrent hypoglycemia |
| Serum osmolality | STAT | URGENT | - | STAT | q6-12h during electrolyte correction | 280-295 mOsm/kg; osmolar gap <10 | Adjust correction rate; watch for ODS risk |
| EEG monitoring | - | URGENT | - | STAT | Continuous in ICU; spot check on floor | No seizures; no triphasic waves; improving background | Treat NCSE; adjust ASM; reassess metabolic cause |
| Bowel movement count (hepatic) | - | STAT | ROUTINE | STAT | Per BM (record every stool) | 2-3 soft BMs per day | Increase lactulose if <2 BMs/day; decrease if >4 BMs/day or diarrhea |
| Dialysis adequacy (Kt/V) | - | ROUTINE | ROUTINE | ROUTINE | Per dialysis session | Kt/V >=1.2 per session | Adjust dialysis prescription; increase duration or frequency |
| Fluid balance (I&O) | STAT | STAT | - | STAT | q1h ICU; q4h floor | Even balance or per clinical target | Adjust IV rate; diuretics if overloaded; bolus if depleted |
| Calcium (ionized) | STAT | STAT | ROUTINE | STAT | q6-12h during correction | Ionized Ca 4.6-5.3 mg/dL | Continue hydration and bisphosphonate; adjust calcitonin |
| TSH/Free T4 (myxedema) | - | URGENT | ROUTINE | URGENT | q24-48h during treatment | Rising free T4; declining TSH | Adjust levothyroxine dose; assess clinical response |
| Core temperature (myxedema) | - | - | - | STAT | q1-2h | Rising toward 36.5 C over 24-48h | Continue passive rewarming; assess for infection if not improving |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **ICU Admission** | Grade 3-4 hepatic encephalopathy (somnolence, coma); acute symptomatic hyponatremia with seizures or obtundation; myxedema coma; need for continuous EEG monitoring; hemodynamic instability requiring vasopressors; need for CRRT; GCS <=8 requiring intubation; active hypertonic saline infusion requiring q1-2h sodium monitoring |
| **Step-down / Telemetry** | Grade 2 hepatic encephalopathy improving on lactulose; sodium correction requiring q4-6h monitoring; uremic encephalopathy initiating intermittent hemodialysis with improving mental status; post-ICU stabilization with ongoing IV medication needs |
| **General Medical Floor** | Grade 1-2 hepatic encephalopathy on stable lactulose regimen; mild-moderate chronic hyponatremia under fluid restriction; uremic encephalopathy with established dialysis schedule and improving cognition; stable electrolyte abnormalities being corrected |
| **Discharge Home** | Mental status returned to baseline; underlying metabolic derangement corrected or stable on outpatient regimen; reliable outpatient follow-up arranged; patient/family education completed; medications reconciled and available; for HE: lactulose and rifaximin prescribed, bowel regimen established; for uremia: dialysis schedule confirmed; for hyponatremia: sodium stable >=125 mEq/L and improving, fluid restriction understood |
| **Transfer to Higher Level of Care** | Need for liver transplant evaluation at transplant center; need for emergent dialysis at facility without nephrology; refractory encephalopathy not responding to standard treatment; need for specialized neurological evaluation not available at current facility |
| **Outpatient Follow-up** | Hepatology within 1-2 weeks (hepatic encephalopathy); Nephrology within 1 week (uremic encephalopathy); Endocrinology within 1-2 weeks (myxedema); Neurology within 2-4 weeks (EEG follow-up, seizure management); PCP within 1 week for all; repeat labs (sodium, BUN/Cr, ammonia, LFTs) within 3-7 days per etiology |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Lactulose is first-line treatment for overt hepatic encephalopathy | Level I (Meta-analysis) | Gluud LL et al. Lactulose, rifaximin or branched chain amino acids for hepatic encephalopathy. Cochrane Database Syst Rev 2017 (PMID 28493663) |
| Rifaximin added to lactulose reduces HE recurrence by 58% | Level I (RCT) | Bass NM et al. Rifaximin treatment in hepatic encephalopathy. N Engl J Med 2010;362:1071-81 (PMID 20197548) |
| EASL/AASLD Practice Guidelines for hepatic encephalopathy management | Level I (Guideline) | Vilstrup H et al. Hepatic encephalopathy in chronic liver disease: 2014 Practice Guideline by EASL and AASLD. Hepatology 2014;60:715-35 (PMID 25042402) |
| Protein restriction is NOT recommended in hepatic encephalopathy; maintain 1.2-1.5 g/kg/day | Level II (Guideline) | EASL/AASLD 2014 Guidelines; European Society for Clinical Nutrition (ESPEN) Guidelines on nutrition in liver disease 2019 (PMID 30170790) |
| Hyponatremia correction rate should not exceed 8 mEq/L in 24 hours to prevent ODS | Level II (Expert consensus/retrospective studies) | Sterns RH. Disorders of plasma sodium — causes, consequences, and correction. N Engl J Med 2015;372:55-65 (PMID 25551526); Sterns RH et al. Osmotic demyelination syndrome following correction of hyponatremia. N Engl J Med 1986 |
| European clinical practice guideline on diagnosis and treatment of hyponatremia | Level I (Guideline) | Spasovski G et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol 2014;170:G1-47 (PMID 24569125) |
| Tolvaptan for SIADH-associated hyponatremia (SALT trials) | Level I (RCT) | Schrier RW et al. Tolvaptan, a selective oral vasopressin V2-receptor antagonist, for hyponatremia. N Engl J Med 2006;355:2099-112 (PMID 17105757) |
| Desmopressin rescue for overcorrection of hyponatremia prevents ODS | Level III (Case series/expert opinion) | Sterns RH et al. Therapeutic relowering of the serum sodium in a patient after excessive correction of hyponatremia. Clin Nephrol 2009 (PMID 26444023) |
| Uremic encephalopathy is reversible with dialysis; pathophysiology review | Level III (Review) | Burn DJ, Bates D. Neurology and the kidney. J Neurol Neurosurg Psychiatry 1998;65:810-21 (PMID 9854954); Seifter JL, Samuels MA. Uremic encephalopathy and other brain disorders associated with renal failure. Semin Neurol 2011 (PMID 21590621) |
| Myxedema coma management: IV levothyroxine loading with stress-dose steroids | Level III (Expert consensus/case series) | Wall CR. Myxedema coma: diagnosis and treatment. Am Fam Physician 2000;62:2485-90 (PMID 10695693); Jonklaas J et al. ATA Guidelines for Hypothyroidism 2014 (PMID 25266247) |
| L-ornithine L-aspartate (LOLA) for hepatic encephalopathy | Level I (Meta-analysis) | Butterworth RF et al. L-ornithine L-aspartate for the treatment of hepatic encephalopathy in cirrhosis: meta-analysis. Dig Dis 2018 (PMID 30625503); Goh ET et al. L-ornithine L-aspartate for prevention and treatment of hepatic encephalopathy. Cochrane Database Syst Rev 2018 (PMID 29762873) |
| ODS prevention: slow correction and desmopressin rescue strategy | Level II (Retrospective cohort/expert consensus) | Sterns RH. Treatment of severe hyponatremia. Clin J Am Soc Nephrol 2018;13:641-49 (PMID 29444771) |
| Continuous EEG monitoring for NCSE detection in encephalopathy | Level II (Guideline/observational) | Claassen J et al. Recommendations on the use of EEG monitoring in critically ill patients. Crit Care Med 2013 (PMID 23979365) |
| Zinc supplementation as adjunct in hepatic encephalopathy | Level II (RCTs) | Chavez-Tapia NC et al. A systematic review and meta-analysis of the use of oral zinc in the treatment of hepatic encephalopathy. Nutr J 2013 (PMID 23742732) |

---

## NOTES

- Hepatic encephalopathy is a clinical diagnosis — ammonia levels correlate poorly with severity; do NOT withhold treatment based on normal ammonia
- Hyponatremia correction: the RATE matters more than the target — overcorrection causes osmotic demyelination syndrome (ODS), which is irreversible
- Always give thiamine BEFORE glucose in suspected nutritional deficiency — glucose without thiamine can precipitate or worsen Wernicke encephalopathy
- Uremic encephalopathy is a diagnosis of exclusion — always rule out structural, infectious, and other metabolic causes
- Protein restriction is NOT recommended in hepatic encephalopathy (outdated practice); maintain 1.2-1.5 g/kg/day
- Triphasic waves on EEG are suggestive but NOT specific for hepatic encephalopathy — they can be seen in uremic encephalopathy, septic encephalopathy, and other metabolic causes
- Multiple metabolic derangements often coexist (e.g., hepatorenal syndrome, electrolyte abnormalities in cirrhosis) — search for and treat ALL contributing factors
- Lactulose is the cornerstone of hepatic encephalopathy treatment — maintain adherence for both acute treatment and secondary prophylaxis

---

## CHANGE LOG

**v1.0 (February 11, 2026)**
- Initial template creation
