import Foundation
import Supabase

/// Centralized Supabase client and helper methods
enum SupabaseService {
    // MARK: - Client

    static let client = SupabaseClient(
        supabaseURL: URL(string: "https://cyaginuvsqcbvyeuizlu.supabase.co")!,
        supabaseKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN5YWdpbnV2c3FjYnZ5ZXVpemx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEwMDY5NjUsImV4cCI6MjA4NjU4Mjk2NX0.UGJN-vnfGy7eECbmT33g4-OXME-2bbwC9sm3ckOmpWA"
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

        enum CodingKeys: String, CodingKey {
            case email, domain
            case isWhitelisted = "is_whitelisted"
        }
    }

    // MARK: - Domain Whitelist

    /// Fetch active whitelisted domains from Supabase
    static func fetchWhitelistedDomains() async throws -> [String] {
        let domains: [WhitelistedDomain] = try await client
            .from("whitelisted_domains")
            .select()
            .eq("is_active", value: true)
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
            isWhitelisted: isWhitelisted
        )

        try await client
            .from("verified_emails")
            .insert(record)
            .execute()
    }
}
