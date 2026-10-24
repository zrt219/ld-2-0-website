# -*- coding: utf-8 -*-
"""
Schedule CFL-NFL Gameday & Playoff Campaign in Buffer
Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Featuring: Edmonton Elks (CFL West Champions) & Cleveland Browns (NFL AFC North)

Strict Invariants:
- Zero asterisks (* or **)
- Zero em dashes (—, &mdash;, \u2014)
- Production custom domain URLs (https://lornettedaye.com/campaigns/cfl-nfl/...)
- Persistent tracking in scripts/cfl-nfl-scheduled-report.json
"""

import sys
import os
import json
import ssl
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

CREATE_POST_MUTATION = """
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
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
    ... on UnauthorizedError { message }
  }
}
"""

def schedule_post(item):
    payload = {
        "query": CREATE_POST_MUTATION,
        "variables": {
            "input": {
                "channelId": CHANNEL_ID,
                "text": item["text"],
                "schedulingType": "automatic",
                "mode": item.get("mode", "customScheduled"),
                "dueAt": item.get("dueAt"),
                "assets": [{"image": {"url": item["asset_url"]}}]
            }
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            res_data = json.loads(resp.read().decode("utf-8"))
            create_post = res_data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            if typename == "PostActionSuccess" and "post" in create_post:
                p = create_post["post"]
                return True, p.get("id"), p.get("status")
            else:
                msg = create_post.get("message") or json.dumps(create_post)
                return False, typename, msg
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get("Retry-After")
        wait = int(retry_after) if retry_after and retry_after.isdigit() else 3600
        return False, "429", wait
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🏈 SCHEDULING CFL-NFL GAMEDAY & PLAYOFF CAMPAIGN")
    print("Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)")
    print("Zero Asterisks | Zero Em Dashes | 3 Production Custom Assets")
    print("================================================================\n")
    
    queue_file = "scripts/master-cfl-nfl-queue.json"
    if not os.path.exists(queue_file):
        print(f"Error: {queue_file} not found. Run scripts/build_cfl_nfl_campaign.py first.")
        sys.exit(1)
        
    with open(queue_file, "r", encoding="utf-8") as f:
        queue = json.load(f)
        
    report_file = "scripts/cfl-nfl-scheduled-report.json"
    if os.path.exists(report_file):
        with open(report_file, "r", encoding="utf-8") as f:
            scheduled_ids = json.load(f)
    else:
        scheduled_ids = {}
        
    print(f"Total posts in queue: {len(queue)}")
    print(f"Already scheduled in report: {len(scheduled_ids)}")
    
    if "--build-only" in sys.argv:
        print("Flag --build-only passed. Exiting without calling Buffer.")
        return

    for idx, item in enumerate(queue):
        item_id = item["id"]
        if item_id in scheduled_ids:
            continue
            
        print(f"[{idx+1}/{len(queue)}] Scheduling {item_id} | {item['slot']}...", end="", flush=True)
        ok, res_id, res_status = schedule_post(item)
        
        if ok:
            print(f" ✅ SUCCESS: Post ID {res_id} ({res_status})")
            scheduled_ids[item_id] = {
                "postId": res_id,
                "status": res_status,
                "dueAt": item.get("dueAt"),
                "slot": item.get("slot"),
                "mode": item.get("mode"),
                "asset_url": item["asset_url"]
            }
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(scheduled_ids, f, indent=2)
            time.sleep(1.0)
        elif res_id == "429":
            print(f"\n⚠️ BUFFER API LIMIT REACHED (429).")
            print(f"Retry-After: {res_status} seconds.")
            break
        else:
            print(f" ⚠️ {res_id}: {res_status}")
            break

    print("\n================================================================")
    print(f"📊 REPORT: {len(scheduled_ids)} of {len(queue)} posts scheduled.")
    print(f"Persistent Report: {report_file}")
    print("================================================================")

if __name__ == "__main__":
    main()
