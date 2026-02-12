import Foundation
import SwiftUI

@Observable
final class PlanBuilder {

    var selectedItems: [SelectedItem] = []
    var activePlanTitle: String = ""

    var isEmpty: Bool { selectedItems.isEmpty }
    var itemCount: Int { selectedItems.count }

    // Grouped by section for display
    var groupedItems: [(section: String, items: [SelectedItem])] {
        let grouped = Dictionary(grouping: selectedItems) { $0.section }
        let sectionOrder = [
            "Laboratory Workup", "Imaging & Studies",
            "Treatment", "Other Recommendations",
            "Monitoring", "Disposition"
        ]
        return sectionOrder.compactMap { section in
            guard let items = grouped[section], !items.isEmpty else { return nil }
            return (section: section, items: items)
        }
    }

    // MARK: - Selection

    func isSelected(_ itemText: String, in planId: String) -> Bool {
        selectedItems.contains { $0.planId == planId && $0.itemText == itemText }
    }

    func toggle(
        itemText: String,
        planId: String,
        planTitle: String,
        section: String,
        subsection: String,
        priority: Priority,
        orderSentence: String? = nil
    ) {
        if let idx = selectedItems.firstIndex(where: {
            $0.planId == planId && $0.itemText == itemText
        }) {
            selectedItems.remove(at: idx)
        } else {
            let item = SelectedItem(
                planId: planId,
                planTitle: planTitle,
                section: section,
                subsection: subsection,
                itemText: itemText,
                priority: priority,
                orderSentence: orderSentence
            )
            selectedItems.append(item)
        }
    }

    func remove(_ item: SelectedItem) {
        selectedItems.removeAll { $0.id == item.id }
    }

    func clearAll() {
        selectedItems.removeAll()
        activePlanTitle = ""
    }

    func move(from source: IndexSet, to destination: Int) {
        selectedItems.move(fromOffsets: source, toOffset: destination)
    }

    // MARK: - Export

    func exportAsText() -> String {
        var lines: [String] = []
        if !activePlanTitle.isEmpty {
            lines.append("CLINICAL PLAN: \(activePlanTitle)")
            lines.append("Generated: \(Date().formatted(date: .abbreviated, time: .shortened))")
            lines.append(String(repeating: "─", count: 50))
            lines.append("")
        }

        for group in groupedItems {
            lines.append("## \(group.section.uppercased())")
            for item in group.items {
                let prefix = item.priority.isApplicable ? "[\(item.priority.rawValue)]" : ""
                lines.append("  \(prefix) \(item.displayText)")
                if let order = item.orderSentence, !order.isEmpty {
                    lines.append("    → \(order)")
                }
            }
            lines.append("")
        }

        lines.append("─── \(selectedItems.count) items selected ───")
        return lines.joined(separator: "\n")
    }
}
