# -*- coding: utf-8 -*-
"""
Autonomous Campaign Scheduler & Recovery Daemon
Campaign: Lewis Hamilton - 15th to 3rd Podium Comeback (Bahrain GP)
5 High-Impact Posts across Oct 4, Oct 5, Oct 6
Invariants:
- 100% Scheduled Queue (saveToDraft: False, mode: 'customScheduled')
- Zero Em Dashes
- Signed strictly 'Lornette'
- 100% Executive Keynote & Summit Bookings (lornettedaye.com/book)
- Custom Domain Production Assets (https://lornettedaye.com/campaigns/lewis-comeback/...)
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
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn
CDN_BASE = 'https://lornettedaye.com/campaigns/lewis-comeback'

posts_data = [
    {
        "id": 1,
        "day": 1,
        "date": "2026-10-04",
        "slot": "Evening (7:45 PM MDT)",
        "dueAt": "2026-10-05T01:45:00.000Z",
        "assetFile": "lewis-comeback-01.jpg",
        "assetUrl": f"{CDN_BASE}/lewis-comeback-01.jpg",
        "cta": "Executive Keynote Booking (lornettedaye.com/book)",
        "title": "Lewis Hamilton Comeback #1: Starting P15 is Not a Sentence",
        "text": """FROM 15TH TO THE PODIUM

When Lewis Hamilton lined up in fifteenth position on the Bahrain grid, commentators wrote off his evening. By the final lap, he was standing on the podium in Ferrari scarlet red.

In forty years of coaching Olympic athletes and advising executive boards, I have learned one fundamental truth about high-stakes competition: your starting position never dictates your destination. Amateurs panic when the opening conditions are unfavourable. They overcompensate, force risky maneuvers on cold tires, and destroy their race before the opening pit window. True champions treat a grid penalty or market deficit as an operational problem to be solved with relentless composure.

If your leadership team is facing an uphill quarter or unexpected disruption, do not accelerate blindly into traffic. Settle into your rhythm, manage your resources, and let your discipline dismantle the field one sector at a time.

With purpose,
Lornette

Equip your executive team with the championship resilience, strategic composure, and tactical poise needed to navigate high-stakes pressure.
Book Lornette Daye for your corporate keynote or leadership summit: https://lornettedaye.com/book

#LewisHamilton #ScuderiaFerrari #BahrainGP #ComebackDrive #OlympicMindset #ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong #CrisisManagement #StrategicPoise #PodiumMentality #F1"""
    },
    {
        "id": 2,
        "day": 1,
        "date": "2026-10-04",
        "slot": "Late Evening (9:30 PM MDT)",
        "dueAt": "2026-10-05T03:30:00.000Z",
        "assetFile": "lewis-comeback-02.jpg",
        "assetUrl": f"{CDN_BASE}/lewis-comeback-02.jpg",
        "cta": "Executive Keynote Booking (lornettedaye.com/book)",
        "title": "Lewis Hamilton Comeback #2: Stillness at 300 KM/H",
        "text": """STILLNESS AT THREE HUNDRED KILOMETERS PER HOUR

Inside a Formula 1 cockpit, the human heart rate exceeds one hundred and seventy beats per minute while experiencing lateral loads above five Gs.

What separated Lewis Hamilton's drive through the midfield from ordinary drivers was cognitive stillness. When you are fighting through the dirty air of four rival cars in Bahrain, every instinct screams to hurry. Yet racing physics rewards the calmest hands. Smooth steering inputs, millimeter throttle modulation, and cold-blooded patience on the brakes. In business, panic is contagious, but emotional composure is transformative.

When market volatility accelerates and your competitors begin making frantic moves, your greatest competitive advantage is the deliberate stillness of your leadership.

Stay focused,
Lornette

Bring Olympic-caliber mental discipline, crisis composure, and championship execution to your next executive retreat or annual conference.
Book Lornette Daye for your keynote: https://lornettedaye.com/book

#LewisHamilton #ScuderiaFerrari #BahrainGP #EmotionalPoise #OlympicMindset #ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong #CorporateCulture #DecisiveCalm #F1"""
    },
    {
        "id": 3,
        "day": 2,
        "date": "2026-10-05",
        "slot": "Morning Prime (10:15 AM MDT)",
        "dueAt": "2026-10-05T16:15:00.000Z",
        "assetFile": "lewis-comeback-03.jpg",
        "assetUrl": f"{CDN_BASE}/lewis-comeback-03.jpg",
        "cta": "Executive Keynote Booking (lornettedaye.com/book)",
        "title": "Lewis Hamilton Comeback #3: Protecting Assets Under Pressure",
        "text": """PROTECTING YOUR ASSETS UNDER PRESSURE

A forty-lap comeback cannot be won by burning through your rubber in five aggressive laps.

Lewis Hamilton’s march from fifteenth to third was a masterclass in tire degradation management. While younger drivers overheated their Pirelli compounds chasing immediate lap times, Hamilton nursed his rubber through the high-load corners of Bahrain, preserving grip for the critical crossover window. He understood that sustainable velocity is built on disciplined stewardship. In corporate leadership, burning out your top talent or burning through cash reserves for a short-term quarterly metric is a rookie mistake.

True championship culture balances aggressive ambition with the disciplined preservation of human and operational capital.

Keep building,
Lornette

Help your organization build sustainable high performance, prevent burnout, and execute long-term strategic turnarounds.
Book Lornette Daye for your keynote: https://lornettedaye.com/book

#LewisHamilton #ScuderiaFerrari #BahrainGP #ResourceManagement #OlympicMindset #ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong #SustainableExcellence #StrategicGrowth #F1"""
    },
    {
        "id": 4,
        "day": 2,
        "date": "2026-10-05",
        "slot": "Afternoon Prime (1:15 PM MDT)",
        "dueAt": "2026-10-05T19:15:00.000Z",
        "assetFile": "lewis-comeback-04.jpg",
        "assetUrl": f"{CDN_BASE}/lewis-comeback-04.jpg",
        "cta": "Executive Keynote Booking (lornettedaye.com/book)",
        "title": "Lewis Hamilton Comeback #4: The Discipline of Pit-Wall Communication",
        "text": """THE DISCIPLINE OF PIT-WALL COMMUNICATION

When you are executing an aggressive undercut strategy, one second of hesitation on the team radio destroys twenty laps of hard work.

During Hamilton's ascent through the field, the radio exchange between driver and race engineer was stripped of all emotional noise. No panic. No debate about past mistakes. Only telemetry, delta times, and decisive tactical commands. As an Olympic coach, I have seen teams fall apart under pressure not because of a lack of skill, but because their communication channels became congested with anxiety and second-guessing.

If you want your leadership team to navigate rapid market pivots, strip away administrative friction and establish concise, trust-based communication protocols.

In your corner,
Lornette

Transform how your leadership teams communicate, collaborate, and execute when stakes are highest and margins are razor thin.
Book Lornette Daye for your keynote: https://lornettedaye.com/book

#LewisHamilton #ScuderiaFerrari #BahrainGP #Teamwork #OlympicMindset #ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong #ClearCommunication #OrganizationalTrust #F1"""
    },
    {
        "id": 5,
        "day": 3,
        "date": "2026-10-06",
        "slot": "Morning Prime (10:15 AM MDT)",
        "dueAt": "2026-10-06T16:15:00.000Z",
        "assetFile": "lewis-comeback-05.jpg",
        "assetUrl": f"{CDN_BASE}/lewis-comeback-05.jpg",
        "cta": "Executive Keynote Booking (lornettedaye.com/book)",
        "title": "Lewis Hamilton Comeback #5: Silverware is Forged in Adversity",
        "text": """SILVERWARE IS FORGED IN ADVERSITY

Standing on the podium holding the Bahrain trophy in red Ferrari colors was not just a celebration of a third-place finish. It was proof of concept for an entire career built on resilience.

Lewis Hamilton did not need an easy starting grid to remind the world why he is a seven-time world champion. Adversity reveals the difference between those who merely look the part when conditions are perfect and those who possess an unbreakable competitive core. Over four decades of coaching elite athletes, I have witnessed countless careers derailed by unexpected setbacks. The few who leave a lasting legacy are those who look adversity directly in the eye and use it as fuel.

Whatever deficit your organization is confronting today, remember this: the greatest stories in sport and business are never about smooth pole positions. They are about the grit it takes to climb from the back of the grid to the podium.

With conviction,
Lornette

Inspire your entire organization with world-class stories of athletic resilience, championship culture, and legendary executive leadership.
Book Lornette Daye for your keynote: https://lornettedaye.com/book

#LewisHamilton #ScuderiaFerrari #BahrainGP #Resilience #OlympicMindset #ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong #LegacyBuilding #AdversityToAdvantage #F1"""
    }
]

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
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

def schedule_posts(catchup_mode=False):
    report_path = "scripts/lewis-comeback-scheduled-report.json"
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    graphql_url = "https://api.buffer.com"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    ctx = ssl._create_unverified_context()

    print(f"=== LEWIS HAMILTON COMEBACK SCHEDULER (5 POSTS) ===")
    print(f"Target Channel ID: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Buffer Mode: Scheduled Queue (saveToDraft: False, mode: 'customScheduled')")
    print(f"Currently scheduled: {len(results)}/5\n")

    for i, p in enumerate(posts_data, 1):
        p_id = p["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{i}/5] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        retries = 0
        while retries < 5:
            print(f"\n[{i}/5] Scheduling Post #{p['id']} ({p['slot']}) - Due: {p['dueAt']}...")
            print(f"  Asset: {p['assetUrl']}")
            print(f"  CTA Focus: {p['cta']}")

            payload = {
                "query": mutation,
                "variables": {
                    "input": {
                        "channelId": CHANNEL_ID,
                        "text": p["text"],
                        "schedulingType": "automatic",
                        "mode": "customScheduled",
                        "dueAt": p["dueAt"],
                        "saveToDraft": False,
                        "needsApproval": False,
                        "assets": [
                            {
                                "image": {
                                    "url": p["assetUrl"]
                                }
                            }
                        ]
                    }
                }
            }

            req = urllib.request.Request(graphql_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    errors = res_data.get("errors")
                    if errors:
                        err_msg = errors[0].get("message", "GraphQL error")
                        print(f"  >>> GRAPHQL ERROR: {err_msg}")
                        p["status"] = "failed"
                        p["error"] = err_msg
                        results[p_id] = p
                        if "RATE_LIMIT" in err_msg or "Too many requests" in err_msg:
                            print("  [RATE LIMIT] 24h Quota reached. Stopping batch for autonomous timer resumption.")
                            sorted_list = sorted(results.values(), key=lambda x: x.get("id", 0))
                            with open(report_path, "w", encoding="utf-8") as rf:
                                json.dump(sorted_list, rf, indent=2, ensure_ascii=False)
                            return False
                        break
                    else:
                        create_res = res_data.get("data", {}).get("createPost", {})
                        if "post" in create_res and create_res["post"].get("id"):
                            post_id = create_res["post"]["id"]
                            st = create_res["post"].get("status")
                            due = create_res["post"].get("dueAt")
                            p["status"] = st
                            p["postId"] = post_id
                            p["dueAt"] = due
                            print(f"  >>> SUCCESS: Post ID: {post_id}")
                            results[p_id] = p
                            sorted_list = sorted(results.values(), key=lambda x: x.get("id", 0))
                            with open(report_path, "w", encoding="utf-8") as rf:
                                json.dump(sorted_list, rf, indent=2, ensure_ascii=False)
                            break
                        else:
                            err_msg = create_res.get("message", "Unknown error")
                            print(f"  >>> ERROR: {err_msg}")
                            p["status"] = "failed"
                            p["error"] = err_msg
                            results[p_id] = p
                            break
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    print(f"  [RATE LIMIT] HTTP 429 encountered.")
                    sorted_list = sorted(results.values(), key=lambda x: x.get("id", 0))
                    with open(report_path, "w", encoding="utf-8") as rf:
                        json.dump(sorted_list, rf, indent=2, ensure_ascii=False)
                    return False
                err_body = he.read().decode("utf-8", errors="replace")
                print(f"  >>> HTTP ERROR {he.code}: {err_body}")
                p["status"] = "failed"
                p["error"] = f"HTTP {he.code}: {err_body}"
                results[p_id] = p
                break
            except Exception as e:
                print(f"  >>> NETWORK ERROR: {e}")
                p["status"] = "failed"
                p["error"] = str(e)
                results[p_id] = p
                retries += 1
                time.sleep(3)

        time.sleep(2)

    sorted_list = sorted(results.values(), key=lambda x: x.get("id", 0))
    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump(sorted_list, rf, indent=2, ensure_ascii=False)
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"] and r.get("postId"))
    print(f"\nExecution complete. Saved {success_count}/5 successfully to {report_path}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    is_catchup = "--catchup" in sys.argv
    schedule_posts(catchup_mode=is_catchup)
