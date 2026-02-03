---
title: "Headache, Unspecified"
description: "Clinical decision support for undifferentiated headache treatment and empiric management"
version: "1.1"
setting: "ED, HOSP, OPD"
status: draft
tags:
  - headache
  - unspecified
  - undifferentiated
  - empiric-treatment
  - emergency
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Headache, Unspecified

**VERSION:** 1.1
**CREATED:** February 2, 2026
**REVISED:** February 2, 2026
**STATUS:** Revised per checker v1.1

---

**DIAGNOSIS:** Headache, Unspecified

**ICD-10:** R51.9 (Headache, unspecified), R51.0 (Headache with orthostatic component, unspecified), G44.1 (Vascular headache, not elsewhere classified), G44.89 (Other headache syndrome)

**CPT CODES:** 99281-99285 (ED E/M levels), 70450 (CT head without contrast), 70551 (MRI brain without contrast), 70553 (MRI brain with/without contrast), 85025 (CBC), 80048 (BMP), 80053 (CMP), 84443 (TSH), 83735 (magnesium), 84703 (hCG qualitative), 85652 (ESR), 86140 (CRP), 62270 (lumbar puncture), 96374 (IV push), 96365 (IV infusion), 93000 (ECG), 96372 (therapeutic injection IM/SC)

**SYNONYMS:** Headache NOS, headache not otherwise specified, undifferentiated headache, unclassified headache, cephalgia unspecified, cephalalgia NOS, head pain unspecified, acute headache NOS, nonspecific headache, headache of unknown etiology, headache under evaluation, primary headache NOS, new headache NOS, recurrent headache unspecified

**SCOPE:** Empiric treatment-focused management of undifferentiated or unspecified headache when the diagnosis is unclear, pending further evaluation, or does not fit a specific headache category. Emphasizes acute headache management in the ED and hospital (parenteral headache cocktail: ketorolac, metoclopramide, diphenhydramine, dexamethasone), empiric abortive treatment, and outpatient follow-up planning. Applies when the patient presents with headache and a definitive primary or secondary headache diagnosis has not yet been established. Differs from the Headache Evaluation plan, which focuses on the diagnostic workup algorithm. Excludes thunderclap headache (separate protocol), confirmed secondary headaches (SAH, meningitis, mass lesion), and specific primary headache disorders once diagnosed (migraine, tension-type, cluster -- see dedicated plans).

---

**DEFINITIONS:**
- **Headache, Unspecified:** Headache not yet classified into a specific primary or secondary headache disorder per ICHD-3 criteria; used when diagnosis is pending or features are atypical/overlapping
- **Undifferentiated Headache:** Clinical presentation where headache is the chief complaint but does not clearly meet diagnostic criteria for a single headache subtype at the time of evaluation
- **Headache Cocktail:** A combination of parenteral medications (typically ketorolac, dopamine antagonist, diphenhydramine, with or without dexamethasone) used empirically in the ED for acute headache regardless of subtype
- **Red Flag Headache:** Headache with features suggesting a secondary (dangerous) cause requiring urgent imaging or LP (thunderclap onset, fever, focal deficits, papilledema, altered mental status, new onset after age 50)

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test (CPT) | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC (85025) | STAT | ROUTINE | ROUTINE | - | Rule out anemia, infection, leukocytosis as headache contributor | Normal |
| BMP (80048) | STAT | ROUTINE | ROUTINE | - | Electrolyte abnormalities, renal function for NSAID safety | Normal |
| hCG qualitative - women of childbearing age (84703) | STAT | STAT | ROUTINE | - | Pregnancy status affects treatment selection (avoid NSAIDs in 3rd trimester, avoid ergotamines) | Document status |
| Magnesium (83735) | URGENT | ROUTINE | ROUTINE | - | Low magnesium associated with headache disorders; guides supplementation | >1.8 mg/dL |

### 1B. Extended Workup (Second-line)

| Test (CPT) | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------------|:--:|:----:|:---:|:---:|-----------|----------------|
| CMP (80053) | URGENT | ROUTINE | ROUTINE | - | Hepatic function for acetaminophen safety; glucose for hypoglycemia | Normal |
| TSH (84443) | - | ROUTINE | ROUTINE | - | Thyroid dysfunction can cause chronic headache | Normal (0.4-4.0 mIU/L) |
| ESR (85652) / CRP (86140) | URGENT | ROUTINE | ROUTINE | - | Rule out GCA if age >50 with new-onset headache; inflammatory cause | Normal |
| Vitamin D, 25-OH (82306) | - | ROUTINE | ROUTINE | - | Deficiency associated with chronic headache frequency | >30 ng/mL |
| Ferritin (82728) | - | ROUTINE | ROUTINE | - | Iron deficiency associated with headache | >50 ng/mL |

### 1C. Rare/Specialized (If Red Flags or Refractory)

| Test (CPT) | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------------|:--:|:----:|:---:|:---:|-----------|----------------|
| Blood cultures (87040) | STAT | STAT | - | - | Febrile headache suggesting meningitis | No growth |
| Procalcitonin (84145) | STAT | STAT | - | - | Suspected bacterial infection as cause | <0.1 ng/mL |
| ANA (86038) | - | EXT | EXT | - | Suspected autoimmune/vasculitis cause in atypical presentations | Negative |
| Lyme serology (86618) | - | EXT | EXT | - | Endemic areas with refractory or subacute headache | Negative |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study (CPT) | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT head without contrast (70450) | STAT | URGENT | - | - | Any red flag: thunderclap onset, worst headache of life, focal deficits, altered mental status, anticoagulation, age >50 new onset | No hemorrhage, mass, hydrocephalus, or midline shift | None in emergency |
| MRI brain without contrast (70551) | - | ROUTINE | ROUTINE | - | Recurrent/chronic unspecified headache, abnormal neurological exam, refractory to treatment | Normal; no structural lesion | Pacemaker, metal implants, severe claustrophobia |

### 2B. Extended

| Study (CPT) | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (70553) | - | ROUTINE | ROUTINE | - | Suspected mass, infection, or inflammation; abnormal non-contrast MRI | No enhancement, mass, or meningeal disease | Gadolinium allergy, severe renal impairment (GFR <30) |
| MRA head (70544) | URGENT | ROUTINE | ROUTINE | - | Suspected vasculopathy, aneurysm, or dissection | Normal vasculature; no aneurysm or dissection | Per MRI contraindications |
| MRV brain (70546) | URGENT | ROUTINE | EXT | - | Suspected cerebral venous thrombosis (headache with papilledema, seizure, postpartum) | Patent venous sinuses | Per MRI contraindications |
| CT angiography head/neck (70496/70498) | STAT | URGENT | - | - | Suspected dissection, aneurysm, or vasculopathy when MRA unavailable | Normal vasculature | Contrast allergy, renal impairment |
| ECG (93000) | STAT | STAT | - | - | Baseline before metoclopramide or prochlorperazine (QTc assessment) | Normal sinus rhythm; QTc <470 ms | None |

### 2C. Rare/Specialized

| Study (CPT) | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Lumbar puncture with opening pressure (62270) | URGENT | URGENT | - | - | Suspected SAH with negative CT, suspected meningitis, suspected IIH | Normal OP (10-20 cm H2O); clear CSF; WBC <5; protein 15-45; glucose >60% serum | Coagulopathy, mass lesion with risk of herniation |
| C-spine MRI (72141) | - | ROUTINE | ROUTINE | - | Suspected cervicogenic headache component | Normal cervical alignment; no disc herniation | MRI contraindications |

---

**IMAGING RED FLAGS (SNNOOP10):** Obtain imaging if any of the following present:
- **S**ystemic symptoms (fever, weight loss) or systemic disease (HIV, cancer, immunosuppression)
- **N**eurological symptoms or abnormal signs (focal deficits, papilledema)
- **N**ew onset or sudden onset (thunderclap)
- **O**nset after age 50
- **O**ther associated conditions (pregnancy, postpartum, anticoagulation)
- **P**attern change from previous headaches
- **P**ositional (worse lying down or standing)
- **P**recipitated by Valsalva (cough, sneeze, exertion)
- **P**apilledema
- **P**rogressive headache or atypical features
- **P**ainful eye with autonomic features

---

## 3. TREATMENT

### 3A. ED Empiric Headache Cocktail (First-Line Parenteral)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| IV normal saline bolus | IV | Dehydration commonly accompanies headache; empiric rehydration | 500-1000 mL :: IV :: once :: NS or LR 500-1000 mL IV bolus over 30-60 min | Heart failure, volume overload | I/O, signs of fluid overload | STAT | STAT | - | - |
| Ketorolac (CPT 96374) | IV | First-line NSAID for acute headache in ED; effective regardless of headache subtype | 30 mg :: IV :: x1 :: 30 mg IV push (15 mg if age >65, CrCl <50, or weight <50 kg); max 5 days total NSAID use | Renal impairment (CrCl <30); active GI bleed; aspirin/NSAID allergy; third trimester pregnancy; anticoagulation with high bleed risk | Renal function if repeated dosing; GI symptoms | STAT | STAT | - | - |
| Ketorolac (CPT 96372) | IM | First-line NSAID for acute headache when IV access unavailable | 60 mg :: IM :: x1 :: 60 mg IM once (30 mg if age >65, CrCl <50, or weight <50 kg); max 5 days total NSAID use | Renal impairment (CrCl <30); active GI bleed; aspirin/NSAID allergy; third trimester pregnancy; anticoagulation with high bleed risk | Renal function if repeated dosing; GI symptoms | STAT | STAT | - | - |
| Metoclopramide (CPT 96374) | IV | Anti-headache properties independent of anti-emetic effect; dopamine antagonist effective for undifferentiated headache | 10 mg :: IV :: x1 :: 10 mg IV over 15 min; repeat once in 30 min if needed; always co-administer diphenhydramine to prevent akathisia | Parkinson's disease; tardive dyskinesia history; bowel obstruction; pheochromocytoma; QTc >500 ms | Akathisia (restlessness), dystonic reaction, QTc | STAT | STAT | - | - |
| Diphenhydramine (CPT 96374) | IV | Prevents akathisia from dopamine antagonists; mild analgesic adjunct | 25 mg :: IV :: x1 :: 25 mg IV push prior to or with metoclopramide | Narrow-angle glaucoma; urinary retention; severe sedation risk (elderly) | Sedation, dry mouth | STAT | STAT | - | - |
| Dexamethasone (CPT 96374) | IV | Reduces 24-72h headache recurrence; recommended adjunct to ED headache cocktail | 10 mg :: IV :: x1 :: 10 mg IV push once (single dose) | Active untreated infection; uncontrolled diabetes (relative -- still give, monitor glucose) | Blood glucose within 4-6h | URGENT | URGENT | - | - |

### 3B. ED Empiric Headache Cocktail - Alternative Dopamine Antagonist

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Prochlorperazine (CPT 96374) | IV | Alternative to metoclopramide; preferred if stronger anti-emetic effect needed | 10 mg :: IV :: x1 :: 10 mg IV slow push over 5-10 min; co-administer diphenhydramine 25 mg IV | Parkinson's disease; QT prolongation; severe hypotension; CNS depression | QTc, akathisia, dystonia, hypotension | STAT | STAT | - | - |
| Chlorpromazine (CPT 96374) | IV | Second-line dopamine antagonist; effective for refractory acute headache | 12.5 mg :: IV :: x1 :: 12.5 mg IV in 500 mL NS over 20 min; repeat 25 mg in 30 min if needed; co-administer diphenhydramine | QT prolongation; severe hepatic disease; Parkinson's disease; CNS depression | BP (orthostatic hypotension common), QTc, sedation | URGENT | URGENT | - | - |

### 3C. Second-Line Parenteral (Refractory to Cocktail)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Magnesium sulfate (CPT 96365) | IV | Adjunct for refractory headache; particularly effective if low magnesium or suspected migraine | 2 g :: IV :: x1 :: 2 g IV in 100 mL NS over 20-30 min | Renal failure (GFR <30); myasthenia gravis; heart block | Mg levels, patellar reflexes, respiratory rate | URGENT | URGENT | - | - |
| Valproate sodium (CPT 96365) | IV | Refractory headache unresponsive to cocktail; broad-spectrum headache efficacy | 500-1000 mg :: IV :: x1 :: 500-1000 mg IV over 15-30 min | Pregnancy; hepatic disease; mitochondrial disease (POLG mutation); pancreatitis history | Ammonia, LFTs | URGENT | URGENT | - | - |
| Acetaminophen IV (CPT 96374) | IV | Alternative if NSAIDs contraindicated; NSAID allergy, renal impairment, GI bleed risk | 1000 mg :: IV :: x1 :: 1000 mg IV over 15 min; max 3000 mg/day from all sources | Severe hepatic impairment (ALT >3x ULN); chronic alcohol use (>3 drinks/day) | LFTs if repeated dosing; total daily dose from all acetaminophen sources | STAT | STAT | - | - |
| Sumatriptan (CPT 96372) | SC | Suspected migraine with uncertain diagnosis; test dose is diagnostic and therapeutic | 6 mg :: SC :: x1 :: 6 mg SC once; repeat in 2h if partial response; max 12 mg/24h | CAD, prior stroke/TIA, uncontrolled HTN, hemiplegic migraine features, pregnancy (relative), triptan within 24h, ergot within 24h | Chest tightness, BP, paresthesias | URGENT | URGENT | - | - |
| Occipital nerve block (CPT 64405) | Local injection | Refractory headache; occipital-predominant pain; avoids systemic medications | 2-3 mL :: SC :: x1 :: 2-3 mL 2% lidocaine (or 0.25% bupivacaine) with or without 40 mg triamcinolone at greater occipital nerve bilaterally | Local anesthetic allergy; infection at injection site | Immediate pain response; vasovagal reaction; local bruising | EXT | EXT | ROUTINE | - |

### 3D. Oral/Outpatient Acute Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Ibuprofen | PO | First-line oral analgesic for mild-moderate headache | 400-800 mg :: PO :: PRN :: 400-800 mg PO at onset; repeat q6-8h; max 2400 mg/day; limit to <15 days/month | Renal impairment; GI bleed history; aspirin allergy; third trimester pregnancy | GI symptoms; renal function if prolonged | URGENT | ROUTINE | ROUTINE | - |
| Naproxen sodium | PO | First-line oral NSAID; longer duration of action than ibuprofen | 500 mg :: PO :: PRN :: 500-550 mg PO at onset; repeat 250 mg in 12h if needed; max 1250 mg/day; limit to <15 days/month | Renal impairment; GI bleed history; aspirin allergy; third trimester pregnancy | GI symptoms; renal function if prolonged | URGENT | ROUTINE | ROUTINE | - |
| Acetaminophen | PO | First-line if NSAID contraindicated; mild-moderate headache | 1000 mg :: PO :: PRN :: 1000 mg PO at onset; repeat q6h; max 3000 mg/day (2000 mg if liver disease); limit to <15 days/month | Severe hepatic impairment; chronic heavy alcohol use | LFTs if chronic use; total daily dose from all sources | URGENT | ROUTINE | ROUTINE | - |
| Aspirin | PO | First-line oral analgesic; anti-inflammatory and anti-platelet | 650-1000 mg :: PO :: PRN :: 650-1000 mg PO at onset; max 4000 mg/day; limit to <15 days/month | Bleeding disorders; GI ulcer; aspirin allergy; children/teens (Reye syndrome); third trimester | GI symptoms; bleeding | URGENT | ROUTINE | ROUTINE | - |
| Acetaminophen/Aspirin/Caffeine (Excedrin) | PO | Combination analgesic with caffeine adjunct; enhanced efficacy | 2 tablets :: PO :: PRN :: 2 tablets PO at onset (acetaminophen 250 mg + aspirin 250 mg + caffeine 65 mg per tablet); max 2 doses/24h | Per component contraindications (hepatic impairment, GI bleed, aspirin allergy, bleeding disorders) | Risk of MOH with frequent use; limit to <10 days/month | - | ROUTINE | ROUTINE | - |
| Metoclopramide | PO | Nausea with headache; has independent anti-headache properties | 10 mg :: PO :: PRN :: 10 mg PO at headache onset; repeat in 8h if needed; max 30 mg/day | Parkinson's disease; tardive dyskinesia history | Akathisia; limit to <12 weeks continuous use | - | ROUTINE | ROUTINE | - |

### 3E. Pregnancy-Safe Options

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Acetaminophen | PO | First-line oral analgesic in pregnancy for any headache | 1000 mg :: PO :: q6h :: 1000 mg PO q6h; max 3000 mg/day | Hepatic disease | LFTs if frequent use | STAT | STAT | ROUTINE | - |
| Acetaminophen IV | IV | First-line parenteral analgesic in pregnancy when oral not tolerated | 1000 mg :: IV :: q6h :: 1000 mg IV over 15 min q6h; max 3000 mg/day | Hepatic disease | LFTs if frequent use | STAT | STAT | - | - |
| Metoclopramide | IV | Safe in pregnancy; anti-headache and anti-emetic | 10 mg :: IV :: q8h :: 10 mg IV q8h | Parkinson's disease | Akathisia | STAT | STAT | ROUTINE | - |
| Metoclopramide | PO | Safe in pregnancy; anti-headache and anti-emetic for outpatient use | 10 mg :: PO :: q8h :: 10 mg PO q8h | Parkinson's disease | Akathisia | - | ROUTINE | ROUTINE | - |
| Ondansetron | IV | Anti-emetic adjunct; caution in first trimester | 4 mg :: IV :: q8h :: 4 mg IV q8h | QT prolongation; first trimester (relative -- limited data) | QTc | URGENT | ROUTINE | - | - |
| Ondansetron | PO | Anti-emetic adjunct for outpatient use; caution in first trimester | 4 mg :: PO :: q8h :: 4 mg PO q8h | QT prolongation; first trimester (relative -- limited data) | QTc | - | ROUTINE | ROUTINE | - |
| Magnesium sulfate | IV | Adjunct for headache in pregnancy; also seizure prophylaxis benefit | 2 g :: IV :: x1 :: 2 g IV over 20-30 min | Renal failure; myasthenia gravis | Reflexes, respiratory rate, Mg level | URGENT | URGENT | - | - |
| Occipital nerve block (lidocaine) | Local injection | Non-systemic option; safe in pregnancy | 2-3 mL :: SC :: PRN :: 2% lidocaine 2-3 mL per side at greater occipital nerve | Local anesthetic allergy | Local reaction; vasovagal | - | ROUTINE | ROUTINE | - |

### 3F. Empiric Outpatient Bridging (Discharge from ED/Hospital)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Naproxen sodium | PO | Bridge therapy for recurrent headache pending outpatient evaluation | 500 mg :: PO :: BID :: 500 mg PO BID with food for 5-7 days; then PRN | Renal impairment; GI bleed; aspirin allergy; 3rd trimester pregnancy | GI symptoms; renal function | ROUTINE | ROUTINE | ROUTINE | - |
| Dexamethasone taper (short) | PO | Prevent headache recurrence after ED discharge; bridging for refractory cases | 4 mg :: PO :: BID :: 4 mg PO BID x 2 days, then 4 mg daily x 2 days, then stop | Active infection; uncontrolled DM | Blood glucose; insomnia; mood changes | ROUTINE | ROUTINE | ROUTINE | - |
| Prochlorperazine suppository | PR | Rescue therapy at home for recurrent nausea/headache | 25 mg :: PR :: q12h :: 25 mg PR q12h PRN; max 3 days | Parkinson's disease; QT prolongation | Akathisia; sedation | ROUTINE | ROUTINE | ROUTINE | - |
| Ondansetron ODT | PO | Anti-emetic rescue for nausea/vomiting with headache recurrence | 4 mg :: PO :: q8h :: 4 mg ODT q8h PRN | QT prolongation; severe hepatic impairment | QTc if chronic use; constipation | ROUTINE | ROUTINE | ROUTINE | - |

---

**MEDICATION OVERUSE HEADACHE WARNING:**
Limit acute analgesic use to <10 days/month for combination analgesics, opioids, or triptans, and <15 days/month for simple analgesics (NSAIDs, acetaminophen). Exceeding these thresholds risks transformation to medication overuse headache (MOH). Educate all patients at discharge. If MOH suspected, refer to medication overuse headache protocol.

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology consult if headache refractory to ED cocktail (>2 rounds) or atypical features present | URGENT | ROUTINE | - | - |
| Headache specialist/Neurology outpatient referral for recurrent unspecified headache requiring classification | - | ROUTINE | ROUTINE | - |
| Ophthalmology/Fundoscopy if papilledema suspected or visual symptoms present | URGENT | URGENT | ROUTINE | - |
| Physical therapy referral for cervicogenic or musculoskeletal component | - | - | ROUTINE | - |
| Behavioral health/Psychology referral for comorbid anxiety, depression, or stress-related headache triggers | - | ROUTINE | ROUTINE | - |
| Dentistry/TMJ specialist if jaw pain, bruxism, or temporomandibular dysfunction contributing | - | - | ROUTINE | - |
| Sleep medicine evaluation for insomnia or sleep apnea contributing to chronic headache | - | - | ROUTINE | - |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return immediately for sudden severe headache ("worst headache of life") which indicates possible hemorrhage | STAT | - | ROUTINE |
| Return immediately for headache with fever, stiff neck, or altered mental status which indicates possible infection | STAT | - | ROUTINE |
| Return if new neurological symptoms develop (weakness, numbness, vision changes, speech difficulty, seizure) | STAT | ROUTINE | ROUTINE |
| Keep headache diary tracking frequency, severity, duration, triggers, and medications to guide follow-up classification | ROUTINE | ROUTINE | ROUTINE |
| Limit acute pain medication use to no more than 10-15 days per month to prevent medication overuse headache | ROUTINE | ROUTINE | ROUTINE |
| Take acute medications early at headache onset for best efficacy rather than waiting for severe pain | ROUTINE | ROUTINE | ROUTINE |
| Follow up with PCP or neurologist within 2-4 weeks for headache classification and preventive planning | ROUTINE | ROUTINE | ROUTINE |
| Bring completed headache diary to follow-up appointment to aid diagnosis | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Maintain regular sleep schedule (7-8 hours, consistent bedtime and wake time) | - | ROUTINE | ROUTINE |
| Stay well-hydrated (at least 64 oz water daily) as dehydration commonly triggers headache | ROUTINE | ROUTINE | ROUTINE |
| Perform regular aerobic exercise (30 minutes moderate activity 5 times/week) to reduce headache frequency | - | ROUTINE | ROUTINE |
| Practice stress management (relaxation techniques, mindfulness, progressive muscle relaxation) | - | ROUTINE | ROUTINE |
| Identify and avoid personal triggers (alcohol, certain foods, weather changes, bright lights, strong smells) | - | ROUTINE | ROUTINE |
| Limit caffeine to moderate consistent intake (less than 200 mg/day) to prevent withdrawal headaches | - | ROUTINE | ROUTINE |
| Eat regular meals; do not skip meals as fasting commonly triggers headache | - | ROUTINE | ROUTINE |
| Complete ergonomic workspace assessment to reduce neck/shoulder strain for office workers | - | - | ROUTINE |
| Limit screen time and take regular breaks (20-20-20 rule: every 20 minutes, look 20 feet away for 20 seconds) | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Migraine | Unilateral, pulsating, moderate-severe intensity; nausea/vomiting; photo AND phonophobia; aggravated by physical activity; lasts 4-72h | Clinical criteria (ICHD-3); response to triptans diagnostic |
| Tension-type headache | Bilateral, pressing/tightening (non-pulsating), mild-moderate intensity; no nausea/vomiting; not worsened by activity | Clinical criteria (ICHD-3); no photophobia AND phonophobia together |
| Cluster headache | Strictly unilateral, periorbital, excruciating; ipsilateral autonomic features (tearing, rhinorrhea, ptosis, miosis); 15-180 min; circadian pattern | Clinical pattern; response to oxygen/triptans |
| Medication overuse headache | Chronic daily headache (>15 days/month); regular analgesic use >10-15 days/month for >3 months | Detailed medication diary; improves with overuse medication withdrawal |
| Subarachnoid hemorrhage | Thunderclap onset (maximal in seconds); "worst headache of life"; neck stiffness; altered mental status | CT head (sensitivity ~95% at 6h); LP for xanthochromia if CT negative |
| Meningitis/Encephalitis | Fever, neck stiffness, photophobia, altered mental status; subacute to acute onset | LP (cell count, protein, glucose, culture); blood cultures |
| Idiopathic intracranial hypertension | Positional (worse lying flat); papilledema; pulsatile tinnitus; visual obscurations; often obese young women | LP with opening pressure >25 cm H2O; MRI/MRV normal |
| Giant cell arteritis | Age >50; new headache type; scalp tenderness; jaw claudication; visual symptoms; polymyalgia | ESR/CRP markedly elevated; temporal artery biopsy |
| Cervicogenic headache | Unilateral, starts in neck, radiates frontally; triggered by neck movement or sustained posture; reduced cervical ROM | Physical exam (decreased ROM, tenderness); diagnostic nerve block |
| Cerebral venous thrombosis | Progressive headache; seizures; focal deficits; risk factors (pregnancy, OCP, thrombophilia) | MRV or CT venogram |
| Intracranial mass lesion | Progressive headache; worse in morning or with Valsalva; focal neurological signs; papilledema | MRI brain with contrast |
| Cervical artery dissection | Sudden severe unilateral headache/neck pain; ipsilateral Horner syndrome possible; history of trauma or neck manipulation | MRA or CTA neck |
| Hypertensive emergency | Severely elevated BP (>180/120); headache with encephalopathy, visual changes, end-organ damage | BP measurement; fundoscopy; renal function; urinalysis |

---

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Pain scale (0-10) | q30 min in ED; q4h inpatient; each visit OPD | Improving trend; target <4/10 for discharge | Escalate treatment per algorithm (cocktail -> second-line -> nerve block) | STAT | q4h | Each visit | - |
| Vital signs (BP, HR, T, RR) | q30 min in ED during treatment; q4h inpatient | Normal; T <38C; BP <180/110 | Address fever (infection workup); treat hypertension; tachycardia indicates pain | STAT | q4h | Each visit | - |
| Neurological exam (alertness, pupils, motor, speech) | q1h in ED; q4-8h inpatient; each visit OPD | No new focal deficits; alert and oriented | Any new deficit: urgent imaging; neurology consult | STAT | q4-8h | Each visit | - |
| ECG (if using dopamine antagonist) | Before first dose | QTc <470 ms; no acute ischemia | QTc >500 ms: avoid dopamine antagonists; use alternative | STAT | STAT | - | - |
| Headache diary (outpatient) | Continuous at home; review each visit | Decreasing frequency; classify headache pattern | Refer to neurology/headache specialist for classification and prevention | - | - | ROUTINE | - |
| Acute medication use days per month | Monthly tracking | <10 days/month (combination); <15 days/month (simple analgesics) | Counsel on MOH risk; initiate prevention; refer if MOH established | - | - | ROUTINE | - |
| Renal function (if repeated NSAIDs) | After 2+ doses ketorolac; if renal risk factors | Creatinine within normal limits | Hold NSAIDs; switch to acetaminophen | URGENT | ROUTINE | ROUTINE | - |

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home from ED | Pain controlled (NRS <4); able to tolerate PO; no red flags on history/exam/imaging; ambulatory; close follow-up arranged (PCP or neurology 2-4 weeks); MOH counseling provided; headache diary instructions given; return precautions reviewed |
| Admit to hospital (observation or floor) | Headache refractory to 2 rounds of ED cocktail; unable to tolerate PO; severe dehydration requiring prolonged IV fluids; pending further workup for red flag features; concern for secondary headache requiring LP or serial imaging |
| ICU admission | Rare for primary headache; indicated if suspected secondary cause with hemodynamic instability, altered mental status, or evolving neurological deficits pending workup |
| Outpatient neurology follow-up | Within 2-4 weeks for recurrent unspecified headache requiring formal classification; sooner (1-2 weeks) if frequent (>4 headache days/month) or disabling |
| Primary care follow-up | Within 1-2 weeks after ED visit for first-time headache; reassess response to acute treatment; determine if prevention needed |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Metoclopramide effective for acute undifferentiated headache in ED | Class I, Level A | [Friedman et al. Ann Emerg Med 2008](https://pubmed.ncbi.nlm.nih.gov/18006188/) |
| Prochlorperazine superior to placebo for acute headache | Class I, Level A | [Coppola et al. Ann Emerg Med 1995](https://pubmed.ncbi.nlm.nih.gov/7832357/) |
| Ketorolac effective for acute headache in ED | Class I, Level A | [Taggart et al. Headache 2013](https://pubmed.ncbi.nlm.nih.gov/23534872/) |
| Dexamethasone single dose reduces headache recurrence at 24-72h | Class I, Level A (meta-analysis) | [Singh et al. Acad Emerg Med 2008](https://pubmed.ncbi.nlm.nih.gov/18976336/) |
| Diphenhydramine prevents akathisia from dopamine antagonists | Class II, Level B | [Vinson et al. Ann Emerg Med 2004](https://pubmed.ncbi.nlm.nih.gov/14747823/) |
| Combination parenteral therapy (cocktail) more effective than single agents | Class II, Level B | [Orr et al. Acad Emerg Med 2016](https://pubmed.ncbi.nlm.nih.gov/26824905/) |
| IV magnesium sulfate as adjunct for acute headache | Class II, Level B | [Bigal et al. Headache 2002](https://pubmed.ncbi.nlm.nih.gov/12390681/) |
| ICHD-3 classification criteria for headache disorders | Expert Consensus | [Headache Classification Committee. Cephalalgia 2018](https://pubmed.ncbi.nlm.nih.gov/29368949/) |
| SNNOOP10 red flags for secondary headache screening | Expert Consensus | [Do et al. Neurology 2019](https://pubmed.ncbi.nlm.nih.gov/30587518/) |
| IV valproate for refractory acute headache | Class II, Level B | [Mathew et al. Headache 2009](https://pubmed.ncbi.nlm.nih.gov/19389136/) |
| Occipital nerve block for refractory headache in ED | Class II, Level B | [Afridi et al. Brain 2006](https://pubmed.ncbi.nlm.nih.gov/16330505/) |
| Chlorpromazine effective for acute headache | Class I, Level B | [Kelly et al. Emerg Med J 2009](https://pubmed.ncbi.nlm.nih.gov/19700579/) |
| Simple analgesics (acetaminophen, NSAIDs) for acute headache | Class I, Level A | [Stephens et al. Cochrane 2016](https://pubmed.ncbi.nlm.nih.gov/27306653/) |
| MOH prevalence and prevention with acute medication limits | Expert Consensus | [Diener et al. Nat Rev Neurol 2016](https://pubmed.ncbi.nlm.nih.gov/27615420/) |
| Sumatriptan SC for acute headache with suspected migraine | Class I, Level A | [Derry et al. Cochrane Review 2014](https://pubmed.ncbi.nlm.nih.gov/24865446/) |

---

## NOTES

- This plan is TREATMENT-focused for undifferentiated headache; for diagnostic algorithms and workup pathways, see the Headache Evaluation plan
- The ED headache cocktail (ketorolac + metoclopramide + diphenhydramine with or without dexamethasone) is effective regardless of headache subtype and is first-line for moderate-severe headache in the ED
- Always screen for red flags (SNNOOP10) before initiating empiric treatment; do not delay imaging for red flag headaches
- Dexamethasone single dose is added to the ED cocktail routinely as it reduces headache recurrence at 24-72 hours (NNT ~9)
- Avoid opioids for primary headache management; associated with worse outcomes, ED revisits, and medication overuse headache
- If response to sumatriptan is diagnostic of migraine, transition to the Migraine plan for ongoing management
- Instruct all patients to start a headache diary at discharge to facilitate classification at follow-up
- Medication overuse headache is the most common reason for chronic daily headache; counsel all patients on analgesic limits
- Pregnancy: acetaminophen, metoclopramide, and nerve blocks are safest options; avoid NSAIDs in third trimester, avoid ergotamines and most triptans

---

## CHANGE LOG

**v1.1 (February 2, 2026)**
- Added Section A/B structural dividers (═══) per template convention (C1)
- Added REVISED date and updated STATUS line (C2)
- Converted all hedging language to directive throughout (C3, R3): removed "consider", "may", "should"; replaced "+/-" with "with or without"
- Split dual-route medications in Section 3E into separate rows (PO and IV) for acetaminophen, metoclopramide, and ondansetron (M2, M3, M4, R4)
- Renamed "Excedrin (ASA/APAP/caffeine)" to "Acetaminophen/Aspirin/Caffeine (Excedrin)" for generic-first naming; expanded contraindications (M6, R5)
- Added IM ketorolac as separate row in Section 3A for IV-access-unavailable scenarios
- Added CPT code for occipital nerve block (64405) and sumatriptan injection (96372) in Section 3C
- Standardized route column: replaced dual routes with single route per row
- Updated SNNOOP10 callout to directive language ("Obtain imaging if any of the following present")
- Updated monitoring Section 6 language to directive ("indicates" instead of "may indicate")
- Incremented version to 1.1

**v1.0 (February 2, 2026)**
- Initial template creation
- Treatment-focused plan for undifferentiated/unspecified headache
- Comprehensive ED headache cocktail protocol (ketorolac, metoclopramide, diphenhydramine, dexamethasone)
- Alternative dopamine antagonists (prochlorperazine, chlorpromazine)
- Second-line parenteral options (magnesium, valproate, acetaminophen IV, sumatriptan, nerve block)
- Oral/outpatient acute treatment section
- Pregnancy-safe options section
- Empiric outpatient bridging therapy for discharge
- SNNOOP10 red flags for imaging decisions
- Structured dosing format for order sentence generation
- Real PubMed citations with verified PMIDs
- Differentiated from Headache Evaluation plan (diagnostic workup) by TREATMENT focus

---

## APPENDIX A: ED Headache Cocktail Administration Sequence

**Recommended Order of Administration:**

1. **Start IV access and fluids** -- NS or LR 500-1000 mL bolus
2. **ECG** -- Check QTc before dopamine antagonist (contraindicated if QTc >500 ms)
3. **Diphenhydramine 25 mg IV push** -- Give first to prevent akathisia
4. **Metoclopramide 10 mg IV over 15 min** (or prochlorperazine 10 mg IV over 5-10 min) -- Give immediately after diphenhydramine
5. **Ketorolac 30 mg IV push** (15 mg if elderly, renal impairment, or <50 kg) -- Give simultaneously with step 4
6. **Reassess at 30 minutes** -- If inadequate response, repeat metoclopramide 10 mg IV x1
7. **Dexamethasone 10 mg IV push** -- Give before discharge to reduce recurrence
8. **Reassess at 60 minutes** -- If still refractory, proceed to second-line agents (magnesium, valproate, nerve block, or sumatriptan)

**Key Reminders:**
- Always co-administer diphenhydramine with any dopamine antagonist
- Do not use ketorolac if patient received NSAIDs within 24h or has renal/GI contraindications
- Total ED ketorolac: maximum 2 doses (30 mg each, or 15 mg if dose-reduced)
- Do not combine sumatriptan with ergotamines or give within 24h of each other

---

## APPENDIX B: Headache Red Flag Mnemonics

### SNNOOP10 Criteria (Do et al. 2019)

| Red Flag | Feature | Concern |
|----------|---------|---------|
| S | Systemic symptoms/disease | Infection, malignancy, immunosuppression |
| N | Neurological signs or symptoms | Focal deficits, papilledema, meningismus |
| N | New onset or sudden onset | SAH, dissection, CVT, pituitary apoplexy |
| O | Onset after age 50 | GCA, malignancy, cerebrovascular disease |
| O | Other conditions (pregnancy, immunosuppression, anticoagulation) | CVT, PRES, secondary cause |
| P1 | Pattern change | Transformation suggests new or secondary cause |
| P2 | Positional | IIH (worse lying), low CSF pressure (worse upright) |
| P3 | Precipitated by Valsalva | Chiari malformation, posterior fossa lesion |
| P4 | Papilledema | IIH, mass lesion, CVT |
| P5 | Progressive headache | Mass, chronic meningitis, subdural |
| P6 | Painful eye with autonomic features | Trigeminal autonomic cephalalgia, cavernous sinus |

**Any positive red flag = imaging indicated (CT and/or MRI)**

---

## APPENDIX C: Headache Classification Quick Reference

This table assists with pattern recognition to guide transition from "unspecified" to a specific headache diagnosis at follow-up:

| Feature | Migraine | Tension-Type | Cluster | IIH | MOH |
|---------|----------|--------------|---------|-----|-----|
| Location | Unilateral (60%) | Bilateral | Unilateral periorbital | Diffuse/bilateral | Diffuse |
| Quality | Pulsating | Pressing/tightening | Boring/stabbing | Pressure | Variable (prior headache type) |
| Intensity | Moderate-severe | Mild-moderate | Severe-excruciating | Moderate-severe | Moderate |
| Duration | 4-72 hours | 30 min - 7 days | 15-180 minutes | Continuous | Daily/near-daily |
| Nausea/Vomiting | Common | Absent | Possible | Possible | Possible |
| Photo/Phonophobia | Both common | One at most | Absent | Absent | Variable |
| Autonomic features | Absent | Absent | Ipsilateral (tearing, rhinorrhea, ptosis) | Absent | Absent |
| Worse with activity | Yes | No | No (restless, pacing) | Worse lying flat | Variable |
| Key clue | Aura (30%); family history | Stress-related; bilateral | Circadian pattern; male predominance | Papilledema; pulsatile tinnitus; obese young women | >10-15 analgesic days/month |
