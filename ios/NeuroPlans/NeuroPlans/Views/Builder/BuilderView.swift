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
            .background(LinearGradient.appBackground.ignoresSafeArea())
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
        VStack(spacing: 16) {
            Spacer()
            Image(systemName: "square.and.pencil")
                .font(.system(size: 48))
                .foregroundStyle(.tertiary)
            Text("No Items Selected")
                .font(AppTheme.titleFont)
                .foregroundStyle(.secondary)
            Text("Browse a plan and tap items to add them here")
                .font(AppTheme.bodyFont)
                .foregroundStyle(.tertiary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 40)
            Spacer()
        }
    }

    // MARK: - Builder Content

    private var builderContent: some View {
        @Bindable var builder = builder
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

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack(spacing: 8) {
                PriorityBadge(priority: item.priority)

                Text(item.displayText)
                    .font(.system(.subheadline, weight: .medium))
                    .lineLimit(3)
            }

            if let order = item.orderSentence, !order.isEmpty {
                Text(order)
                    .font(.system(.caption2, design: .monospaced))
                    .foregroundStyle(.teal.opacity(0.7))
                    .lineLimit(2)
            }

            Text(item.subsection)
                .font(.system(size: 10))
                .foregroundStyle(.tertiary)
        }
        .padding(.vertical, 2)
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
