import SwiftUI

struct PlanListView: View {
    let title: String
    let plans: [Plan]
    var icon: String? = nil

    @Environment(PlanStore.self) private var store
    @State private var searchText = ""

    private var filtered: [Plan] {
        guard !searchText.isEmpty else { return plans }
        let query = searchText.lowercased()
        return plans.filter {
            $0.title.lowercased().contains(query)
            || $0.id.lowercased().contains(query)
            || $0.icd10.contains { $0.lowercased().contains(query) }
        }
    }

    var body: some View {
        List(filtered) { plan in
            NavigationLink(value: plan) {
                PlanRow(plan: plan, setting: store.selectedSetting)
            }
            .listRowBackground(Color.clear)
        }
        .listStyle(.plain)
        .background(LinearGradient.appBackground.ignoresSafeArea())
        .navigationTitle(title)
        .navigationBarTitleDisplayMode(.large)
        .searchable(text: $searchText, prompt: "Filter plans...")
        .navigationDestination(for: Plan.self) { plan in
            PlanDetailView(plan: plan)
        }
    }
}

#Preview {
    NavigationStack {
        PlanListView(title: "Movement Disorders", plans: [])
    }
    .environment(PlanStore())
    .environment(PlanBuilder())
}
