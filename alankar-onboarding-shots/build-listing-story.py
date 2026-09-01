#!/usr/bin/env python3
"""Alankar Play listing — full-bleed app screens. No captions, no extra frame.

Crops 1080x2400 captures to Play 9:16 (1080x1920).

Usage:
  python3 alankar-onboarding-shots/build-listing-story.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

SHOTS = Path("/Users/vaibhav/workspace/alankar-companion/store/instagram-1.6.0-carousel")
HERE = Path(__file__).resolve().parent
OUT_DIR = HERE / "play"
STRIP = HERE / "LISTING-STORY-STRIP.png"
OUT_W, OUT_H = 1080, 1920

# (src, out, top_y) — crop a 1080x1920 window from the 2400-tall capture
# Skip Android status bar (Work-profile briefcase + clock) on home/settings.
FRAMES = [
    ("01_home.png", "01-pick-a-sit.png", 108),
    ("02_kafi_komal_ga_ni.png", "02-sa-on-the-page.png", 160),
    ("03_audio_sheet_sa_picker_drone.png", "03-tune-the-drone.png", 480),
    ("04_settings_tanpura_guide.png", "04-tanpura-mood.png", 108),
]


def crop_play(src: Path, top: int) -> Image.Image:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w != 1080 or h != 2400:
        im = im.resize((1080, int(h * 1080 / w)), Image.Resampling.LANCZOS)
        h = im.size[1]
    top = max(0, min(top, h - OUT_H))
    return im.crop((0, top, OUT_W, top + OUT_H))


def stitch_strip(frames: list[Path], dest: Path) -> None:
    thumbs = [Image.open(p).convert("RGB") for p in frames]
    target_h = 900
    scaled = []
    for im in thumbs:
        w = int(im.width * (target_h / im.height))
        scaled.append(im.resize((w, target_h), Image.Resampling.LANCZOS))
    gap = 16
    strip_w = gap * (len(scaled) + 1) + sum(t.width for t in scaled)
    strip_h = target_h + gap * 2
    canvas = Image.new("RGB", (strip_w, strip_h), (28, 22, 18))
    x = gap
    for t in scaled:
        canvas.paste(t, (x, gap))
        x += t.width + gap
    canvas.save(dest, "PNG", optimize=True)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale in OUT_DIR.glob("01-hero.png"):
        stale.unlink()
    paths: list[Path] = []
    for src_name, out_name, top in FRAMES:
        out = OUT_DIR / out_name
        crop_play(SHOTS / src_name, top).save(out, "PNG", optimize=True)
        paths.append(out)
        print(out)
    stitch_strip(paths, STRIP)
    print(STRIP)


if __name__ == "__main__":
    main()
