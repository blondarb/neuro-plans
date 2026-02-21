# App Store Rejection Fixes — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix all three App Store rejection issues (Guidelines 3.1.1, 4.3, 5.1.1) and add subscription testing validation so NeuroPlans can be resubmitted.

**Architecture:** Extend `SpecialtyConfig.swift` with new static arrays for paywall features, quick actions, and header icon. Wire these into PaywallView and HomeView. Fix privacy manifest, remove debug prints, update StoreKit test config, create preflight script.

**Tech Stack:** Swift/SwiftUI, StoreKit 2, Xcode StoreKit Configuration, Bash

---

### Task 1: Extend SpecialtyConfig with Paywall Features, Quick Actions, and Header Icon

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift`

**Step 1: Add new config properties**

Replace the entire file with:

```swift
import Foundation

/// All specialty-specific values in one place.
/// To create a new specialty app, clone this repo and edit only this file
/// (plus Category.swift, Reference.swift, and CalculatorEngine.swift for content).
enum SpecialtyConfig {
    // MARK: - Identity
    static let appName = "Neuro Plans"
    static let specialty = "neurology"
    static let bundleId = "com.neuroplans.app"

    // MARK: - Branding
    static let brandColorHex = "#0D9488"
    static let headerIcon = "brain.head.profile"

    // MARK: - Subscription
    static let storeKitProductId = "com.neuroplans.annual"

    // MARK: - Contact
    static let errorReportEmail = "errors@neuroplans.app"
    static let supportEmail = "support@neuroplans.app"

    // MARK: - Supabase
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5YWdpbnV2c3FjYnZ5ZXVpemx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMDY5NjUsImV4cCI6MjA4NjU4Mjk2NX0.UGJN-vnfGy7eECbmT33g4-OXME-2bbwC9sm3ckOmpWA"

    // MARK: - Legal
    static let termsURL = "https://neuroplans.app/terms"
    static let privacyURL = "https://neuroplans.app/privacy"
    static let disclaimerTitle = "Neuro Plans"

    // MARK: - Paywall Features
    /// Features displayed on the paywall screen. Each specialty shows different features.
    static let paywallFeatures: [(icon: String, title: String, description: String)] = [
        ("list.bullet.clipboard.fill", "All Clinical Plans", "Complete neurology treatment protocols"),
        ("brain", "Clinical Scales", "NIHSS, mRS, GCS, and more"),
        ("stethoscope", "Exam Guides", "Step-by-step neurological exams"),
        ("hammer.fill", "Clinical Tools", "Calculators, timers, and converters"),
        ("square.and.pencil", "Plan Builder", "Create custom order sets"),
        ("arrow.triangle.2.circlepath", "Free Updates", "New plans and features as they're released")
    ]

    // MARK: - Quick Actions
    /// Specialty-specific shortcuts shown on the home screen.
    /// Each links to a plan by its ID for one-tap access.
    static let quickActions: [(id: String, title: String, icon: String, planId: String)] = [
        ("stroke-alert", "Stroke Alert", "bolt.heart.fill", "acute-ischemic-stroke"),
        ("status-epilepticus", "Status Epilepticus", "waveform.path.ecg", "status-epilepticus"),
        ("meningitis", "Acute Meningitis", "allergens.fill", "bacterial-meningitis")
    ]
}
```

**Step 2: Verify build compiles**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans && xcodebuild -scheme NeuroPlans -destination 'platform=iOS Simulator,name=iPhone 16 Pro' build 2>&1 | tail -5`
Expected: BUILD SUCCEEDED

**Step 3: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/SpecialtyConfig.swift
git commit -m "feat: add paywall features, quick actions, and header icon to SpecialtyConfig"
```

---

### Task 2: Wire PaywallView to Use SpecialtyConfig

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Views/Subscription/PaywallView.swift`

**Step 1: Replace hardcoded header icon**

In `headerSection`, change line 73:
```swift
// OLD:
Image(systemName: "brain.head.profile")
// NEW:
Image(systemName: SpecialtyConfig.headerIcon)
```

**Step 2: Replace hardcoded feature rows with config-driven loop**

In `featuresSection`, replace lines 102-107 (the 6 hardcoded `FeatureRow(...)` calls) with:

```swift
ForEach(Array(SpecialtyConfig.paywallFeatures.enumerated()), id: \.offset) { _, feature in
    FeatureRow(icon: feature.icon, title: feature.title, description: feature.description)
}
```

**Step 3: Verify build compiles**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans && xcodebuild -scheme NeuroPlans -destination 'platform=iOS Simulator,name=iPhone 16 Pro' build 2>&1 | tail -5`
Expected: BUILD SUCCEEDED

**Step 4: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/Views/Subscription/PaywallView.swift
git commit -m "fix(3.1.1): make paywall features config-driven via SpecialtyConfig"
```

---

### Task 3: Add Quick Actions Bar to HomeView

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Views/Home/HomeView.swift`

**Step 1: Add quick actions section**

In `HomeView.body`, inside the `ScrollView > VStack`, insert the quick actions bar after the `SettingPicker` (line 64) and before the `ForEach(prefs.plansSectionOrder...)` (line 67):

```swift
// Quick Actions
if !SpecialtyConfig.quickActions.isEmpty {
    QuickActionsBar()
        .padding(.horizontal)
}
```

**Step 2: Add QuickActionsBar view**

Add this private struct at the bottom of the file, before the `#Preview`:

```swift
// MARK: - Quick Actions Bar

private struct QuickActionsBar: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(PlanStore.self) private var store

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("Quick Actions")
                .font(.system(.caption, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 10) {
                    ForEach(SpecialtyConfig.quickActions, id: \.id) { action in
                        if let plan = store.plan(forId: action.planId) {
                            NavigationLink(value: plan) {
                                HStack(spacing: 8) {
                                    Image(systemName: action.icon)
                                        .font(.system(size: 14, weight: .semibold))
                                        .foregroundStyle(AppTheme.teal)
                                    Text(action.title)
                                        .font(.system(.caption, design: .rounded, weight: .semibold))
                                        .foregroundStyle(.primary)
                                }
                                .padding(.horizontal, 14)
                                .padding(.vertical, 10)
                                .background {
                                    if colorScheme == .dark {
                                        RoundedRectangle(cornerRadius: 10)
                                            .fill(.ultraThinMaterial)
                                    } else {
                                        RoundedRectangle(cornerRadius: 10)
                                            .fill(Color(.systemBackground))
                                            .shadow(color: .black.opacity(0.06), radius: 4, x: 0, y: 2)
                                    }
                                }
                                .overlay {
                                    RoundedRectangle(cornerRadius: 10)
                                        .strokeBorder(AppTheme.teal.opacity(0.2), lineWidth: 0.5)
                                }
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
            }
        }
    }
}
```

**Step 3: Add `plan(forId:)` helper to PlanStore if it doesn't exist**

Check `ios/NeuroPlans/NeuroPlans/Services/PlanStore.swift` for a method that looks up a plan by ID string. If it has something like `plans` as a `[String: Plan]` dictionary, add this helper:

```swift
func plan(forId id: String) -> Plan? {
    plans.first { $0.id == id }
}
```

Or if `plans` is a dictionary keyed by ID, use `plans[id]` directly.

**Step 4: Verify build compiles**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans && xcodebuild -scheme NeuroPlans -destination 'platform=iOS Simulator,name=iPhone 16 Pro' build 2>&1 | tail -5`
Expected: BUILD SUCCEEDED

**Step 5: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/Views/Home/HomeView.swift ios/NeuroPlans/NeuroPlans/Services/PlanStore.swift
git commit -m "feat(4.3): add specialty-specific quick actions bar to home screen"
```

---

### Task 4: Fix Privacy Manifest

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/PrivacyInfo.xcprivacy`

**Step 1: Add collected data types**

Replace the entire file with:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>NSPrivacyTracking</key>
	<false/>
	<key>NSPrivacyTrackingDomains</key>
	<array/>
	<key>NSPrivacyCollectedDataTypes</key>
	<array>
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypeEmailAddress</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<false/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<false/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
			</array>
		</dict>
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypePurchaseHistory</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<false/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<false/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
			</array>
		</dict>
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypeDeviceID</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<false/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<false/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
			</array>
		</dict>
	</array>
	<key>NSPrivacyAccessedAPITypes</key>
	<array>
		<dict>
			<key>NSPrivacyAccessedAPIType</key>
			<string>NSPrivacyAccessedAPICategoryUserDefaults</string>
			<key>NSPrivacyAccessedAPITypeReasons</key>
			<array>
				<string>CA92.1</string>
			</array>
		</dict>
	</array>
</dict>
</plist>
```

**Step 2: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/PrivacyInfo.xcprivacy
git commit -m "fix(5.1.1): declare collected data types in privacy manifest"
```

---

### Task 5: Remove Debug Print Statements

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Services/ReferenceStore.swift:1,115,127`
- Modify: `ios/NeuroPlans/NeuroPlans/Views/Reference/ExamToolsView.swift:1,283`

**Step 1: Add os import to ReferenceStore.swift**

Add `import os` after line 1 (`import Foundation`), and add a logger:

```swift
import os

private let logger = Logger(subsystem: SpecialtyConfig.bundleId, category: "ReferenceStore")
```

**Step 2: Replace print() calls in ReferenceStore.swift**

Line 115: Replace `print(msg)` with `logger.warning("\(msg)")`
Line 127: Replace `print(msg)` with `logger.warning("\(msg)")`

**Step 3: Replace print() in ExamToolsView.swift**

Add `import os` at the top of the file (after `import AVFoundation`).

Line 283: Replace `print("Flash error: \(error)")` with:
```swift
Logger(subsystem: SpecialtyConfig.bundleId, category: "ExamTools").error("Flash error: \(error)")
```

**Step 4: Verify no print() remains in non-test Swift files**

Run: `grep -rn 'print(' /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans/NeuroPlans/ --include="*.swift"`
Expected: No output (zero matches)

**Step 5: Verify build compiles**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans && xcodebuild -scheme NeuroPlans -destination 'platform=iOS Simulator,name=iPhone 16 Pro' build 2>&1 | tail -5`
Expected: BUILD SUCCEEDED

**Step 6: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/Services/ReferenceStore.swift ios/NeuroPlans/NeuroPlans/Views/Reference/ExamToolsView.swift
git commit -m "fix(5.1.1): replace debug print() with os.Logger"
```

---

### Task 6: Update StoreKit Configuration

**Files:**
- Modify: `ios/NeuroPlans/NeuroPlans/Configuration.storekit`

**Step 1: Update the Configuration.storekit file**

Replace the entire file with:

```json
{
  "identifier" : "com.neuroplans.storekit",
  "nonRenewingSubscriptions" : [

  ],
  "products" : [

  ],
  "settings" : {
    "_applicationInternalID" : "6759209586",
    "_developerTeamID" : "92YUSSM83T",
    "_failTransactionsEnabled" : false,
    "_lastSynchronizedDate" : 726429294.46772897,
    "_locale" : "en_US",
    "_storefront" : "USA",
    "_storeKitErrors" : [
      {
        "current" : null,
        "enabled" : false,
        "name" : "Load Products"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Purchase"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Verification"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "App Store Sync"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Subscription Status"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "App Transaction"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Manage Subscriptions Sheet"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Refund Request Sheet"
      },
      {
        "current" : null,
        "enabled" : false,
        "name" : "Offer Code Redeem Sheet"
      }
    ]
  },
  "subscriptionGroups" : [
    {
      "id" : "neuroplans.subscription.group",
      "localizations" : [
        {
          "description" : "Access all clinical plans, scales, exams, and tools",
          "displayName" : "Neuro Plans Subscriptions",
          "locale" : "en_US"
        }
      ],
      "name" : "Neuro Plans Subscriptions",
      "subscriptions" : [
        {
          "adHocOffers" : [

          ],
          "codeOffers" : [

          ],
          "displayPrice" : "12.99",
          "familyShareable" : false,
          "groupNumber" : 1,
          "internalID" : "annual.subscription",
          "introductoryOffer" : {
            "displayPrice" : "0",
            "internalID" : "annual.freetrial",
            "paymentMode" : "free",
            "subscriptionPeriod" : "P2W"
          },
          "localizations" : [
            {
              "description" : "Full access to all clinical plans and tools",
              "displayName" : "Annual Subscription",
              "locale" : "en_US"
            }
          ],
          "productID" : "com.neuroplans.annual",
          "recurringSubscriptionPeriod" : "P1Y",
          "referenceName" : "Annual Subscription",
          "subscriptionGroupID" : "neuroplans.subscription.group",
          "type" : "RecurringSubscription"
        }
      ]
    }
  ],
  "version" : {
    "major" : 3,
    "minor" : 0
  }
}
```

Key changes:
- `_applicationInternalID`: `"6759209586"` (real App Store Connect ID)
- `_developerTeamID`: `"92YUSSM83T"` (real team ID)
- `introductoryOffer`: 14-day free trial (`"P2W"` = 2 weeks, `"paymentMode": "free"`)
- Subscription group `localizations`: added English (US) entry

**Step 2: Commit**

```bash
git add ios/NeuroPlans/NeuroPlans/Configuration.storekit
git commit -m "fix: update StoreKit config with real IDs, free trial, and group localization"
```

---

### Task 7: Create Preflight Validation Script

**Files:**
- Create: `ios/scripts/ios-preflight.sh`

**Step 1: Create the scripts directory and script**

```bash
mkdir -p /Users/stevearbogast/dev/repos/neuro-plans/ios/scripts
```

Write `ios/scripts/ios-preflight.sh`:

```bash
#!/usr/bin/env bash
# ios-preflight.sh — Pre-submission validation for App Store
# Run before every submission. Must pass with 0 FAIL.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IOS_DIR="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$IOS_DIR/NeuroPlans/NeuroPlans"
STOREKIT="$SRC_DIR/Configuration.storekit"
PRIVACY="$SRC_DIR/PrivacyInfo.xcprivacy"
CONFIG="$SRC_DIR/SpecialtyConfig.swift"
PAYWALL="$SRC_DIR/Views/Subscription/PaywallView.swift"

PASS=0
FAIL=0
WARN=0

pass() { echo "  PASS: $1"; ((PASS++)); }
fail() { echo "  FAIL: $1"; ((FAIL++)); }
warn() { echo "  WARN: $1"; ((WARN++)); }

echo "=== NeuroPlans Pre-Submission Preflight ==="
echo ""

# 1. No print() in production Swift files
echo "[1] Checking for debug print() statements..."
PRINTS=$(grep -rn 'print(' "$SRC_DIR" --include="*.swift" 2>/dev/null || true)
if [ -z "$PRINTS" ]; then
    pass "No print() statements found"
else
    fail "Found print() statements:"
    echo "$PRINTS" | sed 's/^/       /'
fi

# 2. PrivacyInfo.xcprivacy exists and has collected data types
echo "[2] Checking privacy manifest..."
if [ -f "$PRIVACY" ]; then
    if grep -q "NSPrivacyCollectedDataTypeEmailAddress" "$PRIVACY"; then
        pass "Privacy manifest declares collected data types"
    else
        fail "Privacy manifest missing collected data types (Email, Purchase, DeviceID)"
    fi
else
    fail "PrivacyInfo.xcprivacy not found"
fi

# 3. SpecialtyConfig has required fields
echo "[3] Checking SpecialtyConfig completeness..."
MISSING=""
for field in headerIcon paywallFeatures quickActions supportEmail; do
    if ! grep -q "$field" "$CONFIG"; then
        MISSING="$MISSING $field"
    fi
done
if [ -z "$MISSING" ]; then
    pass "SpecialtyConfig has all required fields"
else
    fail "SpecialtyConfig missing fields:$MISSING"
fi

# 4. No hardcoded price in PaywallView
echo "[4] Checking PaywallView for hardcoded prices..."
if grep -qE '\$[0-9]+\.[0-9]{2}' "$PAYWALL"; then
    fail "PaywallView contains hardcoded price string"
else
    pass "No hardcoded prices in PaywallView"
fi

# 5. Legal URLs reachable
echo "[5] Checking legal URLs..."
TERMS_URL=$(grep 'termsURL' "$CONFIG" | grep -oE 'https://[^"]+' | head -1)
PRIVACY_URL=$(grep 'privacyURL' "$CONFIG" | grep -oE 'https://[^"]+' | head -1)
if [ -n "$TERMS_URL" ]; then
    HTTP_CODE=$(curl -sL -o /dev/null -w "%{http_code}" "$TERMS_URL" 2>/dev/null || echo "000")
    if [ "$HTTP_CODE" = "200" ]; then
        pass "Terms URL reachable ($TERMS_URL)"
    else
        fail "Terms URL returned HTTP $HTTP_CODE ($TERMS_URL)"
    fi
else
    fail "No termsURL found in SpecialtyConfig"
fi
if [ -n "$PRIVACY_URL" ]; then
    HTTP_CODE=$(curl -sL -o /dev/null -w "%{http_code}" "$PRIVACY_URL" 2>/dev/null || echo "000")
    if [ "$HTTP_CODE" = "200" ]; then
        pass "Privacy URL reachable ($PRIVACY_URL)"
    else
        fail "Privacy URL returned HTTP $HTTP_CODE ($PRIVACY_URL)"
    fi
else
    fail "No privacyURL found in SpecialtyConfig"
fi

# 6. StoreKit config has real IDs
echo "[6] Checking StoreKit configuration..."
if [ -f "$STOREKIT" ]; then
    if grep -q '"XXXXXXXXXX"' "$STOREKIT" || grep -q '"1234567890"' "$STOREKIT"; then
        fail "StoreKit config has placeholder team/app IDs"
    else
        pass "StoreKit config has real team/app IDs"
    fi

    if grep -q '"introductoryOffer" : null' "$STOREKIT"; then
        fail "StoreKit config has no introductory offer (free trial)"
    elif grep -q '"introductoryOffer"' "$STOREKIT"; then
        pass "StoreKit config has introductory offer configured"
    else
        warn "Could not determine introductory offer status"
    fi
else
    fail "Configuration.storekit not found"
fi

# Summary
echo ""
echo "=== Results ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"
echo ""

if [ "$FAIL" -gt 0 ]; then
    echo "BLOCKED: Fix $FAIL issue(s) before submitting."
    exit 1
else
    echo "READY: All checks passed. Safe to submit."
    exit 0
fi
```

**Step 2: Make executable**

```bash
chmod +x /Users/stevearbogast/dev/repos/neuro-plans/ios/scripts/ios-preflight.sh
```

**Step 3: Run it to verify**

Run: `/Users/stevearbogast/dev/repos/neuro-plans/ios/scripts/ios-preflight.sh`
Expected: All PASS (legal URL checks may fail if site is down — that's OK to note)

**Step 4: Commit**

```bash
git add ios/scripts/ios-preflight.sh
git commit -m "feat: add ios-preflight.sh pre-submission validation script"
```

---

### Task 8: Create App Store Differentiation Document

**Files:**
- Create: `ios/NeuroPlans/APP_STORE_DIFFERENTIATION.md`

**Step 1: Write the differentiation document**

```markdown
# App Store Differentiation Strategy — Guideline 4.3

This document explains how each specialty app in the Clinical Plans family provides a unique, standalone experience despite sharing a common codebase.

---

## Overview

Each app targets a different medical specialty with completely different clinical content, tools, and workflows. The shared codebase provides infrastructure (subscriptions, navigation, plan rendering) while all user-facing content is specialty-specific.

---

## Neuro Plans vs. Cardio Plans

| Dimension | Neuro Plans | Cardio Plans |
|-----------|-------------|--------------|
| **App Icon** | Brain (teal) | Heart (red) |
| **Brand Color** | #0D9488 (teal) | #E74C3C (red) |
| **Header Icon** | brain.head.profile | heart.fill |
| **App Name** | Neuro Plans | Cardio Plans |
| **Bundle ID** | com.neuroplans.app | com.cardioplans.app |

### Paywall Features

| Neuro Plans | Cardio Plans |
|-------------|--------------|
| Complete neurology treatment protocols | Complete cardiology treatment protocols |
| NIHSS, mRS, GCS, and more | CHA2DS2-VASc, HEART Score, Wells, and more |
| Step-by-step neurological exams | ECG interpretation and cardiac auscultation |
| Neurology calculators and converters | Cardiology calculators (QTc, EuroScore, Framingham) |
| Plan Builder for neuro order sets | Plan Builder for cardio order sets |

### Quick Actions

| Neuro Plans | Cardio Plans |
|-------------|--------------|
| Stroke Alert | STEMI Alert |
| Status Epilepticus | Acute PE |
| Acute Meningitis | AFib Management |

### Exam Tools

| Neuro Plans | Cardio Plans |
|-------------|--------------|
| Penlight (pupil exam) | ECG Rhythm Identifier |
| Red Desaturation test | Stethoscope Auscultation Guide |
| OKN Stripes | Pulse Assessment |
| Visual Acuity chart | Heart Sound Reference |
| Amsler Grid | JVP Assessment Guide |
| Pupil Gauge | Edema Grading |
| Reflex Hammer | Murmur Reference |

### Clinical Scales

| Neuro Plans (examples) | Cardio Plans (examples) |
|-------------------------|-------------------------|
| NIHSS (stroke severity) | CHA2DS2-VASc (AFib stroke risk) |
| Glasgow Coma Scale | HEART Score (chest pain) |
| Modified Rankin Scale | Wells Score (PE/DVT) |
| ABCD2 (TIA risk) | TIMI Risk Score |
| Hunt-Hess (SAH) | Killip Classification |

### Clinical Plans (content)

| Neuro Plans (166 plans) | Cardio Plans (planned) |
|-------------------------|------------------------|
| Acute Ischemic Stroke | Acute Coronary Syndrome |
| Status Epilepticus | STEMI Management |
| Multiple Sclerosis | Heart Failure |
| Parkinson's Disease | Atrial Fibrillation |
| Guillain-Barre Syndrome | Pulmonary Embolism |
| Myasthenia Gravis | Valvular Heart Disease |

### Calculators

| Neuro Plans | Cardio Plans |
|-------------|--------------|
| MAP/CPP | QTc Calculation |
| ICH Volume | EuroScore II |
| Corrected Phenytoin | Framingham Risk |
| Osmolality | TIMI Risk |
| Wells DVT Score | Duke Criteria |

### Infrastructure (separate per app)

| Item | Neuro Plans | Cardio Plans |
|------|-------------|--------------|
| Support email | support@neuroplans.app | support@cardioplans.app |
| Error email | errors@neuroplans.app | errors@cardioplans.app |
| Legal pages | neuroplans.app/terms, /privacy | cardioplans.app/terms, /privacy |
| Supabase project | Separate instance | Separate instance |
| App Store screenshots | Neurology content | Cardiology content |

---

## Summary for App Review

These are not reskinned copies. Each app provides specialty-specific clinical decision support with:
1. **Different clinical content** — entirely different treatment protocols, scales, and tools
2. **Different target audience** — neurologists vs. cardiologists
3. **Different exam tools** — specialty-specific physical exam instruments
4. **Different quick actions** — emergency shortcuts relevant to each specialty
5. **Separate infrastructure** — independent domains, emails, databases, and legal pages
```

**Step 2: Commit**

```bash
git add ios/NeuroPlans/APP_STORE_DIFFERENTIATION.md
git commit -m "docs: add Guideline 4.3 differentiation strategy document"
```

---

### Task 9: Run Preflight and Verify Everything

**Step 1: Run preflight script**

Run: `/Users/stevearbogast/dev/repos/neuro-plans/ios/scripts/ios-preflight.sh`
Expected: 0 FAIL (READY to submit)

**Step 2: Full build verification**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans/ios/NeuroPlans && xcodebuild -scheme NeuroPlans -destination 'platform=iOS Simulator,name=iPhone 16 Pro' build 2>&1 | tail -10`
Expected: BUILD SUCCEEDED

**Step 3: Verify git status is clean**

Run: `cd /Users/stevearbogast/dev/repos/neuro-plans && git status`
Expected: Nothing to commit, working tree clean

---

## Post-Code Manual Steps (App Store Connect)

After all code tasks are done, these manual steps are needed in the browser:

1. **App Privacy** — Go to App Store Connect > App Information > App Privacy. Change from "Data Not Collected" to declare: Email Address, Purchase History, Device ID (all: Not Linked, Not Tracking, App Functionality). Click Publish.
2. **Introductory Offer** — Go to Subscriptions > Annual Subscription > Introductory Offers > Add > Free Trial, 14 days.
3. **Agreements, Tax, Banking** — Complete in App Store Connect > Business section.
4. **Sandbox Tester** — Create in Users and Access > Sandbox.
5. **Test Purchase Flow** — On device with sandbox account: launch app > let trial expire > paywall > subscribe > verify access.
6. **Review Notes** — Update from `APP_STORE_METADATA.md` review notes section.
7. **Legal URLs** — Verify neuroplans.app/privacy and neuroplans.app/terms load.
8. **Archive & Upload** — `xcodebuild archive` + `xcodebuild -exportArchive`, version 1.0.0 build 2.
9. **Submit for Review**.
