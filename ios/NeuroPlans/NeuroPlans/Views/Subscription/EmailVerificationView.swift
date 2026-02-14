import SwiftUI

struct EmailVerificationView: View {
    @Environment(EntitlementService.self) private var entitlement
    @Environment(\.dismiss) private var dismiss

    @State private var email = ""
    @State private var otpCode = ""
    @State private var verificationState: VerificationState = .enterEmail
    @State private var resendCooldown = 0
    @FocusState private var isEmailFocused: Bool
    @FocusState private var isCodeFocused: Bool

    enum VerificationState: Equatable {
        case enterEmail
        case sendingCode
        case enterCode(email: String)
        case verifyingCode
        case success
        case notWhitelisted(email: String)
        case failure(String)
    }

    var body: some View {
        NavigationStack {
            VStack(spacing: 24) {
                Spacer()

                switch verificationState {
                case .enterEmail, .sendingCode, .failure:
                    emailEntryContent
                case .enterCode, .verifyingCode:
                    codeEntryContent
                case .success:
                    successContent
                case .notWhitelisted:
                    notWhitelistedContent
                }

                Spacer()
                Spacer()
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Email Verification")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Cancel") {
                        dismiss()
                    }
                }
            }
            .onAppear {
                isEmailFocused = true
            }
        }
    }

    // MARK: - Email Entry (Step 1)

    private var emailEntryContent: some View {
        VStack(spacing: 24) {
            // Header
            VStack(spacing: 16) {
                ZStack {
                    Circle()
                        .fill(.purple.opacity(0.15))
                        .frame(width: 80, height: 80)

                    Image(systemName: "envelope.badge.fill")
                        .font(.system(size: 36))
                        .foregroundStyle(.purple)
                }

                Text("Verify Your Email")
                    .font(.system(.title2, design: .rounded, weight: .bold))

                Text("Some organizations provide complimentary access to Neuro Plans.")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)
            }

            // Email input
            VStack(alignment: .leading, spacing: 8) {
                Text("Email Address")
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                    .foregroundStyle(.secondary)

                HStack {
                    Image(systemName: "envelope.fill")
                        .foregroundStyle(.secondary)

                    TextField("you@example.com", text: $email)
                        .textContentType(.emailAddress)
                        .keyboardType(.emailAddress)
                        .autocorrectionDisabled()
                        .textInputAutocapitalization(.never)
                        .focused($isEmailFocused)
                }
                .padding()
                .background {
                    RoundedRectangle(cornerRadius: 12)
                        .fill(Color.white.opacity(0.05))
                        .overlay {
                            RoundedRectangle(cornerRadius: 12)
                                .strokeBorder(
                                    isEmailFocused ? AppTheme.teal : Color.white.opacity(0.1),
                                    lineWidth: 1
                                )
                        }
                }

                HStack(spacing: 4) {
                    Image(systemName: "info.circle")
                        .font(.system(size: 10))
                    Text("Enter your email to check eligibility")
                        .font(.caption2)
                }
                .foregroundStyle(.tertiary)
            }
            .padding(.horizontal)

            // Error message
            if case .failure(let message) = verificationState {
                HStack {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.red)
                    Text(message)
                        .font(.subheadline)
                }
                .foregroundStyle(.red)
                .padding()
                .background(.red.opacity(0.1), in: RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal)
            }

            // Send code button
            Button {
                Task { await sendCode() }
            } label: {
                HStack {
                    if case .sendingCode = verificationState {
                        ProgressView()
                            .tint(.white)
                    } else {
                        Text("Send Verification Code")
                    }
                }
                .font(.system(.headline, design: .rounded, weight: .semibold))
                .foregroundStyle(.white)
                .frame(maxWidth: .infinity)
                .padding()
                .background(
                    isValidEmailFormat ? AppTheme.teal : Color.gray,
                    in: RoundedRectangle(cornerRadius: 14)
                )
            }
            .disabled(!isValidEmailFormat || verificationState == .sendingCode)
            .padding(.horizontal)
        }
    }

    // MARK: - Code Entry (Step 2)

    private var codeEntryContent: some View {
        VStack(spacing: 24) {
            // Header
            VStack(spacing: 16) {
                ZStack {
                    Circle()
                        .fill(.purple.opacity(0.15))
                        .frame(width: 80, height: 80)

                    Image(systemName: "lock.shield.fill")
                        .font(.system(size: 36))
                        .foregroundStyle(.purple)
                }

                Text("Enter Verification Code")
                    .font(.system(.title2, design: .rounded, weight: .bold))

                if case .enterCode(let sentEmail) = verificationState {
                    Text("We sent a 6-digit code to **\(sentEmail)**")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                }
            }

            // Code input
            VStack(alignment: .leading, spacing: 8) {
                Text("Verification Code")
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                    .foregroundStyle(.secondary)

                HStack {
                    Image(systemName: "number")
                        .foregroundStyle(.secondary)

                    TextField("000000", text: $otpCode)
                        .textContentType(.oneTimeCode)
                        .keyboardType(.numberPad)
                        .focused($isCodeFocused)
                        .font(.system(.title3, design: .monospaced, weight: .semibold))
                        .onChange(of: otpCode) { _, newValue in
                            // Limit to 6 digits
                            let filtered = newValue.filter { $0.isNumber }
                            if filtered.count > 6 {
                                otpCode = String(filtered.prefix(6))
                            } else {
                                otpCode = filtered
                            }
                        }
                }
                .padding()
                .background {
                    RoundedRectangle(cornerRadius: 12)
                        .fill(Color.white.opacity(0.05))
                        .overlay {
                            RoundedRectangle(cornerRadius: 12)
                                .strokeBorder(
                                    isCodeFocused ? AppTheme.teal : Color.white.opacity(0.1),
                                    lineWidth: 1
                                )
                        }
                }

                // Resend code link
                HStack {
                    Spacer()
                    Button {
                        Task { await resendCode() }
                    } label: {
                        Text(resendCooldown > 0 ? "Resend code in \(resendCooldown)s" : "Resend Code")
                            .font(.caption)
                            .foregroundColor(resendCooldown > 0 ? .gray : .purple)
                    }
                    .disabled(resendCooldown > 0)
                }
            }
            .padding(.horizontal)

            // Verify button
            Button {
                Task { await verifyCode() }
            } label: {
                HStack {
                    if case .verifyingCode = verificationState {
                        ProgressView()
                            .tint(.white)
                    } else {
                        Text("Verify")
                    }
                }
                .font(.system(.headline, design: .rounded, weight: .semibold))
                .foregroundStyle(.white)
                .frame(maxWidth: .infinity)
                .padding()
                .background(
                    otpCode.count == 6 ? AppTheme.teal : Color.gray,
                    in: RoundedRectangle(cornerRadius: 14)
                )
            }
            .disabled(otpCode.count != 6 || verificationState == .verifyingCode)
            .padding(.horizontal)

            // Back button
            Button {
                verificationState = .enterEmail
                otpCode = ""
            } label: {
                Text("Use a different email")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
        .onAppear {
            isCodeFocused = true
            startResendCooldown()
        }
    }

    // MARK: - Success

    private var successContent: some View {
        VStack(spacing: 20) {
            ZStack {
                Circle()
                    .fill(.green.opacity(0.15))
                    .frame(width: 80, height: 80)

                Image(systemName: "checkmark.circle.fill")
                    .font(.system(size: 48))
                    .foregroundStyle(.green)
            }

            Text("Email Verified!")
                .font(.system(.title2, design: .rounded, weight: .bold))

            Text("You now have complimentary access to Neuro Plans.")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal)
        }
    }

    // MARK: - Not Whitelisted

    private var notWhitelistedContent: some View {
        VStack(spacing: 20) {
            ZStack {
                Circle()
                    .fill(.blue.opacity(0.15))
                    .frame(width: 80, height: 80)

                Image(systemName: "info.circle.fill")
                    .font(.system(size: 48))
                    .foregroundStyle(.blue)
            }

            Text("Email Verified")
                .font(.system(.title2, design: .rounded, weight: .bold))

            Text("Your email was verified, but your organization does not currently have complimentary access. You can subscribe to get full access.")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal)

            VStack(spacing: 12) {
                Button {
                    dismiss()
                    // The paywall is already accessible from the parent view
                } label: {
                    Text("Subscribe")
                        .font(.system(.headline, design: .rounded, weight: .semibold))
                        .foregroundStyle(.white)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(AppTheme.teal, in: RoundedRectangle(cornerRadius: 14))
                }

                Button {
                    dismiss()
                } label: {
                    Text("Done")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
            }
            .padding(.horizontal)
        }
    }

    // MARK: - Validation

    private var isValidEmailFormat: Bool {
        let trimmed = email.trimmingCharacters(in: .whitespacesAndNewlines)
        return trimmed.contains("@") && trimmed.contains(".")
    }

    // MARK: - Actions

    private func sendCode() async {
        verificationState = .sendingCode
        let trimmedEmail = email.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()

        do {
            try await entitlement.sendVerificationCode(to: trimmedEmail)
            verificationState = .enterCode(email: trimmedEmail)
        } catch {
            verificationState = .failure("Unable to send verification code. Please check your internet connection and try again.")
        }
    }

    private func resendCode() async {
        guard case .enterCode(let sentEmail) = verificationState else { return }

        do {
            try await entitlement.sendVerificationCode(to: sentEmail)
            startResendCooldown()
        } catch {
            // Silently fail on resend — the user can try again
        }
    }

    private func verifyCode() async {
        guard case .enterCode(let sentEmail) = verificationState else { return }
        verificationState = .verifyingCode

        let result = await entitlement.verifyCode(otpCode, for: sentEmail)

        switch result {
        case .whitelistedAccessGranted:
            verificationState = .success
            // Auto-dismiss after success
            try? await Task.sleep(nanoseconds: 1_500_000_000)
            dismiss()

        case .emailVerifiedButNotWhitelisted:
            verificationState = .notWhitelisted(email: sentEmail)

        case .invalidCode:
            verificationState = .enterCode(email: sentEmail)
            otpCode = ""
            isCodeFocused = true
            // Brief error display — show inline
            verificationState = .failure("Invalid code. Please check and try again.")
            // Return to code entry after showing error
            try? await Task.sleep(nanoseconds: 2_000_000_000)
            if case .failure = verificationState {
                verificationState = .enterCode(email: sentEmail)
            }

        case .networkError:
            verificationState = .failure("Connection error. Please check your internet and try again.")
        }
    }

    private func startResendCooldown() {
        resendCooldown = 60
        Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { timer in
            if resendCooldown > 0 {
                resendCooldown -= 1
            } else {
                timer.invalidate()
            }
        }
    }
}

// Extension for state comparison
extension EmailVerificationView.VerificationState {
    static func == (lhs: Self, rhs: Self) -> Bool {
        switch (lhs, rhs) {
        case (.enterEmail, .enterEmail),
             (.sendingCode, .sendingCode),
             (.verifyingCode, .verifyingCode),
             (.success, .success):
            return true
        case (.enterCode(let a), .enterCode(let b)):
            return a == b
        case (.notWhitelisted(let a), .notWhitelisted(let b)):
            return a == b
        case (.failure(let a), .failure(let b)):
            return a == b
        default:
            return false
        }
    }
}

#Preview {
    EmailVerificationView()
        .environment(EntitlementService())
}
