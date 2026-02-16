import Foundation
import SwiftUI

@Observable
final class ReferenceStore {

    // MARK: - State

    var scales: [ClinicalScale] = []
    var exams: [NeurologyExam] = []
    var tools: [NeurologyTool] = []
    var isLoaded = false
    var searchText: String = ""
    var loadingError: String? = nil

    // MARK: - Computed

    var allScales: [ClinicalScale] {
        scales.sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }
    }

    var allExams: [NeurologyExam] {
        exams.sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }
    }

    var allTools: [NeurologyTool] {
        tools.sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }
    }

    var filteredScales: [ClinicalScale] {
        guard !searchText.isEmpty else { return allScales }
        let q = searchText.lowercased()
        return allScales.filter {
            $0.title.lowercased().contains(q)
            || $0.abbreviation.lowercased().contains(q)
            || $0.category.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var filteredExams: [NeurologyExam] {
        guard !searchText.isEmpty else { return allExams }
        let q = searchText.lowercased()
        return allExams.filter {
            $0.title.lowercased().contains(q)
            || $0.category.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var filteredTools: [NeurologyTool] {
        guard !searchText.isEmpty else { return allTools }
        let q = searchText.lowercased()
        return allTools.filter {
            $0.title.lowercased().contains(q)
            || $0.category.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var scaleCategories: [ReferenceScaleCategory] {
        ReferenceScaleCategory.all.filter { cat in
            cat.scaleIds.contains { sid in scales.contains { $0.id == sid } }
        }
    }

    var examCategories: [ReferenceExamCategory] {
        ReferenceExamCategory.all.filter { cat in
            cat.examIds.contains { eid in exams.contains { $0.id == eid } }
        }
    }

    var toolCategories: [ReferenceToolCategory] {
        ReferenceToolCategory.all.filter { cat in
            cat.toolIds.contains { tid in tools.contains { $0.id == tid } }
        }
    }

    // MARK: - Access

    func scales(for category: ReferenceScaleCategory) -> [ClinicalScale] {
        category.scaleIds.compactMap { sid in scales.first { $0.id == sid } }
    }

    func exams(for category: ReferenceExamCategory) -> [NeurologyExam] {
        category.examIds.compactMap { eid in exams.first { $0.id == eid } }
    }

    func tools(for category: ReferenceToolCategory) -> [NeurologyTool] {
        category.toolIds.compactMap { tid in tools.first { $0.id == tid } }
    }

    // MARK: - Loading

    func loadAll() async {
        guard !isLoaded else { return }
        async let s = loadJSON([ClinicalScale].self, from: "scales")
        async let e = loadJSON([NeurologyExam].self, from: "exams")
        async let t = loadJSON([NeurologyTool].self, from: "tools")

        let (loadedScales, loadedExams, loadedTools) = await (s, e, t)

        await MainActor.run {
            self.scales = loadedScales
            self.exams = loadedExams
            self.tools = loadedTools
            self.isLoaded = true
        }
    }

    private func loadJSON<T: Decodable>(_ type: T.Type, from resource: String) async -> T {
        do {
            guard let url = Bundle.main.url(forResource: resource, withExtension: "json") else {
                let msg = "\(resource).json not found in bundle"
                print(msg)
                await MainActor.run { self.loadingError = msg }
                if let empty = [String]() as? T { return empty }
                if let empty = [ClinicalScale]() as? T { return empty }
                if let empty = [NeurologyExam]() as? T { return empty }
                if let empty = [NeurologyTool]() as? T { return empty }
                return [] as! T
            }
            let data = try Data(contentsOf: url)
            return try JSONDecoder().decode(T.self, from: data)
        } catch {
            let msg = "Failed to load \(resource): \(error.localizedDescription)"
            print(msg)
            await MainActor.run { self.loadingError = msg }
            if let empty = [String]() as? T { return empty }
            if let empty = [ClinicalScale]() as? T { return empty }
            if let empty = [NeurologyExam]() as? T { return empty }
            if let empty = [NeurologyTool]() as? T { return empty }
            return [] as! T
        }
    }
}
