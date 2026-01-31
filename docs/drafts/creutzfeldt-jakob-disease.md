---
title: "Creutzfeldt-Jakob Disease (CJD)"
description: "Clinical decision support for Creutzfeldt-Jakob disease (CJD) diagnosis, symptomatic management, and palliative care"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - neurodegenerative
  - prion-disease
  - dementia
  - rapidly-progressive-dementia
  - palliative
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Creutzfeldt-Jakob Disease (CJD)

**VERSION:** 1.0
**CREATED:** January 30, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Creutzfeldt-Jakob Disease (CJD)

**ICD-10:** A81.00 (Creutzfeldt-Jakob disease, unspecified), A81.01 (Variant Creutzfeldt-Jakob disease), A81.09 (Other Creutzfeldt-Jakob disease), A81.1 (Subacute sclerosing panencephalitis), A81.9 (Atypical virus infections of CNS, unspecified)

**CPT CODES:** 70553 (MRI brain with and without contrast), 95816 (EEG routine), 95950 (cEEG monitoring), 89051 (CSF cell count), 84157 (CSF protein), 82945 (CSF glucose), 83519 (14-3-3 protein, tau, NfL), 86235 (RT-QuIC), 81479 (PRNP gene sequencing), 88305 (Brain biopsy pathology), 70450 (CT head without contrast)

**SYNONYMS:** Creutzfeldt-Jakob disease, CJD, sporadic CJD, sCJD, variant CJD, vCJD, familial CJD, fCJD, iatrogenic CJD, iCJD, prion disease, transmissible spongiform encephalopathy, TSE, mad cow disease, bovine spongiform encephalopathy related, BSE-related CJD, spongiform encephalopathy, prion encephalopathy, Jakob-Creutzfeldt disease, subacute spongiform encephalopathy, rapid cognitive decline with myoclonus, prion dementia, human prion disease

**SCOPE:** Diagnostic workup, symptomatic management, and palliative care for suspected or confirmed Creutzfeldt-Jakob disease across all subtypes (sporadic, familial/genetic, iatrogenic, variant). Covers WHO/CDC diagnostic criteria application, biomarker interpretation (RT-QuIC, 14-3-3, tau), neuroimaging (MRI DWI cortical ribboning), EEG (periodic sharp wave complexes), PRNP genotyping, myoclonus management, infection control (prion decontamination), palliative care initiation, family counseling, genetic counseling for familial forms, and autopsy/National Prion Disease Pathology Surveillance Center referral. No disease-modifying treatment exists -- management is entirely supportive and palliative. For comprehensive RPD evaluation including treatable mimics, use the "Rapidly Progressive Dementia" template. For autoimmune encephalitis (key differential), use the "Autoimmune Encephalitis" template.

---

**DEFINITIONS:**

- **Sporadic CJD (sCJD):** Most common form (~85-90% of cases); arises spontaneously without identifiable risk factor; median age of onset 62 years; median survival 5-6 months
- **Familial/Genetic CJD (fCJD):** ~10-15% of cases; autosomal dominant PRNP mutations (E200K most common); includes familial CJD, Gerstmann-Straussler-Scheinker syndrome (GSS), and fatal familial insomnia (FFI)
- **Iatrogenic CJD (iCJD):** Transmission via contaminated surgical instruments, corneal transplants, dura mater grafts, human-derived growth hormone; extremely rare since modern precautions
- **Variant CJD (vCJD):** Linked to bovine spongiform encephalopathy (BSE/"mad cow disease"); younger onset (median age 28); prominent psychiatric symptoms early; "pulvinar sign" on MRI; primarily in UK/Europe; extremely rare currently

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| CBC with differential (CPT 85025) | STAT | STAT | ROUTINE | STAT | Baseline; infection screen; rule out hematologic causes of encephalopathy | Normal |
| CMP (CPT 80053) | STAT | STAT | ROUTINE | STAT | Metabolic encephalopathy screen (hepatic, renal, electrolyte); baseline before medications | Normal |
| TSH (CPT 84443), free T4 (CPT 84439) | URGENT | ROUTINE | ROUTINE | URGENT | Hashimoto encephalopathy (SREAT) is a treatable mimic; hypothyroid encephalopathy | Normal |
| B12 (CPT 82607), methylmalonic acid (MMA) (CPT 83921) | URGENT | ROUTINE | ROUTINE | URGENT | B12 deficiency is a reversible cause of cognitive decline; rule out before accepting prion diagnosis | B12 >300 pg/mL; MMA normal |
| ESR (CPT 85652) | URGENT | ROUTINE | ROUTINE | URGENT | Vasculitis screen; inflammatory conditions; normal in CJD (helps exclude autoimmune/inflammatory mimics) | Normal (<20 mm/h age-adjusted) |
| CRP (CPT 86140) | URGENT | ROUTINE | ROUTINE | URGENT | Inflammatory marker; elevated suggests non-prion etiology (autoimmune, infection, vasculitis) | Normal |
| RPR or VDRL (CPT 86592) | URGENT | ROUTINE | ROUTINE | URGENT | Neurosyphilis is a treatable RPD mimic | Non-reactive |
| HIV 1/2 antigen/antibody (CPT 87389) | URGENT | ROUTINE | ROUTINE | URGENT | HIV-associated neurocognitive disorder; opportunistic infections | Negative |
| Ammonia (CPT 82140) | URGENT | ROUTINE | - | URGENT | Hepatic encephalopathy mimic | Normal (<35 micromol/L) |
| Blood glucose (CPT 82947) | STAT | STAT | ROUTINE | STAT | Hypoglycemia; diabetic encephalopathy | Normal |
| Urinalysis (CPT 81003) + urine culture | STAT | ROUTINE | ROUTINE | STAT | UTI causing delirium superimposed on CJD | Negative |
| Urine drug screen | URGENT | ROUTINE | - | URGENT | Substance-related cognitive impairment; drug toxicity | Negative or expected medications only |

### 1B. Extended Workup (Second-line)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| Anti-thyroid antibodies (anti-TPO, anti-thyroglobulin) | - | ROUTINE | ROUTINE | - | Hashimoto encephalopathy (SREAT) -- treatable with steroids; can mimic CJD | Negative (positive + encephalopathy = consider SREAT) |
| ANA (CPT 86235) | - | ROUTINE | ROUTINE | - | Lupus cerebritis; systemic autoimmune disease mimicking RPD | Negative |
| Autoimmune encephalitis panel (serum) -- NMDAR, LGI1, CASPR2, GABA-B, GABA-A, AMPA, DPPX, IgLON5 | - | ROUTINE | ROUTINE | - | Treatable autoimmune encephalitis is the most important reversible CJD mimic to identify | Negative |
| Paraneoplastic panel (serum) -- comprehensive (ANNA-1/Hu, ANNA-2/Ri, CRMP-5, amphiphysin, PCA-1/Yo, GAD65) | - | ROUTINE | ROUTINE | - | Paraneoplastic encephalitis can mimic CJD presentation | Negative |
| Folate (CPT 82746) | - | ROUTINE | ROUTINE | - | Deficiency associated with cognitive impairment | Normal |
| LDH | - | ROUTINE | ROUTINE | - | Lymphoma; intravascular lymphoma (CJD mimic) | Normal |
| Peripheral blood smear | - | ROUTINE | - | - | Intravascular lymphoma (schistocytes); TTP | Normal |
| ACE level (serum) | - | ROUTINE | ROUTINE | - | Neurosarcoidosis | Normal |
| Serum protein electrophoresis (SPEP) (CPT 86334) + immunofixation | - | ROUTINE | ROUTINE | - | CNS lymphoma; POEMS; paraneoplastic | Normal pattern |
| Thiamine (B1) level (CPT 84425) | - | ROUTINE | ROUTINE | - | Wernicke encephalopathy -- reversible with treatment | Normal (>70 nmol/L) |
| Copper (CPT 82390) and ceruloplasmin | - | ROUTINE | ROUTINE | - | Wilson disease (if age <50) | Normal |

### 1C. Rare/Specialized (Prion-Specific and Genetic)

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
| PRNP gene analysis (blood) (CPT 81479) | - | ROUTINE | ROUTINE | - | Identifies genetic/familial prion disease (fCJD, GSS, FFI); determines codon 129 polymorphism (methionine/valine) which influences sCJD phenotype and prognosis; important for family counseling | No pathogenic mutation; document codon 129 genotype (MM, MV, VV) |
| Codon 129 polymorphism (PRNP) | - | ROUTINE | ROUTINE | - | MM homozygosity most common in sCJD-MM1 (classic rapid form); MV and VV associated with different clinical phenotypes and prognosis | MM most common in sCJD; VV/MV in some atypical forms |
| Neurofilament light chain (NfL) (CPT 83519) -- serum | - | ROUTINE | ROUTINE | - | Markedly elevated in CJD; useful as accessible blood biomarker of neuronal damage; may support diagnosis when CSF unavailable | Markedly elevated (>10,000 pg/mL in CJD) |
| Prion protein gene full sequencing | - | EXT | EXT | - | If PRNP targeted analysis negative but clinical suspicion for genetic prion disease remains high | No pathogenic variant |
| AD biomarkers (serum p-tau217, p-tau181) | - | ROUTINE | ROUTINE | - | Rapidly progressive Alzheimer disease is the most common misdiagnosis of CJD; serum AD biomarkers help distinguish | Normal p-tau ratio (elevated suggests rpAD, not CJD) |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| MRI brain with and without contrast (CPT 70553) + DWI/FLAIR | STAT | STAT | ROUTINE | STAT | Within 24h. DWI is CRITICAL -- cortical ribboning on DWI is highly characteristic of CJD. 3T preferred for sensitivity | sCJD: cortical ribboning on DWI (high signal in neocortex) + caudate/putamen signal on DWI/FLAIR. vCJD: pulvinar sign (bilateral pulvinar thalamic high signal). fCJD: variable by mutation. Sensitivity of MRI DWI for sCJD >90% | Pacemaker; metallic implants; severe claustrophobia |
| EEG (routine) (CPT 95816) | URGENT | URGENT | ROUTINE | URGENT | Within 24h | sCJD: periodic sharp wave complexes (PSWCs) at 1-2 Hz -- triphasic morphology; generalized; sensitivity ~65% (highest in sCJD-MM1 subtype). Also rules out non-convulsive status epilepticus | None significant |
| CT head without contrast (CPT 70450) | STAT | STAT | - | STAT | Immediate if acute presentation, focal deficit, or pre-LP | Mass lesion; hydrocephalus; hemorrhage; CT is typically normal early in CJD but may show atrophy in later stages | Pregnancy (relative) |

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Continuous EEG monitoring (cEEG) (CPT 95700) | - | URGENT | - | STAT | If altered consciousness, suspected NCSE, or fluctuating exam | Non-convulsive seizures; evolution of PSWCs; helps distinguish CJD periodic pattern from seizures | None |
| FDG-PET brain (CPT 78608) | - | EXT | ROUTINE | - | Within 1-2 weeks | CJD: cortical and striatal hypometabolism (often asymmetric early); helps distinguish from AD pattern (temporoparietal); may be useful when MRI is equivocal | Pregnancy; uncontrolled diabetes |
| MRA brain | - | ROUTINE | ROUTINE | - | If vasculitis suspected as alternative diagnosis | CNS vasculitis (beading); normal in CJD | Same as MRI |
| CT chest/abdomen/pelvis with contrast | - | ROUTINE | ROUTINE | - | If paraneoplastic syndrome suspected | Occult malignancy (paraneoplastic RPD mimic) | Contrast allergy; renal impairment |
| Sleep polysomnography | - | - | EXT | - | If fatal familial insomnia (FFI) suspected | Absent sleep spindles; disrupted sleep architecture; progressive total insomnia | Cooperation required |

### 2C. Rare/Specialized

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
| Brain biopsy | - | EXT | - | - | When all non-invasive testing inconclusive and treatable etiology must be excluded; NOT required for CJD diagnosis if RT-QuIC positive and MRI/EEG consistent | Spongiform change; PrP immunostaining (definite CJD); also rules out vasculitis, lymphoma, autoimmune | Coagulopathy; surgical risk; biopsy only changes management if treatable diagnosis possible |
| Second opinion MRI neuroradiology review | - | ROUTINE | ROUTINE | - | If initial MRI read as normal but clinical suspicion for CJD remains high | Subtle DWI cortical signal missed on initial read; CJD MRI findings require expertise | None |
| Nasal brushing for RT-QuIC | - | EXT | EXT | - | Emerging alternative to CSF RT-QuIC; non-invasive; sensitivity 97% in some studies | Positive RT-QuIC from olfactory mucosa supports prion diagnosis | None significant; early-stage research |

### LUMBAR PUNCTURE

**Indication:** Essential for CJD diagnostic workup. CSF RT-QuIC is the gold standard biomarker for prion disease (sensitivity 92%, specificity 99-100%). Also needed to exclude treatable RPD mimics (autoimmune encephalitis, infection, malignancy).

**Timing:** URGENT. Perform early in workup after CT head rules out contraindications. Do not delay for MRI.

**Volume Required:** 15-20 mL (multiple specialized tests required; save extra frozen at -80 degrees C for future studies)

| Study | ED | HOSP | OPD | Rationale | Target Finding |
|-------|:--:|:----:|:---:|-----------|----------------|
| Opening pressure | URGENT | ROUTINE | ROUTINE | Elevated ICP assessment; typically normal in CJD | Normal (10-20 cm H2O); normal in CJD |
| Cell count with differential (tubes 1 and 4) (CPT 89051) | URGENT | ROUTINE | ROUTINE | Normal or minimal pleocytosis in CJD; elevated WBC suggests autoimmune or infectious etiology | Normal in CJD (WBC <5); elevated WBC suggests non-prion diagnosis |
| Protein (CPT 84157) | URGENT | ROUTINE | ROUTINE | Mildly elevated or normal in CJD; markedly elevated suggests infection/autoimmune | Normal or mildly elevated in CJD (usually <100 mg/dL) |
| Glucose with paired serum glucose (CPT 82945) | URGENT | ROUTINE | ROUTINE | Low in bacterial/TB/fungal meningitis, carcinomatous meningitis; normal in CJD | Normal in CJD (>60% of serum) |
| Gram stain and bacterial culture (CPT 87205+87070) | URGENT | ROUTINE | ROUTINE | Exclude chronic bacterial infection | No organisms |
| **RT-QuIC (real-time quaking-induced conversion) (CPT 86235)** | URGENT | URGENT | ROUTINE | GOLD STANDARD for CJD diagnosis. Sensitivity 92%, specificity 99-100%. Detects misfolded prion protein amplification. Send to National Prion Disease Pathology Surveillance Center (Cleveland) or Quest/Mayo | Negative (positive = prion disease essentially confirmed) |
| 14-3-3 protein (CPT 83519) | URGENT | ROUTINE | ROUTINE | Elevated in rapid neuronal destruction. Sensitivity ~90% for sCJD but NOT specific (also elevated in stroke, encephalitis, seizures, CNS lymphoma). Largely superseded by RT-QuIC | Negative (positive supports CJD in right clinical context but has significant false-positive rate) |
| Total tau protein (CPT 83519) | URGENT | ROUTINE | ROUTINE | Markedly elevated in CJD (>1150 pg/mL has sensitivity 90%, specificity 86%). Higher levels correlate with more rapid progression. Not specific (also elevated in AD, stroke) | Normal (<400 pg/mL); CJD often >1150, frequently >10,000 pg/mL |
| Neuron-specific enolase (NSE) | - | ROUTINE | ROUTINE | Elevated in CJD (>35 ng/mL); marker of neuronal damage; less specific than tau or RT-QuIC | Normal (<35 ng/mL); elevated in CJD |
| Neurofilament light chain (NfL) (CPT 83519) -- CSF | - | ROUTINE | ROUTINE | Markedly elevated in CJD; non-specific marker of neuronal damage; useful for tracking progression | Markedly elevated in CJD (often >10,000 pg/mL) |
| Autoimmune encephalitis panel (CSF) -- NMDAR, LGI1, CASPR2, GABA-B, GABA-A, AMPA, DPPX | URGENT | ROUTINE | ROUTINE | CSF more sensitive than serum for NMDAR antibodies; rule out treatable autoimmune encephalitis before accepting CJD diagnosis | Negative |
| Alzheimer biomarkers (CSF Abeta42, Abeta40, p-tau 181, t-tau) (CPT 83519) | - | ROUTINE | ROUTINE | Rapidly progressive AD (rpAD) is the most common misdiagnosis of CJD. AD pattern: low Abeta42/Abeta40 ratio + elevated p-tau. In CJD: t-tau markedly elevated but p-tau NOT proportionally elevated (p-tau/t-tau ratio very low) | Context-dependent; p-tau/t-tau ratio helps distinguish CJD from rpAD |
| Oligoclonal bands (CPT 83916), IgG index | - | ROUTINE | ROUTINE | Intrathecal antibody synthesis (MS, autoimmune, neurosarcoidosis); typically absent in CJD | Absent in CJD; present suggests inflammatory/autoimmune etiology |
| HSV 1/2 PCR (CPT 87529) | URGENT | ROUTINE | - | HSV encephalitis mimic | Negative |
| Cytology (CPT 88104) | - | ROUTINE | ROUTINE | Leptomeningeal carcinomatosis/lymphoma (RPD mimic) | Negative |
| Flow cytometry | - | ROUTINE | ROUTINE | CNS lymphoma (B-cell clonality) | Normal |
| VDRL (CSF) (CPT 86592) | - | ROUTINE | ROUTINE | Neurosyphilis | Non-reactive |
| Cryptococcal antigen (CPT 87327) | URGENT | ROUTINE | - | Cryptococcal meningitis (immunocompromised) | Negative |

**Special Handling:** RT-QuIC requires specific collection and shipping procedures -- contact National Prion Disease Pathology Surveillance Center (1-216-368-0587) or reference lab for specimen requirements. Send CSF on dry ice. Standard prion precautions NOT required for CSF handling (prion concentration in CSF is very low). Save 5-10 mL of CSF frozen at -80 degrees C for future studies.

**Contraindications:** Elevated ICP without imaging (get CT first); coagulopathy (INR >1.5, platelets <50K); skin infection at LP site; posterior fossa mass with herniation risk

---

## 3. TREATMENT

*There is NO disease-modifying treatment for CJD. All management is symptomatic and palliative. The primary goals are comfort, dignity, seizure/myoclonus control, and family support.*

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Lorazepam (acute seizure) | IV | Acute seizure or status epilepticus | 0.1 mg/kg IV push PRN seizure :: IV :: :: 0.1 mg/kg IV (max 4 mg/dose); may repeat x1 in 5 min; max 8 mg total | Respiratory depression; acute narrow-angle glaucoma | Respiratory status; sedation level; airway patency | STAT | STAT | - | STAT |
| Levetiracetam (seizure management) | IV | Seizure prophylaxis and treatment in CJD; preferred first-line ASM due to minimal drug interactions | 1000-1500 mg IV BID :: IV :: :: Load 1000-1500 mg IV; maintenance 500-1500 mg PO/IV BID; max 3000 mg/day | Severe renal impairment (dose adjust per CrCl) | Behavioral changes; renal function; seizure frequency | STAT | STAT | ROUTINE | STAT |
| Thiamine (B1) IV -- empiric | IV | Empiric for Wernicke encephalopathy while RPD workup pending; treat before glucose | 500 mg :: IV :: TID :: 500 mg IV TID x 3 days, then 250 mg IV daily x 3-5 days, then 100 mg PO daily | None significant | Clinical response (confusion, ataxia, ophthalmoplegia) | STAT | STAT | - | STAT |
| IV methylprednisolone (empiric trial) | IV | Empiric immunotherapy trial ONLY if autoimmune encephalitis remains in differential; do NOT continue if CJD confirmed (steroids do not help CJD) | 1000 mg :: IV :: daily :: 1000 mg IV daily x 3-5 days; infuse over 1-2 hours; DISCONTINUE if CJD confirmed | Active untreated infection; CJD confirmed (no benefit); uncontrolled diabetes | Glucose q6h; BP; GI prophylaxis; clinical response assessment | - | URGENT | - | URGENT |

*Note: Empiric immunotherapy should be considered ONLY when autoimmune encephalitis has not been ruled out. If RT-QuIC is positive or clinical/imaging profile strongly favors CJD, steroids provide no benefit and should not be given. The critical decision point is whether treatable causes have been adequately excluded.*

### 3B. Symptomatic Treatments -- Myoclonus

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Clonazepam (first-line for myoclonus) | PO | Myoclonus -- most effective treatment for CJD-associated myoclonus; reduces startle response and involuntary jerking | 0.5 mg BID; 1 mg BID; 2 mg TID :: PO :: :: Start 0.5 mg PO BID; increase by 0.5 mg every 3-5 days as tolerated; target 1-2 mg TID; max 6 mg/day | Respiratory depression; severe hepatic impairment; fall risk (elderly); acute narrow-angle glaucoma | Sedation level; respiratory status; fall risk assessment; swallowing function (may worsen dysphagia) | URGENT | STAT | ROUTINE | STAT |
| Valproic acid (adjunctive for myoclonus) | PO | Myoclonus and seizure control -- add to or substitute for clonazepam if insufficient myoclonus control or excessive sedation from benzodiazepines | 250 mg BID; 500 mg BID; 750 mg BID :: PO :: :: Start 250 mg PO BID; increase by 250 mg every 3-5 days; target level 50-100 mcg/mL; max 2000 mg/day | Hepatic disease; pancreatitis; urea cycle disorders; pregnancy (teratogenic) | LFTs; ammonia; CBC (thrombocytopenia); drug level q1-2 weeks until stable; pancreatitis symptoms | URGENT | ROUTINE | ROUTINE | URGENT |
| Levetiracetam (adjunctive for myoclonus) | PO | Myoclonus -- alternative or adjunct when benzodiazepine sedation is limiting; also provides seizure coverage | 500 mg BID; 1000 mg BID; 1500 mg BID :: PO :: :: Start 500 mg PO BID; increase by 500 mg/day every 1-2 weeks; max 3000 mg/day | Severe renal impairment (dose adjust per CrCl) | Behavioral changes (irritability, aggression); renal function; seizure/myoclonus diary | - | ROUTINE | ROUTINE | ROUTINE |
| Piracetam (adjunctive for myoclonus) | PO | Cortical myoclonus -- may be effective for CJD myoclonus; not FDA-approved in US but available internationally | 2400 mg TID; 4800 mg TID :: PO :: :: Start 2400 mg PO TID; may increase to 4800 mg TID; max 24 g/day | Severe renal impairment; cerebral hemorrhage | Renal function; clinical response | - | EXT | EXT | - |

### 3C. Symptomatic Treatments -- Behavioral and Other Symptoms

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Quetiapine (agitation/psychosis) | PO | Agitation, psychosis, behavioral disturbance in CJD -- preferred atypical antipsychotic due to lower EPS risk | 25 mg qHS; 50 mg BID; 100 mg BID :: PO :: :: Start 25 mg PO qHS; increase by 25 mg/day every 2-3 days; max 200-400 mg/day | QTc prolongation; Lewy body dementia (must distinguish from CJD -- DLB has worse antipsychotic sensitivity) | QTc; metabolic panel; sedation; fall risk; EPS monitoring | - | ROUTINE | ROUTINE | ROUTINE |
| Haloperidol (acute severe agitation) | IV | Acute severe agitation or psychosis not responsive to reorientation and non-pharmacologic measures | 0.5-2 mg IV PRN agitation; 0.5-1 mg IV PRN agitation :: IV :: :: 0.5-2 mg IV/IM q4-6h PRN agitation; use lowest effective dose; max 10 mg/day | QTc >500 ms; Parkinson disease; neuroleptic malignant syndrome history | ECG (QTc before and after); EPS; NMS surveillance (temperature, rigidity, CPK) | STAT | URGENT | - | STAT |
| Trazodone (insomnia) | PO | Sleep disruption and insomnia -- common in CJD; preferred over benzodiazepine hypnotics to avoid excessive sedation | 25 mg qHS; 50 mg qHS; 100 mg qHS :: PO :: :: Start 25 mg PO qHS; increase by 25 mg every 3-5 days; max 150 mg qHS | Concurrent MAOIs; QTc prolongation; priapism risk | Sedation; orthostatic hypotension; swallowing safety | - | ROUTINE | ROUTINE | - |
| Melatonin (insomnia) | PO | Sleep-wake cycle disruption -- may be tried first given excellent safety profile | 3-10 mg qHS :: PO :: :: 3-10 mg PO qHS; start at 3 mg | None significant | Sleep quality | - | ROUTINE | ROUTINE | - |
| Morphine (pain and distress) | IV | Pain, suffering, and distress in advanced CJD -- palliative intent; myoclonus can be painful | 2-4 mg IV q4h PRN; 1-2 mg IV q2h PRN :: IV :: :: Start 1-2 mg IV q2-4h PRN; titrate to comfort; convert to scheduled dosing if frequent PRN use | Respiratory depression (acceptable in comfort-focused care); severe hepatic impairment | Respiratory rate; comfort level; sedation; bowel function (constipation prophylaxis) | - | ROUTINE | - | ROUTINE |
| Morphine oral/sublingual (outpatient palliative) | PO | Pain and distress management in home hospice setting | 5-10 mg q4h PRN; 15-30 mg q12h sustained-release :: PO :: :: Immediate release: 5-10 mg PO q4h PRN; convert to sustained-release when dose established; sublingual concentrated solution for dysphagia | Same as IV morphine | Same as IV morphine; stool softener/laxative prophylaxis | - | ROUTINE | ROUTINE | - |
| Glycopyrrolate (sialorrhea) | PO | Excessive drooling/sialorrhea -- common in advanced CJD with bulbar dysfunction | 1 mg TID; 2 mg TID :: PO :: :: Start 1 mg PO TID; increase to 2 mg TID as needed | Narrow-angle glaucoma; urinary retention; GI obstruction | Anticholinergic effects; urinary retention; constipation; dry mouth | - | ROUTINE | ROUTINE | - |
| Hyoscine (scopolamine) patch (sialorrhea) | TOP | Alternative for sialorrhea management when oral medications difficult due to dysphagia | 1.5 mg patch q72h :: TOP :: :: Apply 1 transdermal patch behind ear every 72 hours; rotate ears | Narrow-angle glaucoma; urinary retention | Confusion (may worsen); dry mouth; urinary retention | - | ROUTINE | ROUTINE | - |
| Ondansetron (nausea) | IV | Nausea and vomiting -- may occur with brainstem involvement or medication side effects | 4 mg IV q8h PRN :: IV :: :: 4 mg IV q8h PRN; or 4-8 mg PO q8h PRN | QTc prolongation; severe hepatic impairment | QTc if repeated dosing | URGENT | ROUTINE | ROUTINE | URGENT |
| Docusate + senna (constipation prophylaxis) | PO | Constipation prevention -- universal need with immobility and opioid use | 100 mg BID + 8.6 mg BID :: PO :: :: Docusate 100 mg PO BID + senna 8.6 mg PO BID; titrate senna to effect | Bowel obstruction | Bowel frequency; abdominal distension | - | ROUTINE | ROUTINE | - |
| Polyethylene glycol (PEG 3350) (constipation) | PO | Constipation refractory to docusate/senna | 17 g daily :: PO :: :: 17 g PO daily in 8 oz water; may increase to BID | Bowel obstruction; ileus | Bowel frequency; electrolytes if prolonged use | - | ROUTINE | ROUTINE | - |

### 3D. Palliative Care Interventions

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
| --- | --- | --- | --- | --- | --- | :--: | :--: | :--: | :--: |
| Comfort-focused care transition | - | All confirmed CJD patients -- initiate goals of care discussion at diagnosis; median survival 5-6 months for sCJD | Goals of care discussion; advance directive completion; POLST/MOLST completion; hospice referral when appropriate | None | Goals of care revisited at each visit; functional status; caregiver burden | URGENT | STAT | ROUTINE | STAT |
| Hospice enrollment | - | Prognosis <6 months (applies to most sCJD at diagnosis); patient/family ready for comfort-focused approach | Per hospice agency; home hospice preferred if safe; inpatient hospice if symptoms uncontrolled or caregiver unable | Patient/family not ready; still pursuing curative workup for non-CJD diagnosis | Comfort; family coping; symptom control | - | ROUTINE | ROUTINE | - |
| Discontinuation of non-essential medications | PO | Medication reconciliation -- stop statins, antihypertensives, diabetes medications, preventive therapies that no longer serve goals of care | Gradual taper or discontinuation per clinical judgment | Do not abruptly stop benzodiazepines, opioids, or anticonvulsants (taper if discontinuing) | Comfort; symptom control after medication changes | - | ROUTINE | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Neurology (prion/neurodegenerative specialist if available) for diagnostic confirmation, prognostication, and ongoing management | STAT | STAT | STAT | STAT |
| Palliative care for goals of care discussion, symptom management, advance care planning, and hospice referral coordination | URGENT | STAT | ROUTINE | STAT |
| National Prion Disease Pathology Surveillance Center (NPDPSC, Case Western Reserve University, Cleveland, OH; phone 1-216-368-0587) for diagnostic guidance, RT-QuIC testing, and potential autopsy coordination | - | ROUTINE | ROUTINE | - |
| Genetic counseling for familial CJD evaluation, PRNP testing implications, and family member risk assessment | - | ROUTINE | ROUTINE | - |
| Psychiatry for behavioral symptom management, capacity evaluation, and caregiver psychiatric support | - | ROUTINE | ROUTINE | - |
| Social work for advance directive facilitation, caregiver support, insurance/disability assistance, and community resources | - | ROUTINE | ROUTINE | - |
| Ethics consultation for end-of-life decision-making, especially if family conflict about goals of care or capacity questions | - | ROUTINE | - | ROUTINE |
| Speech-language pathology for dysphagia evaluation and aspiration risk assessment to guide feeding recommendations | - | ROUTINE | ROUTINE | - |
| Physical therapy for safety assessment, mobility aids, and fall prevention as motor function declines | - | ROUTINE | ROUTINE | - |
| Occupational therapy for ADL adaptation, caregiver training for safe transfers, and home safety evaluation | - | ROUTINE | ROUTINE | - |
| Chaplain/spiritual care for patient and family spiritual support during terminal diagnosis | - | ROUTINE | ROUTINE | - |
| Infection control/hospital epidemiology for prion decontamination protocols and staff education | - | ROUTINE | - | ROUTINE |
| CJD Foundation (www.cjdfoundation.org) referral for patient and family support, educational resources, and peer connections | - | ROUTINE | ROUTINE | - |

### 4B. Patient and Family Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| CJD is NOT contagious through casual contact, sharing meals, kissing, or caring for the patient -- standard household precautions are sufficient; no isolation needed at home | ROUTINE | ROUTINE | ROUTINE |
| CJD has no cure or disease-modifying treatment; management focuses entirely on comfort, symptom control, and quality of life | ROUTINE | ROUTINE | ROUTINE |
| Return to ED immediately if new seizures, choking/aspiration, inability to swallow, high fever, or sudden worsening of symptoms | STAT | STAT | ROUTINE |
| Complete advance directives and healthcare power of attorney EARLY while patient can still participate in decision-making (capacity declines rapidly in CJD) | URGENT | URGENT | ROUTINE |
| Do NOT drive at any point after CJD diagnosis due to progressive cognitive and motor impairment | ROUTINE | ROUTINE | ROUTINE |
| Ensure 24/7 supervision due to fall risk, wandering, impaired judgment, and progressive functional decline | - | ROUTINE | ROUTINE |
| Notify all surgical, dental, and medical providers of CJD diagnosis -- special instrument sterilization or single-use instruments required for any invasive procedure | - | ROUTINE | ROUTINE |
| Blood, organ, and tissue donation is NOT permitted with CJD diagnosis | - | ROUTINE | ROUTINE |
| Contact the CJD Foundation (1-800-659-1991 or www.cjdfoundation.org) for family support resources, educational materials, and peer support groups | - | ROUTINE | ROUTINE |
| Autopsy is strongly encouraged for definitive diagnosis, disease surveillance, and scientific research -- discuss with NPDPSC early; autopsy is provided at no cost through the Surveillance Center | - | ROUTINE | ROUTINE |
| Familial CJD: first-degree relatives should be offered genetic counseling and PRNP testing if mutation identified in proband | - | ROUTINE | ROUTINE |

### 4C. Infection Control & Safety

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Standard precautions only for routine patient care (gloves, gown as needed); CJD is NOT transmitted by respiratory droplets, blood, urine, or feces in normal care | ROUTINE | ROUTINE | ROUTINE |
| Prion decontamination for surgical instruments: instruments contacting high-infectivity tissues (brain, spinal cord, eye) must be destroyed or undergo WHO-recommended decontamination (1N NaOH for 1 hour followed by autoclaving at 134 degrees C for 1 hour in a gravity displacement autoclave) | ROUTINE | ROUTINE | ROUTINE |
| Standard sterilization is INSUFFICIENT for prion decontamination -- conventional autoclaving, ethylene oxide, formaldehyde, alcohol, and UV do not reliably inactivate prions | ROUTINE | ROUTINE | ROUTINE |
| Single-use disposable instruments recommended for any invasive procedure on confirmed or suspected CJD patients | ROUTINE | ROUTINE | ROUTINE |
| Avoid LP needle reuse; dispose of all LP supplies as biohazard (standard practice) | ROUTINE | ROUTINE | - |
| CSF handling: standard laboratory precautions are adequate; prion concentration in CSF is very low; gloves and eye protection for splash risk | ROUTINE | ROUTINE | ROUTINE |
| Endoscopy in CJD patients: use disposable accessories where possible; standard endoscope reprocessing may be insufficient for prion decontamination -- consult infection control | - | ROUTINE | ROUTINE |
| Fall prevention measures: bed alarm, non-slip surfaces, grab bars, low bed, hip protectors for patients with gait instability and myoclonus | ROUTINE | ROUTINE | ROUTINE |
| Aspiration precautions: head of bed elevated 30 degrees; thickened liquids if dysphagia present; SLP evaluation for safe diet recommendations | - | ROUTINE | ROUTINE |
| Skin integrity: frequent repositioning every 2 hours; pressure-relieving mattress; skin assessment daily for immobile patients | - | ROUTINE | - |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Rapidly progressive Alzheimer disease (rpAD) | Most common misdiagnosis of CJD; positive AD biomarkers (low Abeta42, elevated p-tau); no myoclonus typically early on; MRI shows atrophy without DWI cortical ribboning; slower course (years not months) | CSF AD biomarkers (Abeta42/Abeta40 ratio low, p-tau elevated, p-tau/t-tau ratio higher than CJD); RT-QuIC negative; MRI without cortical ribboning |
| Autoimmune encephalitis (anti-NMDAR, anti-LGI1) | Subacute onset; psychiatric symptoms prominent (NMDAR); faciobrachial dystonic seizures (LGI1); steroid-responsive; CSF pleocytosis common | Autoimmune encephalitis antibody panel (CSF and serum); MRI mesial temporal signal (LGI1); response to immunotherapy; RT-QuIC negative |
| Hashimoto encephalopathy (SREAT) | Elevated anti-TPO; steroid-responsive; cognitive fluctuation; seizures; may mimic CJD closely; diagnosis of exclusion | Anti-TPO and anti-thyroglobulin antibodies; empiric steroid trial (dramatic improvement supports diagnosis); RT-QuIC negative |
| CNS lymphoma (primary or intravascular) | B symptoms; enhancing mass (primary CNS lymphoma); multifocal white matter changes + elevated LDH (intravascular lymphoma); no myoclonus | MRI with contrast (enhancement); CSF cytology + flow cytometry; LDH; peripheral blood smear; brain biopsy |
| Neurosyphilis | RPR/VDRL positive; Argyll Robertson pupils; psychiatric symptoms; may have CSF pleocytosis | RPR/VDRL (serum); CSF VDRL; FTA-ABS; LP with CSF analysis |
| Viral encephalitis (HSV, others) | Acute onset; fever; CSF pleocytosis; MRI temporal lobe signal (HSV); seizures | HSV PCR (CSF); viral panels; MRI temporal enhancement; CSF pleocytosis present |
| Leptomeningeal carcinomatosis | Known malignancy history; cranial neuropathies; communicating hydrocephalus | CSF cytology (repeat x3); MRI with contrast (leptomeningeal enhancement); known primary malignancy |
| CNS vasculitis | Headache; multifocal deficits; strokes; CSF pleocytosis; ESR/CRP elevated | MRA (beading); DSA; ESR/CRP; brain/meningeal biopsy; ANCA |
| Dementia with Lewy bodies (DLB) | Visual hallucinations; parkinsonism; REM sleep behavior disorder; fluctuating cognition; slower progression | DaT scan (reduced dopamine transporter); clinical criteria; response to cholinesterase inhibitors; no DWI cortical ribboning |
| Toxic/metabolic encephalopathy | Medication toxicity; substance abuse; hepatic/uremic/electrolyte encephalopathy; reversible | Drug levels; LFTs; ammonia; BUN/Cr; UDS; correction of metabolic derangement improves cognition |
| Non-convulsive status epilepticus (NCSE) | Altered consciousness; may have subtle motor signs; EEG shows electrographic seizures not periodic discharges | Continuous EEG (seizure activity vs PSWCs); response to benzodiazepine trial; MRI without CJD pattern |
| Normal pressure hydrocephalus (NPH) | Triad: gait (predominant) + urinary incontinence + dementia; ventricular enlargement disproportionate to atrophy | Large-volume LP with pre/post gait assessment; MRI (Evans index >0.3, disproportionate ventriculomegaly) |
| Fatal familial insomnia (FFI) | Genetic prion disease (PRNP D178N-129M); progressive insomnia; autonomic dysfunction; late motor/cognitive decline; family history | PRNP gene testing; polysomnography (absent sleep spindles); FDG-PET (thalamic hypometabolism) |
| Gerstmann-Straussler-Scheinker syndrome (GSS) | Genetic prion disease; cerebellar ataxia predominant; slower course (2-10 years); family history | PRNP gene testing (P102L most common); cerebellar atrophy on MRI; slower than sCJD |

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Cognitive assessment (MMSE, MoCA, or bedside exam) | Baseline; weekly inpatient; each outpatient visit | Document trajectory (decline expected in CJD) | Document rate of decline; adjust prognosis; guide goals of care | STAT | STAT | ROUTINE | STAT |
| Neurologic exam (myoclonus, focal signs, gait, cranial nerves, akinetic mutism) | Daily inpatient; each outpatient visit | Document progression pattern | Adjust symptomatic medications (clonazepam for myoclonus); update prognosis | STAT | STAT | ROUTINE | STAT |
| Swallowing assessment (SLP bedside or videofluoroscopy) | Weekly inpatient; each outpatient visit; urgent if coughing with meals | Safe oral intake | Modified diet texture; NG tube or PEG tube discussion if progressive; aspiration precautions | - | ROUTINE | ROUTINE | ROUTINE |
| Functional status (ADLs, Barthel Index) | Weekly inpatient; each outpatient visit | Document trajectory | Increase caregiver support; modify care plan; facility placement if home care insufficient | - | ROUTINE | ROUTINE | - |
| Seizure monitoring | Continuous clinical observation; EEG if suspected subclinical seizures | No clinical or electrographic seizures | Adjust ASM dosing; add second agent; cEEG if unclear | STAT | STAT | ROUTINE | STAT |
| Myoclonus severity assessment | Daily inpatient; each outpatient visit | Tolerable myoclonus not interfering with comfort or function | Titrate clonazepam; add valproic acid; adjust doses | - | ROUTINE | ROUTINE | ROUTINE |
| Respiratory status | Each shift inpatient; each visit outpatient | Adequate oxygenation; no aspiration pneumonia | Chest X-ray if fever/tachypnea; antibiotics for aspiration PNA (if consistent with goals of care); supplemental O2 | STAT | ROUTINE | ROUTINE | STAT |
| Weight and nutritional status | Weekly inpatient; each outpatient visit | Stable or expected decline trajectory | Nutritional supplementation; feeding tube discussion; palliative nutrition approach | - | ROUTINE | ROUTINE | - |
| Skin integrity (pressure injury assessment) | Daily (inpatient); each visit (outpatient) | No pressure injuries | Pressure-relieving surfaces; repositioning schedule; wound care if needed | - | ROUTINE | ROUTINE | - |
| Caregiver burden assessment | Each outpatient visit; at discharge | Caregiver coping; not in crisis | Respite care; support groups; social work referral; facility placement if caregiver unable to continue | - | ROUTINE | ROUTINE | - |
| Safety assessment (fall risk, wandering, capacity) | Daily inpatient; each outpatient visit | Safe environment | Increase supervision; bed alarm; sitters; facility placement | STAT | ROUTINE | ROUTINE | STAT |
| Valproic acid level (if prescribed) | Weekly until stable; then q1-3 months | 50-100 mcg/mL | Dose adjustment; LFTs; ammonia | - | ROUTINE | ROUTINE | - |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Stable symptoms with adequate 24/7 caregiver; myoclonus and seizures controlled; safe swallowing or appropriate feeding plan; hospice/palliative care arranged; outpatient neurology follow-up within 1-2 weeks; advance directives completed |
| Admit to hospital | New diagnosis requiring urgent workup (LP, MRI, EEG); uncontrolled seizures or myoclonus; acute decline requiring medication adjustment; aspiration pneumonia (if consistent with goals of care); caregiver inability to manage at home; goals of care discussion needed |
| Admit to ICU | Status epilepticus; respiratory failure requiring mechanical ventilation (if consistent with goals of care); severe autonomic instability; refractory agitation requiring continuous sedation |
| Transfer to tertiary center | Prion disease expertise for diagnostic confirmation; clinical trial enrollment; complex diagnostic workup (brain biopsy consideration); genetic counseling for familial forms |
| Memory care / Long-term care facility | Progressive functional decline exceeding home caregiver capacity; safety concerns (falls, wandering, aspiration) not manageable at home |
| Hospice (home or inpatient) | Confirmed CJD diagnosis with prognosis <6 months (applies to most sCJD at diagnosis); patient/family goals aligned with comfort-focused care; symptom management as primary goal |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| RT-QuIC for CJD diagnosis (sensitivity 92%, specificity 99-100%) -- gold standard CSF prion biomarker | Class I, Level A | [McGuire et al. (Ann Neurol 2012)](https://pubmed.ncbi.nlm.nih.gov/22926858/); [Atarashi et al. (Nat Med 2011)](https://pubmed.ncbi.nlm.nih.gov/21278748/) |
| MRI DWI cortical ribboning for CJD diagnosis (sensitivity >90%) | Class I, Level A | [Vitali et al. (Neurology 2011)](https://pubmed.ncbi.nlm.nih.gov/21471469/); [Young et al. (AJNR 2005)](https://pubmed.ncbi.nlm.nih.gov/15956529/) |
| CSF 14-3-3 protein for CJD (sensitivity ~90%, specificity 70-85%) | Class IIa, Level B | [Muayqil et al. (BMC Neurol 2012)](https://pubmed.ncbi.nlm.nih.gov/22993290/); WHO diagnostic criteria |
| CSF total tau >1150 pg/mL for CJD diagnosis (sensitivity 90%, specificity 86%) | Class IIa, Level B | [Hamlin et al. (Neurology 2012)](https://pubmed.ncbi.nlm.nih.gov/22302548/) |
| CDC diagnostic criteria for probable sporadic CJD (updated 2018) | Class I, Level A | [CDC Prion Disease - Diagnostic Criteria](https://www.cdc.gov/prion-disease/hcp/diagnostic-criteria/) |
| WHO surveillance criteria for CJD classification (definite, probable, possible) | Class I, Level A | [WHO Manual for Surveillance of Human Transmissible Spongiform Encephalopathies (2003)](https://www.who.int/publications/i/item/WHO-CDS-CSR-EPH-2002-6) |
| EEG periodic sharp wave complexes in CJD -- sensitivity ~65% (highest in MM1 subtype) | Class IIa, Level B | [Steinhoff et al. (Clin Neurophysiol 2004)](https://pubmed.ncbi.nlm.nih.gov/15351383/) |
| PRNP codon 129 polymorphism influences CJD phenotype and susceptibility | Class I, Level B | [Parchi et al. (Ann Neurol 1999)](https://pubmed.ncbi.nlm.nih.gov/10482261/) |
| Molecular classification of sCJD subtypes (MM1, VV2, MV2K, etc.) | Class I, Level B | [Parchi et al. (Ann Neurol 1999)](https://pubmed.ncbi.nlm.nih.gov/10482261/); [Parchi et al. (Brain 2012)](https://pubmed.ncbi.nlm.nih.gov/23065788/) |
| Clonazepam for CJD-associated myoclonus | Class IIb, Level C | Expert consensus; [Brown et al. (Neurology 1986)](https://pubmed.ncbi.nlm.nih.gov/3520375/) |
| No disease-modifying treatment exists for CJD; multiple clinical trials have failed | Class I, Level A | [Stewart et al. (Neurology 2008)](https://pubmed.ncbi.nlm.nih.gov/18725590/) -- quinacrine trial; [Geschwind et al. (Ann Neurol 2013)](https://pubmed.ncbi.nlm.nih.gov/24038413/) -- quinacrine RCT |
| Rapidly progressive AD is the most common misdiagnosis of CJD | Class IIa, Level B | [Paterson et al. (Brain 2012)](https://pubmed.ncbi.nlm.nih.gov/23065788/); NPDPSC autopsy series data |
| Prion decontamination requires NaOH + extended autoclaving; standard sterilization insufficient | Class I, Level A | [WHO Infection Control Guidelines for TSE (2000)](https://www.who.int/publications/i/item/WHO-CDS-CSR-APH-2000.3) |
| Pulvinar sign (bilateral pulvinar high signal on MRI) characteristic of variant CJD | Class I, Level B | [Zeidler et al. (Lancet 2000)](https://pubmed.ncbi.nlm.nih.gov/10744092/) |
| National Prion Disease Pathology Surveillance Center (NPDPSC) for diagnostic referral and autopsy | Class I, Level C | [NPDPSC (Case Western Reserve University)](https://case.edu/medicine/npdpsc/) |
| Serum neurofilament light chain (NfL) markedly elevated in CJD; emerging blood biomarker | Class IIa, Level B | [Thompson et al. (Ann Clin Transl Neurol 2018)](https://pubmed.ncbi.nlm.nih.gov/30349859/) |
| CSF p-tau/t-tau ratio distinguishes CJD from Alzheimer disease | Class IIa, Level B | [Skillback et al. (J Alzheimers Dis 2014)](https://pubmed.ncbi.nlm.nih.gov/24898646/) |
| Palliative care approach recommended for all confirmed CJD patients at diagnosis | Class I, Level C | Expert consensus; [Mead et al. (Prion 2013)](https://pubmed.ncbi.nlm.nih.gov/23370273/) |
| Nasal brushing RT-QuIC as emerging non-invasive prion diagnostic (sensitivity ~97%) | Class IIa, Level B | [Orru et al. (NEJM 2014)](https://pubmed.ncbi.nlm.nih.gov/25099575/); [Bongianni et al. (NEJM 2017)](https://pubmed.ncbi.nlm.nih.gov/28125426/) |

---

## CHANGE LOG

**v1.0 (January 30, 2026)**
- Initial template creation
- Comprehensive CJD plan covering all 4 subtypes (sporadic, familial, iatrogenic, variant)
- Full 8-section format with all subsections
- Structured dosing format with :: delimiters
- Standardized treatment tables with Route and Indication columns
- Prion-specific infection control section (Section 4C)
- Palliative care emphasis throughout
- NPDPSC referral and autopsy guidance
- WHO/CDC diagnostic criteria in appendices
- PubMed citation links for all references

---

## APPENDIX A: CDC DIAGNOSTIC CRITERIA FOR SPORADIC CJD (2018 Update)

### Definite sCJD
- Diagnosed by standard neuropathological techniques; and/or
- Immunocytochemically confirmed PrP-positive; and/or
- Western blot confirmed protease-resistant PrP; and/or
- Presence of scrapie-associated fibrils

### Probable sCJD
Requires: **Progressive neuropsychiatric disorder** AND at least ONE of:
1. **Positive RT-QuIC** (CSF or other tissue)
2. **Positive 14-3-3 CSF** AND clinical duration <2 years
3. **Typical MRI signal** (caudate/putamen OR >=2 cortical regions on DWI/FLAIR)
4. **Typical EEG** (periodic sharp wave complexes)

PLUS at least **TWO** of the following clinical features:
- Myoclonus
- Visual or cerebellar disturbance
- Pyramidal or extrapyramidal dysfunction
- Akinetic mutism

AND routine investigations should not suggest an alternative diagnosis.

### Possible sCJD
- Progressive dementia
- Duration <2 years
- At least TWO of the four clinical features above
- No positive result on any of the four diagnostic tests
- Routine investigations do not suggest alternative diagnosis

## APPENDIX B: VARIANT CJD (vCJD) DIAGNOSTIC CRITERIA

### Definite vCJD
- Confirmed by neuropathological examination (florid plaques, PrP immunostaining pattern)

### Probable vCJD
**I. Clinical criteria (ALL 5 required):**
1. Progressive neuropsychiatric disorder
2. Duration >6 months
3. Routine investigations do not suggest an alternative diagnosis
4. No history of potential iatrogenic exposure
5. No evidence of familial form of TSE

**II. Clinical features (at least 4 of 5):**
- Early psychiatric symptoms (depression, anxiety, apathy, withdrawal, delusions)
- Persistent painful sensory symptoms (pain, dysesthesia)
- Ataxia
- Myoclonus or chorea or dystonia
- Dementia

**III. Diagnostic tests:**
- EEG does NOT show typical sCJD pattern (PSWCs usually absent in vCJD)
- **Pulvinar sign** on MRI (bilateral pulvinar high signal, sensitivity ~90%)
- Tonsil biopsy positive for PrP (if performed)

## APPENDIX C: PRNP CODON 129 GENOTYPE AND sCJD SUBTYPES

| Subtype | Codon 129 | PrP Type | Clinical Phenotype | Typical Duration |
|---------|-----------|----------|-------------------|-----------------|
| MM1 (most common, ~70%) | MM | Type 1 | Classic: rapid cognitive decline, myoclonus, PSWCs on EEG, cortical ribboning on MRI | 3-4 months |
| VV2 | VV | Type 2 | Ataxic variant: prominent cerebellar ataxia early; dementia later; longer course | 6-7 months |
| MV2K | MV | Type 2 | Kuru-type: ataxia, dementia, prolonged course; may lack typical EEG findings | 17-18 months |
| MM2C | MM | Type 2 | Cortical: progressive dementia without typical EEG or MRI in early stages | 15-16 months |
| MM2T | MM | Type 2 | Thalamic (sporadic fatal insomnia): insomnia, autonomic dysfunction, resembles FFI | 15-30 months |
| VV1 (rare) | VV | Type 1 | Early onset; slowly progressive dementia; may lack myoclonus | 15-21 months |

*Note: Codon 129 MM homozygosity is a risk factor for sCJD and is present in ~70% of sCJD cases (vs ~37% of the general population). The molecular classification combines codon 129 genotype with PrP type (determined at autopsy) to define clinicopathological subtypes with distinct clinical presentations and prognosis.*

## APPENDIX D: PRION DECONTAMINATION PROTOCOLS

| Tissue Category | Infectivity Level | Decontamination Required |
|-----------------|-------------------|--------------------------|
| Brain, spinal cord, posterior eye | HIGH | WHO-recommended: 1N NaOH for 1 hour at room temperature followed by autoclaving at 134 degrees C for 1 hour in gravity displacement autoclave; OR destroy instruments |
| CSF, anterior eye, olfactory mucosa | LOW-MODERATE | Standard precautions for handling; standard sterilization generally acceptable for instruments not contacting tissue directly |
| Blood, urine, feces, saliva, skin | LOW/NEGLIGIBLE | Standard precautions only; no special decontamination |
| Environmental surfaces | NEGLIGIBLE | Standard cleaning; 1N NaOH or 20,000 ppm sodium hypochlorite for 1 hour if contaminated with high-infectivity tissue |

**Key Principles:**
- Standard autoclaving (121 degrees C for 15-30 min) does NOT reliably inactivate prions
- Formaldehyde, ethanol, ethylene oxide, UV light, and ionizing radiation do NOT inactivate prions
- Single-use disposable instruments are PREFERRED for any invasive procedure on CJD patients
- Contact hospital infection control before ANY invasive procedure on confirmed or suspected CJD patients
