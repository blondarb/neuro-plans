---
title: Review Queue
description: Plans awaiting validation and review
---

# Review Queue

Plans in this queue need to go through the skills pipeline (checker → rebuilder → JSON generation).

## Status Key

| Status | Meaning |
|--------|---------|
| `pending` | Awaiting review - available for a session to claim |
| `in_progress` | Currently being reviewed by a session |
| `completed` | Review complete, ready for physician sign-off |
| `approved` | Physician approved, moved to `docs/plans/` |

---

## Queue

### HIGH-VALUE GAPS (Tier 14A — drafts built, validation in progress)

| Plan | ICD-10 | File | Status | Session | Last Updated |
|------|--------|------|--------|---------|--------------|
| Lumbar Stenosis | M48.06 | `lumbar-stenosis.md` | `approved` | — | 2026-02-09 |
| Ulnar Neuropathy | G56.20 | `ulnar-neuropathy.md` | `approved` | — | 2026-02-09 |
| Chemotherapy-Induced Neuropathy | G62.0 | `chemotherapy-induced-neuropathy.md` | `approved` | — | 2026-02-09 |
| Parkinson's Disease - Motor Fluctuations | G20 | `parkinsons-motor-fluctuations.md` | `approved` | — | 2026-02-09 |
| Delirium vs Dementia | R41.0 | `delirium-vs-dementia.md` | `approved` | — | 2026-02-09 |

---

### SUBSPECIALTY GAPS (Tier 14B — drafts built, validation in progress)

| Plan | ICD-10 | File | Status | Session | Last Updated |
|------|--------|------|--------|---------|--------------|
| New Daily Persistent Headache | G44.52 | `new-daily-persistent-headache.md` | `approved` | — | 2026-02-09 |
| Horner Syndrome | G90.2 | `horner-syndrome.md` | `approved` | — | 2026-02-09 |
| Hypertensive Encephalopathy | I67.4 | `hypertensive-encephalopathy.md` | `approved` | — | 2026-02-09 |
| Parkinson's Disease - Psychosis | F06.0 | `parkinsons-psychosis.md` | `approved` | — | 2026-02-09 |
| Autoimmune Dementia/Encephalopathy | G04.81 | `autoimmune-dementia.md` | `approved` | — | 2026-02-09 |

---

### AUTONOMIC & PAIN EXPANSION (Tier 13 — approved)

| Plan | ICD-10 | File | Status | Session | Last Updated |
|------|--------|------|--------|---------|--------------|
| POTS (Postural Orthostatic Tachycardia Syndrome) | G90.A | `pots.md` | `approved` | — | 2026-02-09 |
| Neurogenic Orthostatic Hypotension | I95.1, G90.09 | `neurogenic-orthostatic-hypotension.md` | `approved` | — | 2026-02-09 |
| Occipital Neuralgia | M54.81 | `occipital-neuralgia.md` | `approved` | — | 2026-02-09 |
| Complex Regional Pain Syndrome (CRPS) | G90.50 | `crps.md` | `approved` | — | 2026-02-09 |
| Neuropathic Pain Management | G89.29, G89.4, G89.0 | `neuropathic-pain-management.md` | `approved` | — | 2026-02-09 |

---

### SLEEP MEDICINE EXPANSION (Tier 12 — approved)

| Plan | ICD-10 | File | Status | Session | Last Updated |
|------|--------|------|--------|---------|--------------|
| REM Sleep Behavior Disorder | G47.52 | `rem-sleep-behavior-disorder.md` | `approved` | — | 2026-02-07 |
| Obstructive Sleep Apnea — Neurological Evaluation | G47.33 | `obstructive-sleep-apnea-neuro.md` | `approved` | — | 2026-02-07 |
| Insomnia — Neurological Approach | G47.00, G47.01 | `insomnia-neurological.md` | `approved` | — | 2026-02-07 |
| Idiopathic Hypersomnia | G47.11 | `idiopathic-hypersomnia.md` | `approved` | — | 2026-02-07 |
| Non-REM Parasomnias | F51.3, F51.4, G47.50, G47.51 | `non-rem-parasomnias.md` | `approved` | — | 2026-02-07 |

---

### HIGH PRIORITY — Tier 11 (completed)

| Plan | ICD-10 | File | Status | Session | Last Updated |
|------|--------|------|--------|---------|--------------|
| *(empty — all Tier 11 plans approved)* | — | — | — | — | — |

---

## Approved (Moved to `docs/plans/`)

| # | Plan | File | Approved Date | Final Score |
|---|------|------|---------------|-------------|
| 1 | Acute Ischemic Stroke | [`acute-ischemic-stroke.md`](../plans/acute-ischemic-stroke.md) | 2026-01-21 | 92% (55/60) |
| 2 | Acute Myelopathy | [`acute-myelopathy.md`](../plans/acute-myelopathy.md) | 2026-01-27 | 90%+ |
| 3 | Autoimmune Encephalitis | [`autoimmune-encephalitis.md`](../plans/autoimmune-encephalitis.md) | 2026-01-26 | 90%+ |
| 4 | Bacterial Meningitis | [`bacterial-meningitis.md`](../plans/bacterial-meningitis.md) | 2026-01-26 | 90%+ |
| 5 | Bell's Palsy | [`bells-palsy.md`](../plans/bells-palsy.md) | 2026-01-27 | 90%+ |
| 6 | Brain Metastases | [`brain-metastases.md`](../plans/brain-metastases.md) | 2026-01-27 | 90%+ |
| 7 | Breakthrough Seizure | [`breakthrough-seizure.md`](../plans/breakthrough-seizure.md) | 2026-01-27 | 90%+ |
| 8 | Cauda Equina Syndrome | [`cauda-equina-syndrome.md`](../plans/cauda-equina-syndrome.md) | 2026-01-27 | 90%+ |
| 9 | CIDP | [`cidp.md`](../plans/cidp.md) | 2026-01-27 | 90%+ |
| 10 | Cluster Headache | [`cluster-headache.md`](../plans/cluster-headache.md) | 2026-01-27 | 90%+ |
| 11 | Dementia Evaluation | [`dementia-evaluation.md`](../plans/dementia-evaluation.md) | 2026-01-27 | 90%+ |
| 12 | Diabetic Neuropathy | [`diabetic-neuropathy.md`](../plans/diabetic-neuropathy.md) | 2026-01-27 | 90%+ |
| 13 | Elevated ICP Management | [`elevated-icp-management.md`](../plans/elevated-icp-management.md) | 2026-01-27 | 90%+ |
| 14 | Epidural Abscess | [`epidural-abscess.md`](../plans/epidural-abscess.md) | 2026-01-27 | 90%+ |
| 15 | Essential Tremor | [`essential-tremor.md`](../plans/essential-tremor.md) | 2026-01-27 | 90%+ |
| 16 | Guillain-Barr\u00e9 Syndrome | [`guillain-barre-syndrome.md`](../plans/guillain-barre-syndrome.md) | 2026-01-26 | 90%+ |
| 17 | HSV Encephalitis | [`hsv-encephalitis.md`](../plans/hsv-encephalitis.md) | 2026-01-26 | 90%+ |
| 18 | Idiopathic Intracranial Hypertension | [`idiopathic-intracranial-hypertension.md`](../plans/idiopathic-intracranial-hypertension.md) | 2026-01-27 | 90%+ |
| 19 | Intracerebral Hemorrhage | [`intracerebral-hemorrhage.md`](../plans/intracerebral-hemorrhage.md) | 2026-01-27 | 90%+ |
| 20 | Medication Overuse Headache | [`medication-overuse-headache.md`](../plans/medication-overuse-headache.md) | 2026-01-27 | 90%+ |
| 21 | Migraine | [`migraine.md`](../plans/migraine.md) | 2026-01-27 | 90%+ |
| 22 | MS - Chronic Management | [`ms-chronic-management.md`](../plans/ms-chronic-management.md) | 2026-01-27 | 90%+ |
| 23 | MS - New Diagnosis | [`ms-new-diagnosis.md`](../plans/ms-new-diagnosis.md) | 2026-01-20 | 90% (54/60) |
| 24 | Myasthenia Gravis - Crisis | [`myasthenia-gravis-crisis.md`](../plans/myasthenia-gravis-crisis.md) | 2026-01-26 | 90%+ |
| 25 | Myasthenia Gravis - New Diagnosis | [`myasthenia-gravis-new-diagnosis.md`](../plans/myasthenia-gravis-new-diagnosis.md) | 2026-01-27 | 90%+ |
| 26 | Neuromuscular Respiratory Failure | [`neuromuscular-respiratory-failure.md`](../plans/neuromuscular-respiratory-failure.md) | 2026-01-27 | 90%+ |
| 27 | New Onset Seizure | [`new-onset-seizure.md`](../plans/new-onset-seizure.md) | 2026-01-20 | 93% (56/60) |
| 28 | Parkinson's Disease | [`parkinsons-disease.md`](../plans/parkinsons-disease.md) | 2026-01-27 | 90%+ |
| 29 | Parkinson's Disease - New Diagnosis | [`parkinsons-disease-new-diagnosis.md`](../plans/parkinsons-disease-new-diagnosis.md) | 2026-01-29 | 90%+ |
| 30 | Peripheral Neuropathy | [`peripheral-neuropathy.md`](../plans/peripheral-neuropathy.md) | 2026-01-20 | 90% (54/60) |
| 31 | Rapidly Progressive Dementia | [`rapidly-progressive-dementia.md`](../plans/rapidly-progressive-dementia.md) | 2026-01-27 | 90%+ |
| 32 | Restless Legs Syndrome | [`restless-legs-syndrome.md`](../plans/restless-legs-syndrome.md) | 2026-01-27 | 90%+ |
| 33 | Spinal Cord Compression (Malignant) | [`spinal-cord-compression-malignant.md`](../plans/spinal-cord-compression-malignant.md) | 2026-01-27 | 90%+ |
| 34 | Status Epilepticus | [`status-epilepticus.md`](../plans/status-epilepticus.md) | 2026-01-27 | 90%+ |
| 35 | Subarachnoid Hemorrhage | [`subarachnoid-hemorrhage.md`](../plans/subarachnoid-hemorrhage.md) | 2026-01-27 | 90%+ |
| 36 | Syncope | [`syncope.md`](../plans/syncope.md) | 2026-01-27 | 90%+ |
| 37 | Transient Ischemic Attack | [`transient-ischemic-attack.md`](../plans/transient-ischemic-attack.md) | 2026-01-27 | 90%+ |
| 38 | Trigeminal Neuralgia | [`trigeminal-neuralgia.md`](../plans/trigeminal-neuralgia.md) | 2026-01-27 | 90%+ |
| 39 | Vertigo/Dizziness Evaluation | [`vertigo-dizziness-evaluation.md`](../plans/vertigo-dizziness-evaluation.md) | 2026-01-27 | 90%+ |
| 40 | Wernicke Encephalopathy | [`wernicke-encephalopathy.md`](../plans/wernicke-encephalopathy.md) | 2026-01-27 | 90%+ |
| 41 | ALS | [`als.md`](../plans/als.md) | 2026-01-30 | 90%+ |
| 42 | Alzheimer's Disease | [`alzheimers-disease.md`](../plans/alzheimers-disease.md) | 2026-01-30 | 90%+ |
| 43 | Carpal Tunnel Syndrome | [`carpal-tunnel-syndrome.md`](../plans/carpal-tunnel-syndrome.md) | 2026-01-30 | 90%+ |
| 44 | Dystonia | [`dystonia.md`](../plans/dystonia.md) | 2026-01-30 | 90%+ |
| 45 | Frontotemporal Dementia | [`frontotemporal-dementia.md`](../plans/frontotemporal-dementia.md) | 2026-01-30 | 90%+ |
| 46 | Huntington's Disease | [`huntingtons-disease.md`](../plans/huntingtons-disease.md) | 2026-01-30 | 90%+ |
| 47 | Lewy Body Dementia | [`lewy-body-dementia.md`](../plans/lewy-body-dementia.md) | 2026-01-30 | 90%+ |
| 48 | Migraine with Aura | [`migraine-with-aura.md`](../plans/migraine-with-aura.md) | 2026-01-30 | 90%+ |
| 49 | Mild Cognitive Impairment | [`mild-cognitive-impairment.md`](../plans/mild-cognitive-impairment.md) | 2026-01-30 | 90%+ |
| 50 | Myasthenia Gravis - Outpatient | [`myasthenia-gravis.md`](../plans/myasthenia-gravis.md) | 2026-01-30 | 90%+ |
| 51 | Normal Pressure Hydrocephalus | [`normal-pressure-hydrocephalus.md`](../plans/normal-pressure-hydrocephalus.md) | 2026-01-30 | 90%+ |
| 52 | Optic Neuritis | [`optic-neuritis.md`](../plans/optic-neuritis.md) | 2026-01-30 | 90%+ |
| 53 | Radiculopathy | [`radiculopathy.md`](../plans/radiculopathy.md) | 2026-01-30 | 90%+ |
| 54 | Small Fiber Neuropathy | [`small-fiber-neuropathy.md`](../plans/small-fiber-neuropathy.md) | 2026-01-30 | 90%+ |
| 55 | Tardive Dyskinesia | [`tardive-dyskinesia.md`](../plans/tardive-dyskinesia.md) | 2026-01-30 | 90%+ |
| 56 | Tension-Type Headache | [`tension-headache.md`](../plans/tension-headache.md) | 2026-01-30 | 90%+ |
| 57 | Vascular Dementia | [`vascular-dementia.md`](../plans/vascular-dementia.md) | 2026-01-30 | 90%+ |
| 58 | NMOSD | [`nmosd.md`](../plans/nmosd.md) | 2026-01-30 | 90%+ |
| 59 | Cerebral Venous Thrombosis | [`cerebral-venous-thrombosis.md`](../plans/cerebral-venous-thrombosis.md) | 2026-01-30 | 90%+ |
| 60 | Giant Cell Arteritis | [`giant-cell-arteritis.md`](../plans/giant-cell-arteritis.md) | 2026-01-30 | 90%+ |
| 61 | Functional Neurological Disorder | [`functional-neurological-disorder.md`](../plans/functional-neurological-disorder.md) | 2026-01-30 | 90%+ |
| 62 | Non-Convulsive Status Epilepticus | [`ncse.md`](../plans/ncse.md) | 2026-01-30 | 90%+ |
| 63 | Chronic Migraine | [`chronic-migraine.md`](../plans/chronic-migraine.md) | 2026-01-30 | 90%+ |
| 64 | Low Pressure Headache / SIH | [`low-pressure-headache.md`](../plans/low-pressure-headache.md) | 2026-01-30 | 90%+ |
| 65 | Post-Concussion Syndrome | [`post-concussion-syndrome.md`](../plans/post-concussion-syndrome.md) | 2026-01-30 | 90%+ |
| 66 | Drug-Induced Parkinsonism | [`drug-induced-parkinsonism.md`](../plans/drug-induced-parkinsonism.md) | 2026-01-30 | 90%+ |
| 67 | Wilson's Disease | [`wilsons-disease.md`](../plans/wilsons-disease.md) | 2026-01-30 | 90%+ |
| 68 | Progressive Supranuclear Palsy | [`progressive-supranuclear-palsy.md`](../plans/progressive-supranuclear-palsy.md) | 2026-01-30 | 90%+ |
| 69 | Multiple System Atrophy | [`multiple-system-atrophy.md`](../plans/multiple-system-atrophy.md) | 2026-01-30 | 90%+ |
| 70 | Lambert-Eaton Syndrome | [`lambert-eaton-syndrome.md`](../plans/lambert-eaton-syndrome.md) | 2026-01-30 | 90%+ |
| 71 | Neurosarcoidosis | [`neurosarcoidosis.md`](../plans/neurosarcoidosis.md) | 2026-01-30 | 90%+ |
| 72 | Glioblastoma | [`glioblastoma.md`](../plans/glioblastoma.md) | 2026-01-30 | 90%+ |
| 73 | Cervical Artery Dissection | [`cervical-artery-dissection.md`](../plans/cervical-artery-dissection.md) | 2026-01-30 | 90%+ |
| 74 | PRES | [`pres.md`](../plans/pres.md) | 2026-01-30 | 90%+ |
| 75 | Creutzfeldt-Jakob Disease | [`creutzfeldt-jakob-disease.md`](../plans/creutzfeldt-jakob-disease.md) | 2026-01-30 | 90%+ |
| 76 | Brain Death Evaluation | [`brain-death-evaluation.md`](../plans/brain-death-evaluation.md) | 2026-01-30 | 90%+ |
| 77 | Leptomeningeal Carcinomatosis | [`leptomeningeal-carcinomatosis.md`](../plans/leptomeningeal-carcinomatosis.md) | 2026-01-30 | 90%+ |
| 78 | RCVS | [`rcvs.md`](../plans/rcvs.md) | 2026-01-30 | 90%+ |
| 79 | CNS Vasculitis (PACNS) | [`cns-vasculitis.md`](../plans/cns-vasculitis.md) | 2026-01-30 | 90%+ |
| 80 | Viral Meningitis | [`viral-meningitis.md`](../plans/viral-meningitis.md) | 2026-01-30 | 90%+ |
| 81 | Brain Abscess | [`brain-abscess.md`](../plans/brain-abscess.md) | 2026-01-30 | 90%+ |
| 82 | Paraneoplastic Neurological Syndrome | [`paraneoplastic-neurological-syndrome.md`](../plans/paraneoplastic-neurological-syndrome.md) | 2026-01-30 | 90%+ |
| 83 | Fungal Meningitis | [`fungal-meningitis.md`](../plans/fungal-meningitis.md) | 2026-01-30 | 90%+ |
| 84 | Tuberculous Meningitis | [`tb-meningitis.md`](../plans/tb-meningitis.md) | 2026-01-30 | 90%+ |
| 85 | MOG Antibody Disease (MOGAD) | [`mogad.md`](../plans/mogad.md) | 2026-01-30 | 90%+ |
| 86 | Critical Illness Myopathy/Neuropathy | [`critical-illness-myopathy-neuropathy.md`](../plans/critical-illness-myopathy-neuropathy.md) | 2026-01-30 | 90%+ |
| 87 | Anoxic Brain Injury | [`anoxic-brain-injury.md`](../plans/anoxic-brain-injury.md) | 2026-01-30 | 90%+ |
| 88 | Alcohol Withdrawal Seizure | [`alcohol-withdrawal-seizure.md`](../plans/alcohol-withdrawal-seizure.md) | 2026-01-30 | 90%+ |
| 89 | Status Migrainosus | [`status-migrainosus.md`](../plans/status-migrainosus.md) | 2026-01-30 | 90%+ |
| 90 | Inflammatory Myopathy (DM/PM) | [`inflammatory-myopathy.md`](../plans/inflammatory-myopathy.md) | 2026-01-30 | 90%+ |
| 91 | B12 Deficiency Neuropathy | [`b12-deficiency-neuropathy.md`](../plans/b12-deficiency-neuropathy.md) | 2026-01-30 | 90%+ |
| 92 | Neurosyphilis | [`neurosyphilis.md`](../plans/neurosyphilis.md) | 2026-01-30 | 90%+ |
| 93 | Inclusion Body Myositis | [`inclusion-body-myositis.md`](../plans/inclusion-body-myositis.md) | 2026-01-30 | 90%+ |
| 94 | Meningioma | [`meningioma.md`](../plans/meningioma.md) | 2026-01-30 | 90%+ |
| 95 | Psychogenic Non-Epileptic Spells (PNES) | [`pnes.md`](../plans/pnes.md) | 2026-01-30 | 90%+ |
| 96 | Lyme Neuroborreliosis | [`lyme-neuroborreliosis.md`](../plans/lyme-neuroborreliosis.md) | 2026-01-30 | 90%+ |
| 97 | Stiff Person Syndrome | [`stiff-person-syndrome.md`](../plans/stiff-person-syndrome.md) | 2026-01-30 | 90%+ |
| 98 | Myotonic Dystrophy | [`myotonic-dystrophy.md`](../plans/myotonic-dystrophy.md) | 2026-01-31 | 90%+ |
| 99 | Narcolepsy | [`narcolepsy.md`](../plans/narcolepsy.md) | 2026-01-31 | 90%+ |
| 100 | Ataxia Evaluation | [`ataxia-evaluation.md`](../plans/ataxia-evaluation.md) | 2026-01-31 | 90%+ |
| 101 | Primary CNS Lymphoma | [`primary-cns-lymphoma.md`](../plans/primary-cns-lymphoma.md) | 2026-01-31 | 90%+ |
| 102 | Cervical Spondylotic Myelopathy | [`cervical-myelopathy.md`](../plans/cervical-myelopathy.md) | 2026-01-31 | 90%+ |
| 103 | Drug-Resistant Epilepsy | [`drug-resistant-epilepsy.md`](../plans/drug-resistant-epilepsy.md) | 2026-02-02 | 90%+ |
| 104 | Epilepsy - Chronic Management | [`epilepsy-chronic-management.md`](../plans/epilepsy-chronic-management.md) | 2026-02-02 | 90%+ |
| 105 | Eclampsia / Seizure in Pregnancy | [`eclampsia-seizure-pregnancy.md`](../plans/eclampsia-seizure-pregnancy.md) | 2026-02-02 | 90%+ |
| 106 | Moyamoya Disease | [`moyamoya-disease.md`](../plans/moyamoya-disease.md) | 2026-02-02 | 90%+ |
| 107 | Post-Stroke Management | [`post-stroke-management.md`](../plans/post-stroke-management.md) | 2026-02-02 | 90%+ |
| 108 | Carotid Stenosis | [`carotid-stenosis.md`](../plans/carotid-stenosis.md) | 2026-02-02 | 90%+ |
| 109 | Headache Evaluation | [`headache-evaluation.md`](../plans/headache-evaluation.md) | 2026-02-02 | 90%+ |
| 110 | Thunderclap Headache Evaluation | [`thunderclap-headache-evaluation.md`](../plans/thunderclap-headache-evaluation.md) | 2026-02-02 | 90%+ |
| 111 | Botulism | [`botulism.md`](../plans/botulism.md) | 2026-02-02 | 90%+ |
| 112 | Peroneal Neuropathy | [`peroneal-neuropathy.md`](../plans/peroneal-neuropathy.md) | 2026-02-02 | 90%+ |
| 113 | Plexopathy | [`plexopathy.md`](../plans/plexopathy.md) | 2026-02-02 | 90%+ |
| 114 | Tics / Tourette Syndrome | [`tics-tourette-syndrome.md`](../plans/tics-tourette-syndrome.md) | 2026-02-02 | 90%+ |
| 115 | Neurocysticercosis | [`neurocysticercosis.md`](../plans/neurocysticercosis.md) | 2026-02-02 | 90%+ |
| 116 | HIV-Associated Neurocognitive Disorder | [`hiv-associated-neurocognitive-disorder.md`](../plans/hiv-associated-neurocognitive-disorder.md) | 2026-02-02 | 90%+ |
| 117 | Susac Syndrome | [`susac-syndrome.md`](../plans/susac-syndrome.md) | 2026-02-02 | 90%+ |
| 118 | Neuro-Behcet's Disease | [`neuro-behcets-disease.md`](../plans/neuro-behcets-disease.md) | 2026-02-02 | 90%+ |
| 119 | Hashimoto's Encephalopathy | [`hashimotos-encephalopathy.md`](../plans/hashimotos-encephalopathy.md) | 2026-02-02 | 90%+ |
| 120 | Nystagmus Evaluation | [`nystagmus-evaluation.md`](../plans/nystagmus-evaluation.md) | 2026-02-02 | 90%+ |
| 121 | Tinnitus Evaluation | [`tinnitus-evaluation.md`](../plans/tinnitus-evaluation.md) | 2026-02-02 | 90%+ |
| 122 | Paresthesia / Numbness / Tingling | [`paresthesia-numbness-tingling.md`](../plans/paresthesia-numbness-tingling.md) | 2026-02-02 | 90%+ |
| 123 | Headache, Unspecified | [`headache-unspecified.md`](../plans/headache-unspecified.md) | 2026-02-02 | 90%+ |
| 124 | Tremor, Unspecified | [`tremor-unspecified.md`](../plans/tremor-unspecified.md) | 2026-02-02 | 90%+ |
| 125 | REM Sleep Behavior Disorder | [`rem-sleep-behavior-disorder.md`](../plans/rem-sleep-behavior-disorder.md) | 2026-02-07 | — |
| 126 | Obstructive Sleep Apnea — Neuro | [`obstructive-sleep-apnea-neuro.md`](../plans/obstructive-sleep-apnea-neuro.md) | 2026-02-07 | — |
| 127 | Insomnia — Neurological Approach | [`insomnia-neurological.md`](../plans/insomnia-neurological.md) | 2026-02-07 | — |
| 128 | Idiopathic Hypersomnia | [`idiopathic-hypersomnia.md`](../plans/idiopathic-hypersomnia.md) | 2026-02-07 | — |
| 129 | Non-REM Parasomnias | [`non-rem-parasomnias.md`](../plans/non-rem-parasomnias.md) | 2026-02-07 | — |
| 130 | POTS (Postural Orthostatic Tachycardia Syndrome) | [`pots.md`](../plans/pots.md) | 2026-02-09 | 90% (54/60) |
| 131 | Neurogenic Orthostatic Hypotension | [`neurogenic-orthostatic-hypotension.md`](../plans/neurogenic-orthostatic-hypotension.md) | 2026-02-09 | 90% (54/60) |
| 132 | Occipital Neuralgia | [`occipital-neuralgia.md`](../plans/occipital-neuralgia.md) | 2026-02-09 | 93% (56/60) |
| 133 | Complex Regional Pain Syndrome (CRPS) | [`crps.md`](../plans/crps.md) | 2026-02-09 | 93% (56/60) |
| 134 | Neuropathic Pain Management | [`neuropathic-pain-management.md`](../plans/neuropathic-pain-management.md) | 2026-02-09 | 93% (56/60) |
| 135 | Ulnar Neuropathy | [`ulnar-neuropathy.md`](../plans/ulnar-neuropathy.md) | 2026-02-09 | 90%+ |
| 136 | Chemotherapy-Induced Peripheral Neuropathy (CIPN) | [`chemotherapy-induced-neuropathy.md`](../plans/chemotherapy-induced-neuropathy.md) | 2026-02-09 | 90%+ |
| 137 | Parkinson's Disease — Motor Fluctuations and Dyskinesia | [`parkinsons-motor-fluctuations.md`](../plans/parkinsons-motor-fluctuations.md) | 2026-02-09 | 90%+ |
| 138 | Parkinson's Disease — Psychosis | [`parkinsons-psychosis.md`](../plans/parkinsons-psychosis.md) | 2026-02-09 | 90%+ |
| 139 | Delirium versus Dementia — Diagnostic Evaluation | [`delirium-vs-dementia.md`](../plans/delirium-vs-dementia.md) | 2026-02-09 | 90%+ |
| 140 | Autoimmune Dementia / Encephalopathy | [`autoimmune-dementia.md`](../plans/autoimmune-dementia.md) | 2026-02-09 | 90%+ |
| 141 | New Daily Persistent Headache (NDPH) | [`new-daily-persistent-headache.md`](../plans/new-daily-persistent-headache.md) | 2026-02-09 | 90%+ |
| 142 | Lumbar Spinal Stenosis | [`lumbar-stenosis.md`](../plans/lumbar-stenosis.md) | 2026-02-09 | 90%+ |
| 143 | Horner Syndrome | [`horner-syndrome.md`](../plans/horner-syndrome.md) | 2026-02-09 | 90%+ |
| 144 | Hypertensive Encephalopathy | [`hypertensive-encephalopathy.md`](../plans/hypertensive-encephalopathy.md) | 2026-02-09 | 90%+ |

---

## Completed (Awaiting Physician Approval)

| Plan | File | Completed Date | Final Score |
|------|------|----------------|-------------|
| *(none)* | — | — | — |

---

## Notes

- **TIA duplicate resolved** (2026-01-30): `tia.md` removed, canonical file is `transient-ischemic-attack.md`.
- **Parkinson's Disease** and **Parkinson's Disease - New Diagnosis** are separate plans (general vs. new diagnosis workup).
- **Myasthenia Gravis** has three variants: Crisis (approved), New Diagnosis (approved), and Outpatient (approved).
- Queue updated 2026-02-09. Total approved: 134 plans. Tier 14 queued: 10 plans (5 high-value gaps + 5 subspecialty gaps).
- **Tier 14 queued** (2026-02-09): 10 plans across Tier 14A (Lumbar Stenosis, Ulnar Neuropathy, Chemo-Induced Neuropathy, PD Motor Fluctuations, Delirium vs Dementia) and Tier 14B (NDPH, Horner Syndrome, Hypertensive Encephalopathy, PD Psychosis, Autoimmune Dementia). 20 more conditions remain in Tier 14C-D (see tracker).
- **Autonomic & Pain expansion** (2026-02-09): 5 Tier 13 drafts approved — POTS, Neurogenic Orthostatic Hypotension, Occipital Neuralgia, CRPS, Neuropathic Pain Management. New "Autonomic & Pain Disorders" nav section created.
- **Sleep Medicine expansion** (2026-02-07): 5 new drafts added — REM Sleep Behavior Disorder, Obstructive Sleep Apnea (Neuro), Insomnia (Neurological), Idiopathic Hypersomnia, Non-REM Parasomnias. Complements existing Narcolepsy and RLS plans.
- **Tier 10 batch** (2026-01-31): 5 new drafts added — Drug-Resistant Epilepsy, Epilepsy Chronic Management, Eclampsia/Seizure in Pregnancy, Moyamoya Disease, Post-Stroke Management. Awaiting physician approval.
- **Tier 11 HIGH PRIORITY batch** (2026-02-01): 17 plans queued as physician-prioritized. Includes vascular (Carotid Stenosis), headache workups (Headache Evaluation, Thunderclap, Headache Unspecified), rare/infectious (Botulism, Neurocysticercosis, HIV-HAND), autoimmune/inflammatory (Susac, Neuro-Behcet's, Hashimoto's Encephalopathy), peripheral (Peroneal Neuropathy, Plexopathy, Paresthesia), movement (Tics/Tourette, Tremor Unspecified), and symptom evaluations (Nystagmus, Tinnitus). Note: "Headache Evaluation" and "Headache, Unspecified" may overlap — physician to clarify scope.

---

## Instructions for Claude

1. **Claim a plan**: Change status from `pending` to `in_progress`, add your session ID
2. **Process the plan**: Follow the skills pipeline in `CLAUDE.md`
3. **Update on completion**: Change status to `completed`, record final score
4. **Commit changes**: Include queue.md updates in your commit
5. **Keep this file current**: When plans are approved or added outside the queue, update this file to reflect the actual repo state
