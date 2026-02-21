# Neuro Plans - App Store Publishing Guide

This guide walks you through everything needed to publish Neuro Plans to the App Store with in-app subscriptions.

---

## Phase 1: Pre-requisites & Accounts Setup

### 1.1 Create a Dedicated Email for the App

You'll need email addresses for:
- **Apple Developer Account**: developer@neuroplans.app (or similar)
- **Error Reports**: errors@neuroplans.app
- **Support Contact**: support@neuroplans.app

**Options:**
- Google Workspace ($6/month) - professional, custom domain
- Zoho Mail (free tier available) - custom domain
- iCloud+ with custom domain ($0.99/month)

**Action Items:**
- [ ] Register domain: neuroplans.app (Google Domains, Namecheap, etc.)
- [ ] Set up email hosting
- [ ] Create: developer@, errors@, support@ addresses

---

### 1.2 Apple Developer Program Enrollment

**Cost:** $99/year

**Steps:**
1. Go to https://developer.apple.com/programs/enroll/
2. Sign in with your Apple ID (or create one with your new developer email)
3. Choose enrollment type:
   - **Individual** - Simpler, your name appears as seller
   - **Organization** - Requires D-U-N-S number, company name appears as seller
4. Complete identity verification
5. Pay $99 annual fee
6. Wait for approval (usually 24-48 hours)

**Action Items:**
- [ ] Decide: Individual or Organization enrollment
- [ ] If Organization: Get D-U-N-S number (free, takes ~5 days) at https://developer.apple.com/support/D-U-N-S/
- [ ] Enroll at developer.apple.com
- [ ] Wait for approval email

---

## Phase 2: App Store Connect Setup

### 2.1 Create Your App in App Store Connect

Once your developer account is approved:

1. Go to https://appstoreconnect.apple.com
2. Click "My Apps" → "+" → "New App"
3. Fill in:
   - **Platform:** iOS
   - **Name:** Neuro Plans
   - **Primary Language:** English (U.S.)
   - **Bundle ID:** Create new → com.neuroplans.app (or your preference)
   - **SKU:** neuroplans-ios-001
   - **User Access:** Full Access

**Action Items:**
- [ ] Log into App Store Connect
- [ ] Create new app record
- [ ] Note your Bundle ID: _______________

---

### 2.2 Configure In-App Purchases (Subscriptions)

In App Store Connect → Your App → Monetization → Subscriptions:

1. **Create Subscription Group:**
   - Name: "Neuro Plans Pro"
   - Reference Name: neuroplans-subscription-group

2. **Create Subscription:**
   - Reference Name: Annual Subscription
   - Product ID: `com.neuroplans.annual` (MUST match code)
   - Subscription Duration: 1 Year
   - Price: $12.99 (Tier 13) or your chosen price
   - Localization:
     - Display Name: "Annual Subscription"
     - Description: "Full access to all clinical plans, scales, exams, and tools. Updated regularly with new content."

3. **Review Information (required for approval):**
   - Screenshot of subscription in action
   - Review notes explaining the subscription

**Action Items:**
- [ ] Create subscription group
- [ ] Create annual subscription product
- [ ] Set pricing
- [ ] Add localization text
- [ ] Upload subscription screenshot

---

### 2.3 Agreements, Tax, and Banking

**CRITICAL:** You cannot receive payments until this is complete!

In App Store Connect → Agreements, Tax, and Banking:

1. **Paid Applications Agreement:**
   - Accept the agreement
   - This covers app sales AND in-app purchases

2. **Tax Forms:**
   - Complete tax interview (W-9 for US)
   - Provide SSN or EIN

3. **Banking Information:**
   - Add bank account for deposits
   - Apple pays monthly, ~45 days after month end

**Action Items:**
- [ ] Accept Paid Applications agreement
- [ ] Complete tax forms
- [ ] Add bank account
- [ ] Verify all shows "Active" status

---

## Phase 3: Legal Requirements

### 3.1 Create Required Legal Pages

You MUST have these URLs before submitting:

**Privacy Policy** (required by Apple):
- What data you collect
- How you use it
- Third-party services
- Contact information

**Terms of Service** (required for subscriptions):
- Subscription terms
- Auto-renewal disclosure
- Cancellation policy
- Refund policy

**Suggested hosting:**
- GitHub Pages (free)
- Notion (free, public pages)
- Your own website

**Action Items:**
- [ ] Create Privacy Policy at: https://neuroplans.app/privacy
- [ ] Create Terms of Service at: https://neuroplans.app/terms
- [ ] Update URLs in PaywallView.swift if different

---

### 3.2 Required Subscription Disclosures

Apple requires these exact disclosures in your app and App Store listing:

> "Payment will be charged to your Apple ID account at confirmation of purchase. Subscription automatically renews unless canceled at least 24 hours before the end of the current period. Your account will be charged for renewal within 24 hours prior to the end of the current period. You can manage and cancel your subscriptions by going to your account settings on the App Store after purchase."

**This is already in PaywallView.swift** ✓

---

## Phase 4: App Store Listing

### 4.1 App Information

In App Store Connect → App Information:

- **Name:** Neuro Plans
- **Subtitle:** Clinical Neurology Reference (max 30 chars)
- **Category:** Medical
- **Secondary Category:** Reference (optional)
- **Content Rights:** "This app does not contain third-party content"
- **Age Rating:** Complete questionnaire (likely 4+ or 12+)

---

### 4.2 App Privacy

Apple requires privacy "nutrition labels":

**Data Types to declare:**
- Identifiers (if any analytics)
- Diagnostics (crash logs)
- Purchases (subscription status)

**Data NOT collected:**
- Health data (plans are reference only, not patient data)
- Contact info
- Location

---

### 4.3 Screenshots & Preview

**Required sizes:**
- 6.7" (iPhone 15 Pro Max): 1290 x 2796 pixels
- 6.5" (iPhone 14 Plus): 1284 x 2778 pixels
- 5.5" (iPhone 8 Plus): 1242 x 2208 pixels
- 12.9" iPad Pro: 2048 x 2732 pixels (if supporting iPad)

**Suggested screenshots:**
1. Plans list with categories
2. Plan detail view showing treatments
3. Clinical scales (NIHSS, etc.)
4. Plan Builder feature
5. Reference tools (calculators, etc.)

**Action Items:**
- [ ] Take screenshots on simulator
- [ ] Add marketing text overlays (optional)
- [ ] Upload all required sizes

---

### 4.4 App Description

**Example:**

```
Neuro Plans is a comprehensive clinical decision support tool for neurological diagnoses, designed by neurologists for neurologists, APPs, and trainees.

CLINICAL PLANS
• Evidence-based treatment protocols for stroke, seizures, MS, headache, and more
• Organized by clinical setting: ED, Hospital, Outpatient, ICU
• Lab workups, imaging studies, and medication dosing
• ICD-10 codes included

CLINICAL SCALES
• NIHSS, Glasgow Coma Scale, mRS, and more
• Interactive scoring with automatic calculation
• Reference ranges and interpretation

EXAM GUIDES
• Step-by-step neurological examination guides
• Motor, sensory, cranial nerve assessments

CLINICAL TOOLS
• Drug dosing calculators
• Unit converters
• Clinical timers

PLAN BUILDER
• Create custom order sets
• Combine items from multiple plans
• Export to paste into your EMR

FREE 14-DAY TRIAL
Try all features free for 14 days. Then continue with an annual subscription.

Questions or feedback? Contact support@neuroplans.app
```

---

### 4.5 Keywords

Max 100 characters, comma-separated:

```
neurology,stroke,NIHSS,clinical,medical,reference,treatment,protocol,seizure,headache,MS,EMR
```

---

## Phase 5: Xcode Configuration

### 5.1 Update Bundle Identifier

In Xcode → Project → Targets → Signing & Capabilities:

1. Set Bundle Identifier to match App Store Connect
2. Select your Team (your developer account)
3. Enable "Automatically manage signing"

**Action Items:**
- [ ] Update Bundle ID to: com.neuroplans.app
- [ ] Select signing team
- [ ] Verify no signing errors

---

### 5.2 Add In-App Purchase Capability

In Xcode → Targets → Signing & Capabilities:

1. Click "+ Capability"
2. Add "In-App Purchase"

---

### 5.3 Update Product ID

Verify the product ID in `EntitlementService.swift` matches App Store Connect:

```swift
static let annualSubscriptionID = "com.neuroplans.annual"
```

---

### 5.4 Update App Version

In Xcode → Project → General:

- **Version:** 1.0.0
- **Build:** 1

Increment Build for each upload to TestFlight.

---

## Phase 6: Testing

### 6.1 StoreKit Testing (Local)

The app includes `Configuration.storekit` for local testing:

1. In Xcode, Edit Scheme → Run → Options
2. Set "StoreKit Configuration" to Configuration.storekit
3. Run app - purchases work in simulator without real charges

---

### 6.2 Sandbox Testing (Real Devices)

1. In App Store Connect → Users and Access → Sandbox Testers
2. Create sandbox tester account (use fake email)
3. On test device: Settings → App Store → Sign out
4. In app, when prompted, sign in with sandbox account
5. Purchases are free but behave like real ones

**Action Items:**
- [ ] Create sandbox tester account
- [ ] Test subscription purchase flow
- [ ] Test restore purchases
- [ ] Test trial expiration → paywall

---

### 6.3 TestFlight Beta Testing

1. Archive app: Product → Archive
2. Upload to App Store Connect
3. In App Store Connect → TestFlight
4. Add internal testers (your team)
5. Optionally add external testers (requires review)

**Action Items:**
- [ ] Archive and upload build
- [ ] Add yourself as internal tester
- [ ] Install via TestFlight
- [ ] Test complete flow

---

## Phase 7: Submission

### 7.1 Build Upload

1. In Xcode: Product → Archive
2. Window → Organizer → Distribute App
3. Choose "App Store Connect"
4. Upload

---

### 7.2 Submit for Review

In App Store Connect:

1. Select your uploaded build
2. Complete all required fields
3. Answer export compliance (likely "No" for encryption)
4. Add review notes:
   - Test account (if needed)
   - Subscription explanation
   - Any special instructions

5. Click "Submit for Review"

**Review typically takes 24-48 hours.**

---

### 7.3 Common Rejection Reasons & Fixes

#### Guideline 3.1.1 — Subscription Disclosure (HIGH RISK)

Apple requires **all** of the following near the purchase button:

- [ ] Subscription price pulled from StoreKit (not hardcoded)
- [ ] Subscription period pulled from StoreKit (not hardcoded "/year")
- [ ] Explicit auto-renewal statement with price and period
- [ ] Cancellation instructions ("Settings > Apple ID > Subscriptions")
- [ ] Working "Restore Purchases" button (labeled clearly)
- [ ] Working links to Terms of Service and Privacy Policy
- [ ] Links must NOT force-unwrap: use `if let url = URL(...)` not `URL(...)!`

**Example disclosure text (must include actual price from StoreKit):**
> Payment of $12.99 will be charged to your Apple ID account at confirmation of purchase. Subscription automatically renews at $12.99/year unless canceled at least 24 hours before the end of the current period. You can manage or cancel your subscription in your device's Settings > Apple ID > Subscriptions.

**Common mistake:** Advertising a free trial in the App Store description or paywall UI when the introductory offer is NOT configured in App Store Connect. If you advertise "14-day free trial," the StoreKit product must have a matching introductory offer.

#### Guideline 4.3 — Spam / Duplicate Apps (HIGH RISK for multi-specialty)

If you publish multiple apps from the same template (e.g., Neuro Plans + Cardio Plans), Apple will reject both unless they are "sufficiently different." Each app must have:

- [ ] Different app icon and brand color
- [ ] Different header icon on disclaimer and paywall screens
- [ ] Different tagline and about description
- [ ] Different paywall feature list (mentions specialty-specific content)
- [ ] Different quick actions on home screen
- [ ] Different exam tools (specialty-specific, not shared)
- [ ] Different clinical scales and calculators
- [ ] Different categories and plan content
- [ ] Separate support email and legal documents
- [ ] Unique App Store screenshots showing specialty content
- [ ] App Review notes that explain the specialty focus

**All differentiation is driven through `SpecialtyConfig.swift`.** See `APP_STORE_DIFFERENTIATION.md` for the full strategy.

#### Guideline 5.1.1 — Privacy (MEDIUM RISK)

- [ ] `PrivacyInfo.xcprivacy` declares ALL accessed APIs and collected data types
- [ ] Privacy policy URL is live and accessible (test from a fresh browser)
- [ ] If using Supabase or any third-party backend, disclose it in privacy policy
- [ ] App Store Connect "App Privacy" section matches PrivacyInfo.xcprivacy

**Data types to declare in PrivacyInfo.xcprivacy:**
- `NSPrivacyAccessedAPICategoryUserDefaults` (for preferences, trial date, etc.)
- `NSPrivacyCollectedDataTypeEmailAddress` (if email verification is used)
- `NSPrivacyCollectedDataTypePurchaseHistory` (StoreKit subscription data)
- `NSPrivacyCollectedDataTypeDeviceID` (if device ID is generated for plan requests)

#### Guideline 4.2 — Minimum Functionality (LOW RISK)

App must provide native value beyond a web wrapper. Our apps include:
- Interactive clinical scales with scoring
- Exam tools with hardware integration (camera flash, gyroscope)
- Plan Builder with export
- Clinical calculators

#### Guideline 2.1 — Crashes (LOW RISK)

- [ ] No `fatalError()` calls in production code
- [ ] No force-unwraps (`!`) on values that could be nil at runtime
- [ ] No `print()` statements in production — use `os_log` / `Logger`
- [ ] Test on device (not just simulator) before submission
- [ ] Check Xcode Organizer for crash logs after TestFlight

---

### 7.4 Pre-Submission Checklist

Run this checklist **every time** before submitting any specialty app:

#### Code Quality
- [ ] Zero `fatalError()` calls (search entire project)
- [ ] Zero `print()` calls (use `Logger` from OSLog)
- [ ] No force-unwrapped URLs: `URL(string:)!` → `if let url = URL(string:)`
- [ ] All strings in PaywallView, SettingsView, DisclaimerView read from `SpecialtyConfig`
- [ ] `PrivacyInfo.xcprivacy` declares all APIs and data types

#### Subscription Compliance (Guideline 3.1.1)
- [ ] Price displayed from `product.displayPrice` (not hardcoded)
- [ ] Period displayed from `subscription.subscriptionPeriod(for:)` (not hardcoded)
- [ ] Auto-renewal disclosure includes price, period, and cancellation path
- [ ] "Restore Purchases" button visible and labeled
- [ ] Terms of Service link works
- [ ] Privacy Policy link works
- [ ] Manage Subscription link available for subscribed users
- [ ] Revoked/refunded transactions handled (`transaction.revocationDate` check)

#### App Store Connect
- [ ] Agreements, Tax, and Banking completed (status: "Active")
- [ ] Introductory offer configured (if trial is advertised)
- [ ] Sandbox tester created and tested
- [ ] App Privacy section published (not just configured)
- [ ] Screenshots uploaded for all required device sizes
- [ ] App Review notes explain subscription flow

#### Multi-Specialty (Guideline 4.3)
- [ ] Run `APP_STORE_DIFFERENTIATION.md` checklist
- [ ] Support email is unique per app (not shared)
- [ ] Legal docs reference correct app name and email
- [ ] App Store screenshots show specialty-specific content
- [ ] Review notes explain how this app differs from others

---

### 7.5 New Specialty App Setup

When cloning the codebase for a new specialty (e.g., Cardio Plans, Pulm Plans):

1. **Change ALL values in `SpecialtyConfig.swift`** — not just identity:
   - `appName`, `specialty`, `bundleId`
   - `brandColorHex`, `headerIcon`, `tagline`
   - `storeKitProductId`
   - `errorReportEmail`, `supportEmail`
   - `supabaseUrl`, `supabaseAnonKey` (create separate Supabase project)
   - `termsURL`, `privacyURL`, `disclaimerTitle`
   - `paywallFeatures` (specialty-specific feature descriptions)
   - `aboutDescription`, `aboutIcon`
   - `quickActions` (specialty-specific emergency protocols)

2. **Replace content files:**
   - `Category.swift` — new categories and plan IDs
   - `Reference.swift` — new scales, exams, and tools
   - `CalculatorEngine.swift` — add specialty-specific calculators
   - `ExamToolsView.swift` — replace exam tool enum with specialty tools
   - `plans.json` — new clinical plan data
   - `scales.json`, `exams.json`, `tools.json` — new reference data

3. **Create legal pages:**
   - Privacy policy at new domain (not shared with other apps)
   - Terms of service at new domain
   - Unique support email

4. **App Store Connect:**
   - Create separate app record
   - Create new subscription group and product
   - Upload unique screenshots
   - Write unique description and keywords

5. **Run the Pre-Submission Checklist (Section 7.4)**

---

## Phase 8: Post-Launch

### 8.1 Monitor & Respond

- Check App Store Connect daily for reviews
- Respond to user feedback
- Monitor crash reports in Xcode Organizer
- Check error report emails

### 8.2 Updates

For updates:
1. Increment Build number
2. Archive and upload
3. Submit for review
4. Updates typically review faster

---

## Quick Reference: Key Values

| Item | Value |
|------|-------|
| Bundle ID | com.neuroplans.app |
| Product ID | com.neuroplans.annual |
| Subscription Price | $12.99/year |
| Trial Duration | 14 days |
| Error Email | errors@neuroplans.app |
| Support Email | support@neuroplans.app |

---

## Claude Browser Session Script

Copy this prompt to start a guided session with Claude in your browser:

```
I'm publishing an iOS app called "Neuro Plans" to the App Store. It's a clinical neurology reference app with a $12.99/year subscription after a 14-day trial. I need help with:

1. Setting up my Apple Developer Account ($99/year)
2. Configuring App Store Connect for subscriptions
3. Setting up Agreements, Tax, and Banking to receive payments
4. Creating my Privacy Policy and Terms of Service
5. Writing my App Store listing (description, keywords, etc.)
6. Preparing for App Review

I'm currently at step: [DESCRIBE WHERE YOU ARE]

My questions/blockers:
- [LIST ANY SPECIFIC QUESTIONS]

Please guide me through the next steps.
```

---

## Submission Log: Version 1.0 (February 15, 2026)

**Status: Submitted for App Review (Waiting for Review)**

### What Was Done

| Step | Status | Notes |
|------|--------|-------|
| Apple Developer Account | Done | Individual enrollment, Team ID: 92YUSSM83T |
| App Store Connect record | Done | App ID: 6759209586, Bundle ID: com.neuroplans.app |
| Subscription configured | Done | Annual $12.99, Group ID: 21934633, Product Apple ID: 6759209768 |
| Subscription group localization | Done | English (U.S.), display name: "Neuro Plans Subscriptions" |
| Subscription review notes | Done | Describes paywall flow and trial |
| Age rating | Done | 4+ (Medical/Treatment Information: Infrequent/Mild) |
| App Privacy | Done | Published as "Data Not Collected" |
| Pricing | Done | Free ($0.00), 175 countries |
| iPhone screenshots (6.9") | Done | 5 screenshots, 1320x2868 (using 6.5" display slot) |
| iPad screenshots (13") | Done | 5 screenshots, 2048x2732 |
| Build archived via xcodebuild | Done | Archive at /tmp/NeuroPlans.xcarchive |
| Build uploaded via xcodebuild | Done | Version 1.0.0, Build 1 |
| Export compliance | Done | No encryption (HTTPS exemption only) |
| Build selected on version page | Done | Build 1.0.0 (1) |
| Submitted for review | Done | February 15, 2026 |

### What Was NOT Done (Post-Approval)

- **Introductory Offer (14-day free trial):** Not available in App Store Connect UI for first-time subscriptions. Must be configured after initial approval.
- **Agreements, Tax, and Banking:** Required for receiving subscription payments. Must be completed in App Store Connect Business section.
- **Subscription review screenshot:** Optional, was not required for submission.
- **Sandbox tester:** Not created yet. Recommended for post-approval testing.

### Key Learnings

1. **iPad screenshots are required** if `TARGETED_DEVICE_FAMILY = "1,2"` (iPhone + iPad). Set to `"1"` if iPhone-only to avoid this requirement.
2. **App Privacy must be explicitly Published** -- configuring responses is not enough; you must click the "Publish" button.
3. **Subscription group localization is required** -- even for English, you must create a localization entry for the subscription group.
4. **Screenshot uploads require manual interaction** -- browser automation cannot programmatically set files on file inputs due to browser security. Plan for manual drag-and-drop.
5. **xcodebuild can archive and export from CLI** -- no Xcode GUI needed for build/upload if signing is configured.
6. **Export compliance "No" for HTTPS-only apps** -- standard HTTPS exemption applies.

---

## Support Contacts

- Apple Developer Support: https://developer.apple.com/contact/
- App Review: https://developer.apple.com/contact/app-store/
- Finance/Payments: Through App Store Connect

---

Good luck with your launch! 🚀
