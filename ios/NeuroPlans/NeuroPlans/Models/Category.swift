import Foundation

struct PlanCategory: Identifiable, Hashable {
    let id: String
    let name: String
    let icon: String
    let color: String
    let planIds: [String]

    var count: Int { planIds.count }
}

// Category definitions matching mkdocs.yml nav structure
extension PlanCategory {
    static let all: [PlanCategory] = [
        PlanCategory(
            id: "seizure-epilepsy",
            name: "Seizures & Epilepsy",
            icon: "bolt.fill",
            color: "purple",
            planIds: [
                "status-epilepticus", "ncse", "new-onset-seizure",
                "breakthrough-seizure", "alcohol-withdrawal-seizure",
                "drug-resistant-epilepsy", "epilepsy-chronic-management",
                "eclampsia-seizure-pregnancy"
            ]
        ),
        PlanCategory(
            id: "stroke-vascular",
            name: "Stroke & Vascular",
            icon: "heart.circle.fill",
            color: "red",
            planIds: [
                "acute-ischemic-stroke", "transient-ischemic-attack",
                "intracerebral-hemorrhage", "subarachnoid-hemorrhage",
                "cerebral-venous-thrombosis", "cervical-artery-dissection",
                "pres", "rcvs", "moyamoya-disease", "post-stroke-management",
                "carotid-stenosis", "hypertensive-encephalopathy"
            ]
        ),
        PlanCategory(
            id: "neuromuscular",
            name: "Neuromuscular",
            icon: "figure.walk",
            color: "orange",
            planIds: [
                "guillain-barre-syndrome", "cidp",
                "myasthenia-gravis-crisis", "myasthenia-gravis-new-diagnosis",
                "neuromuscular-respiratory-failure", "peripheral-neuropathy",
                "diabetic-neuropathy", "myasthenia-gravis", "als",
                "small-fiber-neuropathy", "carpal-tunnel-syndrome",
                "radiculopathy", "lambert-eaton-syndrome",
                "critical-illness-myopathy-neuropathy",
                "inflammatory-myopathy", "inclusion-body-myositis",
                "myotonic-dystrophy", "peroneal-neuropathy", "plexopathy",
                "ulnar-neuropathy", "chemotherapy-induced-neuropathy",
                "vasculitic-neuropathy", "multifocal-motor-neuropathy",
                "muscular-dystrophy-adult", "hereditary-neuropathy-cmt",
                "autonomic-neuropathy"
            ]
        ),
        PlanCategory(
            id: "cns-infections",
            name: "CNS Infections",
            icon: "microbe.fill",
            color: "green",
            planIds: [
                "bacterial-meningitis", "hsv-encephalitis",
                "autoimmune-encephalitis", "viral-meningitis",
                "brain-abscess", "fungal-meningitis", "tb-meningitis",
                "neurosyphilis", "lyme-neuroborreliosis", "botulism",
                "neurocysticercosis", "hiv-associated-neurocognitive-disorder",
                "pml"
            ]
        ),
        PlanCategory(
            id: "spinal",
            name: "Spinal Cord",
            icon: "figure.stand",
            color: "indigo",
            planIds: [
                "acute-myelopathy", "spinal-cord-compression-malignant",
                "cauda-equina-syndrome", "epidural-abscess",
                "cervical-myelopathy", "lumbar-stenosis",
                "myelopathy-general", "syringomyelia",
                "subacute-combined-degeneration"
            ]
        ),
        PlanCategory(
            id: "neuro-oncology",
            name: "Neuro-Oncology",
            icon: "brain.fill",
            color: "pink",
            planIds: [
                "brain-metastases", "glioblastoma",
                "leptomeningeal-carcinomatosis",
                "paraneoplastic-neurological-syndrome", "meningioma",
                "primary-cns-lymphoma", "radiation-neurologic-injury"
            ]
        ),
        PlanCategory(
            id: "critical-care",
            name: "Critical Care",
            icon: "waveform.path.ecg.rectangle.fill",
            color: "red",
            planIds: [
                "elevated-icp-management", "brain-death-evaluation",
                "anoxic-brain-injury", "acute-tbi-management",
                "metabolic-encephalopathy", "neurotoxicology"
            ]
        ),
        PlanCategory(
            id: "demyelinating",
            name: "Demyelinating",
            icon: "circle.dotted",
            color: "blue",
            planIds: [
                "ms-new-diagnosis", "ms-chronic-management",
                "optic-neuritis", "nmosd", "mogad", "adem",
                "diffuse-white-matter-disease"
            ]
        ),
        PlanCategory(
            id: "headache",
            name: "Headache",
            icon: "head.profile.arrow.forward.and.visionpro",
            color: "yellow",
            planIds: [
                "migraine", "cluster-headache",
                "medication-overuse-headache", "migraine-with-aura",
                "tension-headache", "chronic-migraine",
                "low-pressure-headache", "status-migrainosus",
                "headache-evaluation", "thunderclap-headache-evaluation",
                "headache-unspecified", "new-daily-persistent-headache"
            ]
        ),
        PlanCategory(
            id: "movement-disorders",
            name: "Movement Disorders",
            icon: "hand.raised.fingers.spread.fill",
            color: "teal",
            planIds: [
                "parkinsons-disease", "parkinsons-disease-new-diagnosis",
                "essential-tremor", "restless-legs-syndrome", "dystonia",
                "huntingtons-disease", "tardive-dyskinesia",
                "drug-induced-parkinsonism", "wilsons-disease",
                "progressive-supranuclear-palsy", "multiple-system-atrophy",
                "ataxia-evaluation", "tics-tourette-syndrome",
                "tremor-unspecified", "corticobasal-degeneration",
                "chorea-evaluation", "parkinsons-motor-fluctuations",
                "parkinsons-psychosis"
            ]
        ),
        PlanCategory(
            id: "dementia-cognitive",
            name: "Dementia & Cognitive",
            icon: "brain.head.profile.fill",
            color: "purple",
            planIds: [
                "dementia-evaluation", "rapidly-progressive-dementia",
                "alzheimers-disease", "frontotemporal-dementia",
                "lewy-body-dementia", "vascular-dementia",
                "mild-cognitive-impairment", "normal-pressure-hydrocephalus",
                "creutzfeldt-jakob-disease", "delirium-vs-dementia",
                "autoimmune-dementia", "chronic-traumatic-encephalopathy",
                "wernicke-korsakoff-syndrome"
            ]
        ),
        PlanCategory(
            id: "functional",
            name: "Functional Disorders",
            icon: "brain.filled.head.profile",
            color: "cyan",
            planIds: [
                "functional-neurological-disorder", "pnes",
                "functional-movement-disorder",
                "functional-cognitive-disorder"
            ]
        ),
        PlanCategory(
            id: "headache-cranial",
            name: "Cranial Neuropathies",
            icon: "face.smiling",
            color: "mint",
            planIds: [
                "bells-palsy", "trigeminal-neuralgia", "horner-syndrome"
            ]
        ),
        PlanCategory(
            id: "inflammatory",
            name: "Inflammatory",
            icon: "flame.fill",
            color: "orange",
            planIds: [
                "neurosarcoidosis", "stiff-person-syndrome",
                "hashimotos-encephalopathy", "idiopathic-intracranial-hypertension"
            ]
        ),
        PlanCategory(
            id: "vasculitis",
            name: "Vasculitis",
            icon: "drop.triangle.fill",
            color: "red",
            planIds: [
                "giant-cell-arteritis", "cns-vasculitis",
                "susac-syndrome", "neuro-behcets-disease"
            ]
        ),
        PlanCategory(
            id: "sleep",
            name: "Sleep Medicine",
            icon: "moon.fill",
            color: "indigo",
            planIds: [
                "narcolepsy", "rem-sleep-behavior-disorder",
                "obstructive-sleep-apnea-neuro", "insomnia-neurological",
                "idiopathic-hypersomnia", "non-rem-parasomnias"
            ]
        ),
        PlanCategory(
            id: "autonomic-pain",
            name: "Autonomic & Pain",
            icon: "bolt.heart.fill",
            color: "pink",
            planIds: [
                "pots", "neurogenic-orthostatic-hypotension",
                "occipital-neuralgia", "crps",
                "neuropathic-pain-management"
            ]
        ),
        PlanCategory(
            id: "other",
            name: "Other",
            icon: "ellipsis.circle.fill",
            color: "gray",
            planIds: [
                "vertigo-dizziness-evaluation", "post-concussion-syndrome",
                "nystagmus-evaluation", "tinnitus-evaluation",
                "paresthesia-numbness-tingling", "gait-disorder-evaluation",
                "syncope", "wernicke-encephalopathy",
                "b12-deficiency-neuropathy"
            ]
        ),
    ]

    static func category(for planId: String) -> PlanCategory? {
        all.first { $0.planIds.contains(planId) }
    }
}
