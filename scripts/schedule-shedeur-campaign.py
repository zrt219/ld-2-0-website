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

CDN_BASE = 'https://lornettedaye.com/campaigns/shedeur-sanders'

posts_data = [
    {
        "id": 1,
        "slot": "Wednesday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-14T16:30:00.000Z",
        "assetFile": "shedeur-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "STAY READY. YOUR MOMENT DOES NOT SEND WARNINGS. ⏳🏈\n\n"
            "Preparation is how patience speaks. Ready before the call.\n\n"
            "In high-performance athletics and executive leadership, opportunity rarely gives advance notice. "
            "It does not tap you on the shoulder weeks in advance and say, 'Get your conditioning up.' "
            "It arrives violently, unexpectedly, and often in the middle of a crisis.\n\n"
            "Shedeur Sanders understands that greatness is not claimed under bright stadium lights. "
            "It is built during hundreds of unseen hours in dark film rooms and early-morning training sessions. "
            "When the helmet goes on and your number is called, you either have the reps in the bank or you do not.\n\n"
            "Leaders & Athletes: If your biggest career opportunity arrived in the next five minutes, would you be ready to execute immediately?\n\n"
            "👉 Equip your organization with champion-level mental preparedness and poise. "
            "Book Coach Lornette Daye for your next keynote: lornettedaye.com/speaking\n\n"
            "#ShedeurSanders #StayReady #PreparationIsPower #QuarterbackMindset #ColoradoBuffaloes #HighPerformance #ExecutiveLeadership #OlympicStandard #LornetteDaye #KeynoteSpeaker #NoExcuses"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-01.png"
    },
    {
        "id": 2,
        "slot": "Friday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-10-16T22:00:00.000Z",
        "assetFile": "shedeur-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "THE HARDEST POSITION IN FOOTBALL MAY BE QB2. 🏈📋\n\n"
            "You prepare every single week without knowing if your moment will ever come.\n\n"
            "Think about the psychological discipline required: You take mental reps on every drill. "
            "You study the blitz packages until midnight. You take hits on the scout team. "
            "And then on game day, you stand on the sideline holding a play chart, keeping your mind sharp and your arm warm.\n\n"
            "If your commitment depends on guaranteed playing time, you will never survive elite sports or corporate pressure. "
            "Discipline builds options. Composure in waiting is the ultimate test of athletic maturity.\n\n"
            "Athletes: How do you maintain fire and focus when your current role is behind the scenes?\n\n"
            "👉 Master emotional regulation, focus, and resilience through every phase of competition. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#QB2Mindset #ComposureInWaiting #ShedeurSanders #SurvivalSkillsForAthletes #DisciplineBuildsFreedom #MentalPoise #FootballCulture #OlympicMindset #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-02.png"
    },
    {
        "id": 3,
        "slot": "Sunday Mid-day (11:30 AM MDT)",
        "dueAt": "2026-10-18T17:30:00.000Z",
        "assetFile": "shedeur-03.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "PREPARE LIKE THE STARTER. GROW LIKE THE FUTURE. 📖✍️\n\n"
            "Development continues even when the depth chart is quiet. Build while you wait.\n\n"
            "Look at Shedeur Sanders at the study desk: notes open, tablet running film, details logged. "
            "That is where championships are won. When men take ownership of their personal growth without needing an audience, "
            "their foundation becomes unbreakable.\n\n"
            "In four decades coaching Olympic athletes, I have watched many gifted players get distracted when they were not in the spotlight. "
            "The ones who reached the summit were the men who treated quiet seasons as an incubator for greatness.\n\n"
            "Fathers, mentors, and emerging leaders: What is the unseen habit you are investing in today for a bigger tomorrow?\n\n"
            "👉 Build steadier daily habits, purpose, and emotional resilience under pressure. "
            "Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #BuildWhileYouWait #ShedeurSanders #FilmRoomGrind #SelfDiscipline #MasculineLeadership #PersonalGrowth #OlympicExcellence #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-03.png"
    },
    {
        "id": 4,
        "slot": "Tuesday Morning (9:00 AM MDT)",
        "dueAt": "2026-10-20T15:00:00.000Z",
        "assetFile": "shedeur-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "LEADERSHIP DOES NOT REQUIRE THE FIRST SNAP. 🗣️🔥\n\n"
            "Some voices carry a room before they ever carry a game. Lead now.\n\n"
            "A title or a starting role does not make you a leader. Your presence makes you a leader. "
            "When Shedeur Sanders steps into the huddle, his teammates lock in. Why? Because true leadership is felt "
            "in your clarity, your standard, and how you demand excellence from yourself first.\n\n"
            "If you only lead when you are in charge, you are not a leader. You are an opportunist. "
            "Great organizations are full of leaders who elevate their peers from every seat in the room.\n\n"
            "Executives & Directors: Are you cultivating grassroots leadership throughout your teams, or only relying on the top tier?\n\n"
            "👉 Foster dynamic leadership, accountability, and cultural alignment across your workforce. "
            "Bring Lornette Daye to your next executive summit: lornettedaye.com/speaking\n\n"
            "#LeadNow #LeadershipPresence #ShedeurSanders #HuddleCommand #HighPerformanceCulture #ExecutivePresence #OlympicStandard #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-04.png"
    },
    {
        "id": 5,
        "slot": "Thursday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-10-22T22:30:00.000Z",
        "assetFile": "shedeur-05.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "EVEN WHEN YOU WAIT, YOUR DEVELOPMENT SHOULD NOT. 🏟️🌅\n\n"
            "Quiet progress is still progress. Keep building.\n\n"
            "Walking out of the stadium tunnel with the sun setting behind the goalposts, ball in hand, helmet tucked. "
            "That solitary walk tells the entire story. There are days when nobody is chanting your name. "
            "There are seasons when your progress feels invisible to the outside world.\n\n"
            "Do not stop. Do not allow a pause in public recognition to cause a pause in your daily standards. "
            "The athletes and leaders who finish strong are the ones who fall in love with the unglamorous daily routine.\n\n"
            "What quiet discipline has sustained your growth during challenging seasons?\n\n"
            "👉 Discover how to persevere through pressure and finish your life goals with purpose. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FinishStrong #QuietProgress #ShedeurSanders #ColoradoFootball #DailyDiscipline #StayingFocused #ResilienceUnderPressure #LornetteDaye #OlympicMindset"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-05.png"
    },
    {
        "id": 6,
        "slot": "Saturday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-24T16:30:00.000Z",
        "assetFile": "shedeur-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "THE BENCH CAN TEACH PATIENCE WITHOUT LOWERING STANDARDS. 🏋️‍♂️⏱️\n\n"
            "Waiting well is still work. Patience with pressure.\n\n"
            "Sitting on the bench does not mean you have lowered your ambitions. It means you are sharpening the blade in silence. "
            "Notice the towel draped, the water bottle set, the laser focus in Shedeur Sanders's eyes. "
            "He is not slouching. He is not disengaged. He is mentally running the plays.\n\n"
            "In sports and in career development, the bench is either a waiting room or a laboratory. "
            "You decide which one it will be. If you treat it like a laboratory, you will emerge twice as dangerous.\n\n"
            "Athletes: How do you keep your edge sharp when you are waiting for your next start?\n\n"
            "👉 Build unshakeable confidence and focus on and off the field. "
            "Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#PatienceWithPressure #SharpenTheBlade #ShedeurSanders #SurvivalSkillsForAthletes #AthleticFocus #BenchToBreakthrough #OlympicCoach #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-06.png"
    },
    {
        "id": 7,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-10-26T14:30:00.000Z",
        "assetFile": "shedeur-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE BACKUP'S CONFIDENCE IS BUILT IN SILENCE. 🌧️🏈\n\n"
            "Pressure practiced early becomes poise later. Confidence rehearsed.\n\n"
            "Look at this moment in the pouring rain under stadium floodlights: ball cocked, eyes locked on the target, "
            "delivering the pass with perfect mechanics despite the cold and the wet turf. "
            "When you practice under extreme discomfort in silence, game-day conditions feel like second nature.\n\n"
            "Throughout my career as an Olympic coach, I have taught athletes that confidence is not bravado. "
            "Confidence is a proven track record with yourself that you have already survived the storm.\n\n"
            "How does your team practice handling adversity before the crisis actually hits?\n\n"
            "👉 Train your organization to perform at its peak through turbulence. "
            "Book Coach Lornette Daye for your next convention: lornettedaye.com/speaking\n\n"
            "#ConfidenceRehearsed #PracticingUnderPressure #ShedeurSanders #HighPerformanceCulture #PoiseInTheStorm #OlympicTraining #ExecutiveResilience #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-07.png"
    },
    {
        "id": 8,
        "slot": "Wednesday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-10-28T19:00:00.000Z",
        "assetFile": "shedeur-08.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": (
            "EVERY REP WITHOUT THE HEADLINE STILL MATTERS. ☀️🏈\n\n"
            "Invisible work leaves visible growth. Reps build belief.\n\n"
            "In modern culture, everyone wants the highlight reel on Instagram. Everyone wants the viral clip, "
            "the NIL brand deal, and the roar of 70,000 fans. But nobody can buy the thousands of throws "
            "into empty practice nets under the morning sun.\n\n"
            "Shedeur Sanders knows that true swagger is rooted in genuine preparation. When you have done the invisible work, "
            "you walk into any stadium with peace in your heart because you are not pretending. You are simply revealing what you have done in secret.\n\n"
            "Men: Where do you need to recommit to the unglamorous daily reps in your personal or professional life?\n\n"
            "👉 Build resilience, emotional clarity, and lasting purpose. "
            "Order *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#RepsBuildBelief #InvisibleWork #ShedeurSanders #SurvivalSkillsForMen #TrueConfidence #DailyDiscipline #CharacterOverHype #OlympicMindset #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-08.png"
    },
    {
        "id": 9,
        "slot": "Friday Afternoon (5:00 PM MDT)",
        "dueAt": "2026-10-30T23:00:00.000Z",
        "assetFile": "shedeur-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "QB2 IS A MINDSET TEST. 🧠🔒\n\n"
            "Can you stay sharp when the spotlight is somewhere else? Stay sharp.\n\n"
            "When you are not the primary focal point of the organization, it is easy to let your standards slip. "
            "It is easy to arrive five minutes late, take sloppy notes, and let your body drift out of peak condition. "
            "Only the elite understand that maintaining championship standards in the shadows is the ultimate competitive advantage.\n\n"
            "When the spotlight shifts back to you, you will not have time to get ready. You must already be operating at the highest level.\n\n"
            "Leaders: How do you keep your next generation of executives motivated and sharp while they await their turn?\n\n"
            "👉 Build championship depth and succession readiness across your leadership pipeline. "
            "Connect with Lornette Daye: lornettedaye.com/speaking\n\n"
            "#StaySharp #MindsetTest #ShedeurSanders #QuarterbackPreparation #SuccessionPlanning #LeadershipExcellence #OlympicDiscipline #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-09.png"
    },
    {
        "id": 10,
        "slot": "Sunday Mid-day (12:00 PM MDT)",
        "dueAt": "2026-11-01T18:00:00.000Z",
        "assetFile": "shedeur-10.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "WHEN THE DOOR OPENS, ARRIVE ALREADY READY. 🚪✨\n\n"
            "Opportunity favors the quarterback who kept preparing. Arrive ready.\n\n"
            "The tunnel doors swing wide. The crowd noise washes over you. The scoreboard clock is running. "
            "This is what every rep, every film session, and every lonely morning was for. "
            "When you arrive already ready, you do not panic. You execute with calm precision.\n\n"
            "Shedeur Sanders embodies the poise that comes from relentless preparation under intense national expectations. "
            "No matter where you start, trust the work you have put in and take the field with confidence.\n\n"
            "What is the biggest goal you are preparing to conquer as we head into the final stretch of the year?\n\n"
            "👉 Elevate your standards, persevere to the end, and achieve your highest potential. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ArriveReady #OpportunityFavorsThePrepared #ShedeurSanders #FinishStrong #GameDayReady #OlympicMindset #PerseveranceInAction #LornetteDaye #KeynoteSpeaker #ChampionshipLegacy"
        ),
        "assetUrl": f"{CDN_BASE}/shedeur-10.png"
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
    print("Starting Buffer queue scheduling for Shedeur Sanders Solo Campaign...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "shedeur-scheduled-report.json")
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
                "campaign": "Shedeur Sanders Solo QB Leadership",
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
    print(f"Shedeur Sanders Campaign Scheduling Complete: {successful_count}/{len(posts_data)} posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")


if __name__ == "__main__":
    main()
