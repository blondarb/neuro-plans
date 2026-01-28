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
| Total Plans Audited | 2 |
| Total Citations Checked | 29 |
| Verified Correct | 19 |
| Hallucinated PMIDs Found | 10 |
| Corrections Applied | 10 |

**Audit Accuracy Rate:** 66% (19/29 were correct; 10 were hallucinated)

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
