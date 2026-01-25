# API Specification Package

> **Purpose:** Complete specification for building an automated clinical plan generator using Claude Opus 4.5 (generation + verification) and Gemini 3 Pro (citations).
>
> **⚠️ HEALTHCARE SAFETY CONFIGURATION:** This pipeline prioritizes patient safety over cost. All plans require mandatory physician review.

---

## Quick Start

This package contains everything needed to build a multi-model clinical plan generation pipeline:

| Document | What It Contains |
|----------|------------------|
| [PRD.md](./PRD.md) | Product requirements, roadmap, success metrics |
| [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) | GPT-5.2 generation prompt (copy-paste ready) |
| [VERIFICATION_PROMPTS.md](./VERIFICATION_PROMPTS.md) | Claude + Gemini verification prompts |
| [PIPELINE_DESIGN.md](./PIPELINE_DESIGN.md) | API implementation, database schema, code examples |
| [SUPABASE_SYNC.md](./SUPABASE_SYNC.md) | How to sync plans to your Supabase/Vercel app |

---

## Architecture Summary (Safety-First)

```
User submits diagnosis
        │
        ▼
┌───────────────────────┐
│  Claude Opus 4.5      │  Stage 1: Generate plan (~$0.40)
│  (Safest LLM)         │  - Lowest hallucination rate
└─────────┬─────────────┘  - Refuses when uncertain
          │
    ┌─────┴─────┐
    │           │
    ▼           ▼
┌────────────┐ ┌────────┐
│ Claude     │ │ Gemini │  Stage 2: Verify (~$0.19 total)
│ Opus 4.5   │ │ 3 Pro  │  - High-alert med detection
│ Clinical   │ │Citation│  - Citation verification
└────┬───────┘ └───┬────┘
     │             │
     └──────┬──────┘
            │
            ▼
┌─────────────────────────┐
│  🏥 MANDATORY REVIEW    │  Stage 3: ALL plans require
│  (Physician Required)   │  physician approval
└─────────────────────────┘
            │
            ▼
    Supabase + GitHub
```

---

## Cost Per Plan (Safety-First Configuration)

| Model | Role | Cost |
|-------|------|------|
| Claude Opus 4.5 | Generation (safest) | ~$0.40 |
| Claude Opus 4.5 | Clinical verification | ~$0.15 |
| Gemini 3 Pro | Citation verification | ~$0.04 |
| **Total** | | **~$0.59** |

> **Why Claude Opus 4.5?** Lowest hallucination rate among frontier models. For healthcare, safety > cost.

---

## Implementation Checklist

### Phase 1: Setup
- [ ] Create Supabase project
- [ ] Set up Vercel project
- [ ] Configure environment variables
- [ ] Create database tables (see PIPELINE_DESIGN.md)

### Phase 2: Core Pipeline
- [ ] Implement `/api/generate` endpoint
- [ ] Integrate GPT-5.2 generation
- [ ] Integrate Claude verification
- [ ] Integrate Gemini citation check
- [ ] Implement job status tracking

### Phase 3: UI
- [ ] Build submission form
- [ ] Build status/progress view
- [ ] Build review queue
- [ ] Build approval workflow

### Phase 4: Deployment
- [ ] Connect to GitHub for backups
- [ ] Set up real-time sync
- [ ] Configure monitoring/alerts

---

## API Keys Required

| Provider | Key Name | Get It From |
|----------|----------|-------------|
| Anthropic | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) |
| Google | `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) |
| Supabase | `SUPABASE_URL`, `SUPABASE_KEY` | Your Supabase project settings |

> **Note:** OpenAI API key is NOT required. We use Claude Opus 4.5 for both generation and clinical verification (safety-first approach).

---

## Questions?

This spec was generated as part of the neuro-plans project. The prompts are designed to match the quality of plans created with Claude Code's interactive workflow.

For the original skills files (more detailed), see:
- `/skills/neuro-builder-SKILL.md`
- `/skills/neuro-checker-SKILL.md`
- `/docs/skills/neuro-citation-verifier-skill.md`
