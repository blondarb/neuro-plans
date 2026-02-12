import SwiftUI

struct ReferenceHomeView: View {
    @Environment(ReferenceStore.self) private var store
    @State private var searchText = ""

    var body: some View {
        @Bindable var store = store
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                    // Quick Stats - Tappable navigation
                    HStack(spacing: 12) {
                        NavigationLink {
                            ScaleListView(title: "All Scales", scales: store.allScales)
                        } label: {
                            RefStatCard(
                                value: "\(store.scales.count)",
                                label: "Scales",
                                icon: "chart.bar.fill",
                                color: .blue
                            )
                        }
                        .buttonStyle(.plain)
                        
                        NavigationLink {
                            ExamListView(title: "All Exams", exams: store.allExams)
                        } label: {
                            RefStatCard(
                                value: "\(store.exams.count)",
                                label: "Exams",
                                icon: "stethoscope",
                                color: AppTheme.teal
                            )
                        }
                        .buttonStyle(.plain)
                        
                        NavigationLink {
                            ToolListView(title: "All Tools", tools: store.allTools)
                        } label: {
                            RefStatCard(
                                value: "\(store.tools.count)",
                                label: "Tools",
                                icon: "wrench.and.screwdriver.fill",
                                color: .purple
                            )
                        }
                        .buttonStyle(.plain)
                    }
                    .padding(.horizontal)
                    
                    // Exam Tools - Interactive bedside tools
                    NavigationLink {
                        ExamToolsGridView()
                    } label: {
                        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                            HStack(spacing: 16) {
                                ZStack {
                                    Circle()
                                        .fill(LinearGradient(
                                            colors: [.yellow.opacity(0.3), .orange.opacity(0.3)],
                                            startPoint: .topLeading,
                                            endPoint: .bottomTrailing
                                        ))
                                        .frame(width: 50, height: 50)
                                    Image(systemName: "flashlight.on.fill")
                                        .font(.system(size: 24))
                                        .foregroundStyle(.yellow)
                                }
                                
                                VStack(alignment: .leading, spacing: 4) {
                                    Text("Exam Tools")
                                        .font(.system(.headline, design: .rounded, weight: .semibold))
                                    Text("Penlight, OKN stripes, visual acuity, Amsler grid, stopwatch")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                        .lineLimit(1)
                                }
                                
                                Spacer()
                                
                                Image(systemName: "chevron.right")
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                    .buttonStyle(.plain)
                    .padding(.horizontal)

                    // Scales Section
                    VStack(alignment: .leading, spacing: 10) {
                        GlassSectionHeader(
                            title: "Clinical Scores & Scales",
                            icon: "chart.bar.fill",
                            count: store.scales.count
                        )
                        .padding(.horizontal)

                        LazyVGrid(
                            columns: [
                                GridItem(.flexible(), spacing: 10),
                                GridItem(.flexible(), spacing: 10)
                            ],
                            spacing: 10
                        ) {
                            ForEach(store.scaleCategories) { cat in
                                NavigationLink(value: cat) {
                                    RefCategoryCard(
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: cat.color,
                                        count: store.scales(for: cat).count
                                    )
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.horizontal)

                        NavigationLink {
                            ScaleListView(title: "All Scales", scales: store.allScales)
                        } label: {
                            GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                                HStack {
                                    Image(systemName: "chart.bar.fill")
                                        .foregroundStyle(.blue)
                                    Text("Browse All \(store.scales.count) Scales")
                                        .font(AppTheme.headlineFont)
                                    Spacer()
                                    Image(systemName: "chevron.right")
                                        .foregroundStyle(.secondary)
                                }
                            }
                        }
                        .buttonStyle(.plain)
                        .padding(.horizontal)
                    }

                    // Exams Section
                    VStack(alignment: .leading, spacing: 10) {
                        GlassSectionHeader(
                            title: "Standard Examinations",
                            icon: "stethoscope",
                            count: store.exams.count
                        )
                        .padding(.horizontal)

                        LazyVGrid(
                            columns: [
                                GridItem(.flexible(), spacing: 10),
                                GridItem(.flexible(), spacing: 10)
                            ],
                            spacing: 10
                        ) {
                            ForEach(store.examCategories) { cat in
                                NavigationLink(value: cat) {
                                    RefCategoryCard(
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: cat.color,
                                        count: store.exams(for: cat).count
                                    )
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.horizontal)
                    }

                    // Tools Section
                    VStack(alignment: .leading, spacing: 10) {
                        GlassSectionHeader(
                            title: "Tools & References",
                            icon: "wrench.and.screwdriver.fill",
                            count: store.tools.count
                        )
                        .padding(.horizontal)

                        LazyVGrid(
                            columns: [
                                GridItem(.flexible(), spacing: 10),
                                GridItem(.flexible(), spacing: 10)
                            ],
                            spacing: 10
                        ) {
                            ForEach(store.toolCategories) { cat in
                                NavigationLink(value: cat) {
                                    RefCategoryCard(
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: cat.color,
                                        count: store.tools(for: cat).count
                                    )
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.horizontal)
                    }

                    Spacer(minLength: 40)
                }
                .padding(.top, 8)
            }
            .background(LinearGradient.appBackground.ignoresSafeArea())
            .navigationTitle("Reference")
            .searchable(text: $searchText, prompt: "Search scales, exams, tools...")
            .onChange(of: searchText) { _, newValue in
                store.searchText = newValue
            }
            .navigationDestination(for: ReferenceScaleCategory.self) { cat in
                ScaleListView(
                    title: cat.name,
                    scales: store.scales(for: cat),
                    icon: cat.icon
                )
            }
            .navigationDestination(for: ReferenceExamCategory.self) { cat in
                ExamListView(
                    title: cat.name,
                    exams: store.exams(for: cat),
                    icon: cat.icon
                )
            }
            .navigationDestination(for: ReferenceToolCategory.self) { cat in
                ToolListView(
                    title: cat.name,
                    tools: store.tools(for: cat),
                    icon: cat.icon
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
                    ReferenceSearchOverlay(
                        scales: store.filteredScales,
                        exams: store.filteredExams,
                        tools: store.filteredTools
                    )
                }
            }
        }
    }
}

// MARK: - Stat Card

private struct RefStatCard: View {
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

// MARK: - Category Card

struct RefCategoryCard: View {
    let name: String
    let icon: String
    let color: String
    let count: Int

    private var swiftUIColor: Color {
        switch color {
        case "red": .red
        case "orange": .orange
        case "yellow": .yellow
        case "green": .green
        case "teal": .teal
        case "blue": .blue
        case "indigo": .indigo
        case "purple": .purple
        case "pink": .pink
        default: .teal
        }
    }

    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    Image(systemName: icon)
                        .font(.system(size: 22, weight: .semibold))
                        .foregroundStyle(swiftUIColor)
                        .frame(width: 36, height: 36)
                        .background(swiftUIColor.opacity(0.15))
                        .clipShape(RoundedRectangle(cornerRadius: 8))

                    Spacer()

                    Text("\(count)")
                        .font(.system(.caption, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                }

                Text(name)
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
            }
        }
    }
}

// MARK: - Search Overlay

private struct ReferenceSearchOverlay: View {
    let scales: [ClinicalScale]
    let exams: [NeurologyExam]
    let tools: [NeurologyTool]

    var body: some View {
        List {
            if !scales.isEmpty {
                Section("Scales") {
                    ForEach(scales.prefix(8)) { scale in
                        NavigationLink(value: scale) {
                            Label {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(scale.title)
                                        .font(.system(.body, design: .rounded, weight: .medium))
                                    Text(scale.abbreviation)
                                        .font(.caption2)
                                        .foregroundStyle(.blue)
                                }
                            } icon: {
                                Image(systemName: "chart.bar.fill")
                                    .foregroundStyle(.blue)
                            }
                        }
                    }
                }
            }

            if !exams.isEmpty {
                Section("Examinations") {
                    ForEach(exams.prefix(8)) { exam in
                        NavigationLink(value: exam) {
                            Label {
                                Text(exam.title)
                                    .font(.system(.body, design: .rounded, weight: .medium))
                            } icon: {
                                Image(systemName: "stethoscope")
                                    .foregroundStyle(.teal)
                            }
                        }
                    }
                }
            }

            if !tools.isEmpty {
                Section("Tools") {
                    ForEach(tools.prefix(8)) { tool in
                        NavigationLink(value: tool) {
                            Label {
                                Text(tool.title)
                                    .font(.system(.body, design: .rounded, weight: .medium))
                            } icon: {
                                Image(systemName: toolIcon(tool.category))
                                    .foregroundStyle(.purple)
                            }
                        }
                    }
                }
            }
        }
        .listStyle(.plain)
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
}

#Preview {
    ReferenceHomeView()
        .environment(ReferenceStore())
}
