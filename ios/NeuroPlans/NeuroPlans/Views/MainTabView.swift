import SwiftUI

struct MainTabView: View {
    @Environment(PlanBuilder.self) private var builder
    @Environment(StopwatchService.self) private var stopwatch
    @Environment(EntitlementService.self) private var entitlement
    
    @State private var showPaywall = false

    var body: some View {
        ZStack(alignment: .bottom) {
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
            
            // Floating Stopwatch Overlay - positioned above tab bar
            if stopwatch.shouldShowFloating {
                FloatingStopwatchView()
                    .padding(.bottom, 90) // Above the tab bar
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                    .animation(.snappy(duration: 0.3), value: stopwatch.shouldShowFloating)
            }
            
            // Trial status banner (when in trial)
            if case .trial(let days) = entitlement.accessLevel, days <= 7 {
                TrialBannerView(daysRemaining: days) {
                    showPaywall = true
                }
                .padding(.bottom, 90)
                .transition(.move(edge: .bottom).combined(with: .opacity))
            }
        }
        .fullScreenCover(isPresented: $showPaywall) {
            PaywallView()
        }
        .onAppear {
            // Show paywall if trial expired
            if entitlement.shouldShowPaywall {
                showPaywall = true
            }
        }
        .onChange(of: entitlement.accessLevel) { _, newValue in
            // Show paywall when trial expires
            if case .expired = newValue {
                showPaywall = true
            }
        }
    }
}

// MARK: - Trial Banner View

private struct TrialBannerView: View {
    let daysRemaining: Int
    let onUpgrade: () -> Void
    
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: "clock.fill")
                .foregroundStyle(.orange)
            
            Text("\(daysRemaining) day\(daysRemaining == 1 ? "" : "s") left in trial")
                .font(.system(.subheadline, design: .rounded, weight: .medium))
            
            Spacer()
            
            Button {
                onUpgrade()
            } label: {
                Text("Upgrade")
                    .font(.system(.caption, design: .rounded, weight: .bold))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 6)
                    .background(AppTheme.teal, in: Capsule())
            }
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .background {
            if colorScheme == .dark {
                RoundedRectangle(cornerRadius: 12)
                    .fill(.ultraThinMaterial)
            } else {
                RoundedRectangle(cornerRadius: 12)
                    .fill(Color(.systemBackground))
                    .shadow(color: .black.opacity(0.1), radius: 8, y: 2)
            }
        }
        .overlay {
            RoundedRectangle(cornerRadius: 12)
                .strokeBorder(.orange.opacity(0.3), lineWidth: 1)
        }
        .padding(.horizontal, 16)
    }
}

// MARK: - Floating Stopwatch View

private struct FloatingStopwatchView: View {
    @Environment(StopwatchService.self) private var stopwatch
    @Environment(\.colorScheme) var colorScheme
    @State private var isExpanded = false
    
    var body: some View {
        VStack(spacing: 0) {
            // Mini display (always visible when floating)
            HStack(spacing: 12) {
                // Stopwatch icon with pulse animation
                ZStack {
                    Circle()
                        .fill(stopwatch.isRunning ? Color.green.opacity(0.2) : Color.orange.opacity(0.2))
                        .frame(width: 32, height: 32)
                    
                    Image(systemName: "stopwatch.fill")
                        .font(.system(size: 14, weight: .semibold))
                        .foregroundStyle(stopwatch.isRunning ? .green : .orange)
                }
                
                // Time display
                Text(stopwatch.formattedTime())
                    .font(.system(size: 18, weight: .medium, design: .monospaced))
                    .monospacedDigit()
                
                Spacer()
                
                // Quick controls
                HStack(spacing: 8) {
                    // Lap button (only when running)
                    if stopwatch.isRunning {
                        Button {
                            stopwatch.lap()
                        } label: {
                            Image(systemName: "flag.fill")
                                .font(.system(size: 12, weight: .semibold))
                                .foregroundStyle(.white)
                                .frame(width: 28, height: 28)
                                .background(.blue, in: Circle())
                        }
                    }
                    
                    // Play/Pause button
                    Button {
                        stopwatch.toggle()
                    } label: {
                        Image(systemName: stopwatch.isRunning ? "pause.fill" : "play.fill")
                            .font(.system(size: 12, weight: .semibold))
                            .foregroundStyle(.white)
                            .frame(width: 28, height: 28)
                            .background(stopwatch.isRunning ? .orange : .green, in: Circle())
                    }
                    
                    // Reset button (only when stopped)
                    if !stopwatch.isRunning {
                        Button {
                            stopwatch.reset()
                        } label: {
                            Image(systemName: "xmark")
                                .font(.system(size: 11, weight: .bold))
                                .foregroundStyle(.white)
                                .frame(width: 28, height: 28)
                                .background(.red.opacity(0.8), in: Circle())
                        }
                    }
                    
                    // Expand button
                    Button {
                        withAnimation(.snappy(duration: 0.25)) {
                            isExpanded.toggle()
                        }
                    } label: {
                        Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                            .font(.system(size: 11, weight: .bold))
                            .foregroundStyle(.secondary)
                            .frame(width: 28, height: 28)
                            .background(.quaternary, in: Circle())
                    }
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            
            // Expanded content (laps)
            if isExpanded && !stopwatch.laps.isEmpty {
                Divider()
                    .padding(.horizontal)
                
                ScrollView {
                    VStack(spacing: 6) {
                        ForEach(Array(stopwatch.laps.prefix(5).enumerated()), id: \.offset) { index, lap in
                            HStack {
                                Text("Lap \(stopwatch.laps.count - index)")
                                    .font(.system(size: 12))
                                    .foregroundStyle(.secondary)
                                Spacer()
                                Text(stopwatch.formattedTime(lap))
                                    .font(.system(size: 13, design: .monospaced))
                            }
                            .padding(.horizontal, 16)
                        }
                    }
                    .padding(.vertical, 8)
                }
                .frame(maxHeight: 120)
            }
        }
        .background {
            if colorScheme == .dark {
                RoundedRectangle(cornerRadius: 16)
                    .fill(.ultraThinMaterial)
            } else {
                RoundedRectangle(cornerRadius: 16)
                    .fill(Color(.systemBackground))
                    .shadow(color: Color.black.opacity(0.12), radius: 12, x: 0, y: 4)
            }
        }
        .overlay {
            RoundedRectangle(cornerRadius: 16)
                .strokeBorder(
                    colorScheme == .dark ? Color.white.opacity(0.1) : Color.black.opacity(0.05),
                    lineWidth: 0.5
                )
        }
        .padding(.horizontal, 16)
        .padding(.top, 8)
    }
}

#Preview {
    MainTabView()
        .environment(PlanStore())
        .environment(PlanBuilder())
        .environment(ReferenceStore())
        .environment(StopwatchService())
        .environment(UserPreferences())
        .environment(EntitlementService())
        .environment(SubscriptionService())
}
