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

CDN_BASE = 'https://lornettedaye.com/campaigns/travis-hunter'

posts_data = [
    {
        "id": 1,
        "slot": "Thursday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-10-15T22:30:00.000Z",
        "assetFile": "travis-hunter-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "WHY SHOULD AN ATHLETE HAVE TO BE ONLY ONE THING? 🏈⚡️\n\n"
            "Offense. Defense. Comeback. Capacity. More than one lane.\n\n"
            "In modern sports, specialized silos force young talent into narrow boxes. "
            "You are told to pick one position, stick to one role, and never test your wider boundaries. "
            "Then along comes Travis Hunter, playing 130+ snaps a game at both wide receiver and cornerback, "
            "shattering conventional wisdom about human endurance and athletic capacity.\n\n"
            "In four decades coaching Olympic athletes and champions, I have learned that human potential "
            "expands to meet the standard you establish. When you refuse to accept artificial limitations, "
            "you discover stamina and versatility you never knew existed.\n\n"
            "Leaders & Coaches: Are you boxing your team members into narrow job titles, or challenging them to expand their capacity?\n\n"
            "👉 Unlock multidimensional leadership and elite performance in your organization. "
            "Book Coach Lornette Daye for keynotes and executive summits: lornettedaye.com/speaking\n\n"
            "#TravisHunter #TwoWayPlayer #IronmanFootball #AthleticCapacity #ColoradoBuffaloes #BeyondLimitations #HighPerformance #ExecutiveLeadership #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-01.png"
    },
    {
        "id": 2,
        "slot": "Saturday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-17T16:30:00.000Z",
        "assetFile": "travis-hunter-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "OFFENSE. DEFENSE. COMEBACK. UNBOX THE ATHLETE. 💥🔥\n\n"
            "Travis Hunter refuses one box.\n\n"
            "Look at the split intensity in this image: catching a touchdown pass in double coverage on one snap, "
            "then locking down the opponent's best receiver on an island three minutes later.\n\n"
            "To excel at that level requires two completely opposite psychological gears: "
            "the fluid, creative timing of a receiver, and the predatory, disciplined aggression of a lockdown cornerback. "
            "Very few athletes can toggle between those mindsets without breaking focus.\n\n"
            "Athletes: How agile is your mental focus when your responsibilities shift during the heat of competition?\n\n"
            "👉 Build elite mental adaptability, focus, and a champion mindset. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#UnboxTheAthlete #VersatilityInAction #TravisHunter #SurvivalSkillsForAthletes #MentalAgility #TwoWayStar #CollegeFootballSaturdays #CoachLornette #HighPerformance"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-02.png"
    },
    {
        "id": 3,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-10-19T14:30:00.000Z",
        "assetFile": "travis-hunter-03.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE FIELD LOOKS DIFFERENT WHEN YOU CAN IMPACT BOTH SIDES. 🏟️✨\n\n"
            "Some gifts are too big for one position. See the whole player.\n\n"
            "When you understand what the defense is trying to take away, you run sharper routes on offense. "
            "When you understand what the receiver is trying to set up, you anticipate routes faster on defense. "
            "Travis Hunter's greatest superpower is not just his speed. It is his complete holistic vision of the game.\n\n"
            "In business and in leadership: When you understand marketing, sales, product, and finance, "
            "you make executive decisions from an entirely different vantage point. Breadth of knowledge elevates your impact.\n\n"
            "What cross-discipline skill has given you the greatest competitive advantage in your career?\n\n"
            "👉 Rise above narrow boundaries and finish what you started with purpose. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FinishStrong #HolisticVision #TravisHunter #CrossDisciplinaryExcellence #SeeTheWholeGame #OlympicPerspective #LeadershipSight #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-03.png"
    },
    {
        "id": 4,
        "slot": "Wednesday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-10-21T19:00:00.000Z",
        "assetFile": "travis-hunter-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "VERSATILITY IS A WEAPON. DO MORE. 🛡️⚔️\n\n"
            "When preparation is wide enough, opportunity grows.\n\n"
            "Look at Travis Hunter in the weight room: sweat dripping, stance low, hands planted on the turf. "
            "You cannot play 130 plays on Saturday if you only prepare for 60 on Tuesday. "
            "Versatility is not a miracle that shows up on game day. It is an excruciating conditioning standard "
            "rehearsed through relentless volume in the dark.\n\n"
            "If you want to handle greater responsibility in your career, you must first expand your capacity in private. "
            "Expand your lung capacity, your intellectual stamina, and your emotional tolerance for pressure.\n\n"
            "Leaders: Is your team's conditioning adequate for the heavier goals you have set for the upcoming quarter?\n\n"
            "👉 Build endurance, culture, and high-capacity teams. "
            "Schedule Coach Lornette Daye for your company convention: lornettedaye.com/speaking\n\n"
            "#VersatilityIsAWeapon #ConditioningForGreatness #TravisHunter #WeightRoomGrind #HighCapacityLeadership #OlympicStamina #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-04.png"
    },
    {
        "id": 5,
        "slot": "Friday Afternoon (5:00 PM MDT)",
        "dueAt": "2026-10-23T23:00:00.000Z",
        "assetFile": "travis-hunter-05.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "HEALING DID NOT END THE STORY. RETURN READY. 🏥💪\n\n"
            "Comebacks can return stronger and broader.\n\n"
            "When Travis Hunter suffered a lacerated liver on national television, critics rushed to proclaim "
            "that his two-way experiment was officially over. They said human bodies cannot take that punishment. "
            "They told him to pick one side and play it safe.\n\n"
            "What did Travis do? He put his head down, attacked rehabilitation with Olympic discipline, "
            "and returned to the field sharper, faster, and more dominant than before. "
            "Adversity is not an exit ramp. It is a refinement furnace.\n\n"
            "What setback recently tested your commitment, and how did you choose to respond?\n\n"
            "👉 Overcome setbacks, rebuild momentum, and rise again after pressure. "
            "Order *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ReturnReady #AdversityToAdvantage #TravisHunter #ComebackMindset #FinishStrong #OlympicResilience #SetbackNotFinal #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-05.png"
    },
    {
        "id": 6,
        "slot": "Sunday Mid-day (11:30 AM MDT)",
        "dueAt": "2026-10-25T17:30:00.000Z",
        "assetFile": "travis-hunter-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "DO NOT REDUCE A MULTIDIMENSIONAL ATHLETE. FULL RANGE. 🧠📚\n\n"
            "Wide receiver instincts. Cornerback discipline. One competitor.\n\n"
            "Look at the film study desk: notebooks filled with route concepts, coverage adjustments, "
            "situational down-and-distance reads, and football IQ. Travis Hunter does not simply play on athleticism. "
            "He masters the mental playbook of two entirely different coaching rooms.\n\n"
            "When young athletes are encouraged to think broadly, their problem-solving ability explodes. "
            "Never let anyone tell you that having multiple passions dilutes your excellence. "
            "When grounded in discipline, range creates unmatched mastery.\n\n"
            "Coaches & Educators: How are you encouraging your athletes to develop their full intellectual and creative range?\n\n"
            "👉 Equip young competitors with champion-level mental tools and emotional focus. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FullRange #MultidimensionalExcellence #TravisHunter #FootballIQ #FilmStudy #SurvivalSkillsForAthletes #OlympicDevelopment #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-06.png"
    },
    {
        "id": 7,
        "slot": "Tuesday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-27T16:30:00.000Z",
        "assetFile": "travis-hunter-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE BEST ATHLETES DO NOT FIT SMALL BOXES. LET THEM EXPAND. 🚀🏆\n\n"
            "Capacity is a competitive advantage.\n\n"
            "Throughout sports history, the innovators who permanently changed the game were always the ones "
            "who refused to conform to rigid templates: Deion Sanders, Bo Jackson, Shohei Ohtani, and now Travis Hunter. "
            "When leaders give exceptional talent the freedom to operate with high standards across multiple domains, "
            "franchises reach historic heights.\n\n"
            "If your organizational culture punishes curiosity and polices boundaries, your best performers will leave. "
            "Give them room to run, challenge them with larger responsibilities, and watch them soar.\n\n"
            "Executives: Are you creating room for your top talent to innovate and expand their impact?\n\n"
            "👉 Cultivate an environment where high-capacity leaders flourish. "
            "Book Coach Lornette Daye for your leadership summit: lornettedaye.com/speaking\n\n"
            "#CapacityIsAnAdvantage #LetThemExpand #TravisHunter #InnovationInSport #CorporateLeadership #RetentionAndGrowth #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-07.png"
    },
    {
        "id": 8,
        "slot": "Thursday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-10-29T22:00:00.000Z",
        "assetFile": "travis-hunter-08.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "EVERY SNAP ASKS A DIFFERENT QUESTION. ANSWER MORE. 🌧️🏃‍♂️\n\n"
            "Travis Hunter answers more than one.\n\n"
            "Running through the rain on game night, ball tucked securely, accelerating down the sideline with defenders trailing. "
            "In every match, sports present unpredictable challenges: sudden turnovers, bad weather, hostile crowds, and physical fatigue. "
            "If your identity is fragile, you fold.\n\n"
            "True resilience means you possess the tools to answer whatever question the game throws at you. "
            "When you are grounded in core values and unwavering daily discipline, chaos around you becomes white noise.\n\n"
            "Men: How do you maintain composure when life hits you with multiple unexpected demands at once?\n\n"
            "👉 Strengthen your resilience, clarify your purpose, and build steadier daily habits. "
            "Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#AnswerMore #ResilienceUnderPressure #TravisHunter #SurvivalSkillsForMen #WeatherTheStorm #MasculinePoise #GameDayMindset #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-08.png"
    },
    {
        "id": 9,
        "slot": "Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-10-31T16:00:00.000Z",
        "assetFile": "travis-hunter-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "TRAINING FOR TWO RESPONSIBILITIES BUILDS ONE RARE EDGE. 💎⚡️\n\n"
            "Receiver touch. Defender timing. Relentless preparation. Rare edge.\n\n"
            "When you hold yourself to the standard of mastery in multiple disciplines, you do not cut corners. "
            "You cannot afford mental drift. Every rep must be sharp. Every recovery protocol must be sacred. "
            "Every meal, every hour of sleep, and every hydration target becomes a non-negotiable tool of your craft.\n\n"
            "That extreme intentionality is what creates true separation at the highest levels of competition. "
            "When everyone else is looking for an easy exit, the ironman athlete is just getting warmed up.\n\n"
            "Athletes: What non-negotiable standard are you committing to uphold this weekend?\n\n"
            "👉 Build focus, discipline, and champion habits that sustain peak performance. "
            "Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#RareEdge #ExtremeIntentionality #TravisHunter #SurvivalSkillsForAthletes #SaturdayFootball #ChampionHabits #OlympicExcellence #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-09.png"
    },
    {
        "id": 10,
        "slot": "Tuesday Mid-day (12:00 PM MDT)",
        "dueAt": "2026-11-03T18:00:00.000Z",
        "assetFile": "travis-hunter-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "COMEBACKS HIT DIFFERENT WHEN THE ROLE IS BIGGER. BIGGER ROLE. 🏟️🌅\n\n"
            "Returning to the field means returning to possibility.\n\n"
            "Walking up the tunnel steps into the golden stadium light, helmet in hand, eyes fixed on the horizon. "
            "When you understand that your athletic journey is bigger than your personal stats, "
            "every challenge takes on profound meaning. You play for your teammates. You play for the kids watching from the bleachers. "
            "You play to prove that human potential has no ceiling.\n\n"
            "Travis Hunter has shown an entire generation what is possible when athletic excellence meets unshakeable heart. "
            "Whatever role you have been given in this season of life, do not shrink back. Step forward, accept the weight, and carry it with dignity.\n\n"
            "Who is a leader or athlete whose larger purpose inspires you to give more every single day?\n\n"
            "👉 Bring championship vision, purpose, and unyielding inspiration to your team or organization. "
            "Connect with Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#BiggerRole #PurposeOverStats #TravisHunter #OlympicVision #ColoradoFootball #LeadershipLegacy #NoLimits #LornetteDaye #KeynoteSpeaker #ChampionshipMindset"
        ),
        "assetUrl": f"{CDN_BASE}/travis-hunter-10.png"
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
    print("Starting Buffer queue scheduling for Travis Hunter Campaign...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "travis-hunter-scheduled-report.json")
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
            print(f"[{idx}/{len(posts_data)}] Post #{post_id_num} already scheduled (Buffer ID: {results[post_id_num]['bufferPostId']}). Skipping.")
            continue

        while True:
            print(f"[{idx}/{len(posts_data)}] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
            resp = schedule_post(post)

            # Check for 429 rate limit
            if resp.get("status_code") == 429 or "429" in str(resp.get("error", "")):
                wait_sec = resp.get("retry_after", 60)
                if wait_sec > 900:
                    print(f"   [DAILY 24H LIMIT] Buffer 24-hour daily limit reached. Reset in {wait_sec}s.")
                    print(f"   [AUTONOMOUS PERSISTENCE] Persisting queue state to report.")
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
                "campaign": "Travis Hunter Ironman & Versatility",
                "total_posts": len(posts_data),
                "successful_posts": successful_count,
                "daily_limit_hit": daily_limit_hit,
                "channelId": CHANNEL_ID,
                "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "results": ordered_results
            }, f, indent=2)

        if daily_limit_hit:
            print("   [AUTONOMOUS HANDOFF] Stopping execution loop.")
            break

        time.sleep(1.0)

    ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
    successful_count = sum(1 for r in ordered_results if r.get("success"))
    print("-" * 60)
    print(f"Travis Hunter Campaign Scheduling Complete: {successful_count}/{len(posts_data)} posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")


if __name__ == "__main__":
    main()
