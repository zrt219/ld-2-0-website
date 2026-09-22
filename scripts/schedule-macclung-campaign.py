# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for Campaign 2: Mac McClung (11 Posts)
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
        "dueAt": "2026-10-14T19:15:00.000Z",
        "assetFile": "macclung-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "IF THE NBA WON'T GIVE YOU THE STAGE, EUROPE WILL. ✈️🏀\n\nNever let another person's limited perspective dictate the boundary of your career.\n\nMac McClung conquered every minor league challenge: two-time NBA G League MVP, three-time Slam Dunk Champion, and 31.8 points per game last season. Yet when the permanent NBA call didn't materialize, he didn't sulk on the bench or wait for an invitation. He crossed the Atlantic to Girona, Spain.\n\nIn four decades coaching Olympic athletes, I tell my champions that greatness always finds an arena. When one door remains stubbornly locked, a true competitor finds a wider map and builds a new kingdom.\n\nAthletes and professionals: Are you waiting for gatekeepers to validate you, or taking your talent where it is celebrated?\n\n👉 Discover how to push through gatekeepers and finish what you started with unshakeable resolve. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#MacMcClung #GironaBasquet #BiggerMap #FinishStrong #DefyingGravity #OlympicMindset #NoLimits #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Wednesday (03:45 PM MDT)",
        "dueAt": "2026-10-14T21:45:00.000Z",
        "assetFile": "macclung-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "WHEN ONE LEAGUE SAYS 'WAIT,' ANOTHER CAN SAY 'WELCOME.' 🇪🇸🔥\n\nOpportunity often speaks a different language.\n\nTo leave the comfort of American basketball for the rigorous physical and tactical environment of the Spanish ACB league requires supreme confidence. European basketball is disciplined, team-first, and unforgiving. Mac McClung didn't look at Girona as a step down; he saw it as an international platform to prove his complete game.\n\nAthletes who survive and thrive across changing landscapes are those who refuse to attach their self-worth to a single logo.\n\nAthletes: Can your skill and work ethic adapt when the environment demands a total reset?\n\n👉 Build focus, emotional adaptability, and champion confidence on any court in the world. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#MacMcClung #Adaptability #EuropeanHoops #SurvivalSkillsForAthletes #GlobalAthlete #OlympicStandards #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Wednesday (05:45 PM MDT)",
        "dueAt": "2026-10-14T23:45:00.000Z",
        "assetFile": "macclung-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-03.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "TWO-TIME G LEAGUE MVP: THE UNSPOKEN DISCIPLINE OF THE BUS LEAGUES. 🚌💪\n\nAnyone can shine when the private jet is waiting. Greatness is proven on commercial red-eyes and quiet gymnasiums.\n\nThe NBA G League is filled with hungry young men battling for twenty-second auditions. To dominate that league once is an achievement; to win Back-to-Back MVP honors requires an ironclad routine. Mac McClung treated every Tuesday night game in Sioux Falls or Osceola with the exact same professional gravity as an NBA Finals game.\n\nMen: When your current assignment feels beneath your ultimate potential, do you cut corners, or dominate the details?\n\n👉 Strengthen your daily habits, emotional stamina, and purpose during seasons of patient building. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #MacMcClung #GLeagueMVP #TheGrind #DisciplineOverMotivation #MenWhoLead #CoachLornette"
    },
    {
        "id": 4,
        "slot": "Thursday (08:30 AM MDT)",
        "dueAt": "2026-10-15T14:30:00.000Z",
        "assetFile": "macclung-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "DEFYING GRAVITY UNDER GLOBAL LIGHTS: THE ANATOMY OF FEARLESS FOCUS. ⚡🎯\n\nWhen millions of viewers tune in to watch you execute a leap over two seven-footers on live television, your heart rate cannot be racing.\n\nMac McClung's legendary Dunk Contest performances were not reckless improvisation. They were rehearsed until muscle memory conquered human fear. He walked onto the floor, smiled, breathed deeply, and executed flawlessly on his first attempt. That is Olympic-level emotional regulation.\n\nIn high-stakes corporate presentations, executives often freeze when the entire board is watching. Calm is not an accident; calm is the predictable result of exhaustive preparation.\n\nExecutives: Does your leadership team command high-pressure presentations with effortless poise?\n\n👉 Train your organization to execute under intense pressure with Olympic composure. Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n#SlamDunkContest #MacMcClung #PoiseUnderPressure #ExecutivePerformance #EmotionalRegulation #CoachLornette"
    },
    {
        "id": 5,
        "slot": "Thursday (11:00 AM MDT)",
        "dueAt": "2026-10-15T17:00:00.000Z",
        "assetFile": "macclung-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-05.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "SAME GAME. BIGGER HORIZONS. 🌍✨\n\nDo not let the boundary of your hometown define the horizon of your destiny.\n\nHailing from Gate City, Virginia, a town of under two thousand people, Mac McClung has already inspired millions. By taking his craft to Catalunya, he is proving that basketball is an international language. Catalan fans, European scouts, and global brands are watching. He chose expanding his horizons over shrinking his ambition.\n\nWhen your vision outgrows your current environment, you must have the courage to cross the ocean.\n\nLeaders: Where in your career are you clinging to familiar territory instead of claiming new ground?\n\n👉 Break through self-imposed borders and discover how to finish with legacy. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#MacMcClung #GateCityToGirona #BiggerHorizons #FinishStrong #GlobalAmbition #OlympicMindset #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Thursday (01:15 PM MDT)",
        "dueAt": "2026-10-15T19:15:00.000Z",
        "assetFile": "macclung-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-06.png",
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": "VIRAL HIGHLIGHTS DON'T SURVIVE SCOUTING REPORTS WITHOUT SUBSTANCE. 📹🛡️\n\nMillions of teenagers become viral sensations for ten seconds on social media. Almost all of them disappear by age twenty-two.\n\nMac McClung first caught global attention as a high school sensation in 2017. Nine years later, he is still playing professional basketball at the highest levels. He survived because he went to work on his defensive footwork, his pick-and-roll passing, and his three-point accuracy. He transformed from a social media highlight reel into a complete basketball technician.\n\nProfessionals: Are you relying on early reputation, or constantly upgrading your foundational skill set?\n\n👉 Transition from short-term survival into enduring professional mastery. Explore Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n#SubstanceOverHype #MacMcClung #SkillUpgrades #SurvivingToThriving #ProfessionalMastery #LornetteDaye"
    },
    {
        "id": 7,
        "slot": "Thursday (03:45 PM MDT)",
        "dueAt": "2026-10-15T21:45:00.000Z",
        "assetFile": "macclung-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-07.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "A HIGHER GAME ALWAYS AWAITS: PURSUING MASTERY OVER APPROVAL. 🏔️🏀\n\nThe moment you stop seeking external approval is the moment you unlock your authentic speed.\n\nThroughout his career, scouts warned Mac McClung that his height and wingspan would limit his basketball ceiling. Every metric on paper said he would plateau. But scouting reports cannot quantify a player's cardiovascular threshold or the sheer density of his competitive spirit. He out-worked the doubters every single summer.\n\nIn athletics as in life, your ceiling is not determined by external measurements. It is determined by the size of your motor.\n\nAthletes: Are you allowing someone else's evaluation to cap your daily effort?\n\n👉 Build an ironclad champion mindset and emotional poise that refuses to be limited. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#NoCeilings #MacMcClung #ChampionMindset #SurvivalSkillsForAthletes #OlympicCoaching #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Thursday (05:45 PM MDT)",
        "dueAt": "2026-10-15T23:45:00.000Z",
        "assetFile": "macclung-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "THE EUROPEAN CRUCIBLE: EXPANDING TACTICAL MATURITY. 🇪🇸🧠\n\nRaw athleticism wins games in high school; tactical maturity wins championships across the globe.\n\nCompeting in Spain's Liga ACB forces an American guard to master spacing, ball movement, and team defensive schemes. By choosing Girona, Mac McClung submitted himself to a coaching staff that demands tactical discipline on every possession. He is adding European basketball IQ to explosive American athleticism. That combination creates an unstoppable hybrid.\n\nExecutive teams that integrate diverse perspectives and international methodologies consistently outperform insular competitors.\n\nExecutives: Is your organization cross-pollinating ideas, or trapped in domestic echo chambers?\n\n👉 Elevate your executive perspective with Olympic-caliber coaching and global performance strategy. Book Lornette Daye: lornettedaye.com/speaking\n\n#GironaHoops #TacticalMaturity #GlobalStrategy #ExecutiveLeadership #CrossCulturalExcellence #CoachLornette"
    },
    {
        "id": 9,
        "slot": "Friday (08:30 AM MDT)",
        "dueAt": "2026-10-16T14:30:00.000Z",
        "assetFile": "macclung-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-09.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "31.8 PPG: WHEN PREPARATION MEETS UNAPOLOGETIC ATTACK. 🎯🔥\n\nAveraging over thirty points a game is not about taking sixty bad shots. It is about relentless offensive efficiency.\n\nMac McClung's scoring outbursts are built on rim pressure, foul drawing, transition bursts, and deep perimeter range. He attacks defensive gaps before they close, reading rotations in real time. He plays with the urgency of someone who knows every minute on the hardwood is sacred.\n\nWhen you step into your arena, do you play passively hoping not to make a mistake, or do you impose your preparation with decisive attack?\n\nLeaders: Attack your objectives with relentless precision and never settle for second best.\n\n👉 Discover how to channel intense focus into unstoppable execution. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#ScoringMastery #MacMcClung #OffensiveEfficiency #FinishStrong #OlympicMindset #DecisiveExecution #LornetteDaye"
    },
    {
        "id": 10,
        "slot": "Friday (11:00 AM MDT)",
        "dueAt": "2026-10-16T17:00:00.000Z",
        "assetFile": "macclung-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-10.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "WRITING YOUR OWN SCRIPT: WHEN REJECTION TURNS INTO REDIRECTION. 📖✨\n\nRejection is not a stop sign; it is a redirection toward a bigger purpose.\n\nHow many times has Mac McClung been waived, reassigned, or bypassed on draft night? Dozens. Yet you never hear bitterness in his postgame interviews. You never see him looking defeated. He smiles, hugs his teammates, and gets back in the gym at 6:00 AM. He understands that your emotional poise in the face of disappointment is the true test of your character.\n\nIf life has handed you an unexpected detour, do not despair. Trust the process and keep doing the work.\n\nReaders: What detour in your life can you reframe today as an unexpected doorway to growth?\n\n👉 Rebuild confidence, discover perspective, and find hope through seasons of transition. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#Redirection #MacMcClung #Resilience #SurvivingLife #TrustTheProcess #HopeAfterHardship #LornetteDaye"
    },
    {
        "id": 11,
        "slot": "Friday (01:15 PM MDT)",
        "dueAt": "2026-10-16T19:15:00.000Z",
        "assetFile": "macclung-11.png",
        "assetUrl": "https://lornettedaye.com/campaigns/macclung/macclung-11.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "A BRIGHTER CHAPTER AWAITS: THE UNWRITTEN FUTURE OF MAC McCLUNG. 🌅🏀\n\nThe journey of an elite athlete is rarely linear. It is a winding road paved with grit, faith, and relentless belief.\n\nAs Mac McClung laces up his sneakers for Basquet Girona, he carries the hopes of every underdog who was told they were too small, too unconventional, or outside the system's preferred mold. His story is not finished. It is just beginning.\n\nIn four decades coaching Canadian champions, I have learned one final law: Those who dare to bet on themselves, work without complaint, and keep their eyes fixed on excellence will always find their moment in the sun.\n\nBet on yourself. Put in the reps. Finish strong.\n\n👉 Master the habits of elite athletes who turn obstacles into lasting legacy. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#BasquetGirona #MacMcClung #BetOnYourself #FinishStrong #UnderdogMentality #OlympicExcellence #LornetteDaye"
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
    print("CAMPAIGN 2: MAC McCLUNG - DEFYING GRAVITY & DUNK CONTEST POISE (11 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "macclung-scheduled-report.json")
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
    print(f"Summary: {success_count}/11 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
