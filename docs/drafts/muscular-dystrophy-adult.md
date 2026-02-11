---
title: "Muscular Dystrophy (Adult)"
description: "Clinical decision support for evaluation and management of adult-onset muscular dystrophies"
version: "1.2"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - neuromuscular
  - myopathy
  - genetic
  - muscular-dystrophy
  - cardiac
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Muscular Dystrophy (Adult)

**VERSION:** 1.2
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Revised per checker feedback

---

**DIAGNOSIS:** Muscular Dystrophy (Adult)

**ICD-10:** G71.0 (Muscular dystrophy), G71.01 (Duchenne or Becker muscular dystrophy), G71.02 (Facioscapulohumeral muscular dystrophy), G71.09 (Other specified muscular dystrophies)

**CPT CODES:** 85025 (CBC), 80053 (CMP), 82550 (CK total), 84443 (TSH), 82607 (Vitamin B12), 83036 (HbA1c), 95907-95913 (NCS), 95860-95870 (EMG), 88305 (Muscle biopsy pathology), 81400-81408 (Genetic testing panels), 93000 (12-lead ECG), 93306 (Echocardiogram), 94010 (Spirometry/PFTs), 70553 (MRI brain), 73721 (MRI extremity/muscle)

**SYNONYMS:** muscular dystrophy, adult muscular dystrophy, FSHD, facioscapulohumeral dystrophy, LGMD, limb-girdle muscular dystrophy, Becker muscular dystrophy, BMD, oculopharyngeal muscular dystrophy, OPMD, Emery-Dreifuss muscular dystrophy, EDMD, distal myopathy, adult-onset dystrophy

**SCOPE:** Evaluation and management of muscular dystrophies presenting in adults or diagnosed in adulthood. Covers FSHD, LGMD subtypes, Becker MD, OPMD, Emery-Dreifuss MD, and distal myopathies. Includes diagnostic workup (genetic testing, muscle biopsy), cardiac and respiratory monitoring, symptomatic management, and emerging gene therapies. Excludes myotonic dystrophy (covered separately) and pediatric-onset Duchenne MD (though includes adult Becker MD).

---

**DEFINITIONS:**
- **Facioscapulohumeral dystrophy (FSHD):** Most common adult MD; facial and scapular weakness; D4Z4 repeat contraction (FSHD1) or SMCHD1 mutations (FSHD2)
- **Limb-girdle muscular dystrophy (LGMD):** Group of >30 subtypes with proximal weakness; autosomal dominant (LGMD D) or recessive (LGMD R); now classified by gene name
- **Becker muscular dystrophy (BMD):** X-linked dystrophinopathy; milder than Duchenne; presents in adolescence-adulthood; cardiomyopathy common
- **Oculopharyngeal muscular dystrophy (OPMD):** Late-onset (50s-60s); ptosis and dysphagia; GCN trinucleotide expansion in PABPN1 gene
- **Emery-Dreifuss muscular dystrophy (EDMD):** Early contractures (elbows, ankles, spine); humeroperoneal weakness; cardiac conduction defects (HIGH risk); emerin or lamin A/C mutations

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (All Patients)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CK (total creatine kinase) (CPT 82550) | STAT | STAT | ROUTINE | STAT | Elevated in muscular dystrophies; degree varies by subtype (very high in BMD/LGMD, mildly elevated in FSHD/OPMD) | Normal (30-200 U/L); elevated supports myopathy |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal function (rhabdomyolysis risk); electrolytes; LFTs (may be elevated from muscle source, not hepatic) | Normal; note ALT/AST may be elevated from muscle |
| CBC (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline | Normal |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Thyroid myopathy in differential | Normal |
| Aldolase | - | ROUTINE | ROUTINE | - | Elevated in inflammatory and dystrophic myopathies; may be more sensitive than CK in some dystrophies | Normal |

### 1B. Extended Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Genetic testing panel (muscular dystrophy panel) (CPT 81400-81408) | - | - | ROUTINE | - | Definitive diagnosis; >30 LGMD genes; dystrophin gene for BMD; D4Z4 for FSHD; PABPN1 for OPMD | No pathogenic variant (positive = specific diagnosis) |
| Dystrophin gene analysis (deletion/duplication ± sequencing) | - | - | ROUTINE | - | Becker MD diagnosis; large deletions (60-70%) detected by MLPA; sequencing for point mutations | No deletion/duplication; no pathogenic variant |
| D4Z4 repeat sizing (FSHD1) | - | - | ROUTINE | - | FSHD1: contraction of D4Z4 repeats on chromosome 4q35 (1-10 repeats on permissive 4qA allele) | Normal (>10 repeats); reduced = FSHD1 |
| SMCHD1 gene testing | - | - | EXT | - | FSHD2: SMCHD1 mutations with D4Z4 hypomethylation on permissive allele | No pathogenic variant |
| PABPN1 GCN repeat | - | - | ROUTINE | - | OPMD: GCN expansion (>8 repeats vs normal 6) | Normal (6 repeats); expanded = OPMD |
| EMN/LMNA gene testing | - | - | ROUTINE | - | Emery-Dreifuss: emerin (X-linked) or lamin A/C (AD/AR) mutations; cardiac risk stratification | No pathogenic variant |
| Myositis antibody panel (if inflammatory myopathy in differential) | - | ROUTINE | ROUTINE | - | Differentiate inflammatory from dystrophic myopathy; includes Jo-1, Mi-2, SRP, HMGCR | Negative |
| Troponin | STAT | STAT | - | STAT | Cardiac involvement assessment; may be chronically mildly elevated in dystrophies | Normal (<0.04 ng/mL); chronically elevated in some dystrophies |
| BNP/NT-proBNP | STAT | ROUTINE | ROUTINE | STAT | Heart failure screening; cardiomyopathy | Normal |

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Muscle biopsy with immunohistochemistry | - | EXT | EXT | - | When genetic testing is inconclusive; dystrophin staining (BMD: reduced), sarcoglycan panel (LGMD), merosin (LGMD R23) | Normal staining; reduced/absent specific protein directs genetic testing |
| Whole exome/genome sequencing | - | - | EXT | - | Undiagnosed muscular dystrophy after targeted gene panels; novel gene discovery | No known pathogenic variant |
| MRI of muscles (thigh/calf) (CPT 73721) | - | - | EXT | - | Pattern of fatty infiltration helps differentiate MD subtypes; guides biopsy site | Normal muscle without fatty infiltration |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| NCS/EMG (CPT 95907-95913, 95860-95870) | - | ROUTINE | ROUTINE | - | Characterize myopathic vs neurogenic pattern; guides further workup | Myopathic pattern: short-duration, low-amplitude, polyphasic MUPs; early recruitment; no spontaneous activity (or minimal) | None |
| Echocardiogram (CPT 93306) | URGENT | ROUTINE | ROUTINE | URGENT | ALL patients with muscular dystrophy; cardiomyopathy screening (especially BMD, EDMD, LGMD) | Normal LV function (EF >55%); no wall motion abnormalities; no dilation | None |
| Pulmonary function tests (FVC, FEV1, MIP, MEP) (CPT 94010) | - | ROUTINE | ROUTINE | - | Respiratory muscle involvement; restrictive pattern; guide ventilation decisions | FVC >80% predicted; MIP more negative than -60 cmH2O | None |
| 12-lead ECG (CPT 93000) | STAT | STAT | ROUTINE | STAT | Conduction abnormalities; arrhythmia; EDMD and LMNA carriers at high risk of sudden cardiac death | Normal sinus rhythm; normal PR, QRS, QTc intervals | None |

### 2B. Extended Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Cardiac MRI | - | - | ROUTINE | - | Gold standard for detecting myocardial fibrosis (late gadolinium enhancement); more sensitive than echo for early cardiomyopathy | No late gadolinium enhancement; normal EF; no fibrosis | MRI-incompatible devices; severe renal failure (gadolinium) |
| Holter monitor (24-48 hr) | - | ROUTINE | ROUTINE | - | Arrhythmia detection; EDMD and LMNA carriers especially; AV block, atrial fibrillation | Normal rhythm; no high-grade conduction disease | None |
| Overnight oximetry or sleep study (polysomnography) | - | - | ROUTINE | - | Nocturnal hypoventilation; sleep-disordered breathing; guide NIV initiation | Normal overnight O2 saturation (>95%); no significant desaturations | None |
| MRI of muscles (thigh, calf, shoulder) | - | - | EXT | - | Subtype differentiation by pattern of fatty infiltration; FSHD: periscapular + hamstring; LGMD variable | No fatty infiltration; specific patterns guide diagnosis | MRI-incompatible devices |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Modified barium swallow | - | ROUTINE | ROUTINE | - | OPMD: dysphagia quantification; aspiration risk assessment | Normal swallow; no aspiration or penetration | None |
| Video fluoroscopic swallow study | - | - | ROUTINE | - | OPMD: pharyngeal dysfunction characterization; surgical planning (cricopharyngeal myotomy) | Normal pharyngeal contraction | None |
| Bone density (DEXA) | - | - | ROUTINE | - | Osteoporosis from reduced weight-bearing and if on corticosteroids | Normal T-score (>-1.0) | None |

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| BiPAP/NIV (non-invasive ventilation) | NIV | Acute respiratory failure from respiratory muscle weakness; FVC <50% or acute decompensation | IPAP 10-16 cmH2O :: NIV :: continuous :: IPAP 10-16 cmH2O, EPAP 4-6 cmH2O; titrate to comfort and SpO2 >92%; may need 24-hr support in acute setting | Inability to protect airway; facial trauma preventing mask seal; pneumothorax | SpO2; ABG; respiratory rate; patient comfort; CO2 levels; mask fit | STAT | STAT | - | STAT |
| IV Normal Saline | IV | Rhabdomyolysis prevention/treatment if CK markedly elevated (>5x ULN) or acute renal injury | 1000 mL :: IV :: over 1-2 hr :: 1-2 L NS bolus; target urine output >200 mL/hr if rhabdomyolysis; alkalinize urine if CK >10,000 | Heart failure; volume overload | CK; renal function; urine output; myoglobinuria | STAT | STAT | - | STAT |

### 3B. Cardiac Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Lisinopril | PO | Cardiomyopathy prevention/treatment; ACE inhibitor for LV dysfunction in BMD, LGMD, EDMD | 2.5 mg :: PO :: daily :: Start 2.5-5 mg daily; titrate to 10-20 mg daily; initiate at first sign of LV dysfunction or prophylactically in high-risk dystrophies (BMD) | Bilateral renal artery stenosis; pregnancy; angioedema history; hyperkalemia | BP; K+; renal function; cough; EF on echo | - | ROUTINE | ROUTINE | ROUTINE |
| Carvedilol | PO | Heart failure from cardiomyopathy; beta-blocker for LV dysfunction | 3.125 mg :: PO :: BID :: Start 3.125 mg BID; double dose q2wk as tolerated; max 25 mg BID; take with food | Severe bradycardia; 2nd/3rd degree AV block; decompensated HF; severe asthma | HR; BP; fatigue; fluid retention; EF | - | ROUTINE | ROUTINE | ROUTINE |
| Implantable cardioverter-defibrillator (ICD) / Pacemaker | Device | EDMD and LMNA mutations: prophylactic ICD/pacemaker for conduction defects; high risk of sudden cardiac death even with normal EF | N/A :: Device :: per cardiology :: LMNA mutation carriers: prophylactic ICD/pacemaker per HRS guidelines; do NOT wait for symptomatic bradycardia; BMD cardiomyopathy: ICD per standard heart failure criteria | Specific to device implantation | Device checks q6-12 months; rhythm monitoring; lead integrity | - | ROUTINE | ROUTINE | ROUTINE |

### 3C. Symptomatic and Supportive

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Nocturnal BiPAP | NIV | Nocturnal hypoventilation; FVC <50% predicted or symptomatic nocturnal hypoxemia | IPAP 12-18 cmH2O :: NIV :: nightly :: IPAP 12-18, EPAP 4-6 cmH2O; titrate per polysomnography; start when FVC <50% or earlier if symptomatic; assess compliance | Inability to use mask; untreated pneumothorax | Overnight oximetry; ABG or cap gas q6-12mo; mask comfort and compliance | - | ROUTINE | ROUTINE | - |
| Gabapentin | PO | Pain from musculoskeletal sources; contractures; neuropathic component | 300 mg :: PO :: qHS :: Start 300 mg qHS; titrate by 300 mg q1-3d; target 300-600 mg TID; max 3600 mg/day | Severe renal impairment (dose adjust) | Sedation; dizziness; respiratory depression (caution in respiratory compromise) | - | ROUTINE | ROUTINE | - |
| Acetaminophen | PO | Musculoskeletal pain; contracture-related pain | 500 mg :: PO :: Q6H PRN :: 500-1000 mg q6h as needed; max 3000 mg/day (2000 mg/day in elderly or hepatic impairment) | Severe hepatic impairment | Hepatic function; total daily dose | ROUTINE | ROUTINE | ROUTINE | ROUTINE |
| Baclofen | PO | Spasticity; muscle stiffness from contractures | 5 mg :: PO :: TID :: Start 5 mg TID; increase by 5 mg/dose q3d; max 80 mg/day divided TID-QID; taper to discontinue (do NOT stop abruptly) | Abrupt withdrawal (seizures, hallucinations); severe renal impairment | Sedation; weakness (may unmask underlying weakness); respiratory depression | - | ROUTINE | ROUTINE | - |
| Tizanidine | PO | Spasticity (alternative to baclofen); muscle spasms | 2 mg :: PO :: qHS :: Start 2 mg qHS; may increase by 2-4 mg q6-8h; max 36 mg/day | Concurrent CYP1A2 inhibitors (ciprofloxacin, fluvoxamine); hepatic impairment | LFTs at baseline, 1 month, 3 months; sedation; hypotension; dry mouth | - | ROUTINE | ROUTINE | - |
| Modafinil | PO | Fatigue; excessive daytime sleepiness | 100 mg :: PO :: qAM :: Start 100 mg every morning; may increase to 200 mg daily; avoid afternoon dosing | Hypersensitivity; cardiac arrhythmia; left ventricular hypertrophy | Headache; insomnia; cardiac monitoring if history; BP | - | - | ROUTINE | - |
| Sertraline | PO | Depression; anxiety related to chronic progressive disease (ALTERNATIVE to duloxetine — do NOT combine; serotonin syndrome risk) | 25 mg :: PO :: daily :: Start 25 mg daily; increase by 25-50 mg q1-2 weeks; max 200 mg/day | Concurrent MAOIs; concurrent duloxetine (serotonin syndrome); caution with QT-prolonging drugs | Suicidality (first weeks); GI upset; sexual dysfunction; hyponatremia; serotonin syndrome if combined with other serotonergic agents | - | ROUTINE | ROUTINE | - |
| Duloxetine | PO | Depression with comorbid pain; neuropathic pain component (ALTERNATIVE to sertraline — do NOT combine; serotonin syndrome risk) | 30 mg :: PO :: daily :: Start 30 mg daily x 1-2 weeks; increase to 60 mg daily; max 120 mg/day | Severe hepatic impairment; concurrent MAOIs; concurrent sertraline (serotonin syndrome); uncontrolled narrow-angle glaucoma | LFTs; BP; nausea (take with food); serotonin syndrome if combined with other serotonergic agents | - | ROUTINE | ROUTINE | - |
| Oxybutynin | PO | Urinary urgency and frequency from neurogenic bladder dysfunction | 5 mg :: PO :: BID :: Start 5 mg BID-TID; max 5 mg QID; extended-release 5-30 mg daily preferred | Uncontrolled narrow-angle glaucoma; urinary retention; GI obstruction | Dry mouth; cognitive effects (especially elderly); constipation; urinary retention | - | ROUTINE | ROUTINE | - |
| Mirabegron | PO | Overactive bladder (alternative to anticholinergics; fewer cognitive effects) | 25 mg :: PO :: daily :: Start 25 mg daily; may increase to 50 mg daily | Severe uncontrolled hypertension | BP; urinary retention; hepatic function | - | ROUTINE | ROUTINE | - |
| Cyclobenzaprine | PO | Muscle spasms; musculoskeletal pain | 5 mg :: PO :: TID :: Start 5 mg TID; max 10 mg TID; short-term use (2-3 weeks); avoid in elderly | Concurrent MAOIs; recent MI; arrhythmia; heart failure; hyperthyroidism | Sedation; dry mouth; dizziness; anticholinergic effects | - | ROUTINE | ROUTINE | - |
| Melatonin | PO | Insomnia; sleep disturbance common in chronic neuromuscular disease | 3 mg :: PO :: qHS :: 3-5 mg PO 30-60 min before bedtime; max 10 mg | None significant | Daytime drowsiness; vivid dreams | - | ROUTINE | ROUTINE | - |

### 3D. Disease-Specific Therapies

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Deflazacort | PO | Corticosteroid for ambulatory Duchenne/Becker patients (limited evidence for adult BMD specifically); slows loss of ambulation | 0.9 mg/kg :: PO :: daily :: 0.9 mg/kg/day; evidence strongest in Duchenne; limited data in adult BMD but may be considered; take with food | Bone density; BP; glucose; vaccination status | Active infection; uncontrolled diabetes; systemic fungal infection | Weight; bone density; blood glucose; BP; cataracts; adrenal function | - | - | EXT | - |
| Prednisone (alternate-day) | PO | Alternative corticosteroid for dystrophinopathies when deflazacort unavailable; slows decline in muscle function | 0.75 mg/kg :: PO :: every other day :: 0.75 mg/kg every other day; alternate-day dosing reduces side effects; taper if discontinuing | Bone density; BP; glucose; vaccination status | Active infection; uncontrolled diabetes; GI ulceration | Weight; bone density; blood glucose; BP; cataracts; adrenal function | - | - | EXT | - |
| Cricopharyngeal myotomy (surgical) | Surgical | OPMD with disabling dysphagia; cricopharyngeal muscle dysfunction causing obstruction | N/A :: Surgical :: one-time :: Surgical section of cricopharyngeal muscle; performed by ENT/head-neck surgeon; improves swallowing in 80-90% of OPMD patients | Swallowing study confirming cricopharyngeal dysfunction; anesthesia risk assessment | Active aspiration pneumonia; poor surgical candidate; severe respiratory compromise | Swallowing assessment post-procedure; aspiration monitoring; wound healing | - | EXT | EXT | - |
| Scapular fixation surgery | Surgical | FSHD with severe scapular winging limiting arm elevation; failure of conservative management | N/A :: Surgical :: one-time :: Scapulothoracic fusion or scapulopexy; improves overhead arm function in selected FSHD patients; requires adequate deltoid strength | Adequate deltoid function confirmed; respiratory risk assessment; orthopedic evaluation | Poor surgical candidate; inadequate deltoid function; severe respiratory compromise | Post-operative ROM; shoulder function assessment; wound healing | - | EXT | EXT | - |
| Gene therapy (clinical trials) | Variable | Emerging therapies for specific dystrophy subtypes (LGMD R9/FKRP, LGMD R2/dysferlin, FSHD); currently investigational | Per protocol :: Variable :: per protocol :: Refer eligible patients to registries (clinicaltrials.gov); AAV-based gene replacement for sarcoglycanopathies and dysferlinopathies under investigation | Genetic diagnosis confirmed; trial eligibility screening; informed consent | Per specific trial protocol | Trial-specific adverse events; immune response to AAV vector | - | - | EXT | - |

### ANESTHESIA PRECAUTIONS (CRITICAL)

**ALL patients with muscular dystrophy require anesthesia precautions:**
- **AVOID succinylcholine** — risk of hyperkalemic cardiac arrest and rhabdomyolysis
- **AVOID inhaled anesthetic agents (halothane, isoflurane, sevoflurane)** in dystrophinopathies (BMD/DMD) — malignant hyperthermia-like reactions
- Use non-depolarizing neuromuscular blocking agents (rocuronium with sugammadex reversal)
- Anesthesiologist should be aware of diagnosis and respiratory status preoperatively
- Post-operative respiratory monitoring in PACU/ICU given respiratory muscle weakness

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neuromuscular specialist for diagnostic confirmation, genetic testing interpretation, and long-term management | - | ROUTINE | ROUTINE | - |
| Cardiology for echocardiogram, Holter, cardiac MRI, and cardiomyopathy management; electrophysiology referral for EDMD/LMNA carriers | URGENT | ROUTINE | ROUTINE | URGENT |
| Pulmonology for PFT interpretation, NIV initiation and titration, and respiratory failure management | - | ROUTINE | ROUTINE | URGENT |
| Respiratory therapy for BiPAP setup and titration, cough assist training, and secretion management | - | ROUTINE | ROUTINE | URGENT |
| Genetic counseling for inheritance pattern discussion, family screening, and reproductive planning | - | - | ROUTINE | - |
| Physical therapy for stretching, contracture prevention, submaximal strengthening, and mobility optimization | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL adaptation, upper extremity function, and assistive technology evaluation | - | ROUTINE | ROUTINE | - |
| Speech therapy for OPMD dysphagia assessment, swallowing strategies, and communication support | - | ROUTINE | ROUTINE | - |
| Nutrition/Dietitian for caloric needs assessment, weight management, and dietary modification for dysphagia | - | ROUTINE | ROUTINE | - |
| Orthopedic surgery for scoliosis management, contracture release, and scapular fixation (FSHD) | - | - | ROUTINE | - |
| Social work for disability services, insurance navigation, MDA resources, and caregiver support | - | ROUTINE | ROUTINE | - |
| Palliative care for goals of care discussion and advance care planning in progressive disease | - | ROUTINE | ROUTINE | ROUTINE |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Carry a medical alert card or bracelet stating muscular dystrophy diagnosis and AVOID SUCCINYLCHOLINE for all anesthesia encounters | STAT | ROUTINE | ROUTINE | STAT |
| Return to ED immediately for acute shortness of breath, inability to lie flat, or marked respiratory distress — may indicate acute respiratory failure requiring emergent ventilatory support | STAT | ROUTINE | ROUTINE | - |
| Report new shortness of breath (especially lying down), morning headaches, or excessive daytime sleepiness — may indicate respiratory muscle deterioration needing ventilation support | URGENT | ROUTINE | ROUTINE | - |
| Report palpitations, dizziness, or fainting episodes — may indicate cardiac conduction disease or cardiomyopathy requiring urgent evaluation | STAT | ROUTINE | ROUTINE | - |
| Report worsening swallowing difficulty or choking episodes (OPMD patients) — aspiration risk assessment needed | URGENT | ROUTINE | ROUTINE | - |
| Report dark or cola-colored urine after exercise or illness — may indicate rhabdomyolysis requiring IV hydration | STAT | ROUTINE | ROUTINE | - |
| Maintain regular follow-up with cardiology and pulmonology even if asymptomatic — cardiac and respiratory complications may be silent | - | ROUTINE | ROUTINE | - |
| Inform ALL healthcare providers (surgeons, anesthesiologists, dentists) of muscular dystrophy diagnosis before any procedure requiring sedation or anesthesia | STAT | ROUTINE | ROUTINE | STAT |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Regular low-impact aerobic exercise (swimming, recumbent cycling) as tolerated to maintain cardiovascular fitness; avoid eccentric/high-resistance exercise which may worsen muscle damage | - | ROUTINE | ROUTINE | - |
| Stretching program to prevent and manage contractures; daily range-of-motion exercises for all joints | - | ROUTINE | ROUTINE | - |
| Maintain healthy weight: obesity worsens mobility and respiratory function; underweight/sarcopenia worsens weakness | - | ROUTINE | ROUTINE | - |
| Fall prevention measures: grab bars, non-slip surfaces, assistive devices; home safety evaluation | - | ROUTINE | ROUTINE | - |
| Annual influenza and pneumococcal vaccination; COVID-19 vaccination per guidelines to prevent respiratory infections | - | ROUTINE | ROUTINE | - |
| Aspiration precautions for OPMD patients: upright positioning during meals; thickened liquids as recommended by speech therapy | - | ROUTINE | ROUTINE | - |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Inflammatory myopathy (DM/PM/IBM) | Subacute onset; may have skin rash (DM); elevated CK; responds to immunosuppression (except IBM); autoantibodies present | Myositis antibody panel; muscle biopsy (inflammatory infiltrate); MRI (edema vs fatty infiltration); response to steroids |
| Myotonic dystrophy | Myotonia (delayed relaxation); distal weakness; cataracts; cardiac conduction defects; characteristic facies; DMPK/CNBP genetic testing | Genetic testing (CTG repeat in DM1; CCTG in DM2); EMG (myotonic discharges); clinical exam (grip myotonia) |
| Spinal muscular atrophy (adult-onset, SMA type 3/4) | Proximal weakness without CK elevation (or mild); lower motor neuron pattern on EMG; SMN1 deletion | SMN1 gene deletion testing; EMG (neurogenic not myopathic); CK normal/mildly elevated |
| Metabolic myopathy (Pompe, McArdle, CPT2 deficiency) | Exercise intolerance; episodic rhabdomyolysis; specific enzyme deficiencies | GAA enzyme activity (Pompe); muscle biopsy (glycogen/lipid storage); ischemic forearm test; genetic testing |
| Myasthenia gravis | Fatigable weakness; fluctuating; ptosis and diplopia common; no CK elevation | AChR or MuSK antibodies; RNS/SFEMG; edrophonium test; normal CK |
| Hypothyroid myopathy | Proximal weakness with elevated CK; hypothyroid symptoms; reversible with treatment | TSH (elevated); Free T4 (low); symptoms resolve with thyroid replacement |
| Statin myopathy | Proximal weakness with CK elevation in setting of statin use; anti-HMGCR antibodies in immune-mediated necrotizing myopathy | Statin history; anti-HMGCR antibodies; improvement with statin discontinuation (unless immune-mediated) |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Echocardiogram (EF, LV dimensions) | Annually; q6mo if cardiomyopathy present | EF >55%; no progressive dilation | Initiate/optimize ACE inhibitor and beta-blocker; cardiology referral; cardiac MRI | URGENT | ROUTINE | ROUTINE | URGENT |
| ECG / Holter monitor | Annually; q6mo for EDMD/LMNA carriers | Normal sinus rhythm; no AV block; no atrial arrhythmia | EP evaluation; ICD/pacemaker consideration for LMNA; antiarrhythmics | STAT | ROUTINE | ROUTINE | STAT |
| Pulmonary function tests (FVC, MIP, MEP) | Q6-12 months | FVC >50% predicted; stable trend | Initiate NIV if FVC <50% or symptomatic; pulmonology referral | - | ROUTINE | ROUTINE | - |
| Overnight oximetry | Annually if FVC <80%; or if symptoms of nocturnal hypoventilation | SpO2 >92% overnight; no significant desaturations | Initiate nocturnal BiPAP; formal sleep study | - | ROUTINE | ROUTINE | - |
| CK level | Baseline; then as clinically indicated | Stable; not acutely elevated suggesting rhabdomyolysis | Hydration; renal monitoring if markedly elevated | STAT | ROUTINE | ROUTINE | STAT |
| Swallowing assessment (OPMD) | Q6-12 months | Safe oral intake; no aspiration | Diet modification; speech therapy; consider cricopharyngeal myotomy | - | ROUTINE | ROUTINE | - |
| Functional mobility assessment (timed up-and-go, 6MWT) | Q6-12 months | Stable or slow decline | PT reassessment; assistive device prescription; wheelchair evaluation if needed | - | - | ROUTINE | - |
| Bone density (DEXA) | Q2 years; annually if on steroids | T-score >-2.5 | Calcium, vitamin D supplementation; bisphosphonate if osteoporosis | - | - | ROUTINE | - |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge from ED | Stable respiratory function; no acute cardiac arrhythmia; no rhabdomyolysis; outpatient neuromuscular follow-up arranged |
| Admit to floor | Acute respiratory decompensation requiring NIV; rhabdomyolysis with CK >10x ULN; new cardiac arrhythmia; aspiration pneumonia; new diagnosis requiring expedited workup |
| Admit to ICU | Respiratory failure requiring intubation or continuous NIV; cardiac arrhythmia requiring monitoring/intervention; severe rhabdomyolysis with AKI; perioperative monitoring |
| Outpatient follow-up (neuromuscular) | All patients: q6-12 months; more frequently if declining; genetic counseling if new diagnosis |
| Outpatient follow-up (cardiology/pulmonology) | Annually minimum for all dystrophy patients; q3-6 months if cardiomyopathy or respiratory involvement |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Cardiac screening recommended for all muscular dystrophy patients | Class I, Level B | [Groh WJ et al. Heart Rhythm 2008](https://pubmed.ncbi.nlm.nih.gov/18534376/) |
| LMNA mutation carriers: prophylactic ICD reduces sudden cardiac death risk | Class IIa, Level B | [Meune C et al. J Am Coll Cardiol 2006](https://pubmed.ncbi.nlm.nih.gov/16979003/) |
| ACE inhibitors delay cardiomyopathy progression in Becker MD | Class IIa, Level B | [Duboc D et al. J Am Coll Cardiol 2005](https://pubmed.ncbi.nlm.nih.gov/16168286/) |
| NIV improves survival in neuromuscular respiratory failure | Class I, Level B | [Simonds AK. Eur Respir J 2006](https://pubmed.ncbi.nlm.nih.gov/16387949/) |
| Avoid succinylcholine in all muscular dystrophies (hyperkalemic arrest risk) | Class I, Level C | [Hayes J et al. Br J Anaesth 2008](https://pubmed.ncbi.nlm.nih.gov/18344556/) |
| FSHD genetic diagnosis: D4Z4 contraction on 4qA allele | Class I, Level A | [Lemmers RJLF et al. Science 2010](https://pubmed.ncbi.nlm.nih.gov/20724583/) |
| LGMD classification update (2018) | Consensus | [Straub V et al. Neuromuscul Disord 2018](https://pubmed.ncbi.nlm.nih.gov/30055862/) |
| Cricopharyngeal myotomy improves swallowing in OPMD | Class IIa, Level B | [Coiffier L et al. Neuromuscul Disord 2006](https://pubmed.ncbi.nlm.nih.gov/16427281/) |

---

## NOTES

- CRITICAL: ALL muscular dystrophy patients require anesthesia precautions — AVOID succinylcholine (hyperkalemic arrest) and inhaled anesthetics in dystrophinopathies
- Cardiac involvement is a LEADING cause of death in BMD, EDMD, and LGMD; proactive screening saves lives
- LMNA (lamin A/C) mutations carry very high risk of sudden cardiac death from conduction defects — prophylactic ICD/pacemaker should be considered even with normal EF
- FSHD is the most common adult-onset MD (~1:8,000-20,000); facial weakness may be subtle; scapular winging is often the first noticed feature
- CK levels vary dramatically by subtype: BMD/LGMD often 5-50x ULN; FSHD 1-5x ULN; OPMD often normal or minimally elevated
- Genetic testing has largely replaced muscle biopsy as the first-line diagnostic approach; biopsy reserved for inconclusive genetic results
- Muscle MRI can guide diagnosis by showing characteristic patterns of fatty infiltration specific to each dystrophy subtype
- Respiratory failure develops insidiously; FVC should be monitored regularly; initiate NIV when FVC <50% predicted or earlier if symptomatic
- Nocturnal hypoventilation (morning headaches, daytime somnolence) may precede daytime respiratory failure by months-years
- OPMD: late onset (50s-60s); ptosis and dysphagia are hallmark; cricopharyngeal myotomy can significantly improve swallowing
- Gene therapy trials are actively enrolling for multiple dystrophies; refer interested patients to clinical trial registries
- Eccentric/high-resistance exercise may worsen muscle damage in dystrophies; low-impact aerobic exercise is preferred

---

## CHANGE LOG

**v1.2 (February 11, 2026)**
- Removed duplicate 12-lead ECG from Section 1A Core Labs (retained in Section 2A Essential Studies)
- Added serotonin syndrome warning to sertraline and duloxetine in Section 3C; marked as alternatives, not for concurrent use
- Added ICU coverage for Section 3B cardiac medications (lisinopril, carvedilol, ICD/pacemaker) — ICU patients with cardiomyopathy need continuation
- Added HOSP coverage for vaccination counseling in Section 4C

**v1.1 (February 11, 2026)**
- Expanded Section 3C from 3 to 13 medications: added baclofen and tizanidine (spasticity), modafinil (fatigue), sertraline and duloxetine (mood/depression), oxybutynin and mirabegron (bladder), cyclobenzaprine (muscle spasms), melatonin (insomnia)
- Expanded Section 3D from 2 to 5 entries: added prednisone alternate-day dosing, scapular fixation surgery (FSHD), gene therapy clinical trials
- Expanded Section 4A from 9 to 12 referrals: added respiratory therapy, nutrition/dietitian, social work
- Expanded Section 4B from 5 to 8 instructions: added emergent return precaution, rhabdomyolysis warning, anesthesia disclosure instruction
- Fixed structured dosing format: standardized all medications to single starting dose in first field (lisinopril, carvedilol, gabapentin, acetaminophen, BiPAP, nocturnal BiPAP)
- Fixed ICD/pacemaker setting coverage: added HOSP and clarified dosing instructions
- Fixed Section 4B setting coverage: added HOSP column for follow-up instruction
- Added palliative care ICU coverage in Section 4A

**v1.0 (February 11, 2026)**
- Initial template creation
- Covers FSHD, LGMD, Becker, OPMD, and EDMD
- Cardiac and respiratory management protocols
- Anesthesia precautions prominently featured
- Evidence references with PubMed links
