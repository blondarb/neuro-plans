---
title: "Alcohol Withdrawal Seizure"
description: "Clinical decision support for evaluation and management of alcohol withdrawal seizures"
version: "1.1"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - seizure
  - epilepsy
  - alcohol-withdrawal
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Alcohol Withdrawal Seizure

**VERSION:** 1.1
**CREATED:** January 30, 2026
**REVISED:** January 30, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Alcohol Withdrawal Seizure

**ICD-10:** G40.509 (Epilepsy, unspecified, not intractable, without status epilepticus), F10.231 (Alcohol dependence with withdrawal with perceptual disturbance), F10.239 (Alcohol dependence with withdrawal, uncomplicated), F10.230 (Alcohol dependence with withdrawal, uncomplicated), F10.232 (Alcohol dependence with withdrawal with perceptual disturbance), R56.9 (Unspecified convulsions)

**SYNONYMS:** Alcohol withdrawal seizure, AWS, rum fits, alcohol-related seizure, withdrawal seizure, alcohol detox seizure, ethanol withdrawal seizure, alcohol withdrawal convulsion, detoxification seizure, ETOH withdrawal seizure, booze fits, alcohol abstinence seizure, alcohol withdrawal epilepsy, provoked seizure alcohol, acute symptomatic seizure alcohol

**SCOPE:** Evaluation and management of seizures in the context of alcohol withdrawal in adults, including acute seizure management, prevention of recurrence, thiamine supplementation, electrolyte correction, CIWA-Ar protocol monitoring, and disposition planning. Covers both single withdrawal seizures and recurrent withdrawal seizures. Excludes chronic epilepsy management, status epilepticus (see Status Epilepticus template), seizures from acute alcohol intoxication, and non-withdrawal alcohol-associated seizures (e.g., head trauma while intoxicated).

---

**DEFINITIONS:**
- **Alcohol Withdrawal Seizure (AWS):** Generalized tonic-clonic seizure occurring within 6-48 hours after reduction or cessation of chronic alcohol use; peak incidence at 12-24 hours
- **CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol, Revised):** Validated 10-item scoring tool for severity of alcohol withdrawal; scores range 0-67
- **Delirium Tremens (DT):** Severe alcohol withdrawal with altered sensorium, autonomic hyperactivity, and hallucinations; onset typically 48-96 hours after last drink; mortality 1-5% with treatment
- **Kindling:** Progressive worsening of withdrawal severity with repeated withdrawal episodes; each successive withdrawal tends to be more severe
- **Provoked vs. Unprovoked Seizure:** Alcohol withdrawal seizures are classified as acute symptomatic (provoked) seizures and do not establish a diagnosis of epilepsy

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

**CLINICAL CONTEXT:**
- Alcohol withdrawal seizures account for approximately one-third of all new-onset seizures in adults presenting to the ED
- 90% of withdrawal seizures occur within 48 hours of last drink (peak 12-24 hours)
- Approximately 3% of patients with alcohol withdrawal seizures progress to status epilepticus
- Multiple prior withdrawal episodes increase seizure risk via kindling
- Concurrent metabolic derangements (hypomagnesemia, hypoglycemia, hyponatremia) lower seizure threshold further
- Thiamine deficiency is common and must be addressed to prevent Wernicke encephalopathy

---

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Point-of-care glucose (CPT 82962) | STAT | STAT | - | STAT | Hypoglycemia is immediately reversible cause; alcoholics have depleted glycogen stores | >70 mg/dL |
| Blood alcohol level (CPT 80320) | STAT | STAT | - | STAT | Document current level; seizures typically occur as level falls (not at peak); helps timeline estimation | Document level and correlate with withdrawal timeline |
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Infection screen; macrocytosis (chronic alcohol); thrombocytopenia (alcohol-related liver disease); baseline before treatment | Normal; macrocytosis suggests chronic alcohol use |
| CMP (BMP + LFTs) (CPT 80053) | STAT | STAT | ROUTINE | STAT | Electrolyte abnormalities (Na, K, Ca, Mg, glucose); renal function; hepatic function (alcoholic liver disease); AST:ALT ratio >2:1 suggests alcoholic hepatitis | Normal; correct abnormalities |
| Magnesium (CPT 83735) | STAT | STAT | ROUTINE | STAT | Hypomagnesemia is common in chronic alcohol use and lowers seizure threshold; required cofactor for thiamine metabolism | >2.0 mg/dL; replete aggressively if low |
| Calcium, ionized (CPT 82330) | STAT | STAT | ROUTINE | STAT | Hypocalcemia lowers seizure threshold; common in alcoholism and malnutrition | Ionized 4.5-5.3 mg/dL |
| Phosphorus (CPT 84100) | STAT | STAT | ROUTINE | STAT | Hypophosphatemia common in chronic alcohol use; refeeding risk | >2.5 mg/dL |
| Urine drug screen (CPT 80307) | STAT | STAT | - | STAT | Concurrent illicit drug use (cocaine, amphetamines, benzodiazepines); polypharmacy | Identify co-intoxicants; benzodiazepine presence may mask withdrawal |
| Lipase (CPT 83690) | STAT | STAT | - | STAT | Alcoholic pancreatitis as concurrent condition | Normal (<60 U/L) |
| Lactate (CPT 83605) | STAT | STAT | - | STAT | Post-ictal elevation expected; persistent elevation suggests ongoing seizure activity or sepsis | Mildly elevated post-ictal; should normalize within 1-2 hours |
| Urinalysis (CPT 81003) | STAT | STAT | ROUTINE | STAT | UTI as additional precipitant; rhabdomyolysis (myoglobinuria) | Negative; brown urine suggests rhabdomyolysis |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Ammonia (CPT 82140) | URGENT | STAT | - | STAT | Hepatic encephalopathy may coexist with or mimic alcohol withdrawal | <35 µmol/L |
| CPK/CK (CPT 82550) | URGENT | ROUTINE | - | STAT | Rhabdomyolysis from prolonged seizure activity or falls | <1000 U/L; if elevated, aggressive hydration |
| Coagulation panel (PT/INR, PTT) (CPT 85610, 85730) | URGENT | ROUTINE | - | STAT | Coagulopathy from liver disease; needed before LP if considered | Normal; elevated INR suggests hepatic synthetic dysfunction |
| Blood gas (ABG or VBG) (CPT 82803) | URGENT | ROUTINE | - | STAT | Post-ictal acidosis; respiratory status; lactate | Normal or mild post-ictal metabolic acidosis |
| Troponin (CPT 84484) | URGENT | ROUTINE | - | STAT | Cardiac stress from seizure, autonomic surge, or arrhythmia | Negative |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Thyroid dysfunction can affect seizure threshold | Normal |
| Pregnancy test (urine or serum beta-hCG) (CPT 81025) | STAT | STAT | ROUTINE | STAT | Affects treatment decisions (benzodiazepine safety, imaging); eclampsia consideration | Document status |
| Thiamine level (whole blood) (CPT 84425) | - | ROUTINE | - | ROUTINE | Confirms deficiency; do NOT delay treatment for result | Low suggests deficiency; treat empirically regardless |
| Vitamin B12 (CPT 82607) | - | ROUTINE | ROUTINE | - | Often co-deficient with thiamine in chronic alcohol use | Normal (>300 pg/mL) |
| Folate (CPT 82746) | - | ROUTINE | ROUTINE | - | Folate deficiency common in chronic alcohol use; contributes to macrocytic anemia | Normal |
| Prealbumin (CPT 84134) | - | ROUTINE | ROUTINE | - | Nutritional status assessment; short half-life reflects recent intake | Normal |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-seizure medication levels (if on ASMs) | STAT | STAT | ROUTINE | STAT | Subtherapeutic levels if patient on chronic ASMs | Therapeutic range |
| Expanded toxicology panel | URGENT | EXT | - | URGENT | Synthetic drugs, medications not on standard screen; methanol, ethylene glycol | Negative |
| Autoimmune encephalitis panel (serum) | - | EXT | EXT | EXT | If clinical presentation is atypical for simple withdrawal seizure | Negative |
| HIV (CPT 87389) | - | ROUTINE | ROUTINE | - | HIV-associated CNS disease; higher prevalence in some populations with alcohol use disorder | Negative |
| RPR/VDRL (CPT 86592) | - | ROUTINE | ROUTINE | - | Neurosyphilis; risk factor overlap with alcohol use | Negative |
| Hepatitis panel (CPT 86803, 86706) | - | ROUTINE | ROUTINE | - | Hepatitis B/C common with alcohol use disorder; affects treatment decisions | Negative |
| Osmolality (serum) (CPT 83930) | URGENT | ROUTINE | - | URGENT | Osmolar gap to exclude methanol or ethylene glycol poisoning | 280-295 mOsm/kg; calculate osmolar gap |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediately; alcoholic patients at high risk for subdural hematoma, traumatic hemorrhage, and falls | No hemorrhage, mass, or acute stroke; subdural hematoma common in chronic alcoholism | None in emergency |
| EEG (routine) (CPT 95816) | URGENT | URGENT | ROUTINE | URGENT | Within 24 hours if any atypical features or concern for non-convulsive status; not required for classic single withdrawal seizure | No ongoing epileptiform activity; generalized slowing expected in withdrawal | None significant |

**IMPORTANT:** CT head is recommended for ALL alcohol withdrawal seizures because:
1. Chronic alcoholism increases risk of subdural hematoma (even without remembered trauma)
2. Coagulopathy from liver disease increases hemorrhage risk
3. Falls during intoxication may cause unrecognized head injury
4. First-ever withdrawal seizure requires structural cause exclusion

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) | - | URGENT | ROUTINE | URGENT | Within 24-48 hours if first seizure, focal neurologic deficit, focal seizure semiology, or CT findings requiring further evaluation | Structural lesion, cortical abnormality, Wernicke changes (medial thalami, mammillary bodies, periaqueductal gray) | GFR <30 for gadolinium, pacemaker |
| Continuous EEG (cEEG) monitoring (CPT 95700) | - | URGENT | - | STAT | If altered mental status persists beyond expected post-ictal period; concern for non-convulsive status epilepticus | Non-convulsive seizures, non-convulsive status epilepticus | None significant |
| Chest X-ray (CPT 71046) | URGENT | ROUTINE | - | URGENT | Aspiration risk post-ictal; concurrent pneumonia in malnourished patients | Clear lungs; aspiration pneumonitis | None significant |
| ECG (CPT 93000) | URGENT | ROUTINE | ROUTINE | STAT | Arrhythmia from electrolyte abnormalities (hypomagnesemia, hypokalemia); QTc prolongation; cardiomyopathy | Normal sinus rhythm; correct QTc prolongation | None |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT angiography head/neck (CPT 70496, 70498) | URGENT | URGENT | - | URGENT | If stroke suspected | Vascular occlusion, dissection | Contrast allergy, renal insufficiency |
| MRA/MRV brain (CPT 70544) | - | ROUTINE | - | ROUTINE | If vascular etiology suspected | Venous thrombosis, vascular malformation | Same as MRI |
| Abdominal ultrasound (CPT 76700) | - | ROUTINE | ROUTINE | - | Liver assessment if hepatic disease suspected | Cirrhosis, portal hypertension, hepatic steatosis | None significant |

### LUMBAR PUNCTURE (CPT 62270)

**Indication:** Suspected CNS infection (meningitis, encephalitis) given fever, persistent altered mental status, nuchal rigidity, or immunocompromised state. NOT required for uncomplicated alcohol withdrawal seizure.

**Timing:** URGENT if infection suspected; after CT excludes mass effect

**Volume Required:** 10-15 mL (standard diagnostic)

| Study | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|-------|:--:|:----:|:---:|:---:|-----------|----------------|
| Opening pressure | URGENT | ROUTINE | - | STAT | Elevated ICP | 10-20 cm H2O |
| Cell count (tubes 1 and 4) (CPT 89051) | URGENT | ROUTINE | - | STAT | Infection, inflammation | WBC <5; RBC 0 |
| Protein (CPT 84157) | URGENT | ROUTINE | - | STAT | Elevated in infection, inflammation | 15-45 mg/dL |
| Glucose with serum glucose (CPT 82945) | URGENT | ROUTINE | - | STAT | Low in bacterial/fungal meningitis | >60% serum |
| Gram stain and culture (CPT 87205, 87070) | URGENT | ROUTINE | - | STAT | Bacterial meningitis | No organisms |
| BioFire FilmArray ME Panel (CPT 87483) | URGENT | ROUTINE | - | STAT | Rapid pathogen identification | Negative |
| HSV-1/2 PCR (CPT 87529) | URGENT | ROUTINE | - | STAT | HSV encephalitis | Negative |

**Special Handling:** HSV PCR refrigerated. Cell count within 1 hour.

**Contraindications:** Signs of herniation, coagulopathy (INR >1.5, platelets <50K), skin infection at LP site. CT before LP mandatory.

---

## 3. TREATMENT

**CRITICAL:** Alcohol withdrawal seizures require DUAL management: (1) seizure treatment/prevention with benzodiazepines and (2) prevention of Wernicke encephalopathy with IV thiamine. Each medication on its own row with complete dosing.

**KEY PRINCIPLES:**
- Benzodiazepines are the ONLY proven treatment for alcohol withdrawal seizures
- Phenytoin is NOT effective for alcohol withdrawal seizures and should NOT be used unless there is a concurrent epilepsy diagnosis
- Thiamine MUST be given BEFORE or WITH glucose to prevent precipitating Wernicke encephalopathy
- Long-acting benzodiazepines (chlordiazepoxide, diazepam) are preferred for smooth withdrawal prophylaxis
- Lorazepam or oxazepam preferred if significant liver disease (no hepatic metabolism required)

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Lorazepam IV | IV | Acute seizure cessation and withdrawal seizure prevention | 2-4 mg :: IV :: PRN q5-10min :: 2-4 mg IV push over 2 min; may repeat q5-10min; max 8-10 mg in first hour; preferred in hepatic impairment (no hepatic metabolism) | Acute narrow-angle glaucoma; severe respiratory depression without ventilator support | RR, O2 sat, BP, sedation level; airway equipment at bedside | STAT | STAT | - | STAT |
| Diazepam IV | IV | Acute seizure cessation; preferred for smooth withdrawal prophylaxis due to long-acting metabolites | 5-10 mg :: IV :: PRN q5-10min :: 5-10 mg IV push over 2-5 min; may repeat q5-10min; max 30 mg in first hour; long-acting active metabolite (desmethyldiazepam) provides smoother withdrawal coverage | Severe hepatic impairment (use lorazepam instead); severe respiratory depression | RR, O2 sat, BP, sedation level; active metabolites accumulate in liver disease | STAT | STAT | - | STAT |
| Midazolam IM | IM | Acute seizure if no IV access | 10 mg :: IM :: once :: 10 mg IM (if >=40 kg) or 0.2 mg/kg IM; single dose; obtain IV access urgently | Respiratory compromise | RR, O2 sat; prepare IV access immediately | STAT | STAT | - | STAT |
| Thiamine IV (high-dose) | IV | Wernicke encephalopathy prevention and treatment; MUST give before or with glucose | 500 mg :: IV :: TID x 3 days, then 250 mg daily x 5 days :: 500 mg IV TID for 3 days (diluted in 100 mL NS over 30 min), then 250 mg IV daily for 5 days; give BEFORE glucose | Rare anaphylaxis (extremely uncommon); have epinephrine available | Infusion reaction (rare); anaphylaxis extremely rare | STAT | STAT | - | STAT |
| Dextrose 50% IV | IV | Hypoglycemia correction; give AFTER thiamine | 25 g (50 mL) :: IV :: once :: 50 mL IV push (25 g) if glucose <70 or unknown; ALWAYS give thiamine first or simultaneously | Document hyperglycemia | Glucose recheck in 15-30 min | STAT | STAT | - | STAT |
| Magnesium sulfate IV | IV | Hypomagnesemia correction; required cofactor for thiamine metabolism | 2 g :: IV :: once, then 1 g q6h :: 2 g IV over 1 hour initially; then 1 g IV q6h until Mg >2.0 mg/dL; severe deficiency may require 4-6 g over first 24 hours | Renal failure (monitor levels closely); myasthenia gravis | Mg levels q12-24h; deep tendon reflexes; respiratory status; renal function | STAT | STAT | - | STAT |
| Supplemental oxygen | INH | Maintain oxygenation during and after seizure | 2-15 L :: INH :: continuous PRN :: 2-4 L nasal cannula or non-rebreather as needed to maintain O2 sat >94% | None | O2 sat continuous | STAT | STAT | - | STAT |
| IV fluids (isotonic) | IV | Volume resuscitation; chronic alcohol users are often dehydrated | 500-1000 mL :: IV :: bolus, then 150-250 mL/hr :: NS or LR bolus 500-1000 mL, then 150-250 mL/hr maintenance; add dextrose (D5NS) once thiamine given; correct dehydration | Fluid overload; severe hyponatremia (use caution with rate) | I/O, BP, Na; avoid rapid correction of hyponatremia (max 8-10 mEq/L per 24h) | STAT | STAT | - | STAT |

### 3B. Symptomatic/Withdrawal Management

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Chlordiazepoxide PO | PO | Symptom-triggered withdrawal management (CIWA-Ar based); preferred for mild-moderate withdrawal when oral route available | 25-100 mg :: PO :: q1h PRN (CIWA-Ar guided) :: CIWA-Ar >=10: give 25-100 mg PO q1h until CIWA <10; then PRN dosing; typical total day 1: 200-400 mg; taper over 3-5 days; long half-life provides smooth coverage | Severe hepatic impairment (use lorazepam); respiratory depression; acute intoxication | CIWA-Ar q1h during active treatment, then q4h when stable; RR, sedation level | URGENT | ROUTINE | - | - |
| Diazepam PO | PO | Symptom-triggered withdrawal management; alternative to chlordiazepoxide | 10-20 mg :: PO :: q1-2h PRN (CIWA-Ar guided) :: CIWA-Ar >=10: give 10-20 mg PO q1-2h until CIWA <10; then PRN dosing; taper over 3-5 days; long-acting metabolites | Severe hepatic impairment (use lorazepam); respiratory depression | CIWA-Ar q1h during active treatment, then q4h; RR, sedation level | URGENT | ROUTINE | - | - |
| Lorazepam PO | PO | Symptom-triggered withdrawal management; preferred in liver disease (no hepatic metabolism required) | 1-2 mg :: PO :: q1-2h PRN (CIWA-Ar guided) :: CIWA-Ar >=10: give 1-2 mg PO q1-2h until CIWA <10; then PRN dosing; shorter half-life requires more frequent dosing; preferred if AST/ALT elevated or known cirrhosis | Severe respiratory depression | CIWA-Ar q1h during active treatment, then q4h; RR, sedation level; shorter acting - watch for rebound | URGENT | ROUTINE | ROUTINE | URGENT |
| Oxazepam PO | PO | Withdrawal management in severe liver disease; no active metabolites | 15-30 mg :: PO :: q6-8h PRN (CIWA-Ar guided) :: 15-30 mg PO q6-8h; CIWA-Ar guided; no active metabolites; safest in severe hepatic impairment | Severe respiratory depression | CIWA-Ar; shorter half-life requires frequent monitoring | - | ROUTINE | - | - |
| Folic acid PO | PO | Folate deficiency correction; common in chronic alcohol use | 1 mg :: PO :: daily :: 1 mg PO daily; continue long-term if alcohol use disorder | None significant | Folate levels | - | ROUTINE | ROUTINE | ROUTINE |
| Multivitamin PO | PO | Nutritional supplementation; multiple micronutrient deficiencies in chronic alcohol use | 1 tablet :: PO :: daily :: 1 multivitamin tablet PO daily | None significant | Nutritional status | - | ROUTINE | ROUTINE | ROUTINE |
| Potassium chloride | IV/PO | Hypokalemia correction; common in alcoholism and with vomiting | 20-40 mEq :: IV/PO :: per level PRN :: Replace per level: K 3.0-3.5: 40 mEq PO; K <3.0: 20-40 mEq IV over 1-2 hours; check Mg (must replete Mg for K to correct) | Renal failure; hyperkalemia | K levels q6-12h; cardiac monitor if IV replacement | URGENT | ROUTINE | ROUTINE | STAT |
| Calcium gluconate IV | IV | Hypocalcemia correction; ionized calcium low | 1-2 g :: IV :: once over 10-20 min :: 1-2 g calcium gluconate IV over 10-20 min; check Mg (required for calcium homeostasis) | Digoxin use (cardiac arrhythmia risk) | Ionized calcium; cardiac monitor during infusion | URGENT | ROUTINE | - | STAT |
| Phosphorus replacement | IV/PO | Hypophosphatemia correction; common in alcoholism and refeeding | 15-45 mmol IV or 250 mg PO :: IV/PO :: per level :: Mild (2.0-2.5): K-Phos 250 mg PO TID; Moderate (1.0-2.0): NaPhos 15-30 mmol IV over 4-6h; Severe (<1.0): 30-45 mmol IV over 6h | Hyperphosphatemia; renal failure | Phosphorus levels q12-24h; calcium (inversely related) | URGENT | ROUTINE | ROUTINE | STAT |
| Ondansetron | IV | Nausea/vomiting (common in withdrawal) | 4 mg :: IV :: q8h PRN :: 4 mg IV q8h PRN; may also use PO/ODT formulation | QT prolongation; severe hepatic impairment | QTc if multiple doses | URGENT | ROUTINE | ROUTINE | URGENT |
| Acetaminophen | PO/IV | Headache and pain management; avoid NSAIDs due to bleeding and hepatic risk | 650-1000 mg :: PO/IV :: q6h PRN :: 650-1000 mg PO/IV q6h PRN; max 2000 mg/day in liver disease (3000 mg/day if normal liver) | Severe hepatic impairment (reduce max dose) | LFTs if prolonged use; reduce dose in liver disease | URGENT | ROUTINE | ROUTINE | URGENT |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Phenobarbital IV | IV | Refractory alcohol withdrawal not controlled by benzodiazepines alone; synergistic with benzodiazepines at GABA-A receptor | 130-260 mg :: IV :: q15-30min PRN, then 32-65 mg q8-12h :: 130-260 mg IV q15-30 min, titrate to symptom control; max loading 10-20 mg/kg; maintenance 32-65 mg IV/PO q8-12h; can be used as primary agent or adjunct | Porphyria; severe respiratory disease (unless intubated) | RR (respiratory depression additive with benzodiazepines); sedation; intubation equipment at bedside; phenobarbital level if prolonged use | URGENT | URGENT | - | STAT |
| Propofol infusion | IV | Severe refractory withdrawal with seizures requiring ICU-level sedation; GABA-A and NMDA activity | 1-2 mg/kg bolus, then 20-80 mcg/kg/min :: IV :: continuous infusion :: Load 1-2 mg/kg IV bolus; infusion 20-80 mcg/kg/min; titrate to RASS -2 to -3; max 200 mcg/kg/min; limit duration <48h at high doses | Propofol infusion syndrome risk; egg/soy allergy | cEEG if concern for seizures; triglycerides q24h; CPK; metabolic acidosis panel; hemodynamics | - | - | - | STAT |
| Dexmedetomidine infusion | IV | Adjunctive sedation for withdrawal; reduces benzodiazepine requirement; treats sympathetic hyperactivity | 0.2 mcg/kg/hr :: IV :: continuous infusion (max 1.5 mcg/kg/hr) :: Start 0.2 mcg/kg/hr; titrate to effect (max 1.5 mcg/kg/hr); no loading dose in hemodynamically unstable patients; reduces BZD requirements by 30-50% | Severe bradycardia; 2nd/3rd degree heart block; hypotension | HR, BP (bradycardia and hypotension); does NOT prevent seizures - must continue benzodiazepines | - | URGENT | - | STAT |
| Valproate IV | IV | Adjunctive for withdrawal seizure prevention when benzodiazepines insufficient; NOT a substitute for benzodiazepines | 20-40 mg/kg :: IV :: load, then 250-500 mg q8h :: 20-40 mg/kg IV over 30 min; then 250-500 mg IV q8h; monitor ammonia | Pregnancy (teratogenic); hepatic disease (common in this population); pancreatitis; mitochondrial disease | LFTs, ammonia, platelets; hepatotoxicity risk higher in alcoholic liver disease; pancreatitis risk | - | URGENT | - | URGENT |
| Levetiracetam IV | IV | Adjunctive seizure prophylaxis; NOT a substitute for benzodiazepines for withdrawal management; may be considered if concurrent epilepsy diagnosis or concern for non-withdrawal seizures | 1000-1500 mg :: IV :: q12h :: 1000-1500 mg IV q12h; does NOT treat withdrawal syndrome itself; use as adjunct only | Renal impairment (adjust dose if CrCl <50) | Behavioral changes; renal function; does NOT replace benzodiazepines | - | ROUTINE | ROUTINE | ROUTINE |
| Carbamazepine PO | PO | Alternative/adjunctive for mild-moderate withdrawal; may reduce withdrawal severity and seizure risk; evidence in European literature | 200 mg :: PO :: TID (titrate to 400 mg TID) :: Start 200 mg TID on day 1; may increase to 400 mg TID; taper over 5-7 days; can be used alone for mild withdrawal or as adjunct | Hepatic disease; bone marrow suppression; AV block; HLA-B*1502 positive (Asian populations) | CBC, LFTs, sodium (hyponatremia risk); drug interactions | - | ROUTINE | ROUTINE | - |
| Gabapentin PO | PO | Adjunctive for mild-moderate withdrawal symptoms; may reduce benzodiazepine requirements; limited evidence for seizure prevention | 300-600 mg :: PO :: TID (titrate to 900 mg TID) :: Start 300-600 mg TID; may increase to 900 mg TID; taper over 5-7 days; limited evidence for seizure prevention; better evidence for anxiety/insomnia symptoms | Renal impairment (adjust dose) | Sedation; renal function; NOT a substitute for benzodiazepines in moderate-severe withdrawal | - | ROUTINE | ROUTINE | - |

**IMPORTANT CLINICAL NOTES:**
- **Phenytoin is NOT effective** for alcohol withdrawal seizures and should NOT be used unless there is a concurrent established epilepsy diagnosis requiring phenytoin
- **Benzodiazepines are the standard of care** and the only agents with Class I evidence for prevention of recurrent withdrawal seizures and progression to delirium tremens
- Anti-seizure medications (levetiracetam, valproate, etc.) do NOT treat the underlying withdrawal syndrome and should NOT be used as monotherapy
- If patient has a concurrent epilepsy diagnosis, continue home ASMs AND add benzodiazepines for withdrawal management

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consult for first-time seizure evaluation to exclude non-withdrawal etiology and guide workup | URGENT | URGENT | ROUTINE | URGENT |
| Addiction medicine or psychiatry consult for alcohol use disorder treatment initiation (naltrexone, acamprosate, medication-assisted treatment) | - | ROUTINE | ROUTINE | - |
| Social work consult for substance abuse resources, rehabilitation program referral, and discharge planning | - | ROUTINE | ROUTINE | - |
| Gastroenterology/Hepatology referral if liver disease identified (elevated LFTs, cirrhosis on imaging, coagulopathy) | - | ROUTINE | ROUTINE | - |
| Nutrition/Dietitian consult for malnutrition assessment and refeeding syndrome prevention | - | ROUTINE | - | ROUTINE |
| ICU consult if CIWA-Ar >20, recurrent seizures despite treatment, or hemodynamic instability | STAT | STAT | - | - |
| Physical therapy for fall risk assessment and gait evaluation if ataxia or peripheral neuropathy present | - | ROUTINE | ROUTINE | - |
| Outpatient neurology follow-up in 2-4 weeks for seizure evaluation completion (MRI, EEG review) and determination if chronic ASM therapy needed | - | ROUTINE | ROUTINE | - |
| Primary care follow-up within 1 week of discharge for ongoing alcohol cessation support and medical management | ROUTINE | ROUTINE | - | - |
| Alcohol treatment program referral (inpatient rehabilitation, intensive outpatient program, or Alcoholics Anonymous) | - | ROUTINE | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Return to ED immediately if another seizure occurs, seizure lasts >5 minutes, difficulty breathing, persistent confusion, chest pain, or severe tremors/hallucinations (may indicate progression to delirium tremens) | STAT | STAT | STAT | - |
| Do NOT drive until cleared by neurology; seizures impair driving safety and most states require seizure-free interval | STAT | STAT | STAT | - |
| Do NOT stop drinking alcohol abruptly without medical supervision as this can provoke seizures and life-threatening withdrawal (seek medical detoxification) | STAT | STAT | STAT | - |
| Take all medications exactly as prescribed, especially benzodiazepines during the taper period; do NOT stop benzodiazepines abruptly | ROUTINE | ROUTINE | ROUTINE | - |
| Avoid operating heavy machinery, working at heights, swimming alone, or bathing alone until seizure-free and cleared by neurology | ROUTINE | ROUTINE | ROUTINE | - |
| Inform family members or housemates about seizure first aid: stay with person, protect head, do NOT put anything in mouth, time the seizure, call 911 if seizure lasts >5 minutes | ROUTINE | ROUTINE | ROUTINE | ROUTINE |
| Eat regular balanced meals to prevent hypoglycemia and maintain electrolyte balance; malnutrition increases seizure risk | - | ROUTINE | ROUTINE | - |
| Keep follow-up appointments with neurology and addiction medicine; recurrent withdrawal episodes worsen seizure severity via kindling | - | ROUTINE | ROUTINE | - |
| Wear medical identification bracelet indicating seizure history | - | ROUTINE | ROUTINE | - |
| Understand that each episode of alcohol withdrawal increases future seizure risk (kindling phenomenon); this is a progressive condition | - | ROUTINE | ROUTINE | - |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Alcohol cessation is the definitive treatment and most important intervention to prevent recurrent withdrawal seizures | ROUTINE | ROUTINE | ROUTINE | - |
| Supervised medical detoxification for future alcohol cessation attempts to prevent withdrawal seizures and delirium tremens | ROUTINE | ROUTINE | ROUTINE | - |
| Balanced nutrition with emphasis on thiamine-containing foods (whole grains, legumes, lean meats) to rebuild depleted stores | - | ROUTINE | ROUTINE | - |
| Sleep hygiene: maintain regular sleep schedule; sleep deprivation independently lowers seizure threshold | - | ROUTINE | ROUTINE | - |
| Thiamine supplementation 100 mg PO daily indefinitely if continued alcohol use or malnutrition risk persists | - | ROUTINE | ROUTINE | ROUTINE |
| Folic acid supplementation 1 mg PO daily for chronic deficiency prevention | - | ROUTINE | ROUTINE | ROUTINE |
| Avoid illicit drugs (especially stimulants: cocaine, amphetamines) which independently lower seizure threshold | ROUTINE | ROUTINE | ROUTINE | - |
| Stress management and coping strategies as alternatives to alcohol use; consider cognitive behavioral therapy (CBT) | - | - | ROUTINE | - |
| Home safety modifications: remove sharp furniture edges, avoid glass shower doors, keep bathroom door unlocked due to seizure risk | - | ROUTINE | ROUTINE | - |
| Regular exercise to improve overall health and support alcohol recovery; avoid extreme exertion that leads to dehydration | - | - | ROUTINE | - |
| Engage with peer support groups (Alcoholics Anonymous, SMART Recovery) for sustained sobriety | - | ROUTINE | ROUTINE | - |
| Avoid medications that lower seizure threshold (tramadol, bupropion at high doses, certain antipsychotics) without neurology guidance | - | ROUTINE | ROUTINE | ROUTINE |

---

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Epilepsy (new-onset or undiagnosed) | Focal onset features, aura, focal neurologic findings, seizures not temporally related to withdrawal timeline (6-48h) | MRI brain, EEG, detailed seizure semiology; focal epileptiform discharges on EEG |
| Subdural hematoma (acute or chronic) | History of falls or trauma (may be unrecognized); focal neurologic deficits; headache | CT head (STAT); chronic SDH common in alcoholics |
| Hypoglycemia | Diaphoresis, tremor, confusion; rapid improvement with glucose correction | Fingerstick glucose; resolves with dextrose |
| Metabolic encephalopathy (hepatic) | Asterixis, gradual onset, jaundice, ascites; no discrete seizure activity; elevated ammonia | Ammonia level, LFTs, abdominal exam; EEG shows triphasic waves |
| Delirium tremens | Occurs later (48-96h); prominent hallucinations, severe autonomic instability, agitation; altered sensorium is continuous (not post-ictal) | CIWA-Ar scoring; clinical timeline; seizures may precede DTs |
| Meningitis/Encephalitis | Fever, nuchal rigidity, photophobia; may have rash; progressive altered mental status | LP with CSF analysis; blood cultures; BioFire ME Panel |
| Wernicke encephalopathy | Oculomotor dysfunction (nystagmus, ophthalmoplegia), ataxia, confusion; may coexist with withdrawal seizures | MRI brain (thalamic/mammillary body changes); thiamine level; clinical response to thiamine |
| Toxic ingestion (methanol, ethylene glycol) | Anion gap metabolic acidosis, osmolar gap, visual disturbance (methanol), renal failure (ethylene glycol) | Osmolarity, osmolar gap, specific levels if available; ABG |
| Cocaine or amphetamine-induced seizure | Sympathomimetic signs (tachycardia, hypertension, mydriasis); seizure during intoxication rather than withdrawal | Urine drug screen; clinical timeline (seizure during use, not after stopping) |
| Traumatic brain injury | History of head trauma, focal deficits, scalp laceration/hematoma; may be unrecognized in intoxicated patients | CT head; clinical exam for signs of trauma |
| Psychogenic non-epileptic spells | Prolonged duration, asynchronous movements, eye closure, preserved awareness with bilateral movements, no post-ictal confusion | Video-EEG; normal prolactin drawn within 20 min |
| Hyponatremia-induced seizure | Sodium <120 mEq/L; gradual or rapid onset depending on acuity; often with beer potomania or SIADH | Serum sodium, osmolality; clinical response to sodium correction |
| Isoniazid toxicity | History of TB treatment, refractory seizures, metabolic acidosis; pyridoxine-responsive | Medication history; responds to pyridoxine (vitamin B6) |

---

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| CIWA-Ar score | STAT | STAT | - | STAT | q1h during active withdrawal, then q4h when CIWA <10 for 24h | CIWA <10 = mild; 10-18 = moderate; >18 = severe | Administer benzodiazepines per CIWA protocol; CIWA >20 → consider ICU |
| Neurologic exam (mental status, focal deficits) | STAT | STAT | ROUTINE | STAT | q2h in ED; q4h on floor; each visit OPD | Return to baseline; no focal deficits | Persistent AMS → cEEG; focal findings → urgent imaging |
| Vital signs (HR, BP, RR, temp) | STAT | STAT | ROUTINE | STAT | Continuous in ED/ICU; q1-2h on floor during active withdrawal | HR <120; SBP <180; RR >12; Temp <38.5°C | Tachycardia/hypertension → increase benzodiazepines; fever → infection workup |
| Pulse oximetry | STAT | STAT | - | STAT | Continuous in ED/ICU; q4h on floor | O2 sat >94% | Supplemental O2; assess airway; chest X-ray |
| Seizure recurrence | STAT | STAT | ROUTINE | STAT | Continuous observation during withdrawal period (48-72h) | No recurrent seizures | Additional benzodiazepine dosing; consider cEEG; ICU if recurrent |
| Glucose | STAT | STAT | - | STAT | q6h during active withdrawal; QAC if on D5 fluids | >70 mg/dL | Dextrose; adjust IV fluids |
| Electrolytes (Na, K, Mg, Ca, Phos) | STAT | STAT | ROUTINE | STAT | q6-12h during active withdrawal; daily once stable | Normal ranges | Replete deficiencies; monitor sodium correction rate |
| LFTs | URGENT | ROUTINE | ROUTINE | ROUTINE | Baseline, then q24-48h if abnormal | Trending toward normal | Adjust medications metabolized hepatically; hepatology consult if worsening |
| Cardiac telemetry | STAT | STAT | - | STAT | Continuous during active withdrawal | Normal sinus rhythm; QTc <500 ms | Treat arrhythmia; correct electrolytes; avoid QT-prolonging medications |
| Respiratory rate and pattern | STAT | STAT | - | STAT | Continuous with benzodiazepine use | RR >12 | Reduce benzodiazepine dose; naloxone if opioid co-ingestion suspected; consider intubation |
| Fluid balance (I/O) | - | ROUTINE | - | STAT | q8h on floor; q1-4h in ICU | Euvolemic; UOP >0.5 mL/kg/hr | Adjust IV fluids; assess for renal function |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| **Discharge home** | Single withdrawal seizure; returned to baseline neurologic function; CIWA <10 for >24 hours; stable vital signs; able to tolerate oral medications; no dangerous structural findings on CT; reliable adult supervision for 72 hours; outpatient follow-up arranged (neurology within 2-4 weeks, PCP within 1 week); understands return precautions and driving restriction; willing to engage with alcohol cessation resources |
| **Admit to floor (observation/telemetry)** | Multiple seizures; prolonged post-ictal period (>2 hours); CIWA 10-20 requiring ongoing benzodiazepine titration; electrolyte abnormalities requiring IV correction; new structural lesion on imaging requiring monitoring; unable to tolerate oral medications; no reliable supervision at home; history of delirium tremens or complicated withdrawal; significant comorbidities (liver disease, malnutrition) |
| **Admit to ICU** | Recurrent seizures despite benzodiazepine treatment; status epilepticus; CIWA >20 requiring high-dose or continuous benzodiazepine infusion; hemodynamic instability; respiratory compromise; delirium tremens; need for continuous EEG monitoring; phenobarbital or propofol infusion required; aspiration pneumonia with respiratory failure |
| **Transfer to higher level of care** | Neurology unavailable for consultation; continuous EEG monitoring unavailable; ICU services unavailable for refractory withdrawal; need for neurosurgical intervention (e.g., subdural hematoma evacuation) |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Benzodiazepines are first-line treatment for alcohol withdrawal seizures | Class I, Level A | [Mayo-Smith MF. NEJM 1997;337:689-695](https://pubmed.ncbi.nlm.nih.gov/9278467/) |
| Symptom-triggered therapy (CIWA-Ar) reduces total benzodiazepine dose and treatment duration vs fixed-schedule dosing | Class I, Level A | [Saitz R et al. JAMA 1994;272:519-523](https://pubmed.ncbi.nlm.nih.gov/8046805/) |
| Phenytoin is NOT effective for alcohol withdrawal seizures | Class I, Level A | [Rathlev NK et al. Ann Emerg Med 1994;24:116-118](https://pubmed.ncbi.nlm.nih.gov/8010553/); [Chance JF. Ann Emerg Med 1991;20:520-522](https://pubmed.ncbi.nlm.nih.gov/2024791/) |
| Lorazepam IV reduces seizure recurrence in alcohol withdrawal | Class I, Level A | [D'Onofrio G et al. Ann Emerg Med 1999;34:725-731](https://pubmed.ncbi.nlm.nih.gov/10577399/) |
| High-dose IV thiamine (500 mg TID) for Wernicke encephalopathy prevention in at-risk patients | Class IIa, Level B | [Ambrose ML et al. J Clin Neurosci 2001;8:256-259](https://pubmed.ncbi.nlm.nih.gov/11386801/); [Thomson AD et al. Alcohol Alcohol 2002;37:513-521](https://pubmed.ncbi.nlm.nih.gov/12414541/) |
| Alcohol withdrawal seizures occur in 6-48 hours after last drink; peak at 12-24 hours | Class II, Level B | [Victor M, Brausch C. Electroencephalogr Clin Neurophysiol 1967;22:63-70](https://pubmed.ncbi.nlm.nih.gov/4163649/) |
| Kindling phenomenon: progressive worsening of withdrawal with repeated episodes | Class II, Level B | [Ballenger JC, Post RM. Br J Psychiatry 1978;133:1-14](https://pubmed.ncbi.nlm.nih.gov/352467/) |
| CT head recommended for all first alcohol withdrawal seizures due to high incidence of concurrent traumatic pathology | Class II, Level B | [Earnest MP et al. Neurology 1988;38:1561-1565](https://pubmed.ncbi.nlm.nih.gov/3419599/) |
| Magnesium supplementation for alcohol withdrawal | Class IIb, Level B | [Wilson A, Bhagwan T. Cochrane Database Syst Rev 2001](https://pubmed.ncbi.nlm.nih.gov/11279756/) |
| Phenobarbital as adjunct or alternative for severe alcohol withdrawal | Class IIa, Level B | [Tidwell WP et al. Ann Pharmacother 2018;52:57-65](https://pubmed.ncbi.nlm.nih.gov/28886676/) |
| ASAM Clinical Practice Guideline on alcohol withdrawal management | Guideline | [ASAM 2020 Clinical Practice Guideline](https://pubmed.ncbi.nlm.nih.gov/31916890/) |
| ACEP Clinical Policy on alcohol withdrawal management | Guideline | [Wolf SJ et al. Ann Emerg Med 2022;79:e1-e26](https://pubmed.ncbi.nlm.nih.gov/34112510/) |
| Dexmedetomidine as adjunctive therapy reduces benzodiazepine requirements in alcohol withdrawal | Class IIb, Level B | [Mueller SW et al. Pharmacotherapy 2014;34:127-135](https://pubmed.ncbi.nlm.nih.gov/23907726/) |
| Gabapentin and carbamazepine may have role in mild-moderate alcohol withdrawal | Class IIb, Level B | [Myrick H et al. Am J Psychiatry 2009;166:1025-1034](https://pubmed.ncbi.nlm.nih.gov/19487400/) |
| Alcohol withdrawal seizures are provoked/acute symptomatic seizures and do not establish a diagnosis of epilepsy | Class I | [Beghi E et al. Epilepsia 2010;51:671-675](https://pubmed.ncbi.nlm.nih.gov/19874385/) |
| Thiamine must be given before glucose to prevent precipitating Wernicke encephalopathy | Class IIa, Level C | Expert consensus; [Galvin R et al. Eur J Intern Med 2010;21:509-514](https://pubmed.ncbi.nlm.nih.gov/21111935/) |

---

## CHANGE LOG

**v1.1 (January 30, 2026)**
- Standardized all medication dosing to structured 4-field format (dose :: route :: frequency :: full_instructions) across Sections 3A, 3B, 3C for clickable order sentence support
- Added ICU column to Section 4B (Patient Instructions) for family communication coverage
- Added ICU column to Section 4C (Lifestyle & Prevention) for completeness
- Added OPD coverage for Lorazepam PO in Section 3B (medically supervised outpatient detox)
- Changed Chlordiazepoxide ED priority from "-" to URGENT (ED patients may need oral withdrawal management while awaiting admission)
- Populated empty frequency fields (3rd :: position) in all medication dosing cells
- Removed redundant summary dose text from structured dosing fields
- Corrected Dextrose 50% dose field to "25 g (50 mL)" for clarity

**v1.0 (January 30, 2026)**
- Initial template creation
- Comprehensive alcohol withdrawal seizure management across ED, HOSP, OPD, ICU
- Benzodiazepine-first approach with CIWA-Ar protocol integration
- High-dose IV thiamine protocol for Wernicke prevention
- Electrolyte management (Mg, K, Ca, Phos) emphasized
- Phenobarbital and adjunctive agents in second-line section
- Explicit documentation that phenytoin is NOT effective for withdrawal seizures
- Differential diagnosis including concurrent structural pathology (SDH)
- CIWA-Ar monitoring protocol with disposition criteria
- Evidence base with 16 PubMed-linked citations
- APPENDIX A: CIWA-Ar scoring reference

---

## APPENDIX A: CIWA-Ar (Clinical Institute Withdrawal Assessment - Revised) Quick Reference

### Scoring Overview

| Domain | Score Range | Assessment |
|--------|------------|------------|
| Nausea/vomiting | 0-7 | 0 = none; 7 = constant nausea, frequent dry heaves/vomiting |
| Tremor | 0-7 | 0 = none; 7 = severe (arms extended, fingers spread) |
| Paroxysmal sweats | 0-7 | 0 = none; 7 = drenching sweats |
| Anxiety | 0-7 | 0 = none; 7 = acute panic states |
| Agitation | 0-7 | 0 = normal activity; 7 = pacing, thrashing |
| Tactile disturbances | 0-7 | 0 = none; 7 = continuous hallucinations |
| Auditory disturbances | 0-7 | 0 = none; 7 = continuous hallucinations |
| Visual disturbances | 0-7 | 0 = none; 7 = continuous hallucinations |
| Headache/fullness | 0-7 | 0 = not present; 7 = extremely severe |
| Orientation/clouding | 0-4 | 0 = oriented; 4 = disoriented to person/place |
| **Total** | **0-67** | |

### Treatment Thresholds

| CIWA-Ar Score | Severity | Action |
|---------------|----------|--------|
| <10 | Mild | Monitor q4-8h; no pharmacotherapy needed unless rising trend |
| 10-18 | Moderate | Symptom-triggered benzodiazepines; monitor q1-2h |
| 19-20 | Moderate-Severe | Aggressive benzodiazepine dosing; consider ICU |
| >20 | Severe | ICU admission recommended; high-dose benzodiazepines; consider phenobarbital adjunct |

### Typical Symptom-Triggered Protocol

| CIWA-Ar Score | Benzodiazepine Dose (Chlordiazepoxide) | Benzodiazepine Dose (Lorazepam) |
|---------------|---------------------------------------|----------------------------------|
| 10-15 | Chlordiazepoxide 25-50 mg PO q1h PRN | Lorazepam 1 mg PO/IV q1h PRN |
| 16-20 | Chlordiazepoxide 50-100 mg PO q1h PRN | Lorazepam 2 mg PO/IV q1h PRN |
| >20 | Chlordiazepoxide 100 mg PO q1h PRN; consider IV route | Lorazepam 2-4 mg IV q1h PRN; consider phenobarbital adjunct |

---

## APPENDIX B: Alcohol Withdrawal Timeline

```
TIME AFTER LAST DRINK:

6-12 HOURS: MINOR WITHDRAWAL
├── Tremor, anxiety, headache, diaphoresis
├── Nausea, vomiting, insomnia
├── Tachycardia, hypertension
└── CIWA-Ar typically 10-20

12-24 HOURS: ALCOHOLIC HALLUCINOSIS
├── Visual, auditory, or tactile hallucinations
├── Intact sensorium (distinguishes from DTs)
└── Usually self-limited

6-48 HOURS: WITHDRAWAL SEIZURES (Peak 12-24h)
├── Generalized tonic-clonic (>90%)
├── Usually brief, self-limited
├── May occur in clusters (multiple seizures over hours)
├── ~3% progress to status epilepticus
└── RISK FACTORS: prior withdrawal seizures, kindling, low Mg

48-96 HOURS: DELIRIUM TREMENS (Peak 72h)
├── Altered sensorium (confusion, disorientation)
├── Severe autonomic instability
├── Hallucinations (visual > auditory)
├── Agitation, diaphoresis, tachycardia
├── Mortality 1-5% with treatment; up to 35% untreated
└── RISK FACTORS: prior DTs, heavy/prolonged use, older age, comorbidities
```

---

## NOTES

- Alcohol withdrawal seizures are provoked/acute symptomatic seizures; a single withdrawal seizure does NOT establish a diagnosis of epilepsy and does NOT require chronic anti-seizure medication
- However, patients with repeated withdrawal seizures (kindling) may eventually develop unprovoked seizures
- Always obtain CT head in alcoholic patients with seizures due to high rate of concurrent structural pathology (SDH, hemorrhage, trauma)
- Thiamine administration BEFORE glucose is critical to prevent precipitating Wernicke encephalopathy
- Magnesium is a required cofactor for thiamine metabolism; always check and replete Mg in conjunction with thiamine
- The CIWA-Ar protocol allows symptom-triggered therapy, which has been shown to reduce total benzodiazepine requirements and shorten treatment duration compared to fixed-schedule dosing
- Patients with prior DTs, multiple prior withdrawals, or concurrent medical illness (liver disease, infection) are at highest risk for complicated withdrawal
- Long-acting benzodiazepines (chlordiazepoxide, diazepam) are generally preferred for smoother withdrawal management; lorazepam or oxazepam are preferred in liver disease
- Phenobarbital is gaining favor as an adjunct or alternative to benzodiazepines in severe withdrawal, particularly in the ICU setting
- Discharge planning should ALWAYS include alcohol cessation resources and consideration of medication-assisted treatment (naltrexone, acamprosate, disulfiram)
