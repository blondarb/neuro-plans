# Medication Validation Handoff

## Quick Start (Run These Commands)

```bash
# Step 1: Validate the 11 medications already in central DB
python scripts/validate_medication.py --validate-db --save-report docs/data/db-validation-report.md

# Step 2: Batch validate all 1,048 medications from plans (~2 min)
python scripts/validate_medication.py --batch-from-plans --save-report docs/data/full-validation-report.md

# Step 3: Review reports and commit results
git add docs/data/*.md docs/data/.medication_cache.json
git commit -m "Add medication validation reports with RxCUI provenance"
git push
```

## What These Commands Do

### Step 1: `--validate-db`
Validates the 11 medications already in `medications.json`:
- Gabapentin, Pregabalin, Duloxetine, Amitriptyline
- Carbamazepine, Propranolol, Levetiracetam, Sumatriptan
- Prednisone, Pyridostigmine, Baclofen

**Expected output**: All 11 should be VALID with RxCUI codes.

### Step 2: `--batch-from-plans`
Validates all 1,048 unique medications found across plan files:
- Rate: 10 requests/second (safe margin)
- Time: ~2 minutes
- Output: Report showing valid vs invalid medications

**Expected results**:
- ~800-900 valid (real drugs with RxCUI)
- ~100-200 invalid (non-medications like "Airway management", misspellings, or combinations)

### Step 3: Review & Commit
The reports will show:
- Which medications are confirmed real (with RxCUI)
- Which need manual review (invalid list)
- Which have black box warnings

## After Validation: Next Steps

### For Valid Medications
These can be added to the central database with confidence. The RxCUI serves as provenance that the drug is real.

### For Invalid Medications
Review and categorize:

| Category | Example | Action |
|----------|---------|--------|
| Non-medications | "Airway management", "IV fluids" | Keep in plans, don't add to central DB |
| Combinations | "Acetaminophen-aspirin-caffeine" | Add as combination or map to components |
| Misspellings | "Levetiracitam" | Fix in plans, re-validate |
| Brand names | "Mestinon Timespan" | Map to generic (pyridostigmine) |
| New/rare drugs | Some biologics | Flag for manual verification |

## Files Created

| File | Purpose |
|------|---------|
| `scripts/validate_medication.py` | RxNorm/OpenFDA validation script |
| `scripts/medication_resolver.py` | Central DB lookup and enrichment |
| `scripts/extract_medications.py` | Extract medications from plans |
| `docs/data/medications.json` | Central medication database (11 meds) |
| `docs/data/MEDICATION_MIGRATION_PLAN.md` | Full migration strategy |
| `docs/data/.medication_cache.json` | API response cache (gitignored) |

## API Information

**RxNorm API** (NIH/NLM)
- URL: `https://rxnav.nlm.nih.gov/REST/`
- Rate limit: 20 req/sec (we use 10)
- No API key required
- Returns RxCUI (unique drug identifier)

**OpenFDA API**
- URL: `https://api.fda.gov/drug/label.json`
- Rate limit: 240 req/min
- No API key required
- Returns black box warnings, contraindications

## Troubleshooting

**"Network restriction" error**
→ Run in environment with unrestricted internet access

**Timeout errors**
→ Script has 10-second timeout; retry or check network

**Missing `requests` library**
→ `pip install requests`

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│  Plan JSON Files (120+)                                     │
│  └── medications referenced inline                          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  validate_medication.py                                     │
│  └── RxNorm API → confirms drug exists, gets RxCUI          │
│  └── OpenFDA API → cross-checks black box warnings          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  medications.json (Central Database)                        │
│  └── Validated medications with:                            │
│      - RxCUI (provenance)                                   │
│      - Indication-specific dosing                           │
│      - Safety data (black box, renal adjustment)            │
│      - Drug interactions                                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  medication_resolver.py                                     │
│  └── Plans reference central DB                             │
│  └── Updates propagate automatically                        │
│  └── User customizations supported                          │
└─────────────────────────────────────────────────────────────┘
```

## Success Criteria

After running validation:
- [ ] All 11 central DB medications show as VALID
- [ ] Validation reports saved to `docs/data/`
- [ ] Cache file created (speeds up future runs)
- [ ] Invalid medications categorized for follow-up

---

*This handoff was prepared for local execution with internet access.*
