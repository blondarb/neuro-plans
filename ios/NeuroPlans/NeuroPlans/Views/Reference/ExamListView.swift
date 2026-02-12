import SwiftUI

struct ExamListView: View {
    let title: String
    let exams: [NeurologyExam]
    var icon: String = "stethoscope"

    @State private var searchText = ""

    private var filtered: [NeurologyExam] {
        guard !searchText.isEmpty else { return exams }
        let q = searchText.lowercased()
        return exams.filter {
            $0.title.lowercased().contains(q)
            || $0.description.lowercased().contains(q)
        }
    }

    var body: some View {
        List(filtered) { exam in
            NavigationLink(value: exam) {
                HStack(spacing: 12) {
                    Image(systemName: examCategoryIcon(exam.category))
                        .font(.system(size: 18))
                        .foregroundStyle(examCategoryColor(exam.category))
                        .frame(width: 32)

                    VStack(alignment: .leading, spacing: 4) {
                        Text(exam.title)
                            .font(.system(.body, design: .rounded, weight: .medium))
                        HStack(spacing: 6) {
                            Text("\(exam.steps.count) steps")
                                .font(.system(.caption2, design: .rounded, weight: .medium))
                                .foregroundStyle(.secondary)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(.quaternary, in: RoundedRectangle(cornerRadius: 4))
                            Text(exam.description)
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
        .searchable(text: $searchText, prompt: "Search exams...")
        .navigationDestination(for: NeurologyExam.self) { exam in
            ExamDetailView(exam: exam)
        }
    }

    private func examCategoryIcon(_ cat: String) -> String {
        switch cat {
        case "core": "stethoscope"
        case "specialized": "magnifyingglass"
        case "rapid": "bolt.fill"
        default: "stethoscope"
        }
    }

    private func examCategoryColor(_ cat: String) -> Color {
        switch cat {
        case "core": .teal
        case "specialized": .blue
        case "rapid": .orange
        default: .teal
        }
    }
}

#Preview {
    NavigationStack {
        ExamListView(title: "Core Exams", exams: [])
            .navigationDestination(for: NeurologyExam.self) { exam in
                ExamDetailView(exam: exam)
            }
    }
}
