import SwiftUI

/// Generic section container that displays subsections with collapsible headers.
/// Works with any item type (labs, imaging, treatment, other recs).
struct SectionGroup<Item: Identifiable, ItemView: View>: View {
    let title: String
    let icon: String
    let subsections: [String: [Item]]
    let setting: ClinicalSetting
    @ViewBuilder let itemView: (_ subsection: String, _ items: [Item]) -> ItemView

    @State private var expandedSubsections: Set<String> = []
    @State private var expanded = true

    private var sortedSubsections: [(key: String, value: [Item])] {
        // Sort subsections by expected order
        let order = [
            "Essential/Core Labs", "Extended Workup", "Rare/Specialized",
            "Essential/First-line", "Extended/Second-line", "Specialized",
            "Acute/Emergent", "Symptomatic Treatments",
            "Second-line/Refractory", "Disease-Modifying / Chronic Therapies",
            "Referrals", "Patient Education", "Lifestyle/Supportive"
        ]
        return subsections.sorted { a, b in
            let ai = order.firstIndex(of: a.key) ?? 999
            let bi = order.firstIndex(of: b.key) ?? 999
            return ai < bi
        }
    }

    private var totalItemCount: Int {
        subsections.values.reduce(0) { $0 + $1.count }
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // Section header
            Button {
                withAnimation(.snappy) { expanded.toggle() }
            } label: {
                HStack(spacing: 8) {
                    Image(systemName: icon)
                        .font(.system(size: 16, weight: .semibold))
                        .foregroundStyle(AppTheme.teal)
                        .frame(width: 24)

                    Text(title)
                        .font(AppTheme.headlineFont)

                    Spacer()

                    Text("\(totalItemCount)")
                        .font(.system(.caption, design: .rounded, weight: .medium))
                        .foregroundStyle(.secondary)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 2)
                        .background(.quaternary, in: Capsule())

                    Image(systemName: expanded ? "chevron.up" : "chevron.down")
                        .font(.system(size: 12, weight: .semibold))
                        .foregroundStyle(.secondary)
                }
            }
            .buttonStyle(.plain)
            .padding(.horizontal)

            if expanded {
                ForEach(sortedSubsections, id: \.key) { subsection, items in
                    let filteredItems = items
                    if !filteredItems.isEmpty {
                        VStack(alignment: .leading, spacing: 4) {
                            // Subsection header
                            Button {
                                withAnimation(.snappy) {
                                    if expandedSubsections.contains(subsection) {
                                        expandedSubsections.remove(subsection)
                                    } else {
                                        expandedSubsections.insert(subsection)
                                    }
                                }
                            } label: {
                                HStack(spacing: 6) {
                                    Text(subsection)
                                        .font(.system(.subheadline, design: .rounded, weight: .medium))
                                        .foregroundStyle(.secondary)
                                    Text("\(filteredItems.count)")
                                        .font(.system(size: 10, weight: .medium, design: .rounded))
                                        .foregroundStyle(.tertiary)
                                    Spacer()
                                    Image(systemName: expandedSubsections.contains(subsection) ? "chevron.up" : "chevron.down")
                                        .font(.system(size: 10))
                                        .foregroundStyle(.tertiary)
                                }
                                .padding(.horizontal, 20)
                            }
                            .buttonStyle(.plain)

                            if expandedSubsections.contains(subsection) {
                                itemView(subsection, filteredItems)
                                    .padding(.horizontal)
                                    .transition(.opacity.combined(with: .move(edge: .top)))
                            }
                        }
                    }
                }
            }
        }
        .onAppear {
            // Auto-expand first subsection
            if let first = sortedSubsections.first {
                expandedSubsections.insert(first.key)
            }
        }
    }
}
