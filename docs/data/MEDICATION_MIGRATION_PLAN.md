# Medication Validation & Migration Plan

## Overview

This document outlines the plan to validate and migrate 1,048 unique medications from plan files to the central medication database (`medications.json`), ensuring all entries are verified against the [RxNorm API](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html) to prevent hallucinations and ensure hospital safety.

## Current State

| Metric | Count |
|--------|-------|
| Unique medications in plan files | 1,048 |
| Medications in central DB | 11 |
| Medications needing validation | 1,037 |
| Total medication references across plans | 2,937 |

## API Constraints

### RxNorm API
- **Rate Limit**: 20 requests/second (we use 10/sec for safety)
- **Cost**: Free (NLM public data)
- **Validation Time**: ~2 minutes for all 1,048 medications

### OpenFDA API
- **Rate Limit**: 240 requests/minute (~4/sec)
- **Cost**: Free
- **Purpose**: Cross-check black box warnings

## Batch Migration Strategy

### Phase 1: Initial Validation Run (Day 1)
**Goal**: Identify which medications are valid vs. potentially hallucinated

```bash
# Run full batch validation (takes ~2 minutes)
python scripts/validate_medication.py --batch-from-plans --save-report docs/data/validation-report.md
```

**Expected Output**:
- List of valid medications with RxCUI codes
- List of invalid medications (possible hallucinations or non-drug items)
- Black box warning flags

### Phase 2: Triage Invalid Medications (Day 1-2)
**Goal**: Categorize invalid entries

Invalid medications typically fall into these categories:

| Category | Example | Action |
|----------|---------|--------|
| **Non-medications** | "Airway management", "Active rewarming" | Exclude from central DB (keep in plans as interventions) |
| **Combination names** | "Acetaminophen-aspirin-caffeine" | Map to component drugs or add as combination |
| **Misspellings** | "Levetiracitam" | Correct spelling, re-validate |
| **Brand names not in RxNorm** | "Mestinon Timespan" | Map to generic (pyridostigmine) |
| **Investigational drugs** | Some newer biologics | Flag for manual review, add with "unverified" status |
| **True hallucinations** | Completely fabricated drugs | Remove from plans |

### Phase 3: Priority Migration (Week 1)
**Goal**: Add highest-impact medications to central DB first

**Priority 1: Top 50 medications by frequency** (covers ~60% of references)
- Gabapentin (44 plans), Levetiracetam (37 plans), Pregabalin (29 plans)...

**Priority 2: High-risk medications** (black box warnings, narrow therapeutic index)
- Carbamazepine, valproic acid, phenytoin, warfarin...

**Priority 3: Medications with complex dosing contexts**
- Steroids (different doses for MS vs MG vs CIDP)
- Immunosuppressants

### Phase 4: Complete Migration (Week 2-3)
**Goal**: Add remaining validated medications

```bash
# For each validated medication:
python scripts/validate_medication.py <medication-name> --add-to-db
```

### Phase 5: Ongoing Validation (Continuous)
**Goal**: Validate new medications as they're added to plans

Add to CLAUDE.md workflow:
```bash
# Before marking any plan as complete:
python scripts/validate_medication.py <new-medication> --add-to-db
```

## Estimated Timeline

| Phase | Duration | Medications |
|-------|----------|-------------|
| Phase 1: Initial validation | 2 minutes | 1,048 (validate) |
| Phase 2: Triage | 2-4 hours | ~200 invalid (review) |
| Phase 3: Priority migration | 3-4 hours | ~100 (add to DB) |
| Phase 4: Complete migration | 2-3 days | ~800 remaining |
| Phase 5: Ongoing | Continuous | New additions |

## Safety Checks

### Pre-Migration Validation
Each medication must pass:
1. ✓ RxNorm lookup returns valid RxCUI
2. ✓ Drug name matches RxNorm canonical name (or synonym)
3. ✓ Black box warnings identified (if any)
4. ✓ Renal/hepatic adjustment data included

### Post-Migration Verification
```bash
# Verify central DB is valid JSON
python scripts/generate_json.py docs/plans/*.md --validate-only

# Run medication resolver tests
python scripts/medication_resolver.py --list
python scripts/medication_resolver.py --black-box
```

## Commands Reference

```bash
# Validate single medication
python scripts/validate_medication.py gabapentin

# Validate central database
python scripts/validate_medication.py --validate-db

# Dry run batch validation
python scripts/validate_medication.py --batch-from-plans --dry-run

# Full batch validation with report
python scripts/validate_medication.py --batch-from-plans --save-report docs/data/validation-report.md

# Test mode (no API calls)
python scripts/validate_medication.py --test
```

## Network Requirements

The validation script requires external API access:
- `rxnav.nlm.nih.gov` (RxNorm API)
- `api.fda.gov` (OpenFDA API)

If running in a restricted environment, use `--test` mode to verify script logic, then run full validation in an unrestricted environment.

## Attribution

This product uses publicly available data from the U.S. National Library of Medicine (NLM), National Institutes of Health, Department of Health and Human Services; NLM is not responsible for the product and does not endorse or recommend this or any other product.

---

*Last updated: 2026-02-06*
