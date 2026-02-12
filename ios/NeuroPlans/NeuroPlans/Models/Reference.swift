import Foundation

// MARK: - Clinical Scale (Interactive Scoring)

struct ClinicalScale: Codable, Identifiable, Hashable {
    let id: String
    let title: String
    let abbreviation: String
    let category: String
    let description: String
    let components: [ScaleComponent]
    let interpretation: [ScoreInterpretation]
    let citation: String?
    let relatedPlans: [String]

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: ClinicalScale, rhs: ClinicalScale) -> Bool { lhs.id == rhs.id }
}

struct ScaleComponent: Codable, Identifiable {
    let id: String
    let name: String
    let options: [ScoreOption]
}

struct ScoreOption: Codable, Identifiable {
    let label: String
    let value: Int
    let description: String?

    var id: String { "\(label)-\(value)" }
}

struct ScoreInterpretation: Codable {
    let min: Double
    let max: Double
    let label: String
    let color: String
    let action: String?
}

// MARK: - Neurological Examination

struct NeurologyExam: Codable, Identifiable, Hashable {
    let id: String
    let title: String
    let category: String
    let description: String
    let steps: [ExamStep]
    let clinicalPearls: [String]
    let relatedPlans: [String]

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: NeurologyExam, rhs: NeurologyExam) -> Bool { lhs.id == rhs.id }
}

struct ExamStep: Codable, Identifiable {
    let id: String
    let title: String
    let instruction: String
    let technique: String?
    let normalResult: String?
    let abnormalResults: [AbnormalFinding]?
}

struct AbnormalFinding: Codable {
    let finding: String
    let significance: String
}

// MARK: - Neurology Tool (Calculator / Protocol / Reference Table)

struct NeurologyTool: Codable, Identifiable, Hashable {
    let id: String
    let title: String
    let category: String
    let description: String
    let inputs: [ToolInput]?
    let formula: String?
    let resultLabel: String?
    let resultUnit: String?
    let normalRange: String?
    let interpretation: [ScoreInterpretation]?
    let stages: [ProtocolStage]?
    let tableData: TableContent?
    let clinicalPearls: [String]?
    let relatedPlans: [String]

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: NeurologyTool, rhs: NeurologyTool) -> Bool { lhs.id == rhs.id }
}

struct ToolInput: Codable, Identifiable {
    let id: String
    let label: String
    let unit: String?
    let type: String
    let placeholder: String?
    let options: [String]?
}

struct ProtocolStage: Codable, Identifiable {
    let id: String
    let time: String
    let title: String
    let steps: [String]
}

struct TableContent: Codable {
    let columns: [String]
    let rows: [[String]]
}

// MARK: - Reference Categories

struct ReferenceScaleCategory: Identifiable, Hashable {
    let id: String
    let name: String
    let icon: String
    let color: String
    let scaleIds: [String]

    var count: Int { scaleIds.count }

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: ReferenceScaleCategory, rhs: ReferenceScaleCategory) -> Bool { lhs.id == rhs.id }
}

extension ReferenceScaleCategory {
    static let all: [ReferenceScaleCategory] = [
        ReferenceScaleCategory(
            id: "stroke",
            name: "Stroke & Vascular",
            icon: "heart.circle.fill",
            color: "red",
            scaleIds: [
                "nihss", "mrs", "barthel-index", "abcd2", "cha2ds2-vasc",
                "has-bled", "ich-score", "hunt-hess", "fisher-scale",
                "modified-fisher", "wfns-grade", "aspects"
            ]
        ),
        ReferenceScaleCategory(
            id: "consciousness",
            name: "Consciousness & Coma",
            icon: "brain.fill",
            color: "purple",
            scaleIds: [
                "gcs", "four-score", "ranchos-los-amigos"
            ]
        ),
        ReferenceScaleCategory(
            id: "cognitive",
            name: "Cognitive & Dementia",
            icon: "brain.head.profile.fill",
            color: "indigo",
            scaleIds: [
                "mmse", "moca", "mini-cog", "phq9", "gad7"
            ]
        ),
        ReferenceScaleCategory(
            id: "movement",
            name: "Movement Disorders",
            icon: "hand.raised.fingers.spread.fill",
            color: "teal",
            scaleIds: [
                "hoehn-yahr", "updrs-motor", "schwab-england"
            ]
        ),
        ReferenceScaleCategory(
            id: "neuromuscular",
            name: "Neuromuscular",
            icon: "figure.walk",
            color: "orange",
            scaleIds: [
                "mrc-sum-score", "mgfa-class", "alsfrs-r", "gbs-disability"
            ]
        ),
        ReferenceScaleCategory(
            id: "ms",
            name: "Multiple Sclerosis",
            icon: "circle.dotted",
            color: "blue",
            scaleIds: ["edss"]
        ),
        ReferenceScaleCategory(
            id: "headache",
            name: "Headache",
            icon: "head.profile.arrow.forward.and.visionpro",
            color: "yellow",
            scaleIds: ["hit6", "midas"]
        ),
        ReferenceScaleCategory(
            id: "sleep",
            name: "Sleep",
            icon: "moon.fill",
            color: "indigo",
            scaleIds: ["epworth", "stop-bang"]
        ),
    ]

    static func category(for scaleId: String) -> ReferenceScaleCategory? {
        all.first { $0.scaleIds.contains(scaleId) }
    }
}

struct ReferenceExamCategory: Identifiable, Hashable {
    let id: String
    let name: String
    let icon: String
    let color: String
    let examIds: [String]

    var count: Int { examIds.count }

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: ReferenceExamCategory, rhs: ReferenceExamCategory) -> Bool { lhs.id == rhs.id }
}

extension ReferenceExamCategory {
    static let all: [ReferenceExamCategory] = [
        ReferenceExamCategory(
            id: "core",
            name: "Core Examinations",
            icon: "stethoscope",
            color: "teal",
            examIds: [
                "mental-status-exam", "cranial-nerve-exam", "motor-exam",
                "sensory-exam", "deep-tendon-reflexes", "cerebellar-exam",
                "gait-exam", "fundoscopic-exam", "meningeal-signs",
                "speech-language-exam"
            ]
        ),
        ReferenceExamCategory(
            id: "specialized",
            name: "Specialized Examinations",
            icon: "magnifyingglass",
            color: "blue",
            examIds: [
                "coma-exam", "vestibular-exam", "myasthenia-exam",
                "peripheral-neuropathy-exam", "radiculopathy-exam",
                "myelopathy-exam", "movement-disorder-exam",
                "nerve-entrapment-exam"
            ]
        ),
        ReferenceExamCategory(
            id: "rapid",
            name: "Rapid Assessments",
            icon: "bolt.fill",
            color: "orange",
            examIds: [
                "neuro-screen-5min", "icu-neuro-check"
            ]
        ),
        ReferenceExamCategory(
            id: "special-tests",
            name: "Special Tests & Reflexes",
            icon: "hand.tap.fill",
            color: "purple",
            examIds: [
                "pathological-reflexes"
            ]
        ),
    ]
}

struct ReferenceToolCategory: Identifiable, Hashable {
    let id: String
    let name: String
    let icon: String
    let color: String
    let toolIds: [String]

    var count: Int { toolIds.count }

    func hash(into hasher: inout Hasher) { hasher.combine(id) }
    static func == (lhs: ReferenceToolCategory, rhs: ReferenceToolCategory) -> Bool { lhs.id == rhs.id }
}

extension ReferenceToolCategory {
    static let all: [ReferenceToolCategory] = [
        ReferenceToolCategory(
            id: "calculator",
            name: "Calculators",
            icon: "function",
            color: "blue",
            toolIds: [
                "corrected-phenytoin", "creatinine-clearance", "corrected-sodium",
                "corrected-calcium", "serum-osmolality", "anion-gap",
                "bmi-calculator", "steroid-equivalence", "ivig-dose",
                "mean-arterial-pressure", "cerebral-perfusion-pressure", "ich-volume-abc2",
                "corrected-qtc", "wells-score-dvt", "wells-score-pe", "4ts-score-hit",
                "free-water-deficit", "sodium-correction-rate", "body-surface-area",
                "ideal-body-weight", "meld-score", "levodopa-equivalent-dose",
                "plasmapheresis-volume", "predicted-fvc", "osmol-gap", "lp-opening-pressure-correction"
            ]
        ),
        ReferenceToolCategory(
            id: "protocol",
            name: "Clinical Protocols",
            icon: "list.number",
            color: "red",
            toolIds: [
                "status-epilepticus-protocol", "code-stroke-protocol",
                "brain-death-protocol", "icp-management-protocol",
                "myasthenic-crisis-protocol"
            ]
        ),
        ReferenceToolCategory(
            id: "reference_table",
            name: "Reference Tables",
            icon: "tablecells",
            color: "green",
            toolIds: [
                "csf-analysis", "aed-levels", "dermatome-map",
                "reflex-arc-table", "cranial-nerve-table"
            ]
        ),
        ReferenceToolCategory(
            id: "conversion",
            name: "Conversions",
            icon: "arrow.left.arrow.right",
            color: "purple",
            toolIds: [
                "temp-converter", "weight-converter"
            ]
        ),
    ]
}
