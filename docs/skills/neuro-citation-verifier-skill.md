---
name: neuro-citation-verifier
description: Validates citations and evidence references in clinical decision support templates. Uses web search to verify that cited studies, guidelines, and sources exist and accurately support the claims made. Identifies hallucinated or inaccurate citations. Run after neuro-checker validation is complete and content is stable.
---

# Neuro Citation Verifier

Systematically verify all citations and evidence references in clinical recommendation templates to ensure accuracy and prevent hallucinated sources.

## CRITICAL: Preventing PMID Hallucinations

**NEVER guess or assume a PubMed ID.** Hallucinated PMIDs that link to wrong articles are dangerous and misleading.

### Mandatory Verification Steps

Before adding ANY PubMed link, you MUST:

1. **Search for the specific article** using WebSearch with author, title keywords, journal, and year
2. **Find the actual PMID** in the search results (look for "PMID:" or pubmed.ncbi.nlm.nih.gov URLs)
3. **Verify the PMID** by fetching the PubMed page and confirming:
   - Author names match
   - Title matches or is very close
   - Journal matches
   - Year matches
4. **Only then add the link** to the citation

### What NOT to Do

| ❌ DO NOT | ✅ DO INSTEAD |
|-----------|---------------|
| Guess PMIDs based on patterns | Search and verify each one |
| Assume PMID from memory | Fetch the actual PubMed page |
| Add links without clicking through | Verify the linked article is correct |
| Use placeholder PMIDs | Leave as plain text if can't verify |

### When You Cannot Verify

If you cannot find or verify a PMID:
- **Leave the citation as plain text** (no link)
- **Log it** in the verification report as "Unable to verify"
- **Flag for physician review** - they may know the correct source
- **NEVER fabricate a PMID** - wrong links are worse than no links

### Example Correct Process

```
Citation to verify: "Dyck PJ et al. Neurology 1993" (diabetes polyneuropathy)

1. Search: "Dyck diabetic polyneuropathy Neurology 1993 PMID"
2. Find in results: "PMID: 8469345" with title matching
3. Fetch: https://pubmed.ncbi.nlm.nih.gov/8469345/
4. Verify page shows:
   - Authors: Dyck PJ, et al.
   - Journal: Neurology
   - Year: 1993
   - Topic: Diabetic polyneuropathy
5. Confirmed - add link
```

---

## CRITICAL: PMID Content Verification

### Why PMIDs Get Wrong

PMIDs are assigned sequentially. Papers published in the same journal issue often have **consecutive PMIDs**. This leads to common errors:

| Error Type | Example | How It Happens |
|------------|---------|----------------|
| Off-by-one | PMID 15590952 vs 15590953 | Two NEJM papers in same issue (Fahn ELLDOPA vs Emre rivastigmine) |
| Similar topic | PMID 8869765 vs 8792038 | Both 1996 Cephalalgia papers (CGRP vs Magnesium) |
| Same author, different study | Multiple Cochrane reviews | Author has many systematic reviews |
| Wrong section | PMID 38078586 vs 38078577 | ADA Standards Section 6 vs Section 12 |

### Mandatory PMID Verification Checklist

For EVERY PMID, you MUST verify:

- [ ] **Title matches** - The actual paper title supports the claim
- [ ] **Authors match** - First/last author names are correct
- [ ] **Journal matches** - Published in the claimed journal
- [ ] **Year matches** - Publication year is correct
- [ ] **Content supports claim** - The finding you're citing actually exists in this paper

### Search Pattern for PMID Verification

```
Search: "PMID [number] [author name] [journal] [year] [topic]"
```

Example: `"PMID 8792038 Peikert Cephalalgia 1996 magnesium migraine"`

If the search doesn't return results confirming the paper matches your claim, the PMID is likely wrong.

### Use the Citation Verification Script

Run `scripts/verify_citations.py` to validate PMIDs at multiple levels:

```bash
# STEP 1 — Offline lint (always run first, no API needed)
# Catches format errors, out-of-range PMIDs, and year-vs-PMID mismatches
python scripts/verify_citations.py --all --lint

# STEP 2 — API verification (requires PubMed API access)
# Checks each PMID exists and metadata matches claimed citation
python scripts/verify_citations.py docs/plans/migraine.md --verify

# STEP 3 — With caching (recommended: avoids re-verifying known-good PMIDs)
python scripts/verify_citations.py --all --verify --cache

# STEP 4 — Find correct PMIDs for mismatches
python scripts/verify_citations.py --all --repair --apply --cache
```

**Mandatory gate:** The `--lint` check MUST pass (exit code 0) before a plan can be marked `completed` in the queue. This catches hallucinated PMIDs offline without needing API access.

The `--verify` mode will now fail fast if the PubMed API is unreachable, instead of silently reporting 0% accuracy. Use `--cache` to store results from previous runs and avoid redundant API calls.

---

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
6. **Log results to `docs/logs/citation-verification-log.md`** (NEW)
7. Physician reviews flagged citations
8. Corrections implemented via rebuilder
9. Re-verify any changed citations
10. Proceed to CPT/synonym enrichment

## Verification Logging (Required)

**CRITICAL:** After each verification, append results to the central log at `docs/logs/citation-verification-log.md`. This enables pattern analysis and process improvement.

### What to Log

For each plan verified, add:

1. **Summary entry** - Add counts to the Summary Statistics table
2. **Plan section** - Create new section under "Verification Results by Plan" with:
   - Date verified
   - Version
   - List of verified citations with PubMed IDs
   - List of non-PubMed sources
   - List of citations unable to verify (with reasons)
   - Corrections made

### Log Entry Template

```markdown
### [Plan Name]

**Date Verified:** YYYY-MM-DD
**Version:** X.X → X.X
**Verifier:** Claude (neuro-citation-verifier)

#### Verified Citations (X)

| # | Citation | PubMed ID | Status |
|---|----------|-----------|--------|
| 1 | [Author et al. Journal Year] | [PMID](link) | ✅ Verified |

#### Unable to Verify (X)

| # | Citation | Reason | Recommendation |
|---|----------|--------|----------------|
| 1 | [Citation] | [Why unverifiable] | [Suggested action] |

#### Corrections Made (X)

| # | Original Citation | Issue | Corrected To |
|---|-------------------|-------|--------------|
| 1 | [Original] | [Problem] | [Fixed citation] |
```

### Pattern Tracking

When logging, note any patterns in the "Patterns & Improvement Opportunities" section:

| Pattern Type | Example |
|--------------|---------|
| Trial confusion | Multiple trials for same drug, different indications |
| Generic references | "Multiple RCTs" without specific citations |
| Outdated guidelines | Citing old version when newer exists |
| Author name variations | Different spellings across sources |
| Paywall barriers | Cannot access to verify content |

This data helps improve the builder and checker skills over time.

## Limitations

- Some sources may be paywalled (note as "Unable to Verify - Paywall")
- Very old sources may not be indexed online
- Non-English sources may be difficult to verify
- Preprint/unpublished data cannot be fully verified
- Conference abstracts may not be findable

When a source cannot be verified due to access limitations, recommend physician verification or suggest alternative citable sources.

## Change Log

**v1.3 (January 2026)**
- Added CRITICAL section on PMID content verification with common error types
- Added mandatory PMID verification checklist
- Documented the `scripts/verify_citations.py` helper tool
- Added examples of off-by-one and consecutive PMID errors

**v1.2 (January 2026)**
- Added required verification logging to `docs/logs/citation-verification-log.md`
- New "Verification Logging (Required)" section with log entry template
- Added pattern tracking for continuous improvement
- Updated workflow to include logging step

**v1.1 (January 2026)**
- Added clickable source links (PubMed, DOI, organization websites) to all verification output tables
- New Step 5: Capture Source Links with link hierarchy guidance
- Updated output format to include Link column in all citation tables

**v1.0 (January 2026)**
- Initial version
- Comprehensive citation verification framework
- Output format designed for rebuilder integration
- Priority tiers for verification effort allocation
