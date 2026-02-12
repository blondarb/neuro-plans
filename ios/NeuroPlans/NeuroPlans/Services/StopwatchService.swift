import SwiftUI
import Combine

@Observable
final class StopwatchService {
    var elapsedTime: TimeInterval = 0
    var isRunning = false
    var laps: [TimeInterval] = []
    
    /// When true, user is viewing the full stopwatch screen (hide floating)
    var isViewingFullScreen = false
    
    private var timer: Timer?
    private var startDate: Date?
    private var accumulatedTime: TimeInterval = 0
    
    func start() {
        guard !isRunning else { return }
        startDate = Date()
        timer = Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true) { [weak self] _ in
            self?.updateElapsedTime()
        }
        isRunning = true
    }
    
    func stop() {
        timer?.invalidate()
        timer = nil
        accumulatedTime = elapsedTime
        startDate = nil
        isRunning = false
    }
    
    func reset() {
        stop()
        elapsedTime = 0
        accumulatedTime = 0
        laps.removeAll()
    }
    
    func lap() {
        guard isRunning else { return }
        laps.insert(elapsedTime, at: 0)
    }
    
    func toggle() {
        if isRunning {
            stop()
        } else {
            start()
        }
    }
    
    private func updateElapsedTime() {
        guard let startDate = startDate else { return }
        elapsedTime = accumulatedTime + Date().timeIntervalSince(startDate)
    }
    
    func formattedTime(_ time: TimeInterval? = nil) -> String {
        let t = time ?? elapsedTime
        let minutes = Int(t) / 60
        let seconds = Int(t) % 60
        let hundredths = Int((t.truncatingRemainder(dividingBy: 1)) * 100)
        return String(format: "%02d:%02d.%02d", minutes, seconds, hundredths)
    }
    
    func formattedTimeCompact(_ time: TimeInterval? = nil) -> String {
        let t = time ?? elapsedTime
        let minutes = Int(t) / 60
        let seconds = Int(t) % 60
        if minutes > 0 {
            return String(format: "%d:%02d", minutes, seconds)
        } else {
            let hundredths = Int((t.truncatingRemainder(dividingBy: 1)) * 100)
            return String(format: "%02d.%02d", seconds, hundredths)
        }
    }
    
    /// Whether the stopwatch has any activity (running or has time)
    var isActive: Bool {
        isRunning || elapsedTime > 0
    }
    
    /// Whether to show the floating stopwatch
    var shouldShowFloating: Bool {
        isActive && !isViewingFullScreen
    }
}
