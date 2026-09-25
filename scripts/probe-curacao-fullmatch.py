# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

url = "https://lornettedaye.com/campaigns/curacao/curacao-fullmatch.mp4"
print(f"Probing {url} ...")

ctx = ssl._create_unverified_context()
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, method="HEAD")

try:
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        status = resp.status
        clen = resp.headers.get("Content-Length")
        ctype = resp.headers.get("Content-Type")
        print(f"Status: {status}")
        print(f"Content-Length: {clen}")
        print(f"Content-Type: {ctype}")
        if status in [200, 206] and clen == "83754822":
            print("PROBE RESULT: SUCCESS (HTTP 200/206 verified on production domain with exact 83.8MB match)")
            sys.exit(0)
        elif status in [200, 206]:
            print("PROBE RESULT: SUCCESS (HTTP 200/206 verified on production domain)")
            sys.exit(0)
        else:
            print(f"PROBE RESULT: FAILED (Unexpected status {status})")
            sys.exit(1)
except Exception as e:
    print(f"PROBE ERROR: {e}")
    sys.exit(1)
