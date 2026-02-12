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
    }
    
    /// Trial duration in days
    static let trialDurationDays = 14
    
    /// Whitelisted email domains (free access)
    static let whitelistedDomains = ["sevaro.com"]
    
    /// Product identifier for annual subscription
    static let annualSubscriptionID = "com.neuroplans.annual"
    
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
                return "Team Member"
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
        // Check UserDefaults for error reward (stored by ClinicalErrorService)
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
    
    /// Verify and save a whitelisted email
    func verifyEmail(_ email: String) -> Bool {
        let trimmedEmail = email.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
        
        if isWhitelistedEmail(trimmedEmail) {
            verifiedEmail = trimmedEmail
            Task {
                await refreshEntitlementStatus()
            }
            return true
        }
        return false
    }
    
    /// Clear verified email (for testing or logout)
    func clearVerifiedEmail() {
        verifiedEmail = nil
        Task {
            await refreshEntitlementStatus()
        }
    }
    
    /// Check if an email is in the whitelist
    func isWhitelistedEmail(_ email: String) -> Bool {
        let lowercased = email.lowercased()
        return Self.whitelistedDomains.contains { domain in
            lowercased.hasSuffix("@\(domain)")
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
        do {
            // Check for active subscription using StoreKit 2
            for await result in Transaction.currentEntitlements {
                if case .verified(let transaction) = result {
                    if transaction.productID == Self.annualSubscriptionID {
                        return .subscribed(expirationDate: transaction.expirationDate)
                    }
                }
            }
        }
        return nil
    }
}
