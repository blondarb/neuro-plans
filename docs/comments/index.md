# Comments & Feedback

This section tracks comments and suggested improvements to clinical plans. Comments are reviewed, verified against medical literature, and implemented after physician approval.

## How to Submit Feedback

1. **Identify the plan** you want to comment on
2. **Add your comment** to the appropriate file in `docs/comments/active/`
3. **Use the comment template** (see format below)
4. **Submit a pull request** or notify the maintainers

## Comment Template

```markdown
### CMT-XXX (YYYY-MM-DD)
- **Section:** [Section number and name, e.g., "3A Acute Treatment"]
- **Submitter:** [Your name/role]
- **Type:** [CLIN | DOSE | CITE | FMT | Q]
- **Comment:** [Your suggestion or question]
- **Status:** pending
```

## Comment Types

| Code | Type | Description | Verification Required |
|------|------|-------------|----------------------|
| `CLIN` | Clinical Content | New recommendations, workflow changes | Yes - guideline review |
| `DOSE` | Dosing/Medication | Dosing adjustments, new medications | Yes - safety verification |
| `CITE` | Citation/Evidence | New evidence, updated references | Yes - citation verification |
| `FMT` | Formatting | Typos, formatting fixes | No |
| `Q` | Question | Clarification requests | May require content addition |

## Active Comments by Plan

| Plan | Active Comments | Last Updated |
|------|-----------------|--------------|
| [Status Epilepticus](active/status-epilepticus.md) | 0 | — |
| [New Onset Seizure](active/new-onset-seizure.md) | 0 | — |
| [MS - New Diagnosis](active/ms-new-diagnosis.md) | 0 | — |
| [Peripheral Neuropathy](active/peripheral-neuropathy.md) | 0 | — |
| [Acute Ischemic Stroke](active/acute-ischemic-stroke.md) | 0 | — |

## Review Process

1. **Collection** - Comments gathered from active files
2. **Research** - Suggestions verified against current guidelines and literature
3. **Presentation** - Findings presented with ACCEPT/REJECT/MODIFY recommendation
4. **Approval** - Physician reviews and approves changes
5. **Implementation** - Approved changes applied to plan, JSON regenerated
6. **Logging** - Changes recorded in [Comment Changes Log](../logs/comment-changes-log.md)
7. **Archiving** - Resolved comments moved to archive (no longer visible)

## Archives

Resolved comments are moved to the [archive](archive/) directory, organized by month. These are retained for audit purposes but not displayed to users.
