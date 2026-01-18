---
name: neuro-workflow
description: Master workflow document for the neuro clinical decision support template system. Defines the 5-skill pipeline from template creation through deployment.
---

# Neuro Clinical Decision Support Workflow

## Overview

This workflow produces validated, citation-verified, billing-ready clinical decision support templates for neurological diagnoses.

## Skill Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐                           │
│   │  BUILDER │────▶│  CHECKER │◀───▶│ REBUILDER│                           │
│   │   v2.2   │     │   v2.2   │     │   v1.0   │                           │
│   └──────────┘     └────┬─────┘     └──────────┘                           │
│                         │                                                   │
│                         │ ≥90% Score                                        │
│                         ▼                                                   │
│                   ┌──────────┐                                              │
│                   │ CITATION │                                              │
│                   │ VERIFIER │                                              │
│                   │   v1.0   │                                              │
│                   └────┬─────┘                                              │
│                        │                                                    │
│                        ▼                                                    │
│                   ┌──────────┐                                              │
│                   │CPT/SYNON │                                              │
│                   │ ENRICHER │                                              │
│                   │   v1.0   │                                              │
│                   └────┬─────┘                                              │
│                        │                                                    │
│                        ▼                                                    │
│                   ┌──────────┐                                              │
│                   │PHYSICIAN │                                              │
│                   │  REVIEW  │                                              │
│                   └────┬─────┘                                              │
│                        │                                                    │
│                        ▼                                                    │
│                   ┌──────────┐                                              │
│                   │  DEPLOY  │                                              │
│                   └──────────┘                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: BUILD

**Skill:** `neuro-builder-SKILL-v2.2.md`

**Input:** Diagnosis name and scope (e.g., "New Onset Seizure", "MS Exacerbation")

**Process:**
1. Identify diagnosis scope (new onset, exacerbation, chronic, refractory)
2. Generate 8-section template with multi-column format
3. Ensure coverage across all settings (ED, HOSP, OPD, ICU)
4. Include comprehensive treatments with individual drug rows
5. Add diagnosis-specific Section 4 content

**Output:** Initial template `[diagnosis]-v1.0.md`

**Quality Gate:** Template must have all 8 sections populated

---

## Phase 2: VALIDATE

**Skill:** `neuro-checker-SKILL-v2.2.md`

**Input:** Template from Phase 1

**Process:**
1. Score across 6 domains (Completeness, Accuracy, Safety, Objectivity, Setting Appropriateness, Usability)
2. Assess setting coverage (ED, HOSP, OPD, ICU)
3. Assess medication comprehensiveness
4. Assess Section 6 monitoring parameters
5. Generate detailed revision recommendations

**Output:** Validation report with scores and revision list

**Quality Gate:** Must achieve ≥90% (54/60) to proceed

### If Score <90%: REBUILD

**Skill:** `neuro-rebuilder-SKILL` (or manual revision)

**Input:** Original template + Checker revision recommendations

**Process:**
1. Review each recommended revision
2. Physician approves/modifies/rejects each suggestion
3. Implement approved changes
4. Increment version number

**Output:** Revised template `[diagnosis]-v1.x.md`

**Then:** Return to Phase 2 (Validate) and re-check

---

## Phase 3: VERIFY CITATIONS

**Skill:** `neuro-citation-verifier-SKILL-v1.md`

**Input:** Validated template (≥90% score)

**Process:**
1. Extract all citations from Section 8 and inline references
2. Prioritize by safety impact (drug dosing > diagnostic criteria > epidemiology)
3. Web search to verify each citation exists and supports claim
4. Flag: ✅ Verified, ⚠️ Partial Match, ❌ Not Found, ❌ Inaccurate

**Output:** Citation verification report

**Quality Gate:** All HIGH priority citations verified or corrected

### If Citations Need Correction:

1. Generate correction list for Rebuilder
2. Physician reviews flagged citations
3. Implement corrections
4. Re-verify changed citations

---

## Phase 4: ENRICH

**Skill:** `neuro-cpt-synonym-enricher-SKILL-v1.md`

**Input:** Citation-verified template

**Process:**
1. Identify all codeable items (labs, imaging, procedures, infusions)
2. Search and verify CPT/HCPCS codes
3. Collect clinical synonyms (abbreviations, brand names, lay terms)
4. Generate enrichment report

**Output:**
- CPT code mapping table
- Synonym index
- Enriched template ready for integration

**Quality Gate:** All common procedures have verified codes

---

## Phase 5: PHYSICIAN REVIEW

**Input:** Enriched template with all supporting reports

**Reviewer Checklist:**
- [ ] Clinical accuracy verified
- [ ] Drug dosing appropriate
- [ ] Contraindications complete
- [ ] Citations accurate
- [ ] CPT codes appropriate for institution
- [ ] Synonyms include local terminology
- [ ] Safe for clinical deployment

**Output:** Signed-off template ready for deployment

---

## Phase 6: DEPLOY

**Input:** Physician-approved template

**Deployment Options:**
1. **EHR Integration** - Convert to order sets, clinical pathways
2. **Web Tool** - Interactive plan builder artifact
3. **Document Library** - PDF/DOCX for reference
4. **API** - JSON format for third-party integration

---

## File Naming Convention

| Phase | Artifact | Filename |
|-------|----------|----------|
| Build | Initial template | `[diagnosis]-v1.0.md` |
| Check | Validation report | `[diagnosis]-checker-report-[date].md` |
| Rebuild | Revised template | `[diagnosis]-v1.x.md` |
| Citation Verify | Verification report | `[diagnosis]-citation-report-[date].md` |
| Enrich | Enriched template | `[diagnosis]-v2.0.md` |
| Enrich | CPT mapping table | `[diagnosis]-cpt-codes.md` |
| Enrich | Synonym list | `[diagnosis]-synonyms.md` |
| Final | Approved template | `[diagnosis]-FINAL-v2.x.md` |

---

## Estimated Timeline per Template

| Phase | Estimated Time | Notes |
|-------|----------------|-------|
| Build | 15-30 min | Depends on diagnosis complexity |
| Check | 10-15 min | Automated with review |
| Rebuild | 10-20 min | Depends on revision count; may iterate |
| Citation Verify | 20-40 min | Web search intensive |
| Enrich | 15-30 min | Web search for codes |
| Physician Review | Variable | Depends on reviewer availability |

**Total Claude time:** ~1-2 hours per template
**Total including physician review:** Variable

---

## Quick Reference: Which Skill to Use

| Task | Skill |
|------|-------|
| Create new template from scratch | neuro-builder |
| Validate existing template | neuro-checker |
| Implement revisions from checker | neuro-rebuilder |
| Verify citations are accurate | neuro-citation-verifier |
| Add CPT codes and synonyms | neuro-cpt-synonym-enricher |

---

## Skill File Versions

| Skill | Current Version | Last Updated |
|-------|-----------------|--------------|
| neuro-builder | v2.2 | January 14, 2026 |
| neuro-checker | v2.2 | January 14, 2026 |
| neuro-rebuilder | v1.0 | January 13, 2026 |
| neuro-citation-verifier | v1.0 | January 2026 |
| neuro-cpt-synonym-enricher | v1.0 | January 2026 |

---

## Change Log

**v2.0 (January 2026)**
- Added Citation Verifier skill (Phase 3)
- Added CPT/Synonym Enricher skill (Phase 4)
- Expanded workflow to 5 skills + physician review
- Added quality gates between phases
- Added file naming convention
- Added artifact outputs table
- Added timeline estimates

**v1.0 (January 13, 2026)**
- Initial workflow with Builder, Checker, Rebuilder
