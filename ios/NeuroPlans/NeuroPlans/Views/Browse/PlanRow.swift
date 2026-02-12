import SwiftUI

struct PlanRow: View {
    let plan: Plan
    let setting: ClinicalSetting

    @Environment(PlanStore.self) private var store

    var body: some View {
        HStack(spacing: 12) {
            // Category indicator
            if let cat = PlanCategory.category(for: plan.id) {
                Circle()
                    .fill(cat.swiftUIColor)
                    .frame(width: 8, height: 8)
            }

            VStack(alignment: .leading, spacing: 4) {
                Text(plan.title)
                    .font(.system(.body, design: .rounded, weight: .medium))
                    .lineLimit(2)

                HStack(spacing: 6) {
                    // ICD-10 codes
                    ForEach(plan.icd10.prefix(2), id: \.self) { code in
                        ICDCodeBadge(code: code)
                    }
                    if plan.icd10.count > 2 {
                        Text("+\(plan.icd10.count - 2)")
                            .font(.system(size: 10))
                            .foregroundStyle(.tertiary)
                    }
                }

                // Settings availability
                HStack(spacing: 4) {
                    ForEach(ClinicalSetting.allCases) { s in
                        let available = planHasSetting(plan, setting: s)
                        Text(s.rawValue)
                            .font(.system(size: 9, weight: .medium, design: .rounded))
                            .foregroundStyle(available ? (s == setting ? .white : .secondary) : .quaternary)
                            .padding(.horizontal, 5)
                            .padding(.vertical, 2)
                            .background {
                                if s == setting && available {
                                    Capsule().fill(AppTheme.teal.opacity(0.8))
                                } else {
                                    Capsule().fill(.quaternary.opacity(0.3))
                                }
                            }
                    }
                }
            }

            Spacer()

            // Favorite indicator
            if store.isFavorite(plan.id) {
                Image(systemName: "star.fill")
                    .font(.system(size: 12))
                    .foregroundStyle(.yellow)
            }

            Image(systemName: "chevron.right")
                .font(.system(size: 12, weight: .semibold))
                .foregroundStyle(.tertiary)
        }
        .padding(.vertical, 4)
    }

    private func planHasSetting(_ plan: Plan, setting: ClinicalSetting) -> Bool {
        // Check if any item in any section has a non-"-" value for this setting
        for (_, subsections) in plan.sections.treatment {
            for item in subsections {
                if item.priority(for: setting).isApplicable { return true }
            }
        }
        for (_, subsections) in plan.sections.labWorkup {
            for item in subsections {
                if item.priority(for: setting).isApplicable { return true }
            }
        }
        return true // Default to available
    }
}

#Preview {
    List {
        PlanRow(
            plan: Plan(
                id: "sample",
                title: "Acute Ischemic Stroke",
                version: "1.0",
                icd10: ["I63.9", "I63.50"],
                scope: "Sample scope",
                notes: [],
                sections: PlanSections(
                    labWorkup: [:], imaging: [:],
                    treatment: [:], otherRecs: [:]
                ),
                differential: [], evidence: [],
                monitoring: [], disposition: []
            ),
            setting: .ed
        )
    }
    .environment(PlanStore())
}
