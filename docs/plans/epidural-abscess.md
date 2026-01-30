---
title: "Spinal Epidural Abscess"
description: "Clinical decision support for spinal epidural abscess (sea) diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
---

# Spinal Epidural Abscess

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Spinal Epidural Abscess (SEA)

**ICD-10:** G06.1 (Intraspinal abscess and granuloma), M46.40 (Discitis, unspecified site), M46.46 (Discitis, lumbar region), M46.47 (Discitis, lumbosacral region), A41.9 (Sepsis, unspecified organism)

**SYNONYMS:** Spinal epidural abscess, SEA, epidural abscess, spinal abscess, vertebral osteomyelitis, discitis, spondylodiscitis, spinal infection, back pain with fever, paraspinal abscess

**SCOPE:** Emergency evaluation and management of spinal epidural abscess in adults. Covers the classic triad (back pain, fever, neurologic deficit), emergent MRI, surgical drainage vs. medical management decision-making, empiric and targeted antibiotic therapy, and neurologic monitoring. Includes associated vertebral osteomyelitis and discitis. Excludes brain abscess (separate template), subdural empyema, and post-operative wound infections (partially overlaps).

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Blood cultures (x2 sets, before antibiotics) | STAT | STAT | - | STAT | **CRITICAL: Positive in 60-70%**; identifies organism for targeted therapy; guides antibiotic duration; S. aureus most common (60-70%); draw from 2 separate sites | Positive → organism identification; S. aureus (MRSA vs. MSSA) most common; also Streptococci, gram-negatives, anaerobes |
| CBC with differential | STAT | STAT | ROUTINE | STAT | Leukocytosis (WBC >12,000 in 60-80%); left shift; bandemia; baseline for monitoring; thrombocytopenia may indicate DIC/sepsis | Leukocytosis (66%); normal WBC does NOT exclude SEA (20-40% have normal WBC); leukopenia concerning for overwhelming sepsis |
| CMP (BMP + LFTs) | STAT | STAT | ROUTINE | STAT | Renal function (antibiotic dosing, contrast); electrolytes; hepatic function; glucose (diabetes is major risk factor) | Normal or abnormal; elevated glucose → diabetes workup; renal dysfunction affects antibiotic choice |
| ESR (erythrocyte sedimentation rate) | STAT | STAT | ROUTINE | STAT | **Highly sensitive (>94%)**; ESR >20 mm/hr in nearly all cases of SEA; ESR >30-50 typical; useful for monitoring treatment response | ESR >20 mm/hr (sensitivity 94%); mean ESR is typically 50-80 mm/hr; if normal → SEA very unlikely |
| CRP (C-reactive protein) | STAT | STAT | ROUTINE | STAT | Elevated in >90% of SEA; more responsive to treatment changes than ESR; useful for monitoring | Elevated (typically >10 mg/dL); declines faster than ESR with successful treatment |
| Procalcitonin | STAT | STAT | - | STAT | More specific for bacterial infection than CRP; helps distinguish bacterial from non-infectious inflammation; prognostic | >0.5 ng/mL suggests bacterial infection; >2.0 ng/mL concerning for sepsis; useful in atypical presentations |
| Blood glucose / HbA1c | STAT | STAT | ROUTINE | STAT | **Diabetes is a major risk factor (30-50% of SEA patients)**; undiagnosed diabetes common; affects wound healing and immune function | Document diabetes status; HbA1c >6.5% = diabetes; glucose control target <180 mg/dL |
| PT/INR, aPTT | STAT | STAT | - | STAT | Coagulopathy from sepsis (DIC); surgical candidacy; baseline before anticoagulation decisions; epidural hematoma differential | Normal; prolonged → concern for DIC, liver dysfunction; affects surgical risk |
| Lactate | STAT | STAT | - | STAT | Sepsis assessment; tissue hypoperfusion; prognostic | <2 mmol/L (normal); >4 mmol/L = severe sepsis/septic shock requiring aggressive resuscitation |
| Type and screen | STAT | STAT | - | STAT | Surgical candidacy; blood product availability | On file |
| Urinalysis + urine culture | STAT | STAT | ROUTINE | STAT | Urinary source (UTI is common source of hematogenous spread, especially gram-negative SEA); concurrent UTI | Normal or pyuria/bacteriuria; if positive → potential primary source |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| HIV antibody/antigen | - | ROUTINE | ROUTINE | ROUTINE | Immunocompromised state; increases SEA risk; affects prognosis and opportunistic infection risk | Negative; if positive → CD4 count, viral load; consider opportunistic organisms |
| Hepatitis B/C serologies | - | ROUTINE | ROUTINE | - | IVDU population (risk factor for SEA); affects long-term antibiotic choice; liver function | Negative; if positive → affects drug selection, hepatotoxicity monitoring |
| Hemoglobin A1c | - | ROUTINE | ROUTINE | - | Undiagnosed or poorly controlled diabetes | <6.5% (normal); ≥6.5% = diabetes; 5.7-6.4% = prediabetes |
| D-dimer | STAT | ROUTINE | - | STAT | DIC screening; VTE risk (prolonged immobility + inflammation); not specific but elevated in SEA | Elevated (non-specific); very high levels → consider DIC |
| Fibrinogen | - | ROUTINE | - | STAT | DIC assessment; sepsis-associated coagulopathy | >150 mg/dL; low fibrinogen = DIC or consumption |
| Albumin / prealbumin | - | ROUTINE | ROUTINE | - | Nutritional status; wound healing; chronicity of illness; prognostic | >3.5 g/dL (albumin); low = poor nutrition, chronic illness |
| Repeat blood cultures (during treatment) | - | ROUTINE | ROUTINE | - | Document clearance of bacteremia; if persistently positive → evaluate for endocarditis, undrained collection, treatment failure | Negative by 48-72h of appropriate antibiotics; persistent positivity → echocardiogram, repeat imaging |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Surgical specimen culture (intraoperative) | - | STAT | - | - | **Gold standard for organism identification**; culture of abscess material at surgery; sensitivity higher than blood cultures; also send for Gram stain and histopathology | Organism identification; guides targeted antibiotic therapy |
| CT-guided aspiration/biopsy culture | - | URGENT | - | - | If non-operative management chosen; tissue diagnosis; culture for organism identification; distinguishes abscess from tumor/hematoma | Organism identification; Gram stain; histopathology (rule out tumor) |
| Acid-fast bacilli (AFB) smear and culture | - | EXT | EXT | - | TB spine (Pott's disease); endemic areas; immunocompromised; chronic presentation with vertebral destruction | Negative; positive → TB requires different treatment (anti-TB regimen; may not need surgery if no instability/neurologic deficit) |
| Fungal cultures | - | EXT | EXT | - | Immunocompromised; IVDU; indwelling catheters; endemic fungi (coccidioidomycosis, blastomycosis, histoplasmosis); chronic presentation | Negative; positive → prolonged antifungal therapy (6-12+ months) |
| Brucella serology / cultures | - | EXT | EXT | - | Endemic areas (Mediterranean, Middle East); unpasteurized dairy; occupational exposure (farmers, veterinarians); chronic back pain | Negative; positive → doxycycline + streptomycin/gentamicin or rifampin |
| 16S rRNA PCR (on tissue) | - | EXT | EXT | - | Culture-negative SEA; prior antibiotic exposure; fastidious organisms | Identifies organism even when cultures are negative; research/reference lab |
| Transthoracic echocardiogram (TTE) | - | ROUTINE | ROUTINE | STAT | **Infective endocarditis screen**; IE present in 10-15% of SEA patients with S. aureus bacteremia; affects antibiotic duration and management | Normal; vegetations → endocarditis diagnosis; changes antibiotic duration to 4-6 weeks minimum |
| Transesophageal echocardiogram (TEE) | - | URGENT | ROUTINE | URGENT | If TTE negative but high suspicion for endocarditis (S. aureus bacteremia, IVDU, prosthetic valve, persistent fever); TEE more sensitive than TTE | Normal; vegetations → endocarditis; TEE sensitivity 90-95% vs. TTE 65% |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI entire spine with and without contrast (gadolinium) | STAT | STAT | URGENT | STAT | **GOLD STANDARD — within 4 hours of ED presentation if neurologic deficit; within 24h if no deficit**; contrast essential for abscess characterization; image ENTIRE spine (multifocal in 15-20%) | Epidural collection with ring enhancement; T1 hypointense, T2 hyperintense; restricted diffusion (DWI bright, ADC dark within abscess); vertebral body involvement (osteomyelitis); disc involvement (discitis); cord compression; degree of canal compromise | MRI-incompatible implants; severe claustrophobia (sedate — do NOT delay); GFR <30 (gadolinium risk — but benefit outweighs risk in emergency) |
| Plain radiographs (spine) | STAT | STAT | - | STAT | Immediate while awaiting MRI; identifies vertebral body destruction, disc space narrowing, alignment abnormality; LOW sensitivity for early SEA | Disc space narrowing; vertebral body destruction (late finding — takes 2-4 weeks to appear); alignment; pathologic fracture | Pregnancy (shield) |
| CT spine without contrast | STAT | STAT | - | STAT | If MRI unavailable or contraindicated; inferior to MRI for soft tissue and epidural collection; shows bone destruction better than MRI | Bone destruction; disc space narrowing; paraspinal soft tissue mass; canal compromise; less sensitive than MRI for epidural abscess extent | Pregnancy (relative) |
| Chest X-ray | STAT | STAT | - | STAT | Primary pulmonary source (pneumonia); lung abscess; TB (apical infiltrate, cavitation); septic emboli | Primary infection source; pulmonary complications; TB features | Pregnancy (shield) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT chest/abdomen/pelvis with contrast | - | URGENT | ROUTINE | URGENT | Source identification if not obvious; look for primary infection (lung abscess, intra-abdominal abscess, psoas abscess); staging for concurrent infection | Primary source: lung abscess, intra-abdominal abscess, psoas abscess (contiguous spread), renal/perinephric abscess; endocarditis emboli | Contrast allergy; renal impairment |
| Echocardiogram (TTE → TEE if needed) | - | URGENT | ROUTINE | URGENT | **All patients with S. aureus bacteremia should have echocardiogram**; endocarditis in 10-15% of S. aureus SEA | Vegetations; valvular regurgitation; abscess; Duke criteria | None (TTE); TEE: esophageal pathology, uncooperative patient |
| CT myelogram | - | EXT | - | EXT | Only if MRI absolutely contraindicated; intrathecal contrast via LP followed by CT; demonstrates level of compression; risk of meningitis seeding with LP | Complete or partial block; level of compression; intradural vs. extradural | Infection at LP site (SEA itself may preclude LP at involved level); coagulopathy |
| Nuclear medicine bone scan (Tc-99m) | - | - | EXT | - | If MRI unavailable; can identify osteomyelitis; may show uptake before radiographic changes; less specific than MRI | Increased uptake at infection site(s); may identify multifocal disease | Pregnancy; limited specificity |
| Gallium-67 or Indium-111 WBC scan | - | - | EXT | - | Chronic/subacute infection; differentiating active infection from degenerative changes; research use | Increased uptake at infection site | Limited availability; time-consuming; replaced largely by MRI |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT-guided biopsy/aspiration | - | URGENT | - | - | If diagnosis uncertain; culture acquisition for non-surgical management; distinguish abscess from tumor or hematoma | Organism identification; Gram stain; histopathology confirming infection vs. other pathology | Coagulopathy; inaccessible location; very small collection |
| PET/CT (FDG) | - | - | EXT | - | Chronic/recurrent infection; assess treatment response; identify additional sites of infection; research use | Increased FDG uptake at infection site; may identify occult primary source | Uncontrolled diabetes (glucose >200); pregnancy |
| Repeat MRI (during treatment) | - | ROUTINE | ROUTINE | - | At 2-4 weeks or if clinical worsening; assess treatment response; monitor for abscess expansion; may appear worse before better on imaging | Stable or decreasing collection size; resolving edema; NOTE: Imaging may lag behind clinical improvement (may appear worse at 2 weeks even with successful treatment) | Same as initial MRI |
| Post-treatment MRI | - | ROUTINE | ROUTINE | - | At end of antibiotic course (6-8 weeks); baseline for comparison; assess for residual disease | Resolution or significant improvement of collection; healed osteomyelitis; residual enhancement may persist for months (does not necessarily indicate active infection) | Same as MRI |

### Lumbar Puncture

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP — Generally NOT indicated | - | - | - | - | **LP is generally CONTRAINDICATED in suspected SEA**; risk of seeding infection into subarachnoid space → meningitis/spinal subdural empyema; imaging (MRI) is diagnostic modality of choice | N/A | **AVOID LP if SEA suspected** — LP may spread infection into intradural space; if meningitis suspected concurrently, discuss with neurosurgery/ID before LP |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Empiric IV antibiotics (STAT)** | IV | - | 25-30 mg/kg :: IV :: q12h :: **Start IMMEDIATELY after blood cultures drawn — do NOT delay for MRI or organism identification**; **First-line empiric:** Vancomycin 25-30 mg/kg IV load (max 2g), then 15-20 mg/kg IV q8-12h (target trough 15-20 mcg/mL) PLUS Ceftriaxone 2g IV q12h OR Cefepime 2g IV q8h; **Alternative for β-lactam allergy:** Vancomycin + aztreonam 2g IV q8h OR Vancomycin + fluoroquinolone (levofloxacin 750 mg daily); **If Pseudomonas risk (IVDU, immunocompromised):** Add anti-pseudomonal coverage with cefepime or piperacillin-tazobactam 4.5g IV q6h; **Adjust to culture results when available** | - | Vancomycin covers MRSA (most important cause); ceftriaxone/cefepime covers MSSA, streptococci, gram-negatives; early antibiotics are associated with better outcomes; every hour of delay increases mortality in sepsis | STAT | STAT | - | STAT |
| **Emergent surgical decompression + drainage** | - | - | **INDICATIONS (Surgery preferred):** (1) Neurologic deficit (any weakness, bowel/bladder dysfunction), (2) Sepsis/hemodynamic instability not improving with antibiotics, (3) Significant cord compression on imaging, (4) Failure of medical therapy (no improvement at 48-72h, worsening at any time), (5) Unknown organism (need tissue diagnosis); **Procedure:** Posterior laminectomy with abscess drainage; cultures from abscess; débridement of infected tissue; may need instrumentation if instability; **Timing:** Within 24h of diagnosis; emergent (within hours) if progressive deficit | - | Darouiche (2006): Surgical outcomes better than medical management in patients with neurologic deficit; earlier surgery (within 24h) associated with better neurologic recovery; pre-operative neurologic status is #1 predictor of outcome | - | STAT | - | - |
| **DVT prophylaxis** | SC | - | 40 mg :: SC :: daily :: SCDs immediately; pharmacologic prophylaxis: enoxaparin 40 mg SQ daily — timing is nuanced: may start within 24h of admission if no imminent surgery; post-operatively start 12-24h after surgery per surgeon; high VTE risk population | - | Immobile + infection + inflammatory state = very high DVT risk; mechanical prophylaxis universal; pharmacologic prophylaxis as soon as surgically safe | STAT | STAT | - | STAT |
| **Pain management** | IV | - | 650-1000 mg :: IV :: q6h :: Back pain often severe; acetaminophen 650-1000 mg q6h (scheduled) + opioids (morphine 2-4 mg IV q3h PRN or hydromorphone 0.5-1 mg IV q3h PRN); NSAIDs: use cautiously (renal function, surgical bleeding) — some ID physicians avoid NSAIDs in active infection; neuropathic agents (gabapentin) if radicular component | - | Severe pain is hallmark of SEA; adequate analgesia is essential; balance with need for neurologic monitoring | STAT | STAT | ROUTINE | STAT |
| **Sepsis resuscitation (if septic)** | IV | - | 30 mL/kg :: IV :: - :: Surviving Sepsis guidelines: lactate measurement; blood cultures before antibiotics; IV crystalloid 30 mL/kg for hypotension or lactate ≥4 mmol/L; vasopressors (norepinephrine first-line) if MAP <65 despite fluids; reassess volume status; repeat lactate if initially elevated | - | Sepsis from SEA has high mortality; early aggressive resuscitation improves outcomes | STAT | STAT | - | STAT |
| **Glucose control** | IV | - | 180 mg :: IV :: once :: Target glucose <180 mg/dL; insulin infusion if critically ill; sliding scale or basal-bolus for non-ICU patients; diabetes is major risk factor — optimize control | - | Hyperglycemia impairs immune function and wound healing; tight glucose control improves infection outcomes | STAT | STAT | ROUTINE | STAT |

### 3B. Definitive/Targeted Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Targeted IV antibiotic therapy (based on culture results)** | IV | - | 2g :: IV :: q4h :: **Tailor to organism and sensitivities; typical regimens:** — **MSSA:** Nafcillin 2g IV q4h OR cefazolin 2g IV q8h (preferred for tolerability); duration 6-8 weeks; — **MRSA:** Vancomycin 15-20 mg/kg IV q8-12h (trough 15-20) for 6-8 weeks; alternatives: daptomycin 6-8 mg/kg IV daily (avoid if pneumonia), linezolid 600 mg IV/PO q12h (monitor for toxicity if >2 weeks); — **Streptococci:** Penicillin G 4 million units IV q4h or ceftriaxone 2g IV q12h x 6 weeks; — **Enterococcus:** Ampicillin 2g IV q4h (if susceptible) ± gentamicin synergy; vancomycin if ampicillin-resistant; — **Gram-negatives:** Ceftriaxone 2g IV q12h or cefepime 2g IV q8h or ciprofloxacin 400 mg IV q8h x 6 weeks depending on sensitivities; — **Pseudomonas:** Cefepime 2g IV q8h or meropenem 2g IV q8h x 6 weeks | - | IV antibiotics are standard for SEA/osteomyelitis; oral transition data emerging (OVIVA trial) but traditionally 6-8 weeks IV; de-escalate from empiric coverage once cultures return | - | STAT | ROUTINE | STAT |
| **Duration of antibiotics** | IV | - | **SEA without osteomyelitis:** 4-6 weeks IV; **SEA with vertebral osteomyelitis (most cases):** 6-8 weeks IV; **SEA with endocarditis:** 6 weeks minimum from first negative blood culture; duration guided by clinical response, inflammatory markers (ESR, CRP), repeat imaging; may extend if slow response | - | IDSA guidelines: 6 weeks for vertebral osteomyelitis; 4-6 weeks for epidural abscess alone; endocarditis requires 6-week minimum; individualized based on response | - | STAT | ROUTINE | STAT |
| **Oral antibiotic transition (selected cases)** | IV | - | 750 mg :: IV :: daily :: **OVIVA trial (2019):** Oral antibiotics non-inferior to IV for bone/joint infections after initial 2 weeks IV in stable patients; **Candidates:** Clinically improving; afebrile; tolerating PO; CRP trending down; adherent; close follow-up available; **Oral options:** Fluoroquinolone (levofloxacin 750 mg daily or ciprofloxacin 750 mg BID) + rifampin 300 mg BID (NOT monotherapy); linezolid 600 mg BID (monitor CBC, neuropathy); TMP-SMX DS 2 tabs BID (for MRSA); **NOT for:** Endocarditis, undrained abscess, persistent bacteremia, non-adherent patient | - | OVIVA trial showed oral switch after 2 weeks IV is non-inferior for bone/joint infections; reduces costs, IV complications, hospital stay; requires careful patient selection and close monitoring; NOT standard for all SEA cases | - | - | ROUTINE | - |
| **Surgical drainage (if not done emergently)** | - | - | **If initial medical management:** Re-evaluate need for surgery at 48-72h; indications for delayed surgery: failure to improve, neurologic deterioration, persistent fever/bacteremia, abscess enlargement on imaging; **Procedure:** Laminectomy + drainage; send cultures even if already on antibiotics (may still grow organism); instrumented fusion if instability/destruction | - | Surgery provides source control, tissue diagnosis, and decompression; delayed surgery for medical failure still beneficial if performed before complete paralysis | - | URGENT | - | - |
| **Medical management alone (selected cases)** | - | - | **Candidates for medical management without surgery:** (1) No neurologic deficit, (2) Organism identified (blood cultures positive), (3) Small abscess (<3 cm collection), (4) Poor surgical candidate (extreme comorbidities), (5) Panspinal disease (multiple levels — surgery impractical); **Requirements:** Very close neurologic monitoring (q2-4h initially); repeat MRI at 48-72h and weekly; immediate surgery if any deterioration; adherent patient | - | Observational studies: ~40% of SEA can be managed medically if no neurologic deficit and criteria met; HOWEVER, 10-20% will fail medical therapy and require surgery; early surgery generally preferred if feasible | - | STAT | ROUTINE | - |

### 3C. Adjunctive Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **PICC line placement** | IV | - | If prolonged IV antibiotics planned (6-8 weeks); enables outpatient IV therapy (OPAT); placed once stabilized and duration confirmed; confirm tip position with X-ray | - | Required for OPAT; reduces peripheral IV complications; monitor for PICC-associated infection | - | URGENT | ROUTINE | - |
| **Outpatient parenteral antibiotic therapy (OPAT)** | PO | - | Once clinically stable (afebrile, pain controlled, neurologically stable, adequate PO intake, safe home environment); PICC in place; infusion teaching completed; close ID follow-up (weekly visits); VNA nursing for line care | - | Reduces hospital stay; comparable outcomes to inpatient therapy in appropriate patients; weekly ID visits with labs (CBC, CMP, drug levels, CRP) | - | ROUTINE | ROUTINE | - |
| **Rifampin (adjunctive)** | PO | - | 300 mg :: PO :: BID :: For staphylococcal osteomyelitis (vertebral involvement); enhances bone penetration; prevents biofilm; **ONLY as adjunctive therapy — never monotherapy (rapid resistance)**; Rifampin 300 mg PO BID added to primary anti-staphylococcal agent; check interactions (CYP3A4 inducer — reduces warfarin, HIV meds, oral contraceptives, etc.) | - | Rifampin improves outcomes in staphylococcal bone infections; biofilm activity; excellent bone penetration; drug interactions are significant | - | ROUTINE | ROUTINE | - |
| **Bracing / spinal orthosis** | - | - | If spinal instability (vertebral body destruction, kyphosis, instrumentation); TLSO for thoracolumbar; cervical collar for cervical; duration: typically 6-12 weeks or until radiographic healing | - | External stabilization; pain relief; prevents pathologic fracture progression; may allow non-operative management of mild instability | - | ROUTINE | ROUTINE | - |
| **Nutritional optimization** | - | - | 1.2-1.5 g/kg :: - :: - :: Protein supplementation (1.2-1.5 g/kg/day); calorie optimization; correct vitamin deficiencies; dietitian consultation; affects wound healing and immune function | - | Malnutrition common in chronic illness; protein essential for wound healing; improves infection outcomes | - | ROUTINE | ROUTINE | - |
| **Diabetes optimization** | - | - | 180 mg :: PO :: - :: Endocrinology consult if poorly controlled; insulin titration; goal HbA1c <7.5% (individualized); glucose <180 mg/dL during acute illness | - | Diabetes is major risk factor; uncontrolled diabetes impairs healing and immune response | - | STAT | ROUTINE | STAT |
| **Substance abuse counseling (if applicable)** | - | - | 30% :: - :: - :: IVDU is major risk factor for SEA (20-30% of cases); addiction medicine consultation; harm reduction; hepatitis/HIV screening; reduces recurrence risk | - | IVDU patients at high risk for recurrent infection; addressing substance use reduces future SEA risk | - | ROUTINE | ROUTINE | - |

### 3D. Medications to AVOID or Use with Caution

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Daptomycin (with pneumonia) | - | - | - | - | - | - | - | - | - | - |
| Rifampin monotherapy | - | - | - | - | - | - | - | - | - | - |
| Linezolid >2-4 weeks | - | - | - | - | - | - | - | - | - | - |
| Aminoglycosides (prolonged use) | - | - | - | - | - | - | - | - | - | - |
| Corticosteroids (routine use) | - | - | - | - | - | - | - | - | - | - |
| NSAIDs (prolonged, peri-operative) | - | - | - | - | - | - | - | - | - | - |
| LP (in suspected SEA) | - | - | - | - | - | - | - | - | - | - |
| Epidural steroid injection (as treatment or in area of abscess) | - | - | - | - | - | - | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Spine surgery / Neurosurgery consultation — EMERGENT | STAT | STAT | - | STAT | **Consult IMMEDIATELY on suspicion** — before or concurrent with MRI; surgery vs. medical management decision; ALL patients with SEA need spine surgery evaluation even if medical management is planned (contingency for neurologic deterioration) |
| Infectious disease consultation | STAT | STAT | ROUTINE | STAT | Antibiotic selection; duration; OPAT planning; monitoring plan; repeat imaging decisions; often co-manage with surgery |
| Neurologic examination — serial monitoring | STAT | STAT | - | STAT | **CRITICAL:** q2-4h neurologic checks initially; document motor strength (bilateral LE myotomes), sensory level, rectal tone, bladder function; ANY deterioration → STAT surgical evaluation; pre-operative neuro status is the #1 outcome predictor |
| Source identification | STAT | STAT | ROUTINE | STAT | Identify primary infection source: skin/soft tissue (cellulitis, IV site), UTI, endocarditis, dental abscess, pneumonia, intra-abdominal abscess, recent procedure (epidural injection, spinal surgery); treat primary source |
| Blood cultures (before antibiotics) | STAT | STAT | - | STAT | CRITICAL — positive in 60-70%; draw 2 sets from separate sites; do NOT delay antibiotics if cultures cause delay — draw quickly and start treatment |
| Fall precautions / mobility assessment | STAT | STAT | ROUTINE | STAT | SEA patients may have weakness, sensory loss, impaired balance; fall risk assessment; assistive devices; PT/OT evaluation |
| Documentation of timeline | STAT | STAT | - | STAT | Document: time of symptom onset (back pain → radiculopathy → weakness is classic progression over days-weeks), time of presentation, time of MRI, time of surgical consultation, time of antibiotics, neurologic exam at each time point |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Echocardiogram (TTE ± TEE) | - | URGENT | ROUTINE | URGENT | All patients with S. aureus bacteremia (IE in 10-15%); if TTE negative but high suspicion → TEE; affects antibiotic duration and management |
| Dental evaluation | - | ROUTINE | ROUTINE | - | Dental abscess as source; poor dentition as risk factor; dental clearance before prolonged antibiotics (if teeth issues could reinfect) |
| PICC placement / vascular access | - | URGENT | ROUTINE | - | Long-term IV access for 6-8 weeks of antibiotics; PICC is standard; peripherally inserted; confirm tip position |
| Social work / case management | - | ROUTINE | ROUTINE | - | OPAT coordination; home infusion setup; substance abuse services; insurance authorization; discharge planning |
| Addiction medicine (if IVDU) | - | ROUTINE | ROUTINE | - | IVDU is major risk factor (20-30%); buprenorphine or methadone initiation; harm reduction; reduces future infection risk |
| Pain management service | - | ROUTINE | ROUTINE | - | Chronic pain common after SEA; multimodal approach; avoid long-term opioids if possible; neuropathic agents |
| Physical / occupational therapy | - | URGENT | ROUTINE | - | Mobility assessment; strengthening; ADL training; rehabilitation planning if neurologic deficits |
| VNA / home health | - | ROUTINE | ROUTINE | - | PICC care; medication assistance; wound care (if post-operative); safety checks |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Repeat MRI | - | URGENT | ROUTINE | URGENT | At 48-72h if medically managed (assess for enlargement); at 2-4 weeks (assess treatment response — NOTE: imaging may appear worse before better); at end of treatment (baseline); PRN if clinical worsening |
| CT-guided drainage (percutaneous) | - | URGENT | - | - | Alternative to surgery in selected cases (poor surgical candidate, small collection, posterior access); less reliable than surgical drainage; may be repeated if recurrence |
| Revision surgery / repeat drainage | - | URGENT | ROUTINE | - | If treatment failure (persistent fever, neurologic decline, enlarging collection); undrained loculations; retained infected hardware |
| Infectious disease second opinion | - | ROUTINE | ROUTINE | - | Culture-negative SEA; unusual organism; treatment failure; complex antibiotic decisions |
| Long-term suppressive antibiotics | - | - | ROUTINE | - | Selected cases with retained hardware, incompletely treated osteomyelitis, immunocompromised; oral suppressive therapy (TMP-SMX, doxycycline, or other based on organism) after initial 6-8 week course; indefinite duration in some cases |
| Spinal fusion (delayed) | - | - | ROUTINE | - | If significant vertebral destruction and instability after infection controlled; typically 6-12 weeks after infection resolution; staged reconstruction |
| Hyperbaric oxygen therapy | - | - | EXT | - | Refractory osteomyelitis; adjunctive to antibiotics and surgery; limited evidence but some centers use for difficult cases |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Primary Differential Diagnoses

| Diagnosis | Key Differentiating Features | Distinguishing Studies |
|-----------|------------------------------|----------------------|
| Malignant spinal cord compression (MSCC) / Metastatic epidural disease | Known cancer history; bone destruction without disc involvement (SEA typically involves disc); no fever (usually); no elevated ESR/CRP/WBC (unless concurrent infection); may be painful but not typically as acute; enhances but no ring-enhancement or diffusion restriction | MRI: enhancing epidural mass WITHOUT ring enhancement or restricted diffusion; bone destruction; CT/PET: metastatic staging; tumor markers; biopsy if uncertain; ESR/CRP may be mildly elevated in malignancy but not as high as SEA |
| Vertebral compression fracture (osteoporotic) | Older patient; osteoporosis history; no fever; acute onset with movement; no neurologic deficit (usually); no elevated inflammatory markers; vertebral body wedging; may have benign edema | MRI: vertebral body edema WITHOUT epidural collection; no ring enhancement; normal ESR/CRP; DEXA: osteoporosis; mechanism (fall, lifting); responds to bracing/pain management |
| Disc herniation (without infection) | No fever; no elevated inflammatory markers; unilateral radiculopathy (usually); no epidural collection on MRI; common, benign presentation | MRI: disc herniation without epidural enhancement; no T2 hyperintense collection; normal ESR/CRP; normal WBC; unilateral symptoms more common |
| Spinal epidural hematoma | Anticoagulation; post-procedural (epidural injection, LP, surgery); acute onset; hematoma signal characteristics on MRI (not ring-enhancing); no fever; rapidly progressive | MRI: epidural collection with blood signal (T1 hyperintense in subacute phase); NO ring enhancement; NO restricted diffusion in hematoma (unlike abscess); coagulation studies; anticoagulation history; recent procedure |
| Transverse myelitis / NMOSD | Intramedullary (within cord) rather than epidural; autoimmune; no fever; no elevated ESR/CRP (or mildly elevated); subacute onset; responds to steroids/PLEX | MRI: intramedullary T2 hyperintensity, NOT epidural collection; AQP4/MOG antibodies; CSF: pleocytosis but sterile; normal inflammatory markers |
| Degenerative lumbar stenosis | Chronic symptoms (claudication); older patient; no fever; no inflammatory markers; bilateral symptoms with walking; relieved by sitting/flexion; chronic findings on MRI | MRI: chronic stenosis (ligamentum flavum hypertrophy, disc bulging, facet hypertrophy) WITHOUT acute epidural collection; normal ESR/CRP; chronic history |
| Vertebral osteomyelitis (without epidural extension) | Similar to SEA but NO epidural collection; disc and vertebral body involvement; back pain and fever; elevated inflammatory markers; may progress to SEA | MRI: vertebral body and disc enhancement and edema WITHOUT epidural collection; blood cultures may be positive; requires IV antibiotics but not emergent surgical decompression (unless instability or progression to SEA) |
| Psoas abscess | Contiguous spread can cause spinal infection; flank/groin pain; hip flexion pain; may track from spine or vice versa; fever; iliopsoas enhancement on imaging | CT/MRI: psoas muscle enlargement with rim-enhancing collection; may extend to spine; blood cultures; percutaneous drainage often possible |

### Classic Clinical Triad (Only present in 10-15%)

| Phase | Symptom | Timing |
|-------|---------|--------|
| Phase 1 | Back pain (localized, severe) | Days to weeks before diagnosis |
| Phase 2 | Radicular pain (nerve root irritation) | Days after back pain onset |
| Phase 3 | Neurologic deficit (weakness, bowel/bladder) | Hours to days after radicular pain |

**NOTE:** The classic triad (back pain → radiculopathy → paralysis) is present in only 10-15% of patients at presentation. Most patients present with 1-2 features. Maintain HIGH suspicion in any patient with back pain + fever, especially with risk factors.

### Red Flags Requiring Urgent Reassessment

| Red Flag | Concern | Action |
|----------|---------|--------|
| ANY new neurologic deficit (weakness, sensory loss, bladder dysfunction) | Progression of cord/root compression; medical management failure | STAT MRI; immediate surgical consultation; emergent decompression if progressive |
| Fever not improving after 48-72h of antibiotics | Undrained collection; wrong antibiotic coverage; drug fever; secondary site | Repeat imaging (MRI); reassess antibiotic coverage; consider surgical drainage |
| Persistent or worsening back pain | Abscess enlargement; vertebral instability; pathologic fracture | Repeat MRI; surgical re-evaluation; bracing assessment |
| Persistent bacteremia | Undrained source; endocarditis; seeded secondary site | TEE; repeat imaging; consider surgery for source control |
| Sepsis not resolving | Inadequate source control; resistant organism; secondary infection | ICU reassessment; surgical drainage if not done; broaden antibiotics; repeat cultures |
| New back pain at different level | Multifocal SEA (present in 15-20%); skip lesion | MRI whole spine (if not already done); assess new level |
| Rising inflammatory markers after initial improvement | Treatment failure; secondary infection; abscess loculation | Repeat imaging; reassess antibiotic coverage; surgical consultation |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (First 72h)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic examination (motor strength, sensory level, rectal tone, bladder) | q2-4h initially; q4-6h once stable | Stable or improving; NO new deficits | ANY deterioration → STAT MRI → emergent surgical consultation → likely emergent decompression |
| Temperature | q4h | Afebrile (<38°C) by 48-72h of antibiotics | Persistent fever: repeat cultures; imaging for undrained collection; reassess antibiotics; echocardiogram |
| Blood pressure / hemodynamics | Continuous if septic; q4h if stable | MAP >65; resolving sepsis | Vasopressors; fluid resuscitation; ICU care for septic shock |
| Pain score (NRS) | q4h | Improving; NRS <4/10 | Escalate analgesia; worsening pain may indicate abscess enlargement or instability |
| Blood cultures (repeat) | Daily until negative | Negative cultures within 48-72h of appropriate antibiotics | Persistent bacteremia: echocardiogram (TEE); imaging for undrained focus; consider surgery |
| WBC, CRP | Daily initially | Trending down | Rising inflammatory markers: treatment failure; repeat imaging; reassess management |
| Vancomycin trough (if on vancomycin) | Before 4th dose; then 2-3x/week | 15-20 mcg/mL (for serious infection) | Adjust dose if outside range; monitor renal function |
| Renal function (BUN/Cr) | Daily initially; 2-3x/week ongoing | Stable | Nephrotoxicity: adjust vancomycin and other renally-cleared drugs; adequate hydration |
| Blood glucose | q6h (q4h if critically ill) | <180 mg/dL | Insulin titration |

### Subacute Monitoring (Hospital and OPAT)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic examination | Daily (hospital); weekly (OPAT) | Stable or improving | New deficits: urgent MRI; surgical re-evaluation |
| ESR | Weekly | Declining trend (may take 3-4 weeks to start declining); normalize by 6-8 weeks (varies) | Not declining: consider treatment failure; repeat imaging; ID reassessment |
| CRP | Weekly | Should decline within 1-2 weeks; normalize before ESR | Rising CRP: treatment failure; repeat imaging |
| CBC (especially if on linezolid) | Weekly | Stable; no cytopenias | Linezolid: thrombocytopenia, anemia → consider discontinuation if <2 weeks remaining or switch agent |
| Renal function + vancomycin trough | 2-3x/week; weekly once stable | Stable; trough 15-20 | Dose adjustment |
| LFTs (if on rifampin) | Weekly | Stable | Transaminases >3x ULN: consider discontinuing rifampin |
| PICC line site | Daily | No erythema, drainage, tenderness | Line infection: remove PICC; cultures; may need new site |
| MRI spine | At 2-4 weeks; end of treatment; PRN for symptoms | Improving or stable; abscess resolving; NOTE: imaging may lag behind clinical improvement | Enlarging abscess despite antibiotics: surgical drainage; worsening imaging despite clinical improvement may be normal at 2-4 weeks |

### Long-term Follow-up

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Clinic visit (ID) | Weekly during OPAT; 2 weeks after completion; 3 months; 6 months; 12 months | No relapse; no recurrence | Relapse: repeat imaging; extended antibiotics; surgical reassessment |
| ESR/CRP | At end of treatment; 3 months; PRN | Normalized or stable at new baseline | Elevated: repeat MRI; consider relapse |
| MRI spine | End of treatment; 3-6 months; PRN for symptoms | Resolved or stable; no new disease | New or worsening: relapse; restart antibiotics ± surgery |
| Functional assessment | Each visit | Improved or stable function | Rehabilitation referral; pain management; chronic deficit management |
| Spine stability / alignment | Radiographs at 6 weeks, 3 months, 6 months, 12 months if instability | Stable alignment; healing | Progressive kyphosis or instability: surgical stabilization |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| ICU admission | Sepsis/septic shock; hemodynamic instability; respiratory compromise; post-operative monitoring (surgeon-dependent); severe neurologic deficit with close monitoring needed |
| General medical/neurosurgery floor | ALL patients with confirmed or suspected SEA require admission; IV antibiotic initiation; neurologic monitoring; surgical evaluation; pre-operative preparation if surgery planned |
| Observation (NOT appropriate) | SEA is NEVER an observation diagnosis; all patients require admission until diagnosis confirmed/excluded and treatment initiated |

### Discharge Criteria (Transition to OPAT)

| Criterion | Details |
|-----------|---------|
| Neurologic stability | Stable or improving neurologic exam for ≥48-72h; no new deficits; if deficits present: stable plateau |
| Afebrile | Afebrile for ≥24-48h on antibiotics |
| Hemodynamically stable | Off vasopressors; stable vital signs |
| Organism identified | Blood cultures or surgical cultures positive with sensitivities back; targeted antibiotic regimen |
| Antibiotic regimen finalized | IV regimen established; OPAT-compatible dosing (once daily or BID preferred); duration plan documented |
| PICC line placed | Functional PICC; confirmed position; patient educated on care |
| Pain controlled | Adequate oral pain control; no IV opioid requirement |
| Safe home environment | Able to care for self or adequate caregiver support; refrigeration for medications; clean environment; phone access |
| Follow-up arranged | ID clinic within 1 week; spine surgery follow-up (1-2 weeks if post-op); PCP; VNA nursing visits 2-3x/week |
| Patient/family education | PICC care; infusion technique (if self-administering); signs of treatment failure (fever, worsening pain, new weakness); when to call/return |
| Pharmacy/infusion arranged | Home infusion company contracted; medications delivered; pump if needed |

### Discharge Prescriptions Checklist

| Medication | Details |
|-----------|---------|
| IV antibiotic (specific to organism) | Dose, frequency, duration clearly documented (e.g., "Cefazolin 2g IV q8h x 6 weeks from [date]") |
| Oral analgesics | Acetaminophen, limited opioid PRN, gabapentin if neuropathic pain |
| DVT prophylaxis | Enoxaparin 40 mg SQ daily (if continuing) or transition to ambulation-based prevention |
| Rifampin (if applicable) | Only as adjunctive therapy; never monotherapy; document interactions |
| PPI / H2 blocker | If on steroids or at risk for GI bleed |
| Bowel regimen | If on opioids |
| Heparin flushes | For PICC maintenance |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| Vertebral Osteomyelitis Guidelines | IDSA Clinical Practice Guideline | 2015 | 6-week IV antibiotic duration for vertebral osteomyelitis; MRI is imaging modality of choice; surgical drainage if neurologic deficit, spinal instability, or failure of medical therapy |
| Spinal Epidural Abscess Management | AANS/CNS Joint Guidelines | 2017 | Emergent surgical decompression recommended for patients with neurologic deficit; medical management may be considered for select patients without deficit and with identified organism |
| Native Vertebral Osteomyelitis | British Infection Association / British Orthopaedic Association | 2015 | MRI within 24h; blood cultures before antibiotics; echocardiogram for S. aureus bacteremia; 6-week IV antibiotics |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [Darouiche (2006) — NEJM Review](https://pubmed.ncbi.nlm.nih.gov/17093252/) | Comprehensive review of SEA: S. aureus most common (60-70%); pre-operative neurologic status is #1 predictor of outcome; early surgery associated with better outcomes; medical management reasonable in selected cases without deficit | Established framework for surgical vs. medical management decision-making |
| [Siddiq et al. (2004)](https://pubmed.ncbi.nlm.nih.gov/15596629/) — Meta-analysis | 915 patients: Surgical treatment associated with better neurologic outcomes than medical management alone; patients presenting with neurologic deficit benefit most from early surgery | Supports surgical decompression as preferred approach, especially with neurologic deficit |
| [Connor et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23662888/) | Timing of surgery: decompression within 24h of neurologic deficit associated with significantly better outcomes than delayed surgery | Established 24h window for surgical decompression |
| [Patel et al. (2014)](https://pubmed.ncbi.nlm.nih.gov/24231778/) | Risk factors for poor outcome: advanced age, diabetes, MRSA, delayed diagnosis, pre-operative paralysis, cervical/thoracic location | Identified high-risk patients who may benefit from aggressive surgical approach |
| [Berbari et al. (2015) — IDSA Guidelines](https://pubmed.ncbi.nlm.nih.gov/26229122/) | 6-week IV antibiotic duration for vertebral osteomyelitis; longer for complicated cases (endocarditis, undrained abscess); rifampin adjunct for staphylococcal infections | Standardized antibiotic duration and adjunctive therapy |
| [OVIVA Trial (2019)](https://pubmed.ncbi.nlm.nih.gov/30699315/) | Oral antibiotics non-inferior to IV for bone/joint infections after initial IV therapy in stable patients; oral switch after 2 weeks IV | Opened possibility of early oral transition for selected patients; reduces hospitalization/OPAT burden; requires careful patient selection |
| [Reihsaus et al. (2000)](https://pubmed.ncbi.nlm.nih.gov/11153548/) | Meta-analysis: mortality 5%; permanent paralysis 4-22%; earlier surgery and better pre-operative function = better outcomes | Established prognostic importance of pre-operative neurologic status and early intervention |

### Risk Factor Summary

| Major Risk Factors | Prevalence in SEA |
|-------------------|------------------|
| Diabetes mellitus | 30-50% |
| Intravenous drug use (IVDU) | 20-30% |
| Recent spinal procedure/injection | 15-20% |
| Immunocompromised state (HIV, malignancy, steroids) | 15-20% |
| Chronic renal failure/hemodialysis | 10-15% |
| Alcoholism | 10-15% |
| Distant infection source (UTI, endocarditis, skin) | 30-40% |
| Recent bacteremia | 20-30% |
| Spinal abnormality (prior surgery, degenerative disease) | 15-20% |

### Microbiology

| Organism | Frequency | Key Features |
|----------|-----------|--------------|
| Staphylococcus aureus | 60-70% (MRSA 30-50% of S. aureus) | Most common; hematogenous spread; IVDU, skin infection, catheters; MRSA requires vancomycin |
| Coagulase-negative Staphylococci | 5-10% | Post-procedural; hardware-associated |
| Streptococci (including viridans, pneumoniae) | 5-10% | Endocarditis association; dental source |
| Gram-negative bacilli (E. coli, Pseudomonas, Klebsiella) | 10-15% | Urinary source; IVDU (Pseudomonas); diabetics |
| Enterococcus | 2-5% | Urinary source; GI/biliary source |
| Anaerobes | 2-5% | Often polymicrobial; abdominal/pelvic source |
| Mycobacterium tuberculosis | <5% (higher in endemic areas) | Subacute/chronic; Pott's disease; vertebral destruction; cold abscess; paraspinal extension |
| Fungi (Candida, Aspergillus) | <2% | IVDU; immunocompromised; indwelling catheters |
| Culture-negative | 10-20% | Prior antibiotics; fastidious organisms; consider TB, Brucella, fungi |

---

## APPENDICES

### Appendix A: Surgical vs. Medical Management Algorithm

```
SPINAL EPIDURAL ABSCESS CONFIRMED ON MRI
                │
                ├── NEUROLOGIC DEFICIT PRESENT?
                │        (weakness, sensory level, bowel/bladder dysfunction)
                │
                │   YES → EMERGENT SURGICAL DECOMPRESSION + DRAINAGE
                │         (within 24h; within hours if rapidly progressive)
                │         + IV antibiotics
                │
                │   NO (neurologically intact) ↓
                │
                ├── OTHER SURGICAL INDICATIONS?
                │        • Sepsis/hemodynamic instability not improving
                │        • Significant spinal instability
                │        • Large abscess (>2.5-3 cm)
                │        • Unknown organism (need tissue diagnosis)
                │        • Failure of medical therapy
                │
                │   YES → SURGICAL DRAINAGE + IV antibiotics
                │
                │   NO ↓
                │
                ├── CANDIDATE FOR MEDICAL MANAGEMENT?
                │        • No neurologic deficit
                │        • Organism identified (blood cultures positive)
                │        • Small abscess
                │        • Hemodynamically stable
                │        • Able to perform serial neuro exams (reliable)
                │
                │   YES → MEDICAL MANAGEMENT (IV antibiotics)
                │         WITH:
                │         • q2-4h neurologic checks (initially)
                │         • MRI at 48-72h (assess for enlargement)
                │         • Weekly MRI until improving
                │         • LOW threshold for surgery if ANY deterioration
                │
                │   NO → SURGICAL DRAINAGE + IV antibiotics
                │
                └── MEDICAL MANAGEMENT FAILURE?
                          • Neurologic deterioration (ANY)
                          • Persistent fever >72h
                          • Enlarging abscess on imaging
                          • Persistent bacteremia
                          • Clinical worsening
                                    ↓
                          SURGICAL DRAINAGE (delayed surgery)
```

### Appendix B: Antibiotic Selection Quick Reference

| Scenario | Empiric Regimen | Duration |
|----------|----------------|----------|
| Standard empiric (unknown organism) | Vancomycin 15-20 mg/kg IV q8-12h + Ceftriaxone 2g IV q12h | Adjust to cultures → 6-8 weeks total |
| Penicillin/cephalosporin allergy | Vancomycin + Aztreonam 2g IV q8h OR Vancomycin + Fluoroquinolone | Adjust to cultures |
| Pseudomonas risk (IVDU, immunocompromised) | Vancomycin + Cefepime 2g IV q8h OR Vancomycin + Pip-tazo 4.5g IV q6h | Adjust to cultures |
| **MSSA (confirmed)** | Nafcillin 2g IV q4h OR Cefazolin 2g IV q8h ± Rifampin 300mg PO BID (if vertebral involvement) | 6-8 weeks |
| **MRSA (confirmed)** | Vancomycin 15-20 mg/kg IV q8-12h (trough 15-20) ± Rifampin; ALT: Daptomycin 6-8 mg/kg IV daily (if no pneumonia) | 6-8 weeks |
| **Streptococci** | Penicillin G 4 MU IV q4h OR Ceftriaxone 2g IV q12h | 6 weeks |
| **Enterococcus (susceptible)** | Ampicillin 2g IV q4h ± Gentamicin 3mg/kg/day | 6 weeks |
| **Gram-negative (susceptible)** | Ceftriaxone 2g IV q12h OR Ciprofloxacin 400mg IV q8h → PO 750mg BID | 6 weeks |
| **With endocarditis** | Standard regimen for organism + extended duration (6 weeks minimum from first negative culture) | 6+ weeks |

### Appendix C: ESR/CRP Monitoring Interpretation

| Marker | Expected Trajectory | Concerning Trend | Action |
|--------|--------------------| ----------------|--------|
| CRP | Peaks early; should begin declining within 1 week; normalize by 3-4 weeks | Rising or plateau after 1 week | Repeat imaging; reassess antibiotic coverage; consider surgery |
| ESR | May initially rise; begins declining at 2-3 weeks; may not normalize for 6-8 weeks or longer | Rising after 3-4 weeks; failure to decline after 4 weeks | Repeat imaging; ID reassessment; consider treatment failure |
| WBC | Should normalize within days-1 week | Persistent leukocytosis | Evaluate for secondary site; persistent infection |

**NOTE:** ESR is slow to change and may remain elevated for weeks after successful treatment. CRP is more responsive and useful for early treatment monitoring. Imaging may appear worse at 2-4 weeks despite clinical improvement (this is normal — abscess organization and enhancement may increase before resolution).

### Appendix D: Scoring Systems

**Modified MESS Score (Medical vs. Surgical Management)**

Consider medical management if ALL of the following:
- [ ] No neurologic deficit
- [ ] Organism identified (blood cultures or biopsy positive)
- [ ] Abscess ≤2.5 cm in maximum dimension
- [ ] No significant spinal instability (SINS <7)
- [ ] Hemodynamically stable (not septic shock)
- [ ] Patient can be monitored closely (serial exams possible)
- [ ] Patient is a poor surgical candidate (relative factor)

If ANY box is unchecked → strongly consider surgical drainage

**SINS (Spinal Instability Neoplastic Score) — Also useful for infection**

Can be applied to infectious destruction to assess instability (see MSCC template for full scoring details). SINS ≥7 suggests instability requiring surgical stabilization.

### Appendix E: Post-Discharge OPAT Monitoring Checklist

| Monitoring | Frequency | Parameters |
|-----------|-----------|------------|
| ID clinic visit | Weekly | Clinical assessment, review labs, antibiotic tolerance, PICC site |
| CBC | Weekly | Anemia, thrombocytopenia (linezolid), leukopenia |
| CMP | Weekly | Renal function (vancomycin, aminoglycosides) |
| Vancomycin trough | Weekly (more frequent initially) | Target 15-20 mcg/mL |
| ESR, CRP | Weekly | Declining trend |
| LFTs | Weekly (if on rifampin or other hepatotoxic drugs) | Transaminases <3x ULN |
| PICC site assessment | Each VNA visit (2-3x/week) | No erythema, drainage, tenderness |
| Neurologic exam | Each ID visit; patient self-monitoring daily | Stable; no new weakness/numbness |
| Temperature | Patient: daily | Afebrile |

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
