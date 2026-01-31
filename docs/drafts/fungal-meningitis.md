---
title: "Fungal Meningitis"
description: "Evidence-based clinical decision support for diagnosis, antifungal treatment, and monitoring of fungal meningitis"
version: "1.0"
setting: "ED, HOSP, OPD, ICU"
status: draft
tags:
  - cns-infection
  - meningitis
  - infectious-disease
---

<div class="draft-warning-banner">
  <div class="icon">⚠️</div>
  <div class="content">
    <div class="title">DRAFT - Pending Review</div>
    <div class="description">This plan requires physician review before clinical use.</div>
  </div>
</div>

# Fungal Meningitis

**VERSION:** 1.0
**CREATED:** January 30, 2026
**STATUS:** Draft - Pending Review

---

**DIAGNOSIS:** Fungal Meningitis

**ICD-10:** G02 (Meningitis in other infectious and parasitic diseases classified elsewhere), B45.1 (Cerebral cryptococcosis), B38.4 (Coccidioidomycosis meningitis), B39.4 (Histoplasmosis, unspecified — meningitis), B37.5 (Candidal meningitis), B46.1 (Rhinocerebral mucormycosis)

**SYNONYMS:** Fungal meningitis, cryptococcal meningitis, crypto meningitis, coccidioidal meningitis, Valley fever meningitis, Coccidioides meningitis, histoplasma meningitis, candidal meningitis, chronic meningitis, subacute meningitis, fungal CNS infection, AIDS meningitis, HIV meningitis, opportunistic meningitis, lymphocytic meningitis

**SCOPE:** Diagnosis, antifungal treatment, and monitoring of fungal meningitis in adults. Includes cryptococcal meningitis (most common in immunocompromised, especially HIV/AIDS with CD4 <100), coccidioidal meningitis (endemic in southwestern US), histoplasma meningitis (endemic in Ohio/Mississippi River valleys), and other fungal causes (Candida, Aspergillus, Mucorales). Covers induction, consolidation, and maintenance antifungal therapy phases; intracranial pressure management including serial therapeutic lumbar punctures; and immune reconstitution inflammatory syndrome (IRIS) management in HIV patients. Excludes bacterial meningitis (see Bacterial Meningitis template), viral meningitis, TB meningitis, and pediatric fungal meningitis.

---

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical cases | - = Not applicable to this setting

═══════════════════════════════════════════════════════════════
SECTION A: ACTION ITEMS
═══════════════════════════════════════════════════════════════

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| CBC with differential (CPT 85025) | Baseline; leukopenia in immunocompromised; pancytopenia from disseminated fungal infection; pre-treatment baseline for flucytosine (myelosuppressive) | Normal; document baseline for monitoring | STAT | STAT | ROUTINE | STAT |
| CMP (BMP + LFTs) (CPT 80053) | Renal function critical for amphotericin B dosing (nephrotoxic); hepatic function for azole dosing; electrolytes (hypokalemia and hypomagnesemia from amphotericin B) | Normal; baseline Cr, K, Mg, LFTs | STAT | STAT | ROUTINE | STAT |
| Magnesium (CPT 83735) | Amphotericin B causes renal magnesium wasting; must supplement aggressively | Normal (1.8-2.4 mg/dL) | STAT | STAT | ROUTINE | STAT |
| Phosphorus (CPT 84100) | Amphotericin B causes renal electrolyte wasting | Normal | STAT | STAT | - | STAT |
| Blood cultures x2 (different sites) (CPT 87040) | Fungemia detection; Cryptococcus can be cultured from blood in disseminated disease | No growth | STAT | STAT | - | STAT |
| Blood cultures — fungal (CPT 87103) | Fungal blood cultures have higher yield for Histoplasma and Candida; use lysis-centrifugation method (Isolator) if available | No growth | STAT | STAT | - | STAT |
| Serum cryptococcal antigen (CrAg) — lateral flow assay (CPT 87327) | Highly sensitive (>99%) and specific (>97%) for cryptococcal disease; positive in both serum and CSF; can quantify for treatment monitoring; serum CrAg positive in >99% of HIV-associated cryptococcal meningitis | Negative; if positive, report titer | STAT | STAT | ROUTINE | STAT |
| HIV 1/2 antigen/antibody (4th generation) (CPT 87389) | MANDATORY — cryptococcal meningitis is an AIDS-defining illness; CD4 count determines treatment approach and ART timing; all patients with fungal meningitis need HIV testing | Negative; if positive, obtain CD4 and viral load | STAT | STAT | ROUTINE | STAT |
| CD4 count and HIV viral load (if HIV positive) (CPT 86360+87536) | CD4 <100 cells/microL is highest risk for cryptococcal meningitis; guides ART initiation timing (delay 4-6 weeks in crypto to prevent IRIS) | CD4 >200 cells/microL | STAT | STAT | ROUTINE | STAT |
| Procalcitonin (CPT 84145) | Low procalcitonin helps exclude bacterial meningitis; typically low in fungal infection | Low (<0.5 ng/mL suggests non-bacterial) | STAT | STAT | - | STAT |
| CRP (CPT 86140) | Inflammatory marker; typically mildly elevated in fungal meningitis compared to bacterial | Mild elevation | STAT | STAT | ROUTINE | STAT |
| Lactate (serum) (CPT 83605) | Sepsis assessment; monitor hemodynamic status | <2 mmol/L | STAT | STAT | - | STAT |
| Coagulation panel (PT/INR, aPTT) (CPT 85610+85730) | Pre-LP coagulopathy assessment; DIC screen in sepsis | Normal | STAT | STAT | - | STAT |
| Blood glucose (paired with LP) (CPT 82947) | Required to calculate CSF:serum glucose ratio; low CSF glucose is hallmark of fungal meningitis | Paired with CSF glucose | STAT | STAT | - | STAT |
| Type and screen (CPT 86900) | Potential need for blood products; amphotericin B infusion reactions | On file | STAT | ROUTINE | - | STAT |

### 1B. Extended Workup (Second-line)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| 1,3-Beta-D-glucan (serum) (CPT 87449) | Panfungal biomarker; elevated in most invasive fungal infections EXCEPT Cryptococcus and Mucorales (which do not produce beta-D-glucan); sensitivity ~77% for invasive fungal disease | Negative (<60 pg/mL); elevated suggests non-Cryptococcus fungal infection | URGENT | ROUTINE | ROUTINE | URGENT |
| Galactomannan (serum) (CPT 87305) | Aspergillus-specific antigen; sensitivity higher in neutropenic patients; consider if immunocompromised with pulmonary and CNS disease | Negative (index <0.5) | - | ROUTINE | ROUTINE | URGENT |
| Coccidioides serology — IgM and IgG (EIA + immunodiffusion) (CPT 86635) | Coccidioidomycosis screening; complement fixation (CF) titer in CSF is diagnostic of coccidioidal meningitis; serum IgM positive early in infection | Negative; if positive, obtain complement fixation titer | URGENT | ROUTINE | ROUTINE | URGENT |
| Coccidioides complement fixation (CF) titer — serum (CPT 86635) | Quantitative titer correlates with disease severity; rising titers indicate active disease; declining titers suggest treatment response | Negative; if positive, titers >1:16 suggest disseminated disease | - | ROUTINE | ROUTINE | - |
| Histoplasma antigen (urine and serum) (CPT 87385) | Highly sensitive for disseminated histoplasmosis (>90% urine sensitivity in disseminated disease); less sensitive in meningitis alone (~50% in CSF) | Negative | URGENT | ROUTINE | ROUTINE | URGENT |
| Histoplasma antibody (complement fixation and immunodiffusion) | Antibody detection; may be negative in immunocompromised; seroconversion takes 2-6 weeks | Negative | - | ROUTINE | ROUTINE | - |
| Serum osmolality (CPT 83930) | SIADH assessment (common with CNS infections); monitor with amphotericin B | 280-295 mOsm/kg | URGENT | ROUTINE | - | URGENT |
| Urine osmolality and sodium | SIADH confirmation if hyponatremia present | Evaluate if hyponatremic | - | ROUTINE | - | ROUTINE |
| Quantitative immunoglobulins (IgG, IgA, IgM) (CPT 82784+82785+82787) | Identify underlying humoral immunodeficiency predisposing to fungal infections | Normal | - | ROUTINE | ROUTINE | - |
| T-cell subsets (CD4/CD8 ratio) (CPT 86360) | Cellular immunodeficiency assessment if HIV-negative; low CD4 from other causes (transplant, steroids, malignancy) increases risk | Normal | - | ROUTINE | ROUTINE | - |

### 1C. Rare/Specialized (Refractory or Atypical)

| Test | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|------|-----------|----------------|:--:|:----:|:---:|:---:|
| Metagenomic next-generation sequencing (mNGS) of CSF | Culture-negative chronic meningitis; identifies unexpected or rare fungal pathogens; high sensitivity for organisms that are difficult to culture | Pathogen identification | - | EXT | EXT | EXT |
| Aspergillus PCR (CSF) | Suspected CNS aspergillosis; more sensitive than culture; immunocompromised with pulmonary and CNS disease | Negative | - | EXT | - | EXT |
| Mucorales PCR or tissue biopsy | Rhinocerebral mucormycosis suspicion; diabetic ketoacidosis, neutropenia, iron overload | Negative | - | EXT | - | EXT |
| Blastomyces antigen (urine) (CPT 87385) | Blastomycosis in endemic areas (Great Lakes, Ohio/Mississippi River valleys); rare CNS involvement | Negative | - | EXT | EXT | - |
| RPR/VDRL (serum) (CPT 86592) | Neurosyphilis in chronic meningitis differential | Negative | - | ROUTINE | ROUTINE | - |
| QuantiFERON-TB Gold (CPT 86480) | TB meningitis in differential (subacute, basilar, immunocompromised); CSF profile similar to fungal | Negative | - | ROUTINE | ROUTINE | - |
| ACE level (serum) (CPT 82164) | Neurosarcoidosis in chronic meningitis differential | Normal | - | ROUTINE | ROUTINE | - |
| Toxoplasma IgG/IgM (CPT 86777+86778) | Toxoplasmosis in HIV/immunocompromised patients | Negative | - | ROUTINE | ROUTINE | - |
| Strongyloides antibody (CPT 86682) | Hyperinfection risk if immunosuppression planned; eosinophilic meningitis differential | Negative | - | ROUTINE | ROUTINE | - |

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT head without contrast (CPT 70450) | Immediate — before LP to exclude mass effect; obtain in all patients with altered mental status, focal deficits, papilledema, immunocompromised state | Hydrocephalus (common in cryptococcal meningitis); mass lesion (cryptococcoma, abscess); basilar meningeal enhancement is NOT seen on non-contrast CT | Pregnancy (relative) | STAT | STAT | - | STAT |
| MRI brain with and without contrast (CPT 70553) | Within 24-48h; STAT if focal deficits or altered consciousness | Leptomeningeal enhancement (especially basilar); cryptococcomas (gelatinous pseudocysts in basal ganglia/midbrain); dilated perivascular spaces (Virchow-Robin spaces); hydrocephalus; ring-enhancing lesions (Aspergillus abscess); basilar arachnoiditis (Coccidioides, Histoplasma) | Pacemaker; metallic implants | STAT | STAT | ROUTINE | STAT |
| Chest X-ray (CPT 71046) | Within first hours | Pulmonary nodules, cavitary lesions, hilar lymphadenopathy (Histoplasma, Coccidioides); Aspergillus — halo sign; disseminated cryptococcal disease | None significant | URGENT | ROUTINE | ROUTINE | URGENT |

### 2B. Extended

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| CT chest (CPT 71260) | Within 48h if chest X-ray abnormal or pulmonary source suspected | Pulmonary cryptococcal nodules; coccidioidal cavitary disease; Aspergillus halo sign or air-crescent sign; hilar/mediastinal lymphadenopathy (Histoplasma) | Contrast allergy; renal impairment | - | ROUTINE | ROUTINE | ROUTINE |
| MRI spine with contrast (CPT 72156) | If spinal symptoms, radiculopathy, or myelopathy | Arachnoiditis (especially Coccidioides — involves spinal arachnoid); spinal cord compression; epidural abscess | Pacemaker; metallic implants | - | ROUTINE | ROUTINE | ROUTINE |
| CT sinuses (CPT 70486) | If rhinocerebral mucormycosis suspected; facial pain, periorbital swelling, black eschar in diabetic or neutropenic patient | Sinus opacification; bony erosion; orbital extension | None significant | URGENT | ROUTINE | - | URGENT |
| CT angiography head (CTA) (CPT 70496) | If vasculitis or vascular complications suspected (Aspergillus, Mucorales are angioinvasive) | Vessel irregularity; stenosis; aneurysm (mycotic); vascular occlusion | Contrast allergy; renal impairment | URGENT | ROUTINE | - | URGENT |
| MRA brain (CPT 70544) | Non-contrast alternative for vascular assessment | Vessel irregularity; stenosis; aneurysm (mycotic); vascular occlusion | Pacemaker; metallic implants | - | ROUTINE | ROUTINE | ROUTINE |
| Continuous EEG (CPT 95700) | If altered mental status out of proportion to imaging; suspected non-convulsive seizures | Seizure activity; non-convulsive status epilepticus; diffuse slowing | None significant | - | URGENT | - | STAT |

### 2C. Rare/Specialized

| Study | Timing | Target Finding | Contraindications | ED | HOSP | OPD | ICU |
|-------|--------|----------------|-------------------|:--:|:----:|:---:|:---:|
| Brain biopsy (stereotactic) | If diagnosis unclear despite full workup; ring-enhancing lesion of unknown etiology; suspected Aspergillus or Mucorales abscess | Fungal elements on histopathology (GMS and PAS staining); culture identification | Coagulopathy; inaccessible location; surgical risk | - | EXT | - | EXT |
| Nasal/sinus biopsy | Suspected rhinocerebral mucormycosis; tissue diagnosis essential for Mucorales | Broad non-septate hyphae with right-angle branching (mucormycosis); angioinvasion | Coagulopathy | - | URGENT | - | URGENT |
| CT myelogram (CPT 62284+72132) | Suspected arachnoiditis with spinal cord compromise; MRI contraindicated | Arachnoid adhesions; CSF flow obstruction; communicating hydrocephalus | Contrast allergy; coagulopathy | - | EXT | - | EXT |

### LUMBAR PUNCTURE

**Indication:** Diagnostic AND therapeutic — ALL patients with suspected fungal meningitis. LP is CRITICAL for diagnosis (CSF CrAg, fungal culture) AND for management of elevated intracranial pressure (serial therapeutic LPs in cryptococcal meningitis).

**Timing:** URGENT. Perform after CT head excludes mass effect. In cryptococcal meningitis, therapeutic LP on day 1 is essential if opening pressure is elevated.

**Volume Required:** 15-20 mL (diagnostic); 20-30 mL or more (therapeutic LP — drain until opening pressure <20 cm H2O or 50% reduction).

**Opening Pressure:** ALWAYS measure and document. Elevated ICP is the leading cause of death in cryptococcal meningitis.

| Study | Rationale | Target Finding | ED | HOSP | OPD | ICU |
|-------|-----------|----------------|:--:|:----:|:---:|:---:|
| Opening pressure (manometry) | Elevated ICP is common in cryptococcal meningitis (>60-70% have OP >20 cm H2O); elevated ICP is the primary driver of mortality; guides need for serial therapeutic LPs | Normal 10-20 cm H2O; cryptococcal meningitis often 25-50+ cm H2O; >25 cm H2O requires therapeutic drainage | STAT | STAT | ROUTINE | STAT |
| Cell count with differential (tubes 1 AND 4) (CPT 89051) | Lymphocytic pleocytosis typical of fungal meningitis; WBC count may be low in severe immunosuppression (HIV/AIDS) — paucicellular CSF with positive CrAg indicates poor prognosis | WBC 20-500 cells/microL, predominantly lymphocytes; may be <20 in severely immunocompromised | STAT | STAT | ROUTINE | STAT |
| Protein (CPT 84157) | Elevated in fungal meningitis (50-500 mg/dL); very high protein (>500) suggests basilar arachnoiditis (Coccidioides) or CSF block | Elevated (typically 50-200 mg/dL in Cryptococcus; higher in Coccidioides) | STAT | STAT | ROUTINE | STAT |
| Glucose with paired serum glucose (CPT 82945) | Low CSF glucose is hallmark of fungal meningitis; CSF:serum ratio <0.4 | Low (<40 mg/dL); CSF:serum ratio <0.5 (often <0.4) | STAT | STAT | ROUTINE | STAT |
| CSF cryptococcal antigen (CrAg) — lateral flow assay (CPT 87327) | GOLD STANDARD rapid diagnostic test for cryptococcal meningitis; sensitivity >98%, specificity >99% in CSF; quantitative titers correlate with fungal burden; serial titers monitor treatment response | Negative; if positive, report titer (high titers e.g. >1:1024 indicate high fungal burden and worse prognosis) | STAT | STAT | ROUTINE | STAT |
| India ink preparation (CPT 87205) | Classic rapid test showing encapsulated yeast; sensitivity only 50-70% (lower in non-HIV); largely replaced by CrAg but may be diagnostic if CrAg unavailable | Encapsulated yeast (budding yeast with clear halo); negative does NOT exclude diagnosis | STAT | ROUTINE | - | STAT |
| Fungal culture (CPT 87102) | Gold standard for organism identification (grows in 3-7 days for Cryptococcus, longer for others); required for speciation and antifungal susceptibility testing; positive in 75-90% of cryptococcal meningitis | No growth; if positive — speciation and susceptibility testing | STAT | STAT | ROUTINE | STAT |
| Gram stain (CPT 87205) | Exclude concurrent bacterial meningitis | No organisms | STAT | STAT | ROUTINE | STAT |
| Bacterial culture and sensitivity (CPT 87070) | Exclude concurrent bacterial meningitis, especially in immunocompromised | No growth | STAT | STAT | ROUTINE | STAT |
| BioFire FilmArray Meningitis/Encephalitis Panel (CPT 87483) | Rapid multiplex PCR (~1 hour); detects Cryptococcus neoformans/gattii plus 13 other pathogens; useful for rapid differentiation from bacterial and viral causes | Cryptococcus detected or negative; rules out concurrent bacterial/viral pathogens | STAT | STAT | - | STAT |
| CSF lactate (CPT 83605) | Elevated in bacterial (>3.5) but variable in fungal; helps distinguish from bacterial meningitis | Variable in fungal (often 2.5-4.0 mmol/L); elevated >3.5 more suggestive of bacterial | STAT | ROUTINE | - | STAT |
| Coccidioides complement fixation (CF) — CSF (CPT 86635) | Diagnostic of coccidioidal meningitis; CSF CF titer almost always positive in Coccidioides meningitis; declining CSF titers indicate treatment response | Negative; if positive, report titer (any positive CSF CF titer is diagnostic) | - | ROUTINE | ROUTINE | - |
| Histoplasma antigen — CSF (CPT 87385) | Moderate sensitivity (~50%) in Histoplasma meningitis; higher in disseminated disease | Negative | - | ROUTINE | ROUTINE | - |
| AFB smear and culture (CPT 87116) | TB meningitis has identical CSF profile; must exclude in any chronic lymphocytic meningitis, especially immunocompromised or endemic area | Negative | - | ROUTINE | ROUTINE | - |
| Cytology (CPT 88104) | Leptomeningeal carcinomatosis in chronic meningitis differential | Negative | - | ROUTINE | ROUTINE | - |
| VDRL — CSF (CPT 86592) | Neurosyphilis screen in chronic meningitis differential | Negative | - | ROUTINE | ROUTINE | - |
| HSV 1/2 PCR (CPT 87529) | Exclude HSV encephalitis if fever with altered mental status | Negative | STAT | ROUTINE | - | STAT |

**Special Handling:** Fungal cultures require prolonged incubation (up to 4-6 weeks for some organisms). Specify "fungal culture" on lab requisition — standard bacterial cultures will NOT grow most fungi. CrAg lateral flow assay provides results within minutes. India ink preparation must be examined immediately by experienced laboratory personnel.

**Contraindications to LP:** Mass lesion on CT with risk of herniation; severe coagulopathy (INR >1.5, platelets <50K — correct first); skin infection at LP site. In cryptococcal meningitis with elevated ICP, LP is THERAPEUTIC — do NOT avoid LP solely due to elevated opening pressure if no mass lesion on CT.

**THERAPEUTIC LP PROTOCOL (Cryptococcal Meningitis):**

- If opening pressure >25 cm H2O: drain CSF until pressure <20 cm H2O or 50% reduction, whichever is higher
- Remove up to 30 mL per session
- Repeat daily therapeutic LPs if opening pressure remains >25 cm H2O after initial drainage
- If persistent elevated ICP despite daily LPs for >1 week: consider lumbar drain or VP shunt
- Document opening and closing pressures at every LP

---

## 3. TREATMENT

### 3A. Acute/Emergent — Induction Therapy (Cryptococcal Meningitis)

**CRITICAL: Induction phase is 2 weeks minimum. Do NOT shorten. Amphotericin B + flucytosine is the gold standard.**

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Amphotericin B liposomal (AmBisome) | IV | First-line induction therapy for cryptococcal meningitis; fungicidal; liposomal formulation preferred over conventional due to reduced nephrotoxicity | 3-4 mg/kg/day :: IV :: daily :: 3-4 mg/kg IV daily for minimum 2 weeks (induction); infuse over 2 hours; premedicate with acetaminophen, diphenhydramine, and normal saline 500 mL before each dose to reduce infusion reactions and nephrotoxicity | Severe renal impairment (dose adjust or switch formulation); anaphylaxis to amphotericin; concurrent nephrotoxic agents (minimize) | Renal function (BMP daily); potassium and magnesium twice daily during induction; CBC twice weekly; LFTs weekly; infusion reaction monitoring | STAT | STAT | - | STAT |
| Amphotericin B conventional (deoxycholate) | IV | Alternative induction if liposomal formulation unavailable; higher nephrotoxicity but more widely available globally (WHO preferred in resource-limited settings) | 0.7-1.0 mg/kg/day :: IV :: daily :: 0.7-1.0 mg/kg IV daily for minimum 2 weeks; infuse over 4-6 hours; aggressive normal saline pre-hydration (1L before each dose) | Severe renal impairment; concomitant nephrotoxins | Renal function daily; potassium and magnesium twice daily; CBC twice weekly; rigors, fever during infusion | STAT | STAT | - | STAT |
| Flucytosine (5-FC, Ancobon) | PO | Combination with amphotericin B for induction; improves fungal clearance and reduces relapse; synergistic with amphotericin B | 25 mg/kg :: PO :: q6h :: 25 mg/kg PO q6h (100 mg/kg/day in 4 divided doses) for 2 weeks; adjust for renal function (GFR-based dosing); take with food to reduce GI side effects | Severe hepatic impairment; bone marrow suppression; pregnancy (teratogenic, Category C) | CBC with differential twice weekly (myelosuppression — leukopenia, thrombocytopenia); LFTs weekly; flucytosine drug levels if available (target peak 30-80 mcg/mL; toxic >100); renal function daily (adjust dose with declining GFR) | STAT | STAT | - | STAT |
| Fluconazole (high-dose induction alternative) | PO/IV | Alternative induction when amphotericin B or flucytosine unavailable (WHO alternative regimen); inferior to amphotericin-based regimens but used in resource-limited settings | 1200 mg :: PO/IV :: daily :: 1200 mg PO or IV daily for 2 weeks (induction); used with flucytosine if amphotericin B unavailable | Severe hepatic impairment; QT prolongation; concurrent QT-prolonging medications; pregnancy (teratogenic in first trimester at high doses) | LFTs weekly; QTc at baseline and weekly; drug interactions (CYP2C9, CYP3A4 inhibitor) | STAT | STAT | - | STAT |

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Normal saline pre-hydration | IV | Nephroprotection during amphotericin B therapy; prevents amphotericin-induced renal vasoconstriction | 500-1000 mL :: IV :: before each AmB dose :: 500-1000 mL IV normal saline infused before each amphotericin B dose | Volume overload; decompensated heart failure | I/O; weight; electrolytes; signs of volume overload | - | STAT | - | STAT |
| Potassium chloride supplementation | IV/PO | Amphotericin B causes renal potassium wasting in >80% of patients; severe hypokalemia can cause cardiac arrhythmias | 20-40 mEq :: IV/PO :: per replacement protocol :: Replace per institutional protocol; target K >3.5 mEq/L; oral preferred if tolerated; IV replacement for K <3.0 or symptomatic | Hyperkalemia; renal failure (use cautiously) | Potassium levels twice daily during induction; ECG if K <3.0 or >5.5 | - | STAT | - | STAT |
| Magnesium supplementation | IV/PO | Amphotericin B causes renal magnesium wasting; hypomagnesemia worsens hypokalemia (refractory hypokalemia until Mg corrected) | 2-4 g :: IV :: per replacement protocol :: Magnesium sulfate 2-4 g IV over 2-4 hours for Mg <1.5; oral magnesium oxide 400-800 mg daily for mild depletion | Renal failure (use cautiously); heart block | Magnesium levels daily during induction; renal function | - | STAT | - | STAT |
| Acetaminophen (amphotericin premedication) | PO/IV | Prevents infusion-related fever and rigors during amphotericin B administration | 650-1000 mg :: PO/IV :: before each AmB dose :: 650-1000 mg PO or IV 30-60 minutes before each amphotericin B infusion; max 4 g/day | Severe hepatic impairment | LFTs; hepatic function | - | ROUTINE | - | ROUTINE |
| Diphenhydramine (amphotericin premedication) | IV | Prevents infusion-related allergic reactions during amphotericin B | 25-50 mg :: IV :: before each AmB dose :: 25-50 mg IV 30-60 minutes before each amphotericin B infusion | Narrow-angle glaucoma; urinary retention | Sedation level | - | ROUTINE | - | ROUTINE |
| Meperidine | IV | Treatment of amphotericin B-related rigors unresponsive to acetaminophen premedication | 25-50 mg :: IV :: PRN rigors :: 25-50 mg IV PRN for rigors during amphotericin B infusion; avoid repeated dosing (normeperidine accumulation) | Seizure history (lowers threshold); MAOI use; renal failure (normeperidine accumulation) | Sedation; seizure risk; renal function | - | ROUTINE | - | ROUTINE |
| Acetazolamide | PO | Adjunctive ICP reduction in fungal meningitis with persistent mildly elevated ICP after therapeutic LPs; reduces CSF production | 250 mg :: PO :: BID-TID :: 250 mg PO BID-TID; titrate to 500 mg TID if tolerated; monitor for metabolic acidosis and paresthesias | Severe hepatic or renal impairment; sulfonamide allergy; hyponatremia; metabolic acidosis | BMP (bicarbonate, potassium); symptoms of metabolic acidosis; paresthesias | - | ROUTINE | ROUTINE | ROUTINE |
| Mannitol 20% | IV | Acute elevated ICP with signs of herniation (declining consciousness, pupil asymmetry); bridge to therapeutic LP or VP shunt | 1-1.5 g/kg :: IV :: bolus :: 1-1.5 g/kg IV bolus; then 0.25-0.5 g/kg q4-6h; maintain serum osmolality <320 mOsm/kg | Anuria; severe dehydration | Serum osmolality; osmolar gap; renal function; I/O | STAT | - | - | STAT |
| Levetiracetam | IV/PO | Seizure management if seizures occur; NOT routine prophylaxis; lower drug interaction profile than phenytoin (important with azoles) | 1000-1500 mg :: IV :: BID :: 1000-1500 mg IV or PO BID; load 1000-1500 mg if acute seizure; max 3000 mg/day | Severe renal impairment (dose adjust) | Renal function; mood and behavioral changes | STAT | STAT | ROUTINE | STAT |
| Ondansetron | IV/PO | Nausea and vomiting from elevated ICP, medications (flucytosine, azoles), or meningeal irritation | 4 mg :: IV :: q6h PRN :: 4 mg IV or PO q6h PRN nausea; max 16 mg/day | QT prolongation | QTc if concurrent QT-prolonging agents | STAT | ROUTINE | - | STAT |
| Dexamethasone | IV | IRIS management in HIV patients who develop worsening symptoms after ART initiation; NOT recommended as routine adjunct in cryptococcal meningitis (unlike bacterial meningitis — dexamethasone INCREASED mortality in cryptococcal meningitis per ACTA trial) | 0.3 mg/kg/day :: IV :: daily :: 0.3 mg/kg/day IV (or equivalent) for IRIS only; taper over 2-6 weeks based on clinical response; use ONLY for IRIS, NOT for routine cryptococcal meningitis | Active untreated infection; GI bleeding; uncontrolled diabetes | Glucose q6h; GI prophylaxis; BP; signs of infection progression | - | URGENT | - | URGENT |
| Pantoprazole | IV/PO | GI prophylaxis during steroid therapy for IRIS; stress ulcer prevention in ICU | 40 mg :: IV/PO :: daily :: 40 mg IV or PO daily | Prolonged use risks (C. difficile, hypomagnesemia) | GI symptoms | - | ROUTINE | - | ROUTINE |
| Enoxaparin | SC | DVT prophylaxis in hospitalized patients with prolonged immobility | 40 mg :: SC :: daily :: 40 mg SC daily; start when no active coagulopathy | Active bleeding; thrombocytopenia (<50K); coagulopathy | Platelets; coagulation studies | - | ROUTINE | - | ROUTINE |

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|
| Voriconazole | IV/PO | Aspergillus meningitis (first-line for CNS aspergillosis); second-line for resistant Cryptococcus; good CNS penetration | 6 mg/kg IV q12h x2 doses (load); 4 mg/kg IV q12h :: IV :: q12h :: Load: 6 mg/kg IV q12h for 2 doses; Maintenance: 4 mg/kg IV q12h (switch to PO 200-300 mg BID when stable); target trough 2-5.5 mcg/mL | Severe hepatic impairment; co-administration with sirolimus, rifampin, carbamazepine, phenobarbital; IV formulation contains cyclodextrin — avoid in renal impairment (GFR <50) | Trough levels (target 2-5.5 mcg/mL); LFTs weekly; visual disturbance assessment; dermatologic monitoring (photosensitivity, squamous cell carcinoma with prolonged use); drug interactions (CYP2C19, 2C9, 3A4) | - | STAT | ROUTINE | STAT |
| Isavuconazole (Cresemba) | IV/PO | Alternative to voriconazole for CNS aspergillosis; better tolerated; fewer drug interactions; does NOT require cyclodextrin (safe in renal impairment) | 200 mg :: IV/PO :: q8h x6 doses then daily :: Loading: 200 mg IV or PO q8h for 6 doses (48 hours); Maintenance: 200 mg IV or PO daily | Severe hepatic impairment; familial short QT syndrome; concurrent strong CYP3A4 inducers | LFTs weekly; hepatotoxicity monitoring; drug interactions (CYP3A4) | - | STAT | ROUTINE | STAT |
| Itraconazole | PO | Alternative for Histoplasma meningitis (after amphotericin B induction); second-line for Coccidioides meningitis; requires acidic gastric pH for absorption | 200 mg :: PO :: BID-TID :: 200 mg PO BID-TID (solution preferred over capsules for better absorption); target trough >1.0 mcg/mL; take solution on empty stomach, capsules with food | Severe hepatic impairment; ventricular dysfunction (negative inotrope); concurrent CYP3A4 substrates | Trough levels (target >1.0 mcg/mL); LFTs weekly initially then monthly; monitor for heart failure symptoms; drug interactions | - | ROUTINE | ROUTINE | - |
| Posaconazole | PO | Salvage therapy for refractory Aspergillus or Mucorales CNS infection; delayed-release tablets preferred | 300 mg :: PO :: BID x1d then daily :: Loading: 300 mg PO BID on day 1; Maintenance: 300 mg PO daily; delayed-release tablets preferred (consistent absorption) | Severe hepatic impairment; QT prolongation | Trough levels (target >1.0 mcg/mL for prophylaxis; >1.5 for treatment); LFTs; QTc; drug interactions | - | ROUTINE | ROUTINE | ROUTINE |
| Intrathecal amphotericin B | IT | Refractory coccidioidal meningitis not responding to systemic azoles; rarely used due to toxicity; specialist administration only | 0.01-0.5 mg :: IT :: 2-3x/week :: Start 0.01 mg IT; titrate slowly to 0.5 mg as tolerated over weeks; administered via LP or Ommaya reservoir; mix with CSF and inject slowly | Coagulopathy; infection at injection site | Chemical arachnoiditis symptoms (headache, nausea, radiculopathy); neurological exam after each dose; CSF analysis | - | EXT | EXT | EXT |
| VP shunt or lumbar drain | Surgical | Refractory elevated ICP despite daily therapeutic LPs for >1 week; progressive hydrocephalus; clinical deterioration from ICP | Neurosurgical placement; VP shunt with programmable valve preferred | Active ventriculitis (relative); coagulopathy (correct first) | Shunt function; ICP; imaging for shunt position; signs of shunt infection/malfunction | - | URGENT | - | URGENT |

### 3D. Disease-Modifying/Chronic Therapies — Consolidation and Maintenance

| Treatment | Route | Indication | Dosing | Pre-Treatment Requirements | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|---------------------------|-------------------|------------|:--:|:----:|:---:|:---:|
| Fluconazole (consolidation phase) | PO | Consolidation therapy after successful 2-week induction (Cryptococcus); transition from IV amphotericin B when CSF is sterilizing; 8 weeks consolidation | 400 mg :: PO :: daily :: 400 mg PO daily for 8 weeks (consolidation); begin after minimum 2-week induction and clinical improvement | Confirm negative or declining CSF fungal culture at end of induction; clinical improvement; able to take oral medication | Severe hepatic impairment; QT prolongation; pregnancy (teratogenic); concurrent QT-prolonging medications | LFTs at 2 weeks then monthly; QTc if risk factors; drug interactions (CYP2C9, CYP3A4 inhibitor); clinical response | - | STAT | ROUTINE | STAT |
| Fluconazole (maintenance/secondary prophylaxis) | PO | Long-term maintenance after consolidation (Cryptococcus); prevents relapse; continue until immune reconstitution (CD4 >100 for >3 months on ART with suppressed viral load) | 200 mg :: PO :: daily :: 200 mg PO daily; continue for minimum 1 year; in HIV patients, continue until CD4 >100 for >3 months with suppressed viral load; in non-HIV, continue for 6-12 months minimum | Completed consolidation phase; clinically stable | Severe hepatic impairment; QT prolongation; pregnancy | LFTs q3 months; CD4 count and viral load q3 months (HIV); clinical assessment for relapse symptoms | - | ROUTINE | ROUTINE | - |
| Fluconazole (coccidioidal meningitis — lifelong) | PO | LIFELONG therapy for coccidioidal meningitis; relapse rate near 80% if azole discontinued; never discontinue without ID specialist involvement | 400-800 mg :: PO :: daily :: 400 mg PO daily (standard); 800-1000 mg daily for refractory cases; LIFELONG treatment required — do NOT discontinue | Documented Coccidioides meningitis confirmed by CSF CF titer or culture | Severe hepatic impairment; pregnancy | LFTs q3 months; Coccidioides CF titers q3-6 months (declining indicates response); clinical assessment; bone density (long-term azole use) | - | ROUTINE | ROUTINE | - |
| Itraconazole (Histoplasma maintenance) | PO | Maintenance therapy after amphotericin B induction for Histoplasma meningitis; minimum 12 months; longer if immunosuppressed | 200 mg :: PO :: BID-TID :: 200 mg PO BID-TID for minimum 12 months; itraconazole solution preferred (better absorption); take on empty stomach | Completed amphotericin B induction (minimum 4-6 weeks for Histoplasma meningitis); clinical improvement | Ventricular dysfunction; severe hepatic impairment; concurrent CYP3A4 substrates | Itraconazole trough levels (target >1.0 mcg/mL); LFTs monthly; Histoplasma antigen q3 months (declining indicates response); cardiac function | - | ROUTINE | ROUTINE | - |
| Antiretroviral therapy (ART) — for HIV-associated fungal meningitis | PO | DELAYED initiation in cryptococcal meningitis; starting ART too early increases IRIS risk and mortality; initiate 4-6 weeks after antifungal induction therapy | Per HIV specialist :: PO :: daily :: Initiate ART 4-6 WEEKS after starting antifungal therapy (NOT immediately); per COAT trial — early ART (within 1-2 weeks) increased mortality compared to delayed ART (4-6 weeks) | Completed 2-week induction phase minimum; clinical stability; ICP controlled | Do NOT start within 2 weeks of antifungal initiation (IRIS risk) | CD4 count and viral load q3 months; IRIS symptoms (worsening headache, fever, meningismus, new focal deficits 2-8 weeks after ART initiation); LFTs; renal function | - | ROUTINE | ROUTINE | - |

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU |
|----------------|:--:|:----:|:---:|:---:|
| Infectious disease consultation for antifungal selection, treatment duration, and monitoring of drug levels and toxicity | STAT | STAT | ROUTINE | STAT |
| Neurology consultation for seizure management, elevated ICP assessment, and neurological monitoring | URGENT | URGENT | ROUTINE | STAT |
| Neurosurgery consultation for VP shunt placement if refractory elevated ICP despite serial therapeutic LPs, or hydrocephalus requiring external ventricular drain | - | URGENT | - | STAT |
| HIV/AIDS specialist referral for all HIV-positive patients for ART initiation timing (delayed 4-6 weeks), IRIS management, and long-term immunologic monitoring | - | STAT | ROUTINE | STAT |
| Critical care/ICU team for hemodynamic instability, respiratory failure, refractory elevated ICP, or rapidly declining neurological status | STAT | STAT | - | STAT |
| Ophthalmology consultation for fundoscopic examination to assess papilledema (indicates elevated ICP); also screen for ocular cryptococcosis and coccidioidal choroiditis | - | ROUTINE | ROUTINE | ROUTINE |
| Pharmacy consultation for amphotericin B dosing, flucytosine level monitoring, azole drug interaction management, and renal dosing adjustments | - | STAT | ROUTINE | STAT |
| Social work for discharge planning, medication access (antifungals are expensive), insurance assistance, and psychosocial support for prolonged treatment course | - | ROUTINE | ROUTINE | - |
| Physical therapy for mobilization assessment and deconditioning prevention during prolonged hospitalization | - | ROUTINE | ROUTINE | - |
| Palliative care for goals of care discussion in patients with severe disease, poor prognosis, or refractory infection | - | ROUTINE | - | ROUTINE |

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Return to ED immediately if worsening headache, new or worsening confusion, vision changes, fever recurrence, neck stiffness, or seizure (may indicate rising ICP, treatment failure, or IRIS) | STAT | STAT | ROUTINE |
| Do NOT stop antifungal medications without infectious disease physician guidance (premature discontinuation leads to relapse in >50% of cases) | - | ROUTINE | ROUTINE |
| Take fluconazole consistently at the same time each day to maintain therapeutic drug levels | - | ROUTINE | ROUTINE |
| Report any new medications to infectious disease physician before starting (azoles have extensive drug interactions including with statins, certain cardiac drugs, and anticoagulants) | - | ROUTINE | ROUTINE |
| Avoid grapefruit and grapefruit juice while taking azole antifungals (increases azole levels via CYP3A4 inhibition) | - | ROUTINE | ROUTINE |
| Coccidioidal meningitis requires LIFELONG antifungal therapy — never stop medication even if feeling well (relapse rate >80% if discontinued) | - | ROUTINE | ROUTINE |
| For HIV patients: take ART medications as prescribed without missing doses; report any worsening symptoms after starting ART (may indicate IRIS requiring treatment adjustment) | - | ROUTINE | ROUTINE |
| Attend all follow-up appointments including scheduled blood draws for drug level monitoring and liver function tests | - | ROUTINE | ROUTINE |
| Use sun protection (sunscreen, protective clothing) while on voriconazole due to increased photosensitivity and long-term skin cancer risk | - | ROUTINE | ROUTINE |

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
| Strict ART adherence for HIV-positive patients to achieve immune reconstitution and eventual discontinuation of fluconazole maintenance (CD4 >100 x 3 months with suppressed viral load) | - | ROUTINE | ROUTINE |
| Avoid soil disruption activities (digging, construction, archaeological excavation) in Coccidioides-endemic areas (southwestern US, Mexico, Central/South America) to reduce re-exposure risk | - | - | ROUTINE |
| Avoid bird/bat guano exposure, cave exploration, and demolition of old buildings in Histoplasma-endemic areas (Ohio/Mississippi River valleys) | - | - | ROUTINE |
| Alcohol cessation during antifungal therapy to reduce hepatotoxicity risk and improve immune function | - | ROUTINE | ROUTINE |
| Adequate hydration (2-3 L water daily if tolerated) to support renal function during and after amphotericin B therapy | - | ROUTINE | ROUTINE |
| Report any skin lesions, bone/joint pain, or pulmonary symptoms that may indicate disseminated fungal disease outside the CNS | - | ROUTINE | ROUTINE |
| Women of childbearing age must use effective contraception during azole therapy (teratogenic — especially fluconazole at high doses and itraconazole) | - | ROUTINE | ROUTINE |
| Smoking cessation to improve immune function and reduce pulmonary infection risk | - | ROUTINE | ROUTINE |

═══════════════════════════════════════════════════════════════
SECTION B: REFERENCE (Expand as Needed)
═══════════════════════════════════════════════════════════════

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
| Bacterial meningitis | Acute onset (hours to days); high fever; toxic appearance; CSF: high WBC (>1000) with neutrophilic predominance; CSF glucose very low; positive Gram stain | CSF cell count (neutrophils), Gram stain, bacterial culture, BioFire ME panel, procalcitonin (high), CSF lactate (>3.5) |
| Tuberculous (TB) meningitis | Subacute (weeks); basilar meningitis; cranial nerve palsies; CSF profile nearly identical to fungal (lymphocytic, low glucose, high protein); endemic exposure or HIV | AFB smear and culture, TB PCR (GeneXpert), CSF adenosine deaminase (ADA >10), chest X-ray (miliary), QuantiFERON-TB Gold, brain MRI (basilar enhancement) |
| Viral meningitis | Acute onset; less toxic appearance; CSF: lymphocytic pleocytosis but NORMAL glucose (unlike fungal); protein mildly elevated; self-limited | CSF glucose (normal in viral), BioFire ME panel (enterovirus, HSV-2), procalcitonin (low), CRP (mild) |
| HSV encephalitis | Acute; fever + confusion + seizures + focal deficits; temporal lobe predilection; encephalitis rather than meningitis | MRI (temporal T2/FLAIR), CSF HSV PCR, EEG (PLEDs from temporal region) |
| Neurosyphilis | Chronic meningitis; cranial neuropathies; pupillary abnormalities (Argyll Robertson); CSF: lymphocytic with elevated protein | Serum RPR/VDRL, CSF VDRL (specific but not sensitive), FTA-ABS, treponemal tests |
| Leptomeningeal carcinomatosis | Known malignancy; multiple cranial neuropathies; CSF: low glucose, elevated protein; positive cytology | CSF cytology (repeat x3 for sensitivity); MRI with contrast (leptomeningeal enhancement); flow cytometry |
| Neurosarcoidosis | Chronic headache; cranial neuropathies (CN VII); hilar lymphadenopathy; elevated ACE | Chest CT (hilar adenopathy); serum and CSF ACE; biopsy; PET-CT |
| Autoimmune/antibody-mediated encephalitis | Subacute; psychiatric symptoms; seizures; often young women; no fever initially | Autoimmune antibody panel (serum + CSF); MRI; EEG; tumor screening |
| Drug-induced aseptic meningitis | NSAID, IVIG, TMP-SMX exposure; self-limited after drug withdrawal | Drug history; CSF lymphocytic pleocytosis with sterile cultures; resolves with drug removal |
| Lymphocytic choriomeningitis virus (LCMV) | Rodent exposure; biphasic illness; meningitis with normal glucose | LCMV serology (IgM); rodent exposure history |
| CNS lymphoma | Immunocompromised; periventricular enhancing lesions; elevated CSF protein; positive cytology or flow cytometry | MRI (periventricular enhancement); CSF cytology; flow cytometry; brain biopsy |

## 6. MONITORING PARAMETERS

| Parameter | Frequency | Target/Threshold | Action if Abnormal | ED | HOSP | OPD | ICU |
|-----------|-----------|------------------|-------------------|:--:|:----:|:---:|:---:|
| Neurologic exam (GCS, mental status, cranial nerves) | q4h during induction; q8h during consolidation | Improving or stable mental status; no new deficits | If declining: STAT CT, repeat LP with opening pressure; reassess treatment | STAT | STAT | ROUTINE | STAT |
| Opening pressure (LP) | Daily therapeutic LP during induction if OP >25 cm H2O; then per clinical status | <20 cm H2O | If persistently elevated: continue daily LPs; if refractory >1 week, consult neurosurgery for VP shunt | STAT | STAT | ROUTINE | STAT |
| Serum creatinine | Daily during amphotericin B induction; weekly during consolidation | Cr <1.5x baseline | If rising: increase pre-hydration; hold amphotericin if Cr >2x baseline; switch formulation; consider alternative regimen | STAT | STAT | ROUTINE | STAT |
| Potassium | Twice daily during amphotericin B; daily during consolidation | >3.5 mEq/L | If low: aggressive IV/PO replacement; do NOT proceed with amphotericin until K >3.0 | STAT | STAT | ROUTINE | STAT |
| Magnesium | Daily during amphotericin B; weekly during consolidation | >1.8 mg/dL | If low: IV magnesium replacement; correct before treating hypokalemia (refractory K without Mg correction) | STAT | STAT | ROUTINE | STAT |
| CBC with differential | Twice weekly during flucytosine therapy; weekly during consolidation | WBC >3000; ANC >1500; platelets >100K | If cytopenias: check flucytosine level; hold if level >100 mcg/mL; consider dose reduction or discontinuation | - | STAT | ROUTINE | STAT |
| Flucytosine drug level (peak) | 3-5 days after initiation; after dose adjustments; after renal function changes | Peak 30-80 mcg/mL; toxic >100 mcg/mL | If >100: dose reduction or hold; recheck level; if <30: dose increase | - | ROUTINE | - | ROUTINE |
| LFTs (AST, ALT, bilirubin, alk phos) | Weekly during induction and consolidation; monthly during maintenance | <3x upper limit of normal | If >3x ULN: evaluate cause; consider dose reduction; if >5x ULN or symptomatic: hold azole and reassess | - | ROUTINE | ROUTINE | ROUTINE |
| Serum sodium | q6-8h during first 48h; then daily; q12h in ICU | 135-145 mEq/L | If <130: SIADH evaluation; fluid restriction (1-1.2 L/day); if <120: 3% saline per sodium correction protocol | STAT | STAT | ROUTINE | STAT |
| CSF fungal culture (repeat) | At 2 weeks (end of induction); if clinically indicated | Negative (sterile CSF) | If persistent positive culture: extend induction by 2 weeks; reassess regimen; consider salvage therapy | - | ROUTINE | ROUTINE | - |
| Serum CrAg titer (serial) | Baseline; at 2 weeks; at end of consolidation; q3 months during maintenance | Declining titer (ideally >4-fold decrease by 2 weeks) | If rising or stable titer: reassess adherence; repeat LP; consider treatment failure; extend induction | - | ROUTINE | ROUTINE | - |
| CSF CrAg titer (serial) | At baseline; repeat LP at 2 weeks (end of induction) | Declining titer | If not declining: extend induction; reassess therapy | - | ROUTINE | ROUTINE | - |
| CD4 count and HIV viral load | At baseline; then q3 months (HIV patients) | CD4 increasing; viral load undetectable on ART | If CD4 not recovering: assess ART adherence; optimize ART; cannot discontinue fluconazole maintenance until CD4 >100 x 3 months | - | ROUTINE | ROUTINE | - |
| IRIS surveillance (HIV patients) | Daily during first 2 weeks of ART; weekly for first 3 months | No new symptoms after ART initiation | If worsening headache, fever, meningismus, new focal deficits: evaluate for IRIS vs treatment failure; may require steroids (dexamethasone) and therapeutic LP | - | STAT | ROUTINE | STAT |
| Coccidioides CF titer — CSF (if applicable) | At baseline; q3-6 months during treatment | Declining titer | If rising: treatment failure; increase fluconazole dose or switch therapy; ID consultation | - | ROUTINE | ROUTINE | - |
| Temperature | q4h during induction; q8h during consolidation | Afebrile within 1-2 weeks of treatment | If persistent fever >2 weeks: reassess treatment; repeat cultures; imaging for complications | STAT | STAT | - | STAT |
| Azole drug level (voriconazole, itraconazole) | At 5-7 days after initiation; after dose changes; q1-3 months long-term | Voriconazole trough 2-5.5 mcg/mL; Itraconazole trough >1.0 mcg/mL | If subtherapeutic: increase dose; check adherence; check drug interactions; if supratherapeutic: reduce dose | - | ROUTINE | ROUTINE | - |

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | Completed induction (minimum 2 weeks); transitioned to oral consolidation (fluconazole); ICP controlled without need for daily LPs; neurologically stable; tolerating oral medications; reliable outpatient follow-up with ID and neurology; medication access confirmed; patient/family education on warning signs completed |
| Admit to floor (monitored) | Confirmed or suspected fungal meningitis requiring IV antifungal induction therapy; hemodynamically stable; GCS >=13; opening pressure manageable with intermittent (not daily) therapeutic LPs; no respiratory compromise |
| Admit to ICU | GCS <13 or rapidly declining consciousness; opening pressure >40 cm H2O refractory to therapeutic LP; need for EVD or ICP monitoring; respiratory failure requiring ventilatory support; septic shock; seizures (especially status epilepticus); severe electrolyte derangements from amphotericin B (refractory hypokalemia K <2.5); concurrent severe opportunistic infections in HIV/AIDS |
| Transfer to higher level | Need for neurosurgery (VP shunt, EVD) not available at current facility; need for ID specialist management of refractory fungal infection; need for neuro-ICU expertise for complex ICP management |
| Outpatient management (OPD) | Follow-up during consolidation and maintenance phases; serial CrAg titers q3 months; LFTs monthly then q3 months; CD4/viral load monitoring (HIV); medication adherence assessment; azole drug levels; coccidioidal meningitis patients require lifelong follow-up |

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
| Amphotericin B + flucytosine induction (2 weeks) as gold standard for cryptococcal meningitis | Class I, Level A | [Day et al. NEJM 2013 (ACTA trial)](https://pubmed.ncbi.nlm.nih.gov/23550668/); [Perfect et al. CID 2010 (IDSA Guidelines)](https://pubmed.ncbi.nlm.nih.gov/20047480/) |
| Liposomal amphotericin B preferred over conventional for reduced nephrotoxicity | Class I, Level A | [Hamill et al. CID 2010 (AMBITION-cm)](https://pubmed.ncbi.nlm.nih.gov/20047480/); [Molloy et al. NEJM 2018 (AMBITION)](https://pubmed.ncbi.nlm.nih.gov/29897851/) |
| Fluconazole 400 mg daily consolidation for 8 weeks, then 200 mg maintenance | Class I, Level A | [Perfect et al. CID 2010 (IDSA Guidelines)](https://pubmed.ncbi.nlm.nih.gov/20047480/) |
| Aggressive ICP management with serial therapeutic LPs reduces mortality in cryptococcal meningitis | Class I, Level B | [Graybill et al. CID 2000](https://pubmed.ncbi.nlm.nih.gov/10770714/); [Perfect et al. CID 2010](https://pubmed.ncbi.nlm.nih.gov/20047480/) |
| Delay ART by 4-6 weeks after antifungal initiation in HIV-associated cryptococcal meningitis to prevent IRIS | Class I, Level A | [Boulware et al. NEJM 2014 (COAT trial)](https://pubmed.ncbi.nlm.nih.gov/24524400/) |
| Dexamethasone NOT recommended as routine adjunct in cryptococcal meningitis (increased mortality in ACTA trial) | Class I, Level A | [Beardsley et al. NEJM 2016 (ACTA dexamethasone)](https://pubmed.ncbi.nlm.nih.gov/26962745/) |
| Serum and CSF CrAg (lateral flow assay) sensitivity >98% for cryptococcal meningitis | Class I, Level A | [Boulware et al. CID 2014](https://pubmed.ncbi.nlm.nih.gov/24803381/); [Rajasingham et al. Lancet Infect Dis 2017](https://pubmed.ncbi.nlm.nih.gov/28483415/) |
| Lifelong fluconazole for coccidioidal meningitis (>80% relapse rate if discontinued) | Class I, Level B | [Galgiani et al. CID 2016 (IDSA Coccidioidomycosis Guidelines)](https://pubmed.ncbi.nlm.nih.gov/27470238/) |
| Flucytosine drug level monitoring (peak 30-80 mcg/mL) to prevent myelosuppression | Class IIa, Level B | [Perfect et al. CID 2010](https://pubmed.ncbi.nlm.nih.gov/20047480/); Expert consensus |
| Voriconazole as first-line for CNS aspergillosis with trough monitoring (2-5.5 mcg/mL) | Class I, Level B | [Patterson et al. CID 2016 (IDSA Aspergillosis Guidelines)](https://pubmed.ncbi.nlm.nih.gov/27365388/) |
| WHO guidelines for cryptococcal meningitis management in resource-limited settings | Class I, Level A | [WHO Guidelines 2022](https://www.who.int/publications/i/item/9789240052178); [Loyse et al. Lancet Infect Dis 2013](https://pubmed.ncbi.nlm.nih.gov/23375891/) |
| BioFire ME panel for rapid pathogen identification in meningitis | Class IIa, Level B | [Leber et al. JCM 2016](https://pubmed.ncbi.nlm.nih.gov/27335149/) |
| Histoplasma antigen testing (urine) highly sensitive for disseminated disease | Class I, Level B | [Wheat et al. CID 2007](https://pubmed.ncbi.nlm.nih.gov/17682992/) |
| 1,3-Beta-D-glucan as panfungal biomarker (not elevated in Cryptococcus or Mucorales) | Class IIa, Level B | [Onishi et al. J Clin Microbiol 2012](https://pubmed.ncbi.nlm.nih.gov/22170934/) |
| Intrathecal amphotericin B for refractory coccidioidal meningitis | Class IIb, Level C | Expert consensus; [Johnson & Einstein. Ann Intern Med 2007](https://pubmed.ncbi.nlm.nih.gov/17227936/) |
| Immune reconstitution inflammatory syndrome (IRIS) management with corticosteroids | Class IIa, Level C | [Boulware et al. NEJM 2014](https://pubmed.ncbi.nlm.nih.gov/24524400/); Expert consensus |

---

## CHANGE LOG

**v1.0 (January 30, 2026)**
- Initial template creation
- Full 8-section clinical decision support for fungal meningitis
- Comprehensive coverage of cryptococcal, coccidioidal, histoplasma, and other fungal meningitis
- Induction/consolidation/maintenance treatment phases
- Therapeutic LP protocol for elevated ICP management
- IRIS management guidance
- Standardized treatment tables with structured dosing format

---

## APPENDIX A: CSF FINDINGS BY FUNGAL PATHOGEN

| Parameter | Cryptococcus | Coccidioides | Histoplasma | Aspergillus | Candida |
|-----------|-------------|-------------|-------------|-------------|---------|
| WBC (cells/microL) | 20-200 (may be <20 in AIDS) | 100-500 | 10-500 | Variable (often low) | 10-500 |
| Predominant cell | Lymphocytes (may be paucicellular in AIDS) | Lymphocytes + eosinophils (pathognomonic) | Lymphocytes | Neutrophils or mixed | Neutrophils or mixed |
| Protein (mg/dL) | 50-200 | 100-500+ | 50-300 | Elevated | 50-200 |
| Glucose (mg/dL) | <40 (very low in AIDS) | Very low (<20 common) | Low (<40) | Variable | Low |
| CSF:serum glucose | <0.5 | <0.3 | <0.4 | Variable | <0.5 |
| Opening pressure | Often >25 cm H2O (70% elevated) | Normal to mildly elevated | Normal to mildly elevated | Variable | Variable |
| Specific test | CrAg (>98% sensitive); India ink (50-70%) | CF titer (CSF >1:2 diagnostic) | Histoplasma antigen (~50% in CSF); culture | Galactomannan; culture (low yield) | Culture; beta-D-glucan |
| Culture growth time | 3-7 days | 1-3 weeks | 2-4 weeks | 1-2 weeks | 2-5 days |

## APPENDIX B: ANTIFUNGAL TREATMENT PHASES (Cryptococcal Meningitis)

| Phase | Duration | Regimen | Goal | Transition Criteria |
|-------|----------|---------|------|---------------------|
| Induction | Minimum 2 weeks | Amphotericin B (liposomal 3-4 mg/kg/day IV) + Flucytosine (25 mg/kg PO q6h) | Rapid fungicidal activity; sterilize CSF | Clinical improvement; declining CrAg titer; negative or declining CSF culture |
| Consolidation | 8 weeks | Fluconazole 400 mg PO daily | Maintain suppression; transition to oral therapy | Completed induction; clinical stability; tolerable oral medications |
| Maintenance (secondary prophylaxis) | Minimum 1 year (HIV: until immune reconstitution) | Fluconazole 200 mg PO daily | Prevent relapse | HIV: CD4 >100 for >3 months with suppressed viral load; Non-HIV: minimum 6-12 months and clinically stable |

## APPENDIX C: IRIS IN HIV-ASSOCIATED CRYPTOCOCCAL MENINGITIS

**Definition:** Immune reconstitution inflammatory syndrome (IRIS) — paradoxical worsening of meningitis symptoms after ART initiation due to immune system recovery triggering inflammatory response against fungal antigens.

**Timeline:** Typically 2-8 weeks after ART initiation.

**Risk Factors:**
- Low baseline CD4 count (<50 cells/microL)
- High baseline CSF fungal burden (CrAg titer >1:1024)
- Rapid CD4 recovery after ART initiation
- Early ART initiation (<2 weeks after antifungal therapy)

**Clinical Features:**
- Worsening headache
- Recurrent or worsening meningismus
- New or worsening cranial nerve palsies
- Rising ICP (elevated opening pressure)
- Fever recurrence
- New lymphadenopathy

**Management:**
1. Continue antifungal therapy and ART (do NOT stop either)
2. Rule out treatment failure (repeat LP with culture and CrAg)
3. If IRIS confirmed: dexamethasone 0.3 mg/kg/day, taper over 2-6 weeks
4. Serial therapeutic LPs for elevated ICP
5. ID and neurology co-management

**Prevention:**
- Delay ART by 4-6 weeks after antifungal induction (COAT trial evidence)
- Complete full induction course before ART initiation
- Monitor closely during first 3 months of ART
