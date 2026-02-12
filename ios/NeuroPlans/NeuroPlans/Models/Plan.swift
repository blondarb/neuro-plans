import Foundation

// MARK: - Top-level Plan

struct Plan: Codable, Identifiable, Hashable {
    let id: String
    let title: String
    let version: String
    let icd10: [String]
    let scope: String
    let notes: [String]
    let sections: PlanSections
    let differential: [DifferentialItem]
    let evidence: [EvidenceItem]
    let monitoring: [MonitoringItem]
    let disposition: [DispositionItem]

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: Plan, rhs: Plan) -> Bool { lhs.id == rhs.id }
}

// MARK: - Sections Container

struct PlanSections: Codable {
    let labWorkup: [String: [LabItem]]
    let imaging: [String: [ImagingItem]]
    let treatment: [String: [TreatmentItem]]
    let otherRecs: [String: [OtherRecItem]]

    enum CodingKeys: String, CodingKey {
        case labWorkup = "Laboratory Workup"
        case imaging = "Imaging & Studies"
        case treatment = "Treatment"
        case otherRecs = "Other Recommendations"
    }
}

// MARK: - Setting Priority

enum ClinicalSetting: String, CaseIterable, Identifiable, Codable {
    case ed = "ED"
    case hosp = "HOSP"
    case opd = "OPD"
    case icu = "ICU"

    var id: String { rawValue }

    var label: String {
        switch self {
        case .ed: "Emergency"
        case .hosp: "Hospital"
        case .opd: "Outpatient"
        case .icu: "ICU"
        }
    }

    var icon: String {
        switch self {
        case .ed: "cross.case.fill"
        case .hosp: "bed.double.fill"
        case .opd: "building.2.fill"
        case .icu: "waveform.path.ecg"
        }
    }
}

enum Priority: String, Comparable {
    case stat = "STAT"
    case urgent = "URGENT"
    case routine = "ROUTINE"
    case ext = "EXT"
    case na = "-"

    var sortOrder: Int {
        switch self {
        case .stat: 0
        case .urgent: 1
        case .routine: 2
        case .ext: 3
        case .na: 4
        }
    }

    var isApplicable: Bool { self != .na }

    static func < (lhs: Priority, rhs: Priority) -> Bool {
        lhs.sortOrder < rhs.sortOrder
    }
}

// MARK: - Lab Item

struct LabItem: Codable, Identifiable {
    let item: String
    let rationale: String?
    let target: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item }

    func priority(for setting: ClinicalSetting) -> Priority {
        let raw: String?
        switch setting {
        case .ed: raw = ED
        case .hosp: raw = HOSP
        case .opd: raw = OPD
        case .icu: raw = ICU
        }
        return Priority(rawValue: raw ?? "-") ?? .na
    }
}

// MARK: - Imaging Item

struct ImagingItem: Codable, Identifiable {
    let item: String
    let timing: String?
    let target: String?
    let contraindications: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item }

    func priority(for setting: ClinicalSetting) -> Priority {
        let raw: String?
        switch setting {
        case .ed: raw = ED
        case .hosp: raw = HOSP
        case .opd: raw = OPD
        case .icu: raw = ICU
        }
        return Priority(rawValue: raw ?? "-") ?? .na
    }
}

// MARK: - Treatment Item

struct TreatmentItem: Codable, Identifiable {
    let item: String
    let route: String?
    let indication: String?
    let dosing: Dosing?
    let contraindications: String?
    let monitoring: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item }

    func priority(for setting: ClinicalSetting) -> Priority {
        let raw: String?
        switch setting {
        case .ed: raw = ED
        case .hosp: raw = HOSP
        case .opd: raw = OPD
        case .icu: raw = ICU
        }
        return Priority(rawValue: raw ?? "-") ?? .na
    }
}

struct Dosing: Codable {
    let doseOptions: [DoseOption]?
    let route: String?
    let frequency: String?
    let instructions: String?
    let orderSentence: String?
}

struct DoseOption: Codable, Identifiable {
    let text: String
    let orderSentence: String?

    var id: String { text }
}

// MARK: - Other Recommendations

struct OtherRecItem: Codable, Identifiable {
    let item: String
    let rationale: String?
    let timing: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item }

    func priority(for setting: ClinicalSetting) -> Priority {
        let raw: String?
        switch setting {
        case .ed: raw = ED
        case .hosp: raw = HOSP
        case .opd: raw = OPD
        case .icu: raw = ICU
        }
        return Priority(rawValue: raw ?? "-") ?? .na
    }
}

// MARK: - Reference Sections

struct DifferentialItem: Codable, Identifiable {
    let condition: String?
    let features: String?
    let distinguishing: String?

    var id: String { condition ?? UUID().uuidString }
}

struct EvidenceItem: Codable, Identifiable {
    let reference: String?
    let summary: String?
    let grade: String?

    var id: String { reference ?? UUID().uuidString }
}

struct MonitoringItem: Codable, Identifiable {
    let parameter: String?
    let frequency: String?
    let target: String?
    let action: String?

    var id: String { parameter ?? UUID().uuidString }
}

struct DispositionItem: Codable, Identifiable {
    let setting: String?
    let criteria: String?
    let notes: String?

    var id: String { setting ?? UUID().uuidString }
}

// MARK: - Unified Selectable Item (for builder)

struct SelectedItem: Identifiable, Hashable {
    let id = UUID()
    let planId: String
    let planTitle: String
    let section: String
    let subsection: String
    let itemText: String
    var customText: String?
    let priority: Priority
    let orderSentence: String?

    var displayText: String { customText ?? itemText }
}
