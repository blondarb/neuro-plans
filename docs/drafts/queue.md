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
| *(none)* | — | — | — | — |

---

## Approved (Moved to `docs/plans/`)

| Plan | File | Approved Date | Final Score |
|------|------|---------------|-------------|
| New Onset Seizure | [`new-onset-seizure.md`](../plans/new-onset-seizure.md) | 2026-01-20 | 93% (56/60) |
| Multiple Sclerosis (New Diagnosis) | [`ms-new-diagnosis.md`](../plans/ms-new-diagnosis.md) | 2026-01-20 | 90% (54/60) |

---

## Completed (Awaiting Physician Approval)

| Plan | File | Completed Date | Final Score |
|------|------|----------------|-------------|
| Peripheral Neuropathy | [`peripheral-neuropathy.md`](peripheral-neuropathy.md) | 2026-01-20 | 90% (54/60) |

---

## Instructions for Claude

1. **Claim a plan**: Change status from `pending` to `in_progress`, add your session ID
2. **Process the plan**: Follow the skills pipeline in `CLAUDE.md`
3. **Update on completion**: Change status to `completed`, record final score
4. **Commit changes**: Include queue.md updates in your commit
