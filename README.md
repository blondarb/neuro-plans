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
- **Request a Plan:** [Submit Issue](https://github.com/blondarb/neuro-plans/issues/new?template=plan_request.yml)

## Repository Structure

```
neuro-clinical-plans/
├── docs/                    # MkDocs source files
│   ├── index.md            # Home page
│   ├── plans/              # Clinical plan pages
│   ├── skills/             # AI skill documentation
│   └── references/         # Supporting references
├── plans/                   # Source plan files (canonical)
├── skills/                  # AI skill definitions
├── references/              # Reference materials
├── schemas/                 # JSON schemas (future)
├── scripts/                 # Build scripts
├── .github/
│   ├── ISSUE_TEMPLATE/     # Plan request form
│   └── workflows/          # GitHub Actions
└── mkdocs.yml              # MkDocs configuration
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

## License

[Add license information]

---

*Developed for teleneurohospitalist clinical decision support.*
