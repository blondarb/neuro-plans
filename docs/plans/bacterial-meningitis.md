---
title: "Bacterial Meningitis"
description: "Clinical decision support for bacterial meningitis diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
---

# Bacterial Meningitis

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Bacterial Meningitis

**ICD-10:** G00.9 (Bacterial meningitis, unspecified), G00.0 (Hemophilus meningitis), G00.1 (Pneumococcal meningitis), G00.2 (Streptococcal meningitis), G00.3 (Staphylococcal meningitis), G00.8 (Other bacterial meningitis), G01 (Meningitis in bacterial diseases classified elsewhere), A39.0 (Meningococcal meningitis)

**SYNONYMS:** Bacterial meningitis, meningitis, acute meningitis, purulent meningitis, pyogenic meningitis, meningococcal meningitis, pneumococcal meningitis, CNS infection, brain infection, spinal meningitis

**SCOPE:** Acute community-acquired bacterial meningitis in adults. Covers emergency empiric antibiotics, dexamethasone adjunctive therapy, LP and CSF analysis, targeted therapy by organism, and complications management. Excludes viral meningitis, fungal meningitis, TB meningitis, healthcare-associated/post-surgical meningitis, and pediatric meningitis.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Blood cultures x2 (different sites) (CPT 87040) | STAT | STAT | - | STAT | MUST be drawn BEFORE antibiotics but do NOT delay antibiotics to obtain; positive in 50-70% of bacterial meningitis | Organism identification and sensitivities |
| CBC with differential (CPT 85025) | STAT | STAT | - | STAT | Leukocytosis with left shift; baseline; thrombocytopenia (DIC risk) | WBC elevated; neutrophilia |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | - | STAT | Electrolytes (SIADH: hyponatremia), renal/hepatic function for antibiotic dosing | Normal; watch Na |
| Procalcitonin (CPT 84145) | STAT | STAT | - | STAT | Highly sensitive for bacterial infection; helps distinguish bacterial from viral meningitis (>0.5 strongly suggests bacterial) | Elevated (>0.5 ng/mL bacterial; typically >2.0) |
| CRP (CPT 86140) | STAT | STAT | - | STAT | Inflammatory marker; helps monitor treatment response | Elevated |
| Lactate (CPT 83605) | STAT | STAT | - | STAT | Sepsis assessment; elevated in bacterial meningitis | <2 mmol/L (elevated suggests sepsis) |
| Coagulation panel (PT/INR, aPTT, fibrinogen) (CPT 85610+85730+85384) | STAT | STAT | - | STAT | DIC screening (meningococcemia); coagulopathy before LP | Normal; DIC: elevated PT/aPTT, low fibrinogen, elevated D-dimer |
| D-dimer (CPT 85379) | STAT | STAT | - | STAT | DIC assessment (especially meningococcemia) | Normal |
| Blood glucose (concurrent with LP) (CPT 82947) | STAT | STAT | - | STAT | Calculate CSF:serum glucose ratio | Paired with CSF glucose |
| Type and screen (CPT 86900) | STAT | ROUTINE | - | STAT | Potential need for blood products (DIC, sepsis) | On file |
| Point-of-care glucose (CPT 82962) | STAT | STAT | - | STAT | Hypoglycemia assessment; sepsis | >60 mg/dL |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum osmolality (CPT 83930) | URGENT | ROUTINE | - | URGENT | SIADH assessment (common complication) | 280-295 mOsm/kg |
| Urine osmolality and sodium | - | ROUTINE | - | ROUTINE | Confirm SIADH if hyponatremia | Urine osm >100, urine Na >40 in SIADH |
| Serum cortisol (random or AM) (CPT 82533) | URGENT | ROUTINE | - | URGENT | Adrenal insufficiency (Waterhouse-Friderichsen in meningococcemia) | >18 µg/dL (random stress level) |
| HIV 1/2 antigen/antibody (CPT 87389) | - | ROUTINE | - | - | Immunocompromise affects empiric coverage and differential | Negative |
| Complement levels (C5-C9, CH50, AH50) | - | ROUTINE | ROUTINE | - | Terminal complement deficiency predisposes to recurrent Neisseria meningitidis | Normal |
| Immunoglobulin levels (IgG, IgA, IgM) | - | ROUTINE | ROUTINE | - | Hypogammaglobulinemia predisposes to encapsulated organisms | Normal |
| TSH (CPT 84443) | - | ROUTINE | - | - | Thyroid dysfunction screen (critical illness) | Normal |
| Troponin (CPT 84484) | URGENT | ROUTINE | - | URGENT | Sepsis-associated myocardial injury | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Metagenomic next-generation sequencing (mNGS) of CSF | - | EXT | - | EXT | Culture-negative meningitis; prior antibiotic exposure; atypical organisms | Pathogen identification |
| Beta-D-glucan (serum) | - | EXT | - | EXT | If fungal meningitis suspected (immunocompromised) | Negative (<60 pg/mL) |
| Galactomannan (serum) | - | EXT | - | EXT | Aspergillus (immunocompromised) | Negative |
| Cryptococcal antigen (serum) (CPT 87327) | - | ROUTINE | - | ROUTINE | HIV/immunocompromised; chronic meningitis | Negative |
| RPR/VDRL (serum) (CPT 86592) | - | ROUTINE | ROUTINE | - | Neurosyphilis in differential | Negative |
| QuantiFERON-TB Gold | - | ROUTINE | - | ROUTINE | TB meningitis in high-risk patients | Negative |
| Skull base/sinus CT | - | ROUTINE | - | - | Recurrent meningitis: skull base fracture, CSF leak, sinusitis | No fracture or defect |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | ONLY if LP delay indications present (see below). Do NOT delay antibiotics for CT. CT BEFORE LP only if: immunocompromised, history of CNS disease, new seizure, papilledema, altered consciousness (GCS <10), focal neurologic deficit | Mass effect, hydrocephalus, abscess, herniation risk | Pregnancy (relative) |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | Within first hours | Pneumonia (S. pneumoniae source), ARDS | None significant |

**CRITICAL: DO NOT DELAY ANTIBIOTICS FOR IMAGING.** If CT is needed before LP, give empiric antibiotics + dexamethasone FIRST, then CT, then LP. Blood cultures before antibiotics if possible, but NEVER delay antibiotics >30 minutes from presentation.

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) | - | URGENT | - | URGENT | Within 24-48h or sooner if complications suspected | Meningeal enhancement, abscess, empyema, cerebritis, venous sinus thrombosis, hydrocephalus | Pacemaker, metallic implants |
| CT head with contrast (CPT 70460) | - | URGENT | - | URGENT | If MRI not available | Same as MRI (lower sensitivity) | Contrast allergy, renal impairment |
| MRV (MR venography) | - | ROUTINE | - | ROUTINE | If cerebral venous thrombosis suspected (persistent headache, focal signs, seizures) | Venous sinus thrombosis | Same as MRI |
| CT temporal bones / skull base | - | ROUTINE | ROUTINE | - | Recurrent meningitis; suspected CSF leak | Fracture, tegmen dehiscence, cholesteatoma | None significant |
| Echocardiogram (CPT 93306) | - | ROUTINE | - | - | If S. aureus or endocarditis suspected | Vegetations, embolic risk | None significant |
| Continuous EEG (CPT 95700) | - | URGENT | - | URGENT | If altered mental status persists despite treatment; suspected non-convulsive seizures | Seizure activity, status epilepticus | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT cisternogram | - | - | EXT | - | Recurrent meningitis with suspected CSF leak | CSF leak localization | Contrast allergy |
| Beta-2 transferrin (nasal/ear drainage) | - | ROUTINE | ROUTINE | - | Suspected CSF rhinorrhea or otorrhea | Positive = CSF leak | None |
| Intrathecal fluorescein | - | - | EXT | - | CSF leak localization (surgical planning) | Fluorescent leakage site | Allergy |
| ICP monitoring (EVD) | - | - | - | URGENT | If signs of elevated ICP, declining consciousness despite treatment | ICP <22 mmHg; CPP >60 | Coagulopathy (correct first) |

### LUMBAR PUNCTURE

**Indication:** Diagnostic — ALL patients with suspected bacterial meningitis. Do NOT delay antibiotics for LP.

**Timing:** STAT. If CT needed first, give antibiotics + dexamethasone BEFORE CT, then LP ASAP after CT clears for safety.

**Volume Required:** 15-20 mL (4 tubes minimum + extra for additional studies)

**Opening Pressure:** ALWAYS measure and document.

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | STAT | ROUTINE | - | Elevated in bacterial meningitis; monitor for elevated ICP | Typically 200-500 mm H2O (normal <200); markedly elevated suggests edema/hydrocephalus |
| Cell count with differential (tubes 1 AND 4) (CPT 89051) | STAT | ROUTINE | - | Bacterial: neutrophilic pleocytosis; tube 1 vs 4 differentiates traumatic tap | WBC >1000 cells/µL with >80% neutrophils (bacterial); WBC 100-10,000 typical |
| Protein (CPT 84157) | STAT | ROUTINE | - | Elevated in bacterial meningitis | Elevated (>100 mg/dL typical; often 100-500) |
| Glucose with paired serum glucose (CPT 82945) | STAT | ROUTINE | - | CSF:serum ratio <0.4 strongly suggests bacterial meningitis | Low (<40 mg/dL; CSF:serum ratio <0.4) |
| Gram stain (CPT 87205) | STAT | ROUTINE | - | Rapid identification; positive in 60-90% of untreated bacterial meningitis | Organisms identified (gram-positive diplococci = pneumococcus; gram-negative diplococci = meningococcus; gram-positive rods = Listeria; gram-negative rods = E. coli/Haemophilus) |
| Bacterial culture and sensitivity (CPT 87070) | STAT | ROUTINE | - | Gold standard for organism identification and antibiotic sensitivities; may be negative after antibiotics | Organism identified with sensitivities |
| BioFire FilmArray Meningitis/Encephalitis Panel (CPT 87483) | STAT | ROUTINE | - | Rapid multiplex PCR (14 pathogens in ~1 hour); especially valuable if prior antibiotics given | Identifies E. coli K1, H. influenzae, L. monocytogenes, N. meningitidis, S. agalactiae, S. pneumoniae, plus viruses (HSV, enterovirus, VZV, etc.) and Cryptococcus |
| Lactate (CSF) | STAT | ROUTINE | - | CSF lactate >3.5 mmol/L highly suggestive of bacterial (sensitivity ~93%, specificity ~96%); useful post-antibiotics when cultures may be negative | <3.5 mmol/L (bacterial typically >4.0) |
| HSV 1/2 PCR (CPT 87529) | STAT | ROUTINE | - | Exclude concurrent HSV encephalitis; do not miss treatable cause | Negative |
| Cryptococcal antigen (CSF) (CPT 87327) | - | ROUTINE | - | If immunocompromised or subacute presentation | Negative |
| AFB smear and culture (CPT 87116) | - | ROUTINE | - | If TB meningitis suspected (subacute, basilar enhancement, HIV) | Negative |
| VDRL (CSF) (CPT 86592) | - | ROUTINE | - | Neurosyphilis screen | Negative |
| Cytology (CPT 88104) | - | ROUTINE | - | If malignancy in differential | Negative |

**Special Handling:** Culture and Gram stain must be processed IMMEDIATELY. BioFire ME Panel provides results in ~1 hour. CSF lactate must be processed promptly (do not let sample sit).

**Contraindications to LP (perform CT first):** Immunocompromised, known CNS mass, new seizure (within 1 week), papilledema, GCS <10, focal neurologic deficit. Coagulopathy (INR >1.5, platelets <50K) — correct first if possible, but do NOT delay antibiotics.

---

## 3. TREATMENT

### ⚠️ CRITICAL: TIMING OF ANTIBIOTICS

**DO NOT DELAY ANTIBIOTICS.** Door-to-antibiotic time <30 minutes is the target. Each hour of delay increases mortality.

**Sequence:**
1. Blood cultures (if obtainable without delay)
2. Dexamethasone + empiric antibiotics STAT
3. CT head (ONLY if indicated — see criteria above)
4. LP (as soon as CT clears or immediately if no CT indications)

### 3A. Acute/Emergent — Empiric Therapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Dexamethasone (adjunctive — give BEFORE or WITH first antibiotic dose) (CPT 96374) | IV | - | 0.15 mg/kg :: IV :: q6h :: 0.15 mg/kg IV q6h x 4 days (typically 10 mg IV q6h). MUST be given BEFORE or simultaneously with first antibiotic dose. Greatest benefit for S. pneumoniae (reduces mortality and hearing loss). Discontinue if organism is NOT S. pneumoniae (some centers continue regardless) | Not proven beneficial if antibiotics already started >1h prior | Glucose q6h; GI prophylaxis; BP | STAT | STAT | - | STAT |
| Vancomycin IV (CPT 96365) | IV | - | 15-20 mg/kg :: IV :: load :: 15-20 mg/kg IV q8-12h (target trough 15-20 µg/mL or AUC/MIC 400-600); loading dose 25-30 mg/kg if severe. Covers penicillin-resistant S. pneumoniae, MRSA | Red man syndrome (infuse over ≥1h); renal impairment (dose adjust) | Trough levels before 4th dose; renal function daily; watch for nephrotoxicity and ototoxicity | STAT | STAT | - | STAT |
| Ceftriaxone IV (CPT 96374) | IV | - | 2 g :: IV :: q12h :: 2 g IV q12h. Covers S. pneumoniae (penicillin-sensitive), N. meningitidis, H. influenzae, gram-negative organisms | Cephalosporin allergy (cross-reactivity low with penicillin allergy); neonatal hyperbilirubinemia | CBC; LFTs; biliary sludge with prolonged use | STAT | STAT | - | STAT |
| Ampicillin IV (add if Listeria risk) (CPT 96374) | IV | - | 2 g :: IV :: q4h :: 2 g IV q4h. ADD to vancomycin + ceftriaxone if: age >50, immunocompromised, alcoholism, pregnancy. Covers Listeria monocytogenes (resistant to cephalosporins) | Penicillin anaphylaxis (use TMP-SMX as alternative for Listeria) | Rash; renal function | STAT | STAT | - | STAT |
| Acyclovir IV (empiric — until HSV excluded) (CPT 96365) | IV | - | 10 mg/kg :: IV :: q8h :: 10 mg/kg IV q8h. Add empirically if ANY suspicion of encephalitis (confusion, focal signs, seizures, temporal lobe changes). Discontinue when HSV PCR negative | Renal impairment (dose adjust); ensure adequate hydration | Renal function daily; adequate IV hydration (1 mL/kg/h); crystal nephropathy prevention | STAT | STAT | - | STAT |
| IV normal saline | IV | - | Isotonic fluid resuscitation for sepsis; maintenance fluids. Avoid hypo/hypernatremia | Volume overload | I/O; electrolytes q6-12h; watch for SIADH | STAT | STAT | - | STAT |
| Vasopressors: Norepinephrine | IV | - | 0.1-0.5 µg/kg/min IV; first-line for septic shock after fluid resuscitation | Only via central line | MAP target ≥65 mmHg; continuous arterial monitoring | - | - | - | STAT |

### 3B. Targeted Therapy by Organism (Once Identified)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Penicillin G (if penicillin-sensitive S. pneumoniae, MIC <0.06) | IV | S. pneumoniae (sensitive) | 4 million units IV q4h | - | Renal function; CBC | - | STAT | - | STAT |
| Ceftriaxone (if intermediate or unknown sensitivity) | IV | S. pneumoniae (intermediate) | 2 g :: IV :: q12h :: 2 g IV q12h; continue vancomycin until sensitivities confirm | - | Same as empiric | - | STAT | - | STAT |
| Penicillin G or ceftriaxone | IV | N. meningitidis | 2g :: IV :: q4h :: Penicillin G 4 MU IV q4h OR Ceftriaxone 2g IV q12h | - | Renal function | - | STAT | - | STAT |
| Ampicillin | IV | L. monocytogenes | 2 g :: IV :: q4h :: 2 g IV q4h (+ gentamicin 5 mg/kg/day IV for synergy in first 7-10 days, if renal function allows) | - | Renal function (especially with gentamicin); gentamicin levels | - | STAT | - | STAT |
| Ceftriaxone | IV | H. influenzae | 2 g :: IV :: q12h :: 2 g IV q12h | - | Standard | - | STAT | - | STAT |
| Ceftriaxone | IV | E. coli / gram-negative | 2 g :: IV :: q12h :: 2 g IV q12h; adjust per sensitivities | - | Standard | - | STAT | - | STAT |
| Cefepime | IV | Pseudomonas (nosocomial, immunocompromised) | 2 g :: IV :: q8h :: 2 g IV q8h | - | Renal function; neurotoxicity | - | STAT | - | STAT |
| Meropenem | IV | Extended-spectrum beta-lactamase (ESBL) producers or multi-drug resistant | 2 g :: IV :: q8h :: 2 g IV q8h | - | Renal function; seizure threshold | - | STAT | - | STAT |

### 3C. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Levetiracetam | IV | Seizure management (if seizures occur; NOT routine prophylaxis) | 1000-1500 mg :: IV :: BID :: 1000-1500 mg IV load; then 500-1000 mg IV/PO BID; max 3000 mg/day | Severe renal impairment (dose adjust) | Renal function; mood/behavioral changes | STAT | STAT | - | STAT |
| Lorazepam | IV | Active seizure (rescue) | 0.1 mg/kg :: IV :: - :: 0.1 mg/kg IV (max 4 mg); may repeat x1 | Respiratory depression | RR, SpO2 | STAT | STAT | - | STAT |
| Acetaminophen | IV | Fever reduction, headache | 650-1000 mg :: IV :: q6h :: 650-1000 mg PO/IV q6h; max 4g/day | Severe hepatic disease | Temperature; LFTs | STAT | STAT | - | STAT |
| Ibuprofen | PO | Headache (once stable) | 400-600 mg :: PO :: q6h :: 400-600 mg PO q6h with food | Renal impairment, GI bleed risk, coagulopathy | Renal function; GI symptoms | - | ROUTINE | - | - |
| Ondansetron | IV | Nausea/vomiting | 4 mg :: IV :: q6h :: 4 mg IV/PO q6h PRN | QT prolongation | QTc | STAT | ROUTINE | - | STAT |
| Mannitol 20% | IV | Elevated ICP management | 1-1.5 g/kg :: IV :: once :: 1-1.5 g/kg IV bolus; then 0.25-0.5 g/kg q4-6h | Anuria | Serum osm (<320); osmolar gap; renal function | STAT | - | - | STAT |
| Hypertonic saline 23.4% | IV | Elevated ICP (acute herniation) | 30 mL :: IV :: - :: 30 mL IV via central line over 10-20 min | No central access | Serum Na (target 145-155); osmolality | STAT | - | - | STAT |
| Pantoprazole | IV | GI prophylaxis (steroids + critical illness) | 40 mg :: IV :: daily :: 40 mg IV/PO daily | Prolonged use risks | GI symptoms | - | ROUTINE | - | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis | 40 mg :: SC :: daily :: 40 mg SC daily (start 24-48h after stable) | Active bleeding, DIC, coagulopathy | Platelets; coags | - | ROUTINE | - | ROUTINE |

### 3D. Close Contacts Prophylaxis (Public Health)

| Scenario | Agent | Dosing | Indication |
|----------|-------|--------|------------|
| N. meningitidis exposure | Ciprofloxacin | 500 mg PO x 1 dose (adults) | Close contacts within 7 days (household, kissing, shared utensils, healthcare workers with unprotected airway exposure) |
| N. meningitidis exposure | Rifampin | 600 mg PO q12h x 2 days (adults) | Alternative; avoid in pregnancy |
| N. meningitidis exposure | Ceftriaxone | 250 mg IM x 1 dose | Preferred in pregnancy |
| H. influenzae type b exposure | Rifampin | 20 mg/kg PO daily x 4 days (max 600 mg) | Household with child <4 years not fully vaccinated |

**Report meningococcal meningitis to local public health department IMMEDIATELY.**

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Infectious disease consultation | STAT | STAT | - | STAT | All bacterial meningitis; antibiotic optimization; complicated cases |
| Neurology consultation | URGENT | URGENT | - | STAT | Seizures, altered consciousness, focal deficits, ICP management |
| Neurosurgery consultation | - | URGENT | - | STAT | Hydrocephalus (EVD), brain abscess, subdural empyema, ICP management |
| Critical care/ICU team | STAT | STAT | - | STAT | Septic shock, respiratory failure, DIC, ICP management |
| ENT / Otolaryngology | - | ROUTINE | ROUTINE | - | Recurrent meningitis (CSF leak), concurrent sinusitis/mastoiditis source |
| Audiology | - | ROUTINE | ROUTINE | - | Hearing assessment before discharge (hearing loss in up to 30% S. pneumoniae) |
| Public health department | STAT | STAT | - | - | Meningococcal meningitis — mandatory reporting; contact tracing and prophylaxis |
| Speech-language pathology | - | ROUTINE | ROUTINE | - | Swallowing assessment if altered consciousness; cognitive assessment |
| Physical therapy | - | ROUTINE | ROUTINE | - | Mobilization, deconditioning prevention |
| Social work | - | ROUTINE | ROUTINE | - | Family support, discharge planning |
| Palliative care | - | ROUTINE | - | ROUTINE | Severe cases with poor prognosis; goals of care |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED if: worsening headache, fever recurrence, new confusion, seizure, neck stiffness, rash, vision changes | STAT | STAT | ROUTINE |
| Complete full antibiotic course (do NOT stop early even if feeling better) | - | ROUTINE | ROUTINE |
| Hearing test recommended 2-4 weeks after discharge | - | ROUTINE | ROUTINE |
| Vaccination: pneumococcal and meningococcal vaccines after recovery if not previously immunized | - | ROUTINE | ROUTINE |
| Close contacts should receive prophylactic antibiotics if N. meningitidis (public health will coordinate) | STAT | ROUTINE | - |
| Follow-up with infectious disease and neurology in 2-4 weeks | - | ROUTINE | ROUTINE |
| Report any new neurologic symptoms (hearing loss, balance problems, cognitive changes) | - | ROUTINE | ROUTINE |
| Avoid alcohol during antibiotic therapy | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Pneumococcal vaccination (PCV20 or PCV15 + PPSV23) if not previously completed | - | ROUTINE | ROUTINE |
| Meningococcal vaccination (MenACWY + MenB) for at-risk groups | - | ROUTINE | ROUTINE |
| Smoking cessation (upper respiratory tract colonization risk) | - | ROUTINE | ROUTINE |
| Alcohol moderation/cessation (immunocompromise, Listeria risk) | - | ROUTINE | ROUTINE |
| Splenectomy patients: ensure vaccinated (encapsulated organism risk) | - | ROUTINE | ROUTINE |
| Complement-deficient patients: meningococcal vaccination and booster schedule | - | ROUTINE | ROUTINE |
| Hand hygiene and respiratory etiquette education | - | ROUTINE | ROUTINE |
| Skull base fracture/CSF leak patients: surgical repair to prevent recurrence | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Viral meningitis | Less toxic; CSF: lymphocytic pleocytosis, normal glucose, mildly elevated protein; self-limited | CSF cell count (lymphocytes), normal glucose, BioFire ME panel (enterovirus most common), procalcitonin low |
| HSV encephalitis | Encephalitis (confusion, personality change, seizures, focal signs); temporal lobe involvement | MRI (temporal T2/FLAIR), CSF HSV PCR, EEG (PLEDs) |
| Tuberculous meningitis | Subacute (weeks), basilar meningitis, cranial neuropathies, HIV risk; CSF: lymphocytic, low glucose, very high protein | AFB smear/culture, TB PCR (GeneXpert), adenosine deaminase (ADA), chest X-ray (miliary pattern), PPD/IGRA |
| Fungal meningitis (Cryptococcus) | Subacute/chronic; immunocompromised (HIV CD4 <100); headache predominant; minimal CSF pleocytosis | CSF cryptococcal antigen (CrAg), India ink, fungal culture |
| Subarachnoid hemorrhage | Thunderclap headache; meningismus; NOT febrile initially; xanthochromia | CT head (blood), CSF RBC (tube 1 = tube 4), xanthochromia |
| Brain abscess | Focal deficits; fever + headache + focal signs (triad); subacute; seizures | MRI with contrast (ring-enhancing lesion with restricted diffusion), CT with contrast |
| Subdural empyema | Post-sinusitis/otitis; rapid deterioration; focal deficits; seizures | MRI/CT with contrast (extra-axial collection) |
| Autoimmune encephalitis | Subacute onset; psychiatric symptoms; seizures; young women; no fever initially | Autoimmune antibody panel (serum + CSF); MRI; EEG |
| Drug-induced aseptic meningitis | NSAID, IVIG, TMP-SMX, isoniazid exposure; self-limited after drug withdrawal | Drug history; CSF lymphocytic pleocytosis; sterile cultures; resolves with drug removal |
| Carcinomatous/leptomeningeal meningitis | Subacute; cranial neuropathies; known malignancy; CSF: low glucose, elevated protein, positive cytology | CSF cytology (repeat x3 for sensitivity); MRI with contrast (leptomeningeal enhancement) |
| Neurosarcoidosis | Chronic headache; cranial neuropathies (CN VII); hilar adenopathy; ACE level | Chest CT; serum ACE; CSF ACE; biopsy |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Neurologic exam (GCS, pupils, motor, meningismus) | STAT | STAT | - | STAT | q1h x 24h then q2-4h; more frequent if declining | Improving GCS; resolving meningismus | If GCS declining: STAT CT, ICP assessment, consider EVD |
| Temperature | STAT | STAT | - | STAT | q4h (q1h if febrile) | Afebrile within 48-72h of appropriate antibiotics | If persistent fever >72h: repeat cultures, imaging for abscess/empyema, drug fever, new infection |
| Blood pressure | STAT | STAT | - | STAT | q1h if sepsis; q4h if stable | MAP ≥65 mmHg; SBP >90 | Fluid resuscitation; vasopressors |
| Heart rate | STAT | STAT | - | STAT | q1-4h | 60-100 | Sepsis management |
| Serum sodium | STAT | STAT | - | STAT | q6-8h x 48h, then q12h | 135-145 mEq/L | If <130: SIADH likely → fluid restriction (1-1.2 L/day); if <120: 3% saline |
| Serum creatinine | - | ROUTINE | - | ROUTINE | Daily | Stable | Adjust antibiotics if rising; vancomycin nephrotoxicity |
| Vancomycin trough or AUC | - | ROUTINE | - | ROUTINE | Before 4th dose; then q24-48h until stable | Trough 15-20 µg/mL or AUC/MIC 400-600 | Adjust dosing; pharmacy consult |
| CBC | - | ROUTINE | - | ROUTINE | Daily x 3, then q48h | Improving WBC; stable platelets | If platelets dropping: DIC panel; if WBC not improving: reassess antibiotics |
| Coagulation panel (DIC monitoring) | STAT | ROUTINE | - | STAT | q6-12h if meningococcemia/DIC; daily otherwise | Normal PT, aPTT; fibrinogen >100 | FFP for INR >1.5; cryoprecipitate for fibrinogen <100; platelet transfusion if <50K with bleeding |
| CRP / procalcitonin | - | ROUTINE | ROUTINE | ROUTINE | q48-72h during treatment | Declining trend | If not declining by day 3-5: reassess; repeat LP; imaging |
| Seizure monitoring | STAT | STAT | - | STAT | Clinical observation; cEEG if altered consciousness | No seizure activity | Levetiracetam load; if refractory → status epilepticus protocol |
| Hearing assessment | - | ROUTINE | ROUTINE | - | Before discharge; repeat at 2-4 weeks | Normal hearing | Audiology referral; hearing aid evaluation if deficit |
| ICP (if EVD in place) | - | - | - | STAT | Continuous | ICP <22 mmHg; CPP 60-70 | Tiered ICP management: CSF drainage, osmotherapy, sedation |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Never discharge directly from ED with suspected bacterial meningitis. Discharge from hospital when: afebrile ≥48h, improving neurologic exam, able to take oral medications (IV-to-PO switch criteria met for some organisms), adequate outpatient IV access if completing IV course, reliable follow-up |
| Admit to floor (monitored) | Hemodynamically stable; GCS ≥13; no respiratory compromise; no DIC; no seizures |
| Admit to ICU | Septic shock; GCS <13 or declining; respiratory failure; DIC; refractory seizures; signs of elevated ICP; meningococcemia with purpura fulminans; need for vasopressors |
| Transfer to higher level | Need for neurosurgery (abscess, empyema, EVD); need for neuro-ICU expertise not available |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Empiric vancomycin + ceftriaxone +/- ampicillin | Class I, Level A | IDSA Guidelines ([Tunkel et al. CID 2004](https://pubmed.ncbi.nlm.nih.gov/15494903/); [van de Beek et al. NEJM 2006](https://pubmed.ncbi.nlm.nih.gov/16394301/)) |
| Dexamethasone before or with first antibiotic dose | Class I, Level A | [de Gans & van de Beek (NEJM 2002)](https://pubmed.ncbi.nlm.nih.gov/12432041/) — reduces mortality and hearing loss in S. pneumoniae |
| Do NOT delay antibiotics for imaging | Class I, Level A | IDSA Guidelines; multiple observational studies showing increased mortality with delay |
| CT before LP only for specific indications | Class I, Level A | [Hasbun et al. (NEJM 2001)](https://pubmed.ncbi.nlm.nih.gov/11742046/) — criteria for when to CT before LP |
| Blood cultures before antibiotics (if obtainable without delay) | Class I, Level B | IDSA Guidelines |
| BioFire ME Panel for rapid diagnosis | Class IIa, Level B | [Leber et al. (JCM 2016)](https://pubmed.ncbi.nlm.nih.gov/27335149/); FDA-cleared multiplex PCR |
| CSF lactate >3.5 mmol/L for bacterial vs viral | Class IIa, Level B | Meta-analysis: [Sakushima et al. (J Infect 2011)](https://pubmed.ncbi.nlm.nih.gov/21382412/) |
| Targeted antibiotic therapy by organism | Class I, Level A | IDSA Guidelines; organism-specific duration data |
| Close contact prophylaxis for meningococcal | Class I, Level A | CDC MMWR recommendations |
| Hearing assessment post-meningitis | Class I, Level B | High incidence of hearing loss (up to 30% S. pneumoniae) |
| Seizure treatment (not routine prophylaxis) | Class IIb, Level C | Expert consensus; no clear data supporting prophylaxis |
| Procalcitonin to differentiate bacterial from viral | Class IIa, Level B | Meta-analyses showing high sensitivity/specificity |
| Repeat LP at 48h if no clinical improvement | Class IIa, Level C | IDSA Guidelines |

---

**APPENDIX: CSF FINDINGS BY PATHOGEN TYPE**

| Parameter | Bacterial | Viral | TB | Fungal |
|-----------|-----------|-------|-----|---------|
| WBC (cells/µL) | 1,000-10,000 | 10-500 | 50-500 | 10-500 |
| Predominant cell | Neutrophils (>80%) | Lymphocytes | Lymphocytes | Lymphocytes |
| Protein (mg/dL) | 100-500 | 50-100 | 100-500 | 50-200 |
| Glucose (mg/dL) | <40 | Normal | <40 | <40 |
| CSF:serum glucose | <0.4 | >0.6 | <0.4 | <0.4 |
| Opening pressure | 200-500 | Normal-mildly elevated | 100-300 | 100-300 |
| Lactate (mmol/L) | >3.5 | <3.5 | >3.5 | Variable |
| Gram stain | Positive 60-90% | Negative | AFB rarely positive | India ink (Crypto) |

**APPENDIX: ANTIBIOTIC DURATION BY ORGANISM**

| Organism | Duration |
|----------|----------|
| N. meningitidis | 7 days |
| H. influenzae | 7 days |
| S. pneumoniae | 10-14 days |
| Group B Streptococcus | 14-21 days |
| L. monocytogenes | ≥21 days |
| Gram-negative bacilli (E. coli, Klebsiella) | 21 days |
| S. aureus | 14-21+ days (longer if complications) |
