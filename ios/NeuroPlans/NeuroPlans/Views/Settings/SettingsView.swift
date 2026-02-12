import SwiftUI

struct SettingsView: View {
    @Environment(PlanStore.self) private var store
    @State private var feedbackText = ""
    @State private var showFeedbackSent = false

    var body: some View {
        @Bindable var store = store
        NavigationStack {
            List {
                // Default Setting
                Section {
                    Picker("Default Setting", selection: $store.selectedSetting) {
                        ForEach(ClinicalSetting.allCases) { setting in
                            Label(setting.label, systemImage: setting.icon)
                                .tag(setting)
                        }
                    }
                } header: {
                    Text("Clinical Setting")
                } footer: {
                    Text("Plans will filter to show items relevant to this care setting.")
                }

                // Stats
                Section("Database") {
                    HStack {
                        Label("Total Plans", systemImage: "doc.text.fill")
                        Spacer()
                        Text("\(store.plans.count)")
                            .foregroundStyle(.secondary)
                    }

                    HStack {
                        Label("Categories", systemImage: "folder.fill")
                        Spacer()
                        Text("\(PlanCategory.all.count)")
                            .foregroundStyle(.secondary)
                    }

                    HStack {
                        Label("Favorites", systemImage: "star.fill")
                        Spacer()
                        Text("\(store.favorites.count)")
                            .foregroundStyle(.secondary)
                    }
                }

                // Feedback
                Section("Feedback") {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Help us improve")
                            .font(.system(.subheadline, weight: .medium))
                        TextField("Share your feedback...", text: $feedbackText, axis: .vertical)
                            .lineLimit(3...6)
                            .textFieldStyle(.roundedBorder)

                        Button {
                            // Save feedback locally for now
                            saveFeedback()
                        } label: {
                            Label(
                                showFeedbackSent ? "Sent!" : "Send Feedback",
                                systemImage: showFeedbackSent ? "checkmark.circle.fill" : "paperplane.fill"
                            )
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                            .foregroundStyle(.white)
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 10)
                            .background(
                                showFeedbackSent ? Color.green : AppTheme.teal,
                                in: RoundedRectangle(cornerRadius: 10)
                            )
                        }
                        .disabled(feedbackText.trimmingCharacters(in: .whitespaces).isEmpty)
                    }
                }

                // About
                Section("About") {
                    HStack {
                        Label("Version", systemImage: "info.circle")
                        Spacer()
                        Text("1.0.0")
                            .foregroundStyle(.secondary)
                    }

                    HStack {
                        Label("Data Version", systemImage: "cylinder.fill")
                        Spacer()
                        Text("Feb 2026")
                            .foregroundStyle(.secondary)
                    }

                    Label("Evidence-based clinical decision support for neurological diagnoses", systemImage: "brain.fill")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .listStyle(.insetGrouped)
            .scrollContentBackground(.hidden)
            .background(LinearGradient.appBackground.ignoresSafeArea())
            .navigationTitle("Settings")
        }
    }

    private func saveFeedback() {
        // Store feedback locally; could connect to backend later
        var existing = UserDefaults.standard.stringArray(forKey: "feedback") ?? []
        let entry = "[\(Date().formatted())]: \(feedbackText)"
        existing.append(entry)
        UserDefaults.standard.set(existing, forKey: "feedback")

        withAnimation {
            showFeedbackSent = true
            feedbackText = ""
        }
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            withAnimation { showFeedbackSent = false }
        }
    }
}

#Preview {
    SettingsView()
        .environment(PlanStore())
}
