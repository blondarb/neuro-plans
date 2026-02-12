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

1. **Guideline 3.1.1 - Subscription issues**
   - Ensure all disclosures are present
   - Privacy policy accessible
   - Terms of service accessible

2. **Guideline 5.1.1 - Privacy**
   - Privacy policy must be accessible
   - Data collection must be disclosed

3. **Guideline 4.2 - Minimum functionality**
   - App must provide value
   - Not just a website wrapper

4. **Guideline 2.1 - Crashes**
   - Test thoroughly before submission
   - Check crash logs in Xcode

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

## Support Contacts

- Apple Developer Support: https://developer.apple.com/contact/
- App Review: https://developer.apple.com/contact/app-store/
- Finance/Payments: Through App Store Connect

---

Good luck with your launch! 🚀
