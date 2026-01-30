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

| Plan | File | Status | Session | Last Updated |
|------|------|--------|---------|--------------|
| ALS | [`als.md`](als.md) | `completed` | Claude | 2026-01-30 |
| Alzheimer's Disease | [`alzheimers-disease.md`](alzheimers-disease.md) | `completed` | Claude | 2026-01-30 |
| Carpal Tunnel Syndrome | [`carpal-tunnel-syndrome.md`](carpal-tunnel-syndrome.md) | `completed` | Claude | 2026-01-30 |
| Dystonia | [`dystonia.md`](dystonia.md) | `completed` | Claude | 2026-01-30 |
| Frontotemporal Dementia | [`frontotemporal-dementia.md`](frontotemporal-dementia.md) | `completed` | Claude | 2026-01-30 |
| Huntington's Disease | [`huntingtons-disease.md`](huntingtons-disease.md) | `completed` | Claude | 2026-01-30 |
| Lewy Body Dementia | [`lewy-body-dementia.md`](lewy-body-dementia.md) | `completed` | Claude | 2026-01-30 |
| Migraine with Aura | [`migraine-with-aura.md`](migraine-with-aura.md) | `completed` | Claude | 2026-01-30 |
| Mild Cognitive Impairment | [`mild-cognitive-impairment.md`](mild-cognitive-impairment.md) | `completed` | Claude | 2026-01-30 |
| Myasthenia Gravis - Outpatient | [`myasthenia-gravis.md`](myasthenia-gravis.md) | `completed` | Claude | 2026-01-30 |
| Normal Pressure Hydrocephalus | [`normal-pressure-hydrocephalus.md`](normal-pressure-hydrocephalus.md) | `completed` | Claude | 2026-01-30 |
| Optic Neuritis | [`optic-neuritis.md`](optic-neuritis.md) | `completed` | Claude | 2026-01-30 |
| Radiculopathy | [`radiculopathy.md`](radiculopathy.md) | `completed` | Claude | 2026-01-30 |
| Small Fiber Neuropathy | [`small-fiber-neuropathy.md`](small-fiber-neuropathy.md) | `completed` | Claude | 2026-01-30 |
| Tardive Dyskinesia | [`tardive-dyskinesia.md`](tardive-dyskinesia.md) | `completed` | Claude | 2026-01-30 |
| Tension Headache | [`tension-headache.md`](tension-headache.md) | `completed` | Claude | 2026-01-30 |
| Vascular Dementia | [`vascular-dementia.md`](vascular-dementia.md) | `completed` | Claude | 2026-01-30 |

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
| 37 | TIA | [`tia.md`](../plans/tia.md) | 2026-01-27 | 90%+ |
| 38 | Transient Ischemic Attack | [`transient-ischemic-attack.md`](../plans/transient-ischemic-attack.md) | 2026-01-27 | 90%+ |
| 39 | Trigeminal Neuralgia | [`trigeminal-neuralgia.md`](../plans/trigeminal-neuralgia.md) | 2026-01-27 | 90%+ |
| 40 | Vertigo/Dizziness Evaluation | [`vertigo-dizziness-evaluation.md`](../plans/vertigo-dizziness-evaluation.md) | 2026-01-27 | 90%+ |
| 41 | Wernicke Encephalopathy | [`wernicke-encephalopathy.md`](../plans/wernicke-encephalopathy.md) | 2026-01-27 | 90%+ |

---

## Completed (Awaiting Physician Approval)

| Plan | File | Completed Date | Final Score |
|------|------|----------------|-------------|
| *(none)* | — | — | — |

---

## Notes

- **TIA** and **Transient Ischemic Attack** both exist in `docs/plans/` — may be duplicates with different naming conventions.
- **Parkinson's Disease** and **Parkinson's Disease - New Diagnosis** are separate plans (general vs. new diagnosis workup).
- **Myasthenia Gravis** has three variants: Crisis (approved), New Diagnosis (approved), and Outpatient (pending).
- Queue updated 2026-01-29 to reconcile with actual repo contents. Many plans were added via batch commits and bypassed the queue workflow.

---

## Instructions for Claude

1. **Claim a plan**: Change status from `pending` to `in_progress`, add your session ID
2. **Process the plan**: Follow the skills pipeline in `CLAUDE.md`
3. **Update on completion**: Change status to `completed`, record final score
4. **Commit changes**: Include queue.md updates in your commit
5. **Keep this file current**: When plans are approved or added outside the queue, update this file to reflect the actual repo state
