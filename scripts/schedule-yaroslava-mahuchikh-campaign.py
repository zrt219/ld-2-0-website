# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 9: YAROSLAVA MAHUCHIKH - WORLD RECORD HIGH JUMP & POISE (8 Posts)
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
        "slot": "Monday (05:45 PM MDT)",
        "dueAt": "2026-10-26T23:45:00.000Z",
        "assetFile": "yaroslava-mahuchikh-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE BAR KEEPS MOVING. SO DOES SHE. 🇺🇦🥇\n\nYaroslava Mahuchikh: Olympic Champion. World Record Holder. 2.10 Meters.\n\nFor thirty-seven years, Stefka Kostadinova's legendary women's high jump world record of 2.09 meters stood as an unreachable summit in track and field. Experts claimed human biomechanics had met their limit. Then, on a sunlit afternoon in Paris, twenty-two-year-old Yaroslava Mahuchikh cleared 2.10 meters with millimeter perfection.\n\nIn four decades coaching Olympic athletes, I know that human limits exist only until someone with extraordinary technical discipline and emotional poise dares to raise the bar.\n\nLeaders: What 'impossible' ceiling in your field are you ready to shatter?\n\n👉 Discover how world-class competitors break barriers and finish strong. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#YaroslavaMahuchikh #WorldRecord210 #HighJumpQueen #OlympicChampion #FinishStrong #UkraineStrong #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Tuesday (08:30 AM MDT)",
        "dueAt": "2026-10-27T14:30:00.000Z",
        "assetFile": "yaroslava-mahuchikh-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "SLEEPING BETWEEN JUMPS: THE ULTIMATE LESSON IN ATHLETIC RECOVERY. 🛌🧘‍♀️\n\nWhile rivals pace nervously, bite their nails, and burn vital adrenaline, Yaroslava climbs into a green sleeping bag.\n\nShe lies flat on her back next to the high jump mat, puts a jacket over her eyes, and sleeps between competition heights. That is not theatrical indifference. It is world-class autonomic nervous system regulation. She brings her heart rate down to resting levels, conserves energy, and wakes up only when the bar is raised.\n\nAthletes: Can you switch off competition stress between attempts to conserve your explosive power?\n\n👉 Master physiological regulation, visualization, and recovery routines. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#SleepingBagRoutine #HighJumpPoise #Mahuchikh #SurvivalSkillsForAthletes #ParasympatheticReset #OlympicCoach #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Tuesday (11:00 AM MDT)",
        "dueAt": "2026-10-27T17:00:00.000Z",
        "assetFile": "yaroslava-mahuchikh-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-03.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "JUMPING UNDER WAR: COMPETING WHEN YOUR HOMELAND IS UNDER FIRE. 🇺🇦🕊️\n\nCompeting on the world stage is hard. Competing while your family endures missile strikes in Dnipro is heroic.\n\nYaroslava Mahuchikh fled Russian artillery in a car, traveled three days across Europe, and won the World Indoor Championship within weeks. She jumps not for personal glory, but to remind the world of Ukraine's unbreakable spirit. When your purpose is bigger than personal vanity, pain transforms into fuel.\n\nReaders: What weight in your personal life can you transform into purposeful resolve today?\n\n👉 Find strength in times of crisis, renewed perspective, and hope in dark seasons. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#UkraineStrength #Mahuchikh #CourageUnderFire #SurvivingLife #PurposeOverFear #OlympicResilience #LornetteDaye"
    },
    {
        "id": 4,
        "slot": "Tuesday (01:15 PM MDT)",
        "dueAt": "2026-10-27T19:15:00.000Z",
        "assetFile": "yaroslava-mahuchikh-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-04.png",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": "GRACE UNDER PRESSURE: COMBINING ELEGANCE AND EXPLOSIVE FORCE. 🌟👟\n\nHigh jump is poetry combined with violent physics.\n\nThe approach run must build centripetal force along a precise curved arc. The plant foot must withstand five times body weight in ground reaction force. The back must arch into an effortless crescent over the bar. Yaroslava executes this terrifying kinetic collision with the smile and calm grace of a dancer.\n\nWomen in leadership often confront harsh environments. You do not need to mimic harshness to command respect. Poise and supreme technical competence are your greatest weapons.\n\nWomen: Are you leading with grounded poise and unshakeable mastery?\n\n👉 Build lasting confidence, emotional balance, and identity in high-pressure arenas. Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n#GraceUnderPressure #Yaroslava #WomenInSport #SurvivalSkillsForWomen #KineticPoetry #OlympicStandards #CoachLornette"
    },
    {
        "id": 5,
        "slot": "Tuesday (03:45 PM MDT)",
        "dueAt": "2026-10-27T21:45:00.000Z",
        "assetFile": "yaroslava-mahuchikh-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-05.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "PARIS GOLD: FULFILLING DESTINY ON THE WORLD'S GREATEST STAGE. 🥇🇫🇷\n\nOlympic gold is the dream of millions; it is claimed only by those whose nerve remains ironclad when the bar is at 2.00 meters.\n\nIn the Stade de France, in front of eighty thousand roaring fans, Yaroslava Mahuchikh cleared the winning height on her first attempt. First-attempt clearances break the psychological will of your competitors. When you execute cleanly on the first try, you impose insurmountable pressure on everyone else.\n\nLeaders: Is your team prepared to deliver on the first attempt when the championship is on the line?\n\n👉 Master the habits of Olympic champions who execute flawlessly when it matters most. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#OlympicGold #Paris2024 #Mahuchikh #FirstAttemptExecution #FinishStrong #OlympicMindset #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Tuesday (05:45 PM MDT)",
        "dueAt": "2026-10-27T23:45:00.000Z",
        "assetFile": "yaroslava-mahuchikh-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "THE ARCHITECTURE OF HIGH PERFORMANCE: ROUTINE OVER ADRENALINE. 📐🎯\n\nAmateurs rely on hype and adrenaline; Olympic champions rely on repeatable architecture.\n\nWatch Yaroslava's pre-jump ritual: four steps measured with a tape, two deep diaphragmatic breaths, a gentle tap of the spikes, visual mapping of the crossbar, and then the approach. She repeats that identical sequence whether jumping 1.90m in May or 2.10m for a world record. Consistency in routine produces consistency in execution.\n\nExecutives: Does your organization possess repeatable operational routines that function flawlessly under pressure?\n\n👉 Transform your leadership execution with Olympic routine frameworks. Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n#RoutineOverAdrenaline #HighPerformanceArchitecture #ExecutiveDiscipline #CoachLornette #OperationalMastery"
    },
    {
        "id": 7,
        "slot": "Wednesday (08:30 AM MDT)",
        "dueAt": "2026-10-28T14:30:00.000Z",
        "assetFile": "yaroslava-mahuchikh-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-07.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "FLIGHT MECHANICS: OVERCOMING THE FEAR OF GRAVITY. 🕊️⚡\n\nTo jump 2.10 meters, an athlete must throw her body backward over a thin fiberglass bar seven feet off the ground.\n\nAny hesitation in the final two strides kills horizontal speed and causes failure. You must run toward the bar with total commitment, trust your plant, and allow physics to launch you into the air. Faith in your preparation conquers the fear of falling.\n\nAthletes: Where in your competitive execution are you tapping the brakes right before takeoff?\n\n👉 Eliminate hesitation and build fearless competitive commitment. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#FearlessTakeoff #HighJumpMechanics #SurvivalSkillsForAthletes #CommitmentWins #OlympicCoach #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Wednesday (11:00 AM MDT)",
        "dueAt": "2026-10-28T17:00:00.000Z",
        "assetFile": "yaroslava-mahuchikh-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/yaroslava-mahuchikh/yaroslava-mahuchikh-08.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE SKY IS NOT THE LIMIT: INSPIRING A NATION'S TOMORROWS. 🇺🇦🌅\n\nYaroslava Mahuchikh's legacy will be measured not just in centimeters, but in the light she shone into a nation's dark night.\n\nShe proved that Ukrainian youth can face war, displacement, and grief, and still rise to the very top of human achievement. True champions lift more than themselves over the bar; they lift their people.\n\nSet your bar high. Honor your people. Finish strong.\n\n👉 Discover how to finish your race with purpose, courage, and lasting legacy. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#HigherBrighterFurther #YaroslavaMahuchikh #UkrainianPride #FinishStrong #OlympicLegacy #LornetteDaye #MasteryInAction"
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
    print("CAMPAIGN 9: YAROSLAVA MAHUCHIKH - WORLD RECORD HIGH JUMP & POISE (8 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "yaroslava-mahuchikh-scheduled-report.json")
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

        rate_limit_halt = False
        while True:
            print(f"\n[{idx}/{len(posts_data)}] Scheduling: Post #{p_id} ({post['slot']}) - {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                if wait_sec > 120:
                    print(f"  [RATE LIMIT] HTTP 429: Window locked for {wait_sec}s. Exiting for background scheduler.")
                    rate_limit_halt = True
                    break
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

        if rate_limit_halt:
            break

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/8 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
