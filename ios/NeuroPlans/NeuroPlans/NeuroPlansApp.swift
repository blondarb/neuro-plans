import SwiftUI

@main
struct NeuroPlansApp: App {
    @State private var store = PlanStore()
    @State private var builder = PlanBuilder()

    var body: some Scene {
        WindowGroup {
            MainTabView()
                .environment(store)
                .environment(builder)
                .task {
                    await store.loadPlans()
                    store.loadRecents()
                }
                .preferredColorScheme(.dark)
        }
    }
}
