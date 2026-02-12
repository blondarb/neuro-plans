import SwiftUI
import MessageUI

/// A SwiftUI wrapper for MFMailComposeViewController to send error reports
struct ErrorReportMailView: UIViewControllerRepresentable {
    @Environment(\.dismiss) private var dismiss
    
    let subject: String
    let body: String
    let recipients: [String]
    var onComplete: ((Bool) -> Void)?
    
    func makeUIViewController(context: Context) -> MFMailComposeViewController {
        let mailComposer = MFMailComposeViewController()
        mailComposer.mailComposeDelegate = context.coordinator
        mailComposer.setToRecipients(recipients)
        mailComposer.setSubject(subject)
        mailComposer.setMessageBody(body, isHTML: false)
        return mailComposer
    }
    
    func updateUIViewController(_ uiViewController: MFMailComposeViewController, context: Context) {}
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    class Coordinator: NSObject, MFMailComposeViewControllerDelegate {
        let parent: ErrorReportMailView
        
        init(_ parent: ErrorReportMailView) {
            self.parent = parent
        }
        
        func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
            let success = result == .sent
            parent.onComplete?(success)
            parent.dismiss()
        }
    }
    
    /// Check if device can send email
    static var canSendMail: Bool {
        MFMailComposeViewController.canSendMail()
    }
}

/// A view for sending a single error report via email
struct SingleReportMailButton: View {
    let report: ClinicalErrorReport
    @Environment(ClinicalErrorService.self) private var errorService
    @State private var showMailComposer = false
    @State private var showNoMailAlert = false
    
    var body: some View {
        Button {
            if ErrorReportMailView.canSendMail {
                showMailComposer = true
            } else {
                showNoMailAlert = true
            }
        } label: {
            Label("Send Report", systemImage: "envelope.fill")
        }
        .sheet(isPresented: $showMailComposer) {
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
        .alert("Email Not Available", isPresented: $showNoMailAlert) {
            Button("OK") {}
            Button("Copy Report") {
                UIPasteboard.general.string = errorService.formatReportForEmail(report)
            }
        } message: {
            Text("Mail is not configured on this device. You can copy the report to send it manually.")
        }
    }
}

/// A view for sending all unsent error reports via email
struct SendAllReportsButton: View {
    @Environment(ClinicalErrorService.self) private var errorService
    @State private var showMailComposer = false
    @State private var showNoMailAlert = false
    @State private var showNoReportsAlert = false
    
    var body: some View {
        Button {
            if errorService.unsentReportCount == 0 {
                showNoReportsAlert = true
            } else if ErrorReportMailView.canSendMail {
                showMailComposer = true
            } else {
                showNoMailAlert = true
            }
        } label: {
            HStack {
                Label("Send Error Reports", systemImage: "envelope.fill")
                Spacer()
                if errorService.unsentReportCount > 0 {
                    Text("\(errorService.unsentReportCount)")
                        .font(.caption2)
                        .fontWeight(.bold)
                        .foregroundStyle(.white)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 2)
                        .background(.red, in: Capsule())
                }
            }
        }
        .sheet(isPresented: $showMailComposer) {
            ErrorReportMailView(
                subject: "Neuro Plans - Clinical Error Reports (\(errorService.unsentReportCount))",
                body: errorService.formatUnsentReportsForEmail(),
                recipients: [ClinicalErrorService.reportEmailAddress]
            ) { success in
                if success {
                    errorService.markAllReportsAsSent()
                }
            }
        }
        .alert("Email Not Available", isPresented: $showNoMailAlert) {
            Button("OK") {}
            Button("Copy Reports") {
                UIPasteboard.general.string = errorService.formatUnsentReportsForEmail()
            }
        } message: {
            Text("Mail is not configured on this device. You can copy the reports to send them manually.")
        }
        .alert("No Pending Reports", isPresented: $showNoReportsAlert) {
            Button("OK") {}
        } message: {
            Text("All error reports have already been sent.")
        }
    }
}

#Preview {
    List {
        SendAllReportsButton()
    }
    .environment(ClinicalErrorService())
}
