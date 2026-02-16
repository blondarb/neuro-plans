# Neuro Plans -- Product Requirements Document

**Version:** 1.0
**Last Updated:** 2026-02-15
**Status:** v1.0 Submitted to App Store (Waiting for Review)
**Bundle ID:** com.neuroplans.app
**Platform:** iOS 17+ (iPhone and iPad)

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [Target Users & Personas](#2-target-users--personas)
3. [Core Features](#3-core-features)
4. [User Flows](#4-user-flows)
5. [Data Model](#5-data-model)
6. [Subscription & Monetization](#6-subscription--monetization)
7. [Technical Architecture](#7-technical-architecture)
8. [Content Strategy](#8-content-strategy)
9. [Privacy & Security Requirements](#9-privacy--security-requirements)
10. [Accessibility Requirements](#10-accessibility-requirements)
11. [Performance Requirements](#11-performance-requirements)
12. [Success Metrics](#12-success-metrics)
13. [Future Roadmap](#13-future-roadmap)
14. [Known Limitations](#14-known-limitations)
15. [Competitive Landscape](#15-competitive-landscape)

---

## 1. Product Overview

### 1.1 Mission

Deliver venue-specific, priority-driven clinical decision support for neurologists and neurology trainees at the point of care -- structured around how clinicians actually practice across emergency, inpatient, outpatient, and critical care settings.

### 1.2 Vision

Become the standard-of-care clinical companion for neurology, replacing fragmented reference materials with a single, evidence-based, offline-first app that adapts its recommendations to the clinician's current care setting.

### 1.3 Problem Statement

Neurologists and neurology trainees face three persistent challenges:

1. **Fragmented references.** Clinical guidance is scattered across textbooks, pocket cards, institutional protocols, and general-purpose medical apps. None are organized by clinical venue or priority level, which is how decisions are actually made.

2. **Context-blind recommendations.** Existing medical apps present the same treatment information regardless of whether the patient is in the ED, on the floor, in clinic, or in the ICU. A first-line medication that is appropriate for outpatient management may be entirely wrong in a STAT emergency setting.

3. **Workflow friction.** Clinicians cannot quickly assemble, customize, and export a treatment plan into the EMR. They resort to copy-pasting from disparate sources or relying on memory.

Neuro Plans solves all three by bundling 140+ evidence-based clinical plans, 30+ scoring scales, 20+ exam guides, and 35+ tools into a single offline-first app -- organized by clinical setting, tagged with priority levels, and exportable to the EMR via the Plan Builder.

### 1.4 Product Principles

| Principle | Description |
|---|---|
| **Venue-first** | Every recommendation is contextualized by clinical setting (ED, Hospital, Outpatient, ICU). |
| **Priority-driven** | Items are tagged STAT, URGENT, ROUTINE, or EXT so clinicians know what to do first. |
| **Offline-first** | All clinical content ships with the app. No network required at the bedside. |
| **EMR-ready** | The Plan Builder produces formatted text ready to paste into any electronic medical record. |
| **Evidence-based** | Content includes version numbers, evidence citations, and clinical guidelines references. |
| **No patient data** | The app never collects, stores, or transmits patient health information. |

---

## 2. Target Users & Personas

### 2.1 Primary Personas

| Persona | Role | Key Needs | Usage Context |
|---|---|---|---|
| **Dr. A -- Attending Neurologist** | Board-certified neurologist, 5-15 yrs experience | Quick venue-filtered lookups during rounds; dose verification; Plan Builder for complex cases | Hospital, outpatient clinic, on-call coverage |
| **Dr. R -- Neurology Resident** | PGY-2 to PGY-4 neurology resident | Learning plans for unfamiliar diagnoses; exam technique guides; scoring scales during consults | ED consults, inpatient rotations, night float |
| **NP/PA C -- Advanced Practice Provider** | Nurse practitioner or physician assistant in a neurology practice | Structured treatment plans for independent visits; dosing references; differential diagnosis support | Outpatient neurology clinic, urgent care |
| **Dr. E -- Emergency Physician** | EM attending managing acute neuro presentations | STAT-priority protocols (code stroke, status epilepticus); rapid scoring (NIHSS, GCS); brain death determination | Emergency department, trauma bay |
| **Student M -- Medical Student** | Third- or fourth-year student on neurology clerkship | Exam technique learning; clinical scale practice; studying differential diagnoses | Neurology clerkship, shelf exam preparation |

### 2.2 User Characteristics

- Clinicians work in high-pressure, time-constrained environments. The app must deliver answers in under 3 taps.
- Most usage occurs on iPhone. iPad usage is secondary, primarily in clinic or educational settings.
- Connectivity is unreliable in hospitals (elevator, basement, rural sites). Offline access is non-negotiable.
- Clinicians are skeptical of medical apps. Trust is earned through accuracy, citations, and transparent versioning.

---

## 3. Core Features

### 3.1 Plans Tab

The primary content surface. Provides access to approximately 140+ clinical plans organized into 16 neurology categories.

**Categories:**

| # | Category | Example Plans |
|---|---|---|
| 1 | Seizures & Epilepsy | First Seizure Workup, Status Epilepticus, Epilepsy in Pregnancy |
| 2 | Stroke & Vascular | Acute Ischemic Stroke, ICH, SAH, Cerebral Venous Thrombosis |
| 3 | Neuromuscular | Myasthenia Gravis, GBS, CIDP, ALS |
| 4 | CNS Infections | Bacterial Meningitis, Viral Encephalitis, Brain Abscess |
| 5 | Spinal Cord | Acute Myelopathy, Spinal Cord Compression, Cauda Equina |
| 6 | Neuro-Oncology | Brain Metastases, Primary CNS Lymphoma, Glioblastoma |
| 7 | Critical Care | ICP Management, Neuromuscular Respiratory Failure, Brain Death |
| 8 | Demyelinating | MS Relapse, NMOSD, MOGAD, PML |
| 9 | Headache | Migraine, Cluster Headache, Thunderclap Headache |
| 10 | Movement Disorders | Parkinson's Disease, Essential Tremor, Dystonia |
| 11 | Dementia & Cognitive | Alzheimer's Disease, Lewy Body Dementia, NPH |
| 12 | Functional Disorders | Functional Neurological Disorder, PNES |
| 13 | Cranial Neuropathies | Bell's Palsy, Trigeminal Neuralgia, Optic Neuritis |
| 14 | Inflammatory | Autoimmune Encephalitis, CNS Vasculitis, Neurosarcoidosis |
| 15 | Vasculitis | Primary CNS Angiitis, Systemic Vasculitis with CNS Involvement |
| 16 | Sleep Medicine | Narcolepsy, REM Sleep Behavior Disorder, Restless Legs |

**Plan structure -- each plan contains:**

| Section | Content |
|---|---|
| **Header** | Title, version, ICD-10 codes, scope description, clinical notes |
| **Laboratory Workup** | Lab tests with venue-specific priorities |
| **Imaging & Studies** | Imaging modalities, EEG, EMG/NCS, etc. with priorities |
| **Treatment** | Medications with structured dosing, routes, indications, contraindications, monitoring |
| **Other Recommendations** | Consults, disposition, patient education, follow-up |
| **Differential Diagnosis** | Ranked differential considerations |
| **Monitoring Parameters** | What to track and when |
| **Disposition Guidance** | Admission criteria, discharge criteria, follow-up timing |
| **Evidence & Guidelines** | Source citations and guideline references |

**Clinical setting filter:** Users filter plans by venue -- ED, Hospital (HOSP), Outpatient (OPD), ICU. Each action item within a plan carries venue-specific priority tags:

| Priority | Meaning | Visual Indicator |
|---|---|---|
| STAT | Immediate / life-threatening | Red |
| URGENT | Within hours | Orange |
| ROUTINE | Standard timing | Blue |
| EXT | Extended / outpatient follow-up | Gray |

### 3.2 Reference Tab

Three subsections of clinical reference material:

#### 3.2.1 Clinical Scales (30+)

Interactive scoring instruments with real-time calculation, color-coded interpretation bands, and links to related clinical plans.

| Scale Category | Examples |
|---|---|
| Stroke | NIHSS, mRS, ABCD2, Hunt & Hess, Fisher |
| Consciousness | GCS, FOUR Score |
| Cognition | MMSE, MoCA, CDR |
| Psychiatry | PHQ-9, GAD-7, Columbia Suicide |
| Functional | Barthel Index, Karnofsky |
| Disease-specific | EDSS, Hoehn & Yahr, UPDRS |

Each scale provides:
- Interactive input fields for each component
- Real-time total score computation
- Color-coded interpretation bands (e.g., mild / moderate / severe)
- Links to related clinical plans
- Citation to the original validation study

#### 3.2.2 Neurological Examinations (20+)

Step-by-step examination guides with technique instructions, normal and abnormal findings, and clinical pearls.

| Exam Domain | Examples |
|---|---|
| Mental Status | Orientation, attention, memory, language, praxis |
| Cranial Nerves | CN I through CN XII individual guides |
| Motor | Tone, bulk, strength grading, pronator drift |
| Sensory | Light touch, pain, proprioception, vibration |
| Cerebellar | Finger-nose, heel-shin, rapid alternating movements |
| Gait & Station | Romberg, tandem gait, casual gait |
| Reflexes | DTRs, pathological reflexes, frontal release signs |

#### 3.2.3 Tools (35+)

| Tool Type | Count | Examples |
|---|---|---|
| Calculators | 25+ | Corrected phenytoin, creatinine clearance, MAP, CPP, MELD, BMI, anion gap, osmolality, A-a gradient |
| Protocols | 5 | Status epilepticus, code stroke, brain death determination, ICP management, myasthenic crisis |
| Reference Tables | 5 | CSF analysis interpretation, AED therapeutic levels, dermatome map, reflex arc reference, cranial nerve summary |

### 3.3 Favorites Tab

- Users can bookmark any plan, scale, exam, or tool.
- Favorites persist locally across sessions.
- Favorites tab displays bookmarked items grouped by content type.
- Supports recents tracking for quick access to recently viewed items.

### 3.4 Builder Tab (Plan Builder)

The Plan Builder allows clinicians to assemble a custom clinical plan from items across any number of source plans.

**Workflow:**
1. Browse or search for a clinical plan.
2. Tap items (labs, imaging, treatments, recommendations) to add them to the Builder.
3. In the Builder, organize items by section.
4. For treatment items, select from available dose options.
5. Add free-text custom notes to any item.
6. Export the assembled plan as formatted text via clipboard copy or system share sheet.

**Export format:** Plain text structured by section headers, suitable for pasting into any EMR text field.

**Key capabilities:**
- Cross-plan item assembly (mix items from multiple plans)
- Dose option selection per treatment item
- Custom notes per item
- Section-based organization
- Clipboard copy and share sheet export
- Persistent draft (Builder state persists between sessions)

### 3.5 Settings Tab

| Setting | Description |
|---|---|
| Subscription management | View entitlement status, manage subscription, restore purchases |
| Layout customization | Drag-to-reorder sections within the app |
| Clinical setting default | Set preferred venue filter (ED, HOSP, OPD, ICU) |
| Appearance | System / light / dark mode |
| Error reporting | Submit clinical content error reports |
| Feedback | General app feedback submission |
| About | Version, disclaimers, terms, privacy policy |

### 3.6 Search

- Unified search bar available from the Plans and Reference tabs.
- Searches across all content types: plan titles, ICD-10 codes, abbreviations, descriptions, scale names, exam names, tool names.
- Results grouped by content type with clear section headers.
- Search is entirely local (offline).

### 3.7 Floating Stopwatch

- Persistent floating timer accessible from any screen.
- Designed for timed neurological examinations (e.g., MoCA recall, timed walk tests).
- Start, stop, reset controls.
- Remains visible as an overlay while navigating the app.

### 3.8 Clinical Error Reporting

- Users can flag suspected clinical content errors from within any plan, scale, or tool.
- Reports include: content location, error description, suggested correction, reporter entitlement tier.
- Submitting a verified clinical error grants the reporter a free year of access (errorReward entitlement).
- Reports are transmitted to Supabase for review.

### 3.9 Disclaimer Gate

- On first launch, users must accept a clinical disclaimer and terms of use before accessing any content.
- Disclaimer states that the app provides clinical decision support and does not replace clinical judgment.
- Acceptance is recorded locally and does not need to be repeated.

---

## 4. User Flows

### 4.1 First Launch

```
App Launch
  -> Disclaimer / Terms Acceptance Screen
    -> Accept -> Trial Entitlement Activated (14-day free trial)
      -> Plans Tab (default landing screen)
    -> Decline -> App remains on disclaimer screen
```

### 4.2 Finding and Viewing a Clinical Plan

```
Plans Tab
  -> Browse categories OR use search bar
    -> Select category -> View plan list (filtered by current venue setting)
      -> Tap plan -> Plan detail view
        -> Sections: Lab Workup | Imaging | Treatment | Other Recs
        -> Each item shows priority tag for current venue
        -> Tap treatment item -> View dosing options, contraindications, monitoring
        -> Tap "Add to Builder" on any item
```

### 4.3 Using a Clinical Scale

```
Reference Tab -> Scales section
  -> Browse or search scales
    -> Select scale (e.g., NIHSS)
      -> Enter component scores via interactive fields
      -> View real-time total and interpretation band
      -> Tap "Related Plans" to jump to relevant clinical plan
```

### 4.4 Building and Exporting a Plan

```
(From any plan detail view)
  -> Tap items to add to Builder
    -> Navigate to Builder Tab
      -> Review assembled items organized by section
      -> Select dose options for treatment items
      -> Add custom notes
      -> Tap "Copy to Clipboard" or "Share"
        -> Formatted text ready for EMR paste
```

### 4.5 Subscription Flow

```
Trial Expiration (Day 15)
  -> Content locked behind paywall
    -> Tap "Subscribe" -> StoreKit 2 purchase sheet
      -> $12.99/year annual subscription
        -> Success -> Full access restored
        -> Cancel -> Remains on expired tier
```

### 4.6 Domain Whitelist Access

```
Settings -> Subscription -> Institutional Access
  -> Enter institutional email address
    -> Supabase sends OTP to whitelisted domain
      -> Enter OTP -> Whitelisted entitlement granted
        -> Full access without subscription payment
```

### 4.7 Error Reporting Flow

```
(From any content screen)
  -> Tap "Report Error"
    -> Describe the clinical error and suggested correction
      -> Submit -> Report sent to Supabase
        -> If error verified -> errorReward entitlement granted (free year)
```

---

## 5. Data Model

### 5.1 High-Level Architecture

All clinical content is bundled locally within the app as structured Swift data (not a local database). Supabase handles authentication, domain whitelisting, analytics, and error report collection.

### 5.2 Core Data Entities

| Entity | Description | Storage |
|---|---|---|
| **ClinicalPlan** | Complete plan with header, sections, items | Bundled (local) |
| **PlanItem** | Individual lab, imaging, treatment, or recommendation item | Bundled (local) |
| **TreatmentItem** | Extended PlanItem with dosing options, routes, contraindications, monitoring | Bundled (local) |
| **DoseOption** | Structured dose with amount, unit, frequency, route, indication | Bundled (local) |
| **ClinicalScale** | Scoring instrument with components and interpretation bands | Bundled (local) |
| **ScaleComponent** | Individual input field within a scale | Bundled (local) |
| **NeurologicalExam** | Step-by-step exam guide | Bundled (local) |
| **Calculator** | Medical calculator with input parameters and formula | Bundled (local) |
| **Protocol** | Step-by-step clinical protocol | Bundled (local) |
| **ReferenceTable** | Static reference data table | Bundled (local) |
| **UserFavorite** | Bookmarked item reference | Local (UserDefaults / SwiftData) |
| **BuilderDraft** | Assembled plan items with selected doses and notes | Local (UserDefaults / SwiftData) |
| **UserEntitlement** | Current access tier and expiration | Local + Supabase verification |
| **ErrorReport** | Clinical error submission | Supabase (remote) |

### 5.3 Plan Item Priority Model

Each PlanItem carries a dictionary of venue-to-priority mappings:

```
VenuePriority:
  ED:   STAT | URGENT | ROUTINE | EXT | null
  HOSP: STAT | URGENT | ROUTINE | EXT | null
  OPD:  STAT | URGENT | ROUTINE | EXT | null
  ICU:  STAT | URGENT | ROUTINE | EXT | null
```

A null value means the item is not applicable in that venue.

### 5.4 Treatment Dosing Model

```
TreatmentItem:
  name: String
  route: [PO, IV, IM, SC, PR, topical, inhaled]
  indication: String
  doseOptions: [DoseOption]
  contraindications: [String]
  monitoringRequirements: [String]
  venuePriorities: VenuePriority

DoseOption:
  amount: String (e.g., "1000 mg")
  frequency: String (e.g., "q8h")
  route: String
  duration: String? (e.g., "14 days")
  indication: String?
  notes: String?
```

---

## 6. Subscription & Monetization

### 6.1 Pricing

| Plan | Price | Billing Cycle |
|---|---|---|
| Annual Subscription | $12.99 | Yearly auto-renewal |

No monthly option in v1.0. No lifetime purchase option. No in-app purchases beyond the subscription.

### 6.2 Entitlement Tiers

| Tier | Access Level | Duration | How Obtained |
|---|---|---|---|
| **trial** | Full access | 14 days from first launch | Automatic on first app open |
| **subscribed** | Full access | 1 year (auto-renewing) | StoreKit 2 purchase |
| **whitelisted** | Full access | Indefinite (while domain remains whitelisted) | Institutional email OTP verification via Supabase |
| **errorReward** | Full access | 1 year from reward grant | Submitting a verified clinical error report |
| **expired** | Locked (paywall) | Until subscription or other entitlement obtained | Trial or subscription lapsed |
| **loading** | Splash screen | Transient | App is verifying entitlement status |

### 6.3 Entitlement Resolution Order

When multiple entitlements could apply, the system resolves in this order:

1. **whitelisted** (highest -- institutional access always wins)
2. **subscribed** (active StoreKit subscription)
3. **errorReward** (active reward period)
4. **trial** (within 14-day window)
5. **expired** (fallback)

### 6.4 Paywall Behavior

When entitlement is **expired**:
- Plans Tab shows category list but locks plan detail views.
- Reference Tab is locked.
- Builder Tab is locked.
- Settings Tab remains accessible (to manage subscription).
- A paywall screen offers subscription purchase and restore options.

### 6.5 Domain Whitelist

- Institutions can request domain whitelisting for their organization.
- Supabase maintains the list of whitelisted email domains.
- Users verify institutional affiliation via one-time email OTP.
- Whitelisted access does not expire as long as the domain remains on the list.

---

## 7. Technical Architecture

### 7.1 Technology Stack

| Layer | Technology |
|---|---|
| Language | Swift 5.9+ |
| UI Framework | SwiftUI |
| State Management | @Observable pattern (Observation framework) |
| Minimum Target | iOS 17.0 |
| Device Support | iPhone and iPad (universal app) |
| Backend | Supabase (PostgreSQL, Auth, Edge Functions) |
| Payments | StoreKit 2 |
| Package Manager | Swift Package Manager |
| Single Dependency | Supabase Swift SDK v2.41.1 |

### 7.2 Architecture Pattern

The app follows a feature-based modular architecture using the @Observable pattern:

- **Views:** SwiftUI views, one per screen or major UI component.
- **Models:** Plain Swift structs/classes conforming to Codable/Identifiable.
- **Stores / Managers:** @Observable classes managing state for each feature domain (SubscriptionManager, FavoritesManager, BuilderManager, etc.).
- **Services:** Network and persistence abstraction (SupabaseService, StoreKitService).

### 7.3 Data Flow

```
[Bundled Clinical Content]
        |
        v
  [Content Loader] --> [In-Memory Model Cache]
        |                       |
        v                       v
  [Plans Store]          [Reference Store]
        |                       |
        v                       v
   [SwiftUI Views] <---- [@Observable State]
        |
        v
  [Builder Store] --> [Clipboard / Share Sheet]

[Supabase Backend]
   |        |        |
   v        v        v
 [Auth]  [Analytics] [Error Reports]
   |
   v
 [Entitlement Verification]
   |
   v
 [StoreKit 2] <-> [App Store]
```

### 7.4 Offline Strategy

- All clinical content (plans, scales, exams, calculators, protocols, tables) is bundled into the app binary at build time.
- No network call is required to view or interact with clinical content.
- Supabase is required only for: authentication (domain whitelist OTP), error report submission, analytics event logging.
- StoreKit 2 handles subscription verification through the App Store, which manages its own offline grace period.
- The app degrades gracefully when offline: all clinical features work, subscription status uses cached entitlement, error reports queue for later submission.

### 7.5 Dependencies

| Dependency | Version | Purpose |
|---|---|---|
| Supabase Swift SDK | 2.41.1 | Auth, database, edge functions |

No other third-party dependencies. The app avoids dependency bloat intentionally to minimize supply-chain risk and simplify maintenance.

---

## 8. Content Strategy

### 8.1 Content Sourcing

Clinical content is authored by board-certified neurologists and verified against current evidence-based guidelines. Source materials include:

- AAN (American Academy of Neurology) practice guidelines
- AHA/ASA stroke guidelines
- Neurocritical Care Society guidelines
- UpToDate and peer-reviewed journal literature
- Institutional protocols from academic medical centers

### 8.2 Content Versioning

- Each clinical plan carries a version number (e.g., v1.0, v1.1).
- Version changes are documented with a change summary.
- Content updates are delivered via app updates (bundled content model).

### 8.3 Content Review Cycle

| Trigger | Action |
|---|---|
| New major guideline publication | Review and update affected plans within 30 days |
| User error report (verified) | Patch affected content in next app release |
| Annual review | All plans reviewed for currency at least once per year |
| New clinical plan request | Triage, author, review, and publish in a future release |

### 8.4 Content Quality Controls

- Dual-reviewer process: all new content reviewed by at least two clinicians.
- Error reporting system provides crowd-sourced accuracy verification.
- ICD-10 codes validated against current CMS code sets.
- Drug information cross-referenced against FDA-approved labeling.

---

## 9. Privacy & Security Requirements

### 9.1 Core Privacy Principle

**Neuro Plans does not collect, store, or transmit any patient health information (PHI).** The app is a clinical reference tool, not a patient record system.

### 9.2 Data Collection Summary

| Data Type | Collected? | Storage | Purpose |
|---|---|---|---|
| Patient health information | No | N/A | N/A |
| User email (whitelist only) | Yes | Supabase | Institutional verification |
| Subscription status | Yes | Local + App Store | Entitlement management |
| Usage analytics | Yes | Supabase | Product improvement |
| Error reports | Yes | Supabase | Content accuracy improvement |
| Favorites / recents | Yes | Local only | User personalization |
| Builder drafts | Yes | Local only | Plan assembly persistence |

### 9.3 HIPAA Considerations

- The app is designed to operate outside the HIPAA-regulated data boundary.
- No PHI enters the app at any point.
- The Plan Builder exports text to the clipboard; the user pastes it into the EMR. The EMR is the HIPAA-regulated system, not Neuro Plans.
- Clinical disclaimers reinforce that the app is a reference tool and does not replace clinical judgment.

### 9.4 Authentication Security

- Domain whitelist verification uses one-time passwords (OTP) sent to institutional email.
- No passwords are stored by the app.
- Supabase Auth handles token management with industry-standard practices.
- StoreKit 2 handles subscription credentials through Apple's secure infrastructure.

### 9.5 Data Transmission

- All network communication uses HTTPS/TLS.
- Supabase endpoints use Row Level Security (RLS) policies.
- Analytics events contain no personally identifiable information beyond anonymized user IDs.

---

## 10. Accessibility Requirements

### 10.1 Standards Target

The app targets WCAG 2.1 Level AA compliance for mobile applications.

### 10.2 Specific Requirements

| Requirement | Implementation |
|---|---|
| **VoiceOver** | All interactive elements have meaningful accessibility labels. Clinical scales announce score changes. Navigation is fully operable via VoiceOver. |
| **Dynamic Type** | All text respects the user's preferred text size (UIContentSizeCategory). Layouts adapt to larger text sizes without truncation or overlap. |
| **Color contrast** | All text meets WCAG AA contrast ratios (4.5:1 for normal text, 3:1 for large text) in both light and dark modes. |
| **Color independence** | Priority levels (STAT/URGENT/ROUTINE/EXT) use both color and text labels -- information is never conveyed by color alone. |
| **Touch targets** | All interactive elements have a minimum touch target of 44x44 points. |
| **Dark mode** | Full dark mode support with appropriate contrast adjustments for all clinical content. |
| **Reduce motion** | Animations respect the user's "Reduce Motion" accessibility setting. |

### 10.3 Known Accessibility Gaps (v1.0)

- Floating stopwatch may require additional VoiceOver refinement.
- Drag-to-reorder in settings may need accessibility action alternatives.
- Complex calculator inputs may benefit from additional VoiceOver hints.

---

## 11. Performance Requirements

### 11.1 Targets

| Metric | Target | Measurement |
|---|---|---|
| **Cold launch to interactive** | < 2 seconds | Time from app icon tap to Plans Tab fully rendered |
| **Plan detail load** | < 500 ms | Time from plan tap to detail view fully rendered |
| **Scale score update** | < 100 ms | Time from input change to score recalculation and display |
| **Search results** | < 300 ms | Time from keystroke to results displayed |
| **Memory footprint** | < 150 MB | Peak memory usage during normal operation |
| **App binary size** | < 50 MB | Download size from App Store |
| **Battery impact** | Minimal | No background processing, no location services, no continuous networking |
| **Scroll performance** | 60 fps | All list views maintain smooth scrolling |

### 11.2 Optimization Strategy

- Clinical content is loaded lazily by category -- not all 140+ plans are parsed at launch.
- Search indexing is built at first launch and cached.
- SwiftUI views use appropriate identity and equatable optimizations to minimize re-renders.
- No background tasks, no push notifications, no location services in v1.0.

---

## 12. Success Metrics

### 12.1 v1.0 Launch KPIs (First 90 Days)

| Metric | Target | Rationale |
|---|---|---|
| App Store downloads | 1,000+ | Validates market interest in neurology-specific clinical support |
| Trial-to-paid conversion | > 15% | Indicates content value justifies $12.99/year |
| Day-7 retention | > 40% | Shows the app provides recurring clinical value |
| Day-30 retention | > 25% | Confirms sustained usage beyond novelty |
| App Store rating | > 4.5 stars | Reflects clinical accuracy and usability |
| Clinical error reports | < 5 verified errors | Validates content quality |
| Crash-free sessions | > 99.5% | Standard reliability threshold |

### 12.2 Engagement Metrics (Ongoing)

| Metric | Target | Description |
|---|---|---|
| Plans viewed per session | > 2 | Users are exploring multiple plans per session |
| Builder exports per week (active users) | > 1 | Plan Builder is providing clinical workflow value |
| Scales used per session | > 1 | Reference tools are actively used |
| Search usage rate | > 30% of sessions | Search is a primary navigation path |
| Favorites count per user | > 5 | Users are personalizing their experience |

### 12.3 Business Metrics (Annual)

| Metric | Target | Description |
|---|---|---|
| Annual subscribers | 500+ (Year 1) | Sustainable revenue base |
| Annual recurring revenue | $6,500+ (Year 1) | 500 subscribers x $12.99 |
| Subscriber churn rate | < 30% annually | Retention indicates ongoing value |
| Institutional whitelist partners | 3+ | Validates institutional interest |

---

## 13. Future Roadmap

### 13.1 v1.x (Near-Term Enhancements)

| Feature | Priority | Description |
|---|---|---|
| Push notification for content updates | Medium | Notify users when plans are updated with new guidelines |
| Enhanced Builder templates | High | Pre-built plan templates for common clinical scenarios |
| Handoff / continuity | Low | Start on iPhone, continue on iPad |
| Widget support | Medium | Lock screen and home screen widgets for quick scale access |
| Siri Shortcuts | Low | Voice-activated plan lookup ("Hey Siri, open stroke plan") |
| Expanded calculator library | Medium | Additional specialty calculators based on user requests |
| Enhanced analytics dashboard | Internal | Better visibility into content usage patterns |

### 13.2 v2.0 (Major Release)

| Feature | Priority | Description |
|---|---|---|
| AI-assisted differential diagnosis | High | LLM-powered differential ranking based on symptom input |
| Collaborative plan sharing | Medium | Share Builder plans with colleagues via link or QR code |
| Institutional custom plans | High | Organizations can deploy custom plans to their whitelisted users |
| Content update delivery (OTA) | High | Update clinical content without requiring an app update |
| Android companion app | Medium | Expand reach to Android devices |
| EMR integration (SMART on FHIR) | Low | Direct plan export to supported EMR systems |
| Multimedia exam guides | Medium | Video demonstrations for neurological examination techniques |
| Spaced repetition for trainees | Low | Flashcard-style learning mode for scales and differentials |
| Localization | Low | Spanish, French, Portuguese translations for international use |

---

## 14. Known Limitations

### 14.1 v1.0 Limitations

| Limitation | Impact | Mitigation |
|---|---|---|
| **Content updates require app updates** | Users must update the app to receive new or corrected clinical content | Clear update notes; plan for OTA content delivery in v2.0 |
| **No Android version** | Excludes Android users (approximately 25% of US physicians) | Android planned for v2.0 |
| **No EMR integration** | Plan Builder exports via clipboard only; no direct EMR write | Clipboard paste is functional for all EMR systems; SMART on FHIR planned for v2.0 |
| **Single language (English)** | Limits international adoption | Localization planned for v2.0 |
| **No multimedia in exams** | Exam guides are text-only; no photos or videos | Multimedia guides planned for v2.0 |
| **No offline error reporting** | Error reports require network connectivity to submit | Reports could be queued locally for later submission |
| **No collaborative features** | Users cannot share plans or favorites with colleagues | Collaborative sharing planned for v2.0 |
| **No patient-specific input** | App cannot accept patient data to personalize recommendations | By design -- avoids PHI handling and HIPAA scope |

### 14.2 Technical Debt

| Item | Description | Priority |
|---|---|---|
| Search index rebuild on every launch | Search index should be cached and rebuilt only when content changes | Medium |
| Builder state persistence | Currently uses UserDefaults; should migrate to SwiftData for robustness | Low |
| Analytics event batching | Events are sent individually; should batch for network efficiency | Low |
| Content loading architecture | Lazy loading works but could benefit from structured concurrency refinement | Medium |

---

## 15. Competitive Landscape

### 15.1 Key Competitors

| Competitor | Type | Strengths | Weaknesses vs. Neuro Plans |
|---|---|---|---|
| **UpToDate** | General medical reference | Comprehensive, trusted, widely adopted | Not neurology-specific; not venue-organized; no plan builder; expensive ($500+/yr individual) |
| **Epocrates** | Drug reference + clinical tools | Strong drug database, free tier | General purpose; no neurology-specific plans; no venue filtering; limited clinical decision support |
| **MDCalc** | Medical calculators | Excellent calculator library, free | Calculators only; no treatment plans; no exam guides; no plan builder |
| **Medscape** | General medical reference | Broad coverage, free, large user base | Not neurology-specific; ad-supported; no venue filtering; no plan builder |
| **Neurology Pocket** | Neurology reference book (app) | Neurology-specific content | Static reference (no interactivity); no scoring; no plan builder; no venue filtering |
| **AMBOSS** | Medical knowledge platform | Comprehensive, well-designed, study features | Primarily educational; not optimized for point-of-care; expensive; not neurology-specific |

### 15.2 Competitive Differentiation

Neuro Plans occupies a unique position at the intersection of three axes that no competitor addresses simultaneously:

1. **Specialty-specific:** Focused exclusively on neurology, providing depth that general apps cannot match.
2. **Venue-organized:** Structures recommendations by clinical setting (ED, Hospital, Outpatient, ICU) with priority levels -- matching clinical workflow.
3. **Action-oriented:** The Plan Builder transforms reference content into exportable clinical plans, bridging the gap between knowledge and action.

### 15.3 Competitive Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| UpToDate adds venue-based filtering | Low | UpToDate's general-purpose architecture makes this difficult to retrofit |
| MDCalc expands into treatment plans | Medium | MDCalc's brand is calculators; expanding scope dilutes focus |
| New neurology-specific app enters market | Medium | First-mover advantage, clinical accuracy, and Plan Builder workflow create switching costs |
| AI-powered clinical tools (ChatGPT, Med-PaLM) | High | AI tools lack structure, versioning, and venue awareness; regulatory uncertainty; Neuro Plans can integrate AI rather than compete with it |

---

## Appendix A: Glossary

| Term | Definition |
|---|---|
| AAN | American Academy of Neurology |
| AED | Antiepileptic Drug |
| CPP | Cerebral Perfusion Pressure |
| CSF | Cerebrospinal Fluid |
| ED | Emergency Department |
| EMR | Electronic Medical Record |
| EXT | Extended priority (outpatient follow-up) |
| GCS | Glasgow Coma Scale |
| HOSP | Hospital (inpatient) |
| ICD-10 | International Classification of Diseases, 10th Revision |
| ICP | Intracranial Pressure |
| ICU | Intensive Care Unit |
| MAP | Mean Arterial Pressure |
| mRS | Modified Rankin Scale |
| NIHSS | National Institutes of Health Stroke Scale |
| OPD | Outpatient Department |
| OTA | Over-The-Air (content update delivery) |
| OTP | One-Time Password |
| PHI | Protected Health Information |
| RLS | Row Level Security (Supabase) |
| STAT | Immediately / emergent priority |

---

## Appendix B: Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-02-15 | -- | Initial PRD for v1.0 App Store submission |

---

*This is a living document. Update it as the product evolves, features ship, and priorities shift.*
