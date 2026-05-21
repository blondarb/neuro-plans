# CLI Commands Reference

Always use `-X utf8` flag on Windows.

## JSON Generation & Validation

```bash
python -X utf8 scripts/generate_json.py docs/drafts/<plan>.md --validate-only
python -X utf8 scripts/generate_json.py docs/drafts/<plan>.md --merge
python -X utf8 scripts/generate_json.py docs/plans/<plan>.md --check-parity
```

## Citation Verification (requires internet for --verify)

```bash
python -X utf8 scripts/verify_citations.py docs/plans/<plan>.md --verify
python -X utf8 scripts/verify_citations.py docs/plans/<plan>.md --verify --repair --apply
```

## ICD-10 Code Validation

```bash
python -X utf8 scripts/validate_icd10.py docs/drafts/<plan>.md --lint
python -X utf8 scripts/validate_icd10.py docs/drafts/<plan>.md --verify
python -X utf8 scripts/validate_icd10.py --all --lint --quiet
python -X utf8 scripts/validate_icd10.py --all --verify --save-report docs/data/icd10-report.md
```

## Medication Validation (requires internet)

```bash
python3 scripts/validate_medication.py --validate-db
python3 scripts/validate_medication.py --batch-from-plans --save-report docs/data/full-validation-report.md
```

## Medication Harvest (expand central DB from plan data)

```bash
python -X utf8 scripts/harvest_medications.py --stats
python -X utf8 scripts/harvest_medications.py --preview
python -X utf8 scripts/harvest_medications.py --merge
```

## Treatment Row Generation (from central DB)

```bash
python -X utf8 scripts/generate_treatment_row.py <med-name> --header
python -X utf8 scripts/generate_treatment_row.py <med-name> --context <context-id>
python -X utf8 scripts/generate_treatment_row.py --indication "neuropathic pain"
```

## Guideline Freshness (monthly, requires internet)

```bash
python3 scripts/check_guideline_freshness.py --cache
python3 scripts/check_guideline_freshness.py --guidelines-only --cache --quiet
```
