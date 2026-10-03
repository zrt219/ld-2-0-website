# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

base_url = "https://lornettedaye.com/campaigns/penix/"
ctx = ssl._create_unverified_context()

images = [
    "penix-golden-starter-poster.png",
    "penix-01.png",
    "penix-02.png",
    "penix-03.png",
    "penix-04.png",
    "penix-05.png",
    "penix-06.png",
    "penix-07.png",
    "penix-08.png",
    "penix-09.png",
    "penix-10.png"
]

failed = []
print("Probing 11 Michael Penix Jr. campaign images on https://lornettedaye.com ...")

for i, img in enumerate(images, 1):
    url = f"{base_url}{img}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            if resp.status == 200:
                print(f"  [{i:02d}/11] HTTP 200 OK: {img} ({resp.headers.get('Content-Length')} bytes)")
            else:
                print(f"  [{i:02d}/11] UNEXPECTED STATUS {resp.status}: {img}")
                failed.append((img, resp.status))
    except Exception as e:
        print(f"  [{i:02d}/11] ERROR: {img} -> {e}")
        failed.append((img, str(e)))

if failed:
    print(f"\nFAILED: {len(failed)} of 11 images could not be verified.")
    sys.exit(1)
else:
    print("\nPROBE SUCCESS: All 11 Michael Penix Jr. campaign images verified HTTP 200 on production domain!")
    sys.exit(0)
