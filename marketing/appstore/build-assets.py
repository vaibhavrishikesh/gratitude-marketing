#!/usr/bin/env python3
"""Generate styled App Store screenshots from raw device shots.

Usage:
  python3 marketing/appstore/build-assets.py
"""
from pathlib import Path
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[2]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# iPhone 6.9" portrait screenshot requirement
OUT_W = 1290
OUT_H = 2796


def render_html_to_png(html: str, out_path: Path) -> None:
    tmp_dir = Path(tempfile.mkdtemp())
    html_path = tmp_dir / "screen.html"
    html_path.write_text(html, encoding="utf-8")

    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            f"--screenshot={out_path}",
            f"--window-size={OUT_W},{OUT_H}",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )


def build_screenshot(
    shot_file: str,
    kicker: str,
    headline: str,
    sub: str,
    out_name: str,
    phone_width: int = 72,
    phone_bottom: int = 80,
) -> Path:
    shot_path = Path(shot_file)
    shot = shot_path if shot_path.is_absolute() else (ROOT / "img" / shot_file).resolve()
    out_dir = ROOT / "marketing" / "appstore" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / out_name

    html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    * {{ box-sizing: border-box; margin: 0; }}
    html, body {{
      width: {OUT_W}px;
      height: {OUT_H}px;
      overflow: hidden;
      font-family: Georgia, "Times New Roman", serif;
      color: #e9f2ef;
    }}
    body {{
      background:
        radial-gradient(80% 45% at 20% 10%, rgba(85, 188, 168, 0.28), transparent 70%),
        radial-gradient(60% 40% at 80% 80%, rgba(95, 172, 155, 0.20), transparent 72%),
        linear-gradient(180deg, #071b19 0%, #051412 100%);
      position: relative;
    }}
    .title-wrap {{
      position: absolute;
      top: 150px;
      left: 100px;
      right: 100px;
    }}
    .kicker {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 28px;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: #66d6be;
      margin-bottom: 28px;
    }}
    h1 {{
      font-size: 96px;
      line-height: 1.02;
      font-weight: 500;
      max-width: 10.5ch;
      text-wrap: balance;
    }}
    h1 em {{ color: #66d6be; font-style: italic; }}
    .sub {{
      margin-top: 36px;
      max-width: 25ch;
      font-size: 44px;
      line-height: 1.2;
      color: #bfd5cf;
    }}
    .phone {{
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: {phone_bottom}px;
      width: {phone_width}%;
      border-radius: 70px;
      border: 2px solid rgba(190, 245, 234, 0.30);
      box-shadow: 0 38px 80px rgba(0, 0, 0, 0.40);
    }}
  </style>
</head>
<body>
  <div class="title-wrap">
    <div class="kicker">{kicker}</div>
    <h1>{headline}</h1>
    <div class="sub">{sub}</div>
  </div>
  <img class="phone" src="file://{shot}" />
</body>
</html>"""

    render_html_to_png(html, out_file)
    return out_file


SHOTS = [
    {
        "file": "landing-02.jpg",
        "kicker": "Step 1 · Say It",
        "headline": "Speak one affirmation. Then the <em>app</em>.",
        "sub": "Speak or type — ten seconds before the scroll.",
        "out": "01-sentence.png",
    },
    {
        "file": "landing-01.jpg",
        "kicker": "Step 2 · Enforced via Screen Time",
        "headline": "Pick the apps the thumb <em>knows</em>.",
        "sub": "Instagram. YouTube. Games. One line before each opens.",
        "out": "02-pick-apps.png",
    },
    {
        "file": "landing-03.jpg",
        "kicker": "Step 3 · Library",
        "headline": "Everything you <em>said</em>. Kept.",
        "sub": "Gratitude, affirmations, motivation — without journaling.",
        "out": "03-library.png",
    },
    {
        "file": "/Users/vaibhav/workspace/brain/captures/gratitude-2026-08-18/asc/asc-4.png",
        "kicker": "Step 4 · Controls",
        "headline": "Your schedule. <em>Your rules.</em>",
        "sub": "Set one pause per session, with a 6h unlock window.",
        "out": "04-mindless-scroll.png",
        "phone_width": 62,
        "phone_bottom": 34,
    },
    {
        "file": "landing-01.jpg",
        "kicker": "Step 5 · Consistency",
        "headline": "Motivation starts it. <em>Consistency</em> builds it.",
        "sub": "Two or three times a day — without remembering.",
        "out": "05-consistency.png",
        "phone_width": 62,
        "phone_bottom": 36,
    },
]


if __name__ == "__main__":
    for s in SHOTS:
        out = build_screenshot(
            s["file"],
            s["kicker"],
            s["headline"],
            s["sub"],
            s["out"],
            s.get("phone_width", 72),
            s.get("phone_bottom", 80),
        )
        print(out)
