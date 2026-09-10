import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301' # Lornette Daye LinkedIn
manifest_path = os.path.join(os.path.dirname(__file__), 'turkish-empowerment-manifest.json')
report_path = os.path.join(os.path.dirname(__file__), 'turkish-empowerment-scheduled-report.json')

with open(manifest_path, 'r', encoding='utf-8') as f:
    turkish_posts = json.load(f)

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        text
        status
        dueAt
      }
    }
    ... on LimitReachedError {
      message
    }
    ... on InvalidInputError {
      message
    }
    ... on UnexpectedError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
"""

def buffer_request(query, variables):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode("utf-8")).get("data", {})

def schedule_turkish_campaign():
    print("======================================================")
    print("🇹🇷 Scheduling Turkish Female Empowerment 4-Week Sprint (56 Posts)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Sep 10 - Oct 7, 2026 | 2x Daily (9:00 AM & 6:00 PM MDT)")
    print("======================================================\n")

    results = []

    for idx, p in enumerate(turkish_posts):
        if p.get("status") == "scheduled" and p.get("bufferPostId"):
            print(f"[{idx + 1}/{len(turkish_posts)}] Post #{p['id']} already scheduled (ID: {p['bufferPostId']})")
            results.append(p)
            continue

        print(f"[{idx + 1}/{len(turkish_posts)}] Scheduling Post #{p['id']} ({p['slot']}): \"{p['title']}\"")
        print(f"   Slot: {p['displayTime']} ({p['dueAt']})")
        print(f"   Asset: {p['assetUrl']}")

        input_data = {
            "channelId": CHANNEL_ID,
            "text": p["text"],
            "mode": "customScheduled",
            "dueAt": p["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": [
                {
                    "image": {
                        "url": p["assetUrl"]
                    }
                }
            ]
        }

        try:
            data = buffer_request(mutation, {"input": input_data})
            create_post = data.get("createPost", {})
            typename = create_post.get("__typename")

            if typename == "PostActionSuccess" and "post" in create_post:
                post_obj = create_post["post"]
                print(f"   ✅ Success! Buffer Post ID: {post_obj['id']} | Due: {post_obj['dueAt']}\n")
                p["bufferPostId"] = post_obj["id"]
                p["status"] = "scheduled"
                p["scheduledAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                results.append(p)
            elif typename == "LimitReachedError":
                print(f"   ⚠️ Limit Reached: {create_post.get('message')}\n")
                p["status"] = "limit_reached"
                p["error"] = create_post.get("message")
                results.append(p)
            else:
                print(f"   ⚠️ Failed response: {json.dumps(create_post, indent=2)}\n")
                p["status"] = "failed"
                p["error"] = create_post
                results.append(p)
        except Exception as e:
            print(f"   ❌ Error: {str(e)}\n")
            p["status"] = "error"
            p["error"] = str(e)
            results.append(p)

        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(turkish_posts, f, indent=2, ensure_ascii=False)
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        time.sleep(0.5)

    scheduled_count = len([r for r in results if r.get("status") == "scheduled"])
    print(f"🎉 Scheduled Report saved to {report_path}")
    print(f"Summary: {scheduled_count}/{len(turkish_posts)} posts successfully scheduled directly in Buffer.\n")

if __name__ == "__main__":
    schedule_turkish_campaign()
