---
title: "Cauda Equina Syndrome"
description: "Clinical decision support for cauda equina syndrome (ces) diagnosis and management"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
---

# Cauda Equina Syndrome

**VERSION:** 1.0
**CREATED:** January 27, 2026
**STATUS:** Initial build

---

**DIAGNOSIS:** Cauda Equina Syndrome (CES)

**ICD-10:** G83.4 (Cauda equina syndrome), M48.06 (Spinal stenosis, lumbar region), M51.16 (Intervertebral disc disorders with radiculopathy, lumbar region), M51.17 (Intervertebral disc disorders with radiculopathy, lumbosacral region), G95.89 (Other specified diseases of spinal cord)

**SYNONYMS:** Cauda equina syndrome, CES, cauda equina compression, saddle anesthesia, urinary retention with back pain, bowel/bladder dysfunction, lower spine emergency, cauda equina

**SCOPE:** Emergency evaluation and management of cauda equina syndrome in adults. Covers urgent recognition of incomplete vs. complete CES, emergent MRI, surgical decompression timing, etiologic workup (disc herniation, tumor, abscess, hematoma), bladder management, and functional prognostication. Excludes conus medullaris syndrome (partially overlaps — key distinguishing features addressed), malignant epidural spinal cord compression above the conus (separate template), and chronic lumbar stenosis without CES features.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential | STAT | STAT | - | STAT | Infection (epidural abscess); baseline for surgery; leukocytosis; anemia assessment | Normal; leukocytosis → consider abscess; thrombocytopenia affects surgical candidacy |
| CMP (BMP + LFTs) | STAT | STAT | - | STAT | Electrolytes; renal function (contrast, NSAIDs); glucose; hepatic function (anesthetic risk) | Normal |
| PT/INR, aPTT | STAT | STAT | - | STAT | Coagulopathy; anticoagulation status; surgical clearance; epidural hematoma etiology | Normal; INR <1.5 for surgery; prolonged → consider epidural hematoma |
| ESR / CRP | STAT | STAT | - | STAT | Epidural abscess differential (ESR >20 mm/hr: 94% sensitivity for spinal abscess); discitis; malignancy | Normal; markedly elevated (ESR >30-50, CRP >10) → strongly consider abscess or infection |
| Blood cultures (x2 sets) | STAT | STAT | - | STAT | Epidural abscess; bacteremia; source identification if infectious etiology suspected | Negative; positive → epidural abscess or hematogenous source |
| Blood glucose | STAT | STAT | - | STAT | Baseline; anesthetic risk; diabetic patients at increased disc herniation and infection risk | <180 mg/dL |
| Type and screen | STAT | STAT | - | STAT | Surgical candidacy; blood product availability for emergency decompression | On file |
| Urinalysis | STAT | STAT | - | STAT | UTI (common comorbidity and mimicker of urinary symptoms); neurogenic bladder assessment; baseline | Normal; UTI may coexist — treat but do NOT attribute bladder dysfunction solely to UTI if CES features present |
| Pregnancy test (β-hCG) | STAT | STAT | - | STAT | MRI and anesthetic planning; pregnancy may exacerbate disc herniation (increased lordosis/weight) | Negative; if positive → MRI still indicated (no gadolinium needed for CES diagnosis) |
| Procalcitonin | STAT | STAT | - | STAT | Bacterial infection differential (more specific than CRP); if abscess suspected | <0.25 (low bacterial probability); >0.5 → consider abscess |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| HbA1c | - | ROUTINE | ROUTINE | - | Diabetes assessment (risk factor for disc herniation, infection, neuropathy); post-operative wound healing | <7.0% |
| Tumor markers (PSA, CEA, etc.) | - | ROUTINE | ROUTINE | - | If imaging suggests neoplastic etiology rather than disc herniation | Normal; elevated → guides oncologic workup |
| SPEP / free light chains | - | ROUTINE | ROUTINE | - | Multiple myeloma presenting as cauda equina compression | No M-protein; normal kappa/lambda ratio |
| LDH | - | ROUTINE | ROUTINE | - | Lymphoma; tumor burden | Normal; elevated → lymphoma, aggressive malignancy |
| HIV | - | ROUTINE | ROUTINE | - | Immunocompromised → infection risk; primary CNS lymphoma differential | Negative |
| Urine culture | STAT | STAT | - | STAT | Pre-existing UTI; post-catheterization planning; differentiate neurogenic bladder from UTI | Negative; if positive → treat but continue CES workup |
| Post-void residual (PVR) — bladder scan | STAT | STAT | ROUTINE | STAT | KEY DIAGNOSTIC TEST: bladder retention is hallmark of CES; PVR >200 mL is highly concerning; >500 mL strongly suggestive of neurogenic retention | PVR <100 mL (normal); PVR >200 mL → significant retention; >500 mL → almost certainly neurogenic |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CSF analysis (only at surgery or LP if needed) | - | EXT | EXT | - | If inflammatory/infectious etiology suspected (GBS affecting cauda equina = rare); leptomeningeal carcinomatosis | Normal; elevated protein → GBS, tumor; malignant cells → leptomeningeal disease |
| Paraneoplastic antibody panel | - | EXT | EXT | - | Atypical CES without structural cause; paraneoplastic cauda equina neuritis (anti-CRMP5/CV2, anti-amphiphysin) | Negative; positive → paraneoplastic syndrome |
| Anti-ganglioside antibodies (GM1, GD1b, GQ1b) | - | EXT | EXT | - | GBS variant affecting cauda equina roots (rare); if imaging shows nerve root enhancement without structural compression | Negative; positive → GBS/CIDP affecting cauda equina |
| AQP4-IgG / MOG-IgG | - | EXT | EXT | - | If conus medullaris lesion rather than cauda equina compression; NMOSD can affect conus | Negative; positive → NMOSD/MOGAD |
| Sarcoidosis workup (ACE, chest CT, lysozyme) | - | EXT | EXT | - | Neurosarcoidosis affecting cauda equina (nerve root inflammation/enhancement without structural lesion); elevated ACE | Normal ACE; chest CT: no hilar lymphadenopathy; if positive → neurosarcoidosis |
| EMG/NCS | - | EXT | EXT | - | Chronic or atypical CES; differentiate from peripheral neuropathy, plexopathy; establish nerve root involvement pattern; prognostic (denervation = poor recovery) | Abnormal: acute denervation (fibrillations, positive sharp waves) in L4-S4 myotomes bilaterally; absent H-reflex bilaterally; abnormal pudendal nerve conduction |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI lumbar spine without contrast (emergent) | STAT | STAT | - | STAT | **Within 4 hours of ED arrival — SURGICAL EMERGENCY; ideally within 1 hour**; extends to thoracolumbar junction (T10-sacrum) to include conus medullaris | Large disc herniation (most common — 45% of CES cases) compressing cauda equina; canal compromise; level of compression; number of roots compressed; disc fragment migration; tumor, abscess, or hematoma as alternative cause; conus medullaris location and signal | MRI-incompatible implants; severe claustrophobia (sedate — do NOT delay MRI for anxiety); GFR <30 for contrast (but contrast NOT required for disc herniation diagnosis — obtain non-contrast first) |
| MRI lumbar spine WITH contrast (gadolinium) | STAT | STAT | - | STAT | Add contrast if: suspected abscess, tumor, or inflammatory etiology; ring-enhancing epidural collection = abscess; homogeneous enhancement = tumor; nerve root enhancement = inflammatory/neoplastic | Epidural abscess (ring enhancement, restricted diffusion); tumor (enhancing mass); nerve root enhancement (inflammatory, leptomeningeal disease); distinguish from disc herniation (which does NOT enhance) | GFR <30 (gadolinium risk — benefit outweighs risk in emergency); gadolinium allergy (premedicate) |
| Bladder scan (post-void residual) | STAT | STAT | - | STAT | **Before MRI if possible — critical triage tool**; have patient attempt to void → immediate bladder ultrasound for PVR | PVR >200 mL = significant retention → HIGH probability of CES; PVR >500 mL = almost certain neurogenic retention; normal PVR does NOT exclude early/incomplete CES | None (bedside ultrasound) |
| Plain radiographs (lumbar spine AP/lateral) | STAT | STAT | - | STAT | While awaiting MRI; identifies vertebral collapse, spondylolisthesis, fracture, alignment; limited value but rapid triage tool | Disc space narrowing; spondylolisthesis; fracture; alignment abnormality; NOTE: X-rays CANNOT diagnose disc herniation — MRI is required | Pregnancy (shield abdomen) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT lumbar spine without contrast | STAT | STAT | - | STAT | If MRI not available or contraindicated; inferior to MRI for soft tissue but shows bone and canal narrowing; CT myelogram if MRI impossible | Disc herniation (seen as soft tissue density in canal); bone fragments; canal diameter; fracture; spondylolisthesis | CT alone has limited sensitivity for disc herniation vs. MRI; myelogram adds invasive risk |
| CT myelogram | STAT | STAT | - | STAT | If MRI absolutely contraindicated (implant); intrathecal contrast via LP → CT; demonstrates level of block and root compression | Complete or partial block; compressed cauda equina roots; level and extent of compression; may miss small free fragments | LP contraindicated if abscess suspected at LP site; coagulopathy; rare but important if MRI impossible |
| MRI whole spine | - | URGENT | - | URGENT | If etiology unclear; evaluate for additional levels of disease; concurrent cord compression; tumor staging; multilevel disc disease | Additional sites of compression; intramedullary lesion (conus); multifocal disease | Same as lumbar MRI |
| Urodynamic studies | - | - | ROUTINE | - | Post-acute phase; quantify bladder dysfunction; detrusor areflexia (CES pattern); plan long-term bladder management | Detrusor areflexia (areflexic bladder) = cauda equina denervation; decreased bladder sensation; increased capacity; poor emptying | Acute UTI; recent surgery (timing per surgeon) |
| Anal manometry / pudendal nerve testing | - | - | EXT | - | Quantify sphincter dysfunction; prognostic for recovery; pudendal nerve conduction | Reduced anal sphincter pressures; denervated pudendal nerve | Patient tolerance; acute phase may not be appropriate |
| EMG/NCS (lower extremities + paraspinal) | - | - | ROUTINE | - | 2-3 weeks post-onset (acute denervation takes 2-3 weeks to appear on EMG); prognosis; differentiate from peripheral neuropathy or plexopathy | Bilateral L4-S4 denervation; reduced CMAP amplitudes in bilateral L5/S1 distribution; absent H-reflexes bilaterally; bilateral pudendal neuropathy | Too early in acute phase (<2 weeks = may be false negative for denervation); patient tolerance |

### 2C. Rare/Advanced

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| CT angiography (lumbar) | - | EXT | - | EXT | If vascular malformation suspected (spinal dural AV fistula causing venous hypertension → CES symptoms); progressive myelopathy/CES with dilated serpiginous vessels on MRI | Spinal AV fistula; AVM; arteriovenous malformation feeding vessels | Contrast allergy; renal impairment |
| Spinal angiography | - | EXT | EXT | - | Definitive diagnosis and treatment of spinal dural AV fistula; also pre-operative embolization for vascular tumors | Fistula location; endovascular treatment candidate | Invasive; contrast risk; radiation exposure |
| PET/CT | - | - | EXT | - | If malignancy causing CES — staging; unknown primary identification | Primary tumor; metastatic burden | Uncontrolled diabetes; pregnancy |
| Cystometrogram | - | - | EXT | - | Formal bladder function assessment; post-decompression recovery monitoring; long-term bladder management planning | Bladder compliance; detrusor function; capacity; sensation thresholds | Active UTI |

### Lumbar Puncture

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| LP — Generally NOT indicated acutely | - | EXT | EXT | - | LP is NOT required for diagnosis of typical CES (disc herniation, tumor, abscess seen on MRI); ONLY if inflammatory/infectious etiology without clear structural cause; OR CT myelogram if MRI impossible | CSF protein elevation (GBS, tumor); pleocytosis (infection, inflammation); malignant cells (leptomeningeal disease); albuminocytologic dissociation (GBS) | Do NOT perform LP if large disc herniation compressing cauda equina (could theoretically worsen by altering pressure dynamics — proceed to surgery instead); coagulopathy; abscess at LP site |

---

## 3. TREATMENT PROTOCOLS

### 3A. Acute/Emergent Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Emergent surgical decompression** | - | - | **THIS IS A SURGICAL EMERGENCY — TIME IS NERVE**; Emergent neurosurgery/spine surgery consultation; posterior lumbar laminectomy with discectomy (most common procedure); **Timing:** Within 24h of symptom onset — ideally within 24h but outcome improves the sooner surgery is performed; <24h clearly better than >48h; some evidence supports <12h for best outcomes; **Complete CES (CES-R with retention):** Truly emergent — surgery as soon as possible (within hours); **Incomplete CES (CES-I):** Urgent — surgery within 24h; risk of progressing to complete | - | Ahn et al. (2000): Decompression <48h = significantly better outcomes for bladder recovery (70% vs. 30%); Todd (2005) meta-analysis: Earlier surgery = better outcomes, but exact time threshold debated; DeBois et al. (2019): <24h optimal, <48h acceptable; Srikandarajah et al. (2020): Urgent surgery (<24h) associated with better functional outcomes | STAT | STAT | - | - |
| **Bladder management** | - | - | 200 mL :: - :: - :: **Bladder scan (PVR) STAT on arrival** — do NOT wait for MRI; if PVR >200 mL → Foley catheter placement; if PVR >500 mL → Foley + strict I&O monitoring; avoid overdistension (>600 mL causes detrusor damage — may become irreversible); document voiding pattern; post-operative: trial of void at 24-48h with PVR checks; CIC (clean intermittent catheterization) teaching if retention persists | - | Bladder overdistension causes detrusor muscle damage → irreversible areflexic bladder; early catheterization prevents secondary damage; bladder recovery is the MOST SENSITIVE indicator of CES recovery and the MOST COMMON persistent deficit | STAT | STAT | - | STAT |
| **Pain management** | IV | - | 650-1000 mg :: IV :: q6h :: Back pain and radicular pain often severe; acetaminophen 650-1000 mg q6h (scheduled) + opioids (morphine 2-4 mg IV q3h PRN or hydromorphone 0.5-1 mg IV q3h PRN); NSAIDs: ketorolac 15-30 mg IV q6h (short-term, if no surgical contraindication and normal renal function — pre-op use is surgeon-dependent); neuropathic: gabapentin 300 mg TID (start if radicular pain prominent); avoid excessive sedation that obscures neurologic exam | - | Adequate analgesia essential for patient assessment and MRI tolerance; balance with need for neurologic monitoring | STAT | STAT | - | STAT |
| **Dexamethasone (if tumor or abscess)** | IV | - | 10 mg :: IV :: q6h :: **Disc herniation CES:** Steroids NOT routinely indicated (no evidence of benefit; some centers use short course); **Tumor-related CES:** Dexamethasone 10 mg IV bolus → 4 mg q6h (same as MSCC protocol); **Abscess-related CES:** Dexamethasone controversial (may impair immune response) — use only if severe edema with rapid neurologic decline | - | No RCT evidence supporting steroids for disc-related CES; tumor CES: Sorensen et al. (1994) supports steroids; abscess: prioritize antibiotics + surgical drainage | STAT | STAT | - | STAT |
| **Antibiotics (if abscess suspected)** | IV | - | 25-30 mg/kg :: IV :: q12h :: **Epidural abscess causing CES:** Empiric: Vancomycin 25-30 mg/kg IV load + ceftriaxone 2g IV q12h (or cefepime 2g IV q8h); adjust to culture/sensitivity; MRSA coverage essential; **Duration:** Typically 6-8 weeks IV antibiotics for epidural abscess; **Timing:** Start AFTER blood cultures drawn but do NOT delay if patient is deteriorating | - | S. aureus (including MRSA) is most common organism in epidural abscess (60-70%); gram-negative coverage for UTI/abdominal source; streptococci, anaerobes less common | STAT | STAT | - | STAT |
| **DVT prophylaxis** | SC | - | 40 mg :: SC :: daily :: SCDs immediately; pharmacologic prophylaxis: enoxaparin 40 mg SQ daily starting post-operatively (typically 12-24h after surgery per surgeon protocol); immobile CES patients at high VTE risk | - | Immobility + lower extremity weakness = high DVT risk; mechanical prophylaxis pre-operatively; early pharmacologic prophylaxis post-operatively | STAT | STAT | - | STAT |
| **Bowel management** | PR | - | 100 mg :: PR :: BID :: Assess rectal tone (digital rectal exam — absent/reduced in CES); bowel regimen: docusate 100 mg BID + senna 2 tabs HS; bisacodyl suppository daily if no BM in 48h; monitor for fecal incontinence vs. constipation (both occur in CES); opioid-related constipation compounds the issue | - | Bowel dysfunction common in CES; S2-S4 denervation affects external anal sphincter and rectal sensation; proactive management prevents complications | STAT | STAT | - | STAT |

### 3B. Definitive/Targeted Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Lumbar laminectomy + discectomy (disc herniation CES)** | - | - | **Most common surgery:** Posterior approach; laminectomy at affected level(s); remove herniated disc fragment; decompress cauda equina; **Approach:** Midline; may require bilateral laminotomy or hemi-laminectomy for lateralized discs; large central herniations often require bilateral approach; **Key:** Ensure COMPLETE decompression — incomplete decompression leads to persistent deficit; intraoperative confirmation with direct visualization of free cauda equina nerve roots | - | Gold standard for disc-related CES; no RCT comparing surgery vs. non-operative (would be unethical to randomize given natural history); observational data uniformly supports early surgical decompression | - | STAT | - | - |
| **Microdiscectomy (if technically appropriate)** | - | - | Minimally invasive approach; appropriate for contained disc herniations without significant canal stenosis; faster recovery; less tissue disruption; may not provide adequate decompression for massive central disc herniation | - | Smaller incision, less muscle disruption; but surgeon must ensure adequate decompression — do NOT compromise canal visualization for a smaller incision in CES | - | STAT | - | - |
| **Surgical drainage + decompression (epidural abscess)** | IV | - | Posterior approach; laminectomy; drain abscess; culture material; irrigate; leave wound open or with drain; may require multi-level decompression; **Combined with:** IV antibiotics 6-8 weeks; follow with serial MRI and inflammatory markers | - | Epidural abscess with CES = surgical emergency; medical management alone (antibiotics without surgery) only if: no neurologic deficit AND very high surgical risk; most CES presentations require surgery | - | STAT | - | - |
| **Tumor resection + decompression** | - | - | If tumor-related CES (e.g., schwannoma, ependymoma, metastasis); posterior decompression ± en bloc or piecemeal tumor resection; send pathology; may need subsequent radiation/chemotherapy | - | Intradural-extramedullary tumors (schwannoma, meningioma, myxopapillary ependymoma) are potentially curable with complete resection; metastatic CES → decompression + radiation | - | STAT | - | - |
| **Hematoma evacuation** | - | - | Epidural hematoma causing CES (spontaneous on anticoagulation, post-procedural, or post-traumatic); emergent laminectomy with hematoma evacuation; reverse anticoagulation STAT | - | Spontaneous spinal epidural hematoma: Groen & Ponssen (1990): better outcomes with surgery <12h of onset; anticoagulation reversal essential (4F-PCC for warfarin, idarucizumab for dabigatran, andexanet for Xa inhibitors) | - | STAT | - | - |
| **Non-operative management (rare, selected cases)** | - | - | **ONLY appropriate if:** (1) Imaging does NOT show significant structural compression, (2) Symptoms are improving spontaneously, (3) Patient refuses surgery (document informed refusal thoroughly), (4) Medically inoperable (extremely high surgical risk); **Requires:** Close monitoring with serial neuro exams q2-4h; repeat MRI if worsening; immediate surgery if any progression | - | Non-operative management is NOT standard of care for CES with structural compression; delayed surgery has worse outcomes; informed consent must document risks of non-operative management (permanent bladder/bowel/sexual dysfunction, progressive weakness) | - | - | ROUTINE | - |

### 3C. Adjunctive Treatment

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| **Clean intermittent catheterization (CIC) training** | - | - | 100 mL :: - :: - :: If bladder function does not recover by 48-72h post-surgery; teach patient CIC q4-6h; target PVR <100 mL before discontinuing CIC; may take weeks to months to recover | - | CIC is preferred over indwelling Foley for long-term bladder management (lower UTI risk); most patients can learn self-catheterization; bladder recovery may take 6-12 months | - | ROUTINE | ROUTINE | - |
| **Neuropathic pain management** | PO | - | 300 mg :: PO :: TID :: Gabapentin 300 mg PO TID → titrate to 600-900 mg TID over 1-2 weeks; OR pregabalin 75 mg BID → 150-300 mg BID; duloxetine 30 mg daily → 60 mg daily; amitriptyline 10-25 mg HS (caution: urinary retention may worsen); topical lidocaine 5% patches for localized radicular pain | - | Neuropathic pain (burning, tingling, electric shocks in perineum, legs) is common and debilitating after CES; may persist chronically; multimodal approach needed | - | STAT | ROUTINE | STAT |
| **Physical therapy / rehabilitation** | - | - | PT evaluation within 24h post-operatively; early mobilization; lower extremity strengthening; gait training; core stabilization; progressive activity as tolerated; pelvic floor PT for bladder/bowel recovery | - | Early rehabilitation improves functional outcomes; pelvic floor rehabilitation is evidence-based for bladder/bowel recovery after CES | - | URGENT | ROUTINE | - |
| **Occupational therapy** | - | - | ADL assessment; adaptive equipment; if lower extremity weakness impairs function; bathroom modifications; return-to-work planning | - | Functional independence optimization | - | ROUTINE | ROUTINE | - |
| **Pelvic floor rehabilitation** | - | - | Specialized pelvic floor PT; biofeedback for bladder and bowel retraining; Kegel exercises (if able); electrical stimulation of pelvic floor; sacral neuromodulation evaluation if persistent dysfunction >12 months | - | Evidence supports pelvic floor PT for bladder and bowel recovery after CES; biofeedback improves outcomes | - | - | ROUTINE | - |
| **Psychological support** | - | - | CES has devastating psychosocial impact (sexual dysfunction, incontinence, chronic pain, disability in often-young patients); depression screening (PHQ-9); anxiety screening; sexual health counseling; support groups; consider psychiatry referral | - | Depression affects 30-60% of CES patients long-term; sexual dysfunction is profoundly distressing; early psychological intervention improves coping and recovery | - | ROUTINE | ROUTINE | - |
| **Stool softener / bowel program** | - | - | 100 mg :: - :: BID :: Docusate 100 mg BID + senna 2 tabs HS; bisacodyl suppository PRN; digital stimulation for areflexic bowel; timed bowel program; fiber supplementation; adequate hydration | - | Neurogenic bowel management reduces complications (impaction, incontinence); establish routine bowel program early | STAT | STAT | ROUTINE | STAT |

### 3D. Medications to AVOID or Use with Caution

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Anticholinergics (oxybutynin, tolterodine — for urgency) | - | - | - | - | - | - | - | - | - | - |
| Tricyclic antidepressants (amitriptyline, nortriptyline) | - | - | - | - | - | - | - | - | - | - |
| Alpha-blockers (tamsulosin, silodosin) — without urologic guidance | - | - | - | - | - | - | - | - | - | - |
| NSAIDs (prolonged, peri-operative) | - | - | - | - | - | - | - | - | - | - |
| Epidural steroid injection (as treatment for CES) | - | - | - | - | - | - | - | - | - | - |
| Chiropractic manipulation (lumbar) | - | - | - | - | - | - | - | - | - | - |
| Excessive IV fluids (post-operatively) | IV | - | - | - | - | - | - | - | - | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Essential

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Neurosurgery / Spine surgery consultation — EMERGENCY | STAT | STAT | - | STAT | **IMMEDIATE consultation upon clinical suspicion of CES** — do NOT wait for MRI to consult; communicate urgency; CES is a recognized surgical emergency; the spine surgeon should be contacted concurrently with MRI ordering; if no spine surgeon available → emergent transfer to facility with 24/7 spine surgery capability |
| Post-void residual (bladder scan) | STAT | STAT | - | STAT | **Perform BEFORE MRI** — PVR is a rapid, non-invasive triage tool; PVR >200 mL in the setting of bilateral radiculopathy/perineal symptoms = HIGH suspicion for CES; informs urgency of MRI and surgical consultation |
| Digital rectal examination | STAT | STAT | - | STAT | Assess perianal sensation (S2-S4); anal sphincter tone (reduced or absent in CES); voluntary contraction; anocutaneous reflex (absent in CES — tests S2-S4 arc); this is an essential component of the neurologic exam and MUST be documented |
| Comprehensive neurologic exam documentation | STAT | STAT | - | STAT | Document: bilateral lower extremity strength (L2-S2 myotomes); sensation (light touch, pinprick) — especially perianal/perineal (S2-S5 dermatomes); deep tendon reflexes (ankle jerks); plantar responses; bulbocavernosus reflex; anal wink; rectal tone; bladder function; sexual function (ask about erectile function/genital sensation) |
| Classify CES subtype | STAT | STAT | - | STAT | **CES-Incomplete (CES-I):** Altered urinary sensation, difficulty initiating voiding, reduced perineal sensation BUT still has some bladder function (partial retention); **CES-Retention (CES-R):** Painless urinary retention, overflow incontinence, absent perineal sensation, absent anal tone; **CES-R is a more advanced stage with worse prognosis** |
| Informed consent for surgery | STAT | STAT | - | - | Document discussion of: surgical risks, CES natural history without surgery (progressive permanent paralysis, incontinence, sexual dysfunction), realistic outcome expectations (bladder recovery is slowest and most uncertain), risk of persistent deficits even with surgery |
| Transfer to surgical center (if no spine surgeon) | STAT | - | - | - | If presenting ED does not have spine surgery capability → EMERGENT transfer; obtain MRI at presenting facility first if possible (saves time at receiving facility); Foley catheter before transfer; dexamethasone if tumor-related |

### 4B. Extended

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Urology consultation | - | ROUTINE | ROUTINE | - | Neurogenic bladder management; urodynamic testing at 6-12 weeks post-surgery; long-term bladder plan (CIC vs. indwelling vs. suprapubic catheter); sexual health assessment |
| PM&R / Rehabilitation consultation | - | URGENT | ROUTINE | - | Inpatient rehab candidacy if significant motor deficits; PT/OT coordination; assistive devices; functional goals; return-to-work timeline |
| Pain management consultation | - | ROUTINE | ROUTINE | - | If pain refractory to standard analgesics + neuropathic agents; chronic pain planning; may need interventional pain procedures (nerve blocks, neuromodulation) in chronic phase |
| Sexual health counseling | - | ROUTINE | ROUTINE | - | Sexual dysfunction affects 40-70% of CES patients long-term; erectile dysfunction in males (S2-S4); female sexual dysfunction (decreased genital sensation, lubrication difficulties); refer to sexual health specialist; PDE5 inhibitors (sildenafil) for ED; vacuum devices; referral to urology/gynecology |
| Colorectal surgery / GI consultation | - | - | ROUTINE | - | Persistent fecal incontinence; sacral nerve stimulation evaluation; biofeedback-refractory bowel dysfunction; anal sphincter repair assessment |
| Social work / case management | - | ROUTINE | ROUTINE | - | Disability assessment; workplace accommodations; home modifications (bathroom accessibility); caregiver support; insurance navigation; support groups (Cauda Equina Syndrome Association) |
| Medicolegal documentation | STAT | STAT | ROUTINE | STAT | CES is one of the most litigated conditions in spine surgery; document: time of symptom onset, time of presentation, time of MRI, time of surgical consultation, time of surgery, neurologic exam at each time point, bladder function assessment, rationale for any delays; CES diagnosis is a recognized emergency standard of care |

### 4C. Atypical/Refractory

| Recommendation | ED | HOSP | OPD | ICU | Details |
|---------------|:--:|:----:|:---:|:---:|---------|
| Revision surgery | - | URGENT | ROUTINE | - | If post-operative MRI shows residual compression (retained disc fragment); persistent or worsening deficits after initial surgery; recurrent disc herniation |
| Sacral neuromodulation | - | - | EXT | - | For refractory neurogenic bladder or fecal incontinence >12 months post-decompression; InterStim device implantation; requires trial stimulation first; evidence growing for neurogenic populations |
| Intrathecal baclofen pump | - | - | EXT | - | If spasticity develops (rare in pure cauda equina lesion — suggests conus involvement); more relevant for conus medullaris syndrome |
| Chronic pain management program | - | - | ROUTINE | - | Multidisciplinary chronic pain program; cognitive behavioral therapy for pain; mindfulness-based stress reduction; graded activity program; may need long-term opioid management with monitoring |
| Psychiatric referral | - | ROUTINE | ROUTINE | - | PTSD, depression, anxiety common post-CES; body image disturbance; sexual dysfunction grief; chronic pain coping; may need medication management |
| Legal documentation review | - | - | ROUTINE | - | If delayed diagnosis is a concern; risk management consultation; ensure complete medical record documentation |

---

═══════════════════════════════════════════════════════════════
SECTION B: SUPPORTING INFORMATION
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

### Primary Differential Diagnoses

| Diagnosis | Key Differentiating Features | Distinguishing Studies |
|-----------|------------------------------|----------------------|
| Conus medullaris syndrome | Upper motor neuron AND lower motor neuron signs; bilateral and symmetric; early bladder/bowel dysfunction; back pain less prominent than radicular pain; reflexes may be hyperactive (UMN) or absent (LMN); typically at T12-L2 level; more symmetric than CES | MRI: lesion at T12-L2 level (conus); cord signal change (T2 hyperintensity); CES lesion is below L1-L2 (cauda equina roots only); conus lesion → Babinski may be present (CES → absent or flexor) |
| Lumbar spinal stenosis (without CES) | Neurogenic claudication (walking-induced symptoms relieved by sitting/flexion); chronic progressive course; bilateral leg pain/weakness with walking; no bladder/bowel dysfunction (unless severe CES from stenosis); intermittent symptoms | MRI: multilevel stenosis; trefoil canal shape; ligamentum flavum hypertrophy; NO acute disc herniation; symptoms are exercise-induced, not constant; PVR normal |
| Acute disc herniation (without CES) | Unilateral radiculopathy; no bilateral symptoms; no saddle anesthesia; no bladder/bowel dysfunction; straight leg raise positive; single dermatomal pattern | MRI: lateral or posterolateral disc herniation compressing single root; NO cauda equina compression; normal PVR; normal rectal tone |
| Epidural abscess | Fever (50-66%); IVDU, immunocompromised, recent procedure; rapidly progressive; ESR >20 (94% sensitivity); severe spinal tenderness; leukocytosis; can cause CES if lumbar location | MRI: ring-enhancing epidural collection with restricted diffusion; blood cultures positive (60%); ESR/CRP markedly elevated; clinical triad: back pain → radiculopathy → weakness (classic but only 10-15% present with full triad) |
| Epidural hematoma | Acute onset; anticoagulation or post-procedural (epidural injection, spinal surgery, LP); severe back pain → rapid progressive weakness; coagulopathy history | MRI: epidural collection with blood signal (T1 bright in subacute); coagulation studies abnormal; anticoagulation history; post-procedural temporal relationship |
| Guillain-Barré syndrome (GBS) | Ascending symmetric weakness; areflexia; post-infectious (Campylobacter, CMV, EBV); sensory symptoms but often mild; facial weakness may be present; no saddle anesthesia typically; CSF: albuminocytologic dissociation | MRI spine: may show nerve root enhancement BUT no structural compression; CSF: elevated protein, normal cells; NCS: demyelinating pattern or AMAN pattern; anti-ganglioside antibodies |
| Peripheral neuropathy (bilateral) | Chronic course; distal > proximal; length-dependent pattern; diabetes, alcohol; stocking-glove distribution; gradual onset; reflexes may be reduced distally; NO saddle anesthesia; NO acute bladder retention | EMG/NCS: diffuse length-dependent neuropathy; MRI: no structural compression; HbA1c; B12; SPEP; gradual course distinguishes from acute CES |
| Lumbosacral plexopathy | Unilateral (usually); painful; diabetic amyotrophy; radiation-induced; tumor infiltration; asymmetric weakness/sensory loss in lumbosacral plexus distribution; typically NO bladder dysfunction (unless bilateral) | MRI pelvis: plexus enhancement or mass; EMG: plexus distribution denervation; CT abdomen/pelvis: retroperitoneal mass; HbA1c; typically unilateral |
| Functional neurological disorder (FND) | Inconsistent exam findings; Hoover's sign positive; non-anatomical sensory pattern; normal imaging; normal PVR; no objective sphincter dysfunction; give-way weakness; history of psychological stressors | MRI: normal; PVR: normal; rectal tone: normal; neurophysiology: normal; psychiatric history; clinical inconsistency (e.g., inability to lift leg on command but normal gait observed); NOTE: FND is a diagnosis of exclusion in CES — always obtain MRI first |

### CES-I vs. CES-R Classification

| Feature | CES-Incomplete (CES-I) | CES-Retention (CES-R) |
|---------|------------------------|----------------------|
| Bladder function | Altered sensation; difficulty initiating stream; incomplete emptying; urgency | Painless retention; overflow incontinence; no desire to void |
| PVR | 200-500 mL (partial retention) | >500 mL (complete retention) |
| Perineal sensation | Reduced but present | Absent or markedly reduced |
| Anal tone | Reduced | Absent |
| Prognosis with surgery | Better outcomes; most regain bladder function | Worse outcomes; 30-50% persistent bladder dysfunction |
| Urgency | Urgent (within 24h) | Emergent (within hours — ASAP) |

### Red Flags Requiring Urgent Reassessment

| Red Flag | Concern | Action |
|----------|---------|--------|
| Progressive bilateral leg weakness | Evolving CES; worsening compression; expanding hematoma | STAT MRI; emergent surgery; escalate surgical urgency |
| Loss of bladder function (CES-I → CES-R) | Progression from incomplete to complete CES; bladder recovery significantly worse after retention onset | IMMEDIATE surgery; do NOT wait for elective OR time; OR should be arranged within hours |
| Complete saddle anesthesia | Complete S2-S5 denervation; poor prognostic sign | STAT surgery; this represents advanced CES-R |
| Bilateral foot drop (new) | L4-L5 root denervation bilaterally; severe compression | Emergent decompression |
| Fever + back pain + neurologic deficit | Epidural abscess potentially causing/mimicking CES | Blood cultures; MRI with contrast; empiric antibiotics; surgical drainage if abscess confirmed |
| Fecal incontinence (new) | S2-S4 denervation progressing; significant cauda equina compromise | Emergent surgery if not already performed; if post-operative → urgent MRI for residual compression |
| Urinary retention increasing despite Foley (inability to trial void) | Worsening or persistent denervation; incomplete decompression; re-herniation | Post-op MRI; urodynamics; consider revision surgery if compression persists |

---

## 6. MONITORING PARAMETERS

### Acute Phase Monitoring (Pre-operative and First 72h Post-operative)

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic examination (lower extremity strength, sensation, reflexes) | q2-4h pre-operatively; q4h post-operatively x 48h | Stable pre-op; improving post-op | Pre-op worsening: escalate surgical urgency; post-op worsening: STAT MRI (hematoma, residual compression, re-herniation) |
| Perianal/perineal sensation and rectal tone | q4h (at minimum with each neuro check) | Improving or stable | Worsening: STAT MRI |
| Bladder function / PVR | Continuous monitoring via Foley with hourly I&O pre/post-op; Trial of void at 24-48h post-op with PVR check | PVR <100 mL to discontinue catheter; voiding spontaneously | PVR >200 mL after trial of void → replace Foley; begin CIC teaching; urology consult |
| Pain assessment (NRS) | q4h | NRS <4/10 | Escalate analgesics; add neuropathic agents; new/worsening pain post-op → concern for hematoma/complication |
| Wound assessment (post-operative) | q8h | No drainage, swelling, erythema, dehiscence | Wound complication → surgical team notification; drain output monitoring |
| Bowel function | Daily | BM within 48-72h post-op | Bowel regimen intensification; abdominal X-ray if distended; rectal exam |
| Temperature | q4h | Afebrile | Fever: wound infection, UTI (Foley-associated), DVT, abscess; cultures and imaging as indicated |
| DVT screening | Daily calf circumference; symptoms | No DVT signs | Bilateral lower extremity duplex US if symptoms; therapeutic anticoagulation if confirmed |

### Subacute/Outpatient Monitoring

| Parameter | Frequency | Target | Action if Abnormal |
|-----------|-----------|--------|-------------------|
| Neurologic examination | 2 weeks post-op, 6 weeks, 3 months, 6 months, 12 months | Progressive improvement; stable at plateau | Worsening: MRI for re-herniation or residual disease; EMG at 3 months |
| Bladder function (PVR) | Each visit until resolved; formal urodynamics at 6-12 weeks if persistent dysfunction | PVR <100 mL; spontaneous voiding; continent | PVR >200 mL → continue CIC; urology follow-up; sacral neuromodulation evaluation at 12 months if persistent |
| Bowel function | Each visit | Regular BMs; continent | Persistent incontinence → colorectal referral; biofeedback; sacral neuromodulation |
| Sexual function assessment | 6 weeks, 3 months, 6 months, 12 months | Recovering sensation; erectile function (males); genital sensation (all) | PDE5 inhibitors for ED; sexual health counseling; pelvic floor PT |
| Pain assessment | Each visit | Controlled with oral medications; decreasing over time | Chronic neuropathic pain management; multidisciplinary pain program if persistent >6 months |
| MRI lumbar spine | 6 weeks post-op (baseline), then PRN if symptoms recur | No residual compression; no recurrent herniation | Recurrent herniation: revision surgery if symptomatic |
| EMG/NCS | 3 months post-onset (if persistent deficits) | Reinnervation signs; improving motor unit potentials | No reinnervation at 3-6 months → guarded prognosis; continued rehabilitation; adaptive strategies |
| Depression/psychological screening (PHQ-9) | Each visit | PHQ-9 <5 | SSRI; psychological referral; support group (CES Association) |
| Functional assessment (Oswestry Disability Index, SF-36) | 3 months, 6 months, 12 months | Improving scores | Intensify rehabilitation; address barriers; vocational rehabilitation |

---

## 7. DISPOSITION CRITERIA

### Admission Criteria

| Level of Care | Criteria |
|---------------|----------|
| ICU admission | Post-operative monitoring (surgeon-dependent — many post-laminectomies go to floor); bilateral lower extremity paralysis with hemodynamic concerns; epidural abscess with sepsis; significant comorbidities affecting anesthetic recovery; autonomic dysfunction |
| General neurosurgery/spine floor | ALL CES patients require admission; pre-operative CES awaiting surgical decompression; post-operative monitoring; pain management; bladder/bowel monitoring; PT/OT initiation; epidural abscess requiring IV antibiotics |
| Observation (NOT appropriate) | CES is NEVER an observation diagnosis — all suspected CES patients require emergent MRI and admission for surgical evaluation; even if MRI is negative for structural compression, admission for monitoring is prudent if clinical suspicion is high |

### Discharge Criteria

| Criterion | Details |
|-----------|---------|
| Neurologic stability | Stable or improving neurologic exam for ≥24-48h post-surgery; no progressive deficits |
| Pain controlled | Adequate pain control on oral medications; able to participate in PT |
| Bladder management plan | Voiding spontaneously with PVR <100 mL OR CIC teaching completed and patient/caregiver competent; urology follow-up arranged |
| Bowel function | BM occurred; bowel regimen established; patient educated on bowel program |
| Wound healing | Surgical wound clean, dry, intact; no signs of infection; wound care instructions provided |
| Mobility assessment | PT clearance; safe ambulation (with or without assistive device); home safety assessment; OR inpatient rehab transfer |
| DVT prophylaxis plan | Pharmacologic prophylaxis continuing (enoxaparin for 2-4 weeks post-op per surgeon protocol); or transitioned to mobilization-based prevention |
| Follow-up arranged | Spine surgery (2 weeks), urology (4-6 weeks), PM&R (2-4 weeks if deficits), PCP (1 week), pelvic floor PT (after surgical clearance) |
| Patient/family education | Activity restrictions (lifting, bending, twisting restrictions per surgeon — typically 6 weeks); when to return to ED (new weakness, loss of bladder/bowel function, fever, wound drainage); CIC technique if applicable; bowel program; realistic expectations for recovery timeline |

### Discharge Prescriptions Checklist

| Medication | Details |
|-----------|---------|
| Analgesics | Acetaminophen scheduled; limited opioid PRN with taper plan (2-4 weeks); avoid prolonged opioids |
| Neuropathic pain agent | Gabapentin or pregabalin if radicular/neuropathic pain |
| Bowel regimen | Docusate + senna (especially if on opioids); PRN bisacodyl |
| DVT prophylaxis | Enoxaparin 40 mg SQ daily x 2-4 weeks (per surgeon protocol) |
| Antibiotics (if abscess) | Completion of IV antibiotics (arrange PICC and home IV antibiotics); typically 6-8 weeks total course |
| CIC supplies (if applicable) | Catheters, lubricant, collection bags; home health nursing for CIC training reinforcement |
| Stool softeners | Ongoing bowel program medications |

---

## 8. EVIDENCE & REFERENCES

### Key Guidelines

| Guideline | Source | Year | Key Recommendation |
|-----------|--------|------|-------------------|
| Cauda Equina Syndrome Standards of Care | British Association of Spine Surgeons (BASS) / Society of British Neurological Surgeons (SBNS) | 2020 | CES is a surgical emergency; MRI within 4h; surgical decompression within 24h (ideally ASAP); classify CES-I vs. CES-R; bladder scan is essential triage tool |
| CES Emergency Pathway | NICE / NHS England | 2018 (updated 2023) | Suspected CES → emergent MRI → same-day surgical review; do NOT delay MRI; 24/7 access to MRI required; document timeline meticulously |
| AANS/CNS Guidelines on Lumbar Disc Herniation | AANS/CNS Joint Section on Disorders of the Spine and Peripheral Nerves | 2014 | CES from disc herniation is a surgical emergency; emergent decompression recommended |

### Landmark Studies

| Study | Finding | Impact |
|-------|---------|--------|
| [Ahn et al. (2000)](https://pubmed.ncbi.nlm.nih.gov/10851100/) | Systematic review: Decompression <48h of CES onset → 70% bladder recovery vs. 30% if >48h; motor outcomes also significantly better with early surgery | Established 48h as important threshold; but sooner is always better |
| [Todd (2005)](https://pubmed.ncbi.nlm.nih.gov/16455534/) — Meta-analysis | 42 studies: Earlier decompression consistently associated with better outcomes across motor, bladder, and bowel domains; no clear cutoff but <24h is optimal | Confirmed urgency of CES surgical decompression; surgical timing is KEY modifiable factor |
| Srikandarajah et al. (2020) | UK Cohort: Urgent surgery (<24h) vs. delayed (>24h): better bladder outcomes (OR 2.1) and motor outcomes (OR 1.6) with urgent surgery | Modern evidence supporting <24h surgical timing; NHS pathway development |
| DeBois et al. (2019) | Timing analysis: <12h, 12-24h, 24-48h, >48h: progressive decline in outcomes with each delay interval; <12h had best bladder recovery | Supports as-soon-as-possible approach; <12h may be ideal |
| [Gleave & Macfarlane (2002)](https://pubmed.ncbi.nlm.nih.gov/12389883/) | CES-I vs. CES-R outcomes: CES-I (incomplete) with early surgery → 95% good bladder outcome; CES-R (retention) with early surgery → 53% good bladder outcome; CES-R with delayed surgery → 27% good outcome | Established CES-I vs. CES-R classification; demonstrated that retention onset is critical prognostic marker |
| [Groen & Ponssen (1990)](https://pubmed.ncbi.nlm.nih.gov/2243224/) | Spinal epidural hematoma: better outcomes with surgery <12h of onset; anticoagulation most common cause | Established surgical urgency for hematoma-related CES |
| [Kostuik et al. (1986)](https://pubmed.ncbi.nlm.nih.gov/2936744/) | Classic paper on CES natural history: untreated CES from disc herniation → permanent bladder dysfunction in >90%, persistent weakness in >70%, chronic pain in >80% | Established that CES without surgical treatment leads to devastating permanent deficits |
| McCarthy et al. (2014) | Medicolegal analysis: CES is the most litigated condition in spinal surgery; delayed diagnosis is the most common reason for successful claims; failure to perform timely MRI and delayed surgery are key factors | Documentation of timeline is CRITICAL; standardized CES pathways reduce medicolegal risk |

### Clinical Classification

**CES Subtypes (Gleave & Macfarlane Classification)**

| Subtype | Definition | Key Features | Prognosis |
|---------|-----------|--------------|-----------|
| CES-Suspected (CES-S) | Bilateral radiculopathy/symptoms WITHOUT bladder dysfunction | Bilateral leg pain/weakness; bilateral sensory changes; NO urinary symptoms; normal PVR | Best prognosis; may not progress to CES if decompressed promptly; but ~70% will progress to CES-I or CES-R without surgery |
| CES-Incomplete (CES-I) | Altered urinary function WITHOUT retention | Difficulty initiating stream; reduced sensation of voiding; urgency; partial retention (PVR 200-500 mL); reduced but present perineal sensation; reduced anal tone | Good prognosis with early surgery: 95% good bladder outcome (Gleave & Macfarlane, 2002) |
| CES-Retention (CES-R) | Painless urinary retention WITH overflow incontinence | Painless retention (PVR >500 mL); overflow incontinence; absent perineal sensation; absent anal tone; often absent bulbocavernosus reflex | Poorer prognosis: 53% good outcome with early surgery; 27% with delayed surgery |

**Examination Checklist for CES**

| Component | Bilateral L4 | Bilateral L5 | Bilateral S1 | S2-S4 (Sacral roots) |
|-----------|-------------|-------------|-------------|----------------------|
| Motor | Knee extension (quad) | Ankle dorsiflexion (TA), great toe extension (EHL), hip abduction | Ankle plantarflexion (gastroc); hip extension (gluteus max) | Anal sphincter tone (DRE); bulbocavernosus reflex |
| Sensory | Medial leg/shin | Lateral leg, dorsum of foot, first web space | Lateral foot, sole, posterior calf | Perianal (S2-S5); perineum; posterior thigh; "saddle area" |
| Reflex | Patellar (L3-L4) | Tibialis posterior (L5 — inconsistent) | Achilles ankle jerk (S1-S2) | Anocutaneous reflex ("anal wink"); bulbocavernosus reflex (S2-S4) |
| Function | Walking, stairs | Heel walking | Toe walking | Bladder: voiding, PVR; Bowel: rectal sensation, tone; Sexual: erectile function, genital sensation |

---

## APPENDICES

### Appendix A: CES Etiologies and Frequency

| Etiology | Frequency | Key Features | Treatment |
|----------|-----------|--------------|-----------|
| Lumbar disc herniation (massive central) | 45-50% | Most common cause; L4-L5 or L5-S1 most frequent; large central or central-lateral fragment; may follow heavy lifting, trauma, or spontaneous | Emergent laminectomy + discectomy |
| Lumbar spinal stenosis (severe) | 15-20% | Chronic stenosis with acute-on-chronic decompensation; multilevel; often older patients; spondylolisthesis may contribute | Decompressive laminectomy ± fusion for instability |
| Tumor (primary or metastatic) | 10-15% | Intradural-extramedullary (schwannoma, meningioma, ependymoma); extradural (metastasis, myeloma); progressive course; may be insidious or acute | Surgical resection ± radiation; dexamethasone if edema |
| Epidural abscess | 5-10% | Fever; IVDU; recent procedure; immunocompromised; ESR/CRP elevated; subacute course (days to weeks); S. aureus most common | Surgical drainage + IV antibiotics (6-8 weeks) |
| Epidural hematoma | 3-5% | Anticoagulation; post-procedural; coagulopathy; acute onset with rapid progression | Emergent hematoma evacuation; reverse anticoagulation |
| Trauma / fracture | 3-5% | Burst fracture with retropulsed fragments; sacral fracture; seatbelt injury; high-energy mechanism | Surgical stabilization and decompression |
| Post-operative (complication) | 2-3% | After lumbar surgery (hematoma, retained fragment, excessive retraction); onset hours to days after initial surgery | Revision surgery; evacuate hematoma; remove retained fragment |
| Inflammatory (sarcoidosis, arachnoiditis) | 1-2% | Nerve root clumping (arachnoiditis); enhancing roots (sarcoidosis); chronic progressive; often diagnosis of exclusion | Immunosuppression (sarcoidosis); limited options for arachnoiditis (intrathecal steroids controversial) |
| Vascular (AVM, dural AV fistula) | <1% | Progressive myelopathy/CES; dilated vessels on MRI; may have episodic worsening; can cause venous congestion of conus/cauda equina | Endovascular embolization; surgical ligation |
| Chiropractic manipulation (iatrogenic) | Rare but reported | Disc herniation during manipulation; acute onset during or immediately after treatment | Emergent surgical decompression |

### Appendix B: CES Emergency Pathway

```
SUSPECTED CAUDA EQUINA SYNDROME
(Bilateral radiculopathy + ANY of: bladder dysfunction, saddle anesthesia, bowel dysfunction, bilateral weakness)
                    │
                    ├── TRIAGE (within 15 minutes of arrival)
                    │     • Bladder scan (PVR) — STAT
                    │     • Digital rectal exam — perianal sensation + anal tone
                    │     • Document bilateral LE strength + sensation
                    │     • Document time of symptom onset
                    │
                    ├── PVR Result?
                    │     PVR >500 mL → CES-Retention → EMERGENT MRI + Surgery ASAP
                    │     PVR 200-500 mL → CES-Incomplete → URGENT MRI + Surgery within 24h
                    │     PVR <200 mL → CES less likely BUT:
                    │           If saddle anesthesia + bilateral symptoms → URGENT MRI anyway
                    │           If no CES features → standard radiculopathy workup
                    │
                    ├── Order MRI STAT (lumbar spine, without contrast initially)
                    │     Target: MRI within 1-4 hours of presentation
                    │     If MRI unavailable → CT myelogram OR transfer to MRI-capable facility
                    │
                    ├── Contact Spine Surgery IMMEDIATELY (concurrent with MRI)
                    │     Do NOT wait for MRI results to call
                    │
                    ├── MRI Results:
                    │     Structural compression confirmed → Emergent surgical decompression
                    │     │     • Disc herniation → Laminectomy + discectomy
                    │     │     • Abscess → Drainage + antibiotics
                    │     │     • Tumor → Decompression ± dexamethasone
                    │     │     • Hematoma → Evacuation + reverse anticoagulation
                    │     │
                    │     No structural compression → Consider:
                    │           • GBS (CSF, NCS)
                    │           • Inflammatory (sarcoidosis, arachnoiditis)
                    │           • Vascular (AV fistula)
                    │           • Reconsider diagnosis (conus, FND)
                    │
                    └── Post-Operative:
                          • Neurologic checks q4h x 48h
                          • Trial of void at 24-48h → PVR check
                          • PT/OT within 24h
                          • Document all timelines meticulously
```

### Appendix C: CES vs. Conus Medullaris Syndrome — Comparison

| Feature | Cauda Equina Syndrome | Conus Medullaris Syndrome |
|---------|----------------------|--------------------------|
| Anatomic level | Below L1-L2 (nerve roots only) | T12-L2 (spinal cord terminus) |
| Motor | Asymmetric (root distribution); LMN pattern; atrophy; fasciculations | Symmetric; may have UMN signs (Babinski, spasticity) AND LMN signs |
| Sensory | "Saddle" anesthesia (perianal S2-S5); asymmetric; radicular pattern; dermatomal | Symmetric saddle anesthesia; bilateral; may have dissociated sensory loss |
| Pain | Severe radicular pain; unilateral or bilateral; often prominent | Less prominent pain; may have visceral-type pain |
| Reflexes | Absent ankle jerks; reduced patellar reflexes | Ankle jerks absent; Babinski may be present (UMN component); bulbocavernosus reflex absent |
| Bladder | Late onset (may be subtle initially → progression to retention) | Early and prominent (often presenting feature); areflexic bladder |
| Bowel | Late; often preserved initially | Early; constipation and incontinence |
| Sexual function | Late; asymmetric erectile dysfunction | Early; bilateral |
| Onset | Often acute (disc herniation); can be subacute | May be more gradual; depends on etiology |
| MRI finding | Compressive lesion below L1-L2; compressed nerve roots | Lesion at T12-L2; intramedullary conus signal change; may have cord expansion |

### Appendix D: Recovery Timeline and Expectations

| Function | Expected Recovery Timeline | Prognostic Factors | Long-term Outcome |
|----------|--------------------------|-------------------|-------------------|
| Motor (leg strength) | Begins within days-weeks; majority of recovery in first 6 months; continues up to 12-18 months | Pre-operative motor grade; duration of deficit before surgery; CES-I vs. CES-R | 80-90% recover functional ambulation if decompressed within 24-48h; foot drop may be slow/incomplete |
| Bladder | Slowest to recover; may take 6-12 months; initial period of retention → may evolve to urgency/frequency → hopefully normalizes | MOST IMPORTANT: PVR at presentation (retention = worse); surgical timing (<24h = better); bilateral vs. unilateral root involvement | 70% recover useful bladder function if <48h surgery (Ahn et al.); 30-50% persistent dysfunction in CES-R; CIC may be lifelong |
| Bowel | Moderate recovery; weeks to months; fecal urgency common before continence improves | Degree of S2-S4 denervation; surgical timing | 60-70% recover satisfactory continence; 10-20% have persistent fecal incontinence |
| Sexual function | Variable; months to years; often incomplete | S2-S4 root recovery; psychological factors; pre-existing function | 40-70% report persistent sexual dysfunction; male erectile dysfunction common; female genital sensation changes; psychological impact significant |
| Pain | Radicular pain often improves rapidly post-decompression; neuropathic pain may persist or develop over weeks; chronic pain syndrome in 20-40% | Nerve root damage severity; psychological comorbidity; chronicity before surgery | 20-40% develop chronic neuropathic pain syndrome; multimodal management needed |
| Overall | Most recovery occurs in first 6-12 months; slower improvement may continue up to 2 years; deficits persisting beyond 2 years are likely permanent | Surgical timing; pre-operative deficit severity; CES-I vs. CES-R; age; comorbidities | Quality of life significantly impacted in 30-50% long-term; multidisciplinary rehabilitation and psychological support essential |

### Appendix E: Medicolegal Considerations

| Issue | Documentation Required | Risk Mitigation |
|-------|----------------------|-----------------|
| Time of symptom onset | Exact time; patient and family statement; ambulance records | Standardized CES screening tool in ED triage |
| Time of ED arrival | Triage time stamp; registration time | Electronic health record timestamps |
| Time of clinical assessment | Time of exam documented; neurologic exam details; bladder assessment | Dedicated CES assessment proforma |
| Time of MRI request | Order time stamp; radiology communication log | Standardized CES pathway with MRI within 4h target |
| Time of MRI completion | MRI completion time; radiology read time | Prioritized MRI slot for suspected CES |
| Time of surgical consultation | Time called; time responded; time seen by surgeon | Documented communication; spine surgery contact log |
| Time of surgical decompression | Anesthesia start time; knife-to-skin time; case end time | OR availability for emergency CES cases |
| Neurologic exam pre/post-surgery | Detailed exam with motor grading, sensory mapping, rectal tone, PVR | Standardized CES neurologic assessment form |
| Delays and reasons | If any delay: documented reason (MRI availability, OR availability, patient consent, medical optimization) | Contemporaneous notes; clear communication to patient/family about delays |
| Informed consent | Surgical risks discussed; prognosis discussed; realistic expectations documented; patient questions addressed | Standardized consent form for CES decompression |

---

*This template represents the initial build phase (Skill 1) and requires validation through the checker pipeline (Skills 2-6) before clinical deployment.*
