import SwiftUI

// MARK: - Lab Item Row

struct LabItemRow: View {
    let item: LabItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @Environment(PlanStore.self) private var store
    @State private var showDetail = false

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.displayText, in: planId) }
    private var isFavorite: Bool { store.isFavoriteItem(planId, itemText: item.displayText) }

    /// Show item if it has venue-specific priority OR if it's a reference item
    private var shouldShow: Bool {
        !item.displayText.isEmpty && (priority.isApplicable || item.isReferenceItem)
    }

    var body: some View {
        if shouldShow {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.displayText,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Laboratory Workup",
                        subsection: subsection,
                        priority: item.isReferenceItem ? .routine : priority
                    )
                }
            } label: {
                itemContent
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
    }

    private var itemContent: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 6) {
                HStack(spacing: 8) {
                    // Selection indicator
                    Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                        .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                        .font(.system(size: 18))

                    Text(item.displayText)
                        .font(.system(.subheadline, weight: .medium))
                        .lineLimit(3)

                    Spacer()

                    // Info button if there's extra content
                    if hasExpandableContent {
                        Button {
                            withAnimation(.snappy) { showDetail.toggle() }
                        } label: {
                            Image(systemName: showDetail ? "chevron.up.circle.fill" : "info.circle.fill")
                                .font(.system(size: 16))
                                .foregroundStyle(showDetail ? AppTheme.teal : .blue.opacity(0.7))
                        }
                        .buttonStyle(.plain)
                    }

                    // Favorite button
                    Button {
                        withAnimation(.snappy) {
                            store.toggleFavoriteItem(planId, itemText: item.displayText)
                        }
                    } label: {
                        Image(systemName: isFavorite ? "star.fill" : "star")
                            .font(.system(size: 14))
                            .foregroundStyle(isFavorite ? .yellow : .gray.opacity(0.5))
                    }
                    .buttonStyle(.plain)
                    .sensoryFeedback(.impact(flexibility: .soft), trigger: isFavorite)

                    // Show REF badge for reference items, otherwise priority
                    if item.isReferenceItem {
                        Text("REF")
                            .font(.system(size: 10, weight: .bold, design: .rounded))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 6)
                            .padding(.vertical, 2)
                            .background(.purple, in: Capsule())
                    } else {
                        PriorityBadge(priority: priority)
                    }
                }

                // Expanded details
                if showDetail {
                    VStack(alignment: .leading, spacing: 6) {
                        if let rationale = item.rationale, !rationale.isEmpty, rationale != "-" {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "info.circle.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.blue)
                                Text(rationale)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
                            }
                        }
                        if let target = item.target, !target.isEmpty, target != "-" {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "target")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.green)
                                Text("Target: \(target)")
                                    .font(.system(.caption, design: .rounded, weight: .medium))
                                    .foregroundStyle(.green)
                            }
                        }
                    }
                    .padding(.leading, 26)
                    .transition(.opacity.combined(with: .move(edge: .top)))
                }
            }
        }
    }

    private var hasExpandableContent: Bool {
        (item.rationale != nil && item.rationale != "-" && !(item.rationale?.isEmpty ?? true)) ||
        (item.target != nil && item.target != "-" && !(item.target?.isEmpty ?? true))
    }
}

// MARK: - Imaging Item Row

struct ImagingItemRow: View {
    let item: ImagingItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @Environment(PlanStore.self) private var store
    @State private var showDetail = false

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.displayText, in: planId) }
    private var isFavorite: Bool { store.isFavoriteItem(planId, itemText: item.displayText) }

    /// Show item if it has venue-specific priority OR if it's a reference item
    private var shouldShow: Bool {
        !item.displayText.isEmpty && (priority.isApplicable || item.isReferenceItem)
    }

    var body: some View {
        if shouldShow {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.displayText,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Imaging & Studies",
                        subsection: subsection,
                        priority: item.isReferenceItem ? .routine : priority
                    )
                }
            } label: {
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(alignment: .leading, spacing: 6) {
                        HStack(spacing: 8) {
                            Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                                .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                                .font(.system(size: 18))

                            Text(item.displayText)
                                .font(.system(.subheadline, weight: .medium))
                                .lineLimit(3)

                            Spacer()

                            // Info button if there's extra content
                            if hasExpandableContent {
                                Button {
                                    withAnimation(.snappy) { showDetail.toggle() }
                                } label: {
                                    Image(systemName: showDetail ? "chevron.up.circle.fill" : "info.circle.fill")
                                        .font(.system(size: 16))
                                        .foregroundStyle(showDetail ? AppTheme.teal : .blue.opacity(0.7))
                                }
                                .buttonStyle(.plain)
                            }

                            // Favorite button
                            Button {
                                withAnimation(.snappy) {
                                    store.toggleFavoriteItem(planId, itemText: item.displayText)
                                }
                            } label: {
                                Image(systemName: isFavorite ? "star.fill" : "star")
                                    .font(.system(size: 14))
                                    .foregroundStyle(isFavorite ? .yellow : .gray.opacity(0.5))
                            }
                            .buttonStyle(.plain)
                            .sensoryFeedback(.impact(flexibility: .soft), trigger: isFavorite)

                            // Show REF badge for reference items, otherwise priority
                            if item.isReferenceItem {
                                Text("REF")
                                    .font(.system(size: 10, weight: .bold, design: .rounded))
                                    .foregroundStyle(.white)
                                    .padding(.horizontal, 6)
                                    .padding(.vertical, 2)
                                    .background(.purple, in: Capsule())
                            } else {
                                PriorityBadge(priority: priority)
                            }
                        }

                        // Expanded details
                        if showDetail {
                            VStack(alignment: .leading, spacing: 6) {
                                if let rationale = item.rationale, !rationale.isEmpty, rationale != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "lightbulb.fill")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.yellow)
                                        Text(rationale)
                                            .font(.system(.caption, design: .rounded))
                                            .foregroundStyle(.secondary)
                                    }
                                }
                                if let target = item.target, !target.isEmpty, target != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "target")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.green)
                                        Text(target)
                                            .font(.system(.caption, design: .rounded))
                                            .foregroundStyle(.secondary)
                                    }
                                }
                                if let timing = item.timing, !timing.isEmpty, timing != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "clock.fill")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.orange)
                                        Text(timing)
                                            .font(.system(.caption, design: .rounded, weight: .medium))
                                            .foregroundStyle(.orange)
                                    }
                                }
                                if let contra = item.contraindications, !contra.isEmpty, contra != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "exclamationmark.triangle.fill")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.red)
                                        Text(contra)
                                            .font(.system(.caption, design: .rounded))
                                        .foregroundStyle(.red.opacity(0.8))
                                    }
                                }
                            }
                            .padding(.leading, 26)
                            .transition(.opacity.combined(with: .move(edge: .top)))
                        }
                    }
                }
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
    }

    private var hasExpandableContent: Bool {
        (item.rationale != nil && item.rationale != "-" && !(item.rationale?.isEmpty ?? true)) ||
        (item.target != nil && item.target != "-" && !(item.target?.isEmpty ?? true)) ||
        (item.timing != nil && item.timing != "-" && !(item.timing?.isEmpty ?? true)) ||
        (item.contraindications != nil && item.contraindications != "-" && !(item.contraindications?.isEmpty ?? true))
    }
}

// MARK: - Other Rec Item Row

struct OtherRecItemRow: View {
    let item: OtherRecItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @Environment(PlanStore.self) private var store
    @State private var showDetail = false

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.displayText, in: planId) }
    private var isFavorite: Bool { store.isFavoriteItem(planId, itemText: item.displayText) }

    /// Show item if it has venue-specific priority OR if it's a reference item
    private var shouldShow: Bool {
        !item.displayText.isEmpty && (priority.isApplicable || item.isReferenceItem)
    }

    var body: some View {
        if shouldShow {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.displayText,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Other Recommendations",
                        subsection: subsection,
                        priority: item.isReferenceItem ? .routine : priority
                    )
                }
            } label: {
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(alignment: .leading, spacing: 6) {
                        HStack(spacing: 8) {
                            Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                                .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                                .font(.system(size: 18))

                            Text(item.displayText)
                                .font(.system(.subheadline, weight: .medium))
                                .lineLimit(3)

                            Spacer()

                            // Info button if there's extra content
                            if hasExpandableContent {
                                Button {
                                    withAnimation(.snappy) { showDetail.toggle() }
                                } label: {
                                    Image(systemName: showDetail ? "chevron.up.circle.fill" : "info.circle.fill")
                                        .font(.system(size: 16))
                                        .foregroundStyle(showDetail ? AppTheme.teal : .blue.opacity(0.7))
                                }
                                .buttonStyle(.plain)
                            }

                            // Favorite button
                            Button {
                                withAnimation(.snappy) {
                                    store.toggleFavoriteItem(planId, itemText: item.displayText)
                                }
                            } label: {
                                Image(systemName: isFavorite ? "star.fill" : "star")
                                    .font(.system(size: 14))
                                    .foregroundStyle(isFavorite ? .yellow : .gray.opacity(0.5))
                            }
                            .buttonStyle(.plain)
                            .sensoryFeedback(.impact(flexibility: .soft), trigger: isFavorite)

                            // Show REF badge for reference items, otherwise priority
                            if item.isReferenceItem {
                                Text("REF")
                                    .font(.system(size: 10, weight: .bold, design: .rounded))
                                    .foregroundStyle(.white)
                                    .padding(.horizontal, 6)
                                    .padding(.vertical, 2)
                                    .background(.purple, in: Capsule())
                            } else {
                                PriorityBadge(priority: priority)
                            }
                        }

                        // Expanded details
                        if showDetail {
                            VStack(alignment: .leading, spacing: 6) {
                                if let rationale = item.rationale, !rationale.isEmpty, rationale != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "lightbulb.fill")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.yellow)
                                        Text(rationale)
                                            .font(.system(.caption, design: .rounded))
                                            .foregroundStyle(.secondary)
                                    }
                                }
                                if let timing = item.timing, !timing.isEmpty, timing != "-" {
                                    HStack(alignment: .top, spacing: 6) {
                                        Image(systemName: "clock.fill")
                                            .font(.system(size: 10))
                                            .foregroundStyle(.orange)
                                        Text(timing)
                                            .font(.system(.caption, design: .rounded, weight: .medium))
                                            .foregroundStyle(.orange)
                                    }
                                }
                            }
                            .padding(.leading, 26)
                            .transition(.opacity.combined(with: .move(edge: .top)))
                        }
                    }
                }
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
    }

    private var hasExpandableContent: Bool {
        (item.rationale != nil && item.rationale != "-" && !(item.rationale?.isEmpty ?? true)) ||
        (item.timing != nil && item.timing != "-" && !(item.timing?.isEmpty ?? true))
    }
}
