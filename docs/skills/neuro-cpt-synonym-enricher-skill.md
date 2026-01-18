---
name: neuro-cpt-synonym-enricher
description: Enriches clinical decision support templates with verified CPT codes and clinical synonyms. Searches for appropriate billing codes for procedures/studies and adds alternative terminology to improve searchability and cross-system compatibility. Run as final content step after citation verification and before physician sign-off.
---

# Neuro CPT & Synonym Enricher

Add verified CPT/HCPCS codes and clinical synonyms to finalized clinical recommendation templates to support billing integration and terminology standardization.

## When to Use

Run this skill AFTER:
- Template validation (neuro-checker ≥90%)
- All revisions complete (neuro-rebuilder)
- Citation verification complete (neuro-citation-verifier)

Run BEFORE:
- Final physician sign-off
- IT system integration
- Clinical deployment

## Purpose

### CPT Codes
- Enable direct integration with EHR order sets
- Support accurate billing and documentation
- Reduce coding errors and claim denials
- Facilitate cost estimation for patients

### Synonyms
- Improve template searchability across systems
- Account for regional/institutional terminology variations
- Support voice recognition and natural language search
- Enable mapping to different EHR systems (Epic, Cerner, etc.)

## CPT Code Verification Process

### Step 1: Identify Codeable Items

Scan template sections for items requiring CPT/HCPCS codes:

| Section | Codeable Items |
|---------|---------------|
| 1. Labs | All laboratory tests |
| 2. Imaging/Studies | Imaging, EEG, EMG/NCS, LP, etc. |
| 3. Treatment | Infusion codes, injection codes, prolonged services |
| 4A. Referrals | E/M codes for consult types (reference only) |

**Do NOT code:**
- Oral medications (use NDC separately if needed)
- Patient instructions
- Lifestyle recommendations
- Disposition criteria

### Step 2: Search and Verify CPT Codes

For each codeable item:

**Search Strategy:**
```
Search 1: "[procedure name] CPT code 2025"
Search 2: "[procedure name] billing code"
Search 3: "[procedure name] CMS fee schedule"
```

**Verification Sources (in priority order):**
1. CMS Physician Fee Schedule (publicly available)
2. Specialty society coding guides (AAN, ACR, etc.)
3. Major payer LCD/NCD documents
4. Hospital coding references

**Important:** CPT codes are copyrighted by AMA. This skill identifies codes from publicly available CMS and payer sources.

### Step 3: Code Categories

| Category | Code Range | Examples |
|----------|------------|----------|
| E/M Services | 99202-99499 | Consults, hospital visits |
| Laboratory | 80000-89999 | CBC, CMP, drug levels |
| Radiology | 70000-79999 | CT, MRI, X-ray |
| Neurology-specific | 95700-95999 | EEG, EMG, NCS, evoked potentials |
| Medicine | 90000-99199 | Infusions, injections |
| Surgery | 10000-69999 | LP (62270), nerve blocks |

### Step 4: Document Modifiers When Relevant

| Modifier | Use |
|----------|-----|
| -26 | Professional component only |
| -TC | Technical component only |
| -59 | Distinct procedural service |
| -76 | Repeat procedure same physician |
| -77 | Repeat procedure different physician |
| -95 | Synchronous telemedicine service |

## Common Neurology CPT Codes Reference

### EEG Codes

| Code | Description | Notes |
|------|-------------|-------|
| 95816 | EEG, awake and drowsy | Routine outpatient |
| 95819 | EEG, awake and asleep | With sleep recording |
| 95822 | EEG, sleep only | Sleep-deprived |
| 95812 | EEG, extended monitoring 41-60 min | Longer recording |
| 95813 | EEG, extended monitoring >60 min | Each additional hour |
| 95700 | EEG, continuous monitoring setup | cEEG initiation |
| 95711 | EEG, continuous monitoring, unmonitored | Technical component |
| 95714-95716 | EEG, continuous monitoring with review | Per hour, various levels |
| 95957 | EEG, digital analysis | Quantitative EEG |

### EMG/NCS Codes

| Code | Description | Notes |
|------|-------------|-------|
| 95907-95913 | Nerve conduction studies | By number of studies (1-2 up to 13+) |
| 95885 | Needle EMG, limited | 1-2 extremities |
| 95886 | Needle EMG, complete | 3+ extremities or trunk |
| 95887 | Needle EMG, non-extremity | Cranial, paraspinal |
| 95872 | Needle EMG, single fiber | Jitter studies |
| 95937 | Neuromuscular junction testing | Repetitive stim |

### Lumbar Puncture

| Code | Description | Notes |
|------|-------------|-------|
| 62270 | Spinal puncture, lumbar, diagnostic | Standard diagnostic LP |
| 62272 | Spinal puncture, therapeutic | High volume, IIH |
| 62328 | Lumbar puncture with fluoroscopy | Fluoroscopic guidance |

### Infusion Codes

| Code | Description | Notes |
|------|-------------|-------|
| 96365 | IV infusion, initial hour | First hour of infusion |
| 96366 | IV infusion, additional hour | Each additional hour |
| 96367 | IV infusion, additional sequential | Different drug |
| 96374 | IV push, single | Bolus medications |
| 96375 | IV push, additional | Each additional push |
| J0585 | Injection, onabotulinumtoxinA | Per unit |
| J0587 | Injection, rimabotulinumtoxinB | Per 100 units |

### Imaging Codes

| Code | Description | Notes |
|------|-------------|-------|
| 70551 | MRI brain without contrast | |
| 70552 | MRI brain with contrast | |
| 70553 | MRI brain without and with contrast | Most common for neuro |
| 70554 | MRI brain functional (fMRI) | Pre-surgical mapping |
| 70450 | CT head without contrast | Acute stroke, hemorrhage |
| 70460 | CT head with contrast | |
| 70470 | CT head without and with contrast | |
| 70496 | CT angiography, head | CTA head |
| 70498 | CT angiography, neck | CTA neck |
| 70544 | MRA head without contrast | |
| 70545 | MRA head with contrast | |
| 70547 | MRA neck without contrast | |
| 72141 | MRI cervical spine without contrast | |
| 72156 | MRI cervical spine without and with | |
| 72146 | MRI thoracic spine without contrast | |
| 72157 | MRI thoracic spine without and with | |
| 72148 | MRI lumbar spine without contrast | |
| 72158 | MRI lumbar spine without and with | |

### Common Laboratory Codes

| Code | Description |
|------|-------------|
| 85025 | CBC with differential |
| 80053 | Comprehensive metabolic panel |
| 80048 | Basic metabolic panel |
| 84443 | TSH |
| 84439 | Free T4 |
| 82607 | Vitamin B12 |
| 82746 | Folate |
| 82565 | Creatinine |
| 84295 | Sodium |
| 82947 | Glucose |
| 83735 | Magnesium |
| 82310 | Calcium, total |
| 82330 | Calcium, ionized |
| 80195 | Phenytoin level |
| 80164 | Valproic acid level |
| 80156 | Carbamazepine level |
| 80185 | Phenobarbital level |
| 80177 | Levetiracetam level |
| 80176 | Lacosamide level |
| 82542 | Lamotrigine level |
| 82507 | Ammonia |
| 83516 | Oligoclonal bands |
| 86140 | C-reactive protein |
| 86200 | CCP antibodies |
| 86235 | Extractable nuclear antigen antibodies |
| 86255 | ANA |
| 83519 | Immunoassay, NMO/AQP4 antibody |
| 83519 | Immunoassay, MOG antibody |

## Synonym Collection Process

### Step 1: Identify Terms Needing Synonyms

Target terms for synonym expansion:
- Diagnosis name (template header)
- All lab tests
- All imaging studies
- All procedures
- Key medications (especially if multiple brand names)

### Step 2: Synonym Sources

Search for synonyms using:
1. SNOMED CT browser (browser.ihtsdotools.org)
2. ICD-10 index (related terms)
3. MeSH database (meshb.nlm.nih.gov)
4. RxNorm (for medications)
5. LOINC (for lab tests)
6. RadLex (for radiology)
7. Clinical experience/regional variations

### Step 3: Synonym Categories

| Category | Example Base Term | Synonyms |
|----------|------------------|----------|
| Abbreviations | Electroencephalogram | EEG, electroencephalography |
| Eponyms | Guillain-Barré syndrome | GBS, Landry's paralysis, AIDP |
| Lay terms | Seizure | Convulsion, fit, spell |
| Brand/Generic | Levetiracetam | Keppra, LEV |
| Regional variations | Lumbar puncture | LP, spinal tap |
| Historical terms | Multiple sclerosis | MS, disseminated sclerosis (historical) |
| ICD-10 descriptions | Epilepsy | Epileptic seizures, seizure disorder |

### Step 4: Verify Synonym Accuracy

For each synonym:
- Confirm it refers to the same clinical entity
- Note if synonym has slightly different scope (e.g., "AIDP" is a subtype of GBS)
- Flag deprecated terms with notation
- Include common misspellings for search purposes (marked as such)

## Output Format

```
CPT & SYNONYM ENRICHMENT REPORT
================================
TEMPLATE: [Diagnosis Name]
VERSION: [Version]
DATE ENRICHED: [Date]
ENRICHER: Claude (neuro-cpt-synonym-enricher v1.0)

---

## DIAGNOSIS SYNONYMS

**Primary Term:** [Diagnosis name from template]
**ICD-10:** [Code(s) from template]

| Synonym | Type | Source | Notes |
|---------|------|--------|-------|
| [synonym] | Abbreviation | Clinical | Common usage |
| [synonym] | Eponym | SNOMED CT | Historical |
| [synonym] | Lay term | Patient education | For handouts |
| [synonym] | ICD-10 description | CMS | Index term |

**SNOMED CT ID:** [If identified]
**MeSH Term:** [If identified]

---

## SECTION 1: LABORATORY CPT CODES

| Test | CPT Code(s) | Description | Verification Source |
|------|-------------|-------------|---------------------|
| CBC with differential | 85025 | Complete blood count | CMS Fee Schedule |
| Comprehensive metabolic panel | 80053 | CMP | CMS Fee Schedule |
| [Continue for all labs] | | | |

**Lab Panel Notes:**
- [Any relevant bundling or panel notes]

---

## SECTION 2: IMAGING & STUDIES CPT CODES

### Imaging

| Study | CPT Code(s) | Description | Modifiers | Verification Source |
|-------|-------------|-------------|-----------|---------------------|
| MRI brain w/ and w/o contrast | 70553 | MRI brain complete | -26 if read only | CMS Fee Schedule |
| CT head without contrast | 70450 | CT head non-contrast | -26 if read only | CMS Fee Schedule |

### Electrodiagnostics

| Study | CPT Code(s) | Description | Verification Source |
|-------|-------------|-------------|---------------------|
| Routine EEG | 95816 | Awake and drowsy | CMS Fee Schedule |
| Continuous EEG setup | 95700 | cEEG initiation | CMS Fee Schedule |

### Procedures

| Procedure | CPT Code(s) | Description | Verification Source |
|-----------|-------------|-------------|---------------------|
| Lumbar puncture, diagnostic | 62270 | Spinal puncture | CMS Fee Schedule |

---

## SECTION 3: TREATMENT CPT CODES

### Infusions

| Treatment | CPT Code(s) | Description | Units | Verification Source |
|-----------|-------------|-------------|-------|---------------------|
| IV methylprednisolone 1g | 96365 + 96366 | Initial hour + addl hour(s) | Time-based | CMS Fee Schedule |
| IVIG infusion | 96365 + 96366 | Initial hour + addl hour(s) | Time-based | CMS Fee Schedule |

### Injections

| Treatment | CPT Code(s) | Description | Verification Source |
|-----------|-------------|-------------|---------------------|
| [If applicable] | | | |

**Drug J-Codes (if applicable):**
| Drug | J-Code | Unit | Verification Source |
|------|--------|------|---------------------|
| Methylprednisolone sodium succinate | J2920 | Per 40 mg | CMS HCPCS |

---

## SECTION 4: REFERRAL E/M CODES (Reference)

*Note: Actual E/M code depends on complexity and documentation. These are typical ranges.*

| Referral Type | Typical Codes | Notes |
|---------------|---------------|-------|
| Neurology outpatient new | 99203-99205 | Level depends on complexity |
| Neurology outpatient established | 99212-99215 | Level depends on complexity |
| Inpatient consult | 99252-99255 | Initial inpatient consult |
| ED consult | 99281-99285 | ED E/M levels |

---

## TERMINOLOGY SYNONYMS BY SECTION

### Lab Test Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| CBC with differential | Complete blood count, blood count, hemogram |
| Comprehensive metabolic panel | CMP, chem-14, chemistry panel |
| Basic metabolic panel | BMP, chem-7, electrolytes |
| [Continue for all labs] | |

### Imaging Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| MRI brain | Brain MRI, cranial MRI, head MRI, magnetic resonance imaging of brain |
| CT head | Head CT, brain CT, cranial CT, computed tomography of head |
| [Continue for all imaging] | |

### Procedure Synonyms

| Standard Term | Synonyms |
|---------------|----------|
| Lumbar puncture | LP, spinal tap, CSF tap |
| Electroencephalogram | EEG, brain wave test |
| [Continue for all procedures] | |

### Medication Synonyms

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Levetiracetam | Keppra, Keppra XR, Spritam, Roweepra, Elepsia XR | LEV |
| Lacosamide | Vimpat | LCM |
| Lamotrigine | Lamictal, Lamictal XR, Lamictal ODT | LTG |
| Valproate | Depakote, Depakote ER, Depakene, Depacon | VPA, DVP |
| [Continue for all medications] | | |

---

## CODES NOT FOUND / REQUIRING VERIFICATION

| Item | Issue | Recommendation |
|------|-------|----------------|
| [Item] | [Could not verify code] | [Suggest manual verification] |

---

## INTEGRATION NOTES

### For EHR Order Set Development
- Lab panel codes can be grouped for order set efficiency
- Consider creating "Seizure workup" orderable with bundled labs
- Imaging protocols may need site-specific mapping

### For Billing Compliance
- Time-based codes (infusions) require start/stop documentation
- Modifier usage varies by payer; verify with billing department
- Some codes may require prior authorization

### For Searchability
- All synonyms should be indexed in order search
- Consider adding common misspellings to search index
- Brand names essential for medication reconciliation
```

## Workflow Integration

### Input
- Validated template (≥90% checker score)
- Citation-verified template

### Output
1. **Enrichment Report** - Full CPT codes and synonyms (above format)
2. **CPT Quick Reference Table** - Condensed code list for template appendix
3. **Synonym Index** - Machine-readable synonym list for EHR integration

### Post-Enrichment
1. Physician reviews CPT codes for appropriateness
2. Billing/coding team verifies against institutional preferences
3. IT team uses synonym list for search indexing
4. Template finalized for deployment

## File Naming Convention

| Output | Filename |
|--------|----------|
| Enrichment report | `[diagnosis]-cpt-synonym-report-[date].md` |
| CPT quick reference | `[diagnosis]-cpt-codes.md` |
| Synonym index | `[diagnosis]-synonyms.json` or `.csv` |

## Limitations

- CPT codes change annually; verify against current year
- Some codes are payer-specific; check LCD/NCDs
- Institutional preferences may vary
- Some newer tests may not have established CPT codes
- J-codes for drugs change frequently

## Change Log

**v1.0 (January 2026)**
- Initial version
- Comprehensive CPT code reference tables for neurology
- Synonym collection framework
- Output format designed for EHR integration
