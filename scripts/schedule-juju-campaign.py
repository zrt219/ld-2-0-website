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

CDN_BASE = 'https://lornettedaye.com/campaigns/juju'

posts_data = [
    {
        "id": 1,
        "slot": "Saturday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-03T17:15:00.000Z",
        "assetFile": "juju-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE COMEBACK IS ALWAYS LOUDER THAN THE SETBACK. 🏀⚡️\n\n"
            "JuJu Watkins and the standard of athletic resilience.\n\n"
            "When an elite athlete faces injury, the public counts the weeks on the sideline. "
            "What they do not see is the mental battlefield in the athletic training room: "
            "the tedious isometric holds, the film sessions in empty arenas, and the relentless discipline required "
            "to rebuild belief when your body has betrayed you.\n\n"
            "In over 40 years coaching Olympic athletes and national champions, I have observed one undeniable truth: "
            "adversity does not build character. It reveals it. When JuJu Watkins steps back onto the hardwood for USC, "
            "she brings an unshakeable poise that only comes from conquering self-doubt in the dark.\n\n"
            "Athletes and Leaders: How do you respond when your momentum is abruptly stopped?\n\n"
            "👉 Rebuild resilience and discover the power to finish what you started. "
            "Explore *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#JuJuWatkins #USCWBB #WomensBasketball #ComebackSeason #FinishStrong #AthleticResilience #ChampionshipMindset #OlympicCoach #LornetteDaye #FightOn"
        ),
        "assetUrl": f"{CDN_BASE}/juju-01.png"
    },
    {
        "id": 2,
        "slot": "Monday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-05T17:15:00.000Z",
        "assetFile": "juju-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "CHAMPIONSHIP MINDSET IS FORGED IN SILENCE. 🏆🔥\n\n"
            "Greatness is never an accident of raw talent.\n\n"
            "When the spotlight shines on Galen Center, thousands roar for the step-back jumpers and electric transition buckets. "
            "Yet every clutch fourth-quarter performance was purchased months earlier during 6:00 AM conditioning drills when no cameras were rolling.\n\n"
            "JuJu Watkins represents the modern standard of athlete dedication: intense technical precision combined with fierce emotional composure. "
            "She understands that talent opens the door, but relentless preparation locks in the championship legacy.\n\n"
            "Coaches: Are you cultivating emotional stamina in your athletes, or merely focusing on tactical execution?\n\n"
            "👉 Build focus, discipline, and emotional poise on and off the court. "
            "Get *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForAthletes #JuJuWatkins #EliteFocus #ChampionshipDiscipline #USCBasketball #WomensSports #MentalToughness #CoachLornette #AthleteDevelopment"
        ),
        "assetUrl": f"{CDN_BASE}/juju-02.png"
    },
    {
        "id": 3,
        "slot": "Wednesday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-07T17:15:00.000Z",
        "assetFile": "juju-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "PRESSURE IS A PRIVILEGE EARNED BY THE PREPARED. 🎯✨\n\n"
            "Standing in the center of national expectations.\n\n"
            "When you break historic scoring records as a freshman, the entire sporting world watches your every step. "
            "Scouting reports double-team you. Opposing defenses build entire gameplans designed to disrupt your rhythm. "
            "How do you stay composed when you carry the weight of an entire program on your shoulders?\n\n"
            "You anchor yourself in execution, not expectation. JuJu Watkins demonstrates that true poise comes from narrowing your focus "
            "to the immediate possession in front of you. Your previous shot cannot hit your next shot. What matters is the standard right now.\n\n"
            "Executives: When national or corporate stakes reach their peak, how does your executive team preserve operational clarity?\n\n"
            "👉 Train your leadership team to command high-pressure arenas with Olympic calm. "
            "Book Coach Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n"
            "#PressureIsAPrivilege #JuJuWatkins #ExecutivePoise #LeadershipUnderPressure #HighPerformanceTeams #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/juju-03.png"
    },
    {
        "id": 4,
        "slot": "Friday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-09T17:15:00.000Z",
        "assetFile": "juju-04.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE TROJAN LEGACY: BUILDING DOMINANCE ONE POSSESSION AT A TIME. ✌️🏀\n\n"
            "Honoring history while authoring your own chapter.\n\n"
            "USC basketball has a storied heritage of iconic women who transformed the sport: Cheryl Miller, Cynthia Cooper, Lisa Leslie. "
            "Stepping onto that court wearing cardinal and gold is not just about playing basketball. It is about upholding a legacy of relentless excellence.\n\n"
            "JuJu Watkins does not run from that heritage. She embraces it, honoring the pioneers who built the foundation while carving out "
            "her own distinctive identity as a generational leader. That is how champions honor the past while building the future.\n\n"
            "What legacy are you building in your industry that will inspire those who come after you?\n\n"
            "👉 Discover how to transform vision into lasting legacy. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TrojanLegacy #USC #CherylMiller #JuJuWatkins #LegacyBuilding #WomenInSports #FinishStrong #OlympicStandards #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-04.png"
    },
    {
        "id": 5,
        "slot": "Sunday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-11T17:15:00.000Z",
        "assetFile": "juju-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "POISE UNDER FOURTH-QUARTER HEAT. ⏱️🧊\n\n"
            "When the clock ticks down and the margin is thin, leaders emerge.\n\n"
            "Anyone can execute when they are fresh and leading by twenty points. "
            "The real test of competitive excellence arrives in the final four minutes of a grueling contest, "
            "when your legs are heavy, the gym is deafening, and every decision carries championship consequences.\n\n"
            "JuJu Watkins thrives in those exact moments because her emotional regulation matches her physical skill. "
            "She slows the game down mentally while executing at top speed physically. That level of poise is the hallmark of true greatness.\n\n"
            "How does your organization perform when crunch time arrives at fiscal quarter end?\n\n"
            "👉 Cultivate elite situational awareness and clutch execution across your leadership bench. "
            "Book Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#ClutchPerformance #FourthQuarterMindset #JuJuWatkins #EmotionalPoise #ExecutiveLeadership #GameOnTheLine #LornetteDaye #Speaker"
        ),
        "assetUrl": f"{CDN_BASE}/juju-05.png"
    },
    {
        "id": 6,
        "slot": "Tuesday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-13T17:15:00.000Z",
        "assetFile": "juju-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "CHEMISTRY AND TRUST: THE POWER OF DYNAMIC TEAMMATES. 🤝⚡️\n\n"
            "JuJu Watkins x Jazzy Davidson and the synergy of elite talent.\n\n"
            "Individual brilliance sells tickets, but shared commitment wins national championships. "
            "When elite players surrender individual ego to create seamless court chemistry, the entire program elevates.\n\n"
            "Watching JuJu Watkins collaborate with elite teammates like Jazzy Davidson illustrates a foundational sports truth: "
            "the best players make everyone around them better. They make the extra pass, communicate defensively, and celebrate each other's success with genuine joy.\n\n"
            "Athletes and Coaches: Are you building a team of disconnected stars or a unified powerhouse?\n\n"
            "👉 Strengthen team cohesion, trust, and shared standards. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TeamSynergy #JuJuWatkins #JazzyDavidson #USCWBB #BasketballChemistry #SharedVision #SurvivalSkillsForAthletes #LornetteDaye #TeamCulture"
        ),
        "assetUrl": f"{CDN_BASE}/juju-06.png"
    },
    {
        "id": 7,
        "slot": "Thursday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-15T17:15:00.000Z",
        "assetFile": "juju-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "TRANSFORMING RAW TALENT INTO TACTICAL MASTERY. 🧠📊\n\n"
            "The evolution from gifted scorer to complete floor general.\n\n"
            "In high school, superior athleticism can dominate games. In major Division I college basketball, "
            "every defender is fast, physical, and disciplined. Dominance requires intellectual depth: reading help-side rotations, "
            "manipulating screen angles, and dictating tempo before the ball is even snapped into play.\n\n"
            "JuJu Watkins' growth as a tactical decision-maker is what separates her from ordinary scorers. "
            "She studies opponents with surgical focus, turning basketball into an intellectual contest where she is always two moves ahead.\n\n"
            "Leaders: Is your strategy relying on raw hustle, or deep tactical differentiation?\n\n"
            "👉 Accelerate your company's strategic capability with lessons from Olympic-level athletics. "
            "Inquire for leadership summits: lornettedaye.com/speaking\n\n"
            "#TacticalMastery #JuJuWatkins #SportsStrategy #BasketballIQ #ExecutiveStrategy #PreparationWins #OlympicStandards #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-07.png"
    },
    {
        "id": 8,
        "slot": "Saturday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-17T17:15:00.000Z",
        "assetFile": "juju-08.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "UNSHAKEABLE CONFIDENCE STARTS IN THE UNSEEN HOURS. 🛡️🌅\n\n"
            "Belief is not a feeling. It is an earned state of readiness.\n\n"
            "Look at the calm focus in JuJu Watkins' eyes before the opening tip. That is not arrogance. "
            "It is the quiet, settled confidence of an athlete who knows she has out-worked the competition. "
            "She has practiced every shot thousands of times. She has run the conditioning suicides until failure. "
            "There is no panic because there is no mystery.\n\n"
            "When you prepare thoroughly, anxiety evaporates and replaces itself with supreme clarity. "
            "That is the Olympic formula for mental dominance.\n\n"
            "How do you prepare your mind before you step into crucial business presentations or competitions?\n\n"
            "👉 Master the habits that forge unbreakable confidence and endurance. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#UnshakeableConfidence #JuJuWatkins #EarnedBelief #MentalDominance #FinishStrong #OlympicPreparation #HighPerformance #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-08.png"
    },
    {
        "id": 9,
        "slot": "Monday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-19T17:15:00.000Z",
        "assetFile": "juju-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "RISING ABOVE THE NOISE: PROTECTING YOUR INNER SANCTUARY. 🧘‍♀️🔒\n\n"
            "In the social media age, silence is your greatest competitive advantage.\n\n"
            "Every highlight goes viral. Every play is dissected by millions online. "
            "For young phenoms like JuJu Watkins, the loudest threat is not the opponent on the floor; "
            "it is the relentless noise, praise, and criticism circulating in the digital sphere.\n\n"
            "Champions establish strict mental boundaries. They know who is in their inner circle, whose counsel matters, "
            "and how to mute outside noise so they can protect their energy for what truly counts: family, growth, and team victory.\n\n"
            "Athletes & Professionals: Who is in your trusted counsel, and what noise do you need to mute this week?\n\n"
            "👉 Protect your mental resilience, boundary systems, and identity beyond sport. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ProtectYourEnergy #InnerCircle #JuJuWatkins #MuteTheNoise #MentalHealthInSports #SurvivalSkillsForAthletes #LornetteDaye #Boundaries"
        ),
        "assetUrl": f"{CDN_BASE}/juju-09.png"
    },
    {
        "id": 10,
        "slot": "Wednesday Morning (11:15 AM MDT)",
        "dueAt": "2026-10-21T17:15:00.000Z",
        "assetFile": "juju-10.png",
        "cta": "Finish Strong Book & Keynotes (lornettedaye.com)",
        "text": (
            "FINISH STRONG: LEGACY IS DEFINED BY HOW YOU RISE. 🏅🔥\n\n"
            "The journey continues for USC's generational leader.\n\n"
            "Great seasons are not judged by the start; they are immortalized by how you finish. "
            "JuJu Watkins embodies the warrior spirit of women's basketball: fierce competitiveness, technical brilliance, "
            "and an authentic love for the game that inspires young girls across the globe to pick up a basketball.\n\n"
            "As we celebrate athletic excellence, remember that your greatest triumph is not the trophy you hold, "
            "but the standard of discipline and resilience you leave behind for the next generation.\n\n"
            "Whatever race you are running today, commit to finishing with purpose, integrity, and heart.\n\n"
            "👉 Step into your full potential and finish strong in every area of life. "
            "Explore Lornette Daye's books and leadership keynotes: lornettedaye.com\n\n"
            "#FinishStrong #JuJuWatkins #USCWBB #FightOn #GenerationalLeader #OlympicMindset #BetterPeopleBetterPlayers #CoachLornette #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-10.png"
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
    print("=" * 70)
    print("CAMPAIGN 5: JUJU WATKINS - COURT COMEBACK & ATHLETIC EXCELLENCE (10 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    report_path = os.path.join(os.path.dirname(__file__), "juju-scheduled-report.json")
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

    print("\n" + "=" * 70)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/10 posts scheduled successfully.")
    print("=" * 70)

if __name__ == "__main__":
    main()
