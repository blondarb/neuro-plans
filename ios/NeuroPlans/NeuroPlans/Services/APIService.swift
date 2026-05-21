import Foundation

/// REST client for the Neuro Plans v2 API (replaces Supabase PostgREST calls)
enum APIService {
    // MARK: - Base URL

    static let baseURL = SpecialtyConfig.apiBaseURL

    // MARK: - Models

    struct DomainResponse: Codable {
        let domains: [DomainEntry]
    }

    struct DomainEntry: Codable {
        let domain: String
        let organizationName: String?
        let specialties: [String]?

        enum CodingKeys: String, CodingKey {
            case domain
            case organizationName = "organization_name"
            case specialties
        }
    }

    struct SuccessResponse: Codable {
        let success: Bool
    }

    // MARK: - Domain Whitelist

    /// Fetch active whitelisted domains from the v2 API, filtered by specialty
    static func fetchWhitelistedDomains(for specialty: String) async throws -> [String] {
        guard let url = URL(string: "\(baseURL)/api/domains?specialty=\(specialty)") else {
            throw URLError(.badURL)
        }

        let (data, response) = try await URLSession.shared.data(from: url)

        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }

        let decoded = try JSONDecoder().decode(DomainResponse.self, from: data)
        return decoded.domains.map { $0.domain }
    }

    // MARK: - Analytics

    /// Record a verified email for analytics
    static func recordVerifiedEmail(email: String, domain: String, isWhitelisted: Bool) async throws {
        guard let url = URL(string: "\(baseURL)/api/analytics/verify-email") else {
            throw URLError(.badURL)
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body: [String: Any] = [
            "email": email,
            "domain": domain,
            "is_whitelisted": isWhitelisted,
            "specialty": SpecialtyConfig.specialty
        ]
        request.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (_, response) = try await URLSession.shared.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
    }

    // MARK: - Plan Requests

    /// Submit a plan request (feature request)
    static func submitPlanRequest(text: String) async throws {
        guard let url = URL(string: "\(baseURL)/api/feedback/plan-request") else {
            throw URLError(.badURL)
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let deviceId = getOrCreateDeviceId()
        let body: [String: Any] = [
            "specialty": SpecialtyConfig.specialty,
            "request_text": text,
            "device_id": deviceId
        ]
        request.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (_, response) = try await URLSession.shared.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
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
