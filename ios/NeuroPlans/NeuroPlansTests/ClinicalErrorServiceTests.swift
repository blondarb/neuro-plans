import XCTest
@testable import NeuroPlans

/// Tests for ClinicalErrorService — manages clinical error reports submitted
/// by users and the "free year" reward program for early error reporters.
///
/// The reward program incentivizes users to report clinical errors during their
/// first 10 plan views. If they submit a valid report (>= 50 characters), they
/// earn a free year of access. This is a one-time reward.
final class ClinicalErrorServiceTests: XCTestCase {

    // MARK: - Properties

    private var service: ClinicalErrorService!

    // MARK: - UserDefaults Keys (mirroring the service's private Keys enum)

    private let submittedReportsKey = "clinicalError.submittedReports"
    private let planViewCountKey = "clinicalError.planViewCount"
    private let hasEarnedFreeYearKey = "clinicalError.hasEarnedFreeYear"
    private let freeYearEarnedDateKey = "clinicalError.freeYearEarnedDate"

    // MARK: - Setup / Teardown

    override func setUp() {
        super.setUp()
        clearErrorServiceDefaults()
        service = ClinicalErrorService()
    }

    override func tearDown() {
        clearErrorServiceDefaults()
        service = nil
        super.tearDown()
    }

    private func clearErrorServiceDefaults() {
        UserDefaults.standard.removeObject(forKey: submittedReportsKey)
        UserDefaults.standard.removeObject(forKey: planViewCountKey)
        UserDefaults.standard.removeObject(forKey: hasEarnedFreeYearKey)
        UserDefaults.standard.removeObject(forKey: freeYearEarnedDateKey)
    }

    // MARK: - Helpers

    /// Create a valid clinical error report with description of sufficient length
    private func makeValidReport(
        planId: String = "migraine",
        planTitle: String = "Acute Migraine",
        description: String? = nil,
        category: ClinicalErrorReport.ErrorCategory = .dosing,
        severity: ClinicalErrorReport.ErrorSeverity = .major
    ) -> ClinicalErrorReport {
        let desc = description ?? String(repeating: "This medication dosage appears incorrect based on current guidelines. ", count: 2)
        return ClinicalErrorReport(
            planId: planId,
            planTitle: planTitle,
            section: "Treatment",
            itemText: "Sumatriptan",
            category: category,
            severity: severity,
            description: desc,
            suggestedCorrection: "Correct dosage is 6 mg SC",
            reference: "UpToDate 2024"
        )
    }

    /// Create a report with description shorter than the minimum length
    private func makeShortReport() -> ClinicalErrorReport {
        return ClinicalErrorReport(
            planId: "migraine",
            planTitle: "Acute Migraine",
            category: .dosing,
            severity: .minor,
            description: "Too short"  // Less than 50 characters
        )
    }

    // MARK: - Constants

    /// Maximum views for reward eligibility should be 10
    func testMaxViewsForReward() {
        XCTAssertEqual(ClinicalErrorService.maxViewsForReward, 10,
                       "Users should be eligible within first 10 plan views")
    }

    /// Minimum report length should be 50 characters
    func testMinReportLength() {
        XCTAssertEqual(ClinicalErrorService.minReportLength, 50,
                       "Reports must be at least 50 characters to be valid")
    }

    /// Report email address should be correct
    func testReportEmailAddress() {
        XCTAssertEqual(ClinicalErrorService.reportEmailAddress, SpecialtyConfig.errorReportEmail)
    }

    // MARK: - Report Validation

    /// Valid report (>= 50 chars) should be accepted
    func testSubmitReport_Valid() {
        let report = makeValidReport()
        let success = service.submitReport(report)
        XCTAssertTrue(success, "Report with sufficient description length should be accepted")
    }

    /// Short report (< 50 chars) should be rejected
    func testSubmitReport_TooShort() {
        let report = makeShortReport()
        let success = service.submitReport(report)
        XCTAssertFalse(success, "Report with description < 50 characters should be rejected")
    }

    /// Report at exactly 50 characters should be accepted
    func testSubmitReport_ExactlyMinLength() {
        let exactly50 = String(repeating: "a", count: 50)
        let report = ClinicalErrorReport(
            planId: "test",
            planTitle: "Test Plan",
            category: .other,
            severity: .suggestion,
            description: exactly50
        )
        let success = service.submitReport(report)
        XCTAssertTrue(success, "Report at exactly 50 characters should be accepted")
    }

    /// Report at 49 characters should be rejected
    func testSubmitReport_OneBelowMinLength() {
        let fortyNine = String(repeating: "a", count: 49)
        let report = ClinicalErrorReport(
            planId: "test",
            planTitle: "Test Plan",
            category: .other,
            severity: .suggestion,
            description: fortyNine
        )
        let success = service.submitReport(report)
        XCTAssertFalse(success, "Report at 49 characters should be rejected")
    }

    // MARK: - Report Storage

    /// Submitted reports should be stored and retrievable
    func testSubmittedReports_Stored() {
        let report = makeValidReport()
        _ = service.submitReport(report)

        XCTAssertEqual(service.submittedReports.count, 1,
                       "One report should be stored after successful submission")
    }

    /// Multiple reports should accumulate
    func testSubmittedReports_Accumulate() {
        _ = service.submitReport(makeValidReport(planId: "migraine"))
        _ = service.submitReport(makeValidReport(planId: "stroke-ischemic", planTitle: "Acute Ischemic Stroke"))

        XCTAssertEqual(service.submittedReports.count, 2,
                       "Multiple valid reports should accumulate")
    }

    /// Rejected reports should NOT be stored
    func testSubmittedReports_RejectedNotStored() {
        _ = service.submitReport(makeShortReport())
        XCTAssertEqual(service.submittedReports.count, 0,
                       "Rejected reports should not be stored")
    }

    /// Reports should persist across service re-creation (UserDefaults)
    func testSubmittedReports_Persistence() {
        _ = service.submitReport(makeValidReport())

        // Re-create service
        let newService = ClinicalErrorService()
        XCTAssertEqual(newService.submittedReports.count, 1,
                       "Reports should persist in UserDefaults")
    }

    // MARK: - Plan View Tracking

    /// Initial view count should be 0
    func testPlanViewCount_InitiallyZero() {
        XCTAssertEqual(service.planViewCount, 0)
    }

    /// recordPlanView should increment the count
    func testRecordPlanView_Increments() {
        service.recordPlanView()
        XCTAssertEqual(service.planViewCount, 1)

        service.recordPlanView()
        XCTAssertEqual(service.planViewCount, 2)
    }

    /// Remaining eligible views should decrease with each view
    func testRemainingEligibleViews() {
        XCTAssertEqual(service.remainingEligibleViews, 10)

        service.recordPlanView()
        XCTAssertEqual(service.remainingEligibleViews, 9)
    }

    /// Remaining eligible views should not go below 0
    func testRemainingEligibleViews_Floor() {
        for _ in 1...15 {
            service.recordPlanView()
        }
        XCTAssertEqual(service.remainingEligibleViews, 0,
                       "Remaining views should floor at 0, not go negative")
    }

    // MARK: - Reward Eligibility

    /// User should be eligible before any views and before earning reward
    func testIsEligibleForReward_Initially() {
        XCTAssertTrue(service.isEligibleForReward,
                      "New users should be eligible for the error report reward")
    }

    /// User should still be eligible at exactly 10 views
    func testIsEligibleForReward_AtMaxViews() {
        for _ in 1...10 {
            service.recordPlanView()
        }
        XCTAssertTrue(service.isEligibleForReward,
                      "User should still be eligible at exactly 10 views")
    }

    /// User should NOT be eligible after exceeding max views
    func testIsEligibleForReward_ExceededViews() {
        for _ in 1...11 {
            service.recordPlanView()
        }
        XCTAssertFalse(service.isEligibleForReward,
                       "User should lose eligibility after 10 views")
    }

    /// User should NOT be eligible after already earning the reward
    func testIsEligibleForReward_AlreadyEarned() {
        service.hasEarnedFreeYear = true
        XCTAssertFalse(service.isEligibleForReward,
                       "User who already earned reward should not be eligible again")
    }

    // MARK: - Free Year Reward Granting

    /// Submitting a valid report while eligible should grant the free year
    func testSubmitReport_GrantsFreeYear() {
        XCTAssertFalse(service.hasEarnedFreeYear, "Should not have reward before reporting")

        _ = service.submitReport(makeValidReport())

        XCTAssertTrue(service.hasEarnedFreeYear,
                      "Valid report while eligible should grant free year")
        XCTAssertNotNil(service.freeYearEarnedDate,
                        "Free year earned date should be set")
    }

    /// Free year should only be granted once (one-time reward)
    func testSubmitReport_OneTimeReward() {
        _ = service.submitReport(makeValidReport())
        let firstDate = service.freeYearEarnedDate

        // Submit another report
        _ = service.submitReport(makeValidReport(planId: "stroke"))

        XCTAssertEqual(service.freeYearEarnedDate, firstDate,
                       "Free year date should not change on subsequent reports")
    }

    /// Submitting after exceeding view limit should NOT grant reward
    func testSubmitReport_AfterViewLimit_NoReward() {
        for _ in 1...11 {
            service.recordPlanView()
        }

        _ = service.submitReport(makeValidReport())

        XCTAssertFalse(service.hasEarnedFreeYear,
                       "Should not earn reward after exceeding view limit")
    }

    /// Invalid report should NOT grant reward even if eligible
    func testSubmitReport_InvalidReport_NoReward() {
        _ = service.submitReport(makeShortReport())

        XCTAssertFalse(service.hasEarnedFreeYear,
                       "Invalid report should not trigger reward")
    }

    // MARK: - Free Year Active Status

    /// Free year should be active if earned recently
    func testIsFreeYearActive_RecentlyEarned() {
        service.hasEarnedFreeYear = true
        service.freeYearEarnedDate = Date()

        XCTAssertTrue(service.isFreeYearActive,
                      "Free year earned today should be active")
    }

    /// Free year should be inactive if earned more than 1 year ago
    func testIsFreeYearActive_Expired() {
        service.hasEarnedFreeYear = true
        service.freeYearEarnedDate = Calendar.current.date(byAdding: .year, value: -2, to: Date())

        XCTAssertFalse(service.isFreeYearActive,
                       "Free year should be inactive after 1 year")
    }

    /// Free year should be inactive if never earned
    func testIsFreeYearActive_NeverEarned() {
        XCTAssertFalse(service.isFreeYearActive,
                       "Free year should be inactive if never earned")
    }

    /// Free year should be inactive if hasEarned is true but no date
    func testIsFreeYearActive_NoDate() {
        service.hasEarnedFreeYear = true
        service.freeYearEarnedDate = nil

        XCTAssertFalse(service.isFreeYearActive,
                       "Free year should be inactive without an earned date")
    }

    // MARK: - Free Year Expiration Date

    /// Expiration should be exactly 1 year after earned date
    func testFreeYearExpirationDate() {
        let earnedDate = Date()
        service.freeYearEarnedDate = earnedDate

        let expectedExpiration = Calendar.current.date(byAdding: .year, value: 1, to: earnedDate)
        XCTAssertEqual(service.freeYearExpirationDate, expectedExpiration,
                       "Expiration should be 1 year after earned date")
    }

    /// Expiration should be nil if no earned date
    func testFreeYearExpirationDate_Nil() {
        XCTAssertNil(service.freeYearExpirationDate,
                     "Expiration should be nil if never earned")
    }

    // MARK: - Report Sent Tracking

    /// New reports should have wasSent = false
    func testNewReport_NotSent() {
        _ = service.submitReport(makeValidReport())
        let report = service.submittedReports.first
        XCTAssertNotNil(report)
        XCTAssertFalse(report!.wasSent, "New reports should not be marked as sent")
    }

    /// markReportAsSent should flag a specific report
    func testMarkReportAsSent() {
        _ = service.submitReport(makeValidReport())
        let reportId = service.submittedReports.first!.id

        service.markReportAsSent(reportId)

        let updatedReport = service.submittedReports.first { $0.id == reportId }
        XCTAssertTrue(updatedReport!.wasSent, "Report should be marked as sent")
    }

    /// markAllReportsAsSent should flag all reports
    func testMarkAllReportsAsSent() {
        _ = service.submitReport(makeValidReport(planId: "plan-1"))
        _ = service.submitReport(makeValidReport(planId: "plan-2"))

        service.markAllReportsAsSent()

        let allSent = service.submittedReports.allSatisfy { $0.wasSent }
        XCTAssertTrue(allSent, "All reports should be marked as sent")
    }

    /// unsentReportCount should reflect unsent reports only
    func testUnsentReportCount() {
        _ = service.submitReport(makeValidReport(planId: "plan-1"))
        _ = service.submitReport(makeValidReport(planId: "plan-2"))

        XCTAssertEqual(service.unsentReportCount, 2, "Both reports should be unsent initially")

        let firstId = service.submittedReports.first!.id
        service.markReportAsSent(firstId)

        XCTAssertEqual(service.unsentReportCount, 1, "One report should remain unsent")
    }

    // MARK: - Report Formatting

    /// formatReportForEmail should include key fields
    func testFormatReportForEmail() {
        let report = makeValidReport()
        let formatted = service.formatReportForEmail(report)

        XCTAssertTrue(formatted.contains("CLINICAL ERROR REPORT"),
                      "Should contain report header")
        XCTAssertTrue(formatted.contains("Acute Migraine"),
                      "Should contain plan title")
        XCTAssertTrue(formatted.contains("migraine"),
                      "Should contain plan ID")
        XCTAssertTrue(formatted.contains("Medication Dosing"),
                      "Should contain category")
        XCTAssertTrue(formatted.contains("Major"),
                      "Should contain severity")
    }

    /// formatUnsentReportsForEmail should return empty string when no unsent reports
    func testFormatUnsentReports_Empty() {
        let formatted = service.formatUnsentReportsForEmail()
        XCTAssertEqual(formatted, "",
                       "Should return empty string when no unsent reports exist")
    }

    /// formatUnsentReportsForEmail should include report count
    func testFormatUnsentReports_IncludesCount() {
        _ = service.submitReport(makeValidReport(planId: "plan-1"))
        _ = service.submitReport(makeValidReport(planId: "plan-2"))

        let formatted = service.formatUnsentReportsForEmail()
        XCTAssertTrue(formatted.contains("Total Reports: 2"),
                      "Should include total report count")
    }

    // MARK: - ClinicalErrorReport Model

    /// Report should auto-generate UUID and timestamp
    func testReportModel_AutoFields() {
        let report = makeValidReport()
        XCTAssertFalse(report.id.uuidString.isEmpty, "Should have a valid UUID")
        XCTAssertFalse(report.wasSent, "Should default to not sent")
    }

    /// ErrorCategory should have all expected cases
    func testErrorCategory_AllCases() {
        XCTAssertEqual(ClinicalErrorReport.ErrorCategory.allCases.count, 10,
                       "Should have 10 error categories")
    }

    /// ErrorSeverity should have all expected cases
    func testErrorSeverity_AllCases() {
        XCTAssertEqual(ClinicalErrorReport.ErrorSeverity.allCases.count, 4,
                       "Should have 4 severity levels: Critical, Major, Minor, Suggestion")
    }

    /// Each severity should have a description
    func testErrorSeverity_Descriptions() {
        XCTAssertEqual(ClinicalErrorReport.ErrorSeverity.critical.description,
                       "Could cause patient harm")
        XCTAssertEqual(ClinicalErrorReport.ErrorSeverity.major.description,
                       "Significant clinical impact")
        XCTAssertEqual(ClinicalErrorReport.ErrorSeverity.minor.description,
                       "Minor inaccuracy")
        XCTAssertEqual(ClinicalErrorReport.ErrorSeverity.suggestion.description,
                       "Improvement suggestion")
    }
}
