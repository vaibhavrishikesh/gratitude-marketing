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


def build_first_screenshot() -> Path:
    shot = (ROOT / "img" / "landing-02.jpg").resolve()
    out_dir = ROOT / "marketing" / "appstore" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "01-affirmation-sentence.png"

    html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
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
      bottom: 80px;
      width: 72%;
      border-radius: 70px;
      border: 2px solid rgba(190, 245, 234, 0.30);
      box-shadow: 0 38px 80px rgba(0, 0, 0, 0.40);
    }}
  </style>
</head>
<body>
  <div class="title-wrap">
    <div class="kicker">Screen Time Controlled</div>
    <h1>One sentence. Then the <em>app</em>.</h1>
    <div class="sub">Motivation starts it. Consistency keeps it going.</div>
  </div>
  <img class="phone" src="file://{shot}" />
</body>
</html>"""

    render_html_to_png(html, out_file)
    return out_file


def build_screenshot(shot_file: str, kicker: str, headline: str, sub: str, out_name: str) -> Path:
    shot = (ROOT / "img" / shot_file).resolve()
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
      bottom: 80px;
      width: 72%;
      border-radius: 70px;
      border: 2px solid rgba(190, 245, 234, 0.30);
      box-shadow: 0 38px 80px rgba(0, 0, 0, 0.40);
    }}
    .brand {{
      position: absolute;
      left: 100px;
      bottom: 48px;
      font-size: 36px;
      color: #9ec9bf;
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
  <div class="brand">Gratitude Habit Builder</div>
</body>
</html>"""

    render_html_to_png(html, out_file)
    return out_file


SHOTS = [
    {
        "file": "landing-02.jpg",
        "kicker": "Step 1 · Say It",
        "headline": "One sentence. Then the <em>app</em>.",
        "sub": "Speak or type — ten seconds before the scroll.",
        "out": "01-sentence.png",
    },
    {
        "file": "landing-02.jpg",
        "kicker": "Step 2 · Enforced",
        "headline": "Screen Time <em>keeps</em> you honest.",
        "sub": "No sentence, no feed. Built on Apple's own control.",
        "out": "02-screen-time.png",
    },
    {
        "file": "landing-03.jpg",
        "kicker": "Step 3 · Library",
        "headline": "Everything you <em>said</em>. Kept.",
        "sub": "Gratitude, affirmations, motivation — without journaling.",
        "out": "03-library.png",
    },
    {
        "file": "landing-01.jpg",
        "kicker": "Step 4 · Your Apps",
        "headline": "Pick the apps the thumb <em>knows</em>.",
        "sub": "Instagram. YouTube. Games. The hours you already spend.",
        "out": "04-pick-apps.png",
    },
    {
        "file": "landing-01.jpg",
        "kicker": "Step 5 · Control",
        "headline": "Your schedule. <em>Your rules.</em>",
        "sub": "Per session, per day — you decide how often.",
        "out": "05-controls.png",
    },
]


if __name__ == "__main__":
    for s in SHOTS:
        out = build_screenshot(s["file"], s["kicker"], s["headline"], s["sub"], s["out"])
        print(out)
