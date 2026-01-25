# Multi-Model Pipeline Design

> **Purpose:** Technical specification for orchestrating GPT-5.2, Claude Opus 4.5, and Gemini 3 Pro in a clinical plan generation pipeline. Includes API integration, error handling, and deployment architecture.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CLINICAL PLAN GENERATOR SYSTEM                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                         WEB INTERFACE (Vercel)                       │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │    │
│  │  │ Submit Form │  │ Status View │  │ Review Queue│                  │    │
│  │  │             │  │             │  │             │                  │    │
│  │  │ - Diagnosis │  │ - Progress  │  │ - Pending   │                  │    │
│  │  │ - Modifiers │  │ - Stage     │  │ - Flagged   │                  │    │
│  │  │ - Priority  │  │ - Errors    │  │ - Approved  │                  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                       API LAYER (Vercel Functions)                   │    │
│  │                                                                      │    │
│  │  POST /api/generate     - Start new plan generation                 │    │
│  │  GET  /api/status/:id   - Check generation status                   │    │
│  │  GET  /api/plans        - List all plans                            │    │
│  │  POST /api/approve/:id  - Physician approval                        │    │
│  │  POST /api/reject/:id   - Reject with feedback                      │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                    │                                         │
│                                    ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      ORCHESTRATION LAYER                             │    │
│  │                                                                      │    │
│  │  ┌──────────────────────────────────────────────────────────────┐   │    │
│  │  │                    JOB QUEUE (Supabase)                       │   │    │
│  │  │  • job_id, diagnosis, status, created_at, updated_at         │   │    │
│  │  │  • current_stage, stage_results, error_log                   │   │    │
│  │  └──────────────────────────────────────────────────────────────┘   │    │
│  │                                                                      │    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │    │
│  │  │  STAGE 1   │  │  STAGE 2A  │  │  STAGE 2B  │  │  STAGE 3   │    │    │
│  │  │  GPT-5.2   │→ │  Claude    │  │  Gemini    │→ │  Merge &   │    │    │
│  │  │  Generate  │  │  Clinical  │  │  Citation  │  │  Deploy    │    │    │
│  │  └────────────┘  └──────┬─────┘  └─────┬──────┘  └────────────┘    │    │
│  │                         │              │                             │    │
│  │                         └──────┬───────┘                             │    │
│  │                                │ (parallel)                          │    │
│  └────────────────────────────────┼─────────────────────────────────────┘    │
│                                   │                                          │
│                                   ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        DATA LAYER (Supabase)                         │    │
│  │                                                                      │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │    │
│  │  │    plans     │  │ verification │  │    audit     │              │    │
│  │  │              │  │   _reports   │  │    _log      │              │    │
│  │  │ • id         │  │              │  │              │              │    │
│  │  │ • diagnosis  │  │ • plan_id    │  │ • action     │              │    │
│  │  │ • content_md │  │ • clinical   │  │ • user_id    │              │    │
│  │  │ • content_json│ │ • citation   │  │ • timestamp  │              │    │
│  │  │ • status     │  │ • combined   │  │ • details    │              │    │
│  │  │ • version    │  │ • created_at │  │              │              │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘              │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                   │                                          │
│                                   ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    DEPLOYMENT (GitHub + MkDocs)                      │    │
│  │                                                                      │    │
│  │  Approved plans → GitHub commit → GitHub Pages rebuild → Live site  │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Database Schema (Supabase)

### Tables

```sql
-- Plans table
CREATE TABLE plans (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  diagnosis VARCHAR(255) NOT NULL,
  modifier VARCHAR(50), -- 'new-diagnosis', 'exacerbation', 'maintenance', 'refractory'
  slug VARCHAR(255) UNIQUE NOT NULL,

  -- Content
  content_md TEXT,
  content_json JSONB,

  -- Status
  status VARCHAR(50) DEFAULT 'pending', -- pending, generating, verifying, review, approved, rejected
  current_stage VARCHAR(50),

  -- Metadata
  version VARCHAR(10) DEFAULT '1.0',
  icd10 VARCHAR(20)[],
  setting_coverage JSONB, -- {"ED": true, "HOSP": true, "OPD": true, "ICU": false}

  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  approved_at TIMESTAMPTZ,
  approved_by VARCHAR(255),

  -- Scores
  quality_score INTEGER, -- 0-60
  verification_score JSONB -- {"clinical": 95, "citation": 88}
);

-- Generation jobs
CREATE TABLE generation_jobs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  plan_id UUID REFERENCES plans(id),

  -- Stage tracking
  stage VARCHAR(50) NOT NULL, -- 'generate', 'verify_clinical', 'verify_citation', 'merge', 'complete'
  status VARCHAR(50) DEFAULT 'pending', -- pending, running, completed, failed

  -- Model info
  model VARCHAR(100),
  input_tokens INTEGER,
  output_tokens INTEGER,
  cost_usd DECIMAL(10, 6),

  -- Results
  result JSONB,
  error_message TEXT,

  -- Timing
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  duration_ms INTEGER
);

-- Verification reports
CREATE TABLE verification_reports (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  plan_id UUID REFERENCES plans(id),

  -- Clinical verification
  clinical_status VARCHAR(50), -- passed, flagged, failed
  clinical_model VARCHAR(100),
  clinical_result JSONB,

  -- Citation verification
  citation_status VARCHAR(50),
  citation_model VARCHAR(100),
  citation_result JSONB,

  -- Combined
  overall_status VARCHAR(50),
  human_review_required BOOLEAN DEFAULT false,
  human_review_items TEXT[],
  auto_fixes_applied TEXT[],

  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Audit log
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  plan_id UUID REFERENCES plans(id),
  action VARCHAR(100) NOT NULL,
  user_id VARCHAR(255),
  details JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_plans_status ON plans(status);
CREATE INDEX idx_plans_slug ON plans(slug);
CREATE INDEX idx_jobs_plan_id ON generation_jobs(plan_id);
CREATE INDEX idx_jobs_status ON generation_jobs(status);
```

---

## API Endpoints

### POST /api/generate

Start a new plan generation job.

**Request:**
```json
{
  "diagnosis": "Guillain-Barré Syndrome",
  "modifier": "new-diagnosis",
  "priority": "normal",
  "options": {
    "skip_verification": false,
    "model_override": null
  }
}
```

**Response:**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "plan_id": "660e8400-e29b-41d4-a716-446655440001",
  "status": "queued",
  "estimated_time_seconds": 45,
  "stages": [
    {"stage": "generate", "status": "pending"},
    {"stage": "verify_clinical", "status": "pending"},
    {"stage": "verify_citation", "status": "pending"},
    {"stage": "merge", "status": "pending"}
  ]
}
```

### GET /api/status/:job_id

Check generation progress.

**Response:**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "plan_id": "660e8400-e29b-41d4-a716-446655440001",
  "status": "verifying",
  "current_stage": "verify_clinical",
  "progress_percent": 65,
  "stages": [
    {"stage": "generate", "status": "completed", "duration_ms": 12500, "cost_usd": 0.15},
    {"stage": "verify_clinical", "status": "running", "started_at": "2026-01-25T10:30:00Z"},
    {"stage": "verify_citation", "status": "running", "started_at": "2026-01-25T10:30:00Z"},
    {"stage": "merge", "status": "pending"}
  ],
  "estimated_remaining_seconds": 15
}
```

### GET /api/plans

List plans with filtering.

**Query params:** `?status=review&limit=10&offset=0`

**Response:**
```json
{
  "plans": [
    {
      "id": "660e8400-e29b-41d4-a716-446655440001",
      "diagnosis": "Guillain-Barré Syndrome",
      "slug": "guillain-barre-new-diagnosis",
      "status": "review",
      "quality_score": 54,
      "human_review_required": true,
      "human_review_items": ["Methylprednisolone dose verification"],
      "created_at": "2026-01-25T10:28:00Z"
    }
  ],
  "total": 1,
  "limit": 10,
  "offset": 0
}
```

### POST /api/approve/:plan_id

Physician approval.

**Request:**
```json
{
  "approved_by": "dr.smith@hospital.org",
  "comments": "Verified methylprednisolone dose - approved as is",
  "deploy_immediately": true
}
```

---

## Pipeline Implementation

### TypeScript/Node.js Example

```typescript
// lib/pipeline.ts

import { OpenAI } from 'openai';
import Anthropic from '@anthropic-ai/sdk';
import { GoogleGenerativeAI } from '@google/generative-ai';
import { createClient } from '@supabase/supabase-js';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const gemini = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!);

interface PipelineResult {
  plan: string;
  verification: VerificationReport;
  cost: number;
}

export async function generatePlan(
  diagnosis: string,
  modifier: string,
  planId: string
): Promise<PipelineResult> {

  let totalCost = 0;

  // Stage 1: Generate with GPT-5.2
  console.log('Stage 1: Generating plan with GPT-5.2...');
  const generateStart = Date.now();

  const generation = await openai.chat.completions.create({
    model: 'gpt-5.2',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: `Generate a clinical plan for: ${diagnosis} - ${modifier}` }
    ],
    max_tokens: 16000,
    temperature: 0.3
  });

  const plan = generation.choices[0].message.content!;
  const genCost = calculateCost('gpt-5.2', generation.usage!);
  totalCost += genCost;

  await logJob(planId, 'generate', 'completed', {
    model: 'gpt-5.2',
    input_tokens: generation.usage!.prompt_tokens,
    output_tokens: generation.usage!.completion_tokens,
    cost_usd: genCost,
    duration_ms: Date.now() - generateStart
  });

  // Stage 2A & 2B: Verification (parallel)
  console.log('Stage 2: Running verification in parallel...');

  const [clinicalResult, citationResult] = await Promise.all([
    verifyClinical(plan, planId),
    verifyCitation(plan, planId)
  ]);

  totalCost += clinicalResult.cost + citationResult.cost;

  // Stage 3: Merge and resolve
  console.log('Stage 3: Merging verification results...');

  const verification = mergeVerification(clinicalResult, citationResult);

  // Apply auto-fixes
  let finalPlan = plan;
  if (verification.auto_fixes.length > 0) {
    finalPlan = applyAutoFixes(plan, verification.auto_fixes);
  }

  // Save verification report
  await supabase.from('verification_reports').insert({
    plan_id: planId,
    clinical_status: clinicalResult.status,
    clinical_model: 'claude-opus-4.5',
    clinical_result: clinicalResult.result,
    citation_status: citationResult.status,
    citation_model: 'gemini-3-pro',
    citation_result: citationResult.result,
    overall_status: verification.overall_status,
    human_review_required: verification.human_review_required,
    human_review_items: verification.human_review_items,
    auto_fixes_applied: verification.auto_fixes
  });

  return {
    plan: finalPlan,
    verification,
    cost: totalCost
  };
}

async function verifyClinical(plan: string, planId: string) {
  const start = Date.now();

  const response = await anthropic.messages.create({
    model: 'claude-opus-4-5-20251101',
    max_tokens: 4000,
    system: CLINICAL_VERIFICATION_SYSTEM_PROMPT,
    messages: [
      { role: 'user', content: `Review this clinical plan:\n\n${plan}` }
    ]
  });

  const cost = calculateCost('claude-opus-4.5', {
    input_tokens: response.usage.input_tokens,
    output_tokens: response.usage.output_tokens
  });

  await logJob(planId, 'verify_clinical', 'completed', {
    model: 'claude-opus-4.5',
    input_tokens: response.usage.input_tokens,
    output_tokens: response.usage.output_tokens,
    cost_usd: cost,
    duration_ms: Date.now() - start
  });

  return {
    status: parseVerificationStatus(response.content[0].text),
    result: parseVerificationResult(response.content[0].text),
    cost
  };
}

async function verifyCitation(plan: string, planId: string) {
  const start = Date.now();
  const citations = extractCitations(plan);

  const model = gemini.getGenerativeModel({ model: 'gemini-3-pro' });
  const result = await model.generateContent({
    contents: [{ role: 'user', parts: [{ text: CITATION_VERIFICATION_PROMPT + '\n\n' + citations }] }],
    systemInstruction: CITATION_VERIFICATION_SYSTEM_PROMPT
  });

  const response = result.response;
  const cost = calculateCost('gemini-3-pro', {
    input_tokens: response.usageMetadata!.promptTokenCount,
    output_tokens: response.usageMetadata!.candidatesTokenCount
  });

  await logJob(planId, 'verify_citation', 'completed', {
    model: 'gemini-3-pro',
    input_tokens: response.usageMetadata!.promptTokenCount,
    output_tokens: response.usageMetadata!.candidatesTokenCount,
    cost_usd: cost,
    duration_ms: Date.now() - start
  });

  return {
    status: parseVerificationStatus(response.text()),
    result: parseCitationResult(response.text()),
    cost
  };
}

function calculateCost(model: string, usage: { input_tokens: number; output_tokens: number }): number {
  const pricing: Record<string, { input: number; output: number }> = {
    'gpt-5.2': { input: 1.75 / 1_000_000, output: 14 / 1_000_000 },
    'claude-opus-4.5': { input: 5 / 1_000_000, output: 25 / 1_000_000 },
    'gemini-3-pro': { input: 2 / 1_000_000, output: 12 / 1_000_000 }
  };

  const p = pricing[model];
  return (usage.input_tokens * p.input) + (usage.output_tokens * p.output);
}
```

---

## Error Handling & Retry Logic

### Retry Configuration

```typescript
const RETRY_CONFIG = {
  maxRetries: 4,
  baseDelayMs: 2000,
  maxDelayMs: 16000,
  retryableErrors: [
    'RATE_LIMIT_EXCEEDED',
    'SERVICE_UNAVAILABLE',
    'TIMEOUT',
    'NETWORK_ERROR'
  ]
};

async function withRetry<T>(
  fn: () => Promise<T>,
  stage: string
): Promise<T> {
  let lastError: Error;

  for (let attempt = 0; attempt <= RETRY_CONFIG.maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error: any) {
      lastError = error;

      if (!isRetryable(error) || attempt === RETRY_CONFIG.maxRetries) {
        throw error;
      }

      const delay = Math.min(
        RETRY_CONFIG.baseDelayMs * Math.pow(2, attempt),
        RETRY_CONFIG.maxDelayMs
      );

      console.log(`${stage}: Attempt ${attempt + 1} failed, retrying in ${delay}ms...`);
      await sleep(delay);
    }
  }

  throw lastError!;
}
```

### Fallback Models

```typescript
const MODEL_FALLBACKS = {
  generation: ['gpt-5.2', 'gpt-5.1', 'claude-sonnet-4.5'],
  clinical_verification: ['claude-opus-4.5', 'gpt-5.2', 'gemini-3-pro'],
  citation_verification: ['gemini-3-pro', 'claude-sonnet-4.5', 'gpt-5.1']
};

async function generateWithFallback(diagnosis: string): Promise<string> {
  for (const model of MODEL_FALLBACKS.generation) {
    try {
      return await generateWithModel(model, diagnosis);
    } catch (error) {
      console.log(`Model ${model} failed, trying next...`);
    }
  }
  throw new Error('All generation models failed');
}
```

---

## Deployment Flow

### Automatic Deployment (on approval)

```typescript
async function deployPlan(planId: string) {
  // 1. Fetch approved plan
  const { data: plan } = await supabase
    .from('plans')
    .select('*')
    .eq('id', planId)
    .single();

  // 2. Generate JSON from markdown
  const json = markdownToJson(plan.content_md);

  // 3. Update plans.json via GitHub API
  const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

  // Fetch current plans.json
  const { data: file } = await octokit.repos.getContent({
    owner: 'blondarb',
    repo: 'neuro-plans',
    path: 'docs/data/plans.json'
  });

  // Merge new plan
  const currentPlans = JSON.parse(Buffer.from(file.content, 'base64').toString());
  currentPlans[plan.diagnosis] = json;

  // Commit update
  await octokit.repos.createOrUpdateFileContents({
    owner: 'blondarb',
    repo: 'neuro-plans',
    path: 'docs/data/plans.json',
    message: `Add ${plan.diagnosis} plan`,
    content: Buffer.from(JSON.stringify(currentPlans, null, 2)).toString('base64'),
    sha: file.sha
  });

  // 4. Also save markdown file
  await octokit.repos.createOrUpdateFileContents({
    owner: 'blondarb',
    repo: 'neuro-plans',
    path: `docs/plans/${plan.slug}.md`,
    message: `Add ${plan.diagnosis} plan markdown`,
    content: Buffer.from(plan.content_md).toString('base64')
  });

  // 5. Update plan status
  await supabase
    .from('plans')
    .update({
      status: 'deployed',
      deployed_at: new Date().toISOString()
    })
    .eq('id', planId);

  // 6. Log audit
  await supabase.from('audit_log').insert({
    plan_id: planId,
    action: 'deployed',
    details: { github_commit: 'sha...' }
  });
}
```

---

## Environment Variables

```bash
# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...

# Supabase
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJ...
SUPABASE_SERVICE_KEY=eyJ...  # For server-side operations

# GitHub (for deployment)
GITHUB_TOKEN=ghp_...
GITHUB_REPO=blondarb/neuro-plans

# Optional
VERCEL_URL=https://your-app.vercel.app
LOG_LEVEL=info
```

---

## Monitoring & Alerts

### Key Metrics

| Metric | Alert Threshold |
|--------|-----------------|
| Generation success rate | < 95% |
| Verification pass rate | < 80% |
| Average generation time | > 60 seconds |
| API error rate | > 5% |
| Cost per plan | > $0.50 |

### Logging

```typescript
// Structured logging for observability
logger.info('plan.generated', {
  plan_id: planId,
  diagnosis,
  duration_ms: elapsed,
  tokens: { input: inputTokens, output: outputTokens },
  cost_usd: cost,
  quality_score: score
});
```

---

## Version

v1.0 - January 2026
