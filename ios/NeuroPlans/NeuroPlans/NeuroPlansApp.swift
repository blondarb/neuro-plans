import SwiftUI

@main
struct NeuroPlansApp: App {
    @State private var store = PlanStore()
    @State private var builder = PlanBuilder()
    @State private var referenceStore = ReferenceStore()
    @AppStorage("hasAcceptedDisclaimer") private var hasAcceptedDisclaimer = false

    var body: some Scene {
        WindowGroup {
            if hasAcceptedDisclaimer {
                MainTabView()
                    .environment(store)
                    .environment(builder)
                    .environment(referenceStore)
                    .task {
                        await store.loadPlans()
                        store.loadRecents()
                        await referenceStore.loadAll()
                    }
                    .preferredColorScheme(.dark)
            } else {
                DisclaimerView(hasAcceptedDisclaimer: $hasAcceptedDisclaimer)
                    .preferredColorScheme(.dark)
            }
        }
    }
}
