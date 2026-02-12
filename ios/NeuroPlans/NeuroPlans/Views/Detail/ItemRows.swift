import SwiftUI

// MARK: - Lab Item Row

struct LabItemRow: View {
    let item: LabItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @State private var showDetail = false

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.item, in: planId) }

    var body: some View {
        if priority.isApplicable {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.item,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Laboratory Workup",
                        subsection: subsection,
                        priority: priority
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

                    VStack(alignment: .leading, spacing: 2) {
                        Text(item.item)
                            .font(.system(.subheadline, weight: .medium))
                            .lineLimit(3)
                    }

                    Spacer()
                    PriorityBadge(priority: priority)
                }

                // Expandable metadata
                if showDetail {
                    VStack(alignment: .leading, spacing: 4) {
                        if let rationale = item.rationale, !rationale.isEmpty, rationale != "-" {
                            MetadataChip(icon: "info.circle", text: rationale, color: .blue)
                        }
                        if let target = item.target, !target.isEmpty, target != "-" {
                            MetadataChip(icon: "target", text: target, color: .green)
                        }
                    }
                }
            }
        }
        .overlay(alignment: .bottomTrailing) {
            if item.rationale != nil || item.target != nil {
                Button {
                    withAnimation(.snappy) { showDetail.toggle() }
                } label: {
                    Image(systemName: "info.circle")
                        .font(.system(size: 12))
                        .foregroundStyle(.tertiary)
                        .padding(8)
                }
            }
        }
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
    @State private var showDetail = false

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.item, in: planId) }

    var body: some View {
        if priority.isApplicable {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.item,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Imaging & Studies",
                        subsection: subsection,
                        priority: priority
                    )
                }
            } label: {
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(alignment: .leading, spacing: 6) {
                        HStack(spacing: 8) {
                            Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                                .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                                .font(.system(size: 18))

                            Text(item.item)
                                .font(.system(.subheadline, weight: .medium))
                                .lineLimit(3)

                            Spacer()
                            PriorityBadge(priority: priority)
                        }

                        if showDetail {
                            VStack(alignment: .leading, spacing: 4) {
                                if let timing = item.timing, !timing.isEmpty, timing != "-" {
                                    MetadataChip(icon: "clock", text: timing, color: .orange)
                                }
                                if let target = item.target, !target.isEmpty, target != "-" {
                                    MetadataChip(icon: "target", text: target, color: .green)
                                }
                                if let contra = item.contraindications, !contra.isEmpty, contra != "-" {
                                    MetadataChip(icon: "exclamationmark.triangle", text: contra, color: .red)
                                }
                            }
                        }
                    }
                }
                .overlay(alignment: .bottomTrailing) {
                    if item.timing != nil || item.target != nil || item.contraindications != nil {
                        Button {
                            withAnimation(.snappy) { showDetail.toggle() }
                        } label: {
                            Image(systemName: "info.circle")
                                .font(.system(size: 12))
                                .foregroundStyle(.tertiary)
                                .padding(8)
                        }
                    }
                }
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
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

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.item, in: planId) }

    var body: some View {
        if priority.isApplicable {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    builder.toggle(
                        itemText: item.item,
                        planId: planId,
                        planTitle: planTitle,
                        section: "Other Recommendations",
                        subsection: subsection,
                        priority: priority
                    )
                }
            } label: {
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    HStack(spacing: 8) {
                        Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                            .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                            .font(.system(size: 18))

                        Text(item.item)
                            .font(.system(.subheadline, weight: .medium))
                            .lineLimit(3)

                        Spacer()
                        PriorityBadge(priority: priority)
                    }
                }
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
    }
}
