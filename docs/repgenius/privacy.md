---
title: RepGenius — Privacy Policy
hide:
  - navigation
  - toc
---

# RepGenius — Privacy Policy

*Last updated: February 14, 2026*

Steven Arbogast ("we," "our," or "us") operates the RepGenius mobile application (the "App"), an AI-powered fitness coach for iOS and Apple Watch.

## Overview

RepGenius generates personalized workout plans using artificial intelligence. We collect only what is necessary to provide the service and give you full control over your data.

## Information We Collect

**Account Information.** If you create an account (required for Free, Basic, and Pro tiers), we collect your email address for authentication purposes. Accounts are managed through Supabase, our backend provider.

**Health and Fitness Data.** With your permission, RepGenius reads data from Apple Health (such as age, weight, and activity history) to personalize workout recommendations. Completed workouts may be saved back to Apple Health. This data is processed on your device and is not sent to our servers.

**Motion Data.** The Apple Watch companion app uses accelerometer data to count exercise repetitions in real time. This data is processed entirely on your device and is never transmitted or stored.

**Voice Input (Optional).** If you use voice input to describe workout preferences, audio is processed on your device using Apple's Speech framework. Audio recordings are not stored or transmitted to our servers.

**Workout Generation Requests.** When you generate a workout, your fitness profile (goals, experience level, available equipment) and the AI prompt are sent to our server to generate your plan. We do not store the content of generated workouts on our servers.

**Usage Data.** We track workout generation counts to enforce tier limits (e.g., 3 per week for Trial, 1 per month for Free). These counts are stored locally in your device's Keychain.

## API Keys (BYOK Users)

Basic tier users may provide their own OpenAI API key. This key is stored securely in your device's Keychain and is sent directly from your device to OpenAI. We never see or store your API key.

## How We Use Your Information

- **Authentication:** To verify your identity and manage your subscription
- **Workout Generation:** To create personalized AI-generated workout plans
- **Tier Enforcement:** To apply workout limits based on your subscription
- **Service Improvement:** Aggregated, anonymous usage patterns may inform future development

## Third-Party Services

- **Supabase:** Handles authentication and routes workout generation requests. [Supabase Privacy Policy](https://supabase.com/privacy)
- **OpenAI:** Workout generation requests are processed by OpenAI. Requests are routed through our backend proxy (for Trial, Free, and Pro tiers) so your identity is not shared with OpenAI. BYOK users connect directly. [OpenAI Privacy Policy](https://openai.com/privacy)
- **Apple:** StoreKit handles subscriptions and payments. HealthKit handles fitness data. [Apple Privacy Policy](https://www.apple.com/privacy/)

## Data Storage and Security

- Health and motion data stays on your device
- API keys are stored in your device's encrypted Keychain
- Authentication tokens are managed securely through Supabase
- Workout generation uses HTTPS for all network communication
- We do not use third-party analytics or advertising services

## Subscriptions and Payments

Subscriptions are managed entirely by Apple through StoreKit. We do not collect, store, or have access to your payment information.

## Data Retention and Deletion

- Your workout history is stored locally on your device
- Uninstalling the App removes all local data
- To delete your account and server-side data, contact support@neuroplans.app
- Usage tracking data in Keychain persists across reinstalls but contains no personal information

## Children's Privacy

RepGenius is not intended for children under 13. We do not knowingly collect information from children.

## Changes

We may update this policy and will post changes at this URL.

## Contact

support@neuroplans.app
