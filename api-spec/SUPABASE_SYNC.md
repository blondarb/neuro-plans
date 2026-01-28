# Supabase Data Sync Strategy

> **Purpose:** How to sync clinical plan data between the neuro-plans repo (content generation) and your main Supabase/Vercel application (consumer).

---

## Architecture Options

### Option A: Supabase as Single Source of Truth (Recommended)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌────────────────────┐         ┌────────────────────────────────────┐  │
│  │  PLAN GENERATOR    │         │  YOUR MAIN APP (Supabase/Vercel)   │  │
│  │  (This pipeline)   │         │                                    │  │
│  │                    │         │  ┌──────────────────────────────┐  │  │
│  │  GPT-5.2           │         │  │  Supabase Tables             │  │  │
│  │  + Claude          │────────▶│  │  • plans                     │  │  │
│  │  + Gemini          │  writes │  │  • verification_reports      │  │  │
│  │                    │         │  │  • audit_log                 │  │  │
│  └────────────────────┘         │  └──────────────┬───────────────┘  │  │
│                                 │                 │                   │  │
│                                 │                 ▼                   │  │
│                                 │  ┌──────────────────────────────┐  │  │
│                                 │  │  Clinical Tool UI            │  │  │
│                                 │  │  (reads from Supabase)       │  │  │
│                                 │  └──────────────────────────────┘  │  │
│                                 │                                    │  │
│                                 └────────────────────────────────────┘  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Single database for everything
- Real-time updates via Supabase subscriptions
- Simpler architecture
- Easy querying from your main app

**Cons:**
- GitHub repo becomes secondary (just for backup/version control)
- Need to maintain Supabase schema

---

### Option B: GitHub as Source, Sync to Supabase

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌────────────────────┐         ┌────────────────────────────────────┐  │
│  │  NEURO-PLANS REPO  │         │  YOUR MAIN APP                     │  │
│  │  (GitHub)          │         │                                    │  │
│  │                    │         │  ┌──────────────────────────────┐  │  │
│  │  • docs/plans/*.md │ webhook │  │  Supabase                    │  │  │
│  │  • docs/data/      │────────▶│  │  (synced copy of plans.json)│  │  │
│  │    plans.json      │         │  └──────────────────────────────┘  │  │
│  │                    │         │                                    │  │
│  └────────────────────┘         └────────────────────────────────────┘  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Git history preserved
- Easy rollback via git
- Familiar workflow

**Cons:**
- Need sync mechanism
- Potential sync lag

---

## Recommended: Option A (Supabase-First)

Since you're building on Supabase/Vercel anyway, make Supabase the primary data store.

---

## Database Schema for Main App

### Core Tables

```sql
-- Plans table (same as pipeline, used by both)
CREATE TABLE clinical_plans (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Identity
  diagnosis VARCHAR(255) NOT NULL,
  modifier VARCHAR(50), -- 'new-diagnosis', 'exacerbation', etc.
  slug VARCHAR(255) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,

  -- Content (both formats for flexibility)
  content_md TEXT NOT NULL,
  content_json JSONB NOT NULL,

  -- Metadata
  version VARCHAR(10) DEFAULT '1.0',
  icd10 VARCHAR(20)[],
  cpt_codes VARCHAR(20)[],
  synonyms TEXT[],

  -- Status
  status VARCHAR(50) DEFAULT 'draft',
  -- draft, pending_review, approved, deployed, archived

  -- Quality
  quality_score INTEGER,
  verification_passed BOOLEAN DEFAULT false,
  last_verified_at TIMESTAMPTZ,

  -- Tracking
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  approved_at TIMESTAMPTZ,
  approved_by VARCHAR(255),

  -- Settings
  setting_coverage JSONB DEFAULT '{"ED": true, "HOSP": true, "OPD": true, "ICU": false}'
);

-- Enable full-text search on plans
ALTER TABLE clinical_plans ADD COLUMN search_vector tsvector
  GENERATED ALWAYS AS (
    setweight(to_tsvector('english', coalesce(title, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(diagnosis, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(array_to_string(synonyms, ' '), '')), 'B') ||
    setweight(to_tsvector('english', coalesce(content_md, '')), 'C')
  ) STORED;

CREATE INDEX idx_plans_search ON clinical_plans USING GIN(search_vector);

-- RLS policies (Row Level Security)
ALTER TABLE clinical_plans ENABLE ROW LEVEL SECURITY;

-- Anyone can read approved plans
CREATE POLICY "Public read approved plans"
  ON clinical_plans FOR SELECT
  USING (status = 'deployed');

-- Authenticated users can read all plans
CREATE POLICY "Authenticated read all"
  ON clinical_plans FOR SELECT
  TO authenticated
  USING (true);

-- Only service role can insert/update
CREATE POLICY "Service role write"
  ON clinical_plans FOR ALL
  TO service_role
  USING (true);
```

### Views for Your Main App

```sql
-- Simplified view for clinical tool
CREATE VIEW clinical_plans_public AS
SELECT
  id,
  slug,
  title,
  diagnosis,
  icd10,
  content_json,
  setting_coverage,
  version,
  updated_at
FROM clinical_plans
WHERE status = 'deployed';

-- Search function
CREATE OR REPLACE FUNCTION search_plans(query text)
RETURNS SETOF clinical_plans_public AS $$
  SELECT * FROM clinical_plans_public
  WHERE search_vector @@ plainto_tsquery('english', query)
  ORDER BY ts_rank(search_vector, plainto_tsquery('english', query)) DESC;
$$ LANGUAGE sql;
```

---

## API Functions for Your Main App

### Vercel API Routes

```typescript
// app/api/plans/route.ts
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_KEY!
);

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q');
  const setting = searchParams.get('setting'); // ED, HOSP, OPD, ICU

  let dbQuery = supabase
    .from('clinical_plans_public')
    .select('*');

  // Full-text search
  if (query) {
    const { data } = await supabase.rpc('search_plans', { query });
    return Response.json(data);
  }

  // Filter by setting
  if (setting) {
    dbQuery = dbQuery.filter(`setting_coverage->>${setting}`, 'eq', true);
  }

  const { data, error } = await dbQuery.order('title');

  if (error) {
    return Response.json({ error: error.message }, { status: 500 });
  }

  return Response.json(data);
}
```

```typescript
// app/api/plans/[slug]/route.ts
export async function GET(
  request: Request,
  { params }: { params: { slug: string } }
) {
  const { data, error } = await supabase
    .from('clinical_plans_public')
    .select('*')
    .eq('slug', params.slug)
    .single();

  if (error || !data) {
    return Response.json({ error: 'Plan not found' }, { status: 404 });
  }

  return Response.json(data);
}
```

---

## Real-Time Updates

### Subscribe to Plan Changes

```typescript
// In your React component
import { useEffect, useState } from 'react';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export function usePlans() {
  const [plans, setPlans] = useState([]);

  useEffect(() => {
    // Initial fetch
    const fetchPlans = async () => {
      const { data } = await supabase
        .from('clinical_plans_public')
        .select('*')
        .order('title');
      setPlans(data || []);
    };

    fetchPlans();

    // Subscribe to changes
    const subscription = supabase
      .channel('plans_changes')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'clinical_plans',
          filter: 'status=eq.deployed'
        },
        (payload) => {
          console.log('Plan changed:', payload);
          fetchPlans(); // Refetch on any change
        }
      )
      .subscribe();

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  return plans;
}
```

---

## Sync from GitHub (Optional Backup)

If you want to keep GitHub as a backup source:

### GitHub Action for Sync

```yaml
# .github/workflows/sync-to-supabase.yml
name: Sync Plans to Supabase

on:
  push:
    paths:
      - 'docs/data/plans.json'
    branches:
      - main

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Sync to Supabase
        env:
          SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          SUPABASE_SERVICE_KEY: ${{ secrets.SUPABASE_SERVICE_KEY }}
        run: |
          node scripts/sync-to-supabase.js
```

### Sync Script

```javascript
// scripts/sync-to-supabase.js
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_KEY
);

async function sync() {
  const plans = JSON.parse(fs.readFileSync('docs/data/plans.json', 'utf-8'));

  for (const [title, plan] of Object.entries(plans)) {
    const slug = title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');

    const { error } = await supabase
      .from('clinical_plans')
      .upsert({
        slug,
        title,
        diagnosis: title,
        content_json: plan,
        icd10: plan.icd10,
        version: plan.version,
        status: 'deployed',
        updated_at: new Date().toISOString()
      }, {
        onConflict: 'slug'
      });

    if (error) {
      console.error(`Error syncing ${title}:`, error);
    } else {
      console.log(`Synced: ${title}`);
    }
  }
}

sync();
```

---

## Accessing Plans from Your Main App

### React Component Example

```tsx
// components/ClinicalPlanViewer.tsx
'use client';

import { useState, useEffect } from 'react';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

interface ClinicalPlan {
  id: string;
  slug: string;
  title: string;
  content_json: {
    sections: Record<string, Record<string, any[]>>;
    differential: any[];
    evidence: any[];
  };
  setting_coverage: {
    ED: boolean;
    HOSP: boolean;
    OPD: boolean;
    ICU: boolean;
  };
}

export function ClinicalPlanViewer({ slug }: { slug: string }) {
  const [plan, setPlan] = useState<ClinicalPlan | null>(null);
  const [activeSetting, setActiveSetting] = useState<'ED' | 'HOSP' | 'OPD' | 'ICU'>('ED');

  useEffect(() => {
    async function fetchPlan() {
      const { data } = await supabase
        .from('clinical_plans_public')
        .select('*')
        .eq('slug', slug)
        .single();

      setPlan(data);
    }

    fetchPlan();
  }, [slug]);

  if (!plan) return <div>Loading...</div>;

  return (
    <div>
      <h1>{plan.title}</h1>

      {/* Setting selector */}
      <div className="flex gap-2 mb-4">
        {(['ED', 'HOSP', 'OPD', 'ICU'] as const).map((setting) => (
          <button
            key={setting}
            onClick={() => setActiveSetting(setting)}
            disabled={!plan.setting_coverage[setting]}
            className={`px-4 py-2 rounded ${
              activeSetting === setting ? 'bg-blue-600 text-white' : 'bg-gray-200'
            } ${!plan.setting_coverage[setting] ? 'opacity-50' : ''}`}
          >
            {setting}
          </button>
        ))}
      </div>

      {/* Render sections filtered by active setting */}
      {Object.entries(plan.content_json.sections).map(([sectionName, subsections]) => (
        <section key={sectionName} className="mb-6">
          <h2 className="text-xl font-bold">{sectionName}</h2>
          {Object.entries(subsections).map(([subsectionName, items]) => (
            <div key={subsectionName}>
              <h3 className="text-lg font-semibold">{subsectionName}</h3>
              <ul>
                {items
                  .filter((item: any) => item[activeSetting] && item[activeSetting] !== '-')
                  .map((item: any, idx: number) => (
                    <li key={idx} className="flex justify-between p-2 border-b">
                      <span>{item.item}</span>
                      <span className="text-blue-600">{item[activeSetting]}</span>
                    </li>
                  ))}
              </ul>
            </div>
          ))}
        </section>
      ))}
    </div>
  );
}
```

---

## Data Flow Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        COMPLETE DATA FLOW                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. GENERATION                                                          │
│     User submits diagnosis → Pipeline generates plan → Saves to Supabase│
│                                                                          │
│  2. VERIFICATION                                                         │
│     Plan in Supabase → Claude/Gemini verify → Update verification status│
│                                                                          │
│  3. APPROVAL                                                             │
│     Physician reviews in UI → Approves → Status = 'deployed'            │
│                                                                          │
│  4. CONSUMPTION                                                          │
│     Main app queries Supabase → Renders clinical tool → Real-time sync  │
│                                                                          │
│  5. BACKUP (Optional)                                                    │
│     Supabase → GitHub commit (for version history)                      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Version

v1.0 - January 2026
