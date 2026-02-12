import SwiftUI

struct ReferenceHomeView: View {
    @Environment(ReferenceStore.self) private var store
    @Environment(UserPreferences.self) private var prefs
    @State private var searchText = ""

    var body: some View {
        @Bindable var store = store
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    
                    // Render sections in user's preferred order
                    ForEach(prefs.referenceSectionOrder, id: \.self) { sectionId in
                        switch sectionId {
                        case "examTools":
                            ExamToolsSection(sectionId: "examTools")
                        case "scales":
                            ReferenceSection(
                                sectionId: "scales",
                                title: "Clinical Scales",
                                icon: "chart.bar.fill",
                                color: .blue,
                                items: store.scaleCategories.map { cat in
                                    ReferenceSectionItem(
                                        id: cat.id,
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: colorFromString(cat.color),
                                        count: store.scales(for: cat).count,
                                        destination: cat
                                    )
                                },
                                browseAllCount: store.scales.count,
                                browseAllDestination: "allScales"
                            )
                        case "exams":
                            ReferenceSection(
                                sectionId: "exams",
                                title: "Examinations",
                                icon: "stethoscope",
                                color: .teal,
                                items: store.examCategories.map { cat in
                                    ReferenceSectionItem(
                                        id: cat.id,
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: colorFromString(cat.color),
                                        count: store.exams(for: cat).count,
                                        destination: cat
                                    )
                                },
                                browseAllCount: store.exams.count,
                                browseAllDestination: "allExams"
                            )
                        case "tools":
                            ReferenceSection(
                                sectionId: "tools",
                                title: "Tools & Calculators",
                                icon: "function",
                                color: .purple,
                                items: store.toolCategories.map { cat in
                                    ReferenceSectionItem(
                                        id: cat.id,
                                        name: cat.name,
                                        icon: cat.icon,
                                        color: colorFromString(cat.color),
                                        count: store.tools(for: cat).count,
                                        destination: cat
                                    )
                                },
                                browseAllCount: store.tools.count,
                                browseAllDestination: "allTools"
                            )
                        default:
                            EmptyView()
                        }
                    }

                    Spacer(minLength: 40)
                }
                .padding(.top, 8)
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Reference")
            .searchable(text: $searchText, prompt: "Search scales, exams, tools...")
            .onChange(of: searchText) { _, newValue in
                store.searchText = newValue
            }
            // Navigation destinations
            .navigationDestination(for: String.self) { value in
                switch value {
                case "allScales":
                    ScaleListView(title: "All Scales", scales: store.allScales)
                case "allExams":
                    ExamListView(title: "All Exams", exams: store.allExams)
                case "allTools":
                    ToolListView(title: "All Tools", tools: store.allTools)
                default:
                    EmptyView()
                }
            }
            .navigationDestination(for: ExamToolType.self) { tool in
                ExamToolDetailView(toolType: tool)
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
    
    private func colorFromString(_ color: String) -> Color {
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
}

// MARK: - Exam Tools Section

private struct ExamToolsSection: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(UserPreferences.self) private var prefs
    let sectionId: String
    
    private let tools = ExamToolType.allCases
    
    private var isExpanded: Bool {
        prefs.isExpanded(sectionId, in: .reference)
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Section Header
            Button {
                withAnimation(.snappy(duration: 0.25)) {
                    prefs.toggleExpanded(sectionId, in: .reference)
                }
            } label: {
                HStack(spacing: 10) {
                    ZStack {
                        Circle()
                            .fill(Color.orange.opacity(0.15))
                            .frame(width: 32, height: 32)
                        Image(systemName: "hand.point.up.left.fill")
                            .font(.system(size: 14, weight: .semibold))
                            .foregroundStyle(.orange)
                    }
                    
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Exam Tools")
                            .font(.system(.headline, design: .rounded, weight: .semibold))
                        Text("Interactive bedside tools")
                            .font(.system(size: 11))
                            .foregroundStyle(.secondary)
                    }
                    
                    Spacer()
                    
                    Text("\(tools.count)")
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
                    ForEach(tools, id: \.self) { tool in
                        NavigationLink(value: tool) {
                            ExamToolSectionRow(tool: tool)
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

private struct ExamToolSectionRow: View {
    @Environment(\.colorScheme) var colorScheme
    let tool: ExamToolType
    
    var body: some View {
        HStack(spacing: 12) {
            ZStack {
                Circle()
                    .fill(tool.color.opacity(0.12))
                    .frame(width: 36, height: 36)
                Image(systemName: tool.icon)
                    .font(.system(size: 14, weight: .medium))
                    .foregroundStyle(tool.color)
            }
            
            VStack(alignment: .leading, spacing: 2) {
                Text(tool.rawValue)
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                Text(tool.description)
                    .font(.system(size: 10))
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }
            
            Spacer()
            
            Image(systemName: "chevron.right")
                .font(.system(size: 11))
                .foregroundStyle(.tertiary)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .background(colorScheme == .dark ? Color.white.opacity(0.02) : Color.black.opacity(0.01))
    }
}

// MARK: - Reference Section

private struct ReferenceSectionItem<Destination: Hashable>: Identifiable {
    let id: String
    let name: String
    let icon: String
    let color: Color
    let count: Int
    let destination: Destination
}

private struct ReferenceSection<Destination: Hashable>: View {
    @Environment(\.colorScheme) var colorScheme
    @Environment(UserPreferences.self) private var prefs
    let sectionId: String
    let title: String
    let icon: String
    let color: Color
    let items: [ReferenceSectionItem<Destination>]
    let browseAllCount: Int
    let browseAllDestination: String
    
    private var isExpanded: Bool {
        prefs.isExpanded(sectionId, in: .reference)
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Section Header
            Button {
                withAnimation(.snappy(duration: 0.25)) {
                    prefs.toggleExpanded(sectionId, in: .reference)
                }
            } label: {
                HStack(spacing: 10) {
                    ZStack {
                        Circle()
                            .fill(color.opacity(0.15))
                            .frame(width: 32, height: 32)
                        Image(systemName: icon)
                            .font(.system(size: 14, weight: .semibold))
                            .foregroundStyle(color)
                    }
                    
                    Text(title)
                        .font(.system(.headline, design: .rounded, weight: .semibold))
                    
                    Spacer()
                    
                    Text("\(browseAllCount)")
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
                    ForEach(items) { item in
                        NavigationLink(value: item.destination) {
                            ReferenceSectionRow(
                                name: item.name,
                                icon: item.icon,
                                color: item.color,
                                count: item.count
                            )
                        }
                        .buttonStyle(.plain)
                    }
                    
                    // Browse All row
                    NavigationLink(value: browseAllDestination) {
                        HStack(spacing: 12) {
                            ZStack {
                                Circle()
                                    .fill(color.opacity(0.1))
                                    .frame(width: 36, height: 36)
                                Image(systemName: "list.bullet")
                                    .font(.system(size: 14))
                                    .foregroundStyle(color)
                            }
                            
                            Text("Browse All \(browseAllCount)")
                                .font(.system(.subheadline, design: .rounded, weight: .medium))
                                .foregroundStyle(color)
                            
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

private struct ReferenceSectionRow: View {
    @Environment(\.colorScheme) var colorScheme
    let name: String
    let icon: String
    let color: Color
    let count: Int
    
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
            
            Text("\(count)")
                .font(.system(.caption2, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)
            
            Image(systemName: "chevron.right")
                .font(.system(size: 11))
                .foregroundStyle(.tertiary)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .background(colorScheme == .dark ? Color.white.opacity(0.02) : Color.black.opacity(0.01))
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
                        .listRowBackground(Color(.systemBackground))
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
                        .listRowBackground(Color(.systemBackground))
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
                        .listRowBackground(Color(.systemBackground))
                    }
                }
            }
        }
        .scrollContentBackground(.visible)
        .background(Color(.systemBackground))
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
        .environment(UserPreferences())
}
