# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

base_url = "https://lornettedaye.com/campaigns/oilers/"
ctx = ssl._create_unverified_context()

images = [f"oilers-{i:02d}.png" for i in range(1, 11)]

failed = []
print("Probing 10 Edmonton Oilers campaign images on https://lornettedaye.com ...")

for i, img in enumerate(images, 1):
    url = f"{base_url}{img}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            if resp.status == 200:
                print(f"  [{i:02d}/10] HTTP 200 OK: {img} ({resp.headers.get('Content-Length')} bytes)")
            else:
                print(f"  [{i:02d}/10] UNEXPECTED STATUS {resp.status}: {img}")
                failed.append((img, resp.status))
    except Exception as e:
        print(f"  [{i:02d}/10] ERROR: {img} -> {e}")
        failed.append((img, str(e)))

if failed:
    print(f"\nFAILED: {len(failed)} of 10 images could not be verified.")
    sys.exit(1)
else:
    print("\nPROBE SUCCESS: All 10 Edmonton Oilers campaign images verified HTTP 200 on production domain!")
    sys.exit(0)
