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
| **HEAD** | `44429b7` — Vary onboarding Canvas motifs (steps 4–9 unique) |
| **Display** | UnlockYou (`CFBundleDisplayName`; session header also UnlockYou) |
| **Bundle** | `com.tranquilwaters.gratitudedaily` |
| **Open** | `gratitudedaily.xcodeproj` → scheme `gratitudedaily` → Run |

**Dev step jump (scheme env):** `STARTUP_ONBOARDING_STEP=0`…`8` (hook…paywall). Forces onboarding even if completed. Fresh install after pull if sim looks stale.

---

## What’s on `main` now (Canvas decor pass)

Per-screen motifs — **neighbors are not the same**. Shared code: `OnboardingChrome.swift` (`OnboardingMotifHeader`, blooms, clipped arcs). No new PNGs required.

| # | Screen | Motif |
|---|---|---|
| 1 Hook | Full **sunrise** + ambient bloom + glow rule under arcs (kept) |
| 2 Promise | **Pulse** rings (no bottom glow line — was slicing title) |
| 3 Time sink | **Orbit** rings (short axis; no line into title) |
| 4 Desire | **Rays** (upward fan) |
| 5 Science | **Sunrise compact** (Hook DNA, no long horizon line) |
| 6 Screen Time | **Orbit** |
| 7 Mic | **Waveform** curves |
| 8 Commitment | **Seal** (vow ring + tick) |
| 9 Paywall | **Hush** (bloom + tiny center only) |

Also earlier on `main`: Meta layout polish (`e115c0e`), full onboarding redesign (`dd5d780`), Coach drop / green cards / etc. (`f03ac3f`), display name UnlockYou (`7008d87` / `55e9039`).

**Optional PNG:** `Assets.xcassets/OnboardingHorizonArc.imageset/` — Hook defaults to Canvas (`useImageAsset: false`).

---

## Deferred (do not do unless asked)

- Merge Screen Time + Mic / trim 9 → fewer screens
- ASC resubmit / App Store screenshots remake
- Physical phone CLI install (needs signing on that Mac)
- Hybrid AI hero assets (Path B/C) — Path A Canvas only for now

---

## Other Mac checklist

1. `cd ~/workspace/gratitudedaily && git pull origin main`
2. Open scheme → Run (or uninstall app on sim, then run)
3. Walk steps 1→9 — motifs should differ; no hairline through titles
4. Optional: `STARTUP_ONBOARDING_STEP=3` for Desire (rays), `=8` for Paywall (hush)
