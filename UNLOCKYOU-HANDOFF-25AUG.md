# UnlockYou onboarding redesign — handoff · 25 Aug 2026

**Owner resting.** Next session: device QA only — no new design work unless something looks off on phone.

---

## Repo

| | |
|---|---|
| **Path** | `~/workspace/gratitudedaily` |
| **Branch** | `main` |
| **Display name** | UnlockYou |
| **Bundle** | `com.tranquilwaters.gratitudedaily` (unchanged) |
| **Design mocks** | `~/Desktop/aug_image/unlockyou/` (`screen01` … `screen09`) |

---

## Shipped in this push

Two commits on `main`:

1. **`f03ac3f`** — Pass 1 polish: Coach tab removed, home streak removed, green card colors, smoother card swipe, About in Controls, library tap→retry, Gemini `--` strip, font bumps.
2. **Latest** — Full onboarding redesign (9 screens) + shared chrome + paywall layout + UnlockYou brand in shield/settings/Gemini.

### Onboarding (all 9 screens)

| # | Screen | Notes |
|---|---|---|
| 1 | Hook | 38 days stat, coral sun card, white CTA |
| 2 | Promise | Vertical timeline + “One private minute” card |
| 3 | Time sink | 2×3 chips, coral selection, new labels |
| 4 | Desire | Focus / Presence / Confidence / **Creativity** / **Rest** |
| 5 | Science | Lock card + “Set up my ritual” |
| 6 | Screen Time | Privacy card; honest copy |
| 7 | Mic | Privacy card; **no** “audio never leaves device” claim |
| 8 | Commitment | **Vow card** (defaults 1 gratitude · 6h saved silently) |
| 9 | Paywall | Coral plan cards; **StoreKit prices only** |

**Chrome:** `UNLOCKYOU` header + coral segment progress (current step only).

**New file:** `gratitudedaily/Views/Onboarding/OnboardingChrome.swift`

---

## Dev hooks

```bash
# Open a specific onboarding step (sim or device via Xcode scheme env)
STARTUP_ONBOARDING_STEP=0   # hook … 8 = paywall
```

With `STARTUP_ONBOARDING_STEP` set, app opens onboarding even if `hasCompletedOnboarding` is true (screenshot/QA).

---

## Not done / next person

1. **Device QA** — Run from **Xcode → your iPhone** (CLI install failed: no provisioning on this machine). Walk full funnel: Screen Time picker, mic permission, shield on blocked app, paywall loads products.
2. **Paywall label** — Mock says “Monthly”; App Store product is **weekly** (`gratitudelock.pro.weekly`). UI shows Weekly unless ASC product changes.
3. **App Store screenshots** — Mocks in `Desktop/aug_image/unlockyou/`; marketing shots in `gratitude-marketing/unlockyou-onboarding-shots/` (older sim captures — remake from device if submitting).
4. **ASC / resubmit** — Only when Vaibhav is back and device QA is green.

---

## Build

Last verified: **xcodebuild** iOS Simulator iPhone 16 — **BUILD SUCCEEDED** (25 Aug 2026).

---

## Related (other apps)

- **Shwaas ASC** — resolved 22 Aug; see `SHWAAS-ASC-STUCK-22AUG.md`.
- **NIFTY paper engine** — fix in `marketmantri` `f47a8b6`; separate repo.

---

*Get well, Vaibhav.*
