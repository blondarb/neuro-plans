import SwiftUI

struct PriorityBadge: View {
    let priority: Priority

    var body: some View {
        if priority.isApplicable {
            Text(priority.rawValue)
                .font(.system(.caption2, design: .rounded, weight: .bold))
                .foregroundStyle(priority.color)
                .padding(.horizontal, 8)
                .padding(.vertical, 3)
                .background(priority.backgroundColor, in: Capsule())
        }
    }
}

#Preview {
    HStack(spacing: 8) {
        PriorityBadge(priority: .stat)
        PriorityBadge(priority: .urgent)
        PriorityBadge(priority: .routine)
        PriorityBadge(priority: .ext)
    }
    .padding()
}
