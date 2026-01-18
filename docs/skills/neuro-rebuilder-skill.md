---
title: Rebuilder Skill
---

---
name: neuro-rebuilder
description: Incorporates approved revisions from neuro-checker validation into clinical decision support templates. Use after physician review of Checker recommendations to systematically apply approved changes while maintaining document integrity and version control.
---

# Neuro Clinical Recommendation Rebuilder

Systematically incorporate validated revisions into clinical decision support templates while maintaining document structure, version control, and audit trails.

## When to Use

Use neuro-rebuilder when:
1. neuro-checker has produced a validation report with recommended revisions
2. A physician has reviewed the Checker recommendations
3. Specific revisions have been approved for implementation
4. The template needs to be updated to a new version

## Input Requirements

The Rebuilder requires:
1. **Original template** - The current version of the clinical recommendation
2. **Checker report** - The validation output with scored domains and revision recommendations
3. **Physician approval** - Clear indication of which revisions are approved (may be all, some, or modified versions)

## Rebuilder Workflow

### Step 1: Parse Approved Revisions

Review the Checker report and identify:
- **Critical Issues (C-codes)** - Must be addressed; these block clinical use
- **Setting Coverage Issues (S-codes)** - High priority gaps in venue coverage
- **Medication Issues (M-codes)** - Dosing, grouping, or coverage gaps
- **Recommended Revisions (R-codes)** - Prioritized improvement suggestions
- **Verification Items (V-codes)** - Items needing physician confirmation

For each item, note whether it is:
- ✅ Approved as written
- ✅ Approved with modification (note the modification)
- ❌ Declined (note reason if provided)
- ⏸️ Deferred for future version

### Step 2: Implement Revisions Systematically

Process revisions in this order:

1. **Critical Issues First** - Safety and accuracy fixes
2. **Setting Coverage** - Add missing venue tags
3. **Medication Completeness** - Individual drug rows, dosing
4. **Section 6 Monitoring** - Venue columns, critical monitoring
5. **Other Revisions** - In priority order (R1, R2, R3...)

For each revision:
- Locate the exact section and row
- Make the specified change
- Preserve surrounding formatting
- Do NOT introduce new changes not in the approval list

### Step 3: Update Metadata

After implementing revisions:

1. **Increment version number** (e.g., v1.0 → v1.1 for minor, v1.0 → v2.0 for major)
2. **Update REVISED date** to current date
3. **Update STATUS** if applicable
4. **Add Change Log entry** documenting all changes made

### Step 4: Verify Structure Integrity

After rebuilding, confirm:
- [ ] All 8 sections present (1-4 Action Items, 5-8 Reference)
- [ ] Table formatting intact (columns aligned, headers present)
- [ ] Priority key included
- [ ] Section dividers (═══) present
- [ ] No orphaned content or broken tables

## Output Format

```
# [DIAGNOSIS NAME]

**VERSION:** [X.X]  
**CREATED:** [Original date]  
**REVISED:** [Today's date]  
**STATUS:** [Revised per physician feedback / Validated / etc.]

---

[Full rebuilt template with all approved revisions incorporated]

---

## CHANGE LOG

**vX.X ([Today's date])**
- [Change 1 from approved revision]
- [Change 2 from approved revision]
- [Change 3 from approved revision]
...

**vX.X-1 ([Previous date])**
- [Previous changes]
```

## Rebuilder Principles

1. **Only implement approved revisions** - Do not add, remove, or modify content beyond what was explicitly approved
2. **Preserve document structure** - Maintain the 8-section format, table structures, and formatting conventions
3. **Maintain audit trail** - Every change must be documented in the Change Log
4. **Verify accuracy** - When implementing dosing or clinical changes, verify the revision is clinically accurate
5. **Flag uncertainties** - If an approved revision is ambiguous, ask for clarification before implementing
6. **Protect safety content** - Take extra care with contraindications, warnings, and critical monitoring parameters

## Version Numbering

| Change Type | Version Increment | Examples |
|-------------|-------------------|----------|
| Minor corrections | +0.1 | Typo fix, clarification, minor dosing adjustment |
| Moderate revisions | +0.1 | Added labs, expanded referrals, new monitoring |
| Major restructuring | +1.0 | New sections, significant clinical content changes |
| Complete rebuild | +1.0 | Structural overhaul, format change |

## Handling Conflicts

If approved revisions conflict with each other:
1. Stop and flag the conflict
2. Present both revisions to the physician
3. Request clarification on which takes precedence
4. Document the resolution in Change Log

## Post-Rebuild Verification

After rebuilding, the template should be re-validated with neuro-checker to confirm:
- Validation score improved (or maintained if already high)
- No new issues introduced
- All approved revisions successfully implemented

## Example Change Log Entry

```
**v1.2 (January 18, 2026)**
- Added phosphorus to Section 1A core labs per C1 (hypophosphatemia in alcohol withdrawal)
- Updated levetiracetam loading dose range to 40-60 mg/kg per R2
- Added flumazenil to Section 3A with seizure threshold warning per R3
- Expanded Section 4B patient instructions with seizure diary guidance per S2
- Added venue columns to Section 6 Monitoring per M1
- Corrected lamotrigine titration schedule in Section 3C per V1 (physician confirmed)
```

## Integration with Claude Code

When using neuro-rebuilder in Claude Code:

1. Load the original template file
2. Load the Checker report
3. Parse the approved revisions (from physician input or file)
4. Apply changes systematically using str_replace or file editing
5. Save the rebuilt template with new version number
6. Generate a summary of changes made

## Change Log

**v1.0 (January 18, 2026)**
- Initial creation
- Defined workflow: parse approvals → implement systematically → update metadata → verify structure
- Added version numbering guidelines
- Added conflict handling procedures
- Added post-rebuild verification requirements
