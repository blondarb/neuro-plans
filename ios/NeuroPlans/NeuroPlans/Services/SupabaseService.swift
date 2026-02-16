import Foundation
import Supabase

/// Centralized Supabase client and helper methods
enum SupabaseService {
    // MARK: - Client

    static let client = SupabaseClient(
        supabaseURL: URL(string: SpecialtyConfig.supabaseUrl)!,
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
}
