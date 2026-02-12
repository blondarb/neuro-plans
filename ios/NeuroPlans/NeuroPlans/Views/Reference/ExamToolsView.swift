import SwiftUI

// MARK: - Exam Tools Grid View

struct ExamToolsGridView: View {
    let tools: [ExamToolType] = ExamToolType.allCases
    
    var body: some View {
        ScrollView {
            LazyVGrid(columns: [
                GridItem(.flexible()),
                GridItem(.flexible())
            ], spacing: 16) {
                ForEach(tools, id: \.self) { tool in
                    NavigationLink {
                        ExamToolDetailView(toolType: tool)
                    } label: {
                        ExamToolCard(tool: tool)
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding()
        }
        .background(LinearGradient.appBackground.ignoresSafeArea())
        .navigationTitle("Exam Tools")
    }
}

// MARK: - Exam Tool Types

enum ExamToolType: String, CaseIterable, Hashable {
    case penlight = "Penlight"
    case redDesaturation = "Red Desaturation"
    case oknStripes = "OKN Stripes"
    case visualAcuity = "Visual Acuity"
    case amslerGrid = "Amsler Grid"
    case stopwatch = "Stopwatch"
    case pupilGauge = "Pupil Gauge"
    case reflexHammer = "Reflex Hammer"
    
    var icon: String {
        switch self {
        case .penlight: return "flashlight.on.fill"
        case .redDesaturation: return "circle.fill"
        case .oknStripes: return "line.3.horizontal"
        case .visualAcuity: return "eye"
        case .amslerGrid: return "grid"
        case .stopwatch: return "stopwatch.fill"
        case .pupilGauge: return "circle.circle"
        case .reflexHammer: return "hammer.fill"
        }
    }
    
    var color: Color {
        switch self {
        case .penlight: return .yellow
        case .redDesaturation: return .red
        case .oknStripes: return .blue
        case .visualAcuity: return .green
        case .amslerGrid: return .orange
        case .stopwatch: return .purple
        case .pupilGauge: return .cyan
        case .reflexHammer: return .brown
        }
    }
    
    var description: String {
        switch self {
        case .penlight: return "Pupil examination light with white and red options"
        case .redDesaturation: return "Test for optic nerve dysfunction"
        case .oknStripes: return "Optokinetic nystagmus testing"
        case .visualAcuity: return "Near vision card with distance guide"
        case .amslerGrid: return "Macular function and visual field test"
        case .stopwatch: return "Timer for timed neurological tests"
        case .pupilGauge: return "Standardized pupil size measurement"
        case .reflexHammer: return "For the creative examiner"
        }
    }
}

// MARK: - Exam Tool Card

struct ExamToolCard: View {
    let tool: ExamToolType
    
    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(spacing: 12) {
                Image(systemName: tool.icon)
                    .font(.system(size: 32))
                    .foregroundStyle(tool.color)
                
                Text(tool.rawValue)
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .multilineTextAlignment(.center)
                
                Text(tool.description)
                    .font(.caption2)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .lineLimit(2)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 8)
        }
    }
}

// MARK: - Exam Tool Detail View

struct ExamToolDetailView: View {
    let toolType: ExamToolType
    
    var body: some View {
        Group {
            switch toolType {
            case .penlight:
                PenlightToolView()
            case .redDesaturation:
                RedDesaturationToolView()
            case .oknStripes:
                OKNStripesToolView()
            case .visualAcuity:
                VisualAcuityToolView()
            case .amslerGrid:
                AmslerGridToolView()
            case .stopwatch:
                StopwatchToolView()
            case .pupilGauge:
                PupilGaugeToolView()
            case .reflexHammer:
                ReflexHammerToolView()
            }
        }
        .navigationTitle(toolType.rawValue)
        .navigationBarTitleDisplayMode(.inline)
    }
}

// MARK: - Penlight Tool

struct PenlightToolView: View {
    @State private var isOn = false
    @State private var isRed = false
    @State private var brightness: Double = 1.0
    
    private var lightColor: Color {
        isOn ? (isRed ? Color.red : Color.white) : Color.black
    }
    
    var body: some View {
        ZStack {
            // Light background - simple color fill
            lightColor
                .opacity(isOn ? brightness : 1.0)
                .ignoresSafeArea()
                .contentShape(Rectangle())
                .onTapGesture {
                    isOn.toggle()
                }
            
            // Controls when off
            if !isOn {
                VStack(spacing: 24) {
                    Image(systemName: "flashlight.off.fill")
                        .font(.system(size: 80))
                        .foregroundStyle(.gray)
                    
                    Text("Tap anywhere to turn on")
                        .font(.system(.headline, design: .rounded))
                        .foregroundStyle(.white)
                    
                    VStack(spacing: 16) {
                        Toggle("Red Light (dark adaptation)", isOn: $isRed)
                            .tint(.red)
                        
                        HStack {
                            Text("Brightness")
                            Slider(value: $brightness, in: 0.3...1.0)
                                .tint(isRed ? .red : .yellow)
                        }
                    }
                    .padding()
                    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                    .padding(.horizontal, 32)
                    
                    Text("White: pupil reflex testing\nRed: preserves dark adaptation")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                }
            }
        }
        .navigationBarHidden(isOn)
        .statusBarHidden(isOn)
    }
}

// MARK: - Red Desaturation Tool

struct RedDesaturationToolView: View {
    @State private var showInstructions = true
    
    var body: some View {
        ZStack {
            Color.red
                .ignoresSafeArea()
            
            if showInstructions {
                VStack(spacing: 20) {
                    Image(systemName: "eye.fill")
                        .font(.system(size: 60))
                        .foregroundStyle(.white)
                    
                    Text("Red Desaturation Test")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                        .foregroundStyle(.white)
                    
                    VStack(alignment: .leading, spacing: 12) {
                        instructionRow(number: "1", text: "Have patient cover one eye")
                        instructionRow(number: "2", text: "Show this red screen to the open eye")
                        instructionRow(number: "3", text: "Ask: \"Rate the redness from 0-100%\"")
                        instructionRow(number: "4", text: "Repeat with the other eye")
                        instructionRow(number: "5", text: "Compare the two values")
                    }
                    .padding()
                    .background(.black.opacity(0.3), in: RoundedRectangle(cornerRadius: 12))
                    
                    Text("A difference >20% suggests optic nerve dysfunction on the side seeing less red.")
                        .font(.caption)
                        .foregroundStyle(.white.opacity(0.9))
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                    
                    Button {
                        withAnimation {
                            showInstructions = false
                        }
                    } label: {
                        Text("Show Full Red Screen")
                            .font(.system(.headline, design: .rounded, weight: .semibold))
                            .foregroundStyle(.red)
                            .padding(.horizontal, 24)
                            .padding(.vertical, 12)
                            .background(.white, in: RoundedRectangle(cornerRadius: 10))
                    }
                }
                .padding()
            } else {
                VStack {
                    Spacer()
                    Button {
                        withAnimation {
                            showInstructions = true
                        }
                    } label: {
                        Text("Show Instructions")
                            .font(.caption)
                            .foregroundStyle(.white.opacity(0.7))
                            .padding(8)
                            .background(.black.opacity(0.3), in: RoundedRectangle(cornerRadius: 8))
                    }
                    .padding(.bottom, 40)
                }
            }
        }
        .statusBarHidden(!showInstructions)
    }
    
    private func instructionRow(number: String, text: String) -> some View {
        HStack(alignment: .top, spacing: 12) {
            Text(number)
                .font(.system(.caption, design: .rounded, weight: .bold))
                .foregroundStyle(.red)
                .frame(width: 20, height: 20)
                .background(.white, in: Circle())
            Text(text)
                .font(.system(.subheadline))
                .foregroundStyle(.white)
        }
    }
}

// MARK: - OKN Stripes Tool

struct OKNStripesToolView: View {
    @State private var isRunning = false
    @State private var speed: Double = 1.5
    @State private var direction: Bool = true // true = left, false = right
    @State private var phase: CGFloat = 0
    
    let stripeWidth: CGFloat = 50
    
    var body: some View {
        ZStack {
            // Background
            Color.gray.opacity(0.5)
                .ignoresSafeArea()
            
            // Animated stripes using phase offset
            if isRunning {
                TimelineView(.animation(minimumInterval: 0.016)) { timeline in
                    Canvas { context, size in
                        let stripeCount = Int(size.width / stripeWidth) + 4
                        let elapsed = timeline.date.timeIntervalSinceReferenceDate
                        let phaseOffset = CGFloat(elapsed * speed * 100).truncatingRemainder(dividingBy: stripeWidth * 2)
                        let adjustedOffset = direction ? -phaseOffset : phaseOffset
                        
                        for i in -2..<stripeCount {
                            let x = CGFloat(i) * stripeWidth + adjustedOffset
                            let rect = CGRect(x: x, y: 0, width: stripeWidth, height: size.height)
                            let color: Color = i % 2 == 0 ? .black : .white
                            context.fill(Path(rect), with: .color(color))
                        }
                    }
                }
                .ignoresSafeArea()
                .onTapGesture {
                    isRunning = false
                }
            }
            
            // Controls overlay
            if !isRunning {
                VStack(spacing: 24) {
                    Image(systemName: "line.3.horizontal")
                        .font(.system(size: 60))
                        .foregroundStyle(.blue)
                    
                    Text("OKN Stripes")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                    
                    Text("Optokinetic nystagmus testing")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                    
                    VStack(spacing: 16) {
                        HStack {
                            Text("Speed")
                                .frame(width: 70, alignment: .leading)
                            Slider(value: $speed, in: 0.5...3.0)
                                .tint(.blue)
                        }
                        
                        HStack {
                            Text("Direction")
                                .frame(width: 70, alignment: .leading)
                            Picker("", selection: $direction) {
                                Text("← Left").tag(true)
                                Text("Right →").tag(false)
                            }
                            .pickerStyle(.segmented)
                        }
                    }
                    .padding()
                    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                    .padding(.horizontal, 32)
                    
                    Button {
                        isRunning = true
                    } label: {
                        Label("Start", systemImage: "play.fill")
                            .font(.system(.headline, design: .rounded, weight: .semibold))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 32)
                            .padding(.vertical, 14)
                            .background(.blue, in: RoundedRectangle(cornerRadius: 10))
                    }
                    
                    VStack(spacing: 8) {
                        Text("Tap anywhere to stop")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        
                        Text("Normal: eyes follow stripes, then quick reset saccade opposite")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding(.horizontal)
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .background(LinearGradient.appBackground)
            }
        }
        .navigationBarHidden(isRunning)
        .statusBarHidden(isRunning)
    }
}

// MARK: - Visual Acuity Tool

struct VisualAcuityToolView: View {
    @State private var selectedLine = 4 // 20/40 default
    
    let acuityLines: [(String, String, CGFloat)] = [
        ("E", "20/200", 72),
        ("F P", "20/100", 48),
        ("T O Z", "20/70", 36),
        ("L P E D", "20/50", 28),
        ("P E C F D", "20/40", 22),
        ("E D F C Z P", "20/30", 18),
        ("F E L O P Z D", "20/25", 15),
        ("D E F P O T E C", "20/20", 12),
        ("L E F O D P C T", "20/15", 10),
    ]
    
    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                // Distance instruction card
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(spacing: 12) {
                        HStack {
                            Image(systemName: "ruler")
                                .foregroundStyle(.orange)
                            Text("Hold at 14 inches (35 cm) from eyes")
                                .font(.system(.headline, design: .rounded, weight: .semibold))
                        }
                        
                        Text("This is approximately the distance from your elbow to your fingertips")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                }
                .padding(.horizontal)
                
                // Acuity chart
                VStack(spacing: 8) {
                    ForEach(Array(acuityLines.enumerated()), id: \.offset) { index, line in
                        HStack {
                            Text(line.1)
                                .font(.system(.caption, design: .monospaced))
                                .foregroundStyle(.secondary)
                                .frame(width: 60, alignment: .leading)
                            
                            Spacer()
                            
                            Text(line.0)
                                .font(.system(size: line.2, weight: .medium, design: .monospaced))
                                .tracking(line.2 * 0.2)
                            
                            Spacer()
                            
                            // Tap indicator
                            Image(systemName: selectedLine == index ? "checkmark.circle.fill" : "circle")
                                .foregroundStyle(selectedLine == index ? .green : .secondary)
                                .frame(width: 60, alignment: .trailing)
                        }
                        .padding(.vertical, 4)
                        .contentShape(Rectangle())
                        .onTapGesture {
                            selectedLine = index
                        }
                        
                        if index < acuityLines.count - 1 {
                            Divider()
                        }
                    }
                }
                .padding()
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal)
                
                // Instructions
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Instructions")
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        
                        Text("• Test each eye separately\n• Patient should wear corrective lenses if used\n• Record the smallest line read correctly\n• Tap line to mark patient's acuity")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
                .padding(.horizontal)
                
                if selectedLine >= 0 {
                    Text("Selected: \(acuityLines[selectedLine].1)")
                        .font(.system(.headline, design: .rounded))
                        .foregroundStyle(.green)
                }
                
                Spacer(minLength: 100)
            }
            .padding(.top)
        }
        .background(LinearGradient.appBackground.ignoresSafeArea())
    }
}

// MARK: - Amsler Grid Tool

struct AmslerGridToolView: View {
    @State private var showInstructions = true
    
    let gridSize: Int = 20
    
    var body: some View {
        ZStack {
            Color.black
                .ignoresSafeArea()
            
            VStack {
                if showInstructions {
                    instructionsView
                } else {
                    gridView
                }
            }
        }
    }
    
    var instructionsView: some View {
        VStack(spacing: 20) {
            Image(systemName: "grid")
                .font(.system(size: 60))
                .foregroundStyle(.white)
            
            Text("Amsler Grid")
                .font(.system(.title2, design: .rounded, weight: .bold))
                .foregroundStyle(.white)
            
            GlassCard(cornerRadius: 12) {
                VStack(alignment: .leading, spacing: 12) {
                    Text("Distance: 12-14 inches (30-35 cm)")
                        .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        .foregroundStyle(.orange)
                    
                    instructionRow("1", "Patient wears reading glasses if needed")
                    instructionRow("2", "Cover one eye completely")
                    instructionRow("3", "Focus on the central dot")
                    instructionRow("4", "While looking at dot, note if any lines appear wavy, missing, or distorted")
                    instructionRow("5", "Repeat with other eye")
                }
            }
            .padding(.horizontal, 24)
            
            Text("Abnormal: Missing areas, wavy lines, or distortion suggests macular pathology")
                .font(.caption)
                .foregroundStyle(.white.opacity(0.8))
                .multilineTextAlignment(.center)
                .padding(.horizontal)
            
            Button {
                withAnimation {
                    showInstructions = false
                }
            } label: {
                Text("Show Grid")
                    .font(.system(.headline, design: .rounded, weight: .semibold))
                    .foregroundStyle(.black)
                    .padding(.horizontal, 32)
                    .padding(.vertical, 14)
                    .background(.white, in: RoundedRectangle(cornerRadius: 10))
            }
        }
        .padding()
    }
    
    var gridView: some View {
        GeometryReader { geo in
            let size = min(geo.size.width, geo.size.height) - 40
            let cellSize = size / CGFloat(gridSize)
            
            ZStack {
                // Grid lines
                Path { path in
                    for i in 0...gridSize {
                        let pos = CGFloat(i) * cellSize
                        // Vertical lines
                        path.move(to: CGPoint(x: pos, y: 0))
                        path.addLine(to: CGPoint(x: pos, y: size))
                        // Horizontal lines
                        path.move(to: CGPoint(x: 0, y: pos))
                        path.addLine(to: CGPoint(x: size, y: pos))
                    }
                }
                .stroke(Color.white, lineWidth: 0.5)
                
                // Center dot
                Circle()
                    .fill(Color.white)
                    .frame(width: 8, height: 8)
                    .position(x: size / 2, y: size / 2)
            }
            .frame(width: size, height: size)
            .position(x: geo.size.width / 2, y: geo.size.height / 2)
        }
        .onTapGesture {
            withAnimation {
                showInstructions = true
            }
        }
        .statusBarHidden(true)
    }
    
    private func instructionRow(_ number: String, _ text: String) -> some View {
        HStack(alignment: .top, spacing: 10) {
            Text(number)
                .font(.system(.caption, design: .rounded, weight: .bold))
                .frame(width: 20, height: 20)
                .background(AppTheme.teal, in: Circle())
            Text(text)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
    }
}

// MARK: - Stopwatch Tool

struct StopwatchToolView: View {
    @State private var elapsedTime: TimeInterval = 0
    @State private var isRunning = false
    @State private var timer: Timer?
    @State private var laps: [TimeInterval] = []
    
    var body: some View {
        VStack(spacing: 24) {
            // Timer display
            Text(formatTime(elapsedTime))
                .font(.system(size: 64, weight: .light, design: .monospaced))
                .foregroundStyle(.primary)
            
            // Preset buttons
            VStack(spacing: 8) {
                Text("Common Timed Tests")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                
                HStack(spacing: 12) {
                    presetButton("60s Upgaze", duration: 60)
                    presetButton("30s Hold", duration: 30)
                    presetButton("10m Walk", duration: nil)
                }
            }
            
            // Control buttons
            HStack(spacing: 32) {
                // Reset/Lap button
                Button {
                    if isRunning {
                        laps.insert(elapsedTime, at: 0)
                    } else {
                        elapsedTime = 0
                        laps.removeAll()
                    }
                } label: {
                    Text(isRunning ? "Lap" : "Reset")
                        .font(.system(.headline, design: .rounded))
                        .frame(width: 80, height: 80)
                        .background(.ultraThinMaterial, in: Circle())
                }
                
                // Start/Stop button
                Button {
                    toggleTimer()
                } label: {
                    Text(isRunning ? "Stop" : "Start")
                        .font(.system(.headline, design: .rounded, weight: .semibold))
                        .foregroundStyle(.white)
                        .frame(width: 80, height: 80)
                        .background(isRunning ? .red : .green, in: Circle())
                }
            }
            
            // Laps
            if !laps.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Laps")
                        .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    
                    ForEach(Array(laps.enumerated()), id: \.offset) { index, lap in
                        HStack {
                            Text("Lap \(laps.count - index)")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                            Spacer()
                            Text(formatTime(lap))
                                .font(.system(.body, design: .monospaced))
                        }
                    }
                }
                .padding()
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal)
            }
            
            Spacer()
        }
        .padding(.top, 40)
        .background(LinearGradient.appBackground.ignoresSafeArea())
        .onDisappear {
            timer?.invalidate()
        }
    }
    
    private func presetButton(_ title: String, duration: TimeInterval?) -> some View {
        Button {
            elapsedTime = 0
            laps.removeAll()
            if !isRunning {
                toggleTimer()
            }
        } label: {
            Text(title)
                .font(.system(.caption, design: .rounded, weight: .medium))
                .padding(.horizontal, 12)
                .padding(.vertical, 8)
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 8))
        }
    }
    
    private func toggleTimer() {
        if isRunning {
            timer?.invalidate()
            timer = nil
        } else {
            timer = Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true) { _ in
                elapsedTime += 0.01
            }
        }
        isRunning.toggle()
    }
    
    private func formatTime(_ time: TimeInterval) -> String {
        let minutes = Int(time) / 60
        let seconds = Int(time) % 60
        let hundredths = Int((time.truncatingRemainder(dividingBy: 1)) * 100)
        return String(format: "%02d:%02d.%02d", minutes, seconds, hundredths)
    }
}

// MARK: - Pupil Gauge Tool

struct PupilGaugeToolView: View {
    let pupilSizes: [CGFloat] = [2, 3, 4, 5, 6, 7, 8, 9]
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                // Instructions
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(spacing: 8) {
                        HStack {
                            Image(systemName: "info.circle.fill")
                                .foregroundStyle(.blue)
                            Text("Pupil Size Reference")
                                .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        }
                        Text("Compare patient's pupils to these standardized circles. Normal pupil size: 2-4mm in bright light, 4-8mm in dark.")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                }
                .padding(.horizontal)
                
                // Pupil circles
                LazyVGrid(columns: [
                    GridItem(.flexible()),
                    GridItem(.flexible()),
                    GridItem(.flexible()),
                    GridItem(.flexible())
                ], spacing: 20) {
                    ForEach(pupilSizes, id: \.self) { size in
                        VStack(spacing: 8) {
                            ZStack {
                                Circle()
                                    .fill(Color.white)
                                    .frame(width: 60, height: 60)
                                
                                Circle()
                                    .fill(Color.black)
                                    .frame(width: size * 5, height: size * 5) // Scale for visibility
                            }
                            
                            Text("\(Int(size)) mm")
                                .font(.system(.caption, design: .monospaced, weight: .medium))
                        }
                    }
                }
                .padding()
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                .padding(.horizontal)
                
                // Clinical reference
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Clinical Reference")
                            .font(.system(.subheadline, design: .rounded, weight: .semibold))
                        
                        VStack(alignment: .leading, spacing: 4) {
                            referenceRow("Miosis", "<2mm", "Opioids, pontine lesion, Horner")
                            referenceRow("Normal", "2-4mm", "Bright light")
                            referenceRow("Normal", "4-8mm", "Dim light")
                            referenceRow("Mydriasis", ">8mm", "CN III palsy, drugs, trauma")
                        }
                    }
                }
                .padding(.horizontal)
                
                Spacer(minLength: 100)
            }
            .padding(.top)
        }
        .background(LinearGradient.appBackground.ignoresSafeArea())
    }
    
    private func referenceRow(_ condition: String, _ size: String, _ causes: String) -> some View {
        HStack(alignment: .top) {
            Text(condition)
                .font(.caption)
                .fontWeight(.medium)
                .frame(width: 60, alignment: .leading)
            Text(size)
                .font(.system(.caption, design: .monospaced))
                .frame(width: 50, alignment: .leading)
            Text(causes)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
    }
}

// MARK: - Reflex Hammer Tool

struct ReflexHammerToolView: View {
    @State private var rotation: Double = 0
    @State private var showTip = true
    
    var body: some View {
        VStack(spacing: 24) {
            Spacer()
            
            // Hammer illustration using SF Symbols and shapes
            ZStack {
                // Handle
                RoundedRectangle(cornerRadius: 8)
                    .fill(LinearGradient(
                        colors: [Color.brown.opacity(0.8), Color.brown.opacity(0.6)],
                        startPoint: .leading,
                        endPoint: .trailing
                    ))
                    .frame(width: 20, height: 200)
                    .offset(y: 80)
                
                // Head
                Capsule()
                    .fill(LinearGradient(
                        colors: [Color.red.opacity(0.9), Color.red.opacity(0.7)],
                        startPoint: .top,
                        endPoint: .bottom
                    ))
                    .frame(width: 120, height: 50)
                    .overlay {
                        Capsule()
                            .strokeBorder(.white.opacity(0.3), lineWidth: 2)
                    }
            }
            .rotationEffect(.degrees(rotation))
            .gesture(
                RotationGesture()
                    .onChanged { value in
                        rotation = value.degrees
                    }
            )
            .onTapGesture {
                withAnimation(.spring(response: 0.3, dampingFraction: 0.5)) {
                    rotation = rotation == 0 ? 15 : 0
                }
            }
            
            Spacer()
            
            if showTip {
                GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
                    VStack(spacing: 12) {
                        Text("The Phone Reflex Test")
                            .font(.system(.headline, design: .rounded, weight: .semibold))
                        
                        Text("While we can't recommend using your phone as a reflex hammer, the firm edge of a smartphone can work in a pinch for eliciting reflexes.")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                        
                        Text("⚠️ Use the side edge, not the screen!")
                            .font(.caption)
                            .foregroundStyle(.orange)
                        
                        Button {
                            withAnimation {
                                showTip = false
                            }
                        } label: {
                            Text("Got it")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                .padding(.horizontal, 32)
            }
            
            Text("Tap or rotate the hammer")
                .font(.caption)
                .foregroundStyle(.secondary)
            
            Spacer()
        }
        .background(LinearGradient.appBackground.ignoresSafeArea())
    }
}

#Preview {
    NavigationStack {
        ExamToolsGridView()
    }
}
