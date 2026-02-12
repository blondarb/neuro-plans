import SwiftUI

/// Manages user preferences that persist across app sessions
@Observable
final class UserPreferences {
    
    // MARK: - Section Expansion States
    
    /// Plans tab section expansion states
    var plansSectionExpanded: [String: Bool] {
        didSet { savePlansSectionExpanded() }
    }
    
    /// Reference tab section expansion states
    var referenceSectionExpanded: [String: Bool] {
        didSet { saveReferenceSectionExpanded() }
    }
    
    // MARK: - Section Order
    
    /// Order of sections on Plans tab
    var plansSectionOrder: [String] {
        didSet { savePlansSectionOrder() }
    }
    
    /// Order of sections on Reference tab
    var referenceSectionOrder: [String] {
        didSet { saveReferenceSectionOrder() }
    }
    
    /// Order of favorite plans
    var favoritesOrder: [String] {
        didSet { saveFavoritesOrder() }
    }
    
    // MARK: - Keys
    
    private enum Keys {
        static let plansSectionExpanded = "plansSectionExpanded"
        static let referenceSectionExpanded = "referenceSectionExpanded"
        static let plansSectionOrder = "plansSectionOrder"
        static let referenceSectionOrder = "referenceSectionOrder"
        static let favoritesOrder = "favoritesOrder"
    }
    
    // MARK: - Default Values
    
    static let defaultPlansSectionOrder = ["recents", "favorites", "categories"]
    static let defaultReferenceSectionOrder = ["examTools", "scales", "exams", "tools"]
    
    // MARK: - Initialization
    
    init() {
        // Load persisted values
        if let data = UserDefaults.standard.data(forKey: Keys.plansSectionExpanded),
           let decoded = try? JSONDecoder().decode([String: Bool].self, from: data) {
            plansSectionExpanded = decoded
        } else {
            plansSectionExpanded = [:]
        }
        
        if let data = UserDefaults.standard.data(forKey: Keys.referenceSectionExpanded),
           let decoded = try? JSONDecoder().decode([String: Bool].self, from: data) {
            referenceSectionExpanded = decoded
        } else {
            referenceSectionExpanded = [:]
        }
        
        if let order = UserDefaults.standard.stringArray(forKey: Keys.plansSectionOrder), !order.isEmpty {
            plansSectionOrder = order
        } else {
            plansSectionOrder = Self.defaultPlansSectionOrder
        }
        
        if let order = UserDefaults.standard.stringArray(forKey: Keys.referenceSectionOrder), !order.isEmpty {
            referenceSectionOrder = order
        } else {
            referenceSectionOrder = Self.defaultReferenceSectionOrder
        }
        
        if let order = UserDefaults.standard.stringArray(forKey: Keys.favoritesOrder) {
            favoritesOrder = order
        } else {
            favoritesOrder = []
        }
    }
    
    // MARK: - Section Expansion Helpers
    
    func isExpanded(_ sectionId: String, in tab: Tab, default defaultValue: Bool = true) -> Bool {
        switch tab {
        case .plans:
            return plansSectionExpanded[sectionId] ?? defaultValue
        case .reference:
            return referenceSectionExpanded[sectionId] ?? defaultValue
        }
    }
    
    func setExpanded(_ sectionId: String, in tab: Tab, to value: Bool) {
        switch tab {
        case .plans:
            plansSectionExpanded[sectionId] = value
        case .reference:
            referenceSectionExpanded[sectionId] = value
        }
    }
    
    func toggleExpanded(_ sectionId: String, in tab: Tab) {
        let current = isExpanded(sectionId, in: tab)
        setExpanded(sectionId, in: tab, to: !current)
    }
    
    // MARK: - Section Order Helpers
    
    func moveSection(from source: IndexSet, to destination: Int, in tab: Tab) {
        switch tab {
        case .plans:
            plansSectionOrder.move(fromOffsets: source, toOffset: destination)
        case .reference:
            referenceSectionOrder.move(fromOffsets: source, toOffset: destination)
        }
    }
    
    func moveFavorite(from source: IndexSet, to destination: Int) {
        favoritesOrder.move(fromOffsets: source, toOffset: destination)
    }
    
    /// Ensures favoritesOrder contains all current favorites and removes any that are no longer favorites
    func syncFavoritesOrder(with currentFavorites: Set<String>) {
        // Remove any favorites that no longer exist
        favoritesOrder = favoritesOrder.filter { currentFavorites.contains($0) }
        
        // Add any new favorites that aren't in the order
        for favoriteId in currentFavorites {
            if !favoritesOrder.contains(favoriteId) {
                favoritesOrder.append(favoriteId)
            }
        }
    }
    
    // MARK: - Tab Enum
    
    enum Tab {
        case plans
        case reference
    }
    
    // MARK: - Persistence
    
    private func savePlansSectionExpanded() {
        if let data = try? JSONEncoder().encode(plansSectionExpanded) {
            UserDefaults.standard.set(data, forKey: Keys.plansSectionExpanded)
        }
    }
    
    private func saveReferenceSectionExpanded() {
        if let data = try? JSONEncoder().encode(referenceSectionExpanded) {
            UserDefaults.standard.set(data, forKey: Keys.referenceSectionExpanded)
        }
    }
    
    private func savePlansSectionOrder() {
        UserDefaults.standard.set(plansSectionOrder, forKey: Keys.plansSectionOrder)
    }
    
    private func saveReferenceSectionOrder() {
        UserDefaults.standard.set(referenceSectionOrder, forKey: Keys.referenceSectionOrder)
    }
    
    private func saveFavoritesOrder() {
        UserDefaults.standard.set(favoritesOrder, forKey: Keys.favoritesOrder)
    }
}
