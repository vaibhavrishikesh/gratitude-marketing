# UnlockYou onboarding — handoff · 29 Aug 2026

**Switch Mac / build + deploy elsewhere.** Code is on branch `feat/onboarding-speak-climax` (pushed). Do **not** assume `main` has this yet until merged.

---

## Repo (build here)

| | |
|---|---|
| **Path** | `~/workspace/gratitudedaily` |
| **Remote** | `github.com:vaibhavgt/gratitudedaily.git` |
| **Branch** | `feat/onboarding-speak-climax` |
| **Pull** | `git fetch && git checkout feat/onboarding-speak-climax && git pull` |
| **Display** | UnlockYou (`CFBundleDisplayName`; session header UnlockYou) |
| **Icon** | **sun-heart-ripple** (AppIcon light/dark/tinted) |
| **Bundle** | `com.tranquilwaters.gratitudedaily` |
| **Open** | `gratitudedaily.xcodeproj` → scheme `gratitudedaily` → Run |

**Dev step jump (scheme env):** `STARTUP_ONBOARDING_STEP=0`…`7`  
`0` Hook · `1` Promise · `2` Time · `3` Desire · `4` Science · `5` Screen Time · `6` **Speak** · `7` Paywall.  
Forces onboarding even if completed. Fresh install after pull if sim looks stale.

---

## Funnel now (8 steps)

| # | Screen | Visual |
|---|---|---|
| 1 Hook | Compact sun-heart logo + horizontal coral leaf band + big **38** (rounded) |
| 2 Promise | `OnboardingLogoHero` (sun-heart) |
| 3 Time sink | Logo hero |
| 4 Desire | Logo hero |
| 5 Science | Logo hero |
| 6 Screen Time | Logo hero |
| 7 **Speak** | Live `GratitudeSessionView` onboarding mode — vow line, then paywall |
| 8 Paywall | Logo hero |

**Removed from funnel:** Mic + Commitment (files may still exist unused).

**Speak line:** `I'll take one private minute before I scroll.`

Shots strip: `gratitude-marketing/unlockyou-onboarding-shots/CURRENT-base-flow-sim.png` · clean speak `sim-speak-clean.png` · hook `sim-00-hook.png`.

---

## Other Mac checklist

1. `cd ~/workspace/gratitudedaily && git fetch && git checkout feat/onboarding-speak-climax && git pull`
2. Open scheme → Run (or uninstall app on sim, then run)
3. Walk 1→8 — speak should request Speech once, then listening UI; Continue → paywall
4. Optional: `STARTUP_ONBOARDING_STEP=6` for Speak, `=0` for Hook
5. **Deploy / ASC** from that machine when ready (merge to main first if that’s your ship rule)

---

## Deferred

- Merge branch → `main` (when ready to ship)
- ASC resubmit / App Store screenshot remake with new funnel
- Physical phone CLI install (needs signing on that Mac)
