# -*- coding: utf-8 -*-
"""
Mike Grier Executive Series Scheduler: 3-Week Campaign (Oct 25, Nov 01, Nov 08, 2026)
Creative: Mike Grier - From the Ice to the Front Office (San Jose Sharks GM)
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Asset URL: https://lornettedaye.com/campaigns/hockey/hockey-11-mike-grier-front-office.jpg (Verified HTTP 200 OK)

Invariants:
- Zero em dashes (—, \u2014)
- Zero "Coach Lornette" prefixes in copy
- Strict plural "Lornette’s Foundations"
- Dual Touchpoint CTA: Direct message on LinkedIn + https://lornettedaye.com/foundations
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
ASSET_URL = 'https://lornettedaye.com/campaigns/hockey/hockey-11-mike-grier-front-office.jpg'

GRIER_POSTS = [
    {
        "id": "GRIER_SERIES_01",
        "week": "Week 1",
        "slot": "Sunday, Oct 25, 2026 (09:00 AM MDT)",
        "dueAt": "2026-10-25T15:00:00.000Z",
        "theme": "The Transition: From 1,060 NHL Games to the Front Office",
        "text": """FROM THE ICE TO THE FRONT OFFICE: MIKE GRIER. 🏒💼

1,060 regular-season games in the National Hockey League. Decades battling in the dirty areas along the boards, absorbing hits, and earning every shift through relentless physical commitment.

Yet when Mike Grier hung up his skates, he refused to let his identity disappear when the locker room lights went dim. He committed to learning scouting, player development, and the complex business of hockey operations, ultimately making history as the first Black General Manager in NHL history with the San Jose Sharks.

In my four decades coaching Olympic-level performers and national champions, one foundational truth remains absolute: the jersey you wear is what you do, not who you are.

The athletes who achieve generational impact understand that physical discipline, locker room accountability, and high-pressure decision-making are not just sports skills. They are executive leadership skills that transfer directly into boardrooms and corporate governance.

When your playing days or current career chapter transitions, what foundation are you standing on?

Build an identity and career discipline that outlasts the arena:

👉 Explore Lornette's Foundations, our complete athlete development system: https://lornettedaye.com/foundations
💬 Or send me a direct message right here on LinkedIn to discuss athlete career transition programs and executive keynotes.

#MikeGrier #SanJoseSharks #NHL #FrontOffice #GeneralManager #HockeyHistory #AthleteTransition #IdentityBeyondSport #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "GRIER_SERIES_02",
        "week": "Week 2",
        "slot": "Sunday, Nov 01, 2026 (09:00 AM MST)",
        "dueAt": "2026-11-01T16:00:00.000Z",
        "theme": "Executive Leadership Under Pressure: Rebuilding an NHL Franchise",
        "text": """EXECUTIVE LEADERSHIP UNDER PRESSURE: REBUILDING WITH POISE. 🦈📊

Rebuilding a professional sports franchise is one of the most unforgiving leadership assignments in the world.

Fans want immediate gratification. The media dissects every roster tweak and draft selection. The noise is constant. As General Manager of the San Jose Sharks, Mike Grier has demonstrated the rarest trait in modern executive management: strategic patience.

He has not chased short-term emotional fixes. He has systematically drafted elite foundation pieces, rebuilt organizational depth, and established a culture anchored in work ethic, accountability, and character.

In elite sports coaching, championships are never built by reacting to last night's score. They are constructed through unshakeable systems executed with daily discipline.

Are you leading your organization with steady long-term vision, or reacting to daily noise?

Develop the emotional regulation, decision systems, and composure of a high-performance executive:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to schedule an executive leadership workshop or keynote.

#MikeGrier #SanJoseSharks #ExecutiveLeadership #StrategicPatience #CultureBuilding #EmotionalPoise #HighPerformance #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "GRIER_SERIES_03",
        "week": "Week 3",
        "slot": "Sunday, Nov 08, 2026 (09:00 AM MST)",
        "dueAt": "2026-11-08T16:00:00.000Z",
        "theme": "History in the Boardroom: Expanding Hockey's Horizons & Creating Legacy",
        "text": """HISTORY IN THE BOARDROOM: EXPANDING HOCKEY'S HORIZONS. 🏒🚪

For over a century, the decision-making corridors of the National Hockey League were occupied by a narrow tradition.

When Mike Grier was appointed General Manager in 2022, he didn't just accept a job. He broke a barrier that had stood since 1917, proving that Black excellence in hockey belongs at the very top of organizational governance.

Every young athlete and young professional watching Mike Grier negotiate trades, manage multimillion-dollar payrolls, and set franchise direction learns a profound lesson: your heritage, your discipline, and your integrity qualify you for any boardroom in the world.

At Lornette's Foundations, our guiding principle is simple: BETTER PEOPLE · BETTER PLAYERS.

When you develop character, resilience, and executive presence, the barriers of yesterday cannot contain the possibilities of tomorrow.

Who are you inspiring through the standard you set in your daily work?

Partner with us to build leaders who transform culture and leave enduring legacies:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect with me via direct message on LinkedIn for speaking engagements and leadership mentorship.

#MikeGrier #BlackHockeyHistory #Trailblazer #BetterPeopleBetterPlayers #DiversityInSport #ExecutivePresence #Legacy #LornettesFoundations #LornetteDaye"""
    }
]

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

def schedule_grier_post(post_item):
    ctx = ssl._create_unverified_context()
    input_data = {
        "channelId": CHANNEL_ID,
        "text": post_item["text"],
        "mode": "customScheduled",
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "dueAt": post_item["dueAt"],
        "assets": [{"image": {"url": ASSET_URL}}]
    }
    
    payload = json.dumps({"query": CREATE_POST_MUTATION, "variables": {"input": input_data}}).encode("utf-8")
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
            create_post = data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            if typename == "PostActionSuccess" and "post" in create_post:
                p = create_post["post"]
                return True, p.get("id"), p.get("status")
            else:
                msg = create_post.get("message") or json.dumps(create_post)
                return False, typename, msg
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🏒 MIKE GRIER 3-WEEK EXECUTIVE CAMPAIGN SCHEDULER")
    print(f"Asset: {ASSET_URL}")
    print("Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)")
    print("================================================================\n")
    
    report_file = "scripts/mike-grier-scheduled-report.json"
    if os.path.exists(report_file):
        with open(report_file, "r", encoding="utf-8") as f:
            scheduled_ids = json.load(f)
    else:
        scheduled_ids = {}

    for idx, item in enumerate(GRIER_POSTS):
        item_id = item["id"]
        if item_id in scheduled_ids:
            print(f"Already scheduled: {item_id}")
            continue

        print(f"[{idx+1}/3] Scheduling {item_id} | {item['week']} ({item['slot']})")
        print(f"   Theme: {item['theme']}")
        ok, res_id, res_status = schedule_grier_post(item)
        if ok:
            print(f"   ✅ SUCCESS: Post ID {res_id} ({res_status})\n")
            scheduled_ids[item_id] = {
                "postId": res_id,
                "status": res_status,
                "dueAt": item["dueAt"],
                "week": item["week"],
                "slot": item["slot"],
                "theme": item["theme"],
                "asset_url": ASSET_URL
            }
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(scheduled_ids, f, indent=2)
            time.sleep(2)
        else:
            print(f"   ⚠️ ERROR: {res_id} - {res_status}\n")
            break

    print("================================================================")
    print(f"📊 SUMMARY: {len(scheduled_ids)} / {len(GRIER_POSTS)} Mike Grier posts scheduled in Buffer.")
    print(f"Report: {report_file}")
    print("================================================================")

if __name__ == "__main__":
    main()
