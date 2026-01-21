# Neuro Comment Review Skill

**Version:** 2.0
**Last Updated:** January 21, 2026

## Purpose

Review and process comments/feedback on clinical plans. For each comment, research the suggestion, verify against medical literature, and present findings for physician approval before implementing changes.

## Trigger

User says any of:
- "Review comments on [Plan Name]"
- "Check feedback on [Plan Name]"
- "Process comments"
- "What comments need review?"

## File Locations

| Purpose | Location |
|---------|----------|
| Active comments | `docs/comments/active/[plan-name].md` |
| Archived comments | `docs/comments/archive/YYYY-MM/[plan-name].md` |
| Change log | `docs/logs/comment-changes-log.md` |
| Comments index | `docs/comments/index.md` |

## Workflow

### Phase 1: Comment Collection

1. **Read active comment files** from `docs/comments/active/`
2. **Identify comments with `Status: pending`**
3. **Read the target plan** to understand context

```bash
# Check all active comment files
ls docs/comments/active/
cat docs/comments/active/[plan-name].md
```

### Phase 2: Comment Categorization

For each comment, verify the category:

| Category | Code | Action Required |
|----------|------|-----------------|
| Clinical Content Change | `CLIN` | Research required before implementation |
| Dosing/Medication Update | `DOSE` | Research required + safety verification |
| New Evidence/Citation | `CITE` | Citation verification required |
| Formatting/Typo | `FMT` | Can implement directly |
| Question/Clarification | `Q` | May need content addition |
| Out of Scope | `OOS` | Note for future or reject |
| Already Addressed | `DONE` | Mark as resolved |

### Phase 3: Research & Verification

For each `CLIN`, `DOSE`, or `CITE` comment:

1. **Search for evidence** using WebSearch to find:
   - Current guidelines (AAN, AES, NCS, etc.)
   - Recent systematic reviews
   - Major clinical trials
   - UpToDate/expert consensus

2. **Evaluate the suggestion**:
   - Is it supported by evidence?
   - Does it conflict with existing recommendations?
   - What is the evidence level (Class I-IV)?
   - Are there safety concerns?

3. **Document findings** in this format:

```markdown
### Comment CMT-XX-NNN: [Brief summary]

**Category:** [CODE]
**Section Affected:** [Section number and name]
**Original Comment:** "[Full comment text]"

**Research Findings:**
- [Source 1]: [Finding]
- [Source 2]: [Finding]
- [Guideline reference if applicable]

**Recommendation:** ACCEPT / REJECT / MODIFY / NEEDS DISCUSSION

**Rationale:** [Why this recommendation]

**Proposed Change:** (if ACCEPT or MODIFY)
```
[Exact text change to be made]
```

**Evidence Level:** [I/II/III/IV or N/A]
```

### Phase 4: Summary Report

Present a summary table to the physician:

```markdown
## Comment Review Summary for [Plan Name]

| # | Comment ID | Category | Summary | Recommendation | Evidence |
|---|------------|----------|---------|----------------|----------|
| 1 | CMT-SE-001 | CLIN | [brief] | ACCEPT | Level II |
| 2 | CMT-SE-002 | DOSE | [brief] | REJECT | Insufficient |
| 3 | CMT-SE-003 | FMT | [brief] | ACCEPT | N/A |

### Recommended Actions
- [ ] Accept CMT-SE-001: [change description]
- [ ] Accept CMT-SE-003: [change description]
- [ ] Reject CMT-SE-002: [reason]

### Questions Requiring Your Input
- CMT-SE-004: [question needing physician decision]

**How would you like to proceed?**
- "Accept all" - Implement all recommended changes
- "Accept [IDs]" - Implement specific changes (e.g., "Accept 001, 003")
- "Reject [IDs]" - Reject specific comments
- "Discuss [ID]" - Need more information on a specific comment
```

### Phase 5: Implementation

After physician approval:

1. **Apply approved changes** to the plan markdown file
   ```bash
   # Edit the plan file
   docs/plans/[plan-name].md
   ```

2. **Run validation** to ensure quality maintained
   ```bash
   python scripts/generate_json.py docs/plans/[plan-name].md --validate-only
   ```

3. **Regenerate JSON** for clinical tool
   ```bash
   python scripts/generate_json.py docs/plans/[plan-name].md --merge
   ```

4. **Update plan metadata**:
   - Increment version number (e.g., 1.5 → 1.6)
   - Update REVISED date
   - Add changelog entry

5. **Update comment status** in active file:
   - Change `Status: pending` → `Status: resolved-accepted` or `Status: resolved-rejected`

6. **Log the change** in `docs/logs/comment-changes-log.md`:

```markdown
### 2026-01-21 - Status Epilepticus - CMT-SE-001

**Comment:** "Should phenobarbital be listed as second-line option?"
**Type:** CLIN
**Section Affected:** 3B Second-Line ASMs

**Research Findings:**
- ESETT Trial (NEJM 2019): Phenobarbital non-inferior to levetiracetam/fosphenytoin
- NCS Guidelines 2023: Lists phenobarbital as acceptable second-line agent

**Resolution:** ACCEPTED
**Evidence Level:** I

**Change Made:** Added phenobarbital 15-20 mg/kg IV to Section 3B
**Plan Version:** 1.5 → 1.6
**Rationale:** Supported by Level I evidence from ESETT trial
```

7. **Archive the comment**:
   - Create archive file if needed: `docs/comments/archive/2026-01/[plan-name].md`
   - Move resolved comment from active to archive
   - Update comment counts in `docs/comments/index.md`

8. **Commit and push**:
```bash
git add docs/plans/[plan-name].md docs/data/plans.json \
        docs/comments/active/[plan-name].md \
        docs/comments/archive/2026-01/[plan-name].md \
        docs/logs/comment-changes-log.md \
        docs/comments/index.md
git commit -m "Address reviewer comment CMT-XX-NNN on [Plan Name]

- [Change summary]
- Evidence: [Source]
- Plan version: X.Y → X.Z"
git push
```

### Phase 6: Rejection Handling

For rejected comments:

1. **Update comment status** to `resolved-rejected`
2. **Log rejection** with rationale in comment-changes-log.md
3. **Archive the comment** (same as accepted)
4. **No changes** made to plan

## Research Guidelines

### Preferred Sources (in order)

1. **Practice Guidelines**
   - American Academy of Neurology (AAN)
   - American Epilepsy Society (AES)
   - Neurocritical Care Society (NCS)
   - European Academy of Neurology (EAN)

2. **Systematic Reviews**
   - Cochrane Database
   - PubMed systematic reviews

3. **Landmark Trials**
   - ESETT, RAMPART, etc. for epilepsy
   - Named trials for specific conditions

4. **Expert Consensus**
   - UpToDate
   - Continuum (AAN)
   - Major textbooks

### Evidence Levels

| Level | Description |
|-------|-------------|
| I | Randomized controlled trial, systematic review of RCTs |
| II | Prospective cohort, well-designed observational |
| III | Retrospective cohort, case-control |
| IV | Case series, expert opinion |

### Safety-Critical Changes

For any dosing or medication changes:
- Verify against FDA labeling
- Check for contraindications
- Note monitoring requirements
- Flag any black box warnings

## Comment ID Format

Use plan-specific prefixes:
- `CMT-SE-XXX` - Status Epilepticus
- `CMT-NOS-XXX` - New Onset Seizure
- `CMT-MS-XXX` - MS - New Diagnosis
- `CMT-PN-XXX` - Peripheral Neuropathy
- `CMT-AIS-XXX` - Acute Ischemic Stroke

## Integration with Other Skills

After implementing comment changes:

1. **Checker** - Validate the updated plan still meets quality standards
2. **Citation Verifier** - If new citations were added
3. **Rebuilder** - If extensive changes needed

## Example Session

**User:** "Review comments on Status Epilepticus"

**Assistant:**
```
I'll review the active comments for Status Epilepticus.

Reading docs/comments/active/status-epilepticus.md...

Found 2 pending comments:

### CMT-SE-001 (2026-01-20)
- Section: 3B Second-Line ASMs
- Type: DOSE
- Comment: "Fosphenytoin loading should be 20 PE/kg, not 15 PE/kg"

### CMT-SE-002 (2026-01-20)
- Section: 3D Anesthetics
- Type: CLIN
- Comment: "Consider adding ketamine earlier in the algorithm"

Let me research these...

[Performs WebSearch for current guidelines]

## Comment Review Summary

| # | ID | Category | Summary | Recommendation | Evidence |
|---|------------|----------|---------|----------------|----------|
| 1 | CMT-SE-001 | DOSE | Fosphenytoin 20 PE/kg | ACCEPT | Level I (NCS) |
| 2 | CMT-SE-002 | CLIN | Earlier ketamine | MODIFY | Level III |

### Research Details

**CMT-SE-001:** NCS Guidelines 2023 recommend fosphenytoin 20 PE/kg.
Our current 15 PE/kg is below guideline recommendation.

**CMT-SE-002:** Ketamine is reasonable but evidence is Level III.
Recommend adding as "consider" rather than primary agent.

How would you like to proceed?
```

**User:** "Accept both"

**Assistant:**
```
Implementing approved changes...

1. Updated Section 3B: Fosphenytoin 15 PE/kg → 20 PE/kg
2. Updated Section 3D: Added ketamine consideration note
3. Version: 1.5 → 1.6
4. Validation: ✅ PASSED
5. JSON regenerated
6. Comments archived
7. Change log updated

Committed and pushed to branch.
```

## Change Log

**v2.0 (January 21, 2026)**
- Added file-based comment storage system
- Added archive workflow for resolved comments
- Added comment-changes-log integration
- Added comment ID format with plan prefixes
- Restructured for automated workflow

**v1.0 (January 19, 2026)**
- Initial version with manual comment collection
