import SwiftUI

struct ExamDetailView: View {
    let exam: NeurologyExam

    @State private var completedSteps: Set<String> = []
    @State private var expandedStep: String? = nil
    @State private var copied = false
    @State private var showShareSheet = false

    private var progress: Double {
        guard !exam.steps.isEmpty else { return 0 }
        return Double(completedSteps.count) / Double(exam.steps.count)
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                // Header
                VStack(alignment: .leading, spacing: 8) {
                    Text(exam.title)
                        .font(.system(.title2, design: .rounded, weight: .bold))

                    Text(exam.description)
                        .font(.caption)
                        .foregroundStyle(.secondary)

                    // Progress bar
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            Text("\(completedSteps.count) / \(exam.steps.count) steps")
                                .font(.system(.caption, design: .rounded, weight: .medium))
                                .foregroundStyle(.secondary)
                            Spacer()
                            Text("\(Int(progress * 100))%")
                                .font(.system(.caption, design: .rounded, weight: .bold))
                                .foregroundStyle(progress == 1.0 ? .green : AppTheme.teal)
                        }

                        GeometryReader { geo in
                            ZStack(alignment: .leading) {
                                RoundedRectangle(cornerRadius: 4)
                                    .fill(.quaternary)
                                    .frame(height: 6)
                                RoundedRectangle(cornerRadius: 4)
                                    .fill(progress == 1.0 ? .green : AppTheme.teal)
                                    .frame(width: geo.size.width * progress, height: 6)
                                    .animation(.snappy, value: progress)
                            }
                        }
                        .frame(height: 6)
                    }
                }
                .padding(.horizontal)

                // Steps
                ForEach(Array(exam.steps.enumerated()), id: \.element.id) { index, step in
                    stepCard(step, index: index + 1)
                }

                // Clinical Pearls
                if !exam.clinicalPearls.isEmpty {
                    pearlsSection
                }

                // Actions
                VStack(spacing: 10) {
                    HStack(spacing: 12) {
                        Button {
                            copyExamResults()
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
                                completedSteps = []
                                expandedStep = nil
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
                    ShareSheet(text: generateExamShareText())
                }

                Spacer(minLength: 100)
            }
            .padding(.top, 8)
        }
        .background { AdaptiveBackground() }
        .navigationBarTitleDisplayMode(.inline)
    }

    // MARK: - Step Card

    private func stepCard(_ step: ExamStep, index: Int) -> some View {
        let isComplete = completedSteps.contains(step.id)
        let isExpanded = expandedStep == step.id

        return VStack(alignment: .leading, spacing: 0) {
            // Step header (always visible)
            Button {
                withAnimation(.snappy) {
                    if isExpanded {
                        expandedStep = nil
                    } else {
                        expandedStep = step.id
                    }
                }
            } label: {
                HStack(spacing: 12) {
                    // Step number / check
                    ZStack {
                        Circle()
                            .fill(isComplete ? .green.opacity(0.2) : AppTheme.teal.opacity(0.15))
                            .frame(width: 32, height: 32)
                        if isComplete {
                            Image(systemName: "checkmark")
                                .font(.system(size: 14, weight: .bold))
                                .foregroundStyle(.green)
                        } else {
                            Text("\(index)")
                                .font(.system(.caption, design: .rounded, weight: .bold))
                                .foregroundStyle(AppTheme.teal)
                        }
                    }

                    VStack(alignment: .leading, spacing: 2) {
                        Text(step.title)
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                            .foregroundStyle(.primary)
                        Text(step.instruction)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .lineLimit(isExpanded ? nil : 2)
                            .multilineTextAlignment(.leading)
                    }

                    Spacer()

                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.system(size: 12))
                        .foregroundStyle(.tertiary)
                }
                .padding(.horizontal)
                .padding(.vertical, 10)
            }
            .buttonStyle(.plain)

            // Expanded content
            if isExpanded {
                VStack(alignment: .leading, spacing: 10) {
                    // Technique
                    if let technique = step.technique, !technique.isEmpty {
                        detailRow(icon: "hand.draw.fill", title: "Technique", text: technique, color: .blue)
                    }

                    // Normal
                    if let normal = step.normalResult, !normal.isEmpty {
                        detailRow(icon: "checkmark.circle.fill", title: "Normal", text: normal, color: .green)
                    }

                    // Abnormal
                    if let abnormals = step.abnormalResults, !abnormals.isEmpty {
                        VStack(alignment: .leading, spacing: 6) {
                            HStack(spacing: 4) {
                                Image(systemName: "exclamationmark.triangle.fill")
                                    .font(.system(size: 11))
                                    .foregroundStyle(.orange)
                                Text("Abnormal Findings")
                                    .font(.system(.caption, design: .rounded, weight: .semibold))
                                    .foregroundStyle(.orange)
                            }

                            ForEach(Array(abnormals.enumerated()), id: \.offset) { _, abnormal in
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(abnormal.finding)
                                        .font(.system(.caption, weight: .medium))
                                    Text(abnormal.significance)
                                        .font(.caption2)
                                        .foregroundStyle(.secondary)
                                }
                                .padding(.leading, 16)
                            }
                        }
                    }

                    // Mark complete button
                    Button {
                        withAnimation(.snappy) {
                            if isComplete {
                                completedSteps.remove(step.id)
                            } else {
                                completedSteps.insert(step.id)
                                // Auto-advance to next step
                                if let currentIdx = exam.steps.firstIndex(where: { $0.id == step.id }),
                                   currentIdx + 1 < exam.steps.count {
                                    expandedStep = exam.steps[currentIdx + 1].id
                                } else {
                                    expandedStep = nil
                                }
                            }
                        }
                    } label: {
                        Label(
                            isComplete ? "Mark Incomplete" : "Mark Complete",
                            systemImage: isComplete ? "xmark.circle" : "checkmark.circle.fill"
                        )
                        .font(.system(.caption, design: .rounded, weight: .semibold))
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 8)
                        .background(isComplete ? Color.gray.opacity(0.15) : Color.green.opacity(0.15))
                        .foregroundStyle(isComplete ? Color.secondary : Color.green)
                        .clipShape(RoundedRectangle(cornerRadius: 8))
                    }
                    .sensoryFeedback(.impact(flexibility: .soft), trigger: isComplete)
                }
                .padding(.horizontal)
                .padding(.bottom, 12)
                .padding(.leading, 44)
            }

            Divider().opacity(0.2).padding(.horizontal)
        }
    }

    private func detailRow(icon: String, title: String, text: String, color: Color) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack(spacing: 4) {
                Image(systemName: icon)
                    .font(.system(size: 11))
                    .foregroundStyle(color)
                Text(title)
                    .font(.system(.caption, design: .rounded, weight: .semibold))
                    .foregroundStyle(color)
            }
            Text(text)
                .font(.caption)
                .foregroundStyle(.secondary)
                .padding(.leading, 16)
        }
    }

    // MARK: - Pearls

    private func generateExamShareText() -> String {
        var text = "\(exam.title)\n"
        text += "Progress: \(completedSteps.count)/\(exam.steps.count) steps (\(Int(progress * 100))%)\n"
        text += "\nCompleted Steps:"
        
        for step in exam.steps {
            let status = completedSteps.contains(step.id) ? "✓" : "○"
            text += "\n\(status) \(step.title)"
        }
        
        if !exam.clinicalPearls.isEmpty {
            text += "\n\nClinical Pearls:"
            for pearl in exam.clinicalPearls {
                text += "\n• \(pearl)"
            }
        }
        
        text += "\n\n— Generated by Neuro Plans"
        return text
    }

    private func copyExamResults() {
        UIPasteboard.general.string = generateExamShareText()
        withAnimation { copied = true }
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            withAnimation { copied = false }
        }
    }

    private var pearlsSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            GlassSectionHeader(title: "Clinical Pearls", icon: "lightbulb.fill")
                .padding(.horizontal)

            VStack(alignment: .leading, spacing: 6) {
                ForEach(exam.clinicalPearls, id: \.self) { pearl in
                    HStack(alignment: .top, spacing: 8) {
                        Image(systemName: "lightbulb.fill")
                            .font(.system(size: 11))
                            .foregroundStyle(.yellow)
                            .frame(width: 16)
                        Text(pearl)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
            }
            .padding(.horizontal)
        }
    }
}

#Preview {
    NavigationStack {
        ExamDetailView(exam: NeurologyExam(
            id: "sample", title: "Cranial Nerve Exam",
            category: "core",
            description: "Systematic evaluation of CN I through XII",
            steps: [
                ExamStep(
                    id: "cn1", title: "CN I — Olfactory",
                    instruction: "Test smell in each nostril",
                    technique: "Present familiar scents with eyes closed",
                    normalResult: "Identifies scents bilaterally",
                    abnormalResults: [
                        AbnormalFinding(finding: "Anosmia", significance: "Frontal lobe lesion")
                    ]
                ),
            ],
            clinicalPearls: ["Always test each nostril separately"],
            relatedPlans: []
        ))
    }
}
