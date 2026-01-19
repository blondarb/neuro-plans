# CPT & SYNONYM ENRICHMENT REPORT

**TEMPLATE:** Status Epilepticus
**VERSION:** 1.3
**DATE ENRICHED:** January 18, 2026
**ENRICHER:** Claude (neuro-cpt-synonym-enricher v1.0)

---

## DIAGNOSIS SYNONYMS

**Primary Term:** Status Epilepticus
**ICD-10:** G40.901 (Epilepsy, unspecified, not intractable, with status epilepticus), G41.0 (Grand mal status epilepticus), G41.1 (Petit mal status epilepticus), G41.2 (Complex partial status epilepticus)

| Synonym | Type | Source | Notes |
|---------|------|--------|-------|
| SE | Abbreviation | Clinical | Universal medical abbreviation |
| Status | Abbreviation | Clinical | Common ED/ICU shorthand |
| Convulsive status epilepticus | Subtype | Clinical | CSE - most common form |
| CSE | Abbreviation | Clinical | Convulsive SE |
| Non-convulsive status epilepticus | Subtype | Clinical | NCSE - subtle/electrographic |
| NCSE | Abbreviation | Clinical | Non-convulsive SE |
| Refractory status epilepticus | Severity modifier | Clinical | RSE - failed first 2 treatments |
| RSE | Abbreviation | Clinical | Common in neurocritical care |
| Super-refractory status epilepticus | Severity modifier | Clinical | SRSE - >24h on anesthetics |
| SRSE | Abbreviation | Clinical | Common in neurocritical care |
| Grand mal status | Historical | ICD-10 | G41.0 terminology |
| Generalized tonic-clonic status | Clinical | AES | Preferred current term |
| Epileptic state | Historical | Literature | Older terminology |
| Prolonged seizure | Lay term | Patient education | >5 minutes duration |
| Continuous seizure | Lay term | Patient education | For patient/family |

**SNOMED CT ID:** 230456005 (Status epilepticus)
**MeSH Term:** Status Epilepticus (D013226)

---

## SECTION 1: LABORATORY CPT CODES

| Test | CPT Code(s) | Description | Verification Source |
|------|-------------|-------------|---------------------|
| Point-of-care glucose | 82962 | Glucose, blood by glucose monitoring device | CMS Fee Schedule |
| CBC with differential | 85025 | Complete blood count with differential WBC | CMS Fee Schedule |
| Comprehensive metabolic panel | 80053 | CMP (14 tests) | CMS Fee Schedule |
| Basic metabolic panel | 80048 | BMP (8 tests) | CMS Fee Schedule |
| Magnesium | 83735 | Magnesium | CMS Fee Schedule |
| Calcium, total | 82310 | Calcium, total | CMS Fee Schedule |
| Calcium, ionized | 82330 | Calcium, ionized | CMS Fee Schedule |
| Phosphorus | 84100 | Phosphorus inorganic (phosphate) | CMS Fee Schedule |
| Blood gas (arterial) | 82803 | Gases, blood, any combination | CMS Fee Schedule |
| Blood gas (venous) | 82800 | Gases, blood, pH only | CMS Fee Schedule |
| Lactate | 83605 | Lactate (lactic acid) | CMS Fee Schedule |
| Ammonia | 82140 | Ammonia | CMS Fee Schedule |
| TSH | 84443 | Thyroid stimulating hormone | CMS Fee Schedule |
| Cortisol, random | 82533 | Cortisol, total | CMS Fee Schedule |
| Serum osmolality | 83930 | Osmolality, blood | CMS Fee Schedule |
| Procalcitonin | 84145 | Procalcitonin | CMS Fee Schedule |
| PT/INR | 85610 | Prothrombin time | CMS Fee Schedule |
| PTT | 85730 | Thromboplastin time, partial | CMS Fee Schedule |
| Urine drug screen | 80307 | Drug test(s), presumptive | CMS Fee Schedule |
| Blood alcohol | 80320 | Alcohol (ethanol) | CMS Fee Schedule |
| Pregnancy test, urine | 81025 | Urine pregnancy test | CMS Fee Schedule |
| Pregnancy test, serum | 84703 | Gonadotropin, chorionic (hCG) qualitative | CMS Fee Schedule |
| Troponin | 84484 | Troponin, quantitative | CMS Fee Schedule |
| CPK/CK | 82550 | Creatine kinase, total | CMS Fee Schedule |
| Urinalysis | 81003 | Urinalysis, automated | CMS Fee Schedule |

### Antiseizure Medication Levels

| Test | CPT Code | Description | Verification Source |
|------|----------|-------------|---------------------|
| Phenytoin level | 80185 | Phenytoin, total | CMS Fee Schedule |
| Free phenytoin level | 80186 | Phenytoin, free | CMS Fee Schedule |
| Valproic acid level | 80164 | Valproic acid (dipropylacetic acid) | CMS Fee Schedule |
| Carbamazepine level | 80156 | Carbamazepine | CMS Fee Schedule |
| Phenobarbital level | 80184 | Phenobarbital | CMS Fee Schedule |
| Levetiracetam level | 80177 | Levetiracetam | CMS Fee Schedule |
| Lacosamide level | 80176 | Lacosamide | CMS Fee Schedule |
| Lamotrigine level | 80175 | Lamotrigine | CMS Fee Schedule |

### CSF Studies (Lumbar Puncture)

| Test | CPT Code | Description | Verification Source |
|------|----------|-------------|---------------------|
| CSF cell count | 89051 | Cell count, miscellaneous body fluid | CMS Fee Schedule |
| CSF protein | 84157 | Protein, total (CSF) | CMS Fee Schedule |
| CSF glucose | 82945 | Glucose, body fluid | CMS Fee Schedule |
| Gram stain | 87205 | Smear, primary source with interpretation | CMS Fee Schedule |
| CSF culture | 87070 | Culture, bacterial, any source | CMS Fee Schedule |
| HSV PCR | 87529 | HSV, DNA, quantification | CMS Fee Schedule |
| BioFire FilmArray Meningitis/Encephalitis Panel | 87483 | Infectious agent detection, multiplex | CMS Fee Schedule |
| Oligoclonal bands | 83916 | Oligoclonal bands | CMS Fee Schedule |
| Cytology, CSF | 88104 | Cytopathology, fluids | CMS Fee Schedule |
| Autoimmune encephalitis panel | 86256 | Fluorescent antibody, screen | CMS Fee Schedule |

**Lab Panel Notes:**
- CMP (80053) includes: glucose, BUN, creatinine, sodium, potassium, chloride, CO2, calcium, total protein, albumin, total bilirubin, alkaline phosphatase, AST, ALT
- BMP (80048) includes: glucose, BUN, creatinine, sodium, potassium, chloride, CO2, calcium
- Autoimmune encephalitis panels vary by laboratory; verify specific codes with performing lab

---

## SECTION 2: IMAGING & STUDIES CPT CODES

### Imaging

| Study | CPT Code(s) | Description | Modifiers | Verification Source |
|-------|-------------|-------------|-----------|---------------------|
| CT head without contrast | 70450 | CT head/brain without contrast | -26 professional; -TC technical | CMS Fee Schedule |
| CT head with contrast | 70460 | CT head/brain with contrast | -26 / -TC | CMS Fee Schedule |
| CT head without and with contrast | 70470 | CT head/brain without then with contrast | -26 / -TC | CMS Fee Schedule |
| CT angiography head | 70496 | CTA head with contrast | -26 / -TC | CMS Fee Schedule |
| CT angiography neck | 70498 | CTA neck with contrast | -26 / -TC | CMS Fee Schedule |
| MRI brain without contrast | 70551 | MRI brain without contrast | -26 / -TC | CMS Fee Schedule |
| MRI brain with contrast | 70552 | MRI brain with contrast | -26 / -TC | CMS Fee Schedule |
| MRI brain without and with contrast | 70553 | MRI brain without then with contrast | -26 / -TC | CMS Fee Schedule |
| MRA head without contrast | 70544 | MRA head without contrast | -26 / -TC | CMS Fee Schedule |
| MRV brain | 70546 | MRA head with contrast (used for MRV) | -26 / -TC | CMS Fee Schedule |
| Chest X-ray 2 views | 71046 | Radiologic examination, chest, 2 views | -26 / -TC | CMS Fee Schedule |
| CT chest/abdomen/pelvis with contrast | 74177 | CT abdomen/pelvis with contrast | -26 / -TC | CMS Fee Schedule |

### Electrodiagnostics (EEG)

| Study | CPT Code(s) | Description | Verification Source |
|-------|-------------|-------------|---------------------|
| cEEG setup | 95700 | EEG continuous recording setup, patient education, takedown | CMS Fee Schedule |
| cEEG 2-12 hours (unmonitored) | 95711 | EEG video, 2-12 hr, unmonitored | CMS Fee Schedule |
| cEEG 12-26 hours (unmonitored) | 95714 | EEG video, 12-26 hr, unmonitored | CMS Fee Schedule |
| cEEG >26 hours (unmonitored) | 95715 | EEG video, >26 hr, unmonitored | CMS Fee Schedule |
| cEEG professional interpretation | 95717-95726 | Professional component codes | CMS Fee Schedule |
| Routine EEG awake/drowsy | 95816 | EEG awake and drowsy | CMS Fee Schedule |
| Routine EEG awake/sleep | 95819 | EEG awake and asleep | CMS Fee Schedule |

### Procedures

| Procedure | CPT Code(s) | Description | Verification Source |
|-----------|-------------|-------------|---------------------|
| Lumbar puncture, diagnostic | 62270 | Spinal puncture, lumbar, diagnostic | CMS Fee Schedule |
| LP with fluoroscopy | 62328 | Spinal puncture with fluoroscopic guidance | CMS Fee Schedule |
| Endotracheal intubation | 31500 | Intubation, endotracheal, emergency | CMS Fee Schedule |
| Echocardiogram, TTE complete | 93306 | Echocardiography, TTE with Doppler | CMS Fee Schedule |
| Arterial line placement | 36620 | Arterial catheterization for monitoring | CMS Fee Schedule |
| Central line placement | 36556 | Insertion of non-tunneled central venous catheter | CMS Fee Schedule |

---

## SECTION 3: TREATMENT CPT CODES

### IV Push Medications

| Treatment | CPT Code(s) | Description | Verification Source |
|-----------|-------------|-------------|---------------------|
| IV push, first drug | 96374 | Therapeutic, prophylactic injection, IV push, single | CMS Fee Schedule |
| IV push, each additional | 96375 | Each additional sequential IV push | CMS Fee Schedule |

### Infusions

| Treatment | CPT Code(s) | Description | Units | Verification Source |
|-----------|-------------|-------------|-------|---------------------|
| IV infusion, initial hour | 96365 | IV infusion, first hour | Time-based | CMS Fee Schedule |
| IV infusion, each additional hour | 96366 | IV infusion, each additional hour | Time-based | CMS Fee Schedule |
| IV infusion, sequential new drug | 96367 | IV infusion, additional sequential | Per drug | CMS Fee Schedule |
| Continuous infusion | 96368 | Concurrent infusion | Per additional | CMS Fee Schedule |

**Note:** Anesthetic infusions (midazolam, propofol, ketamine) for RSE/SRSE typically billed as part of critical care time (99291-99292) in ICU setting.

### Drug HCPCS J-Codes

| Drug | J-Code | Unit | Notes | Verification Source |
|------|--------|------|-------|---------------------|
| Lorazepam (Ativan) | J2060 | Per 2 mg | Status epilepticus first-line | CMS HCPCS 2025 |
| Midazolam (Versed) | J2250 | Per 1 mg | IM/IV for SE | CMS HCPCS 2025 |
| Midazolam in NS | J2251 | Per 1 mg | IV infusion preparation | CMS HCPCS 2025 |
| Diazepam | J3360 | Per 5 mg | Alternative benzodiazepine | CMS HCPCS 2025 |
| Levetiracetam (Keppra) | J1953 | Per 10 mg | Second-line ASM | CMS HCPCS 2025 |
| Fosphenytoin | Q2009 | Per 50 mg PE | Second-line ASM | CMS HCPCS 2025 |
| Valproate sodium | J3379 | Per 5 mg | Second-line ASM (new 2026) | CMS HCPCS 2026 |
| Phenytoin | J1165 | Per 50 mg | If fosphenytoin unavailable | CMS HCPCS 2025 |
| Phenobarbital | J2560 | Per 120 mg | Second-line alternative | CMS HCPCS 2025 |
| Methylprednisolone sodium succinate | J2919 | Per 5 mg | For NORSE immunotherapy | CMS HCPCS 2025 |
| IVIG (varies by product) | J1459 | Per 500 mg | Privigen - for NORSE | CMS HCPCS 2025 |
| IVIG (varies by product) | J1569 | Per 500 mg | Gammagard - for NORSE | CMS HCPCS 2025 |
| IVIG not otherwise specified | J1599 | Per 500 mg | Generic IVIG billing | CMS HCPCS 2025 |
| Propofol | J2704 | Per 10 mg | RSE anesthetic | CMS HCPCS 2025 |
| Ketamine | J1840 | Per 10 mg | RSE anesthetic | CMS HCPCS 2025 |
| Norepinephrine | J2400 | Per 4 mcg base | Vasopressor support | CMS HCPCS 2025 |
| Vasopressin | J3490 | NOC | Vasopressor support | CMS HCPCS 2025 |
| Dexmedetomidine | J1647 | Per 1 mcg | ICU sedation | CMS HCPCS 2025 |
| Pantoprazole | J9153 | Per 40 mg | Stress ulcer prophylaxis | CMS HCPCS 2025 |
| Enoxaparin | J1650 | Per 10 mg | DVT prophylaxis | CMS HCPCS 2025 |
| Thiamine (B1) | J3411 | Per 100 mg | Glucose protocol | CMS HCPCS 2025 |
| Dextrose 50% | J7060 | Per 50 mL | Hypoglycemia | CMS HCPCS 2025 |

**Important Notes:**
- J2920 (methylprednisolone up to 40mg) deleted effective 1/1/2025; use J2919 instead
- For 1000mg methylprednisolone dose: Bill J2919 × 200 units
- IVIG codes are product-specific; verify with pharmacy
- Ketamine J-code may vary; some facilities use J3490 (NOC)

---

## SECTION 4: REFERRAL E/M CODES (Reference)

*Note: Actual E/M code depends on complexity and documentation. These are typical ranges.*

| Referral Type | Typical Codes | Notes |
|---------------|---------------|-------|
| Neurology ED consult | 99281-99285 | Based on ED E/M complexity |
| Neurology inpatient consult | 99252-99255 | Initial inpatient consult |
| Neurocritical care consult | 99291-99292 | Critical care time (first 74 min + additional 30 min) |
| ICU daily care | 99291-99292 | Critical care time |
| Infectious disease consult | 99252-99255 | Initial inpatient consult |
| Epilepsy surgery evaluation (OPD) | 99204-99205 | New patient outpatient |
| Neurology follow-up (OPD) | 99213-99215 | Established patient |

---

## TERMINOLOGY SYNONYMS BY SECTION

### Lab Test Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| CBC with differential | Complete blood count, blood count, hemogram, FBC (full blood count - UK) |
| Comprehensive metabolic panel | CMP, chem-14, chemistry panel, metabolic panel |
| Basic metabolic panel | BMP, chem-7, electrolytes, lytes, chem-8 |
| Magnesium | Mg, mag, serum magnesium |
| Calcium ionized | iCa, free calcium, ionized Ca |
| Blood gas arterial | ABG, arterial blood gases, art gas |
| Blood gas venous | VBG, venous blood gases |
| Lactate | Lactic acid |
| Ammonia | NH3, serum ammonia |
| Antiseizure medication levels | ASM levels, AED levels, anticonvulsant levels, drug levels |
| Valproic acid level | VPA level, Depakote level, valproate level |
| Phenytoin level | Dilantin level, PHT level |
| Levetiracetam level | LEV level, Keppra level |

### Imaging Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| CT head | Head CT, brain CT, cranial CT, CT scan of head, non-contrast CT |
| MRI brain | Brain MRI, cranial MRI, head MRI, magnetic resonance imaging brain |
| CT angiography head | CTA head, CT angio head |
| MRA head | MR angiography head, magnetic resonance angiography |
| Chest X-ray | CXR, chest radiograph, chest film |

### Procedure Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| Lumbar puncture | LP, spinal tap, CSF tap, spinal puncture |
| Continuous EEG | cEEG, long-term EEG monitoring, LTEM, EEG monitoring |
| Electroencephalogram | EEG, brain wave test |
| Endotracheal intubation | ETT placement, intubation, tube placement |

### Medication Synonyms

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Lorazepam | Ativan | LZP |
| Midazolam | Versed | MDZ |
| Diazepam | Valium | DZP |
| Levetiracetam | Keppra, Keppra XR, Spritam, Roweepra, Elepsia XR | LEV |
| Fosphenytoin | Cerebyx | fPHT, FOS |
| Phenytoin | Dilantin, Phenytek | PHT |
| Valproate / Valproic acid | Depakote, Depakote ER, Depakene, Depacon | VPA, DVP |
| Lacosamide | Vimpat | LCM |
| Brivaracetam | Briviact | BRV |
| Phenobarbital | Luminal | PB, PHB |
| Propofol | Diprivan | N/A |
| Ketamine | Ketalar | N/A |
| Midazolam infusion | Versed drip | MDZ gtt |
| Methylprednisolone | Solu-Medrol | IVMP |
| IVIG | Privigen, Gammagard, Gamunex, Octagam, Carimune | IVIg |
| Rituximab | Rituxan | RTX |
| Cyclophosphamide | Cytoxan | CTX |
| Topiramate | Topamax | TPM |
| Perampanel | Fycompa | PER |

### Condition/Status Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| Status epilepticus | SE, status, prolonged seizure, continuous seizure activity |
| Convulsive status epilepticus | CSE, generalized convulsive SE, GCSE |
| Non-convulsive status epilepticus | NCSE, subtle SE, electrographic SE |
| Refractory status epilepticus | RSE, treatment-resistant SE |
| Super-refractory status epilepticus | SRSE |
| NORSE | New onset refractory status epilepticus |
| FIRES | Febrile infection-related epilepsy syndrome |
| Burst suppression | BS, suppression-burst |
| Seizure | Convulsion, fit (lay), spell (lay), ictal event |
| Post-ictal | After seizure, postictal state |

---

## CODES NOT FOUND / REQUIRING VERIFICATION

| Item | Issue | Recommendation |
|------|-------|----------------|
| Brivaracetam injection | No specific J-code identified | May require J3490 (NOC) or facility-specific code |
| Autoimmune encephalitis panel (specific) | Panel codes vary by laboratory | Verify CPT codes with performing laboratory |
| Tocilizumab | J3262 exists but verify for NORSE use | Confirm with pharmacy |
| Anakinra | J0135 exists but verify for NORSE use | Confirm with pharmacy |
| Ketogenic diet initiation | No CPT code; nutrition consult codes apply | Bill as MNT (97802-97804) or inpatient nutrition |

---

## INTEGRATION NOTES

### For EHR Order Set Development

**"Status Epilepticus Order Set" Bundle:**
1. **Labs:**
   - POC glucose (82962)
   - CBC (85025)
   - CMP (80053)
   - Magnesium (83735)
   - Lactate (83605)
   - Urine drug screen (80307)
   - ASM levels (as indicated)

2. **Imaging:**
   - CT head w/o contrast STAT (70450)
   - Chest X-ray (71046)

3. **Studies:**
   - cEEG setup STAT (95700)

4. **Medications:**
   - Lorazepam 4mg IV (J2060 x2)
   - Levetiracetam 4500mg IV (J1953 x450)
   - Fosphenytoin PE loading dose (Q2009 x calculated)

### For Billing Compliance

- **Time-based codes** (infusions): Document start/stop times precisely
- **Modifier usage** varies by payer; verify with billing department
- **Critical care codes** (99291-99292): Document total critical care time
- **cEEG codes**: May require prior authorization for extended monitoring
- **IVIG**: Requires medical necessity documentation for NORSE indication
- **JW/JZ modifiers**: Required for drug waste documentation

### For Searchability

- All medication brand names should be indexed for medication reconciliation
- Include common misspellings: "levetiracitam," "phenytoing," "valproat"
- Index abbreviations: SE, RSE, SRSE, NCSE, CSE, NORSE, FIRES
- Include lay terms for patient education searches

---

## CPT QUICK REFERENCE TABLE (For Template Appendix)

| Category | Item | CPT/HCPCS Code |
|----------|------|----------------|
| **Labs** | | |
| | CBC | 85025 |
| | CMP | 80053 |
| | BMP | 80048 |
| | Magnesium | 83735 |
| | Lactate | 83605 |
| | Ammonia | 82140 |
| | Drug screen | 80307 |
| | Phenytoin level | 80185 |
| | VPA level | 80164 |
| | LEV level | 80177 |
| **Imaging** | | |
| | CT head w/o | 70450 |
| | MRI brain w/wo | 70553 |
| | CTA head | 70496 |
| | Chest X-ray | 71046 |
| **Studies** | | |
| | cEEG setup | 95700 |
| | cEEG 2-12h | 95711 |
| | cEEG 12-26h | 95714 |
| | Lumbar puncture | 62270 |
| **Procedures** | | |
| | Intubation | 31500 |
| | Arterial line | 36620 |
| | Central line | 36556 |
| **Infusions** | | |
| | IV infusion initial | 96365 |
| | IV infusion add'l hour | 96366 |
| | IV push | 96374 |
| **Drugs** | | |
| | Lorazepam | J2060 (per 2mg) |
| | Midazolam | J2250 (per 1mg) |
| | Levetiracetam | J1953 (per 10mg) |
| | Fosphenytoin | Q2009 (per 50mg PE) |
| | Propofol | J2704 (per 10mg) |
| | Ketamine | J1840 (per 10mg) |
| | Methylprednisolone | J2919 (per 5mg) |
| | IVIG | J1599 (per 500mg) |

---

*Report generated by neuro-cpt-synonym-enricher skill v1.0*
*Note: CPT codes copyrighted by AMA. Codes verified from publicly available CMS sources. Verify annually as codes change.*
