---
name: neuro-citation-verifier
description: Validates citations and evidence references in clinical decision support templates. Uses web search to verify that cited studies, guidelines, and sources exist and accurately support the claims made. Identifies hallucinated or inaccurate citations. Run after neuro-checker validation is complete and content is stable.
---

# Neuro Citation Verifier

Systematically verify all citations and evidence references in clinical recommendation templates to ensure accuracy and prevent hallucinated sources.

## When to Use

Run this skill AFTER:
- Initial template generation (neuro-builder)
- Validation and revision cycle (neuro-checker + neuro-rebuilder)
- Template has achieved ≥90% validation score

Run BEFORE:
- CPT/synonym enrichment
- Final physician sign-off
- Clinical deployment

## Citation Types to Verify

| Citation Type | Example | Verification Method |
|---------------|---------|---------------------|
| Journal articles | "Fisher RS et al. Epilepsia 2017" | Search PubMed, journal website |
| Clinical guidelines | "AAN Practice Parameter 2007" | Search society website, PubMed |
| Consensus statements | "ILAE Commission Report 2019" | Search organization website |
| Clinical trials | "ESETT Trial, NEJM 2019" | Search ClinicalTrials.gov, PubMed |
| Textbook references | "Adams and Victor's Neurology" | Verify edition, chapter exists |
| Drug labeling | "FDA prescribing information" | Search FDA label database |
| Evidence levels | "Class I, Level A" | Verify grading system matches source |

## Verification Process

### Step 1: Extract All Citations

Scan the template for citations in:
- **Section 8 (Evidence & References)** - Primary location
- **Inline references** - Within rationale columns or notes
- **Dosing sources** - Drug dosing citations
- **Diagnostic criteria sources** - Classification systems

### Step 2: Categorize by Priority

| Priority | Category | Rationale |
|----------|----------|-----------|
| **HIGH** | Drug dosing citations | Patient safety - incorrect dosing is dangerous |
| **HIGH** | Diagnostic criteria | Misdiagnosis risk |
| **HIGH** | Treatment efficacy claims | Direct patient care impact |
| **MEDIUM** | Epidemiology/prevalence | Context but not actionable |
| **MEDIUM** | Pathophysiology | Educational, less actionable |
| **LOW** | Historical references | Background only |

### Step 3: Verify Each Citation

For each citation, perform web search to confirm:

1. **Source exists** - Can the article/guideline be found?
2. **Authors match** - Are the cited authors correct?
3. **Year matches** - Is the publication year correct?
4. **Journal/source matches** - Is it published where claimed?
5. **Content supports claim** - Does the source actually say what's claimed?

### Step 4: Assign Verification Status

| Status | Symbol | Meaning |
|--------|--------|---------|
| Verified | ✅ | Source found, content confirmed |
| Partial Match | ⚠️ | Source found but details differ (wrong year, different authors, etc.) |
| Not Found | ❌ | Cannot locate source despite thorough search |
| Inaccurate | ❌ | Source found but does NOT support the claim made |
| Unable to Verify | ❓ | Paywalled or inaccessible; cannot confirm content |

### Step 5: Capture Source Links

For each verified or partially matched citation, include a direct link to the source. Use the following link hierarchy (prefer earlier options):

| Source Type | Preferred Link | Example |
|-------------|----------------|---------|
| Journal articles | PubMed link (PMID) | `https://pubmed.ncbi.nlm.nih.gov/28276064/` |
| Guidelines | Organization website | `https://www.aan.com/Guidelines/...` |
| Clinical trials | ClinicalTrials.gov | `https://clinicaltrials.gov/study/NCT01960075` |
| FDA labeling | DailyMed or FDA | `https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=...` |
| Consensus statements | Organization or PubMed | Direct link to PDF or abstract |
| Textbooks | Publisher page | Link to edition/chapter if available online |

**Link Priority:**
1. **PubMed** - Preferred for journal articles (stable, free access to abstracts)
2. **DOI link** - `https://doi.org/10.xxxx/...` (permanent, resolves to publisher)
3. **Organization website** - For guidelines and consensus statements
4. **Publisher/journal site** - Direct article link
5. **Google Scholar** - Fallback if no direct link available

## Search Strategy

### For Journal Articles

```
Search 1: "[Author last name] [key topic] [journal] [year]"
Search 2: "[Article title keywords] PubMed"
Search 3: "[Author] [year] [condition]"
```

### For Guidelines

```
Search 1: "[Organization] [topic] guideline [year]"
Search 2: "[Organization] practice parameter [condition]"
Search 3: "site:[organization website] [topic] guideline"
```

### For Clinical Trials

```
Search 1: "[Trial name] [condition] trial"
Search 2: "[Trial acronym] [journal] [year]"
Search 3: "ClinicalTrials.gov [trial name]"
```

### For FDA Information

```
Search 1: "[Drug name] FDA prescribing information"
Search 2: "[Drug name] package insert"
Search 3: "site:accessdata.fda.gov [drug name]"
```

## Output Format

```
CITATION VERIFICATION REPORT
============================
TEMPLATE: [Diagnosis Name]
VERSION: [Version]
DATE VERIFIED: [Date]
VERIFIER: Claude (neuro-citation-verifier v1.1)

## SUMMARY

| Status | Count |
|--------|-------|
| ✅ Verified | X |
| ⚠️ Partial Match | X |
| ❌ Not Found | X |
| ❌ Inaccurate | X |
| ❓ Unable to Verify | X |
| **TOTAL** | X |

**Overall Citation Integrity:** [X]% verified or partially matched

---

## HIGH PRIORITY CITATIONS

### Drug Dosing / Treatment Citations

| Citation | Claim in Template | Status | Link | Verification Notes |
|----------|-------------------|--------|------|-------------------|
| [Citation] | [What template claims] | ✅/⚠️/❌ | [PubMed](url) | [Search findings] |

### Diagnostic Criteria Citations

| Citation | Claim in Template | Status | Link | Verification Notes |
|----------|-------------------|--------|------|-------------------|
| [Citation] | [What template claims] | ✅/⚠️/❌ | [PubMed](url) | [Search findings] |

---

## MEDIUM PRIORITY CITATIONS

| Citation | Claim in Template | Status | Link | Verification Notes |
|----------|-------------------|--------|------|-------------------|
| [Citation] | [What template claims] | ✅/⚠️/❌ | [PubMed](url) | [Search findings] |

---

## LOW PRIORITY CITATIONS

| Citation | Claim in Template | Status | Link | Verification Notes |
|----------|-------------------|--------|------|-------------------|
| [Citation] | [What template claims] | ✅/⚠️/❌ | [PubMed](url) | [Search findings] |

---

## ISSUES REQUIRING CORRECTION

### Critical (Must Fix Before Deployment)

| Issue # | Section | Original Citation | Problem | Suggested Correction |
|---------|---------|-------------------|---------|---------------------|
| C1 | [Section] | [Original] | [Problem found] | [Correction] |

### Recommended (Should Fix)

| Issue # | Section | Original Citation | Problem | Suggested Correction |
|---------|---------|-------------------|---------|---------------------|
| R1 | [Section] | [Original] | [Problem found] | [Correction] |

### Minor (Nice to Fix)

| Issue # | Section | Original Citation | Problem | Suggested Correction |
|---------|---------|-------------------|---------|---------------------|
| M1 | [Section] | [Original] | [Problem found] | [Correction] |

---

## VERIFICATION DETAILS

[For each citation, include detailed search notes]

### Citation 1: [Full citation text]
**Location in template:** Section 8, Row X
**Claim supported:** [What the template claims this source supports]
**Search performed:**
- Search 1: "[query]" → [result]
- Search 2: "[query]" → [result]
**Verification result:** ✅/⚠️/❌
**Source link:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/XXXXXXXX/) or [DOI](https://doi.org/XX.XXXX/...) or N/A if not found
**Notes:** [Detailed findings]

[Repeat for each citation]

---

## CITATIONS RECOMMENDED TO ADD

[If verification reveals important missing citations that should be added]

| Recommendation | Source | Link | Rationale |
|----------------|--------|------|-----------|
| [What to cite] | [Actual source found] | [PubMed](url) | [Why it should be added] |
```

## Common Citation Issues

### Hallucination Patterns

| Pattern | Example | How to Catch |
|---------|---------|--------------|
| Plausible but nonexistent | "Smith et al. Neurology 2018" (no such article) | PubMed search returns nothing |
| Wrong author order | "Jones and Smith 2015" (actually "Smith and Jones") | Check actual author list |
| Wrong year | "NEJM 2019" (actually published 2020) | Verify publication date |
| Wrong journal | "Published in Lancet" (actually in BMJ) | Check actual publication venue |
| Conflated studies | Combines findings from 2 different papers | Read abstracts carefully |
| Outdated guidelines | Cites 2007 guideline when 2022 update exists | Search for latest version |
| Misattributed findings | Claims study shows X when it shows Y | Read abstract/full text |

### Red Flags Requiring Extra Scrutiny

- Very specific statistics without clear source
- Claims that seem too good/clean (e.g., "100% sensitivity")
- Guidelines from organizations that don't exist
- Trial names that don't appear in registries
- Evidence levels without methodology explanation

## Integration with Rebuilder

After verification, generate a correction list formatted for the neuro-rebuilder skill:

```
## CITATION CORRECTIONS FOR REBUILDER

C1. Section 8 - Change "Fisher 2016" to "Fisher RS et al. Epilepsia 2017;58(4):531-542"
C2. Section 3A - Remove dosing claim "per ESETT trial" (trial does not specify this dose)
C3. Section 8 - Add missing citation: "Hauser WA et al. NEJM 1998;338:429-34" for recurrence risk data
```

## Integration with Templates

**CRITICAL: After verification, update the main template file** to add clickable PubMed links to Section 8 (Evidence & References). This ensures links render in the Clinical Plan Builder interface.

### Template Update Process

1. Open the main template file (e.g., `docs/plans/status-epilepticus.md`)
2. Navigate to Section 8 (Evidence & References)
3. Replace plain text citations with markdown links:

**Before:**
```
| Lorazepam preferred IV benzodiazepine | Class I, Level A | Alldredge et al. NEJM 2001 |
```

**After:**
```
| Lorazepam preferred IV benzodiazepine | Class I, Level A | [Alldredge et al. NEJM 2001](https://pubmed.ncbi.nlm.nih.gov/11547716/) |
```

4. For multiple sources in one row, link each:
```
| Benzodiazepines first-line for SE | Class I, Level A | [NCS Guidelines 2012](https://pubmed.ncbi.nlm.nih.gov/22528274/); [AES Guidelines 2016](https://pubmed.ncbi.nlm.nih.gov/26900382/) |
```

5. Commit and push changes to GitHub for links to appear in Clinical Plan Builder

## Verification Workflow

1. Extract all citations from template
2. Categorize by priority tier
3. Search and verify each citation (HIGH priority first)
4. Document findings in verification report
5. Generate correction list compatible with neuro-rebuilder
6. Physician reviews flagged citations
7. Corrections implemented via rebuilder
8. Re-verify any changed citations
9. Proceed to CPT/synonym enrichment

## Limitations

- Some sources may be paywalled (note as "Unable to Verify - Paywall")
- Very old sources may not be indexed online
- Non-English sources may be difficult to verify
- Preprint/unpublished data cannot be fully verified
- Conference abstracts may not be findable

When a source cannot be verified due to access limitations, recommend physician verification or suggest alternative citable sources.

## Change Log

**v1.1 (January 2026)**
- Added clickable source links (PubMed, DOI, organization websites) to all verification output tables
- New Step 5: Capture Source Links with link hierarchy guidance
- Updated output format to include Link column in all citation tables

**v1.0 (January 2026)**
- Initial version
- Comprehensive citation verification framework
- Output format designed for rebuilder integration
- Priority tiers for verification effort allocation
