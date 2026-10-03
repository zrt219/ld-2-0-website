# -*- coding: utf-8 -*-
import json
import os
import ssl
import sys
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

def get_token():
    t = os.environ.get('BUFFER_ACCESS_TOKEN')
    if t:
        return t
    for env_name in ['.env.local', '.env']:
        p = os.path.join(os.path.dirname(__file__), '..', env_name)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('BUFFER_ACCESS_TOKEN='):
                        val = line.strip().split('=', 1)[1].strip()
                        if val:
                            return val
    return 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0'

TOKEN = get_token()

mutation = '''
mutation EditPost($input: EditPostInput!) {
    editPost(input: $input) {
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
        ... on NotFoundError {
            message
        }
    }
}
'''

def edit_post(post_id, new_due, text, asset_url):
    payload = {
        "query": mutation,
        "variables": {
            "input": {
                "id": post_id,
                "dueAt": new_due,
                "mode": "customScheduled",
                "schedulingType": "automatic",
                "text": text,
                "assets": [
                    {
                        "image": {
                            "url": asset_url
                        }
                    }
                ]
            }
        }
    }
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    req = urllib.request.Request("https://api.buffer.com", data=json.dumps(payload).encode("utf-8"), headers=headers)
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    # 1. Load curacao streak posts
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", "scripts/schedule-curacao-streak.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    posts_by_id = {p["id"]: p for p in mod.posts_data}

    # Load report
    with open("scripts/curacao-streak-scheduled-report.json", "r", encoding="utf-8") as f:
        report = json.load(f)

    updates = [
        {"id": 3, "new_due": "2026-10-03T23:30:00.000Z", "new_slot": "Day 1: Saturday 5:30 PM MDT (Oct 03, 2026)"},
        {"id": 5, "new_due": "2026-10-04T23:30:00.000Z", "new_slot": "Day 2: Sunday 5:30 PM MDT (Oct 04, 2026)"}
    ]

    for u in updates:
        p_id = u["id"]
        post_obj = posts_by_id[p_id]
        report_item = next((r for r in report if r["id"] == p_id), None)
        if not report_item:
            print(f"Error: Post #{p_id} not found in report.")
            continue
        buffer_id = report_item.get("postId")
        print(f"Rescheduling Curaçao Streak Post #{p_id} (Buffer ID: {buffer_id}) to {u['new_due']} ({u['new_slot']})...")
        res = edit_post(buffer_id, u["new_due"], post_obj["text"], post_obj["assetUrl"])
        print("  Response:", json.dumps(res))
        edit_res = res.get("data", {}).get("editPost", {})
        if "post" in edit_res:
            print(f"  >>> SUCCESS: Post #{p_id} updated in Buffer to {edit_res['post']['dueAt']}")
            report_item["dueAt"] = u["new_due"]
            report_item["slot"] = u["new_slot"]
        else:
            print(f"  >>> FAILED: {res}")
            sys.exit(1)
        time.sleep(2)

    # Save updated report
    with open("scripts/curacao-streak-scheduled-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("Updated scripts/curacao-streak-scheduled-report.json successfully.")

    # Update master queue
    with open("scripts/master-campaign-queue.json", "r", encoding="utf-8") as f:
        mq = json.load(f)

    for item in mq:
        if item.get("id") == "curacao-strk-03":
            item["dueAt"] = "2026-10-03T23:30:00.000Z"
            item["slot"] = "Day 1: Saturday 5:30 PM MDT (Oct 03, 2026)"
        elif item.get("id") == "curacao-strk-05":
            item["dueAt"] = "2026-10-04T23:30:00.000Z"
            item["slot"] = "Day 2: Sunday 5:30 PM MDT (Oct 04, 2026)"

    with open("scripts/master-campaign-queue.json", "w", encoding="utf-8") as f:
        json.dump(mq, f, indent=2, ensure_ascii=False)
    print("Updated scripts/master-campaign-queue.json successfully.")

if __name__ == "__main__":
    main()
