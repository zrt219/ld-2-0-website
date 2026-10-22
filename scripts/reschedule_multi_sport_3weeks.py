# -*- coding: utf-8 -*-
"""
Reschedule Multi-Sport Campaign: 3-Week Pacing (Oct 30 - Nov 19, 2026)
Total: 30 posts paced across 21 days (3 full weeks)
Cadence: 1 to 2 posts / day
Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
"""

import sys
import os
import json
import ssl
import urllib.request
import urllib.error
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

# 21-Day Pacing Schedule (Oct 30 to Nov 19, 2026)
PACED_SCHEDULE = [
    # Day 1: Thu Oct 30 (MDT = UTC-6)
    {"id": "CAMPAIGN_MULTI_001", "day": 1, "slot": "Day 1 Morning (08:30 AM MDT)", "dueAt": "2026-10-30T14:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_002", "day": 1, "slot": "Day 1 Afternoon (03:00 PM MDT)", "dueAt": "2026-10-30T21:00:00.000Z"},
    
    # Day 2: Fri Oct 31 (MDT = UTC-6)
    {"id": "CAMPAIGN_MULTI_003", "day": 2, "slot": "Day 2 Morning (08:30 AM MDT)", "dueAt": "2026-10-31T14:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_004", "day": 2, "slot": "Day 2 Afternoon (03:00 PM MDT)", "dueAt": "2026-10-31T21:00:00.000Z"},
    
    # Day 3: Sat Nov 01 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_005", "day": 3, "slot": "Day 3 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-01T18:00:00.000Z"},
    
    # Day 4: Sun Nov 02 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_006", "day": 4, "slot": "Day 4 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-02T18:00:00.000Z"},
    
    # Day 5: Mon Nov 03 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_007", "day": 5, "slot": "Day 5 Morning (08:30 AM MST)", "dueAt": "2026-11-03T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_008", "day": 5, "slot": "Day 5 Afternoon (03:00 PM MST)", "dueAt": "2026-11-03T22:00:00.000Z"},
    
    # Day 6: Tue Nov 04 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_009", "day": 6, "slot": "Day 6 Morning (08:30 AM MST)", "dueAt": "2026-11-04T15:30:00.000Z"},
    
    # Day 7: Wed Nov 05 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_010", "day": 7, "slot": "Day 7 Morning (08:30 AM MST)", "dueAt": "2026-11-05T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_011", "day": 7, "slot": "Day 7 Afternoon (03:00 PM MST)", "dueAt": "2026-11-05T22:00:00.000Z"},
    
    # Day 8: Thu Nov 06 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_012", "day": 8, "slot": "Day 8 Morning (08:30 AM MST)", "dueAt": "2026-11-06T15:30:00.000Z"},
    
    # Day 9: Fri Nov 07 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_013", "day": 9, "slot": "Day 9 Morning (08:30 AM MST)", "dueAt": "2026-11-07T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_014", "day": 9, "slot": "Day 9 Afternoon (03:00 PM MST)", "dueAt": "2026-11-07T22:00:00.000Z"},
    
    # Day 10: Sat Nov 08 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_015", "day": 10, "slot": "Day 10 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-08T18:00:00.000Z"},
    
    # Day 11: Sun Nov 09 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_016", "day": 11, "slot": "Day 11 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-09T18:00:00.000Z"},
    
    # Day 12: Mon Nov 10 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_017", "day": 12, "slot": "Day 12 Morning (08:30 AM MST)", "dueAt": "2026-11-10T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_018", "day": 12, "slot": "Day 12 Afternoon (03:00 PM MST)", "dueAt": "2026-11-10T22:00:00.000Z"},
    
    # Day 13: Tue Nov 11 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_019", "day": 13, "slot": "Day 13 Morning (08:30 AM MST)", "dueAt": "2026-11-11T15:30:00.000Z"},
    
    # Day 14: Wed Nov 12 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_020", "day": 14, "slot": "Day 14 Morning (08:30 AM MST)", "dueAt": "2026-11-12T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_021", "day": 14, "slot": "Day 14 Afternoon (03:00 PM MST)", "dueAt": "2026-11-12T22:00:00.000Z"},
    
    # Day 15: Thu Nov 13 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_022", "day": 15, "slot": "Day 15 Morning (08:30 AM MST)", "dueAt": "2026-11-13T15:30:00.000Z"},
    
    # Day 16: Fri Nov 14 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_023", "day": 16, "slot": "Day 16 Morning (08:30 AM MST)", "dueAt": "2026-11-14T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_024", "day": 16, "slot": "Day 16 Afternoon (03:00 PM MST)", "dueAt": "2026-11-14T22:00:00.000Z"},
    
    # Day 17: Sat Nov 15 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_025", "day": 17, "slot": "Day 17 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-15T18:00:00.000Z"},
    
    # Day 18: Sun Nov 16 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_026", "day": 18, "slot": "Day 18 Mid-Day (11:00 AM MST)", "dueAt": "2026-11-16T18:00:00.000Z"},
    
    # Day 19: Mon Nov 17 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_027", "day": 19, "slot": "Day 19 Morning (08:30 AM MST)", "dueAt": "2026-11-17T15:30:00.000Z"},
    {"id": "CAMPAIGN_MULTI_028", "day": 19, "slot": "Day 19 Afternoon (03:00 PM MST)", "dueAt": "2026-11-17T22:00:00.000Z"},
    
    # Day 20: Tue Nov 18 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_029", "day": 20, "slot": "Day 20 Morning (08:30 AM MST)", "dueAt": "2026-11-18T15:30:00.000Z"},
    
    # Day 21: Wed Nov 19 (MST = UTC-7)
    {"id": "CAMPAIGN_MULTI_030", "day": 21, "slot": "Day 21 Morning (08:30 AM MST)", "dueAt": "2026-11-19T15:30:00.000Z"}
]

EDIT_POST_MUTATION = """
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
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
  }
}
"""

def update_post(post_id, new_due_at, text, asset_url):
    ctx = ssl._create_unverified_context()
    input_data = {
        "id": post_id,
        "dueAt": new_due_at,
        "mode": "customScheduled",
        "schedulingType": "automatic",
        "text": text,
        "assets": [{"image": {"url": asset_url}}]
    }
    
    payload = json.dumps({"query": EDIT_POST_MUTATION, "variables": {"input": input_data}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            edit_post = data.get("data", {}).get("editPost", {})
            typename = edit_post.get("__typename")
            if typename == "PostActionSuccess" and "post" in edit_post:
                p = edit_post["post"]
                return True, p.get("id"), p.get("dueAt")
            else:
                msg = edit_post.get("message") or json.dumps(edit_post)
                return False, typename, msg
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🔄 RESCHEDULING MULTI-SPORT CAMPAIGN ACROSS 21 DAYS (3 FULL WEEKS)")
    print("Dates: Thursday, Oct 30, 2026 - Wednesday, Nov 19, 2026")
    print("Cadence: 1 to 2 Posts / Day = 30 Posts Total")
    print("================================================================\n")
    
    with open("scripts/master-multi-sport-queue.json", "r", encoding="utf-8") as f:
        master_queue = json.load(f)
    
    with open("scripts/multi-sport-scheduled-report.json", "r", encoding="utf-8") as f:
        scheduled_report = json.load(f)
    
    post_lookup = {p["id"]: p for p in master_queue}
    schedule_lookup = {s["id"]: s for s in PACED_SCHEDULE}

    success_count = 0
    for idx, item in enumerate(PACED_SCHEDULE):
        pid = item["id"]
        report_entry = scheduled_report.get(pid, {})
        buffer_post_id = report_entry.get("postId")
        post_data = post_lookup.get(pid)
        
        if not buffer_post_id or not post_data:
            print(f"[{idx+1}/30] ⚠️ Missing info for {pid}")
            continue

        new_due_at = item["dueAt"]
        print(f"[{idx+1}/30] Rescheduling {pid} -> Day {item['day']} ({item['slot']})")
        ok, r_id, r_due = update_post(buffer_post_id, new_due_at, post_data["text"], post_data["asset_url"])
        
        if ok:
            print(f"   ✅ SUCCESS: Post {r_id} updated to {r_due}")
            # Update report entry
            report_entry["dueAt"] = new_due_at
            report_entry["slot"] = item["slot"]
            report_entry["day"] = item["day"]
            scheduled_report[pid] = report_entry
            
            # Update master queue item
            post_data["dueAt"] = new_due_at
            post_data["slot"] = item["slot"]
            success_count += 1
            time.sleep(1.5)  # Respect API pacing
        else:
            print(f"   ⚠️ ERROR: {r_id} - {r_due}")
            break

    # Save updated files
    with open("scripts/multi-sport-scheduled-report.json", "w", encoding="utf-8") as f:
        json.dump(scheduled_report, f, indent=2)
    
    with open("scripts/master-multi-sport-queue.json", "w", encoding="utf-8") as f:
        json.dump(master_queue, f, indent=2)

    print("\n================================================================")
    print(f"📊 SUMMARY: {success_count} / 30 posts successfully rescheduled across 21 days (3 weeks).")
    print("Date Span: Oct 30, 2026 to Nov 19, 2026")
    print("Report: scripts/multi-sport-scheduled-report.json")
    print("================================================================")

if __name__ == "__main__":
    main()
