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
}
