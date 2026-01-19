# Neuro Clinical Plans

Evidence-based clinical decision support templates for neurological diagnoses.

## Overview

This repository contains structured clinical recommendation templates for neurologists and hospitalists. Each plan covers:

- Laboratory workup (core, extended, specialized)
- Diagnostic imaging and studies
- Treatment protocols (acute, maintenance, disease-modifying)
- Monitoring parameters
- Disposition criteria

Plans are organized by care setting (ED, Hospital, Outpatient, ICU) with priority levels (STAT, URGENT, ROUTINE).

## Quick Links

- **Website:** https://blondarb.github.io/neuro-plans/
- **Clinical Plan Builder:** https://blondarb.github.io/neuro-plans/clinical/
- **Request a Plan:** [Submit Issue](https://github.com/blondarb/neuro-plans/issues/new?template=plan_request.yml)

## Features

### Clinical Plan Builder (Interactive Tool)

An interactive web-based tool for building customized clinical plans:

- **Filter by Setting** - ED, Hospital, Outpatient, ICU
- **Filter by Priority** - STAT, URGENT, ROUTINE
- **Progressive Disclosure** - Essential info visible; details on hover via icons:
  - ℹ️ Rationale (blue) - Clinical reasoning and evidence basis
  - ⏱ Timing (amber) - When to perform/administer
  - 🎯 Target (green) - Expected findings or goals
  - ⚠️ Contraindications (red, pulsing) - Safety warnings
  - 📊 Monitoring (purple) - Required monitoring parameters
- **Selected Items Sidebar** - Build and export custom plans
- **Editable Items** - Click to customize text
- **Clinical Notes Banner** - Plan-level notes in collapsible section

### Review Mode (Comment System)

- Section-specific comments with Firebase backend
- TOC badges showing comment counts
- Physician review workflow for draft → approved status

### AI-Powered Skills Pipeline

Five skills for generating and validating plans:
1. **Builder** - Generates comprehensive plans from diagnosis
2. **Checker** - Validates against 6 quality domains (target 90%+)
3. **Rebuilder** - Applies corrections from checker
4. **Citation Verifier** - Validates medical references
5. **ICD/Synonym Enricher** - Adds billing codes and synonyms

## Repository Structure

```
neuro-clinical-plans/
├── docs/
│   ├── index.md                # Home page
│   ├── clinical/
│   │   └── index.html          # Clinical Plan Builder (interactive tool)
│   ├── data/
│   │   └── plans.json          # JSON data for Clinical Tool
│   ├── plans/                  # Approved clinical plan pages
│   ├── drafts/                 # Plans pending review
│   ├── skills/                 # AI skill documentation (public)
│   ├── references/             # Supporting references
│   └── assets/css/custom.css   # Custom styling
├── skills/                     # AI skill definitions (source)
│   ├── neuro-builder-SKILL.md
│   ├── neuro-checker-SKILL.md
│   ├── neuro-rebuilder-SKILL.md
│   ├── neuro-citation-verifier-SKILL.md
│   ├── neuro-cpt-synonym-enricher-SKILL.md
│   └── neuro-comment-review-SKILL.md
├── references/                 # Reference materials
├── scripts/                    # Build scripts
└── mkdocs.yml                  # MkDocs configuration
```

## Workflow

### Requesting a New Plan

1. Go to [Issues](https://github.com/blondarb/neuro-plans/issues/new?template=plan_request.yml)
2. Fill out the plan request form
3. Submit for triage

### Creating Plans

1. **Build** - Use `neuro-builder-SKILL.md` to generate a draft
2. **Check** - Use `neuro-checker-SKILL.md` to validate (target 90%+)
3. **Review** - Physician reviews recommendations
4. **Rebuild** - Use `neuro-rebuilder-SKILL.md` to apply approved changes
5. **Publish** - Merge to main to deploy

### Adding/Editing Plans

1. Create or edit a `.md` file in `docs/plans/`
2. Include YAML frontmatter:
   ```yaml
   ---
   title: "Diagnosis Name"
   description: "Brief description"
   version: "1.0"
   setting: "ED, HOSP, OPD, ICU"
   tags:
     - category
     - subcategory
   ---
   ```
3. Follow the 8-section structure (see Style Guide)
4. Push to main to auto-deploy

## Local Development

### Prerequisites

- Python 3.x
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/blondarb/neuro-plans.git
cd neuro-clinical-plans

# Install dependencies
pip install mkdocs-material pyyaml

# Run local server
mkdocs serve
```

Visit `http://localhost:8000` to preview.

### Building

```bash
# Run build script
python scripts/build.py

# Build static site
mkdocs build
```

Output goes to `site/` directory.

## Current Status

| Metric | Count |
|--------|-------|
| Completed Plans | 4 |
| Planned | 130 |

See [Template Tracker](docs/references/tracker.md) for full roadmap.

## Quality Standards

- All plans require **90%+ validation score** across 6 domains
- Physician review required before clinical use
- Plans updated when new guidelines published

## Contributing

1. Check the [Template Tracker](docs/references/tracker.md) for needed plans
2. Submit a plan request or claim an existing issue
3. Follow the [Style Guide](docs/skills/style-guide.md)
4. Submit a PR for review

## Disclaimer

These templates are decision support tools, not clinical guidelines. They require physician review and adaptation to individual patient circumstances. Always apply clinical judgment.

## Changelog

### January 2026

**Clinical Plan Builder Enhancements**
- Progressive disclosure UI with icon-based tooltips (v1.5)
- Icon types: rationale (ℹ️), timing (⏱), target (🎯), contraindications (⚠️), monitoring (📊)
- Collapsible clinical notes banner for plan-level notes
- Click-to-edit functionality for selected items
- Dosing shown in selected items sidebar
- Custom item creation capability

**JSON Schema Documentation**
- Added Clinical Tool JSON Schema to Builder skill
- Documents all fields that display as icons
- Safety-critical field guidance for medications

**Data Updates**
- Status Epilepticus v1.5: Added timing, target, contraindications, monitoring fields
- Full metadata for imaging, first-line benzodiazepines, second-line ASMs, anesthetics

**Skills Pipeline**
- Added Comment Review skill for processing website feedback
- Auto-push workflow for drafts after pipeline completion

**Comment System**
- Section-specific inline comments with Firebase
- TOC badges showing comment counts per section
- Draft/approved status workflow

## License

[Add license information]

---

*Developed for teleneurohospitalist clinical decision support.*
