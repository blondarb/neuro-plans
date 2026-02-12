import SwiftUI

struct GlassCard<Content: View>: View {
    @Environment(\.colorScheme) var colorScheme
    var cornerRadius: CGFloat = AppTheme.cornerRadius
    @ViewBuilder var content: () -> Content

    var body: some View {
        content()
            .padding(AppTheme.cardPadding)
            .background {
                if colorScheme == .dark {
                    RoundedRectangle(cornerRadius: cornerRadius)
                        .fill(.ultraThinMaterial)
                } else {
                    RoundedRectangle(cornerRadius: cornerRadius)
                        .fill(Color(.systemBackground))
                        .shadow(
                            color: Color.black.opacity(0.06),
                            radius: 8,
                            x: 0,
                            y: 2
                        )
                }
            }
            .overlay {
                RoundedRectangle(cornerRadius: cornerRadius)
                    .strokeBorder(
                        colorScheme == .dark 
                            ? Color.white.opacity(0.08) 
                            : Color.black.opacity(0.04),
                        lineWidth: 0.5
                    )
            }
    }
}

struct GlassSectionHeader: View {
    let title: String
    let icon: String
    var count: Int? = nil

    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: icon)
                .font(.system(size: 14, weight: .semibold))
                .foregroundStyle(AppTheme.teal)
            Text(title)
                .font(AppTheme.headlineFont)
            Spacer()
            if let count {
                Text("\(count)")
                    .font(.system(.caption, design: .rounded, weight: .medium))
                    .foregroundStyle(.secondary)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 2)
                    .background(.quaternary, in: Capsule())
            }
        }
    }
}

#Preview {
    GlassCard {
        VStack(alignment: .leading, spacing: 8) {
            GlassSectionHeader(title: "Laboratory Workup", icon: "testtube.2", count: 12)
            Text("Sample content")
                .foregroundStyle(.secondary)
        }
    }
    .padding()
    .background(Color.black)
}
