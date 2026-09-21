# -*- coding: utf-8 -*-
import os
import json

# Python builder that generates scripts/schedule-mondo-campaign.py
def build():
    script_path = os.path.join(os.path.dirname(__file__), "schedule-mondo-campaign.py")
    
    # We will write the schedule script with all 42 posts
    with open(script_path, "w", encoding="utf-8") as f:
        f.write('''import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/mondo'

HASHTAGS = "#MondoDuplantis #Duplantis #TrackAndField #PoleVault #OlympicChampion #AthleticDirector #CoachingExcellence #HighPerformance #NCAATrack #WorldAthletics #SportsLeadership #OlympicMindset #LornetteDaye #RaisingTheBar"

posts_data = [
''')
        # We will write each post
        import mondo_posts_builder
        posts = mondo_posts_builder.get_mondo_posts()
        for p in posts:
            f.write("    " + json.dumps(p, ensure_ascii=False, indent=4).replace("\\n", "\\\\n") + ",\n")
            
        f.write(''''
]

def schedule_post(post):
    query = """
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            ... on PostActionSuccess {
                post {
                    id
                    status
                    scheduledAt
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

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "customScheduled",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "assets": {
                "images": [
                    {
                        "url": post["assetUrl"]
                    }
                ]
            }
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
            body = json.loads(resp.read().decode('utf-8'))
            return body
    except Exception as e:
        return {"error": str(e)}

def main():
    print(f"Starting Buffer queue scheduling for Mondo Duplantis Campaign (42 posts)...")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    results = []
    success_count = 0

    for idx, post in enumerate(posts_data, 1):
        print(f"[{idx}/42] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
        resp = schedule_post(post)

        create_post_data = resp.get("data", {}).get("createPost", {})
        post_obj = create_post_data.get("post")

        if post_obj and post_obj.get("id"):
            post_id = post_obj["id"]
            status = post_obj.get("status")
            sched_at = post_obj.get("scheduledAt")
            print(f"   --> SUCCESS! Post ID: {post_id} | Status: {status} | Scheduled: {sched_at}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "bufferPostId": post_id,
                "status": status,
                "assetUrl": post["assetUrl"],
                "cta": post["cta"],
                "success": True
            })
            success_count += 1
        else:
            err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
            print(f"   --> FAILED: {err_msg}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "error": err_msg,
                "success": False
            })

        time.sleep(0.5)

    print("-" * 60)
    print(f"Mondo Campaign Scheduling Complete: {success_count}/42 posts successfully placed into Buffer Scheduled Queue.")

    report_path = os.path.join(os.path.dirname(__file__), "mondo-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({
            "campaign": "Mondo Duplantis - The Ceiling is an Illusion",
            "total_posts": len(posts_data),
            "successful_posts": success_count,
            "channelId": CHANNEL_ID,
            "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "results": results
        }, f, indent=2)
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
''')
    print("Wrote scripts/schedule-mondo-campaign.py successfully!")

if __name__ == "__main__":
    build()