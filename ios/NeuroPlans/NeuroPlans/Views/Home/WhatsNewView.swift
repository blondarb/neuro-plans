import SwiftUI

struct WhatsNewView: View {
    @Environment(PlanStore.self) private var store
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    // Header
                    VStack(spacing: 8) {
                        Text("What's New")
                            .font(.system(.title, design: .rounded, weight: .bold))
                        if let changelog = store.changelog {
                            Text(changelog.date)
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                        }
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.top, 12)

                    // Stats bar
                    if let stats = store.changelog?.stats {
                        HStack(spacing: 16) {
                            StatBadge(value: "\(stats.totalPlans)", label: "Total Plans")
                            if stats.newPlans > 0 {
                                StatBadge(value: "+\(stats.newPlans)", label: "New", color: .green)
                            }
                            if stats.updatedPlans > 0 {
                                StatBadge(value: "\(stats.updatedPlans)", label: "Updated", color: .blue)
                            }
                        }
                        .frame(maxWidth: .infinity)
                    }

                    // New plans
                    if let entries = store.changelog?.entries.filter({ $0.type == "new" }),
                       !entries.isEmpty {
                        VStack(alignment: .leading, spacing: 12) {
                            Label("New Plans", systemImage: "plus.circle.fill")
                                .font(.system(.headline, design: .rounded))
                                .foregroundStyle(.green)

                            ForEach(entries) { entry in
                                HStack {
                                    VStack(alignment: .leading, spacing: 2) {
                                        Text(entry.title)
                                            .font(.system(.body, design: .rounded, weight: .medium))
                                        if let category = entry.category {
                                            Text(category)
                                                .font(.caption)
                                                .foregroundStyle(.secondary)
                                        }
                                    }
                                    Spacer()
                                    Image(systemName: "chevron.right")
                                        .font(.caption)
                                        .foregroundStyle(.tertiary)
                                }
                                .padding(.vertical, 4)
                            }
                        }
                        .padding(.horizontal)
                    }

                    // Updated plans
                    if let entries = store.changelog?.entries.filter({ $0.type == "updated" }),
                       !entries.isEmpty {
                        VStack(alignment: .leading, spacing: 12) {
                            Label("Updated Plans", systemImage: "arrow.triangle.2.circlepath.circle.fill")
                                .font(.system(.headline, design: .rounded))
                                .foregroundStyle(.blue)

                            ForEach(entries) { entry in
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(entry.title)
                                        .font(.system(.body, design: .rounded, weight: .medium))
                                    if let summary = entry.summary {
                                        Text(summary)
                                            .font(.caption)
                                            .foregroundStyle(.secondary)
                                    }
                                }
                                .padding(.vertical, 4)
                            }
                        }
                        .padding(.horizontal)
                    }
                }
                .padding(.bottom, 40)
            }
            .background { AdaptiveBackground() }
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") {
                        store.markChangelogSeen()
                        dismiss()
                    }
                }
            }
        }
    }
}

// MARK: - Stat Badge

private struct StatBadge: View {
    let value: String
    let label: String
    var color: Color = .primary

    var body: some View {
        VStack(spacing: 2) {
            Text(value)
                .font(.system(.title3, design: .rounded, weight: .bold))
                .foregroundStyle(color)
            Text(label)
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
        .frame(minWidth: 60)
        .padding(.vertical, 8)
        .padding(.horizontal, 12)
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 10))
    }
}
