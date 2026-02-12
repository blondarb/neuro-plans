import SwiftUI

struct ToolDetailView: View {
    let tool: NeurologyTool

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: AppTheme.sectionSpacing) {

                // Header
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Image(systemName: categoryIcon(tool.category))
                            .font(.system(size: 24))
                            .foregroundStyle(categoryColor(tool.category))
                        Text(tool.title)
                            .font(.system(.title2, design: .rounded, weight: .bold))
                    }
                    Text(tool.description)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .padding(.horizontal)

                // Content based on category
                switch tool.category {
                case "calculator", "conversion":
                    CalculatorContent(tool: tool)
                case "protocol":
                    ProtocolContent(tool: tool)
                case "reference_table":
                    ReferenceTableContent(tool: tool)
                default:
                    Text("Unknown tool type")
                        .foregroundStyle(.secondary)
                        .padding(.horizontal)
                }

                // Clinical Pearls
                if let pearls = tool.clinicalPearls, !pearls.isEmpty {
                    VStack(alignment: .leading, spacing: 8) {
                        GlassSectionHeader(title: "Clinical Pearls", icon: "lightbulb.fill")

                        ForEach(pearls, id: \.self) { pearl in
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

                Spacer(minLength: 100)
            }
            .padding(.top, 8)
        }
        .background { AdaptiveBackground() }
        .navigationBarTitleDisplayMode(.inline)
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
}

// MARK: - Calculator Content

private struct CalculatorContent: View {
    let tool: NeurologyTool
    @State private var inputValues: [String: String] = [:]
    @State private var selectValues: [String: String] = [:]
    @State private var result: Double? = nil
    @State private var copied = false
    @State private var showShareSheet = false

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Input fields
            if let inputs = tool.inputs {
                ForEach(inputs) { input in
                    inputField(input)
                }
            }

            // Calculate button
            Button {
                calculateResult()
            } label: {
                Label("Calculate", systemImage: "equal.circle.fill")
                    .font(.system(.headline, design: .rounded, weight: .semibold))
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
                    .background(LinearGradient.tealAccent)
                    .foregroundStyle(.white)
                    .clipShape(RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius))
            }

            // Result
            if let result {
                resultCard(result)
            }
        }
        .padding(.horizontal)
    }

    private func inputField(_ input: ToolInput) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack {
                Text(input.label)
                    .font(.system(.subheadline, design: .rounded, weight: .medium))
                if let unit = input.unit {
                    Spacer()
                    Text(unit)
                        .font(.system(.caption, design: .rounded))
                        .foregroundStyle(.secondary)
                }
            }

            if input.type == "select", let options = input.options {
                // Dropdown / segmented
                let binding = Binding<String>(
                    get: { selectValues[input.id] ?? options.first ?? "" },
                    set: { selectValues[input.id] = $0 }
                )
                if options.count <= 4 {
                    Picker("", selection: binding) {
                        ForEach(options, id: \.self) { opt in
                            Text(opt).tag(opt)
                        }
                    }
                    .pickerStyle(.segmented)
                } else {
                    Picker(input.label, selection: binding) {
                        ForEach(options, id: \.self) { opt in
                            Text(opt).tag(opt)
                        }
                    }
                    .pickerStyle(.menu)
                    .padding(.vertical, 8)
                    .padding(.horizontal, 12)
                    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 8))
                }
            } else if input.type == "bool" {
                let binding = Binding<Bool>(
                    get: { inputValues[input.id] == "true" },
                    set: { inputValues[input.id] = $0 ? "true" : "false" }
                )
                Toggle(input.placeholder ?? "Yes", isOn: binding)
                    .tint(AppTheme.teal)
            } else {
                TextField(
                    input.placeholder ?? "",
                    text: Binding(
                        get: { inputValues[input.id] ?? "" },
                        set: { inputValues[input.id] = $0 }
                    )
                )
                .keyboardType(.decimalPad)
                .font(.system(.body, design: .monospaced))
                .padding(.vertical, 10)
                .padding(.horizontal, 12)
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 8))
                .overlay {
                    RoundedRectangle(cornerRadius: 8)
                        .strokeBorder(.white.opacity(0.1), lineWidth: 0.5)
                }
            }
        }
    }

    private func resultCard(_ value: Double) -> some View {
        let interp = tool.interpretation?.first { value >= $0.min && value <= $0.max }
        let color: Color = {
            switch interp?.color {
            case "green": .green
            case "yellow": .yellow
            case "orange": .orange
            case "red": .red
            default: AppTheme.teal
            }
        }()

        return GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(spacing: 12) {
                // Result value
                HStack(alignment: .firstTextBaseline, spacing: 4) {
                    Text(formatResult(value))
                        .font(.system(.largeTitle, design: .rounded, weight: .bold))
                        .foregroundStyle(color)
                    if let unit = tool.resultUnit {
                        Text(unit)
                            .font(.system(.body, design: .rounded))
                            .foregroundStyle(color.opacity(0.7))
                    }
                }

                if let label = tool.resultLabel {
                    Text(label)
                        .font(.system(.caption, design: .rounded, weight: .medium))
                        .foregroundStyle(.secondary)
                }

                if let range = tool.normalRange {
                    MetadataChip(icon: "target", text: "Normal: \(range)", color: .green)
                }

                if let interp {
                    Text(interp.label)
                        .font(.system(.headline, design: .rounded, weight: .bold))
                        .foregroundStyle(color)
                    if let action = interp.action {
                        Text(action)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                // Action buttons
                HStack(spacing: 16) {
                    Button {
                        copyResult(value, interp: interp)
                    } label: {
                        Label(
                            copied ? "Copied!" : "Copy",
                            systemImage: copied ? "checkmark.circle.fill" : "doc.on.doc"
                        )
                        .font(.system(.caption, design: .rounded, weight: .semibold))
                        .foregroundStyle(copied ? .green : AppTheme.teal)
                    }
                    
                    Button {
                        showShareSheet = true
                    } label: {
                        Label("Share", systemImage: "square.and.arrow.up")
                            .font(.system(.caption, design: .rounded, weight: .semibold))
                            .foregroundStyle(.blue)
                    }
                }
                .sheet(isPresented: $showShareSheet) {
                    ShareSheet(text: generateResultText(value, interp: interp))
                }
            }
        }
    }

    private func formatResult(_ value: Double) -> String {
        if value == value.rounded() {
            return String(format: "%.0f", value)
        }
        return String(format: "%.1f", value)
    }

    private func generateResultText(_ value: Double, interp: ScoreInterpretation?) -> String {
        var text = "\(tool.title)\n"
        text += "Result: \(formatResult(value))"
        if let unit = tool.resultUnit { text += " \(unit)" }
        if let interp {
            text += "\nInterpretation: \(interp.label)"
            if let action = interp.action, !action.isEmpty {
                text += "\nRecommendation: \(action)"
            }
        }
        if let range = tool.normalRange {
            text += "\nNormal range: \(range)"
        }
        
        // Include inputs
        if let inputs = tool.inputs, !inputs.isEmpty {
            text += "\n\nInputs:"
            for input in inputs {
                if let val = inputValues[input.id], !val.isEmpty {
                    text += "\n• \(input.label): \(val)"
                    if let unit = input.unit { text += " \(unit)" }
                } else if let val = selectValues[input.id] {
                    text += "\n• \(input.label): \(val)"
                }
            }
        }
        
        text += "\n\n— Generated by Neuro Plans"
        return text
    }

    private func copyResult(_ value: Double, interp: ScoreInterpretation?) {
        UIPasteboard.general.string = generateResultText(value, interp: interp)
        withAnimation { copied = true }
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            withAnimation { copied = false }
        }
    }

    private func calculateResult() {
        guard tool.formula != nil else { return }

        // Parse inputs into values
        var vals: [String: Double] = [:]
        for input in tool.inputs ?? [] {
            if input.type == "number" || input.type == "decimal" {
                vals[input.id] = Double(inputValues[input.id] ?? "") ?? 0
            }
        }

        // Use the calculator engine
        let computed = CalculatorEngine.calculate(
            toolId: tool.id,
            vals: vals,
            selectValues: selectValues
        )

        withAnimation(.snappy) {
            result = computed
        }
    }
}

// MARK: - Protocol Content

private struct ProtocolContent: View {
    let tool: NeurologyTool
    @State private var completedStages: Set<String> = []

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            if let stages = tool.stages {
                ForEach(stages) { stage in
                    protocolStageCard(stage)
                }
            }
        }
        .padding(.horizontal)
    }

    private func protocolStageCard(_ stage: ProtocolStage) -> some View {
        let isComplete = completedStages.contains(stage.id)

        return GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 10) {
                // Stage header
                HStack {
                    Text(stage.time)
                        .font(.system(.caption, design: .monospaced, weight: .bold))
                        .foregroundStyle(.white)
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(.red, in: RoundedRectangle(cornerRadius: 6))

                    Text(stage.title)
                        .font(.system(.subheadline, design: .rounded, weight: .semibold))

                    Spacer()

                    Button {
                        withAnimation(.snappy) {
                            if isComplete {
                                completedStages.remove(stage.id)
                            } else {
                                completedStages.insert(stage.id)
                            }
                        }
                    } label: {
                        Image(systemName: isComplete ? "checkmark.circle.fill" : "circle")
                            .foregroundStyle(isComplete ? .green : .secondary)
                    }
                }

                // Steps
                ForEach(Array(stage.steps.enumerated()), id: \.offset) { idx, step in
                    HStack(alignment: .top, spacing: 8) {
                        Text("\(idx + 1).")
                            .font(.system(.caption, design: .rounded, weight: .bold))
                            .foregroundStyle(.secondary)
                            .frame(width: 20, alignment: .trailing)
                        Text(step)
                            .font(.system(.caption))
                            .foregroundStyle(isComplete ? .secondary : .primary)
                            .strikethrough(isComplete)
                    }
                }
            }
        }
    }
}

// MARK: - Reference Table Content

private struct ReferenceTableContent: View {
    let tool: NeurologyTool

    var body: some View {
        if let table = tool.tableData {
            VStack(alignment: .leading, spacing: 0) {
                // Header row
                ScrollView(.horizontal, showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {
                        // Column headers
                        HStack(spacing: 0) {
                            ForEach(Array(table.columns.enumerated()), id: \.offset) { idx, col in
                                Text(col)
                                    .font(.system(.caption2, design: .rounded, weight: .bold))
                                    .foregroundStyle(AppTheme.teal)
                                    .frame(width: columnWidth(idx, total: table.columns.count), alignment: .leading)
                                    .padding(.vertical, 8)
                                    .padding(.horizontal, 6)
                            }
                        }
                        .background(AppTheme.teal.opacity(0.1))

                        // Data rows
                        ForEach(Array(table.rows.enumerated()), id: \.offset) { rowIdx, row in
                            HStack(spacing: 0) {
                                ForEach(Array(row.enumerated()), id: \.offset) { colIdx, cell in
                                    Text(cell)
                                        .font(.system(.caption2))
                                        .foregroundStyle(colIdx == 0 ? .primary : .secondary)
                                        .fontWeight(colIdx == 0 ? .medium : .regular)
                                        .frame(width: columnWidth(colIdx, total: table.columns.count), alignment: .leading)
                                        .padding(.vertical, 6)
                                        .padding(.horizontal, 6)
                                }
                            }
                            .background(rowIdx % 2 == 0 ? .clear : .white.opacity(0.03))
                        }
                    }
                }
            }
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius))
            .overlay {
                RoundedRectangle(cornerRadius: AppTheme.smallCornerRadius)
                    .strokeBorder(.white.opacity(0.1), lineWidth: 0.5)
            }
            .padding(.horizontal)
        }
    }

    private func columnWidth(_ index: Int, total: Int) -> CGFloat {
        // First column wider for labels
        if index == 0 {
            return total <= 3 ? 120 : 100
        }
        return total <= 3 ? 120 : 90
    }
}

#Preview {
    NavigationStack {
        ToolDetailView(tool: NeurologyTool(
            id: "test", title: "Test Calculator", category: "calculator",
            description: "A test", inputs: nil, formula: nil,
            resultLabel: nil, resultUnit: nil, normalRange: nil,
            interpretation: nil, stages: nil, tableData: nil,
            clinicalPearls: nil, relatedPlans: []
        ))
    }
}
