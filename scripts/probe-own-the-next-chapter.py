# -*- coding: utf-8 -*-
import sys
import urllib.request
import ssl

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

BASE_URL = "https://lornettedaye.com/campaigns/own-the-next-chapter"
ctx = ssl._create_unverified_context()

def probe():
    print(f"Probing 40 'Own The Next Chapter' campaign images on {BASE_URL} ...")
    success_count = 0
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # Lewis Hamilton (5)
    # Serena Williams (5)
    # Tiger Woods (5)
    # Stephen Curry (5)
    # Ayesha Curry (10)
    # Stephen & Ayesha Curry (10)
    targets = []
    for i in range(1, 6):
        targets.append(f"lewis-hamilton-{i:02d}.png")
    for i in range(1, 6):
        targets.append(f"serena-williams-{i:02d}.png")
    for i in range(1, 6):
        targets.append(f"tiger-woods-{i:02d}.png")
    for i in range(1, 6):
        targets.append(f"stephen-curry-{i:02d}.png")
    for i in range(1, 11):
        targets.append(f"ayesha-curry-{i:02d}.png")
    for i in range(1, 11):
        targets.append(f"stephen-ayesha-{i:02d}.png")

    assert len(targets) == 40, f"Expected 40 targets, got {len(targets)}"

    for idx, filename in enumerate(targets, 1):
        url = f"{BASE_URL}/{filename}"
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status == 200:
                    cl = resp.headers.get("Content-Length", "unknown")
                    print(f"  [{idx:02d}/40] HTTP 200 OK: {filename} ({cl} bytes)")
                    success_count += 1
                else:
                    print(f"  [{idx:02d}/40] WARNING: {filename} -> HTTP {resp.status}")
        except Exception as e:
            print(f"  [{idx:02d}/40] ERROR: {filename} -> {e}")

    if success_count == 40:
        print("\nPROBE SUCCESS: All 40 'Own The Next Chapter' images verified HTTP 200 on production domain!")
        sys.exit(0)
    else:
        print(f"\nFAILED: {40 - success_count} of 40 images could not be verified.")
        sys.exit(1)

if __name__ == "__main__":
    probe()
