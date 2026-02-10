# App Transition Strategy — Neuro Clinical Plans

**Date:** February 2026
**Purpose:** Evaluate paths from the current MkDocs static site to a mobile-friendly clinical application
**Current State:** MkDocs Material static site hosted on Vercel/GitHub Pages

---

## 1. Requirements Summary

Based on the UX Audit and Benchmark Comparison, the mobile/app transition must deliver:

| Requirement | Priority | Rationale |
|------------|----------|-----------|
| Works well on phones (375px+) | **Critical** | Clinicians use phones at bedside |
| Offline access to plans | **High** | Hospital WiFi is unreliable |
| Fast load times (<3s) | **High** | Clinical urgency requires instant access |
| Dark mode everywhere | **High** | On-call/low-light usage |
| Installable / home screen | **Medium** | Quick launch without browser URL entry |
| Push notifications | **Low** | New plan alerts (nice to have, not essential) |
| Native device features | **Low** | No camera, GPS, or sensor needs |

---

## 2. Options Evaluated

### Option A: Progressive Web App (PWA)

**What it is:** Add a service worker and web app manifest to the existing MkDocs site to enable offline caching, home screen installation, and app-like behavior.

**Implementation:**
- Add `manifest.json` with app name, icons, theme color
- Add service worker for offline caching (cache-first strategy for plan pages)
- Add MkDocs plugin or custom script to generate service worker at build time
- Configure `<meta>` tags for iOS home screen support

**Effort:** 1-2 weeks

**Pros:**
- ✅ Lowest effort — builds on existing MkDocs infrastructure
- ✅ No new tech stack to learn or maintain
- ✅ Single codebase (same site, same deployment)
- ✅ Instant updates (no app store review process)
- ✅ Works on all platforms (iOS, Android, desktop)
- ✅ Offline access via service worker cache
- ✅ Home screen installable on both iOS and Android
- ✅ Free — no app store developer fees

**Cons:**
- ❌ iOS Safari has limited PWA support (no push notifications until iOS 16.4+, 50MB cache limit)
- ❌ Still fundamentally a website — table-heavy layouts remain hard on mobile
- ❌ No app store presence (discoverability)
- ❌ Cannot deeply customize navigation patterns (still MkDocs sidebar)
- ❌ Performance depends on browser engine, not native

**Risk:** LOW — worst case, it is simply the existing site with offline caching added.

---

### Option B: React/Expo Native App

**What it is:** Build a native mobile application using React Native (via Expo framework) that reads the existing JSON data layer.

**Implementation:**
- New Expo project with React Navigation
- Custom screens for: Plan List, Plan Detail, Clinical Tool, Search, Settings
- Fetch JSON data from the existing `plans.json` or a Supabase API
- Implement native components for tables, badges, dosing details
- Publish to iOS App Store and Google Play

**Effort:** 3-6 months

**Pros:**
- ✅ Full native experience with platform-specific UI patterns
- ✅ True offline with SQLite or AsyncStorage
- ✅ App store presence and discoverability
- ✅ Push notifications (new plans, guideline updates)
- ✅ Better performance for interactive features
- ✅ Can design mobile-optimized table layouts (card-based, collapsible)

**Cons:**
- ❌ High effort — entirely new codebase to build and maintain
- ❌ Two codebases to maintain (web + app)
- ❌ Content updates require app rebuild or API integration
- ❌ Apple developer account ($99/year) + Google Play ($25 one-time)
- ❌ App store review process for each update
- ❌ React Native expertise required
- ❌ Must re-implement all existing features (search, dark mode, comments)

**Risk:** HIGH — large investment for a single-developer project. Maintenance burden could become unsustainable.

---

### Option C: Capacitor Hybrid App

**What it is:** Wrap the existing MkDocs site in a native shell using Capacitor (by Ionic), giving it access to native features while keeping the web codebase.

**Implementation:**
- Install Capacitor in the project
- Configure native shell (app icon, splash screen, status bar)
- Build MkDocs site → copy to Capacitor `www/` directory
- Add Capacitor plugins for: offline storage, file system, status bar
- Publish to app stores

**Effort:** 2-4 weeks

**Pros:**
- ✅ Reuses existing web codebase (MkDocs output)
- ✅ Access to native APIs (offline storage, push notifications, status bar)
- ✅ App store presence
- ✅ Single codebase (web + app from same source)
- ✅ Lower effort than full native app
- ✅ Can incrementally add native features

**Cons:**
- ❌ Still renders web content in a WebView — same table layout issues on mobile
- ❌ Performance is web-limited (not truly native)
- ❌ Some features feel "web-in-a-box" rather than native
- ❌ Capacitor + MkDocs is an unusual combination with limited community examples
- ❌ Must still fix responsive layout issues before the app will feel good
- ❌ App store review may reject if it feels like a simple web wrapper

**Risk:** MEDIUM — depends on whether the responsive web issues are fixed first.

---

### Option D: Enhanced Responsive Web (No App)

**What it is:** Invest heavily in the responsive web experience without building an app. Focus on making the existing site excellent on mobile browsers.

**Implementation:**
- Add 375px breakpoint and small phone styles
- Redesign tables for mobile (card-based responsive table pattern)
- Add `prefers-color-scheme` and complete dark mode
- Optimize performance (lazy load comments, split JSON)
- Add "Add to Home Screen" prompt

**Effort:** 2-4 weeks

**Pros:**
- ✅ Addresses the actual problem (mobile usability) directly
- ✅ No new infrastructure
- ✅ Benefits all users (desktop too)
- ✅ Fastest path to improved mobile experience
- ✅ No app store maintenance

**Cons:**
- ❌ No offline access (unless combined with PWA)
- ❌ No app store presence
- ❌ Limited by MkDocs template system for layout customization

**Risk:** LOW — improvements are incremental and reversible.

---

## 3. Recommendation

### Recommended Path: **Option D + Option A** (Enhanced Responsive + PWA)

**Phase 1 (Weeks 1-2): Enhanced Responsive Web**
Fix the critical mobile usability issues first:
- Add 375px breakpoint
- Implement responsive table pattern (card-based on mobile, or horizontal scroll with sticky first column)
- Complete dark mode for all components
- Increase minimum touch targets to 44px
- Add sticky table headers

**Phase 2 (Week 3): PWA Layer**
Add PWA capabilities to the improved site:
- Service worker with cache-first strategy for plan pages
- Web app manifest with icons and theme color
- Offline fallback page
- "Add to Home Screen" prompt

**Phase 3 (Month 2-3): Progressive Enhancement**
Add features that close the gap with competitors:
- localStorage-based favorites and recent plans
- Lazy-loaded comment system
- Improved search within Clinical Tool
- JSON data splitting for faster Clinical Tool load

**Future Option: Native App (Only if needed)**
Only pursue a native app (Option B or C) if:
- User analytics show >60% mobile usage
- Offline access is insufficient via PWA
- Push notifications become a requirement
- App store presence is needed for credibility

### Why Not Native First?

1. **The mobile problem is a layout problem, not a platform problem.** The tables are hard to read on mobile because of CSS, not because it is a website. Fixing the CSS fixes the problem on all platforms.

2. **Maintenance burden matters.** This is a physician-maintained project. Adding a separate native codebase doubles the maintenance work for someone whose primary job is clinical, not engineering.

3. **PWA gets 80% of native benefits.** With a service worker, the site loads offline. With a manifest, it installs to the home screen. With proper responsive CSS, it looks and feels like an app on mobile.

4. **The content update model favors web.** Plans are updated via git push → Vercel deploy. An app store update cycle adds days of delay to getting corrected clinical information to users.

---

## 4. Technical Implementation Notes

### Service Worker Strategy

```
Cache Strategy: Stale-While-Revalidate for plan pages
  - Serve cached version immediately
  - Fetch updated version in background
  - Update cache for next visit

Pre-cache:
  - All 144 plan HTML pages (~50KB each ≈ 7MB total)
  - CSS and JS assets
  - plans.json for Clinical Tool
  - Home page and index pages

Do NOT cache:
  - Firebase/comment system (requires network)
  - Draft pages (change frequently)
```

### Web App Manifest

```json
{
  "name": "Neuro Clinical Plans",
  "short_name": "NeuroPlan",
  "description": "Evidence-based neurology decision support",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0d9488",
  "theme_color": "#0d9488",
  "orientation": "any",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

### Responsive Table Pattern (Mobile)

On screens <768px, transform data tables into card stacks:

```
Desktop (table):
| Item        | ED    | HOSP  | OPD   | ICU   | Rationale       |
|-------------|-------|-------|-------|-------|-----------------|
| CBC w/ diff | STAT  | STAT  | ROUT  | STAT  | Baseline blood  |

Mobile (card):
┌─────────────────────────────────┐
│ CBC w/ diff                     │
│ ED: STAT  HOSP: STAT  ICU: STAT│
│ OPD: ROUTINE                    │
│ Baseline blood counts           │
└─────────────────────────────────┘
```

---

## 5. Decision Summary

| Approach | Effort | Mobile Quality | Offline | Maintenance | **Recommendation** |
|----------|--------|---------------|---------|-------------|-------------------|
| PWA only | 1-2 wk | ⚠️ Same layout | ✅ | Low | Not enough alone |
| React Native | 3-6 mo | ✅ Excellent | ✅ | High | Overkill for now |
| Capacitor | 2-4 wk | ⚠️ WebView | ✅ | Medium | Premature |
| Enhanced Responsive | 2-4 wk | ✅ Good | ❌ | Low | Foundation first |
| **Responsive + PWA** | **3-4 wk** | **✅ Good** | **✅** | **Low** | **✅ Recommended** |

---

*End of App Strategy. See also: [UX Audit](UX_AUDIT.md) | [UI Audit](UI_AUDIT.md) | [Design System](DESIGN_SYSTEM.md) | [Roadmap](ROADMAP.md)*
