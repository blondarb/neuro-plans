---
title: "Neurocysticercosis"
description: "Evidence-based clinical decision support for diagnosis, staging, antiparasitic treatment, seizure management, and follow-up of neurocysticercosis"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - cns-infection
  - parasitic
  - seizure
  - infectious-disease
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Neurocysticercosis

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Revised per checker/rebuilder pipeline (v1.1)

---

**DIAGNOSIS:** Neurocysticercosis

**ICD-10:** B69.0 (Cysticercosis of central nervous system), B69.1 (Cysticercosis of eye), B69.81 (Myositis in cysticercosis), B69.89 (Cysticercosis of other sites)

**CPT CODES:** 86682 (Cysticercosis antibody), 87015 (CSF concentration for infectious agents), 86235 (Nuclear antibody, extractable), 70553 (MRI brain with/without contrast), 70460 (CT head with contrast), 70450 (CT head without contrast), 95816 (EEG routine), 95819 (EEG with sleep), 95700-95720 (continuous EEG), 89051 (CSF cell count with differential), 84157 (CSF protein), 82945 (CSF glucose), 87205 (Gram stain), 96374 (IV push injection), 96365 (IV infusion), 61510 (craniotomy for excision), 62270 (lumbar puncture), 70551 (MRI brain without contrast), 77084 (MRI whole body screening), 93000 (ECG)

**SYNONYMS:** Neurocysticercosis, NCC, cerebral cysticercosis, brain cysticercosis, cysticercosis of the central nervous system, Taenia solium neurocysticercosis, pork tapeworm brain infection, parenchymal neurocysticercosis, racemose neurocysticercosis, ventricular cysticercosis, subarachnoid cysticercosis, spinal cysticercosis, calcified neurocysticercosis, cysticercal encephalitis

**SCOPE:** Diagnosis, staging, antiparasitic treatment, corticosteroid management, antiseizure medication selection, and follow-up of neurocysticercosis in adults. Covers all anatomic forms: parenchymal (vesicular, colloidal vesicular, granular nodular, calcified), ventricular (intraventricular), subarachnoid (racemose/basilar), and spinal neurocysticercosis. Includes Del Brutto diagnostic criteria, staging-based treatment approach, albendazole and praziquantel combination therapy, corticosteroid protocols, and surgical indications for hydrocephalus and intraventricular cysts. Excludes ocular cysticercosis (ophthalmology management), isolated subcutaneous cysticercosis without CNS involvement, and pediatric neurocysticercosis (dosing differences).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Eosinophilia in 10-30% of NCC; baseline for monitoring corticosteroid and antiparasitic toxicity; leukocytosis indicates co-infection or cysticercal encephalitis | Eosinophilia (peripheral) in minority; normal WBC does NOT exclude NCC |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Hepatic function for albendazole metabolism (hepatotoxicity risk); renal function baseline; electrolytes for seizure management; glucose monitoring during corticosteroid use | Normal; monitor LFTs during albendazole course |
| CRP (C-reactive protein) (CPT 86140) | STAT | STAT | ROUTINE | STAT | Assess inflammatory response to cyst degeneration; elevated during colloidal stage (active inflammation); monitor treatment-related inflammation | Variable; elevated during colloidal vesicular stage; declining with treatment |
| ESR (erythrocyte sedimentation rate) (CPT 85652) | URGENT | ROUTINE | ROUTINE | URGENT | Nonspecific inflammatory marker; mildly elevated; useful to distinguish from other infectious etiologies | Normal or mildly elevated |
| Serum cysticercosis antibody (EITB/immunoblot) (CPT 86682) | URGENT | STAT | ROUTINE | STAT | **Preferred serologic test** — enzyme-linked immunoelectrotransfer blot (EITB) sensitivity 94-98% for >1 viable cyst, specificity ~100%; sensitivity drops to 50-70% for single calcified lesion; positive supports diagnosis per Del Brutto criteria | Positive (reactive to >=1 of 7 glycoprotein antigens); negative does NOT exclude NCC with single lesion or calcified disease |
| Serum cysticercosis ELISA (CPT 86682) | URGENT | STAT | ROUTINE | STAT | Screening test; sensitivity 65-87%; specificity 75-100%; less specific than EITB; cross-reacts with other cestodes; use as adjunct if EITB unavailable | Positive supports diagnosis; confirm with EITB if available |
| PT/INR, aPTT (CPT 85610+85730) | STAT | STAT | - | STAT | Coagulopathy assessment before LP or surgical intervention | Normal; correct if abnormal before procedures |
| Blood glucose / HbA1c (CPT 82947+83036) | STAT | STAT | ROUTINE | STAT | Baseline before corticosteroid therapy; diabetes screening (steroid-induced hyperglycemia common) | HbA1c <6.5%; glucose <180 mg/dL during steroid use |
| Pregnancy test (urine/serum hCG) (CPT 81025) | STAT | STAT | ROUTINE | - | Albendazole is teratogenic (Category C); praziquantel is Category B; exclude pregnancy before initiating antiparasitic therapy | Negative required before antiparasitic therapy |
| Lactate (CPT 83605) | STAT | - | - | STAT | If sepsis or meningoencephalitis suspected; cysticercal encephalitis with systemic inflammatory response | <2 mmol/L |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum antigen detection (Ag-ELISA) for T. solium (CPT 86682) | - | ROUTINE | ROUTINE | ROUTINE | Detects circulating parasite antigen; positive indicates viable (living) cysts; useful for monitoring treatment response (declining antigen = cyst death); sensitivity 65-90% for multiple viable cysts | Positive indicates viable cysts; declining titer monitors treatment response; negative in single cyst or calcified disease |
| HIV 1/2 antigen/antibody (CPT 87389) | - | ROUTINE | ROUTINE | - | Immunocompromise assessment; HIV alters NCC presentation and treatment response; concurrent opportunistic infections complicate management | Negative; if positive: obtain CD4 count; affects treatment duration |
| Stool ova and parasites x3 (CPT 87177) | - | ROUTINE | ROUTINE | - | Identify intestinal Taenia solium carriage (taeniasis); present in 5-15% of NCC patients; treatment of intestinal tapeworm prevents ongoing autoinfection and community transmission | Negative; if positive: treat with niclosamide or praziquantel (single dose) for intestinal tapeworm |
| Taenia solium stool antigen (coproantigen) (CPT 87177) | - | ROUTINE | ROUTINE | - | More sensitive than microscopic stool O&P for detecting intestinal Taenia solium; important for public health (household contacts) | Negative; if positive: treat intestinal taeniasis |
| Serum sodium (CPT 84295) | STAT | ROUTINE | - | STAT | SIADH assessment (intracranial pathology); hyponatremia from cerebral salt wasting; important with corticosteroid use and ICP management | 135-145 mEq/L |
| Serum osmolality (CPT 83930) | URGENT | ROUTINE | - | URGENT | SIADH vs. cerebral salt wasting differentiation; relevant if on mannitol or hypertonic saline for elevated ICP | 280-295 mOsm/kg |
| Strongyloides serology (CPT 86682) | - | ROUTINE | ROUTINE | - | Screen before high-dose corticosteroids; Strongyloides hyperinfection syndrome is fatal during immunosuppression; endemic area overlap with NCC | Negative required before initiating prolonged corticosteroids; if positive: treat with ivermectin before steroids |
| LFTs (ALT, AST, bilirubin, alkaline phosphatase) (CPT 80076) | - | ROUTINE | ROUTINE | ROUTINE | Albendazole causes hepatotoxicity in 2-5%; monitor during and after treatment; praziquantel primarily hepatically metabolized | Normal; if ALT/AST >3x ULN: hold albendazole |
| Antiepileptic drug levels (CPT 80201-80299) | - | ROUTINE | ROUTINE | ROUTINE | If on concurrent AEDs; praziquantel levels reduced by 50-75% with enzyme-inducing AEDs (carbamazepine, phenytoin); albendazole sulfoxide levels reduced by dexamethasone co-administration | Therapeutic range for specific AED |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CSF cysticercosis antibody (EITB) (CPT 86682) | - | ROUTINE | - | ROUTINE | Higher sensitivity than serum for subarachnoid/ventricular NCC; important when serum EITB negative but clinical suspicion high; CSF detects intrathecal antibody production | Positive; intrathecal synthesis supports CNS NCC |
| CSF cysticercus antigen (Ag-ELISA) (CPT 86682) | - | ROUTINE | - | ROUTINE | Detects viable cysts in CSF; especially useful in subarachnoid (racemose) and ventricular NCC where serum tests less reliable; monitor treatment response | Positive indicates viable cysts in CSF space |
| CSF Taenia solium PCR (CPT 87798) | - | EXT | - | EXT | Molecular confirmation when serology equivocal; identifies species-specific DNA in CSF; limited availability | Positive; confirms T. solium DNA |
| Histopathology of excised cyst | - | ROUTINE | - | - | **Gold standard** per Del Brutto absolute criteria; identifies scolex, cyst wall, hooklets; confirms T. solium species; from surgical excision or endoscopic removal | Parasitic structures: scolex with rostellar hooklets, cyst wall with tegument and subtegumental cells |
| Brain biopsy / cyst excision with pathology | - | EXT | - | - | When diagnosis uncertain despite imaging and serology; to differentiate from tumor, abscess, or other granulomatous disease | Cysticercus larva identified; parasitic elements within cyst; surrounding inflammatory tissue |
| QuantiFERON-TB Gold (CPT 86480) | - | ROUTINE | ROUTINE | - | Tuberculoma is key differential for ring-enhancing lesions in endemic areas with geographic overlap; rule out concurrent TB meningitis | Negative |
| Toxoplasma IgG antibody (CPT 86777) | - | ROUTINE | ROUTINE | ROUTINE | Differential diagnosis in immunocompromised patients; ring-enhancing lesions; especially if HIV-positive | Negative; if positive with HIV: evaluate for concurrent toxoplasmosis |
| Serum galactomannan (CPT 87305) | - | EXT | - | EXT | If immunocompromised with atypical enhancement pattern; fungal abscess in differential | Negative (<0.5 index) |
| Complement levels (CH50, C3, C4) | - | EXT | EXT | - | Subarachnoid NCC triggers complement-mediated vasculitis; monitor if vasculitis suspected | Normal or decreased |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediate; first-line in ED for seizure, headache; **best for detecting calcified lesions** which MRI misses | **Calcified granulomas** (most common finding in endemic areas); single or multiple calcified nodules; perilesional edema around calcified lesion (seizure trigger); hydrocephalus; parenchymal cysts | Pregnancy (relative; benefit outweighs risk in acute setting) |
| CT head with contrast (CPT 70460) | STAT | STAT | - | STAT | Immediate if non-contrast shows edema or cysts; **ring enhancement identifies colloidal/granular stage** | Ring-enhancing lesion (colloidal vesicular stage); disc enhancement (granular nodular stage); calcified nodules with or without surrounding edema; **scolex** visible as eccentric hyperdense dot within cyst | Contrast allergy (pre-medicate); renal impairment |
| MRI brain with and without contrast (CPT 70553) | STAT | STAT | ROUTINE | STAT | Within 24h if CT suspicious; **gold standard** for NCC staging, cyst counting, scolex visualization, and identifying ventricular/subarachnoid disease | **Vesicular stage:** CSF-intensity cyst with scolex (bright dot on FLAIR); **Colloidal stage:** ring enhancement, perilesional edema, bright cyst fluid on FLAIR; **Granular nodular:** nodular/ring enhancement, decreasing edema; **Calcified:** T2 hypointense, perilesional edema possible; **Ventricular:** mobile cyst within ventricle; **Subarachnoid/racemose:** multilobulated grape-like cysts in cisterns | Pacemaker; metallic implants; claustrophobia (sedate) |
| Chest X-ray (CPT 71046) | - | ROUTINE | ROUTINE | - | Within first 24h if admitted | Soft tissue calcifications (subcutaneous/muscular cysticerci, "cigar-shaped" calcifications); pulmonary findings; baseline | None significant |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI spine with and without contrast (CPT 72156) | - | ROUTINE | ROUTINE | - | If spinal symptoms (radiculopathy, myelopathy); within 48-72h | Intradural extramedullary or intramedullary cysticercus; spinal leptomeningeal enhancement; arachnoiditis; subarachnoid cysts along spinal cord | Same as MRI brain |
| CT cisternography (CPT 70450) | - | EXT | - | - | If subarachnoid NCC suspected but standard imaging equivocal; enhances visualization of cisternal cysts | Racemose cysts in basal cisterns; filling defects in subarachnoid space | Intrathecal contrast allergy; elevated ICP |
| Plain radiographs of thighs and shoulders (CPT 73552+73030) | - | ROUTINE | ROUTINE | - | Screening for disseminated cysticercosis; confirm systemic disease | **Cigar-shaped calcifications** in muscles (pathognomonic for disseminated cysticercosis); supports NCC diagnosis per Del Brutto minor criteria | None |
| EEG (routine) (CPT 95816) | - | ROUTINE | ROUTINE | - | If seizure at presentation; baseline for patients starting AED therapy; evaluate for subclinical seizure activity | Focal epileptiform discharges corresponding to cyst location; generalized abnormalities; background slowing | None significant |
| Continuous EEG (cEEG) (CPT 95700) | - | URGENT | - | STAT | If altered mental status; concern for cysticercal encephalitis with non-convulsive seizures; refractory seizures | Seizure activity; non-convulsive status epilepticus | None significant |
| Echocardiogram (TTE) (CPT 93306) | - | EXT | EXT | - | If cardiac cysticercosis suspected (rare); disseminated disease | Intracardiac cysts (rare) | None significant |
| CT orbits (CPT 70480) | - | ROUTINE | ROUTINE | - | If visual symptoms or concern for ocular cysticercosis; **rule out ocular cysts before starting antiparasitic therapy** (treatment causes cyst inflammation that destroys vision) | Intraocular or periorbital cysticercus; retinal cyst; subretinal cyst | Contrast allergy |
| Ophthalmologic examination (fundoscopy) | URGENT | STAT | ROUTINE | - | **MANDATORY before starting antiparasitic treatment**; ocular cysticercosis is a contraindication to antiparasitic drugs; treatment-induced inflammation causes blindness | Intraocular cyst (vitreous, retinal, subretinal); papilledema (elevated ICP) | None |
| ECG (12-lead) (CPT 93000) | URGENT | ROUTINE | - | URGENT | Baseline; QTc assessment before medications; cardiac cysticercosis screen in disseminated disease | Normal; QTc prolongation risk with some AEDs | None |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| FIESTA/CISS MRI sequences (3D heavily T2-weighted) | - | ROUTINE | ROUTINE | - | For intraventricular cyst visualization; superior to standard MRI for small ventricular and subarachnoid cysts | Intraventricular cyst outline clearly delineated; scolex visible; cyst relationship to ventricular walls and foramina | Same as MRI brain |
| Phase-contrast cine MRI | - | EXT | - | - | If mobile intraventricular cyst suspected (ball-valve hydrocephalus); demonstrates cyst mobility with CSF flow | Mobile cyst causing intermittent foramen obstruction | Same as MRI brain |
| PET-CT brain (CPT 78816) | - | - | EXT | - | If diagnosis uncertain despite standard workup; differentiate from neoplasm | Cysticercal lesion: minimal FDG uptake (peripheral inflammatory ring); neoplasm: diffuse uptake | Pregnancy; uncontrolled diabetes |
| ICP monitoring (EVD) | - | - | - | URGENT | Acute hydrocephalus from ventricular cyst obstruction; declining consciousness from cysticercal encephalitis | ICP <22 mmHg; CPP >60 mmHg | Coagulopathy (correct first) |
| Neuroendoscopy (diagnostic/therapeutic) | - | URGENT | - | - | Intraventricular cyst removal; direct visualization and excision; avoids open craniotomy | Cyst visualized and excised intact; scolex identified; cyst-free ventricle post-procedure | Coagulopathy; inaccessible cyst location |

### LUMBAR PUNCTURE

**Indication:** Recommended when subarachnoid or ventricular NCC suspected; useful for CSF cysticercosis antibody/antigen testing; monitor treatment response in extraparenchymal disease. Generally NOT needed for isolated parenchymal calcified lesions.

**Timing:** URGENT if meningitis or elevated ICP suspected; ROUTINE for diagnostic workup of suspected subarachnoid/ventricular NCC.

**Volume Required:** 10-15 mL (standard diagnostic; additional for cysticercosis antibody and antigen testing)

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| Opening pressure (CPT 89050) | URGENT | ROUTINE | ROUTINE | URGENT | Elevated ICP common in ventricular and subarachnoid NCC; hydrocephalus assessment; baseline for monitoring | Normal 10-20 cm H2O; elevated in 50% of NCC with active inflammation or hydrocephalus |
| Cell count with differential (tubes 1 and 4) (CPT 89051) | URGENT | ROUTINE | ROUTINE | URGENT | CSF pleocytosis with lymphocytic/eosinophilic predominance; eosinophils (>5%) highly suggestive of parasitic infection; mononuclear predominance in chronic disease | WBC 5-500; **CSF eosinophilia (>5%) strongly supports parasitic etiology**; lymphocytic predominance common; polymorphonuclear in acute cyst rupture |
| Protein (CPT 84157) | URGENT | ROUTINE | ROUTINE | URGENT | Elevated in active inflammation and subarachnoid disease; markedly elevated in racemose NCC and arachnoiditis | Mildly to moderately elevated (50-300 mg/dL); markedly elevated (>200) in subarachnoid/racemose NCC |
| Glucose with paired serum (CPT 82945) | URGENT | ROUTINE | ROUTINE | URGENT | Low glucose indicates chronic meningitis (subarachnoid NCC, TB meningitis, fungal); usually normal in parenchymal NCC | Normal in parenchymal NCC; low (CSF/serum ratio <0.5) in subarachnoid NCC and chronic cysticercal meningitis |
| CSF cysticercosis antibody (EITB) (CPT 86682) | - | ROUTINE | ROUTINE | ROUTINE | Higher sensitivity than serum for subarachnoid and ventricular NCC; intrathecal antibody synthesis | Positive; supports active CNS cysticercosis |
| CSF cysticercosis antigen (Ag-ELISA) (CPT 86682) | - | ROUTINE | ROUTINE | ROUTINE | Detects viable cysts in CSF; serial monitoring of treatment response in extraparenchymal disease; declining antigen = successful treatment | Positive indicates viable cysts; serial decline with treatment |
| Gram stain and bacterial culture (CPT 87205+87070) | URGENT | ROUTINE | - | URGENT | Rule out bacterial meningitis as concurrent or alternative diagnosis | Negative |
| AFB smear and culture (CPT 87116) | - | ROUTINE | ROUTINE | ROUTINE | Rule out TB meningitis (key differential in endemic areas with overlapping epidemiology) | Negative |
| Fungal culture (CPT 87102) | - | ROUTINE | - | ROUTINE | Rule out fungal meningitis (Coccidioides, Histoplasma, Cryptococcus) if immunocompromised or endemic area | Negative |
| Cytology (CPT 88108) | - | ROUTINE | - | - | Rule out leptomeningeal carcinomatosis if atypical presentation or subarachnoid enhancement | No malignant cells |

**Special Handling:** CSF cysticercosis antibody and antigen testing are specialized assays; send to reference laboratory (CDC or designated centers). Eosinophilia in CSF (>5% eosinophils) is highly suggestive of parasitic CNS infection. Serial CSF antigen monitoring useful for subarachnoid/ventricular NCC treatment response.

**Contraindications:** Obstructive hydrocephalus (risk of herniation); large space-occupying cyst with mass effect; obtain imaging BEFORE LP. If hydrocephalus present, place EVD first.

---

## 3. TREATMENT

### CRITICAL: TREATMENT APPROACH

**Neurocysticercosis treatment is STAGING-DEPENDENT. Not all NCC requires antiparasitic therapy.** Treatment varies dramatically based on cyst viability, location, number, and host inflammatory response.

**MANDATORY PRE-TREATMENT STEPS:**
1. Ophthalmologic exam to rule out ocular cysticercosis (antiparasitic drugs cause intraocular inflammation leading to vision loss)
2. Brain imaging to stage disease and count cysts
3. Assess for hydrocephalus (treat hydrocephalus BEFORE antiparasitic therapy)
4. Start corticosteroids BEFORE or WITH antiparasitic drugs (prevent treatment-induced inflammation)
5. Start antiseizure medication if seizures present

**STAGING-BASED APPROACH:**

| Stage | Imaging Appearance | Treatment |
|-------|-------------------|-----------|
| Vesicular (viable cyst) | CSF-intensity cyst with scolex; no enhancement; minimal edema | Antiparasitic therapy + corticosteroids |
| Colloidal vesicular (degenerating) | Ring-enhancing cyst; perilesional edema; bright cyst fluid on FLAIR | Antiparasitic therapy + corticosteroids |
| Granular nodular (involuting) | Nodular enhancement; shrinking lesion; decreasing edema | Antiparasitic therapy for residual viable elements; corticosteroids for edema |
| Calcified (inactive) | Calcified nodule; no enhancement (unless perilesional edema) | NO antiparasitic therapy; AEDs for seizures; corticosteroids only if perilesional edema |
| Ventricular | Cyst within ventricle; hydrocephalus | Surgical removal (endoscopic preferred) followed by antiparasitic therapy; treat hydrocephalus first |
| Subarachnoid (racemose) | Multilobulated cysts in cisterns; hydrocephalus; arachnoiditis | Prolonged antiparasitic + high-dose corticosteroids; VP shunt if hydrocephalus |
| Spinal | Intradural cyst; leptomeningeal enhancement | Surgical excision if accessible; antiparasitic + corticosteroids |
| Cysticercal encephalitis | Massive edema; diffuse viable cysts; elevated ICP | **NO antiparasitic initially** (worsens edema); corticosteroids + ICP management first; antiparasitic only after edema controlled |

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Dexamethasone (CPT 96374) | IV | Pre-treatment corticosteroid BEFORE antiparasitic therapy; reduces treatment-induced inflammation from cyst degeneration; essential for cysticercal encephalitis; subarachnoid NCC with arachnoiditis | 0.15 mg/kg :: IV :: q6h :: 0.15 mg/kg IV q6h (typically 4-8 mg q6h); start 1-2 days BEFORE antiparasitic drugs; taper over 2-4 weeks based on clinical response; longer courses for subarachnoid NCC; dexamethasone increases albendazole sulfoxide levels by 50% | Active untreated fungal/bacterial infection; uncontrolled diabetes (relative); GI bleed (relative) | Glucose q6h during IV therapy; GI prophylaxis; blood pressure; mood changes; taper schedule; infection signs | STAT | STAT | - | STAT |
| Levetiracetam (seizure management) (CPT 96374) | IV/PO | First-line antiseizure medication for NCC-related seizures; no hepatic enzyme induction (avoids reducing praziquantel levels); seizures occur in 70-90% of parenchymal NCC | 1000 mg :: IV :: load then 500-1500 mg BID :: 1000 mg IV load, then 500-1000 mg IV/PO BID; titrate by 500 mg/day every 2 weeks to 1500 mg BID if seizures persist; max 3000 mg/day; does NOT interact with antiparasitic drugs | Severe renal impairment (dose adjust CrCl <30); behavioral side effects | Renal function; behavioral/mood changes (irritability, depression); CBC | STAT | STAT | ROUTINE | STAT |
| Mannitol 20% (CPT 96365) | IV | Elevated ICP from cysticercal encephalitis, large perilesional edema, or obstructive hydrocephalus; bridge to definitive treatment | 1 g/kg :: IV :: bolus then 0.25-0.5 g/kg q4-6h :: 1-1.5 g/kg IV bolus over 20 min; then 0.25-0.5 g/kg q4-6h PRN for ICP >22; hold if serum osm >320 | Anuria; severe dehydration; active intracranial bleeding | Serum osmolality (<320 mOsm/kg); osmolar gap; renal function; serum Na; I/O | STAT | URGENT | - | STAT |
| Hypertonic saline 23.4% | IV | Acute herniation from massive cerebral edema in cysticercal encephalitis; more sustained ICP reduction than mannitol | 30 mL :: IV :: once over 10-20 min via central line :: 30 mL via central line over 10-20 min; target Na 145-155 mEq/L; repeat PRN | No central access (causes tissue necrosis peripherally) | Serum Na q4-6h; osmolality; central line access confirmed | STAT | URGENT | - | STAT |
| Lorazepam (seizure rescue) | IV | Active seizure in NCC; breakthrough seizure during antiparasitic treatment | 4 mg :: IV :: push PRN seizure :: 0.1 mg/kg IV (max 4 mg) over 2 min; repeat x1 in 5 min if seizure continues; max 8 mg total | Respiratory depression; severe hypotension | Respiratory rate; SpO2; blood pressure; airway equipment at bedside | STAT | STAT | - | STAT |
| IV normal saline | IV | Maintenance fluids; avoid hypotonic solutions which worsen cerebral edema; euvolemia during corticosteroid therapy | 0.9% NaCl :: IV :: continuous at 75-125 mL/h :: Isotonic fluids only; avoid D5W and half-normal saline; maintain euvolemia | Volume overload; CHF | I/O; electrolytes daily; serum Na | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Acetaminophen | PO/IV | Headache management; fever control; avoid NSAIDs if concern for GI bleed during corticosteroid therapy | 1000 mg :: PO :: q6h PRN :: 650-1000 mg PO/IV q6h; max 4 g/day; IV route if unable to take PO | Severe hepatic disease (caution with concurrent albendazole hepatotoxicity) | Temperature; LFTs (especially with concurrent albendazole) | STAT | STAT | ROUTINE | STAT |
| Ondansetron | IV/PO | Nausea and vomiting (common with elevated ICP and antiparasitic therapy; albendazole commonly causes nausea) | 4 mg :: IV :: q6h PRN :: 4 mg IV/PO q6h PRN nausea; max 16 mg/day | QT prolongation; severe hepatic impairment (max 8 mg/day) | QTc if risk factors; hepatic function | STAT | ROUTINE | ROUTINE | STAT |
| Pantoprazole | IV/PO | GI prophylaxis during corticosteroid therapy; stress ulcer prevention in ICU; steroid-induced gastropathy prevention | 40 mg :: IV :: daily :: 40 mg IV/PO daily; discontinue when steroids stopped and no longer in ICU | Long-term use risks (C. diff, hypomagnesemia); only while on steroids | GI symptoms; discontinue when steroids tapered | - | ROUTINE | ROUTINE | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis; prolonged hospitalization and immobilization; steroid use increases VTE risk | 40 mg :: SC :: daily :: 40 mg SC daily; start 24h post-surgery if no active bleeding; hold if upcoming surgery | Active intracranial bleeding; recent craniotomy (<24h); coagulopathy; platelets <50K | Platelets q3 days (HIT monitoring); coagulation panel | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | Mechanical | DVT prophylaxis; apply on admission; use in conjunction with pharmacologic prophylaxis when safe | N/A :: Mechanical :: continuous :: Bilateral sequential compression devices; apply on admission; continue until fully ambulatory | Acute DVT in lower extremity; severe peripheral vascular disease | Skin integrity; proper fit; compliance | STAT | STAT | - | STAT |
| Fosphenytoin (seizure rescue second-line) | IV | Refractory seizure not responding to levetiracetam; status epilepticus; **NOTE: phenytoin/fosphenytoin is enzyme-inducing and reduces praziquantel levels by 50%** | 20 mg PE/kg :: IV :: load then 100 mg PE q8h :: 20 mg PE/kg IV at 150 mg PE/min; maintenance 100 mg PE q8h; target free phenytoin level 1-2 mcg/mL | Bradycardia; second/third-degree heart block; hypotension; reduces praziquantel levels | Continuous telemetry during load; free phenytoin level; LFTs; drug interactions with antiparasitic agents | STAT | STAT | - | STAT |
| Lacosamide | IV/PO | Second-line AED for NCC-related seizures; no enzyme induction (preferred over carbamazepine/phenytoin which reduce praziquantel levels) | 200 mg :: IV :: load then 100-200 mg BID :: 200 mg IV load, then 100-200 mg PO BID; max 400 mg/day; no significant drug interactions with antiparasitic agents | PR prolongation; second/third-degree AV block; severe hepatic impairment | ECG (PR interval); LFTs; cardiac rhythm | - | STAT | ROUTINE | STAT |

### 3C. Second-line/Refractory — Antiparasitic Therapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Albendazole | PO | **First-line antiparasitic** for viable parenchymal NCC (vesicular and colloidal stages); 1-2 viable cysts: albendazole monotherapy x 7-14 days; >2 viable cysts: combine with praziquantel; subarachnoid/racemose NCC: prolonged courses (months); take with fatty meal (increases absorption 5-fold) | 15 mg/kg/day :: PO :: divided BID (max 800 mg/day) :: 15 mg/kg/day PO divided BID (standard max 400 mg BID = 800 mg/day; up to 600 mg BID = 1200 mg/day for subarachnoid NCC or heavy cyst burden per ID specialist guidance); take with fatty meal; duration: 7-14 days for 1-2 parenchymal cysts; 10-14 days for >2 cysts (with praziquantel); weeks to months for subarachnoid NCC | **Ocular cysticercosis** (ABSOLUTE — causes vision loss); pregnancy (teratogenic); severe hepatic disease; cysticercal encephalitis with uncontrolled edema (treat edema first) | LFTs at baseline, day 7, day 14, then biweekly; CBC q2 weeks (leukopenia, thrombocytopenia); clinical response; repeat imaging at 3-6 months | - | STAT | ROUTINE | - |
| Praziquantel | PO | **Combined with albendazole** for >2 viable parenchymal cysts (combination more effective than either alone per RCTs); single agent if albendazole intolerance; **NOTE: levels reduced 50-75% by enzyme-inducing AEDs (carbamazepine, phenytoin) and by dexamethasone — increase dose or use cimetidine to boost levels** | 50 mg/kg/day :: PO :: divided TID x 10-14 days :: 50 mg/kg/day PO divided TID; take with fatty meal; combine with albendazole for >2 viable cysts; duration 10-14 days for parenchymal NCC; if on enzyme-inducing AEDs: increase dose to 100 mg/kg/day or add cimetidine 400 mg TID to inhibit metabolism | **Ocular cysticercosis** (ABSOLUTE); pregnancy (Category B but avoid during treatment); concurrent rifampin (reduces levels markedly); cysticercal encephalitis with uncontrolled edema | LFTs; clinical response; drug interactions (enzyme-inducing AEDs reduce levels by 50-75%); repeat imaging at 3-6 months | - | STAT | ROUTINE | - |
| Cimetidine (praziquantel booster) | PO | Inhibits CYP3A4 metabolism of praziquantel; increases praziquantel bioavailability 2-fold; essential when enzyme-inducing AEDs cannot be avoided | 400 mg :: PO :: TID :: 400 mg PO TID; start 1-2 days before praziquantel; continue throughout praziquantel course | Renal impairment (dose adjust); drug interactions (inhibits CYP3A4) | Drug interactions; renal function | - | ROUTINE | ROUTINE | - |
| Prednisone (oral steroid taper) | PO | Transition from IV dexamethasone; prolonged steroid course for subarachnoid NCC; maintenance anti-inflammatory therapy during outpatient antiparasitic treatment | 1 mg/kg :: PO :: daily :: 1 mg/kg/day PO (max 60 mg) then taper over 2-4 weeks for parenchymal NCC; for subarachnoid/racemose NCC: prolonged taper over months (years for chronic arachnoiditis) | Active infections; uncontrolled diabetes; GI ulcer; osteoporosis (relative for prolonged use) | Glucose; blood pressure; weight; bone density if prolonged use (>3 months); mood changes; infection signs; adrenal suppression | - | ROUTINE | ROUTINE | - |
| Methotrexate (steroid-sparing agent) | PO | Steroid-sparing agent for subarachnoid/racemose NCC requiring prolonged anti-inflammatory therapy (months to years); allows corticosteroid taper while maintaining anti-inflammatory effect | 7.5-20 mg :: PO :: weekly :: Start 7.5 mg PO weekly; titrate to 15-20 mg weekly as tolerated; supplement with folic acid 1 mg daily (except on MTX day); onset of effect 4-6 weeks | Pregnancy (teratogenic); severe hepatic/renal impairment; immunodeficiency; bone marrow suppression; interstitial lung disease | CBC with differential monthly; LFTs monthly; renal function monthly; folic acid compliance; pulmonary symptoms | - | - | ROUTINE | - |
| Niclosamide | PO | Treatment of intestinal Taenia solium (taeniasis) to eliminate tapeworm and prevent ongoing autoinfection and community transmission | 2 g :: PO :: single dose :: 2 g PO as single dose (chew thoroughly then swallow with water); take on empty stomach; purge 2h after to expel worm segments | Allergy; none significant | Stool follow-up at 1 and 3 months post-treatment to confirm eradication; household contacts screened | - | ROUTINE | ROUTINE | - |

### 3D. Surgical Management (Disease-Modifying)

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Neuroendoscopic cyst removal | Surgical | **Preferred approach** for intraventricular cysticercosis; direct visualization and excision of cyst; avoids open craniotomy; lateral and third ventricle cysts most amenable; fourth ventricle more challenging | Single procedure; cyst removed intact when possible; combined with ventriculostomy if hydrocephalus | MRI with FIESTA/CISS sequences to localize cyst; coagulation panel (INR <1.5, platelets >100K); neurosurgery consultation; anesthesia clearance | Coagulopathy (correct first); inaccessible cyst location; severe inflammation precluding safe dissection | Post-procedure MRI within 24-48h; neurologic exam q1h x 6h then q2h; signs of hemorrhage; CSF leak; hydrocephalus resolution | - | STAT | - | STAT |
| VP shunt placement | Surgical | Obstructive hydrocephalus from subarachnoid (racemose) NCC or chronic arachnoiditis; communicating hydrocephalus from chronic meningitis; when endoscopic cyst removal not feasible or hydrocephalus persists after cyst removal | Permanent CSF diversion; programmable valve preferred | CT/MRI confirming hydrocephalus; coagulation panel; neurosurgery consultation; assess for shunt infection risk | Active CNS infection (relative; requires simultaneous treatment); coagulopathy | Shunt function (clinical and imaging); shunt infection surveillance; ventricular size on follow-up imaging; signs of over-drainage or under-drainage | - | STAT | - | STAT |
| Endoscopic third ventriculostomy (ETV) | Surgical | Alternative to VP shunt for obstructive hydrocephalus; avoids shunt dependency; combine with endoscopic cyst removal when feasible | Single procedure; creates CSF pathway bypassing obstruction | MRI anatomy assessment; coagulation panel; neurosurgery | Communicating hydrocephalus (ETV less effective); basilar artery adherent to floor of third ventricle | Post-procedure imaging; neurologic exam; ICP monitoring if EVD placed | - | STAT | - | STAT |
| Craniotomy with cyst excision | Surgical | Large parenchymal cyst with significant mass effect not amenable to medical therapy; giant subarachnoid (racemose) cyst; fourth ventricle cyst not amenable to endoscopic removal; diagnostic uncertainty requiring tissue | Complete excision of cyst with capsule when feasible | CT/MRI navigation imaging; coagulation panel; type and crossmatch; corticosteroid pre-treatment; neurosurgery and anesthesia | Multiple deep cysts; eloquent cortex (relative); severe comorbidities precluding general anesthesia | Post-operative neurologic exam q1h x 12h then q2h; CT at 24h; wound care; ICP if EVD; seizure monitoring | - | STAT | - | STAT |
| External ventricular drain (EVD) | Surgical | Acute obstructive hydrocephalus from ventricular cyst; cysticercal encephalitis with elevated ICP; bridge to definitive treatment | Continuous or intermittent CSF drainage; target ICP <22 mmHg; target CPP >60 mmHg | Coagulation panel; neurosurgery; CT confirming hydrocephalus | Severe coagulopathy (correct first) | ICP continuous; CSF output hourly; CSF culture daily; EVD site care; neurologic exam q1h | - | - | - | STAT |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Infectious disease consultation for antiparasitic regimen selection, dosing optimization, drug interactions, and treatment duration guidance | STAT | STAT | ROUTINE | STAT |
| Neurosurgery consultation for ventricular cysts, hydrocephalus management (VP shunt, ETV, EVD), large cysts with mass effect, and diagnostic tissue sampling | STAT | STAT | - | STAT |
| Neurology consultation for seizure management, AED selection (avoiding enzyme-inducing agents), EEG interpretation, and long-term epilepsy management | URGENT | URGENT | ROUTINE | STAT |
| Ophthalmology consultation MANDATORY before initiating antiparasitic therapy to rule out ocular cysticercosis (treatment-induced inflammation causes blindness) | STAT | STAT | STAT | STAT |
| Critical care/ICU team for cysticercal encephalitis with diffuse cerebral edema, elevated ICP, herniation, or respiratory failure | STAT | STAT | - | STAT |
| Gastroenterology consultation if intestinal taeniasis confirmed for treatment and surveillance | - | ROUTINE | ROUTINE | - |
| Endocrinology consultation for corticosteroid-induced diabetes management during prolonged steroid courses (especially subarachnoid NCC requiring months of therapy) | - | ROUTINE | ROUTINE | - |
| Public health notification and household contact screening for Taenia solium (stool examination of household members; identify tapeworm carrier to prevent ongoing transmission) | - | ROUTINE | ROUTINE | - |
| Pharmacy consultation for drug interaction management (praziquantel interactions with enzyme-inducing AEDs; albendazole bioavailability optimization; cimetidine boosting) | - | ROUTINE | ROUTINE | - |
| Physical therapy for deconditioning prevention and rehabilitation if focal deficits present | - | ROUTINE | ROUTINE | - |
| Social work for discharge planning, medication access (albendazole availability), immigration/insurance barriers common in endemic populations | - | ROUTINE | ROUTINE | - |
| Neuropsychology referral if cognitive complaints persist after treatment (encephalitis, multiple cysts, or chronic hydrocephalus cause lasting cognitive impact) | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED immediately if worsening headache, new confusion, seizure, fever, new weakness, vision changes, or vomiting (indicates treatment-induced inflammation, hydrocephalus, or cysticercal encephalitis) | STAT | STAT | ROUTINE |
| Take albendazole WITH a fatty meal (increases drug absorption 5-fold; without fat, most of the drug is not absorbed and treatment fails) | - | ROUTINE | ROUTINE |
| Do NOT stop corticosteroids abruptly (adrenal crisis risk with sudden discontinuation; taper as directed by physician; risk increases after >2 weeks of use) | - | ROUTINE | ROUTINE |
| Report any yellowing of skin/eyes, dark urine, or right upper abdominal pain (signs of albendazole hepatotoxicity requiring medication hold and evaluation) | - | ROUTINE | ROUTINE |
| Take antiseizure medications as prescribed; do NOT stop abruptly (risk of breakthrough seizure; NCC is the leading cause of adult-onset epilepsy worldwide) | - | ROUTINE | ROUTINE |
| Do NOT drive until cleared by neurology due to seizure risk (state laws typically require 3-12 months seizure-free; NCC-related seizures recur even after cyst resolution) | - | ROUTINE | ROUTINE |
| Follow-up MRI scans are essential to confirm cyst resolution (typically at 3 and 6 months after treatment; some cysts take 12+ months to fully resolve or calcify) | - | ROUTINE | ROUTINE |
| Report any vision changes immediately (indicates ocular cysticercosis or treatment-related intraocular inflammation) | - | ROUTINE | ROUTINE |
| Ensure household members are screened for intestinal Taenia solium by stool examination (identifying and treating the tapeworm carrier prevents ongoing transmission) | - | ROUTINE | ROUTINE |
| Practice strict hand hygiene and food safety: wash hands thoroughly before eating and after using the restroom; wash all fruits and vegetables; cook pork to internal temperature of >=145F (63C) | - | ROUTINE | ROUTINE |
| Bring all medications to every follow-up visit for medication reconciliation and compliance assessment | - | ROUTINE | ROUTINE |
| Follow-up with neurology in 4-6 weeks for seizure assessment, AED level monitoring, and imaging review | - | ROUTINE | ROUTINE |
| Follow-up with infectious disease in 2-4 weeks for antiparasitic treatment response assessment and lab monitoring | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Food safety education: thoroughly cook all pork products to internal temperature >=145F (63C); avoid raw or undercooked pork (prevents intestinal tapeworm acquisition) | - | ROUTINE | ROUTINE |
| Hand hygiene education: wash hands with soap and water before preparing food, before eating, and after using the restroom (fecal-oral transmission of T. solium eggs causes cysticercosis) | - | ROUTINE | ROUTINE |
| Water safety: drink boiled or filtered water in endemic areas; avoid consuming water potentially contaminated with human feces | - | ROUTINE | ROUTINE |
| Seizure safety precautions: avoid heights, swimming alone, unsupervised bathing, and operating heavy machinery until seizure-free period established per neurology guidance | - | ROUTINE | ROUTINE |
| Glycemic control optimization during corticosteroid therapy (monitor glucose closely; initiate insulin or oral hypoglycemic agents during treatment as needed) | - | ROUTINE | ROUTINE |
| Bone health: calcium 1000-1200 mg/day and vitamin D 1000-2000 IU/day supplementation during prolonged corticosteroid use (>3 months); DEXA scan if prolonged steroid course anticipated | - | ROUTINE | ROUTINE |
| Screen household contacts for T. solium tapeworm carriage with stool O&P and/or coproantigen testing (public health imperative to interrupt transmission cycle) | - | ROUTINE | ROUTINE |
| Travel counseling for patients returning to endemic areas: emphasize food and water hygiene, pork cooking practices, and sanitation | - | - | ROUTINE |
| Avoid alcohol during antiparasitic therapy (hepatotoxicity risk with albendazole potentiated by alcohol; impairs medication compliance) | - | ROUTINE | ROUTINE |
| Stress management and mental health support (chronic disease management; immigration-related stressors common in endemic populations; seizure-related anxiety and depression) | - | ROUTINE | ROUTINE |
| Gradual return to work and daily activities with seizure precautions; driving restrictions per state law; employer notification if safety-sensitive occupation | - | - | ROUTINE |
| Women of childbearing age: effective contraception MANDATORY during albendazole therapy and for 1 month after completion (albendazole is teratogenic) | - | ROUTINE | ROUTINE |
| Follow-up imaging schedule: MRI at 3 months, 6 months, 12 months, then annually until cyst resolution confirmed and seizure-free; longer follow-up for subarachnoid NCC | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Tuberculoma | Endemic area overlap; ring-enhancing or solid nodular lesion; conglomerate lesions; basilar meningeal enhancement; no scolex; slower progression; constitutional symptoms | QuantiFERON-TB Gold; chest imaging; AFB culture; CSF TB PCR; biopsy with caseating granulomas; response to anti-TB therapy; NO scolex on imaging |
| Brain abscess | Ring-enhancing lesion with DWI restriction; fever; acute presentation; peripheral leukocytosis; thinner wall on ventricular side; no scolex | MRI DWI (restricted diffusion = abscess; NCC does NOT restrict); blood cultures; fever pattern; surgical aspiration with Gram stain and culture |
| Brain metastasis | Multiple ring-enhancing lesions at gray-white junction; known primary malignancy; progressive neurologic decline; no scolex; surrounded by vasogenic edema | CT chest/abdomen/pelvis for primary; no DWI restriction; no scolex; no calcifications; biopsy if uncertain |
| High-grade glioma (GBM) | Irregular thick ring enhancement; necrotic center without scolex; older age; progressive over weeks; mass effect disproportionate to size | MRI DWI (no restriction); MR spectroscopy (elevated choline); PET (hypermetabolic); biopsy |
| Toxoplasmosis | HIV/AIDS with CD4 <100; multiple ring-enhancing lesions in basal ganglia; no scolex; responds to empiric therapy within 2 weeks | Toxoplasma IgG (>95% positive); CD4 count; empiric treatment trial; no calcifications; serology |
| Primary CNS lymphoma | Periventricular homogeneous enhancement; immunocompromised or immunocompetent; no scolex; responds dramatically to steroids (ghost tumor) | MRI (homogeneous enhancement); CSF cytology; EBV PCR in CSF; avoid steroids before biopsy; no calcifications |
| Meningioma | Extra-axial dural-based mass; homogeneous enhancement with dural tail; no scolex; no calcification pattern of NCC | MRI (extra-axial, dural-based, dural tail); no DWI restriction; no ring enhancement; biopsy if uncertain |
| Colloid cyst (third ventricle) | Anterior third ventricle location; hyperdense on CT; no enhancement; intermittent hydrocephalus; positional headache | CT (hyperdense third ventricle cyst); MRI (variable signal but no scolex); no enhancement; no serologic markers |
| Arachnoid cyst | CSF-intensity cyst WITHOUT scolex; no enhancement; no perilesional edema; no calcification; congenital; asymptomatic or mass effect | MRI (CSF signal on ALL sequences, no scolex, no enhancement, no FLAIR signal); negative serology; stable on serial imaging |
| Epidermoid cyst | CSF-like cyst on T1/T2 but RESTRICTS on DWI (unlike arachnoid cyst); pearly white appearance; extra-axial; no scolex | MRI DWI (restricted diffusion unlike NCC cyst); no enhancement; no scolex; no calcification; no serology |
| Cavernous malformation | Popcorn-like lesion with hemosiderin rim; mixed signal on MRI; no enhancement (typically); seizures; no scolex; blooming on GRE/SWI | MRI GRE/SWI (prominent hemosiderin blooming); no enhancement; no scolex; gradient echo sequences diagnostic; negative serology |
| Calcified AVM or old hemorrhage | Calcification on CT; mimics calcified NCC; vascular flow voids on MRI; history of hemorrhage or incidental finding | CTA/MRA (vascular malformation); angiography (definitive); no scolex; negative serology; different calcification pattern |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Neurologic exam (GCS, pupils, motor, speech) | STAT | STAT | ROUTINE | STAT | q2-4h inpatient; each OPD visit | Stable or improving; no new focal deficits | If declining: STAT CT; assess for treatment-induced inflammation, hydrocephalus; hold antiparasitic if worsening; increase corticosteroids |
| Temperature | STAT | STAT | ROUTINE | STAT | q4h (q1h if febrile) | Afebrile; low-grade fever common during cyst degeneration | If persistent high fever: evaluate for bacterial superinfection; cysticercal encephalitis; other etiology |
| LFTs (ALT, AST, bilirubin) | - | ROUTINE | ROUTINE | ROUTINE | Baseline; day 7; day 14 of albendazole; then biweekly during treatment | ALT/AST <3x ULN | If ALT/AST >3x ULN: HOLD albendazole; recheck in 1 week; resume at lower dose if normalized or switch to praziquantel monotherapy |
| CBC with differential | STAT | ROUTINE | ROUTINE | STAT | Baseline; weekly during antiparasitic therapy; q2 weeks during prolonged courses | WBC >3000; ANC >1500; platelets >100K | If leukopenia or thrombocytopenia: hold albendazole; recheck in 1 week; dose reduction |
| Blood glucose | STAT | ROUTINE | ROUTINE | STAT | q6h during IV dexamethasone; daily during oral steroid taper; each OPD visit | Glucose <180 mg/dL; HbA1c <7% | If persistently elevated: start insulin sliding scale or oral hypoglycemic; endocrine consultation for prolonged steroid courses |
| Serum sodium | STAT | ROUTINE | - | STAT | Daily x 3 then twice weekly inpatient; each OPD visit during steroid taper | 135-145 mEq/L | If <130: SIADH workup; fluid restriction; if <120: 3% saline |
| Antiepileptic drug levels | - | ROUTINE | ROUTINE | ROUTINE | Once at steady state; after dose changes; if breakthrough seizures | Therapeutic range for specific AED | Adjust dosing; assess compliance; drug interaction review |
| Serial MRI brain with contrast | - | ROUTINE | ROUTINE | ROUTINE | At 3 months, 6 months, 12 months post-treatment; then annually until resolved | Cyst resolution (disappearance or calcification); no new cysts; decreasing edema; no new enhancement | If enlarging or new cysts: retreat with antiparasitic; if new edema around calcification: short steroid course; neurosurgery if hydrocephalus |
| Seizure monitoring (clinical + EEG) | STAT | STAT | ROUTINE | STAT | Clinical: continuous inpatient; EEG if altered consciousness; OPD: seizure diary | No seizure activity | If seizures: optimize AED levels; add second agent; continuous EEG in ICU; assess for new cyst inflammation |
| CSF antigen levels (subarachnoid NCC) | - | ROUTINE | ROUTINE | - | Baseline; at 3 months; at 6 months; then q6 months until negative | Declining cysticercus antigen titer | If rising or stable: treatment failure; extend antiparasitic course; reassess surgical options |
| ICP (if EVD in place) | - | - | - | STAT | Continuous | ICP <22 mmHg; CPP 60-70 mmHg | Tiered ICP management: CSF drainage, osmotherapy, sedation, surgical decompression |
| Ophthalmologic exam | - | ROUTINE | ROUTINE | - | Baseline before treatment; at 3 months; if new visual symptoms | No intraocular cysts; stable vision | If new intraocular findings: HOLD antiparasitic; urgent ophthalmology |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home (with outpatient follow-up) | Clinically stable; seizure-free >=48h on AEDs; tolerating oral medications (antiparasitic + steroids + AED); no signs of elevated ICP; no hydrocephalus on imaging; outpatient MRI and lab follow-up arranged; neurology and ID follow-up confirmed within 2-4 weeks; reliable medication access and compliance anticipated |
| Admit to floor (monitored) | New NCC diagnosis with active parenchymal cysts requiring initiation of antiparasitic therapy under observation; mild headache without signs of elevated ICP; GCS >=14; seizures controlled on medication; monitoring for treatment-induced inflammation during first 48-72h of antiparasitic + steroid initiation |
| Admit to ICU / Neuro-ICU | Cysticercal encephalitis (massive edema, diffuse viable cysts); acute hydrocephalus requiring EVD; GCS <13 or declining; herniation syndrome; refractory seizures or status epilepticus; post-operative monitoring after craniotomy or endoscopic cyst removal; need for ICP monitoring |
| Transfer to higher level | Need for neurosurgery not available at current facility (endoscopic cyst removal, VP shunt, craniotomy); need for neuro-ICU expertise; need for continuous EEG not available; need for specialized NCC serologic testing |
| Outpatient management | Calcified NCC (inactive) with controlled seizures; known NCC on established AED regimen with seizure diary; follow-up imaging and serology monitoring; stable subarachnoid NCC on maintenance steroid/antiparasitic taper |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Del Brutto diagnostic criteria for NCC | Class I, Level A | [Del Brutto et al. J Neurol Sci 2017](https://pubmed.ncbi.nlm.nih.gov/28320184/) — revised diagnostic criteria with absolute, major, minor, and epidemiologic criteria |
| Albendazole 15 mg/kg/day for parenchymal NCC | Class I, Level A | [Garcia et al. N Engl J Med 2004](https://pubmed.ncbi.nlm.nih.gov/15306668/) — randomized controlled trial demonstrating albendazole reduces seizure burden and promotes cyst resolution |
| Combination albendazole + praziquantel for >2 viable cysts | Class I, Level A | [Garcia et al. Lancet Infect Dis 2014](https://pubmed.ncbi.nlm.nih.gov/25444472/) — RCT showing combination therapy superior to albendazole alone for multiple cysts |
| Corticosteroids before and during antiparasitic therapy | Class I, Level A | [Garcia et al. N Engl J Med 2004](https://pubmed.ncbi.nlm.nih.gov/15306668/); [IDSA/ASTMH Guidelines — White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) |
| IDSA/ASTMH Clinical Practice Guidelines for NCC | Class I, Level A | [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — comprehensive guidelines for diagnosis and treatment of NCC |
| No antiparasitic therapy for calcified NCC | Class I, Level B | [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — calcified lesions are dead parasites; antiparasitic therapy has no target; AEDs for seizures |
| EITB (immunoblot) as preferred serologic test | Class I, Level A | [Tsang et al. J Infect Dis 1989](https://pubmed.ncbi.nlm.nih.gov/2715568/) — EITB sensitivity 94-98% for >1 viable cyst; specificity ~100% |
| Enzyme-inducing AEDs reduce praziquantel levels by 50-75% | Class I, Level B | [Bittencourt et al. Neurology 1992](https://pubmed.ncbi.nlm.nih.gov/1549209/) — phenytoin and carbamazepine significantly reduce praziquantel bioavailability; prefer non-enzyme-inducing AEDs |
| Ophthalmologic exam mandatory before antiparasitic therapy | Class I, Level C | [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — treatment-induced inflammation causes vision loss in ocular NCC; absolute contraindication |
| Neuroendoscopy preferred for intraventricular cyst removal | Class IIa, Level B | [Sinha & Sharma. Neurosurg Focus 2012](https://pubmed.ncbi.nlm.nih.gov/22537130/) — endoscopic approach offers direct visualization with lower morbidity than open surgery for ventricular cysts |
| VP shunt for chronic hydrocephalus in subarachnoid NCC | Class IIa, Level B | [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — chronic arachnoiditis causes communicating hydrocephalus requiring permanent CSF diversion |
| Prolonged antiparasitic therapy for subarachnoid NCC | Class IIa, Level C | [Proano et al. Ann Intern Med 2001](https://pubmed.ncbi.nlm.nih.gov/11293476/) — subarachnoid (racemose) NCC requires prolonged courses (months); monitor with CSF antigen |
| NCC is the leading cause of adult-onset epilepsy worldwide | Class I, Level A | [Ndimubanzi et al. PLoS Negl Trop Dis 2010](https://pubmed.ncbi.nlm.nih.gov/21152057/) — systematic review confirming NCC accounts for ~30% of epilepsy in endemic areas |
| Methotrexate as steroid-sparing agent for subarachnoid NCC | Class IIb, Level C | [Mitre et al. Clin Infect Dis 2007](https://pubmed.ncbi.nlm.nih.gov/17712753/) — case series supporting methotrexate for chronic arachnoiditis requiring prolonged immunosuppression |
| Albendazole bioavailability increased 5-fold with fatty meal | Class I, Level B | [Mottier et al. J Pharm Pharmacol 2006](https://pubmed.ncbi.nlm.nih.gov/16553415/) — pharmacokinetic studies demonstrating critical importance of fatty meal for drug absorption |
| Cysticercal encephalitis: no antiparasitic initially | Class I, Level C | [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — antiparasitic drugs worsen cerebral edema in cysticercal encephalitis; control edema first with corticosteroids and ICP management |
| Dexamethasone increases albendazole sulfoxide levels by 50% | Class I, Level B | [Jung et al. J Clin Pharmacol 1990](https://pubmed.ncbi.nlm.nih.gov/2229455/) — pharmacokinetic synergy; concurrent dexamethasone enhances albendazole efficacy |
| Serial MRI for monitoring treatment response | Class I, Level B | Expert consensus; [White et al. Clin Infect Dis 2018](https://pubmed.ncbi.nlm.nih.gov/29481580/) — imaging at 3 and 6 months; cyst resolution or calcification confirms successful treatment |

---

## CHANGE LOG

**v1.1 (February 2, 2026)**
- Checker/rebuilder pipeline revision (all findings approved)
- C1: Replaced hedging language in staging table granular nodular row ("may be considered" -> "Antiparasitic therapy for residual viable elements")
- C2: Clarified albendazole dosing (standard max 800 mg/day; up to 1200 mg/day for heavy disease per ID specialist)
- C3: Added ICU column to LP table for all 10 CSF studies with appropriate priorities
- C4: Removed incorrect CPT 96374 from albendazole (oral medication, not IV push)
- S1: LP table ICU column populated (URGENT for acute studies, ROUTINE for specialized)
- S2: Added HOSP = URGENT for mannitol and hypertonic saline (usable on monitored floors)
- M1: Converted staging table hedging to directives; ventricular row updated to directive phrasing
- M2: Clarified levetiracetam titration (titrate by 500 mg/day every 2 weeks to 1500 mg BID)
- M3: Pneumatic compression device dosing field corrected (N/A for dose)
- R1: Removed hedging language throughout ("may suggest" -> "indicates", "may cross-react" -> "cross-reacts", "can be fatal" -> "is fatal", "can destroy" -> "destroys", "can cause" -> "causes", "may indicate" -> "indicates", "may fail" -> "fails", "may recur" -> "recur", "may require" -> "requires/as needed", "consider" -> "evaluate for")
- R2: 4B/4C tables corrected to 4-column format (ED, HOSP, OPD — no ICU per spec)
- R3: VP shunt contraindication updated from "may need" to "requires"
- R4: ETV indication updated from "may be combined" to "combine when feasible"
- R5: Lorazepam dosing updated from "may repeat" to "repeat x1 if seizure continues"
- R6: Prednisone taper updated from "may require years" to "years for chronic arachnoiditis"
- R7: Methotrexate onset updated from "may take 4-6 weeks" to "onset of effect 4-6 weeks"
- R8: Appendix B granular nodular treatment updated to match staging table directive
- Updated version to 1.1; added REVISED date

**v1.0 (February 2, 2026)**
- Initial template creation
- Comprehensive 8-section format covering neurocysticercosis diagnosis, staging, antiparasitic therapy, seizure management, and follow-up
- All four anatomic forms covered: parenchymal, ventricular, subarachnoid (racemose), and spinal NCC
- Staging-based treatment approach: vesicular, colloidal vesicular, granular nodular, calcified
- Antiparasitic regimen: albendazole monotherapy for 1-2 cysts; combination albendazole + praziquantel for >2 cysts
- Drug interaction management: enzyme-inducing AEDs reduce praziquantel levels; cimetidine as booster
- Del Brutto diagnostic criteria referenced
- Surgical management: neuroendoscopy for ventricular cysts, VP shunt for chronic hydrocephalus, craniotomy indications
- Mandatory ophthalmologic exam before antiparasitic therapy
- Cysticercal encephalitis management (no antiparasitic initially)
- Steroid-sparing agents (methotrexate) for chronic subarachnoid NCC
- Public health measures: household contact screening, intestinal tapeworm treatment
- IDSA/ASTMH 2018 guidelines as primary evidence source

---

## APPENDIX A: DEL BRUTTO DIAGNOSTIC CRITERIA (2017 REVISED)

### Absolute Criteria (any one = definitive diagnosis)
| Criterion | Details |
|-----------|---------|
| Histologic demonstration | Parasitic structures (scolex, cyst wall) in CNS tissue from biopsy or autopsy |
| Cystic lesion with scolex on CT or MRI | **Pathognomonic:** visualization of scolex (bright dot) within a cystic lesion on neuroimaging |
| Fundoscopic visualization | Direct visualization of subretinal cysticercus by ophthalmoscopy |

### Neuroimaging Criteria
| Category | Findings |
|----------|----------|
| Major | Cystic lesions without scolex; enhancing lesions; multilobulated cysts in subarachnoid space (racemose); typical parenchymal calcifications |
| Confirmatory | Resolution of cystic lesions after antiparasitic therapy; spontaneous resolution of single enhancing lesion (compatible with natural history); migration of ventricular cyst on sequential imaging |
| Minor | Obstructive hydrocephalus; abnormal enhancement of basal leptomeninges; myelographic filling defect in spinal canal |

### Clinical/Exposure Criteria
| Category | Findings |
|----------|----------|
| Major | Positive serum cysticercosis EITB (immunoblot); resolution of intracranial cystic lesion after albendazole/praziquantel therapy; cysticercosis outside CNS (subcutaneous/intramuscular cigar-shaped calcifications) |
| Minor | Clinical manifestations suggestive of NCC (seizures, focal deficits, elevated ICP); positive CSF ELISA for cysticercal antigen or antibody; individual from or living in endemic area |

### Diagnostic Categories

| Diagnosis | Criteria Required |
|-----------|-------------------|
| Definitive NCC | 1 absolute criterion; OR 2 major neuroimaging + 1 clinical/exposure criteria |
| Probable NCC | 1 major neuroimaging + 2 clinical/exposure criteria; OR 1 major + 1 confirmatory neuroimaging + 1 clinical/exposure criteria; OR 1 major neuroimaging + 1 clinical/exposure + 1 epidemiologic criterion |

## APPENDIX B: NCC STAGING AND IMAGING CHARACTERISTICS

| Stage | Timeline | CT Findings | MRI Findings | Pathology | Treatment Implication |
|-------|----------|-------------|--------------|-----------|----------------------|
| Vesicular (viable) | Months to years after infection | Well-defined cyst (CSF density); scolex visible as eccentric dot; no enhancement; minimal/no edema | Cyst = CSF signal on all sequences; scolex bright on FLAIR/T1+C; no surrounding edema; no restriction on DWI | Viable larva with intact membrane; minimal host immune response | Antiparasitic therapy indicated; corticosteroids for inflammation |
| Colloidal vesicular (degenerating) | Host immune response begins | Ring-enhancing cyst; perilesional edema; cyst contents slightly hyperdense to CSF | Ring enhancement; cyst fluid brighter than CSF on FLAIR and T1; perilesional edema (T2/FLAIR hyperintensity); scolex still visible | Degenerating larva; thick capsule; intense inflammatory infiltrate; colloidal fluid | Antiparasitic therapy + corticosteroids; most symptomatic stage |
| Granular nodular (involuting) | Cyst shrinking | Enhancing nodule or small ring-enhancing lesion; less edema than colloidal stage; lesion shrinking | Nodular or ring enhancement; decreasing size; less perilesional edema; scolex no longer visible | Larval remnants; dense collagen capsule; granulomatous inflammation | Antiparasitic therapy for residual viable elements; corticosteroids if symptomatic edema |
| Calcified (inactive/dead) | Years post-infection | **Calcified nodule** (best seen on CT); small, round, dense calcification; no enhancement unless perilesional edema | T2/GRE/SWI hypointense (dark); perilesional edema possible (seizure trigger); NO enhancement of calcification itself | Dead parasite; calcium deposits; gliotic scar; mineralized remnant | NO antiparasitic (cyst is dead); AEDs for seizures; short steroid course for perilesional edema |

## APPENDIX C: DRUG INTERACTION MANAGEMENT FOR NCC

| Drug Interaction | Clinical Effect | Management |
|------------------|----------------|------------|
| Phenytoin/carbamazepine + praziquantel | Enzyme-inducing AEDs reduce praziquantel levels by 50-75% (CYP3A4 induction) | Switch to non-enzyme-inducing AED (levetiracetam, lacosamide) if possible; if not possible: increase praziquantel dose to 100 mg/kg/day OR add cimetidine 400 mg TID |
| Dexamethasone + praziquantel | Dexamethasone reduces praziquantel levels by ~50% (CYP3A4 induction) | Add cimetidine 400 mg TID; monitor clinical response; increase praziquantel dose if needed |
| Dexamethasone + albendazole | Dexamethasone INCREASES albendazole sulfoxide (active metabolite) levels by ~50% | Beneficial interaction; no dose adjustment needed; enhances albendazole efficacy |
| Cimetidine + praziquantel | Cimetidine inhibits CYP3A4, increases praziquantel bioavailability 2-fold | Use cimetidine 400 mg TID when enzyme-inducing AEDs or dexamethasone reduce praziquantel levels |
| Albendazole + fatty meal | Fat increases albendazole absorption 5-fold | ALWAYS take albendazole with fatty meal; counsel patient on importance |
| Valproate + albendazole | No significant interaction | Safe combination; no dose adjustment |
| Levetiracetam + albendazole/praziquantel | No significant interaction | Preferred AED for NCC due to no enzyme induction |
| Lacosamide + albendazole/praziquantel | No significant interaction | Safe alternative AED; no enzyme induction |
| Phenobarbital + praziquantel | Reduces praziquantel levels (CYP3A4 induction) | Avoid; switch to non-enzyme-inducing AED |

## APPENDIX D: TREATMENT DURATION BY NCC TYPE

| NCC Type | Antiparasitic Duration | Steroid Duration | AED Duration | Follow-up Imaging |
|----------|----------------------|------------------|-------------|-------------------|
| 1-2 parenchymal cysts (viable) | Albendazole 7-14 days | Dexamethasone: start 1 day before, taper over 2-4 weeks | Continue >=2 years seizure-free; trial withdrawal if cyst resolved and EEG normal | MRI at 3 and 6 months; annual until resolved |
| >2 parenchymal cysts (viable) | Albendazole + praziquantel 10-14 days | Dexamethasone: start 1 day before, taper over 2-4 weeks | Continue >=2 years seizure-free | MRI at 3 and 6 months; annual until resolved |
| Calcified (inactive) | NONE (cyst is dead) | Short course (5-7 days) only if perilesional edema | Lifelong if recurrent seizures; trial AED withdrawal after >=2 years seizure-free | CT at 6-12 months to confirm stable calcification |
| Ventricular | Antiparasitic after surgical cyst removal if viable cysts remain | Variable based on inflammation | Per seizure management | MRI at 1, 3, 6, 12 months; assess shunt function |
| Subarachnoid (racemose) | Prolonged: weeks to months (repeat courses common); monitor with CSF antigen until negative | Prolonged: months to years; steroid-sparing agents (methotrexate) for chronic arachnoiditis | Per seizure management; often prolonged | MRI + CSF antigen q3-6 months until antigen negative |
| Spinal | Antiparasitic after surgical excision if accessible; medical therapy if diffuse or inoperable | Prolonged during treatment | If seizures present | MRI spine at 3, 6, 12 months |
| Cysticercal encephalitis | DELAYED: only after edema controlled (weeks); start low dose | HIGH-DOSE: dexamethasone 0.15-0.3 mg/kg q6h; prolonged taper | Aggressive AED management; often requires multiple agents | MRI at 2 weeks, then monthly until stable |
