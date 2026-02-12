import SwiftUI

struct TreatmentItemRow: View {
    let item: TreatmentItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @State private var showDetail = false
    @State private var copiedSentence = false

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
                        section: "Treatment",
                        subsection: subsection,
                        priority: priority,
                        orderSentence: item.dosing?.orderSentence
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
            VStack(alignment: .leading, spacing: 8) {
                // Main row
                HStack(spacing: 8) {
                    Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                        .foregroundStyle(isSelected ? AppTheme.teal : .secondary)
                        .font(.system(size: 18))

                    VStack(alignment: .leading, spacing: 3) {
                        Text(item.item)
                            .font(.system(.subheadline, weight: .medium))
                            .lineLimit(2)

                        // Route badge
                        if let route = item.route, !route.isEmpty, route != "-" {
                            Text(route)
                                .font(.system(size: 10, weight: .semibold, design: .rounded))
                                .foregroundStyle(.teal)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(.teal.opacity(0.15), in: Capsule())
                        }
                    }

                    Spacer()
                    PriorityBadge(priority: priority)
                }

                // Dose options (always visible for treatment)
                if let dosing = item.dosing, let options = dosing.doseOptions, !options.isEmpty {
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 6) {
                            ForEach(options) { option in
                                DoseBadge(option: option, onCopy: {
                                    if let sentence = option.orderSentence {
                                        UIPasteboard.general.string = sentence
                                        copiedSentence = true
                                        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                                            copiedSentence = false
                                        }
                                    }
                                })
                            }
                        }
                    }
                }

                // Copied feedback
                if copiedSentence {
                    HStack(spacing: 4) {
                        Image(systemName: "checkmark.circle.fill")
                            .font(.system(size: 10))
                        Text("Order sentence copied")
                            .font(.system(size: 10, weight: .medium))
                    }
                    .foregroundStyle(.green)
                    .transition(.opacity)
                }

                // Expanded metadata
                if showDetail {
                    VStack(alignment: .leading, spacing: 6) {
                        if let indication = item.indication, !indication.isEmpty, indication != "-" {
                            MetadataChip(icon: "pill.fill", text: indication, color: .teal)
                        }

                        if let instructions = item.dosing?.instructions, !instructions.isEmpty {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "info.circle.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.blue)
                                Text(instructions)
                                    .font(.system(.caption2))
                                    .foregroundStyle(.secondary)
                            }
                        }

                        if let contra = item.contraindications, !contra.isEmpty, contra != "-" {
                            MetadataChip(icon: "exclamationmark.triangle.fill", text: contra, color: .red)
                        }

                        if let monitoring = item.monitoring, !monitoring.isEmpty, monitoring != "-" {
                            MetadataChip(icon: "chart.xyaxis.line", text: monitoring, color: .purple)
                        }
                    }
                }
            }
        }
        .overlay(alignment: .bottomTrailing) {
            Button {
                withAnimation(.snappy) { showDetail.toggle() }
            } label: {
                Image(systemName: showDetail ? "chevron.up.circle.fill" : "info.circle")
                    .font(.system(size: 14))
                    .foregroundStyle(.tertiary)
                    .padding(8)
            }
        }
    }
}

// MARK: - Dose Badge

struct DoseBadge: View {
    let option: DoseOption
    var onCopy: (() -> Void)? = nil

    var body: some View {
        Button {
            onCopy?()
        } label: {
            HStack(spacing: 4) {
                Image(systemName: "syringe.fill")
                    .font(.system(size: 8))
                Text(option.text)
                    .font(.system(.caption2, design: .monospaced, weight: .medium))
            }
            .foregroundStyle(.teal)
            .padding(.horizontal, 8)
            .padding(.vertical, 4)
            .background(.teal.opacity(0.1), in: Capsule())
            .overlay {
                Capsule()
                    .strokeBorder(.teal.opacity(0.3), lineWidth: 0.5)
            }
        }
        .buttonStyle(.plain)
        .sensoryFeedback(.impact(flexibility: .soft, intensity: 0.5), trigger: option.text)
    }
}
