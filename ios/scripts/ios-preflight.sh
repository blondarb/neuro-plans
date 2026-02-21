#!/bin/bash
#
# iOS Pre-Submission Preflight Check
# Run before every App Store submission to catch common rejection risks.
#
# Usage:
#   ./ios/scripts/ios-preflight.sh [path-to-ios-project]
#
# Default path: ios/NeuroPlans/NeuroPlans (relative to repo root)

set -uo pipefail

# Colors
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m'

# Counters
ERRORS=0
WARNINGS=0
PASS=0

# Determine project path
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROJECT_DIR="${1:-$REPO_ROOT/ios/NeuroPlans/NeuroPlans}"

if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}ERROR: Project directory not found: $PROJECT_DIR${NC}"
    exit 1
fi

echo -e "${BOLD}=== iOS Pre-Submission Preflight Check ===${NC}"
echo "Project: $PROJECT_DIR"
echo ""

# Helper functions
fail() {
    echo -e "  ${RED}FAIL${NC} $1"
    ERRORS=$((ERRORS + 1))
}

warn() {
    echo -e "  ${YELLOW}WARN${NC} $1"
    WARNINGS=$((WARNINGS + 1))
}

pass() {
    echo -e "  ${GREEN}PASS${NC} $1"
    PASS=$((PASS + 1))
}

# ─────────────────────────────────────────────
# 1. Guideline 2.1 — Crash Risks
# ─────────────────────────────────────────────
echo -e "${BOLD}[Guideline 2.1] Crash Risks${NC}"

# Check for print() statements (should use Logger)
PRINTS=$(grep -rn 'print(' "$PROJECT_DIR" --include="*.swift" \
    | grep -v '#Preview' \
    | grep -v '// print' \
    | grep -v 'Tests/' \
    || true)
if [ -n "$PRINTS" ]; then
    fail "print() statements found (use Logger from OSLog):"
    echo "$PRINTS" | head -5 | sed 's/^/         /'
else
    pass "No print() statements in production code"
fi

# Check for force-unwrapped URLs
FORCE_URLS=$(grep -rn 'URL(string:.*)\!' "$PROJECT_DIR" --include="*.swift" \
    | grep -v 'Tests/' \
    || true)
if [ -n "$FORCE_URLS" ]; then
    fail "Force-unwrapped URLs found (use if let url = URL(string:)):"
    echo "$FORCE_URLS" | head -5 | sed 's/^/         /'
else
    pass "No force-unwrapped URLs"
fi

# Check for fatalError (excluding guarded config init)
FATALS=$(grep -rn 'fatalError(' "$PROJECT_DIR" --include="*.swift" \
    | grep -v 'Tests/' \
    | grep -v 'SpecialtyConfig' \
    || true)
if [ -n "$FATALS" ]; then
    warn "fatalError() calls found (verify these are config guards only):"
    echo "$FATALS" | head -5 | sed 's/^/         /'
else
    pass "No unexpected fatalError() calls"
fi

echo ""

# ─────────────────────────────────────────────
# 2. Guideline 3.1.1 — Subscription Compliance
# ─────────────────────────────────────────────
echo -e "${BOLD}[Guideline 3.1.1] Subscription Compliance${NC}"

# Check PaywallView uses StoreKit product data (not hardcoded prices)
PAYWALL="$PROJECT_DIR/Views/Subscription/PaywallView.swift"
if [ -f "$PAYWALL" ]; then
    if grep -q 'product\.displayPrice' "$PAYWALL"; then
        pass "PaywallView uses StoreKit displayPrice"
    else
        fail "PaywallView may have hardcoded pricing (missing product.displayPrice)"
    fi

    if grep -q 'subscriptionPeriod' "$PAYWALL"; then
        pass "PaywallView uses StoreKit subscription period"
    else
        fail "PaywallView may have hardcoded period (missing subscriptionPeriod)"
    fi

    if grep -q 'Restore' "$PAYWALL"; then
        pass "Restore Purchases button present"
    else
        fail "No Restore Purchases button found in PaywallView"
    fi

    if grep -q 'termsURL\|Terms of Service' "$PAYWALL"; then
        pass "Terms of Service link present"
    else
        fail "No Terms of Service link in PaywallView"
    fi

    if grep -q 'privacyURL\|Privacy Policy' "$PAYWALL"; then
        pass "Privacy Policy link present"
    else
        fail "No Privacy Policy link in PaywallView"
    fi

    if grep -q 'auto-renew\|Auto-renew\|automatically renews' "$PAYWALL" -i; then
        pass "Auto-renewal disclosure present"
    else
        fail "No auto-renewal disclosure in PaywallView"
    fi

    if grep -q 'revocationDate' "$PROJECT_DIR/Services/EntitlementService.swift" 2>/dev/null; then
        pass "Revocation/refund handling present in EntitlementService"
    else
        warn "No revocationDate check in EntitlementService (refunds may not be handled)"
    fi
else
    fail "PaywallView.swift not found at expected path"
fi

# Check StoreKit config has introductory offer
STOREKIT_CONFIG=$(find "$REPO_ROOT/ios" -name "*.storekit" -type f 2>/dev/null | head -1)
if [ -n "$STOREKIT_CONFIG" ]; then
    if grep -q 'introductoryOffer' "$STOREKIT_CONFIG" && ! grep -q '"introductoryOffer" : null' "$STOREKIT_CONFIG"; then
        pass "StoreKit config has introductory offer configured"
    else
        warn "StoreKit config has no introductory offer (configure if advertising free trial)"
    fi
else
    warn "No .storekit configuration file found"
fi

echo ""

# ─────────────────────────────────────────────
# 3. Guideline 4.3 — Differentiation
# ─────────────────────────────────────────────
echo -e "${BOLD}[Guideline 4.3] Differentiation${NC}"

CONFIG="$PROJECT_DIR/SpecialtyConfig.swift"
if [ -f "$CONFIG" ]; then
    # Check all required config properties exist
    for prop in appName specialty headerIcon tagline paywallFeatures aboutDescription quickActions supportEmail brandColorHex; do
        if grep -q "$prop" "$CONFIG"; then
            pass "SpecialtyConfig.$prop defined"
        else
            fail "SpecialtyConfig.$prop missing"
        fi
    done
else
    fail "SpecialtyConfig.swift not found"
fi

# Check for hardcoded app name in view files
HARDCODED=$(grep -rn '"Neuro Plans"\|"Cardio Plans"\|"Pulm Plans"' "$PROJECT_DIR" --include="*.swift" \
    | grep -v 'SpecialtyConfig.swift' \
    | grep -v 'Tests/' \
    || true)
if [ -n "$HARDCODED" ]; then
    fail "Hardcoded app name found outside SpecialtyConfig (use SpecialtyConfig.appName):"
    echo "$HARDCODED" | head -5 | sed 's/^/         /'
else
    pass "No hardcoded app names outside SpecialtyConfig"
fi

echo ""

# ─────────────────────────────────────────────
# 4. Guideline 5.1.1 — Privacy
# ─────────────────────────────────────────────
echo -e "${BOLD}[Guideline 5.1.1] Privacy${NC}"

PRIVACY="$PROJECT_DIR/PrivacyInfo.xcprivacy"
if [ -f "$PRIVACY" ]; then
    pass "PrivacyInfo.xcprivacy exists"

    if grep -q 'NSPrivacyAccessedAPICategoryUserDefaults' "$PRIVACY"; then
        pass "UserDefaults API declared"
    else
        fail "UserDefaults API not declared in privacy manifest"
    fi

    if grep -q 'NSPrivacyCollectedDataTypeEmailAddress' "$PRIVACY"; then
        pass "Email data type declared"
    else
        warn "Email data type not declared (required if using email verification)"
    fi

    if grep -q 'NSPrivacyCollectedDataTypePurchaseHistory' "$PRIVACY"; then
        pass "Purchase history data type declared"
    else
        warn "Purchase history not declared (required if using StoreKit)"
    fi

    # Check it's in the Xcode project build phase
    PBXPROJ=$(find "$REPO_ROOT/ios" -name "project.pbxproj" -type f 2>/dev/null | head -1)
    if [ -n "$PBXPROJ" ] && grep -q 'PrivacyInfo.xcprivacy in Resources' "$PBXPROJ"; then
        pass "PrivacyInfo.xcprivacy is in Copy Bundle Resources"
    else
        warn "Could not verify PrivacyInfo.xcprivacy is in Copy Bundle Resources build phase"
    fi
else
    fail "PrivacyInfo.xcprivacy not found"
fi

echo ""

# ─────────────────────────────────────────────
# 5. Code Quality
# ─────────────────────────────────────────────
echo -e "${BOLD}[Code Quality] General Checks${NC}"

# Check for TODO/FIXME/HACK
TODOS=$(grep -rn 'TODO\|FIXME\|HACK\|XXX' "$PROJECT_DIR" --include="*.swift" \
    | grep -v 'Tests/' \
    || true)
if [ -n "$TODOS" ]; then
    warn "TODO/FIXME/HACK comments found (review before submission):"
    echo "$TODOS" | head -5 | sed 's/^/         /'
else
    pass "No TODO/FIXME/HACK comments"
fi

# Check for test/debug/sandbox in user-facing strings
DEBUG_STRINGS=$(grep -rn '".*\(test\|debug\|sandbox\|beta\|placeholder\).*"' "$PROJECT_DIR" --include="*.swift" -i \
    | grep -v 'Tests/' \
    | grep -v '// ' \
    | grep -v 'special-tests' \
    | grep -v 'distinguishing' \
    || true)
if [ -n "$DEBUG_STRINGS" ]; then
    warn "Possible debug/test strings in user-visible code:"
    echo "$DEBUG_STRINGS" | head -5 | sed 's/^/         /'
else
    pass "No debug/test strings in user-facing code"
fi

echo ""

# ─────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────
echo -e "${BOLD}=== Summary ===${NC}"
echo -e "  ${GREEN}PASS:${NC} $PASS"
echo -e "  ${YELLOW}WARN:${NC} $WARNINGS"
echo -e "  ${RED}FAIL:${NC} $ERRORS"
echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo -e "${RED}${BOLD}BLOCKED: $ERRORS error(s) must be fixed before submission.${NC}"
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}${BOLD}READY WITH WARNINGS: Review $WARNINGS warning(s) before submission.${NC}"
    exit 0
else
    echo -e "${GREEN}${BOLD}ALL CLEAR: Ready for submission.${NC}"
    exit 0
fi
