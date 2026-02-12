import SwiftUI

struct MetadataChip: View {
    let icon: String
    let text: String
    var color: Color = .secondary

    var body: some View {
        HStack(spacing: 4) {
            Image(systemName: icon)
                .font(.system(size: 10))
            Text(text)
                .font(.system(.caption2, design: .default))
                .lineLimit(2)
        }
        .foregroundStyle(color)
        .padding(.horizontal, 8)
        .padding(.vertical, 4)
        .background(color.opacity(0.1), in: RoundedRectangle(cornerRadius: 6))
    }
}

// ICD-10 code badge
struct ICDCodeBadge: View {
    let code: String

    var body: some View {
        Text(cleanCode(code))
            .font(.system(.caption2, design: .monospaced, weight: .medium))
            .foregroundStyle(.secondary)
            .padding(.horizontal, 6)
            .padding(.vertical, 2)
            .background(.quaternary, in: RoundedRectangle(cornerRadius: 4))
    }

    private func cleanCode(_ code: String) -> String {
        // Strip "** " prefix and parenthetical descriptions
        var cleaned = code
            .replacingOccurrences(of: "** ", with: "")
            .replacingOccurrences(of: "**", with: "")
        if let parenRange = cleaned.range(of: " (") {
            cleaned = String(cleaned[cleaned.startIndex..<parenRange.lowerBound])
        }
        return cleaned.trimmingCharacters(in: .whitespaces)
    }
}

#Preview {
    VStack(spacing: 8) {
        MetadataChip(icon: "exclamationmark.triangle", text: "Active bleeding", color: .red)
        MetadataChip(icon: "clock", text: "Within 4.5h", color: .orange)
        ICDCodeBadge(code: "** G40.909 (Epilepsy, unspecified)")
        ICDCodeBadge(code: "I63.9")
    }
    .padding()
}
