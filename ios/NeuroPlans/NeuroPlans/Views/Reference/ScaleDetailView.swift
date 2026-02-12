import SwiftUI

struct ScaleDetailView: View {
    let scale: ClinicalScale

    @State private var selections: [String: Int] = [:]
    @State private var copied = false
    @State private var showShareSheet = false

    private var totalScore: Int {
        selections.values.reduce(0, +)
    }

    private var currentInterpretation: ScoreInterpretation? {
        scale.interpretation.first { Double(totalScore) >= $0.min && Double(totalScore) <= $0.max }
    }

    private var interpretationColor: Color {
        switch currentInterpretation?.color {
        case "green": .green
        case "yellow": .yellow
        case "orange": .orange
        case "red": .red
        default: .secondary
        }
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                // Header
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Text(scale.abbreviation)
                            .font(.system(.title, design: .rounded, weight: .bold))
                            .foregroundStyle(.blue)
                        Spacer()
                        scoreDisplay
                    }
                    Text(scale.title)
                        .font(.system(.headline, design: .rounded))
                    Text(scale.description)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .padding(.horizontal)

                // Score Bar
                scoreBar
                    .padding(.horizontal)

                // Components
                ForEach(scale.components) { component in
                    componentCard(component)
                }

                // Interpretation
                if let interp = currentInterpretation {
                    interpretationCard(interp)
                        .padding(.horizontal)
                }

                // Citation
                if let citation = scale.citation, !citation.isEmpty {
                    GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                        HStack(alignment: .top, spacing: 8) {
                            Image(systemName: "book.closed.fill")
                                .foregroundStyle(.secondary)
                                .font(.system(size: 12))
                            Text(citation)
                                .font(.system(.caption2))
                                .foregroundStyle(.secondary)
                        }
                    }
                    .padding(.horizontal)
                }

                // Actions
                VStack(spacing: 10) {
                    HStack(spacing: 12) {
                        Button {
                            copyScore()
                        } label: {
                            Label(
                                copied ? "Copied!" : "Copy",
                                systemImage: copied ? "checkmark.circle.fill" : "doc.on.doc"
                            )
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 12)
                            .background(copied ? .green.opacity(0.2) : AppTheme.teal.opacity(0.2))
                            .foregroundStyle(copied ? .green : AppTheme.teal)
                            .clipShape(RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius))
                        }

                        Button {
                            showShareSheet = true
                        } label: {
                            Label("Share", systemImage: "square.and.arrow.up")
                                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 12)
                                .background(.blue.opacity(0.2))
                                .foregroundStyle(.blue)
                                .clipShape(RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius))
                        }

                        Button {
                            withAnimation(.snappy) {
                                selections = [:]
                            }
                        } label: {
                            Label("Reset", systemImage: "arrow.counterclockwise")
                                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 12)
                                .background(.quaternary)
                                .foregroundStyle(.secondary)
                                .clipShape(RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius))
                        }
                    }
                }
                .padding(.horizontal)
                .sheet(isPresented: $showShareSheet) {
                    ShareSheet(text: generateShareText())
                }

                Spacer(minLength: 100)
            }
            .padding(.top, 8)
        }
        .background { AdaptiveBackground() }
        .navigationBarTitleDisplayMode(.inline)
    }

    // MARK: - Score Display

    private var scoreDisplay: some View {
        VStack(alignment: .trailing, spacing: 2) {
            Text("\(totalScore)")
                .font(.system(.largeTitle, design: .rounded, weight: .bold))
                .foregroundStyle(interpretationColor)
                .contentTransition(.numericText())
                .animation(.snappy, value: totalScore)
            if let interp = currentInterpretation {
                Text(interp.label)
                    .font(.system(.caption2, design: .rounded, weight: .medium))
                    .foregroundStyle(interpretationColor)
            }
        }
    }

    // MARK: - Score Bar

    private var scoreBar: some View {
        GeometryReader { geo in
            let totalWidth = geo.size.width
            let ranges = scale.interpretation
            let maxScore = ranges.map(\.max).max() ?? 1

            ZStack(alignment: .leading) {
                // Background segments
                HStack(spacing: 1) {
                    ForEach(Array(ranges.enumerated()), id: \.offset) { _, range in
                        let width = CGFloat(range.max - range.min + 1) / CGFloat(maxScore + 1) * totalWidth
                        RoundedRectangle(cornerRadius: 3)
                            .fill(colorFor(range.color).opacity(0.25))
                            .frame(width: max(width, 4), height: 8)
                    }
                }

                // Indicator
                let progress = CGFloat(totalScore) / CGFloat(max(maxScore, 1))
                Circle()
                    .fill(interpretationColor)
                    .frame(width: 14, height: 14)
                    .shadow(color: interpretationColor.opacity(0.5), radius: 4)
                    .offset(x: progress * (totalWidth - 14))
                    .animation(.snappy, value: totalScore)
            }
        }
        .frame(height: 14)
    }

    // MARK: - Component Card

    private func componentCard(_ component: ScaleComponent) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(component.name)
                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                .padding(.horizontal)

            VStack(spacing: 4) {
                ForEach(component.options) { option in
                    let isSelected = selections[component.id] == option.value
                    Button {
                        withAnimation(.snappy) {
                            selections[component.id] = option.value
                        }
                    } label: {
                        HStack(spacing: 10) {
                            Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                                .foregroundStyle(isSelected ? .blue : .secondary)
                                .font(.system(size: 18))

                            VStack(alignment: .leading, spacing: 2) {
                                Text(option.label)
                                    .font(.system(.subheadline))
                                    .foregroundStyle(.primary)
                                    .multilineTextAlignment(.leading)
                                if let desc = option.description, !desc.isEmpty {
                                    Text(desc)
                                        .font(.caption2)
                                        .foregroundStyle(.secondary)
                                        .multilineTextAlignment(.leading)
                                }
                            }

                            Spacer()

                            Text("\(option.value)")
                                .font(.system(.caption, design: .rounded, weight: .bold))
                                .foregroundStyle(isSelected ? Color.blue : Color.gray)
                                .frame(width: 24)
                        }
                        .padding(.horizontal, AppTheme.cardPadding)
                        .padding(.vertical, 10)
                        .background(
                            isSelected
                                ? .blue.opacity(0.08)
                                : .clear,
                            in: RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius)
                        )
                    }
                    .buttonStyle(.plain)
                    .sensoryFeedback(.selection, trigger: isSelected)
                }
            }
            .padding(.horizontal, 4)
        }
        .padding(.vertical, 4)
    }

    // MARK: - Interpretation Card

    private func interpretationCard(_ interp: ScoreInterpretation) -> some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    Image(systemName: "info.circle.fill")
                        .foregroundStyle(interpretationColor)
                    Text("Score Interpretation")
                        .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    Spacer()
                    Text("\(totalScore) pts")
                        .font(.system(.caption, design: .rounded, weight: .bold))
                        .foregroundStyle(interpretationColor)
                }

                Text(interp.label)
                    .font(.system(.headline, design: .rounded, weight: .bold))
                    .foregroundStyle(interpretationColor)

                if let action = interp.action, !action.isEmpty {
                    Text(action)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }

    // MARK: - Helpers

    private func colorFor(_ name: String) -> Color {
        switch name {
        case "green": .green
        case "yellow": .yellow
        case "orange": .orange
        case "red": .red
        default: .secondary
        }
    }

    private func generateShareText() -> String {
        var text = "\(scale.title) (\(scale.abbreviation))\n"
        text += "Score: \(totalScore)"
        if let interp = currentInterpretation {
            text += " — \(interp.label)"
            if let action = interp.action, !action.isEmpty {
                text += "\nRecommendation: \(action)"
            }
        }
        text += "\n\nComponents:"
        for component in scale.components {
            if let val = selections[component.id],
               let option = component.options.first(where: { $0.value == val }) {
                text += "\n• \(component.name): \(option.label) (\(val))"
            } else {
                text += "\n• \(component.name): Not scored"
            }
        }
        text += "\n\n— Generated by Neuro Plans"
        return text
    }

    private func copyScore() {
        UIPasteboard.general.string = generateShareText()
        withAnimation { copied = true }
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            withAnimation { copied = false }
        }
    }
}

#Preview {
    NavigationStack {
        ScaleDetailView(scale: ClinicalScale(
            id: "gcs", title: "Glasgow Coma Scale", abbreviation: "GCS",
            category: "consciousness",
            description: "Assessment of consciousness level",
            components: [
                ScaleComponent(id: "eye", name: "Eye Opening", options: [
                    ScoreOption(label: "Spontaneous", value: 4, description: nil),
                    ScoreOption(label: "To voice", value: 3, description: nil),
                    ScoreOption(label: "To pain", value: 2, description: nil),
                    ScoreOption(label: "None", value: 1, description: nil),
                ]),
            ],
            interpretation: [
                ScoreInterpretation(min: 3, max: 8, label: "Severe", color: "red", action: "Intubate"),
                ScoreInterpretation(min: 9, max: 12, label: "Moderate", color: "orange", action: nil),
                ScoreInterpretation(min: 13, max: 15, label: "Mild", color: "green", action: nil),
            ],
            citation: "Teasdale & Jennett, Lancet 1974",
            relatedPlans: []
        ))
    }
}
