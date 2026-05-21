import Foundation
import Supabase

/// Supabase client — retained only for Auth OTP email verification.
/// All data API calls (domains, analytics, plan requests) use APIService.
enum SupabaseService {
    static let client = SupabaseClient(
        supabaseURL: URL(string: SpecialtyConfig.supabaseUrl)!,
        supabaseKey: SpecialtyConfig.supabaseAnonKey
    )
}
