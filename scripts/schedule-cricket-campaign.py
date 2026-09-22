# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 6: CRICKET - INTERNATIONAL HERITAGE & PRECISION (14 Posts)
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
        "slot": "Monday (03:45 PM MDT)",
        "dueAt": "2026-10-19T21:45:00.000Z",
        "assetFile": "cricket-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "SOMETIMES THE NEXT LEVEL IS ONE CONVERSATION AWAY. 🏏🏴󠁧󠁢󠁥󠁮󠁧󠁿\n\nA champion can still need a mentor. A captain can still be coached. A great athlete can still learn.\n\nWhen Harry Brook sat down with legendary English batsman Kevin Pietersen on the boundary wall at Lord's, he wasn't looking for swing analysis. He was seeking psychological insight into commanding the international stage. Greatness is never too proud to seek counsel from those who walked the path before them.\n\nIn four decades coaching Olympic champions, I have seen careers transformed by a single conversation with the right mentor.\n\nAthletes and leaders: Who is speaking wisdom into your preparation today?\n\n👉 Discover how humility and world-class mentorship unlock your true competitive ceiling. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#HarryBrook #KevinPietersen #EnglandCricket #MentorshipInSport #FinishStrong #OlympicMindset #CoachLornette"
    },
    {
        "id": 2,
        "slot": "Monday (05:45 PM MDT)",
        "dueAt": "2026-10-19T23:45:00.000Z",
        "assetFile": "cricket-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "NEVER BECOME TOO GOOD TO BE TAUGHT. 🧢📚\n\nThe moment an athlete believes they have arrived is the precise moment their decline begins.\n\nHarry Brook has established himself as one of the most destructive young batsmen in world cricket. Yet watch his practice sessions: he asks questions, listens intently to coaches, and analyzes deliveries with student curiosity. Ego closes the mind; coachability expands your capacity.\n\nAthletes: When was the last time you asked for critical feedback on your technique?\n\n👉 Build an enduring champion mindset that remains coachable in every season. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#Coachability #HarryBrook #CricketExcellence #SurvivalSkillsForAthletes #OlympicStandards #LifelongLearner #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Tuesday (08:30 AM MDT)",
        "dueAt": "2026-10-20T14:30:00.000Z",
        "assetFile": "cricket-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "BETTER PEOPLE BUILD BRIGHTER PLAYERS: THE ETHOS OF TEST CRICKET. 🏛️☀️\n\nTest cricket spans five days in the blazing sun. It tests human patience, dignity, and moral stamina.\n\nIn our performance framework, athletic development is never separate from character development. When an athlete learns emotional regulation, respectful presence, and quiet resilience, their on-field performance becomes steady, reliable, and unbreakable under immense match pressure.\n\nExecutives: Are you investing in technical training alone, or building the character foundation of your workforce?\n\n👉 Elevate your corporate culture with Olympic coaching that builds high-integrity, high-execution teams. Book Lornette Daye: lornettedaye.com/speaking\n\n#BetterPeopleBetterPlayers #TestCricket #ExecutiveCulture #IntegrityUnderPressure #CoachLornette #LeadershipDevelopment"
    },
    {
        "id": 4,
        "slot": "Tuesday (11:00 AM MDT)",
        "dueAt": "2026-10-20T17:00:00.000Z",
        "assetFile": "cricket-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-04.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "DISCIPLINE. CONVERSATION. PROGRESS. A BRIGHTER TOMORROW. 🌅🏏\n\nSmall conversations held in quiet corners often yield the greatest competitive breakthroughs.\n\nWatching the masters of cricket exchange insights on the boundary teaches us that connection is an essential ingredient of performance. We are not meant to battle through demanding seasons in isolation. Opening up to a trusted voice can illuminate the exact adjustment you need to make.\n\nReaders: Is there an area of life where you need to reach out and seek guidance instead of struggling alone?\n\n👉 Rebuild confidence, find encouragement, and gain fresh perspective in hard chapters. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#DisciplineAndProgress #SurvivingLife #ConnectionInSport #CricketWisdom #OlympicCoach #HopeAndPerspective #LornetteDaye"
    },
    {
        "id": 5,
        "slot": "Tuesday (01:15 PM MDT)",
        "dueAt": "2026-10-20T19:15:00.000Z",
        "assetFile": "cricket-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-05.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "114 NOT OUT OFF 49 BALLS: EXPLOSIVE IMPACT BORN IN PATIENT STUDY. ⚡🏏\n\nHarry Brook exploded against Sri Lanka with a breathtaking century off just forty-nine deliveries. Spectators saw fireworks; coaches saw hours of meticulous video study, weight-shift analysis, and tactical courage. Violent speed on the field is always born from deep clarity in the mind.\n\nWhen preparation removes doubt, execution becomes ferocious and free.\n\nLeaders: Is your team prepared to capitalize with total conviction when opportunity opens up?\n\n👉 Master the habits of elite finishers who seize the moment without hesitation. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#HarryBrook #114NotOut #ExplosiveBatting #FinishStrong #CricketHighlights #PreparationIsEverything #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Tuesday (03:45 PM MDT)",
        "dueAt": "2026-10-20T21:45:00.000Z",
        "assetFile": "cricket-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-06.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "TALENT OPENS DOORS. COACHABILITY KEEPS THEM OPEN. 🚪🔑\n\nNatural hand-eye coordination will earn an athlete an international debut. Only coachability will keep them in the international lineup for a decade.\n\nOpposing bowlers adjust their fields and line of attack after every single innings. If a batsman is stubborn and unwilling to tweak their stance or trigger movements, international competition will expose them ruthlessly. Adaptability is survival.\n\nAthletes: Are you willing to dismantle a comfortable habit to achieve a higher standard?\n\n👉 Develop mental adaptability, tactical poise, and focus under pressure. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#CoachabilityWins #CricketTactics #SurvivalSkillsForAthletes #OlympicMindset #AdaptOrDecline #LornetteDaye"
    },
    {
        "id": 7,
        "slot": "Tuesday (05:45 PM MDT)",
        "dueAt": "2026-10-20T23:45:00.000Z",
        "assetFile": "cricket-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-07.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "YOUNG TALENT. BRIGHTER TOMORROWS: NAVIGATING SUDDEN ACCLAIM. 🌟🏏\n\nHandling failure is hard; handling overnight acclaim without losing your head is even harder.\n\nWhen a young player scores record-breaking hundreds, media praise and lucrative sponsorship contracts arrive instantly. The challenge for young men is keeping their circle grounded, their routines sacred, and their focus locked on the game. Do not let the noise outside enter your preparation sanctuary.\n\nMen: How are you guarding your personal routines against the distractions of external attention?\n\n👉 Build steady habits, emotional discipline, and balanced perspective through seasons of growth. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #GroundedLeadership #HandlingSuccess #CricketEngland #MenWhoLead #CoachLornette"
    },
    {
        "id": 8,
        "slot": "Wednesday (08:30 AM MDT)",
        "dueAt": "2026-10-21T14:30:00.000Z",
        "assetFile": "cricket-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-08.png",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": "18 HUNDREDS. 18 HUNDREDS. ONE NEW STANDARD. 🇿🇦🇮🇳👑\n\nWhen women raise the bar, the entire sporting world moves forward.\n\nLaura Wolvaardt of South Africa and Smriti Mandhana of India: two masterclasses in batting elegance and power. Wolvaardt drawing level with Mandhana for the most international hundreds in women's cricket history. Two distinct nations, two extraordinary batting journeys, united by an unyielding commitment to world-class precision.\n\nIn Olympic athletics, we celebrate pioneers who do not simply break records; they expand what future generations believe is possible.\n\nWomen: What boundary in your industry are you tearing down through your daily excellence?\n\n👉 Build unshakable confidence, identity, and resilience across every stage of your journey. Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n#LauraWolvaardt #SmritiMandhana #WomensCricket #18Hundreds #SurvivalSkillsForWomen #OlympicStandard #GlobalExcellence #LornetteDaye"
    },
    {
        "id": 9,
        "slot": "Wednesday (11:00 AM MDT)",
        "dueAt": "2026-10-21T17:00:00.000Z",
        "assetFile": "cricket-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-09.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE BEAUTY OF THE COVER DRIVE: TECHNICAL PURITY UNDER PRESSURE. 🏏✨\n\nFew sights in global sport rival the cover drive of Laura Wolvaardt or Smriti Mandhana.\n\nHigh elbow, head balanced directly over the ball, smooth follow-through, and effortless placement through the covers. That purity of stroke play is not accidental. It is the mathematical reward of tens of thousands of throwdowns in batting nets from Potchefstroom to Mumbai. Technical perfection delivers its own protection under pressure.\n\nWhen your technique is sound, you do not need frantic effort. You let the ball meet the sweet spot.\n\nProfessionals: Are you polishing the fundamentals of your craft until they shine effortlessly?\n\n👉 Master the discipline of technical excellence and learn how to finish strong. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#CoverDrive #TechnicalPurity #SmritiMandhana #LauraWolvaardt #FinishStrong #OlympicDiscipline #LornetteDaye"
    },
    {
        "id": 10,
        "slot": "Wednesday (01:15 PM MDT)",
        "dueAt": "2026-10-21T19:15:00.000Z",
        "assetFile": "cricket-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "GLOBAL EXPANSION: WOMEN'S SPORT REWRITING ECONOMIC REALITY. 🌍📈\n\nThe explosion of the Women's Premier League (WPL) and international women's cricket is an economic revolution.\n\nRecord television viewership, sold-out stadiums across India, and historic commercial partnerships. Athletes like Mandhana and Wolvaardt are proving that when you deliver elite athletic performance, global audiences and corporate capital will respond in massive numbers.\n\nExecutive leadership teams that champion women's excellence build stronger, more resilient global organizations.\n\nExecutives: Are you investing in the transformative power of women's leadership in your sector?\n\n👉 Inspire your executive organization with high-performance keynote strategies from an Olympic champion coach. Book Lornette Daye: lornettedaye.com/speaking\n\n#WomensSportEconomy #WPL #GlobalLeadership #ExecutiveStrategy #CoachLornette #EconomicEmpowerment"
    },
    {
        "id": 11,
        "slot": "Wednesday (03:45 PM MDT)",
        "dueAt": "2026-10-21T21:45:00.000Z",
        "assetFile": "cricket-11.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-11.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "EXCELLENCE HAS NO BORDERS: FROM SOUTH AFRICA TO INDIA. 🇿🇦🇮🇳\n\nSport is the universal bridge that connects diverse cultures through shared respect.\n\nDespite different backgrounds, different pitches, and different languages, Laura Wolvaardt and Smriti Mandhana share the same heartbeat: the relentless pursuit of mastery with a bat in hand. When opponents respect each other's work, competition elevates everyone.\n\nReaders: How can you build bridges of mutual respect with colleagues across different backgrounds today?\n\n👉 Discover encouragement, renewed hope, and perspective for navigating life with grace. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#ExcellenceHasNoBorders #CricketUnites #SurvivingLife #MutualRespect #OlympicSpirit #LornetteDaye"
    },
    {
        "id": 12,
        "slot": "Wednesday (05:45 PM MDT)",
        "dueAt": "2026-10-21T23:45:00.000Z",
        "assetFile": "cricket-12.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-12.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "BATTING THROUGH THE NERVOUS NINETIES: MENTAL POISE AT THE THRESHOLD. 🎯🏏\n\nEvery cricketer knows the psychological terror of batting on ninety-five.\n\nYour century is five runs away. The stadium is on its feet. Your pulse quickens. This is where ordinary players play a reckless shot and throw away hours of disciplined labor. To reach eighteen international hundreds, you must treat ninety-nine with the exact same calm process as zero.\n\nAthletes: Can you maintain your emotional discipline when you are right on the verge of a breakthrough?\n\n👉 Learn how to regulate pressure and finish your achievements with champion calm. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#NervousNineties #CenturyMakers #MentalPoise #SurvivalSkillsForAthletes #OlympicMentalToughness #LornetteDaye"
    },
    {
        "id": 13,
        "slot": "Thursday (08:30 AM MDT)",
        "dueAt": "2026-10-22T14:30:00.000Z",
        "assetFile": "cricket-13.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-13.png",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": "MORE WOMEN. HIGHER POSSIBILITIES: INSPIRING A CONTINENT. 🌏👑\n\nWhen Smriti Mandhana drives through extra cover or Laura Wolvaardt cuts backward of point, millions of girls in Delhi, Cape Town, and beyond see proof that their ambitions are valid.\n\nVisibility is the catalyst of aspiration. When women see women excelling on global stages, the mental limits of what is possible vanish.\n\nWomen: Never underestimate the quiet impact your courage and competence have on those watching you from afar.\n\n👉 Step boldly into your purpose with practical tools for resilience and leadership. Read Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n#MoreWomenHigherPossibilities #WomensCricket #InspireTheNext #SurvivalSkillsForWomen #OlympicLegacy #CoachLornette"
    },
    {
        "id": 14,
        "slot": "Thursday (11:00 AM MDT)",
        "dueAt": "2026-10-22T17:00:00.000Z",
        "assetFile": "cricket-14.png",
        "assetUrl": "https://lornettedaye.com/campaigns/cricket/cricket-14.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE ENDURING HERITAGE OF CRICKET: FINISHING STRONG ACROSS INNINGS. 🏆🏏\n\nWhether it is Harry Brook's fearless stroke play or Wolvaardt and Mandhana rewriting the century record books, international cricket reminds us of a timeless truth: talent gets you into the stadium, but patience, humility, and disciplined preparation decide how you finish.\n\nStep up to your crease today with purpose. Respect the delivery. Trust your training. Finish strong.\n\n👉 Master the habits of elite athletes who turn pressure into enduring legacy. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#CricketHeritage #FinishStrong #GlobalAthletes #OlympicMindset #PlayYourBest #LornetteDaye #ExcellenceInSport"
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
    print("CAMPAIGN 6: CRICKET - INTERNATIONAL HERITAGE & PRECISION (14 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "cricket-scheduled-report.json")
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
    print(f"Summary: {success_count}/14 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
