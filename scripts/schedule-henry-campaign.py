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

CDN_BASE = 'https://lornettedaye.com/campaigns/henry'

posts_data = [
    {
        "id": 1,
        "slot": "Monday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-05T18:30:00.000Z",
        "assetFile": "henry-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "KING HENRY: THE STANDARD OF WORKHORSE DISCIPLINE. 👑🏈\n\n"
            "When other runners wear down, true dominance begins.\n\n"
            "In modern professional football, running backs are told their career shelf life is three years. "
            "They are told 30 carries a game will break their body, and after age 28, decline is inevitable. "
            "Then you watch Derrick Henry, standing 6 foot 3 and 247 pounds, punishing defensive secondaries "
            "in the fourth quarter with the exact same violent burst he displayed on the opening snap.\n\n"
            "In four decades coaching Olympic champions, I have learned that human physical capacity is not dictated "
            "by league averages; it is dictated by the severity of your personal standard. When you out-condition "
            "the world, statistics bend to your will.\n\n"
            "Leaders: Are you accepting industry averages for your team, or establishing a standard of elite endurance?\n\n"
            "👉 Defy conventional limits and learn how to finish what you started with unstoppable momentum. "
            "Explore *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#DerrickHenry #KingHenry #WorkhorseDiscipline #NFLDominance #FinishStrong #PhysicalResilience #OlympicMindset #LornetteDaye #RunningBackRoyalty"
        ),
        "assetUrl": f"{CDN_BASE}/henry-01.png"
    },
    {
        "id": 2,
        "slot": "Tuesday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-06T18:30:00.000Z",
        "assetFile": "henry-02.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "CONFRONTING THE AGING CURVE WITH OBSESSIVE CONDITIONING. ⏳🛡️\n\n"
            "Longevity is never granted. It is engineered.\n\n"
            "Every offseason, while critics debate his workload and mileage, Derrick Henry retreats to the humidity of Florida. "
            "He sprints steep sand hills, pushes weighted sleds in silence, and subjects his frame to grueling mobility protocols. "
            "He does not negotiate with fatigue. He understands that if you want to extend your competitive prime, "
            "your recovery habits must be even more disciplined than your game-day execution.\n\n"
            "Men often ask how to maintain physical vitality and mental drive as professional and personal pressures mount. "
            "The answer is simple: you cannot let your daily foundation decay.\n\n"
            "Men & Leaders: What foundational discipline have you let slide that you need to reclaim this week?\n\n"
            "👉 Build steadier daily habits, emotional resilience, and physical balance through seasons of heavy demand. "
            "Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #DerrickHenry #LongevityInSport #OffseasonGrind #DefyingTheOdds #DisciplineOverMotivation #MenWhoLead #CoachLornette"
        ),
        "assetUrl": f"{CDN_BASE}/henry-02.png"
    },
    {
        "id": 3,
        "slot": "Wednesday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-07T18:30:00.000Z",
        "assetFile": "henry-03.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "THE ART OF THE STIFF-ARM: IMPOSING YOUR WILL WITH LEVERAGE. 💪💥\n\n"
            "Power without technique is merely reckless exertion.\n\n"
            "The iconic Derrick Henry stiff-arm is not simply brute muscle. It is a masterpiece of kinetic timing, "
            "shoulder drop, hip leverage, and psychological authority. He does not evade contact; he dictates the collision point. "
            "By establishing physical and mental dominance on the perimeter, he forces every defender to hesitate for a split second. "
            "In sports and business, hesitation is fatal.\n\n"
            "Athletes: When obstacles confront your path, do you shy away, or do you impose your preparation with decisive authority?\n\n"
            "👉 Build a champion mindset, focus under contact, and emotional poise on and off the field. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TheStiffArm #DerrickHenry #PhysicalLeverage #DecisiveAction #SurvivalSkillsForAthletes #ChampionMindset #HighPerformance #OlympicCoach #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-03.png"
    },
    {
        "id": 4,
        "slot": "Thursday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-08T18:30:00.000Z",
        "assetFile": "henry-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "FOURTH-QUARTER PUNISHMENT: WEARING OUT RESISTANCE. ⏱️🧱\n\n"
            "Championship games are decided when the body wants to surrender.\n\n"
            "In the first quarter, every defense is energized, swarming to the ball with fresh legs. "
            "By the fourth quarter, after tackling a 247-pound runaway locomotive twenty-five times, shoulders ache, "
            "pursuit angles widen, and defensive willpower fractures. Derrick Henry thrives on that war of attrition. "
            "He breaks opponents not with flashy trickery, but with cumulative, relentless pressure.\n\n"
            "In corporate competition, true differentiation is not about a flashy opening launch. "
            "It is about whether your operational execution can sustain the grueling grind when competitors burn out.\n\n"
            "Executives: Is your organization built for flash, or built for fourth-quarter endurance?\n\n"
            "👉 Train your leadership team to command high-pressure arenas with Olympic stamina and calm. "
            "Book Coach Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n"
            "#FourthQuarterMindset #WarOfAttrition #DerrickHenry #RelentlessPressure #ExecutiveStamina #CorporateEndurance #OlympicStandards #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-04.png"
    },
    {
        "id": 5,
        "slot": "Friday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-09T18:30:00.000Z",
        "assetFile": "henry-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "HUMILITY IN THE CROWN: RESPECTING THE TRENCHES. 🛡️🤝\n\n"
            "A king never forgets who cleared the pathway.\n\n"
            "Whenever Derrick Henry crosses the goal line or reaches 2,000 yards, the first thing he does is turn around "
            "and celebrate the five offensive linemen who dug their cleats into the dirt. "
            "He understands that every rushing title was purchased with broken fingers, bloodied jerseys, and uncredited sweat "
            "by teammates who never see their names on the fantasy football ticker.\n\n"
            "The greatest leaders never absorb credit for individual glory. They redirect honor downward to the front lines "
            "where the real work takes place every single day.\n\n"
            "Leaders: How are you recognizing and elevating the unheralded frontline workers in your organization today?\n\n"
            "👉 Cultivate selfless leadership, loyalty, and powerhouse team cultures. "
            "Inquire for leadership keynotes: lornettedaye.com/speaking\n\n"
            "#InTheTrenches #OffensiveLine #DerrickHenry #HumilityInLeadership #TeamCulture #FrontlineAppreciation #OlympicCoach #LornetteDaye #Speaker"
        ),
        "assetUrl": f"{CDN_BASE}/henry-05.png"
    },
    {
        "id": 6,
        "slot": "Saturday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-10T18:30:00.000Z",
        "assetFile": "henry-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "SPEED AT 250 POUNDS: THE PARADOX OF POWER ATHLETICISM. ⚡️🦏\n\n"
            "Mastering fast-twitch mechanics under a heavy frame.\n\n"
            "People often associate size with sluggishness. Yet Derrick Henry clocked over 21.8 miles per hour in the open field, "
            "faster than many wide receivers fifty pounds lighter than him. "
            "That extraordinary velocity is the result of surgical sprint mechanics: vertical knee lift, dorsiflexion, "
            "and posture discipline drilled thousands of times under high resistance.\n\n"
            "Never assume that because your organization is large, you cannot move with agile speed. "
            "Power and agility can coexist when systems are disciplined and waste is eliminated.\n\n"
            "Athletes: Are you training for raw bulk, or dynamic, functional speed?\n\n"
            "👉 Optimize your physical mechanics, mental clarity, and athletic performance. "
            "Get *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SprintMechanics #PowerAndSpeed #DerrickHenry #TopEndSpeed #SurvivalSkillsForAthletes #AthleticDevelopment #FunctionalAgility #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-06.png"
    },
    {
        "id": 7,
        "slot": "Sunday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-11T18:30:00.000Z",
        "assetFile": "henry-07.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE BALTIMORE CHAPTER: REIGNITING THE FIRE IN PURPLE. 🟣🔥\n\n"
            "New chapters demand fresh hunger, not resting on previous laurels.\n\n"
            "After a legendary career in Tennessee, many veterans would have rested on their resume, "
            "accepted a reduced role, or chased an easy paycheck. Instead, Derrick Henry stepped into Baltimore "
            "with the ferocious intensity of an undrafted rookie trying to make the final roster cut. "
            "He embraced new blocking schemes, integrated seamlessly with Lamar Jackson, and raised the competitive temperature of the entire building.\n\n"
            "Greatness is not about past accolades; it is about bringing championship energy to whatever room you enter today.\n\n"
            "How do you approach new professional transitions: with the arrogance of past success or the hunger of day one?\n\n"
            "👉 Rise above transitions and finish every chapter of life with purpose. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BaltimoreRavens #DerrickHenry #NewChapters #DayOneHunger #FinishStrong #VeteranLeadership #OlympicStandards #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-07.png"
    },
    {
        "id": 8,
        "slot": "Monday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-12T18:30:00.000Z",
        "assetFile": "henry-08.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "THE UNSEEN MILES: OFFSEASON HILL SPRINTS IN FLORIDA. 🏃‍♂️🌅\n\n"
            "True greatness is purchased when the stadium is completely empty.\n\n"
            "Look at the grit etched into this image. No fans. No broadcast commentators. No social media praise. "
            "Just 95-degree Florida sun, a steep grassy incline, and a champion forcing himself up the slope until his lungs burn. "
            "You cannot replicate that level of inner drive through external pressure. It must be born from a personal covenant with excellence.\n\n"
            "When life tests you under pressure, you do not rise to the occasion; you sink to the level of your training.\n\n"
            "Men & Leaders: What personal covenant are you keeping with yourself in private to ensure your public success?\n\n"
            "👉 Strengthen your inner foundation, self-discipline, and purpose. "
            "Explore *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HillSprints #UnseenHours #DerrickHenry #InnerDrive #PersonalCovenant #SurvivalSkillsForMen #OlympicDiscipline #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-08.png"
    },
    {
        "id": 9,
        "slot": "Tuesday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-13T18:30:00.000Z",
        "assetFile": "henry-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "BALL SECURITY THROUGH CONTACT: PROTECTING THE PRIZE. 🔒🏈\n\n"
            "Eliminating fatal turnovers when the world is clawing at your hands.\n\n"
            "When Derrick Henry takes a handoff, eleven defenders attack with one primary objective: strip the football. "
            "Yet his career fumble rate is among the lowest in modern history because his ball-security discipline is absolute: "
            "high and tight, two hands through traffic, locking down the nose of the football against his ribs.\n\n"
            "In leadership, you can generate immense momentum, but if you cannot protect core intellectual property, "
            "client trust, and financial stability, one careless turnover will wipe out five years of hard work.\n\n"
            "What critical asset in your business or life requires tighter security and vigilance today?\n\n"
            "👉 Protect your standards, focus, and competitive edge under pressure. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BallSecurity #ProtectThePrize #DerrickHenry #ZeroTurnovers #HighPerformanceDiscipline #SurvivalSkillsForAthletes #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/henry-09.png"
    },
    {
        "id": 10,
        "slot": "Wednesday Midday (12:30 PM MDT)",
        "dueAt": "2026-10-14T18:30:00.000Z",
        "assetFile": "henry-10.png",
        "cta": "Finish Strong Book & Leadership Summits (lornettedaye.com)",
        "text": (
            "FINISH STRONG: LEGENDS ARE BUILT ON RELENTLESS FORWARD LEAN. 🏆🔥\n\n"
            "It is not about how many times they hit you. It is about where you finish the run.\n\n"
            "Watch Derrick Henry in slow motion: even when three linebackers wrap his waist, his legs keep churning, "
            "driving forward for two more yards, three more yards, moving the chains on fourth down. "
            "That relentless forward lean is the definition of athletic resilience. You never allow external resistance "
            "to dictate your final resting spot.\n\n"
            "Whatever battle you are fighting today in business, health, or career, keep your legs moving. "
            "Maintain your forward lean. And always finish strong.\n\n"
            "👉 Discover how to build unshakeable perseverance and finish strong in every area of life. "
            "Explore Lornette Daye's official catalog and leadership keynotes: lornettedaye.com\n\n"
            "#FinishStrong #DerrickHenry #ForwardLean #RelentlessDrive #NeverStopChurning #OlympicMindset #CoachLornette #LornetteDaye #ExecutiveCoaching"
        ),
        "assetUrl": f"{CDN_BASE}/henry-10.png"
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
    print("CAMPAIGN 7: DERRICK HENRY - WORKHORSE DISCIPLINE & POWER DOMINANCE (10 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "henry-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                            results[item["id"]] = item
                elif isinstance(data, dict):
                    for item in data.get("results", []):
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
    print(f"Summary: {success_count}/10 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
