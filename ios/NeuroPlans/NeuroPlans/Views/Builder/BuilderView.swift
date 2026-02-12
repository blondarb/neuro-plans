import SwiftUI

struct BuilderView: View {
    @Environment(PlanBuilder.self) private var builder
    @State private var showExportSheet = false
    @State private var showClearConfirm = false

    var body: some View {
        NavigationStack {
            Group {
                if builder.isEmpty {
                    emptyState
                } else {
                    builderContent
                }
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Plan Builder")
            .toolbar {
                if !builder.isEmpty {
                    ToolbarItem(placement: .topBarTrailing) {
                        Menu {
                            Button {
                                showExportSheet = true
                            } label: {
                                Label("Share Plan", systemImage: "square.and.arrow.up")
                            }

                            Button {
                                UIPasteboard.general.string = builder.exportAsText()
                            } label: {
                                Label("Copy to Clipboard", systemImage: "doc.on.clipboard")
                            }

                            Divider()

                            Button(role: .destructive) {
                                showClearConfirm = true
                            } label: {
                                Label("Clear All", systemImage: "trash")
                            }
                        } label: {
                            Image(systemName: "ellipsis.circle")
                        }
                    }
                }
            }
            .sheet(isPresented: $showExportSheet) {
                ShareSheet(text: builder.exportAsText())
            }
            .confirmationDialog(
                "Clear all selected items?",
                isPresented: $showClearConfirm,
                titleVisibility: .visible
            ) {
                Button("Clear All", role: .destructive) {
                    withAnimation { builder.clearAll() }
                }
            }
        }
    }

    // MARK: - Empty State

    private var emptyState: some View {
        ScrollView {
            VStack(spacing: 24) {
                Spacer(minLength: 40)
                
                // Icon
                Image(systemName: "square.and.pencil")
                    .font(.system(size: 56))
                    .foregroundStyle(AppTheme.teal.opacity(0.6))
                
                // Title
                Text("Plan Builder")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                
                Text("Create a custom clinical plan by combining items from different diagnoses")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
                
                // Instructions
                VStack(alignment: .leading, spacing: 16) {
                    InstructionRow(
                        step: "1",
                        icon: "magnifyingglass",
                        title: "Browse Plans",
                        description: "Go to the Plans tab and select a diagnosis"
                    )
                    
                    InstructionRow(
                        step: "2",
                        icon: "hand.tap.fill",
                        title: "Tap to Add",
                        description: "Tap any lab, imaging, treatment, or recommendation to add it here"
                    )
                    
                    InstructionRow(
                        step: "3",
                        icon: "note.text.badge.plus",
                        title: "Add Notes",
                        description: "Tap the note icon to add custom instructions to any item"
                    )
                    
                    InstructionRow(
                        step: "4",
                        icon: "square.and.arrow.up",
                        title: "Share or Copy",
                        description: "Export your compiled plan to paste into your EMR"
                    )
                }
                .padding(20)
                .background(Color.white.opacity(0.05))
                .clipShape(RoundedRectangle(cornerRadius: 16))
                .padding(.horizontal, 20)
                
                Spacer(minLength: 60)
            }
        }
    }

    // MARK: - Builder Content

    @ViewBuilder
    private var builderContent: some View {
        let builder = builder
        List {
            // Header
            Section {
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        if !builder.activePlanTitle.isEmpty {
                            Text(builder.activePlanTitle)
                                .font(.system(.headline, design: .rounded, weight: .bold))
                        }
                        Text("\(builder.itemCount) items selected")
                            .font(.system(.subheadline, design: .rounded))
                            .foregroundStyle(.secondary)
                    }
                    Spacer()

                    Button {
                        showExportSheet = true
                    } label: {
                        Label("Share", systemImage: "square.and.arrow.up")
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(AppTheme.teal, in: Capsule())
                    }
                }
            }
            .listRowBackground(Color.clear)

            // Grouped items
            ForEach(builder.groupedItems, id: \.section) { group in
                Section {
                    ForEach(group.items) { item in
                        SelectedItemCard(item: item)
                            .swipeActions(edge: .trailing) {
                                Button(role: .destructive) {
                                    withAnimation { builder.remove(item) }
                                } label: {
                                    Label("Remove", systemImage: "trash")
                                }
                            }
                    }
                    .onMove { source, dest in
                        // Note: move only works within section
                    }
                } header: {
                    HStack(spacing: 6) {
                        sectionIcon(for: group.section)
                        Text(group.section)
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        Spacer()
                        Text("\(group.items.count)")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }
                }
                .listRowBackground(Color.white.opacity(0.05))
            }
        }
        .listStyle(.insetGrouped)
        .scrollContentBackground(.hidden)
    }

    private func sectionIcon(for section: String) -> some View {
        let icon: String = switch section {
        case "Laboratory Workup": "testtube.2"
        case "Imaging & Studies": "photo.artframe"
        case "Treatment": "pill.fill"
        case "Other Recommendations": "text.badge.checkmark"
        default: "doc.text"
        }
        return Image(systemName: icon)
            .font(.system(size: 12))
            .foregroundStyle(AppTheme.teal)
    }
}

// MARK: - Selected Item Card

struct SelectedItemCard: View {
    let item: SelectedItem
    @Environment(PlanBuilder.self) private var builder
    @State private var isEditingNote = false
    @State private var noteText: String = ""

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(spacing: 8) {
                PriorityBadge(priority: item.priority)

                Text(item.displayText)
                    .font(.system(.subheadline, weight: .medium))
                    .lineLimit(3)

                Spacer()

                // Add note button
                Button {
                    noteText = item.customNote ?? ""
                    isEditingNote = true
                } label: {
                    Image(systemName: item.hasCustomNote ? "note.text" : "note.text.badge.plus")
                        .font(.system(size: 14))
                        .foregroundStyle(item.hasCustomNote ? .orange : .gray.opacity(0.5))
                }
                .buttonStyle(.plain)
            }

            // Dose picker dropdown for items with multiple dose options
            if let options = item.doseOptions, !options.isEmpty {
                DosePickerView(item: item, options: options)
            } else if let order = item.currentOrderSentence, !order.isEmpty {
                // Show static order sentence if no options
                Text(order)
                    .font(.system(.caption2, design: .monospaced))
                    .foregroundStyle(.teal.opacity(0.7))
                    .lineLimit(2)
            }

            // Show custom note if exists
            if let note = item.customNote, !note.isEmpty {
                HStack(alignment: .top, spacing: 4) {
                    Image(systemName: "note.text")
                        .font(.system(size: 10))
                        .foregroundStyle(.orange)
                    Text(note)
                        .font(.system(.caption, design: .rounded))
                        .foregroundStyle(.orange.opacity(0.9))
                        .italic()
                }
                .padding(.top, 2)
            }

            Text(item.subsection)
                .font(.system(size: 10))
                .foregroundStyle(.tertiary)
        }
        .padding(.vertical, 2)
        .alert("Add Note", isPresented: $isEditingNote) {
            TextField("Enter note...", text: $noteText)
            Button("Save") {
                builder.updateNote(for: item.id, note: noteText)
            }
            Button("Clear", role: .destructive) {
                builder.updateNote(for: item.id, note: nil)
            }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("Add a custom note to \"\(item.itemText.prefix(30))...\"")
        }
    }
}

// MARK: - Dose Picker View

struct DosePickerView: View {
    let item: SelectedItem
    let options: [DoseOption]
    @Environment(PlanBuilder.self) private var builder
    
    private var selectedIndex: Int {
        item.selectedDoseIndex ?? 0
    }
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            // Dropdown picker
            Menu {
                ForEach(Array(options.enumerated()), id: \.offset) { index, option in
                    Button {
                        builder.updateSelectedDose(for: item.id, doseIndex: index)
                    } label: {
                        HStack {
                            Text(option.text)
                            if index == selectedIndex {
                                Image(systemName: "checkmark")
                            }
                        }
                    }
                }
            } label: {
                HStack(spacing: 6) {
                    Image(systemName: "syringe.fill")
                        .font(.system(size: 10))
                    
                    Text(options[selectedIndex].text)
                        .font(.system(.caption, design: .monospaced, weight: .medium))
                    
                    Image(systemName: "chevron.up.chevron.down")
                        .font(.system(size: 8))
                }
                .foregroundStyle(.teal)
                .padding(.horizontal, 10)
                .padding(.vertical, 6)
                .background(.teal.opacity(0.1), in: RoundedRectangle(cornerRadius: 8))
                .overlay {
                    RoundedRectangle(cornerRadius: 8)
                        .strokeBorder(.teal.opacity(0.3), lineWidth: 0.5)
                }
            }
            .buttonStyle(.plain)
            
            // Show the order sentence for the selected dose
            if let sentence = options[selectedIndex].orderSentence, !sentence.isEmpty {
                Text(sentence)
                    .font(.system(.caption2, design: .monospaced))
                    .foregroundStyle(.teal.opacity(0.7))
                    .lineLimit(3)
            }
        }
    }
}

// MARK: - Instruction Row

private struct InstructionRow: View {
    let step: String
    let icon: String
    let title: String
    let description: String
    
    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            // Step number
            Text(step)
                .font(.system(.caption, design: .rounded, weight: .bold))
                .foregroundStyle(.white)
                .frame(width: 24, height: 24)
                .background(AppTheme.teal)
                .clipShape(Circle())
            
            // Content
            VStack(alignment: .leading, spacing: 4) {
                HStack(spacing: 6) {
                    Image(systemName: icon)
                        .font(.system(size: 14))
                        .foregroundStyle(AppTheme.teal)
                    Text(title)
                        .font(.system(.subheadline, design: .rounded, weight: .semibold))
                }
                Text(description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
    }
}

// MARK: - Share Sheet

struct ShareSheet: UIViewControllerRepresentable {
    let text: String

    func makeUIViewController(context: Context) -> UIActivityViewController {
        UIActivityViewController(activityItems: [text], applicationActivities: nil)
    }

    func updateUIViewController(_ uiViewController: UIActivityViewController, context: Context) {}
}
