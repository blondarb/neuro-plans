---
title: "Hereditary Neuropathy / Charcot-Marie-Tooth Disease (CMT)"
description: "Clinical decision support for evaluation and management of hereditary motor and sensory neuropathies"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - neuromuscular
  - neuropathy
  - hereditary
  - genetic
  - outpatient
  - CMT
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Hereditary Neuropathy / Charcot-Marie-Tooth Disease (CMT)

**VERSION:** 1.0
**CREATED:** February 11, 2026
**REVISED:** February 11, 2026
**STATUS:** Draft

---

**DIAGNOSIS:** Hereditary Neuropathy / Charcot-Marie-Tooth Disease (CMT)

**ICD-10:** G60.0 (Hereditary motor and sensory neuropathy), G60.1 (Refsum disease), G60.8 (Other hereditary and idiopathic neuropathies), G60.9 (Hereditary and idiopathic neuropathy, unspecified)

**CPT CODES:** 85025 (CBC), 80053 (CMP), 81324 (PMP22 duplication/deletion analysis), 81405-81406 (Molecular pathology, multigene panels), 81479 (Unlisted molecular pathology), 95907-95913 (NCS), 95860-95870 (EMG), 84443 (TSH), 82607 (Vitamin B12), 83036 (HbA1c), 82784 (Immunoglobulins quantitative), 86255 (Antibody screen), 70553 (MRI brain), 72141-72158 (MRI spine), 89050 (CSF analysis), 94010 (Spirometry), 93000 (12-lead ECG), 93306 (Echocardiogram)

**SYNONYMS:** Charcot-Marie-Tooth disease, CMT, hereditary motor and sensory neuropathy, HMSN, peroneal muscular atrophy, CMT1A, CMT1B, CMT2, CMT1X, CMTX1, CMT4, hereditary neuropathy with liability to pressure palsies, HNPP, tomaculous neuropathy, Dejerine-Sottas disease, CMT3, hereditary demyelinating neuropathy, hereditary axonal neuropathy, distal hereditary motor neuropathy, dHMN

**SCOPE:** Evaluation and management of hereditary motor and sensory neuropathies (Charcot-Marie-Tooth disease and related disorders) in adults. Covers CMT1 (demyelinating), CMT2 (axonal), CMTX (X-linked), CMT4 (autosomal recessive), HNPP, and Dejerine-Sottas disease. Includes genetic testing strategy, electrodiagnostic classification, neurotoxic medication avoidance, supportive management, and surgical considerations. Excludes hereditary sensory and autonomic neuropathies (HSAN) as primary diagnosis but includes in differential. Excludes pediatric-onset evaluation (but most CMT presents in childhood/adolescence with adult follow-up).

---

**DEFINITIONS:**
- **Charcot-Marie-Tooth disease (CMT):** Group of inherited peripheral neuropathies characterized by progressive distal muscle weakness and atrophy, sensory loss, and skeletal deformities (pes cavus, hammertoes)
- **CMT1 (demyelinating):** Autosomal dominant; NCV uniformly slow (median motor <38 m/s); CMT1A (PMP22 duplication, ~60% of all CMT) is most common subtype
- **CMT2 (axonal):** Autosomal dominant; NCVs normal or mildly slow (median motor >38 m/s) with reduced amplitudes; CMT2A (MFN2 mutation) is most common subtype
- **CMTX1 (X-linked):** GJB1/Connexin 32 mutation; intermediate NCVs in males (25-40 m/s), mild or normal in carrier females; second most common CMT form
- **HNPP (Hereditary Neuropathy with Liability to Pressure Palsies):** PMP22 deletion; episodic painless mononeuropathies triggered by minor compression; tomacula on nerve biopsy
- **Dejerine-Sottas disease (CMT3):** Severe early-onset demyelinating neuropathy (NCV <10-12 m/s); usually PMP22, MPZ, or EGR2 mutations; hypertrophic nerves

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (All Patients)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline hematologic assessment | Normal |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Renal/hepatic function; electrolytes; glucose | Normal |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Exclude diabetic neuropathy as comorbid or alternative diagnosis | <5.7% |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Exclude thyroid-related neuropathy | Normal |
| Vitamin B12 (CPT 82607) | - | ROUTINE | ROUTINE | - | Exclude B12 deficiency neuropathy (treatable cause) | >300 pg/mL |
| CK (creatine kinase) | - | ROUTINE | ROUTINE | - | Mildly elevated in some CMT2 subtypes; markedly elevated suggests myopathy | Normal or mildly elevated |
| ESR / CRP | - | ROUTINE | ROUTINE | - | Exclude inflammatory/acquired neuropathy | Normal |

### 1B. Genetic Testing (Stepwise Approach)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| PMP22 duplication/deletion (CPT 81324) | - | - | ROUTINE | - | First-line test: PMP22 duplication = CMT1A (~60% of CMT1); PMP22 deletion = HNPP; order if demyelinating NCS pattern (median motor NCV <38 m/s) | Identifies CMT1A or HNPP |
| GJB1/Connexin 32 sequencing (CPT 81406) | - | - | ROUTINE | - | Second-line if PMP22 negative; CMTX1 is second most common CMT; order especially if intermediate NCV (25-40 m/s) or X-linked pattern | Identifies CMTX1 |
| MPZ (P0) sequencing (CPT 81406) | - | - | ROUTINE | - | CMT1B; order if PMP22 and GJB1 negative with demyelinating pattern; late-onset axonal phenotype also possible | Identifies CMT1B |
| MFN2 sequencing (CPT 81406) | - | - | ROUTINE | - | CMT2A; most common axonal CMT subtype; order if axonal NCS pattern (median motor NCV >38 m/s) | Identifies CMT2A |
| CMT multigene panel (NGS) (CPT 81479) | - | - | ROUTINE | - | Comprehensive panel (>80 genes) if targeted testing negative; includes CMT1, CMT2, CMT4, CMTX, dHMN genes; higher yield than sequential single-gene testing in atypical cases | Identifies causative mutation |
| Whole exome sequencing (WES) | - | - | EXT | - | Consider if multigene panel negative in strong hereditary phenotype; may identify novel mutations | Identifies causative variant |

### 1C. Extended Labs (Exclude Acquired Mimics)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| SPEP / UPEP with immunofixation | - | ROUTINE | ROUTINE | - | Exclude paraproteinemic neuropathy (anti-MAG IgM neuropathy mimics CMT1) | No monoclonal protein |
| Anti-MAG antibodies | - | - | ROUTINE | - | Anti-MAG neuropathy causes uniform demyelination mimicking CMT1; treatable | Negative |
| ANA (CPT 86235) | - | ROUTINE | ROUTINE | - | Autoimmune neuropathy screen | Negative |
| Quantitative immunoglobulins (CPT 82784) | - | ROUTINE | ROUTINE | - | Exclude CIDP (elevated CSF protein); IgM gammopathy evaluation | Normal |
| Phytanic acid level | - | - | EXT | - | Refsum disease (G60.1): elevated phytanic acid, demyelinating neuropathy, retinitis pigmentosa, ichthyosis; treatable with dietary restriction | Normal (<0.3 mg/dL) |
| Very long chain fatty acids (VLCFA) | - | - | EXT | - | Adrenomyeloneuropathy (adult AMN): axonal neuropathy with myelopathy; X-linked | Normal |

### 1D. Lumbar Puncture (Selected Cases)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CSF protein, cell count, glucose | - | ROUTINE | EXT | - | Distinguish CMT from CIDP: CMT has normal or mildly elevated protein; CIDP typically >45 mg/dL; Dejerine-Sottas may have elevated protein | Normal protein (<45 mg/dL); normal cells; normal glucose |
| CSF oligoclonal bands | - | ROUTINE | EXT | - | Absent in CMT; present in inflammatory conditions | Absent |

---

## 2. IMAGING

### 2A. Core Imaging

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| MRI brain with contrast (CPT 70553) | - | ROUTINE | ROUTINE | - | CMTX1: transient white matter lesions during metabolic stress; CMT4 subtypes with CNS involvement; exclude structural causes | Normal in most CMT; CMTX1 may show reversible white matter changes |
| MRI spine (cervical/lumbar) | - | ROUTINE | ROUTINE | - | Exclude compressive myelopathy/radiculopathy as contributing factor; hypertrophic nerves in Dejerine-Sottas | No cord compression; may show nerve root hypertrophy in demyelinating CMT |

### 2B. Advanced Imaging

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| MR neurography (brachial plexus / lumbosacral plexus) | - | - | EXT | - | Assess nerve hypertrophy pattern; differentiate from CIDP or neoplastic infiltration; research use in CMT | Uniform nerve enlargement (CMT1); CIDP tends to be patchy/multifocal |
| Nerve ultrasound (high-resolution) | - | - | ROUTINE | - | Non-invasive assessment of nerve cross-sectional area; diffusely enlarged nerves in CMT1A; focal enlargement suggests acquired neuropathy or HNPP | Diffusely enlarged nerves (CMT1); normal caliber (CMT2) |
| Chest X-ray / CT chest | - | ROUTINE | EXT | - | Screen for diaphragmatic elevation (phrenic nerve involvement in CMT2C/TRPV4); scoliosis assessment | Normal; no diaphragm elevation |

### 2C. Pulmonary Function Assessment

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| Spirometry (FVC upright and supine) (CPT 94010) | - | ROUTINE | ROUTINE | STAT | Assess respiratory muscle weakness; FVC <80% predicted or >10% drop supine indicates diaphragm weakness; relevant in severe CMT, CMT2C, CMT4 | FVC >80% predicted; <10% supine drop |
| Echocardiogram (CPT 93306) | - | ROUTINE | ROUTINE | - | Screen for cardiomyopathy in LMNA-related CMT2; arrhythmias in selected subtypes | Normal LVEF; no structural abnormalities |
| ECG (CPT 93000) | - | ROUTINE | ROUTINE | - | Screen for conduction abnormalities; LMNA mutations associated with cardiac conduction disease | Normal sinus rhythm; no conduction block |

---

## 3. TREATMENT

### 3A. Neurotoxic Medication Avoidance (CRITICAL)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| **AVOID vincristine** | - | ABSOLUTE CONTRAINDICATION in CMT | Vincristine causes severe, potentially fatal neuropathy in CMT patients even at standard doses | ABSOLUTE CONTRAINDICATION — do NOT administer | Alert oncology; document allergy/contraindication prominently in chart | STAT | STAT | STAT | STAT |
| **AVOID high-dose/prolonged nitrofurantoin** | - | DEFINITE HIGH RISK | Can cause severe worsening of neuropathy | Avoid in CMT | Monitor for worsening neuropathy if inadvertently given | STAT | STAT | ROUTINE | STAT |
| **AVOID cisplatin/oxaliplatin** | - | DEFINITE HIGH RISK | Platinum agents cause dose-dependent neurotoxicity; accelerated in CMT | Use alternative chemotherapy agents | Oncology co-management if chemotherapy needed | STAT | STAT | ROUTINE | STAT |
| **AVOID taxanes (paclitaxel, docetaxel)** | - | DEFINITE HIGH RISK | Microtubule-disrupting agents worsen neuropathy | Use alternatives when possible | Discuss risk/benefit with oncology if no alternative | STAT | STAT | ROUTINE | STAT |
| **Use caution: metronidazole (prolonged courses)** | - | MODERATE RISK | Prolonged courses (>2 weeks) can worsen neuropathy | Limit duration; use alternatives when possible | Monitor for worsening symptoms | URGENT | URGENT | ROUTINE | URGENT |
| **Use caution: fluoroquinolones** | - | MODERATE RISK | Associated with peripheral neuropathy; risk additive in CMT | Use alternatives when possible | Monitor for new or worsening symptoms | URGENT | URGENT | ROUTINE | URGENT |
| **Use caution: amiodarone** | - | MODERATE RISK | Can cause demyelinating neuropathy with prolonged use | Minimize dose and duration; use alternatives | Periodic NCS if prolonged use required | URGENT | URGENT | ROUTINE | URGENT |
| **Use caution: statins** | - | LOW-MODERATE RISK | May worsen neuropathy symptoms in some patients | Not absolute contraindication; weigh cardiovascular benefit | Monitor symptoms; discontinue if worsening | - | ROUTINE | ROUTINE | - |

### 3B. Neuropathic Pain Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Gabapentin | PO | Neuropathic pain (first-line) | 300 mg; 600 mg; 900 mg :: PO :: TID :: Start 300 mg nightly, increase by 300 mg every 3-5 days to 300-1200 mg TID as tolerated | Renal impairment (dose adjust); sedation risk | Sedation, dizziness, edema; renal dose adjustment | - | ROUTINE | ROUTINE | - |
| Pregabalin | PO | Neuropathic pain (first-line alternative) | 75 mg; 150 mg; 300 mg :: PO :: BID :: Start 75 mg BID, increase to 150-300 mg BID over 1-2 weeks | Renal impairment (dose adjust); sedation risk | Sedation, weight gain, edema; renal dose adjustment | - | ROUTINE | ROUTINE | - |
| Duloxetine | PO | Neuropathic pain (first-line alternative) | 30 mg; 60 mg :: PO :: daily :: Start 30 mg daily for 1 week, then increase to 60 mg daily | Hepatic impairment; concurrent MAOIs; uncontrolled glaucoma | LFTs; serotonin syndrome risk; blood pressure | - | ROUTINE | ROUTINE | - |
| Amitriptyline | PO | Neuropathic pain (second-line) | 10 mg; 25 mg; 50 mg :: PO :: nightly :: Start 10 mg nightly, increase by 10 mg weekly to 25-75 mg nightly | Cardiac conduction disease; urinary retention; glaucoma; elderly (fall risk) | ECG if >50 mg/day; anticholinergic effects; QTc | - | ROUTINE | ROUTINE | - |
| Tramadol | PO | Moderate-severe neuropathic pain (third-line) | 50 mg; 100 mg :: PO :: Q6H PRN :: 50-100 mg every 6 hours as needed; max 400 mg/day | Seizure disorder; concurrent serotonergic drugs; respiratory depression risk | Seizure risk; serotonin syndrome; dependence risk | URGENT | ROUTINE | ROUTINE | - |

### 3C. Orthotic and Rehabilitative Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Ankle-foot orthoses (AFOs) | Device | Foot drop, ankle instability, gait impairment | Custom-molded AFOs preferred; articulated AFOs allow ankle motion :: Device :: continuous during ambulation :: Custom fitting by orthotist; reassess annually or with functional decline | Skin breakdown; poor fitting | Assess fit, skin integrity, functional benefit every 6-12 months | - | ROUTINE | ROUTINE | - |
| Physical therapy (PT) | Rehab | Maintain strength, flexibility, balance; prevent contractures | PT evaluation and program :: Rehab :: 2-3x/week initially :: Moderate-intensity strengthening (avoid eccentric overload); stretching; balance training; aquatic therapy | Overexertion (avoid high-resistance eccentric exercise) | Functional assessments (6MWT, timed up-and-go); adjust program to avoid overwork weakness | - | ROUTINE | ROUTINE | - |
| Occupational therapy (OT) | Rehab | Hand weakness, fine motor impairment, ADL adaptation | OT evaluation and program :: Rehab :: 1-2x/week :: Adaptive equipment, hand strengthening, splinting for intrinsic weakness | None | Functional hand assessments; adaptive equipment needs | - | ROUTINE | ROUTINE | - |
| Thumb opposition splint / hand splints | Device | Thenar weakness, difficulty with pinch grip | Custom or prefabricated splints :: Device :: during activities :: Fitted by OT/orthotist | Skin breakdown | Assess fit and functional benefit | - | ROUTINE | ROUTINE | - |
| Assistive devices (cane, walker, wheelchair) | Device | Progressive gait impairment, fall risk | Appropriate assistive device :: Device :: as needed :: PT assessment for device selection; powered wheelchair for severe cases | None | Reassess mobility needs with disease progression | - | ROUTINE | ROUTINE | - |

### 3D. Surgical Management (Selected Cases)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Foot/ankle reconstructive surgery | Surgical | Fixed pes cavus, hammertoes, ankle instability unresponsive to orthoses | Orthopedic evaluation :: Surgical :: elective :: Procedures include plantar fascia release, posterior tibial tendon transfer, calcaneal osteotomy, triple arthrodesis; staged procedures preferred | Active infection; poor healing potential; minimal functional impairment | Post-operative rehabilitation; monitor for recurrence; long-term orthotic use may still be needed | - | ROUTINE | ROUTINE | - |
| Carpal tunnel release | Surgical | Median neuropathy at wrist (common comorbidity in CMT; also HNPP) | Standard carpal tunnel release :: Surgical :: elective :: Lower success rate in CMT than idiopathic CTS; discuss expectations | Asymptomatic; mild symptoms manageable with splinting | Symptom relief; NCS may remain abnormal | - | ROUTINE | ROUTINE | - |
| Scapular fixation (scapulothoracic fusion) | Surgical | Severe scapular winging (CMT1 with serratus anterior weakness) | Orthopedic evaluation :: Surgical :: elective :: Scapulothoracic fusion improves shoulder function and cosmesis | Mild winging without functional impairment | Post-operative shoulder ROM; functional improvement | - | - | EXT | - |

### 3E. Emerging Therapies and Disease-Modifying Agents

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| PXT3003 (baclofen-naltrexone-sorbitol) | PO | CMT1A (investigational) | Clinical trial dosing :: PO :: TID :: Phase III PLEO-CMT-3 trial; targets PMP22 overexpression | Investigational; not yet FDA-approved | Trial endpoints: CMTNS, 10-meter walk test | - | - | EXT | - |
| Ascorbic acid (high-dose vitamin C) | PO | CMT1A — NOT RECOMMENDED | Not recommended :: PO :: daily :: Multiple RCTs (TREAT-CMT, Pareyson 2011) showed NO benefit in CMT1A despite preclinical promise | Not effective; do not prescribe for CMT | N/A — no proven benefit | - | - | - | - |

---

## 4. RECOMMENDATIONS

### 4A. General Recommendations (All Patients)

- Provide patients with CMT Foundation neurotoxic medication list; document prominently in medical record and medication allergy list
- Genetic counseling for all patients with confirmed or suspected CMT — discuss inheritance pattern (AD, AR, X-linked), family planning, and predictive testing for at-risk relatives
- Avoid excessive eccentric exercise and overwork weakness; moderate aerobic exercise and low-to-moderate resistance training are safe and beneficial
- Annual foot examination by podiatrist experienced with neuromuscular conditions; early orthotic intervention prevents deformity progression
- Fall risk assessment at every visit; home safety evaluation as needed
- Weight management — excess weight increases functional burden on weakened muscles
- Vocational counseling for patients with progressive hand weakness affecting employment

### 4B. Setting-Specific Recommendations

- **ED:** CMT patients presenting to ED: verify neurotoxic medication avoidance (especially vincristine, nitrofurantoin); document CMT diagnosis prominently; avoid succinylcholine (risk of hyperkalemia in severe cases with muscle wasting); consider HNPP if recurrent painless compression neuropathies
- **Inpatient:** Pressure point padding during prolonged procedures/surgeries (especially in HNPP); physical and occupational therapy evaluation; document neurotoxic medication alerts; monitor respiratory function in severe CMT (FVC if respiratory symptoms)
- **Outpatient:** Longitudinal care model with neuromuscular specialist; annual assessments with CMT Neuropathy Score (CMTNS/CMTNSv2); coordinate orthopedic, PT/OT, orthotics, genetic counseling; reassess pain management; annual PFTs if respiratory involvement suspected
- **ICU:** Rare unless perioperative or respiratory failure in severe CMT; avoid neurotoxic agents; cautious neuromuscular blocking agent use; avoid succinylcholine; monitor respiratory weaning parameters; HNPP patients vulnerable to prolonged compression neuropathies from positioning

### 4C. Patient and Family Education

- CMT is a slowly progressive inherited condition — set realistic expectations; most patients maintain ambulation throughout life, though ~10% of CMT1A patients require wheelchair
- Neurotoxic drug avoidance is the single most important actionable step — carry medication alert card or bracelet
- Regular moderate exercise improves fitness and quality of life without worsening neuropathy
- Genetic counseling recommended for family planning; inheritance pattern depends on CMT subtype
- CMT Foundation (cmtausa.org) provides educational materials, support groups, and clinical trial information
- Fatigue is a recognized but underappreciated feature of CMT — pacing and energy conservation strategies help

---

## 5. DIFFERENTIAL DIAGNOSIS

| Diagnosis | Key Distinguishing Features | Key Differentiating Test |
|-----------|---------------------------|------------------------|
| CIDP (chronic inflammatory demyelinating polyneuropathy) | Acquired; progressive or relapsing; proximal AND distal weakness; elevated CSF protein (>45 mg/dL); nerve ultrasound shows patchy enlargement; responds to IVIg/steroids | NCS (non-uniform slowing, temporal dispersion in CIDP vs uniform slowing in CMT1); CSF protein; treatment response |
| Anti-MAG neuropathy | Acquired; distal predominant; IgM paraprotein with anti-MAG antibodies; slowly progressive; tremor common; uniform demyelination mimics CMT1 | SPEP/immunofixation; anti-MAG antibody titer |
| Hereditary sensory and autonomic neuropathy (HSAN) | Prominent sensory loss including pain insensitivity; autonomic dysfunction; painless injuries and ulceration; less motor involvement | Clinical phenotype (sensory predominant); genetic testing (SPTLC1, WNK1, IKBKAP, NTRK1) |
| Distal myopathy | Distal weakness mimicking CMT; normal or mildly abnormal NCS; myopathic EMG pattern; elevated CK | EMG (myopathic MUPs); CK; muscle biopsy; genetic testing (dysferlin, GNE, myotilin) |
| Spinal muscular atrophy (SMA type III/IV) | Proximal > distal weakness; fasciculations; no sensory loss; childhood onset typical | SMN1 deletion testing; EMG (anterior horn cell pattern) |
| Friedreich ataxia | Ataxia, areflexia, sensory neuropathy, cardiomyopathy, scoliosis; progressive ataxia is dominant feature | FXN GAA repeat expansion; echocardiogram |
| Adrenomyeloneuropathy (AMN) | Axonal neuropathy with progressive myelopathy (spastic paraparesis); X-linked; adrenal insufficiency | VLCFA levels (elevated); ABCD1 gene testing |
| Refsum disease | Demyelinating neuropathy with retinitis pigmentosa, cerebellar ataxia, ichthyosis, elevated CSF protein | Phytanic acid level (markedly elevated) |
| Hereditary transthyretin amyloidosis (hATTR) | Progressive axonal sensorimotor and autonomic neuropathy; cardiomyopathy; family history; late onset | TTR gene sequencing; tissue biopsy with Congo red stain |
| Multifocal acquired demyelinating sensory and motor neuropathy (MADSAM/Lewis-Sumner) | Asymmetric, multifocal; sensory AND motor involvement; conduction block; responds to IVIg/steroids | NCS (asymmetric, multifocal conduction block); treatment response |

---

## 6. MONITORING

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| CMT Neuropathy Score (CMTNS/CMTNSv2) | Every 6-12 months | Stable or minimal change | Document progression rate; adjust supportive care; consider clinical trial enrollment |
| Manual muscle testing | Every 6-12 months | Stable strength | Adjust PT/OT program; orthotic reassessment; functional adaptation |
| Spirometry (FVC upright and supine) | Annually if FVC <80% or respiratory symptoms; baseline then as indicated | FVC >80% predicted; <10% supine drop | Refer pulmonology; consider NIV/BiPAP if FVC <50% or symptomatic; sleep study if nocturnal hypoventilation |
| Foot examination | Every 6-12 months | No new ulceration; stable deformity | Orthotic adjustment; podiatry referral; surgical consultation for progressive deformity |
| ECG / Echocardiogram | Annually if LMNA or other cardiac-associated CMT subtype | Normal conduction; normal LVEF | Cardiology referral; consider ICD for conduction disease; heart failure management |
| Pain assessment (NRS, DN4) | Every visit | Adequate pain control (NRS <4) | Adjust analgesic regimen; add or switch neuropathic pain agents |
| Fall risk assessment | Every visit | No falls or near-falls | PT reassessment; environmental modifications; assistive device upgrade |
| Genetic counseling follow-up | At diagnosis; pre-conception; at family request | Informed decision-making | Referral to genetics; update testing with new gene discoveries |
| 10-meter walk test / 6-minute walk test | Every 6-12 months | Stable or minimally declining | Adjust rehabilitation; adaptive equipment; consider clinical trial |

---

## 7. DISPOSITION

| Setting | Criteria | Follow-up |
|---------|----------|-----------|
| ED discharge | HNPP with acute compression neuropathy and stable neurological exam; known CMT with non-neurological chief complaint | Neuromuscular neurology follow-up within 2-4 weeks; provide neurotoxic medication avoidance list |
| Admission | Severe respiratory compromise (FVC <50% or declining); perioperative monitoring for complex surgeries; acute severe worsening (consider superimposed GBS/CIDP) | Neuromuscular and pulmonary co-management; daily FVC monitoring if respiratory |
| Outpatient neuromuscular clinic | All newly diagnosed or suspected CMT; established CMT for longitudinal monitoring | Every 6-12 months with neuromuscular specialist; coordinate with genetics, PT/OT, orthotics, orthopedics |
| Genetic counseling | All confirmed CMT; suspected hereditary neuropathy; family members requesting predictive testing | At diagnosis; pre-conception; update with new family members or testing advances |
| Rehabilitation services | All CMT patients benefit from PT/OT; orthotics | Ongoing; reassess every 6-12 months; intensify after surgical procedures |
| Palliative care | Severe CMT with significant functional impairment, chronic pain, respiratory insufficiency | Co-management; symptom-directed care; psychosocial support |

---

## 8. EVIDENCE & REFERENCES

| # | Citation | Key Finding | Link |
|---|----------|-------------|------|
| 1 | Pareyson D, Marchesi C. Diagnosis, natural history, and management of Charcot-Marie-Tooth disease. Lancet Neurol. 2009;8(7):654-667. | Comprehensive review of CMT classification, diagnosis, and management | [PubMed](https://pubmed.ncbi.nlm.nih.gov/19539236/) |
| 2 | Shy ME, et al. CMT1 neuropathies: diagnosis and management. Neurology. 2005;64(12):2220-2226. | AAN practice parameter for CMT1 diagnosis and management; genetic testing algorithm | [PubMed](https://pubmed.ncbi.nlm.nih.gov/15668420/) |
| 3 | Reilly MM, Murphy SM, Laurá M. Charcot-Marie-Tooth disease. J Peripher Nerv Syst. 2011;16(1):1-14. | Updated review of CMT genetics, phenotypes, and emerging therapies | [PubMed](https://pubmed.ncbi.nlm.nih.gov/21504497/) |
| 4 | Pareyson D, et al. Ascorbic acid in Charcot-Marie-Tooth disease type 1A (CMT-TRIAAL and CMT-TRAUK): a double-blind randomised trial. Lancet Neurol. 2011;10(4):320-328. | High-dose ascorbic acid showed NO benefit in CMT1A; large multicenter RCT | [PubMed](https://pubmed.ncbi.nlm.nih.gov/21393063/) |
| 5 | Attarian S, et al. An exploratory randomised double-blind and placebo-controlled phase 2 study of a combination of baclofen, naltrexone and sorbitol (PXT3003) in patients with Charcot-Marie-Tooth disease type 1A. Orphanet J Rare Dis. 2014;9:199. | PXT3003 showed dose-dependent improvement in ONLS score in CMT1A; phase 3 trial ongoing | [PubMed](https://pubmed.ncbi.nlm.nih.gov/25519680/) |
| 6 | Corrado B, et al. Evidence-based practice in rehabilitation of Charcot-Marie-Tooth disease: a systematic review. J Exerc Rehabil. 2019;15(4):467-477. | Moderate exercise is safe and beneficial in CMT; avoid high-intensity eccentric exercise; AFOs improve gait | [PubMed](https://pubmed.ncbi.nlm.nih.gov/31523667/) |
| 7 | Weimer LH, Podwall D. Medication-induced exacerbation of neuropathy in Charcot-Marie-Tooth disease. J Neurol Sci. 2006;242(1-2):47-54. | Comprehensive review of neurotoxic medications in CMT; vincristine is highest risk; provides risk categorization | [PubMed](https://pubmed.ncbi.nlm.nih.gov/16386274/) |
| 8 | Murphy SM, et al. Reliability of the CMT neuropathy score (second version) in Charcot-Marie-Tooth disease. J Peripher Nerv Syst. 2011;16(3):191-198. | CMTNSv2 is reliable outcome measure for CMT clinical trials and longitudinal monitoring | [PubMed](https://pubmed.ncbi.nlm.nih.gov/22003934/) |
| 9 | Padua L, et al. Natural history of Charcot-Marie-Tooth 2: 2-year follow-up of muscle strength, walking ability and quality of life. Neurol Sci. 2010;31(2):175-178. | CMT2 shows slower progression than CMT1 in longitudinal follow-up; CMTNS useful for monitoring | [PubMed](https://pubmed.ncbi.nlm.nih.gov/19924387/) |
| 10 | Mannil M, et al. Nerve ultrasound in hereditary motor and sensory neuropathies. Eur J Neurol. 2014;21(3):400-407. | Nerve ultrasound shows diffuse enlargement in CMT1A; distinguishes from CIDP (patchy enlargement) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/23834542/) |

---

## NOTES

- **Vincristine is ABSOLUTELY CONTRAINDICATED** in all CMT patients and carriers — can cause fatal neurotoxicity even at standard doses; document prominently in allergy/alert list
- CMT is the most common inherited neuropathy (~1:2,500 prevalence); CMT1A (PMP22 duplication) accounts for ~60% of all CMT
- Genetic testing strategy: start with PMP22 duplication/deletion (covers CMT1A and HNPP); if negative, test GJB1 (CMTX1), then MPZ (CMT1B); if all negative, proceed to multigene NGS panel
- HNPP (PMP22 deletion) presents with episodic painless pressure palsies — consider in patients with recurrent carpal tunnel, peroneal palsy, or ulnar neuropathy
- CMTX1 (GJB1): intermediate NCV in males; females may be asymptomatic or mildly affected; transient CNS symptoms (white matter lesions on MRI) can occur with metabolic stress or high altitude
- No disease-modifying therapy currently approved for any CMT subtype — management is supportive (orthotics, rehabilitation, pain management, neurotoxic medication avoidance, surgical correction of deformity)
- Anesthesia considerations: avoid succinylcholine in patients with significant muscle wasting (hyperkalemia risk); cautious use of neuromuscular blocking agents; document CMT in preoperative evaluation
- CMT1A progression is typically slow (1-2 points per year on CMTNS); most patients maintain ambulation; ~10% require wheelchair by age 50
- Distinguish CMT from treatable mimics: CIDP (responds to IVIg/steroids/PLEX), anti-MAG neuropathy (responds to rituximab), Refsum disease (dietary phytanic acid restriction)

---

## CHANGE LOG

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-11 | Initial draft — Hereditary Neuropathy / CMT evaluation and management plan |
