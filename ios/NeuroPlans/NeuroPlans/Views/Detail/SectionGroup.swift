import SwiftUI

/// Protocol for items that can report their visibility for a clinical setting
protocol SettingFilterable {
    func isVisible(for setting: ClinicalSetting) -> Bool
}

/// Generic section container that displays subsections with collapsible headers.
/// Works with any item type (labs, imaging, treatment, other recs).
struct SectionGroup<Item: Identifiable, ItemView: View>: View {
    let title: String
    let icon: String
    let subsections: [String: [Item]]
    let setting: ClinicalSetting
    @ViewBuilder let itemView: (_ subsection: String, _ items: [Item]) -> ItemView

    @State private var expandedSubsections: Set<String>
    @State private var expanded = true
    @State private var hasInitialized = false

    /// Check if a subsection name indicates first-line/essential items
    private static func isFirstLineSubsection(_ name: String) -> Bool {
        let keywords = ["essential", "core", "first-line", "first line", "primary", "acute", "emergent", "stat"]
        let lower = name.lowercased()
        return keywords.contains { lower.contains($0) }
    }

    init(title: String, icon: String, subsections: [String: [Item]], setting: ClinicalSetting, @ViewBuilder itemView: @escaping (_ subsection: String, _ items: [Item]) -> ItemView) {
        self.title = title
        self.icon = icon
        self.subsections = subsections
        self.setting = setting
        self.itemView = itemView

        // Pre-compute which subsections should be expanded
        // Only expand subsections that have items AND are first-line
        var initialExpanded = Set<String>()
        for (key, items) in subsections {
            if !items.isEmpty && Self.isFirstLineSubsection(key) {
                initialExpanded.insert(key)
            }
        }
        // If none found, expand first non-empty subsection alphabetically
        if initialExpanded.isEmpty {
            let nonEmptyKeys = subsections.filter { !$0.value.isEmpty }.keys.sorted()
            if let first = nonEmptyKeys.first {
                initialExpanded.insert(first)
            }
        }
        self._expandedSubsections = State(initialValue: initialExpanded)
    }

    private var sortedSubsections: [(key: String, value: [Item])] {
        // Sort subsections: first-line items first, then by priority keywords
        return subsections.sorted { a, b in
            let aIsFirst = Self.isFirstLineSubsection(a.key)
            let bIsFirst = Self.isFirstLineSubsection(b.key)

            // First-line subsections come first
            if aIsFirst && !bIsFirst { return true }
            if !aIsFirst && bIsFirst { return false }

            // Secondary sort by keywords
            let secondaryOrder = ["extended", "second", "rare", "specialized", "referral", "education", "lifestyle"]
            let aSecondary = secondaryOrder.firstIndex { a.key.lowercased().contains($0) } ?? 999
            let bSecondary = secondaryOrder.firstIndex { b.key.lowercased().contains($0) } ?? 999

            if aSecondary != bSecondary { return aSecondary < bSecondary }

            // Finally, alphabetical
            return a.key < b.key
        }
    }

    private var totalItemCount: Int {
        subsections.values.reduce(0) { $0 + $1.count }
    }
    
    /// Count of items visible in the current setting (for filterable items)
    private var visibleItemCount: Int {
        var count = 0
        for items in subsections.values {
            for item in items {
                if let filterable = item as? SettingFilterable {
                    if filterable.isVisible(for: setting) {
                        count += 1
                    }
                } else {
                    // Non-filterable items are always visible
                    count += 1
                }
            }
        }
        return count
    }
    
    /// Check if any items are hidden due to the current setting filter
    private var hasHiddenItems: Bool {
        visibleItemCount < totalItemCount
    }
    
    /// Settings that have visible items for this section
    private var settingsWithItems: [ClinicalSetting] {
        ClinicalSetting.allCases.filter { testSetting in
            for items in subsections.values {
                for item in items {
                    if let filterable = item as? SettingFilterable {
                        if filterable.isVisible(for: testSetting) {
                            return true
                        }
                    }
                }
            }
            return false
        }
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
                    // Filter items based on visibility for current setting
                    let filteredItems = items.filter { item in
                        if let filterable = item as? SettingFilterable {
                            return filterable.isVisible(for: setting)
                        }
                        return true // Non-filterable items are always visible
                    }
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
                
                // Show hint when no items are visible in current setting
                if visibleItemCount == 0 && totalItemCount > 0 {
                    NoItemsHintView(
                        totalCount: totalItemCount,
                        currentSetting: setting,
                        availableSettings: settingsWithItems
                    )
                    .padding(.horizontal)
                }
            }
        }
        
    }
}

// MARK: - No Items Hint View

struct NoItemsHintView: View {
    let totalCount: Int
    let currentSetting: ClinicalSetting
    let availableSettings: [ClinicalSetting]
    
    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 8) {
                HStack(spacing: 6) {
                    Image(systemName: "info.circle.fill")
                        .foregroundStyle(.orange)
                    Text("No items for \(currentSetting.label)")
                        .font(.system(.subheadline, design: .rounded, weight: .medium))
                }
                
                if !availableSettings.isEmpty {
                    Text("\(totalCount) item\(totalCount == 1 ? "" : "s") available in:")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    
                    HStack(spacing: 8) {
                        ForEach(availableSettings) { setting in
                            HStack(spacing: 4) {
                                Image(systemName: setting.icon)
                                    .font(.system(size: 10))
                                Text(setting.label)
                                    .font(.system(.caption2, design: .rounded, weight: .medium))
                            }
                            .foregroundStyle(.teal)
                            .padding(.horizontal, 8)
                            .padding(.vertical, 4)
                            .background(.teal.opacity(0.1), in: Capsule())
                        }
                    }
                } else {
                    Text("This section has \(totalCount) reference item\(totalCount == 1 ? "" : "s").")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }
}
