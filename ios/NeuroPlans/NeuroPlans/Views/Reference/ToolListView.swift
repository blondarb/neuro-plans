import SwiftUI

struct ToolListView: View {
    let title: String
    let tools: [NeurologyTool]
    var icon: String = "wrench.and.screwdriver.fill"

    @State private var searchText = ""

    private var filtered: [NeurologyTool] {
        guard !searchText.isEmpty else { return tools }
        let q = searchText.lowercased()
        return tools.filter {
            $0.title.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var body: some View {
        List(filtered) { tool in
            NavigationLink(value: tool) {
                HStack(spacing: 12) {
                    Image(systemName: categoryIcon(tool.category))
                        .font(.system(size: 18))
                        .foregroundStyle(categoryColor(tool.category))
                        .frame(width: 32)

                    VStack(alignment: .leading, spacing: 4) {
                        Text(tool.title)
                            .font(.system(.body, design: .rounded, weight: .medium))
                        HStack(spacing: 6) {
                            Text(categoryLabel(tool.category))
                                .font(.system(.caption2, design: .rounded, weight: .medium))
                                .foregroundStyle(categoryColor(tool.category))
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(categoryColor(tool.category).opacity(0.12), in: RoundedRectangle(cornerRadius: 4))
                            Text(tool.description)
                                .font(.caption2)
                                .foregroundStyle(.secondary)
                                .lineLimit(1)
                        }
                    }
                }
            }
        }
        .listStyle(.plain)
        .navigationTitle(title)
        .searchable(text: $searchText, prompt: "Search tools...")
        .navigationDestination(for: NeurologyTool.self) { tool in
            ToolDetailView(tool: tool)
        }
    }

    private func categoryIcon(_ cat: String) -> String {
        switch cat {
        case "calculator": "function"
        case "protocol": "list.number"
        case "reference_table": "tablecells"
        case "conversion": "arrow.left.arrow.right"
        default: "wrench.fill"
        }
    }

    private func categoryColor(_ cat: String) -> Color {
        switch cat {
        case "calculator": .blue
        case "protocol": .red
        case "reference_table": .green
        case "conversion": .purple
        default: .secondary
        }
    }

    private func categoryLabel(_ cat: String) -> String {
        switch cat {
        case "calculator": "Calculator"
        case "protocol": "Protocol"
        case "reference_table": "Reference"
        case "conversion": "Conversion"
        default: "Tool"
        }
    }
}

#Preview {
    NavigationStack {
        ToolListView(title: "Calculators", tools: [])
    }
}
