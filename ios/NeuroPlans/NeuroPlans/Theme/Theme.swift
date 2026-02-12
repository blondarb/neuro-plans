import SwiftUI

// MARK: - Design System

enum AppTheme {
    // Brand colors
    static let teal = Color(red: 0.051, green: 0.580, blue: 0.533)       // #0D9488
    static let tealDark = Color(red: 0.059, green: 0.463, blue: 0.431)   // #0F766E
    static let tealLight = Color(red: 0.800, green: 0.984, blue: 0.945)  // #CCFBF1

    // Priority colors
    static let statColor = Color.red
    static let urgentColor = Color.orange
    static let routineColor = Color.blue
    static let extColor = Color.purple

    // Typography
    static let titleFont = Font.system(.title, design: .rounded, weight: .bold)
    static let headlineFont = Font.system(.headline, design: .rounded, weight: .semibold)
    static let bodyFont = Font.system(.body, design: .default)
    static let captionFont = Font.system(.caption, design: .default)

    // Spacing
    static let cardPadding: CGFloat = 16
    static let sectionSpacing: CGFloat = 20
    static let itemSpacing: CGFloat = 12
    static let cornerRadius: CGFloat = 16
    static let smallCornerRadius: CGFloat = 10

    // Glass effect
    static let glassOpacity: CGFloat = 0.15
}

// MARK: - Priority Color

extension Priority {
    var color: Color {
        switch self {
        case .stat: AppTheme.statColor
        case .urgent: AppTheme.urgentColor
        case .routine: AppTheme.routineColor
        case .ext: AppTheme.extColor
        case .na: .secondary
        }
    }

    var backgroundColor: Color {
        color.opacity(0.15)
    }
}

// MARK: - Category Color

extension PlanCategory {
    var swiftUIColor: Color {
        switch color {
        case "red": .red
        case "orange": .orange
        case "yellow": .yellow
        case "green": .green
        case "mint": .mint
        case "teal": .teal
        case "cyan": .cyan
        case "blue": .blue
        case "indigo": .indigo
        case "purple": .purple
        case "pink": .pink
        case "gray": .gray
        default: .teal
        }
    }
}

// MARK: - Glass Card Modifier

struct GlassBackground: ViewModifier {
    var cornerRadius: CGFloat = AppTheme.cornerRadius

    func body(content: Content) -> some View {
        content
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: cornerRadius))
    }
}

extension View {
    func glassBackground(cornerRadius: CGFloat = AppTheme.cornerRadius) -> some View {
        modifier(GlassBackground(cornerRadius: cornerRadius))
    }
}

// MARK: - Gradient Backgrounds

extension LinearGradient {
    static var appBackground: LinearGradient {
        LinearGradient(
            colors: [
                Color(red: 0.05, green: 0.10, blue: 0.15),
                Color(red: 0.02, green: 0.06, blue: 0.12)
            ],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
    }

    static var tealAccent: LinearGradient {
        LinearGradient(
            colors: [AppTheme.teal, AppTheme.tealDark],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
    }
}
