import SwiftUI

struct EmailVerificationView: View {
    @Environment(EntitlementService.self) private var entitlement
    @Environment(\.dismiss) private var dismiss
    
    @State private var email = ""
    @State private var verificationState: VerificationState = .idle
    @FocusState private var isEmailFocused: Bool
    
    enum VerificationState {
        case idle
        case verifying
        case success
        case failure(String)
    }
    
    var body: some View {
        NavigationStack {
            VStack(spacing: 24) {
                Spacer()
                
                // Header
                VStack(spacing: 16) {
                    ZStack {
                        Circle()
                            .fill(.purple.opacity(0.15))
                            .frame(width: 80, height: 80)
                        
                        Image(systemName: "building.2.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.purple)
                    }
                    
                    Text("Team Verification")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                    
                    Text("Enter your @sevaro.com email address to get free access to Neuro Plans.")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                }
                
                // Email input
                VStack(alignment: .leading, spacing: 8) {
                    Text("Work Email")
                        .font(.system(.subheadline, design: .rounded, weight: .medium))
                        .foregroundStyle(.secondary)
                    
                    HStack {
                        Image(systemName: "envelope.fill")
                            .foregroundStyle(.secondary)
                        
                        TextField("name@sevaro.com", text: $email)
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
                    
                    // Hint about valid domains
                    HStack(spacing: 4) {
                        Image(systemName: "info.circle")
                            .font(.system(size: 10))
                        Text("Only @sevaro.com addresses qualify for free access")
                            .font(.caption2)
                    }
                    .foregroundStyle(.tertiary)
                }
                .padding(.horizontal)
                
                // Status message
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
                
                if case .success = verificationState {
                    HStack {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(.green)
                        Text("Email verified! You now have free access.")
                            .font(.subheadline)
                    }
                    .foregroundStyle(.green)
                    .padding()
                    .background(.green.opacity(0.1), in: RoundedRectangle(cornerRadius: 12))
                    .padding(.horizontal)
                }
                
                // Verify button
                Button {
                    verifyEmail()
                } label: {
                    HStack {
                        if case .verifying = verificationState {
                            ProgressView()
                                .tint(.white)
                        } else {
                            Text("Verify Email")
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
                .disabled(!isValidEmailFormat || verificationState == .verifying)
                .padding(.horizontal)
                
                Spacer()
                Spacer()
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Team Access")
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
    
    // MARK: - Validation
    
    private var isValidEmailFormat: Bool {
        let trimmed = email.trimmingCharacters(in: .whitespacesAndNewlines)
        return trimmed.contains("@") && trimmed.contains(".")
    }
    
    // MARK: - Actions
    
    private func verifyEmail() {
        verificationState = .verifying
        
        // Small delay for UX
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            let success = entitlement.verifyEmail(email)
            
            if success {
                verificationState = .success
                
                // Auto-dismiss after success
                DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
                    dismiss()
                }
            } else {
                verificationState = .failure("This email address is not eligible for free access. Please use a @sevaro.com email or subscribe.")
            }
        }
    }
}

// Extension for state comparison
extension EmailVerificationView.VerificationState: Equatable {
    static func == (lhs: EmailVerificationView.VerificationState, rhs: EmailVerificationView.VerificationState) -> Bool {
        switch (lhs, rhs) {
        case (.idle, .idle), (.verifying, .verifying), (.success, .success):
            return true
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
