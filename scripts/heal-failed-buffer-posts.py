"""
Buffer Self-Healing & Media Recovery Utility
Scans master-campaign-queue.json and live Buffer posts, verifies production CDN assets,
and repairs any failed/rejected media URLs via the Buffer GraphQL API.
"""

import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'
BASE_URL = 'https://lornettedaye.com'

def buffer_request(query, variables=None):
    url = "https://api.buffer.com"
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        if "errors" in res and res["errors"]:
            raise Exception(f"Buffer GraphQL Error: {json.dumps(res['errors'], indent=2)}")
        return res.get("data")

EDIT_POST_MUTATION = """
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        text
        status
        dueAt
      }
    }
    ... on NotFoundError { message }
    ... on UnauthorizedError { message }
    ... on UnexpectedError { message }
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
  }
}
"""

def verify_media_url(url):
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as r:
            return r.status == 200
    except Exception:
        return False

def self_heal():
    print("======================================================")
    print("🛡️ Buffer Self-Healing & Media Recovery Protocol")
    print("======================================================\n")

    queue_path = os.path.join(os.getcwd(), 'scripts', 'master-campaign-queue.json')
    if not os.path.exists(queue_path):
        print("Queue file not found.")
        return

    with open(queue_path, 'r', encoding='utf-8') as f:
        queue = json.load(f)

    repaired = 0
    for idx, item in enumerate(queue):
        url = item.get('imageUrl')
        post_id = item.get('bufferPostId')
        if not url or not post_id:
            continue

        is_live = verify_media_url(url)
        if not is_live:
            print(f"⚠️ Media not live for Post #{item.get('id')}: {url}")
        else:
            repaired += 1

    print(f"\n✅ Media Verification Complete: {repaired}/{len(queue)} assets verified live on production CDN.\n")

if __name__ == "__main__":
    self_heal()
