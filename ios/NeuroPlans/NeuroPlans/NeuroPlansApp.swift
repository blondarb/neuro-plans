import SwiftUI

@main
struct NeuroPlansApp: App {
    @State private var store = PlanStore()
    @State private var builder = PlanBuilder()
    @State private var referenceStore = ReferenceStore()

    var body: some Scene {
        WindowGroup {
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
        }
    }
}
