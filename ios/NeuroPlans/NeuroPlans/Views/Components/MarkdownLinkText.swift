import SwiftUI

/// Renders a string containing markdown-style links `[text](url)` as tappable
/// attributed text. Linked portions open in Safari; unlinked text is plain.
/// Falls back to regular `Text` when the string has no links.
struct MarkdownLinkText: View {
    let text: String
    var font: Font = .system(.caption, design: .default)
    var color: Color = .primary

    var body: some View {
        Text(attributedString)
            .font(font)
            .tint(AppTheme.teal)
    }

    // MARK: - Attributed String Builder

    private var attributedString: AttributedString {
        let input = text
        var result = AttributedString()

        // Regex: [display text](url)
        let pattern = #"\[([^\]]+)\]\(([^)]+)\)"#
        guard let regex = try? NSRegularExpression(pattern: pattern) else {
            var plain = AttributedString(input)
            plain.foregroundColor = color
            return plain
        }

        let nsRange = NSRange(input.startIndex..., in: input)
        let matches = regex.matches(in: input, range: nsRange)

        var lastEnd = input.startIndex

        for match in matches {
            // Plain text before this link
            if let beforeRange = Range(match.range, in: input),
               lastEnd < beforeRange.lowerBound {
                var plain = AttributedString(String(input[lastEnd..<beforeRange.lowerBound]))
                plain.foregroundColor = color
                result.append(plain)
            }

            // Extract display text and URL
            if let displayRange = Range(match.range(at: 1), in: input),
               let urlRange = Range(match.range(at: 2), in: input),
               let url = URL(string: String(input[urlRange])) {
                var linked = AttributedString(String(input[displayRange]))
                linked.link = url
                linked.foregroundColor = AppTheme.teal
                result.append(linked)
            }

            // Advance past this match
            if let fullRange = Range(match.range, in: input) {
                lastEnd = fullRange.upperBound
            }
        }

        // Trailing plain text after the last link
        if lastEnd < input.endIndex {
            var plain = AttributedString(String(input[lastEnd...]))
            plain.foregroundColor = color
            result.append(plain)
        }

        // If no matches were found, just return the plain text
        if matches.isEmpty {
            var plain = AttributedString(input)
            plain.foregroundColor = color
            return plain
        }

        return result
    }
}

// MARK: - Preview

#Preview {
    VStack(alignment: .leading, spacing: 16) {
        MarkdownLinkText(
            text: "[AHA/ASA 2019 Guidelines (Powers et al.)](https://pubmed.ncbi.nlm.nih.gov/31662037/); [NINDS trial (NEJM 1995)](https://pubmed.ncbi.nlm.nih.gov/7477192/)"
        )

        MarkdownLinkText(
            text: "[MR CLEAN (Berkhemer et al. NEJM 2015)](https://pubmed.ncbi.nlm.nih.gov/25517348/), ESCAPE, EXTEND-IA, SWIFT-PRIME, REVASCAT"
        )

        MarkdownLinkText(text: "Expert consensus")

        MarkdownLinkText(text: "Standard of care for immobilized patients")
    }
    .padding()
}
