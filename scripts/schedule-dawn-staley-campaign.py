# -*- coding: utf-8 -*-
"""
Dawn Staley WNBA Player Development Master Campaign: 4 Weeks (28 Days x 3 Posts/Day = 84 Posts)
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Cadence: 3 Posts / Day (Morning 8:00 AM, Midday 1:00 PM, Evening 6:30 PM MDT/MST)

Strict Invariants:
- Zero asterisks anywhere in copy (* or **)
- Zero em dashes (—, &mdash;, \u2014)
- Authoritative Olympian coach voice (first-person, "I", "my work with champions")
- Signed strictly as "Lornette Daye" or "Lornette"
- Call to action strictly points to: https://lornettedaye.com/foundations
- Production custom domain assets only (https://lornettedaye.com/campaigns/dawn-staley/...)
"""

import sys
import os
import json
import ssl
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'
BASE_URL = 'https://lornettedaye.com/campaigns/dawn-staley'

IMAGES = [f'{BASE_URL}/dawn-staley-{i:02d}.png' for i in range(1, 13)]

# 28-day player development spotlight schedule
PLAYERS = [
    ("A'ja Wilson", "The Gold Standard of Modern WNBA Dominance", "Las Vegas Aces"),
    ("Aliyah Boston", "Footwork, Spatial IQ, and Immediate Pro Impact", "Indiana Fever"),
    ("Kamilla Cardoso", "Rim Protection, Paint Physicality, and Poise", "Chicago Sky"),
    ("Allisha Gray", "Two-Way Tenacity and the Defensive Motor", "Atlanta Dream"),
    ("Tiffany Mitchell", "Professional Longevity and Everyday Work Ethic", "Connecticut Sun"),
    ("Brea Beal", "The Lock-Down Perimeter Specialist", "Las Vegas Aces"),
    ("Zia Cooke", "Shot Creation, Dynamic Pace, and Clutch Confidence", "Los Angeles Sparks"),
    ("Destanni Henderson", "Championship Floor General and Big-Stage Composure", "Los Angeles Sparks"),
    ("Laeticia Amihere", "Versatility, Length, and Positionless Athleticism", "Atlanta Dream"),
    ("Mikiah Herbert Harrigan", "Midrange Precision and Shot-Blocking Instincts", "Phoenix Mercury"),
    ("A'ja Wilson & Aliyah Boston", "The Passing Bigs: Reading Defenses Before the Trap", "WNBA All-Stars"),
    ("The Dawn Staley Recruiting Standard", "Vetting Character and Coachability Over Social Media Hype", "Gamecocks"),
    ("The 40-Minute Defensive Identity", "Why South Carolina Held Teams Under Thirty Percent Shooting", "Culture"),
    ("Sacrificing Minutes for Collective Supremacy", "How Lottery Picks Learned to Share the Floor", "Teamwork"),
    ("A'ja Wilson", "Sustaining MVP Standards When You Are the Target", "Las Vegas Aces"),
    ("Aliyah Boston", "Adjusting to the WNBA Physicality in Year One", "Indiana Fever"),
    ("Kamilla Cardoso", "Handling Height and Contact at the Professional Level", "Chicago Sky"),
    ("Allisha Gray", "The Value of an Elite Midrange and Transition Game", "Atlanta Dream"),
    ("Tiffany Mitchell", "Surviving and Thriving in the League Across a Decade", "Connecticut Sun"),
    ("Brea Beal", "Embracing the Unglamorous Role That Wins Titles", "Las Vegas Aces"),
    ("Zia Cooke", "Developing Shot Discipline and Defensive Discipline", "Los Angeles Sparks"),
    ("Destanni Henderson", "Pace Control: The Difference Between Fast and Hurried", "Los Angeles Sparks"),
    ("The Bench Mob Standard", "Developing Pro Habits Before You Become a Starter", "Gamecocks"),
    ("Dawn Staley's Sideline Presence", "The Coach as an Emotional Thermostat During Chaos", "Leadership"),
    ("Preparing Women for the Business of Sport", "Financial Literacy and Brand Sovereignty", "Life Skills"),
    ("The Power of Authentic Self-Expression", "Style, Voice, and Culture in Modern Women's Basketball", "Impact"),
    ("From Columbia to the WNBA Finals", "How the Gamecock DNA Translates to Trophies", "Legacy"),
    ("The Complete Athlete Blueprint", "Better People Make Better Players on Every Stage", "Foundations")
]

CTA_TEXT = """Send me a direct message here on LinkedIn or visit https://lornettedaye.com/foundations to learn how Lornette’s Foundations develops the complete athlete on and off the court."""

HASHTAG_STACK = "#DawnStaley #WNBA #Gamecocks #AjaWilson #AliyahBoston #KamillaCardoso #WNBADraft #AthleteDevelopment #WomenInSports #HighPerformance #LeadershipCulture #LornetteDaye #LD #Foundations"

def generate_post(post_idx, day_num, slot_name):
    player, theme, org = PLAYERS[(day_num - 1) % len(PLAYERS)]
    
    if slot_name == "Morning":
        title = f"DAWN STALEY AND {player.upper()}: {theme.upper()} (DAY {day_num} - MORNING)"
        hook = f"When Dawn Staley recruits a player, she does not promise starting minutes. She promises that if you submit to the daily standard, you will be prepared for the professional stage."
        body = f"""Look at how {player} transitioned to the WNBA with {org}. Most college phenoms struggle during their rookie season because they rely entirely on athletic superiority.

Under Dawn's tutelage, {player} spent years executing against high-level defensive concepts, learning to read defensive rotations, and competing against future professionals in practice every single afternoon.

In four decades coaching Olympic athletes and national champions, I tell young competitors: your college coach either coddles your talent or refines it. Dawn Staley refines it through accountability. She demands that you defend, rebound, and communicate before you are ever given the green light to hunt your own shot."""
        takeaway = f"Elite player development is not about inflating egos. It is about building repeatable physical and mental habits that survive when the competition levels up."

    elif slot_name == "Midday":
        title = f"THE BLUEPRINT: HOW DAWN STALEY INSTILLS PRO POISE IN {player.upper()} (DAY {day_num} - MIDDAY)"
        hook = f"Skill gets an athlete drafted in the first round. Mental composure determines whether they survive their rookie contract."
        body = f"""Watch {player} execute in late-game pressure situations for {org}. There is no frantic panic, no rushed decisions against full-court pressure, and no emotional unraveling after a bad whistle.

That poise was engineered in Columbia, South Carolina. Dawn Staley played point guard at the highest Olympic and professional level. She understands the exact physiological response when the game speeds up. She teaches her players how to breathe, reset their posture, and see the floor with panoramic clarity.

Through Lornette’s Foundations, we call this Emotional Regulation and Recovery. If an athlete cannot regulate their pulse rate between possessions, their shooting percentage plummets. Dawn’s players enter the WNBA already equipped with veteran composure."""
        takeaway = "Pressure is a mental construct. When your fundamentals and emotional poise are automated, the arena slows down."

    else:
        # Evening Slot
        title = f"CULTURE OVER CELEBRITY: DAWN STALEY, {player.upper()}, AND ENDURING EXCELLENCE (DAY {day_num} - EVENING)"
        hook = f"In an era dominated by individual transfer portals and viral highlights, Dawn Staley built a permanent dynasty grounded in radical selflessness."
        body = f"""When {player} reflects on their time under Dawn Staley, the conversation never centers on scoring averages. It centers on love, discipline, and sisterhood.

Dawn shows up for her players as complete human beings. She attends their WNBA games, supports their off-court businesses, and reminds them that their value is never tied solely to a box score.

That holistic approach is why South Carolina is the premier pipeline to the WNBA. When an athlete feels secure in who they are as a person, they play with complete freedom on the hardwood. That is the exact mission we champion: Better People, Better Players."""
        takeaway = "You cannot build a champion on the court until you have secured their foundation as a human being."

    post_text = f"""{title}

{hook}

{body}

Key Takeaway: {takeaway}

In your corner,
Lornette Daye
Olympic-level Coach and Canadian National Champion

{CTA_TEXT}

{HASHTAG_STACK}"""

    # Enforce zero asterisks assertion
    assert "*" not in post_text, "Assertion failed: post contains asterisks!"
    assert "—" not in post_text, "Assertion failed: post contains em dashes!"

    return post_text

def build_queue():
    queue = []
    slots = [
        ("Morning", 8, 0),
        ("Midday", 13, 0),
        ("Evening", 18, 30)
    ]
    
    start_date = datetime(2026, 10, 23)
    post_idx = 1
    
    for day_offset in range(28):
        cur_date = start_date + timedelta(days=day_offset)
        day_num = day_offset + 1
        
        for slot_name, hour, minute in slots:
            time_slot = cur_date.replace(hour=hour, minute=minute)
            p_text = generate_post(post_idx, day_num, slot_name)
            img_url = IMAGES[(post_idx - 1) % len(IMAGES)]
            
            queue.append({
                "id": f"DAWN_STALEY_{post_idx:03d}",
                "day": day_num,
                "slot": f"{slot_name} ({hour:02d}:{minute:02d})",
                "mode": "customScheduled",
                "dueAt": time_slot.isoformat() + "Z",
                "asset_url": img_url,
                "text": p_text
            })
            post_idx += 1

    return queue

# Buffer GraphQL Mutation
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
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
    ... on UnauthorizedError { message }
  }
}
"""

def schedule_post(item):
    ctx = ssl._create_unverified_context()
    input_data = {
        "channelId": CHANNEL_ID,
        "text": item["text"],
        "mode": item["mode"],
        "dueAt": item["dueAt"],
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "assets": [{"image": {"url": item["asset_url"]}}]
    }
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
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get("Retry-After")
        wait = int(retry_after) if retry_after and retry_after.isdigit() else 3600
        return False, "429", wait
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🏀 DAWN STALEY WNBA PLAYER DEVELOPMENT 4-WEEK CAMPAIGN")
    print("Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)")
    print("Cadence: 3 Posts / Day x 28 Days = 84 Bespoke Posts Total")
    print("Zero Asterisks | Zero Em Dashes | Strict Foundations CTA")
    print("================================================================\n")
    
    queue = build_queue()
    print(f"Generated {len(queue)} bespoke posts in master queue.")
    
    queue_file = "scripts/master-dawn-staley-queue.json"
    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
    print(f"Master queue saved to: {queue_file}\n")
    
    report_file = "scripts/dawn-staley-scheduled-report.json"
    if os.path.exists(report_file):
        with open(report_file, "r", encoding="utf-8") as f:
            scheduled_ids = json.load(f)
    else:
        scheduled_ids = {}

    print(f"Already scheduled from prior runs: {len(scheduled_ids)} posts.")
    
    if "--build-only" in sys.argv:
        print("Flag --build-only detected. Staging complete.")
        return

    for idx, item in enumerate(queue):
        item_id = item["id"]
        if item_id in scheduled_ids:
            continue
            
        print(f"[{idx+1}/{len(queue)}] Processing {item_id} | Day {item['day']} | Slot: {item['slot']}...", end="", flush=True)
        ok, res_id, res_status = schedule_post(item)
        
        if ok:
            print(f" ✅ SUCCESS: Post ID {res_id} ({res_status})")
            scheduled_ids[item_id] = {
                "postId": res_id,
                "status": res_status,
                "dueAt": item.get("dueAt"),
                "mode": item["mode"],
                "asset_url": item["asset_url"]
            }
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(scheduled_ids, f, indent=2)
            time.sleep(0.5)
        elif res_id == "429":
            print(f"\n⚠️ BUFFER API DAILY LIMIT REACHED (429).")
            print(f"Co-pilot will pause and resume when the daily limit resets.")
            break
        else:
            print(f" ⚠️ {res_id}: {res_status}")
            break

    print("\n================================================================")
    print(f"📊 SUMMARY: {len(scheduled_ids)} of {len(queue)} posts scheduled.")
    print(f"Report: {report_file}")
    print("================================================================")

if __name__ == "__main__":
    main()
