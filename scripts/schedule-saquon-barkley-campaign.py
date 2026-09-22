# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 10: SAQUON BARKLEY - NFL POWER, RECOVERY & RESILIENCE (10 Posts)
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
        "slot": "Wednesday (01:15 PM MDT)",
        "dueAt": "2026-10-28T19:15:00.000Z",
        "assetFile": "saquon-barkley-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "WHAT DO YOU DO AFTER GREATNESS? SAQUON BARKLEY IN PHILADELPHIA. 🦅🏈\n\nThe work does not end at the top. A higher kind of greatness begins when you start fresh.\n\nAfter six seasons battling through injuries, franchise instability, and intense scrutiny in New York, Saquon Barkley arrived in Philadelphia with clear intent. In his opening games in midnight green, he exploded for three touchdowns, hurdled defenders backward, and established the Eagles as title contenders. He did not rest on his past reputation; he brought an elevated standard of workhorse excellence.\n\nIn four decades coaching Olympic champions, I remind athletes: greatness is not a trophy on your shelf. It is the standard of sweat you bring to today's practice.\n\nLeaders: When entering a new chapter, do you rely on your resume, or prove your value on day one?\n\n👉 Master the habits of elite performers who finish strong in every arena. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#SaquonBarkley #FlyEaglesFly #AfterGreatness #FinishStrong #WorkhorseDiscipline #OlympicMindset #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Wednesday (03:45 PM MDT)",
        "dueAt": "2026-10-28T21:45:00.000Z",
        "assetFile": "saquon-barkley-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE BACKWARD HURDLE: ATHLETIC AUDACITY BACKED BY PHYSICAL SCIENCE. 🦅⚡\n\nWhen Saquon Barkley leaped backward over an NFL cornerback in live combat, the sports world gasped.\n\nSpectators called it a miracle. Biomechanists called it an unprecedented display of quad force, hip flexion, and spatial proprioception. You cannot execute that maneuver without thousands of squats, plyometric box jumps, and unyielding trust in your knee ligaments. Audacity on the field is earned in the weight room.\n\nAthletes: Are you putting in the structural conditioning necessary to support creative brilliance under contact?\n\n👉 Build elite physical resilience, rotational power, and explosive balance. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#BackwardHurdle #Saquon #PhysicalGenius #SurvivalSkillsForAthletes #OlympicBiomechanics #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Wednesday (05:45 PM MDT)",
        "dueAt": "2026-10-28T23:45:00.000Z",
        "assetFile": "saquon-barkley-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-03.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "RECOVERING FROM THE TORN ACL: THE PSYCHOLOGY OF THE REBUILD. 🛡️🦵\n\nWhen Saquon's ACL tore on the turf at Soldier Field in 2020, critics declared his elite burst was gone forever.\n\nThe darkest hours of an athlete's life are spent in physical therapy clinics, relearning how to bend the knee, enduring scar-tissue breakdown, and fighting off feelings of obsolescence. Saquon embraced that lonely crucible. He rebuilt his body from the ground up and returned faster, stronger, and more durable than before.\n\nMen: When an unexpected injury or financial setback knocks you down, do you complain, or begin the quiet rebuild?\n\n👉 Build mental toughness, emotional resilience, and steady habits through seasons of physical repair. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#ACLRecovery #SaquonRebuild #PhysicalResilience #SurvivalSkillsForMen #MenWhoLead #OvercomingAdversity #CoachLornette"
    },
    {
        "id": 4,
        "slot": "Thursday (08:30 AM MDT)",
        "dueAt": "2026-10-29T14:30:00.000Z",
        "assetFile": "saquon-barkley-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-04.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE RUNNING BACK STANDARD: CONFRONTING THE POSITION DISRESPECT. 🏈💪\n\nModern NFL analytics claim running backs are disposable commodities that should not receive second contracts.\n\nSaquon Barkley rejected that narrative. He demonstrated that an elite running back who catches out of the backfield, protects in pass block, and punishes linebackers in the fourth quarter alters the entire geometry of an offense. When the industry devalues your role, the solution is not resentment; it is making yourself completely irreplaceable.\n\nProfessionals: Has your industry attempted to commoditize your expertise? How are you making yourself indispensable?\n\n👉 Learn how to rise above industry averages and finish what you started with undeniable impact. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#RunningBackValue #SaquonBarkley #IndispensableTalent #FinishStrong #OlympicStandards #LornetteDaye"
    },
    {
        "id": 5,
        "slot": "Thursday (11:00 AM MDT)",
        "dueAt": "2026-10-29T17:00:00.000Z",
        "assetFile": "saquon-barkley-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "THE EAGLES CULTURE: EXECUTING IN A FOOTBALL CITY THAT DEMANDS PERFECTION. 🔔🦅\n\nPhiladelphia is not a city for the faint of heart. The fans are knowledgeable, passionate, and relentlessly demanding.\n\nSaquon stepped into that passionate environment and embraced the standard immediately. He ran with violent purpose, celebrated with his offensive line, and spoke with authentic humility. When high-profile acquisitions honor the local community's passion, team chemistry explodes.\n\nExecutives: How well does your executive leadership integrate with the unique culture of your organization?\n\n👉 Build a culture of fierce accountability and high performance with Olympic keynote frameworks. Book Lornette Daye: lornettedaye.com/speaking\n\n#PhillyEagles #Saquon #HighExpectations #ExecutiveLeadership #TeamChemistry #CoachLornette"
    },
    {
        "id": 6,
        "slot": "Thursday (01:15 PM MDT)",
        "dueAt": "2026-10-29T19:15:00.000Z",
        "assetFile": "saquon-barkley-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-06.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "PEOPLE. PURPOSE. PERFORMANCE: A BRIGHTER TOMORROW BUILDS TODAY. 🌅🤝\n\nBeyond the sixty-yard touchdown runs and highlight clips, Saquon Barkley is a devoted father and philanthropist.\n\nHis Michael Ann & Saquon Barkley Hope Foundation empowers underprivileged youth with educational scholarships, athletic camps, and food security. He knows that scoring touchdowns without uplifting others is an empty triumph. Greatness is defined by how much light you leave in the lives of those around you.\n\nReaders: How are you using your personal success to uplift those who cannot repay you?\n\n👉 Find deep meaning, perspective, and joy through service to others. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#HopeFoundation #SaquonCares #PurposeLivesHigher #SurvivingLife #LegacyOfGiving #LornetteDaye"
    },
    {
        "id": 7,
        "slot": "Thursday (03:45 PM MDT)",
        "dueAt": "2026-10-29T21:45:00.000Z",
        "assetFile": "saquon-barkley-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-07.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE POWER OF BALANCE: STAYING UPRIGHT THROUGH THE COLLISION. ⚖️🏈\n\nSaquon's legendary thigh development is not for aesthetics; it is a human suspension system.\n\nWhen safeties dive at his ankles, his core activates, his base widens, and he absorbs the blow while maintaining forward momentum. Contact balance is the defining difference between a two-yard gain and an explosive fifty-yard breakaway.\n\nAthletes: Are you training your stabilization muscles to keep your balance when hits arrive off-center?\n\n👉 Develop elite balance, joint integrity, and contact recovery systems. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#ContactBalance #SaquonBarkley #RunningBackBiomechanics #SurvivalSkillsForAthletes #OlympicTraining #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Thursday (05:45 PM MDT)",
        "dueAt": "2026-10-29T23:45:00.000Z",
        "assetFile": "saquon-barkley-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-08.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "BETTING ON YOURSELF: CHOOSING THE CHALLENGE OVER THE COMFORTABLE. 🎲🦅\n\nStaying in familiar circumstances is safe, but it rarely produces personal transformation.\n\nLeaving New York for Philadelphia meant facing intense divisional rivalry, learning a new offensive scheme, and playing under immense championship pressure. Saquon bet on his health, his work ethic, and his ability to thrive in a competitive system. Bet on yourself when you know your preparation is real.\n\nMen: What bold decision have you been postponing because staying comfortable felt safer?\n\n👉 Rebuild confidence, clarify purpose, and step into decisive leadership. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#BetOnYourself #SaquonMove #DecisiveLeadership #SurvivalSkillsForMen #MenWhoLead #CoachLornette"
    },
    {
        "id": 9,
        "slot": "Friday (08:30 AM MDT)",
        "dueAt": "2026-10-30T14:30:00.000Z",
        "assetFile": "saquon-barkley-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-09.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "FOURTH QUARTER WEAR-DOWN: PUNISHING SECONDARIES IN THE DYING MINUTES. ⏱️🧱\n\nIn the first quarter, every defense is fast and energetic. By the fourth quarter, after tackling Saquon Barkley twenty times, defenders take wider angles, hesitate at the hole, and look to avoid contact. Great backs don't just gain yards; they break the defensive spirit.\n\nIn your professional battles, stay relentless through the early friction. The fourth quarter is where you pull away.\n\nLeaders: Is your team built to outlast competitors in the final quarter of the fiscal year?\n\n👉 Master the habits of elite athletes who conquer fatigue and finish strong. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#FourthQuarterFinish #SaquonBarkley #RelentlessPressure #FinishStrong #OlympicStandards #LornetteDaye"
    },
    {
        "id": 10,
        "slot": "Friday (11:00 AM MDT)",
        "dueAt": "2026-10-30T17:00:00.000Z",
        "assetFile": "saquon-barkley-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/saquon-barkley/saquon-barkley-10.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "FLY EAGLES FLY: THE QUEST FOR THE ULTIMATE PRIZE. 🏆🦅\n\nIndividual accolades mean nothing compared to lifting the Lombardi Trophy.\n\nSaquon Barkley's career has featured Pro Bowls, Offensive Rookie of the Year awards, and viral highlights. Yet what burns in his chest is the championship ring. He joined the Eagles to play for the title, knowing that championship glory is the only achievement that never tarnishes.\n\nKeep your eyes fixed on the ultimate prize. Honor the daily grind. Finish strong.\n\n👉 Discover the championship mindset that carries elite performers to the summit. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#FlyEaglesFly #SaquonBarkley #ChampionshipQuest #FinishStrong #OlympicGlory #LornetteDaye #MasteryInSport"
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
    print("CAMPAIGN 10: SAQUON BARKLEY - NFL POWER, RECOVERY & RESILIENCE (10 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "saquon-barkley-scheduled-report.json")
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
    print(f"Summary: {success_count}/10 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
