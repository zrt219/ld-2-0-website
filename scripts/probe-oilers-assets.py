import urllib.request
import ssl
import sys

url = "https://lornettedaye.com/campaigns/oilers/rnh-shootout-winner.mp4"
ctx = ssl._create_unverified_context()

print(f"Probing production asset URL: {url}...")
req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        content_type = resp.headers.get("Content-Type", "")
        content_len = resp.headers.get("Content-Length", "0")
        size_mb = int(content_len) / (1024 * 1024) if content_len.isdigit() else 0
        print(f"[OK 200] {url} ({content_type}, {size_mb:.2f} MB)")
        print("\nSUCCESS: Production asset verified HTTP 200 OK!")
except Exception as e:
    print(f"[FAIL] {url} -> {e}")
    sys.exit(1)
