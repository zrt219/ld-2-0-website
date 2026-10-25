import urllib.request
import ssl
import json
import sys

with open("scripts/master-ucf-byu-queue.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

ctx = ssl._create_unverified_context()

all_ok = True
unique_urls = sorted(list(set(p["assetUrl"] for p in posts)))
print(f"Probing {len(unique_urls)} unique production asset URLs...")

for url in unique_urls:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            content_type = resp.headers.get("Content-Type", "")
            content_len = resp.headers.get("Content-Length", "0")
            size_mb = int(content_len) / (1024 * 1024) if content_len.isdigit() else 0
            print(f"[OK 200] {url} ({content_type}, {size_mb:.2f} MB)")
    except Exception as e:
        print(f"[FAIL] {url} -> {e}")
        all_ok = False

if not all_ok:
    print("\nERROR: One or more production assets failed HTTP 200 verification!")
    sys.exit(1)
else:
    print("\nSUCCESS: All production assets verified HTTP 200 OK!")
