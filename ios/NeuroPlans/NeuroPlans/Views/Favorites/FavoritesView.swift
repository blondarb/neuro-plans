import SwiftUI

struct FavoritesView: View {
    @Environment(PlanStore.self) private var store

    var body: some View {
        NavigationStack {
            Group {
                if store.favoritePlans.isEmpty {
                    emptyState
                } else {
                    List(store.favoritePlans) { plan in
                        NavigationLink(value: plan) {
                            PlanRow(plan: plan, setting: store.selectedSetting)
                        }
                        .listRowBackground(Color.clear)
                        .swipeActions(edge: .trailing) {
                            Button(role: .destructive) {
                                withAnimation { store.toggleFavorite(plan.id) }
                            } label: {
                                Label("Unfavorite", systemImage: "star.slash")
                            }
                        }
                    }
                    .listStyle(.plain)
                }
            }
            .scrollContentBackground(.hidden)
            .background { AdaptiveBackground() }
            .navigationTitle("Favorites")
            .navigationDestination(for: Plan.self) { plan in
                PlanDetailView(plan: plan)
            }
        }
    }

    private var emptyState: some View {
        VStack(spacing: 16) {
            Spacer()
            Image(systemName: "star")
                .font(.system(size: 48))
                .foregroundStyle(.tertiary)
            Text("No Favorites Yet")
                .font(AppTheme.titleFont)
                .foregroundStyle(.secondary)
            Text("Tap the star on any plan to save it here for quick access")
                .font(AppTheme.bodyFont)
                .foregroundStyle(.tertiary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 40)
            Spacer()
        }
    }
}

#Preview {
    FavoritesView()
        .environment(PlanStore())
        .environment(PlanBuilder())
}
