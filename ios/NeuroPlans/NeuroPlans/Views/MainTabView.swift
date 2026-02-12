import SwiftUI

struct MainTabView: View {
    @Environment(PlanBuilder.self) private var builder

    var body: some View {
        TabView {
            HomeView()
                .tabItem {
                    Label("Plans", systemImage: "list.bullet.clipboard")
                }

            ReferenceHomeView()
                .tabItem {
                    Label("Reference", systemImage: "book.fill")
                }

            FavoritesView()
                .tabItem {
                    Label("Favorites", systemImage: "star.fill")
                }

            BuilderView()
                .tabItem {
                    Label("Builder", systemImage: "square.and.pencil")
                }
                .badge(builder.itemCount)

            SettingsView()
                .tabItem {
                    Label("Settings", systemImage: "gearshape.fill")
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
