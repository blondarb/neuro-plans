# API Specification Package

> **Purpose:** Complete specification for building an automated clinical plan generator using GPT-5.2, Claude Opus 4.5, and Gemini 3 Pro.

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

## Architecture Summary

```
User submits diagnosis
        │
        ▼
┌───────────────────┐
│  GPT-5.2          │  Stage 1: Generate plan (~$0.15)
│  Generation       │
└─────────┬─────────┘
          │
    ┌─────┴─────┐
    │           │
    ▼           ▼
┌────────┐ ┌────────┐
│ Claude │ │ Gemini │  Stage 2: Verify (parallel, ~$0.15 total)
│Clinical│ │Citation│
└────┬───┘ └───┬────┘
     │         │
     └────┬────┘
          │
          ▼
┌───────────────────┐
│  Merge & Deploy   │  Stage 3: Auto-fix or flag for review
└───────────────────┘
          │
          ▼
    Supabase + GitHub
```

---

## Cost Per Plan

| Model | Role | Cost |
|-------|------|------|
| GPT-5.2 | Generation | $0.15 |
| Claude Opus 4.5 | Clinical verification | $0.11 |
| Gemini 3 Pro | Citation verification | $0.04 |
| **Total** | | **$0.30** |

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
| OpenAI | `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com) |
| Anthropic | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) |
| Google | `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) |
| Supabase | `SUPABASE_URL`, `SUPABASE_KEY` | Your Supabase project settings |

---

## Questions?

This spec was generated as part of the neuro-plans project. The prompts are designed to match the quality of plans created with Claude Code's interactive workflow.

For the original skills files (more detailed), see:
- `/skills/neuro-builder-SKILL.md`
- `/skills/neuro-checker-SKILL.md`
- `/docs/skills/neuro-citation-verifier-skill.md`
