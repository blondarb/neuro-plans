import SwiftUI

struct PlanRequestView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var requestText = ""
    @State private var submitState: SubmitState = .idle

    private enum SubmitState {
        case idle
        case submitting
        case success
        case error(String)

        var isSubmitting: Bool {
            if case .submitting = self { return true }
            return false
        }

        var isSuccess: Bool {
            if case .success = self { return true }
            return false
        }
    }

    /// Rate limit: 1 submission per 7 days
    private var isRateLimited: Bool {
        guard let lastSubmission = UserDefaults.standard.object(forKey: "lastPlanRequestDate") as? Date else {
            return false
        }
        let sevenDays: TimeInterval = 7 * 24 * 60 * 60
        return Date().timeIntervalSince(lastSubmission) < sevenDays
    }

    private var canSubmit: Bool {
        !requestText.trimmingCharacters(in: .whitespaces).isEmpty
        && !submitState.isSubmitting
        && !isRateLimited
    }

    var body: some View {
        NavigationStack {
            Form {
                if submitState.isSuccess {
                    successSection
                } else {
                    requestSection

                    if isRateLimited {
                        rateLimitSection
                    }

                    if case .error(let message) = submitState {
                        errorSection(message)
                    }
                }
            }
            .scrollContentBackground(.hidden)
            .background { AdaptiveBackground() }
            .navigationTitle("Request a Plan")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
    }

    // MARK: - Sections

    private var requestSection: some View {
        Section {
            TextField(
                "e.g., Cardiac amyloidosis screening protocol",
                text: $requestText,
                axis: .vertical
            )
            .lineLimit(3...6)

            Button {
                submit()
            } label: {
                HStack {
                    if submitState.isSubmitting {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(submitState.isSubmitting ? "Submitting..." : "Submit Request")
                }
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.white)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 10)
                .background(
                    AppTheme.teal,
                    in: RoundedRectangle(cornerRadius: 10)
                )
            }
            .buttonStyle(.plain)
            .disabled(!canSubmit)
            .opacity(canSubmit ? 1.0 : 0.5)
        } header: {
            Text("What plan would you like us to add?")
        } footer: {
            Text("Describe the clinical plan or protocol you'd like to see in the app.")
        }
    }

    private var successSection: some View {
        Section {
            VStack(spacing: 12) {
                Image(systemName: "checkmark.circle.fill")
                    .font(.system(size: 44))
                    .foregroundStyle(.green)

                Text("Thank you!")
                    .font(.system(.headline, design: .rounded, weight: .bold))

                Text("We review requests monthly and prioritize by demand.")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 20)
        }
    }

    private var rateLimitSection: some View {
        Section {
            Label(
                "You can submit another request in a few days.",
                systemImage: "clock.fill"
            )
            .font(.caption)
            .foregroundStyle(.secondary)
        }
    }

    private func errorSection(_ message: String) -> some View {
        Section {
            VStack(alignment: .leading, spacing: 8) {
                Label(message, systemImage: "exclamationmark.triangle.fill")
                    .font(.caption)
                    .foregroundStyle(.red)

                Button {
                    submit()
                } label: {
                    Label("Retry", systemImage: "arrow.clockwise")
                        .font(.system(.caption, design: .rounded, weight: .semibold))
                }
            }
        }
    }

    // MARK: - Submit

    private func submit() {
        submitState = .submitting
        Task {
            do {
                try await SupabaseService.submitPlanRequest(text: requestText.trimmingCharacters(in: .whitespaces))
                UserDefaults.standard.set(Date(), forKey: "lastPlanRequestDate")
                await MainActor.run {
                    withAnimation {
                        submitState = .success
                    }
                }
            } catch {
                await MainActor.run {
                    submitState = .error("Failed to submit. Please check your connection and try again.")
                }
            }
        }
    }
}

#Preview {
    PlanRequestView()
}
