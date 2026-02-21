import Foundation

/// All specialty-specific values in one place.
/// To create a new specialty app, clone this repo and edit only this file
/// (plus Category.swift, Reference.swift, and CalculatorEngine.swift for content).
///
/// Apple App Store Guideline 4.3 requires that apps from the same developer
/// are "sufficiently different" in UI, features, and content. Every property
/// below contributes to making each specialty app visually and functionally
/// distinct. When cloning for a new specialty, change ALL values — not just
/// the identity block.
enum SpecialtyConfig {
    // MARK: - Identity
    static let appName = "Neuro Plans"
    static let specialty = "neurology"
    static let bundleId = "com.neuroplans.app"

    // MARK: - Branding
    static let brandColorHex = "#0D9488"
    /// SF Symbol shown on disclaimer, paywall header, and about section
    static let headerIcon = "brain.head.profile"
    /// Short tagline shown below app name on disclaimer screen
    static let tagline = "Clinical Neurology Decision Support"

    // MARK: - Subscription
    static let storeKitProductId = "com.neuroplans.annual"

    // MARK: - Error Reporting
    static let errorReportEmail = "errors@neuroplans.app"

    // MARK: - Supabase
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5YWdpbnV2c3FjYnZ5ZXVpemx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMDY5NjUsImV4cCI6MjA4NjU4Mjk2NX0.UGJN-vnfGy7eECbmT33g4-OXME-2bbwC9sm3ckOmpWA"

    // MARK: - Legal
    static let termsURL = "https://neuroplans.app/terms"
    static let privacyURL = "https://neuroplans.app/privacy"
    static let disclaimerTitle = "Neuro Plans"
    static let supportEmail = "support@neuroplans.app"

    // MARK: - Paywall Features
    /// Feature rows shown on the paywall screen. Each specialty highlights
    /// its own clinical content so the paywall reads differently.
    static let paywallFeatures: [(icon: String, title: String, description: String)] = [
        ("list.bullet.clipboard.fill", "All Clinical Plans", "Complete neurology treatment protocols for stroke, seizure, MS, and more"),
        ("brain", "Clinical Scales", "NIHSS, mRS, GCS, EDSS, and 20+ validated scoring tools"),
        ("stethoscope", "Neuro Exam Guides", "Step-by-step cranial nerve, motor, and sensory exams"),
        ("hammer.fill", "Exam Tools", "Penlight, OKN stripes, pupil gauge, and red desaturation"),
        ("square.and.pencil", "Plan Builder", "Create custom order sets and export to your EMR"),
        ("arrow.triangle.2.circlepath", "Free Updates", "New plans and features as they're released"),
    ]

    // MARK: - About / Settings
    /// Description shown in the Settings > About section
    static let aboutDescription = "Evidence-based clinical decision support for neurological diagnoses"
    /// SF Symbol shown next to the about description
    static let aboutIcon = "brain.fill"

    // MARK: - Emergency Quick Actions
    /// Specialty-specific emergency protocols shown as quick-access buttons
    /// on the home screen. Each specialty has its own critical pathways.
    static let quickActions: [(id: String, label: String, icon: String, color: String)] = [
        ("acute-ischemic-stroke", "Stroke Alert", "bolt.heart.fill", "red"),
        ("status-epilepticus", "Status Epilepticus", "waveform.path.ecg", "orange"),
        ("new-onset-seizure", "Seizure Workup", "brain.head.profile", "purple"),
    ]
}
