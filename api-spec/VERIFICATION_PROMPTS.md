# Multi-Model Verification Prompts

> **Purpose:** Independent verification prompts for Claude Opus 4.5 (clinical verification) and Gemini 3 Pro (citation verification). These run AFTER GPT-5.2 generates the initial plan.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     MULTI-MODEL VERIFICATION PIPELINE                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  INPUT: Generated clinical plan from GPT-5.2                            │
│                                                                          │
│  ┌──────────────────────┐    ┌──────────────────────┐                   │
│  │  STAGE 2A            │    │  STAGE 2B            │                   │
│  │  Claude Opus 4.5     │    │  Gemini 3 Pro        │                   │
│  │  ─────────────────   │    │  ─────────────────   │                   │
│  │  Clinical Verifier   │    │  Citation Verifier   │                   │
│  │                      │    │                      │                   │
│  │  • Medication dosing │    │  • PubMed lookup     │                   │
│  │  • Contraindications │    │  • DOI validation    │                   │
│  │  • Drug interactions │    │  • Author/year check │                   │
│  │  • Clinical logic    │    │  • Guideline sources │                   │
│  │                      │    │                      │                   │
│  │  Cost: ~$0.10/plan   │    │  Cost: ~$0.05/plan   │                   │
│  └──────────┬───────────┘    └──────────┬───────────┘                   │
│             │                           │                                │
│             └─────────┬─────────────────┘                                │
│                       ▼                                                  │
│  ┌──────────────────────────────────────────────────────────────┐       │
│  │  STAGE 3: Discrepancy Resolution                              │       │
│  │  • Merge verification reports                                 │       │
│  │  • Flag items needing human review                           │       │
│  │  • Auto-fix clear errors                                     │       │
│  └──────────────────────────────────────────────────────────────┘       │
│                       │                                                  │
│                       ▼                                                  │
│  OUTPUT: Verified plan + verification report                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Stage 2A: Clinical Verification (Claude Opus 4.5)

### System Prompt

```
You are a clinical pharmacist and neurologist reviewing a clinical decision support plan for accuracy and safety.

Your task is to verify:
1. Medication dosing is within standard ranges
2. All critical contraindications are listed
3. Drug-drug interactions are noted where relevant
4. Monitoring requirements are appropriate
5. Clinical recommendations are evidence-based

OUTPUT FORMAT:
For each medication, output ONE line:
✅ OK: [Drug name] - dosing and safety info verified
⚠️ FLAG: [Drug name] - [specific concern requiring physician review]
❌ ERROR: [Drug name] - [critical safety issue that must be fixed]

At the end, provide:
## SUMMARY
- Total medications reviewed: X
- Verified OK: X
- Flagged for review: X
- Critical errors: X

## CRITICAL ERRORS (must fix)
[List each error with specific correction]

## FLAGS FOR PHYSICIAN REVIEW
[List each flag with context]

## SUGGESTED ADDITIONS
[Any missing contraindications, interactions, or monitoring]
```

### User Prompt Template

```
Review this clinical plan for [DIAGNOSIS NAME].

Focus on:
1. Are drug doses within standard therapeutic ranges?
2. Are contraindications complete for each medication?
3. Are there missing drug-drug interactions?
4. Is monitoring appropriate for each medication?
5. Are there any dangerous omissions?

CLINICAL PLAN:
---
[INSERT GENERATED PLAN HERE]
---

Provide your verification report.
```

### Expected Token Usage

| Component | Tokens |
|-----------|--------|
| System prompt | ~400 |
| Plan content | ~8,000-12,000 |
| Output | ~1,500-2,500 |
| **Total** | ~10,000-15,000 |

### Cost Estimate (Claude Opus 4.5)

- Input: ~12,000 tokens × $5/1M = $0.06
- Output: ~2,000 tokens × $25/1M = $0.05
- **Total: ~$0.11 per plan**

---

## Stage 2B: Citation Verification (Gemini 3 Pro)

### System Prompt

```
You are a medical librarian verifying citations in a clinical document.

For each citation, you must:
1. Search for the article/guideline
2. Verify it exists
3. Confirm authors, year, and journal match
4. Return the PubMed ID (PMID) if found

OUTPUT FORMAT for each citation:
✅ VERIFIED: [Citation] → PMID: [number] | [Title matches: YES/PARTIAL] | [Year: CORRECT/OFF BY X]
⚠️ PARTIAL: [Citation] → Found similar: [actual citation details] | Suggested correction: [correction]
❌ NOT FOUND: [Citation] → Searched: [search terms used] | Recommendation: [remove/replace/flag for physician]
❓ UNABLE TO VERIFY: [Citation] → Reason: [paywall/non-indexed/etc]

IMPORTANT:
- NEVER guess or fabricate a PMID
- If uncertain, mark as UNABLE TO VERIFY
- Include search terms you used

At the end, provide:
## CITATION SUMMARY
- Total citations: X
- Verified with PMID: X
- Partial match: X
- Not found: X
- Unable to verify: X

## CORRECTIONS NEEDED
[List specific corrections in format: "Change [original] to [corrected]"]

## PMID LINKS TO ADD
[List verified citations with their PubMed links]
```

### User Prompt Template

```
Verify the following citations from a clinical plan for [DIAGNOSIS NAME].

For each citation:
1. Search PubMed and Google Scholar
2. Verify the source exists
3. Confirm author names, year, and journal
4. Return the PMID if found

CITATIONS TO VERIFY:
---
[EXTRACT SECTION 8 FROM PLAN]

Example format of citations you'll see:
| Lorazepam first-line for SE | Class I, Level A | Alldredge et al. NEJM 2001 |
| IV levetiracetam efficacy | Class I, Level B | Kapur et al. Lancet Neurol 2019 |
---

Provide your verification report with PMIDs for all verified citations.
```

### Expected Token Usage

| Component | Tokens |
|-----------|--------|
| System prompt | ~350 |
| Citations (Section 8) | ~1,500-2,500 |
| Output | ~2,000-3,000 |
| **Total** | ~4,000-6,000 |

### Cost Estimate (Gemini 3 Pro)

- Input: ~4,000 tokens × $2/1M = $0.008
- Output: ~2,500 tokens × $12/1M = $0.03
- **Total: ~$0.04 per plan**

---

## Discrepancy Handling

### Severity Classification

| Severity | Definition | Action |
|----------|------------|--------|
| **CRITICAL** | Safety issue (wrong dose, missing contraindication) | Block deployment, auto-flag for human |
| **HIGH** | Accuracy issue (wrong citation, incomplete info) | Require correction before deployment |
| **MEDIUM** | Quality issue (formatting, completeness) | Note for improvement, allow deployment |
| **LOW** | Style issue (wording, organization) | Optional fix |

### Auto-Fix Rules

The pipeline can automatically fix these issues without human review:

| Issue Type | Auto-Fix Action |
|------------|-----------------|
| Citation year off by 1 | Correct to verified year |
| Author name spelling | Correct to PubMed spelling |
| Missing PMID link | Add verified PMID link |
| Formatting inconsistency | Standardize format |

### Human Review Required

These issues MUST be flagged for physician review:

| Issue Type | Why Human Needed |
|------------|------------------|
| Dose outside standard range | Clinical judgment needed |
| Missing contraindication | Safety decision |
| Conflicting recommendations | Clinical expertise required |
| Citation not found | May know correct source |
| Drug interaction flagged | Risk-benefit assessment |

---

## Verification Report Schema

### JSON Output Format

```json
{
  "plan_id": "guillain-barre-new-diagnosis",
  "verification_timestamp": "2026-01-25T10:30:00Z",
  "clinical_verification": {
    "model": "claude-opus-4.5",
    "status": "passed|flagged|failed",
    "medications_reviewed": 15,
    "ok_count": 12,
    "flagged_count": 2,
    "error_count": 1,
    "errors": [
      {
        "medication": "Methylprednisolone",
        "issue": "Dose exceeds standard range",
        "current": "2000 mg IV daily",
        "recommended": "1000 mg IV daily",
        "severity": "critical",
        "auto_fixable": false
      }
    ],
    "flags": [
      {
        "medication": "IVIG",
        "issue": "Consider adding renal function monitoring",
        "severity": "medium",
        "auto_fixable": false
      }
    ]
  },
  "citation_verification": {
    "model": "gemini-3-pro",
    "status": "passed|flagged|failed",
    "total_citations": 12,
    "verified_count": 10,
    "partial_count": 1,
    "not_found_count": 1,
    "corrections": [
      {
        "original": "Hughes et al. Lancet 2006",
        "corrected": "Hughes et al. Lancet Neurol 2007",
        "pmid": "17462515",
        "auto_fixable": true
      }
    ],
    "pmids_to_add": [
      {
        "citation": "Alldredge et al. NEJM 2001",
        "pmid": "11547716",
        "link": "https://pubmed.ncbi.nlm.nih.gov/11547716/"
      }
    ]
  },
  "overall_status": "passed|needs_review|blocked",
  "human_review_required": true,
  "human_review_items": [
    "Methylprednisolone dose verification",
    "Citation not found: Smith et al. 2019"
  ],
  "auto_fixes_applied": [
    "Corrected Hughes citation year",
    "Added 10 PMID links"
  ]
}
```

---

## Integration with Pipeline

### API Call Sequence

```python
# Stage 1: Generate plan with GPT-5.2
plan = call_gpt52(system_prompt=SYSTEM_PROMPT, user_prompt=f"Generate clinical plan for: {diagnosis}")

# Stage 2A & 2B: Run verification in parallel
clinical_result, citation_result = await asyncio.gather(
    call_claude_opus(CLINICAL_VERIFICATION_PROMPT, plan),
    call_gemini_pro(CITATION_VERIFICATION_PROMPT, extract_citations(plan))
)

# Stage 3: Merge and resolve
verification_report = merge_verification_results(clinical_result, citation_result)

# Apply auto-fixes
if verification_report.auto_fixable_count > 0:
    plan = apply_auto_fixes(plan, verification_report)

# Check if human review needed
if verification_report.human_review_required:
    save_for_review(plan, verification_report)
else:
    deploy_plan(plan)
```

---

## Cost Summary

| Stage | Model | Cost/Plan |
|-------|-------|-----------|
| Generation | GPT-5.2 | $0.15 |
| Clinical verification | Claude Opus 4.5 | $0.11 |
| Citation verification | Gemini 3 Pro | $0.04 |
| **Total** | | **$0.30** |

### Cost Optimization Options

| Option | Approach | Cost/Plan | Trade-off |
|--------|----------|-----------|-----------|
| Full verification | GPT-5.2 + Claude + Gemini | $0.30 | Maximum safety |
| Reduced verification | GPT-5.2 + Claude only | $0.26 | Skip citation PMIDs |
| Budget mode | GPT-5.2 + Gemini for both | $0.23 | Less thorough clinical check |
| Minimum viable | GPT-5.2 only | $0.15 | No independent verification |

---

## Version

v1.0 - January 2026
