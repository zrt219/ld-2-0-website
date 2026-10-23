import urllib.request
import json
import ssl

TOKEN = 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0'

req = urllib.request.Request(
    'https://api.buffer.com',
    data=b'{"query": "{ account { id } }"}',
    headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
)
ctx = ssl._create_unverified_context()
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
        print("Success:", r.read().decode())
except urllib.error.HTTPError as e:
    print("HTTPError Status:", e.code)
    for k, v in e.headers.items():
        if "ratelimit" in k.lower() or "retry" in k.lower():
            print(f"  {k}: {v}")
except Exception as e:
    print("Error:", e)
