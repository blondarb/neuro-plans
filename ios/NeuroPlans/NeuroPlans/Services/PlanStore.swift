import Foundation
import SwiftUI

@Observable
final class PlanStore {

    // MARK: - Published State

    var plans: [String: Plan] = [:]
    var favorites: Set<String> = []
    var favoriteItems: Set<String> = []  // "planId::itemText" format for favorite actions
    var selectedSetting: ClinicalSetting = .opd
    var searchText: String = ""
    var isLoaded = false
    var loadingError: String? = nil

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
        loadFavoriteItems()
    }

    // MARK: - Data Loading

    func loadPlans() async {
        guard !isLoaded else { return }
        do {
            guard let url = Bundle.main.url(forResource: "plans", withExtension: "json") else {
                await MainActor.run {
                    self.loadingError = "Clinical plans data file not found."
                    self.isLoaded = true
                }
                return
            }
            let data = try Data(contentsOf: url)
            let decoded = try JSONDecoder().decode([String: Plan].self, from: data)
            await MainActor.run {
                self.plans = decoded
                self.isLoaded = true
            }
        } catch {
            await MainActor.run {
                self.loadingError = "Unable to load clinical plans: \(error.localizedDescription)"
                self.isLoaded = true
            }
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

    // MARK: - Favorite Items (Actions)

    private func itemKey(_ planId: String, _ itemText: String) -> String {
        "\(planId)::\(itemText)"
    }

    func toggleFavoriteItem(_ planId: String, itemText: String) {
        let key = itemKey(planId, itemText)
        if favoriteItems.contains(key) {
            favoriteItems.remove(key)
        } else {
            favoriteItems.insert(key)
        }
        saveFavoriteItems()
    }

    func isFavoriteItem(_ planId: String, itemText: String) -> Bool {
        favoriteItems.contains(itemKey(planId, itemText))
    }

    private func saveFavoriteItems() {
        UserDefaults.standard.set(Array(favoriteItems), forKey: "favoriteItems")
    }

    private func loadFavoriteItems() {
        if let saved = UserDefaults.standard.stringArray(forKey: "favoriteItems") {
            favoriteItems = Set(saved)
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
