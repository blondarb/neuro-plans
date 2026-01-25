# CLAUDE CODE ONE-SHOT PROMPT
## Clinical Plan Generator - Full Stack Build

Copy everything below the line and paste it into Claude Code in a new empty directory.

---

# BUILD REQUEST: Clinical Plan Generator

Build a complete full-stack application for generating clinical decision support plans using a multi-model AI pipeline. This will be a Next.js app deployed on Vercel with Supabase as the backend.

## CRITICAL: HANDLING VERCEL TIMEOUTS

**Vercel free tier has a 10-second function timeout.** AI generation takes 30-90 seconds. We MUST use this architecture:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TIMEOUT-SAFE ARCHITECTURE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  USER SUBMITS                VERCEL API               SUPABASE               │
│  ───────────────────────────────────────────────────────────────────────    │
│                                                                              │
│  1. POST /api/generate  ──▶  Creates job record  ──▶  job_id returned       │
│     (returns in <2 sec)      in Supabase                                    │
│                                                                              │
│  2. Supabase Edge Function triggered ──▶ Runs AI pipeline (60+ sec OK)     │
│     (via database trigger or pg_cron)                                       │
│                                                                              │
│  3. Client polls GET /api/status/:id every 3 seconds                        │
│     (each poll <2 sec)                                                      │
│                                                                              │
│  4. When complete, client redirects to plan view                            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**KEY INSIGHT:** Vercel handles the quick HTTP requests. Supabase Edge Functions handle the slow AI work.

---

## PROJECT OVERVIEW

**What it does:**
1. User submits a neurological diagnosis (e.g., "Guillain-Barré Syndrome - New Diagnosis")
2. Job queued in Supabase (returns immediately)
3. Supabase Edge Function runs the multi-model pipeline:
   - GPT-4o generates comprehensive clinical plan (~$0.15)
   - Claude Sonnet 4 verifies clinical accuracy (~$0.08)
   - Gemini 1.5 Pro verifies citations (~$0.04)
4. Results saved to Supabase
5. Client polls until complete, then shows result
6. Physician reviews and approves via web UI
7. Approved plans available via API for other apps

**Total cost: ~$0.27 per plan**

**Tech Stack:**
- Next.js 14+ (App Router)
- TypeScript
- Tailwind CSS
- Supabase (database, auth, real-time, **Edge Functions**)
- Vercel (hosting - UI and quick APIs only)
- OpenAI API (GPT-4o)
- Anthropic API (Claude Sonnet 4)
- Google AI API (Gemini 1.5 Pro)

---

## STEP 1: PROJECT SETUP

Create a new Next.js project with these specifications:

```bash
npx create-next-app@latest clinical-plan-generator --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
cd clinical-plan-generator
npm install @supabase/supabase-js @supabase/ssr openai @anthropic-ai/sdk @google/generative-ai lucide-react
```

Also initialize Supabase CLI for Edge Functions:
```bash
npx supabase init
npx supabase login
```

---

## STEP 2: ENVIRONMENT VARIABLES

Create `.env.local` with placeholders (I will fill in):

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# AI Providers (also add these to Supabase Edge Function secrets)
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GEMINI_API_KEY=your_gemini_key

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

Also create `.env.example` with the same structure but empty values for documentation.

---

## STEP 3: SUPABASE DATABASE SCHEMA

Create a file `supabase/schema.sql` with the complete database schema:

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_net"; -- For calling Edge Functions

-- Plans table
CREATE TABLE plans (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- Identity
  diagnosis VARCHAR(255) NOT NULL,
  modifier VARCHAR(50),
  slug VARCHAR(255) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,

  -- Content
  content_md TEXT,
  content_json JSONB,

  -- Status: queued, generating, verifying_clinical, verifying_citation, review, approved, rejected, failed
  status VARCHAR(50) DEFAULT 'queued',
  current_stage VARCHAR(50),
  progress_percent INTEGER DEFAULT 0,

  -- Metadata
  version VARCHAR(10) DEFAULT '1.0',
  icd10 VARCHAR(20)[],
  setting_coverage JSONB DEFAULT '{"ED": true, "HOSP": true, "OPD": true, "ICU": false}',

  -- Quality
  quality_score INTEGER,

  -- Cost tracking
  total_cost_usd DECIMAL(10, 6) DEFAULT 0,

  -- Error handling
  error_message TEXT,
  retry_count INTEGER DEFAULT 0,

  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  approved_at TIMESTAMPTZ,
  approved_by VARCHAR(255)
);

-- Generation jobs table (tracks each stage)
CREATE TABLE generation_jobs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  plan_id UUID REFERENCES plans(id) ON DELETE CASCADE,

  -- Stage: generate, verify_clinical, verify_citation, complete
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
  raw_response TEXT,
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
  clinical_raw TEXT,

  -- Citation verification (Gemini)
  citation_status VARCHAR(50),
  citation_model VARCHAR(100),
  citation_result JSONB,
  citation_raw TEXT,

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

-- Indexes for performance
CREATE INDEX idx_plans_status ON plans(status);
CREATE INDEX idx_plans_slug ON plans(slug);
CREATE INDEX idx_plans_created ON plans(created_at DESC);
CREATE INDEX idx_plans_queued ON plans(status) WHERE status = 'queued';
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

-- Function to trigger Edge Function when new plan is queued
CREATE OR REPLACE FUNCTION trigger_plan_generation()
RETURNS TRIGGER AS $$
BEGIN
  -- Call the Edge Function via pg_net (async HTTP call)
  PERFORM net.http_post(
    url := current_setting('app.settings.supabase_url') || '/functions/v1/generate-plan',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', 'Bearer ' || current_setting('app.settings.service_role_key')
    ),
    body := jsonb_build_object('plan_id', NEW.id)
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger on new plan insert
CREATE TRIGGER on_plan_queued
  AFTER INSERT ON plans
  FOR EACH ROW
  WHEN (NEW.status = 'queued')
  EXECUTE FUNCTION trigger_plan_generation();

-- Row Level Security
ALTER TABLE plans ENABLE ROW LEVEL SECURITY;
ALTER TABLE generation_jobs ENABLE ROW LEVEL SECURITY;
ALTER TABLE verification_reports ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;

-- Public read for approved plans
CREATE POLICY "Public read approved plans" ON plans
  FOR SELECT USING (status = 'approved');

-- Anon can read plans in progress (for status polling)
CREATE POLICY "Anon read own plans" ON plans
  FOR SELECT USING (true);

-- Service role full access
CREATE POLICY "Service role full access plans" ON plans
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access jobs" ON generation_jobs
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access reports" ON verification_reports
  FOR ALL TO service_role USING (true);

CREATE POLICY "Service role full access audit" ON audit_log
  FOR ALL TO service_role USING (true);

-- Public read for jobs (status tracking)
CREATE POLICY "Public read jobs" ON generation_jobs
  FOR SELECT USING (true);

-- Public read for reports
CREATE POLICY "Public read reports" ON verification_reports
  FOR SELECT USING (true);
```

**IMPORTANT: After creating your Supabase project:**
1. Go to SQL Editor and run this schema
2. Go to Project Settings → Database → Connection string
3. Set the app settings for the trigger:
```sql
ALTER DATABASE postgres SET "app.settings.supabase_url" = 'https://YOUR_PROJECT.supabase.co';
ALTER DATABASE postgres SET "app.settings.service_role_key" = 'YOUR_SERVICE_ROLE_KEY';
```

---

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
│       │   └── route.ts            # POST - queue generation (fast)
│       ├── status/
│       │   └── [planId]/
│       │       └── route.ts        # GET - check status (fast)
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
│   ├── GenerationForm.tsx
│   ├── PlanCard.tsx
│   ├── PlanViewer.tsx
│   ├── ReviewQueue.tsx
│   ├── StatusTracker.tsx           # Real-time status with polling
│   └── Navigation.tsx
├── lib/
│   ├── supabase/
│   │   ├── client.ts               # Browser client
│   │   └── server.ts               # Server client
│   ├── utils/
│   │   ├── costs.ts                # Token cost calculations
│   │   └── slug.ts                 # Slug generation
│   └── types.ts                    # TypeScript types
└── styles/
    └── globals.css

supabase/
├── functions/
│   └── generate-plan/
│       └── index.ts                # Edge Function - main pipeline
└── schema.sql
```

---

## STEP 5: SUPABASE EDGE FUNCTION (THE HEAVY LIFTER)

This is where the AI work happens. Edge Functions have **no timeout limit** on paid plans (400 seconds on free).

Create `supabase/functions/generate-plan/index.ts`:

```typescript
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

// Pricing per million tokens (January 2026)
const PRICING = {
  'gpt-4o': { input: 2.5, output: 10 },
  'claude-sonnet-4': { input: 3, output: 15 },
  'gemini-1.5-pro': { input: 1.25, output: 5 },
}

function calculateCost(model: string, inputTokens: number, outputTokens: number): number {
  const p = PRICING[model] || PRICING['gpt-4o']
  return (inputTokens * p.input / 1_000_000) + (outputTokens * p.output / 1_000_000)
}

// ============================================================================
// SYSTEM PROMPTS
// ============================================================================

const GENERATION_SYSTEM_PROMPT = `You are a clinical decision support generator specializing in neurology. You create comprehensive, evidence-based treatment plans for physicians in Emergency Departments, Hospitals, Outpatient Clinics, and ICUs.

Your output must be:
1. ACCURATE - Drug dosing, diagnostic criteria, and clinical claims must be factually correct
2. COMPLETE - All 8 sections populated with appropriate setting coverage
3. SAFE - Critical contraindications, monitoring requirements, and red flags included
4. ACTIONABLE - Written as physician-ready directives, not suggestions

## OUTPUT FORMAT

Generate plans using this EXACT markdown structure:

---
title: [Diagnosis Name]
version: 1.0
status: draft
icd10: [Primary ICD-10 code]
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
[Include 5-10 essential labs relevant to the diagnosis]

### 1B. Extended Workup

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
[Include 5-10 second-line labs]

### 1C. Rare/Specialized

| Test | ED | HOSP | OPD | ICU | Rationale | Target Finding |
|------|:--:|:----:|:---:|:---:|-----------|----------------|
[Include 3-5 specialized tests]

---

## 2. DIAGNOSTIC IMAGING & STUDIES

### 2A. Essential/First-line

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|
[Include relevant imaging - MRI, CT, etc.]

### 2B. Extended

| Study | ED | HOSP | OPD | ICU | Timing | Target Finding | Contraindications |
|-------|:--:|:----:|:---:|:---:|--------|----------------|-------------------|

---

## 3. TREATMENT

### 3A. Acute/Emergent

| Treatment | Route | Indication | Dosing | Contraindications | Monitoring | ED | HOSP | OPD | ICU |
|-----------|-------|------------|--------|-------------------|------------|:--:|:----:|:---:|:---:|

**CRITICAL: Every medication on its own row. Use structured dosing format:**
[dose] :: [route] :: [frequency] :: [full instructions including titration and max dose]

Example: 5 mg :: PO :: TID :: Start 5 mg TID; titrate by 5 mg/dose every 3 days; max 80 mg/day

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
[Include at least 5 relevant referrals]

### 4B. Patient Instructions

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
[Include at least 5 specific instructions with return precautions]

### 4C. Lifestyle & Prevention

| Recommendation | ED | HOSP | OPD |
|----------------|:--:|:----:|:---:|
[Include at least 3 lifestyle modifications]

---

## 5. DIFFERENTIAL DIAGNOSIS

| Alternative Diagnosis | Key Distinguishing Features | Tests to Differentiate |
|-----------------------|----------------------------|------------------------|
[Include 5-8 differential diagnoses]

---

## 6. MONITORING PARAMETERS

| Parameter | ED | HOSP | OPD | ICU | Frequency | Target/Threshold | Action if Abnormal |
|-----------|:--:|:----:|:---:|:---:|-----------|------------------|-------------------|
[Include vital signs, lab values, clinical assessments]

---

## 7. DISPOSITION CRITERIA

| Disposition | Criteria |
|-------------|----------|
| Discharge home | [specific criteria] |
| Admit to floor | [specific criteria] |
| Admit to ICU | [specific criteria] |
| Transfer to higher level | [specific criteria] |

---

## 8. EVIDENCE & REFERENCES

| Recommendation | Evidence Level | Source |
|----------------|----------------|--------|
[Include 10-15 key references with author, journal, year]

## CRITICAL REQUIREMENTS

1. EVERY medication must be on its own row - never group drugs
2. Use structured dosing: [dose] :: [route] :: [frequency] :: [instructions]
3. Include starting dose, titration schedule, and maximum dose
4. Evaluate ALL settings (ED, HOSP, OPD, ICU) for each item
5. Use "-" only when truly not applicable
6. Write as checkbox-ready directives, not suggestions
7. Include complete contraindications and monitoring for each drug`

const CLINICAL_VERIFICATION_SYSTEM_PROMPT = `You are a clinical pharmacist and board-certified neurologist reviewing a clinical decision support plan for accuracy and safety.

VERIFY EACH MEDICATION FOR:
1. Dose within standard therapeutic range (check mg, frequency, max daily dose)
2. Route appropriate for indication and setting
3. All critical contraindications listed (drug-specific, not generic)
4. Drug-drug interactions that should be mentioned
5. Monitoring parameters appropriate and complete

OUTPUT FORMAT:

For each medication, output ONE line:
✅ OK: [Drug name] - [brief verification note]
⚠️ FLAG: [Drug name] - [specific concern for physician review]
❌ ERROR: [Drug name] - [critical safety issue - MUST FIX]

Then provide a JSON summary block:

\`\`\`json
{
  "status": "passed" | "flagged" | "failed",
  "medications_reviewed": 0,
  "ok_count": 0,
  "flagged_count": 0,
  "error_count": 0,
  "errors": [
    {
      "medication": "Drug Name",
      "issue": "Specific problem",
      "current": "What the plan says",
      "recommended": "What it should say",
      "severity": "critical" | "high" | "medium",
      "auto_fixable": false
    }
  ],
  "flags": [
    {
      "medication": "Drug Name",
      "issue": "Concern requiring physician review",
      "severity": "medium" | "low"
    }
  ],
  "suggested_additions": [
    "Missing contraindication or interaction to add"
  ]
}
\`\`\`

IMPORTANT:
- Be SPECIFIC about dose issues (e.g., "Max is 3200mg/day, plan says 4000mg")
- Flag drug interactions (e.g., "SSRIs + triptans = serotonin syndrome risk")
- Check pediatric vs adult dosing if age not specified
- Verify renal/hepatic adjustment recommendations where needed`

const CITATION_VERIFICATION_SYSTEM_PROMPT = `You are a medical librarian verifying citations in a clinical document.

For each citation in Section 8 (Evidence & References):
1. Search your knowledge for the article/guideline
2. Verify it exists and is accurately cited
3. Note the PubMed ID (PMID) if you know it
4. Flag any that appear fabricated or inaccurate

OUTPUT FORMAT for each citation:
✅ VERIFIED: [Citation] → PMID: [number if known] | Accurate
⚠️ PARTIAL: [Citation] → [Issue: wrong year, wrong journal, etc.] | Correction: [correct info]
❌ NOT FOUND: [Citation] → Appears fabricated or cannot verify | Recommend: remove or replace
❓ UNABLE: [Citation] → Cannot verify (obscure source) | Flag for manual check

Then provide a JSON summary:

\`\`\`json
{
  "status": "passed" | "flagged" | "failed",
  "total_citations": 0,
  "verified_count": 0,
  "partial_count": 0,
  "not_found_count": 0,
  "unable_count": 0,
  "corrections": [
    {
      "original": "Incorrect citation",
      "corrected": "Correct citation",
      "pmid": "12345678",
      "auto_fixable": true
    }
  ],
  "pmids_to_add": [
    {
      "citation": "Author et al. Journal Year",
      "pmid": "12345678",
      "link": "https://pubmed.ncbi.nlm.nih.gov/12345678/"
    }
  ],
  "flagged_for_removal": [
    "Citation that appears fabricated"
  ]
}
\`\`\`

IMPORTANT:
- NEVER fabricate a PMID - only include if you are confident
- Mark as UNABLE if you cannot verify (better than guessing)
- Common red flags: implausible author combinations, non-existent journals, wrong decades`

// ============================================================================
// MAIN HANDLER
// ============================================================================

serve(async (req) => {
  // Handle CORS
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { plan_id } = await req.json()

    if (!plan_id) {
      return new Response(
        JSON.stringify({ error: 'plan_id required' }),
        { status: 400, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
      )
    }

    // Initialize Supabase client
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    )

    // Fetch the plan
    const { data: plan, error: fetchError } = await supabase
      .from('plans')
      .select('*')
      .eq('id', plan_id)
      .single()

    if (fetchError || !plan) {
      throw new Error(\`Plan not found: \${plan_id}\`)
    }

    // Update status to generating
    await supabase
      .from('plans')
      .update({
        status: 'generating',
        started_at: new Date().toISOString(),
        progress_percent: 10
      })
      .eq('id', plan_id)

    let totalCost = 0

    // ========================================================================
    // STAGE 1: GENERATE PLAN WITH GPT-4o
    // ========================================================================
    console.log('Stage 1: Generating plan with GPT-4o...')

    await logJob(supabase, plan_id, 'generate', 'running')

    const genStart = Date.now()
    const openaiResponse = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': \`Bearer \${Deno.env.get('OPENAI_API_KEY')}\`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'gpt-4o',
        messages: [
          { role: 'system', content: GENERATION_SYSTEM_PROMPT },
          { role: 'user', content: \`Generate a comprehensive clinical decision support plan for: \${plan.diagnosis} - \${plan.modifier || 'New Diagnosis'}

Focus on evidence-based recommendations with complete medication dosing, contraindications, and monitoring requirements. Include all 8 sections with thorough coverage.\` }
        ],
        max_tokens: 16000,
        temperature: 0.3
      })
    })

    if (!openaiResponse.ok) {
      const err = await openaiResponse.text()
      throw new Error(\`OpenAI error: \${err}\`)
    }

    const openaiData = await openaiResponse.json()
    const generatedPlan = openaiData.choices[0].message.content
    const genCost = calculateCost('gpt-4o', openaiData.usage.prompt_tokens, openaiData.usage.completion_tokens)
    totalCost += genCost

    await logJob(supabase, plan_id, 'generate', 'completed', {
      model: 'gpt-4o',
      input_tokens: openaiData.usage.prompt_tokens,
      output_tokens: openaiData.usage.completion_tokens,
      cost_usd: genCost,
      duration_ms: Date.now() - genStart,
      result: { preview: generatedPlan.substring(0, 500) }
    })

    // Update plan with generated content
    await supabase
      .from('plans')
      .update({
        content_md: generatedPlan,
        status: 'verifying_clinical',
        progress_percent: 40
      })
      .eq('id', plan_id)

    // ========================================================================
    // STAGE 2A: CLINICAL VERIFICATION WITH CLAUDE
    // ========================================================================
    console.log('Stage 2A: Clinical verification with Claude...')

    await supabase.from('plans').update({ current_stage: 'verify_clinical' }).eq('id', plan_id)
    await logJob(supabase, plan_id, 'verify_clinical', 'running')

    const clinicalStart = Date.now()
    const claudeResponse = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'x-api-key': Deno.env.get('ANTHROPIC_API_KEY') ?? '',
        'anthropic-version': '2023-06-01',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 4000,
        system: CLINICAL_VERIFICATION_SYSTEM_PROMPT,
        messages: [
          { role: 'user', content: \`Review this clinical plan for medication safety and accuracy:\n\n\${generatedPlan}\` }
        ]
      })
    })

    if (!claudeResponse.ok) {
      const err = await claudeResponse.text()
      throw new Error(\`Claude error: \${err}\`)
    }

    const claudeData = await claudeResponse.json()
    const clinicalResult = claudeData.content[0].text
    const clinicalCost = calculateCost('claude-sonnet-4', claudeData.usage.input_tokens, claudeData.usage.output_tokens)
    totalCost += clinicalCost

    // Parse JSON from response
    const clinicalJsonMatch = clinicalResult.match(/```json\n([\s\S]*?)\n```/)
    const clinicalParsed = clinicalJsonMatch ? JSON.parse(clinicalJsonMatch[1]) : { status: 'unknown' }

    await logJob(supabase, plan_id, 'verify_clinical', 'completed', {
      model: 'claude-sonnet-4',
      input_tokens: claudeData.usage.input_tokens,
      output_tokens: claudeData.usage.output_tokens,
      cost_usd: clinicalCost,
      duration_ms: Date.now() - clinicalStart,
      result: clinicalParsed
    })

    await supabase.from('plans').update({ progress_percent: 60 }).eq('id', plan_id)

    // ========================================================================
    // STAGE 2B: CITATION VERIFICATION WITH GEMINI
    // ========================================================================
    console.log('Stage 2B: Citation verification with Gemini...')

    await supabase.from('plans').update({
      status: 'verifying_citation',
      current_stage: 'verify_citation'
    }).eq('id', plan_id)

    await logJob(supabase, plan_id, 'verify_citation', 'running')

    const citationStart = Date.now()
    const geminiResponse = await fetch(\`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=\${Deno.env.get('GEMINI_API_KEY')}\`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          role: 'user',
          parts: [{ text: \`\${CITATION_VERIFICATION_SYSTEM_PROMPT}\n\nVerify the citations in this clinical plan:\n\n\${generatedPlan}\` }]
        }],
        generationConfig: {
          maxOutputTokens: 4000,
          temperature: 0.2
        }
      })
    })

    if (!geminiResponse.ok) {
      const err = await geminiResponse.text()
      throw new Error(\`Gemini error: \${err}\`)
    }

    const geminiData = await geminiResponse.json()
    const citationResult = geminiData.candidates[0].content.parts[0].text
    const citationCost = calculateCost('gemini-1.5-pro',
      geminiData.usageMetadata?.promptTokenCount || 5000,
      geminiData.usageMetadata?.candidatesTokenCount || 2000
    )
    totalCost += citationCost

    // Parse JSON from response
    const citationJsonMatch = citationResult.match(/```json\n([\s\S]*?)\n```/)
    const citationParsed = citationJsonMatch ? JSON.parse(citationJsonMatch[1]) : { status: 'unknown' }

    await logJob(supabase, plan_id, 'verify_citation', 'completed', {
      model: 'gemini-1.5-pro',
      input_tokens: geminiData.usageMetadata?.promptTokenCount || 5000,
      output_tokens: geminiData.usageMetadata?.candidatesTokenCount || 2000,
      cost_usd: citationCost,
      duration_ms: Date.now() - citationStart,
      result: citationParsed
    })

    await supabase.from('plans').update({ progress_percent: 80 }).eq('id', plan_id)

    // ========================================================================
    // STAGE 3: MERGE RESULTS AND FINALIZE
    // ========================================================================
    console.log('Stage 3: Merging results...')

    const humanReviewRequired =
      clinicalParsed.status === 'failed' ||
      clinicalParsed.error_count > 0 ||
      citationParsed.status === 'failed' ||
      (citationParsed.not_found_count || 0) > 2

    const reviewItems: string[] = [
      ...(clinicalParsed.errors?.map((e: any) => \`CLINICAL: \${e.medication} - \${e.issue}\`) || []),
      ...(clinicalParsed.flags?.map((f: any) => \`FLAG: \${f.medication} - \${f.issue}\`) || []),
      ...(citationParsed.flagged_for_removal?.map((c: string) => \`CITATION: Remove - \${c}\`) || [])
    ]

    // Save verification report
    await supabase.from('verification_reports').insert({
      plan_id,
      clinical_status: clinicalParsed.status,
      clinical_model: 'claude-sonnet-4',
      clinical_result: clinicalParsed,
      clinical_raw: clinicalResult,
      citation_status: citationParsed.status,
      citation_model: 'gemini-1.5-pro',
      citation_result: citationParsed,
      citation_raw: citationResult,
      overall_status: humanReviewRequired ? 'flagged' : 'passed',
      human_review_required: humanReviewRequired,
      human_review_items: reviewItems
    })

    // Update plan as complete
    await supabase
      .from('plans')
      .update({
        status: 'review',
        current_stage: 'complete',
        progress_percent: 100,
        total_cost_usd: totalCost,
        completed_at: new Date().toISOString()
      })
      .eq('id', plan_id)

    // Log completion
    await supabase.from('audit_log').insert({
      plan_id,
      action: 'generation_complete',
      details: {
        total_cost: totalCost,
        human_review_required: humanReviewRequired,
        clinical_status: clinicalParsed.status,
        citation_status: citationParsed.status
      }
    })

    console.log(\`Plan \${plan_id} completed. Cost: $\${totalCost.toFixed(4)}\`)

    return new Response(
      JSON.stringify({
        success: true,
        plan_id,
        cost: totalCost,
        human_review_required: humanReviewRequired
      }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )

  } catch (error) {
    console.error('Pipeline error:', error)

    // Try to update plan status to failed
    try {
      const { plan_id } = await req.json()
      const supabase = createClient(
        Deno.env.get('SUPABASE_URL') ?? '',
        Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
      )
      await supabase
        .from('plans')
        .update({
          status: 'failed',
          error_message: String(error)
        })
        .eq('id', plan_id)
    } catch (e) {
      // Ignore - couldn't update
    }

    return new Response(
      JSON.stringify({ error: String(error) }),
      { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )
  }
})

// Helper to log job stages
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
      .eq('status', 'running')
  }
}
```

**Deploy the Edge Function:**
```bash
# Set secrets first
npx supabase secrets set OPENAI_API_KEY=your_key
npx supabase secrets set ANTHROPIC_API_KEY=your_key
npx supabase secrets set GEMINI_API_KEY=your_key

# Deploy
npx supabase functions deploy generate-plan
```

---

## STEP 6: VERCEL API ROUTES (FAST - NO TIMEOUTS)

These routes just queue jobs and check status - they complete in <2 seconds.

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

Create `src/lib/utils/slug.ts`:
```typescript
export function generateSlug(diagnosis: string, modifier: string): string {
  return \`\${diagnosis}-\${modifier}\`
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
}
```

Create `src/app/api/generate/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'
import { generateSlug } from '@/lib/utils/slug'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { diagnosis, modifier = 'new-diagnosis' } = body

    if (!diagnosis) {
      return NextResponse.json({ error: 'Diagnosis is required' }, { status: 400 })
    }

    const supabase = createServiceClient()
    const slug = generateSlug(diagnosis, modifier)

    // Check if plan with this slug already exists
    const { data: existing } = await supabase
      .from('plans')
      .select('id, slug')
      .eq('slug', slug)
      .single()

    if (existing) {
      return NextResponse.json({
        success: true,
        planId: existing.id,
        slug: existing.slug,
        message: 'Plan already exists'
      })
    }

    // Create plan record - this triggers the Edge Function automatically
    const { data: plan, error } = await supabase
      .from('plans')
      .insert({
        diagnosis,
        modifier,
        slug,
        title: \`\${diagnosis} - \${modifier.replace('-', ' ')}\`,
        status: 'queued'
      })
      .select()
      .single()

    if (error) {
      throw error
    }

    // Return immediately - Edge Function will process in background
    return NextResponse.json({
      success: true,
      planId: plan.id,
      slug: plan.slug,
      status: 'queued',
      message: 'Generation started'
    })

  } catch (error) {
    console.error('Generate error:', error)
    return NextResponse.json(
      { error: 'Failed to queue generation', details: String(error) },
      { status: 500 }
    )
  }
}
```

Create `src/app/api/status/[planId]/route.ts`:
```typescript
import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase/server'

export async function GET(
  request: NextRequest,
  { params }: { params: { planId: string } }
) {
  try {
    const supabase = createServiceClient()

    // Fetch plan and jobs
    const [planResult, jobsResult] = await Promise.all([
      supabase
        .from('plans')
        .select('id, slug, status, current_stage, progress_percent, error_message, total_cost_usd')
        .eq('id', params.planId)
        .single(),
      supabase
        .from('generation_jobs')
        .select('stage, status, duration_ms, cost_usd')
        .eq('plan_id', params.planId)
        .order('created_at', { ascending: true })
    ])

    if (planResult.error || !planResult.data) {
      return NextResponse.json({ error: 'Plan not found' }, { status: 404 })
    }

    const plan = planResult.data
    const jobs = jobsResult.data || []

    return NextResponse.json({
      planId: plan.id,
      slug: plan.slug,
      status: plan.status,
      currentStage: plan.current_stage,
      progressPercent: plan.progress_percent,
      error: plan.error_message,
      cost: plan.total_cost_usd,
      stages: jobs.map(j => ({
        stage: j.stage,
        status: j.status,
        durationMs: j.duration_ms,
        cost: j.cost_usd
      })),
      isComplete: ['review', 'approved', 'rejected', 'failed'].includes(plan.status)
    })

  } catch (error) {
    return NextResponse.json({ error: String(error) }, { status: 500 })
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

  const supabase = createServiceClient()

  let query = supabase
    .from('plans')
    .select('*', { count: 'exact' })
    .order('created_at', { ascending: false })
    .limit(limit)

  if (status) {
    query = query.eq('status', status)
  }

  const { data, error, count } = await query

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }

  return NextResponse.json({ plans: data, total: count })
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
  const { approved_by = 'physician', comments } = body

  const supabase = createServiceClient()

  const { data, error } = await supabase
    .from('plans')
    .update({
      status: 'approved',
      approved_at: new Date().toISOString(),
      approved_by
    })
    .eq('id', params.planId)
    .select()
    .single()

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }

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
  const { rejected_by = 'physician', reason } = body

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

---

## STEP 7: UI COMPONENTS

Create the UI with real-time status polling.

Create `src/app/layout.tsx`:
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

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation />
        <main className="min-h-screen bg-gray-50">{children}</main>
      </body>
    </html>
  )
}
```

Create `src/components/Navigation.tsx`:
```typescript
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { FileText, PlusCircle, CheckSquare, LayoutDashboard } from 'lucide-react'

export function Navigation() {
  const pathname = usePathname()

  const links = [
    { href: '/', label: 'Dashboard', icon: LayoutDashboard },
    { href: '/generate', label: 'Generate', icon: PlusCircle },
    { href: '/plans', label: 'Plans', icon: FileText },
    { href: '/review', label: 'Review', icon: CheckSquare },
  ]

  return (
    <nav className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <span className="text-xl font-bold text-blue-600">Clinical Plan Generator</span>
            <div className="hidden sm:ml-8 sm:flex sm:space-x-2">
              {links.map((link) => {
                const Icon = link.icon
                const isActive = pathname === link.href
                return (
                  <Link
                    key={link.href}
                    href={link.href}
                    className={\`inline-flex items-center px-3 py-2 text-sm font-medium rounded-md \${
                      isActive ? 'bg-blue-50 text-blue-700' : 'text-gray-600 hover:bg-gray-50'
                    }\`}
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

Create `src/components/StatusTracker.tsx`:
```typescript
'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { Loader2, CheckCircle, XCircle, Clock } from 'lucide-react'

interface StatusTrackerProps {
  planId: string
  onComplete?: (slug: string) => void
}

interface StatusData {
  planId: string
  slug: string
  status: string
  currentStage: string
  progressPercent: number
  error: string | null
  cost: number
  stages: Array<{
    stage: string
    status: string
    durationMs: number
    cost: number
  }>
  isComplete: boolean
}

export function StatusTracker({ planId, onComplete }: StatusTrackerProps) {
  const router = useRouter()
  const [status, setStatus] = useState<StatusData | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let interval: NodeJS.Timeout

    const checkStatus = async () => {
      try {
        const res = await fetch(\`/api/status/\${planId}\`)
        const data = await res.json()

        if (!res.ok) {
          setError(data.error)
          return
        }

        setStatus(data)

        if (data.isComplete) {
          clearInterval(interval)
          if (data.status === 'review' && onComplete) {
            setTimeout(() => onComplete(data.slug), 1500)
          }
        }
      } catch (err) {
        setError(String(err))
      }
    }

    checkStatus()
    interval = setInterval(checkStatus, 3000) // Poll every 3 seconds

    return () => clearInterval(interval)
  }, [planId, onComplete])

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-4">
        <div className="flex items-center text-red-700">
          <XCircle className="w-5 h-5 mr-2" />
          Error: {error}
        </div>
      </div>
    )
  }

  if (!status) {
    return (
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <div className="flex items-center text-blue-700">
          <Loader2 className="w-5 h-5 mr-2 animate-spin" />
          Connecting...
        </div>
      </div>
    )
  }

  const stages = [
    { key: 'generate', label: 'Generate Plan', sublabel: 'GPT-4o' },
    { key: 'verify_clinical', label: 'Clinical Check', sublabel: 'Claude' },
    { key: 'verify_citation', label: 'Citation Check', sublabel: 'Gemini' },
  ]

  const getStageStatus = (key: string) => {
    const stage = status.stages.find(s => s.stage === key)
    return stage?.status || 'pending'
  }

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-6">
      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-gray-700">
            {status.status === 'failed' ? 'Generation Failed' :
             status.isComplete ? 'Complete!' :
             'Generating Plan...'}
          </span>
          <span className="text-sm text-gray-500">{status.progressPercent}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2">
          <div
            className={\`h-2 rounded-full transition-all duration-500 \${
              status.status === 'failed' ? 'bg-red-500' :
              status.isComplete ? 'bg-green-500' : 'bg-blue-500'
            }\`}
            style={{ width: \`\${status.progressPercent}%\` }}
          />
        </div>
      </div>

      <div className="space-y-3">
        {stages.map((stage, idx) => {
          const stageStatus = getStageStatus(stage.key)
          const stageData = status.stages.find(s => s.stage === stage.key)

          return (
            <div key={stage.key} className="flex items-center justify-between">
              <div className="flex items-center">
                {stageStatus === 'completed' ? (
                  <CheckCircle className="w-5 h-5 text-green-500 mr-3" />
                ) : stageStatus === 'running' ? (
                  <Loader2 className="w-5 h-5 text-blue-500 animate-spin mr-3" />
                ) : stageStatus === 'failed' ? (
                  <XCircle className="w-5 h-5 text-red-500 mr-3" />
                ) : (
                  <Clock className="w-5 h-5 text-gray-300 mr-3" />
                )}
                <div>
                  <p className="text-sm font-medium text-gray-900">{stage.label}</p>
                  <p className="text-xs text-gray-500">{stage.sublabel}</p>
                </div>
              </div>
              {stageData && stageStatus === 'completed' && (
                <div className="text-right">
                  <p className="text-xs text-gray-500">
                    {(stageData.durationMs / 1000).toFixed(1)}s
                  </p>
                  <p className="text-xs text-green-600">
                    ${stageData.cost?.toFixed(4)}
                  </p>
                </div>
              )}
            </div>
          )
        })}
      </div>

      {status.isComplete && status.cost && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <div className="flex justify-between text-sm">
            <span className="text-gray-600">Total Cost</span>
            <span className="font-medium text-green-600">${status.cost.toFixed(4)}</span>
          </div>
        </div>
      )}

      {status.status === 'failed' && status.error && (
        <div className="mt-4 p-3 bg-red-50 rounded text-sm text-red-700">
          {status.error}
        </div>
      )}
    </div>
  )
}
```

Create `src/app/page.tsx` (Dashboard):
```typescript
import Link from 'next/link'
import { createServiceClient } from '@/lib/supabase/server'
import { PlusCircle, FileText, CheckSquare, DollarSign } from 'lucide-react'

export const dynamic = 'force-dynamic'

export default async function Dashboard() {
  const supabase = createServiceClient()

  const [
    { count: totalPlans },
    { count: reviewCount },
    { count: approvedCount },
    { data: recentPlans },
    { data: costData }
  ] = await Promise.all([
    supabase.from('plans').select('*', { count: 'exact', head: true }),
    supabase.from('plans').select('*', { count: 'exact', head: true }).eq('status', 'review'),
    supabase.from('plans').select('*', { count: 'exact', head: true }).eq('status', 'approved'),
    supabase.from('plans').select('*').order('created_at', { ascending: false }).limit(5),
    supabase.from('plans').select('total_cost_usd').not('total_cost_usd', 'is', null)
  ])

  const totalCost = costData?.reduce((sum, p) => sum + (p.total_cost_usd || 0), 0) || 0

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-8">Dashboard</h1>

      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white rounded-lg shadow p-4">
          <div className="flex items-center">
            <FileText className="w-8 h-8 text-blue-500" />
            <div className="ml-3">
              <p className="text-2xl font-bold">{totalPlans || 0}</p>
              <p className="text-sm text-gray-500">Total Plans</p>
            </div>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <div className="flex items-center">
            <CheckSquare className="w-8 h-8 text-yellow-500" />
            <div className="ml-3">
              <p className="text-2xl font-bold">{reviewCount || 0}</p>
              <p className="text-sm text-gray-500">Pending Review</p>
            </div>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <div className="flex items-center">
            <CheckSquare className="w-8 h-8 text-green-500" />
            <div className="ml-3">
              <p className="text-2xl font-bold">{approvedCount || 0}</p>
              <p className="text-sm text-gray-500">Approved</p>
            </div>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-4">
          <div className="flex items-center">
            <DollarSign className="w-8 h-8 text-green-500" />
            <div className="ml-3">
              <p className="text-2xl font-bold">${totalCost.toFixed(2)}</p>
              <p className="text-sm text-gray-500">Total Spent</p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="flex gap-4 mb-8">
        <Link
          href="/generate"
          className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          <PlusCircle className="w-5 h-5 mr-2" />
          Generate New Plan
        </Link>
        {(reviewCount || 0) > 0 && (
          <Link
            href="/review"
            className="inline-flex items-center px-4 py-2 bg-yellow-500 text-white rounded-lg hover:bg-yellow-600"
          >
            Review Queue ({reviewCount})
          </Link>
        )}
      </div>

      {/* Recent Plans */}
      <div className="bg-white rounded-lg shadow">
        <div className="px-6 py-4 border-b"><h2 className="font-semibold">Recent Plans</h2></div>
        <div className="divide-y">
          {recentPlans?.map((plan) => (
            <Link key={plan.id} href={\`/plans/\${plan.slug}\`} className="block px-6 py-4 hover:bg-gray-50">
              <div className="flex justify-between">
                <div>
                  <p className="font-medium">{plan.title}</p>
                  <p className="text-sm text-gray-500">{new Date(plan.created_at).toLocaleDateString()}</p>
                </div>
                <span className={\`px-3 py-1 text-sm rounded-full h-fit \${
                  plan.status === 'approved' ? 'bg-green-100 text-green-800' :
                  plan.status === 'review' ? 'bg-yellow-100 text-yellow-800' :
                  plan.status === 'generating' || plan.status === 'verifying_clinical' || plan.status === 'verifying_citation'
                    ? 'bg-blue-100 text-blue-800' :
                  plan.status === 'failed' ? 'bg-red-100 text-red-800' :
                  'bg-gray-100 text-gray-800'
                }\`}>
                  {plan.status}
                </span>
              </div>
            </Link>
          ))}
          {(!recentPlans || recentPlans.length === 0) && (
            <div className="px-6 py-12 text-center text-gray-500">
              No plans yet. Generate your first plan!
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
```

Create `src/app/generate/page.tsx`:
```typescript
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Sparkles } from 'lucide-react'
import { StatusTracker } from '@/components/StatusTracker'

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
  'Bell Palsy',
  'Trigeminal Neuralgia',
  'Essential Tremor'
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
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [planId, setPlanId] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const finalDiagnosis = diagnosis === 'custom' ? customDiagnosis : diagnosis

    if (!finalDiagnosis) {
      setError('Please select or enter a diagnosis')
      return
    }

    setIsSubmitting(true)
    setError(null)

    try {
      const res = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ diagnosis: finalDiagnosis, modifier })
      })

      const data = await res.json()

      if (!res.ok) {
        throw new Error(data.error || 'Failed to start generation')
      }

      setPlanId(data.planId)

    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
      setIsSubmitting(false)
    }
  }

  const handleComplete = (slug: string) => {
    router.push(\`/plans/\${slug}\`)
  }

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-2">Generate Clinical Plan</h1>
      <p className="text-gray-600 mb-8">Create an evidence-based clinical decision support plan</p>

      {!planId ? (
        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow p-6 space-y-6">
          <div>
            <label className="block text-sm font-medium mb-2">Diagnosis</label>
            <select
              value={diagnosis}
              onChange={(e) => setDiagnosis(e.target.value)}
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              disabled={isSubmitting}
            >
              <option value="">Select a diagnosis...</option>
              {DIAGNOSES.map((d) => (
                <option key={d} value={d}>{d}</option>
              ))}
              <option value="custom">Custom (enter below)</option>
            </select>
          </div>

          {diagnosis === 'custom' && (
            <div>
              <label className="block text-sm font-medium mb-2">Custom Diagnosis</label>
              <input
                type="text"
                value={customDiagnosis}
                onChange={(e) => setCustomDiagnosis(e.target.value)}
                placeholder="Enter diagnosis..."
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                disabled={isSubmitting}
              />
            </div>
          )}

          <div>
            <label className="block text-sm font-medium mb-2">Plan Type</label>
            <div className="grid grid-cols-2 gap-3">
              {MODIFIERS.map((m) => (
                <label
                  key={m.value}
                  className={\`flex items-center justify-center px-4 py-3 border rounded-lg cursor-pointer \${
                    modifier === m.value ? 'border-blue-500 bg-blue-50 text-blue-700' : 'border-gray-300 hover:border-gray-400'
                  }\`}
                >
                  <input
                    type="radio"
                    name="modifier"
                    value={m.value}
                    checked={modifier === m.value}
                    onChange={(e) => setModifier(e.target.value)}
                    className="sr-only"
                    disabled={isSubmitting}
                  />
                  {m.label}
                </label>
              ))}
            </div>
          </div>

          <div className="bg-gray-50 rounded-lg p-4 text-sm">
            <p><strong>Estimated cost:</strong> ~$0.27 per plan</p>
            <p className="text-gray-500 mt-1">GPT-4o + Claude verification + Gemini citation check</p>
          </div>

          {error && (
            <div className="bg-red-50 text-red-700 p-3 rounded-lg text-sm">{error}</div>
          )}

          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full flex items-center justify-center px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400"
          >
            <Sparkles className="w-5 h-5 mr-2" />
            {isSubmitting ? 'Starting...' : 'Generate Plan'}
          </button>
        </form>
      ) : (
        <StatusTracker planId={planId} onComplete={handleComplete} />
      )}
    </div>
  )
}
```

Create `src/app/plans/page.tsx`, `src/app/plans/[slug]/page.tsx`, and `src/app/review/page.tsx` following the same patterns from the previous version (I'll provide if needed, but they're similar - just display components).

---

## STEP 8: DEPLOYMENT INSTRUCTIONS

### 1. Create Supabase Project
1. Go to https://supabase.com
2. Create new project
3. Copy URL, anon key, and service role key

### 2. Run Database Schema
1. Go to SQL Editor in Supabase
2. Paste the entire schema from Step 3
3. Run it
4. Then run:
```sql
ALTER DATABASE postgres SET "app.settings.supabase_url" = 'https://YOUR_PROJECT.supabase.co';
ALTER DATABASE postgres SET "app.settings.service_role_key" = 'YOUR_SERVICE_ROLE_KEY';
```

### 3. Deploy Edge Function
```bash
cd your-project
npx supabase link --project-ref YOUR_PROJECT_REF
npx supabase secrets set OPENAI_API_KEY=sk-...
npx supabase secrets set ANTHROPIC_API_KEY=sk-ant-...
npx supabase secrets set GEMINI_API_KEY=AIza...
npx supabase functions deploy generate-plan
```

### 4. Configure Vercel
1. Push to GitHub
2. Import in Vercel
3. Add environment variables:
   - NEXT_PUBLIC_SUPABASE_URL
   - NEXT_PUBLIC_SUPABASE_ANON_KEY
   - SUPABASE_SERVICE_ROLE_KEY
4. Deploy

### 5. Test
1. Go to your Vercel URL
2. Click "Generate New Plan"
3. Select a diagnosis
4. Watch the status tracker update in real-time
5. Review the generated plan

---

## COST SUMMARY

| Model | Role | Cost per Plan |
|-------|------|---------------|
| GPT-4o | Generation | ~$0.15 |
| Claude Sonnet 4 | Clinical verification | ~$0.08 |
| Gemini 1.5 Pro | Citation verification | ~$0.04 |
| **Total** | | **~$0.27** |

---

## TROUBLESHOOTING

**If Edge Function times out:**
- Check Supabase logs: Dashboard → Edge Functions → Logs
- Increase timeout in Supabase settings

**If status stuck at "queued":**
- Check if Edge Function was triggered
- Verify database trigger is set up correctly
- Manually call: `curl -X POST https://YOUR_PROJECT.supabase.co/functions/v1/generate-plan -H "Authorization: Bearer YOUR_ANON_KEY" -d '{"plan_id":"..."}'`

**If API keys not working:**
- Verify they're set in Supabase secrets (not just env vars)
- Check Edge Function logs for specific errors

Now build all of this. Create each file completely. Ask me to fill in environment variables when done.
