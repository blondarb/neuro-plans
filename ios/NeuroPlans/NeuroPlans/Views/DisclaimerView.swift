import SwiftUI

struct DisclaimerView: View {
    @Binding var hasAcceptedDisclaimer: Bool
    @State private var hasScrolledToBottom = false
    
    var body: some View {
        VStack(spacing: 0) {
            // Header (specialty-specific icon and tagline)
            VStack(spacing: 8) {
                Image(systemName: SpecialtyConfig.headerIcon)
                    .font(.system(size: 60))
                    .foregroundStyle(AppTheme.teal)

                Text(SpecialtyConfig.disclaimerTitle)
                    .font(.largeTitle)
                    .fontWeight(.bold)

                Text(SpecialtyConfig.tagline)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
            .padding(.top, 40)
            .padding(.bottom, 24)
            
            // Disclaimer content
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    DisclaimerSection(
                        icon: "exclamationmark.triangle.fill",
                        iconColor: .orange,
                        title: "Important Notice",
                        content: "This application is designed as a clinical reference and decision support tool. It is intended for use by qualified healthcare professionals only."
                    )
                    
                    DisclaimerSection(
                        icon: "info.circle.fill",
                        iconColor: .blue,
                        title: "Information Only",
                        content: "The content provided in this app is for informational and educational purposes only. It does not constitute medical advice, diagnosis, or treatment recommendations."
                    )
                    
                    DisclaimerSection(
                        icon: "person.fill.questionmark",
                        iconColor: .purple,
                        title: "Clinical Judgment Required",
                        content: "All clinical decisions must be made by a qualified healthcare provider based on individual patient circumstances. This app does not replace professional medical judgment, clinical experience, or the provider-patient relationship."
                    )
                    
                    DisclaimerSection(
                        icon: "checkmark.shield.fill",
                        iconColor: .green,
                        title: "Verification Required",
                        content: "Users are responsible for verifying all information, including drug dosages, contraindications, and treatment protocols, against current medical literature and institutional guidelines before clinical application."
                    )
                    
                    DisclaimerSection(
                        icon: "hand.raised.fill",
                        iconColor: .red,
                        title: "Limitation of Liability",
                        content: "The developers, authors, and distributors of this application assume no liability for any adverse outcomes, errors, omissions, or damages arising from the use of this application or reliance on its content."
                    )
                    
                    DisclaimerSection(
                        icon: "arrow.triangle.2.circlepath",
                        iconColor: .teal,
                        title: "Content Updates",
                        content: "Medical knowledge evolves continuously. While efforts are made to keep content current, some information may become outdated. Always consult the most recent clinical guidelines and evidence-based resources."
                    )
                    
                    // Scroll indicator
                    GeometryReader { geo in
                        Color.clear
                            .onAppear {
                                hasScrolledToBottom = true
                            }
                    }
                    .frame(height: 1)
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 20)
            }
            
            // Accept button
            VStack(spacing: 12) {
                Divider()
                
                Text("By tapping \"I Understand & Accept\", you acknowledge that you have read, understood, and agree to these terms.")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)
                
                Button {
                    withAnimation {
                        hasAcceptedDisclaimer = true
                    }
                } label: {
                    Text("I Understand & Accept")
                        .font(.headline)
                        .foregroundStyle(.white)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 16)
                        .background(AppTheme.teal)
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 20)
            }
            .background(Color(.systemBackground))
        }
        .background(Color(.systemGroupedBackground))
    }
}

struct DisclaimerSection: View {
    let icon: String
    let iconColor: Color
    let title: String
    let content: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .foregroundStyle(iconColor)
                    .font(.title3)
                
                Text(title)
                    .font(.headline)
            }
            
            Text(content)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color(.secondarySystemGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

#Preview {
    DisclaimerView(hasAcceptedDisclaimer: .constant(false))
}
