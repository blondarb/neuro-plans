---
title: "Botulism"
description: "Clinical decision support for botulism diagnosis and management"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - neuromuscular
  - toxin
  - paralysis
  - respiratory failure
  - infectious
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Botulism

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Validated per checker pipeline

---

**DIAGNOSIS:** Botulism

**ICD-10:** A05.1 (Botulism food poisoning — foodborne botulism), T48.1X1A (Poisoning by skeletal muscle relaxants, accidental — iatrogenic botulism), A48.51 (Infant botulism), A48.52 (Wound botulism), A48.59 (Other specified botulism — adult intestinal colonization, inhalational)

**CPT CODES:** 95907-95913 (nerve conduction studies), 95886 (needle EMG), 95937 (repetitive nerve stimulation), 87900 (bacterial toxin assay — mouse bioassay, sent via public health), 80053 (CMP), 85025 (CBC), 71046 (chest X-ray), 93000 (ECG), 70553 (MRI brain), 72156 (MRI spine), 94010 (spirometry/PFTs), 94726 (FVC), 99291-99292 (critical care E/M), 31500 (intubation)

**SYNONYMS:** Botulism, botulinum toxin poisoning, Clostridium botulinum poisoning, food poisoning botulism, foodborne botulism, wound botulism, infant botulism, iatrogenic botulism, descending paralysis, botulinum intoxication, sausage poisoning, botulism food poisoning, adult intestinal toxemia botulism, inhalational botulism

**SCOPE:** Diagnosis and management of all forms of botulism: foodborne (toxin ingestion), wound (toxin produced in infected wound), iatrogenic (therapeutic botulinum toxin overdose), infant botulism (intestinal colonization in infants), and adult intestinal colonization. Covers acute recognition of descending flaccid paralysis, respiratory monitoring (NIF/FVC), antitoxin administration (heptavalent equine antitoxin via CDC), electrophysiologic diagnosis, differentiation from GBS/MG/stroke, and supportive ICU care. Excludes cosmetic botulinum toxin use without adverse effect and bioterrorism-specific protocols (notify public health).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; infection screen; wound botulism may show leukocytosis | Normal; leukocytosis suggests wound infection |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolyte abnormalities; renal/hepatic function; baseline for prolonged ICU course | Normal |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia worsens neuromuscular weakness; can compound paralysis | >1.8 mg/dL |
| Phosphorus (CPT 84100) | STAT | ROUTINE | ROUTINE | STAT | Hypophosphatemia can worsen respiratory muscle weakness | >2.5 mg/dL |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Critical illness hyperglycemia management; autonomic dysfunction | Normal |
| Arterial blood gas (ABG) (CPT 82803) | STAT | STAT | - | STAT | Respiratory failure assessment; early CO2 retention precedes hypoxia | Normal pH, pCO2 <45 mmHg; rising pCO2 indicates impending respiratory failure |
| PT/INR (CPT 85610), aPTT (CPT 85730) | STAT | ROUTINE | - | STAT | Coagulation status before procedures; wound botulism may need surgical debridement | Normal |
| Blood cultures (aerobic/anaerobic) (CPT 87040) | STAT | ROUTINE | - | STAT | Wound botulism — rule out secondary bacteremia; exclude sepsis | No growth |
| Urinalysis (CPT 81003) | STAT | ROUTINE | ROUTINE | STAT | Baseline; UTI as complication in prolonged hospitalization | Normal |
| Pregnancy test (beta-hCG) | STAT | STAT | ROUTINE | STAT | Antitoxin is equine-derived — pregnancy category C; imaging considerations | Document result |
| Lactate (CPT 83605) | STAT | STAT | - | STAT | Assess tissue perfusion; distinguish from septic shock | <2.0 mmol/L |
| Type and screen (CPT 86900) | STAT | ROUTINE | - | STAT | Potential need for surgical intervention (wound botulism); ICU procedures | On file |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Serum botulinum toxin assay (mouse bioassay) (CPT 87900) | STAT | STAT | - | STAT | Definitive diagnostic test; contact CDC/state health department for testing; sensitivity 33-44% in serum | Positive confirms diagnosis (negative does NOT exclude) |
| Stool botulinum toxin assay and culture | STAT | STAT | - | STAT | Higher sensitivity than serum (60%+ in foodborne); also identifies colonization (infant, adult intestinal) | Positive toxin or culture of C. botulinum |
| Wound culture (anaerobic) | STAT | STAT | - | STAT | Wound botulism — culture for C. botulinum; send tissue/exudate for anaerobic culture and toxin assay | C. botulinum isolation |
| Suspected food sample (for toxin testing) | STAT | STAT | - | - | Epidemiologic confirmation; send to state public health lab via CDC coordination | Toxin identified in food |
| Serum for toxin type identification (A-G) | - | ROUTINE | - | ROUTINE | Identifies toxin serotype to guide antitoxin selection; types A, B, E most common in humans | Type identified |
| ESR (CPT 85652) / CRP (CPT 86140) | URGENT | ROUTINE | ROUTINE | ROUTINE | Inflammatory markers; elevated in wound botulism | Normal in foodborne; elevated in wound botulism |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Hypothyroidism can contribute to weakness (differential) | Normal |
| AChR antibody panel (binding, blocking, modulating) | - | ROUTINE | ROUTINE | - | Exclude myasthenia gravis (key differential) | Negative |
| Anti-MuSK antibody | - | ROUTINE | ROUTINE | - | Exclude MuSK-MG (bulbar-predominant MG mimic) | Negative |
| Creatine kinase (CK) (CPT 82550) | STAT | ROUTINE | ROUTINE | STAT | Elevated in some neuromuscular conditions; usually normal in botulism; rhabdomyolysis from prolonged immobility | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-ganglioside antibodies (GM1, GD1a, GQ1b) | - | EXT | EXT | - | Exclude GBS variants if diagnostic uncertainty persists | Negative |
| Edrophonium (Tensilon) test | - | EXT | EXT | - | Differentiates from MG (positive in MG, negative in botulism); rarely performed now | No improvement (negative) in botulism |
| Heavy metals (lead, arsenic, thallium) | - | EXT | EXT | - | Toxic neuropathy differential; environmental exposure | Normal |
| Tick paralysis assessment (physical exam) | STAT | STAT | - | STAT | Ascending paralysis mimic; search skin/scalp for embedded tick | No tick found |
| Organophosphate/carbamate level (cholinesterase) | - | EXT | - | EXT | Cholinergic crisis differential (excess secretions + weakness); toxicology screen | Normal cholinesterase levels |
| CSF analysis (LP) — if diagnostic uncertainty | - | EXT | EXT | - | CSF normal in botulism; elevated protein with normal cells suggests GBS; pleocytosis suggests infection | Normal in botulism (protein normal, WBC normal) |
| Porphyrins (urine ALA, PBG) | - | EXT | EXT | - | Acute intermittent porphyria — motor neuropathy + autonomic dysfunction mimic | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Nerve conduction studies (NCS) (CPT 95907-95913) / EMG (CPT 95886) with repetitive nerve stimulation (RNS) (CPT 95937) | - | URGENT | ROUTINE | URGENT | As soon as available (ideally within 24-48h); diagnostic cornerstone | Reduced CMAP amplitudes; normal sensory nerve action potentials (SNAPs); INCREMENTAL response (facilitation) at high-rate (20-50 Hz) repetitive stimulation (post-exercise facilitation); normal or mildly prolonged distal latencies; brief-duration, small-amplitude motor unit potentials (BSAPs) on needle EMG; fibrillation potentials in severe cases | None significant |
| Chest X-ray (CPT 71046) | STAT | ROUTINE | - | STAT | On admission | Aspiration pneumonia; atelectasis; baseline for ventilator management; mediastinal mass (differential) | None significant |
| ECG (12-lead) (CPT 93000) | STAT | ROUTINE | - | STAT | On admission and PRN | Sinus tachycardia; conduction abnormalities; autonomic effects on cardiac rhythm | None |
| CT head without contrast (CPT 70450) | URGENT | ROUTINE | - | URGENT | On admission if stroke in differential | Normal (excludes stroke, mass lesion) | Contrast allergy (if contrast used) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) | - | ROUTINE | ROUTINE | ROUTINE | If brainstem pathology suspected | Normal in botulism; excludes brainstem stroke, demyelination, mass | Pacemaker, metallic implants |
| MRI spine with and without contrast (CPT 72156) | - | ROUTINE | ROUTINE | - | If myelopathy in differential | Normal in botulism; excludes spinal cord compression | Same as MRI |
| CT chest with contrast (CPT 71260) | - | EXT | - | EXT | If thymoma suspected (MG differential) or pulmonary complication | No thymoma; assess for aspiration pneumonia | Contrast allergy, renal impairment |
| CT abdomen/pelvis (wound botulism with IVDU) | - | EXT | - | EXT | If deep abscess suspected as source of wound botulism | Abscess identification for surgical drainage | Contrast allergy, renal impairment |
| Repeat NCS/EMG | - | ROUTINE | ROUTINE | - | At 1-2 weeks if initial study non-diagnostic or to assess recovery | Evolution of findings; improving CMAPs indicate recovery | Same as initial |
| Echocardiogram (CPT 93306) | - | EXT | - | ROUTINE | If hemodynamic instability or autonomic dysfunction | Cardiac function assessment | None significant |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Single-fiber EMG (CPT 95872) | - | EXT | EXT | - | If standard EMG non-diagnostic | Increased jitter and blocking (present in botulism but non-specific — also seen in MG, LEMS) | Anticoagulation (relative) |
| Pulmonary function testing (formal) (CPT 94010) | - | ROUTINE | ROUTINE | - | If borderline respiratory function during recovery | Quantify restrictive defect; guide weaning | Unable to cooperate |

### LUMBAR PUNCTURE

**Indication:** NOT routinely indicated in botulism. Perform only if GBS, meningitis, or other CNS infection is in the differential and cannot be excluded clinically. CSF is NORMAL in botulism.

**Timing:** URGENT only if diagnostic uncertainty — particularly if ascending weakness or CSF pleocytosis/protein elevation would change diagnosis

**Volume Required:** 10-15 mL (standard diagnostic)

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | URGENT | ROUTINE | - | Rule out elevated ICP | 10-20 cm H2O (normal in botulism) |
| Cell count (tubes 1 and 4) (CPT 89051) | URGENT | ROUTINE | - | Normal WBC distinguishes from GBS (albuminocytologic dissociation) and meningitis | WBC <5 cells/uL (NORMAL in botulism) |
| Protein (CPT 84157) | URGENT | ROUTINE | - | Normal in botulism; elevated in GBS | NORMAL (<45 mg/dL) — elevated protein favors GBS |
| Glucose with serum glucose (CPT 82945) | URGENT | ROUTINE | - | Normal in botulism; low in bacterial meningitis | Normal (>60% serum) |
| Gram stain and culture | URGENT | ROUTINE | - | Exclude bacterial meningitis | No organisms |

**Special Handling:** Standard processing. The KEY finding is a NORMAL CSF, which helps EXCLUDE GBS (where protein is typically elevated) and meningitis (where pleocytosis is present).

**Contraindications:** Elevated ICP without imaging (CT first), coagulopathy (INR >1.5, platelets <50K), skin infection at LP site. Anticoagulation should be held.

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Heptavalent botulinum antitoxin (HBAT) (equine-derived, serotypes A-G) — obtained from CDC | IV | All forms of botulism (foodborne, wound, adult intestinal colonization, inhalational); administer as early as possible — antitoxin neutralizes circulating toxin but does NOT reverse already-bound toxin | 1 vial :: IV :: :: 1 vial (containing equine-derived antibodies to types A-G) IV; dilute 1:10 in 0.9% NS; infuse slowly over 15-30 min initially, increase rate per CDC protocol; contact CDC Emergency Operations Center 770-488-7100 (24/7) to obtain antitoxin; administer as soon as clinical suspicion is high — do NOT wait for lab confirmation | History of equine protein hypersensitivity (perform skin test first per CDC protocol); serum sickness risk 5-10% (monitor for 10-21 days post-infusion) | Skin test before infusion if history of atopy or equine exposure; monitor VS q5min during infusion and q15min x 4h post; observe for anaphylaxis (epinephrine at bedside); delayed serum sickness (fever, rash, arthralgias at 10-21 days) | STAT | STAT | - | STAT |
| BabyBIG (botulism immune globulin intravenous, human) | IV | Infant botulism ONLY (age <1 year); FDA-approved for infant botulism types A and B | 50 mg/kg :: IV :: :: 50 mg/kg (1 mL/kg) IV single dose; infuse at 0.5 mL/kg/h initially, increase to 1.0 mL/kg/h if tolerated; obtain from California Infant Botulism Treatment and Prevention Program (IBTPP) at 510-231-7600 (24/7) | IgA deficiency; prior severe reaction to human immunoglobulin | Vital signs q15min during infusion; watch for anaphylaxis; renal function | - | STAT | - | STAT |
| Intubation and mechanical ventilation | - | Respiratory failure — single most important cause of death in botulism | N/A :: - :: :: Indications: FVC <15-20 mL/kg, NIF weaker than -30 cmH2O, >30% decline in FVC from baseline, rising pCO2, clinical respiratory distress, inability to protect airway due to bulbar weakness. Use non-depolarizing agents (rocuronium preferred). AVOID succinylcholine (risk of exaggerated response in denervated muscle). Anticipate PROLONGED ventilation (weeks to months) | N/A (life-saving) | Ventilator settings per ICU protocol; daily assessment; plan for tracheostomy if ventilation expected >14 days | STAT | STAT | - | STAT |
| Wound debridement and drainage (wound botulism) | Surgical | Wound botulism — remove source of ongoing toxin production; perform AFTER antitoxin administration to avoid releasing more toxin into circulation | N/A :: Surgical :: :: Thorough surgical debridement of infected wound; drain abscess if present; obtain tissue for anaerobic culture; perform AFTER antitoxin has been given | Hemodynamic instability (stabilize first) | Wound site; CBC; signs of secondary infection | - | STAT | - | STAT |
| Metronidazole (wound botulism) | IV | Wound botulism — eradicate C. botulinum from wound; adjunct to debridement | 500 mg :: IV :: :: 500 mg IV q8h x 10-14 days; alternative to penicillin (avoids aminoglycoside interaction concern) | Severe hepatic impairment; disulfiram-like reaction with alcohol | LFTs; neuropathy (prolonged use); seizures (rare) | - | STAT | - | STAT |
| Penicillin G (wound botulism — alternative) | IV | Wound botulism — alternative to metronidazole for C. botulinum eradication | 3 million units :: IV :: :: 3 million units IV q4h x 10-14 days | Penicillin allergy; AVOID aminoglycosides concurrently (potentiate neuromuscular blockade) | Allergic reaction; renal function | - | STAT | - | STAT |
| DVT prophylaxis: Enoxaparin | SC | Immobilized patients at high risk of VTE | 40 mg :: SC :: :: 40 mg SC daily; start on admission | Active bleeding, platelets <50K, CrCl <30 (use UFH) | Platelets q3 days; anti-Xa if renal impairment | - | ROUTINE | - | ROUTINE |
| DVT prophylaxis: Heparin SC (alternative) | SC | VTE prophylaxis if enoxaparin contraindicated | 5000 units :: SC :: :: 5000 units SC q8-12h | Active bleeding, HIT | Platelets q3 days | - | ROUTINE | - | ROUTINE |
| Pneumatic compression devices | - | All immobilized patients | N/A :: - :: :: Apply bilaterally on admission; continue until ambulatory | Acute DVT, severe PVD | Skin checks daily | STAT | STAT | - | STAT |
| IV fluid resuscitation (0.9% NS) | IV | Dehydration from GI prodrome (foodborne botulism — nausea, vomiting, diarrhea) | 20 mL/kg :: IV :: :: 20 mL/kg IV bolus, then maintenance; target euvolemia | Fluid overload, CHF | I/O, BMP, volume status | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Atropine | IV | Bradycardia from autonomic dysfunction; excessive secretions | 0.5-1 mg :: IV :: :: 0.5-1 mg IV PRN for symptomatic bradycardia; may repeat q3-5 min; max 3 mg | Tachycardia, angle-closure glaucoma | HR, rhythm; urinary retention | STAT | STAT | - | STAT |
| Glycopyrrolate | IV/PO | Excessive oral secretions (antisialagogue); preferred over atropine for secretion management | 0.2 mg :: IV :: :: 0.2 mg IV q4-6h PRN; or 1-2 mg PO TID | Ileus, urinary retention, angle-closure glaucoma | Secretion volume; HR; bowel function | - | ROUTINE | - | ROUTINE |
| Acetaminophen | PO/IV | Pain, headache, fever | 650-1000 mg :: PO :: :: 650-1000 mg PO/IV q6h; max 4g/day (2g if hepatic impairment) | Severe liver disease | LFTs if prolonged | STAT | ROUTINE | ROUTINE | STAT |
| Metoclopramide | IV | Gastroparesis, nausea, ileus (autonomic dysfunction common) | 10 mg :: IV :: :: 10 mg IV q6h PRN; max 40 mg/day; limit to <12 weeks | Seizure history, Parkinson disease, GI obstruction | Tardive dyskinesia with prolonged use | - | ROUTINE | - | ROUTINE |
| Ondansetron | IV | Nausea and vomiting (foodborne botulism GI symptoms) | 4 mg :: IV :: :: 4 mg IV q6-8h PRN | QT prolongation, severe hepatic impairment | ECG if QT concern | STAT | ROUTINE | - | ROUTINE |
| Docusate sodium | PO | Constipation (immobility + autonomic dysfunction) | 100 mg :: PO :: :: 100 mg PO BID | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | ROUTINE |
| Senna | PO | Constipation | 8.6-17.2 mg :: PO :: :: 8.6-17.2 mg PO qHS | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | - |
| Polyethylene glycol (MiraLAX) | PO | Constipation (if docusate insufficient) | 17 g :: PO :: :: 17 g PO daily in 8 oz water | GI obstruction | Bowel function | - | ROUTINE | ROUTINE | - |
| Artificial tears (methylcellulose) | Ophthalmic | Dry eyes from impaired blinking (CN VII involvement, reduced lacrimation) | 1-2 drops :: Ophthalmic :: :: 1-2 drops each eye q2-4h while awake; lubricating ointment at night | None significant | Corneal integrity; ophthalmology if corneal exposure | - | ROUTINE | ROUTINE | ROUTINE |
| Melatonin | PO | Insomnia, ICU delirium prevention | 3-5 mg :: PO :: :: 3-5 mg PO qHS | None significant | Sleep quality | - | ROUTINE | - | ROUTINE |
| Lorazepam | IV | Anxiety, agitation in intubated patient | 0.5-1 mg :: IV :: :: 0.5-1 mg IV q6-8h PRN; use with caution — may worsen hypotonia | Respiratory depression (extreme caution if not intubated) | RR, sedation scale; avoid in non-intubated patients | - | URGENT | - | URGENT |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Guanidine hydrochloride | PO | Historical agent to enhance acetylcholine release at NMJ; limited efficacy; NOT standard of care; may provide modest improvement in chronic phase | 15-35 mg/kg :: PO :: :: 15-35 mg/kg/day divided TID-QID; start low and titrate; limited evidence for benefit | Bone marrow suppression, renal impairment | CBC, BMP weekly; bone marrow toxicity (aplastic anemia reported) | - | EXT | EXT | EXT |
| 4-Aminopyridine (dalfampridine) | PO | Potassium channel blocker to enhance neuromuscular transmission; off-label, limited evidence; may improve strength in recovery phase | 10 mg :: PO :: :: 10 mg PO BID (extended-release); off-label use | Seizure history (lowers threshold), renal impairment (CrCl <50) | Seizures; renal function | - | EXT | EXT | - |
| Tracheostomy | Surgical | Prolonged mechanical ventilation (>14 days expected — common in botulism) | N/A :: Surgical :: :: Perform when ventilation anticipated >14 days; improves patient comfort, oral hygiene, weaning potential | Coagulopathy (correct first) | Stoma site; decannulation readiness in recovery | - | ROUTINE | - | ROUTINE |
| Percutaneous gastrostomy (PEG) | Surgical | Prolonged inability to swallow safely; enteral nutrition access | N/A :: Surgical :: :: Place when dysphagia expected to persist >2-3 weeks | Coagulopathy, abdominal pathology | Tube site; feeding tolerance | - | ROUTINE | - | ROUTINE |

### 3D. Recovery/Rehabilitation Therapies

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Physical therapy (PT) (CPT 97110-97542) | - | All botulism patients; early passive ROM to prevent contractures; progressive strengthening during recovery | N/A :: - :: :: Daily passive ROM while paralyzed; active-assisted exercises as strength returns; progressive strengthening and gait training in recovery | Hemodynamic instability | Functional status; fall risk; fatigue | - | ROUTINE | ROUTINE | ROUTINE |
| Occupational therapy (OT) | - | Upper extremity function, ADLs, adaptive equipment | N/A :: - :: :: Daily OT for fine motor recovery, ADL training, adaptive equipment | Hemodynamic instability | Functional independence | - | ROUTINE | ROUTINE | ROUTINE |
| Speech-language pathology (SLP) | - | Dysphagia evaluation and treatment; aspiration prevention; communication strategies if intubated/trached | N/A :: - :: :: Bedside swallow evaluation; instrumental assessment (FEES or MBS) before oral intake; speech/communication strategies | None | Aspiration risk; swallow function | - | URGENT | ROUTINE | URGENT |

**CRITICAL MEDICATION WARNINGS:**

- **AVOID aminoglycosides** (gentamicin, tobramycin, amikacin) — potentiate neuromuscular blockade and worsen paralysis
- **AVOID magnesium sulfate** at high doses — potentiates neuromuscular blockade
- **AVOID succinylcholine** — risk of exaggerated response; use rocuronium if paralytic needed
- **AVOID fluoroquinolones** — potential neuromuscular blockade potentiation
- **AVOID neuromuscular blocking agents** unless absolutely necessary for intubation
- **DO NOT use antibiotics for foodborne botulism** (organism is in gut only; lysis could release more toxin — applies to infant botulism; foodborne is pre-formed toxin)
- **Infant botulism: AVOID antibiotics** that lyse C. botulinum in gut (aminoglycosides especially contraindicated) — use BabyBIG, not HBAT

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consultation — all suspected botulism; diagnostic confirmation; EMG/NCS interpretation; differentiation from GBS, MG, stroke | STAT | STAT | - | STAT |
| Critical care / Pulmonology — respiratory monitoring and ventilator management; all patients with bulbar or respiratory weakness | STAT | STAT | - | STAT |
| Infectious disease — confirm diagnosis; guide antibiotic therapy for wound botulism; coordinate public health notification | URGENT | URGENT | - | URGENT |
| Public health / CDC notification — MANDATORY: botulism is a nationally notifiable disease; contact state health department AND CDC Emergency Operations Center (770-488-7100) to obtain antitoxin and for epidemiologic investigation | STAT | STAT | - | STAT |
| Toxicology / Poison control — if foodborne: identify implicated food; coordinate with public health; differential diagnosis assistance | URGENT | ROUTINE | - | URGENT |
| Surgery (wound botulism) — wound debridement and drainage for wound botulism; abscess management in IVDU patients | - | STAT | - | STAT |
| Speech-language pathology (SLP) — dysphagia evaluation; aspiration prevention; communication strategies | - | URGENT | ROUTINE | URGENT |
| Physical therapy (PT) — early passive ROM; progressive mobilization; gait training in recovery | - | URGENT | ROUTINE | URGENT |
| Occupational therapy (OT) — upper extremity function; ADLs; adaptive equipment | - | URGENT | ROUTINE | URGENT |
| Rehabilitation medicine (physiatry) — rehabilitation planning; disposition (inpatient rehab vs SNF vs home) | - | ROUTINE | ROUTINE | - |
| Respiratory therapy — bedside spirometry (FVC, NIF); pulmonary toilet; ventilator weaning protocols | - | STAT | - | STAT |
| Ophthalmology — if persistent diplopia, ptosis, or corneal exposure from impaired blinking | - | ROUTINE | ROUTINE | - |
| Nutrition / Dietitian — enteral/parenteral feeding plan if prolonged dysphagia; caloric needs during recovery | - | ROUTINE | - | ROUTINE |
| Social work — discharge planning; family support; financial resources for prolonged hospitalization | - | ROUTINE | ROUTINE | - |
| Psychology / Psychiatry — anxiety, depression, PTSD (common with prolonged ICU stay and ventilator dependence) | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED / Call 911 if: increasing difficulty breathing, new swallowing difficulty, worsening double vision, progressive weakness, inability to hold up head, chest pain, or lightheadedness | STAT | STAT | ROUTINE |
| Botulism is a serious but treatable condition; early antitoxin administration improves outcomes | STAT | ROUTINE | ROUTINE |
| Recovery is typically slow (weeks to months); full recovery is possible but may take up to a year | - | ROUTINE | ROUTINE |
| Do NOT drive until vision (diplopia), strength, and reflexes have fully recovered and cleared by neurologist | - | ROUTINE | ROUTINE |
| Comply with physical and occupational therapy exercises as prescribed | - | ROUTINE | ROUTINE |
| Report any new difficulty breathing, swallowing, or worsening weakness immediately | - | ROUTINE | ROUTINE |
| Foodborne botulism prevention: do not eat food from bulging or damaged cans; properly refrigerate foods; follow safe home canning practices (pressure canning for low-acid foods; boil home-canned foods for 10 min before eating) | - | ROUTINE | ROUTINE |
| Wound botulism (IVDU patients): avoid injection drug use; if continuing, use clean needles and do not skin-pop or muscle-pop; seek help for substance use disorder | - | ROUTINE | ROUTINE |
| Follow-up with neurology in 1-2 weeks after discharge; NCS/EMG may be repeated at 3-6 months to document recovery | - | ROUTINE | ROUTINE |
| Inform future healthcare providers about botulism history (anesthesia precautions — prolonged paralysis risk with certain agents) | - | ROUTINE | ROUTINE |
| Fall prevention: use assistive devices as recommended during recovery; remove tripping hazards at home | - | ROUTINE | ROUTINE |
| Monitor for signs of blood clots: leg swelling, redness, chest pain, shortness of breath | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Gradual return to activity as tolerated; avoid overexertion during recovery; fatigue is common for months | - | ROUTINE | ROUTINE |
| Safe food handling: proper canning techniques (pressure canning at 250F/121C for low-acid foods); refrigerate perishables; discard bulging, leaking, or damaged cans | - | ROUTINE | ROUTINE |
| Boil home-canned foods for 10 minutes before eating (destroys botulinum toxin) | - | ROUTINE | ROUTINE |
| Honey should NOT be given to infants <1 year (infant botulism risk from Clostridium spores) | - | ROUTINE | ROUTINE |
| Wound care: keep wounds clean; seek medical attention for infected wounds especially in IVDU patients | - | ROUTINE | ROUTINE |
| Substance use disorder treatment referral for IVDU patients with wound botulism | - | ROUTINE | ROUTINE |
| Balanced nutrition for neuromuscular recovery (adequate protein, B vitamins) | - | ROUTINE | ROUTINE |
| Mental health support (prolonged ICU stay, ventilator dependence, slow recovery cause significant psychological stress) | - | ROUTINE | ROUTINE |
| Adequate sleep (promotes neurologic recovery) | - | ROUTINE | ROUTINE |
| Smoking cessation (impairs tissue healing and neuromuscular recovery) | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Guillain-Barre syndrome (GBS) | ASCENDING paralysis (starts distally, moves proximally — opposite of botulism); sensory symptoms common; areflexia; CSF shows elevated protein with normal WBC (albuminocytologic dissociation); no pupil involvement; no GI prodrome typical of botulism | NCS/EMG (demyelinating or axonal pattern; NO incremental response); LP (elevated protein); anti-ganglioside antibodies |
| Myasthenia gravis (MG) | Fatigable weakness; fluctuating symptoms; ptosis and diplopia (similar to botulism); intact pupillary reflexes; no GI prodrome; chronic course | AChR/MuSK antibodies; repetitive nerve stimulation shows DECREMENTAL response at LOW-rate (2-3 Hz) stimulation (vs. incremental at high-rate in botulism); edrophonium test positive |
| Lambert-Eaton myasthenic syndrome (LEMS) | Proximal weakness; hyporeflexia with post-exercise facilitation; autonomic dysfunction (dry mouth); associated with SCLC; chronic onset | NCS shows incremental response at high-rate RNS (SIMILAR to botulism); VGCC antibodies positive; CT chest for malignancy |
| Brainstem stroke | Acute onset; focal neurologic deficits; cranial nerve findings may overlap; crossed findings (ipsilateral face, contralateral body); no GI prodrome; no descending pattern | MRI brain with DWI (acute infarct); CTA/MRA (vascular occlusion); normal NCS/EMG |
| Tick paralysis | Ascending paralysis similar to GBS; rapid onset; tick found on exam; rapid reversal after tick removal; no sensory loss; normal CSF | Physical exam (search for tick — scalp, hairline, skin folds); NCS may show reduced CMAPs; CSF normal |
| Organophosphate/nerve agent poisoning | Cholinergic crisis: SLUDGE symptoms (salivation, lacrimation, urination, defecation, GI distress, emesis); miosis; muscle fasciculations then weakness; bradycardia | Cholinesterase levels (depressed); atropine challenge (improves symptoms); toxicology screen |
| Diphtheria | Pharyngeal membrane; palatal weakness early; sensorimotor neuropathy develops weeks after infection; myocarditis | Throat culture; diphtheria toxin assay; clinical history; travel/vaccination history |
| Acute intermittent porphyria | Abdominal pain (prominent); psychiatric symptoms; autonomic dysfunction; motor-predominant neuropathy; dark urine | Urine ALA and PBG (elevated during attack); genetic testing |
| Poliomyelitis / West Nile virus | Asymmetric flaccid paralysis; fever; anterior horn cell pattern; CSF pleocytosis | CSF (elevated WBC); viral PCR; MRI (anterior horn signal change) |
| Myasthenic crisis | Similar bulbar and respiratory failure; known MG history typically; rapid deterioration | AChR antibodies; history of MG; decremental response on RNS |
| Eaton-Lambert crisis | Acute exacerbation of LEMS; proximal weakness; autonomic symptoms | VGCC antibodies; malignancy screening; high-rate RNS |
| Hypermagnesemia | Iatrogenic (MgSO4 infusion); weakness; hyporeflexia; respiratory depression | Serum magnesium level (markedly elevated) |
| Conversion disorder (FND) | Non-physiologic weakness pattern; Hoover sign; give-way weakness; may mimic any neurologic presentation | Normal NCS/EMG; normal labs; clinical exam features inconsistent with organic disease |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Forced Vital Capacity (FVC) | STAT | STAT | ROUTINE | STAT | q2-4h in ED/ICU; q4-6h on floor; q1h if declining | FVC >15-20 mL/kg (approx >1.0-1.5L for 75 kg adult) | FVC <15-20 mL/kg or declining >30% from baseline -> elective intubation; transfer to ICU |
| Negative Inspiratory Force (NIF/MIP) | STAT | STAT | ROUTINE | STAT | q2-4h with FVC | NIF more negative than -30 cmH2O (e.g., -40 is better than -20) | NIF weaker than -30 cmH2O -> prepare for intubation |
| Peak Cough Flow | - | ROUTINE | - | ROUTINE | q4-6h with FVC | >270 L/min (effective cough) | Airway clearance interventions; suction; assisted cough |
| Oxygen saturation (SpO2) | STAT | STAT | - | STAT | Continuous in ICU; q2-4h on floor | >=94% | LATE finding — do NOT rely on SpO2 alone; FVC and NIF are far more sensitive indicators of impending failure |
| Arterial blood gas (pCO2) | STAT | ROUTINE | - | STAT | q4-6h; more frequently if declining FVC | pCO2 <45 mmHg | Rising pCO2 indicates hypoventilation and impending respiratory failure — intubate |
| Blood pressure | STAT | STAT | - | STAT | q4h on floor; continuous in ICU | Stable; watch for hypotension (autonomic) | Hypotension: IV fluids, vasopressors if refractory; AVOID long-acting agents |
| Heart rate and rhythm (telemetry) | STAT | STAT | - | STAT | Continuous in ICU; telemetry on floor | HR 60-100; sinus rhythm | Bradycardia: atropine; tachycardia: volume, pain control; arrhythmia: per ACLS |
| Neurologic exam (cranial nerves, strength, reflexes) | STAT | STAT | ROUTINE | STAT | q4-8h; focus on pupillary response, ptosis, bulbar function, proximal then distal strength | Stable or improving; descending pattern is characteristic | Worsening (new cranial nerve palsies, progressing to limbs) -> reassess respiratory status STAT; ensure antitoxin given |
| Pupillary examination | STAT | STAT | ROUTINE | STAT | q4h | Reactive, symmetric pupils | Fixed, dilated pupils (mydriasis) suggest botulism (distinguishes from GBS/MG); document progression |
| Swallowing function | URGENT | STAT | ROUTINE | STAT | Daily assessment; formal SLP if bulbar symptoms | Safe oral intake | NPO if unsafe; NG tube or PEG for nutrition |
| Gag reflex and cough strength | STAT | STAT | ROUTINE | STAT | q4-6h | Present and strong | Absent gag -> NPO; aspiration precautions; suction at bedside |
| Bowel function | - | ROUTINE | ROUTINE | ROUTINE | Daily | Regular bowel movements | Ileus is common (autonomic dysfunction); bowel program; avoid opioids if possible |
| Bladder function | - | ROUTINE | ROUTINE | ROUTINE | I/O monitoring; post-void residual if needed | Adequate output; PVR <200 mL | Urinary retention (autonomic dysfunction) -> bladder scan; intermittent catheterization |
| Renal function (BUN, Cr) | - | ROUTINE | - | ROUTINE | Daily in acute phase; q48h when stable | Stable creatinine | Adjust medications; hydration |
| Wound inspection (wound botulism) | - | STAT | ROUTINE | STAT | BID wound checks post-debridement | Clean, healing wound; no signs of re-infection | Signs of infection -> repeat debridement; adjust antibiotics |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Extremely rare in acute botulism; only for VERY mild cases (minimal weakness, stable respiratory function, no bulbar symptoms); reliable outpatient follow-up; family/caregiver support; neurology follow-up within 1-2 weeks |
| Admit to ICU (MOST patients) | All suspected botulism should be admitted to ICU or monitored setting; respiratory monitoring (FVC/NIF) required; any bulbar weakness; any respiratory compromise; antitoxin administration and monitoring; autonomic instability |
| Admit to floor (monitored bed) | Mild cases after antitoxin with stable respiratory function (FVC >25 mL/kg and stable); no bulbar weakness; able to protect airway; continuous telemetry available; step-down from ICU when improving |
| Transfer to higher level of care | Need for ICU with neurology and critical care expertise; need for antitoxin (coordinate with CDC for transfer if antitoxin unavailable locally); ECMO capability if refractory respiratory failure |
| Inpatient rehabilitation | Significant residual motor deficits; able to participate in 3h/day therapy; medically stable; ventilator weaned or stable tracheostomy |
| Skilled nursing facility | Unable to tolerate intensive rehabilitation; requires ongoing nursing care; ventilator-dependent (long-term acute care facility — LTAC) |
| Long-term acute care (LTAC) | Prolonged ventilator dependence (common in botulism — weeks to months); requires weaning protocol; medically stable but not ready for rehab |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Heptavalent botulinum antitoxin (HBAT) — early administration reduces mortality and duration of illness | Class IIa, Level B | [Arnon et al. JAMA 2006](https://pubmed.ncbi.nlm.nih.gov/16507803/); [Tacket et al. Am J Med 1984](https://pubmed.ncbi.nlm.nih.gov/6702902/) |
| BabyBIG (human botulism immune globulin) for infant botulism — reduces hospitalization by 3+ weeks | Class I, Level A | [Arnon et al. N Engl J Med 2006](https://pubmed.ncbi.nlm.nih.gov/16467544/) |
| EMG/NCS with repetitive nerve stimulation — incremental response at high-rate stimulation diagnostic | Class IIa, Level B | [Cherington M. J Neurol Neurosurg Psychiatry 1982](https://pubmed.ncbi.nlm.nih.gov/6278099/); [Gutierrez et al. Muscle Nerve 2000](https://pubmed.ncbi.nlm.nih.gov/10918203/) |
| Mouse bioassay — gold standard for botulinum toxin detection; serum sensitivity ~33-44% | Class IIa, Level C | [CDC. MMWR Recomm Rep 1998](https://pubmed.ncbi.nlm.nih.gov/9639369/) |
| Respiratory monitoring (FVC/NIF) for intubation decisions in neuromuscular respiratory failure | Class I, Level B | [Lawn et al. Arch Neurol 2001](https://pubmed.ncbi.nlm.nih.gov/11405803/); [Wijdicks & Borel, Neurology 1998](https://pubmed.ncbi.nlm.nih.gov/9443451/) |
| Wound debridement AFTER antitoxin administration for wound botulism | Class IIa, Level C | [Werner et al. Clin Infect Dis 2000](https://pubmed.ncbi.nlm.nih.gov/10770748/); CDC guidelines |
| Avoid aminoglycosides — potentiate neuromuscular blockade in botulism | Class III (Harm), Level C | [Santos et al. Ann Intern Med 1981](https://pubmed.ncbi.nlm.nih.gov/6263133/) |
| Contact CDC Emergency Operations Center (770-488-7100) for antitoxin access | Class I, Level C | [CDC Botulism Treatment Guidelines](https://pubmed.ncbi.nlm.nih.gov/9639369/) |
| Botulism is a nationally notifiable disease — mandatory reporting | Class I, Level C | CDC nationally notifiable conditions; state public health law |
| Do not administer antibiotics in infant botulism (risk of toxin release from bacterial lysis) | Class III (Harm), Level C | [Arnon et al. N Engl J Med 2006](https://pubmed.ncbi.nlm.nih.gov/16467544/); IBTPP guidelines |
| Prolonged mechanical ventilation expected (median 58 days type A; 26 days type B) | Class IIa, Level B | [Wilcox et al. Chest 1990](https://pubmed.ncbi.nlm.nih.gov/2340814/) |
| DVT prophylaxis for immobilized patients | Class I, Level C | Standard of care for immobilized patients |
| Early rehabilitation improves functional outcomes | Class I, Level B | Standard of care in neuromuscular disease |
| Metronidazole preferred over aminoglycosides for wound botulism antibiotic therapy | Class IIa, Level C | Expert consensus; [Werner et al. Clin Infect Dis 2000](https://pubmed.ncbi.nlm.nih.gov/10770748/) |
| Succinylcholine avoidance in neuromuscular junction disorders | Class III (Harm), Level C | Risk of hyperkalemia and prolonged blockade |
| Antitoxin most effective when given within 24h of symptom onset; still beneficial up to 72h | Class IIa, Level B | [Tacket et al. Am J Med 1984](https://pubmed.ncbi.nlm.nih.gov/6702902/); retrospective data |

---

**APPENDIX A: BOTULISM TYPES AND CLINICAL FEATURES**

| Type | Source/Mechanism | Typical Onset | Key Features | Antitoxin |
|------|-----------------|---------------|--------------|-----------|
| Foodborne | Pre-formed toxin ingested in contaminated food (home-canned goods, fermented fish, honey-based products) | 12-36h (range 6h-10 days) | GI prodrome (N/V/D) -> cranial nerve palsies -> descending paralysis | HBAT (adults) |
| Wound | C. botulinum colonizes wound (IVDU — black tar heroin skin-popping); toxin produced in vivo | 4-14 days after wound contamination | NO GI prodrome; wound infection signs; fever; descending paralysis | HBAT + antibiotics + debridement |
| Infant | C. botulinum spores colonize infant gut (honey, soil, dust); toxin produced in vivo | Gradual (days) | Age <1 year; constipation, poor feeding, weak cry, floppy infant, descending weakness | BabyBIG (human-derived) |
| Iatrogenic | Therapeutic/cosmetic botulinum toxin (onabotulinumtoxinA, etc.) overdose or systemic spread | Hours to days post-injection | Local then systemic weakness; dose-related; history of recent injection | Supportive care; HBAT if systemic |
| Adult intestinal colonization | Rare; similar to infant botulism but in adults (GI surgery, altered flora, antimicrobial use) | Gradual | Similar to foodborne but without clear food source; prolonged course | HBAT |
| Inhalational | Aerosolized toxin (bioterrorism concern); not naturally occurring | 12-80h post-exposure | No GI prodrome; same descending paralysis pattern | HBAT |

**APPENDIX B: EMG/NCS FINDINGS IN BOTULISM vs. KEY DIFFERENTIALS**

| Parameter | Botulism | GBS (AIDP) | Myasthenia Gravis | Lambert-Eaton (LEMS) |
|-----------|----------|------------|-------------------|---------------------|
| CMAP amplitude | Reduced (especially type A) | Normal early; reduced in axonal variants | Normal | Reduced |
| SNAP amplitude | Normal | Reduced or absent | Normal | Normal |
| Distal latency | Normal | Prolonged (demyelinating) | Normal | Normal |
| Conduction velocity | Normal | Slow (demyelinating) | Normal | Normal |
| F-waves | Normal | Prolonged or absent | Normal | Normal |
| Low-rate RNS (2-3 Hz) | Decremental (mild) | Normal or decremental | Decremental (>10%) | Decremental |
| High-rate RNS (20-50 Hz) | INCREMENTAL (>100% facilitation) | No facilitation | No significant change | INCREMENTAL (>100%) |
| Post-exercise facilitation | Present | Absent | No improvement or worse | Present (marked) |
| Needle EMG | BSAPs; fibrillations in severe cases | Fibrillations if axonal; normal early | Normal or myopathic in severe | Normal or myopathic |

**APPENDIX C: CDC ANTITOXIN ACCESS PROTOCOL**

| Step | Action |
|------|--------|
| 1 | Clinical suspicion of botulism established (do NOT wait for lab confirmation) |
| 2 | Contact state/local health department IMMEDIATELY |
| 3 | Contact CDC Emergency Operations Center: **770-488-7100** (24/7) |
| 4 | CDC releases HBAT from nearest Strategic National Stockpile (SNS) location |
| 5 | Typical delivery time: 1-2 hours within continental US after CDC approval |
| 6 | Perform skin test for equine sensitivity BEFORE infusion (per CDC protocol included with antitoxin) |
| 7 | Administer antitoxin: dilute 1:10 in NS; slow IV infusion; epinephrine at bedside |
| 8 | Collect pre-treatment specimens (serum, stool, wound if applicable) for confirmatory testing |
| 9 | Monitor for anaphylaxis (acute) and serum sickness (10-21 days post-infusion) |

**APPENDIX D: RESPIRATORY MONITORING AND INTUBATION THRESHOLDS**

| Parameter | Threshold for Intubation | Notes |
|-----------|-------------------------|-------|
| FVC | <15-20 mL/kg | More aggressive threshold than GBS due to rapid progression |
| NIF (MIP) | Weaker than -30 cmH2O | Same threshold as GBS |
| FVC decline | >30% from baseline | Trend is critical — check frequently |
| pCO2 | Rising above 45-50 mmHg | Indicates hypoventilation; late sign |
| SpO2 | <94% | Very late sign — do NOT wait for desaturation |
| Clinical signs | Dyspnea, use of accessory muscles, paradoxical breathing, tachypnea >30, inability to count to 20, weak cough, inability to swallow secretions | Clinical judgment is essential |
| Special consideration | Botulism patients may require PROLONGED ventilation (type A median 58 days; type B median 26 days); plan for early tracheostomy | Discuss with patient/family early |

---

## CHANGE LOG

**v1.1 (February 2, 2026)**
- Validated per checker pipeline (v1.1)
- Standardized Section 4A (Referrals & Consults) to 5-column format (Recommendation | ED | HOSP | OPD | ICU); merged Indication content into Recommendation column
- Standardized all structured dosing fields to empty third field format (dose :: route :: :: full_instructions) across Sections 3A, 3B, 3C, 3D to match approved plan conventions
- Fixed intubation dosing field from erroneous "20 mL/kg" first field to "N/A" (intubation is a procedure, not a medication dose)
- Fixed pneumatic compression devices dosing field to use "N/A" first field (non-medication intervention)
- Updated OT contraindications from "Same as PT" to explicit "Hemodynamic instability" (removed cross-reference)

**v1.0 (February 2, 2026)**
- Initial template creation
- Comprehensive botulism management covering foodborne, wound, iatrogenic, infant, and adult intestinal colonization forms
- Structured dosing format for all medications
- CDC antitoxin access protocol included
- EMG/NCS differential table (botulism vs. GBS vs. MG vs. LEMS)
- Respiratory monitoring thresholds with botulism-specific considerations
- Complete differential diagnosis section with 13 alternative diagnoses
- Critical medication warnings (aminoglycosides, succinylcholine, antibiotics in infant botulism)
