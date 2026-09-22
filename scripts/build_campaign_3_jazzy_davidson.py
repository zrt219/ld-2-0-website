# -*- coding: utf-8 -*-
"""
Campaign 3: Jazzy Davidson (Next-Gen Women's Hoops & USC Future) - 10 Posts
Generates and runs scripts/schedule-jazzy-davidson-campaign.py
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

slots_info = [
    ("2026-10-16T21:45:00.000Z", "Friday (03:45 PM MDT)"),
    ("2026-10-16T23:45:00.000Z", "Friday (05:45 PM MDT)"),
    ("2026-10-17T14:30:00.000Z", "Saturday (08:30 AM MDT)"),
    ("2026-10-17T17:00:00.000Z", "Saturday (11:00 AM MDT)"),
    ("2026-10-17T19:15:00.000Z", "Saturday (01:15 PM MDT)"),
    ("2026-10-17T21:45:00.000Z", "Saturday (03:45 PM MDT)"),
    ("2026-10-17T23:45:00.000Z", "Saturday (05:45 PM MDT)"),
    ("2026-10-18T14:30:00.000Z", "Sunday (08:30 AM MDT)"),
    ("2026-10-18T17:00:00.000Z", "Sunday (11:00 AM MDT)"),
    ("2026-10-18T19:15:00.000Z", "Sunday (01:15 PM MDT)"),
]

posts_raw = [
    {
        "id": 1,
        "title": "National Freshman Standard: Setting the Bar Early",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "THE NATIONAL FRESHMAN STANDARD: JAZZY DAVIDSON AT USC. ✌️🏀\n\n"
            "Greatness does not wait for a senior season to announce itself.\n\n"
            "Stepping onto a storied campus like USC with national championship aspirations can overwhelm an ordinary freshman. "
            "Jazzy Davidson walked into the Galen Center and established her presence immediately. "
            "USBWA Tamika Catchings National Freshman Player of the Year. WBCA Division I Freshman of the Year. "
            "Big Ten Freshman of the Year. First Team All-Big Ten.\n\n"
            "In four decades coaching Olympic champions, I look for one foundational trait in young athletes: "
            "the ability to handle sudden elevation without losing your daily humility.\n\n"
            "Women and young leaders: When elevated into demanding environments, do you shrink back, or stand tall in your preparation?\n\n"
            "👉 Build lasting confidence, emotional resilience, and grounded identity in seasons of high visibility. "
            "Read Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#JazzyDavidson #USC #WomensBasketball #FightOn #FreshmanOfTheYear #SurvivalSkillsForWomen #OlympicStandard #LornetteDaye"
        )
    },
    {
        "id": 2,
        "title": "Consistency Is a Weapon: 32 Games, 32 Starts",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "CONSISTENCY IS A WEAPON: SHOWING UP AGAIN AND AGAIN IS A SKILL. 🛡️🔥\n\n"
            "Flash gets headlines. Consistency wins championships.\n\n"
            "Thirty-two games played. Thirty-two starts. Twenty-nine double-figure scoring games, including twenty-six consecutive games. "
            "In modern collegiate basketball, with grueling travel schedules, scouting adjustments, and physical wear, "
            "that level of night-in, night-out reliability is rare for any player, let alone a freshman.\n\n"
            "The standard is not built in emotional speeches; it is built in the Tuesday afternoon film session when nobody is clapping.\n\n"
            "Athletes: Can your coach rely on your execution regardless of how you feel when the ball is tipped?\n\n"
            "👉 Develop repeatable focus, discipline systems, and champion poise on and off the court. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ConsistencyIsAWeapon #JazzyDavidson #USCWBB #RepetitionBuildsGreatness #SurvivalSkillsForAthletes #OlympicCoach #LornetteDaye"
        )
    },
    {
        "id": 3,
        "title": "Defense First: The All-Defensive Honor",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "SCORING SELLS TICKETS. DEFENSE COMMANDS RESPECT. 🔒🏀\n\n"
            "Many elite high school recruits believe they can rest on defense once they arrive in college. "
            "Jazzy Davidson earned Big Ten All-Defensive Team honors as a true freshman.\n\n"
            "She guards the opposing team's premier scorer, dives for loose possessions, navigates ball screens, "
            "and contests shots without fouling. That commitment to two-way basketball reveals an athlete "
            "who loves winning far more than personal stat-sheet padding.\n\n"
            "Championship culture is established when your brightest offensive talent takes immense pride in doing the dirty defensive work.\n\n"
            "Leaders: Is your team celebrating vanity metrics, or the foundational efforts that secure victory?\n\n"
            "👉 Master the mindset of athletes who finish every assignment with pride. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TwoWayExcellence #AllDefensive #JazzyDavidson #USCStandard #FinishStrong #OlympicMindset #DisciplineInAction #CoachLornette"
        )
    },
    {
        "id": 4,
        "title": "USC: Always a Higher Standard",
        "cta": "Survival Skills for Students ($14.99 CAD)",
        "text": (
            "USC: ALWAYS A HIGHER STANDARD. BALANCING THE PRESSURE OF ELITE DEMANDS. ✌️📚\n\n"
            "Competing at the highest level of Division I athletics while balancing collegiate academics is a masterclass in time management.\n\n"
            "For student-athletes like Jazzy Davidson, the pressure arrives from every angle: nationwide television, academic midterms, "
            "donor expectations, and high-stakes postseason tournament games. "
            "Navigating that demands emotional maturity far beyond your chronological age.\n\n"
            "When you build structured daily routines, external chaos cannot infiltrate your peace of mind.\n\n"
            "Students and parents: Are your daily habits structured to protect your focus and mental well-being?\n\n"
            "👉 Practical strategies for managing academic and athletic pressure with purpose and balance. "
            "Read Survival Skills for Students ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForStudents #JazzyDavidson #StudentAthleteLife #BigTenHoops #FocusAndBalance #YouthLeadership #LornetteDaye"
        )
    },
    {
        "id": 5,
        "title": "Los Angeles Builds Greatness: The Next Era of Women's Hoops",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "LOS ANGELES BUILDS GREATNESS: THE EXPLOSION OF WOMEN'S BASKETBALL. 🌴🌟\n\n"
            "Women's basketball is experiencing a generational golden age, and Los Angeles is at the center of the movement.\n\n"
            "With sold-out arenas, record-breaking broadcast ratings, and global endorsement deals, young women athletes are proving "
            "that elite sports culture is powered by their skill, charisma, and competitive brilliance. "
            "Jazzy Davidson represents the next wave of this transformative movement.\n\n"
            "In executive leadership, organizations that recognize cultural momentum and invest early in female talent consistently drive innovation.\n\n"
            "Executives: Are you investing in the emerging leaders who are reshaping your industry landscape?\n\n"
            "👉 Empower your executive team with keynote insights on modern talent development and high-performance culture. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#WomensBasketball #GenerationalMovement #JazzyDavidson #ExecutiveLeadership #FutureOfSports #CoachLornette"
        )
    },
    {
        "id": 6,
        "title": "The Standard Gets Built in Repetition",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "THE STANDARD GETS BUILT IN REPETITION: 26 STRAIGHT DOUBLE-FIGURE GAMES. 🔁🏀\n\n"
            "Anyone can have a hot shooting night when the gym feels right. "
            "Scoring in double figures for twenty-six consecutive games means your shot mechanics hold up under severe fatigue.\n\n"
            "It means when opposing defenses double-team you and run junk zones, you remain patient. "
            "You let the game come to you. You find open teammates. You get to the free-throw line. "
            "You refuse to have an 'off night' mentally, even when shots are rimming out.\n\n"
            "Mastery is not about hitting twenty shots in an empty gym. It is about trusting your mechanics when tired legs want to fade.\n\n"
            "Athletes: Have you grooved your mechanics so deeply that pressure cannot disrupt your rhythm?\n\n"
            "👉 Build elite technical habits and composure under defensive pressure. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ShotMechanics #JazzyDavidson #RepeatableExcellence #SurvivalSkillsForAthletes #OlympicDiscipline #LornetteDaye"
        )
    },
    {
        "id": 7,
        "title": "More Than a Game: A Brighter Tomorrow",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "MORE THAN A GAME: A BRIGHTER TOMORROW BUILDS TODAY. 🌅✨\n\n"
            "Athletics is an incredible vehicle, but your character is the destination.\n\n"
            "When you watch Jazzy Davidson interact with young girls in the stands after a game, signing jerseys and offering words of encouragement, "
            "you see an athlete who understands the responsibility of visibility. "
            "She knows that every shot she makes and every interview she gives is opening doors for the next generation of girls picking up a basketball.\n\n"
            "When your purpose extends beyond personal achievement to community empowerment, your motivation never runs dry.\n\n"
            "Readers: Who are you building a brighter tomorrow for through your daily work today?\n\n"
            "👉 Find strength, renew hope, and anchor your life in meaningful purpose. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#MoreThanAGame #JazzyDavidson #RoleModel #SurvivingLife #PurposeOverSelf #InspiringYouth #LornetteDaye"
        )
    },
    {
        "id": 8,
        "title": "Poise on the Road: Thriving in Hostile Arenas",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "POISE ON THE ROAD: SILENCING HOSTILE ARENAS WITH COMPOSURE. 🏟️🤫\n\n"
            "Playing in the Big Ten means traveling to Carver-Hawkeye, Assembly Hall, and the Breslin Center. "
            "Fifteen thousand screaming fans hoping you collapse. "
            "Jazzy Davidson stepped onto those hostile courts as an eighteen-year-old and played with the calm pulse of a veteran pro.\n\n"
            "She didn't engage with the crowd. She didn't argue with referees. She communicated with her point guard and executed the offense. "
            "Composure in hostile territory is the definitive hallmark of championship DNA.\n\n"
            "Professionals: When entering adversarial negotiations or high-tension rooms, does your pulse remain steady?\n\n"
            "👉 Master Olympic-level emotional regulation in high-stakes environments. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HostileArenas #JazzyDavidson #BigTenRoadTrip #FinishStrong #ComposureUnderFire #OlympicPoise #LornetteDaye"
        )
    },
    {
        "id": 9,
        "title": "Discipline Builds Brighter Days",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "DISCIPLINE BUILDS BRIGHTER DAYS: EMBRACING THE UNSEEN PREPARATION. 🌅💪\n\n"
            "Confidence is not a switch you flip when the spotlight turns on. It is an unshakeable inner knowledge that you did the work.\n\n"
            "Before Jazzy Davidson scored thirty points in national broadcasts, there were thousands of morning shooting sessions "
            "in Oregon high school gyms, agility ladders in the summer rain, and resistance training before sunrise. "
            "Her freedom on the court was purchased by discipline in the dark.\n\n"
            "Women in leadership often battle imposter syndrome when stepping into major rooms. "
            "When you remember the depth of your preparation, self-doubt has to leave the room.\n\n"
            "Women: What discipline are you cultivating today that will fuel your confidence tomorrow?\n\n"
            "👉 Rebuild confidence, thrive through transitions, and discover purpose-centered momentum. "
            "Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForWomen #JazzyDavidson #UnseenHours #DisciplineBuildsConfidence #WomenWhoLead #LornetteDaye"
        )
    },
    {
        "id": 10,
        "title": "The Future of Hoops: A Stronger Tomorrow",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "A STRONGER TOMORROW: THE FUTURE IS WRITTEN BY THOSE WHO WORK. 🚀🏀\n\n"
            "Jazzy Davidson's freshman campaign was not the pinnacle; it was the foundation.\n\n"
            "The greatest danger for any young sensation who sweeps national awards is complacency. "
            "Those who truly make history are the ones who review their tape, identify three defensive tendencies to improve, "
            "and show up to offseason workouts with greater hunger than when they were unranked recruits.\n\n"
            "In four decades of coaching, I have watched prodigies fade and relentless workers conquer the world. "
            "When talent and work ethic combine, dynasties are born.\n\n"
            "Keep your standard high. Put in the work. Finish strong.\n\n"
            "👉 Step into your greatness with Olympic principles of endurance and legacy. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#JazzyDavidson #USCHoops #FightOnForever #FinishStrong #NextGenGreatness #OlympicStandard #LornetteDaye"
        )
    }
]

for p in posts_raw:
    t = p["text"]
    assert "—" not in t, f"Post #{p['id']} contains em dash —"
    assert "\u2014" not in t, f"Post #{p['id']} contains unicode em dash"
    assert "&mdash;" not in t, f"Post #{p['id']} contains &mdash;"

print("Verification passed: ZERO em dashes across all 10 Jazzy Davidson posts!")

posts_data = []
for idx, p in enumerate(posts_raw):
    due_at, slot_name = slots_info[idx]
    asset_file = f"jazzy-davidson-{idx+1:02d}.png"
    asset_url = f"https://lornettedaye.com/campaigns/jazzy-davidson/{asset_file}"
    posts_data.append({
        "id": p["id"],
        "slot": slot_name,
        "dueAt": due_at,
        "assetFile": asset_file,
        "assetUrl": asset_url,
        "cta": p["cta"],
        "text": p["text"]
    })

script_template = f'''# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for Campaign 3: Jazzy Davidson (10 Posts)
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

posts_data = {json.dumps(posts_data, indent=4, ensure_ascii=False)}

def schedule_post(post):
    query = \'\'\'
    mutation CreatePost($input: CreatePostInput!) {{
        createPost(input: $input) {{
            __typename
            ... on PostActionSuccess {{
                post {{
                    id
                    status
                    dueAt
                }}
            }}
            ... on LimitReachedError {{
                message
            }}
            ... on InvalidInputError {{
                message
            }}
            ... on UnexpectedError {{
                message
            }}
            ... on UnauthorizedError {{
                message
            }}
        }}
    }}
    \'\'\'

    variables = {{
        "input": {{
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {{
                    "image": {{
                        "url": post["assetUrl"]
                    }}
                }}
            ]
        }}
    }}

    data = json.dumps({{"query": query, "variables": variables}}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.buffer.com',
        data=data,
        headers={{
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {{TOKEN}}',
            'User-Agent': 'Mozilla/5.0'
        }}
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {{
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }}
    except Exception as e:
        return {{"error": str(e)}}

def main():
    print("=" * 75)
    print("CAMPAIGN 3: JAZZY DAVIDSON - NEXT-GEN WOMEN'S HOOPS & USC FUTURE (10 POSTS)")
    print(f"Target Channel: {{CHANNEL_ID}} (Lornette Daye LinkedIn)")
    print(f"Time: {{time.strftime('%Y-%m-%d %H:%M:%S')}}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "jazzy-davidson-scheduled-report.json")
    results = {{}}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("results", [])
                for item in items:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {{e}}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{{idx}}/{{len(posts_data)}}] Post #{{p_id}} already scheduled (Buffer ID: {{results[p_id]['postId']}}). Skipping.")
            continue

        while True:
            print(f"\\n[{{idx}}/{{len(posts_data)}}] Scheduling: Post #{{p_id}} ({{post['slot']}}) - {{post['dueAt']}}...")
            print(f"  Asset: {{post['assetUrl']}}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {{wait_sec + 5}}s...")
                time.sleep(wait_sec + 5)
                continue

            create_post_data = res.get("data", {{}}).get("createPost", {{}})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                st = post_obj.get("status")
                due = post_obj.get("dueAt")
                print(f"  >>> SUCCESS: Post ID {{b_id}} scheduled for {{due}} (status: {{st}})")
                results[p_id] = {{
                    "id": p_id,
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }}
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {{err_msg}}")
                results[p_id] = {{
                    "id": p_id,
                    "slot": post["slot"],
                    "assetUrl": post["assetUrl"],
                    "error": err_msg,
                    "status": "failed"
                }}
                break

            time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\\n" + "=" * 75)
    print(f"Execution complete. Report written to {{report_path}}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {{success_count}}/10 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
'''

with open("scripts/schedule-jazzy-davidson-campaign.py", "w", encoding="utf-8") as f:
    f.write(script_template)

print("Generated scripts/schedule-jazzy-davidson-campaign.py successfully!")
