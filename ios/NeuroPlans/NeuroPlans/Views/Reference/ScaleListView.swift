import SwiftUI

struct ScaleListView: View {
    let title: String
    let scales: [ClinicalScale]
    var icon: String = "chart.bar.fill"

    @State private var searchText = ""

    private var filtered: [ClinicalScale] {
        guard !searchText.isEmpty else { return scales }
        let q = searchText.lowercased()
        return scales.filter {
            $0.title.lowercased().contains(q)
            || $0.abbreviation.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var body: some View {
        List(filtered) { scale in
            NavigationLink(value: scale) {
                HStack(spacing: 12) {
                    Image(systemName: "chart.bar.fill")
                        .font(.system(size: 18))
                        .foregroundStyle(.blue)
                        .frame(width: 32)

                    VStack(alignment: .leading, spacing: 4) {
                        Text(scale.title)
                            .font(.system(.body, design: .rounded, weight: .medium))
                        HStack(spacing: 8) {
                            Text(scale.abbreviation)
                                .font(.system(.caption, design: .rounded, weight: .bold))
                                .foregroundStyle(.blue)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(.blue.opacity(0.12), in: RoundedRectangle(cornerRadius: 4))
                            Text(scale.description)
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
        .searchable(text: $searchText, prompt: "Search scales...")
    }
}

#Preview {
    NavigationStack {
        ScaleListView(title: "Stroke", scales: [])
    }
}
