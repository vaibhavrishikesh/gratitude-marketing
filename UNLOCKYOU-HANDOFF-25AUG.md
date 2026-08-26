# UnlockYou onboarding — handoff · 26 Aug 2026

**Switch Mac / build elsewhere.** Code is on `main` (pushed). Screen merge still deferred.

---

## Repo (build here)

| | |
|---|---|
| **Path** | `~/workspace/gratitudedaily` |
| **Remote** | `github.com:vaibhavgt/gratitudedaily.git` |
| **Branch** | `main` |
| **Pull** | `git pull origin main` |
| **Display** | UnlockYou |
| **Bundle** | `com.tranquilwaters.gratitudedaily` |
| **Open** | `gratitudedaily.xcodeproj` → scheme `gratitudedaily` → Run |

**Dev step jump (scheme env):** `STARTUP_ONBOARDING_STEP=0`…`8` (hook…paywall). Forces onboarding even if completed.

---

## What’s new since `dd5d780` (this push)

Meta polish pass — layout + decor, not funnel trim.

| # | Screen | Shipped behavior |
|---|---|---|
| 1 Hook | Canvas sunrise arcs + coral gradient `38` + glow rule; content vertically balanced |
| 2 Promise | **Glow line only** (no Hook arcs); timeline spacing; demo chips **all start inactive**, tap to select; voice wave + sun card |
| 3 Time sink | **Glow line only**; chips **start empty** (Continue disabled until pick); content shifted down |
| 4 Desire | Shared **HeroArcHeader** (big arc) + title/list shifted down |
| 5 Science | HeroArcHeader + shorter body + coral glow on lock |
| 6 Screen Time | HeroArcHeader + privacy card |
| 7 Mic | HeroArcHeader + honest “does not save recordings” |
| 8 Commitment | HeroArcHeader + vow card |
| 9 Paywall | HeroArcHeader + StoreKit prices; Weekly (not Monthly) |

**Shared chrome:** `OnboardingChrome.swift` — `OnboardingHorizonArc`, `OnboardingHeroArcHeader`, `OnboardingGlowRule`, `OnboardingPromiseDecor`, `OnboardingTimeSinkDecor`, disabled-CTA contrast, voice wave.

**Asset (optional PNG):** `Assets.xcassets/OnboardingHorizonArc.imageset/` — Hook defaults to **Canvas** (`useImageAsset: false`); PNG kept for A/B.

---

## Deferred (do not do unless asked)

- Merge Screen Time + Mic / trim 9 → fewer screens
- ASC resubmit / App Store screenshots remake
- Physical phone CLI install (needs signing on that Mac)

---

## Other apps (unrelated)

- Shwaas ASC — see `SHWAAS-ASC-STUCK-22AUG.md` (resolved 22 Aug)
- NIFTY paper engine — `marketmantri` (separate)

---

*Build on the other Mac from `main` after pull. Latest: **`e115c0e`**.*
