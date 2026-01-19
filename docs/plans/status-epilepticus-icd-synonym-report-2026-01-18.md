# ICD-10 & SYNONYM ENRICHMENT REPORT

**TEMPLATE:** Status Epilepticus
**VERSION:** 1.3
**DATE ENRICHED:** January 18, 2026
**ENRICHER:** Claude (neuro-icd-synonym-enricher v2.0)

---

## DIAGNOSIS IDENTITY

**Primary Term:** Status Epilepticus
**SNOMED CT ID:** 230456005 (Status epilepticus)
**MeSH Term:** Status Epilepticus (D013226)

---

## ICD-10-CM CODES

### Primary Codes (Most Specific)

| Code | Description | Use When |
|------|-------------|----------|
| G40.901 | Epilepsy, unspecified, not intractable, with status epilepticus | First presentation of SE in patient without known intractable epilepsy |
| G40.911 | Epilepsy, unspecified, intractable, with status epilepticus | SE in patient with known intractable/refractory epilepsy |
| G41.0 | Grand mal status epilepticus | Generalized tonic-clonic SE (convulsive SE) |
| G41.1 | Petit mal status epilepticus | Absence status epilepticus |
| G41.2 | Complex partial status epilepticus | Focal SE with impaired awareness |
| G41.8 | Other status epilepticus | NCSE, simple partial SE, other subtypes |
| G41.9 | Status epilepticus, unspecified | SE type not specified |

### Related Codes (May Apply)

| Code | Description | Use When |
|------|-------------|----------|
| G40.301 | Generalized idiopathic epilepsy, not intractable, with SE | Known generalized epilepsy patient in SE |
| G40.311 | Generalized idiopathic epilepsy, intractable, with SE | Known intractable generalized epilepsy in SE |
| G40.401 | Other generalized epilepsy, not intractable, with SE | Other generalized epilepsy type in SE |
| G40.411 | Other generalized epilepsy, intractable, with SE | Intractable other generalized in SE |
| G40.501 | Epileptic seizures related to external causes, with SE | SE triggered by external cause (drugs, toxins) |
| G40.801 | Other epilepsy, not intractable, with SE | Specific epilepsy syndrome in SE |
| G40.811 | Other epilepsy, intractable, with SE | Intractable specific syndrome in SE |
| R56.9 | Unspecified convulsions | Pre-diagnosis, before SE confirmed |
| G93.1 | Anoxic brain damage | Complication of prolonged SE |
| G93.40 | Encephalopathy, unspecified | Post-SE encephalopathy |

### Etiology Codes (Code Additionally When Applicable)

| Code | Description | Use When |
|------|-------------|----------|
| G04.90 | Encephalitis, unspecified | SE from encephalitis (NORSE workup) |
| G04.81 | Other encephalitis and encephalomyelitis | Autoimmune encephalitis causing SE |
| F10.231 | Alcohol dependence with withdrawal with perceptual disturbance | Alcohol withdrawal SE |
| T43.205A | Poisoning by antidepressants, accidental, initial | Drug-induced SE |
| E11.649 | Type 2 DM with hypoglycemia without coma | Hypoglycemia precipitating SE |
| I63.9 | Cerebral infarction, unspecified | Stroke-related SE |
| C71.9 | Malignant neoplasm of brain, unspecified | Tumor-related SE |

### Code Selection Guide

**For new presentation:**
- Use G40.901 (not intractable, with SE) for first-time SE
- Use G41.0/G41.1/G41.2 if seizure type is clearly identified

**For known epilepsy patients:**
- Use the specific epilepsy code with SE modifier (5th character "1")
- Use "intractable" codes (G40.x11) if patient has drug-resistant epilepsy

**For NORSE/FIRES:**
- Primary: G41.8 (Other status epilepticus)
- Add: G04.81 if autoimmune encephalitis confirmed

---

## SEARCH TERMS & SYNONYMS

### Clinical Abbreviations

| Term | Expansion | Notes |
|------|-----------|-------|
| SE | Status epilepticus | Universal abbreviation |
| CSE | Convulsive status epilepticus | Generalized tonic-clonic SE |
| NCSE | Non-convulsive status epilepticus | Subtle/electrographic SE |
| RSE | Refractory status epilepticus | Failed 2 treatment lines |
| SRSE | Super-refractory status epilepticus | >24h on anesthetics |
| GCSE | Generalized convulsive status epilepticus | Same as CSE |
| CPSE | Complex partial status epilepticus | Focal SE with impaired awareness |
| NORSE | New onset refractory status epilepticus | No prior epilepsy, no clear cause |
| FIRES | Febrile infection-related epilepsy syndrome | NORSE subtype with preceding fever |
| EPC | Epilepsia partialis continua | Focal motor SE subtype |

### Alternative Names

| Synonym | Type | Scope | Notes |
|---------|------|-------|-------|
| Status epilepticus | Primary term | - | Standard clinical term |
| Epileptic status | Historical | Same | Older terminology |
| Epileptic state | Historical | Same | ICD terminology |
| Grand mal status | Historical | Subtype (CSE) | G41.0 descriptor |
| Petit mal status | Historical | Subtype (absence) | G41.1 descriptor |
| Absence status | Clinical | Subtype | Non-convulsive absence SE |
| Subtle status epilepticus | Clinical | Subtype | NCSE with minimal motor signs |
| Electrographic status epilepticus | Clinical | Subtype | NCSE detected only on EEG |
| Focal status epilepticus | Clinical | Subtype | Formerly "partial SE" |
| Generalized status epilepticus | Clinical | Subtype | Generalized seizure activity |
| Tonic-clonic status | Clinical | Subtype | Same as grand mal/CSE |
| Convulsive status | Clinical | Subtype | Same as CSE |
| Non-convulsive status | Clinical | Subtype | Same as NCSE |
| Treatment-resistant SE | Clinical | Severity (RSE) | Synonymous with RSE |
| Prolonged seizure | Lay/Clinical | Broader | >5 minutes |

### Lay Terms (Patient-Friendly)

| Term | Clinical Equivalent |
|------|---------------------|
| Prolonged seizure | Status epilepticus |
| Continuous seizure | Status epilepticus |
| Seizure that won't stop | Status epilepticus |
| Long seizure | Status epilepticus |
| Nonstop seizure | Status epilepticus |
| Seizure emergency | Status epilepticus |
| Back-to-back seizures | Serial seizures / impending SE |
| Cluster seizures | Serial seizures / impending SE |

### Common Misspellings (For Search Index)

| Misspelling | Correct Term |
|-------------|--------------|
| status epileptus | status epilepticus |
| statis epilepticus | status epilepticus |
| status epelepticus | status epilepticus |
| status epileptics | status epilepticus |
| status epileptcus | status epilepticus |
| convulsive staus | convulsive status |
| refractory staus | refractory status |

---

## MEDICATION SYNONYMS

### Benzodiazepines (First-Line)

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Lorazepam | Ativan | LZP |
| Midazolam | Versed, Nayzilam (nasal) | MDZ |
| Diazepam | Valium, Diastat (rectal) | DZP |
| Clonazepam | Klonopin | CZP |

### Second-Line ASMs

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Levetiracetam | Keppra, Keppra XR, Spritam, Roweepra, Elepsia XR | LEV |
| Fosphenytoin | Cerebyx | fPHT, FOS |
| Phenytoin | Dilantin, Phenytek | PHT |
| Valproate/Valproic acid | Depakote, Depakote ER, Depakene, Depacon | VPA, DVP |
| Lacosamide | Vimpat | LCM |
| Brivaracetam | Briviact | BRV |
| Phenobarbital | Luminal | PB, PHB |

### Anesthetics (Third-Line)

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Propofol | Diprivan | - |
| Ketamine | Ketalar | - |
| Pentobarbital | Nembutal | PTB |
| Thiopental | Pentothal | - |

### Immunotherapy (NORSE/FIRES)

| Generic Name | Brand Names | Abbreviations |
|--------------|-------------|---------------|
| Methylprednisolone | Solu-Medrol | IVMP |
| IVIG | Privigen, Gammagard, Gamunex, Octagam | IVIg |
| Rituximab | Rituxan, Truxima, Ruxience | RTX |
| Cyclophosphamide | Cytoxan | CTX, CYC |
| Tocilizumab | Actemra | TCZ |
| Anakinra | Kineret | - |

---

## SEARCH INDEX ENTRY

**Recommended search index terms for this template:**

```json
{
  "primary_diagnosis": "Status Epilepticus",
  "icd10_codes": [
    "G40.901",
    "G40.911",
    "G41.0",
    "G41.1",
    "G41.2",
    "G41.8",
    "G41.9",
    "G40.301",
    "G40.311",
    "G40.401",
    "G40.411"
  ],
  "snomed_ct": "230456005",
  "mesh_id": "D013226",
  "search_terms": [
    "status epilepticus",
    "convulsive status epilepticus",
    "non-convulsive status epilepticus",
    "refractory status epilepticus",
    "super-refractory status epilepticus",
    "NORSE",
    "FIRES",
    "grand mal status",
    "absence status",
    "focal status epilepticus",
    "prolonged seizure",
    "continuous seizure",
    "epileptic status",
    "treatment-resistant seizure"
  ],
  "abbreviations": [
    "SE",
    "CSE",
    "NCSE",
    "RSE",
    "SRSE",
    "GCSE",
    "CPSE",
    "NORSE",
    "FIRES",
    "EPC"
  ],
  "medications": [
    "lorazepam",
    "ativan",
    "midazolam",
    "versed",
    "diazepam",
    "valium",
    "levetiracetam",
    "keppra",
    "fosphenytoin",
    "cerebyx",
    "phenytoin",
    "dilantin",
    "valproate",
    "depakote",
    "lacosamide",
    "vimpat",
    "propofol",
    "ketamine",
    "methylprednisolone",
    "IVIG"
  ],
  "settings": ["ED", "HOSP", "ICU"],
  "tags": ["seizure", "epilepsy", "emergency", "neurocritical-care"]
}
```

---

## INTEGRATION NOTES

### For EHR Problem List Mapping
- Primary mapping: G41.0 (Grand mal status) for convulsive SE
- For NCSE: G41.8 (Other status epilepticus)
- Add etiology codes as secondary diagnoses when identified
- Consider adding "resolved" status after SE termination

### For Search Implementation
- Index all abbreviations as high-priority search terms
- Include medication names for users searching "keppra protocol" or "ativan dose"
- Weight exact matches (SE, status epilepticus) higher than partial matches
- Include misspellings with fuzzy matching

### For Template Metadata
Suggested YAML frontmatter updates:
```yaml
search_aliases:
  - SE
  - CSE
  - NCSE
  - RSE
  - SRSE
  - NORSE
  - FIRES
  - prolonged seizure
  - convulsive status
icd10_primary:
  - G40.901
  - G41.0
  - G41.8
icd10_related:
  - G40.911
  - G41.1
  - G41.2
  - G41.9
snomed_ct: "230456005"
```

---

*Report generated by neuro-icd-synonym-enricher skill v2.0*
