import SwiftUI

struct SettingsView: View {
    @Environment(PlanStore.self) private var store
    @Environment(UserPreferences.self) private var prefs
    @Environment(EntitlementService.self) private var entitlement
    @Environment(ClinicalErrorService.self) private var errorService
    @State private var feedbackText = ""
    @State private var showFeedbackSent = false
    @State private var showPaywall = false
    @State private var showEmailVerification = false

    var body: some View {
        @Bindable var store = store
        NavigationStack {
            List {
                // Subscription Status
                Section {
                    SubscriptionStatusRow(onUpgrade: { showPaywall = true }, onVerifyEmail: { showEmailVerification = true })
                } header: {
                    Text("Subscription")
                }
                
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
                
                // Customize Layout
                Section {
                    NavigationLink {
                        CustomizeLayoutView()
                    } label: {
                        Label("Customize Layout", systemImage: "rectangle.3.group")
                    }
                } header: {
                    Text("Personalization")
                } footer: {
                    Text("Reorder sections on the Plans and Reference tabs.")
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

                // Clinical Error Reports
                Section {
                    SendAllReportsButton()
                } header: {
                    Text("Clinical Error Reports")
                } footer: {
                    Text("Send pending error reports to help us improve clinical accuracy.")
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
            .background { AdaptiveBackground() }
            .navigationTitle("Settings")
            .sheet(isPresented: $showPaywall) {
                PaywallView()
            }
            .sheet(isPresented: $showEmailVerification) {
                EmailVerificationView()
            }
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

// MARK: - Customize Layout View

struct CustomizeLayoutView: View {
    @Environment(UserPreferences.self) private var prefs
    
    var body: some View {
        List {
            // Plans Tab Sections
            Section {
                ForEach(prefs.plansSectionOrder, id: \.self) { sectionId in
                    HStack {
                        Image(systemName: plansSectionIcon(sectionId))
                            .foregroundStyle(plansSectionColor(sectionId))
                            .frame(width: 24)
                        Text(plansSectionName(sectionId))
                        Spacer()
                        Image(systemName: "line.3.horizontal")
                            .foregroundStyle(.tertiary)
                    }
                }
                .onMove { source, destination in
                    prefs.plansSectionOrder.move(fromOffsets: source, toOffset: destination)
                }
            } header: {
                Text("Plans Tab")
            } footer: {
                Text("Drag to reorder sections on the Plans tab.")
            }
            
            // Reference Tab Sections
            Section {
                ForEach(prefs.referenceSectionOrder, id: \.self) { sectionId in
                    HStack {
                        Image(systemName: referenceSectionIcon(sectionId))
                            .foregroundStyle(referenceSectionColor(sectionId))
                            .frame(width: 24)
                        Text(referenceSectionName(sectionId))
                        Spacer()
                        Image(systemName: "line.3.horizontal")
                            .foregroundStyle(.tertiary)
                    }
                }
                .onMove { source, destination in
                    prefs.referenceSectionOrder.move(fromOffsets: source, toOffset: destination)
                }
            } header: {
                Text("Reference Tab")
            } footer: {
                Text("Drag to reorder sections on the Reference tab.")
            }
            
            // Reset Button
            Section {
                Button(role: .destructive) {
                    withAnimation {
                        prefs.plansSectionOrder = UserPreferences.defaultPlansSectionOrder
                        prefs.referenceSectionOrder = UserPreferences.defaultReferenceSectionOrder
                    }
                } label: {
                    Label("Reset to Default Order", systemImage: "arrow.counterclockwise")
                }
            }
        }
        .listStyle(.insetGrouped)
        .scrollContentBackground(.hidden)
        .background { AdaptiveBackground() }
        .navigationTitle("Customize Layout")
        .navigationBarTitleDisplayMode(.inline)
        .environment(\.editMode, .constant(.active))
    }
    
    // MARK: - Plans Section Helpers
    
    private func plansSectionName(_ id: String) -> String {
        switch id {
        case "recents": "Recent Plans"
        case "favorites": "Favorites"
        case "categories": "Categories"
        default: id.capitalized
        }
    }
    
    private func plansSectionIcon(_ id: String) -> String {
        switch id {
        case "recents": "clock.fill"
        case "favorites": "star.fill"
        case "categories": "folder.fill"
        default: "square.fill"
        }
    }
    
    private func plansSectionColor(_ id: String) -> Color {
        switch id {
        case "recents": .blue
        case "favorites": .yellow
        case "categories": .purple
        default: .gray
        }
    }
    
    // MARK: - Reference Section Helpers
    
    private func referenceSectionName(_ id: String) -> String {
        switch id {
        case "examTools": "Exam Tools"
        case "scales": "Clinical Scales"
        case "exams": "Examinations"
        case "tools": "Tools & Calculators"
        default: id.capitalized
        }
    }
    
    private func referenceSectionIcon(_ id: String) -> String {
        switch id {
        case "examTools": "hand.point.up.left.fill"
        case "scales": "chart.bar.fill"
        case "exams": "stethoscope"
        case "tools": "function"
        default: "square.fill"
        }
    }
    
    private func referenceSectionColor(_ id: String) -> Color {
        switch id {
        case "examTools": .orange
        case "scales": .blue
        case "exams": .teal
        case "tools": .purple
        default: .gray
        }
    }
}

// MARK: - Subscription Status Row

private struct SubscriptionStatusRow: View {
    @Environment(EntitlementService.self) private var entitlement
    let onUpgrade: () -> Void
    let onVerifyEmail: () -> Void
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Status badge
            HStack {
                Image(systemName: entitlement.accessLevel.icon)
                    .foregroundStyle(entitlement.accessLevel.color)
                Text(entitlement.accessLevel.displayName)
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                Spacer()
            }
            
            // Status-specific content
            switch entitlement.accessLevel {
            case .loading:
                ProgressView()
                    .frame(maxWidth: .infinity, alignment: .center)
                
            case .trial(let days):
                VStack(alignment: .leading, spacing: 8) {
                    Text("You have \(days) day\(days == 1 ? "" : "s") remaining in your free trial.")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    
                    HStack(spacing: 12) {
                        Button {
                            onUpgrade()
                        } label: {
                            Text("Subscribe")
                                .font(.system(.caption, design: .rounded, weight: .semibold))
                                .foregroundStyle(.white)
                                .padding(.horizontal, 16)
                                .padding(.vertical, 8)
                                .background(AppTheme.teal, in: Capsule())
                        }
                        
                        Button {
                            onVerifyEmail()
                        } label: {
                            Text("Team Member?")
                                .font(.system(.caption, design: .rounded, weight: .medium))
                                .foregroundStyle(.purple)
                        }
                    }
                }
                
            case .subscribed(let expiration):
                VStack(alignment: .leading, spacing: 4) {
                    Text("Thank you for subscribing!")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    if let exp = expiration {
                        Text("Renews \(exp.formatted(date: .abbreviated, time: .omitted))")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }
                    
                    Button {
                        // Open subscription management
                        if let url = URL(string: "https://apps.apple.com/account/subscriptions") {
                            UIApplication.shared.open(url)
                        }
                    } label: {
                        Text("Manage Subscription")
                            .font(.system(.caption, design: .rounded, weight: .medium))
                            .foregroundStyle(.blue)
                    }
                    .padding(.top, 4)
                }
                
            case .whitelisted(let email):
                VStack(alignment: .leading, spacing: 4) {
                    Text("Free access with \(email)")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    
                    Button {
                        entitlement.clearVerifiedEmail()
                    } label: {
                        Text("Remove Team Email")
                            .font(.system(.caption2, design: .rounded))
                            .foregroundStyle(.red.opacity(0.8))
                    }
                    .padding(.top, 4)
                }
                
            case .errorReward(let expiration):
                VStack(alignment: .leading, spacing: 4) {
                    HStack(spacing: 6) {
                        Image(systemName: "gift.fill")
                            .foregroundStyle(.yellow)
                        Text("Thank you for your feedback!")
                            .font(.caption)
                    }
                    Text("Free access until \(expiration.formatted(date: .abbreviated, time: .omitted))")
                        .font(.caption2)
                        .foregroundStyle(.secondary)
                    Text("Your clinical error report helps improve accuracy for everyone.")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                }
                
            case .expired:
                VStack(alignment: .leading, spacing: 8) {
                    Text("Your trial has ended. Subscribe to continue using all features.")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    
                    HStack(spacing: 12) {
                        Button {
                            onUpgrade()
                        } label: {
                            Text("Subscribe Now")
                                .font(.system(.caption, design: .rounded, weight: .semibold))
                                .foregroundStyle(.white)
                                .padding(.horizontal, 16)
                                .padding(.vertical, 8)
                                .background(AppTheme.teal, in: Capsule())
                        }
                        
                        Button {
                            onVerifyEmail()
                        } label: {
                            Text("Team Member?")
                                .font(.system(.caption, design: .rounded, weight: .medium))
                                .foregroundStyle(.purple)
                        }
                    }
                }
            }
        }
        .padding(.vertical, 4)
    }
}

#Preview {
    SettingsView()
        .environment(PlanStore())
        .environment(UserPreferences())
        .environment(EntitlementService())
        .environment(SubscriptionService())
        .environment(ClinicalErrorService())
}
