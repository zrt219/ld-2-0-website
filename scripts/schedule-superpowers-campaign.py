# -*- coding: utf-8 -*-
"""
Superpowers Champions Campaign Scheduler: A'ja Wilson, Jeremiah Smith, Mike Grier
Total: 42 bespoke posts across 21 days (Oct 21, 2026 Kickoff - Nov 11, 2026).
Cadence: 2 posts per day (Morning 8:15 AM MDT/MST, Evening 5:45 PM MDT/MST).
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)

Strict Invariants:
- Zero em dashes (—, &mdash;, \u2014)
- Authoritative Olympian coach voice (first-person, "I", "my athletes")
- Dual Touchpoint CTA on every post (Direct message on LinkedIn + https://lornettedaye.com/foundations)
- Maximized, discoverable hashtags
- Production custom domain assets only (https://lornettedaye.com/campaigns/champions/...)
"""

import sys
import os
import json
import ssl
import urllib.request
import urllib.error
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn
BASE_URL = 'https://lornettedaye.com/campaigns/champions'

ASSETS = {
    "AJA_MOMENT": f"{BASE_URL}/aja-wilson-own-the-moment.jpg",
    "AJA_STANDARD": f"{BASE_URL}/aja-wilson-raise-the-standard.jpg",
    "JEREMIAH_TALENT": f"{BASE_URL}/jeremiah-smith-more-than-talent.jpg",
    "JEREMIAH_MOMENT": f"{BASE_URL}/jeremiah-smith-built-for-the-big-moment.jpg",
    "MIKE_GRIER": f"{BASE_URL}/mike-grier-front-office.jpg"
}

# -------------------------------------------------------------
# BESPOKE POST BLUEPRINTS (42 HIGH-IMPACT POSTS)
# -------------------------------------------------------------

def get_post_blueprint(idx, day_num, slot_name):
    # Determines theme, subject, and copy
    cycle = (idx - 1) % 6  # 6-day cycle for icons
    
    if idx == 0:
        # Kickoff tonight (Oct 21, 9:00 PM) - A'ja Wilson Hero Launch
        title = "A'JA WILSON: THE ART OF OWNING THE MOMENT"
        hook = "When you reach the absolute pinnacle of your sport, the hardest opponent is no longer the team on the other side of the court. The hardest opponent is complacency."
        body = """Watching A'ja Wilson dominate the WNBA and lead the USA Olympic squad is a clinic in emotional regulation. She does not play with frantic tension. She plays with absolute, grounded authority.

Most players search for motivation when the spotlight turns on. The true legends know that greatness is manufactured in private: through disciplined sleep systems, uncompromised recovery, and mental resilience long before the arena doors open.

In my four decades coaching Olympic athletes, I teach that your talent opens the door, but your emotional poise determines whether you stay in the room. A'ja Wilson does not just score points. She dictates the psychological temperature of every game she plays."""
        takeaway = "Stop chasing temporary hype. Build your daily discipline so deeply that composure becomes your natural reaction under pressure."
        asset = ASSETS["AJA_MOMENT"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to learn how Lornette’s Foundations develops complete athletic poise on and off the court.

For women leaders and competitors navigating high-pressure seasons:
Get 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books"""
        hashtags = "#AjaWilson #WNBA #LasVegasAces #WNBAFinals #WomenInSports #ChampionMindset #OlympicGold #AthleteDevelopment #LornetteDaye #LD #RaiseTheStandard #OwnTheMoment #HighPerformance #Leadership #MentalToughness"

    elif cycle == 0:
        # A'ja Wilson - Raise the Standard
        title = f"A'JA WILSON: RAISING THE STANDARD WHEN YOU ARE ALREADY AT THE TOP (DAY {day_num} - {slot_name.upper()})"
        hook = "The most dangerous place for an elite performer is not a losing streak. It is being celebrated so loudly that you stop critiquing your own tape."
        body = f"""When A'ja Wilson steps onto the floor, you are watching a player who refuses to be satisfied with yesterday's trophies. After winning back-to-back WNBA championships and Olympic gold, her focus did not drift. It sharpened.

She added range to her pull-up jumper. She tightened her defensive footwork. She studied opponent tendencies with the hunger of a rookie fighting for a roster spot.

As an Olympic-level coach, I look at body language during adversity. When calls go against her, A'ja resets in three seconds. No theatrics, no lingering frustration. That is mental sovereignty in action."""
        takeaway = "Your previous championship cannot win your next game. Reset your standard daily."
        asset = ASSETS["AJA_STANDARD"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to explore private high-performance mentorship.

Equip yourself with the Olympic mindset to finish what you start:
Order 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A"""
        hashtags = "#AjaWilson #WNBA #LasVegasAces #WNBAMVP #WomenInSport #BasketballExcellence #OlympicCoach #HighPerformance #MentalDiscipline #LornetteDaye #LD #Foundations #EliteAthletics"

    elif cycle == 1:
        # Jeremiah Smith - More Than Talent
        title = f"JEREMIAH SMITH: WHY RAW TALENT IS ONLY THE DOWN PAYMENT (DAY {day_num} - {slot_name.upper()})"
        hook = "College football is filled with five-star recruits who possessed world-class speed but never mastered the quiet discipline between their ears."
        body = f"""Jeremiah Smith arrived at Ohio State with immense national expectations. As a true freshman wide receiver wearing number 4, every route he runs is dissected by millions on national television.

What makes Jeremiah extraordinary is not just his leaping ability or his catching radius. It is his mature decision-making. Watch how he tracks the ball in heavy traffic, sets up defensive backs with patient stems, and blocks on perimeter run plays when the ball is not coming to him.

In my athlete development work, I tell young athletes: talent gets you noticed, but unselfish details earn trust. When a young superstar commits to doing the dirty work, the entire locker room is elevated."""
        takeaway = "Greatness is not a highlight reel. It is the unglamorous habits you execute when the cameras are looking somewhere else."
        asset = ASSETS["JEREMIAH_TALENT"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to learn how we build complete student-athletes ready for the national stage.

For young competitors, parents, and coaches:
Order 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books"""
        hashtags = "#JeremiahSmith #OhioState #Buckeyes #CollegeFootball #CFB #BigTen #WideReceiver #NextLevelReady #AthleteDevelopment #YouthSports #MentalFocus #OlympicCoach #LornetteDaye #LD #Superpowers"

    elif cycle == 2:
        # Jeremiah Smith - Built for the Big Moment
        title = f"JEREMIAH SMITH: FOCUS AND COMPOSURE IN THE FOURTH QUARTER (DAY {day_num} - {slot_name.upper()})"
        hook = "When 100,000 fans are screaming and the game is on the line, your pulse rate determines your execution."
        body = f"""Pressure is not something that exists outside of you. Pressure is a physiological reaction that occurs when you let your mind jump ahead to the scoreboard.

Watch how Jeremiah Smith handles hostile road environments. Before the snap, his eyes are relaxed. His breathing is steady. He is not thinking about the press conference or the final score. He is locked exclusively into his release technique and depth of route.

In track and field and in high-stakes football, peak acceleration requires relaxation. If your shoulders are tense, your stride shortens. When you regulate your nervous system, the game slows down to your pace."""
        takeaway = "You cannot control the noise in the stadium. You can only control your breathing, your alignment, and your execution on this single snap."
        asset = ASSETS["JEREMIAH_MOMENT"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to discover how Lornette’s Foundations trains pressure regulation.

Give your student-athlete practical tools for focus, balance, and academic balance:
Get 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books"""
        hashtags = "#JeremiahSmith #OhioStateFootball #BuckeyeNation #CFBPlayoff #WideReceiver1 #HighPerformanceMindset #PressureIsAPrivilege #AthleteDevelopment #LornetteDaye #LD #SportsPerformance"

    elif cycle == 3:
        # Mike Grier - From the Ice to the Front Office
        title = f"MIKE GRIER: SOVEREIGNTY FROM THE ICE TO THE FRONT OFFICE (DAY {day_num} - {slot_name.upper()})"
        hook = "Playing 1,060 games in the National Hockey League takes physical toughness. Stepping into the General Manager chair takes visionary intellectual sovereignty."
        body = f"""When Mike Grier was named the first Black General Manager in NHL history by the San Jose Sharks in 2022, it was not merely a symbolic milestone. It was the culmination of decades of disciplined study of player personnel, salary cap dynamics, and organizational culture.

On the ice, Mike was known as an uncompromising power forward who played with heart, defensive responsibility, and respect for his teammates. In the front office, he brings that exact same clarity. He did not rush into short-sighted trades. He committed to drafting high-character prospects, rebuilding infrastructure, and establishing an enduring standard.

As an Olympic coach, I remind athletes that your playing career is only chapter one. What intellectual assets are you accumulating today that will position you to run the organization tomorrow?"""
        takeaway = "Do not just play the game. Study the business, understand the architecture, and prepare to lead from the boardroom."
        asset = ASSETS["MIKE_GRIER"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to discuss executive transition and leadership advisory.

For men in leadership navigating career pivots and high-pressure transitions:
Get 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00"""
        hashtags = "#MikeGrier #SanJoseSharks #NHL #HockeyHistory #FirstBlackGM #FrontOffice #ExecutiveLeadership #BlackExcellence #SportsBusiness #AthleteTransition #NextChapter #LornetteDaye #LD #Foundations"

    elif cycle == 4:
        # A'ja Wilson - Leadership & Culture
        title = f"A'JA WILSON: CARRYING THE WEIGHT OF A CULTURAL MOVEMENT (DAY {day_num} - {slot_name.upper()})"
        hook = "Leadership is easy when everyone is winning and the cameras are supportive. Leadership is tested when the spotlight becomes relentless."
        body = f"""Women's basketball is experiencing an unprecedented surge in global viewership, commercial endorsement, and cultural debate. Sitting right at the center of that explosion is A'ja Wilson.

Notice how she handles the microphone. She does not tear down others to elevate herself. She honors the legends who came before her while holding her teammates accountable to championship detail. She speaks with clarity, dignity, and unapologetic self-belief.

In my four decades working with champions, I have seen athletes crumble under public scrutiny because their self-worth was tethered to media headlines. A'ja's foundation is internal. When your self-worth is anchored in daily discipline, external noise cannot shake you."""
        takeaway = "True authority comes from internal alignment, not external validation. Speak with composure, compete with joy, and let your work do the talking."
        asset = ASSETS["AJA_MOMENT"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to learn how we build athletes who lead with presence and poise.

Strengthen your inner foundation through difficult seasons:
Explore our official book catalog ($14.99 CAD): https://lornettedaye.com/books"""
        hashtags = "#AjaWilson #WNBA #LasVegasAces #CultureShifter #LeadershipInSports #WomenWhoLead #AthleteMindset #OlympicWisdom #LornetteDaye #LD #BetterPeopleBetterPlayers"

    else:
        # Cross-Sport Synthesis: The Championship Trinity
        title = f"THE ANATOMY OF EXCELLENCE: A'JA, JEREMIAH, AND MIKE GRIER (DAY {day_num} - {slot_name.upper()})"
        hook = "Look across three completely different arenas: the WNBA, college football, and an NHL front office. The principles of enduring excellence never change."
        body = f"""Whether it is A'ja Wilson controlling the paint, Jeremiah Smith winning 50-50 balls downfield, or Mike Grier drafting the future of a hockey franchise, the fundamental law remains identical.

Excellence is not a switch you flip on game day. It is an operational standard. It requires emotional regulation when friction occurs, radical accountability to your team, and the patience to execute the fundamentals when no one is clapping.

In Lornette’s Foundations, we build Better People and Better Players. Because when you develop the human being behind the athlete, victory on the field becomes the natural byproduct."""
        takeaway = "The arena changes, but the standard does not. Master your emotional control, commit to your craft, and build a legacy that outlasts your trophies."
        asset = ASSETS["JEREMIAH_MOMENT"] if slot_name == "Morning" else ASSETS["MIKE_GRIER"]
        cta = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to bring the 10-Foundation development model to your athlete or organization.

Order your published digital edition ($14.99 CAD): https://lornettedaye.com/books"""
        hashtags = "#HighPerformance #ChampionMindset #AjaWilson #JeremiahSmith #MikeGrier #MultiSportExcellence #AthleteDevelopment #ExecutiveLeadership #LornetteDaye #LD #Foundations"

    post_text = f"""{title}

{hook}

{body}

Key Takeaway: {takeaway}

In your corner,
Lornette Daye
Olympic-level Coach & Canadian National Champion

{cta}

{hashtags}"""

    return post_text, asset

# -------------------------------------------------------------
# BUILD MASTER QUEUE FOR 42 POSTS
# -------------------------------------------------------------

def build_queue():
    queue = []
    
    # Post 1: Tonight Kickoff (Oct 21, 2026 9:00 PM MDT)
    text_0, asset_0 = get_post_blueprint(0, 1, "Evening")
    queue.append({
        "id": "SUPERPOWER_001",
        "day": 1,
        "slot": "Tonight Kickoff (09:00 PM)",
        "mode": "shareNow",
        "dueAt": datetime(2026, 10, 21, 21, 0).isoformat() + "Z",
        "asset_url": asset_0,
        "text": text_0
    })
    
    # Posts 2 to 42: Oct 22 to Nov 11 (2 posts daily at 8:15 AM and 5:45 PM MDT/MST)
    start_date = datetime(2026, 10, 22)
    post_idx = 1
    
    for day_offset in range(21):
        cur_date = start_date + timedelta(days=day_offset)
        day_num = day_offset + 1
        
        # Slot 1: Morning (08:15 AM)
        if post_idx < 42:
            time_m = cur_date.replace(hour=8, minute=15)
            text_m, asset_m = get_post_blueprint(post_idx, day_num, "Morning")
            queue.append({
                "id": f"SUPERPOWER_{post_idx+1:03d}",
                "day": day_num,
                "slot": "Morning (08:15 AM)",
                "mode": "customScheduled",
                "dueAt": time_m.isoformat() + "Z",
                "asset_url": asset_m,
                "text": text_m
            })
            post_idx += 1
            
        # Slot 2: Evening (05:45 PM)
        if post_idx < 42:
            time_e = cur_date.replace(hour=17, minute=45)
            text_e, asset_e = get_post_blueprint(post_idx, day_num, "Evening")
            queue.append({
                "id": f"SUPERPOWER_{post_idx+1:03d}",
                "day": day_num,
                "slot": "Evening (05:45 PM)",
                "mode": "customScheduled",
                "dueAt": time_e.isoformat() + "Z",
                "asset_url": asset_e,
                "text": text_e
            })
            post_idx += 1

    return queue

# -------------------------------------------------------------
# BUFFER GRAPHQL PUBLISHING
# -------------------------------------------------------------

CREATE_POST_MUTATION = """
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
"""

def schedule_post(item):
    ctx = ssl._create_unverified_context()
    input_data = {
        "channelId": CHANNEL_ID,
        "text": item["text"],
        "mode": item["mode"],
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "assets": [{"image": {"url": item["asset_url"]}}]
    }
    if item["mode"] == "customScheduled":
        input_data["dueAt"] = item["dueAt"]
        
    payload = json.dumps({"query": CREATE_POST_MUTATION, "variables": {"input": input_data}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            create_post = data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            if typename == "PostActionSuccess" and "post" in create_post:
                p = create_post["post"]
                return True, p.get("id"), p.get("status")
            else:
                msg = create_post.get("message") or json.dumps(create_post)
                return False, typename, msg
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🔥 SUPERPOWERS CHAMPIONS CAMPAIGN: A'JA, JEREMIAH, MIKE GRIER")
    print("Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)")
    print("Schedule: 42 Posts across 21 Days (2 Posts/Day)")
    print("================================================================\n")
    
    queue = build_queue()
    print(f"Generated {len(queue)} bespoke campaign posts.")
    
    queue_file = "scripts/master-superpowers-queue.json"
    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    print(f"Master queue saved: {queue_file}\n")
    
    if "--build-only" in sys.argv:
        print("Flag --build-only detected. Queue built without posting.")
        return

    report_file = "scripts/superpowers-scheduled-report.json"
    if os.path.exists(report_file):
        with open(report_file, "r", encoding="utf-8") as f:
            scheduled_ids = json.load(f)
    else:
        scheduled_ids = {}

    print(f"Already scheduled from prior runs: {len(scheduled_ids)} posts.\n")
    
    for idx, item in enumerate(queue):
        item_id = item["id"]
        if item_id in scheduled_ids:
            continue
            
        print(f"[{idx+1}/{len(queue)}] Processing {item_id} | Day {item['day']} | Slot: {item['slot']} | Mode: {item['mode']}")
        ok, res_id, res_status = schedule_post(item)
        
        if ok:
            print(f"   ✅ SUCCESS: Post ID {res_id} ({res_status})")
            scheduled_ids[item_id] = {
                "postId": res_id,
                "status": res_status,
                "dueAt": item.get("dueAt"),
                "mode": item["mode"],
                "asset_url": item["asset_url"]
            }
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(scheduled_ids, f, indent=2)
            time.sleep(2)  # Polite pacing between API requests
        else:
            print(f"   ⚠️ STOP / LIMIT: {res_id} - {res_status}")
            print(f"   Post will remain queued in {queue_file} for autonomous catchup.")
            break

    print("\n================================================================")
    print(f"📊 SUMMARY: {len(scheduled_ids)} of {len(queue)} posts scheduled in Buffer.")
    print(f"Report: {report_file}")
    print("================================================================")

if __name__ == "__main__":
    main()
