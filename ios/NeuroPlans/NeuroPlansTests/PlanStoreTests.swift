import XCTest
@testable import NeuroPlans

/// Tests for PlanStore — the @Observable data store that manages plan loading,
/// search filtering, favorites, and recently viewed plans.
///
/// These tests work with manually injected plan data (not Bundle loading) so
/// they can run without the app's bundle resources. The loadPlans() async method
/// that reads from Bundle.main is tested indirectly via integration tests.
final class PlanStoreTests: XCTestCase {

    // MARK: - Properties

    private var store: PlanStore!

    // MARK: - Test Data

    /// Create a minimal Plan for testing
    private func makePlan(
        id: String,
        title: String,
        icd10: [String] = [],
        scope: String = "Test scope"
    ) -> Plan {
        // We need to decode from JSON since Plan uses Codable and has nested types
        let json: [String: Any] = [
            "id": id,
            "title": title,
            "version": "1.0",
            "icd10": icd10,
            "scope": scope,
            "notes": [],
            "sections": [
                "Laboratory Workup": [:],
                "Imaging & Studies": [:],
                "Treatment": [:],
                "Other Recommendations": [:]
            ]
        ]
        let data = try! JSONSerialization.data(withJSONObject: json)
        return try! JSONDecoder().decode(Plan.self, from: data)
    }

    /// Populate the store with sample plans
    private func loadSamplePlans() {
        store.plans = [
            "migraine": makePlan(id: "migraine", title: "Acute Migraine",
                                icd10: ["G43.909"], scope: "Emergency"),
            "status-epilepticus": makePlan(id: "status-epilepticus", title: "Status Epilepticus",
                                          icd10: ["G41.0"], scope: "ICU"),
            "stroke-ischemic": makePlan(id: "stroke-ischemic", title: "Acute Ischemic Stroke",
                                       icd10: ["I63.9"], scope: "Emergency / Hospital"),
            "ms-relapse": makePlan(id: "ms-relapse", title: "Multiple Sclerosis Relapse",
                                  icd10: ["G35"], scope: "Outpatient / Hospital"),
            "guillain-barre": makePlan(id: "guillain-barre", title: "Guillain-Barre Syndrome",
                                      icd10: ["G61.0"], scope: "Hospital / ICU")
        ]
        store.isLoaded = true
    }

    // MARK: - Setup / Teardown

    override func setUp() {
        super.setUp()
        // Clear UserDefaults keys used by PlanStore to ensure clean state
        UserDefaults.standard.removeObject(forKey: "favorites")
        UserDefaults.standard.removeObject(forKey: "favoriteItems")
        UserDefaults.standard.removeObject(forKey: "recents")
        store = PlanStore()
    }

    override func tearDown() {
        // Clean up UserDefaults
        UserDefaults.standard.removeObject(forKey: "favorites")
        UserDefaults.standard.removeObject(forKey: "favoriteItems")
        UserDefaults.standard.removeObject(forKey: "recents")
        store = nil
        super.tearDown()
    }

    // MARK: - Plan Loading

    /// Verify that plans dictionary is populated after manual loading
    func testPlansLoadedSuccessfully() {
        loadSamplePlans()
        XCTAssertEqual(store.plans.count, 5, "Should have 5 sample plans loaded")
        XCTAssertTrue(store.isLoaded, "isLoaded flag should be true")
    }

    /// allPlans should return plans sorted alphabetically by title
    func testAllPlans_SortedAlphabetically() {
        loadSamplePlans()
        let titles = store.allPlans.map { $0.title }
        XCTAssertEqual(titles, [
            "Acute Ischemic Stroke",
            "Acute Migraine",
            "Guillain-Barre Syndrome",
            "Multiple Sclerosis Relapse",
            "Status Epilepticus"
        ], "allPlans should be sorted alphabetically by title")
    }

    /// plan(for:) should return the correct plan by ID
    func testPlanForId() {
        loadSamplePlans()
        let plan = store.plan(for: "migraine")
        XCTAssertNotNil(plan)
        XCTAssertEqual(plan?.title, "Acute Migraine")
    }

    /// plan(for:) with nonexistent ID should return nil
    func testPlanForId_NotFound() {
        loadSamplePlans()
        let plan = store.plan(for: "nonexistent-plan")
        XCTAssertNil(plan, "Should return nil for unknown plan ID")
    }

    // MARK: - Search / Filtering

    /// Empty search text should return all plans
    func testFilteredPlans_EmptySearch() {
        loadSamplePlans()
        store.searchText = ""
        XCTAssertEqual(store.filteredPlans.count, 5,
                       "Empty search should return all plans")
    }

    /// Search by title substring
    func testFilteredPlans_ByTitle() {
        loadSamplePlans()
        store.searchText = "migraine"
        XCTAssertEqual(store.filteredPlans.count, 1)
        XCTAssertEqual(store.filteredPlans.first?.id, "migraine")
    }

    /// Search should be case-insensitive
    func testFilteredPlans_CaseInsensitive() {
        loadSamplePlans()
        store.searchText = "STROKE"
        XCTAssertEqual(store.filteredPlans.count, 1)
        XCTAssertEqual(store.filteredPlans.first?.id, "stroke-ischemic")
    }

    /// Search by plan ID
    func testFilteredPlans_ById() {
        loadSamplePlans()
        store.searchText = "guillain"
        XCTAssertEqual(store.filteredPlans.count, 1,
                       "Should match plan ID substring")
    }

    /// Search by ICD-10 code
    func testFilteredPlans_ByICD10() {
        loadSamplePlans()
        store.searchText = "G43"
        XCTAssertEqual(store.filteredPlans.count, 1,
                       "Should match ICD-10 code")
        XCTAssertEqual(store.filteredPlans.first?.id, "migraine")
    }

    /// Search by scope
    func testFilteredPlans_ByScope() {
        loadSamplePlans()
        store.searchText = "ICU"
        // "Status Epilepticus" has scope "ICU", "Guillain-Barre" has "Hospital / ICU"
        XCTAssertEqual(store.filteredPlans.count, 2,
                       "Should match plans with ICU in their scope")
    }

    /// Search with no matches
    func testFilteredPlans_NoMatches() {
        loadSamplePlans()
        store.searchText = "zzzznonexistent"
        XCTAssertEqual(store.filteredPlans.count, 0,
                       "No plans should match nonsense query")
    }

    // MARK: - Favorites

    /// Toggle favorite on and off
    func testToggleFavorite() {
        loadSamplePlans()

        // Initially not a favorite
        XCTAssertFalse(store.isFavorite("migraine"))

        // Toggle on
        store.toggleFavorite("migraine")
        XCTAssertTrue(store.isFavorite("migraine"),
                      "Plan should be a favorite after toggling on")

        // Toggle off
        store.toggleFavorite("migraine")
        XCTAssertFalse(store.isFavorite("migraine"),
                       "Plan should not be a favorite after toggling off")
    }

    /// favoritePlans should return only favorited plans
    func testFavoritePlans() {
        loadSamplePlans()
        store.toggleFavorite("migraine")
        store.toggleFavorite("stroke-ischemic")

        let favTitles = store.favoritePlans.map { $0.id }
        XCTAssertEqual(favTitles.count, 2)
        XCTAssertTrue(favTitles.contains("migraine"))
        XCTAssertTrue(favTitles.contains("stroke-ischemic"))
    }

    /// Favorites should persist via UserDefaults
    func testFavorites_Persistence() {
        loadSamplePlans()
        store.toggleFavorite("migraine")

        // Verify it was saved to UserDefaults
        let saved = UserDefaults.standard.stringArray(forKey: "favorites") ?? []
        XCTAssertTrue(saved.contains("migraine"),
                      "Favorites should be persisted to UserDefaults")
    }

    // MARK: - Favorite Items (Actions)

    /// Toggle a favorite item (plan action)
    func testToggleFavoriteItem() {
        XCTAssertFalse(store.isFavoriteItem("migraine", itemText: "CBC"))

        store.toggleFavoriteItem("migraine", itemText: "CBC")
        XCTAssertTrue(store.isFavoriteItem("migraine", itemText: "CBC"))

        store.toggleFavoriteItem("migraine", itemText: "CBC")
        XCTAssertFalse(store.isFavoriteItem("migraine", itemText: "CBC"))
    }

    /// Different plans with same item text should be tracked independently
    func testFavoriteItems_PlanScoped() {
        store.toggleFavoriteItem("migraine", itemText: "CBC")
        XCTAssertTrue(store.isFavoriteItem("migraine", itemText: "CBC"))
        XCTAssertFalse(store.isFavoriteItem("stroke-ischemic", itemText: "CBC"),
                       "Favorite items should be scoped to specific plan IDs")
    }

    // MARK: - Recent Plans

    /// markViewed should add plan to recents
    func testMarkViewed() {
        store.markViewed("migraine")
        XCTAssertEqual(store.recentPlanIds.count, 1)
        XCTAssertEqual(store.recentPlanIds.first, "migraine")
    }

    /// Most recently viewed should be first in the list
    func testMarkViewed_Order() {
        store.markViewed("migraine")
        store.markViewed("stroke-ischemic")
        store.markViewed("ms-relapse")

        XCTAssertEqual(store.recentPlanIds.first, "ms-relapse",
                       "Most recently viewed should be first")
    }

    /// Viewing an already-recent plan should move it to the front
    func testMarkViewed_Deduplication() {
        store.markViewed("migraine")
        store.markViewed("stroke-ischemic")
        store.markViewed("migraine")  // View again

        XCTAssertEqual(store.recentPlanIds.count, 2,
                       "Should not have duplicate entries")
        XCTAssertEqual(store.recentPlanIds.first, "migraine",
                       "Re-viewed plan should move to front")
    }

    /// Recents list should cap at 10 entries
    func testMarkViewed_MaxLimit() {
        for i in 1...15 {
            store.markViewed("plan-\(i)")
        }
        XCTAssertEqual(store.recentPlanIds.count, 10,
                       "Recent plans should be capped at 10")
        XCTAssertEqual(store.recentPlanIds.first, "plan-15",
                       "Most recent should be first")
    }

    /// recentPlans should resolve plan IDs to Plan objects
    func testRecentPlans_ResolvesToPlanObjects() {
        loadSamplePlans()
        store.markViewed("migraine")
        store.markViewed("stroke-ischemic")

        let recentPlans = store.recentPlans
        XCTAssertEqual(recentPlans.count, 2)
        XCTAssertEqual(recentPlans.first?.id, "stroke-ischemic")
    }

    /// Recents should persist via UserDefaults
    func testRecents_Persistence() {
        store.markViewed("migraine")

        let saved = UserDefaults.standard.stringArray(forKey: "recents") ?? []
        XCTAssertTrue(saved.contains("migraine"),
                      "Recents should be persisted to UserDefaults")
    }

    /// loadRecents should restore from UserDefaults
    func testLoadRecents() {
        UserDefaults.standard.set(["plan-a", "plan-b"], forKey: "recents")

        store.loadRecents()
        XCTAssertEqual(store.recentPlanIds, ["plan-a", "plan-b"],
                       "loadRecents should restore saved plan IDs")
    }

    // MARK: - Empty State

    /// Store should be empty before any data is loaded
    func testEmptyStore() {
        XCTAssertTrue(store.plans.isEmpty)
        XCTAssertFalse(store.isLoaded)
        XCTAssertTrue(store.allPlans.isEmpty)
        XCTAssertTrue(store.filteredPlans.isEmpty)
        XCTAssertTrue(store.favoritePlans.isEmpty)
    }
}
