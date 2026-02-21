import SwiftUI
import StoreKit

/// Manages user entitlements: trial, subscription, and domain whitelist
@Observable
final class EntitlementService {
    // MARK: - Entitlement State

    /// Current access level
    var accessLevel: AccessLevel = .loading

    /// Trial start date (nil if never started)
    var trialStartDate: Date? {
        get { UserDefaults.standard.object(forKey: Keys.trialStartDate) as? Date }
        set { UserDefaults.standard.set(newValue, forKey: Keys.trialStartDate) }
    }

    /// Verified whitelist email (nil if not verified)
    var verifiedEmail: String? {
        get { UserDefaults.standard.string(forKey: Keys.verifiedEmail) }
        set { UserDefaults.standard.set(newValue, forKey: Keys.verifiedEmail) }
    }

    /// Whether the paywall should be shown
    var shouldShowPaywall: Bool {
        switch accessLevel {
        case .expired:
            return true
        default:
            return false
        }
    }

    /// Whether user has full access
    var hasFullAccess: Bool {
        switch accessLevel {
        case .trial, .subscribed, .whitelisted, .errorReward:
            return true
        case .expired, .loading:
            return false
        }
    }

    // MARK: - Constants

    private enum Keys {
        static let trialStartDate = "entitlement.trialStartDate"
        static let verifiedEmail = "entitlement.verifiedEmail"
        static let cachedDomains = "entitlement.cachedDomains"
    }

    /// Trial duration in days
    static let trialDurationDays = 14

    /// Product identifier for annual subscription
    static let annualSubscriptionID = SpecialtyConfig.storeKitProductId

    // MARK: - Domain Cache

    /// Cached whitelisted domains (fetched from server)
    private var cachedDomains: [String] = []

    /// Last time domains were fetched
    private var domainsFetchedAt: Date?

    /// How long to cache domains before re-fetching (1 hour)
    private static let domainCacheDuration: TimeInterval = 3600

    // MARK: - Verification Result

    enum VerificationResult {
        case whitelistedAccessGranted
        case emailVerifiedButNotWhitelisted
        case invalidCode
        case networkError(Error)
    }

    // MARK: - Access Level

    enum AccessLevel: Equatable {
        case loading
        case trial(daysRemaining: Int)
        case subscribed(expirationDate: Date?)
        case whitelisted(email: String)
        case errorReward(expirationDate: Date)
        case expired

        var displayName: String {
            switch self {
            case .loading:
                return "Loading..."
            case .trial(let days):
                return "Trial (\(days) days left)"
            case .subscribed:
                return "Subscribed"
            case .whitelisted:
                return "Verified Member"
            case .errorReward:
                return "Error Reporter Reward"
            case .expired:
                return "Trial Expired"
            }
        }

        var icon: String {
            switch self {
            case .loading:
                return "hourglass"
            case .trial:
                return "clock.fill"
            case .subscribed:
                return "checkmark.seal.fill"
            case .whitelisted:
                return "star.fill"
            case .errorReward:
                return "gift.fill"
            case .expired:
                return "exclamationmark.triangle.fill"
            }
        }

        var color: Color {
            switch self {
            case .loading:
                return .gray
            case .trial:
                return .orange
            case .subscribed:
                return .green
            case .whitelisted:
                return .purple
            case .errorReward:
                return .yellow
            case .expired:
                return .red
            }
        }
    }

    // MARK: - Initialization

    init() {
        // Load cached domains from UserDefaults for offline use
        cachedDomains = UserDefaults.standard.stringArray(forKey: Keys.cachedDomains) ?? []

        // Listen for error reward notifications
        NotificationCenter.default.addObserver(
            forName: .clinicalErrorRewardEarned,
            object: nil,
            queue: .main
        ) { [weak self] _ in
            Task {
                await self?.refreshEntitlementStatus()
            }
        }

        Task {
            await refreshEntitlementStatus()
        }
    }

    // MARK: - Public Methods

    /// Refresh entitlement status from all sources
    @MainActor
    func refreshEntitlementStatus() async {
        // Pre-fetch domains for whitelist checks
        _ = await fetchWhitelistedDomains()

        // 1. Check for whitelisted email first
        if let email = verifiedEmail, isWhitelistedEmail(email) {
            accessLevel = .whitelisted(email: email)
            return
        }

        // 2. Check for active subscription
        if let subscriptionStatus = await checkSubscriptionStatus() {
            accessLevel = subscriptionStatus
            return
        }

        // 3. Check for error reward (free year from clinical error reporting)
        if let errorRewardStatus = checkErrorRewardStatus() {
            accessLevel = errorRewardStatus
            return
        }

        // 4. Check trial status
        accessLevel = checkTrialStatus()
    }

    /// Check if the error reporting reward is active
    private func checkErrorRewardStatus() -> AccessLevel? {
        let hasEarned = UserDefaults.standard.bool(forKey: "clinicalError.hasEarnedFreeYear")
        guard hasEarned else { return nil }

        guard let earnedDate = UserDefaults.standard.object(forKey: "clinicalError.freeYearEarnedDate") as? Date else {
            return nil
        }

        let oneYearLater = Calendar.current.date(byAdding: .year, value: 1, to: earnedDate) ?? earnedDate

        if Date() < oneYearLater {
            return .errorReward(expirationDate: oneYearLater)
        }

        return nil
    }

    /// Start the trial period
    func startTrial() {
        guard trialStartDate == nil else { return }
        trialStartDate = Date()
        Task {
            await refreshEntitlementStatus()
        }
    }

    // MARK: - OTP Email Verification

    /// Step 1: Send a 6-digit OTP code to the given email via Supabase Auth
    func sendVerificationCode(to email: String) async throws {
        try await SupabaseService.client.auth.signInWithOTP(
            email: email,
            shouldCreateUser: true
        )
    }

    /// Step 2: Verify the OTP code, then check if the email domain is whitelisted
    func verifyCode(_ code: String, for email: String) async -> VerificationResult {
        // 1. Verify OTP with Supabase
        do {
            try await SupabaseService.client.auth.verifyOTP(
                email: email,
                token: code,
                type: .email
            )
        } catch {
            return .invalidCode
        }

        // 2. Email is verified — check domain whitelist
        let trimmedEmail = email.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
        let domain = trimmedEmail.components(separatedBy: "@").last ?? ""
        let domains = await fetchWhitelistedDomains()
        let isWhitelisted = domains.contains(domain)

        // 3. Record for analytics (fire and forget)
        Task {
            try? await SupabaseService.recordVerifiedEmail(
                email: trimmedEmail,
                domain: domain,
                isWhitelisted: isWhitelisted
            )
        }

        // 4. If whitelisted, grant access
        if isWhitelisted {
            verifiedEmail = trimmedEmail
            await refreshEntitlementStatus()
            return .whitelistedAccessGranted
        } else {
            // Sign out since we don't need to keep the session for non-whitelisted users
            try? await SupabaseService.client.auth.signOut()
            return .emailVerifiedButNotWhitelisted
        }
    }

    // MARK: - Domain Whitelist

    /// Fetch whitelisted domains from Supabase, using cache if fresh
    func fetchWhitelistedDomains() async -> [String] {
        // Return cache if fresh
        if let fetchedAt = domainsFetchedAt,
           Date().timeIntervalSince(fetchedAt) < Self.domainCacheDuration,
           !cachedDomains.isEmpty {
            return cachedDomains
        }

        do {
            let domains = try await SupabaseService.fetchWhitelistedDomains(for: SpecialtyConfig.specialty)
            cachedDomains = domains
            domainsFetchedAt = Date()
            // Persist to UserDefaults for offline access
            UserDefaults.standard.set(domains, forKey: Keys.cachedDomains)
            return domains
        } catch {
            // Fall back to UserDefaults cache if network fails
            return UserDefaults.standard.stringArray(forKey: Keys.cachedDomains) ?? []
        }
    }

    /// Check if an email is in the whitelist (uses cached domains)
    func isWhitelistedEmail(_ email: String) -> Bool {
        let lowercased = email.lowercased()
        let domains = cachedDomains.isEmpty
            ? (UserDefaults.standard.stringArray(forKey: Keys.cachedDomains) ?? [])
            : cachedDomains
        return domains.contains { domain in
            lowercased.hasSuffix("@\(domain)")
        }
    }

    /// Clear verified email and sign out of Supabase
    func clearVerifiedEmail() {
        verifiedEmail = nil
        Task {
            try? await SupabaseService.client.auth.signOut()
            await refreshEntitlementStatus()
        }
    }

    // MARK: - Private Methods

    private func checkTrialStatus() -> AccessLevel {
        guard let startDate = trialStartDate else {
            // No trial started yet - start it now
            trialStartDate = Date()
            return .trial(daysRemaining: Self.trialDurationDays)
        }

        let daysSinceStart = Calendar.current.dateComponents([.day], from: startDate, to: Date()).day ?? 0
        let daysRemaining = Self.trialDurationDays - daysSinceStart

        if daysRemaining > 0 {
            return .trial(daysRemaining: daysRemaining)
        } else {
            return .expired
        }
    }

    private func checkSubscriptionStatus() async -> AccessLevel? {
        // Check for active subscription using StoreKit 2
        for await result in Transaction.currentEntitlements {
            if case .verified(let transaction) = result {
                if transaction.productID == Self.annualSubscriptionID {
                    // Check if the transaction has been revoked (refunded)
                    if transaction.revocationDate != nil {
                        continue // Skip revoked transactions
                    }
                    return .subscribed(expirationDate: transaction.expirationDate)
                }
            }
        }
        return nil
    }
}
