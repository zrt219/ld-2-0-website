# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for Jazzy Davidson & JuJu Watkins USC 20-Day Campaign
Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Source: scripts/master-jazzy-usc-queue.json
Output: scripts/jazzy-usc-scheduled-report.json
"""

import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

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
            "text": post["caption"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {
                    "image": {
                        "url": post["image"]
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
        with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
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
    print("JAZZY DAVIDSON & JUJU WATKINS USC 20-DAY CAMPAIGN SCHEDULER")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    queue_path = os.path.join(os.path.dirname(__file__), "master-jazzy-usc-queue.json")
    report_path = os.path.join(os.path.dirname(__file__), "jazzy-usc-scheduled-report.json")

    with open(queue_path, "r", encoding="utf-8") as f:
        posts_data = json.load(f)

    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
                items = existing if isinstance(existing, list) else existing.get("results", [])
                for item in items:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["day"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        day = post["day"]
        if day in results and results[day].get("postId"):
            print(f"[{idx}/{len(posts_data)}] Day {day:02d} already scheduled (Buffer ID: {results[day]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/{len(posts_data)}] Scheduling: Day {day:02d} ({post['date']}) - Due: {post['dueAt']}")
            print(f"  Title: {post['title']}")
            print(f"  Image: {post['image']}")
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
                print(f"  >>> SUCCESS: Buffer Post ID {b_id} scheduled for {due} (status: {st})")
                results[day] = {
                    "day": day,
                    "date": post["date"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "image": post["image"],
                    "title": post["title"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[day] = {
                    "day": day,
                    "date": post["date"],
                    "dueAt": post["dueAt"],
                    "image": post["image"],
                    "title": post["title"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

            time.sleep(2.0)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 80)
    print(f"Scheduling complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/{len(posts_data)} posts scheduled successfully.")
    print("=" * 80)

if __name__ == "__main__":
    main()
