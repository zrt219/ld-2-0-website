# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 5: NBA - PRO BASKETBALL LEADERSHIP & EXECUTION (3 Posts)
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
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

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

posts_data = [
    {
        "id": 1,
        "slot": "Monday (08:30 AM MDT)",
        "dueAt": "2026-10-19T14:30:00.000Z",
        "assetFile": "nba-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "ANTHONY EDWARDS: THE NEXT LEVEL ALWAYS DEMANDS MORE. 🐺🏀\n\nTalent gets you noticed. Growth keeps you there.\n\nWhen Anthony Edwards entered the NBA, his raw physical explosion and charisma were undeniable. Yet what separates an exciting young talent from an MVP contender is the relentless appetite to refine weaknesses. Edwards overhauled his catch-and-shoot mechanics, dedicated himself to lock-down perimeter defense, and learned how to control game tempo in the closing four minutes.\n\nIn four decades coaching Olympic athletes, I tell champions: the hardest part of success is not arriving. It is answering the elevated demand of the room you just entered.\n\nLeaders: What part of your professional craft needs to elevate to meet your next opportunity?\n\n👉 Discover how Olympic-level self-assessment builds unstoppable career momentum. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#AnthonyEdwards #MinnesotaTimberwolves #TheNextLevel #FinishStrong #OlympicMindset #GrowthMindset #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Monday (11:00 AM MDT)",
        "dueAt": "2026-10-19T17:00:00.000Z",
        "assetFile": "nba-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "DISCIPLINE BUILDS FREEDOM: COMMANDING THE ARENA IN MINNEAPOLIS. 🌲⚡\n\nTrue athletic freedom looks effortless, but it is anchored in ruthless discipline.\n\nWhen you watch Anthony Edwards drive into the lane, elevate above rim protectors, and absorb contact, you are witnessing core strength, deceleration mechanics, and kinetic control forged through thousands of invisible repetitions. Freedom on the court is not reckless abandonment; it is the privilege of complete physical preparation.\n\nAthletes: Are you putting in the quiet conditioning required to make pressure situations feel effortless?\n\n👉 Build a champion mindset, focus, and recovery systems on and off the court. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#DisciplineBuildsFreedom #AntMan #WolvesHoops #SurvivalSkillsForAthletes #OlympicCoach #PhysicalResilience #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Monday (01:15 PM MDT)",
        "dueAt": "2026-10-19T19:15:00.000Z",
        "assetFile": "nba-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "DIFFERENT GENERATIONS. SAME GOAL: EMBIID & EDGECOMBE IN PHILADELPHIA. 🔔🏙️\n\nChampionship culture bridges the gap between veteran mastery and youthful energy.\n\nJoel Embiid brings MVP experience, leadership presence, and tactical authority. VJ Edgecombe brings explosive rookie athleticism, fierce hunger, and modern speed. When an organization aligns the wisdom of established leadership with the vitality of the next generation, dynasties take root.\n\nIn corporate enterprises, senior executives must mentor rising talent without feeling threatened, and emerging leaders must honor institutional knowledge without losing their innovative edge.\n\nExecutives: How effectively is your organization bridging the generational divide to drive collective victory?\n\n👉 Align multi-generational teams to perform at peak capacity with Olympic team-building frameworks. Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n#Philadelphia76ers #JoelEmbiid #VJEdgecombe #GenerationalLeadership #ExecutivePerformance #CoachLornette"
    }
]

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
    print("=" * 75)
    print("CAMPAIGN 5: NBA - PRO BASKETBALL LEADERSHIP & EXECUTION (3 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "nba-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("results", [])
                for item in items:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/{len(posts_data)}] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/{len(posts_data)}] Scheduling: Post #{p_id} ({post['slot']}) - {post['dueAt']}...")
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
                results[p_id] = {
                    "id": p_id,
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "slot": post["slot"],
                    "assetUrl": post["assetUrl"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

            time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/3 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
