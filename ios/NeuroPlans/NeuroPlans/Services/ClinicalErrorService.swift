import SwiftUI
import Foundation

/// Manages clinical error reports and the free year reward program
@Observable
final class ClinicalErrorService {
    // MARK: - Properties
    
    /// All submitted error reports
    var submittedReports: [ClinicalErrorReport] {
        get {
            guard let data = UserDefaults.standard.data(forKey: Keys.submittedReports),
                  let reports = try? JSONDecoder().decode([ClinicalErrorReport].self, from: data) else {
                return []
            }
            return reports
        }
        set {
            if let data = try? JSONEncoder().encode(newValue) {
                UserDefaults.standard.set(data, forKey: Keys.submittedReports)
            }
        }
    }
    
    /// Number of plan views (for tracking first 10 uses)
    var planViewCount: Int {
        get { UserDefaults.standard.integer(forKey: Keys.planViewCount) }
        set { UserDefaults.standard.set(newValue, forKey: Keys.planViewCount) }
    }
    
    /// Whether the user has earned a free year from error reporting
    var hasEarnedFreeYear: Bool {
        get { UserDefaults.standard.bool(forKey: Keys.hasEarnedFreeYear) }
        set { UserDefaults.standard.set(newValue, forKey: Keys.hasEarnedFreeYear) }
    }
    
    /// Date when free year was earned
    var freeYearEarnedDate: Date? {
        get { UserDefaults.standard.object(forKey: Keys.freeYearEarnedDate) as? Date }
        set { UserDefaults.standard.set(newValue, forKey: Keys.freeYearEarnedDate) }
    }
    
    // MARK: - Constants
    
    private enum Keys {
        static let submittedReports = "clinicalError.submittedReports"
        static let planViewCount = "clinicalError.planViewCount"
        static let hasEarnedFreeYear = "clinicalError.hasEarnedFreeYear"
        static let freeYearEarnedDate = "clinicalError.freeYearEarnedDate"
    }
    
    /// Maximum plan views for error report reward eligibility
    static let maxViewsForReward = 10
    
    /// Minimum report length for validity
    static let minReportLength = 50
    
    // MARK: - Computed Properties
    
    /// Whether the user is still eligible to earn a free year
    var isEligibleForReward: Bool {
        !hasEarnedFreeYear && planViewCount <= Self.maxViewsForReward
    }
    
    /// Remaining views before reward eligibility expires
    var remainingEligibleViews: Int {
        max(0, Self.maxViewsForReward - planViewCount)
    }
    
    /// Whether the free year is still active
    var isFreeYearActive: Bool {
        guard hasEarnedFreeYear, let earnedDate = freeYearEarnedDate else {
            return false
        }
        let oneYearLater = Calendar.current.date(byAdding: .year, value: 1, to: earnedDate) ?? earnedDate
        return Date() < oneYearLater
    }
    
    /// Expiration date of the free year
    var freeYearExpirationDate: Date? {
        guard let earnedDate = freeYearEarnedDate else { return nil }
        return Calendar.current.date(byAdding: .year, value: 1, to: earnedDate)
    }
    
    // MARK: - Methods
    
    /// Record a plan view
    func recordPlanView() {
        planViewCount += 1
    }
    
    /// Submit a clinical error report
    func submitReport(_ report: ClinicalErrorReport) -> Bool {
        // Validate report
        guard report.description.count >= Self.minReportLength else {
            return false
        }
        
        // Save report
        var reports = submittedReports
        reports.append(report)
        submittedReports = reports
        
        // Award free year if eligible and this is first valid report
        if isEligibleForReward && !hasEarnedFreeYear {
            hasEarnedFreeYear = true
            freeYearEarnedDate = Date()
            
            // Post notification for entitlement refresh
            NotificationCenter.default.post(name: .clinicalErrorRewardEarned, object: nil)
        }
        
        return true
    }
    
    /// Email address for receiving error reports
    static let reportEmailAddress = SpecialtyConfig.errorReportEmail
    
    /// Number of unsent reports
    var unsentReportCount: Int {
        submittedReports.filter { !$0.wasSent }.count
    }
    
    /// Mark a report as sent
    func markReportAsSent(_ reportId: UUID) {
        var reports = submittedReports
        if let index = reports.firstIndex(where: { $0.id == reportId }) {
            reports[index].wasSent = true
            submittedReports = reports
        }
    }
    
    /// Mark all reports as sent
    func markAllReportsAsSent() {
        var reports = submittedReports
        for i in reports.indices {
            reports[i].wasSent = true
        }
        submittedReports = reports
    }
    
    /// Format a single report for email
    func formatReportForEmail(_ report: ClinicalErrorReport) -> String {
        var output = """
        CLINICAL ERROR REPORT
        =====================
        
        Report ID: \(report.id.uuidString.prefix(8))
        Submitted: \(report.submittedAt.formatted(date: .abbreviated, time: .shortened))
        
        LOCATION
        --------
        Plan: \(report.planTitle)
        Plan ID: \(report.planId)
        Section: \(report.section ?? "Not specified")
        Item: \(report.itemText ?? "Not specified")
        
        CLASSIFICATION
        --------------
        Category: \(report.category.rawValue)
        Severity: \(report.severity.rawValue) - \(report.severity.description)
        
        DESCRIPTION
        -----------
        \(report.description)
        
        """
        
        if let suggested = report.suggestedCorrection, !suggested.isEmpty {
            output += """
            
            SUGGESTED CORRECTION
            --------------------
            \(suggested)
            
            """
        }
        
        if let reference = report.reference, !reference.isEmpty {
            output += """
            
            REFERENCE/SOURCE
            ----------------
            \(reference)
            
            """
        }
        
        return output
    }
    
    /// Format all unsent reports for email
    func formatUnsentReportsForEmail() -> String {
        let unsent = submittedReports.filter { !$0.wasSent }
        guard !unsent.isEmpty else { return "" }
        
        var output = """
        \(SpecialtyConfig.appName.uppercased()) - CLINICAL ERROR REPORTS
        ====================================
        Total Reports: \(unsent.count)
        Generated: \(Date().formatted())
        
        
        """
        
        for (index, report) in unsent.enumerated() {
            output += "--- REPORT \(index + 1) of \(unsent.count) ---\n\n"
            output += formatReportForEmail(report)
            output += "\n\n"
        }
        
        return output
    }
    
    /// Get reports for export/review (legacy format)
    func exportReports() -> String {
        var output = "Clinical Error Reports\n"
        output += "Generated: \(Date().formatted())\n"
        output += "=" .repeated(50) + "\n\n"
        
        for (index, report) in submittedReports.enumerated() {
            output += "Report #\(index + 1)\n"
            output += "-".repeated(30) + "\n"
            output += "Date: \(report.submittedAt.formatted())\n"
            output += "Plan: \(report.planTitle) (ID: \(report.planId))\n"
            output += "Section: \(report.section ?? "Not specified")\n"
            output += "Item: \(report.itemText ?? "Not specified")\n"
            output += "Severity: \(report.severity.rawValue)\n"
            output += "Category: \(report.category.rawValue)\n"
            output += "\nDescription:\n\(report.description)\n"
            if let suggested = report.suggestedCorrection {
                output += "\nSuggested Correction:\n\(suggested)\n"
            }
            if let reference = report.reference {
                output += "\nReference: \(reference)\n"
            }
            output += "\n"
        }
        
        return output
    }
}

// MARK: - Clinical Error Report Model

struct ClinicalErrorReport: Codable, Identifiable {
    let id: UUID
    let planId: String
    let planTitle: String
    let section: String?
    let itemText: String?
    let category: ErrorCategory
    let severity: ErrorSeverity
    let description: String
    let suggestedCorrection: String?
    let reference: String?
    let submittedAt: Date
    var wasSent: Bool
    
    init(
        planId: String,
        planTitle: String,
        section: String? = nil,
        itemText: String? = nil,
        category: ErrorCategory,
        severity: ErrorSeverity,
        description: String,
        suggestedCorrection: String? = nil,
        reference: String? = nil
    ) {
        self.id = UUID()
        self.planId = planId
        self.planTitle = planTitle
        self.section = section
        self.itemText = itemText
        self.category = category
        self.severity = severity
        self.description = description
        self.suggestedCorrection = suggestedCorrection
        self.reference = reference
        self.submittedAt = Date()
        self.wasSent = false
    }
    
    enum ErrorCategory: String, Codable, CaseIterable {
        case dosing = "Medication Dosing"
        case indication = "Wrong Indication"
        case contraindication = "Missing Contraindication"
        case interaction = "Drug Interaction"
        case labValue = "Lab Value Error"
        case diagnosis = "Diagnostic Criteria"
        case procedure = "Procedure Error"
        case monitoring = "Monitoring Gap"
        case outdated = "Outdated Information"
        case other = "Other"
        
        var icon: String {
            switch self {
            case .dosing: return "pills.fill"
            case .indication: return "exclamationmark.triangle.fill"
            case .contraindication: return "xmark.shield.fill"
            case .interaction: return "arrow.triangle.2.circlepath"
            case .labValue: return "testtube.2"
            case .diagnosis: return "stethoscope"
            case .procedure: return "cross.case.fill"
            case .monitoring: return "chart.xyaxis.line"
            case .outdated: return "clock.arrow.circlepath"
            case .other: return "questionmark.circle.fill"
            }
        }
    }
    
    enum ErrorSeverity: String, Codable, CaseIterable {
        case critical = "Critical"
        case major = "Major"
        case minor = "Minor"
        case suggestion = "Suggestion"
        
        var color: Color {
            switch self {
            case .critical: return .red
            case .major: return .orange
            case .minor: return .yellow
            case .suggestion: return .blue
            }
        }
        
        var description: String {
            switch self {
            case .critical: return "Could cause patient harm"
            case .major: return "Significant clinical impact"
            case .minor: return "Minor inaccuracy"
            case .suggestion: return "Improvement suggestion"
            }
        }
    }
}

// MARK: - String Extension

private extension String {
    func repeated(_ count: Int) -> String {
        String(repeating: self, count: count)
    }
}

// MARK: - Notification Names

extension Notification.Name {
    static let clinicalErrorRewardEarned = Notification.Name("clinicalErrorRewardEarned")
}
