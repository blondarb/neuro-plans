---
title: "Idiopathic Intracranial Hypertension (IIH)"
description: "Clinical decision support for idiopathic intracranial hypertension diagnosis and management"
version: "1.0"
setting: "HOSP, OPD, ICU"
status: approved
tags:
  - cerebrovascular
  - headache
  - neurodegenerative
  - demyelinating
  - infectious
---

# Idiopathic Intracranial Hypertension (IIH)

**VERSION:** 1.0
**CREATED:** January 29, 2026
**REVISED:** January 29, 2026
**STATUS:** Approved

---

**DIAGNOSIS:** Idiopathic Intracranial Hypertension

**ICD-10:** G93.2 (Benign intracranial hypertension), G93.5 (Compression of brain)

**CPT CODES:** 85025 (CBC), 80053 (CMP), 84443 (TSH), 84703 (Pregnancy test), 89051 (CSF cell count), 84157 (CSF protein), 82945 (CSF glucose), 88104 (Cytology), 70553 (MRI brain with and without contrast + MRV), 70450 (CT head (if MRI unavailable)), 92134 (Optical coherence tomography (OCT)), 92250 (Fundus photography), 62272 (Large-volume LP), 96374 (High-dose IV acetazolamide), 96365 (IV steroids (controversial))

**SYNONYMS:** Idiopathic intracranial hypertension, IIH, pseudotumor cerebri, PTC, benign intracranial hypertension, BIH, primary intracranial hypertension

**SCOPE:** Evaluation and management of idiopathic intracranial hypertension in adults including diagnosis, medical management, and surgical interventions. Applies to ED, hospital, and outpatient settings. Excludes secondary causes of elevated ICP.

---

**DEFINITIONS:**
- **Idiopathic Intracranial Hypertension (IIH):** Syndrome of elevated ICP (≥25 cm H2O in adults) with no identifiable cause, normal CSF composition, and normal neuroimaging except signs of elevated ICP
- **Papilledema:** Optic disc swelling due to elevated ICP; bilateral in most cases
- **Visual Field Defects:** Enlarged blind spot (most common), peripheral constriction, central/cecocentral scotoma (severe)
- **Fulminant IIH:** Rapid visual decline over days to weeks; requires urgent intervention
- **Frisen Scale:** Grading system for papilledema (0-5); 0=normal, 5=severe with obscured vessels
- **Transverse Sinus Stenosis:** Common imaging finding; may be cause or effect of elevated ICP

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

---

## 1. LABORATORY WORKUP

### 1A. Core Labs (Rule Out Secondary Causes)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC (CPT 85025) | ROUTINE | ROUTINE | ROUTINE | ROUTINE | Anemia (can cause papilledema); baseline | Normal |
| CMP (CPT 80053) | ROUTINE | ROUTINE | ROUTINE | ROUTINE | Renal function (for acetazolamide); electrolytes | Normal |
| TSH (CPT 84443) | - | ROUTINE | ROUTINE | - | Hypothyroidism/hyperthyroidism can cause ICP | Normal |
| Vitamin A level | - | ROUTINE | ROUTINE | - | Hypervitaminosis A | Normal |
| Pregnancy test (CPT 84703) | ROUTINE | ROUTINE | ROUTINE | - | Pregnancy considerations for treatment | Document |

### 1B. CSF Analysis (Diagnostic LP)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Opening pressure | STAT | STAT | ROUTINE | - | Diagnostic criterion; ≥25 cm H2O in adults | Elevated (≥25 cm H2O) |
| CSF cell count (CPT 89051) | STAT | STAT | ROUTINE | - | Rule out meningitis | Normal (≤5 WBC/μL) |
| CSF protein (CPT 84157) | STAT | STAT | ROUTINE | - | Rule out meningitis, malignancy | Normal (≤45 mg/dL) |
| CSF glucose (CPT 82945) | STAT | STAT | ROUTINE | - | Rule out infection | Normal (>60% serum) |
| Cytology (CPT 88104) | - | ROUTINE | EXT | - | If malignancy suspected | Negative |
| Cultures | ROUTINE | ROUTINE | - | - | If infection suspected | Negative |

### 1C. Extended Labs (If Secondary Cause Suspected)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Iron studies | - | ROUTINE | ROUTINE | - | Iron deficiency anemia associated | Normal |
| Cortisol (AM or stimulation test) | - | - | EXT | - | Adrenal insufficiency; steroid withdrawal | Normal |
| ANA, dsDNA (CPT 86235, 86225) | - | - | EXT | - | SLE (cerebral venous thrombosis risk) | Negative |
| Hypercoagulability panel | - | ROUTINE | EXT | - | If venous sinus thrombosis suspected | Normal |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Neuroimaging (Required Before LP)

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast + MRV (CPT 70553) | STAT | STAT | ROUTINE | - | Before LP; rule out mass, CVT | No mass; may show empty sella, flattened globes, optic nerve sheath distension, transverse sinus stenosis | Pacemaker, metal |
| CT head (if MRI unavailable) (CPT 70450) | STAT | STAT | - | - | Emergent exclusion of mass | No mass, hemorrhage | None (contrast: renal) |
| CT venography | URGENT | URGENT | - | - | If MRV inconclusive for CVT | No venous sinus thrombosis | Renal disease; contrast allergy |

### 2B. Ophthalmologic Studies

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Dilated fundoscopic exam | STAT | STAT | ROUTINE | - | All patients; before LP if possible | Papilledema grading (Frisen scale) | None |
| Optical coherence tomography (OCT) (CPT 92134) | - | ROUTINE | ROUTINE | - | Quantify RNFL thickness; follow progression | Baseline RNFL; monitor for atrophy | None |
| Automated perimetry (visual fields) | - | ROUTINE | ROUTINE | - | Detect visual field defects; monitor | Document defects; enlarged blind spot | None |
| Visual acuity | STAT | STAT | ROUTINE | STAT | Baseline and monitoring | 20/20 or stable | None |
| Color vision testing | - | ROUTINE | ROUTINE | - | Optic nerve function | Normal | None |
| Fundus photography (CPT 92250) | - | ROUTINE | ROUTINE | - | Document papilledema; follow | Baseline; monitor | None |

### 2C. IIH MRI Findings (Supportive but Not Diagnostic)

| Finding | Significance |
|---------|--------------|
| Empty or partially empty sella | Chronic elevated ICP |
| Flattening of posterior sclera | Elevated ICP transmitted to globe |
| Optic nerve sheath distension | Elevated ICP; perineural CSF |
| Vertical tortuosity of optic nerve | Elevated ICP |
| Transverse sinus stenosis | Common; may be cause or effect |
| Enhancement of optic nerve head | Active papilledema |

---

## 3. TREATMENT

### 3A. Weight Management (Cornerstone for Obese Patients)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Weight loss (diet/lifestyle) | - | Long-term ICP reduction in obese IIH patients | 10% :: - :: - :: Target 5-10% body weight loss; improves ICP | None | Weight; symptoms; visual function | - | ROUTINE | ROUTINE | - |
| Bariatric surgery referral | - | Refractory IIH with BMI >35 and obesity-related comorbidities | N/A :: - :: once :: Consider if BMI >35 with comorbidities; effective for IIH | Per surgical criteria | Weight; ICP | - | - | ROUTINE | - |
| Nutrition/dietitian referral | - | Structured weight management for IIH patients with obesity | N/A :: - :: daily :: Structured weight loss program | None | Progress | - | ROUTINE | ROUTINE | - |

### 3B. First-Line Medical Therapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Acetazolamide (Diamox) | PO | First-line ICP reduction in idiopathic intracranial hypertension | 500 mg :: PO :: BID :: 500 mg BID; titrate to 2-4 g/day as tolerated; IIHTT used up to 4 g/day | Sulfa allergy, severe renal/hepatic disease, hypokalemia | K+, bicarb, renal function q1-3 months; paresthesias (expected); fatigue, dysgeusia | ROUTINE | ROUTINE | ROUTINE | - |
| Potassium supplementation | PO | Prevent hypokalemia from acetazolamide therapy | 20-40 mEq :: PO :: daily :: 20-40 mEq daily; PRN based on K+ level | Renal failure, hyperkalemia | K+ levels | - | ROUTINE | ROUTINE | - |

### 3C. Second-Line/Adjunctive Medical Therapy

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Topiramate | PO | Second-line ICP reduction with additional weight loss benefit | 25 mg :: PO :: BID :: 25 mg BID; titrate to 50-100 mg BID; also promotes weight loss | Nephrolithiasis, glaucoma, pregnancy | Weight; cognitive effects; metabolic acidosis | - | ROUTINE | ROUTINE | - |
| Furosemide (add-on) | PO | Adjunctive ICP reduction when acetazolamide alone is insufficient | 20-40 mg :: PO :: daily :: 20-40 mg daily; if acetazolamide insufficient alone | Sulfa allergy (cross-reactivity uncommon), severe dehydration | K+, renal function | - | ROUTINE | ROUTINE | - |

### 3D. Headache Management

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Acetazolamide (treats underlying cause) | PO | IIH-related headache via ICP reduction | N/A :: PO :: per protocol :: Per above | - | Per above | Per above | - | ROUTINE | ROUTINE | - |
| Analgesics (acute) | PO | Acute symptomatic headache relief in IIH | N/A :: PO :: PRN :: NSAIDs, acetaminophen PRN; avoid opioids | - | NSAID: GI/renal issues | Limit use to prevent MOH | ROUTINE | ROUTINE | ROUTINE | - |
| Migraine prophylaxis (if comorbid) | PO | Preventive therapy for comorbid migraine in IIH patients | N/A :: PO :: per protocol :: Topiramate (dual benefit); beta-blockers, amitriptyline | - | Per medication | Per medication | - | - | ROUTINE | - |

### 3E. Therapeutic Lumbar Puncture

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Large-volume LP (CPT 62272) | - | Immediate ICP reduction and symptom relief in IIH | 20-40 mL :: - :: - :: Remove 20-40 mL CSF; immediate symptom relief | Mass lesion, coagulopathy, infection at site | Headache, symptoms; temporary benefit | URGENT | URGENT | ROUTINE | - |
| Serial LPs (CPT 62272) | - | Bridge therapy to surgery or when medical therapy is insufficient | N/A :: - :: per protocol :: Bridge to surgery or when medical therapy insufficient | Same | Same; not long-term solution | - | ROUTINE | ROUTINE | - |

### 3F. Surgical Interventions (Vision-Threatening or Refractory)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Optic nerve sheath fenestration (ONSF) | - | Vision-threatening papilledema refractory to medical therapy | N/A :: - :: once :: Incision in optic nerve sheath; protects vision; does not reduce ICP | Severe optic atrophy (relative) | Visual fields, acuity post-op | - | URGENT | ROUTINE | - |
| CSF shunting (VP or LP shunt) | - | Refractory IIH with persistent elevated ICP and headache | N/A :: - :: once :: Ventriculoperitoneal or lumboperitoneal shunt; reduces ICP and headache | Infection, peritoneal pathology | Shunt function; revision rate high (50%+) | - | URGENT | ROUTINE | - |
| Venous sinus stenting | - | IIH with significant transverse sinus stenosis and pressure gradient | N/A :: - :: per protocol :: Stent transverse sinus stenosis; emerging therapy | No significant stenosis; venous anatomy | ICP; stent patency; headache | - | ROUTINE | ROUTINE | - |

### 3G. Fulminant IIH (Urgent Vision Loss)

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| High-dose IV acetazolamide (CPT 96374) | IV | Urgent ICP reduction in fulminant IIH with acute vision loss | 500 mg :: IV :: q6h :: 500 mg IV q6h initially | Per above | K+, bicarb | STAT | STAT | - | - |
| Emergent therapeutic LP | - | Emergent ICP reduction in fulminant IIH with rapid vision decline | N/A :: - :: daily :: Large-volume LP; may repeat daily | Mass lesion, coagulopathy | Symptoms, vision | STAT | STAT | - | - |
| Urgent surgical referral | - | Fulminant IIH failing medical therapy with progressive vision loss | N/A :: - :: once :: ONSF or shunt within days | Per procedure | Vision | STAT | STAT | - | - |
| IV steroids (controversial) (CPT 96365) | IV | Short-term bridge therapy in fulminant IIH pending surgery | 250 mg :: IV :: q6h :: Methylprednisolone 250 mg IV q6h; short-term bridge only; can worsen IIH long-term | Contraindicated for maintenance | Glucose; short-term only | STAT | STAT | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|
| Neuro-ophthalmology | URGENT | ROUTINE | ROUTINE | URGENT | All patients; diagnosis, monitoring, management |
| Neurology | - | ROUTINE | ROUTINE | - | Headache management; atypical cases |
| Neurosurgery | URGENT | URGENT | ROUTINE | URGENT | Fulminant IIH; shunt evaluation |
| Interventional neuroradiology | - | ROUTINE | ROUTINE | - | Venous sinus stenting evaluation |
| Ophthalmology | URGENT | ROUTINE | ROUTINE | URGENT | If neuro-ophthalmology unavailable |
| Bariatric surgery | - | - | ROUTINE | - | Obese patients; BMI >35 |
| Nutrition/dietitian | - | ROUTINE | ROUTINE | - | Weight loss counseling |

### 4B. Medication Review (Discontinue IIH-Associated Drugs)

| Medications to Avoid/Discontinue |
|----------------------------------|
| Vitamin A and retinoids (isotretinoin, tretinoin) |
| Tetracyclines (doxycycline, minocycline) |
| Growth hormone |
| Lithium |
| Corticosteroid withdrawal (taper slowly if on steroids) |
| Levonorgestrel (controversial) |

### 4C. Patient/Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| IIH is a chronic condition requiring ongoing monitoring | - | ROUTINE | ROUTINE |
| Weight loss is critical for long-term management | - | ROUTINE | ROUTINE |
| Take acetazolamide as prescribed; stay hydrated | - | ROUTINE | ROUTINE |
| Report new visual symptoms immediately (blurred vision, double vision, vision loss) | ROUTINE | ROUTINE | ROUTINE |
| Report worsening headache, nausea/vomiting, pulsatile tinnitus | ROUTINE | ROUTINE | ROUTINE |
| Avoid medications that can worsen IIH (vitamin A, tetracyclines) | - | ROUTINE | ROUTINE |
| Keep all ophthalmology appointments; visual field testing is critical | - | ROUTINE | ROUTINE |
| IIH Research Foundation (ihrfoundation.org) for resources | - | - | ROUTINE |

### 4D. Pregnancy Considerations

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Acetazolamide: Category C; discuss risks/benefits; some use in 2nd/3rd trimester | - | ROUTINE | ROUTINE |
| Topiramate: Category D; contraindicated in pregnancy | - | ROUTINE | ROUTINE |
| Weight management critical before conception | - | - | ROUTINE |
| Serial LPs may be used in pregnancy if needed | - | ROUTINE | ROUTINE |
| Surgical intervention if vision-threatening | - | URGENT | - |
| Vaginal delivery generally safe; avoid prolonged Valsalva | - | ROUTINE | ROUTINE |

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Cerebral venous thrombosis | Acute headache; hypercoagulable state; may have focal signs | MRV, CT venography |
| Meningitis (infectious or carcinomatous) | Fever, meningismus, abnormal CSF | CSF analysis, cultures, cytology |
| Intracranial mass (tumor, abscess) | Focal signs; mass on imaging | MRI with contrast |
| Hydrocephalus | Enlarged ventricles; gait, cognition changes | MRI/CT |
| Medication-induced ICP elevation | History of causative medication | History; resolve after discontinuation |
| Sleep apnea | Nocturnal headaches; daytime somnolence; may coexist | Sleep study |
| Systemic hypertension (hypertensive encephalopathy) | Severely elevated BP; may cause papilledema | BP measurement |
| Optic neuritis | Unilateral vision loss; pain with eye movement; no papilledema initially | MRI orbits; OCT |
| Hypervitaminosis A | History of vitamin A/retinoid use | Vitamin A level |
| Anemia (severe) | Can cause papilledema without true ICP elevation | CBC |

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
| Visual acuity | STAT | Daily | Every visit | STAT | Ongoing | Stable or improving | Escalate treatment |
| Visual fields (perimetry) | - | Daily (if fulminant) | q1-3 months | - | Per risk | Stable or improving | Escalate treatment |
| Papilledema grade (Frisen) | STAT | Daily | Every visit | STAT | Ongoing | Improving or resolved | Continue treatment |
| OCT (RNFL thickness) | - | Baseline | q3-6 months | - | Per schedule | Stable; no atrophy | Indicates chronic damage |
| Weight | - | Weekly | Every visit | - | Ongoing | Decreasing (if obese) | Reinforce; consider bariatric |
| Potassium | - | Daily initially | q1-3 months | - | On acetazolamide | >3.5 mEq/L | Supplement |
| Bicarbonate | - | Daily initially | q1-3 months | - | On acetazolamide | >18 mEq/L | May need dose reduction |
| Creatinine | - | Baseline | q3-6 months | - | On acetazolamide | Stable | Adjust dose if impaired |
| Headache severity | ROUTINE | Daily | Every visit | - | Ongoing | Improving | Optimize treatment |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Outpatient management | Mild-moderate symptoms; stable vision; reliable follow-up |
| Admit to hospital | New diagnosis with significant papilledema; fulminant IIH; progressive vision loss; unable to tolerate oral medications |
| ICU admission | Rarely needed; severe headache requiring IV therapy; post-operative monitoring |
| Neuro-ophthalmology follow-up | q2-4 weeks initially; q1-3 months when stable |
| Urgent follow-up | Any decline in vision; worsening headache; medication intolerance |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Acetazolamide effective for IIH | Class I, Level A | IIHTT (Idiopathic Intracranial Hypertension Treatment Trial) |
| Weight loss improves IIH | Class II, Level B | Multiple studies; IIHTT secondary analysis |
| ONSF protects vision in IIH | Class III, Level B | Case series; observational data |
| CSF shunting reduces ICP and headache | Class III, Level B | Case series; high revision rate noted |
| Venous sinus stenting emerging therapy | Class III, Level C | Growing evidence; case series |
| Modified Dandy criteria for diagnosis | Expert consensus | [Friedman et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23966248/) |
| Topiramate as adjunct with weight loss benefit | Class III, Level C | Observational data |

---

## DIAGNOSTIC CRITERIA (Modified Dandy Criteria - Friedman 2013)

**Required for IIH Diagnosis:**
1. Papilledema
2. Normal neurologic exam (except CN VI palsy allowed)
3. Neuroimaging: Normal brain parenchyma; no meningeal enhancement; no venous thrombosis (MRV required); may show empty sella, flattened globes, optic nerve sheath distension
4. Normal CSF composition
5. Elevated opening pressure: ≥25 cm H2O in adults (≥28 cm H2O in children)
6. No other cause of intracranial hypertension identified

**IIH Without Papilledema (IIHWOP):**
- Diagnosis possible if unilateral or bilateral CN VI palsy present
- Or if ALL of: typical headache, elevated OP, normal CSF, supportive MRI findings
- Requires more stringent exclusion of secondary causes

---

## NOTES

- IIH typically affects young obese women (BMI >30); male IIH exists but consider secondary causes more carefully
- Vision loss is the most important outcome; headache is common but not the priority
- Papilledema can cause permanent optic atrophy if untreated
- Acetazolamide is first-line; titrate to maximum tolerated dose (up to 4 g/day)
- Weight loss is critical for obese patients; even 5-10% loss can significantly improve IIH
- Fulminant IIH (rapid vision loss over days to weeks) is a neuro-ophthalmic emergency
- ONSF protects vision but does not reduce ICP or headache
- Shunts reduce ICP and headache but have high revision rates (up to 50%+)
- Venous sinus stenting is emerging as effective for selected patients with significant stenosis
- Pregnancy: IIH can develop or worsen; treatment options limited; close monitoring essential
- Discontinue medications that can cause/worsen IIH (vitamin A, tetracyclines, etc.)
- Long-term follow-up required; IIH can recur, especially with weight gain

---

## CHANGE LOG

**v1.0 (January 29, 2026)**
- Initial template creation
- IIHTT evidence incorporated
- Modified Dandy criteria included
- Full surgical options (ONSF, shunt, venous stenting)
- Fulminant IIH section
- Pregnancy considerations
- IIH-associated medications to avoid
