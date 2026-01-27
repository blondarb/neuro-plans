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
| *(empty - all plans moved to completed)* | — | — | — | — |

---

## Approved (Moved to `docs/plans/`)

| Plan | File | Approved Date | Final Score |
|------|------|---------------|-------------|
| New Onset Seizure | [`new-onset-seizure.md`](../plans/new-onset-seizure.md) | 2026-01-20 | 93% (56/60) |
| Multiple Sclerosis (New Diagnosis) | [`ms-new-diagnosis.md`](../plans/ms-new-diagnosis.md) | 2026-01-20 | 90% (54/60) |
| Peripheral Neuropathy | [`peripheral-neuropathy.md`](../plans/peripheral-neuropathy.md) | 2026-01-20 | 90% (54/60) |
| Acute Ischemic Stroke | [`acute-ischemic-stroke.md`](../plans/acute-ischemic-stroke.md) | 2026-01-21 | 92% (55/60) |
| Guillain-Barré Syndrome | [`guillain-barre-syndrome.md`](../plans/guillain-barre-syndrome.md) | 2026-01-26 | 90%+ |
| Myasthenia Gravis - Crisis | [`myasthenia-gravis-crisis.md`](../plans/myasthenia-gravis-crisis.md) | 2026-01-26 | 90%+ |
| Bacterial Meningitis | [`bacterial-meningitis.md`](../plans/bacterial-meningitis.md) | 2026-01-26 | 90%+ |
| HSV Encephalitis | [`hsv-encephalitis.md`](../plans/hsv-encephalitis.md) | 2026-01-26 | 90%+ |
| Autoimmune Encephalitis | [`autoimmune-encephalitis.md`](../plans/autoimmune-encephalitis.md) | 2026-01-26 | 90%+ |

---

## Completed (Awaiting Physician Approval)

| Plan | File | Completed Date | Final Score |
|------|------|----------------|-------------|
| *(none)* | — | — | — |

---

## Instructions for Claude

1. **Claim a plan**: Change status from `pending` to `in_progress`, add your session ID
2. **Process the plan**: Follow the skills pipeline in `CLAUDE.md`
3. **Update on completion**: Change status to `completed`, record final score
4. **Commit changes**: Include queue.md updates in your commit
