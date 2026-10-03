# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

base_url = "https://lornettedaye.com/campaigns/finish-strong-keynote/"
ctx = ssl._create_unverified_context()

images = [
    "lead-through-the-storm.jpg",
    "mentorship-message-momentum.jpg",
    "finish-strong-purpose.jpg",
    "track-lanes-to-boardrooms.jpg",
    "setback-not-finish-line.jpg"
]

failed = []
print("Probing 5 Finish Strong Keynote campaign images on https://lornettedaye.com ...")

for i, img in enumerate(images, 1):
    url = f"{base_url}{img}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            if resp.status == 200:
                print(f"  [{i}/5] HTTP 200 OK: {img} ({resp.headers.get('Content-Length')} bytes)")
            else:
                print(f"  [{i}/5] UNEXPECTED STATUS {resp.status}: {img}")
                failed.append((img, resp.status))
    except Exception as e:
        print(f"  [{i}/5] ERROR: {img} -> {e}")
        failed.append((img, str(e)))

if failed:
    print(f"\nFAILED: {len(failed)} of 5 images could not be verified.")
    sys.exit(1)
else:
    print("\nPROBE SUCCESS: All 5 Finish Strong Keynote images verified HTTP 200 on production domain!")
    sys.exit(0)
