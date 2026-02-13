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
    let differential: [DifferentialItem]?
    let evidence: [EvidenceItem]?
    let monitoring: [MonitoringItem]?
    let disposition: [DispositionItem]?

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

struct LabItem: Codable, Identifiable, SettingFilterable {
    let item: String?
    let rationale: String?
    let target: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item ?? rationale ?? UUID().uuidString }
    var displayText: String { item ?? rationale ?? "" }

    /// True if this item has no applicable venue-specific priorities (reference/guidance item)
    var isReferenceItem: Bool {
        let edNA = ED == nil || ED == "-"
        let hospNA = HOSP == nil || HOSP == "-"
        let opdNA = OPD == nil || OPD == "-"
        let icuNA = ICU == nil || ICU == "-"
        return edNA && hospNA && opdNA && icuNA
    }

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
    
    func isVisible(for setting: ClinicalSetting) -> Bool {
        !displayText.isEmpty && (priority(for: setting).isApplicable || isReferenceItem)
    }
}

// MARK: - Imaging Item

struct ImagingItem: Codable, Identifiable, SettingFilterable {
    let item: String?
    let timing: String?
    let target: String?
    let contraindications: String?
    let rationale: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item ?? timing ?? UUID().uuidString }
    var displayText: String { item ?? "" }

    /// True if this item has no applicable venue-specific priorities (reference/guidance item)
    var isReferenceItem: Bool {
        let edNA = ED == nil || ED == "-"
        let hospNA = HOSP == nil || HOSP == "-"
        let opdNA = OPD == nil || OPD == "-"
        let icuNA = ICU == nil || ICU == "-"
        return edNA && hospNA && opdNA && icuNA
    }

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
    
    func isVisible(for setting: ClinicalSetting) -> Bool {
        !displayText.isEmpty && (priority(for: setting).isApplicable || isReferenceItem)
    }
}

// MARK: - Treatment Item

struct TreatmentItem: Codable, Identifiable, SettingFilterable {
    let item: String?
    let route: String?
    let indication: String?
    let dosing: Dosing?
    let dosingString: String?
    let contraindications: String?
    let monitoring: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?
    // Additional fields for reference-style items (like ASM adjustment strategies)
    let rationale: String?
    let therapeuticRange: String?
    let adjustmentNotes: String?

    var id: String { item ?? indication ?? dosingString ?? UUID().uuidString }
    var displayText: String { item ?? indication ?? dosingString ?? "" }

    /// True if this item has no applicable venue-specific priorities (reference/guidance item)
    /// This includes items where all venue columns are nil OR all are "-"
    var isReferenceItem: Bool {
        let edNA = ED == nil || ED == "-"
        let hospNA = HOSP == nil || HOSP == "-"
        let opdNA = OPD == nil || OPD == "-"
        let icuNA = ICU == nil || ICU == "-"
        return edNA && hospNA && opdNA && icuNA
    }

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
    
    func isVisible(for setting: ClinicalSetting) -> Bool {
        !displayText.isEmpty && (priority(for: setting).isApplicable || isReferenceItem)
    }

    enum CodingKeys: String, CodingKey {
        case item, route, indication, dosing, contraindications, monitoring
        case ED, HOSP, OPD, ICU
        case rationale
        case therapeuticRange = "therapeutic range"
        case adjustmentNotes = "adjustment notes"
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        item = try container.decodeIfPresent(String.self, forKey: .item)
        route = try container.decodeIfPresent(String.self, forKey: .route)
        indication = try container.decodeIfPresent(String.self, forKey: .indication)
        contraindications = try container.decodeIfPresent(String.self, forKey: .contraindications)
        monitoring = try container.decodeIfPresent(String.self, forKey: .monitoring)
        ED = try container.decodeIfPresent(String.self, forKey: .ED)
        HOSP = try container.decodeIfPresent(String.self, forKey: .HOSP)
        OPD = try container.decodeIfPresent(String.self, forKey: .OPD)
        ICU = try container.decodeIfPresent(String.self, forKey: .ICU)
        rationale = try container.decodeIfPresent(String.self, forKey: .rationale)
        therapeuticRange = try container.decodeIfPresent(String.self, forKey: .therapeuticRange)
        adjustmentNotes = try container.decodeIfPresent(String.self, forKey: .adjustmentNotes)

        // Handle dosing as either a Dosing object or a plain string
        if let dosingObj = try? container.decodeIfPresent(Dosing.self, forKey: .dosing) {
            dosing = dosingObj
            dosingString = nil
        } else if let dosingStr = try? container.decodeIfPresent(String.self, forKey: .dosing) {
            dosing = nil
            dosingString = dosingStr
        } else {
            dosing = nil
            dosingString = nil
        }
    }
}

struct Dosing: Codable {
    let doseOptions: [DoseOption]?
    let route: String?
    let frequency: String?
    let instructions: String?
    let orderSentence: String?
}

struct DoseOption: Codable, Identifiable, Hashable {
    let text: String
    let orderSentence: String?

    var id: String { text }
}

// MARK: - Other Recommendations

struct OtherRecItem: Codable, Identifiable, SettingFilterable {
    let item: String?
    let rationale: String?
    let timing: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item ?? rationale ?? UUID().uuidString }
    var displayText: String { item ?? rationale ?? "" }

    /// True if this item has no applicable venue-specific priorities (reference/guidance item)
    var isReferenceItem: Bool {
        let edNA = ED == nil || ED == "-"
        let hospNA = HOSP == nil || HOSP == "-"
        let opdNA = OPD == nil || OPD == "-"
        let icuNA = ICU == nil || ICU == "-"
        return edNA && hospNA && opdNA && icuNA
    }

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
    
    func isVisible(for setting: ClinicalSetting) -> Bool {
        !displayText.isEmpty && (priority(for: setting).isApplicable || isReferenceItem)
    }
}

// MARK: - Reference Sections

struct DifferentialItem: Codable, Identifiable {
    let diagnosis: String?      // JSON uses "diagnosis"
    let features: String?
    let tests: String?          // JSON uses "tests" for distinguishing tests

    var id: String { diagnosis ?? UUID().uuidString }
    
    // Computed property for backward compatibility with views
    var condition: String? { diagnosis }
    var distinguishing: String? { tests }
}

struct EvidenceItem: Codable, Identifiable {
    let recommendation: String? // JSON uses "recommendation"
    let evidenceLevel: String?  // JSON uses "evidenceLevel"
    let source: String?         // JSON uses "source" for the reference links

    var id: String { recommendation ?? UUID().uuidString }
    
    // Computed properties for view compatibility
    var reference: String? { recommendation }
    var grade: String? { evidenceLevel }
    var summary: String? { source }
}

struct MonitoringItem: Codable, Identifiable {
    let item: String?           // JSON uses "item"
    let frequency: String?
    let action: String?
    let ED: String?
    let HOSP: String?
    let OPD: String?
    let ICU: String?

    var id: String { item ?? UUID().uuidString }
    
    // Computed property for backward compatibility
    var parameter: String? { item }
}

struct DispositionItem: Codable, Identifiable {
    let disposition: String?    // JSON uses "disposition"
    let criteria: String?

    var id: String { disposition ?? UUID().uuidString }
    
    // Computed property for backward compatibility
    var setting: String? { disposition }
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
    var customNote: String?  // User-added note/comment for this item
    let priority: Priority
    let orderSentence: String?
    
    // Dose options for treatments with multiple dosing choices
    let doseOptions: [DoseOption]?
    var selectedDoseIndex: Int?

    var displayText: String { customText ?? itemText }
    var hasCustomNote: Bool { customNote != nil && !(customNote?.isEmpty ?? true) }
    var hasDoseOptions: Bool { doseOptions != nil && !(doseOptions?.isEmpty ?? true) }
    
    /// Returns the currently selected order sentence (from dose picker or default)
    var currentOrderSentence: String? {
        if let options = doseOptions, let idx = selectedDoseIndex, idx < options.count {
            return options[idx].orderSentence
        }
        return orderSentence
    }
    
    /// Returns the currently selected dose text for display
    var selectedDoseText: String? {
        if let options = doseOptions, let idx = selectedDoseIndex, idx < options.count {
            return options[idx].text
        }
        return nil
    }
}
