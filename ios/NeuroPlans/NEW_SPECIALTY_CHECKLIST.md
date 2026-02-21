# New Specialty App — Complete Setup Checklist

Step-by-step guide for creating a new specialty app (e.g., Pulm Plans, GI Plans)
from the Neuro Plans template. Follow every section in order.

**Estimated time:** 2–3 days (excludes content creation and physician review)

---

## Prerequisites

- [ ] macOS with Xcode 15+ installed
- [ ] Apple Developer Program membership ($99/year) — one account covers all apps
- [ ] Access to this GitHub repo
- [ ] Domain registered for new specialty (e.g., pulmplans.app)
- [ ] Supabase account (free tier is fine)
- [ ] App icon designed (1024×1024 PNG, no alpha)

---

## Phase 1: Infrastructure Setup (Do First)

### 1.1 Register Domain

| Step | Action |
|------|--------|
| 1 | Go to Porkbun (or any registrar) and register `[specialty]plans.app` |
| 2 | Enable WHOIS privacy (usually free) |
| 3 | Set up email forwarding (Porkbun includes this free): |

Create these forwarding addresses (all forward to your personal email):

| Address | Purpose |
|---------|---------|
| `developer@[specialty]plans.app` | Apple Developer, App Store Connect |
| `support@[specialty]plans.app` | User support, legal docs contact |
| `errors@[specialty]plans.app` | Clinical error reports from app |

**Cost:** ~$11–15/year for `.app` domain

### 1.2 Create Supabase Project

| Step | Action |
|------|--------|
| 1 | Go to [supabase.com](https://supabase.com) → New Project |
| 2 | Name it `[specialty]-plans` (e.g., `pulm-plans`) |
| 3 | Choose a region close to your users (US East recommended) |
| 4 | Save the **Project URL** and **anon key** from Settings → API |

**Create the database tables:**

```sql
-- Table 1: Whitelisted email domains (for institutional access)
CREATE TABLE whitelisted_domains (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  domain TEXT NOT NULL UNIQUE,
  organization TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Table 2: Verified emails
CREATE TABLE verified_emails (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  domain TEXT NOT NULL,
  verified_at TIMESTAMPTZ DEFAULT now(),
  is_whitelisted BOOLEAN DEFAULT false
);

-- Enable Row Level Security
ALTER TABLE whitelisted_domains ENABLE ROW LEVEL SECURITY;
ALTER TABLE verified_emails ENABLE ROW LEVEL SECURITY;

-- Allow anonymous reads on whitelisted_domains (app checks eligibility)
CREATE POLICY "Allow anonymous read" ON whitelisted_domains
  FOR SELECT USING (true);

-- Allow anonymous insert on verified_emails (app verifies email)
CREATE POLICY "Allow anonymous insert" ON verified_emails
  FOR INSERT WITH CHECK (true);

-- Allow anonymous read on own verified_emails
CREATE POLICY "Allow anonymous read own" ON verified_emails
  FOR SELECT USING (true);
```

**Set up Auth OTP (email verification):**

| Step | Action |
|------|--------|
| 1 | Supabase Dashboard → Authentication → Providers |
| 2 | Enable "Email" provider |
| 3 | Enable "OTP" (one-time password) sign-in |
| 4 | Set OTP expiry to 10 minutes |
| 5 | Customize email template with your app name |

**Save these values — you'll need them for SpecialtyConfig:**
- Project URL: `https://[project-ref].supabase.co`
- Anon Key: `eyJ...` (long JWT string from Settings → API)

### 1.3 Create Legal Pages

Copy and customize the legal document templates:

**Privacy Policy** — Copy `docs/privacy.md` and replace:

| Find | Replace With |
|------|-------------|
| `Neuro Plans` | `[Your App Name]` (e.g., `Pulm Plans`) |
| `neuroplans.app` | `[specialty]plans.app` |
| `errors@neuroplans.app` | `errors@[specialty]plans.app` |
| `support@neuroplans.app` | `support@[specialty]plans.app` |
| `neurology` / `neurological` | your specialty name |

**Terms of Service** — Copy `docs/terms.md` and replace the same values.

**Host them:** These must be accessible at:
- `https://[specialty]plans.app/privacy`
- `https://[specialty]plans.app/terms`

Options for hosting:
1. **GitHub Pages** (recommended) — Deploy with MkDocs like Neuro Plans
2. **Netlify/Vercel** — Free static site hosting
3. **Porkbun URL forwarding** — Forward to GitHub Pages URLs

**Verify:** Open both URLs in a browser before proceeding. Apple checks these during review.

---

## Phase 2: Xcode Project Setup

### 2.1 Clone the Repository

```bash
git clone [repo-url] [specialty]-plans
cd [specialty]-plans
git checkout -b [specialty]-plans-setup
```

### 2.2 Update Xcode Project Settings

Open `ios/NeuroPlans/NeuroPlans.xcodeproj` in Xcode, then:

| Step | Where | Action |
|------|-------|--------|
| 1 | Target → General → Identity | Change **Display Name** to your app name (e.g., "Pulm Plans") |
| 2 | Target → General → Identity | Change **Bundle Identifier** to `com.[specialty]plans.app` |
| 3 | Target → Signing & Capabilities | Select your Development Team |
| 4 | Target → Signing & Capabilities | Ensure "Automatically manage signing" is checked |
| 5 | Target → General → App Icons | Replace AppIcon with your app icon (drag 1024×1024 PNG) |

**Important:** You do NOT need to rename the .xcodeproj folder or the Xcode scheme.
The Display Name controls what users see. The internal project name can stay "NeuroPlans."

### 2.3 Update Info.plist (if needed)

The Display Name from step 2.2 should auto-update Info.plist. Verify:
- `CFBundleDisplayName` = your app name
- `CFBundleName` = your app name

---

## Phase 3: Code Changes (SpecialtyConfig + Content)

### 3.1 Update SpecialtyConfig.swift ← MOST IMPORTANT FILE

Open `ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift` and change **every** value:

```swift
enum SpecialtyConfig {
    // MARK: - Identity
    static let appName = "Pulm Plans"                    // ← Your app name
    static let specialty = "pulmonology"                  // ← Your specialty
    static let bundleId = "com.pulmplans.app"             // ← Must match Xcode

    // MARK: - Branding
    static let brandColorHex = "#2563EB"                  // ← Pick a DIFFERENT color
    static let headerIcon = "lungs.fill"                  // ← SF Symbol for your specialty
    static let tagline = "Clinical Pulmonology Decision Support"

    // MARK: - Subscription
    static let storeKitProductId = "com.pulmplans.annual" // ← Must match App Store Connect

    // MARK: - Error Reporting
    static let errorReportEmail = "errors@pulmplans.app"

    // MARK: - Supabase
    static let supabaseUrl = "https://[your-project].supabase.co"  // ← From Phase 1.2
    static let supabaseAnonKey = "eyJ..."                           // ← From Phase 1.2

    // MARK: - Legal
    static let termsURL = "https://pulmplans.app/terms"
    static let privacyURL = "https://pulmplans.app/privacy"
    static let disclaimerTitle = "Pulm Plans"
    static let supportEmail = "support@pulmplans.app"

    // MARK: - Paywall Features (must be specialty-specific!)
    static let paywallFeatures: [(icon: String, title: String, description: String)] = [
        ("list.bullet.clipboard.fill", "All Clinical Plans", "Complete pulmonology protocols for COPD, asthma, PE, and more"),
        ("lungs.fill", "Clinical Scales", "CURB-65, Wells Score, BODE Index, and 15+ validated tools"),
        ("stethoscope", "Pulm Exam Guides", "Step-by-step lung auscultation and respiratory exams"),
        ("waveform.path.ecg", "ABG Calculator", "Arterial blood gas interpretation with acid-base analysis"),
        ("square.and.pencil", "Plan Builder", "Create custom order sets and export to your EMR"),
        ("arrow.triangle.2.circlepath", "Free Updates", "New plans and features as they're released"),
    ]

    // MARK: - About / Settings
    static let aboutDescription = "Evidence-based clinical decision support for pulmonary diagnoses"
    static let aboutIcon = "lungs.fill"

    // MARK: - Emergency Quick Actions (must be specialty-specific!)
    static let quickActions: [(id: String, label: String, icon: String, color: String)] = [
        ("pulmonary-embolism", "PE Alert", "bolt.heart.fill", "red"),
        ("status-asthmaticus", "Status Asthmaticus", "wind", "orange"),
        ("copd-exacerbation", "COPD Exacerbation", "lungs.fill", "purple"),
    ]
}
```

**Guideline 4.3 requirement:** The `paywallFeatures`, `quickActions`, `headerIcon`, `aboutIcon`, `tagline`, `aboutDescription`, and `brandColorHex` must ALL be different from Neuro Plans and any other specialty. Apple compares these screens side-by-side.

### 3.2 Replace ExamToolsView.swift ← REQUIRES FULL REWRITE

This file at `Views/Reference/ExamToolsView.swift` contains a hardcoded enum of **neurology-specific** exam tools (penlight, OKN stripes, pupil gauge, etc.).

**You must replace the entire `ExamToolType` enum** with tools relevant to your specialty.

Example for Pulmonology:

```swift
enum ExamToolType: String, CaseIterable, Hashable {
    case peakFlowMeter = "Peak Flow Meter"
    case pulseOximeter = "Pulse Oximeter"
    case incentiveSpirometer = "Incentive Spirometer"
    case abgInterpreter = "ABG Interpreter"
    case chestXrayGuide = "Chest X-Ray Guide"
    case ventSettings = "Vent Settings"
    case inhalerTechnique = "Inhaler Technique"
    case oxygenTitration = "O2 Titration"

    var icon: String {
        switch self {
        case .peakFlowMeter: return "gauge.with.dots.needle.33percent"
        case .pulseOximeter: return "waveform.path.ecg"
        // ... etc.
        }
    }
    // ... color, description computed properties too
}
```

You'll also need to update `ExamToolDetailView` further down in the same file — each case renders a different interactive tool view. This is the most significant code change.

### 3.3 Replace Category.swift

This defines the plan categories shown on the home screen.

| Neuro Plans (current) | Example: Pulm Plans |
|----------------------|---------------------|
| Seizure | COPD |
| Stroke | Asthma |
| Multiple Sclerosis | Pulmonary Embolism |
| Headache | Pneumonia |
| Movement Disorders | Interstitial Lung Disease |
| Neuromuscular | Pleural Disease |
| etc. | etc. |

Each category needs: `id`, `name`, `icon` (SF Symbol), `color`, and an array of `planIds` that reference entries in `plans.json`.

### 3.4 Replace Reference.swift

This defines scales, exams, and tools data. Replace all neuro content:

| Section | Neuro Plans | Your Specialty |
|---------|-------------|----------------|
| Scales | NIHSS, mRS, GCS, EDSS | CURB-65, Wells, BODE, CAT |
| Exams | Cranial nerve, motor, sensory | Lung auscultation, respiratory pattern |
| Tools | Penlight, reflex hammer | Peak flow, pulse ox |

### 3.5 Replace/Update CalculatorEngine.swift

Add specialty-specific calculators. Neuro Plans has GCS calculator, etc.
Your specialty needs its own formulas.

### 3.6 Replace Content Data Files

| File | What to Replace |
|------|----------------|
| `plans.json` | All clinical plan data (from your markdown plans) |
| `scales.json` | Clinical scoring tool definitions |
| `exams.json` | Physical examination guides |
| `tools.json` | Interactive tool definitions |

Generate `plans.json` using:
```bash
python -X utf8 scripts/generate_json.py docs/plans/*.md --merge
```

### 3.7 Update Configuration.storekit

Open `Configuration.storekit` and update:
- Product ID to match your `SpecialtyConfig.storeKitProductId`
- `_applicationInternalID` to your App Store Connect app ID (get after creating app record)
- `_developerTeamID` to your Team ID

---

## Phase 4: App Store Connect Setup

### 4.1 Create App Record

| Step | Action |
|------|--------|
| 1 | [App Store Connect](https://appstoreconnect.apple.com) → My Apps → "+" |
| 2 | Platform: iOS |
| 3 | Name: your app name (must be unique on App Store) |
| 4 | Primary Language: English (U.S.) |
| 5 | Bundle ID: select from dropdown (must match Xcode) |
| 6 | SKU: `[specialty]plans` (internal reference) |

### 4.2 Create Subscription

| Step | Action |
|------|--------|
| 1 | App → Subscriptions → Create Subscription Group |
| 2 | Group name: "[App Name] Subscriptions" |
| 3 | Add subscription: Reference Name = "Annual", Product ID = `com.[specialty]plans.annual` |
| 4 | Set price: $12.99/year (or your chosen price) |
| 5 | Add localization (English) with description |
| 6 | **IMPORTANT:** Add Introductory Offer → Free Trial → 14 days |

### 4.3 Configure App Privacy

In App Store Connect → App → App Privacy:

| Data Type | Declare | Purpose | Linked? | Tracking? |
|-----------|---------|---------|---------|-----------|
| Email Address | Yes | App Functionality | No | No |
| Purchase History | Yes | App Functionality | No | No |
| Device ID | Yes | App Functionality | No | No |

**Click "Publish"** after configuring. Saving is not enough.

### 4.4 Agreements, Tax, and Banking

| Step | Action |
|------|--------|
| 1 | App Store Connect → Agreements, Tax, and Banking |
| 2 | Accept the Paid Applications agreement |
| 3 | Complete Tax Forms (W-9 for US, W-8BEN for non-US) |
| 4 | Add Bank Account for payments |
| 5 | Wait for status to show **"Active"** before submitting |

### 4.5 Prepare Metadata

| Field | Guidance |
|-------|----------|
| Description | Specialty-specific, mention key features, mention subscription terms |
| Keywords | Specialty-specific medical terms (100 chars max) |
| Screenshots | Must show YOUR specialty content (not generic UI) |
| Support URL | `https://[specialty]plans.app` |
| Privacy URL | `https://[specialty]plans.app/privacy` |
| Age Rating | Medical/Treatment Information → Infrequent/Mild → Result: 4+ |

### 4.6 Screenshots

Take screenshots on iOS Simulator at these sizes:

| Device | Size | Required? |
|--------|------|-----------|
| iPhone 16 Pro Max | 6.9" | Yes |
| iPhone 16 Pro | 6.3" | Yes (or use 6.9" scaled) |
| iPad Pro 13" | 13" | Only if app supports iPad |

**How to capture:** In Simulator, press **Cmd+S** to save screenshot to Desktop.

Take at least 5 screenshots showing:
1. Home screen with quick actions (shows specialty differentiation)
2. A clinical plan detail view
3. A clinical scale/calculator
4. The paywall (shows subscription pricing)
5. An exam tool (specialty-specific)

### 4.7 Review Notes

Copy this template into App Store Connect → App Review Information → Notes:

```
This is a clinical reference app for [specialty] professionals.

**Subscription:** The app provides a 14-day free trial on first launch
(no sign-up required). After the trial, users subscribe at $[price]/year
via StoreKit.

**Email Verification (optional):** On the paywall screen, users can tap
"Check Eligibility" to verify their institutional email. This uses
Supabase Auth OTP — no account creation, no password. If their domain
is whitelisted, they get complimentary access. If not, they're shown
the subscription option.

**No login required.** No test account needed.
**Internet not required** for core content — all clinical data is bundled.
```

---

## Phase 5: Build, Test, Submit

### 5.1 Run Pre-Submission Validation

```bash
./ios/scripts/ios-preflight.sh
```

All checks must PASS (warnings are acceptable but should be reviewed).

### 5.2 Create Sandbox Tester

| Step | Action |
|------|--------|
| 1 | App Store Connect → Users and Access → Sandbox → Testers |
| 2 | Create test account (use fake email, any name) |
| 3 | On device: Settings → App Store → Sandbox Account → sign in |
| 4 | Launch app → trigger paywall → test purchase flow |
| 5 | Verify: trial starts, restore works, cancel works |

### 5.3 Archive and Upload

| Step | Action |
|------|--------|
| 1 | In Xcode: Product → Archive |
| 2 | Wait for archive to complete |
| 3 | Window → Organizer → select archive → Distribute App |
| 4 | Choose "App Store Connect" → Upload |
| 5 | Wait for processing email from Apple (5–30 minutes) |

### 5.4 Submit for Review

| Step | Action |
|------|--------|
| 1 | App Store Connect → select build |
| 2 | Fill in all metadata fields |
| 3 | Verify review notes are filled in |
| 4 | Click "Submit for Review" |
| 5 | Expected review time: 24–48 hours |

---

## Phase 6: Post-Submission

### If Approved
- Monitor crash reports in Xcode Organizer
- Respond to App Store reviews
- Plan content updates

### If Rejected
Common reasons and fixes:

| Guideline | Reason | Fix |
|-----------|--------|-----|
| 2.1 | App crashes | Check `plans.json` loads properly, no force-unwraps |
| 3.1.1 | Subscription issues | Ensure StoreKit `displayPrice` used, legal links present |
| 4.3 | Too similar to other app | More differentiation needed — see `APP_STORE_DIFFERENTIATION.md` |
| 5.1.1 | Privacy | Update `PrivacyInfo.xcprivacy` and App Privacy in ASC |

**To appeal or respond:** App Store Connect → Resolution Center

---

## Quick Reference: Files to Change

| File | Change Required | Difficulty |
|------|----------------|------------|
| `SpecialtyConfig.swift` | Replace all values | Easy (fill in blanks) |
| `Category.swift` | Replace all categories | Medium (new data) |
| `Reference.swift` | Replace scales/exams/tools | Medium (new data) |
| `ExamToolsView.swift` | Full rewrite of enum + detail views | Hard (new UI code) |
| `CalculatorEngine.swift` | Add specialty calculators | Hard (new formulas) |
| `plans.json` | Generate from plan markdown files | Easy (use script) |
| `scales.json`, `exams.json`, `tools.json` | New reference data | Medium |
| `Configuration.storekit` | Update product ID, app ID, team ID | Easy |
| `AppIcon` (asset catalog) | Replace icon image | Easy (drag & drop) |
| `PrivacyInfo.xcprivacy` | Usually no changes needed | None |
| Legal docs (privacy, terms) | Copy and replace names/emails | Easy |

---

## Differentiation Checklist (Guideline 4.3)

Before submitting, verify ALL of these are different from every other specialty app:

- [ ] App icon — visually distinct (different shape, color, symbol)
- [ ] Brand color (`brandColorHex`) — different hex value
- [ ] Header icon — different SF Symbol
- [ ] Tagline — mentions your specialty
- [ ] Paywall features — lists your specialty's content
- [ ] Quick actions — your specialty's emergency protocols
- [ ] About description — your specialty
- [ ] Exam tools — completely different tools
- [ ] Categories — your specialty's diagnoses
- [ ] Scales/calculators — your specialty's scoring tools
- [ ] Support email — your domain
- [ ] Legal URLs — your domain
- [ ] App Store screenshots — show your specialty content
- [ ] App Store description — describes your specialty

---

## Annual Costs Per Specialty App

| Item | Cost | Notes |
|------|------|-------|
| Domain (.app) | ~$15/year | Porkbun, includes email forwarding |
| Apple Developer | $99/year | **Shared** across all apps (pay once) |
| Supabase | $0/year | Free tier (up to 50K monthly active users) |
| **Total (first app)** | **~$114/year** | Includes developer program |
| **Total (each additional)** | **~$15/year** | Just the domain |
