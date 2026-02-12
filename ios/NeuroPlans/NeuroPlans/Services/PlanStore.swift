import Foundation
import SwiftUI

@Observable
final class PlanStore {

    // MARK: - Published State

    var plans: [String: Plan] = [:]
    var favorites: Set<String> = []
    var selectedSetting: ClinicalSetting = .opd
    var searchText: String = ""
    var isLoaded = false

    // MARK: - Computed

    var allPlans: [Plan] {
        plans.values.sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }
    }

    var filteredPlans: [Plan] {
        guard !searchText.isEmpty else { return allPlans }
        let query = searchText.lowercased()
        return allPlans.filter { plan in
            plan.title.lowercased().contains(query)
            || plan.id.lowercased().contains(query)
            || plan.icd10.contains { $0.lowercased().contains(query) }
            || plan.scope.lowercased().contains(query)
        }
    }

    var favoritePlans: [Plan] {
        allPlans.filter { favorites.contains($0.id) }
    }

    var categories: [PlanCategory] {
        PlanCategory.all.filter { cat in
            cat.planIds.contains { plans[$0] != nil }
        }
    }

    // MARK: - Init

    init() {
        loadFavorites()
    }

    // MARK: - Data Loading

    func loadPlans() async {
        guard !isLoaded else { return }
        do {
            guard let url = Bundle.main.url(forResource: "plans", withExtension: "json") else {
                print("plans.json not found in bundle")
                return
            }
            let data = try Data(contentsOf: url)
            let decoded = try JSONDecoder().decode([String: Plan].self, from: data)
            await MainActor.run {
                self.plans = decoded
                self.isLoaded = true
            }
        } catch {
            print("Failed to load plans: \(error)")
        }
    }

    // MARK: - Plan Access

    func plan(for id: String) -> Plan? {
        plans[id]
    }

    func plans(for category: PlanCategory) -> [Plan] {
        category.planIds.compactMap { plans[$0] }
            .sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }
    }

    // MARK: - Favorites

    func toggleFavorite(_ planId: String) {
        if favorites.contains(planId) {
            favorites.remove(planId)
        } else {
            favorites.insert(planId)
        }
        saveFavorites()
    }

    func isFavorite(_ planId: String) -> Bool {
        favorites.contains(planId)
    }

    private func saveFavorites() {
        UserDefaults.standard.set(Array(favorites), forKey: "favorites")
    }

    private func loadFavorites() {
        if let saved = UserDefaults.standard.stringArray(forKey: "favorites") {
            favorites = Set(saved)
        }
    }

    // MARK: - Recents

    private(set) var recentPlanIds: [String] = [] {
        didSet {
            UserDefaults.standard.set(recentPlanIds, forKey: "recents")
        }
    }

    var recentPlans: [Plan] {
        recentPlanIds.compactMap { plans[$0] }
    }

    func markViewed(_ planId: String) {
        recentPlanIds.removeAll { $0 == planId }
        recentPlanIds.insert(planId, at: 0)
        if recentPlanIds.count > 10 {
            recentPlanIds = Array(recentPlanIds.prefix(10))
        }
    }

    func loadRecents() {
        if let saved = UserDefaults.standard.stringArray(forKey: "recents") {
            recentPlanIds = saved
        }
    }
}
