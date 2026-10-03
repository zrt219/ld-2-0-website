# -*- coding: utf-8 -*-
import sys
import urllib.request
import ssl

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

BASE_URL = "https://lornettedaye.com/campaigns/business-athletes"
ctx = ssl._create_unverified_context()

def probe():
    print(f"Probing 20 Business Athletes campaign images on {BASE_URL} ...")
    success_count = 0
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for i in range(1, 21):
        filename = f"business-athletes-{i:02d}.png"
        url = f"{BASE_URL}/{filename}"
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status == 200:
                    cl = resp.headers.get("Content-Length", "unknown")
                    print(f"  [{i:02d}/20] HTTP 200 OK: {filename} ({cl} bytes)")
                    success_count += 1
                else:
                    print(f"  [{i:02d}/20] WARNING: {filename} -> HTTP {resp.status}")
        except Exception as e:
            print(f"  [{i:02d}/20] ERROR: {filename} -> {e}")

    if success_count == 20:
        print("\nPROBE SUCCESS: All 20 Business Athletes images verified HTTP 200 on production domain!")
        sys.exit(0)
    else:
        print(f"\nFAILED: {20 - success_count} of 20 images could not be verified.")
        sys.exit(1)

if __name__ == "__main__":
    probe()
