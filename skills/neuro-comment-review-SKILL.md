# Neuro Comment Review Skill

**Version:** 1.0
**Last Updated:** January 19, 2026

## Purpose

Review and process comments/feedback from the clinical plans website. For each comment, research the suggestion, verify against medical literature, and present findings for physician approval before implementing changes.

## Trigger

User says any of:
- "Review comments on [Plan Name]"
- "Check feedback on [Plan Name]"
- "Process comments for [Plan Name]"
- "What comments are on [Plan Name]?"

## Workflow

### Phase 1: Comment Collection

1. **Identify the plan file** based on user request
2. **Read the current plan** to understand context
3. **Ask user to provide comments** from the website (since we can't directly access Firebase from CLI)

Present this prompt to the user:
```
To review comments, please:
1. Go to the plan page on the website
2. Look at the comments section at the bottom
3. Copy/paste each comment here, or summarize the feedback

Format: [Section] - [Comment text] - [Commenter if visible]
```

### Phase 2: Comment Categorization

For each comment received, categorize as:

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
### Comment #[N]: [Brief summary]

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

Present a summary table:

```markdown
## Comment Review Summary for [Plan Name]

| # | Category | Summary | Recommendation | Evidence |
|---|----------|---------|----------------|----------|
| 1 | CLIN | [brief] | ACCEPT | Level II |
| 2 | DOSE | [brief] | REJECT | Insufficient |
| 3 | FMT | [brief] | ACCEPT | N/A |
...

### Recommended Actions
- [ ] Accept Comment #1: [change]
- [ ] Accept Comment #3: [change]
- [ ] Reject Comment #2: [reason]

### Questions Requiring Your Input
- Comment #4: [question needing physician decision]
```

### Phase 5: Implementation

After user approval:

1. **Make approved changes** to the plan file
2. **Update version number** (increment minor version, e.g., 1.4 → 1.5)
3. **Update REVISED date**
4. **Add changelog entry** documenting:
   - What changed
   - Why (comment-driven, with evidence reference)
   - Source of the suggestion

5. **Commit and push** to GitHub:
```bash
git add [plan-file]
git commit -m "Update [Plan Name] v[X.Y]: Address reviewer comments

- [Change 1 summary]
- [Change 2 summary]

Based on reviewer feedback with evidence verification.

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
git push
```

6. **Generate resolution summary** for user to mark comments as resolved on website

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

## Output Format

The skill produces:

1. **Comment Review Report** (presented in chat)
2. **Updated plan file** (after approval)
3. **Git commit** with changes pushed
4. **Resolution notes** for marking comments done on website

## Example Session

**User:** "Review comments on Status Epilepticus"

**Assistant:**
```
I'll help review comments on the Status Epilepticus plan.

To get started, please visit the Status Epilepticus page on the website and copy any comments from the feedback section.

Format each comment as:
[Section] - [Comment text]

For example:
"Section 3 Treatment - Should we add phenobarbital as a second-line option?"
```

**User:** [provides comments]

**Assistant:**
```
I found 3 comments to review. Let me research each one...

[Performs research]

## Comment Review Summary for Status Epilepticus

| # | Category | Summary | Recommendation | Evidence |
|---|----------|---------|----------------|----------|
| 1 | DOSE | Add phenobarbital 2nd line | ACCEPT | Level I (ESETT) |
| 2 | FMT | Fix typo in Section 4 | ACCEPT | N/A |
| 3 | CLIN | Add PNES differentiation | MODIFY | Level III |

### Recommended Actions
- [ ] Accept #1: Add phenobarbital 15-20 mg/kg IV to Section 3B
- [ ] Accept #2: Fix "benzodiazapine" → "benzodiazepine"
- [ ] Modify #3: Add brief PNES note to differential, not full protocol

Would you like me to implement these changes?
```

**User:** "Yes, implement all"

**Assistant:** [Makes changes, updates version, pushes to GitHub]

## Integration with Other Skills

This skill works alongside:
- **Builder**: Creates initial drafts
- **Checker/Rebuilder**: Validates content
- **Citation Verifier**: Verifies any new citations added
- **ICD/Synonym Enricher**: Updates codes if diagnoses change

## Change Log

**v1.0 (January 19, 2026)**
- Initial version
- Comment categorization framework
- Research and verification workflow
- Evidence-based recommendation system
- Auto-push after implementation
