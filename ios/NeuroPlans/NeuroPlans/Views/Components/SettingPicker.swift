import SwiftUI

struct SettingPicker: View {
    @Binding var selected: ClinicalSetting

    var body: some View {
        HStack(spacing: 6) {
            ForEach(ClinicalSetting.allCases) { setting in
                Button {
                    withAnimation(.snappy(duration: 0.2)) {
                        selected = setting
                    }
                } label: {
                    HStack(spacing: 4) {
                        Image(systemName: setting.icon)
                            .font(.system(size: 11, weight: .semibold))
                        Text(setting.rawValue)
                            .font(.system(.caption, design: .rounded, weight: .semibold))
                    }
                    .padding(.horizontal, 12)
                    .padding(.vertical, 8)
                    .background {
                        if selected == setting {
                            Capsule()
                                .fill(AppTheme.teal)
                        } else {
                            Capsule()
                                .fill(.ultraThinMaterial)
                        }
                    }
                    .foregroundStyle(selected == setting ? .white : .secondary)
                }
                .buttonStyle(.plain)
                .sensoryFeedback(.selection, trigger: selected)
            }
        }
    }
}

#Preview {
    SettingPicker(selected: .constant(.opd))
        .padding()
        .background(Color.black)
}
