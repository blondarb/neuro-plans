# Sync System Handoff — February 6, 2026

**Commit:** `426ec58`
**Branch:** `main`

---

## What Changed

Two updates were pushed in this commit. Only one affects the data layer.

### 1. Visual Refresh (No Data Impact)

The site palette changed from indigo to teal across CSS, the MkDocs theme, and the Clinical Plan Builder UI. **Zero changes to any JSON files or schemas.** The sync system does not need to do anything for this.

### 2. Medication Database Expansion (Data Impact)

`docs/data/medications.json` was expanded from **11 medications to 936 medications**. All medication data was harvested from the existing 124 approved plans.

---

## Data File Status

| File | Changed? | Schema Change? | Sync Action |
|------|----------|----------------|-------------|
| `docs/data/plans.json` | **No** | No | None. Same 124 plans, same schema, same keys. |
| `docs/data/medications.json` | **Yes** | Yes (additive only) | See details below. |

---

## plans.json — No Changes

- 124 plans, same structure, same IDs
- Schema unchanged: `{ "plan-id": { id, title, version, icd10, scope, notes, sections, differential, evidence, monitoring, disposition } }`
- `notes` is still an array; `sections` is still an object
- No new plans added, no plans removed, no field changes

**If your sync only consumes plans.json, you are done. No action needed.**

---

## medications.json — What Changed

### Size Change
- **Before:** ~1,000 lines, 11 medications
- **After:** ~109,000 lines, 936 medications

### Top-Level Structure (Unchanged)
```json
{
  "_metadata": {
    "version": "2.0.0",
    "lastUpdated": "2026-02-06",
    "description": "...",
    "safetyNotice": "...",
    "schema": { ... }
  },
  "medications": {
    "gabapentin": { ... },
    "levetiracetam": { ... }
  }
}
```

### New Fields (Additive — Won't Break Existing Parsers)

**1. `settings` object on each context:**
```json
"contexts": {
  "neuropathic-pain": {
    "indication": "Neuropathic pain",
    "doseOptions": [...],
    "startingDose": "300 mg QHS",
    "maxDose": "3600 mg/day",
    "titration": "Increase by 300 mg every 1-3 days",
    "notes": "First-line for neuropathic pain",
    "settings": {              // <-- NEW FIELD
      "ED": "-",               // STAT | URGENT | ROUTINE | -
      "HOSP": "ROUTINE",
      "OPD": "ROUTINE",
      "ICU": "ROUTINE"
    }
  }
}
```

Values for `ED`, `HOSP`, `OPD`, `ICU`: `"STAT"`, `"URGENT"`, `"ROUTINE"`, or `"-"` (not applicable).

**2. `_sourcePlans` array on each context:**
```json
"_sourcePlans": ["diabetic-neuropathy", "small-fiber-neuropathy"]
```
Lists which plan IDs contributed this context. Useful for traceability.

**3. Medication-level metadata (on harvested entries only):**
```json
{
  "id": "riluzole",
  "name": "Riluzole",
  ...
  "_harvested": true,       // <-- NEW: this entry was auto-extracted from plans
  "_sourceCount": 3,        // <-- NEW: number of plans referencing this med
  "_sourcePlans": ["als", "alzheimers-disease", "frontotemporal-dementia"]  // <-- NEW
}
```

### Two Types of Entries

| Type | Count | How to Identify | Data Completeness |
|------|-------|-----------------|-------------------|
| **Validated** (original) | 11 | `_harvested` is absent or false | Full: genericName, brandNames, drugClass, mechanisms, formulations, safety (including blackBoxWarnings, drugInteractions), renalAdjustment tiers, hepaticAdjustment, patientCounseling |
| **Harvested** (new) | 925 | `_harvested: true` | Partial: name, routes, contexts (with dosing and settings), contraindications, monitoring. Empty: genericName, brandNames, drugClass, mechanisms, blackBoxWarnings, drugInteractions, renalAdjustment, hepaticAdjustment, patientCounseling |

### Original 11 Validated Medications (Preserved)
These were NOT overwritten. New contexts from plans were merged in alongside their existing contexts:

1. gabapentin
2. pregabalin
3. levetiracetam
4. carbamazepine
5. phenytoin
6. valproic-acid
7. lamotrigine
8. topiramate
9. oxcarbazepine
10. lacosamide
11. brivaracetam

---

## Medication Entry Schema (Complete Reference)

```json
{
  "id": "gabapentin",
  "name": "Gabapentin",
  "genericName": "gabapentin",
  "brandNames": ["Neurontin", "Gralise", "Horizant"],
  "drugClass": "Gabapentinoid / Anticonvulsant",
  "mechanisms": ["Binds alpha-2-delta subunit of voltage-gated calcium channels"],
  "routes": ["PO"],
  "formulations": ["100 mg capsule", "300 mg capsule", "600 mg tablet"],

  "contexts": {
    "neuropathic-pain": {
      "indication": "Neuropathic pain (diabetic neuropathy, post-herpetic neuralgia)",
      "doseOptions": [
        { "text": "100 mg TID", "orderSentence": "Gabapentin 100 mg PO TID" },
        { "text": "300 mg TID", "orderSentence": "Gabapentin 300 mg PO TID" }
      ],
      "startingDose": "300 mg QHS or 100-300 mg TID",
      "maxDose": "3600 mg/day",
      "titration": "Increase by 300 mg every 1-3 days as tolerated",
      "notes": "First-line for neuropathic pain; full effect may take 2-4 weeks",
      "settings": { "ED": "-", "HOSP": "ROUTINE", "OPD": "ROUTINE", "ICU": "ROUTINE" },
      "_sourcePlans": ["diabetic-neuropathy", "small-fiber-neuropathy"]
    },
    "epilepsy": { ... },
    "migraine-prophylaxis": { ... }
  },

  "safety": {
    "blackBoxWarnings": [],
    "contraindications": ["Hypersensitivity to gabapentin"],
    "precautions": ["Renal impairment (dose adjustment required)"],
    "drugInteractions": [
      { "drug": "Morphine", "severity": "moderate", "effect": "Increased gabapentin levels" }
    ],
    "pregnancyCategory": "C",
    "lactation": "Enters breast milk; use caution"
  },

  "renalAdjustment": {
    "required": true,
    "tiers": [
      { "gfr": ">=60", "adjustment": "No adjustment needed" },
      { "gfr": "30-59", "adjustment": "200-700 mg/day" },
      { "gfr": "15-29", "adjustment": "100-300 mg/day" },
      { "gfr": "<15", "adjustment": "100-150 mg/day" },
      { "gfr": "HD", "adjustment": "125-350 mg post-dialysis" }
    ]
  },

  "hepaticAdjustment": {
    "required": false,
    "notes": "No hepatic adjustment needed (renally eliminated)"
  },

  "monitoring": {
    "baseline": ["Renal function (BMP/CMP)", "Seizure frequency baseline"],
    "ongoing": ["Sedation", "Dizziness", "Peripheral edema", "Renal function"],
    "frequency": "Renal function every 6-12 months"
  },

  "patientCounseling": [
    "Do not stop abruptly — taper over minimum 1 week",
    "May cause drowsiness — avoid driving until effects known"
  ],

  "_harvested": false,
  "_sourceCount": 8,
  "_sourcePlans": ["diabetic-neuropathy", "epilepsy-new-onset", "essential-tremor", ...]
}
```

---

## What's NOT Ready Yet

- **925 harvested entries are not API-validated.** They have dosing and settings from the plans but lack enrichment (brand names, drug class, black box warnings, drug interactions, renal/hepatic dosing).
- The `_harvested: true` flag lets you filter these out if you only want validated entries.
- Full API validation (RxNorm + OpenFDA) is available but hasn't been run on the expanded database yet.

---

## Summary for Sync System Implementation

1. **If you sync plans.json only** — no changes needed, schema and data are identical.
2. **If you sync medications.json** — handle the file being ~100x larger (936 entries). New fields (`settings`, `_harvested`, `_sourceCount`, `_sourcePlans`) are additive and can be ignored if not needed.
3. **If you want to distinguish validated vs harvested meds** — check `_harvested` field. Only 11 entries have full safety/pharmacology data.
4. **Medication IDs** are lowercase, hyphenated slugs (e.g., `gabapentin`, `valproic-acid`, `3-4-diaminopyridine`).
5. **Context IDs** are slugified indication strings (e.g., `neuropathic-pain`, `status-epilepticus`).
