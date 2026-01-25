# Product Requirements Document (PRD)
## Clinical Plan Generator API

**Version:** 1.0
**Date:** January 25, 2026
**Author:** Generated for neuro-plans project

---

## Executive Summary

Build an automated clinical decision support plan generator that:
1. Accepts a neurological diagnosis as input
2. Generates a comprehensive, evidence-based treatment plan
3. Verifies accuracy using multiple AI models
4. Deploys approved plans to a clinical tool

**Cost:** ~$0.30 per plan (with full verification)
**Time:** ~45 seconds per plan generation

---

## Problem Statement

Currently, creating clinical decision support plans requires:
- Manual research and compilation (hours per plan)
- Expert review for accuracy
- Manual formatting for clinical tools
- No systematic verification process

**Goal:** Reduce plan creation time to minutes while maintaining or improving quality through multi-model verification.

---

## User Stories

### Primary Users

| User | Story | Acceptance Criteria |
|------|-------|---------------------|
| **Physician** | "I want to submit a diagnosis and receive a ready-to-use clinical plan" | Plan generated in <60 seconds, all 8 sections populated |
| **Physician** | "I want confidence that drug doses are accurate" | Independent verification by clinical AI |
| **Physician** | "I want to review and approve plans before they go live" | Review queue with flagged items highlighted |
| **Admin** | "I want to see cost and usage metrics" | Dashboard showing tokens, cost, success rate |

### Secondary Users

| User | Story | Acceptance Criteria |
|------|-------|---------------------|
| **Developer** | "I want to integrate plans into my app via API" | RESTful API with JSON responses |
| **Developer** | "I want real-time updates when plans change" | Supabase real-time subscriptions |

---

## Features

### MVP (Phase 1)

| Feature | Description | Priority |
|---------|-------------|----------|
| **Plan Generation** | Submit diagnosis, receive markdown plan | P0 |
| **Multi-Model Verification** | Clinical (Claude) + Citation (Gemini) verification | P0 |
| **Review Queue** | Web interface to review flagged plans | P0 |
| **Approval Workflow** | Physician approval before deployment | P0 |
| **Supabase Storage** | Plans stored in Supabase tables | P0 |

### Phase 2

| Feature | Description | Priority |
|---------|-------------|----------|
| **Batch Generation** | Generate multiple plans in parallel | P1 |
| **Custom Modifiers** | Support all diagnosis modifiers | P1 |
| **Version History** | Track plan versions and changes | P1 |
| **Usage Dashboard** | Cost, tokens, success metrics | P1 |

### Phase 3

| Feature | Description | Priority |
|---------|-------------|----------|
| **Plan Editor** | Web-based editing of generated plans | P2 |
| **Feedback Loop** | Physician corrections improve prompts | P2 |
| **Model A/B Testing** | Compare quality across models | P2 |
| **Auto-Update** | Regenerate plans when guidelines update | P2 |

---

## Technical Architecture

### Component Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         SYSTEM ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────────┐   │
│  │   VERCEL    │     │  SUPABASE   │     │    AI PROVIDERS     │   │
│  │             │     │             │     │                     │   │
│  │ • Next.js   │────▶│ • Database  │     │ • OpenAI (GPT-5.2)  │   │
│  │ • API Routes│     │ • Auth      │◀───▶│ • Anthropic (Claude)│   │
│  │ • UI        │     │ • Real-time │     │ • Google (Gemini)   │   │
│  │             │     │ • Storage   │     │                     │   │
│  └─────────────┘     └─────────────┘     └─────────────────────┘   │
│                              │                                       │
│                              ▼                                       │
│                      ┌─────────────┐                                │
│                      │   GITHUB    │                                │
│                      │             │                                │
│                      │ • Backup    │                                │
│                      │ • MkDocs    │                                │
│                      │ • Pages     │                                │
│                      └─────────────┘                                │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User Request → Vercel API → GPT-5.2 Generation →
    → Claude Clinical Verification (parallel)
    → Gemini Citation Verification (parallel)
→ Merge Results → Save to Supabase →
    → If no issues: Auto-deploy
    → If flagged: Queue for review
```

### API Specifications

See [PIPELINE_DESIGN.md](./PIPELINE_DESIGN.md) for full API documentation.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/generate` | POST | Start plan generation |
| `/api/status/:id` | GET | Check generation progress |
| `/api/plans` | GET | List all plans |
| `/api/plans/:slug` | GET | Get single plan |
| `/api/approve/:id` | POST | Approve plan |
| `/api/reject/:id` | POST | Reject with feedback |

---

## Multi-Model Strategy

### Why Multiple Models?

| Concern | Solution |
|---------|----------|
| Single point of failure | Fallback models if primary fails |
| Correlated errors | Different training = different mistakes |
| Cost optimization | Use cheaper models where quality sufficient |
| Specialization | Each model has different strengths |

### Model Assignment

| Task | Primary Model | Why | Fallback |
|------|---------------|-----|----------|
| Generation | GPT-5.2 | Best reasoning benchmarks, good value | GPT-5.1, Claude Sonnet |
| Clinical Verification | Claude Opus 4.5 | Best instruction-following, SWE-bench leader | GPT-5.2 |
| Citation Verification | Gemini 3 Pro | 1M context, good at factual lookup | Claude Sonnet |

### Cost Analysis

| Scenario | Cost/Plan | Monthly (20 plans) |
|----------|-----------|-------------------|
| Full verification (GPT + Claude + Gemini) | $0.30 | $6.00 |
| Reduced (GPT + Claude only) | $0.26 | $5.20 |
| Minimum (GPT only) | $0.15 | $3.00 |
| Current (Claude Code interactive) | ~$0.50-1.00 | ~$10-20 |

---

## Quality Assurance

### Verification Checks

**Clinical Verification (Claude):**
- [ ] Drug doses within standard ranges
- [ ] Contraindications complete
- [ ] Drug interactions noted
- [ ] Monitoring appropriate
- [ ] Clinical logic sound

**Citation Verification (Gemini):**
- [ ] Each citation exists in PubMed/source
- [ ] Author names correct
- [ ] Year correct
- [ ] Journal/source correct
- [ ] Content supports claim

### Quality Gates

| Gate | Criteria | Action if Failed |
|------|----------|------------------|
| Structure | All 8 sections present | Auto-fix or regenerate |
| Formatting | Medication format correct | Auto-fix |
| Clinical Safety | No critical errors | Block, require human review |
| Citations | >80% verified | Flag for review |

### Human Review Required

These issues ALWAYS require physician review:
- Drug dose outside standard range
- Missing critical contraindication
- Citation not found (may know correct source)
- Conflicting recommendations

---

## Security & Compliance

### Data Handling

| Data Type | Storage | Encryption | Retention |
|-----------|---------|------------|-----------|
| Plan content | Supabase | At rest (AES-256) | Indefinite |
| API keys | Vercel env vars | In transit (TLS) | N/A |
| Audit logs | Supabase | At rest | 1 year |
| Generated prompts | Not stored | In transit only | None |

### Access Control

| Role | Permissions |
|------|-------------|
| Public | Read deployed plans |
| Authenticated | Read all plans, view review queue |
| Physician | Approve/reject plans |
| Admin | All permissions, API key management |

### Compliance Notes

- Plans are **decision support**, not medical advice
- Physician review required before deployment
- Audit trail maintained for all changes
- No PHI stored (plans are generic templates)

---

## Success Metrics

### KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Generation success rate | >95% | Jobs completed / jobs started |
| Verification pass rate | >80% | Plans passing without flags / total |
| Time to generation | <60 seconds | Job start to completion |
| Cost per plan | <$0.35 | API costs tracked per job |
| Physician approval rate | >90% | Approved / (approved + rejected) |

### Monitoring

```
Dashboard displays:
- Plans generated (daily/weekly/monthly)
- Average cost per plan
- Verification pass rate trend
- Most common flag reasons
- Model usage breakdown
```

---

## Implementation Roadmap

### Phase 1: MVP (2-3 weeks)

| Week | Tasks |
|------|-------|
| 1 | Supabase schema setup, API routes scaffolding |
| 1 | GPT-5.2 generation integration |
| 2 | Claude verification integration |
| 2 | Gemini citation verification |
| 3 | Review queue UI |
| 3 | Approval workflow, deployment |

### Phase 2: Polish (2 weeks)

| Week | Tasks |
|------|-------|
| 4 | Error handling, retry logic |
| 4 | Usage dashboard |
| 5 | Batch generation |
| 5 | Version history |

### Phase 3: Optimization (ongoing)

- Feedback loop from physician corrections
- Model performance comparison
- Prompt optimization based on failures

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| API rate limits | Medium | Medium | Implement queuing, backoff |
| Model hallucination | Medium | High | Multi-model verification |
| Incorrect drug dose | Low | Critical | Claude verification + human review |
| API cost overrun | Low | Low | Budget alerts, usage caps |
| Citation not verifiable | Medium | Low | Flag for physician, allow plain text |

---

## Dependencies

### External Services

| Service | Purpose | Required |
|---------|---------|----------|
| OpenAI API | GPT-5.2 generation | Yes |
| Anthropic API | Claude verification | Yes (for full verification) |
| Google AI API | Gemini citation check | Yes (for full verification) |
| Supabase | Database, auth, real-time | Yes |
| Vercel | Hosting, serverless functions | Yes |
| GitHub | Version control, backup | Optional |

### Environment Variables

```bash
# Required
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_SERVICE_KEY=

# Optional
GITHUB_TOKEN=
VERCEL_URL=
```

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) | GPT-5.2 generation prompt |
| [VERIFICATION_PROMPTS.md](./VERIFICATION_PROMPTS.md) | Claude/Gemini verification prompts |
| [PIPELINE_DESIGN.md](./PIPELINE_DESIGN.md) | Technical implementation details |
| [SUPABASE_SYNC.md](./SUPABASE_SYNC.md) | Database schema and sync strategy |

---

## Appendix: Comparison with Current Workflow

| Aspect | Current (Claude Code) | New (API Pipeline) |
|--------|----------------------|-------------------|
| Cost | ~$20/month flat | ~$0.30/plan |
| Speed | 10-30 min interactive | ~45 seconds |
| Verification | Same model self-check | Independent multi-model |
| Human involvement | Throughout | Review only flagged items |
| Scalability | 1 at a time | Parallel batch |
| Customization | High (interactive) | Template-based |
| Error handling | Manual iteration | Automated retry + fallback |

**Recommendation:** Use API pipeline for standard plans, keep Claude Code for complex edge cases or when heavy customization needed.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-25 | Initial PRD |
