import Foundation

/// All specialty-specific values in one place.
/// To create a new specialty app, clone this repo and edit only this file
/// (plus Category.swift, Reference.swift, and CalculatorEngine.swift for content).
enum SpecialtyConfig {
    // MARK: - Identity
    static let appName = "Neuro Plans"
    static let specialty = "neurology"
    static let bundleId = "com.neuroplans.app"

    // MARK: - Branding
    static let brandColorHex = "#0D9488"
    static let headerIcon = "brain.head.profile"

    // MARK: - Subscription
    static let storeKitProductId = "com.neuroplans.annual"

    // MARK: - Contact
    static let errorReportEmail = "errors@neuroplans.app"
    static let supportEmail = "support@neuroplans.app"

    // MARK: - Supabase
    static let supabaseUrl = "https://cyaginuvsqcbvyeuizlu.supabase.co"
    static let supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5YWdpbnV2c3FjYnZ5ZXVpemx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMDY5NjUsImV4cCI6MjA4NjU4Mjk2NX0.UGJN-vnfGy7eECbmT33g4-OXME-2bbwC9sm3ckOmpWA"

    // MARK: - Legal
    static let termsURL = "https://neuroplans.app/terms"
    static let privacyURL = "https://neuroplans.app/privacy"
    static let disclaimerTitle = "Neuro Plans"

    // MARK: - Paywall Features
    /// Features displayed on the paywall screen. Each specialty shows different features.
    static let paywallFeatures: [(icon: String, title: String, description: String)] = [
        ("list.bullet.clipboard.fill", "All Clinical Plans", "Complete neurology treatment protocols"),
        ("brain", "Clinical Scales", "NIHSS, mRS, GCS, and more"),
        ("stethoscope", "Exam Guides", "Step-by-step neurological exams"),
        ("hammer.fill", "Clinical Tools", "Calculators, timers, and converters"),
        ("square.and.pencil", "Plan Builder", "Create custom order sets"),
        ("arrow.triangle.2.circlepath", "Free Updates", "New plans and features as they're released")
    ]

    // MARK: - Quick Actions
    /// Specialty-specific shortcuts shown on the home screen.
    /// Each links to a plan by its ID for one-tap access.
    static let quickActions: [(id: String, title: String, icon: String, planId: String)] = [
        ("stroke-alert", "Stroke Alert", "bolt.heart.fill", "acute-ischemic-stroke"),
        ("status-epilepticus", "Status Epilepticus", "waveform.path.ecg", "status-epilepticus"),
        ("meningitis", "Acute Meningitis", "allergens.fill", "bacterial-meningitis")
    ]
}
