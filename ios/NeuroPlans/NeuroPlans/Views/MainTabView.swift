import SwiftUI

struct MainTabView: View {
    @Environment(PlanBuilder.self) private var builder

    var body: some View {
        TabView {
            Tab("Plans", systemImage: "list.bullet.clipboard") {
                HomeView()
            }

            Tab("Reference", systemImage: "book.fill") {
                ReferenceHomeView()
            }

            Tab("Favorites", systemImage: "star.fill") {
                FavoritesView()
            }

            Tab("Builder", systemImage: "square.and.pencil") {
                BuilderView()
            }
            .badge(builder.itemCount)

            Tab("Settings", systemImage: "gearshape.fill") {
                SettingsView()
            }
        }
        .tint(AppTheme.teal)
    }
}

#Preview {
    MainTabView()
        .environment(PlanStore())
        .environment(PlanBuilder())
        .environment(ReferenceStore())
}
