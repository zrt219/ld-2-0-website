# -*- coding: utf-8 -*-
import urllib.request
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
ctx = ssl.create_default_context()

urls = [f"https://lornettedaye.com/campaigns/henry/henry-{i:02d}.png" for i in range(1, 11)]

print(f"Probing {len(urls)} Derrick Henry campaign asset URLs...")
success = 0
for u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 LornetteDayeProbe/2.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            status = resp.status
            size = resp.headers.get("Content-Length", "unknown")
            if status == 200:
                success += 1
                print(f"  [HTTP 200] {u} ({size} bytes)")
            else:
                print(f"  [FAIL {status}] {u}")
    except Exception as e:
        print(f"  [ERROR] {u} -> {e}")

print(f"\nResult: {success}/{len(urls)} URLs returned HTTP 200.")
if success == len(urls):
    sys.exit(0)
else:
    sys.exit(1)
