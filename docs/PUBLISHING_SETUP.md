# Neuro Plans — Publishing Setup

Documentation of infrastructure and accounts for App Store publishing.

## Domain

- **Domain:** neuroplans.app
- **Registrar:** Porkbun
- **Registered:** February 12, 2026
- **Expires:** February 12, 2027
- **Cost:** $10.81/year (first year), $14.93/year renewal
- **Includes:** WHOIS privacy, SSL certificate, email forwarding

## Email Forwarding

All forwarding addresses deliver to steven.d.arbogast@gmail.com via Porkbun Email Forwarding (free).

| Address | Purpose |
|---|---|
| developer@neuroplans.app | Apple Developer, App Store Connect |
| support@neuroplans.app | User support, legal docs contact |
| errors@neuroplans.app | Clinical error reports from app |
| blondarb@neuroplans.app | Account default |

## Apple Developer Program

- **Account holder:** Steven Arbogast
- **Enrollment type:** Individual
- **Enrolled:** February 12, 2026
- **Order:** W1477600147
- **Cost:** $99/year
- **Bundle ID:** com.neuroplans.app

## Legal Documents

Located in `docs/legal/`:

- `PRIVACY_POLICY.md` — Privacy Policy
- `TERMS_OF_SERVICE.md` — Terms of Service

These must be hosted at:

- https://neuroplans.app/privacy
- https://neuroplans.app/terms

Required URLs for App Store Connect submission.

## App Store Connect Checklist

- [ ] Host Privacy Policy and Terms of Service on neuroplans.app
- [ ] Create app record in App Store Connect
- [ ] Configure subscription product (com.neuroplans.annual, $12.99/year)
- [ ] Configure 14-day free trial offer
- [ ] Upload screenshots (6.7" and 6.1" iPhone required)
- [ ] Write App Store description and metadata
- [ ] Set age rating (Medical/Health — reference only)
- [ ] Submit for review

## Subscription Details

- **Product ID:** com.neuroplans.annual
- **Price:** $12.99 USD/year
- **Free trial:** 14 days
- **StoreKit config:** `ios/NeuroPlans/NeuroPlans/Configuration.storekit`

## Annual Costs

| Item | Cost |
|---|---|
| neuroplans.app domain | $14.93/year |
| Apple Developer Program | $99.00/year |
| Email forwarding | Free |
| **Total** | **$113.93/year** |
