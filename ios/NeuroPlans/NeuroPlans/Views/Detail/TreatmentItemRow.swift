import SwiftUI

struct TreatmentItemRow: View {
    let item: TreatmentItem
    let setting: ClinicalSetting
    let planId: String
    let planTitle: String
    let subsection: String

    @Environment(PlanBuilder.self) private var builder
    @Environment(PlanStore.self) private var store
    @State private var showDetail = false
    @State private var copiedSentence = false
    @State private var selectedDoseIndex: Int = 0

    private var priority: Priority { item.priority(for: setting) }
    private var isSelected: Bool { builder.isSelected(item.displayText, in: planId) }
    private var isFavorite: Bool { store.isFavoriteItem(planId, itemText: item.displayText) }

    /// Show item if it has venue-specific priority OR if it's a reference item (no venue columns)
    private var shouldShow: Bool {
        !item.displayText.isEmpty && (priority.isApplicable || item.isReferenceItem)
    }

    var body: some View {
        if shouldShow {
            Button {
                withAnimation(.snappy(duration: 0.2)) {
                    toggleItem()
                }
            } label: {
                itemContent
            }
            .buttonStyle(.plain)
            .sensoryFeedback(.selection, trigger: isSelected)
        }
    }
    
    private func toggleItem() {
        // Get the order sentence based on selected dose
        let orderSentence: String?
        if let options = item.dosing?.doseOptions, !options.isEmpty {
            orderSentence = options[selectedDoseIndex].orderSentence
        } else {
            orderSentence = item.dosing?.orderSentence
        }
        
        builder.toggle(
            itemText: item.displayText,
            planId: planId,
            planTitle: planTitle,
            section: "Treatment",
            subsection: subsection,
            priority: item.isReferenceItem ? .routine : priority,
            orderSentence: orderSentence,
            doseOptions: item.dosing?.doseOptions,
            selectedDoseIndex: item.dosing?.doseOptions?.isEmpty == false ? selectedDoseIndex : nil
        )
    }
    
    /// Select the item with a specific dose index (used for auto-select on dose pick)
    private func selectItemWithDose(_ doseIndex: Int) {
        let orderSentence: String?
        if let options = item.dosing?.doseOptions, !options.isEmpty {
            orderSentence = options[doseIndex].orderSentence
        } else {
            orderSentence = item.dosing?.orderSentence
        }
        
        builder.toggle(
            itemText: item.displayText,
            planId: planId,
            planTitle: planTitle,
            section: "Treatment",
            subsection: subsection,
            priority: item.isReferenceItem ? .routine : priority,
            orderSentence: orderSentence,
            doseOptions: item.dosing?.doseOptions,
            selectedDoseIndex: doseIndex
        )
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
                        Text(item.displayText)
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

                    // Show "REF" badge for reference items, otherwise show priority
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

                // Dose options (selectable for treatment)
                if let dosing = item.dosing, let options = dosing.doseOptions, !options.isEmpty {
                    if options.count <= 3 {
                        // For 1-3 options: show horizontal badges
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 6) {
                                ForEach(Array(options.enumerated()), id: \.offset) { index, option in
                                    SelectableDoseBadge(
                                        option: option,
                                        isSelected: index == selectedDoseIndex,
                                        onSelect: {
                                            withAnimation(.snappy(duration: 0.15)) {
                                                selectedDoseIndex = index
                                            }
                                            // Auto-select the medication when a dose is picked
                                            if !isSelected {
                                                withAnimation(.snappy(duration: 0.2)) {
                                                    selectItemWithDose(index)
                                                }
                                            }
                                        },
                                        onCopy: {
                                            if let sentence = option.orderSentence {
                                                UIPasteboard.general.string = sentence
                                                copiedSentence = true
                                                DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                                                    copiedSentence = false
                                                }
                                            }
                                        }
                                    )
                                }
                            }
                        }
                    } else {
                        // For 4+ options: use dropdown picker
                        DoseDropdownPicker(
                            options: options,
                            selectedIndex: $selectedDoseIndex,
                            onDoseSelected: { index in
                                // Auto-select the medication when a dose is picked from dropdown
                                if !isSelected {
                                    withAnimation(.snappy(duration: 0.2)) {
                                        selectItemWithDose(index)
                                    }
                                }
                            },
                            onCopy: { sentence in
                                UIPasteboard.general.string = sentence
                                copiedSentence = true
                                DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                                    copiedSentence = false
                                }
                            }
                        )
                    }
                    
                    // Show the order sentence for selected dose
                    if let sentence = options[selectedDoseIndex].orderSentence, !sentence.isEmpty {
                        Text(sentence)
                            .font(.system(.caption2, design: .monospaced))
                            .foregroundStyle(.teal.opacity(0.8))
                            .lineLimit(2)
                            .padding(.leading, 2)
                    }
                }

                // Show dosing string if no structured dosing (simple string dosing)
                if item.dosing == nil, let dosingStr = item.dosingString, !dosingStr.isEmpty {
                    HStack(spacing: 4) {
                        Image(systemName: "syringe.fill")
                            .font(.system(size: 9))
                        Text(dosingStr)
                            .font(.system(.caption, design: .monospaced, weight: .medium))
                    }
                    .foregroundStyle(.teal)
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
                        // Reference item fields
                        if let rationale = item.rationale, !rationale.isEmpty {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "lightbulb.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.yellow)
                                Text(rationale)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
                            }
                        }

                        if let range = item.therapeuticRange, !range.isEmpty {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "target")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.green)
                                Text("Range: \(range)")
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
                            }
                        }

                        if let notes = item.adjustmentNotes, !notes.isEmpty {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "doc.text.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.orange)
                                Text(notes)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
                            }
                        }

                        // Standard treatment item fields
                        if let indication = item.indication, !indication.isEmpty, indication != "-" {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "pill.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.teal)
                                Text(indication)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
                            }
                        }

                        if let instructions = item.dosing?.instructions, !instructions.isEmpty {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "info.circle.fill")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.blue)
                                Text(instructions)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.secondary)
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

                        if let monitoring = item.monitoring, !monitoring.isEmpty, monitoring != "-" {
                            HStack(alignment: .top, spacing: 6) {
                                Image(systemName: "chart.xyaxis.line")
                                    .font(.system(size: 10))
                                    .foregroundStyle(.purple)
                                Text(monitoring)
                                    .font(.system(.caption, design: .rounded))
                                    .foregroundStyle(.purple.opacity(0.8))
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
        // Reference item fields
        (item.rationale != nil && !(item.rationale?.isEmpty ?? true)) ||
        (item.therapeuticRange != nil && !(item.therapeuticRange?.isEmpty ?? true)) ||
        (item.adjustmentNotes != nil && !(item.adjustmentNotes?.isEmpty ?? true)) ||
        // Standard treatment fields
        (item.indication != nil && item.indication != "-" && !(item.indication?.isEmpty ?? true)) ||
        (item.dosing?.instructions != nil && !(item.dosing?.instructions?.isEmpty ?? true)) ||
        (item.contraindications != nil && item.contraindications != "-" && !(item.contraindications?.isEmpty ?? true)) ||
        (item.monitoring != nil && item.monitoring != "-" && !(item.monitoring?.isEmpty ?? true))
    }
}

// MARK: - Dose Dropdown Picker (for 4+ options)

struct DoseDropdownPicker: View {
    let options: [DoseOption]
    @Binding var selectedIndex: Int
    var onDoseSelected: ((Int) -> Void)? = nil
    var onCopy: ((String) -> Void)? = nil
    
    var body: some View {
        Menu {
            ForEach(Array(options.enumerated()), id: \.offset) { index, option in
                Button {
                    withAnimation(.snappy(duration: 0.15)) {
                        selectedIndex = index
                    }
                    // Notify parent that a dose was selected
                    onDoseSelected?(index)
                } label: {
                    HStack {
                        Text(option.text)
                        if index == selectedIndex {
                            Image(systemName: "checkmark")
                        }
                    }
                }
            }
            
            Divider()
            
            if let sentence = options[selectedIndex].orderSentence {
                Button {
                    onCopy?(sentence)
                } label: {
                    Label("Copy Order Sentence", systemImage: "doc.on.clipboard")
                }
            }
        } label: {
            HStack(spacing: 6) {
                Image(systemName: "syringe.fill")
                    .font(.system(size: 10))
                
                Text(options[selectedIndex].text)
                    .font(.system(.caption, design: .monospaced, weight: .medium))
                
                Spacer()
                
                Text("\(selectedIndex + 1)/\(options.count)")
                    .font(.system(size: 9, weight: .medium, design: .rounded))
                    .foregroundStyle(.teal.opacity(0.6))
                
                Image(systemName: "chevron.up.chevron.down")
                    .font(.system(size: 9))
            }
            .foregroundStyle(.teal)
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(.teal.opacity(0.1), in: RoundedRectangle(cornerRadius: 8))
            .overlay {
                RoundedRectangle(cornerRadius: 8)
                    .strokeBorder(.teal.opacity(0.3), lineWidth: 0.5)
            }
        }
        .buttonStyle(.plain)
        .sensoryFeedback(.selection, trigger: selectedIndex)
    }
}

// MARK: - Selectable Dose Badge

struct SelectableDoseBadge: View {
    let option: DoseOption
    let isSelected: Bool
    var onSelect: (() -> Void)? = nil
    var onCopy: (() -> Void)? = nil

    var body: some View {
        Button {
            onSelect?()
        } label: {
            HStack(spacing: 4) {
                if isSelected {
                    Image(systemName: "checkmark.circle.fill")
                        .font(.system(size: 9))
                } else {
                    Image(systemName: "circle")
                        .font(.system(size: 9))
                }
                Text(option.text)
                    .font(.system(.caption2, design: .monospaced, weight: .medium))
            }
            .foregroundStyle(isSelected ? .white : .teal)
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(isSelected ? .teal : .teal.opacity(0.1), in: Capsule())
            .overlay {
                Capsule()
                    .strokeBorder(isSelected ? .teal : .teal.opacity(0.3), lineWidth: isSelected ? 0 : 0.5)
            }
        }
        .buttonStyle(.plain)
        .sensoryFeedback(.selection, trigger: isSelected)
        .contextMenu {
            Button {
                onCopy?()
            } label: {
                Label("Copy Order Sentence", systemImage: "doc.on.clipboard")
            }
        }
    }
}

// MARK: - Legacy Dose Badge (for non-selectable contexts)

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
