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
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

def load_module_posts(filepath):
    spec = importlib.util.spec_from_file_location("mod", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.posts_data

def load_report_ids(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    id_map = {}
    if isinstance(data, list):
        for item in data:
            pid = item.get("postId") or item.get("bufferPostId")
            id_map[item["id"]] = pid
    elif isinstance(data, dict):
        for item in data.get("results", []):
            pid = item.get("postId") or item.get("bufferPostId")
            id_map[item["id"]] = pid
    return id_map

# Load all 6 campaigns
base_dir = os.path.dirname(__file__)

toronto_posts = load_module_posts(os.path.join(base_dir, "schedule-toronto-campaign.py"))
toronto_ids = load_report_ids(os.path.join(base_dir, "toronto-scheduled-report.json"))

camward_posts = load_module_posts(os.path.join(base_dir, "schedule-camward-shedeur-campaign.py"))
camward_ids = load_report_ids(os.path.join(base_dir, "camward-shedeur-scheduled-report.json"))

shedeur_posts = load_module_posts(os.path.join(base_dir, "schedule-shedeur-campaign.py"))
shedeur_ids = load_report_ids(os.path.join(base_dir, "shedeur-scheduled-report.json"))

travis_posts = load_module_posts(os.path.join(base_dir, "schedule-travis-hunter-campaign.py"))
travis_ids = load_report_ids(os.path.join(base_dir, "travis-hunter-scheduled-report.json"))

juju_posts = load_module_posts(os.path.join(base_dir, "schedule-juju-campaign.py"))
juju_ids = load_report_ids(os.path.join(base_dir, "juju-scheduled-report.json"))

juju_biz_posts = load_module_posts(os.path.join(base_dir, "schedule-juju-business-campaign.py"))
juju_biz_ids = load_report_ids(os.path.join(base_dir, "juju-business-scheduled-report.json"))

def tag_pool(posts, ids, campaign_name):
    items = []
    for p in posts:
        b_id = ids.get(p["id"])
        items.append({
            "campaign": campaign_name,
            "campaign_post_id": p["id"],
            "buffer_id": b_id,
            "text": p["text"],
            "assetUrl": p["assetUrl"],
            "cta": p.get("cta", "")
        })
    return items

pool_toronto = tag_pool(toronto_posts, toronto_ids, "Toronto (Olympic Mindset)")
pool_camward = tag_pool(camward_posts, camward_ids, "Cam Ward x Shedeur")
pool_juju = tag_pool(juju_posts, juju_ids, "JuJu Watkins (USC Comeback)")
pool_travis = tag_pool(travis_posts, travis_ids, "Travis Hunter (Two-Way)")
pool_biz = tag_pool(juju_biz_posts, juju_biz_ids, "JuJu Business & Naomi Osaka")
pool_shedeur = tag_pool(shedeur_posts, shedeur_ids, "Shedeur Sanders Solo")

# Interleave using balanced round-robin
# In each cycle: Toronto, Cam Ward, JuJu, Travis, Biz 1, Shedeur, Biz 2
interleaved = []
p_toronto = list(pool_toronto)
p_camward = list(pool_camward)
p_juju = list(pool_juju)
p_travis = list(pool_travis)
p_biz = list(pool_biz)
p_shedeur = list(pool_shedeur)

while p_toronto or p_camward or p_juju or p_travis or p_biz or p_shedeur:
    if p_toronto:
        interleaved.append(p_toronto.pop(0))
    if p_camward:
        interleaved.append(p_camward.pop(0))
    if p_juju:
        interleaved.append(p_juju.pop(0))
    if p_travis:
        interleaved.append(p_travis.pop(0))
    if p_biz:
        interleaved.append(p_biz.pop(0))
    if p_shedeur:
        interleaved.append(p_shedeur.pop(0))
    if p_biz:
        interleaved.append(p_biz.pop(0))

print(f"Total interleaved posts: {len(interleaved)}")
assert len(interleaved) == 71, f"Expected 71 posts, got {len(interleaved)}"

# Build the 71 schedule slots (Sep 22 - Oct 12, 2026)
schedule_plan = [
    # Week 1: 5 posts / day (35 posts)
    ("2026-09-22", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-23", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-24", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-25", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-26", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-27", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),
    ("2026-09-28", ["14:15:00.000Z", "16:45:00.000Z", "19:15:00.000Z", "21:45:00.000Z", "23:45:00.000Z"]),

    # Week 2: 4 posts / day Tue-Fri, 3 posts / day Sat-Mon (25 posts)
    ("2026-09-29", ["15:00:00.000Z", "18:00:00.000Z", "21:00:00.000Z", "23:30:00.000Z"]),
    ("2026-09-30", ["15:00:00.000Z", "18:00:00.000Z", "21:00:00.000Z", "23:30:00.000Z"]),
    ("2026-10-01", ["15:00:00.000Z", "18:00:00.000Z", "21:00:00.000Z", "23:30:00.000Z"]),
    ("2026-10-02", ["15:00:00.000Z", "18:00:00.000Z", "21:00:00.000Z", "23:30:00.000Z"]),
    ("2026-10-03", ["15:30:00.000Z", "19:30:00.000Z", "23:00:00.000Z"]),
    ("2026-10-04", ["15:30:00.000Z", "19:30:00.000Z", "23:00:00.000Z"]),
    ("2026-10-05", ["15:30:00.000Z", "19:30:00.000Z", "23:00:00.000Z"]),

    # Week 3: 2 posts / day Tue-Fri, 1 post / day Sat-Mon (11 posts)
    ("2026-10-06", ["16:00:00.000Z", "21:00:00.000Z"]),
    ("2026-10-07", ["16:00:00.000Z", "21:00:00.000Z"]),
    ("2026-10-08", ["16:00:00.000Z", "21:00:00.000Z"]),
    ("2026-10-09", ["16:00:00.000Z", "21:00:00.000Z"]),
    ("2026-10-10", ["17:30:00.000Z"]),
    ("2026-10-11", ["17:30:00.000Z"]),
    ("2026-10-12", ["17:30:00.000Z"])
]

all_slots = []
for date_str, times in schedule_plan:
    for t in times:
        all_slots.append(f"{date_str}T{t}")

print(f"Total time slots generated: {len(all_slots)}")
assert len(all_slots) == 71, f"Expected 71 slots, got {len(all_slots)}"

# Assign new slot to each post
for i in range(71):
    interleaved[i]["new_dueAt"] = all_slots[i]
    interleaved[i]["slot_index"] = i + 1

def edit_buffer_post(b_id, new_due, text, asset_url):
    query = '''
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
    variables = {
        "input": {
            "id": b_id,
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
    print("ACCELERATED MASTER RESCHEDULING: 71 POSTS ACROSS SEP 22 - OCT 12, 2026")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Execution Start: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    report_file = os.path.join(base_dir, "rescheduled-master-report.json")
    results = {}
    if os.path.exists(report_file):
        try:
            with open(report_file, "r", encoding="utf-8") as f:
                saved = json.load(f)
                for item in saved:
                    if item.get("status") in ["scheduled", "success"] and item.get("dueAt") == item.get("new_dueAt"):
                        results[item["buffer_id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    print(f"Loaded {len(results)} already rescheduled posts from prior run.")

    for idx, item in enumerate(interleaved, 1):
        b_id = item["buffer_id"]
        new_due = item["new_dueAt"]
        camp = item["campaign"]
        post_num = item["campaign_post_id"]

        if b_id in results:
            print(f"[{idx}/71] Post #{b_id} ({camp} #{post_num}) already rescheduled to {new_due}. Skipping.")
            continue

        while True:
            print(f"[{idx}/71] Rescheduling Post #{b_id} ({camp} #{post_num}) -> {new_due}...")
            res = edit_buffer_post(b_id, new_due, item["text"], item["assetUrl"])

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Buffer cooldown: sleeping {wait_sec + 5}s...")
                time.sleep(wait_sec + 5)
                continue

            edit_data = res.get("data", {}).get("editPost", {})
            typename = edit_data.get("__typename")
            post_obj = edit_data.get("post")

            if typename == "PostActionSuccess" and post_obj:
                confirmed_due = post_obj.get("dueAt")
                st = post_obj.get("status")
                print(f"  >>> SUCCESS: Updated Post {b_id} dueAt: {confirmed_due} (Status: {st})")
                results[b_id] = {
                    "slot_index": idx,
                    "campaign": camp,
                    "campaign_post_id": post_num,
                    "buffer_id": b_id,
                    "new_dueAt": new_due,
                    "dueAt": confirmed_due,
                    "status": st,
                    "assetUrl": item["assetUrl"],
                    "cta": item["cta"]
                }
                break
            else:
                err_msg = edit_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[b_id] = {
                    "slot_index": idx,
                    "campaign": camp,
                    "campaign_post_id": post_num,
                    "buffer_id": b_id,
                    "new_dueAt": new_due,
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(1.2)

        # Save checkpoint every 5 posts
        if idx % 5 == 0 or idx == 71:
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 80)
    print(f"Rescheduling complete! Full report written to {report_file}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Final Outcome: {success_count}/71 posts rescheduled successfully into accelerated calendar.")
    print("=" * 80)

if __name__ == "__main__":
    main()
