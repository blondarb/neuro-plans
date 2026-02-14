# Guideline Maintenance Process

Procedures for keeping clinical plan content aligned with current guidelines.

## Overview

NeuroPlans references ~50 clinical practice guidelines and ~55 landmark trials. Guidelines are updated periodically by their issuing organizations. This document describes how to detect and respond to guideline changes.

## Monthly Freshness Check

Run the freshness checker on the 1st of each month (or after any major guideline release):

```bash
python3 scripts/check_guideline_freshness.py --cache
```

This produces two outputs:
- **Console summary** — quick pass/fail with counts
- **`docs/data/freshness-report.md`** — detailed report with flagged items, age tiers, and affected plans

### Interpreting the Report

The report has four sections:

| Section | What It Shows | Action Required |
|---------|---------------|-----------------|
| **Items Requiring Review** | Newer PubMed version found, or PMID retracted/erratum | Update plan references and content immediately |
| **Aging Guidelines (≥8yr)** | Old guideline, no newer PubMed version detected | Check the society website for updates not yet on PubMed |
| **Review Recommended (≥5yr)** | Moderately old guideline | Verify content still reflects current practice |
| **Current** | No issues detected | No action needed |

### Important Caveat

The freshness checker searches PubMed for newer publications. Some guideline updates are:
- Published on society websites but not yet on PubMed
- Published as "reaffirmations" without a new PMID
- Published under a different organization or different title

For aging guidelines (≥8yr), always manually check the relevant society website.

## When a Newer Guideline Is Found

### Step 1: Link Update (5 min per plan)

Update the PubMed link in the evidence table and any inline references:

1. Confirm the new PMID is correct by checking the PubMed page
2. Add the new PMID to `scripts/landmark_pmids.json`
3. Find all plan files referencing the old guideline (listed in the freshness report)
4. Update links in Section 8 (Evidence & References) and any inline references
5. Run `python3 scripts/verify_citations.py --all --verify --cache` to confirm

### Step 2: Content Alignment Review (15-30 min per plan)

This is the critical step that the freshness checker cannot automate. Compare the old and new guideline to identify changed recommendations:

1. **Read the new guideline's abstract/summary** (PubMed, society website, or full text if available)
2. **Identify changed recommendations** — what's new, modified, or withdrawn?
3. **Compare against plan content** — do our treatment tables, dosing, indications, contraindications, or monitoring match the new recommendations?
4. **Update plan content** where it diverges from the new guideline
5. **Update the evidence table** with new evidence levels if they changed

### Common Types of Guideline Changes

| Change Type | Example | Plan Sections Affected |
|-------------|---------|----------------------|
| New drug class recommendation | Tenecteplase upgraded from IIa to Class I | Treatment (3A), Evidence (8) |
| Expanded indication | Thrombectomy now includes ASPECTS 3-5 | Treatment (3A), Appendix |
| New contraindication/warning | Topiramate teratogenicity warning | Treatment (3B/3C), Patient Instructions (4B) |
| New diagnostic tool | CTS-6 prediction tool recommended | Appendix, Referrals (4A) |
| Withdrawn recommendation | Aggressive early mobilization <24h harmful | Treatment (3B), Disposition (7) |
| New monitoring requirement | Additional labs or imaging | Labs (1), Imaging (2), Monitoring (6) |

### Step 3: Regenerate and Sync

After updating plan markdown files:

```bash
# Regenerate JSON
python3 scripts/generate_json.py --all --merge --quiet

# Copy to iOS bundle
cp docs/data/plans.json ios/NeuroPlans/NeuroPlans/Resources/plans.json

# Verify parity
python3 scripts/generate_json.py --all --check-parity
```

## Handling Aging Guidelines (No Newer Version Found)

For guidelines ≥5-8 years old that the freshness checker marks as "current" (no newer PubMed version detected):

1. **Check the issuing society's website** for updates, reaffirmations, or retirement notices
2. **Search PubMed manually** with broader terms (the checker's automated search has limitations)
3. **If the guideline is still current**: No changes needed; note the verification date
4. **If a newer version exists that the checker missed**: Update `landmark_pmids.json` with the new PMID and follow Steps 1-3 above
5. **If the guideline has been retired without replacement**: Add a note in the plan indicating limited/dated evidence

## Organization Website Quick Reference

| Organization | Guidelines Page |
|--------------|----------------|
| AAN | https://www.aan.com/practice/guidelines |
| AHA/ASA | https://professional.heart.org/en/guidelines-and-statements |
| IDSA | https://www.idsociety.org/practice-guideline |
| NCS | https://www.neurocriticalcare.org/guidelines |
| EFNS/EAN | https://www.ean.org/research/ean-guidelines |
| ACOG | https://www.acog.org/clinical |
| WHO | https://www.who.int/publications/guidelines |

## Quarterly Review Cadence

| Month | Focus |
|-------|-------|
| January | Full freshness check; review all aging (≥8yr) guidelines |
| April | Full freshness check; review society websites for recent releases |
| July | Full freshness check; focus on stroke/vascular guidelines (AHA cycle) |
| October | Full freshness check; focus on AAN guidelines (annual meeting cycle) |
