# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time
import importlib.util

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

base_dir = os.path.dirname(__file__)

# Load original posts_data from schedule-juju-business-campaign.py
orig_script_path = os.path.join(base_dir, "schedule-juju-business-campaign.py")
spec = importlib.util.spec_from_file_location("juju_biz", orig_script_path)
juju_biz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(juju_biz)

orig_posts = juju_biz.posts_data
assert len(orig_posts) == 20, f"Expected 20 posts, found {len(orig_posts)}"

# The 20 new dates (Evening Drive: 7:15 PM MDT -> 01:15:00.000Z UTC next day)
# Oct 12 7:15 PM MDT -> 2026-10-13T01:15:00.000Z
# Oct 13 7:15 PM MDT -> 2026-10-14T01:15:00.000Z
# ...
# Oct 31 7:15 PM MDT -> 2026-11-01T01:15:00.000Z

encore_slots = [
    ("2026-10-12", "2026-10-13T01:15:00.000Z"),
    ("2026-10-13", "2026-10-14T01:15:00.000Z"),
    ("2026-10-14", "2026-10-15T01:15:00.000Z"),
    ("2026-10-15", "2026-10-16T01:15:00.000Z"),
    ("2026-10-16", "2026-10-17T01:15:00.000Z"),
    ("2026-10-17", "2026-10-18T01:15:00.000Z"),
    ("2026-10-18", "2026-10-19T01:15:00.000Z"),
    ("2026-10-19", "2026-10-20T01:15:00.000Z"),
    ("2026-10-20", "2026-10-21T01:15:00.000Z"),
    ("2026-10-21", "2026-10-22T01:15:00.000Z"),
    ("2026-10-22", "2026-10-23T01:15:00.000Z"),
    ("2026-10-23", "2026-10-24T01:15:00.000Z"),
    ("2026-10-24", "2026-10-25T01:15:00.000Z"),
    ("2026-10-25", "2026-10-26T01:15:00.000Z"),
    ("2026-10-26", "2026-10-27T01:15:00.000Z"),
    ("2026-10-27", "2026-10-28T01:15:00.000Z"),
    ("2026-10-28", "2026-10-29T01:15:00.000Z"),
    ("2026-10-29", "2026-10-30T01:15:00.000Z"),
    ("2026-10-30", "2026-10-31T01:15:00.000Z"),
    ("2026-10-31", "2026-11-01T01:15:00.000Z")
]

encore_posts_data = []
for i, p in enumerate(orig_posts):
    cal_date, utc_due = encore_slots[i]
    feature_label = "NAOMI OSAKA" if p["id"] >= 11 else "JUJU WATKINS"
    encore_posts_data.append({
        "id": p["id"],
        "encore_id": f"encore-{p['id']:02d}",
        "feature": feature_label,
        "calDate": cal_date,
        "slot": f"{cal_date} Evening (7:15 PM MDT)",
        "dueAt": utc_due,
        "assetFile": p["assetFile"],
        "assetUrl": p["assetUrl"],
        "cta": p.get("cta", ""),
        "text": p["text"]
    })

def schedule_post(post):
    query = '''
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            __typename
            ... on PostActionSuccess {
                post {
                    id
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
    '''

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {
                    "image": {
                        "url": post["assetUrl"]
                    }
                }
            ]
        }
    }

    data = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.buffer.com',
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 80)
    print("CAMPAIGN AMPLIFICATION: JUJU BUSINESS & NAOMI OSAKA ENCORE WAVE (20 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Window: Oct 12 – Oct 31, 2026 (Daily at 7:15 PM MDT / 01:15 UTC)")
    print(f"Execution Start: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    report_path = os.path.join(base_dir, "juju-business-encore-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["encore_id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(encore_posts_data, 1):
        e_id = post["encore_id"]
        feat = post["feature"]

        if e_id in results and results[e_id].get("postId"):
            print(f"[{idx}/20] ({feat}) Post #{e_id} already scheduled (Buffer ID: {results[e_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/20] ({feat}) Scheduling: #{e_id} ({post['slot']}) - {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {wait_sec + 5}s...")
                time.sleep(wait_sec + 5)
                continue

            create_post_data = res.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                st = post_obj.get("status")
                due = post_obj.get("dueAt")
                print(f"  >>> SUCCESS: Post ID {b_id} scheduled for {due} (status: {st})")
                results[e_id] = {
                    "id": post["id"],
                    "encore_id": e_id,
                    "campaign": "juju-business-encore",
                    "feature": feat,
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetFile": post["assetFile"],
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[e_id] = {
                    "id": post["id"],
                    "encore_id": e_id,
                    "campaign": "juju-business-encore",
                    "feature": feat,
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 80)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/20 encore posts scheduled successfully.")
    print("=" * 80)

if __name__ == "__main__":
    main()
