# App Store Differentiation: Neuro Plans vs Cardio Plans

This document explains how Neuro Plans and Cardio Plans are meaningfully different apps that serve distinct medical specialties, not template duplicates.

---

## Identity & Branding

| Aspect | Neuro Plans | Cardio Plans |
|--------|------------|--------------|
| App Name | Neuro Plans | Cardio Plans |
| Icon | Brain (teal) | Heart (red) |
| Header SF Symbol | brain.head.profile | heart.text.square |
| Brand Color | Teal (#0D9488) | Red (#DC2626) |
| Bundle ID | com.neuroplans.app | com.cardioplans.app |

## Clinical Content (100% Different)

### Treatment Plans
- **Neuro Plans:** 40+ neurology protocols (stroke, seizures, meningitis, MS, Parkinson's, etc.)
- **Cardio Plans:** Cardiology protocols (STEMI, heart failure, AFib, PE, hypertension, etc.)

### Clinical Scales & Scoring Tools
- **Neuro Plans:** NIHSS, Glasgow Coma Scale, Modified Rankin Scale, ABCD2, HAS-BLED
- **Cardio Plans:** CHA2DS2-VASc, HEART Score, Wells Criteria, TIMI Risk, Duke Criteria

### Examination Guides
- **Neuro Plans:** Cranial nerve exam, motor exam, sensory exam, cerebellar testing, gait assessment
- **Cardio Plans:** Cardiac auscultation, JVP assessment, peripheral vascular exam, ECG interpretation

### Clinical Tools
- **Neuro Plans:** Penlight, OKN stripes, visual acuity chart, dermatome map
- **Cardio Plans:** ECG calipers, heart sound simulator, murmur atlas, stethoscope guide

## Quick Actions (Specialty Shortcuts)

- **Neuro Plans:** Stroke Alert, Status Epilepticus, Acute Meningitis
- **Cardio Plans:** STEMI Alert, Acute PE, AFib Management

## Paywall Features

Each app highlights its own specialty capabilities:
- **Neuro Plans:** "Complete neurology treatment protocols", "NIHSS, mRS, GCS, and more", "Step-by-step neurological exams"
- **Cardio Plans:** "Complete cardiology treatment protocols", "CHA2DS2-VASc, HEART, Wells, and more", "Cardiac examination guides"

## ICD-10 Code Coverage

- **Neuro Plans:** G-codes (nervous system), I60-I69 (cerebrovascular), R-codes (neurological symptoms)
- **Cardio Plans:** I-codes (circulatory system), I20-I25 (ischemic heart), I26-I28 (pulmonary)

## Shared Architecture (Different Content)

Both apps use the same SwiftUI framework and SpecialtyConfig pattern, but every piece of clinical content — plans, scales, exams, tools, categories — is unique to its specialty. The shared architecture reduces bugs and ensures consistent quality, similar to how Mayo Clinic publishes separate specialty reference apps built on a common platform.

## Target Users

- **Neuro Plans:** Neurologists, neurology residents, stroke team nurses, neurocritical care
- **Cardio Plans:** Cardiologists, cardiology residents, cardiac cath lab staff, heart failure teams

---

*This document is for App Review reference. Updated 2026-02-21.*
