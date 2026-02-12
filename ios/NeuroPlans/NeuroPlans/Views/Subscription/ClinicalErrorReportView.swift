import SwiftUI

struct ClinicalErrorReportView: View {
    let planId: String
    let planTitle: String
    let section: String?
    let itemText: String?
    
    @Environment(ClinicalErrorService.self) private var errorService
    @Environment(\.dismiss) private var dismiss
    
    @State private var category: ClinicalErrorReport.ErrorCategory = .other
    @State private var severity: ClinicalErrorReport.ErrorSeverity = .major
    @State private var description = ""
    @State private var suggestedCorrection = ""
    @State private var reference = ""
    @State private var showSuccessAlert = false
    @State private var showRewardAlert = false
    @State private var showSendEmailPrompt = false
    @State private var showMailComposer = false
    @State private var lastSubmittedReport: ClinicalErrorReport?
    @State private var errorMessage: String?
    
    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 20) {
                    // Reward banner (if eligible)
                    if errorService.isEligibleForReward {
                        RewardBannerView(remainingViews: errorService.remainingEligibleViews)
                    }
                    
                    // Context info
                    contextSection
                    
                    // Error details form
                    errorDetailsSection
                    
                    // Description
                    descriptionSection
                    
                    // Suggested correction
                    suggestionSection
                    
                    // Reference
                    referenceSection
                    
                    // Submit button
                    submitButton
                    
                    // Character count hint
                    if description.count < ClinicalErrorService.minReportLength {
                        Text("Please provide at least \(ClinicalErrorService.minReportLength) characters (\(ClinicalErrorService.minReportLength - description.count) more needed)")
                            .font(.caption)
                            .foregroundStyle(.orange)
                    }
                }
                .padding()
            }
            .background { AdaptiveBackground() }
            .navigationTitle("Report Clinical Error")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Cancel") {
                        dismiss()
                    }
                }
            }
            .alert("Report Submitted", isPresented: $showSuccessAlert) {
                Button("Send Now") {
                    if ErrorReportMailView.canSendMail {
                        showMailComposer = true
                    } else {
                        // Copy to clipboard if mail not available
                        if let report = lastSubmittedReport {
                            UIPasteboard.general.string = errorService.formatReportForEmail(report)
                        }
                        dismiss()
                    }
                }
                Button("Send Later") {
                    dismiss()
                }
            } message: {
                Text("Thank you for helping improve clinical accuracy. Would you like to send this report now?")
            }
            .alert("Free Year Earned!", isPresented: $showRewardAlert) {
                Button("Send Report Now") {
                    if ErrorReportMailView.canSendMail {
                        showMailComposer = true
                    } else {
                        if let report = lastSubmittedReport {
                            UIPasteboard.general.string = errorService.formatReportForEmail(report)
                        }
                        dismiss()
                    }
                }
                Button("Send Later") {
                    dismiss()
                }
            } message: {
                Text("Thank you for your valuable clinical feedback! You've earned one year of free access to Neuro Plans. Would you like to send this report now?")
            }
            .sheet(isPresented: $showMailComposer, onDismiss: {
                dismiss()
            }) {
                if let report = lastSubmittedReport {
                    ErrorReportMailView(
                        subject: "Clinical Error Report: \(report.planTitle)",
                        body: errorService.formatReportForEmail(report),
                        recipients: [ClinicalErrorService.reportEmailAddress]
                    ) { success in
                        if success {
                            errorService.markReportAsSent(report.id)
                        }
                    }
                }
            }
        }
    }
    
    // MARK: - Sections
    
    private var contextSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Reporting Error In")
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)
            
            GlassCard(cornerRadius: 12) {
                VStack(alignment: .leading, spacing: 6) {
                    HStack {
                        Image(systemName: "doc.text.fill")
                            .foregroundStyle(AppTheme.teal)
                        Text(planTitle)
                            .font(.system(.subheadline, weight: .medium))
                    }
                    
                    if let section = section {
                        HStack {
                            Image(systemName: "folder.fill")
                                .foregroundStyle(.secondary)
                                .font(.caption)
                            Text(section)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    }
                    
                    if let item = itemText {
                        HStack(alignment: .top) {
                            Image(systemName: "arrow.right.circle.fill")
                                .foregroundStyle(.secondary)
                                .font(.caption)
                            Text(item)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                                .lineLimit(2)
                        }
                    }
                }
            }
        }
    }
    
    private var errorDetailsSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Error Details")
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)
            
            // Category picker
            VStack(alignment: .leading, spacing: 6) {
                Text("Category")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                
                Menu {
                    ForEach(ClinicalErrorReport.ErrorCategory.allCases, id: \.self) { cat in
                        Button {
                            category = cat
                        } label: {
                            Label(cat.rawValue, systemImage: cat.icon)
                        }
                    }
                } label: {
                    HStack {
                        Image(systemName: category.icon)
                            .foregroundStyle(AppTheme.teal)
                        Text(category.rawValue)
                            .font(.subheadline)
                        Spacer()
                        Image(systemName: "chevron.up.chevron.down")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                    }
                    .padding()
                    .background(Color.white.opacity(0.05), in: RoundedRectangle(cornerRadius: 10))
                }
                .buttonStyle(.plain)
            }
            
            // Severity picker
            VStack(alignment: .leading, spacing: 6) {
                Text("Severity")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                
                HStack(spacing: 8) {
                    ForEach(ClinicalErrorReport.ErrorSeverity.allCases, id: \.self) { sev in
                        Button {
                            severity = sev
                        } label: {
                            VStack(spacing: 4) {
                                Text(sev.rawValue)
                                    .font(.system(.caption, design: .rounded, weight: .medium))
                            }
                            .padding(.horizontal, 12)
                            .padding(.vertical, 8)
                            .frame(maxWidth: .infinity)
                            .background(
                                severity == sev ? sev.color.opacity(0.2) : Color.white.opacity(0.05),
                                in: RoundedRectangle(cornerRadius: 8)
                            )
                            .overlay {
                                RoundedRectangle(cornerRadius: 8)
                                    .strokeBorder(severity == sev ? sev.color : Color.clear, lineWidth: 1)
                            }
                        }
                        .buttonStyle(.plain)
                        .foregroundStyle(severity == sev ? sev.color : .secondary)
                    }
                }
            }
        }
    }
    
    private var descriptionSection: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack {
                Text("Description")
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .foregroundStyle(.secondary)
                Text("*")
                    .foregroundStyle(.red)
            }
            
            TextField("Describe the clinical error in detail. What is incorrect and why is it clinically significant?", text: $description, axis: .vertical)
                .lineLimit(5...10)
                .padding()
                .background(Color.white.opacity(0.05), in: RoundedRectangle(cornerRadius: 10))
            
            Text("\(description.count) characters")
                .font(.caption2)
                .foregroundStyle(.tertiary)
        }
    }
    
    private var suggestionSection: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Suggested Correction")
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)
            
            TextField("What should it say instead? (Optional but helpful)", text: $suggestedCorrection, axis: .vertical)
                .lineLimit(3...6)
                .padding()
                .background(Color.white.opacity(0.05), in: RoundedRectangle(cornerRadius: 10))
        }
    }
    
    private var referenceSection: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Reference/Source")
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .foregroundStyle(.secondary)
            
            TextField("Citation, guideline, or source supporting the correction (Optional)", text: $reference, axis: .vertical)
                .lineLimit(2...4)
                .padding()
                .background(Color.white.opacity(0.05), in: RoundedRectangle(cornerRadius: 10))
        }
    }
    
    private var submitButton: some View {
        Button {
            submitReport()
        } label: {
            HStack {
                Image(systemName: "paperplane.fill")
                Text("Submit Report")
            }
            .font(.system(.headline, design: .rounded, weight: .semibold))
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .padding()
            .background(
                isValidReport ? AppTheme.teal : Color.gray,
                in: RoundedRectangle(cornerRadius: 14)
            )
        }
        .disabled(!isValidReport)
        
    }
    
    // MARK: - Helpers
    
    private var isValidReport: Bool {
        description.count >= ClinicalErrorService.minReportLength
    }
    
    private func submitReport() {
        let willEarnReward = errorService.isEligibleForReward && !errorService.hasEarnedFreeYear
        
        let report = ClinicalErrorReport(
            planId: planId,
            planTitle: planTitle,
            section: section,
            itemText: itemText,
            category: category,
            severity: severity,
            description: description,
            suggestedCorrection: suggestedCorrection.isEmpty ? nil : suggestedCorrection,
            reference: reference.isEmpty ? nil : reference
        )
        
        let success = errorService.submitReport(report)
        
        if success {
            lastSubmittedReport = report
            if willEarnReward {
                showRewardAlert = true
            } else {
                showSuccessAlert = true
            }
        }
    }
}

// MARK: - Reward Banner View

private struct RewardBannerView: View {
    let remainingViews: Int
    
    var body: some View {
        VStack(spacing: 10) {
            HStack {
                Image(systemName: "gift.fill")
                    .font(.title2)
                    .foregroundStyle(.yellow)
                
                VStack(alignment: .leading, spacing: 2) {
                    Text("Earn 1 Year Free!")
                        .font(.system(.subheadline, design: .rounded, weight: .bold))
                    Text("Report a clinical error to help improve accuracy")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                
                Spacer()
            }
            
            HStack {
                Image(systemName: "clock.fill")
                    .font(.caption)
                    .foregroundStyle(.orange)
                Text("Offer expires after \(remainingViews) more plan view\(remainingViews == 1 ? "" : "s")")
                    .font(.caption2)
                    .foregroundStyle(.orange)
                Spacer()
            }
        }
        .padding()
        .background {
            RoundedRectangle(cornerRadius: 12)
                .fill(LinearGradient(
                    colors: [.yellow.opacity(0.15), .orange.opacity(0.1)],
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                ))
                .overlay {
                    RoundedRectangle(cornerRadius: 12)
                        .strokeBorder(.yellow.opacity(0.3), lineWidth: 1)
                }
        }
    }
}

#Preview {
    ClinicalErrorReportView(
        planId: "test-plan",
        planTitle: "Acute Ischemic Stroke",
        section: "Treatment",
        itemText: "tPA 0.9 mg/kg IV"
    )
    .environment(ClinicalErrorService())
}
