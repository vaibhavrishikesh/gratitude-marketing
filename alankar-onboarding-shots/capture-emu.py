#!/usr/bin/env python3
"""Capture Alankar screens from a connected emulator via adb + uiautomator."""
from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path

PKG = "com.riyaaz.alankar"
OUT = Path("/Users/vaibhav/workspace/gratitude-marketing/alankar-onboarding-shots/emu-1.6.5")
DUMP = Path("/tmp/alankar-ui.xml")


def adb(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["adb", *args], check=check, capture_output=True, text=True)


def screencap(name: str) -> Path:
    dest = OUT / f"{name}.png"
    data = subprocess.check_output(["adb", "exec-out", "screencap", "-p"])
    dest.write_bytes(data)
    print("shot", dest.name, dest.stat().st_size)
    return dest


def dump_ui() -> str:
    adb("shell", "uiautomator", "dump", "/sdcard/ui.xml")
    adb("pull", "/sdcard/ui.xml", str(DUMP))
    return DUMP.read_text(encoding="utf-8", errors="replace")


def bounds(xml: str, *, text: str | None = None, desc: str | None = None) -> tuple[int, int, int, int] | None:
    for m in re.finditer(r"<node [^>]+>", xml):
        n = m.group(0)
        if text is not None and f'text="{text}"' not in n and f'text="{text}.' not in n:
            # allow startswith for long compose text
            if f'text="{text}' not in n:
                continue
        if desc is not None and f'content-desc="{desc}"' not in n:
            continue
        b = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        if b:
            return tuple(int(x) for x in b.groups())  # type: ignore
    return None


def tap_bounds(b: tuple[int, int, int, int]) -> None:
    x = (b[0] + b[2]) // 2
    y = (b[1] + b[3]) // 2
    adb("shell", "input", "tap", str(x), str(y))


def tap(text: str | None = None, desc: str | None = None, wait: float = 1.2) -> bool:
    xml = dump_ui()
    b = bounds(xml, text=text, desc=desc)
    if not b:
        print("MISS", text or desc)
        return False
    tap_bounds(b)
    time.sleep(wait)
    return True


def wait_text(needle: str, tries: int = 12, delay: float = 1.0) -> bool:
    for i in range(tries):
        xml = dump_ui()
        if needle in xml:
            return True
        print(f"wait {needle!r} {i+1}/{tries}")
        time.sleep(delay)
    return False


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    adb("shell", "am", "force-stop", PKG)
    adb("shell", "pm", "clear", PKG)
    adb(
        "shell",
        "am",
        "start",
        "-n",
        f"{PKG}/.MainActivity",
    )
    time.sleep(8)
    if not wait_text("RIYAAZ", tries=20, delay=1.5):
        screencap("00-launch-fail")
        raise SystemExit("app did not show RIYAAZ")

    # 1 onboarding
    screencap("01-onboarding")
    if not tap(text="begin", wait=3):
        # lowercase begin
        tap(text="begin")
        time.sleep(3)

    wait_text("Pick a sit", tries=15, delay=1.5)
    time.sleep(1)
    screencap("02-home")

    tap(desc="Settings", wait=1.5)
    wait_text("Settings", tries=8)
    screencap("03-settings")
    adb("shell", "input", "keyevent", "4")
    time.sleep(1)

    tap(desc="History", wait=1.5)
    screencap("04-history")
    adb("shell", "input", "keyevent", "4")
    time.sleep(1)

    tap(text="Build new session", wait=1.5)
    wait_text("Build", tries=8)
    screencap("05-build")
    adb("shell", "input", "keyevent", "4")
    time.sleep(1.2)

    # practice — tap 7-day day 1 card
    if not tap(text="7-Day Beginner", wait=3):
        tap(text="Sa & Breath", wait=3)
    wait_text("BPM", tries=12, delay=1.5)
    time.sleep(1)
    screencap("06-practice")

    tap(desc="Change Sa, BPM and volumes", wait=1.5)
    time.sleep(1)
    screencap("07-tune-drone")
    # dismiss sheet
    adb("shell", "input", "keyevent", "4")
    time.sleep(1)

    tap(desc="Play", wait=2)
    time.sleep(2)
    screencap("08-practice-playing")
    tap(desc="Pause", wait=1.5)
    time.sleep(1)
    screencap("09-paused")

    if tap(text="End session", wait=2.5):
        time.sleep(2)
        screencap("10-end-session")
    else:
        print("no End session")

    print("DONE", OUT)


if __name__ == "__main__":
    main()
