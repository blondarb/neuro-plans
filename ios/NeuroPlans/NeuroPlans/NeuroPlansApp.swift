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
                    .alert("Data Loading Error",
                           isPresented: .constant(store.loadingError != nil || referenceStore.loadingError != nil)) {
                        Button("Retry") {
                            let planError = store.loadingError != nil
                            let refError = referenceStore.loadingError != nil
                            store.loadingError = nil
                            referenceStore.loadingError = nil
                            if planError { store.isLoaded = false }
                            if refError { referenceStore.isLoaded = false }
                            Task {
                                if planError {
                                    await store.loadPlans()
                                    store.loadRecents()
                                }
                                if refError {
                                    await referenceStore.loadAll()
                                }
                            }
                        }
                        Button("Continue Anyway", role: .cancel) {
                            store.loadingError = nil
                            referenceStore.loadingError = nil
                        }
                    } message: {
                        Text(store.loadingError ?? referenceStore.loadingError ?? "An error occurred loading clinical data.")
                    }
            } else {
                DisclaimerView(hasAcceptedDisclaimer: $hasAcceptedDisclaimer)
                    .environment(entitlementService)
                    .environment(subscriptionService)
            }
        }
    }
}
