#!/bin/bash
# ios-preflight.sh — Pre-submission validation for App Store review
# Run from the repo root: bash ios/scripts/ios-preflight.sh

set -euo pipefail

FAIL=0
WARN=0
PASS=0
SRC="ios/NeuroPlans/NeuroPlans"

pass() { ((PASS++)); echo "  ✅ PASS: $1"; }
fail() { ((FAIL++)); echo "  ❌ FAIL: $1"; }
warn() { ((WARN++)); echo "  ⚠️  WARN: $1"; }

echo "╔══════════════════════════════════════════╗"
echo "║   iOS App Store Pre-flight Checks        ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# ── 1. No print() calls in Swift source (excluding tests) ──
echo "── 1. Debug print() statements ──"
PRINTS=$(grep -rn 'print(' "$SRC" --include='*.swift' | grep -v 'Test' | grep -v '\.build/' || true)
if [ -z "$PRINTS" ]; then
    pass "No print() calls in source"
else
    fail "Found print() calls in source:"
    echo "$PRINTS" | head -10
fi
echo ""

# ── 2. PrivacyInfo.xcprivacy has collected data types ──
echo "── 2. Privacy manifest ──"
PRIVACY="$SRC/PrivacyInfo.xcprivacy"
if [ -f "$PRIVACY" ]; then
    if grep -q 'NSPrivacyCollectedDataType' "$PRIVACY"; then
        pass "PrivacyInfo.xcprivacy has NSPrivacyCollectedDataTypes entries"
    else
        fail "PrivacyInfo.xcprivacy has empty NSPrivacyCollectedDataTypes"
    fi
else
    fail "PrivacyInfo.xcprivacy not found"
fi
echo ""

# ── 3. SpecialtyConfig has required fields ──
echo "── 3. SpecialtyConfig completeness ──"
CONFIG="$SRC/SpecialtyConfig.swift"
if [ -f "$CONFIG" ]; then
    for field in headerIcon paywallFeatures quickActions supportEmail; do
        if grep -q "$field" "$CONFIG"; then
            pass "SpecialtyConfig has $field"
        else
            fail "SpecialtyConfig missing $field"
        fi
    done
else
    fail "SpecialtyConfig.swift not found"
fi
echo ""

# ── 4. Legal URLs reachable ──
echo "── 4. Legal URLs ──"
for url in "https://neuroplans.app/terms" "https://neuroplans.app/privacy"; do
    STATUS=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 10 "$url" 2>/dev/null || echo "000")
    if [ "$STATUS" = "200" ] || [ "$STATUS" = "301" ] || [ "$STATUS" = "302" ]; then
        pass "$url responds ($STATUS)"
    else
        warn "$url returned $STATUS (may not be deployed yet)"
    fi
done
echo ""

# ── 5. No hardcoded price strings in PaywallView ──
echo "── 5. Hardcoded prices ──"
PAYWALL="$SRC/Views/Subscription/PaywallView.swift"
if [ -f "$PAYWALL" ]; then
    PRICES=$(grep -nE '\$[0-9]+\.[0-9]{2}' "$PAYWALL" || true)
    if [ -z "$PRICES" ]; then
        pass "No hardcoded prices in PaywallView"
    else
        fail "Found hardcoded prices in PaywallView:"
        echo "$PRICES"
    fi
else
    fail "PaywallView.swift not found"
fi
echo ""

# ── 6. StoreKit config has real IDs ──
echo "── 6. StoreKit configuration ──"
STOREKIT="$SRC/Configuration.storekit"
if [ -f "$STOREKIT" ]; then
    if grep -q 'XXXXXXXXXX' "$STOREKIT"; then
        fail "Configuration.storekit has placeholder team ID"
    else
        pass "Team ID is set"
    fi

    if grep -q '1234567890' "$STOREKIT"; then
        fail "Configuration.storekit has placeholder app ID"
    else
        pass "App ID is set"
    fi

    if grep -q 'introductoryOffer' "$STOREKIT" && ! grep -q '"introductoryOffer" : null' "$STOREKIT"; then
        pass "Introductory offer is configured"
    else
        fail "No introductory offer configured"
    fi
else
    fail "Configuration.storekit not found"
fi
echo ""

# ── 7. Build number (informational) ──
echo "── 7. Build info ──"
PBXPROJ=$(find ios/NeuroPlans -name '*.pbxproj' 2>/dev/null | head -1)
if [ -n "$PBXPROJ" ]; then
    BUILD=$(grep -m1 'CURRENT_PROJECT_VERSION' "$PBXPROJ" | sed 's/.*= //' | sed 's/;.*//' | tr -d ' ' || echo "unknown")
    VERSION=$(grep -m1 'MARKETING_VERSION' "$PBXPROJ" | sed 's/.*= //' | sed 's/;.*//' | tr -d ' ' || echo "unknown")
    echo "  ℹ️  Version: $VERSION (build $BUILD)"
else
    warn "Could not find .pbxproj to read build number"
fi
echo ""

# ── Summary ──
echo "══════════════════════════════════════════"
echo "  Results: $PASS passed, $FAIL failed, $WARN warnings"
echo "══════════════════════════════════════════"

if [ "$FAIL" -gt 0 ]; then
    echo "  ⛔ NOT READY — fix $FAIL issue(s) before submitting"
    exit 1
else
    echo "  🚀 READY for App Store submission"
    exit 0
fi
