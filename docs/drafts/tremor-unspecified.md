---
title: "Tremor, Unspecified"
description: "Clinical decision support for the evaluation of undifferentiated tremor in adults, including classification, differential diagnosis, and empiric management"
version: "1.1"
setting: "ED, HOSP, OPD"
status: draft
tags:
  - movement-disorders
  - tremor
  - evaluation
  - diagnostic-workup
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Tremor, Unspecified

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Revised per checker pipeline (v1.1)

---

**DIAGNOSIS:** Tremor, Unspecified

**ICD-10:** R25.1 (Tremor, unspecified), G25.0 (Essential tremor), G25.1 (Drug-induced tremor), G25.2 (Other specified forms of tremor), G25.9 (Extrapyramidal and movement disorder, unspecified)

**CPT CODES:** 99213-99215 (E&M outpatient), 99221-99223 (E&M inpatient), 78830 (DaTscan), 70553 (MRI brain with/without contrast), 70551 (MRI brain without contrast), 84443 (TSH), 84439 (Free T4), 80053 (CMP), 82390 (Ceruloplasmin), 82607 (Vitamin B12), 95907-95913 (NCS/EMG), 95885 (EMG), 95816 (EEG), 70450 (CT head without contrast), 80307 (Drug screen), 82525 (24-hour urine copper)

**SYNONYMS:** Tremor, unspecified tremor, tremor evaluation, tremor workup, trembling, shaking, involuntary shaking, hand tremor, head tremor, voice tremor, action tremor, resting tremor, postural tremor, kinetic tremor, intention tremor, undifferentiated tremor, tremor NOS, new-onset tremor

**SCOPE:** Evaluation and diagnostic workup of undifferentiated tremor in adults. Covers the systematic approach to tremor classification (rest, postural, kinetic, intention, task-specific), differentiation of essential tremor, Parkinson tremor, enhanced physiologic tremor, drug-induced tremor, cerebellar tremor, Holmes (rubral) tremor, dystonic tremor, and psychogenic (functional) tremor. Includes DaTscan indications, laboratory workup (thyroid, Wilson disease, medication review), and empiric treatment while awaiting definitive diagnosis. Settings: ED, HOSP, OPD. Excludes definitive management of established diagnoses (see Essential Tremor, Parkinson's Disease, Drug-Induced Parkinsonism, Dystonia, Functional Neurological Disorder templates for ongoing management after diagnosis confirmed).

---

**DEFINITIONS:**
- **Tremor:** Involuntary, rhythmic, oscillatory movement of a body part produced by alternating or synchronous contractions of reciprocally innervated muscles
- **Rest Tremor:** Tremor occurring in a body part that is completely supported against gravity and not voluntarily activated; classic for Parkinson's disease (4-6 Hz, pill-rolling)
- **Postural Tremor:** Tremor occurring when voluntarily maintaining a position against gravity (e.g., arms outstretched); characteristic of essential tremor and enhanced physiologic tremor
- **Kinetic Tremor:** Tremor occurring during voluntary movement; includes simple kinetic (during movement) and intention tremor (worsening as target is approached)
- **Intention Tremor:** Subtype of kinetic tremor that increases in amplitude as the limb approaches a visual target (finger-to-nose); classic for cerebellar lesions
- **Task-Specific Tremor:** Tremor occurring only during specific activities (e.g., writing, playing musical instrument)
- **Holmes Tremor (Rubral Tremor):** Combination of rest, postural, and kinetic/intention tremor; low frequency (< 4.5 Hz), large amplitude; caused by midbrain/thalamic lesions disrupting both cerebellar and dopaminergic pathways
- **Dystonic Tremor:** Irregular, jerky tremor occurring in a body part affected by dystonia; presence of a "null point" (position where tremor diminishes)
- **Enhanced Physiologic Tremor:** Exaggeration of normal physiologic tremor (8-12 Hz) by reversible causes (anxiety, caffeine, medications, hyperthyroidism, hypoglycemia)
- **Functional (Psychogenic) Tremor:** Tremor with features of variability, distractibility, and entrainment, inconsistent with organic tremor patterns

---

**TREMOR CLASSIFICATION FRAMEWORK:**

| Feature | Rest Tremor | Postural Tremor | Kinetic Tremor | Intention Tremor | Task-Specific |
|---------|-------------|-----------------|----------------|------------------|---------------|
| **When present** | Limb fully supported, relaxed | Maintaining position against gravity | During voluntary movement | Approaching target | Only during specific task |
| **Frequency** | 4-6 Hz | 6-12 Hz | 4-8 Hz | 3-5 Hz | Variable |
| **Typical cause** | Parkinson's disease | Essential tremor, physiologic | Essential tremor | Cerebellar lesion | Primary writing tremor |
| **Amplitude** | Moderate, may re-emerge | Low-moderate | Moderate | Increases at target | Variable |

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| TSH (CPT 84443) | ROUTINE | ROUTINE | ROUTINE | - | Hyperthyroidism is a common reversible cause of enhanced physiologic tremor; hypothyroidism rarely causes tremor | Normal (0.4-4.0 mIU/L); abnormal TSH triggers free T4; hyperthyroidism identified directs treatment of underlying cause |
| Free T4 (CPT 84439) | ROUTINE | ROUTINE | ROUTINE | - | Order if TSH abnormal; confirms hyper- or hypothyroidism as cause of tremor | Normal; elevated confirms hyperthyroidism contributing to tremor |
| CMP (CPT 80053) | URGENT | ROUTINE | ROUTINE | - | Electrolyte derangements (hypoglycemia, hyponatremia, uremia, hepatic dysfunction) cause or worsen tremor | Normal; hypoglycemia, hyponatremia, liver failure, renal failure all produce tremor |
| Glucose (CPT 82947) | URGENT | ROUTINE | ROUTINE | - | Hypoglycemia is an acute reversible cause of tremor; hyperglycemia with diabetic neuropathy | Normal (70-100 mg/dL fasting); hypoglycemia triggers treatment and tremor resolves |
| CBC with differential (CPT 85025) | ROUTINE | ROUTINE | ROUTINE | - | General health assessment; infection screen; anemia workup | Normal; leukocytosis suggests infectious or inflammatory cause |
| Comprehensive medication reconciliation | STAT | STAT | ROUTINE | - | Drug-induced tremor is one of the most common causes; review ALL current medications including OTC, herbal, and supplements | Complete medication list; identify tremor-inducing agents (valproate, lithium, SSRIs, stimulants, bronchodilators, amiodarone, metoclopramide, antipsychotics) |
| Caffeine intake assessment | ROUTINE | ROUTINE | ROUTINE | - | Excessive caffeine is a leading cause of enhanced physiologic tremor; often overlooked | Quantify daily caffeine intake (coffee, tea, energy drinks, supplements); >400 mg/day causes significant tremor |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum ceruloplasmin (CPT 82390) | - | ROUTINE | ROUTINE | - | Wilson disease screening in patients <50 years or with atypical features (hepatic dysfunction, psychiatric symptoms, Kayser-Fleischer rings) | 20-40 mg/dL; low (<20 mg/dL) triggers 24-hour urine copper and slit-lamp exam for K-F rings |
| 24-hour urine copper (CPT 82525) | - | EXT | EXT | - | Wilson disease confirmation if ceruloplasmin low or borderline | <40 mcg/24h normal; >100 mcg/24h strongly suggestive of Wilson disease |
| Serum copper (CPT 82390) | - | ROUTINE | ROUTINE | - | Wilson disease evaluation alongside ceruloplasmin; copper deficiency causes neurological symptoms | Normal (70-140 mcg/dL); low total copper with low ceruloplasmin indicates Wilson disease |
| Liver function tests (CPT 80076) | - | ROUTINE | ROUTINE | - | Wilson disease screening; hepatic encephalopathy; medication hepatotoxicity | Normal; abnormal triggers evaluation for Wilson disease, hepatic tremor |
| Vitamin B12 (CPT 82607) | - | ROUTINE | ROUTINE | - | Deficiency causes tremor, neuropathy, and myelopathy contributing to movement disorder | >400 pg/mL; borderline (200-400) triggers methylmalonic acid; deficiency triggers supplementation |
| Drug levels (lithium, valproate, phenytoin, theophylline) (CPT 80178/80164/80185/80198) | URGENT | ROUTINE | ROUTINE | - | Drug toxicity is a common and reversible cause of tremor; supratherapeutic levels worsen EPS | Therapeutic ranges; supratherapeutic levels require dose adjustment or discontinuation |
| Drug/toxin screen (CPT 80307) | URGENT | ROUTINE | ROUTINE | - | Identify sympathomimetics, illicit substances (amphetamines, cocaine), or other toxins causing tremor | Negative; positive identifies offending agent for targeted management |
| Urine metanephrines/catecholamines | - | EXT | EXT | - | Pheochromocytoma presenting with tremor, hypertension, tachycardia, and diaphoresis | Normal; elevated triggers CT/MRI adrenals and endocrinology referral |
| Magnesium (CPT 83735) | URGENT | ROUTINE | ROUTINE | - | Hypomagnesemia contributes to tremor and neuromuscular excitability; common in alcoholism | Normal (1.7-2.2 mg/dL); low requires supplementation |
| ESR (CPT 85652) / CRP (CPT 86140) | - | ROUTINE | ROUTINE | - | Inflammatory markers if autoimmune or paraneoplastic etiology suspected | Normal; elevated triggers further workup for inflammatory/autoimmune cause |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Heavy metal levels (mercury, lead, manganese, arsenic) | - | - | EXT | - | Occupational or environmental exposure causing tremor; manganese causes parkinsonism | Normal; elevated triggers toxicology consultation and chelation therapy |
| Anti-neuronal antibodies (paraneoplastic panel) (CPT 86255) | - | - | EXT | - | Autoimmune or paraneoplastic movement disorder presenting as tremor | Negative; positive triggers malignancy search and immunotherapy |
| Anti-GAD65 antibodies (CPT 86235) | - | - | EXT | - | Autoimmune movement disorder (stiff-person spectrum, cerebellar ataxia with tremor) | Negative; positive at high titers confirms autoimmune etiology |
| Genetic testing (LINGO1, FUS, ETM1/2, DYT genes) | - | - | EXT | - | Family history of tremor or dystonia; research interest; young-onset tremor | Informational; positive triggers genetic counseling |
| Serum ferritin and iron studies | - | - | EXT | - | Restless legs/periodic limb movements sometimes confused with tremor; iron deposition disorders | Normal; low ferritin (<50 mcg/L) requires supplementation; very high ferritin triggers iron overload evaluation |
| Cortisol level (CPT 82533) | - | - | EXT | - | Cushing syndrome with tremor and proximal myopathy | Normal; elevated triggers dexamethasone suppression test |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Comprehensive neurologic examination | STAT | ROUTINE | ROUTINE | - | At presentation; document tremor type, distribution, activation conditions, frequency, associated signs (bradykinesia, rigidity, dystonia, ataxia) | Characterize tremor (rest, postural, kinetic, intention, task-specific); identify associated neurologic signs; laterality and symmetry | None |
| Handwriting sample | - | ROUTINE | ROUTINE | - | At presentation and follow-up visits; compare over time | Large, tremulous writing (essential tremor) vs micrographia (Parkinson's); progressive change | None |
| Spiral drawing test (Archimedes spiral) | - | ROUTINE | ROUTINE | - | At presentation; objective assessment tool | Objective tremor severity rating; track progression or treatment response | None |
| Finger-to-nose testing | ROUTINE | ROUTINE | ROUTINE | - | At presentation | Dysmetria and intention tremor indicate cerebellar cause; past-pointing increases with action in intention tremor | None |
| CT head without contrast (CPT 70450) | STAT | STAT | - | - | STAT if acute onset tremor with other neurologic signs (weakness, ataxia, altered consciousness) suggesting structural lesion | Rule out hemorrhage, mass, hydrocephalus; does NOT adequately visualize posterior fossa or midbrain | None for non-contrast |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain without contrast (CPT 70551) | - | ROUTINE | ROUTINE | - | If structural cause suspected; atypical features; young onset; acute onset | Rule out midbrain/thalamic lesion (Holmes tremor), cerebellar lesion, basal ganglia pathology, Wilson disease (T2 basal ganglia changes), demyelination | MRI-incompatible implants, severe claustrophobia |
| MRI brain with and without contrast (CPT 70553) | - | ROUTINE | ROUTINE | - | If mass lesion, demyelination, or infection suspected | Midbrain lesion (Holmes tremor); cerebellar tumor/abscess; MS plaques; basal ganglia enhancement | MRI-incompatible implants; contrast allergy; GFR <30 for gadolinium |
| DaTscan (Ioflupane I-123 SPECT) (CPT 78830) | - | - | ROUTINE | - | Key study to differentiate essential tremor from Parkinson's disease when clinical features overlap; order when diagnostic uncertainty persists after clinical evaluation | Normal striatal uptake indicates essential tremor, enhanced physiologic tremor, drug-induced tremor, psychogenic tremor; reduced striatal uptake indicates Parkinson's disease, MSA, PSP, DLB | Pregnancy; iodine/shellfish allergy; hold interfering medications (bupropion, amphetamines, modafinil, cocaine) 2 weeks before |
| MRI with susceptibility-weighted imaging (SWI) | - | ROUTINE | ROUTINE | - | If Wilson disease or iron deposition suspected | Basal ganglia T2 hypointensity (iron deposition); "face of the giant panda" sign in Wilson disease (midbrain) | Per MRI contraindications |
| Accelerometry / Tremor analysis | - | - | EXT | - | Objective quantification of tremor frequency and amplitude; distinguish tremor types by frequency characteristics | ET: 4-12 Hz; physiologic: 8-12 Hz; PD rest: 4-6 Hz; cerebellar: 3-5 Hz; Holmes: <4.5 Hz; orthostatic: 13-18 Hz | None |
| EMG (CPT 95885) | - | - | EXT | - | If neuropathic tremor suspected; orthostatic tremor evaluation; distinguish tremor types | Rhythmic bursting pattern; high-frequency EMG bursts in orthostatic tremor (13-18 Hz); neuropathic tremor pattern | None significant |
| NCS/EMG (CPT 95907-95913) | - | ROUTINE | ROUTINE | - | If peripheral neuropathy suspected as contributing factor to sensory-mediated tremor | Sensory or sensorimotor neuropathy; demyelinating features (CIDP) | Anticoagulation (relative for EMG) |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| FDG-PET brain (CPT 78608) | - | - | EXT | - | Atypical parkinsonism suspected; distinguish PD from MSA, PSP, CBD | Characteristic metabolic patterns differ by diagnosis; hypometabolism in posterior cortex (DLB), frontal (PSP), asymmetric cortical (CBD) | Significant hyperglycemia; pregnancy |
| MIBG cardiac scintigraphy | - | - | EXT | - | Differentiate PD (reduced cardiac sympathetic innervation) from MSA or drug-induced parkinsonism (normal) | Reduced uptake indicates PD or DLB; normal indicates MSA, DIP, essential tremor | Drugs affecting cardiac norepinephrine uptake |
| Olfactory testing (UPSIT) | - | - | ROUTINE | - | Supportive test; olfactory dysfunction suggests underlying PD (present early) vs normal olfaction in ET or DIP | Impaired indicates PD, DLB; normal indicates ET, DIP, functional tremor | Nasal obstruction |
| Transcranial sonography | - | - | EXT | - | Substantia nigra hyperechogenicity assessment; supports PD diagnosis | Hyperechogenicity suggests PD; normal indicates ET, DIP | Inadequate temporal bone window |
| Polysomnography (CPT 95810) | - | - | EXT | - | REM sleep behavior disorder suggests underlying synucleinopathy (PD, DLB, MSA) | RBD present strongly supports underlying neurodegenerative parkinsonism | None |
| Slit-lamp ophthalmologic exam | - | ROUTINE | ROUTINE | - | Kayser-Fleischer ring detection for Wilson disease in patients <50 with low ceruloplasmin or liver disease | K-F rings present confirms Wilson disease highly likely | None |

---

## 3. TREATMENT

### 3A. Immediate Management (ED/Acute Setting)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Discontinue or reduce suspected causative medication | PO | Drug-induced tremor; temporal relationship between medication initiation and tremor onset | N/A :: PO :: once :: Identify and discontinue offending agent if safe; taper if abrupt withdrawal is dangerous (benzodiazepines, antiepileptics, antipsychotics); coordinate with prescribing physician | Active psychosis, seizure disorder, or condition requiring the medication without safe alternative | Symptom resolution timeline; withdrawal symptoms; rebound of treated condition | STAT | STAT | ROUTINE | - |
| Dextrose (for hypoglycemia) | IV | Hypoglycemia-induced tremor with blood glucose <70 mg/dL | 25 g :: IV :: once :: Administer 50 mL of D50W IV push; recheck glucose in 15 minutes; repeat if glucose remains <70 mg/dL; transition to oral carbohydrates once able | None in emergent hypoglycemia | Blood glucose q15 min until >100 mg/dL; identify and treat underlying cause of hypoglycemia | STAT | STAT | - | - |
| Electrolyte correction (hyponatremia) | IV | Enhanced physiologic tremor from hyponatremia | 0.9% NaCl :: IV :: continuous :: Normal saline or hypertonic saline per sodium deficit calculation; correct sodium no faster than 8-10 mEq/L per 24 hours to prevent osmotic demyelination | Hypervolemic hyponatremia (use fluid restriction instead) | Serum sodium q4-6h during correction; strict I/O monitoring; tremor resolution with correction | STAT | STAT | - | - |
| Magnesium sulfate (for hypomagnesemia) | IV | Hypomagnesemia-induced tremor and neuromuscular excitability | 2 g :: IV :: once :: Administer 2 g IV over 1 hour; recheck magnesium in 4-6 hours; repeat 1-2 g IV if still low; transition to oral magnesium oxide 400-800 mg daily | Renal failure (dose adjust); heart block | Serum magnesium levels; deep tendon reflexes; respiratory rate | URGENT | URGENT | ROUTINE | - |
| Propranolol (empiric) | PO | Empiric symptomatic relief for functionally impairing tremor while diagnostic workup in progress; effective for postural and action tremor | 20 mg :: PO :: BID :: Start 20 mg BID; titrate by 20 mg q3-7d based on response and tolerability; target 60-320 mg/day in divided doses; use LA formulation once optimal dose determined | Asthma/severe COPD; bradycardia (HR <50); second/third-degree AV block; decompensated heart failure; severe peripheral vascular disease; concurrent verapamil | HR, BP at each visit; bronchospasm; fatigue, depression; masks hypoglycemia in diabetics | - | ROUTINE | ROUTINE | - |
| Lorazepam (short-term) | PO/IV | Severe acute tremor causing significant distress or functional impairment; short-term bridge while definitive evaluation underway | 0.5 mg :: PO/IV :: q8h PRN :: 0.5-1 mg PO/IV q8h PRN for severe tremor; limit to 48-72 hours acute use; not for chronic management due to dependence risk | Respiratory depression; severe hepatic impairment; myasthenia gravis; concurrent opioids (relative); elderly (fall risk) | Sedation, respiratory rate, fall risk; do NOT prescribe for chronic use | URGENT | URGENT | - | - |

### 3B. Empiric Pharmacologic Treatment (Awaiting Diagnosis)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Propranolol (Inderal) | PO | First-line empiric for postural/action tremor pending diagnosis; effective for essential tremor and enhanced physiologic tremor | 20 mg :: PO :: BID :: Start 20 mg BID; titrate by 20 mg q3-7d; target 60-320 mg/day divided BID-TID; Inderal LA 60-320 mg daily once stable dose determined | Asthma/severe COPD; bradycardia (HR <50); second/third-degree AV block; decompensated heart failure; severe peripheral vascular disease | HR, BP; bronchospasm; fatigue; depression; cold extremities; erectile dysfunction; do NOT stop abruptly (rebound tachycardia) | - | ROUTINE | ROUTINE | - |
| Primidone (Mysoline) | PO | Alternative first-line for action/postural tremor; use when propranolol is contraindicated or inadequate | 12.5 mg :: PO :: QHS :: Start 12.5-25 mg QHS (ultra-low dose); titrate very slowly by 12.5-25 mg/week; target 250-750 mg/day in divided doses; initiation reaction (nausea, dizziness, sedation) common -- start very low | Porphyria; severe sedation to initial dose; pregnancy (teratogenic) | Sedation, ataxia, nausea (especially first dose -- warn patient); CBC periodically; cognitive effects in elderly | - | ROUTINE | ROUTINE | - |
| Gabapentin (Neurontin) | PO | Second-line for tremor when beta-blockers and primidone not tolerated or contraindicated | 300 mg :: PO :: QHS :: Start 300 mg QHS; titrate by 300 mg q3-5d; target 900-1800 mg/day divided TID; max 3600 mg/day; adjust for renal function | Severe renal impairment (dose adjust); respiratory depression with opioids or CNS depressants | Sedation, dizziness, peripheral edema; renal function; suicidality (rare) | - | ROUTINE | ROUTINE | - |
| Topiramate (Topamax) | PO | Second-line for tremor; evidence for essential tremor | 25 mg :: PO :: daily :: Start 25 mg daily; titrate by 25-50 mg/week; target 100-400 mg/day divided BID | Kidney stones; narrow-angle glaucoma; pregnancy (teratogenic); metabolic acidosis | Cognitive effects (word-finding difficulty, concentration); paresthesias; weight loss; kidney stones; metabolic acidosis | - | ROUTINE | ROUTINE | - |
| Clonazepam (Klonopin) | PO | Third-line for tremor; useful when anxiety is a major contributing factor; effective for orthostatic tremor | 0.25 mg :: PO :: BID :: Start 0.25 mg BID; titrate by 0.25 mg q3-5d; target 0.5-4 mg/day divided BID-TID; use lowest effective dose | Respiratory insufficiency; severe hepatic impairment; myasthenia gravis; avoid abrupt discontinuation | Sedation, dependence, fall risk (especially elderly); cognitive impairment; limit duration; taper do not stop abruptly | - | ROUTINE | ROUTINE | - |

### 3C. Etiology-Specific Treatment (When Cause Identified)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Levodopa/Carbidopa (Sinemet) | PO | PD tremor confirmed or strongly suspected based on clinical features and/or DaTscan; diagnostic and therapeutic trial | 25/100 mg :: PO :: TID :: Start 25/100 mg TID with meals; titrate by 25/100 mg q1-2 weeks based on response; robust response supports PD diagnosis | Narrow-angle glaucoma; concurrent non-selective MAOIs; active psychosis (relative) | Nausea, orthostatic hypotension, dyskinesia (long-term); hallucinations; response to levodopa is diagnostically supportive of PD | - | ROUTINE | ROUTINE | - |
| Botulinum toxin (OnabotulinumtoxinA) | IM | Focal tremor refractory to oral medications; head tremor; voice tremor; dystonic tremor; hand tremor affecting function | 50-100 units :: IM :: q3 months :: 50-100 units per affected limb for hand tremor; 40-400 units for head/cervical tremor; individualized by movement disorders specialist; effects onset 1-2 weeks, peak 4-6 weeks | Infection at injection site; myasthenia gravis; pregnancy | Weakness at injection site (dose-related); dysphagia with head/voice injections; repeat q3 months | - | - | ROUTINE | - |
| Methimazole | PO | Hyperthyroid tremor; first-line antithyroid agent for Graves disease causing tremor | 10 mg :: PO :: daily :: Start 10 mg daily; titrate per thyroid function; typical range 5-30 mg daily; tremor resolves with euthyroid state; endocrinology co-management | Pregnancy first trimester (use PTU instead); prior agranulocytosis from antithyroid drugs; severe hepatic disease | Thyroid function tests q4-8 weeks initially; CBC (agranulocytosis risk -- instruct patient to report fever/sore throat immediately); LFTs | - | ROUTINE | ROUTINE | - |
| Propylthiouracil (PTU) | PO | Hyperthyroid tremor; use in first trimester pregnancy or when methimazole is contraindicated | 100 mg :: PO :: TID :: Start 100 mg TID; titrate per thyroid function; typical range 100-200 mg TID; tremor resolves with euthyroid state; endocrinology co-management | Hepatotoxicity (black box warning); prior agranulocytosis from antithyroid drugs | Thyroid function tests q4-8 weeks initially; CBC (agranulocytosis risk); LFTs q1-3 months (hepatotoxicity -- black box); instruct patient to report jaundice, dark urine, abdominal pain | - | ROUTINE | ROUTINE | - |
| D-Penicillamine | PO | Wilson disease confirmed; first-line copper chelation therapy | 250 mg :: PO :: daily :: Start 250 mg daily; increase by 250 mg q4-7d to target 1000-1500 mg/day divided QID; take on empty stomach 1 hour before meals; pyridoxine 25 mg daily supplementation required | Penicillin allergy (relative); renal impairment; blood dyscrasias; lupus-like syndrome history | 24-hour urine copper; CBC q2 weeks for first 3 months then monthly; urinalysis (proteinuria); hepatologist co-management; neurologic monitoring for initial worsening (up to 50% of patients) | - | ROUTINE | ROUTINE | - |
| Trientine (Syprine) | PO | Wilson disease confirmed; use when D-penicillamine is not tolerated or contraindicated | 250 mg :: PO :: TID :: Start 250 mg TID; titrate to 750-1500 mg/day divided TID; take on empty stomach 1 hour before meals; separate from iron supplements by 2 hours | Iron supplementation within 2 hours (chelates iron); pregnancy (relative -- risk-benefit) | 24-hour urine copper q3-6 months; CBC; hepatic function; hepatologist co-management; fewer side effects than D-penicillamine | - | ROUTINE | ROUTINE | - |
| Amantadine | PO | Parkinsonian features suspected but not yet confirmed; mild symptomatic benefit; avoids levodopa commitment | 100 mg :: PO :: daily :: Start 100 mg daily; increase to 100 mg BID after 1 week; max 300 mg/day; reduce dose if CrCl <50 | Severe renal impairment (CrCl <15); seizure history (relative); livedo reticularis | Renal function; hallucinations (especially elderly); insomnia (avoid evening dosing); livedo reticularis; ankle edema | - | ROUTINE | ROUTINE | - |

### 3D. Non-Pharmacologic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Caffeine reduction or elimination | Dietary | Enhanced physiologic tremor exacerbated by caffeine; all tremor types worsened by caffeine | N/A :: Dietary :: continuous :: Reduce caffeine intake gradually to avoid withdrawal headache; target <200 mg/day or elimination; educate on hidden caffeine sources (chocolate, energy drinks, medications) | None | Tremor severity with caffeine reduction; withdrawal symptoms (headache, fatigue for 1-2 weeks) | ROUTINE | ROUTINE | ROUTINE | - |
| Weighted utensils and adaptive equipment | Device | Functional impairment with eating, writing, or ADLs due to hand tremor of any etiology | N/A :: Device :: as needed :: Weighted utensils, stabilizing spoons (Liftware), weighted pens, two-handled cups, button hooks, rocker knives; OT assists with selection and training | None | OT assessment and follow-up; functional improvement | - | ROUTINE | ROUTINE | - |
| Wrist weights | Device | Reduce tremor amplitude during activities; kinetic and postural tremor | N/A :: Device :: as needed :: 1-2 lb wrist weights during functional activities; causes fatigue with prolonged use | None | Arm fatigue monitoring; not for prolonged continuous use | - | - | ROUTINE | - |
| Stress management and relaxation techniques | Behavioral | Stress, anxiety, and fatigue exacerbate all tremor types; anxiety is the primary driver in enhanced physiologic tremor | N/A :: Behavioral :: daily :: Deep breathing exercises, progressive muscle relaxation, mindfulness meditation, biofeedback; formal CBT if anxiety is prominent | None | Tremor severity correlation with stress levels; obtain formal psychiatric referral if anxiety disorder identified | - | ROUTINE | ROUTINE | - |
| Sleep hygiene optimization | Behavioral | Sleep deprivation and fatigue worsen all tremor types | N/A :: Behavioral :: continuous :: Target 7-9 hours sleep; consistent sleep schedule; avoid caffeine after noon; screen for sleep disorders (RBD in PD, OSA) | None | Sleep quality; if RBD suspected, refer for polysomnography | - | ROUTINE | ROUTINE | - |
| Alcohol avoidance counseling | Behavioral | Alcohol transiently suppresses essential tremor but is NOT a treatment; chronic alcohol causes cerebellar tremor; withdrawal causes severe tremor | N/A :: Behavioral :: continuous :: Educate that alcohol is NOT a treatment for tremor despite temporary relief; chronic alcohol worsens tremor long-term through cerebellar toxicity; screen for alcohol use disorder | None | Alcohol use screening (AUDIT-C); if alcohol use disorder identified, refer to addiction medicine | ROUTINE | ROUTINE | ROUTINE | - |
| Limit tremor-exacerbating activities | Behavioral | Avoid or modify activities that worsen tremor or where tremor causes safety risk | N/A :: Behavioral :: continuous :: Plan activities for times of day when tremor is least severe; use both hands for pouring; use straws for drinking; electronic devices over handwriting when possible | None | Functional impact assessment at each visit | - | ROUTINE | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology referral for tremor evaluation when etiology is uncertain, tremor is progressive, or associated neurologic signs present (bradykinesia, rigidity, ataxia, dystonia) | URGENT | URGENT | ROUTINE | - |
| Movement disorders specialist referral for diagnostic uncertainty after initial neurology evaluation, DaTscan interpretation, tremor refractory to first-line therapy, or interventional treatment evaluation (DBS, MRgFUS) | - | ROUTINE | ROUTINE | - |
| Occupational therapy for functional impairment with ADLs; adaptive equipment assessment; handwriting strategies; workplace modification | - | ROUTINE | ROUTINE | - |
| Physical therapy for balance and gait assessment if parkinsonian features or fall risk identified | - | ROUTINE | ROUTINE | - |
| Speech therapy if voice tremor identified affecting communication or swallowing | - | - | ROUTINE | - |
| Endocrinology referral if hyperthyroidism confirmed as tremor etiology for definitive thyroid management | - | ROUTINE | ROUTINE | - |
| Hepatology referral if Wilson disease suspected or confirmed for chelation therapy co-management | - | ROUTINE | ROUTINE | - |
| Psychiatry referral if functional (psychogenic) tremor diagnosed for integrated treatment approach; or if anxiety disorder is primary driver | - | ROUTINE | ROUTINE | - |
| Toxicology or occupational medicine if heavy metal exposure or environmental toxin suspected | - | - | ROUTINE | - |
| Ophthalmology (slit-lamp exam) if Wilson disease suspected and patient age <50 to evaluate for Kayser-Fleischer rings | - | ROUTINE | ROUTINE | - |
| Pharmacy consult for comprehensive medication reconciliation to identify all potential tremor-inducing agents including OTC, herbal, supplements | ROUTINE | ROUTINE | ROUTINE | - |
| Neuropsychology if cognitive concerns in addition to tremor (suggests neurodegenerative process) | - | - | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return immediately for sudden worsening of tremor with new weakness, speech changes, vision changes, or difficulty walking (indicates stroke or structural brain lesion) | STAT | STAT | ROUTINE |
| Return immediately for high fever with severe rigidity and altered consciousness (indicates neuroleptic malignant syndrome if on antipsychotics) | STAT | STAT | ROUTINE |
| Tremor has many causes, most of which are treatable or manageable; an evaluation is needed to determine the specific cause before starting long-term treatment | ROUTINE | ROUTINE | ROUTINE |
| Bring a complete list of ALL medications (prescription, OTC, herbal, supplements) to every appointment as many common medications cause tremor | ROUTINE | ROUTINE | ROUTINE |
| Reduce or eliminate caffeine intake as this often significantly improves tremor regardless of the underlying cause | ROUTINE | ROUTINE | ROUTINE |
| Get adequate sleep (7-9 hours) and manage stress as fatigue and anxiety consistently worsen all types of tremor | - | ROUTINE | ROUTINE |
| Do not self-medicate with alcohol; while alcohol temporarily reduces essential tremor, it is not a treatment and chronic use causes permanent cerebellar damage with worsening tremor | ROUTINE | ROUTINE | ROUTINE |
| Keep a tremor diary noting when tremor is worst, what makes it better or worse, and any new symptoms to share with your neurologist | - | - | ROUTINE |
| Inform all healthcare providers about your tremor so they avoid prescribing medications that worsen it | ROUTINE | ROUTINE | ROUTINE |
| If a specific medication was identified as causing your tremor, do NOT restart it without neurologist approval | STAT | STAT | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Reduce caffeine to <200 mg/day or eliminate entirely; taper gradually over 1-2 weeks to avoid withdrawal headache | ROUTINE | ROUTINE | ROUTINE |
| Limit or avoid alcohol; not a treatment for tremor despite temporary relief | ROUTINE | ROUTINE | ROUTINE |
| Regular exercise (aerobic and strength training) improves overall neurologic health and reduces tremor severity | - | - | ROUTINE |
| Maintain regular sleep schedule; sleep deprivation worsens tremor | - | ROUTINE | ROUTINE |
| Stress reduction techniques (meditation, yoga, tai chi, biofeedback) reduce tremor exacerbation | - | - | ROUTINE |
| Avoid sympathomimetics (decongestants containing pseudoephedrine, diet pills, energy supplements) which worsen tremor | ROUTINE | ROUTINE | ROUTINE |
| Use adaptive equipment (weighted utensils, stabilizing devices) to maintain functional independence | - | ROUTINE | ROUTINE |
| Fall prevention measures if gait or balance affected (non-slip footwear, grab bars, adequate lighting, remove loose rugs) | - | ROUTINE | ROUTINE |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Primary Differential by Tremor Type

| Diagnosis | Tremor Type | Frequency | Distribution | Key Distinguishing Features | Tests to Differentiate |
|-----------|-------------|-----------|-------------|----------------------------|------------------------|
| Essential tremor | Postural + kinetic (action tremor) | 4-12 Hz | Bilateral hands (often asymmetric); head (titubational); voice | Duration >3 years; family history (~50%); alcohol responsive; NO bradykinesia, rigidity, or rest tremor; large tremulous handwriting | Clinical exam; DaTscan normal; response to propranolol/primidone |
| Parkinson's disease | Rest tremor (postural component with re-emergence) | 4-6 Hz | Unilateral onset then bilateral; "pill-rolling" hands; chin/jaw | Bradykinesia (decrement); rigidity (cogwheel); postural instability; hyposmia; RBD; micrographia | DaTscan reduced uptake; clinical exam (MDS criteria); olfactory testing impaired |
| Enhanced physiologic tremor | Postural | 8-12 Hz | Bilateral hands; low amplitude | Reversible cause present: anxiety, caffeine, medications, hyperthyroidism, hypoglycemia, fatigue; resolves when cause removed | TSH; medication review; caffeine assessment; resolves with trigger removal |
| Drug-induced tremor | Variable (postural, rest, or mixed depending on agent) | Variable | Bilateral, often symmetric | Temporal relationship to medication; valproate (postural); lithium (postural/intention); SSRIs (postural); antipsychotics (rest/postural); bronchodilators (postural) | Medication review; drug levels; improvement with dose reduction or discontinuation |
| Cerebellar tremor (intention) | Intention (kinetic, worse at target) | 3-5 Hz | Ipsilateral to cerebellar lesion; limbs > proximal | Dysmetria; dysdiadochokinesia; nystagmus; ataxic gait; scanning speech; past-pointing on finger-to-nose | MRI brain (cerebellar lesion, atrophy); clinical exam for cerebellar signs |
| Holmes tremor (rubral) | Rest + postural + intention (all three) | <4.5 Hz | Unilateral; large amplitude; proximal + distal | Combination of ALL tremor types; very large amplitude; delayed onset after midbrain/thalamic lesion (stroke, demyelination, trauma); poor medication response | MRI brain (midbrain/thalamic lesion); history of prior brain injury/stroke |
| Dystonic tremor | Irregular, jerky, oscillatory | Variable (usually 4-7 Hz) | Focal; in body part affected by dystonia | Irregular amplitude and frequency; "null point" where tremor diminishes; associated dystonic posturing; tremor only without obvious dystonia ("tremor associated with dystonia") | Clinical exam (irregular tremor, null point, dystonic posturing); DaTscan normal; botulinum toxin response |
| Psychogenic (functional) tremor | Variable (any type) | Variable; changes with distraction | Any distribution; often bilateral | Variable frequency; entrainment (tremor adopts frequency of contralateral voluntary tapping); distractibility (tremor stops with cognitive tasks); sudden onset; inconsistent pattern; coactivation sign | Clinical exam (entrainment test, distraction, loading); DaTscan normal; neuropsychiatric evaluation |
| Orthostatic tremor | Postural (standing only) | 13-18 Hz (very high) | Legs; relief with walking or sitting | Occurs ONLY when standing; sensation of unsteadiness; high frequency (often palpable but not visible); relief with sitting, walking, or leaning | Surface EMG showing 13-18 Hz rhythmic discharge; accelerometry |
| Wilson disease | Variable (postural, kinetic, wing-beating) | 3-6 Hz | Proximal > distal; "wing-beating" tremor (arms abducted, elbows flexed) | Age <50; hepatic dysfunction; psychiatric symptoms; Kayser-Fleischer rings; mixed movement disorder (tremor + dystonia + parkinsonism) | Ceruloplasmin (low); 24h urine copper (elevated); slit-lamp exam (K-F rings); MRI (basal ganglia T2 changes) |
| Neuropathic tremor | Postural + kinetic | Variable | Distal; associated with neuropathy | Concomitant peripheral neuropathy (sensory loss, weakness, areflexia); IgM paraproteinemia common cause; CIDP | NCS/EMG (neuropathy); serum protein electrophoresis; anti-MAG antibodies |
| Hyperthyroidism | Enhanced postural | 8-12 Hz | Bilateral hands; fine, rapid | Weight loss; palpitations; heat intolerance; lid lag; goiter; hyperreflexia; tachycardia | TSH (suppressed); free T4 (elevated) |
| Paraneoplastic tremor | Variable | Variable | Variable | Subacute onset; associated cerebellar signs or other paraneoplastic features; weight loss; smoking history | Paraneoplastic antibody panel; CT chest/abdomen/pelvis; PET-CT |

### Key Exam Maneuvers for Tremor Evaluation

| Maneuver | What It Tests | Expected Finding |
|----------|--------------|-----------------|
| Arms at rest in lap, distraction with mental task (serial 7s) | Rest tremor (PD) | Rest tremor emerges or increases with distraction in PD |
| Arms outstretched, fingers spread (15-30 seconds) | Postural tremor (ET, physiologic) | Immediate onset postural tremor (ET); re-emergent tremor after latency (PD) |
| Finger-to-nose (repeatedly) | Intention tremor (cerebellar) | Worsening amplitude as finger approaches target |
| Rapid alternating hand movements | Dysdiadochokinesia (cerebellar) | Irregular rhythm and amplitude if cerebellar dysfunction |
| Handwriting sample and spiral drawing | Tremor characterization | Large tremulous (ET) vs micrographia (PD) |
| Contralateral voluntary rhythmic tapping during tremor observation | Entrainment (functional tremor) | Tremor frequency shifts to match voluntary tapping frequency indicates functional |
| Distraction (cognitive task, contralateral complex movement) | Distractibility (functional tremor) | Tremor stops or markedly reduces with distraction indicates functional |
| Standing with eyes open then closed (Romberg) | Orthostatic tremor assessment | Tremor in legs present ONLY on standing; patient reports unsteadiness rather than tremor |
| Search for "null point" in affected dystonic body part | Dystonic tremor | Tremor diminishes or stops in certain positions indicates dystonic tremor |

---

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Tremor severity (clinical rating: FTM scale, Bain composite score, or spiral drawing) | - | ROUTINE | ROUTINE | - | Each visit; baseline and q3-6 months | Stable or improving with treatment | Worsening triggers reassessment of diagnosis; adjust treatment; order additional workup |
| Neurologic exam (look for emerging signs: bradykinesia, rigidity, ataxia, dystonia) | - | ROUTINE | ROUTINE | - | Each visit | No new neurologic signs developing | New bradykinesia/rigidity indicates PD evolving; new ataxia indicates cerebellar pathology; order DaTscan or MRI |
| Functional impact assessment (QUEST, ADL questionnaire) | - | - | ROUTINE | - | q6-12 months | Minimal functional impairment | Increasing functional impairment triggers treatment intensification; therapy referral; evaluate interventional options |
| Heart rate and blood pressure | - | ROUTINE | ROUTINE | - | Each visit if on propranolol or other beta-blocker | HR >50 bpm; SBP >90 mmHg | HR <50 or symptomatic bradycardia triggers dose reduction; SBP <90 triggers dose reduction or agent switch |
| Handwriting sample / spiral drawing | - | ROUTINE | ROUTINE | - | Each visit | Stable or improved | Progressive deterioration triggers diagnosis reassessment; possible PD evolving or treatment failure |
| TSH (if hyperthyroidism was the cause) | - | ROUTINE | ROUTINE | - | q4-8 weeks until stable, then q6-12 months | Normal (0.4-4.0 mIU/L) | Persistent hyperthyroidism triggers endocrinology management; tremor resolves with euthyroid state |
| Drug levels (if on tremor-inducing medications that cannot be discontinued) | - | ROUTINE | ROUTINE | - | Per drug-specific schedule | Therapeutic range | Supratherapeutic triggers dose reduction; correlate with tremor severity |
| Sedation and cognitive effects (if on primidone, gabapentin, benzodiazepines) | - | ROUTINE | ROUTINE | - | Each visit | Tolerable side effects; no cognitive impairment | Intolerable sedation or cognitive effects triggers dose reduction or agent switch |
| Wilson disease markers (ceruloplasmin, 24h urine copper) if on chelation therapy | - | ROUTINE | ROUTINE | - | q3-6 months | Improving copper levels; stable neurologic exam | Worsening triggers hepatology adjustment; neurologic monitoring for chelation-related neurological deterioration |
| Mood and anxiety assessment | - | ROUTINE | ROUTINE | - | Each visit | No significant depression or anxiety | Depression or anxiety triggers SSRI selection (choose agents that do not worsen tremor); psychiatry referral; note that tremor itself causes anxiety (bidirectional relationship) |
| Fall risk assessment | - | ROUTINE | ROUTINE | - | Each visit if gait involved | No falls | Recurrent falls triggers PT reassessment; home safety evaluation; assistive device |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **Discharge home from ED** | Tremor is chronic/slowly progressive without acute neurologic emergency; no new focal deficits; no concern for stroke or acute structural lesion; outpatient neurology follow-up arranged within 2-4 weeks; immediate metabolic causes addressed; patient educated on caffeine reduction and medication review |
| **Outpatient neurology evaluation** | Most patients; new-onset tremor without red flags; chronic tremor for diagnostic classification; referral within 2-4 weeks for routine evaluation |
| **Urgent neurology referral (within 1-2 weeks)** | Rapidly progressive tremor; tremor with new neurologic signs (bradykinesia, ataxia, weakness); age <50 with tremor and liver disease (Wilson disease concern); significant functional impairment |
| **Admit to floor** | Acute onset tremor with additional neurologic signs requiring expedited workup (MRI, DaTscan, labs); severe drug-induced tremor requiring monitored medication adjustment; Wilson disease with acute neurologic deterioration; tremor causing inability to perform ADLs (feeding, ambulation) without support |
| **Movement disorders specialist referral** | Diagnostic uncertainty after initial neurology evaluation; tremor refractory to first- and second-line medications; DaTscan interpretation needed; candidacy for interventional treatment (DBS, MRgFUS, botulinum toxin); suspected functional tremor requiring confirmation |
| **DBS/MRgFUS evaluation** | Medically refractory essential tremor with significant functional impairment; adequate cognition; no surgical contraindications; confirmed diagnosis (not for undiagnosed tremor) |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| Consensus Statement on the Classification of Tremors | [Bhatia et al. Mov Disord 2018](https://pubmed.ncbi.nlm.nih.gov/29193359/) | 2018 | Task Force of the International Parkinson and Movement Disorder Society; updated tremor classification system (Axis 1: clinical features; Axis 2: etiology) |
| AAN Practice Parameter: Therapies for Essential Tremor | [Zesiewicz et al. Neurology 2011](https://pubmed.ncbi.nlm.nih.gov/22013182/) | 2011 | Propranolol and primidone Level A; topiramate Level B; botulinum toxin Level B for hand tremor |
| MDS Criteria for Essential Tremor Diagnosis | [Bhatia et al. Mov Disord 2018](https://pubmed.ncbi.nlm.nih.gov/29193359/) | 2018 | Bilateral upper limb action tremor for >3 years; absence of other neurologic signs; "ET plus" category for soft signs |
| MDS Clinical Diagnostic Criteria for Parkinson's Disease | [Postuma et al. Mov Disord 2015](https://pubmed.ncbi.nlm.nih.gov/26474316/) | 2015 | Bradykinesia required plus rest tremor or rigidity; supportive criteria and red flags |

### Landmark Studies and Key Evidence

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Propranolol reduces essential tremor amplitude by 50-60% | Class I, Level A | [Cochrane Review: Hedera et al. 2017](https://pubmed.ncbi.nlm.nih.gov/23152214/) |
| Primidone equally effective to propranolol for essential tremor; combination is synergistic | Class I, Level A | [Koller & Vetere-Overfield. Neurology 1989](https://pubmed.ncbi.nlm.nih.gov/2685648/) |
| DaTscan differentiates essential tremor (normal uptake) from Parkinson's disease (reduced uptake) with >95% sensitivity | Class I, Level A | [Benamer et al. Mov Disord 2000](https://pubmed.ncbi.nlm.nih.gov/10884298/) |
| Drug-induced tremor is among the most common causes of tremor; medication review is essential in all patients | Class II, Level B | [Morgan & Sethi. Lancet Neurol 2005](https://pubmed.ncbi.nlm.nih.gov/15721829/) |
| Functional (psychogenic) tremor identified by entrainment and distractibility testing with high specificity | Class II, Level B | [Schwingenschuh et al. Mov Disord 2011](https://pubmed.ncbi.nlm.nih.gov/21692115/) |
| Wilson disease must be excluded in all patients <50 years with new-onset tremor | Class III, Level C | [EASL Clinical Practice Guidelines: Wilson Disease 2012](https://pubmed.ncbi.nlm.nih.gov/22424438/) |
| Orthostatic tremor is characterized by 13-18 Hz frequency on surface EMG; clonazepam first-line treatment | Class III, Level C | [Hassan et al. Brain 2016](https://pubmed.ncbi.nlm.nih.gov/27190023/) |
| Holmes tremor (rubral) results from combined dopaminergic and cerebellar pathway disruption; poor response to medications | Class III, Level C | [Raina et al. Neurol India 2016](https://pubmed.ncbi.nlm.nih.gov/27381128/) |
| Dystonic tremor distinguished by irregular amplitude and null point; botulinum toxin effective | Class II, Level B | [Defazio et al. Mov Disord 2013](https://pubmed.ncbi.nlm.nih.gov/23629708/) |
| MRI-guided focused ultrasound (MRgFUS) effective for medically refractory essential tremor | Class I, Level A | [Elias et al. N Engl J Med 2016](https://pubmed.ncbi.nlm.nih.gov/27557301/) |
| Deep brain stimulation of VIM thalamus effective for essential tremor and PD tremor refractory to medications | Class I, Level A | [Schuurman et al. N Engl J Med 2000](https://pubmed.ncbi.nlm.nih.gov/10657427/) |
| Topiramate effective for essential tremor as second-line agent | Class I, Level B | [Connor et al. Neurology 2008](https://pubmed.ncbi.nlm.nih.gov/18316687/) |
| Enhanced physiologic tremor resolves with removal of exacerbating factors (caffeine, medications, metabolic correction) | Class III, Level C | [Deuschl et al. Mov Disord 1998](https://pubmed.ncbi.nlm.nih.gov/9827612/) |
| Botulinum toxin effective for ET hand tremor but limited by weakness | Class II, Level B | [Brin et al. Neurology 2001](https://pubmed.ncbi.nlm.nih.gov/11706104/) |
| Task Force consensus: tremor evaluation includes classification by activation condition, body distribution, and frequency | Expert consensus | [Deuschl et al. Mov Disord 1998](https://pubmed.ncbi.nlm.nih.gov/9827612/) |

---

## NOTES

- Tremor is the most common movement disorder, affecting approximately 5% of the population over age 65
- Essential tremor and enhanced physiologic tremor are the two most common causes of tremor; Parkinson's disease is the most common cause of rest tremor
- A thorough medication review is the single most important initial step; drug-induced tremor is common and reversible
- The critical clinical distinction is between action tremor (suggests ET, physiologic, drug-induced) and rest tremor (suggests PD); some patients have both
- DaTscan is the key differentiating test when clinical features of ET and PD overlap; it does NOT distinguish PD from atypical parkinsonism (PSP, MSA, CBD)
- Wilson disease must be excluded in ALL patients under 50 years presenting with new tremor, especially with liver disease, psychiatric features, or mixed movement disorder
- Functional (psychogenic) tremor accounts for approximately 3-5% of tremor referrals; entrainment test is the most reliable bedside diagnostic maneuver
- Holmes tremor (rest + postural + intention) is pathognomonic for combined cerebellar and nigrostriatal pathway lesions in the midbrain/thalamus
- Orthostatic tremor is frequently misdiagnosed; diagnosis requires surface EMG showing characteristic 13-18 Hz frequency; patient reports "unsteadiness" rather than "tremor"
- Alcohol responsiveness is characteristic of essential tremor but is NOT a recommended treatment strategy and must not be encouraged
- Start propranolol or primidone as empiric treatment for functionally impairing postural/action tremor while awaiting diagnostic evaluation
- Propranolol and primidone are first-line; start primidone at very low doses (12.5 mg) to avoid initiation reaction
- DBS and MRgFUS are highly effective for medication-refractory essential tremor; VIM thalamus is the target

---

## CHANGE LOG

**v1.1 (February 2, 2026)**
- Reordered lab table columns (Sections 1A/1B/1C) to standard format: Test | ED | HOSP | OPD | ICU | Rationale | Target Finding (C1)
- Reordered imaging table columns (Sections 2A/2B/2C) to standard format: Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications (C2)
- Added ICU column to Section 4A Referrals table (5 columns) (C3)
- Applied proper Unicode section dividers (C4)
- Reordered Section 6 Monitoring table columns to place venue columns after Parameter (C6)
- Split "Methimazole or propylthiouracil" into separate rows with individual dosing in Section 3C (M1)
- Split "D-Penicillamine or trientine" into separate rows with individual dosing in Section 3C (M2)
- Added specific dosing for methimazole (10 mg daily) and PTU (100 mg TID) (M3)
- Added specific dosing for D-penicillamine (250 mg daily titrated) and trientine (250 mg TID) (M4)
- Replaced vague "Correct underlying metabolic derangement" with specific rows for dextrose, electrolyte correction, and magnesium sulfate in Section 3A (M5)
- Removed directive language issues: replaced "consider", "may", "should" throughout with direct action statements (R1)
- Updated version to 1.1 with REVISED date
- Added change log entry documenting all revisions

**v1.0 (February 2, 2026)**
- Initial template creation
- Comprehensive 8-section format focused on EVALUATION of undifferentiated tremor
- Full tremor classification framework (rest, postural, kinetic, intention, task-specific)
- Detailed differential diagnosis table with 12 tremor etiologies including distinguishing features and tests
- Key exam maneuvers table for bedside tremor characterization
- DaTscan indications and interpretation guidance
- Wilson disease screening protocol for patients <50
- Empiric treatment pathway (propranolol/primidone) while awaiting diagnosis
- Etiology-specific treatments including levodopa trial for suspected PD
- Non-pharmacologic interventions (caffeine reduction, adaptive equipment, stress management)
- 15 evidence-based references with PubMed citation links
- Settings: ED, HOSP, OPD

---

## APPENDIX A: Systematic Approach to Tremor Evaluation

### Step 1: Classify the Tremor by Activation Condition
- **Rest tremor:** Arms fully supported in lap, patient distracted -- suggests PD
- **Postural tremor:** Arms outstretched -- suggests ET, enhanced physiologic, drug-induced
- **Kinetic/Intention tremor:** Finger-to-nose worsening at target -- suggests cerebellar lesion
- **Combined (rest + postural + intention):** -- suggests Holmes tremor (midbrain lesion)
- **Task-specific:** Only during writing, playing instrument -- primary writing tremor

### Step 2: Determine Distribution and Symmetry
- **Unilateral onset:** Parkinson's disease; Holmes tremor; cerebellar lesion
- **Bilateral, symmetric:** Enhanced physiologic tremor; drug-induced; essential tremor (often asymmetric)
- **Head tremor (titubational):** Essential tremor (most common); cervical dystonia
- **Voice tremor:** Essential tremor; spasmodic dysphonia
- **Chin/jaw tremor at rest:** Parkinson's disease
- **Legs on standing only:** Orthostatic tremor

### Step 3: Review Medications and Reversible Causes
- **Tremor-inducing medications:** Valproate, lithium, SSRIs/SNRIs, amiodarone, theophylline, bronchodilators, stimulants, antipsychotics, metoclopramide, cyclosporine, tacrolimus, corticosteroids
- **Substances:** Caffeine, alcohol withdrawal, nicotine, sympathomimetics
- **Metabolic:** Hyperthyroidism, hypoglycemia, hyponatremia, hypomagnesemia, hepatic encephalopathy, uremia

### Step 4: Look for Associated Signs
- **Bradykinesia + rigidity:** -- Parkinson's disease or drug-induced parkinsonism
- **Dysmetria + ataxia + nystagmus:** -- Cerebellar pathology
- **Dystonic posturing + null point:** -- Dystonic tremor
- **Variable frequency + entrainment + distractibility:** -- Functional tremor
- **Kayser-Fleischer rings + liver disease + young age:** -- Wilson disease
- **No other signs + bilateral action tremor + family history:** -- Essential tremor

### Step 5: Order Investigations by Priority
1. **All patients:** TSH, CMP, glucose, comprehensive medication review, caffeine assessment
2. **If <50 years or atypical:** Ceruloplasmin, copper, liver function, slit-lamp exam
3. **If diagnostic uncertainty (ET vs PD):** DaTscan
4. **If structural lesion suspected:** MRI brain
5. **If orthostatic tremor suspected:** Surface EMG
6. **If neuropathic tremor suspected:** NCS/EMG
7. **If subacute onset with red flags:** Paraneoplastic antibodies, B12, heavy metals

---

## APPENDIX B: DaTscan Decision Guide for Tremor Evaluation

**When to Order DaTscan:**
- Clinical uncertainty between essential tremor and Parkinson's disease
- Mixed tremor features (both postural and rest tremor) making clinical diagnosis unclear
- Tremor with subtle signs that may or may not represent early parkinsonism
- Need for diagnostic clarification before starting PD-specific treatment

**When NOT to Order DaTscan:**
- Classic essential tremor with bilateral postural/action tremor, family history, no rest tremor, no bradykinesia
- Classic Parkinson's disease with unilateral rest tremor, clear bradykinesia and rigidity
- Obvious drug-induced tremor with clear temporal relationship
- Enhanced physiologic tremor with identified reversible cause
- Clear cerebellar tremor with MRI lesion

**Interpretation:**

| DaTscan Result | Interpretation | Next Step |
|----------------|---------------|-----------|
| Normal bilateral striatal uptake | Essential tremor, enhanced physiologic tremor, drug-induced tremor, dystonic tremor, functional tremor, orthostatic tremor | Treat as ET or identified cause; no dopaminergic therapy |
| Reduced striatal uptake (asymmetric) | Parkinson's disease most likely; also possible in MSA, PSP, DLB, CBD | Movement disorders referral; levodopa trial; does NOT distinguish PD from atypical parkinsonism |
| Reduced striatal uptake (symmetric) | Atypical parkinsonism (PSP, MSA); or advanced PD | Movement disorders referral; further clinical and imaging evaluation |

**Medications to Hold Before DaTscan (2 weeks):**
- Bupropion
- Amphetamines / methylphenidate
- Modafinil
- Cocaine
- Phentermine
- Note: Propranolol, primidone, benzodiazepines, anticholinergics do NOT interfere

---

## APPENDIX C: Tremor-Inducing Medications Quick Reference

| Drug Class | Specific Agents | Tremor Type | Reversibility |
|------------|----------------|-------------|---------------|
| Antiepileptics | Valproate, phenytoin (at toxic levels), carbamazepine (at toxic levels) | Postural, intention (if toxic) | Reversible with dose adjustment |
| Mood stabilizers | Lithium | Postural (fine at therapeutic; coarse at toxic) | Reversible with dose reduction |
| Antidepressants (SSRIs/SNRIs) | Fluoxetine, sertraline, paroxetine, venlafaxine, duloxetine | Fine postural tremor | Usually mild; dose-dependent |
| Antidepressants (TCAs) | Amitriptyline, nortriptyline | Postural tremor | Dose-dependent |
| Antipsychotics (typical) | Haloperidol, chlorpromazine, fluphenazine | Rest tremor (parkinsonian) | Reversible with discontinuation (weeks-months) |
| Antipsychotics (atypical) | Risperidone (dose-dependent), olanzapine | Rest tremor (parkinsonian) | Reversible with discontinuation |
| Antiemetics | Metoclopramide, prochlorperazine | Rest tremor (parkinsonian) | Reversible with discontinuation |
| Bronchodilators | Albuterol, salmeterol, theophylline | Postural tremor | Reversible; dose-dependent |
| Stimulants | Amphetamine, methylphenidate, modafinil | Postural tremor | Reversible |
| Cardiac | Amiodarone, procainamide | Postural tremor; intention | Amiodarone: tremor persists after discontinuation (long half-life) |
| Immunosuppressants | Cyclosporine, tacrolimus, corticosteroids | Postural tremor | Dose-dependent; reversible |
| Other | Caffeine, nicotine, thyroid hormones (excess), medroxyprogesterone | Enhanced physiologic tremor | Reversible |

---

*This template has been validated through the checker/rebuilder pipeline (v1.1) and requires physician review before clinical deployment.*
