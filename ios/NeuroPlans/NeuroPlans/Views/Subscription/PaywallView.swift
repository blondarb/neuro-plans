import SwiftUI
import StoreKit

struct PaywallView: View {
    @Environment(EntitlementService.self) private var entitlement
    @Environment(SubscriptionService.self) private var subscription
    @Environment(\.dismiss) private var dismiss

    @State private var showEmailVerification = false
    @State private var isPurchasing = false
    @State private var showRestoreAlert = false
    @State private var restoreMessage = ""

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {
                    // Header
                    headerSection

                    // Features
                    featuresSection

                    // Pricing
                    pricingSection

                    // Team member option
                    teamMemberSection

                    // Legal
                    legalSection
                }
                .padding()
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Upgrade")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Close") {
                        dismiss()
                    }
                }

                ToolbarItem(placement: .topBarTrailing) {
                    Button("Restore Purchases") {
                        Task {
                            await restorePurchases()
                        }
                    }
                    .font(.subheadline)
                }
            }
            .sheet(isPresented: $showEmailVerification) {
                EmailVerificationView()
            }
            .alert("Restore Purchases", isPresented: $showRestoreAlert) {
                Button("OK") {}
            } message: {
                Text(restoreMessage)
            }
            .task {
                await subscription.loadProducts()
            }
        }
    }

    // MARK: - Header Section

    private var headerSection: some View {
        VStack(spacing: 16) {
            // App icon (specialty-specific)
            Image(systemName: SpecialtyConfig.headerIcon)
                .font(.system(size: 60))
                .foregroundStyle(
                    LinearGradient(
                        colors: [AppTheme.teal, .cyan],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                )

            Text("\(SpecialtyConfig.appName) Pro")
                .font(.system(.title, design: .rounded, weight: .bold))

            Text("Subscribe to access all clinical plans and tools.")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal)
        }
        .padding(.top, 20)
    }

    // MARK: - Features Section

    private var featuresSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("What's Included")
                .font(.system(.headline, design: .rounded, weight: .semibold))

            ForEach(Array(SpecialtyConfig.paywallFeatures.enumerated()), id: \.offset) { _, feature in
                FeatureRow(icon: feature.icon, title: feature.title, description: feature.description)
            }
        }
        .padding()
        .background {
            RoundedRectangle(cornerRadius: 16)
                .fill(Color.white.opacity(0.05))
        }
    }

    // MARK: - Pricing Section

    private var pricingSection: some View {
        VStack(spacing: 16) {
            if subscription.isLoading {
                ProgressView()
                    .padding()
            } else if let product = subscription.annualProduct {
                // Price card with subscription period from StoreKit
                VStack(spacing: 8) {
                    HStack(alignment: .firstTextBaseline, spacing: 4) {
                        Text(product.displayPrice)
                            .font(.system(size: 44, weight: .bold, design: .rounded))
                        Text("/\(subscription.subscriptionPeriod(for: product))")
                            .font(.title3)
                            .foregroundStyle(.secondary)
                    }

                    Text("That's less than \(monthlyEquivalent(product)) per month")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .padding(.vertical, 8)

                // Subscription disclosure (required by Apple 3.1.1)
                Text("\(product.displayPrice) per \(subscription.subscriptionPeriod(for: product)). Auto-renews until canceled.")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)

                // Subscribe button
                Button {
                    Task {
                        await purchaseSubscription(product)
                    }
                } label: {
                    HStack {
                        if isPurchasing {
                            ProgressView()
                                .tint(.white)
                        } else {
                            Text("Subscribe Now")
                        }
                    }
                    .font(.system(.headline, design: .rounded, weight: .semibold))
                    .foregroundStyle(.white)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(AppTheme.teal, in: RoundedRectangle(cornerRadius: 14))
                }
                .disabled(isPurchasing)

                if let error = subscription.errorMessage {
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.red)
                        .multilineTextAlignment(.center)
                }

                // Manage existing subscription
                if case .subscribed = entitlement.accessLevel {
                    Button {
                        if let url = URL(string: "https://apps.apple.com/account/subscriptions") {
                            UIApplication.shared.open(url)
                        }
                    } label: {
                        Text("Manage Subscription")
                            .font(.system(.caption, design: .rounded, weight: .medium))
                            .foregroundStyle(.blue)
                    }
                    .padding(.top, 4)
                }
            } else {
                // Products not available
                VStack(spacing: 8) {
                    Image(systemName: "exclamationmark.triangle")
                        .font(.title)
                        .foregroundStyle(.orange)
                    Text("Subscription not available")
                        .font(.subheadline)
                    Text("Please try again later or contact support.")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .padding()
            }
        }
        .padding()
        .background {
            RoundedRectangle(cornerRadius: 16)
                .fill(Color.white.opacity(0.05))
                .overlay {
                    RoundedRectangle(cornerRadius: 16)
                        .strokeBorder(AppTheme.teal.opacity(0.3), lineWidth: 1)
                }
        }
    }

    // MARK: - Team Member Section

    private var teamMemberSection: some View {
        VStack(spacing: 12) {
            HStack {
                Image(systemName: "building.2.fill")
                    .foregroundStyle(.purple)
                Text("Verify Your Email")
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
            }

            Text("Some organizations provide complimentary access.")
                .font(.caption)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)

            Button {
                showEmailVerification = true
            } label: {
                Text("Check Eligibility")
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .foregroundStyle(.purple)
                    .padding(.horizontal, 20)
                    .padding(.vertical, 10)
                    .background(.purple.opacity(0.15), in: Capsule())
            }
        }
        .padding()
        .background {
            RoundedRectangle(cornerRadius: 16)
                .fill(Color.white.opacity(0.05))
        }
    }

    // MARK: - Legal Section

    private var legalSection: some View {
        VStack(spacing: 8) {
            if let product = subscription.annualProduct {
                Text("Payment of \(product.displayPrice) will be charged to your Apple ID account at confirmation of purchase. Subscription automatically renews at \(product.displayPrice)/\(subscription.subscriptionPeriod(for: product)) unless canceled at least 24 hours before the end of the current period. You can manage or cancel your subscription in your device's Settings > Apple ID > Subscriptions.")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
                    .multilineTextAlignment(.center)
            } else {
                Text("Payment will be charged to your Apple ID account at confirmation of purchase. Subscription automatically renews unless canceled at least 24 hours before the end of the current period. You can manage or cancel your subscription in your device's Settings > Apple ID > Subscriptions.")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
                    .multilineTextAlignment(.center)
            }

            HStack(spacing: 16) {
                if let termsURL = URL(string: SpecialtyConfig.termsURL) {
                    Link("Terms of Service", destination: termsURL)
                }
                if let privacyURL = URL(string: SpecialtyConfig.privacyURL) {
                    Link("Privacy Policy", destination: privacyURL)
                }
            }
            .font(.caption2)
            .foregroundStyle(.secondary)
        }
        .padding(.horizontal)
        .padding(.top, 8)
    }

    // MARK: - Helper Methods

    private func monthlyEquivalent(_ product: Product) -> String {
        let yearly = product.price
        let monthly = yearly / 12
        return monthly.formatted(.currency(code: product.priceFormatStyle.currencyCode ?? "USD"))
    }

    private func purchaseSubscription(_ product: Product) async {
        isPurchasing = true
        let success = await subscription.purchase(product)
        isPurchasing = false

        if success {
            await entitlement.refreshEntitlementStatus()
            dismiss()
        }
    }

    private func restorePurchases() async {
        let success = await subscription.restorePurchases()

        if success {
            await entitlement.refreshEntitlementStatus()

            if entitlement.hasFullAccess {
                restoreMessage = "Your subscription has been restored!"
                showRestoreAlert = true

                // Dismiss after a short delay
                try? await Task.sleep(nanoseconds: 1_500_000_000)
                dismiss()
            } else {
                restoreMessage = "No active subscription found. If you believe this is an error, please contact support."
                showRestoreAlert = true
            }
        } else {
            restoreMessage = subscription.errorMessage ?? "Failed to restore purchases."
            showRestoreAlert = true
        }
    }
}

// MARK: - Feature Row

private struct FeatureRow: View {
    let icon: String
    let title: String
    let description: String

    var body: some View {
        HStack(alignment: .top, spacing: 12) {
            Image(systemName: icon)
                .font(.system(size: 16))
                .foregroundStyle(AppTheme.teal)
                .frame(width: 24)

            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                Text(description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }

            Spacer()
        }
    }
}

#Preview {
    PaywallView()
        .environment(EntitlementService())
        .environment(SubscriptionService())
}
