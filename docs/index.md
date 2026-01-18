---
title: Home
---

# Neuro Clinical Plans

Evidence-based clinical decision support templates for neurological diagnoses.

## What This Is

A library of structured clinical recommendations for neurologists and hospitalists, covering:

- **Laboratory workup** - Essential and extended testing
- **Imaging studies** - When and what to order
- **Treatment protocols** - Acute, maintenance, and disease-modifying therapies
- **Monitoring parameters** - What to track and when
- **Disposition criteria** - Admission, discharge, and follow-up guidance

Each plan is organized by care setting (ED, Hospital, Outpatient, ICU) with priority levels (STAT, URGENT, ROUTINE).

## Quick Links

<div class="grid cards" markdown>

- :material-file-document-multiple: **[Browse Plans](plans/index.md)**

    View all available clinical decision support templates

- :material-plus-circle: **[Request a Plan](https://github.com/blondarb/neuro-plans/issues/new?template=plan_request.yml)**

    Submit a request for a new diagnosis template

- :material-github: **[View on GitHub](https://github.com/blondarb/neuro-plans)**

    Access the source repository

</div>

## How Plans Are Created

1. **Request** - Submit a plan request via GitHub Issues
2. **Build** - AI-assisted draft generation using the [Builder Skill](skills/neuro-builder-skill.md)
3. **Validate** - Quality scoring using the [Checker Skill](skills/neuro-checker-skill.md)
4. **Review** - Physician review and approval
5. **Publish** - Validated plans added to the library

All plans target **90%+ validation score** across six domains: completeness, accuracy, safety, objectivity, setting appropriateness, and usability.

## Current Status

| Metric | Count |
|--------|-------|
| Completed Plans | 4 |
| In Development | 0 |
| Planned | 130 |

See the [Template Tracker](references/tracker.md) for the full roadmap.

## Disclaimer

!!! warning "Clinical Use Notice"

    These templates are decision support tools, not clinical guidelines. They require physician review and adaptation to individual patient circumstances. Always apply clinical judgment.

---

*Developed for teleneurohospitalist clinical decision support.*
