# -*- coding: utf-8 -*-
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
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/marcus-freeman'

HASHTAGS = "#MarcusFreeman #NotreDame #FightingIrish #CollegeFootball #NCAA #SportsLeadership #CoachingExcellence #RepresentationMatters #AthleticDirector #ExecutiveLeadership #OlympicMindset #LornetteDaye #DisciplineBuildsFreedom"

posts_data = [
    {
        "id": 1,
        "slot": "Week 1 Mid-Week: Wednesday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-16T16:00:00.000Z",
        "assetFile": "marcus-freeman.png",
        "assetUrl": f"{CDN_BASE}/marcus-freeman.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""MARCUS FREEMAN: CULTURE BEFORE SCHEME. ☘️🏈⚡

When Marcus Freeman took the helm at the University of Notre Dame, he stepped into one of the most storied, pressurized leadership roles in all of sports.

Everyone wanted to ask about defensive schemes, transfer portal acquisitions, and offensive play-calling. But Coach Freeman did what true generational leaders do: he focused entirely on culture.

"Our standard is not just about winning games on Saturday," Freeman noted. "It is about building men who understand discipline, selflessness, and accountability long after the stadium lights go out."

In my 40+ years coaching Olympic athletes and advising athletic directors, schemes win plays—culture wins championships. When your locker room is united in purpose and mutual respect, execution takes care of itself.

Collegiate Athletic Directors & Head Coaches: Are you recruiting talent to fit your playbook, or building a culture strong enough to shape your talent?

👉 Bring Lornette Daye to your coaching staff symposium or athletic department leadership retreat: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 2,
        "slot": "Week 1 Game Day: Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-19T16:00:00.000Z",
        "assetFile": "marcus-freeman.png",
        "assetUrl": f"{CDN_BASE}/marcus-freeman.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": f"""PRESSURE UNDER THE GOLDEN DOME. 🏟️✨☘️

It is Saturday morning. 80,000 screaming fans are filling Notre Dame Stadium, millions more are tuned in on national television, and every single decision you make with a headset on will be dissected by commentators across the nation.

How does Marcus Freeman stay calm when the noise reaches deafening levels?

He anchors himself in daily preparation and emotional balance. He teaches his players: "Don't rise to the occasion. Sink to the level of your training."

Masculine leadership under extreme pressure isn't about rage or panic. It is about steady, unshakeable presence that settles the nervous system of everyone around you.

Fathers, coaches, and male executives: When crisis strikes your organization or family, do they mirror your panic, or your poise?

👉 Master emotional resilience, purpose-centered reflection, and steadfast leadership. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 3,
        "slot": "Week 2 Mid-Week: Wednesday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-23T16:00:00.000Z",
        "assetFile": "marcus-freeman.png",
        "assetUrl": f"{CDN_BASE}/marcus-freeman.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""REPRESENTATION, EXCELLENCE & BREAKING BARRIERS. 🌍🤝🏈

Marcus Freeman's journey is a powerful testament to the changing face of modern leadership. Born to an African American father and a Korean mother, Coach Freeman carries a rich multicultural heritage that connects deeply with today's student-athletes.

He is only the second Black head football coach in Notre Dame's 135-year history. Yet Freeman never asks for lowered standards. He demands excellence in the classroom, in the community, and on the gridiron.

As an Olympian coach who has spent four decades advocating for diversity and mental toughness in sports, representation matters not because of quotas, but because young athletes need to see that excellence has no single face.

University Leaders & Corporate Executives: How are you cultivating leadership pipelines that celebrate diverse lived experiences while upholding championship standards?

👉 Book Lornette Daye for keynotes on inclusive leadership, team cohesion, and breaking athletic barriers: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 4,
        "slot": "Week 2 Game Day: Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-26T16:00:00.000Z",
        "assetFile": "marcus-freeman.png",
        "assetUrl": f"{CDN_BASE}/marcus-freeman.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""DISCIPLINE BUILDS FREEDOM. 🛡️🏆☘️

Look closely at the slogan behind Coach Marcus Freeman: "Discipline builds freedom. Change. A stronger tomorrow."

Most people view discipline as a restriction—a grueling list of things you can't do. Elite performers understand that discipline is the exact mechanism that unlocks creative freedom under pressure.

When footwork is automatic, when conditioning is unmatched, and when trust in your brother beside you is absolute—fear evaporates. You play fast, aggressive, and free.

Athletes, coaches, and competitors: Are you willing to pay the daily price of discipline in an empty stadium so you can taste freedom under the lights?

👉 Train the inner endurance of champions and finish your race with purpose. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
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
            body = json.loads(resp.read().decode('utf-8'))
            return body
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
    print("Starting Buffer queue scheduling for Marcus Freeman Campaign (4 posts)...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "marcus-freeman-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                existing_report = json.load(f)
                for item in existing_report.get("results", []):
                    if item.get("success") and item.get("bufferPostId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    print(f"Loaded {len(results)} previously scheduled posts from report.")

    daily_limit_hit = False

    for idx, post in enumerate(posts_data, 1):
        post_id_num = post["id"]
        if post_id_num in results and results[post_id_num].get("success"):
            print(f"[{idx}/4] Post #{post_id_num} already scheduled (Buffer ID: {results[post_id_num]['bufferPostId']}). Skipping.")
            continue

        while True:
            print(f"[{idx}/4] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
            resp = schedule_post(post)

            # Check for 429 rate limit
            if resp.get("status_code") == 429 or "429" in str(resp.get("error", "")):
                wait_sec = resp.get("retry_after", 60)
                if wait_sec > 900:
                    print(f"   [DAILY 24H LIMIT] Buffer 24-hour daily limit reached. Reset in {wait_sec}s.")
                    print(f"   [AUTONOMOUS PERSISTENCE] Persisting queue state to report for background timer catchup.")
                    daily_limit_hit = True
                    break
                print(f"   [RATE LIMIT] HTTP 429 encountered. Buffer cooldown: sleeping {wait_sec + 5} seconds...")
                time.sleep(wait_sec + 5)
                print(f"   [RESUMING] Retrying Post #{post['id']} now...")
                continue

            create_post_data = resp.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                status = post_obj.get("status")
                due_at = post_obj.get("dueAt")
                print(f"   --> SUCCESS! Post ID: {b_id} | Status: {status} | Due: {due_at}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "bufferPostId": b_id,
                    "status": status,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"],
                    "success": True
                }
                break
            else:
                err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
                print(f"   --> FAILED: {err_msg}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "error": str(err_msg),
                    "success": False
                }
                break

        # Save checkpoint after each post
        ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
        successful_count = sum(1 for r in ordered_results if r.get("success"))
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump({
                "campaign": "Marcus Freeman - Leadership. Legacy. Barriers Broken",
                "total_posts": len(posts_data),
                "successful_posts": successful_count,
                "daily_limit_hit": daily_limit_hit,
                "channelId": CHANNEL_ID,
                "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "results": ordered_results
            }, f, indent=2)

        if daily_limit_hit:
            print("   [AUTONOMOUS HANDOFF] Stopping execution loop for background timer catchup.")
            break

        time.sleep(1.0)

    ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
    successful_count = sum(1 for r in ordered_results if r.get("success"))
    print("-" * 60)
    print(f"Marcus Freeman Campaign Scheduling Complete: {successful_count}/4 posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")

if __name__ == "__main__":
    main()
