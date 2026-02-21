import SwiftUI

struct HomeView: View {
    @Environment(PlanStore.self) private var store
    @Environment(ReferenceStore.self) private var referenceStore
    @Environment(UserPreferences.self) private var prefs
    @State private var searchText = ""
    @State private var showWhatsNew = false

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
            Group {
                if !store.isLoaded {
                    // Loading state for cold start
                    VStack(spacing: 16) {
                        Spacer()
                        ProgressView()
                            .scaleEffect(1.2)
                        Text("Loading clinical plans...")
                            .font(.system(.subheadline, design: .rounded))
                            .foregroundStyle(.secondary)
                        Spacer()
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                } else {
                    ScrollView {
                        VStack(alignment: .leading, spacing: 16) {

                            // What's New banner
                            if store.hasUnseenChanges {
                                Button {
                                    showWhatsNew = true
                                } label: {
                                    HStack {
                                        Image(systemName: "sparkles")
                                            .foregroundStyle(.yellow)
                                        Text("New plans added — see what's new")
                                            .font(.system(.subheadline, design: .rounded, weight: .medium))
                                        Spacer()
                                        Image(systemName: "chevron.right")
                                            .font(.caption)
                                            .foregroundStyle(.tertiary)
                                    }
                                    .padding(.horizontal, 16)
                                    .padding(.vertical, 12)
                                    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                                }
                                .buttonStyle(.plain)
                                .padding(.horizontal)
                            }

                            // Setting Picker
                            SettingPicker(selected: $store.selectedSetting)
                                .padding(.horizontal)

                            // Quick Actions
                            if !SpecialtyConfig.quickActions.isEmpty {
                                QuickActionsBar(store: store)
                                    .padding(.horizontal)
                            }

                            // Render sections in user's preferred order
                            ForEach(prefs.plansSectionOrder, id: \.self) { sectionId in
                                switch sectionId {
                                case "recents":
                                    if !store.recentPlans.isEmpty {
                                        RecentPlansHeroCard(plans: store.recentPlans)
                                            .padding(.horizontal)
                                    }
                                case "favorites":
                                    if !store.favorites.isEmpty {
                                        FavoritesPlanSection(
                                            sectionId: "favorites",
                                            plans: store.favoritePlans
                                        )
                                    }
                                case "categories":
                                    CategoriesPlanSection(
                                        sectionId: "categories",
                                        categories: store.categories,
                                        totalPlans: store.plans.count
                                    )
                                default:
                                    EmptyView()
                                }
                            }

                            Spacer(minLength: 40)
                        }
                        .padding(.top, 8)
                    }
                }
            }
            .background { AdaptiveBackground() }
            .navigationTitle(greeting)
            .searchable(text: $searchText, prompt: "Search plans, scales, exams, tools...")
            .onChange(of: searchText) { _, newValue in
                store.searchText = newValue
                referenceStore.searchText = newValue
            }
            .navigationDestination(for: String.self) { value in
                switch value {
                case "allPlans":
                    PlanListView(title: "All Plans", plans: store.allPlans)
                case "allFavorites":
                    PlanListView(title: "Favorites", plans: store.favoritePlans, icon: "star.fill")
                default:
                    EmptyView()
                }
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
            .navigationDestination(for: ClinicalScale.self) { scale in
                ScaleDetailView(scale: scale)
            }
            .navigationDestination(for: NeurologyExam.self) { exam in
                ExamDetailView(exam: exam)
            }
            .navigationDestination(for: NeurologyTool.self) { tool in
                ToolDetailView(tool: tool)
            }
            .overlay {
                if !searchText.isEmpty {
                    GlobalSearchOverlay(
                        searchText: searchText,
                        plans: store.filteredPlans,
                        scales: referenceStore.filteredScales,
                        exams: referenceStore.filteredExams,
                        tools: referenceStore.filteredTools
                    )
                }
            }
            .sheet(isPresented: $showWhatsNew) {
                WhatsNewView()
                    .environment(store)
            }
        }
    }
}

// MARK: - Recent Plans Hero Card

private struct RecentPlansHeroCard: View {
    @Environment(\.colorScheme) var colorScheme
    let plans: [Plan]
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text("Recent Plans")
                        .font(.system(.title3, design: .rounded, weight: .bold))
                    Text("Continue where you left off")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                Spacer()
            }
            
            // Recent plans row
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 12) {
                    ForEach(plans.prefix(5)) { plan in
                        NavigationLink(value: plan) {
                            RecentPlanChip(plan: plan)
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
        }
        .padding(16)
        .background {
            if colorScheme == .dark {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(.ultraThinMaterial)
            } else {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(Color(.systemBackground))
                    .shadow(color: Color.black.opacity(0.06), radius: 8, x: 0, y: 2)
            }
        }
        .overlay {
            RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                .strokeBorder(
                    colorScheme == .dark ? Color.white.opacity(0.08) : Color.black.opacity(0.04),
                    lineWidth: 0.5
                )
        }
    }
}

private struct RecentPlanChip: View {
    @Environment(\.colorScheme) var colorScheme
    let plan: Plan
    
    private var category: PlanCategory? {
        PlanCategory.category(for: plan.id)
    }
    
    var body: some View {
        VStack(spacing: 6) {
            ZStack {
                Circle()
                    .fill((category?.swiftUIColor ?? AppTheme.teal).opacity(0.15))
                    .frame(width: 44, height: 44)
                Image(systemName: category?.icon ?? "doc.text.fill")
                    .font(.system(size: 18))
                    .foregroundStyle(category?.swiftUIColor ?? AppTheme.teal)
            }
            Text(plan.title)
                .font(.system(size: 10, weight: .medium))
                .foregroundStyle(.primary)
                .lineLimit(2)
                .multilineTextAlignment(.center)
                .frame(width: 64)
        }
    }
}

// MARK: - Favorites Plan Section

private struct FavoritesPlanSection: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(UserPreferences.self) private var prefs
    let sectionId: String
    let plans: [Plan]
    
    private var isExpanded: Bool {
        prefs.isExpanded(sectionId, in: .plans)
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Section Header
            Button {
                withAnimation(.snappy(duration: 0.25)) {
                    prefs.toggleExpanded(sectionId, in: .plans)
                }
            } label: {
                HStack(spacing: 10) {
                    ZStack {
                        Circle()
                            .fill(Color.yellow.opacity(0.15))
                            .frame(width: 32, height: 32)
                        Image(systemName: "star.fill")
                            .font(.system(size: 14, weight: .semibold))
                            .foregroundStyle(.yellow)
                    }
                    
                    Text("Favorites")
                        .font(.system(.headline, design: .rounded, weight: .semibold))
                    
                    Spacer()
                    
                    Text("\(plans.count)")
                        .font(.system(.caption, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(.quaternary, in: Capsule())
                    
                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.system(size: 12, weight: .semibold))
                        .foregroundStyle(.secondary)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
            }
            .buttonStyle(.plain)
            
            if isExpanded {
                VStack(spacing: 1) {
                    ForEach(plans.prefix(5)) { plan in
                        NavigationLink(value: plan) {
                            PlanSectionRow(
                                name: plan.title,
                                icon: PlanCategory.category(for: plan.id)?.icon ?? "doc.text.fill",
                                color: PlanCategory.category(for: plan.id)?.swiftUIColor ?? AppTheme.teal,
                                count: nil
                            )
                        }
                        .buttonStyle(.plain)
                    }
                    
                    // Browse All row (if more than 5)
                    if plans.count > 5 {
                        NavigationLink(value: "allFavorites") {
                            HStack(spacing: 12) {
                                ZStack {
                                    Circle()
                                        .fill(Color.yellow.opacity(0.1))
                                        .frame(width: 36, height: 36)
                                    Image(systemName: "list.bullet")
                                        .font(.system(size: 14))
                                        .foregroundStyle(.yellow)
                                }
                                
                                Text("Browse All \(plans.count)")
                                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                                    .foregroundStyle(.yellow)
                                
                                Spacer()
                                
                                Image(systemName: "chevron.right")
                                    .font(.system(size: 12))
                                    .foregroundStyle(.tertiary)
                            }
                            .padding(.horizontal, 16)
                            .padding(.vertical, 10)
                            .background(colorScheme == .dark ? Color.white.opacity(0.02) : Color.black.opacity(0.01))
                        }
                        .buttonStyle(.plain)
                    }
                }
                .clipShape(RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal, 16)
                .padding(.bottom, 8)
                .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .background {
            if colorScheme == .dark {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(.ultraThinMaterial)
            } else {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(Color(.systemBackground))
                    .shadow(color: Color.black.opacity(0.04), radius: 6, x: 0, y: 2)
            }
        }
        .overlay {
            RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                .strokeBorder(
                    colorScheme == .dark ? Color.white.opacity(0.06) : Color.black.opacity(0.03),
                    lineWidth: 0.5
                )
        }
        .padding(.horizontal)
    }
}

// MARK: - Categories Plan Section

private struct CategoriesPlanSection: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(UserPreferences.self) private var prefs
    let sectionId: String
    let categories: [PlanCategory]
    let totalPlans: Int
    
    private var isExpanded: Bool {
        prefs.isExpanded(sectionId, in: .plans)
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Section Header
            Button {
                withAnimation(.snappy(duration: 0.25)) {
                    prefs.toggleExpanded(sectionId, in: .plans)
                }
            } label: {
                HStack(spacing: 10) {
                    ZStack {
                        Circle()
                            .fill(Color.purple.opacity(0.15))
                            .frame(width: 32, height: 32)
                        Image(systemName: "folder.fill")
                            .font(.system(size: 14, weight: .semibold))
                            .foregroundStyle(.purple)
                    }
                    
                    Text("Categories")
                        .font(.system(.headline, design: .rounded, weight: .semibold))
                    
                    Spacer()
                    
                    Text("\(totalPlans)")
                        .font(.system(.caption, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(.quaternary, in: Capsule())
                    
                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.system(size: 12, weight: .semibold))
                        .foregroundStyle(.secondary)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
            }
            .buttonStyle(.plain)
            
            if isExpanded {
                VStack(spacing: 1) {
                    ForEach(categories) { category in
                        NavigationLink(value: category) {
                            PlanSectionRow(
                                name: category.name,
                                icon: category.icon,
                                color: category.swiftUIColor,
                                count: category.planIds.count
                            )
                        }
                        .buttonStyle(.plain)
                    }
                    
                    // Browse All row
                    NavigationLink(value: "allPlans") {
                        HStack(spacing: 12) {
                            ZStack {
                                Circle()
                                    .fill(Color.purple.opacity(0.1))
                                    .frame(width: 36, height: 36)
                                Image(systemName: "list.bullet")
                                    .font(.system(size: 14))
                                    .foregroundStyle(.purple)
                            }
                            
                            Text("Browse All \(totalPlans)")
                                .font(.system(.subheadline, design: .rounded, weight: .medium))
                                .foregroundStyle(.purple)
                            
                            Spacer()
                            
                            Image(systemName: "chevron.right")
                                .font(.system(size: 12))
                                .foregroundStyle(.tertiary)
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 10)
                        .background(colorScheme == .dark ? Color.white.opacity(0.02) : Color.black.opacity(0.01))
                    }
                    .buttonStyle(.plain)
                }
                .clipShape(RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal, 16)
                .padding(.bottom, 8)
                .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .background {
            if colorScheme == .dark {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(.ultraThinMaterial)
            } else {
                RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                    .fill(Color(.systemBackground))
                    .shadow(color: Color.black.opacity(0.04), radius: 6, x: 0, y: 2)
            }
        }
        .overlay {
            RoundedRectangle(cornerRadius: AppTheme.cornerRadius)
                .strokeBorder(
                    colorScheme == .dark ? Color.white.opacity(0.06) : Color.black.opacity(0.03),
                    lineWidth: 0.5
                )
        }
        .padding(.horizontal)
    }
}

// MARK: - Plan Section Row

private struct PlanSectionRow: View {
    @Environment(\.colorScheme) var colorScheme
    let name: String
    let icon: String
    let color: Color
    let count: Int?
    
    var body: some View {
        HStack(spacing: 12) {
            ZStack {
                Circle()
                    .fill(color.opacity(0.12))
                    .frame(width: 36, height: 36)
                Image(systemName: icon)
                    .font(.system(size: 14, weight: .medium))
                    .foregroundStyle(color)
            }
            
            Text(name)
                .font(.system(.subheadline, design: .rounded, weight: .medium))
            
            Spacer()
            
            if let count = count {
                Text("\(count)")
                    .font(.system(.caption2, design: .rounded, weight: .semibold))
                    .foregroundStyle(.secondary)
            }
            
            Image(systemName: "chevron.right")
                .font(.system(size: 11))
                .foregroundStyle(.tertiary)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .background(colorScheme == .dark ? Color.white.opacity(0.02) : Color.black.opacity(0.01))
    }
}

// MARK: - Global Search Overlay

private struct GlobalSearchOverlay: View {
    @Environment(\.colorScheme) var colorScheme
    let searchText: String
    let plans: [Plan]
    let scales: [ClinicalScale]
    let exams: [NeurologyExam]
    let tools: [NeurologyTool]
    
    private var hasResults: Bool {
        !plans.isEmpty || !scales.isEmpty || !exams.isEmpty || !tools.isEmpty
    }
    
    private var totalCount: Int {
        plans.count + scales.count + exams.count + tools.count
    }

    var body: some View {
        VStack(spacing: 0) {
            // Results summary header
            HStack {
                Text("\(totalCount) result\(totalCount == 1 ? "" : "s")")
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                    .foregroundStyle(.secondary)
                Spacer()
            }
            .padding(.horizontal)
            .padding(.vertical, 10)
            .background(colorScheme == .dark ? Color.black.opacity(0.3) : Color.white.opacity(0.9))
            
            if hasResults {
                List {
                    // Plans Section
                    if !plans.isEmpty {
                        Section {
                            ForEach(plans.prefix(8)) { plan in
                                NavigationLink(value: plan) {
                                    PlanSearchRow(plan: plan)
                                }
                                .listRowBackground(Color.clear)
                            }
                        } header: {
                            SearchSectionHeader(
                                title: "Clinical Plans",
                                icon: "doc.text.fill",
                                color: AppTheme.teal,
                                count: plans.count
                            )
                        }
                    }
                    
                    // Scales Section
                    if !scales.isEmpty {
                        Section {
                            ForEach(scales.prefix(6)) { scale in
                                NavigationLink(value: scale) {
                                    ScaleSearchRow(scale: scale)
                                }
                                .listRowBackground(Color.clear)
                            }
                        } header: {
                            SearchSectionHeader(
                                title: "Clinical Scales",
                                icon: "chart.bar.fill",
                                color: .blue,
                                count: scales.count
                            )
                        }
                    }
                    
                    // Exams Section
                    if !exams.isEmpty {
                        Section {
                            ForEach(exams.prefix(6)) { exam in
                                NavigationLink(value: exam) {
                                    ExamSearchRow(exam: exam)
                                }
                                .listRowBackground(Color.clear)
                            }
                        } header: {
                            SearchSectionHeader(
                                title: "Examinations",
                                icon: "stethoscope",
                                color: .teal,
                                count: exams.count
                            )
                        }
                    }
                    
                    // Tools Section
                    if !tools.isEmpty {
                        Section {
                            ForEach(tools.prefix(6)) { tool in
                                NavigationLink(value: tool) {
                                    ToolSearchRow(tool: tool)
                                }
                                .listRowBackground(Color.clear)
                            }
                        } header: {
                            SearchSectionHeader(
                                title: "Tools & Calculators",
                                icon: "wrench.and.screwdriver.fill",
                                color: .purple,
                                count: tools.count
                            )
                        }
                    }
                }
                .listStyle(.plain)
                .scrollContentBackground(.hidden)
            } else {
                // No results state
                VStack(spacing: 16) {
                    Spacer()
                    Image(systemName: "magnifyingglass")
                        .font(.system(size: 40))
                        .foregroundStyle(.tertiary)
                    Text("No results for \"\(searchText)\"")
                        .font(.system(.headline, design: .rounded))
                        .foregroundStyle(.secondary)
                    Text("Try searching for a condition, medication, or tool name")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                        .multilineTextAlignment(.center)
                    Spacer()
                }
                .padding()
            }
        }
        .background(colorScheme == .dark ? Color.black.opacity(0.95) : Color.white.opacity(0.98))
    }
}

// MARK: - Search Section Header

private struct SearchSectionHeader: View {
    let title: String
    let icon: String
    let color: Color
    let count: Int
    
    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: icon)
                .font(.system(size: 14, weight: .semibold))
                .foregroundStyle(color)
            Text(title)
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.primary)
            Spacer()
            if count > 0 {
                Text("\(count)")
                    .font(.system(.caption2, design: .rounded, weight: .bold))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 3)
                    .background(color, in: Capsule())
            }
        }
        .textCase(nil)
        .listRowInsets(EdgeInsets(top: 12, leading: 0, bottom: 6, trailing: 0))
    }
}

// MARK: - Search Result Rows

private struct PlanSearchRow: View {
    let plan: Plan
    
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(plan.title)
                .font(.system(.body, design: .rounded, weight: .medium))
                .lineLimit(2)
            
            HStack(spacing: 8) {
                if let cat = PlanCategory.category(for: plan.id) {
                    HStack(spacing: 4) {
                        Image(systemName: cat.icon)
                            .font(.system(size: 10))
                        Text(cat.name)
                            .font(.system(size: 11, weight: .medium))
                    }
                    .foregroundStyle(cat.swiftUIColor)
                }
                
                if let firstCode = plan.icd10.first {
                    Text(firstCode.prefix(10))
                        .font(.system(size: 10, design: .monospaced))
                        .foregroundStyle(.secondary)
                        .padding(.horizontal, 6)
                        .padding(.vertical, 2)
                        .background(.quaternary, in: RoundedRectangle(cornerRadius: 4))
                }
            }
        }
        .padding(.vertical, 4)
    }
}

private struct ScaleSearchRow: View {
    let scale: ClinicalScale
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(scale.title)
                .font(.system(.body, design: .rounded, weight: .medium))
                .lineLimit(1)
            
            HStack(spacing: 8) {
                Text(scale.abbreviation)
                    .font(.system(size: 11, weight: .semibold, design: .rounded))
                    .foregroundStyle(.blue)
                
                if !scale.components.isEmpty {
                    Text("\(scale.components.count) components")
                        .font(.system(size: 10))
                        .foregroundStyle(.secondary)
                }
            }
        }
        .padding(.vertical, 2)
    }
}

private struct ExamSearchRow: View {
    let exam: NeurologyExam
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(exam.title)
                .font(.system(.body, design: .rounded, weight: .medium))
                .lineLimit(1)
            
            if !exam.steps.isEmpty {
                Text("\(exam.steps.count) steps")
                    .font(.system(size: 10))
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical, 2)
    }
}

private struct ToolSearchRow: View {
    let tool: NeurologyTool
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(tool.title)
                .font(.system(.body, design: .rounded, weight: .medium))
                .lineLimit(1)
            
            HStack(spacing: 8) {
                HStack(spacing: 4) {
                    Image(systemName: toolIcon(tool.category))
                        .font(.system(size: 10))
                    Text(toolCategory(tool.category))
                        .font(.system(size: 10, weight: .medium))
                }
                .foregroundStyle(.purple)
            }
        }
        .padding(.vertical, 2)
    }
    
    private func toolIcon(_ category: String) -> String {
        switch category {
        case "calculator": "function"
        case "protocol": "list.number"
        case "reference_table": "tablecells"
        case "conversion": "arrow.left.arrow.right"
        default: "wrench.fill"
        }
    }
    
    private func toolCategory(_ category: String) -> String {
        switch category {
        case "calculator": "Calculator"
        case "protocol": "Protocol"
        case "reference_table": "Reference"
        case "conversion": "Conversion"
        default: "Tool"
        }
    }
}

// MARK: - Quick Actions Bar

private struct QuickActionsBar: View {
    let store: PlanStore

    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 10) {
                ForEach(SpecialtyConfig.quickActions, id: \.id) { action in
                    if let plan = store.plan(for: action.planId) {
                        NavigationLink(value: plan) {
                            HStack(spacing: 6) {
                                Image(systemName: action.icon)
                                    .font(.system(size: 13, weight: .semibold))
                                Text(action.title)
                                    .font(.system(.caption, design: .rounded, weight: .semibold))
                            }
                            .foregroundStyle(AppTheme.teal)
                            .padding(.horizontal, 14)
                            .padding(.vertical, 8)
                            .background(AppTheme.teal.opacity(0.12), in: Capsule())
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
        }
    }
}

#Preview {
    HomeView()
        .environment(PlanStore())
        .environment(PlanBuilder())
        .environment(ReferenceStore())
        .environment(UserPreferences())
}
