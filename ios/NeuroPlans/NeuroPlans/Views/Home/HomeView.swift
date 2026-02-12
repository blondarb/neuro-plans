import SwiftUI

struct HomeView: View {
    @Environment(PlanStore.self) private var store
    @State private var searchText = ""
    @State private var showAllPlans = false

    private var greeting: String {
        let hour = Calendar.current.component(.hour, from: Date())
        switch hour {
        case 5..<12: return "Good morning"
        case 12..<17: return "Good afternoon"
        default: return "Good evening"
        }
    }

    var body: some View {
        @Bindable var store = store
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                    // Setting Picker
                    SettingPicker(selected: $store.selectedSetting)
                        .padding(.horizontal)

                    // Quick Stats
                    HStack(spacing: 12) {
                        StatCard(
                            value: "\(store.plans.count)",
                            label: "Plans",
                            icon: "doc.text.fill",
                            color: AppTheme.teal
                        )
                        StatCard(
                            value: "\(store.favorites.count)",
                            label: "Favorites",
                            icon: "star.fill",
                            color: .yellow
                        )
                        StatCard(
                            value: "\(PlanCategory.all.count)",
                            label: "Categories",
                            icon: "folder.fill",
                            color: .purple
                        )
                    }
                    .padding(.horizontal)

                    // Recents
                    if !store.recentPlans.isEmpty {
                        VStack(alignment: .leading, spacing: 10) {
                            GlassSectionHeader(title: "Recent", icon: "clock.fill")
                                .padding(.horizontal)

                            ScrollView(.horizontal, showsIndicators: false) {
                                LazyHStack(spacing: 10) {
                                    ForEach(store.recentPlans) { plan in
                                        NavigationLink(value: plan) {
                                            RecentPlanCard(plan: plan)
                                        }
                                        .buttonStyle(.plain)
                                    }
                                }
                                .padding(.horizontal)
                            }
                        }
                    }

                    // Categories Grid
                    VStack(alignment: .leading, spacing: 10) {
                        GlassSectionHeader(
                            title: "Categories",
                            icon: "square.grid.2x2.fill",
                            count: store.categories.count
                        )
                        .padding(.horizontal)

                        LazyVGrid(
                            columns: [
                                GridItem(.flexible(), spacing: 10),
                                GridItem(.flexible(), spacing: 10)
                            ],
                            spacing: 10
                        ) {
                            ForEach(store.categories) { category in
                                NavigationLink(value: category) {
                                    CategoryCard(category: category)
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.horizontal)
                    }

                    // All Plans Link
                    NavigationLink {
                        PlanListView(title: "All Plans", plans: store.allPlans)
                    } label: {
                        GlassCard {
                            HStack {
                                Image(systemName: "list.bullet")
                                    .foregroundStyle(AppTheme.teal)
                                Text("Browse All \(store.plans.count) Plans")
                                    .font(AppTheme.headlineFont)
                                Spacer()
                                Image(systemName: "chevron.right")
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                    .buttonStyle(.plain)
                    .padding(.horizontal)

                    Spacer(minLength: 40)
                }
                .padding(.top, 8)
            }
            .background(LinearGradient.appBackground.ignoresSafeArea())
            .navigationTitle(greeting)
            .searchable(text: $searchText, prompt: "Search plans, ICD codes...")
            .onChange(of: searchText) { _, newValue in
                store.searchText = newValue
            }
            .navigationDestination(for: Plan.self) { plan in
                PlanDetailView(plan: plan)
            }
            .navigationDestination(for: PlanCategory.self) { category in
                PlanListView(
                    title: category.name,
                    plans: store.plans(for: category),
                    icon: category.icon
                )
            }
            .overlay {
                if !searchText.isEmpty {
                    SearchResultsOverlay(results: store.filteredPlans)
                }
            }
        }
    }
}

// MARK: - Stat Card

private struct StatCard: View {
    let value: String
    let label: String
    let icon: String
    let color: Color

    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(spacing: 4) {
                Image(systemName: icon)
                    .font(.system(size: 18))
                    .foregroundStyle(color)
                Text(value)
                    .font(.system(.title2, design: .rounded, weight: .bold))
                Text(label)
                    .font(AppTheme.captionFont)
                    .foregroundStyle(.secondary)
            }
            .frame(maxWidth: .infinity)
        }
    }
}

// MARK: - Recent Plan Card

private struct RecentPlanCard: View {
    let plan: Plan

    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 6) {
                Text(plan.title)
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)

                if let cat = PlanCategory.category(for: plan.id) {
                    HStack(spacing: 4) {
                        Image(systemName: cat.icon)
                            .font(.system(size: 9))
                        Text(cat.name)
                            .font(.system(size: 10))
                    }
                    .foregroundStyle(cat.swiftUIColor)
                }
            }
            .frame(width: 140, alignment: .leading)
        }
    }
}

// MARK: - Search Results

private struct SearchResultsOverlay: View {
    let results: [Plan]

    var body: some View {
        List(results) { plan in
            NavigationLink(value: plan) {
                VStack(alignment: .leading, spacing: 4) {
                    Text(plan.title)
                        .font(.system(.body, design: .rounded, weight: .medium))
                    HStack(spacing: 6) {
                        if let cat = PlanCategory.category(for: plan.id) {
                            Label(cat.name, systemImage: cat.icon)
                                .font(.caption2)
                                .foregroundStyle(cat.swiftUIColor)
                        }
                        ForEach(plan.icd10.prefix(2), id: \.self) { code in
                            ICDCodeBadge(code: code)
                        }
                    }
                }
            }
        }
        .listStyle(.plain)
    }
}

#Preview {
    HomeView()
        .environment(PlanStore())
        .environment(PlanBuilder())
}
