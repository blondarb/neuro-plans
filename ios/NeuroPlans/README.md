# Neuro Plans - iOS App

Native iPhone app for clinical decision support in neurology. Powered by 166 evidence-based clinical plans.

## Requirements

- macOS 14+ (Sonoma)
- Xcode 15+
- iOS 17+ deployment target
- XcodeGen (for project generation)

## Quick Start

### Option A: XcodeGen (Recommended)

```bash
# Install XcodeGen if needed
brew install xcodegen

# Generate Xcode project
cd ios/NeuroPlans
xcodegen generate

# Open in Xcode
open NeuroPlans.xcodeproj
```

### Option B: Manual Xcode Setup

1. Open Xcode → File → New → Project → iOS App
2. Product Name: "NeuroPlans", Interface: SwiftUI, Language: Swift
3. Set deployment target to iOS 17.0
4. Delete the default ContentView.swift
5. Drag all files from `NeuroPlans/` folder into the project
6. Ensure `plans.json` is added to the target (Build Phases → Copy Bundle Resources)
7. Build and run

## Architecture

- **SwiftUI** with `@Observable` (iOS 17+)
- **MVVM** pattern
- **NavigationStack** with type-safe navigation
- **Glass morphism** dark UI with `.ultraThinMaterial`

## Project Structure

```
NeuroPlans/
├── NeuroPlansApp.swift          # App entry point
├── Models/
│   ├── Plan.swift               # All data models (Plan, items, dosing)
│   └── Category.swift           # 18 category definitions
├── Services/
│   ├── PlanStore.swift          # Data loading, search, favorites
│   └── PlanBuilder.swift        # Plan builder state, export
├── Theme/
│   └── Theme.swift              # Design system, colors, glass effects
├── Views/
│   ├── MainTabView.swift        # Tab navigation
│   ├── Home/                    # Home screen, category cards
│   ├── Browse/                  # Plan list, search results
│   ├── Detail/                  # Plan detail, section views, item rows
│   ├── Builder/                 # Plan builder, export
│   ├── Favorites/               # Favorites list
│   ├── Settings/                # Settings, feedback
│   └── Components/              # Reusable UI components
├── Resources/
│   └── plans.json               # 166 clinical plans (11MB)
└── Assets.xcassets/             # Colors, app icon
```

## Features

- **166 clinical plans** covering all major neurological diagnoses
- **Setting filter** (ED / Hospital / Outpatient / ICU) — see only relevant items
- **Priority badges** (STAT / URGENT / ROUTINE / EXT) color-coded
- **Plan Builder** — select items across plans, export as text
- **Dose options** — tap to copy order sentences to clipboard
- **Progressive disclosure** — tap info icons for rationale, contraindications, monitoring
- **Favorites** — quick access to frequently used plans
- **Search** — fuzzy search across plan names, ICD-10 codes, scope
- **Dark mode** glass morphism UI
- **Haptic feedback** on selections
- **Offline** — all data bundled, no internet required

## Updating Data

To refresh the plans database:

```bash
# From project root
cp docs/data/plans.json ios/NeuroPlans/NeuroPlans/Resources/plans.json
```

Then rebuild in Xcode.
