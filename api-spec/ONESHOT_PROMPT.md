# CLAUDE CODE ONE-SHOT PROMPT
## Clinical Plan Generator - Full Stack Build

Copy everything below the line and paste it into Claude Code in a new empty directory.

---

# BUILD REQUEST: Clinical Plan Generator

Build a complete full-stack application for generating clinical decision support plans using a multi-model AI pipeline. This will be a Next.js app deployed on Vercel with Supabase as the backend.

## PROJECT OVERVIEW

**What it does:**
1. User submits a neurological diagnosis (e.g., "Guillain-Barré Syndrome - New Diagnosis")
2. GPT-5.2 generates a comprehensive clinical plan
3. Claude Opus 4.5 verifies clinical accuracy (drug doses, contraindications)
4. Gemini 3 Pro verifies citations (PubMed lookup)
5. Results saved to Supabase
6. Physician reviews and approves via web UI
7. Approved plans available via API for other apps to consume

**Tech Stack:**
- Next.js 14+ (App Router)
- TypeScript
- Tailwind CSS
- Supabase (database, auth, real-time)
- Vercel (hosting)
- OpenAI API (GPT-5.2)
- Anthropic API (Claude Opus 4.5)
- Google AI API (Gemini 3 Pro)

## STEP 1: PROJECT SETUP

Create a new Next.js project with these specifications:

```bash
npx create-next-app@latest clinical-plan-generator --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
cd clinical-plan-generator
npm install @supabase/supabase-js @supabase/ssr openai @anthropic-ai/sdk @google/generative-ai lucide-react
```

## STEP 2: ENVIRONMENT VARIABLES

Create `.env.local` with placeholders (I will fill in):

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# AI Providers
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GEMINI_API_KEY=your_gemini_key

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

Also create `.env.example` with the same structure but empty values for documentation.

## STEP 3: SUPABASE DATABASE SCHEMA

Create a file `supabase/schema.sql` with the complete database schema:

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Plans table
CREATE TABLE plans (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- Identity
  diagnosis VARCHAR(255) NOT NULL,
  modifier VARCHAR(50), -- 'new-diagnosis', 'exacerbation', 'maintenance', 'refractory'
  slug VARCHAR(255) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,

  -- Content
  content_md TEXT,
  content_json JSONB,

  -- Status: draft, generating, verifying, review, approved, rejected
  status VARCHAR(50) DEFAULT 'draft',
  current_stage VARCHAR(50),

  -- Metadata
  version VARCHAR(10) DEFAULT '1.0',
  icd10 VARCHAR(20)[],
  setting_coverage JSONB DEFAULT '{"ED": true, "HOSP": true, "OPD": true, "ICU": false}',

  -- Quality
  quality_score INTEGER,

  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  approved_at TIMESTAMPTZ,
  approved_by VARCHAR(255)
);

-- Generation jobs table
CREATE TABLE generation_jobs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  plan_id UUID REFERENCES plans(id) ON DELETE CASCADE,

  -- Stage: generate, verify_clinical, verify_citation, merge, complete
  stage VARCHAR(50) NOT NULL,
  -- Status: pending, running, completed, failed
  status VARCHAR(50) DEFAULT 'pending',

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
  duration_ms INTEGER,

  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Verification reports
CREATE TABLE verification_reports (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  plan_id UUID REFERENCES plans(id) ON DELETE CASCADE,

  -- Clinical verification (Claude)
  clinical_status VARCHAR(50),
  clinical_model VARCHAR(100),
  clinical_result JSONB,

  -- Citation verification (Gemini)
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
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  plan_id UUID REFERENCES plans(id) ON DELETE SET NULL,
  action VARCHAR(100) NOT NULL,
  user_id VARCHAR(255),
  details JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_plans_status ON plans(status);
CREATE INDEX idx_plans_slug ON plans(slug);
CREATE INDEX idx_plans_created ON plans(created_at DESC);
CREATE INDEX idx_jobs_plan_id ON generation_jobs(plan_id);
CREATE INDEX idx_jobs_status ON generation_jobs(status);

-- Updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER plans_updated_at
  BEFORE UPDATE ON plans
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- Row Level Security
ALTER TABLE plans ENABLE ROW LEVEL SECURITY;
ALTER TABLE generation_jobs ENABLE ROW LEVEL SECURITY;
ALTER TABLE verification_reports ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;

-- Public read for approved plans
CREATE POLICY "Public read approved plans" ON plans
  FOR SELECT USING (status = 'approved');

-- Service role full access (for API routes)
CREATE POLICY "Service role full access plans" ON plans
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access jobs" ON generation_jobs
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access reports" ON verification_reports
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access audit" ON audit_log
  FOR ALL TO service_role USING (true);
```

**IMPORTANT: Tell me to run this SQL in the Supabase SQL Editor after creating the project.**

## STEP 4: PROJECT STRUCTURE

Create this file structure:

```
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx                    # Home/dashboard
│   ├── generate/
│   │   └── page.tsx                # Plan generation form
│   ├── plans/
│   │   ├── page.tsx                # List all plans
│   │   └── [slug]/
│   │       └── page.tsx            # Single plan view
│   ├── review/
│   │   └── page.tsx                # Review queue for approval
│   └── api/
│       ├── generate/
│       │   └── route.ts            # POST - start generation
│       ├── status/
│       │   └── [jobId]/
│       │       └── route.ts        # GET - check job status
│       ├── plans/
│       │   ├── route.ts            # GET - list plans
│       │   └── [slug]/
│       │       └── route.ts        # GET - single plan
│       ├── approve/
│       │   └── [planId]/
│       │       └── route.ts        # POST - approve plan
│       └── reject/
│           └── [planId]/
│               └── route.ts        # POST - reject plan
├── components/
│   ├── ui/
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   ├── Select.tsx
│   │   ├── Badge.tsx
│   │   ├── Progress.tsx
│   │   └── Spinner.tsx
│   ├── GenerationForm.tsx
│   ├── PlanCard.tsx
│   ├── PlanViewer.tsx
│   ├── ReviewQueue.tsx
│   ├── StatusTracker.tsx
│   └── Navigation.tsx
├── lib/
│   ├── supabase/
│   │   ├── client.ts               # Browser client
│   │   └── server.ts               # Server client
│   ├── ai/
│   │   ├── openai.ts               # GPT-5.2 generation
│   │   ├── anthropic.ts            # Claude verification
│   │   ├── gemini.ts               # Gemini citation check
│   │   └── prompts.ts              # All system prompts
│   ├── pipeline/
│   │   ├── generate.ts             # Main pipeline orchestrator
│   │   ├── verify-clinical.ts
│   │   ├── verify-citation.ts
│   │   └── merge.ts
│   ├── utils/
│   │   ├── costs.ts                # Token cost calculations
│   │   ├── slug.ts                 # Slug generation
│   │   └── markdown.ts             # MD parsing utilities
│   └── types.ts                    # TypeScript types
└── styles/
    └── globals.css
```

## STEP 5: AI PROMPTS

Create `src/lib/ai/prompts.ts` with these prompts:

### GPT-5.2 SYSTEM PROMPT (for generation)

```typescript
export const GENERATION_SYSTEM_PROMPT = `You are a clinical decision support generator specializing in neurology. You create comprehensive, evidence-based treatment plans that can be used by physicians in Emergency Departments, Hospitals, Outpatient Clinics, and ICUs.

Your output must be:
1. Accurate - Drug dosing, diagnostic criteria, and clinical claims must be factually correct
2. Complete - All 8 sections populated with appropriate setting coverage
3. Safe - Critical contraindications, monitoring requirements, and red flags included
4. Actionable - Written as physician-ready directives, not suggestions

## OUTPUT FORMAT

Generate plans using this exact markdown structure:

---
title: [Diagnosis Name]
version: 1.0
status: draft
icd10: [Primary ICD-10 code]
last_updated: [YYYY-MM-DD]
---

# [Diagnosis Name]

**ICD-10:** [Code(s)]
**SCOPE:** [Brief statement of what this template covers and excludes]

**PRIORITY KEY:** STAT = Immediate | URGENT = Within hours | ROUTINE = Standard | EXT = Extended/atypical | - = Not applicable

---

## 1. LABORATORY WORKUP

### 1A. Essential/Core Labs

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|

### 1B. Extended Workup

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

### 3B. Symptomatic Treatments

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

### 3C. Second-line/Refractory

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

---

## 4. OTHER RECOMMENDATIONS

### 4A. Referrals & Consults

| Recommendation | ED | HOSP | OPD | ICU | Indication |
|----------------|:--:|:----:|:---:|:---:|------------|

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|

---

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | [criteria] |
| Admit to floor | [criteria] |
| Admit to ICU | [criteria] |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|

## CRITICAL REQUIREMENTS

### Medication Format
EVERY medication must be on its own row. Never group drugs.
Use structured dosing: [dose] :: [route] :: [frequency] :: [full instructions]

Example: 5 mg :: PO :: TID :: Start 5 mg TID; titrate by 5 mg/dose q3d; max 80 mg/day

### Setting Coverage
Evaluate every item for ALL settings (ED, HOSP, OPD, ICU).
Use "-" only when truly not applicable.

### Priority Values
STAT = Minutes | URGENT = Hours | ROUTINE = Days | EXT = Weeks | - = N/A`;

export const GENERATION_USER_PROMPT = (diagnosis: string, modifier: string) =>
  \`Generate a comprehensive clinical decision support plan for: \${diagnosis} - \${modifier}

Focus on evidence-based recommendations with complete medication dosing, contraindications, and monitoring requirements.\`;
```

### CLAUDE VERIFICATION PROMPT (for clinical check)

```typescript
export const CLINICAL_VERIFICATION_SYSTEM_PROMPT = `You are a clinical pharmacist and neurologist reviewing a clinical decision support plan for accuracy and safety.

Your task is to verify:
1. Medication dosing is within standard therapeutic ranges
2. All critical contraindications are listed
3. Drug-drug interactions are noted where relevant
4. Monitoring requirements are appropriate
5. Clinical recommendations are evidence-based

OUTPUT FORMAT:
For each medication, output ONE line:
✅ OK: [Drug name] - dosing and safety info verified
⚠️ FLAG: [Drug name] - [specific concern requiring physician review]
❌ ERROR: [Drug name] - [critical safety issue that must be fixed]

At the end, provide a JSON block:

\`\`\`json
{
  "status": "passed" | "flagged" | "failed",
  "medications_reviewed": number,
  "ok_count": number,
  "flagged_count": number,
  "error_count": number,
  "errors": [
    {
      "medication": "string",
      "issue": "string",
      "current": "string",
      "recommended": "string",
      "severity": "critical" | "high" | "medium"
    }
  ],
  "flags": [
    {
      "medication": "string",
      "issue": "string",
      "severity": "medium" | "low"
    }
  ],
  "suggested_additions": ["string"]
}
\`\`\``;

export const CLINICAL_VERIFICATION_USER_PROMPT = (plan: string) =>
  \`Review this clinical plan for safety and accuracy.

Focus on:
1. Are drug doses within standard therapeutic ranges?
2. Are contraindications complete for each medication?
3. Are there missing drug-drug interactions?
4. Is monitoring appropriate for each medication?

CLINICAL PLAN:
---
\${plan}
---

Provide your verification report with the JSON summary at the end.\`;
```

### GEMINI VERIFICATION PROMPT (for citations)

```typescript
export const CITATION_VERIFICATION_SYSTEM_PROMPT = `You are a medical librarian verifying citations in a clinical document.

For each citation in Section 8 (Evidence & References):
1. Search for the article/guideline
2. Verify it exists
3. Confirm authors, year, and journal match
4. Return the PubMed ID (PMID) if found

OUTPUT FORMAT for each citation:
✅ VERIFIED: [Citation] → PMID: [number]
⚠️ PARTIAL: [Citation] → Found similar: [details] | Correction: [correction]
❌ NOT FOUND: [Citation] → Searched: [terms] | Action: [remove/replace/flag]
❓ UNABLE: [Citation] → Reason: [paywall/non-indexed]

IMPORTANT:
- NEVER guess or fabricate a PMID
- If uncertain, mark as UNABLE TO VERIFY

End with a JSON block:

\`\`\`json
{
  "status": "passed" | "flagged" | "failed",
  "total_citations": number,
  "verified_count": number,
  "partial_count": number,
  "not_found_count": number,
  "unable_count": number,
  "corrections": [
    {
      "original": "string",
      "corrected": "string",
      "pmid": "string",
      "auto_fixable": boolean
    }
  ],
  "pmids_to_add": [
    {
      "citation": "string",
      "pmid": "string",
      "link": "string"
    }
  ]
}
\`\`\``;

export const CITATION_VERIFICATION_USER_PROMPT = (plan: string) =>
  \`Verify the citations in Section 8 (Evidence & References) of this clinical plan.

For each citation:
1. Search PubMed for the article
2. Verify authors, year, journal
3. Return PMID if found

CLINICAL PLAN:
---
\${plan}
---

Provide your verification report with the JSON summary at the end.\`;
```

## STEP 6: CORE IMPLEMENTATION

### Supabase Clients

Create `src/lib/supabase/client.ts`:
```typescript
import { createBrowserClient } from '@supabase/ssr'

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

Create `src/lib/supabase/server.ts`:
```typescript
import { createClient } from '@supabase/supabase-js'

export function createServiceClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { persistSession: false } }
  )
}
```

### AI Clients

Create `src/lib/ai/openai.ts`:
```typescript
import OpenAI from 'openai'
import { GENERATION_SYSTEM_PROMPT, GENERATION_USER_PROMPT } from './prompts'

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY })

export async function generatePlan(diagnosis: string, modifier: string) {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o', // Use gpt-4o for now, upgrade to gpt-5.2 when available
    messages: [
      { role: 'system', content: GENERATION_SYSTEM_PROMPT },
      { role: 'user', content: GENERATION_USER_PROMPT(diagnosis, modifier) }
    ],
    max_tokens: 16000,
    temperature: 0.3
  })

  return {
    content: response.choices[0].message.content!,
    usage: response.usage!
  }
}
```

Create `src/lib/ai/anthropic.ts`:
```typescript
import Anthropic from '@anthropic-ai/sdk'
import { CLINICAL_VERIFICATION_SYSTEM_PROMPT, CLINICAL_VERIFICATION_USER_PROMPT } from './prompts'

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY })

export async function verifyClinical(plan: string) {
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514', // Or claude-opus-4-5-20251101 for highest quality
    max_tokens: 4000,
    system: CLINICAL_VERIFICATION_SYSTEM_PROMPT,
    messages: [
      { role: 'user', content: CLINICAL_VERIFICATION_USER_PROMPT(plan) }
    ]
  })

  const text = response.content[0].type === 'text' ? response.content[0].text : ''

  return {
    content: text,
    usage: response.usage
  }
}
```

Create `src/lib/ai/gemini.ts`:
```typescript
import { GoogleGenerativeAI } from '@google/generative-ai'
import { CITATION_VERIFICATION_SYSTEM_PROMPT, CITATION_VERIFICATION_USER_PROMPT } from './prompts'

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY!)

export async function verifyCitations(plan: string) {
  const model = genAI.getGenerativeModel({
    model: 'gemini-1.5-pro', // Or gemini-2.0-flash for faster/cheaper
    systemInstruction: CITATION_VERIFICATION_SYSTEM_PROMPT
  })

  const result = await model.generateContent(CITATION_VERIFICATION_USER_PROMPT(plan))
  const response = result.response

  return {
    content: response.text(),
    usage: response.usageMetadata
  }
}
```

### Main Pipeline

Create `src/lib/pipeline/generate.ts`:
```typescript
import { createServiceClient } from '../supabase/server'
import { generatePlan } from '../ai/openai'
import { verifyClinical } from '../ai/anthropic'
import { verifyCitations } from '../ai/gemini'
import { calculateCost } from '../utils/costs'
import { generateSlug } from '../utils/slug'

interface PipelineOptions {
  skipVerification?: boolean
}

export async function runPipeline(
  diagnosis: string,
  modifier: string,
  options: PipelineOptions = {}
) {
  const supabase = createServiceClient()
  const slug = generateSlug(diagnosis, modifier)
  let totalCost = 0

  // Create plan record
  const { data: plan, error: planError } = await supabase
    .from('plans')
    .insert({
      diagnosis,
      modifier,
      slug,
      title: `${diagnosis} - ${modifier}`,
      status: 'generating',
      current_stage: 'generate'
    })
    .select()
    .single()

  if (planError) throw planError

  try {
    // Stage 1: Generate with GPT
    const genStart = Date.now()
    await logJob(supabase, plan.id, 'generate', 'running')

    const generation = await generatePlan(diagnosis, modifier)
    const genCost = calculateCost('gpt-4o', generation.usage.prompt_tokens, generation.usage.completion_tokens)
    totalCost += genCost

    await logJob(supabase, plan.id, 'generate', 'completed', {
      model: 'gpt-4o',
      input_tokens: generation.usage.prompt_tokens,
      output_tokens: generation.usage.completion_tokens,
      cost_usd: genCost,
      duration_ms: Date.now() - genStart,
      result: { preview: generation.content.substring(0, 500) }
    })

    // Update plan with generated content
    await supabase
      .from('plans')
      .update({
        content_md: generation.content,
        status: options.skipVerification ? 'review' : 'verifying',
        current_stage: options.skipVerification ? 'complete' : 'verify_clinical'
      })
      .eq('id', plan.id)

    if (options.skipVerification) {
      return { planId: plan.id, slug, cost: totalCost }
    }

    // Stage 2: Verification (parallel)
    const [clinicalResult, citationResult] = await Promise.all([
      runClinicalVerification(supabase, plan.id, generation.content),
      runCitationVerification(supabase, plan.id, generation.content)
    ])

    totalCost += clinicalResult.cost + citationResult.cost

    // Save verification report
    const humanReviewRequired =
      clinicalResult.status === 'failed' ||
      clinicalResult.status === 'flagged' ||
      citationResult.status === 'failed'

    await supabase.from('verification_reports').insert({
      plan_id: plan.id,
      clinical_status: clinicalResult.status,
      clinical_model: 'claude-sonnet-4',
      clinical_result: clinicalResult.result,
      citation_status: citationResult.status,
      citation_model: 'gemini-1.5-pro',
      citation_result: citationResult.result,
      overall_status: humanReviewRequired ? 'flagged' : 'passed',
      human_review_required: humanReviewRequired,
      human_review_items: [
        ...clinicalResult.reviewItems,
        ...citationResult.reviewItems
      ]
    })

    // Update plan status
    await supabase
      .from('plans')
      .update({
        status: 'review',
        current_stage: 'complete'
      })
      .eq('id', plan.id)

    return {
      planId: plan.id,
      slug,
      cost: totalCost,
      humanReviewRequired,
      reviewItems: [...clinicalResult.reviewItems, ...citationResult.reviewItems]
    }

  } catch (error) {
    // Update plan as failed
    await supabase
      .from('plans')
      .update({ status: 'failed' })
      .eq('id', plan.id)

    throw error
  }
}

async function runClinicalVerification(supabase: any, planId: string, content: string) {
  const start = Date.now()
  await logJob(supabase, planId, 'verify_clinical', 'running')

  try {
    const result = await verifyClinical(content)
    const cost = calculateCost('claude-sonnet-4', result.usage.input_tokens, result.usage.output_tokens)

    // Parse the JSON from the response
    const jsonMatch = result.content.match(/```json\n([\s\S]*?)\n```/)
    const parsed = jsonMatch ? JSON.parse(jsonMatch[1]) : { status: 'unknown' }

    await logJob(supabase, planId, 'verify_clinical', 'completed', {
      model: 'claude-sonnet-4',
      input_tokens: result.usage.input_tokens,
      output_tokens: result.usage.output_tokens,
      cost_usd: cost,
      duration_ms: Date.now() - start,
      result: parsed
    })

    return {
      status: parsed.status,
      result: parsed,
      cost,
      reviewItems: parsed.errors?.map((e: any) => e.issue) || []
    }
  } catch (error) {
    await logJob(supabase, planId, 'verify_clinical', 'failed', {
      error_message: String(error)
    })
    return { status: 'failed', result: null, cost: 0, reviewItems: ['Clinical verification failed'] }
  }
}

async function runCitationVerification(supabase: any, planId: string, content: string) {
  const start = Date.now()
  await logJob(supabase, planId, 'verify_citation', 'running')

  try {
    const result = await verifyCitations(content)
    const cost = calculateCost('gemini-1.5-pro',
      result.usage?.promptTokenCount || 0,
      result.usage?.candidatesTokenCount || 0
    )

    // Parse the JSON from the response
    const jsonMatch = result.content.match(/```json\n([\s\S]*?)\n```/)
    const parsed = jsonMatch ? JSON.parse(jsonMatch[1]) : { status: 'unknown' }

    await logJob(supabase, planId, 'verify_citation', 'completed', {
      model: 'gemini-1.5-pro',
      input_tokens: result.usage?.promptTokenCount || 0,
      output_tokens: result.usage?.candidatesTokenCount || 0,
      cost_usd: cost,
      duration_ms: Date.now() - start,
      result: parsed
    })

    return {
      status: parsed.status,
      result: parsed,
      cost,
      reviewItems: parsed.corrections?.filter((c: any) => !c.auto_fixable).map((c: any) => c.original) || []
    }
  } catch (error) {
    await logJob(supabase, planId, 'verify_citation', 'failed', {
      error_message: String(error)
    })
    return { status: 'failed', result: null, cost: 0, reviewItems: ['Citation verification failed'] }
  }
}

async function logJob(
  supabase: any,
  planId: string,
  stage: string,
  status: string,
  data: any = {}
) {
  if (status === 'running') {
    await supabase.from('generation_jobs').insert({
      plan_id: planId,
      stage,
      status,
      started_at: new Date().toISOString()
    })
  } else {
    await supabase
      .from('generation_jobs')
      .update({
        status,
        completed_at: new Date().toISOString(),
        ...data
      })
      .eq('plan_id', planId)
      .eq('stage', stage)
  }
}
```

### Utility Functions

Create `src/lib/utils/costs.ts`:
```typescript
const PRICING: Record<string, { input: number; output: number }> = {
  'gpt-4o': { input: 2.5 / 1_000_000, output: 10 / 1_000_000 },
  'gpt-5.2': { input: 1.75 / 1_000_000, output: 14 / 1_000_000 },
  'claude-sonnet-4': { input: 3 / 1_000_000, output: 15 / 1_000_000 },
  'claude-opus-4.5': { input: 5 / 1_000_000, output: 25 / 1_000_000 },
  'gemini-1.5-pro': { input: 1.25 / 1_000_000, output: 5 / 1_000_000 },
  'gemini-2.0-flash': { input: 0.1 / 1_000_000, output: 0.4 / 1_000_000 }
}

export function calculateCost(model: string, inputTokens: number, outputTokens: number): number {
  const pricing = PRICING[model] || PRICING['gpt-4o']
  return (inputTokens * pricing.input) + (outputTokens * pricing.output)
}
```

Create `src/lib/utils/slug.ts`:
```typescript
export function generateSlug(diagnosis: string, modifier: string): string {
  const combined = `${diagnosis}-${modifier}`
  return combined
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
}
```

Create `src/lib/types.ts`:
```typescript
export interface Plan {
  id: string
  diagnosis: string
  modifier: string
  slug: string
  title: string
  content_md: string | null
  content_json: any | null
  status: 'draft' | 'generating' | 'verifying' | 'review' | 'approved' | 'rejected'
  current_stage: string | null
  version: string
  icd10: string[]
  setting_coverage: {
    ED: boolean
    HOSP: boolean
    OPD: boolean
    ICU: boolean
  }
  quality_score: number | null
  created_at: string
  updated_at: string
  approved_at: string | null
  approved_by: string | null
}

export interface GenerationJob {
  id: string
  plan_id: string
  stage: string
  status: string
  model: string | null
  input_tokens: number | null
  output_tokens: number | null
  cost_usd: number | null
  result: any | null
  error_message: string | null
  started_at: string | null
  completed_at: string | null
  duration_ms: number | null
}

export interface VerificationReport {
  id: string
  plan_id: string
  clinical_status: string | null
  clinical_result: any | null
  citation_status: string | null
  citation_result: any | null
  overall_status: string | null
  human_review_required: boolean
  human_review_items: string[]
  auto_fixes_applied: string[]
}
```

## STEP 7: API ROUTES

Create `src/app/api/generate/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { runPipeline } from '@/lib/pipeline/generate'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { diagnosis, modifier = 'new-diagnosis', skipVerification = false } = body

    if (!diagnosis) {
      return NextResponse.json({ error: 'Diagnosis is required' }, { status: 400 })
    }

    const result = await runPipeline(diagnosis, modifier, { skipVerification })

    return NextResponse.json({
      success: true,
      planId: result.planId,
      slug: result.slug,
      cost: result.cost,
      humanReviewRequired: result.humanReviewRequired,
      reviewItems: result.reviewItems
    })

  } catch (error) {
    console.error('Generation error:', error)
    return NextResponse.json(
      { error: 'Failed to generate plan', details: String(error) },
      { status: 500 }
    )
  }
}
```

Create `src/app/api/plans/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const status = searchParams.get('status')
  const limit = parseInt(searchParams.get('limit') || '50')
  const offset = parseInt(searchParams.get('offset') || '0')

  const supabase = createServiceClient()

  let query = supabase
    .from('plans')
    .select('*', { count: 'exact' })
    .order('created_at', { ascending: false })
    .range(offset, offset + limit - 1)

  if (status) {
    query = query.eq('status', status)
  }

  const { data, error, count } = await query

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }

  return NextResponse.json({ plans: data, total: count, limit, offset })
}
```

Create `src/app/api/plans/[slug]/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'

export async function GET(
  request: NextRequest,
  { params }: { params: { slug: string } }
) {
  const supabase = createServiceClient()

  const { data: plan, error } = await supabase
    .from('plans')
    .select('*')
    .eq('slug', params.slug)
    .single()

  if (error || !plan) {
    return NextResponse.json({ error: 'Plan not found' }, { status: 404 })
  }

  // Also fetch verification report
  const { data: report } = await supabase
    .from('verification_reports')
    .select('*')
    .eq('plan_id', plan.id)
    .order('created_at', { ascending: false })
    .limit(1)
    .single()

  return NextResponse.json({ plan, verificationReport: report })
}
```

Create `src/app/api/approve/[planId]/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'

export async function POST(
  request: NextRequest,
  { params }: { params: { planId: string } }
) {
  const body = await request.json()
  const { approved_by, comments } = body

  const supabase = createServiceClient()

  const { data, error } = await supabase
    .from('plans')
    .update({
      status: 'approved',
      approved_at: new Date().toISOString(),
      approved_by: approved_by || 'physician'
    })
    .eq('id', params.planId)
    .select()
    .single()

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }

  // Log to audit
  await supabase.from('audit_log').insert({
    plan_id: params.planId,
    action: 'approved',
    user_id: approved_by,
    details: { comments }
  })

  return NextResponse.json({ success: true, plan: data })
}
```

Create `src/app/api/reject/[planId]/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'

export async function POST(
  request: NextRequest,
  { params }: { params: { planId: string } }
) {
  const body = await request.json()
  const { rejected_by, reason } = body

  const supabase = createServiceClient()

  const { data, error } = await supabase
    .from('plans')
    .update({ status: 'rejected' })
    .eq('id', params.planId)
    .select()
    .single()

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }

  await supabase.from('audit_log').insert({
    plan_id: params.planId,
    action: 'rejected',
    user_id: rejected_by,
    details: { reason }
  })

  return NextResponse.json({ success: true, plan: data })
}
```

## STEP 8: UI COMPONENTS

Create all the UI components with a clean, professional medical interface:

### Layout and Navigation

`src/app/layout.tsx`:
```typescript
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Navigation } from '@/components/Navigation'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Clinical Plan Generator',
  description: 'AI-powered clinical decision support plan generator',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation />
        <main className="min-h-screen bg-gray-50">
          {children}
        </main>
      </body>
    </html>
  )
}
```

`src/components/Navigation.tsx`:
```typescript
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { FileText, PlusCircle, CheckSquare, LayoutDashboard } from 'lucide-react'

export function Navigation() {
  const pathname = usePathname()

  const links = [
    { href: '/', label: 'Dashboard', icon: LayoutDashboard },
    { href: '/generate', label: 'Generate Plan', icon: PlusCircle },
    { href: '/plans', label: 'All Plans', icon: FileText },
    { href: '/review', label: 'Review Queue', icon: CheckSquare },
  ]

  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <span className="text-xl font-bold text-blue-600">Clinical Plan Generator</span>
            </div>
            <div className="hidden sm:ml-8 sm:flex sm:space-x-4">
              {links.map((link) => {
                const Icon = link.icon
                const isActive = pathname === link.href
                return (
                  <Link
                    key={link.href}
                    href={link.href}
                    className={`inline-flex items-center px-3 py-2 text-sm font-medium rounded-md ${
                      isActive
                        ? 'bg-blue-50 text-blue-700'
                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                    }`}
                  >
                    <Icon className="w-4 h-4 mr-2" />
                    {link.label}
                  </Link>
                )
              })}
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}
```

### Dashboard Page

`src/app/page.tsx`:
```typescript
import Link from 'next/link'
import { createServiceClient } from '@/lib/supabase/server'
import { PlusCircle, FileText, CheckSquare, AlertCircle } from 'lucide-react'

export const dynamic = 'force-dynamic'

export default async function Dashboard() {
  const supabase = createServiceClient()

  const [
    { count: totalPlans },
    { count: reviewCount },
    { count: approvedCount },
    { data: recentPlans }
  ] = await Promise.all([
    supabase.from('plans').select('*', { count: 'exact', head: true }),
    supabase.from('plans').select('*', { count: 'exact', head: true }).eq('status', 'review'),
    supabase.from('plans').select('*', { count: 'exact', head: true }).eq('status', 'approved'),
    supabase.from('plans').select('*').order('created_at', { ascending: false }).limit(5)
  ])

  const stats = [
    { name: 'Total Plans', value: totalPlans || 0, icon: FileText, color: 'bg-blue-500' },
    { name: 'Pending Review', value: reviewCount || 0, icon: AlertCircle, color: 'bg-yellow-500' },
    { name: 'Approved', value: approvedCount || 0, icon: CheckSquare, color: 'bg-green-500' },
  ]

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600">AI-powered clinical decision support plan generator</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {stats.map((stat) => {
          const Icon = stat.icon
          return (
            <div key={stat.name} className="bg-white rounded-lg shadow p-6">
              <div className="flex items-center">
                <div className={`${stat.color} p-3 rounded-lg`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-600">{stat.name}</p>
                  <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Quick Actions */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-lg font-semibold mb-4">Quick Actions</h2>
        <div className="flex gap-4">
          <Link
            href="/generate"
            className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            <PlusCircle className="w-5 h-5 mr-2" />
            Generate New Plan
          </Link>
          <Link
            href="/review"
            className="inline-flex items-center px-4 py-2 bg-yellow-500 text-white rounded-lg hover:bg-yellow-600"
          >
            <CheckSquare className="w-5 h-5 mr-2" />
            Review Queue ({reviewCount || 0})
          </Link>
        </div>
      </div>

      {/* Recent Plans */}
      <div className="bg-white rounded-lg shadow">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-semibold">Recent Plans</h2>
        </div>
        <div className="divide-y divide-gray-200">
          {recentPlans?.map((plan) => (
            <Link
              key={plan.id}
              href={`/plans/${plan.slug}`}
              className="block px-6 py-4 hover:bg-gray-50"
            >
              <div className="flex justify-between items-center">
                <div>
                  <p className="font-medium text-gray-900">{plan.title}</p>
                  <p className="text-sm text-gray-500">
                    {new Date(plan.created_at).toLocaleDateString()}
                  </p>
                </div>
                <span className={`px-3 py-1 text-sm rounded-full ${
                  plan.status === 'approved' ? 'bg-green-100 text-green-800' :
                  plan.status === 'review' ? 'bg-yellow-100 text-yellow-800' :
                  plan.status === 'generating' ? 'bg-blue-100 text-blue-800' :
                  'bg-gray-100 text-gray-800'
                }`}>
                  {plan.status}
                </span>
              </div>
            </Link>
          ))}
          {(!recentPlans || recentPlans.length === 0) && (
            <div className="px-6 py-8 text-center text-gray-500">
              No plans yet. Generate your first plan!
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
```

### Generation Page

`src/app/generate/page.tsx`:
```typescript
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Loader2, Sparkles, CheckCircle, AlertCircle } from 'lucide-react'

const DIAGNOSES = [
  'Guillain-Barré Syndrome',
  'Multiple Sclerosis',
  'Status Epilepticus',
  'Acute Ischemic Stroke',
  'Myasthenia Gravis',
  'Parkinson Disease',
  'Migraine',
  'Meningitis',
  'Peripheral Neuropathy',
  'Bell Palsy'
]

const MODIFIERS = [
  { value: 'new-diagnosis', label: 'New Diagnosis' },
  { value: 'exacerbation', label: 'Exacerbation/Acute' },
  { value: 'maintenance', label: 'Chronic/Maintenance' },
  { value: 'refractory', label: 'Refractory' }
]

export default function GeneratePage() {
  const router = useRouter()
  const [diagnosis, setDiagnosis] = useState('')
  const [customDiagnosis, setCustomDiagnosis] = useState('')
  const [modifier, setModifier] = useState('new-diagnosis')
  const [skipVerification, setSkipVerification] = useState(false)
  const [isGenerating, setIsGenerating] = useState(false)
  const [status, setStatus] = useState<'idle' | 'generating' | 'verifying' | 'complete' | 'error'>('idle')
  const [result, setResult] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const finalDiagnosis = diagnosis === 'custom' ? customDiagnosis : diagnosis

    if (!finalDiagnosis) {
      setError('Please select or enter a diagnosis')
      return
    }

    setIsGenerating(true)
    setStatus('generating')
    setError(null)

    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          diagnosis: finalDiagnosis,
          modifier,
          skipVerification
        })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Generation failed')
      }

      setStatus('complete')
      setResult(data)

      // Redirect after a short delay
      setTimeout(() => {
        router.push(`/plans/${data.slug}`)
      }, 2000)

    } catch (err) {
      setStatus('error')
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Generate Clinical Plan</h1>
        <p className="text-gray-600">Create a new evidence-based clinical decision support plan</p>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Diagnosis Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Diagnosis
            </label>
            <select
              value={diagnosis}
              onChange={(e) => setDiagnosis(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              disabled={isGenerating}
            >
              <option value="">Select a diagnosis...</option>
              {DIAGNOSES.map((d) => (
                <option key={d} value={d}>{d}</option>
              ))}
              <option value="custom">Custom (enter below)</option>
            </select>
          </div>

          {/* Custom Diagnosis Input */}
          {diagnosis === 'custom' && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Custom Diagnosis
              </label>
              <input
                type="text"
                value={customDiagnosis}
                onChange={(e) => setCustomDiagnosis(e.target.value)}
                placeholder="Enter diagnosis name..."
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                disabled={isGenerating}
              />
            </div>
          )}

          {/* Modifier Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Plan Type
            </label>
            <div className="grid grid-cols-2 gap-3">
              {MODIFIERS.map((m) => (
                <label
                  key={m.value}
                  className={`flex items-center justify-center px-4 py-3 border rounded-lg cursor-pointer transition-colors ${
                    modifier === m.value
                      ? 'border-blue-500 bg-blue-50 text-blue-700'
                      : 'border-gray-300 hover:border-gray-400'
                  } ${isGenerating ? 'opacity-50 cursor-not-allowed' : ''}`}
                >
                  <input
                    type="radio"
                    name="modifier"
                    value={m.value}
                    checked={modifier === m.value}
                    onChange={(e) => setModifier(e.target.value)}
                    className="sr-only"
                    disabled={isGenerating}
                  />
                  {m.label}
                </label>
              ))}
            </div>
          </div>

          {/* Skip Verification Option */}
          <div className="flex items-center">
            <input
              type="checkbox"
              id="skipVerification"
              checked={skipVerification}
              onChange={(e) => setSkipVerification(e.target.checked)}
              className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
              disabled={isGenerating}
            />
            <label htmlFor="skipVerification" className="ml-2 text-sm text-gray-600">
              Skip verification (faster, but no clinical/citation check)
            </label>
          </div>

          {/* Cost Estimate */}
          <div className="bg-gray-50 rounded-lg p-4">
            <p className="text-sm text-gray-600">
              <strong>Estimated cost:</strong> {skipVerification ? '~$0.15' : '~$0.30'} per plan
            </p>
            <p className="text-xs text-gray-500 mt-1">
              {skipVerification
                ? 'GPT-4o generation only'
                : 'GPT-4o generation + Claude clinical verification + Gemini citation check'
              }
            </p>
          </div>

          {/* Status Display */}
          {status !== 'idle' && (
            <div className={`rounded-lg p-4 ${
              status === 'error' ? 'bg-red-50' :
              status === 'complete' ? 'bg-green-50' :
              'bg-blue-50'
            }`}>
              <div className="flex items-center">
                {status === 'generating' && (
                  <>
                    <Loader2 className="w-5 h-5 text-blue-600 animate-spin mr-2" />
                    <span className="text-blue-700">Generating plan with AI...</span>
                  </>
                )}
                {status === 'verifying' && (
                  <>
                    <Loader2 className="w-5 h-5 text-blue-600 animate-spin mr-2" />
                    <span className="text-blue-700">Verifying clinical accuracy...</span>
                  </>
                )}
                {status === 'complete' && (
                  <>
                    <CheckCircle className="w-5 h-5 text-green-600 mr-2" />
                    <span className="text-green-700">
                      Plan generated! Cost: ${result?.cost?.toFixed(3)}. Redirecting...
                    </span>
                  </>
                )}
                {status === 'error' && (
                  <>
                    <AlertCircle className="w-5 h-5 text-red-600 mr-2" />
                    <span className="text-red-700">{error}</span>
                  </>
                )}
              </div>
            </div>
          )}

          {/* Submit Button */}
          <button
            type="submit"
            disabled={isGenerating}
            className={`w-full flex items-center justify-center px-4 py-3 rounded-lg text-white font-medium transition-colors ${
              isGenerating
                ? 'bg-gray-400 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700'
            }`}
          >
            {isGenerating ? (
              <>
                <Loader2 className="w-5 h-5 mr-2 animate-spin" />
                Generating...
              </>
            ) : (
              <>
                <Sparkles className="w-5 h-5 mr-2" />
                Generate Plan
              </>
            )}
          </button>
        </form>
      </div>
    </div>
  )
}
```

### Plans List Page

`src/app/plans/page.tsx`:
```typescript
import Link from 'next/link'
import { createServiceClient } from '@/lib/supabase/server'

export const dynamic = 'force-dynamic'

export default async function PlansPage() {
  const supabase = createServiceClient()

  const { data: plans } = await supabase
    .from('plans')
    .select('*')
    .order('created_at', { ascending: false })

  const statusColors: Record<string, string> = {
    approved: 'bg-green-100 text-green-800',
    review: 'bg-yellow-100 text-yellow-800',
    generating: 'bg-blue-100 text-blue-800',
    verifying: 'bg-purple-100 text-purple-800',
    rejected: 'bg-red-100 text-red-800',
    draft: 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8 flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">All Plans</h1>
          <p className="text-gray-600">{plans?.length || 0} clinical plans</p>
        </div>
        <Link
          href="/generate"
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Generate New
        </Link>
      </div>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Plan
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Created
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Settings
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {plans?.map((plan) => (
              <tr key={plan.id} className="hover:bg-gray-50">
                <td className="px-6 py-4">
                  <Link href={`/plans/${plan.slug}`} className="block">
                    <div className="font-medium text-gray-900 hover:text-blue-600">
                      {plan.title}
                    </div>
                    <div className="text-sm text-gray-500">
                      {plan.icd10?.join(', ') || 'No ICD-10'}
                    </div>
                  </Link>
                </td>
                <td className="px-6 py-4">
                  <span className={`px-3 py-1 text-sm rounded-full ${statusColors[plan.status] || statusColors.draft}`}>
                    {plan.status}
                  </span>
                </td>
                <td className="px-6 py-4 text-sm text-gray-500">
                  {new Date(plan.created_at).toLocaleDateString()}
                </td>
                <td className="px-6 py-4">
                  <div className="flex gap-1">
                    {plan.setting_coverage?.ED && <span className="px-2 py-0.5 text-xs bg-red-100 text-red-800 rounded">ED</span>}
                    {plan.setting_coverage?.HOSP && <span className="px-2 py-0.5 text-xs bg-blue-100 text-blue-800 rounded">HOSP</span>}
                    {plan.setting_coverage?.OPD && <span className="px-2 py-0.5 text-xs bg-green-100 text-green-800 rounded">OPD</span>}
                    {plan.setting_coverage?.ICU && <span className="px-2 py-0.5 text-xs bg-purple-100 text-purple-800 rounded">ICU</span>}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {(!plans || plans.length === 0) && (
          <div className="px-6 py-12 text-center text-gray-500">
            No plans yet. Generate your first plan!
          </div>
        )}
      </div>
    </div>
  )
}
```

### Single Plan View Page

`src/app/plans/[slug]/page.tsx`:
```typescript
import { createServiceClient } from '@/lib/supabase/server'
import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, CheckCircle, AlertTriangle, XCircle } from 'lucide-react'

export const dynamic = 'force-dynamic'

export default async function PlanPage({ params }: { params: { slug: string } }) {
  const supabase = createServiceClient()

  const { data: plan } = await supabase
    .from('plans')
    .select('*')
    .eq('slug', params.slug)
    .single()

  if (!plan) {
    notFound()
  }

  const { data: report } = await supabase
    .from('verification_reports')
    .select('*')
    .eq('plan_id', plan.id)
    .order('created_at', { ascending: false })
    .limit(1)
    .single()

  const { data: jobs } = await supabase
    .from('generation_jobs')
    .select('*')
    .eq('plan_id', plan.id)
    .order('created_at', { ascending: true })

  const totalCost = jobs?.reduce((sum, job) => sum + (job.cost_usd || 0), 0) || 0

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="mb-6">
        <Link href="/plans" className="inline-flex items-center text-gray-600 hover:text-gray-900 mb-4">
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Plans
        </Link>
        <div className="flex justify-between items-start">
          <div>
            <h1 className="text-2xl font-bold text-gray-900">{plan.title}</h1>
            <p className="text-gray-600">Version {plan.version} | Created {new Date(plan.created_at).toLocaleDateString()}</p>
          </div>
          <span className={`px-4 py-2 rounded-full text-sm font-medium ${
            plan.status === 'approved' ? 'bg-green-100 text-green-800' :
            plan.status === 'review' ? 'bg-yellow-100 text-yellow-800' :
            'bg-gray-100 text-gray-800'
          }`}>
            {plan.status}
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-6">
          {/* Plan Content */}
          <div className="bg-white rounded-lg shadow">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-semibold">Plan Content</h2>
            </div>
            <div className="p-6">
              {plan.content_md ? (
                <pre className="whitespace-pre-wrap text-sm font-mono bg-gray-50 p-4 rounded-lg overflow-auto max-h-[600px]">
                  {plan.content_md}
                </pre>
              ) : (
                <p className="text-gray-500">No content generated yet.</p>
              )}
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Generation Info */}
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="font-semibold mb-4">Generation Details</h3>
            <dl className="space-y-3 text-sm">
              <div className="flex justify-between">
                <dt className="text-gray-600">Total Cost</dt>
                <dd className="font-medium">${totalCost.toFixed(4)}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-gray-600">ICD-10</dt>
                <dd className="font-medium">{plan.icd10?.join(', ') || 'Not set'}</dd>
              </div>
            </dl>
          </div>

          {/* Verification Status */}
          {report && (
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="font-semibold mb-4">Verification</h3>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-600">Clinical</span>
                  <span className={`flex items-center text-sm ${
                    report.clinical_status === 'passed' ? 'text-green-600' :
                    report.clinical_status === 'flagged' ? 'text-yellow-600' :
                    'text-red-600'
                  }`}>
                    {report.clinical_status === 'passed' ? <CheckCircle className="w-4 h-4 mr-1" /> :
                     report.clinical_status === 'flagged' ? <AlertTriangle className="w-4 h-4 mr-1" /> :
                     <XCircle className="w-4 h-4 mr-1" />}
                    {report.clinical_status}
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-600">Citations</span>
                  <span className={`flex items-center text-sm ${
                    report.citation_status === 'passed' ? 'text-green-600' :
                    report.citation_status === 'flagged' ? 'text-yellow-600' :
                    'text-red-600'
                  }`}>
                    {report.citation_status === 'passed' ? <CheckCircle className="w-4 h-4 mr-1" /> :
                     report.citation_status === 'flagged' ? <AlertTriangle className="w-4 h-4 mr-1" /> :
                     <XCircle className="w-4 h-4 mr-1" />}
                    {report.citation_status}
                  </span>
                </div>
                {report.human_review_items?.length > 0 && (
                  <div className="mt-4 pt-4 border-t border-gray-200">
                    <p className="text-sm font-medium text-yellow-800 mb-2">Review Items:</p>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {report.human_review_items.map((item: string, i: number) => (
                        <li key={i} className="flex items-start">
                          <AlertTriangle className="w-4 h-4 text-yellow-500 mr-2 mt-0.5 flex-shrink-0" />
                          {item}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Actions */}
          {plan.status === 'review' && (
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="font-semibold mb-4">Actions</h3>
              <div className="space-y-3">
                <ApproveButton planId={plan.id} />
                <RejectButton planId={plan.id} />
              </div>
            </div>
          )}

          {/* Pipeline Stages */}
          {jobs && jobs.length > 0 && (
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="font-semibold mb-4">Pipeline Stages</h3>
              <div className="space-y-3">
                {jobs.map((job) => (
                  <div key={job.id} className="flex items-center justify-between text-sm">
                    <span className="text-gray-600 capitalize">{job.stage.replace('_', ' ')}</span>
                    <span className={`${
                      job.status === 'completed' ? 'text-green-600' :
                      job.status === 'running' ? 'text-blue-600' :
                      job.status === 'failed' ? 'text-red-600' :
                      'text-gray-400'
                    }`}>
                      {job.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

// Client components for buttons
'use client'
function ApproveButton({ planId }: { planId: string }) {
  const handleApprove = async () => {
    if (!confirm('Approve this plan?')) return
    await fetch(`/api/approve/${planId}`, { method: 'POST', body: JSON.stringify({}) })
    window.location.reload()
  }
  return (
    <button onClick={handleApprove} className="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
      Approve Plan
    </button>
  )
}

function RejectButton({ planId }: { planId: string }) {
  const handleReject = async () => {
    const reason = prompt('Rejection reason:')
    if (!reason) return
    await fetch(`/api/reject/${planId}`, { method: 'POST', body: JSON.stringify({ reason }) })
    window.location.reload()
  }
  return (
    <button onClick={handleReject} className="w-full px-4 py-2 bg-red-100 text-red-700 rounded-lg hover:bg-red-200">
      Reject Plan
    </button>
  )
}
```

### Review Queue Page

`src/app/review/page.tsx`:
```typescript
import Link from 'next/link'
import { createServiceClient } from '@/lib/supabase/server'
import { AlertTriangle, ArrowRight } from 'lucide-react'

export const dynamic = 'force-dynamic'

export default async function ReviewPage() {
  const supabase = createServiceClient()

  const { data: plans } = await supabase
    .from('plans')
    .select(`
      *,
      verification_reports (
        human_review_required,
        human_review_items,
        clinical_status,
        citation_status
      )
    `)
    .eq('status', 'review')
    .order('created_at', { ascending: true })

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Review Queue</h1>
        <p className="text-gray-600">{plans?.length || 0} plans awaiting review</p>
      </div>

      {plans && plans.length > 0 ? (
        <div className="space-y-4">
          {plans.map((plan) => {
            const report = plan.verification_reports?.[0]
            return (
              <div key={plan.id} className="bg-white rounded-lg shadow p-6">
                <div className="flex justify-between items-start">
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-gray-900">{plan.title}</h3>
                    <p className="text-sm text-gray-500 mt-1">
                      Created {new Date(plan.created_at).toLocaleDateString()}
                    </p>

                    {report?.human_review_items?.length > 0 && (
                      <div className="mt-4">
                        <p className="text-sm font-medium text-yellow-800 flex items-center">
                          <AlertTriangle className="w-4 h-4 mr-2" />
                          {report.human_review_items.length} item(s) need review:
                        </p>
                        <ul className="mt-2 text-sm text-gray-600 space-y-1 ml-6">
                          {report.human_review_items.slice(0, 3).map((item: string, i: number) => (
                            <li key={i}>• {item}</li>
                          ))}
                          {report.human_review_items.length > 3 && (
                            <li className="text-gray-400">
                              +{report.human_review_items.length - 3} more...
                            </li>
                          )}
                        </ul>
                      </div>
                    )}
                  </div>

                  <Link
                    href={`/plans/${plan.slug}`}
                    className="ml-4 inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                  >
                    Review
                    <ArrowRight className="w-4 h-4 ml-2" />
                  </Link>
                </div>
              </div>
            )
          })}
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow p-12 text-center">
          <p className="text-gray-500 text-lg">No plans awaiting review</p>
          <Link href="/generate" className="mt-4 inline-block text-blue-600 hover:text-blue-700">
            Generate a new plan
          </Link>
        </div>
      )}
    </div>
  )
}
```

## STEP 9: TAILWIND CONFIG

Update `tailwind.config.ts`:
```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
export default config
```

## STEP 10: SETUP INSTRUCTIONS FOR USER

After you build all this, give me these instructions:

### 1. Create Supabase Project
1. Go to https://supabase.com and create a new project
2. Copy the Project URL and anon key from Settings → API
3. Copy the service_role key (keep this secret!)

### 2. Run Database Schema
1. Go to Supabase → SQL Editor
2. Paste the contents of `supabase/schema.sql`
3. Click "Run"

### 3. Get API Keys
- **OpenAI:** https://platform.openai.com/api-keys
- **Anthropic:** https://console.anthropic.com/settings/keys
- **Google AI:** https://aistudio.google.com/app/apikey

### 4. Configure Environment
1. Copy `.env.example` to `.env.local`
2. Fill in all the API keys

### 5. Run Locally
```bash
npm run dev
```
Open http://localhost:3000

### 6. Deploy to Vercel
1. Push to GitHub
2. Import in Vercel
3. Add environment variables in Vercel dashboard
4. Deploy

## IMPORTANT NOTES

1. **API keys are NEVER stored in Supabase** - they stay in Vercel environment variables
2. The free Vercel tier has a 10-second function timeout - if generation takes longer, it will fail. Consider using edge functions or upgrading to Pro for 60-second timeout.
3. Start with `gpt-4o` since `gpt-5.2` may not be available via API yet. Update the model name when available.
4. The UI is intentionally simple and clean - it can be enhanced later.

Now build all of this. Create each file with the complete code. Do not skip any files. Ask me to fill in environment variables when done.
