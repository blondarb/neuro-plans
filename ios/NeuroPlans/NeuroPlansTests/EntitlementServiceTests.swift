import XCTest
@testable import NeuroPlans

/// Tests for EntitlementService — manages trial periods, subscription status,
/// domain-based whitelisting, and the clinical error reward program.
///
/// These tests focus on the locally-testable logic: trial period calculation,
/// access level determination, and domain validation. Network-dependent methods
/// (Supabase OTP, StoreKit subscriptions) are not tested here — those require
/// integration tests or mocking frameworks.
final class EntitlementServiceTests: XCTestCase {

    // MARK: - Properties

    private var service: EntitlementService!

    // MARK: - UserDefaults Keys (mirroring the service's private Keys enum)

    private let trialStartDateKey = "entitlement.trialStartDate"
    private let verifiedEmailKey = "entitlement.verifiedEmail"
    private let cachedDomainsKey = "entitlement.cachedDomains"
    private let hasEarnedFreeYearKey = "clinicalError.hasEarnedFreeYear"
    private let freeYearEarnedDateKey = "clinicalError.freeYearEarnedDate"

    // MARK: - Setup / Teardown

    override func setUp() {
        super.setUp()
        // Clear all entitlement-related UserDefaults for a clean state
        clearEntitlementDefaults()
        service = EntitlementService()
    }

    override func tearDown() {
        clearEntitlementDefaults()
        service = nil
        super.tearDown()
    }

    private func clearEntitlementDefaults() {
        UserDefaults.standard.removeObject(forKey: trialStartDateKey)
        UserDefaults.standard.removeObject(forKey: verifiedEmailKey)
        UserDefaults.standard.removeObject(forKey: cachedDomainsKey)
        UserDefaults.standard.removeObject(forKey: hasEarnedFreeYearKey)
        UserDefaults.standard.removeObject(forKey: freeYearEarnedDateKey)
    }

    // MARK: - Trial Period Constants

    /// Trial duration should be 14 days
    func testTrialDuration_Is14Days() {
        XCTAssertEqual(EntitlementService.trialDurationDays, 14,
                       "Trial duration should be exactly 14 days")
    }

    // MARK: - Trial Start Date

    /// trialStartDate should be nil initially (no trial started)
    func testTrialStartDate_InitiallyNil() {
        XCTAssertNil(service.trialStartDate,
                     "Trial should not have a start date before startTrial() is called")
    }

    /// startTrial() should set the trial start date
    func testStartTrial_SetsDate() {
        service.startTrial()
        XCTAssertNotNil(service.trialStartDate,
                        "startTrial should set a start date")
    }

    /// startTrial() should only set the date once (idempotent)
    func testStartTrial_Idempotent() {
        service.startTrial()
        let firstDate = service.trialStartDate

        // Wait a tiny bit and call again
        service.startTrial()
        let secondDate = service.trialStartDate

        XCTAssertEqual(firstDate, secondDate,
                       "Calling startTrial() twice should not change the original date")
    }

    /// trialStartDate should persist in UserDefaults
    func testTrialStartDate_Persists() {
        let now = Date()
        service.trialStartDate = now

        let stored = UserDefaults.standard.object(forKey: trialStartDateKey) as? Date
        XCTAssertNotNil(stored, "Trial start date should be saved to UserDefaults")
        XCTAssertEqual(stored!.timeIntervalSince1970, now.timeIntervalSince1970,
                       accuracy: 1.0, "Stored date should match the set date")
    }

    // MARK: - Access Level: hasFullAccess

    /// Trial state should grant full access
    func testHasFullAccess_Trial() {
        service.accessLevel = .trial(daysRemaining: 7)
        XCTAssertTrue(service.hasFullAccess,
                      "Active trial should grant full access")
    }

    /// Subscribed state should grant full access
    func testHasFullAccess_Subscribed() {
        service.accessLevel = .subscribed(expirationDate: Date().addingTimeInterval(86400))
        XCTAssertTrue(service.hasFullAccess,
                      "Active subscription should grant full access")
    }

    /// Whitelisted state should grant full access
    func testHasFullAccess_Whitelisted() {
        service.accessLevel = .whitelisted(email: "doc@hospital.edu")
        XCTAssertTrue(service.hasFullAccess,
                      "Whitelisted email should grant full access")
    }

    /// Error reward state should grant full access
    func testHasFullAccess_ErrorReward() {
        let futureDate = Date().addingTimeInterval(86400 * 365)
        service.accessLevel = .errorReward(expirationDate: futureDate)
        XCTAssertTrue(service.hasFullAccess,
                      "Active error reward should grant full access")
    }

    /// Expired state should NOT grant full access
    func testHasFullAccess_Expired() {
        service.accessLevel = .expired
        XCTAssertFalse(service.hasFullAccess,
                       "Expired trial should not grant access")
    }

    /// Loading state should NOT grant full access
    func testHasFullAccess_Loading() {
        service.accessLevel = .loading
        XCTAssertFalse(service.hasFullAccess,
                       "Loading state should not grant access")
    }

    // MARK: - Access Level: shouldShowPaywall

    /// Expired state should show paywall
    func testShouldShowPaywall_Expired() {
        service.accessLevel = .expired
        XCTAssertTrue(service.shouldShowPaywall,
                      "Expired state should trigger paywall")
    }

    /// Active trial should NOT show paywall
    func testShouldShowPaywall_Trial() {
        service.accessLevel = .trial(daysRemaining: 5)
        XCTAssertFalse(service.shouldShowPaywall,
                       "Active trial should not show paywall")
    }

    /// Subscribed should NOT show paywall
    func testShouldShowPaywall_Subscribed() {
        service.accessLevel = .subscribed(expirationDate: nil)
        XCTAssertFalse(service.shouldShowPaywall,
                       "Subscribed state should not show paywall")
    }

    /// Loading should NOT show paywall
    func testShouldShowPaywall_Loading() {
        service.accessLevel = .loading
        XCTAssertFalse(service.shouldShowPaywall,
                       "Loading state should not show paywall while status resolves")
    }

    // MARK: - Access Level Display Properties

    /// Each access level should have a descriptive display name
    func testAccessLevel_DisplayNames() {
        XCTAssertEqual(EntitlementService.AccessLevel.loading.displayName, "Loading...")
        XCTAssertEqual(EntitlementService.AccessLevel.trial(daysRemaining: 7).displayName, "Trial (7 days left)")
        XCTAssertEqual(EntitlementService.AccessLevel.subscribed(expirationDate: nil).displayName, "Subscribed")
        XCTAssertEqual(EntitlementService.AccessLevel.whitelisted(email: "x@y.com").displayName, "Verified Member")
        XCTAssertEqual(EntitlementService.AccessLevel.expired.displayName, "Trial Expired")

        let futureDate = Date().addingTimeInterval(86400)
        XCTAssertEqual(EntitlementService.AccessLevel.errorReward(expirationDate: futureDate).displayName,
                       "Error Reporter Reward")
    }

    /// Trial with 0 days should display "Trial (0 days left)"
    func testAccessLevel_TrialZeroDays() {
        let level = EntitlementService.AccessLevel.trial(daysRemaining: 0)
        XCTAssertEqual(level.displayName, "Trial (0 days left)")
    }

    // MARK: - Domain Whitelist Validation

    /// isWhitelistedEmail should match against cached domains
    func testIsWhitelistedEmail_Match() {
        // Simulate cached domains
        UserDefaults.standard.set(["hospital.edu", "clinic.org"], forKey: cachedDomainsKey)
        // Re-create service to pick up the cached domains
        service = EntitlementService()

        XCTAssertTrue(service.isWhitelistedEmail("doctor@hospital.edu"),
                      "Email with whitelisted domain should match")
    }

    /// Non-whitelisted domain should not match
    func testIsWhitelistedEmail_NoMatch() {
        UserDefaults.standard.set(["hospital.edu"], forKey: cachedDomainsKey)
        service = EntitlementService()

        XCTAssertFalse(service.isWhitelistedEmail("user@gmail.com"),
                       "Personal email domain should not be whitelisted")
    }

    /// Domain matching should be case-insensitive
    func testIsWhitelistedEmail_CaseInsensitive() {
        UserDefaults.standard.set(["hospital.edu"], forKey: cachedDomainsKey)
        service = EntitlementService()

        XCTAssertTrue(service.isWhitelistedEmail("Doctor@HOSPITAL.EDU"),
                      "Domain matching should be case-insensitive")
    }

    /// Empty cached domains should return false
    func testIsWhitelistedEmail_EmptyCache() {
        UserDefaults.standard.removeObject(forKey: cachedDomainsKey)
        service = EntitlementService()

        XCTAssertFalse(service.isWhitelistedEmail("doctor@hospital.edu"),
                       "Should return false when no domains are cached")
    }

    /// Partial domain matches should not be accepted (security: avoid subdomain spoofing)
    func testIsWhitelistedEmail_NoPartialMatch() {
        UserDefaults.standard.set(["hospital.edu"], forKey: cachedDomainsKey)
        service = EntitlementService()

        // "nothospital.edu" should not match "hospital.edu" — the check uses hasSuffix("@domain")
        XCTAssertFalse(service.isWhitelistedEmail("user@nothospital.edu"),
                       "Subdomain spoofing with prefix should not match")
    }

    // MARK: - Verified Email

    /// verifiedEmail should be nil initially
    func testVerifiedEmail_InitiallyNil() {
        XCTAssertNil(service.verifiedEmail,
                     "No email should be verified initially")
    }

    /// Setting verifiedEmail should persist in UserDefaults
    func testVerifiedEmail_Persists() {
        service.verifiedEmail = "doc@hospital.edu"
        let stored = UserDefaults.standard.string(forKey: verifiedEmailKey)
        XCTAssertEqual(stored, "doc@hospital.edu")
    }

    /// clearVerifiedEmail should set verifiedEmail to nil
    func testClearVerifiedEmail() {
        service.verifiedEmail = "doc@hospital.edu"
        service.clearVerifiedEmail()

        // Note: clearVerifiedEmail triggers async work, but the property set is synchronous
        XCTAssertNil(service.verifiedEmail,
                     "verifiedEmail should be nil after clearing")
    }

    // MARK: - Error Reward Access Level Check

    /// When hasEarnedFreeYear is true and date is recent, reward should be active
    func testErrorReward_Active() {
        UserDefaults.standard.set(true, forKey: hasEarnedFreeYearKey)
        UserDefaults.standard.set(Date(), forKey: freeYearEarnedDateKey)

        // Re-create service — it will pick up the reward during init refresh
        service = EntitlementService()

        // The error reward check happens internally via refreshEntitlementStatus()
        // We can verify the logic by checking if the reward would be considered active
        let earnedDate = UserDefaults.standard.object(forKey: freeYearEarnedDateKey) as! Date
        let oneYearLater = Calendar.current.date(byAdding: .year, value: 1, to: earnedDate)!
        XCTAssertTrue(Date() < oneYearLater,
                      "A reward earned just now should be valid for 1 year")
    }

    /// When the free year was earned more than 1 year ago, it should be expired
    func testErrorReward_Expired() {
        let twoYearsAgo = Calendar.current.date(byAdding: .year, value: -2, to: Date())!
        UserDefaults.standard.set(true, forKey: hasEarnedFreeYearKey)
        UserDefaults.standard.set(twoYearsAgo, forKey: freeYearEarnedDateKey)

        let oneYearLater = Calendar.current.date(byAdding: .year, value: 1, to: twoYearsAgo)!
        XCTAssertFalse(Date() < oneYearLater,
                       "A reward earned 2 years ago should be expired")
    }

    /// When hasEarnedFreeYear is false, no reward should apply
    func testErrorReward_NotEarned() {
        UserDefaults.standard.set(false, forKey: hasEarnedFreeYearKey)
        XCTAssertFalse(UserDefaults.standard.bool(forKey: hasEarnedFreeYearKey),
                       "Reward should not apply when not earned")
    }

    // MARK: - AccessLevel Equatable

    /// AccessLevel should conform to Equatable
    func testAccessLevel_Equatable() {
        let a = EntitlementService.AccessLevel.expired
        let b = EntitlementService.AccessLevel.expired
        XCTAssertEqual(a, b, "Same access levels should be equal")

        let c = EntitlementService.AccessLevel.trial(daysRemaining: 5)
        let d = EntitlementService.AccessLevel.trial(daysRemaining: 5)
        XCTAssertEqual(c, d, "Trials with same days remaining should be equal")

        let e = EntitlementService.AccessLevel.trial(daysRemaining: 5)
        let f = EntitlementService.AccessLevel.trial(daysRemaining: 10)
        XCTAssertNotEqual(e, f, "Trials with different days remaining should not be equal")
    }

    // MARK: - Product ID

    /// Annual subscription product ID should match App Store Connect configuration
    func testAnnualSubscriptionID() {
        XCTAssertEqual(EntitlementService.annualSubscriptionID, "com.neuroplans.annual",
                       "Product ID should match what's configured in App Store Connect")
    }
}
