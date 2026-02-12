import SwiftUI

@main
struct NeuroPlansApp: App {
    @State private var store = PlanStore()
    @State private var builder = PlanBuilder()
    @State private var referenceStore = ReferenceStore()
    @State private var stopwatchService = StopwatchService()
    @State private var userPreferences = UserPreferences()
    @State private var entitlementService = EntitlementService()
    @State private var subscriptionService = SubscriptionService()
    @State private var clinicalErrorService = ClinicalErrorService()
    @AppStorage("hasAcceptedDisclaimer") private var hasAcceptedDisclaimer = false

    var body: some Scene {
        WindowGroup {
            if hasAcceptedDisclaimer {
                MainTabView()
                    .environment(store)
                    .environment(builder)
                    .environment(referenceStore)
                    .environment(stopwatchService)
                    .environment(userPreferences)
                    .environment(entitlementService)
                    .environment(subscriptionService)
                    .environment(clinicalErrorService)
                    .task {
                        await store.loadPlans()
                        store.loadRecents()
                        await referenceStore.loadAll()
                    }
            } else {
                DisclaimerView(hasAcceptedDisclaimer: $hasAcceptedDisclaimer)
                    .environment(entitlementService)
                    .environment(subscriptionService)
            }
        }
    }
}
