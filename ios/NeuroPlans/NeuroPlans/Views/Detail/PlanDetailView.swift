import SwiftUI

struct PlanDetailView: View {
    let plan: Plan

    @Environment(PlanStore.self) private var store
    @Environment(PlanBuilder.self) private var builder
    @Environment(ClinicalErrorService.self) private var errorService
    @State private var showScope = false
    @State private var showErrorReport = false

    var body: some View {
        @Bindable var store = store
        ScrollView {
            VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                // Header
                PlanHeader(plan: plan, showScope: $showScope)

                // Sticky Setting Picker
                SettingPicker(selected: $store.selectedSetting)
                    .padding(.horizontal)

                // Clinical Notes
                if !plan.notes.isEmpty {
                    NotesCard(notes: plan.notes)
                        .padding(.horizontal)
                }

                // Section A: Action Items
                sectionHeader("Action Items", icon: "checkmark.circle.fill")

                // 1. Labs
                if !plan.sections.labWorkup.isEmpty {
                    SectionGroup(
                        title: "Laboratory Workup",
                        icon: "testtube.2",
                        subsections: plan.sections.labWorkup,
                        setting: store.selectedSetting
                    ) { subsection, items in
                        ForEach(items) { item in
                            LabItemRow(
                                item: item,
                                setting: store.selectedSetting,
                                planId: plan.id,
                                planTitle: plan.title,
                                subsection: subsection
                            )
                        }
                    }
                }

                // 2. Imaging
                if !plan.sections.imaging.isEmpty {
                    SectionGroup(
                        title: "Imaging & Studies",
                        icon: "photo.artframe",
                        subsections: plan.sections.imaging,
                        setting: store.selectedSetting
                    ) { subsection, items in
                        ForEach(items) { item in
                            ImagingItemRow(
                                item: item,
                                setting: store.selectedSetting,
                                planId: plan.id,
                                planTitle: plan.title,
                                subsection: subsection
                            )
                        }
                    }
                }

                // 3. Treatment
                if !plan.sections.treatment.isEmpty {
                    SectionGroup(
                        title: "Treatment",
                        icon: "pill.fill",
                        subsections: plan.sections.treatment,
                        setting: store.selectedSetting
                    ) { subsection, items in
                        ForEach(items) { item in
                            TreatmentItemRow(
                                item: item,
                                setting: store.selectedSetting,
                                planId: plan.id,
                                planTitle: plan.title,
                                subsection: subsection
                            )
                        }
                    }
                }

                // 4. Other Recommendations
                if !plan.sections.otherRecs.isEmpty {
                    SectionGroup(
                        title: "Other Recommendations",
                        icon: "text.badge.checkmark",
                        subsections: plan.sections.otherRecs,
                        setting: store.selectedSetting
                    ) { subsection, items in
                        ForEach(items) { item in
                            OtherRecItemRow(
                                item: item,
                                setting: store.selectedSetting,
                                planId: plan.id,
                                planTitle: plan.title,
                                subsection: subsection
                            )
                        }
                    }
                }

                // Section B: Reference
                sectionHeader("Reference", icon: "book.fill")

                // 5. Differential
                if let differential = plan.differential, !differential.isEmpty {
                    DifferentialSection(items: differential)
                }

                // 6. Monitoring
                if let monitoring = plan.monitoring, !monitoring.isEmpty {
                    MonitoringSection(items: monitoring)
                }

                // 7. Disposition
                if let disposition = plan.disposition, !disposition.isEmpty {
                    DispositionSection(items: disposition)
                }

                // 8. Evidence
                if let evidence = plan.evidence, !evidence.isEmpty {
                    EvidenceSection(items: evidence)
                }

                Spacer(minLength: 100)
            }
            .padding(.top, 8)
        }
        .background { AdaptiveBackground() }
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                Button {
                    store.toggleFavorite(plan.id)
                } label: {
                    Image(systemName: store.isFavorite(plan.id) ? "star.fill" : "star")
                        .foregroundStyle(store.isFavorite(plan.id) ? .yellow : .secondary)
                }
                .sensoryFeedback(.impact(flexibility: .soft), trigger: store.isFavorite(plan.id))
            }

            ToolbarItem(placement: .topBarTrailing) {
                if !builder.isEmpty {
                    NavigationLink {
                        BuilderView()
                    } label: {
                        Image(systemName: "square.and.pencil")
                            .overlay(alignment: .topTrailing) {
                                Text("\(builder.itemCount)")
                                    .font(.system(size: 9, weight: .bold))
                                    .foregroundStyle(.white)
                                    .padding(3)
                                    .background(AppTheme.teal, in: Circle())
                                    .offset(x: 6, y: -6)
                            }
                    }
                }
            }
            
            ToolbarItem(placement: .topBarTrailing) {
                Menu {
                    Button {
                        showErrorReport = true
                    } label: {
                        Label("Report Clinical Error", systemImage: "exclamationmark.bubble.fill")
                    }
                } label: {
                    Image(systemName: "ellipsis.circle")
                }
            }
        }
        .onAppear {
            store.markViewed(plan.id)
            builder.activePlanTitle = plan.title
            errorService.recordPlanView()
        }
        .sheet(isPresented: $showErrorReport) {
            ClinicalErrorReportView(
                planId: plan.id,
                planTitle: plan.title,
                section: nil,
                itemText: nil
            )
        }
    }

    private func sectionHeader(_ title: String, icon: String) -> some View {
        HStack(spacing: 8) {
            Image(systemName: icon)
                .foregroundStyle(AppTheme.teal)
            Text(title)
                .font(.system(.title3, design: .rounded, weight: .bold))
            Rectangle()
                .fill(.quaternary)
                .frame(height: 1)
        }
        .padding(.horizontal)
        .padding(.top, 8)
    }
}

// MARK: - Plan Header

private struct PlanHeader: View {
    let plan: Plan
    @Binding var showScope: Bool

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            // Title
            Text(plan.title)
                .font(.system(.title2, design: .rounded, weight: .bold))
                .padding(.horizontal)

            // ICD-10 Codes
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 6) {
                    ForEach(plan.icd10, id: \.self) { code in
                        ICDCodeBadge(code: code)
                    }
                }
                .padding(.horizontal)
            }

            // Scope (collapsible)
            if !plan.scope.isEmpty {
                Button {
                    withAnimation(.snappy) { showScope.toggle() }
                } label: {
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        VStack(alignment: .leading, spacing: 6) {
                            HStack {
                                Image(systemName: "scope")
                                    .foregroundStyle(AppTheme.teal)
                                Text("Scope")
                                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                                Spacer()
                                Image(systemName: showScope ? "chevron.up" : "chevron.down")
                                    .font(.system(size: 12))
                                    .foregroundStyle(.secondary)
                            }
                            if showScope {
                                Text(plan.scope.replacingOccurrences(of: "** ", with: ""))
                                    .font(.system(.caption, design: .default))
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                }
                .buttonStyle(.plain)
                .padding(.horizontal)
            }

            // Version
            HStack {
                Text("v\(plan.version)")
                    .font(.system(.caption2, design: .monospaced))
                    .foregroundStyle(.tertiary)
                if let cat = PlanCategory.category(for: plan.id) {
                    Label(cat.name, systemImage: cat.icon)
                        .font(.system(.caption2, design: .rounded))
                        .foregroundStyle(cat.swiftUIColor)
                }
            }
            .padding(.horizontal)
        }
    }
}

// MARK: - Notes Card

private struct NotesCard: View {
    let notes: [String]
    @State private var expanded = false

    var body: some View {
        Button {
            withAnimation(.snappy) { expanded.toggle() }
        } label: {
            GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                VStack(alignment: .leading, spacing: 6) {
                    HStack {
                        Image(systemName: "exclamationmark.bubble.fill")
                            .foregroundStyle(.yellow)
                        Text("Clinical Notes")
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        Spacer()
                        Text("\(notes.count)")
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                        Image(systemName: expanded ? "chevron.up" : "chevron.down")
                            .font(.system(size: 12))
                            .foregroundStyle(.secondary)
                    }
                    if expanded {
                        ForEach(notes, id: \.self) { note in
                            HStack(alignment: .top, spacing: 6) {
                                Circle()
                                    .fill(.yellow)
                                    .frame(width: 4, height: 4)
                                    .padding(.top, 6)
                                Text(note)
                                    .font(.system(.caption))
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                }
            }
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Reference Sections

private struct DifferentialSection: View {
    let items: [DifferentialItem]
    @State private var expanded = false

    var body: some View {
        DisclosureGroup(isExpanded: $expanded) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(items) { item in
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        VStack(alignment: .leading, spacing: 4) {
                            Text(item.condition ?? "—")
                                .font(.system(.subheadline, weight: .medium))
                            if let features = item.features {
                                Text(features)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                            if let dist = item.distinguishing {
                                MetadataChip(icon: "arrow.left.arrow.right", text: dist, color: .orange)
                            }
                        }
                    }
                }
            }
            .padding(.horizontal)
        } label: {
            GlassSectionHeader(title: "Differential Diagnosis", icon: "list.triangle", count: items.count)
        }
        .tint(.secondary)
        .padding(.horizontal)
    }
}

private struct MonitoringSection: View {
    let items: [MonitoringItem]
    @State private var expanded = false

    var body: some View {
        DisclosureGroup(isExpanded: $expanded) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(items) { item in
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        VStack(alignment: .leading, spacing: 4) {
                            Text(item.parameter ?? "—")
                                .font(.system(.subheadline, weight: .medium))
                            if let freq = item.frequency {
                                HStack(spacing: 4) {
                                    Image(systemName: "clock")
                                        .font(.system(size: 10))
                                    Text(freq)
                                }
                                .font(.caption)
                                .foregroundStyle(.secondary)
                            }
                            if let action = item.action {
                                Text(action)
                                    .font(.caption)
                                    .foregroundStyle(.purple)
                            }
                        }
                    }
                }
            }
            .padding(.horizontal)
        } label: {
            GlassSectionHeader(title: "Monitoring", icon: "chart.xyaxis.line", count: items.count)
        }
        .tint(.secondary)
        .padding(.horizontal)
    }
}

private struct DispositionSection: View {
    let items: [DispositionItem]
    @State private var expanded = false

    var body: some View {
        DisclosureGroup(isExpanded: $expanded) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(items) { item in
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        VStack(alignment: .leading, spacing: 4) {
                            HStack(spacing: 6) {
                                Image(systemName: "arrow.right.circle.fill")
                                    .foregroundStyle(.green)
                                Text(item.setting ?? "—")
                                    .font(.system(.subheadline, weight: .medium))
                            }
                            if let criteria = item.criteria {
                                Text(criteria)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                }
            }
            .padding(.horizontal)
        } label: {
            GlassSectionHeader(title: "Disposition", icon: "arrow.right.square", count: items.count)
        }
        .tint(.secondary)
        .padding(.horizontal)
    }
}

private struct EvidenceSection: View {
    let items: [EvidenceItem]
    @State private var expanded = false

    var body: some View {
        DisclosureGroup(isExpanded: $expanded) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(items) { item in
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        VStack(alignment: .leading, spacing: 6) {
                            // Recommendation text
                            Text(item.recommendation ?? "—")
                                .font(.system(.subheadline, weight: .medium))
                            
                            // Evidence level badge
                            if let level = item.evidenceLevel, !level.isEmpty {
                                MetadataChip(icon: "checkmark.seal.fill", text: level, color: .green)
                            }
                            
                            // Source/references - parse markdown links
                            if let source = item.source {
                                Text(parseMarkdownLinks(source))
                                    .font(.caption)
                                    .foregroundStyle(.blue)
                                    .tint(.blue)
                            }
                        }
                    }
                }
            }
            .padding(.horizontal)
        } label: {
            GlassSectionHeader(title: "Evidence & References", icon: "books.vertical", count: items.count)
        }
        .tint(.secondary)
        .padding(.horizontal)
    }
    
    // Parse markdown-style links and return AttributedString
    private func parseMarkdownLinks(_ text: String) -> AttributedString {
        var result = AttributedString()
        let pattern = #"\[([^\]]+)\]\(([^)]+)\)"#
        
        guard let regex = try? NSRegularExpression(pattern: pattern) else {
            return AttributedString(text)
        }
        
        var lastEnd = text.startIndex
        let nsRange = NSRange(text.startIndex..., in: text)
        
        for match in regex.matches(in: text, range: nsRange) {
            // Add text before this match
            if let beforeRange = Range(NSRange(location: nsRange.location, length: match.range.location - nsRange.location), in: text) {
                let beforeText = String(text[lastEnd..<beforeRange.upperBound])
                if !beforeText.isEmpty {
                    result += AttributedString(beforeText)
                }
            }
            
            // Extract link text and URL
            if let textRange = Range(match.range(at: 1), in: text),
               let urlRange = Range(match.range(at: 2), in: text) {
                let linkText = String(text[textRange])
                let urlString = String(text[urlRange])
                
                var linkAttr = AttributedString(linkText)
                if let url = URL(string: urlString) {
                    linkAttr.link = url
                    linkAttr.underlineStyle = .single
                }
                result += linkAttr
            }
            
            if let matchRange = Range(match.range, in: text) {
                lastEnd = matchRange.upperBound
            }
        }
        
        // Add remaining text
        if lastEnd < text.endIndex {
            result += AttributedString(String(text[lastEnd...]))
        }
        
        return result
    }
}

#Preview {
    NavigationStack {
        PlanDetailView(plan: Plan(
            id: "sample", title: "Acute Ischemic Stroke",
            version: "1.0", icd10: ["I63.9"],
            scope: "Sample scope", notes: ["Note 1"],
            sections: PlanSections(labWorkup: [:], imaging: [:], treatment: [:], otherRecs: [:]),
            differential: [], evidence: [], monitoring: [], disposition: []
        ))
    }
    .environment(PlanStore())
    .environment(PlanBuilder())
    .environment(ClinicalErrorService())
}
