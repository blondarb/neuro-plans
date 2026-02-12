import SwiftUI

struct GlassCard<Content: View>: View {
    var cornerRadius: CGFloat = AppTheme.cornerRadius
    @ViewBuilder var content: () -> Content

    var body: some View {
        content()
            .padding(AppTheme.cardPadding)
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: cornerRadius))
            .overlay {
                RoundedRectangle(cornerRadius: cornerRadius)
                    .strokeBorder(.white.opacity(0.1), lineWidth: 0.5)
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
