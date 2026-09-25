# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

base_url = "https://lornettedaye.com/campaigns/curacao/curacao-ad-"
ctx = ssl._create_unverified_context()

failed = []
print("Probing 20 Curaçao ad images on https://lornettedaye.com ...")

for i in range(1, 21):
    url = f"{base_url}{i:02d}.png"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            if resp.status == 200:
                print(f"  [{i:02d}/20] HTTP 200 OK: curacao-ad-{i:02d}.png ({resp.headers.get('Content-Length')} bytes)")
            else:
                print(f"  [{i:02d}/20] UNEXPECTED STATUS {resp.status}: curacao-ad-{i:02d}.png")
                failed.append((i, resp.status))
    except Exception as e:
        print(f"  [{i:02d}/20] ERROR: curacao-ad-{i:02d}.png -> {e}")
        failed.append((i, str(e)))

if failed:
    print(f"\nFAILED: {len(failed)} of 20 images could not be verified.")
    sys.exit(1)
else:
    print("\nPROBE SUCCESS: All 20 Curaçao ad images verified HTTP 200 on production domain!")
    sys.exit(0)
