---
title: "Neuropathic Pain Management"
description: "Clinical decision support for neuropathic pain treatment across care settings"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - pain
  - peripheral-neuropathy
  - neuromuscular
  - neuropathic-pain
  - chronic-pain
  - central-pain
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Neuropathic Pain Management

**VERSION:** 1.0
**CREATED:** February 8, 2026
**REVISED:** February 8, 2026
**STATUS:** Draft

---

**DIAGNOSIS:** Neuropathic Pain

**ICD-10:** G89.29 (Other chronic pain), G89.4 (Chronic pain syndrome), G89.0 (Central pain syndrome)

**CPT CODES:** 99213-99215 (Office visit), 99281-99285 (ED visit), 64450 (Peripheral nerve block), 64555 (Peripheral nerve stimulator implant), 63650 (Spinal cord stimulator implant), 62350 (Intrathecal drug delivery implant), 64633-64636 (Radiofrequency ablation), 96372 (Therapeutic injection), 20553 (Trigger point injection), 95907-95913 (Nerve conduction studies), 36000 (IV access for infusion)

**SYNONYMS:** Neuropathic pain, nerve pain, neuralgia, central pain syndrome, thalamic pain, post-stroke pain, central post-stroke pain, diabetic neuropathic pain, painful diabetic neuropathy, post-herpetic neuralgia, PHN, chemotherapy-induced neuropathic pain, CIPN, spinal cord injury pain, SCI pain, MS-related pain, trigeminal neuralgia, painful polyneuropathy, neuropathic pain syndrome, chronic neuropathic pain

**SCOPE:** Treatment-focused plan for neuropathic pain management in adults. Covers peripheral neuropathic pain (diabetic, post-herpetic, traumatic, chemotherapy-induced) and central neuropathic pain (post-stroke, spinal cord injury, MS-related). Includes pain screening tools (DN4, LANSS), step therapy per AAN/EFNS/NeuPSIG guidelines, combination therapy strategies, opioid risk assessment, interventional options, and deprescribing guidance. Covers ED acute exacerbation, inpatient management, and outpatient chronic care. Excludes diagnostic workup for neuropathy etiology (covered in neuropathy-specific plans).

---

**DEFINITIONS:**
- **Neuropathic Pain:** Pain caused by a lesion or disease of the somatosensory nervous system; characterized by burning, shooting, electric shock-like quality, allodynia, or hyperalgesia
- **Central Pain Syndrome:** Neuropathic pain arising from a lesion or disease of the central somatosensory nervous system (e.g., post-stroke thalamic pain, spinal cord injury pain, MS-related pain)
- **Peripheral Neuropathic Pain:** Pain arising from a lesion or disease of peripheral somatosensory neurons (e.g., diabetic neuropathy, post-herpetic neuralgia, traumatic nerve injury)
- **Allodynia:** Pain due to a stimulus that does not normally provoke pain (e.g., light touch)
- **Hyperalgesia:** Increased pain from a stimulus that normally provokes pain
- **DN4 (Douleur Neuropathique 4):** 10-item screening questionnaire; score >=4/10 indicates neuropathic pain (sensitivity 83%, specificity 90%)
- **LANSS (Leeds Assessment of Neuropathic Symptoms and Signs):** 7-item tool; score >=12/24 suggests neuropathic pain
- **NRS (Numeric Rating Scale):** 0-10 pain intensity scale; 0 = no pain, 10 = worst pain imaginable
- **NNT (Number Needed to Treat):** Number of patients who need to be treated to achieve one additional good outcome (>=50% pain relief)

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (Monitoring for Treatment)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| BMP (CPT 80048) | ROUTINE | ROUTINE | ROUTINE | ROUTINE | Renal function for dose adjustment (gabapentinoids, tramadol); electrolytes | Normal eGFR; normal electrolytes |
| CBC (CPT 85025) | ROUTINE | ROUTINE | ROUTINE | ROUTINE | Baseline before carbamazepine/oxcarbazepine (agranulocytosis risk) | Normal WBC, platelets |
| Hepatic panel (CPT 80076) | - | ROUTINE | ROUTINE | - | Baseline before duloxetine, TCAs; hepatotoxicity monitoring | Normal ALT/AST/bilirubin |
| HbA1c (CPT 83036) | - | ROUTINE | ROUTINE | - | Glycemic control in diabetic neuropathic pain; treatment target | < 7.0% |
| Urine drug screen (CPT 80307) | ROUTINE | ROUTINE | ROUTINE | - | Opioid risk assessment; compliance monitoring; identify unreported substances | Consistent with prescribed medications |

### 1B. Extended Labs (Based on Treatment Selection)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| ECG (CPT 93000) | STAT | ROUTINE | ROUTINE | STAT | Baseline before TCAs (QTc prolongation risk); cardiac monitoring | QTc < 500 ms; no conduction abnormality |
| Sodium level | - | ROUTINE | ROUTINE | - | Monitor for hyponatremia with carbamazepine, oxcarbazepine, SNRIs | Na > 130 mEq/L |
| Carbamazepine level (CPT 80156) | - | ROUTINE | ROUTINE | - | Therapeutic drug monitoring for trigeminal neuralgia treatment | 4-12 mcg/mL |
| HLA-B*1502 genotype | - | EXT | ROUTINE | - | Pre-carbamazepine/oxcarbazepine in patients of Southeast Asian descent (SJS/TEN risk) | Negative |
| Lipid panel | - | - | ROUTINE | - | Metabolic monitoring with pregabalin (weight gain); cardiovascular risk | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Pain Assessment Tools (Essential)

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Numeric Rating Scale (NRS 0-10) | STAT | STAT | ROUTINE | STAT | Every encounter; q4h inpatient | Document baseline and response; target >=30% reduction | None |
| DN4 Questionnaire | ROUTINE | ROUTINE | ROUTINE | - | Initial assessment; confirm neuropathic mechanism | Score >=4/10 = neuropathic pain | None |
| LANSS Pain Scale | - | ROUTINE | ROUTINE | - | Initial assessment if DN4 equivocal | Score >=12/24 = neuropathic pain | None |
| Brief Pain Inventory (BPI) | - | ROUTINE | ROUTINE | - | Baseline and follow-up; functional impact | Document interference with ADLs | None |
| Opioid Risk Tool (ORT) | ROUTINE | ROUTINE | ROUTINE | - | Before any opioid prescribing | Low (0-3), moderate (4-7), high (>=8) | None |
| PDMP check (Prescription Drug Monitoring Program) | ROUTINE | ROUTINE | ROUTINE | - | Before prescribing controlled substances | No concerning patterns | None |

### 2B. Extended Studies (Select Cases)

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain/spinal cord | - | EXT | EXT | - | If central pain suspected (post-stroke, MS, SCI) | Identify CNS lesion correlating with pain | Pacemaker, metal |
| EMG/NCS (CPT 95907-95913) | - | - | ROUTINE | - | If neuropathy type uncertain; guide treatment selection | Characterize nerve injury pattern | None (relative: anticoagulation for needle EMG) |
| Quantitative sensory testing (QST) | - | - | EXT | - | Research; difficult-to-characterize pain | Small fiber dysfunction | None |

---

## 3. TREATMENT

### 3A. Acute Pain Exacerbation

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| IV lidocaine infusion | IV | Severe refractory neuropathic pain crisis; inpatient only | 1-3 mg/kg :: IV :: once over 30-60 min :: Infuse 1-3 mg/kg over 30-60 min; may repeat once in 24h; cardiac monitoring required | Cardiac arrhythmia, heart block, hepatic failure, seizure disorder | Continuous cardiac monitoring; BP q15min during infusion; lidocaine level if repeated | URGENT | URGENT | - | URGENT |
| Ketorolac | IV/IM | Acute exacerbation with inflammatory component; short-course only | 15 mg; 30 mg :: IV :: q6h :: 15-30 mg IV/IM q6h; max 5 days; use lowest effective dose | Renal impairment, GI bleeding, coagulopathy, age >65 (use 15 mg) | Renal function; GI symptoms | STAT | ROUTINE | - | STAT |
| Ketamine (subanesthetic) | IV | Severe refractory neuropathic pain; opioid-resistant pain crisis | 0.1-0.3 mg/kg/hr :: IV :: continuous :: 0.1-0.3 mg/kg/hr infusion; max 72h; monitor for dissociative symptoms | Uncontrolled HTN, raised ICP, psychosis, pregnancy | BP, HR, dissociative symptoms, hepatic function if >24h | - | URGENT | - | URGENT |
| Morphine (short-course crisis) | IV | Severe acute exacerbation unresponsive to non-opioid measures; bridge only | 2 mg; 4 mg :: IV :: q3-4h PRN :: 2-4 mg IV q3-4h PRN; max 48-72h; document exit plan | Respiratory depression, concurrent benzodiazepines, substance use disorder, untreated sleep apnea | Respiratory rate, sedation scale, SpO2 | STAT | URGENT | - | STAT |
| Dexamethasone (acute nerve compression) | IV | Acute nerve compression or inflammation contributing to pain | 4-10 mg :: IV :: daily :: 4-10 mg IV daily x 3-5 days; taper if >5 days | Active infection, uncontrolled diabetes | Blood glucose; GI symptoms | URGENT | ROUTINE | - | URGENT |

### 3B. First-Line Agents --- Gabapentinoids

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Gabapentin | PO | Peripheral neuropathic pain (diabetic, PHN); first-line; NNT 6.3 | 300 mg qHS; 300 mg TID; 600 mg TID; 900 mg TID; 1200 mg TID :: PO :: TID :: Start 300 mg qHS; titrate by 300 mg q3-7 days; target 1800-3600 mg/day in 3 divided doses; reduce dose if CrCl <60 | Severe renal impairment (adjust dose); history of substance use (abuse potential) | Sedation, dizziness, peripheral edema, renal function; suicidal ideation (FDA warning) | - | ROUTINE | ROUTINE | - |
| Pregabalin | PO | Peripheral neuropathic pain (diabetic, PHN, SCI); first-line; NNT 7.7 for diabetic neuropathy | 75 mg BID; 150 mg BID; 300 mg BID :: PO :: BID :: Start 75 mg BID; titrate to 150 mg BID at week 1; max 300 mg BID (600 mg/day); reduce if CrCl <60 | Severe renal impairment (adjust dose); schedule V controlled substance | Sedation, dizziness, weight gain, peripheral edema; suicidal ideation (FDA warning) | - | ROUTINE | ROUTINE | - |

### 3C. First-Line Agents --- SNRIs

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Duloxetine | PO | Diabetic neuropathic pain (FDA approved); also effective for other peripheral neuropathic pain; NNT 6.4 | 30 mg daily; 60 mg daily :: PO :: daily :: Start 30 mg daily x 1 week; increase to 60 mg daily; max 120 mg/day; take with food | Hepatic impairment, CrCl <30, concurrent MAOIs, uncontrolled narrow-angle glaucoma | BP, hepatic function, sodium, nausea, sexual dysfunction; serotonin syndrome risk with other serotonergic agents; taper over 2 weeks to discontinue | - | ROUTINE | ROUTINE | - |
| Venlafaxine XR | PO | Neuropathic pain (various types); effective at higher doses (>=150 mg); NNT 6.4 | 37.5 mg daily; 75 mg daily; 150 mg daily; 225 mg daily :: PO :: daily :: Start 37.5 mg daily x 1 week; titrate by 37.5-75 mg weekly; target 150-225 mg/day; analgesic effect requires >=150 mg | Uncontrolled HTN, concurrent MAOIs, severe hepatic/renal impairment | BP (dose-dependent HTN), sodium, serotonin syndrome risk; taper over 2-4 weeks to discontinue | - | ROUTINE | ROUTINE | - |

### 3D. First-Line Agents --- TCAs

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Amitriptyline | PO | Neuropathic pain (all types); first-line; NNT 3.6; also effective for central pain | 10 mg qHS; 25 mg qHS; 50 mg qHS; 75 mg qHS :: PO :: qHS :: Start 10-25 mg qHS; titrate by 10-25 mg q1-2 weeks; target 50-75 mg qHS; max 150 mg/day; give at bedtime | Cardiac conduction defects, recent MI, concurrent MAOIs, urinary retention, narrow-angle glaucoma, age >65 (use nortriptyline instead) | ECG before and after dose changes (QTc); anticholinergic effects (dry mouth, constipation, urinary retention); weight gain; sedation; fall risk in elderly | - | ROUTINE | ROUTINE | - |
| Nortriptyline | PO | Neuropathic pain; preferred TCA in elderly (less anticholinergic); NNT 3.6 (class) | 10 mg qHS; 25 mg qHS; 50 mg qHS; 75 mg qHS :: PO :: qHS :: Start 10 mg qHS; titrate by 10-25 mg q1-2 weeks; target 50-75 mg qHS; max 150 mg/day | Cardiac conduction defects, recent MI, concurrent MAOIs, urinary retention | ECG before and after dose changes; fewer anticholinergic effects than amitriptyline; therapeutic drug level available (target 50-150 ng/mL) | - | ROUTINE | ROUTINE | - |
| Desipramine | PO | Neuropathic pain; least sedating TCA; preferred when daytime alertness required | 25 mg daily; 50 mg daily; 75 mg daily; 100 mg daily :: PO :: daily :: Start 25 mg daily; titrate by 25 mg q1-2 weeks; target 75-100 mg/day; max 150 mg/day; may give in AM | Cardiac conduction defects, recent MI, concurrent MAOIs | ECG before and after dose changes; least anticholinergic of TCAs; may cause insomnia | - | ROUTINE | ROUTINE | - |

### 3E. Second-Line Agents

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Tramadol | PO | Neuropathic pain when first-line agents fail or as add-on; NNT 4.7 | 50 mg q6h; 100 mg q6h :: PO :: q6h :: Start 50 mg q4-6h PRN; may increase to 50-100 mg q6h; max 400 mg/day; reduce to max 200 mg/day if age >75 or CrCl <30 | Seizure disorder (lowers threshold), concurrent MAOIs/SSRIs/SNRIs (serotonin syndrome), substance use disorder | Serotonin syndrome symptoms, seizure risk, constipation; schedule IV controlled substance; PDMP check required; naloxone co-prescription if risk factors | - | ROUTINE | ROUTINE | - |
| Lidocaine 5% patch (Lidoderm) | Topical | Localized peripheral neuropathic pain (PHN, focal neuropathy); NNT 4.4 for PHN | 1-3 patches :: topical :: 12h on/12h off :: Apply up to 3 patches to painful area; 12 hours on, 12 hours off; may cut to size | Allergy to local anesthetics; avoid on broken skin | Skin irritation; minimal systemic absorption; safe in elderly | - | ROUTINE | ROUTINE | - |
| Capsaicin 8% patch (Qutenza) | Topical | Post-herpetic neuralgia (FDA approved); localized peripheral neuropathic pain; NNT 10.6 | 1-4 patches :: topical :: q3 months :: Apply to painful area for 60 min (feet: 30 min); in-clinic procedure; pretreat with topical anesthetic; repeat q3 months | Allergy to capsaicin; avoid on face; avoid broken skin | Application-site pain/erythema (expected); BP monitoring during application; transient pain flare; use nitrile gloves | - | - | ROUTINE | - |
| Carbamazepine | PO | Trigeminal neuralgia (first-line for TN); NNT 1.7 for TN | 100 mg BID; 200 mg BID; 400 mg BID; 600 mg BID :: PO :: BID :: Start 100 mg BID; titrate by 100-200 mg q3-7 days; target 400-1200 mg/day; use controlled-release formulation when available | HLA-B*1502 positive, bone marrow suppression, hepatic porphyria, concurrent MAOIs | CBC q2 weeks x 2 months then q3 months (agranulocytosis); sodium (hyponatremia); LFTs; drug level (4-12 mcg/mL); drug interactions (CYP3A4 inducer) | - | ROUTINE | ROUTINE | - |
| Oxcarbazepine | PO | Trigeminal neuralgia (alternative to carbamazepine); fewer drug interactions | 150 mg BID; 300 mg BID; 600 mg BID; 900 mg BID :: PO :: BID :: Start 150 mg BID; titrate by 150-300 mg weekly; target 600-1800 mg/day | HLA-B*1502 positive, severe hyponatremia | Sodium q2 weeks initially then q3 months (higher hyponatremia risk than carbamazepine); fewer drug interactions than carbamazepine | - | ROUTINE | ROUTINE | - |

### 3F. Third-Line/Refractory Agents

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Tapentadol ER | PO | Refractory neuropathic pain; dual mechanism (mu-opioid agonist + NRI); NNT 10.2 | 50 mg BID; 100 mg BID; 150 mg BID; 250 mg BID :: PO :: BID :: Start 50 mg BID; titrate by 50 mg BID q3 days; max 500 mg/day; do not crush ER tablets | Severe respiratory depression, concurrent MAOIs, GI obstruction, substance use disorder | Respiratory rate, sedation, constipation; schedule II controlled; PDMP check; naloxone co-prescription | - | - | ROUTINE | - |
| Buprenorphine transdermal (Butrans) | Transdermal | Refractory neuropathic pain; partial mu-agonist; lower abuse potential; safer respiratory profile | 5 mcg/hr; 10 mcg/hr; 20 mcg/hr :: transdermal :: weekly :: Start 5 mcg/hr patch; apply q7 days; titrate q72h by one patch strength; max 20 mcg/hr | Severe respiratory depression, long QT, concurrent full opioid agonists (block effect) | Respiratory rate, QTc, sedation; ceiling effect on respiratory depression; partial agonist (precipitate withdrawal if on full agonist) | - | - | ROUTINE | - |
| Lamotrigine | PO | Central neuropathic pain (post-stroke, SCI, HIV neuropathy); third-line for peripheral neuropathic pain | 25 mg daily; 50 mg daily; 100 mg daily; 200 mg daily; 400 mg daily :: PO :: daily-BID :: Start 25 mg daily x 2 weeks; then 50 mg daily x 2 weeks; then 100 mg daily; titrate slowly to 200-400 mg/day; halve titration rate with valproate | SJS/TEN risk (slow titration mandatory), hepatic impairment | Rash (discontinue immediately if suspected SJS); very slow titration mandatory; therapeutic range 3-14 mcg/mL for seizures (pain target uncertain) | - | ROUTINE | ROUTINE | - |
| Mexiletine | PO | Refractory peripheral neuropathic pain; oral sodium channel blocker; evidence limited | 150 mg TID; 200 mg TID; 300 mg TID :: PO :: TID :: Start 150 mg daily with food; titrate by 150 mg q3 days; target 150-300 mg TID; max 1200 mg/day | Cardiac arrhythmia, second/third-degree heart block, cardiogenic shock | ECG before initiation and with dose changes; GI side effects common; hepatic function; drug interactions with CYP1A2 inhibitors | - | - | EXT | - |
| Methadone | PO | Refractory neuropathic pain; NMDA antagonist properties; long-acting; low cost | 2.5 mg BID; 5 mg BID; 10 mg BID :: PO :: BID-TID :: Start 2.5 mg BID-TID; titrate slowly q5-7 days; highly variable pharmacokinetics; specialist prescribing recommended | QTc >500 ms, severe respiratory depression, concurrent benzodiazepines (relative), substance use disorder | ECG at baseline, 30 days, annually (QTc); respiratory rate; variable half-life (8-59h) requires careful titration; deaths from accumulation; PDMP check | - | - | EXT | - |
| Oxycodone CR (last resort) | PO | Severe refractory neuropathic pain failing all other options; documented risk assessment | 10 mg BID; 20 mg BID :: PO :: BID :: Start 10 mg BID; lowest effective dose; re-evaluate q1-3 months; mandatory opioid agreement; combine with non-opioid regimen | Active substance use disorder, concurrent benzodiazepines, untreated sleep apnea | PDMP check q3 months; UDS q3-6 months; functional assessment; naloxone co-prescription mandatory; opioid agreement mandatory; document risk-benefit at each visit | - | - | EXT | - |

### 3G. Topical Agents

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Lidocaine 5% patch (Lidoderm) | Topical | Localized peripheral neuropathic pain; first-line topical; see also 3E | 1-3 patches :: topical :: 12h on/12h off :: Apply up to 3 patches for 12h on/12h off; may cut to fit | Allergy to local anesthetics | Local skin irritation; minimal systemic absorption | - | ROUTINE | ROUTINE | - |
| Capsaicin 0.075% cream | Topical | Localized neuropathic pain; OTC option; depletes substance P | Apply QID :: topical :: QID :: Apply thin layer to painful area 3-4 times daily; burning sensation decreases with regular use over 1-2 weeks; wash hands after application | Allergy to capsaicin; open wounds | Application-site burning (expected first 1-2 weeks); avoid mucous membranes and eyes; use gloves | - | ROUTINE | ROUTINE | - |
| Compounding cream (gabapentin/ketamine/lidocaine) | Topical | Localized neuropathic pain refractory to single-agent topicals; limited evidence | Apply BID-TID :: topical :: BID-TID :: Apply to affected area BID-TID; formulation varies by compounding pharmacy; typical: gabapentin 6%/ketamine 10%/lidocaine 5% | Allergy to components | Local irritation; limited systemic absorption; insurance coverage often denied; evidence base limited | - | - | EXT | - |

### 3H. Interventional Therapies

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Spinal cord stimulation (SCS) | Implant | CRPS, failed back surgery syndrome, painful diabetic neuropathy (FDA approved); refractory to >=2 pharmacologic agents | N/A :: implant :: continuous :: Trial period (5-7 days) followed by permanent implant if >=50% pain relief; multiple waveform options (tonic, burst, HF10, DTM) | Active infection, coagulopathy, psychiatric instability, patient unable to manage device | Pain relief (NRS), functional status, device interrogation q6-12 months; trial success defined as >=50% pain reduction | - | ROUTINE | ROUTINE | - |
| Dorsal root ganglion (DRG) stimulation | Implant | CRPS type I/II, focal neuropathic pain (groin, foot, knee); superior to SCS for focal pain | N/A :: implant :: continuous :: Trial period followed by permanent implant; targets specific DRG levels | Active infection, coagulopathy; not MRI conditional for all systems | Pain scores, functional assessment, device checks; higher precision for focal pain vs. traditional SCS | - | ROUTINE | ROUTINE | - |
| Peripheral nerve stimulation (PNS) | Implant | Focal peripheral nerve injury pain; post-surgical neuropathic pain; occipital neuralgia | N/A :: implant :: continuous :: Percutaneous or surgical lead placement; trial then permanent; 60-day temporary PNS systems available | Active infection, coagulopathy | Pain relief, functional status; newer percutaneous systems allow office-based trials | - | ROUTINE | ROUTINE | - |
| Intrathecal drug delivery (ITDD) | Implant | Severe refractory neuropathic pain; failed SCS or not a candidate; cancer-related neuropathic pain | N/A :: implant :: continuous :: Intrathecal trial (bolus or catheter) before permanent pump; ziconotide (first-line intrathecal for neuropathic pain); morphine/hydromorphone (second-line); baclofen for spasticity-related pain | Active infection, coagulopathy, CSF obstruction, psychosis (ziconotide) | Pump refills q1-6 months; drug levels; infection surveillance; catheter integrity; ziconotide: CK levels, psychiatric symptoms | - | ROUTINE | ROUTINE | - |
| Peripheral nerve block (diagnostic/therapeutic) | Injection | Focal peripheral neuropathic pain; diagnostic localization; bridge during medication titration | N/A :: injection :: per protocol :: Ultrasound-guided; bupivacaine 0.25-0.5% with or without dexamethasone; repeat q2-4 weeks if effective | Allergy to local anesthetics, infection at site, coagulopathy | Pain relief duration; infection signs; motor block (transient); nerve injury (rare) | URGENT | ROUTINE | ROUTINE | - |

### 3I. Central Pain Syndrome Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Lamotrigine (central pain) | PO | Central post-stroke pain (first-line); SCI pain; NNT 5.9 for central pain | 25 mg daily; 50 mg daily; 100 mg daily; 200 mg daily :: PO :: daily-BID :: Start 25 mg daily; titrate by 25 mg q2 weeks; target 200 mg/day; see 3F for full titration | SJS/TEN risk; hepatic impairment | Rash surveillance; very slow titration mandatory | - | ROUTINE | ROUTINE | - |
| Amitriptyline (central pain) | PO | Central post-stroke pain; SCI pain; first-line TCA for central pain | 10 mg qHS; 25 mg qHS; 50 mg qHS; 75 mg qHS :: PO :: qHS :: Start 10-25 mg qHS; titrate by 10-25 mg q1-2 weeks; target 50-75 mg/day; see 3D for full details | See 3D | ECG; anticholinergic effects; see 3D | - | ROUTINE | ROUTINE | - |
| Pregabalin (SCI pain) | PO | Spinal cord injury pain (Level A evidence); central neuropathic pain | 75 mg BID; 150 mg BID; 300 mg BID :: PO :: BID :: Start 75 mg BID; titrate to 150-300 mg BID; max 600 mg/day; see 3B for full details | See 3B | Sedation, edema, weight gain; see 3B | - | ROUTINE | ROUTINE | - |
| Gabapentin (SCI pain) | PO | Spinal cord injury pain; central neuropathic pain; alternative to pregabalin | 300 mg TID; 600 mg TID; 900 mg TID; 1200 mg TID :: PO :: TID :: Start 300 mg qHS; titrate by 300 mg q3-7 days; target 1800-3600 mg/day; see 3B for full details | See 3B | See 3B | - | ROUTINE | ROUTINE | - |
| Nabiximols (Sativex) or medical cannabis (where legal) | PO/Spray | MS-related central neuropathic pain; refractory SCI pain; jurisdiction-dependent | Varies :: oromucosal spray or PO :: BID-TID :: Nabiximols: start 1 spray BID; titrate by 1 spray/day; max 12 sprays/day; or oral cannabis per state protocol | Psychosis, unstable cardiac disease, pregnancy, age <25 (brain development) | Psychiatric symptoms, cognitive function, dizziness; legal status varies; limited evidence base; not FDA-approved for pain in US | - | - | EXT | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Clinical Rationale |
|----------------|:--:|:----:|:---:|:---:|-------------------|
| Pain medicine specialist | - | ROUTINE | ROUTINE | - | Refractory pain failing >=2 first-line agents; interventional procedure candidacy; opioid management |
| Neurology | ROUTINE | ROUTINE | ROUTINE | ROUTINE | Neuropathy characterization; central pain workup; treatment optimization |
| Psychiatry/Psychology | - | ROUTINE | ROUTINE | - | Comorbid depression/anxiety (present in >50% of chronic pain patients); CBT for pain; opioid risk assessment |
| Physical therapy | - | ROUTINE | ROUTINE | - | Desensitization therapy; TENS; graded motor imagery; functional restoration |
| Addiction medicine | - | ROUTINE | ROUTINE | - | Substance use disorder identified; opioid use disorder risk; buprenorphine transition |
| Palliative care | - | ROUTINE | ROUTINE | - | Cancer-related neuropathic pain; refractory pain with functional decline; goals of care |
| Interventional pain specialist | - | - | ROUTINE | - | SCS/DRG candidacy; intrathecal pump evaluation; nerve block procedures |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD | Rationale |
|----------------|:--:|:----:|:---:|-----------|
| Pain diary (NRS, triggers, functional impact) | ROUTINE | ROUTINE | ROUTINE | Tracks treatment response; identifies patterns; guides medication adjustment |
| Set realistic expectations: goal is >=30% pain reduction and improved function, not zero pain | ROUTINE | ROUTINE | ROUTINE | Prevents treatment frustration; aligns goals with achievable outcomes |
| Medication adherence: take scheduled medications regularly even when pain is low | - | ROUTINE | ROUTINE | Preventive effect requires steady-state levels; PRN use alone is less effective |
| Do not abruptly stop gabapentinoids, SNRIs, or TCAs (taper required) | ROUTINE | ROUTINE | ROUTINE | Withdrawal seizures (gabapentinoids); discontinuation syndrome (SNRIs); cardiac risk (TCAs) |
| Opioid safety counseling: store securely, no sharing, disposal of unused medication, naloxone training | ROUTINE | ROUTINE | ROUTINE | Prevent diversion, accidental ingestion, overdose death; mandatory for opioid prescriptions |
| Naloxone (Narcan) co-prescription: obtain and keep accessible if receiving any opioid | ROUTINE | ROUTINE | ROUTINE | Reverses opioid overdose; FDA recommends co-prescribing with all opioid prescriptions |
| Avoid alcohol and sedatives with CNS-depressant medications | ROUTINE | ROUTINE | ROUTINE | Additive CNS depression with gabapentinoids, opioids, TCAs; respiratory depression risk |
| Return to ED for sudden severe pain escalation, new weakness, bowel/bladder dysfunction | ROUTINE | ROUTINE | ROUTINE | May indicate new neurologic emergency (cord compression, cauda equina) |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD | Rationale |
|----------------|:--:|:----:|:---:|-----------|
| Regular aerobic exercise (walking, swimming, cycling) 30 min x 5 days/week | - | - | ROUTINE | Level A evidence for pain reduction; improves endogenous pain modulation; reduces comorbid depression |
| Cognitive behavioral therapy (CBT) for chronic pain | - | - | ROUTINE | Level A evidence as adjunct; reduces pain catastrophizing; improves coping and function |
| Sleep hygiene optimization | - | ROUTINE | ROUTINE | Poor sleep amplifies pain perception; sleep disorders common in chronic pain; may reduce medication needs |
| Glycemic control optimization (diabetic neuropathic pain) | - | ROUTINE | ROUTINE | Prevents neuropathy progression; HbA1c <7% associated with reduced pain severity |
| Smoking cessation | - | ROUTINE | ROUTINE | Smoking worsens neuropathy and pain perception; impairs microvascular circulation |
| Weight management | - | - | ROUTINE | Reduces mechanical nerve compression; improves metabolic syndrome; enhances mobility |
| Mindfulness-based stress reduction (MBSR) | - | - | ROUTINE | Moderate evidence for chronic pain; reduces pain unpleasantness; complements pharmacotherapy |

### 4D. Combination Therapy Strategies

| Combination | Evidence | Monitoring Notes |
|-------------|----------|-----------------|
| Gabapentinoid + SNRI (e.g., gabapentin + duloxetine) | Level A; superior to monotherapy in COMBO-DN trial | Additive sedation; monitor for dizziness, falls |
| Gabapentinoid + TCA (e.g., pregabalin + nortriptyline) | Level B; effective but requires cardiac monitoring | ECG at baseline and with TCA dose changes; additive sedation and anticholinergic effects |
| TCA + topical (e.g., amitriptyline + lidocaine patch) | Level C; reasonable for localized pain with sleep disruption | Minimal systemic interaction; monitor anticholinergic burden |
| SNRI + topical (e.g., duloxetine + capsaicin 8% patch) | Level C; practical combination for localized + diffuse pain | Minimal interaction; SNRI provides systemic coverage |
| Gabapentinoid + tramadol | Level B; short-term combination data | Seizure threshold lowering (additive); sedation; limit tramadol duration |
| Do NOT combine: TCA + SNRI | Contraindicated; serotonin syndrome risk; excessive norepinephrine effect | If switching, allow adequate washout period |

### 4E. Deprescribing Guidance

| Scenario | Strategy | Timeline |
|----------|----------|----------|
| Ineffective medication (no response after adequate trial at therapeutic dose) | Taper and discontinue; document lack of efficacy | Gabapentinoids: taper over 1-2 weeks; SNRIs: taper over 2-4 weeks; TCAs: taper over 2-4 weeks |
| Opioid reduction for stable chronic neuropathic pain | Optimize non-opioid regimen first; reduce opioid by 10% of total daily dose q2-4 weeks | 10% reduction q2-4 weeks; slower if withdrawal symptoms; pause taper if pain significantly worsens |
| Opioid rotation (inadequate relief or intolerable side effects) | Calculate morphine milligram equivalents (MME); convert at 50-75% of equianalgesic dose; cross-tolerance incomplete | Complete transition over 3-7 days; close monitoring during rotation |
| Polypharmacy reduction (patient on >3 pain medications) | Eliminate least effective agent first; maintain agents with dual benefit (e.g., SNRI for pain + depression) | One change at a time; reassess in 2-4 weeks before next change |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Nociceptive pain (inflammatory, mechanical) | Aching/throbbing quality; localized to joint/tissue; responds to NSAIDs; no burning/electric quality | DN4 <4; responds to anti-inflammatory agents; normal nerve exam |
| Fibromyalgia | Widespread pain (not dermatomal); fatigue; cognitive dysfunction; tender points; no nerve distribution | ACR criteria; DN4 often <4; normal NCS/EMG; normal neurologic exam |
| Vascular pain (ischemic) | Claudication pattern; pallor/cyanosis; diminished pulses; worsens with exertion | ABI (ankle-brachial index); vascular duplex; angiography |
| Radiculopathy | Dermatomal distribution; worsens with Valsalva; positive straight leg raise; motor/reflex changes | MRI spine; EMG/NCS; dermatomal pain pattern |
| Complex regional pain syndrome (CRPS) | Limb edema, color/temperature changes, trophic changes; disproportionate to inciting event; Budapest criteria | Budapest diagnostic criteria; bone scan (early); no specific lab test |
| Psychogenic pain / somatic symptom disorder | Non-anatomical distribution; inconsistent exam; significant psychosocial stressors; does not follow neurologic patterns | Psychiatric evaluation; normal investigations; DN4 <4; diagnosis of exclusion |
| Myofascial pain | Trigger points; taut bands; referred pain patterns; responds to trigger point injection | Physical examination; trigger point identification; normal NCS/EMG |
| Phantom limb pain | Post-amputation; pain felt in absent limb; burning/cramping quality | History of amputation; clinical diagnosis |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Pain intensity (NRS 0-10) | STAT | q4-8h | Every visit | q4h | Per setting | >=30% reduction from baseline | Adjust regimen; consider escalation or combination therapy |
| Functional assessment (BPI interference, ADL status) | - | Weekly | Every visit | - | q1-3 months | Improved or stable function | Reassess treatment goals; consider rehabilitation referral |
| PDMP check | ROUTINE | At admission | Every visit with controlled substance | ROUTINE | Before each controlled substance prescription | No concerning patterns (multiple prescribers, escalating doses) | Address directly; consider addiction medicine referral |
| Urine drug screen | ROUTINE | At admission if on opioids | q3-6 months if on opioids | ROUTINE | q3-6 months for opioid patients | Consistent with prescribed; negative for illicit | Discuss discrepancies; adjust treatment plan; consider taper |
| Sedation assessment (Pasero scale or similar) | STAT | q4h if on opioids | Every visit | q2h | Per setting | Alert and oriented; no excessive sedation | Hold opioid dose; reduce; naloxone if severe |
| Renal function (eGFR) | ROUTINE | Weekly | q6-12 months | ROUTINE | Based on agent | Normal for gabapentinoid/tramadol dosing | Adjust doses per renal dosing guidelines |
| ECG (QTc) | STAT | After TCA dose change | At TCA initiation and dose changes; q6-12 months on methadone | STAT | Per agent | QTc <500 ms | Reduce dose or switch agent if QTc prolonged |
| CBC (if on carbamazepine/oxcarbazepine) | - | Weekly x 2 months | q3 months | - | q3 months after initial period | Normal WBC and platelets | Hold and consult hematology if WBC <3000 or ANC <1500 |
| Sodium (if on carbamazepine, oxcarbazepine, or SNRIs) | - | Weekly | q3 months | - | q3 months | Na >130 mEq/L | Reduce dose or switch agent; fluid restriction if mild |
| Weight and metabolic parameters (pregabalin, TCAs) | - | - | q3-6 months | - | q3-6 months | Stable weight; no metabolic syndrome | Dietary counseling; consider switch if >7% weight gain |
| Suicidal ideation screening (PHQ-9 item 9) | ROUTINE | Weekly | Every visit | ROUTINE | Every encounter | No suicidal ideation | Psychiatric referral; safety plan; adjust medications |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge from ED | Acute exacerbation managed; pain at tolerable level; no new neurologic deficits; oral medications effective; reliable follow-up within 1-2 weeks |
| Admit to hospital | Pain crisis unresponsive to oral medications; IV infusion required (lidocaine, ketamine); new neurologic deficits requiring workup; suicidal ideation related to pain; opioid complications |
| ICU admission | IV ketamine infusion requiring close monitoring; hemodynamic instability; respiratory depression from opioids; severe autonomic instability |
| Pain clinic referral | Chronic neuropathic pain failing >=2 first-line agents; interventional procedure candidate; complex medication management; opioid taper guidance |
| Outpatient neurology follow-up | New neuropathic pain diagnosis; treatment optimization; neuropathy characterization needed; central pain syndrome management |
| Addiction medicine referral | Opioid use disorder identified; aberrant drug behaviors; PDMP or UDS concerns; buprenorphine transition candidacy |
| Physical therapy/rehabilitation | Functional limitation from pain; desensitization therapy; TENS trial; graded exercise program |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| NeuPSIG pharmacotherapy guidelines: gabapentinoids, SNRIs, TCAs as first-line | Strong recommendation; Level A | [Finnerup NB et al. Lancet Neurol 2015;14(2):162-173](https://pubmed.ncbi.nlm.nih.gov/25575710/) |
| EFNS guidelines on neuropathic pain pharmacotherapy | Class I-II evidence | [Attal N et al. Eur J Neurol 2010;17(9):1113-e88](https://pubmed.ncbi.nlm.nih.gov/20402746/) |
| AAN guidelines for painful diabetic neuropathy treatment | Level A-B recommendations | [Bril V et al. Neurology 2011;76(20):1758-1765](https://pubmed.ncbi.nlm.nih.gov/21482920/) |
| Combination pharmacotherapy for neuropathic pain | Level A for gabapentinoid + SNRI | [Gilron I et al. CMAJ 2006;174(10):1411-1414](https://pubmed.ncbi.nlm.nih.gov/16682708/) |
| Canadian guidelines for neuropathic pain management | Consensus guidelines | [Moulin DE et al. Pain Res Manag 2014;19(6):328-335](https://pubmed.ncbi.nlm.nih.gov/25479151/) |
| Gabapentin for neuropathic pain in adults (Cochrane) | NNT 6.3 for >=50% pain relief | [Wiffen PJ et al. Cochrane Database Syst Rev 2017;6:CD007938](https://pubmed.ncbi.nlm.nih.gov/28597471/) |
| Duloxetine for painful neuropathy (Cochrane) | NNT 6.4 for >=50% pain relief | [Lunn MP et al. Cochrane Database Syst Rev 2014;1:CD007115](https://pubmed.ncbi.nlm.nih.gov/24385423/) |
| Pregabalin for neuropathic pain (Cochrane) | NNT 7.7 for diabetic neuropathy | [Derry S et al. Cochrane Database Syst Rev 2019;1:CD007076](https://pubmed.ncbi.nlm.nih.gov/30673120/) |
| Lamotrigine for central post-stroke pain | Moderate evidence | [Vestergaard K et al. Neurology 2001;56(2):184-190](https://pubmed.ncbi.nlm.nih.gov/11160953/) |
| Spinal cord stimulation for diabetic neuropathic pain | RCT evidence; superior to best medical therapy | [de Vos CC et al. BMJ 2014;348:g1799](https://pubmed.ncbi.nlm.nih.gov/24803311/) |
| Capsaicin 8% patch for neuropathic pain (Cochrane) | NNT 10.6 for PHN | [Derry S et al. Cochrane Database Syst Rev 2017;1:CD007393](https://pubmed.ncbi.nlm.nih.gov/28085183/) |
| Opioid guidelines for chronic non-cancer pain (CDC 2022) | Guideline recommendation | [Dowell D et al. MMWR Recomm Rep 2022;71(3):1-95](https://pubmed.ncbi.nlm.nih.gov/36327391/) |
| IV lidocaine for neuropathic pain | Moderate evidence | [Moulin DE et al. Can J Anaesth 2021;68(2):178-188](https://pubmed.ncbi.nlm.nih.gov/33108635/) |

---

## NOTES

- Neuropathic pain affects 7-10% of the general population; frequently underdiagnosed and undertreated
- DN4 questionnaire is the most validated screening tool (>=4/10 = neuropathic pain; 83% sensitivity, 90% specificity)
- Number needed to treat (NNT) values reflect >=50% pain reduction; NNT <10 is considered clinically meaningful
- First-line agents (gabapentinoids, SNRIs, TCAs) have comparable efficacy; selection guided by comorbidities, side effect profile, and patient preference
- TCAs have lowest NNT (~3.6) but highest side effect burden; avoid in elderly, cardiac disease, urinary retention
- Adequate trial = therapeutic dose for >=4-8 weeks before declaring failure
- Combination therapy is often necessary; best evidence for gabapentinoid + SNRI (COMBO-DN trial)
- Opioids are third-line only after adequate trials of >=2 first-line agents; always document risk assessment (ORT, PDMP, UDS)
- Central pain syndromes (post-stroke, SCI) may respond differently than peripheral neuropathic pain; lamotrigine has best evidence for post-stroke pain
- Interventional options (SCS, DRG stimulation) should be considered before chronic opioid therapy when appropriate
- Always assess and treat comorbid depression and anxiety, which amplify pain perception and impair treatment response
- Deprescribing is as important as prescribing: regularly reassess and discontinue ineffective agents

---

## CHANGE LOG

**v1.0 (February 8, 2026)**
- Initial plan creation
- NeuPSIG, AAN, EFNS guideline-based treatment algorithm
- Step therapy: first-line (gabapentinoids, SNRIs, TCAs), second-line (tramadol, topicals, carbamazepine), third-line (opioids, lamotrigine, interventional)
- Central pain syndrome treatment section included
- Opioid risk assessment and deprescribing guidance incorporated
- Combination therapy strategies and contraindicated combinations documented
- 13 evidence references with PubMed links
