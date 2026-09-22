# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

campaigns = [
    ("vintage-nfl", 24),
    ("macclung", 11),
    ("jazzy-davidson", 10),
    ("mendoza", 20),
    ("nba", 3),
    ("cricket", 14),
]

ctx = ssl._create_unverified_context()

total = 0
passed = 0
failed = []

print("=" * 70)
print("PROBING PRODUCTION ASSETS FOR ALL 6 NEW CAMPAIGNS (82 ASSETS)")
print("Target: https://lornettedaye.com/campaigns/...")
print("=" * 70)

for slug, count in campaigns:
    print(f"\n--- Checking {slug} ({count} assets) ---")
    for i in range(1, count + 1):
        total += 1
        url = f"https://lornettedaye.com/campaigns/{slug}/{slug}-{i:02d}.png"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status == 200:
                    passed += 1
                    print(f"  [{passed}/{total}] HTTP 200: {url}")
                else:
                    failed.append((url, resp.status))
                    print(f"  [FAIL] HTTP {resp.status}: {url}")
        except Exception as e:
            failed.append((url, str(e)))
            print(f"  [ERROR] {url} -> {e}")

print("\n" + "=" * 70)
print(f"PROBE SUMMARY: {passed}/{total} assets verified HTTP 200 OK.")
if failed:
    print(f"FAILED ASSETS ({len(failed)}):")
    for u, err in failed:
        print(f"  {u} -> {err}")
    sys.exit(1)
else:
    print("ALL 82 ASSETS 100% LIVE ON PRODUCTION CUSTOM DOMAIN!")
print("=" * 70)
