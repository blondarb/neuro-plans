import Foundation
import Supabase

/// Centralized Supabase client and helper methods
enum SupabaseService {
    // MARK: - Client

    // swiftlint:disable:next force_unwrapping
    private static let supabaseURL: URL = {
        guard let url = URL(string: SpecialtyConfig.supabaseUrl) else {
            fatalError("Invalid Supabase URL in SpecialtyConfig: \(SpecialtyConfig.supabaseUrl)")
        }
        return url
    }()

    static let client = SupabaseClient(
        supabaseURL: supabaseURL,
        supabaseKey: SpecialtyConfig.supabaseAnonKey
    )

    // MARK: - Models

    struct WhitelistedDomain: Codable {
        let id: UUID
        let domain: String
        let organizationName: String?
        let isActive: Bool

        enum CodingKeys: String, CodingKey {
            case id, domain
            case organizationName = "organization_name"
            case isActive = "is_active"
        }
    }

    struct VerifiedEmailRecord: Encodable {
        let email: String
        let domain: String
        let isWhitelisted: Bool
        let specialty: String

        enum CodingKeys: String, CodingKey {
            case email, domain, specialty
            case isWhitelisted = "is_whitelisted"
        }
    }

    // MARK: - Domain Whitelist

    /// Fetch active whitelisted domains from Supabase, filtered by specialty
    static func fetchWhitelistedDomains(for specialty: String) async throws -> [String] {
        let domains: [WhitelistedDomain] = try await client
            .from("whitelisted_domains")
            .select()
            .eq("is_active", value: true)
            .or("specialties.cs.{\(specialty)},specialties.cs.{all}")
            .execute()
            .value

        return domains.map { $0.domain }
    }

    // MARK: - Analytics

    /// Record a verified email for analytics
    static func recordVerifiedEmail(email: String, domain: String, isWhitelisted: Bool) async throws {
        let record = VerifiedEmailRecord(
            email: email,
            domain: domain,
            isWhitelisted: isWhitelisted,
            specialty: SpecialtyConfig.specialty
        )

        try await client
            .from("verified_emails")
            .insert(record)
            .execute()
    }

    // MARK: - Plan Requests

    struct PlanRequestRecord: Encodable {
        let specialty: String
        let requestText: String
        let deviceId: String

        enum CodingKeys: String, CodingKey {
            case specialty
            case requestText = "request_text"
            case deviceId = "device_id"
        }
    }

    static func submitPlanRequest(text: String) async throws {
        let deviceId = getOrCreateDeviceId()
        let record = PlanRequestRecord(
            specialty: SpecialtyConfig.specialty,
            requestText: text,
            deviceId: deviceId
        )
        try await client
            .from("plan_requests")
            .insert(record)
            .execute()
    }

    private static func getOrCreateDeviceId() -> String {
        let key = "plan_request_device_id"
        if let existing = UserDefaults.standard.string(forKey: key) {
            return existing
        }
        let newId = UUID().uuidString
        UserDefaults.standard.set(newId, forKey: key)
        return newId
    }
}
