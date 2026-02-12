import SwiftUI
import StoreKit

/// Manages StoreKit 2 subscriptions
@Observable
final class SubscriptionService {
    // MARK: - Properties
    
    /// Available products
    var products: [Product] = []
    
    /// Current purchase state
    var purchaseState: PurchaseState = .idle
    
    /// Error message if any
    var errorMessage: String?
    
    /// Whether products are loading
    var isLoading = false
    
    // MARK: - Purchase State
    
    enum PurchaseState {
        case idle
        case purchasing
        case purchased
        case failed(Error)
        case cancelled
    }
    
    // MARK: - Product IDs
    
    private let productIDs = [
        EntitlementService.annualSubscriptionID
    ]
    
    // MARK: - Initialization
    
    init() {
        // Start listening for transaction updates
        Task {
            await listenForTransactions()
        }
    }
    
    // MARK: - Public Methods
    
    /// Load available products from App Store
    @MainActor
    func loadProducts() async {
        isLoading = true
        errorMessage = nil
        
        do {
            products = try await Product.products(for: productIDs)
            isLoading = false
        } catch {
            errorMessage = "Failed to load products: \(error.localizedDescription)"
            isLoading = false
        }
    }
    
    /// Purchase a product
    @MainActor
    func purchase(_ product: Product) async -> Bool {
        purchaseState = .purchasing
        errorMessage = nil
        
        do {
            let result = try await product.purchase()
            
            switch result {
            case .success(let verification):
                // Check if transaction is verified
                switch verification {
                case .verified(let transaction):
                    // Transaction is valid
                    await transaction.finish()
                    purchaseState = .purchased
                    return true
                    
                case .unverified(_, let error):
                    // Transaction failed verification
                    errorMessage = "Purchase verification failed: \(error.localizedDescription)"
                    purchaseState = .failed(error)
                    return false
                }
                
            case .userCancelled:
                purchaseState = .cancelled
                return false
                
            case .pending:
                // Transaction is pending (e.g., Ask to Buy)
                errorMessage = "Purchase is pending approval"
                purchaseState = .idle
                return false
                
            @unknown default:
                purchaseState = .idle
                return false
            }
        } catch {
            errorMessage = "Purchase failed: \(error.localizedDescription)"
            purchaseState = .failed(error)
            return false
        }
    }
    
    /// Restore previous purchases
    @MainActor
    func restorePurchases() async -> Bool {
        do {
            try await AppStore.sync()
            return true
        } catch {
            errorMessage = "Failed to restore purchases: \(error.localizedDescription)"
            return false
        }
    }
    
    /// Get the annual subscription product
    var annualProduct: Product? {
        products.first { $0.id == EntitlementService.annualSubscriptionID }
    }
    
    /// Format price for display
    func formattedPrice(for product: Product) -> String {
        product.displayPrice
    }
    
    /// Format subscription period
    func subscriptionPeriod(for product: Product) -> String {
        guard let subscription = product.subscription else { return "" }
        
        let unit = subscription.subscriptionPeriod.unit
        let value = subscription.subscriptionPeriod.value
        
        switch unit {
        case .day:
            return value == 1 ? "day" : "\(value) days"
        case .week:
            return value == 1 ? "week" : "\(value) weeks"
        case .month:
            return value == 1 ? "month" : "\(value) months"
        case .year:
            return value == 1 ? "year" : "\(value) years"
        @unknown default:
            return ""
        }
    }
    
    // MARK: - Private Methods
    
    /// Listen for transaction updates (renewals, refunds, etc.)
    private func listenForTransactions() async {
        for await result in Transaction.updates {
            if case .verified(let transaction) = result {
                await transaction.finish()
                
                // Notify that entitlements may have changed
                await MainActor.run {
                    NotificationCenter.default.post(
                        name: .entitlementDidChange,
                        object: nil
                    )
                }
            }
        }
    }
}

// MARK: - Notification Names

extension Notification.Name {
    static let entitlementDidChange = Notification.Name("entitlementDidChange")
}
