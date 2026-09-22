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

CDN_BASE = 'https://lornettedaye.com/campaigns/camward-shedeur'

posts_data = [
    {
        "id": 1,
        "slot": "Wednesday Morning (10:30 AM MDT)",
        "dueAt": "2026-09-23T16:30:00.000Z",
        "assetFile": "camward-shedeur-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "SAME DRAFT. DIFFERENT RUNWAY. 🏈⚡️\n\n"
            "Look at Cam Ward and Shedeur Sanders side by side. Two elite quarterbacks entering the same national spotlight. "
            "Two distinct paths to the exact same high-stakes arena.\n\n"
            "One quarterback started at Incarnate Word in FCS, transferred to Washington State, and developed step by step into a Miami powerhouse. "
            "The other grew up with NFL royalty in his living room, won at Jackson State under intense scrutiny, and carried the weight of Colorado football on his shoulders.\n\n"
            "In four decades of coaching Olympic athletes and national champions, I have seen this truth prove out repeatedly: "
            "Development is never linear. What matters is not how early you get noticed. What matters is the runway you build beneath your feet.\n\n"
            "Coaches & Leaders: Are you judging your emerging talent by where they started, or by how rapidly they adapt to higher competition?\n\n"
            "👉 Bring Olympic-level athletic leadership and development systems to your organization. "
            "Book Coach Lornette Daye for keynotes and executive summits: lornettedaye.com/speaking\n\n"
            "#CamWard #ShedeurSanders #CollegeFootball #NFLDraft #QuarterbackLeadership #PlayerDevelopment #HighPerformance #ExecutiveCoaching #OlympicMindset #LornetteDaye #LeadershipExcellence #GridironCulture"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-01.png"
    },
    {
        "id": 2,
        "slot": "Friday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-25T22:00:00.000Z",
        "assetFile": "camward-shedeur-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "WHAT BUILDS A QUARTERBACK? 🧠📋\n\n"
            "Confidence. Reps. Coaching. Patience.\n\n"
            "Notice what is NOT on that list: Hype. Social media followers. Preseason accolades.\n\n"
            "The quarterback position is the most mentally demanding role in team sports. You must read coverages in 1.8 seconds, "
            "navigate a collapsing pocket, protect your receivers, manage the clock, and hold the collective belief of 53 men on your shoulders.\n\n"
            "You cannot shortcut that standard with raw talent. It requires thousands of unglamorous reps in an empty film room when nobody is cheering. "
            "When you develop the whole athlete from the inside out, the poise on Saturday afternoon becomes automatic.\n\n"
            "Athletes: What part of your preparation routine needs more discipline this week?\n\n"
            "👉 Build focus, emotional composure, and a champion mindset on and off the field. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#QuarterbackMindset #SurvivalSkillsForAthletes #CamWard #ShedeurSanders #FilmRoomGrind #MentalToughness #HighSchoolAthletes #CollegeFootball #ChampionHabits #LornetteDaye #SportsPsychology"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-02.png"
    },
    {
        "id": 3,
        "slot": "Sunday Mid-day (11:30 AM MDT)",
        "dueAt": "2026-09-27T17:30:00.000Z",
        "assetFile": "camward-shedeur-03.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "PLAYING TEACHES. WAITING TESTS. ⏳🎯\n\n"
            "Game reps build rhythm. Patience builds resilience. Both are necessary parts of the journey.\n\n"
            "When an athlete is on the field taking live snaps, they learn how to adjust to game speed. But what happens during the seasons "
            "when you are waiting for your opportunity? What happens when the transfer portal, the depth chart, or an injury forces you to watch from the sideline?\n\n"
            "That waiting period is not wasted time unless you choose to waste it. It is where you build mental stamina. It is where you learn to study "
            "defenses without taking the physical hits. When your number is finally called, the work you did in the shadows will be revealed.\n\n"
            "What is a season of waiting that ended up preparing you for your biggest breakthrough?\n\n"
            "👉 Rise again after setbacks, persevere through delays, and finish what you started. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FinishStrong #PatienceInTheGrind #CamWard #ShedeurSanders #CollegeFootball #OlympicResilience #StayingReady #NextManUp #AthleticDevelopment #LornetteDaye #Perseverance"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-03.png"
    },
    {
        "id": 4,
        "slot": "Tuesday Morning (9:00 AM MDT)",
        "dueAt": "2026-09-29T15:00:00.000Z",
        "assetFile": "camward-shedeur-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "DIFFERENT PATHS. SAME POSITION. 🧭🏟️\n\n"
            "Two timelines. One demanding profession. The position requires more.\n\n"
            "In every corporate boardroom and athletic program, leaders arrive with different backgrounds. Some come through prestigious elite pipelines. "
            "Others fight their way up from non-traditional routes through pure grit and relentless adaptation.\n\n"
            "Once the whistle blows, the pedigree no longer matters. The scoreboard does not care how many stars were beside your name in high school. "
            "It only cares whether you can deliver poise under pressure, make decisive calls, and elevate the people around you.\n\n"
            "Executives & Athletic Directors: Do you judge leaders by their background, or by their repeatable execution under fire?\n\n"
            "👉 Train your organization to execute under intense pressure. "
            "Book Lornette Daye for your leadership conference: lornettedaye.com/speaking\n\n"
            "#LeadershipUnderPressure #CamWard #ShedeurSanders #ExecutivePresence #CorporateCulture #HighPerformanceLeadership #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-04.png"
    },
    {
        "id": 5,
        "slot": "Thursday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-10-01T22:30:00.000Z",
        "assetFile": "camward-shedeur-05.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "ONE STARTS. ONE STAYS READY. ⏱️💪\n\n"
            "Different assignments. Same standard. Prepare for your moment.\n\n"
            "In professional football, your entire career can change on a single play. If the starter goes down in the second quarter, "
            "the backup has zero seconds to warm up emotionally. You have to jog onto the field with complete command of the playbook and absolute confidence in your eyes.\n\n"
            "True masculine leadership and personal integrity are demonstrated when you prepare like a starter even when your name is listed second on the depth chart. "
            "You do not slack off in practice. You do not pout in meetings. You stay locked in, because readiness is a matter of personal honor.\n\n"
            "Men & Leaders: Are you preparing every day for the bigger responsibilities you have been praying for?\n\n"
            "👉 Build steadier daily habits, purpose, and emotional resilience under pressure. "
            "Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #StayReady #CamWard #ShedeurSanders #QuarterbackDepth #MasculineResilience #WorkEthic #LeadershipHabits #DisciplineOverMotivation #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-05.png"
    },
    {
        "id": 6,
        "slot": "Saturday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-03T16:30:00.000Z",
        "assetFile": "camward-shedeur-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "STARTER PRESSURE. BACKUP PRESSURE. ⚖️🔥\n\n"
            "One must deliver now. One must be ready without warning. Both mindsets matter.\n\n"
            "Starter pressure is relentless scrutiny: every incompletion is dissected on national television, every loss is blamed on you, and expectations are sky-high.\n\n"
            "Backup pressure is quiet isolation: staying sharp without the reward of game reps, maintaining intense mental focus while holding a clipboard, and waiting for an unpredictable window.\n\n"
            "In 40+ years coaching Olympic-caliber athletes, I teach that elite organizations fail when they only care about the starters. "
            "Championship teams are won by the depth. When the second unit embraces their critical role with pride, your organization becomes bulletproof.\n\n"
            "How does your team recognize and motivate the vital contributors working behind the scenes?\n\n"
            "👉 Elevate team cohesion, depth, and cultural alignment. "
            "Bring Coach Lornette Daye to your next team summit: lornettedaye.com/speaking\n\n"
            "#StarterPressure #DepthWinsChampionships #CamWard #ShedeurSanders #TeamCulture #HighPerformanceTeams #OlympicCoach #LornetteDaye #KeynoteSpeaker #CollegeFootball"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-06.png"
    },
    {
        "id": 7,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-10-05T14:30:00.000Z",
        "assetFile": "camward-shedeur-07.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "TALENT MATTERS. RUNWAY MATTERS TOO. 🛫📊\n\n"
            "Development is never only about ability. Reps change everything.\n\n"
            "A pilot cannot take off on a runway that is too short. In the exact same way, an immensely gifted quarterback cannot reach their full potential "
            "without adequate developmental runway: competent coaching, offensive line protection, and the grace to learn from mistakes without being benched immediately.\n\n"
            "Look at Cam Ward's journey: Incarnate Word gave him the reps to build confidence. Washington State gave him the reps against Pac-12 speed. Miami gave him the platform to contend nationally.\n\n"
            "Athletes and parents: Do not rush the process. Seek environments that give you the runway to develop, rather than chasing quick fame.\n\n"
            "Coaches: How do you protect your young athletes' developmental runways from outside pressure?\n\n"
            "👉 Equip your athlete with mental tools to handle expectations and thrive. "
            "Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#DevelopmentRunway #CamWard #ShedeurSanders #SurvivalSkillsForAthletes #YouthSports #PlayerGrowth #CoachingWisdom #OlympicDevelopment #LornetteDaye #FootballCulture"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-07.png"
    },
    {
        "id": 8,
        "slot": "Wednesday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-10-07T19:00:00.000Z",
        "assetFile": "camward-shedeur-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "REPS BUILD CLARITY. 🔍🏈\n\n"
            "The more a quarterback sees, the more the game slows down. Grow into the speed.\n\n"
            "When young quarterbacks first enter college football, the game looks like an overwhelming blur of blitz packages, disguise coverages, and deafening crowd noise. "
            "Everything moves at 100 miles per hour.\n\n"
            "How do Cam Ward and Shedeur Sanders stand in the pocket so calmly today? Because after seeing thousands of snaps, the human brain begins recognizing patterns before they unfold. "
            "What looks like magic on Saturday is simply the compound effect of relentless repetition.\n\n"
            "In leadership, in high-stakes negotiations, and in sports: Confidence is not a feeling. Confidence is pattern recognition born from preparation.\n\n"
            "What is a skill that used to intimidate you that has now completely slowed down through practice?\n\n"
            "👉 Build elite pattern recognition and calm execution under fire. "
            "Schedule Coach Lornette Daye for your executive retreat: lornettedaye.com/speaking\n\n"
            "#GameSlowsDown #PatternRecognition #CamWard #ShedeurSanders #MentalComposure #HighPerformance #OlympicTraining #ExecutivePresence #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-08.png"
    },
    {
        "id": 9,
        "slot": "Friday Afternoon (5:00 PM MDT)",
        "dueAt": "2026-10-09T23:00:00.000Z",
        "assetFile": "camward-shedeur-09.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE DRAFT WAS ONLY THE BEGINNING. 🎟️💼\n\n"
            "Pick number makes noise. Daily work builds the quarterback. Build after the spotlight.\n\n"
            "Every spring, the draft media creates a circus of draft grades, mock boards, and television debates. "
            "Whether you are drafted in the first round or enter the building as a late-round pick, the celebration lasts exactly 24 hours.\n\n"
            "The very next morning, everyone is an NFL employee starting from zero. The defensive ends charging at you do not care about your signing bonus or your jersey sales. "
            "They only care if you can stand in the pocket and deliver the ball accurately under heavy contact.\n\n"
            "Do not fall in love with milestones. Fall in love with the unglamorous process of getting better every single day.\n\n"
            "Raptors and football fans: What is the most memorable late-round pick or underdog who became a superstar through pure daily work?\n\n"
            "👉 Build staying power that outlasts early acclaim. "
            "Order *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#DraftDayReality #WorkOverNoise #CamWard #ShedeurSanders #FinishStrong #NFLDraft #WorkEthic #StayingPower #OlympicDiscipline #LornetteDaye #UnderdogMindset"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-09.png"
    },
    {
        "id": 10,
        "slot": "Sunday Mid-day (12:00 PM MDT)",
        "dueAt": "2026-10-11T18:00:00.000Z",
        "assetFile": "camward-shedeur-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "YOUR PATH IS NOT YOUR CEILING. 🏔️✨\n\n"
            "Where you start is not the final story. Keep building.\n\n"
            "Cam Ward started with zero FBS scholarship offers coming out of high school. "
            "Shedeur Sanders had to carry the immense pressure of proving he was not just living in his father's shadow.\n\n"
            "Both quarterbacks refused to let external labels define their destiny. They put their heads down, trusted the grind, "
            "and forged their own identity through performance, leadership, and unshakeable self-belief.\n\n"
            "Never allow anyone to tell you that your beginnings limit your horizon. When your purpose is clear and your discipline is consistent, "
            "every setback becomes fuel for your ascent.\n\n"
            "Who is an athlete or leader whose journey from humble beginnings inspires you the most? Tag them below!\n\n"
            "👉 Empower your entire organization to shatter their ceilings. "
            "Book Coach Lornette Daye for your annual keynote: lornettedaye.com/speaking\n\n"
            "#YourPathIsNotYourCeiling #KeepBuilding #CamWard #ShedeurSanders #UnshakeableBelief #OvercomingOdds #CollegeFootball #OlympicExcellence #LornetteDaye #KeynoteSpeaker #InspirationInAction"
        ),
        "assetUrl": f"{CDN_BASE}/camward-shedeur-10.png"
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
    print("Starting Buffer queue scheduling for Cam Ward x Shedeur Sanders QB Leadership Campaign...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "camward-shedeur-scheduled-report.json")
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
                "campaign": "Cam Ward x Shedeur Sanders QB Leadership",
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
    print(f"Cam Ward x Shedeur Sanders Campaign Scheduling Complete: {successful_count}/{len(posts_data)} posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")


if __name__ == "__main__":
    main()
