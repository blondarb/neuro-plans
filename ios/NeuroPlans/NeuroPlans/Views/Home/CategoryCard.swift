import SwiftUI

struct CategoryCard: View {
    let category: PlanCategory

    var body: some View {
        GlassCard(cornerRadius: AppTheme.smallCornerRadius) {
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    Image(systemName: category.icon)
                        .font(.system(size: 22, weight: .semibold))
                        .foregroundStyle(category.swiftUIColor)
                        .frame(width: 36, height: 36)
                        .background(category.swiftUIColor.opacity(0.15))
                        .clipShape(RoundedRectangle(cornerRadius: 8))

                    Spacer()

                    Text("\(category.count)")
                        .font(.system(.caption, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                }

                Text(category.name)
                    .font(.system(.subheadline, design: .rounded, weight: .semibold))
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
            }
        }
    }
}

#Preview {
    LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 10) {
        ForEach(PlanCategory.all.prefix(6)) { cat in
            CategoryCard(category: cat)
        }
    }
    .padding()
    .background(Color.black)
}
