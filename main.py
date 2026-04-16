#!/usr/bin/env python3
"""
Countdown Timer
Author: brainiacweb-tech
"""
import time
import os


def parse_time(s):
    """Parse time string like 5m, 1h30m, 90s, 1h2m30s, or plain seconds."""
    s = s.strip().lower().replace(" ", "")
    total = 0
    try:
        if "h" in s:
            h, s = s.split("h", 1)
            total += int(h) * 3600
        if "m" in s:
            m, s = s.split("m", 1)
            total += int(m) * 60
        if "s" in s:
            sec = s.replace("s", "")
            total += int(sec) if sec else 0
        elif s.isdigit():
            total += int(s)
    except ValueError:
        return 0
    return total


def desktop_notify(title, message):
    try:
        from plyer import notification
        notification.notify(title=title, message=message, app_name="Countdown Timer", timeout=8)
    except Exception:
        pass


def countdown(seconds, label=""):
    tag = f" — {label}" if label else ""
    print(f"\n  Timer{tag} started!\n")
    start = time.time()
    try:
        remaining = seconds
        while remaining > 0:
            hrs, rem = divmod(remaining, 3600)
            mins, secs = divmod(rem, 60)
            display = f"  {hrs:02d}:{mins:02d}:{secs:02d}" if hrs else f"  {mins:02d}:{secs:02d}"
            print(display, end="\r", flush=True)
            time.sleep(1)
            remaining -= 1
        print("\n")
        print("  Time is up! " + ("(" + label + ")" if label else ""))
        desktop_notify("Timer Done!", label if label else "Your countdown has ended.")
    except KeyboardInterrupt:
        elapsed = int(time.time() - start)
        m, s = divmod(elapsed, 60)
        print(f"\n\n  Timer stopped after {m:02d}:{s:02d}.")


if __name__ == "__main__":
    print("=" * 44)
    print("           Countdown Timer")
    print("=" * 44)
    print("\n  Time format examples: 5m  |  1h30m  |  90s  |  1h2m30s  |  60")
    t = input("\n  Set timer: ").strip()
    label = input("  Label (optional, press Enter to skip): ").strip()
    seconds = parse_time(t)
    if seconds <= 0:
        print("  Invalid time. Try: 5m or 90s")
    else:
        hrs, rem = divmod(seconds, 3600)
        mins, secs = divmod(rem, 60)
        print(f"\n  Counting down {hrs:02d}h {mins:02d}m {secs:02d}s...")
        countdown(seconds, label)
