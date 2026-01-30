---
title: Citation Verification Log
description: Tracking citation verification results across all plans to identify patterns and improvement opportunities
---

# Citation Verification Log

This log tracks citation verification results to identify patterns and improve the verification process.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Plans Audited | 12 |
| Total Citations Checked | 105 |
| Verified Correct | 19 |
| Hallucinated PMIDs Found | 10 |
| Corrections Applied | 10 |
| Citations Linked (new, verified via WebSearch) | 41 |
| Generic References Left Unchanged | 38 |

**Audit Accuracy Rate (Plans 1-2):** 66% (19/29 were correct; 10 were hallucinated)
**Plans 3-7:** No pre-existing PMIDs to audit. 18 citations verified and linked via WebSearch. 20 generic references left unchanged.
**Plans 8-12:** No pre-existing PMIDs to audit. 23 citations verified and linked via WebSearch. 3 citations could not be verified. 18 generic references left unchanged.

**Critical Finding:** 10 PMIDs were hallucinated - they linked to completely unrelated articles (pediatric growth hormone, rat neuroscience, immunology crystallization, dental, IBD) or non-existent pages.

---

## Verification Results by Plan

### Peripheral Neuropathy - New Diagnosis/Evaluation

**Date Audited:** 2026-01-21
**Version:** 1.5 → 1.6
**Auditor:** Claude (citation audit)

#### Verified Correct (12)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Dyck PJ et al. Neurology 1993 | [8469345](https://pubmed.ncbi.nlm.nih.gov/8469345/) | ✅ Verified |
| 2 | AAN/AANEM Practice Guideline 2022 | [34965987](https://pubmed.ncbi.nlm.nih.gov/34965987/) | ✅ Verified |
| 3 | Finnerup NB et al. Lancet Neurol 2015 | [25575710](https://pubmed.ncbi.nlm.nih.gov/25575710/) | ✅ Verified |
| 4 | AAN Practice Parameter 2009 | [19056666](https://pubmed.ncbi.nlm.nih.gov/19056666/) | ✅ Verified |
| 5 | Singleton et al. Diabetes Care 2001 | [11473085](https://pubmed.ncbi.nlm.nih.gov/11473085/) | ✅ Verified |
| 6 | Hoffman-Snyder et al. Arch Neurol 2006 | [16769858](https://pubmed.ncbi.nlm.nih.gov/16769858/) | ✅ Verified |
| 7 | Lauria G et al. Eur J Neurol 2010 | [20642627](https://pubmed.ncbi.nlm.nih.gov/20642627/) | ✅ Verified |
| 8 | EAN/PNS Guidelines 2021 (CIDP) | [33506534](https://pubmed.ncbi.nlm.nih.gov/33506534/) | ✅ Verified |
| 9 | Coelho T et al. Neurology 2012 (tafamidis) | [22843282](https://pubmed.ncbi.nlm.nih.gov/22843282/) | ✅ Verified |
| 10 | Adams D et al. NEJM 2018 (APOLLO/patisiran) | [29972753](https://pubmed.ncbi.nlm.nih.gov/29972753/) | ✅ Verified |
| 11 | Benson MD et al. NEJM 2018 (NEURO-TTR/inotersen) | [29972757](https://pubmed.ncbi.nlm.nih.gov/29972757/) | ✅ Verified |
| 12 | Qutenza Prescribing Information | [FDA Label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022395s012lbl.pdf) | ✅ Non-PubMed |

#### Hallucinated PMIDs Found & Corrected (3)

| # | Claimed Citation | Wrong PMID | Actual Article at That PMID | Correct PMID | Status |
|---|------------------|------------|------------------------------|--------------|--------|
| 1 | DCCT/EDIC neuropathy study | 24357209 | "Standards of medical care in diabetes--2014" (ADA general standards, NOT neuropathy study) | **24356595** (Martin et al. Diabetes Care 2014 - actual DCCT/EDIC neuropathy findings) | ✅ Fixed |
| 2 | ADA Standards of Care - Foot Care | 36507645 | "Management of Diabetes in Pregnancy" (wrong section) | **36507636** (Section 12: Foot Care) | ✅ Fixed |
| 3 | Gilron I et al. Lancet 2009 (combination therapy) | 19837455 | "Lymphoproliferative disorders in patients receiving thiopurines for inflammatory bowel disease" (IBD, not neuropathy!) | **19796802** (Nortriptyline and gabapentin combination trial) | ✅ Fixed |

---

### Acute Ischemic Stroke

**Date Audited:** 2026-01-21
**Version:** 1.0 → 1.2
**Auditor:** Claude (citation audit - 2 passes)

#### Verified Correct (7)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | NINDS tPA Trial | [7477192](https://pubmed.ncbi.nlm.nih.gov/7477192/) | ✅ Verified |
| 2 | MR CLEAN | [25517348](https://pubmed.ncbi.nlm.nih.gov/25517348/) | ✅ Verified |
| 3 | DAWN | [29129157](https://pubmed.ncbi.nlm.nih.gov/29129157/) | ✅ Verified |
| 4 | DEFUSE 3 | [29364767](https://pubmed.ncbi.nlm.nih.gov/29364767/) | ✅ Verified |
| 5 | POINT | [29766750](https://pubmed.ncbi.nlm.nih.gov/29766750/) | ✅ Verified |
| 6 | SPARCL | [16899775](https://pubmed.ncbi.nlm.nih.gov/16899775/) | ✅ Verified |
| 7 | AHA/ASA Guidelines 2021 | [34024117](https://pubmed.ncbi.nlm.nih.gov/34024117/) | ✅ Verified |
| 8 | NASCET | [1852179](https://pubmed.ncbi.nlm.nih.gov/1852179/) | ✅ Verified |
| 9 | RESPECT (PFO) | [28885996](https://pubmed.ncbi.nlm.nih.gov/28885996/) | ✅ Verified |

#### Hallucinated PMIDs Found & Corrected (7)

| # | Claimed Citation | Wrong PMID | Actual Article at That PMID | Correct PMID | Status |
|---|------------------|------------|------------------------------|--------------|--------|
| 1 | AcT Trial, Campbell et al. NEJM 2022 | 36036072 | Non-existent or unrelated article | **35779553** (Menon et al. Lancet 2022 - actual AcT trial; also wrong author/journal in original) | ✅ Fixed |
| 2 | CHANCE (DAPT trial) | 23726497 | "An insight into peri-implantitis" (dental article!) | **23803136** (Wang et al. NEJM 2013 - actual CHANCE trial) | ✅ Fixed |
| 3 | AVERT Trial (early mobilization) | 25677597 | "Implementing a simple care bundle..." (different stroke study) | **25892679** (AVERT Collaboration, Lancet 2015 - actual AVERT trial) | ✅ Fixed |
| 4 | CLOSE (PFO closure) | 28902629 | "Individualised growth response optimisation (iGRO) tool" (pediatric growth hormone paper!) | **28902580** (Mas et al. NEJM 2017 - actual CLOSE trial) | ✅ Fixed |
| 5 | DEFENSE-PFO | 29766764 | "Local cortical activity of distant brain areas can phase-lock to olfactory bulb's respiratory rhythm in freely behaving rat" (rat neuroscience!) | **29544871** (Lee et al. JACC 2018 - actual DEFENSE-PFO trial) | ✅ Fixed |
| 6 | ECST 1991 (carotid) | 1754711 | "Crystallization of HLA-DR antigens" (immunology/crystallography paper!) | **1674060** (ECST Collaborative Group, Lancet 1991 - actual ECST interim results) | ✅ Fixed |
| 7 | DECIMAL/DESTINY/HAMLET | 17482661 | Unknown/invalid PMID | **17303527** (Vahedi et al. Lancet Neurol 2007 - pooled analysis of craniectomy trials) | ✅ Fixed |

---

### Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)

**Date Audited:** 2026-01-29
**Version:** 1.0
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (3)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Van den Bergh et al., Eur J Neurol 2021 (EFNS/PNS Criteria) | [34327760](https://pubmed.ncbi.nlm.nih.gov/34327760/) | ✅ Linked |
| 2 | ICE trial (Hughes et al., Lancet Neurol 2008) | [18178525](https://pubmed.ncbi.nlm.nih.gov/18178525/) | ✅ Linked |
| 3 | PATH trial (van Schaik et al., Lancet Neurol 2018) | [29122523](https://pubmed.ncbi.nlm.nih.gov/29122523/) | ✅ Linked |

#### Cochrane Review Linked (1)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Cochrane Review IVIG for CIDP (Eftimov et al., 2013) | [24379104](https://pubmed.ncbi.nlm.nih.gov/24379104/) | ✅ Linked |

#### Generic References Left Unchanged (5)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Corticosteroids effective for CIDP — Cochrane Reviews | Generic Cochrane reference (multiple reviews) |
| 2 | Plasma exchange effective — Cochrane Reviews | Generic Cochrane reference |
| 3 | IVIG, steroids, PLEX equivalent — Multiple comparative studies | No single study |
| 4 | Rituximab for anti-nodal CIDP — Case series; expert consensus | No single landmark study |
| 5 | Steroid-sparing agents — Limited controlled data | No single study |

---

### Cluster Headache

**Date Audited:** 2026-01-29
**Version:** 1.0
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (1)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | GAAIN trial — Galcanezumab for episodic CH (Goadsby et al., NEJM 2019) | [31291515](https://pubmed.ncbi.nlm.nih.gov/31291515/) | ✅ Linked |

#### Generic References Left Unchanged (7)

| # | Citation | Reason |
|---|----------|--------|
| 1 | High-flow oxygen — Multiple RCTs; Cochrane Reviews | Generic |
| 2 | Sumatriptan SC — Multiple RCTs | Generic |
| 3 | Verapamil — Multiple RCTs | Generic |
| 4 | Lithium — RCTs with limitations | Generic |
| 5 | Corticosteroids for transitional — Multiple studies | Generic |
| 6 | Greater occipital nerve block — Multiple studies | Generic |
| 7 | Indomethacin response — Diagnostic criterion | Not a study |

---

### Dementia Evaluation

**Date Audited:** 2026-01-29
**Version:** 1.0
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (5)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | AAN Practice Parameters 2001 (Knopman et al., Neurology) | [11342678](https://pubmed.ncbi.nlm.nih.gov/11342678/) | ✅ Linked (2 rows) |
| 2 | DOMINO trial (Howard et al., NEJM 2012) | [22397651](https://pubmed.ncbi.nlm.nih.gov/22397651/) | ✅ Linked |
| 3 | Clarity AD trial (van Dyck et al., NEJM 2023) | [36449413](https://pubmed.ncbi.nlm.nih.gov/36449413/) | ✅ Linked |
| 4 | TRAILBLAZER-ALZ 2 (Sims et al., JAMA 2023) | [37459141](https://pubmed.ncbi.nlm.nih.gov/37459141/) | ✅ Linked |

#### Generic References Left Unchanged (5)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Cholinesterase inhibitors — Cochrane Reviews | Generic Cochrane |
| 2 | Memantine — Cochrane Reviews | Generic Cochrane |
| 3 | Non-pharmacologic BPSD — APA Guidelines | Guideline body, not single study |
| 4 | Antipsychotics mortality — FDA black box warning | Regulatory, not PubMed |
| 5 | CSF biomarkers — AT(N) framework | Framework, not single study |
| 6 | Amyloid PET — Appropriate Use Criteria | Consensus criteria |
| 7 | Exercise — Multiple RCTs | Generic |

---

### Diabetic Neuropathy

**Date Audited:** 2026-01-29
**Version:** 1.0
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (2)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | DCCT (DCCT Research Group, NEJM 1993) | [8366922](https://pubmed.ncbi.nlm.nih.gov/8366922/) | ✅ Linked |
| 2 | UKPDS 33 (Lancet 1998) | [9742976](https://pubmed.ncbi.nlm.nih.gov/9742976/) | ✅ Linked |

#### Generic References Left Unchanged (7)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Duloxetine — Multiple RCTs; FDA-approved | Generic |
| 2 | Pregabalin — Multiple RCTs; FDA-approved | Generic |
| 3 | Gabapentin — Multiple RCTs | Generic |
| 4 | TCAs — Multiple RCTs | Generic |
| 5 | Capsaicin 8% — Multiple RCTs; FDA-approved | Generic |
| 6 | Midodrine — Multiple RCTs | Generic |
| 7 | Annual foot screening — Multiple studies | Generic |
| 8 | Multifactorial risk reduction — Multiple studies | Generic |

---

### Elevated ICP Management

**Date Audited:** 2026-01-29
**Version:** 1.0
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (9)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | BTF Guidelines 4th Edition (Carney et al., Neurosurgery 2017) | [27654000](https://pubmed.ncbi.nlm.nih.gov/27654000/) | ✅ Linked (2 tables) |
| 2 | CRASH Trial (Roberts et al., Lancet 2004) | [15474134](https://pubmed.ncbi.nlm.nih.gov/15474134/) | ✅ Linked |
| 3 | DECRA Trial (Cooper et al., NEJM 2011) | [21434843](https://pubmed.ncbi.nlm.nih.gov/21434843/) | ✅ Linked |
| 4 | RESCUEicp Trial (Hutchinson et al., NEJM 2016) | [27602507](https://pubmed.ncbi.nlm.nih.gov/27602507/) | ✅ Linked |
| 5 | DESTINY/DECIMAL/HAMLET pooled (Vahedi et al., Lancet Neurol 2007) | [17303527](https://pubmed.ncbi.nlm.nih.gov/17303527/) | ✅ Linked |
| 6 | EUROTHERM (Andrews et al., NEJM 2015) | [26444221](https://pubmed.ncbi.nlm.nih.gov/26444221/) | ✅ Linked |
| 7 | INTERACT2 (Anderson et al., NEJM 2013) | [23713578](https://pubmed.ncbi.nlm.nih.gov/23713578/) | ✅ Linked |
| 8 | ATACH-2 (Qureshi et al., NEJM 2016) | [27276234](https://pubmed.ncbi.nlm.nih.gov/27276234/) | ✅ Linked |

#### Not Linked — Unable to Find Specific PMID (1)

| # | Citation | Reason |
|---|----------|--------|
| 1 | SAFE-TBI (2021) — mannitol vs. hypertonic saline | No specific trial named "SAFE-TBI" found comparing mannitol vs. HTS for ICP. The SAFE-TBI study (PMID: 17761591) is about albumin vs. saline resuscitation, not osmotherapy. A 2021 meta-analysis exists (Schwimmbeck et al., PMID: 31567726) but is not the same study. Left unchanged. |

#### Generic References Left Unchanged (4)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Malignant MCA Stroke Guidelines — AHA/ASA 2019 | Guideline body |
| 2 | ICH Guidelines — AHA/ASA 2022 | Guideline body |
| 3 | SAH Guidelines — AHA/ASA 2023 | Guideline body |
| 4 | IIH Guidelines — British Consensus 2018 | Guideline body |

---

### Acute Myelopathy

**Date Audited:** 2026-01-29
**Version:** Current approved version
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (7)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Transverse Myelitis Consortium Working Group (2002) | [12236201](https://pubmed.ncbi.nlm.nih.gov/12236201/) | Verified & Linked |
| 2 | Weinshenker et al. (Ann Neurol 1999) — PLEX for demyelinating attacks | [10589540](https://pubmed.ncbi.nlm.nih.gov/10589540/) | Verified & Linked |
| 3 | Wingerchuk et al. IPND 2015 criteria — NMOSD diagnosis | [26092914](https://pubmed.ncbi.nlm.nih.gov/26092914/) | Verified & Linked |
| 4 | Banwell et al. (Lancet Neurol 2023) — MOGAD criteria | [36706773](https://pubmed.ncbi.nlm.nih.gov/36706773/) | Verified & Linked |
| 5 | Fehlings et al. (2012) — Surgical decompression timing | [22384132](https://pubmed.ncbi.nlm.nih.gov/22384132/) | Verified & Linked |
| 6 | Darouiche et al. (NEJM 2006) — Epidural abscess | [17093252](https://pubmed.ncbi.nlm.nih.gov/17093252/) | Verified & Linked |
| 7 | PREVENT trial (Pittock et al. NEJM 2019) — Eculizumab for NMOSD | [31050279](https://pubmed.ncbi.nlm.nih.gov/31050279/) | Verified & Linked |

#### Generic References Left Unchanged (4)

| # | Citation | Reason |
|---|----------|--------|
| 1 | IV methylprednisolone for acute inflammatory myelitis | Standard practice; multiple studies |
| 2 | MAP ≥85 mmHg for traumatic SCI | Guideline recommendation |
| 3 | Satralizumab/inebilizumab for NMOSD prevention | Multiple recent trials |
| 4 | MS DMT initiation | Multiple guidelines |

---

### Breakthrough Seizure

**Date Audited:** 2026-01-29
**Version:** Current approved version
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (4)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Kwan & Brodie (2000) — Seizure freedom and drug-resistant epilepsy | [10660394](https://pubmed.ncbi.nlm.nih.gov/10660394/) | Verified & Linked |
| 2 | SANAD I (2007) — Focal epilepsy ASM comparison | [17382827](https://pubmed.ncbi.nlm.nih.gov/17382827/) | Verified & Linked |
| 3 | SANAD II (2021) — Lamotrigine vs. levetiracetam/zonisamide | [33838757](https://pubmed.ncbi.nlm.nih.gov/33838757/) | Verified & Linked |
| 4 | ERSET (2012) — Early surgery for drug-resistant TLE | [22396514](https://pubmed.ncbi.nlm.nih.gov/22396514/) | Verified & Linked |

#### Generic References Left Unchanged (4)

| # | Citation | Reason |
|---|----------|--------|
| 1 | AAN/AES guidelines for breakthrough seizure management | Guideline body |
| 2 | ASM serum level monitoring | Standard practice |
| 3 | VNS/RNS/DBS for drug-resistant epilepsy | Multiple device trials |
| 4 | Epilepsy monitoring unit referral criteria | Standard practice |

---

### Cauda Equina Syndrome

**Date Audited:** 2026-01-29
**Version:** Current approved version
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (5)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Ahn et al. (2000) — CES meta-analysis, 48h threshold | [10851100](https://pubmed.ncbi.nlm.nih.gov/10851100/) | Verified & Linked |
| 2 | Todd (2005) — CES surgery timing review | [16455534](https://pubmed.ncbi.nlm.nih.gov/16455534/) | Verified & Linked |
| 3 | Gleave & Macfarlane (2002) — CES-I vs. CES-R classification | [12389883](https://pubmed.ncbi.nlm.nih.gov/12389883/) | Verified & Linked |
| 4 | Groen & Ponssen (1990) — Spinal epidural hematoma etiology | [2243224](https://pubmed.ncbi.nlm.nih.gov/2243224/) | Verified & Linked |
| 5 | Kostuik et al. (1986) — CES natural history | [2936744](https://pubmed.ncbi.nlm.nih.gov/2936744/) | Verified & Linked |

#### Not Linked — Unable to Verify (2)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Srikandarajah et al. (2020) — UK Cohort | Could not find a specific 2020 publication matching "UK Cohort" description. Srikandarajah published CESCOS (2020, PMID 31923259) and bladder outcomes study (2015, PMID 25646751). The UCES multi-centre cohort was published in 2022 (PMID 36426378). Left unchanged to avoid incorrect attribution. |
| 2 | DeBois et al. (2019) — Systematic review 12/24/48h | Could not find any publication by author "DeBois" on CES surgical timing. May be misspelled or non-indexed. Left unchanged. |

#### Generic References Left Unchanged (3)

| # | Citation | Reason |
|---|----------|--------|
| 1 | McCarthy et al. (2014) — Medicolegal review | Could not find a specific 2014 McCarthy paper on CES litigation. Known McCarthy CES paper is 2007 (PMID 17224816). Left unchanged as may refer to non-indexed publication. |
| 2 | Expert consensus — surgical timing urgency | Generic consensus |
| 3 | Clinical practice — PVR measurement | Standard practice |

---

### Spinal Cord Compression (Malignant)

**Date Audited:** 2026-01-29
**Version:** Current approved version
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (7)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Patchell et al. (2005) — Surgery + RT vs. RT alone (Lancet) | [16112300](https://pubmed.ncbi.nlm.nih.gov/16112300/) | Verified & Linked |
| 2 | Sorensen et al. (1994) — Dexamethasone + RT trial | [8142159](https://pubmed.ncbi.nlm.nih.gov/8142159/) | Verified & Linked |
| 3 | Vecht et al. (1989) — High vs. standard dose dexamethasone | [2771077](https://pubmed.ncbi.nlm.nih.gov/2771077/) | Verified & Linked |
| 4 | Rades et al. (2008) — Short vs. long course RT (SCORE-1) | [18539406](https://pubmed.ncbi.nlm.nih.gov/18539406/) | Verified & Linked |
| 5 | Laufer et al. (2013) — Separation surgery + SBRT | [23339593](https://pubmed.ncbi.nlm.nih.gov/23339593/) | Verified & Linked |
| 6 | Rosen et al. (2003) — Zoledronic acid SRE reduction | [14534891](https://pubmed.ncbi.nlm.nih.gov/14534891/) | Verified & Linked |
| 7 | Fizazi et al. (2011) — Denosumab vs. zoledronic acid | [21353695](https://pubmed.ncbi.nlm.nih.gov/21353695/) | Verified & Linked |

#### Generic References Left Unchanged (3)

| # | Citation | Reason |
|---|----------|--------|
| 1 | NOMS framework — Surgical decision-making | Institutional framework, multiple publications |
| 2 | SINS scoring — Spinal instability | Multiple validation studies |
| 3 | Tokuhashi/Tomita scoring — Survival prediction | Multiple validation studies |

---

### Parkinson's Disease - New Diagnosis

**Date Audited:** 2026-01-29
**Version:** Current approved version
**Auditor:** Claude (citation verification via WebSearch)

#### Citations Verified & Linked (1)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | Postuma et al., Mov Disord 2015 — MDS PD Criteria | [26474316](https://pubmed.ncbi.nlm.nih.gov/26474316/) | Verified & Linked |

#### Generic References Left Unchanged (4)

| # | Citation | Reason |
|---|----------|--------|
| 1 | Levodopa trials — Multiple landmark studies | Generic |
| 2 | Dopamine agonist trials | Generic |
| 3 | MAO-B inhibitor trials | Generic |
| 4 | AAN/MDS treatment guidelines | Guideline body |

---

## Patterns & Improvement Opportunities

### CRITICAL Pattern: PMID Hallucination

**Issue:** 10 PMIDs across 2 plans were completely fabricated. They linked to unrelated articles:
- Pediatric growth hormone papers instead of stroke PFO trials
- Rat olfactory neuroscience instead of cardiac trials
- HLA-DR crystallization (immunology) instead of carotid surgery trials
- Dental articles instead of neurology papers
- IBD studies instead of neuropathic pain trials
- Pregnancy guidelines instead of foot care guidelines
- Non-existent/invalid PMIDs

**Root Cause:** AI model generated plausible-looking PMIDs without verification.

**Egregious Examples Found:**
- PMID 28902629 claimed to be CLOSE PFO trial → actually "Individualised growth response optimisation (iGRO) tool" (pediatric endocrinology!)
- PMID 29766764 claimed to be DEFENSE-PFO trial → actually rat olfactory bulb neuroscience paper!
- PMID 1754711 claimed to be ECST carotid trial → actually "Crystallization of HLA-DR antigens" (immunology!)
- PMID 23726497 claimed to be CHANCE stroke trial → actually "An insight into peri-implantitis" (dental)
- PMID 19837455 claimed to be Gilron neuropathy combination therapy → actually IBD thiopurines study

**Prevention Added:** Updated `neuro-citation-verifier-skill.md` with mandatory verification steps:
1. Search for article by author, title, journal, year
2. Find actual PMID in search results
3. Fetch and verify PubMed page matches
4. Only then add the link

### Pattern 2: Author/Journal Confusion

**Issue:** AcT Trial cited as "Campbell et al. NEJM" but correct citation is "Menon et al. Lancet"

**Root Cause:** Multiple tenecteplase stroke trials exist. Campbell published EXTEND-IA TNK; Menon published AcT.

**Recommendation:** Always verify author AND journal, not just trial name.

### Pattern 3: Section Number Confusion

**Issue:** ADA Standards of Care foot care section linked to pregnancy section (different PMID within same supplement)

**Root Cause:** Multi-section documents have different PMIDs per section.

**Recommendation:** When citing guidelines, include section number/title in the verification.

---

## Verification Process Improvements

### Current Process

1. Extract citations from Section 8
2. Search web for each citation
3. Verify accuracy of claim
4. Add PubMed hyperlink if available
5. Flag issues for correction

### Proposed Improvements

| Improvement | Priority | Status |
|-------------|----------|--------|
| Create approved non-PubMed source list | High | Pending |
| Add trial indication verification step | High | Pending |
| Flag generic references ("Multiple RCTs") | Medium | Pending |
| Add duplicate citation detection | Low | Pending |
| Integrate PubMed API for automated lookup | Low | Pending |

---

## Approved Non-PubMed Sources

These sources are acceptable when PubMed links are not available:

| Source Type | Domain | Example |
|-------------|--------|---------|
| FDA Drug Labels | accessdata.fda.gov | Prescribing information |
| CMS Coverage | cms.gov | LCD/NCD documents |
| Cochrane Library | cochranelibrary.com | Systematic reviews |
| AAN Guidelines | aan.com | Practice parameters |
| EFNS/EAN Guidelines | ean.org | European guidelines |
| WHO Guidelines | who.int | International guidelines |
| CDC Guidelines | cdc.gov | Public health guidance |

---

## Change Log

**2026-01-29 - Batch Citation Verification (5 More Approved Plans)**
- Verified citations in: Acute Myelopathy, Breakthrough Seizure, Cauda Equina Syndrome, Spinal Cord Compression (Malignant), Parkinson's Disease - New Diagnosis
- 23 citations verified and linked via WebSearch (no pre-existing PMIDs to audit)
- 3 citations could not be verified: Srikandarajah et al. (2020), DeBois et al. (2019), McCarthy et al. (2014)
- 18 generic references left unchanged per policy
- All PMIDs verified by searching PubMed via WebSearch — no hallucinated PMIDs added
- Notable: DeBois et al. (2019) author name could not be found in any CES literature — may be misspelled or non-indexed
- Notable: McCarthy et al. CES medicolegal paper found as 2007 (PMID 17224816), not 2014 as cited

**2026-01-29 - Batch Citation Verification (5 Approved Plans)**
- Verified citations in: CIDP, Cluster Headache, Dementia Evaluation, Diabetic Neuropathy, Elevated ICP Management
- 18 citations verified and linked via WebSearch (no pre-existing PMIDs to audit)
- 20 generic references (e.g., "Multiple RCTs", "Cochrane Reviews") left unchanged per policy
- 1 citation (SAFE-TBI 2021) could not be linked — no matching trial found in PubMed
- Notable: SAFE-TBI appears to reference albumin vs. saline (PMID 17761591), not mannitol vs. HTS
- All PMIDs verified by searching PubMed via WebSearch — no hallucinated PMIDs added

**2026-01-21 - Complete Citation Audit (Pass 2)**
- Conducted complete verification of ALL citations (not just spot-checking)
- Found 4 additional hallucinated PMIDs in Acute Ischemic Stroke
- Total hallucinated: 10 PMIDs across 2 plans (34% error rate)
- Most egregious: PFO trial linked to pediatric growth hormone paper; carotid trial linked to immunology crystallization paper
- Updated Acute Ischemic Stroke to v1.2 with all fixes

**2026-01-21 - Citation Audit (Pass 1)**
- Conducted initial audit of existing citations
- Found 6 hallucinated PMIDs across 2 plans
- Fixed PMIDs in Peripheral Neuropathy and Acute Ischemic Stroke
- Updated neuro-citation-verifier-skill.md with mandatory PMID verification steps
- Added CRITICAL hallucination pattern to improvement opportunities

**2026-01-20**
- Initial log created
- Added Peripheral Neuropathy verification results
- Identified 3 improvement patterns
- Created approved non-PubMed source list
