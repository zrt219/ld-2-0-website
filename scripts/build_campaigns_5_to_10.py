# -*- coding: utf-8 -*-
"""
Builder for Campaigns 5 through 10:
5. NBA (3 posts)
6. Cricket (14 posts)
7. Sitaya Fagan (10 posts)
8. Tyrese Gibson (12 posts)
9. Yaroslava Mahuchikh (8 posts)
10. Saquon Barkley (10 posts)

Enforces strict zero em dashes, authoritative Olympian voice, canonical books, and production custom domain URLs.
"""

import os
import sys
import json
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

# 1. Load existing booked slots
existing_due = set()
for rpt in ['scripts/rescheduled-master-report.json', 'scripts/henry-scheduled-report.json']:
    if os.path.exists(rpt):
        with open(rpt, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                if item.get('dueAt'):
                    existing_due.add(item['dueAt'])

candidate_times = ['14:30:00.000Z', '17:00:00.000Z', '19:15:00.000Z', '21:45:00.000Z', '23:45:00.000Z']
curr = datetime(2026, 10, 6)
all_122_slots = []
while len(all_122_slots) < 122:
    day_str = curr.strftime('%Y-%m-%d')
    for t in candidate_times:
        slot_iso = f'{day_str}T{t}'
        if slot_iso not in existing_due:
            all_122_slots.append(slot_iso)
            if len(all_122_slots) == 122:
                break
    curr += timedelta(days=1)

def get_slot_name(iso_str):
    dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    mdt_dt = dt - timedelta(hours=6)
    day_name = mdt_dt.strftime('%A')
    time_str = mdt_dt.strftime('%I:%M %p')
    return f"{day_name} ({time_str} MDT)"

def generate_script(campaign_name, slug, posts_raw, start_idx, filename, report_name):
    posts_data = []
    for idx, p in enumerate(posts_raw):
        slot_idx = start_idx + idx
        due_at = all_122_slots[slot_idx]
        slot_name = get_slot_name(due_at)
        asset_file = f"{slug}-{idx+1:02d}.png"
        asset_url = f"https://lornettedaye.com/campaigns/{slug}/{asset_file}"
        
        # Verify zero em dashes
        t = p["text"]
        assert "—" not in t, f"Post #{p['id']} in {campaign_name} contains em dash —"
        assert "\u2014" not in t, f"Post #{p['id']} in {campaign_name} contains unicode em dash"
        assert "&mdash;" not in t, f"Post #{p['id']} in {campaign_name} contains &mdash;"
        
        posts_data.append({
            "id": p["id"],
            "slot": slot_name,
            "dueAt": due_at,
            "assetFile": asset_file,
            "assetUrl": asset_url,
            "cta": p["cta"],
            "text": t
        })
        
    script_content = f'''# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for {campaign_name} ({len(posts_data)} Posts)
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
    print("{campaign_name} ({len(posts_data)} POSTS)")
    print(f"Target Channel: {{CHANNEL_ID}} (Lornette Daye LinkedIn)")
    print(f"Time: {{time.strftime('%Y-%m-%d %H:%M:%S')}}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "{report_name}")
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
    print(f"Summary: {{success_count}}/{len(posts_data)} posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
'''
    with open(os.path.join("scripts", filename), "w", encoding="utf-8") as f:
        f.write(script_content)
    print(f"Generated scripts/{filename} successfully ({len(posts_data)} posts).")

# ==========================================
# CAMPAIGN 5: NBA (3 Posts) - slots 65 to 67
# ==========================================
nba_posts = [
    {
        "id": 1,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "ANTHONY EDWARDS: THE NEXT LEVEL ALWAYS DEMANDS MORE. 🐺🏀\n\n"
            "Talent gets you noticed. Growth keeps you there.\n\n"
            "When Anthony Edwards entered the NBA, his raw physical explosion and charisma were undeniable. "
            "Yet what separates an exciting young talent from an MVP contender is the relentless appetite to refine weaknesses. "
            "Edwards overhauled his catch-and-shoot mechanics, dedicated himself to lock-down perimeter defense, "
            "and learned how to control game tempo in the closing four minutes.\n\n"
            "In four decades coaching Olympic athletes, I tell champions: the hardest part of success is not arriving. "
            "It is answering the elevated demand of the room you just entered.\n\n"
            "Leaders: What part of your professional craft needs to elevate to meet your next opportunity?\n\n"
            "👉 Discover how Olympic-level self-assessment builds unstoppable career momentum. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#AnthonyEdwards #MinnesotaTimberwolves #TheNextLevel #FinishStrong #OlympicMindset #GrowthMindset #LornetteDaye"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "DISCIPLINE BUILDS FREEDOM: COMMANDING THE ARENA IN MINNEAPOLIS. 🌲⚡\n\n"
            "True athletic freedom looks effortless, but it is anchored in ruthless discipline.\n\n"
            "When you watch Anthony Edwards drive into the lane, elevate above rim protectors, and absorb contact, "
            "you are witnessing core strength, deceleration mechanics, and kinetic control forged through thousands of invisible repetitions. "
            "Freedom on the court is not reckless abandonment; it is the privilege of complete physical preparation.\n\n"
            "Athletes: Are you putting in the quiet conditioning required to make pressure situations feel effortless?\n\n"
            "👉 Build a champion mindset, focus, and recovery systems on and off the court. "
            "Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#DisciplineBuildsFreedom #AntMan #WolvesHoops #SurvivalSkillsForAthletes #OlympicCoach #PhysicalResilience #LornetteDaye"
        )
    },
    {
        "id": 3,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "DIFFERENT GENERATIONS. SAME GOAL: EMBIID & EDGECOMBE IN PHILADELPHIA. 🔔🏙️\n\n"
            "Championship culture bridges the gap between veteran mastery and youthful energy.\n\n"
            "Joel Embiid brings MVP experience, leadership presence, and tactical authority. "
            "VJ Edgecombe brings explosive rookie athleticism, fierce hunger, and modern speed. "
            "When an organization aligns the wisdom of established leadership with the vitality of the next generation, "
            "dynasties take root.\n\n"
            "In corporate enterprises, senior executives must mentor rising talent without feeling threatened, "
            "and emerging leaders must honor institutional knowledge without losing their innovative edge.\n\n"
            "Executives: How effectively is your organization bridging the generational divide to drive collective victory?\n\n"
            "👉 Align multi-generational teams to perform at peak capacity with Olympic team-building frameworks. "
            "Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n"
            "#Philadelphia76ers #JoelEmbiid #VJEdgecombe #GenerationalLeadership #ExecutivePerformance #CoachLornette"
        )
    }
]

# ==========================================
# CAMPAIGN 6: CRICKET (14 Posts) - slots 68 to 81
# ==========================================
cricket_posts = [
    {
        "id": 1,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "SOMETIMES THE NEXT LEVEL IS ONE CONVERSATION AWAY. 🏏🏴󠁧󠁢󠁥󠁮󠁧󠁿\n\n"
            "A champion can still need a mentor. A captain can still be coached. A great athlete can still learn.\n\n"
            "When Harry Brook sat down with legendary English batsman Kevin Pietersen on the boundary wall at Lord's, "
            "he wasn't looking for swing analysis. He was seeking psychological insight into commanding the international stage. "
            "Greatness is never too proud to seek counsel from those who walked the path before them.\n\n"
            "In four decades coaching Olympic champions, I have seen careers transformed by a single conversation with the right mentor.\n\n"
            "Athletes and leaders: Who is speaking wisdom into your preparation today?\n\n"
            "👉 Discover how humility and world-class mentorship unlock your true competitive ceiling. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HarryBrook #KevinPietersen #EnglandCricket #MentorshipInSport #FinishStrong #OlympicMindset #CoachLornette"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "NEVER BECOME TOO GOOD TO BE TAUGHT. 🧢📚\n\n"
            "The moment an athlete believes they have arrived is the precise moment their decline begins.\n\n"
            "Harry Brook has established himself as one of the most destructive young batsmen in world cricket. "
            "Yet watch his practice sessions: he asks questions, listens intently to coaches, and analyzes deliveries with student curiosity. "
            "Ego closes the mind; coachability expands your capacity.\n\n"
            "Athletes: When was the last time you asked for critical feedback on your technique?\n\n"
            "👉 Build an enduring champion mindset that remains coachable in every season. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#Coachability #HarryBrook #CricketExcellence #SurvivalSkillsForAthletes #OlympicStandards #LifelongLearner #LornetteDaye"
        )
    },
    {
        "id": 3,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "BETTER PEOPLE BUILD BRIGHTER PLAYERS: THE ETHOS OF TEST CRICKET. 🏛️☀️\n\n"
            "Test cricket spans five days in the blazing sun. It tests human patience, dignity, and moral stamina.\n\n"
            "In our performance framework, athletic development is never separate from character development. "
            "When an athlete learns emotional regulation, respectful presence, and quiet resilience, "
            "their on-field performance becomes steady, reliable, and unbreakable under immense match pressure.\n\n"
            "Executives: Are you investing in technical training alone, or building the character foundation of your workforce?\n\n"
            "👉 Elevate your corporate culture with Olympic coaching that builds high-integrity, high-execution teams. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#BetterPeopleBetterPlayers #TestCricket #ExecutiveCulture #IntegrityUnderPressure #CoachLornette #LeadershipDevelopment"
        )
    },
    {
        "id": 4,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "DISCIPLINE. CONVERSATION. PROGRESS. A BRIGHTER TOMORROW. 🌅🏏\n\n"
            "Small conversations held in quiet corners often yield the greatest competitive breakthroughs.\n\n"
            "Watching the masters of cricket exchange insights on the boundary teaches us that connection is an essential ingredient of performance. "
            "We are not meant to battle through demanding seasons in isolation. "
            "Opening up to a trusted voice can illuminate the exact adjustment you need to make.\n\n"
            "Readers: Is there an area of life where you need to reach out and seek guidance instead of struggling alone?\n\n"
            "👉 Rebuild confidence, find encouragement, and gain fresh perspective in hard chapters. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#DisciplineAndProgress #SurvivingLife #ConnectionInSport #CricketWisdom #OlympicCoach #HopeAndPerspective #LornetteDaye"
        )
    },
    {
        "id": 5,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "114 NOT OUT OFF 49 BALLS: EXPLOSIVE IMPACT BORN IN PATIENT STUDY. ⚡🏏\n\n"
            "Harry Brook exploded against Sri Lanka with a breathtaking century off just forty-nine deliveries. "
            "Spectators saw fireworks; coaches saw hours of meticulous video study, weight-shift analysis, and tactical courage. "
            "Violent speed on the field is always born from deep clarity in the mind.\n\n"
            "When preparation removes doubt, execution becomes ferocious and free.\n\n"
            "Leaders: Is your team prepared to capitalize with total conviction when opportunity opens up?\n\n"
            "👉 Master the habits of elite finishers who seize the moment without hesitation. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HarryBrook #114NotOut #ExplosiveBatting #FinishStrong #CricketHighlights #PreparationIsEverything #LornetteDaye"
        )
    },
    {
        "id": 6,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "TALENT OPENS DOORS. COACHABILITY KEEPS THEM OPEN. 🚪🔑\n\n"
            "Natural hand-eye coordination will earn an athlete an international debut. "
            "Only coachability will keep them in the international lineup for a decade.\n\n"
            "Opposing bowlers adjust their fields and line of attack after every single innings. "
            "If a batsman is stubborn and unwilling to tweak their stance or trigger movements, "
            "international competition will expose them ruthlessly. Adaptability is survival.\n\n"
            "Athletes: Are you willing to dismantle a comfortable habit to achieve a higher standard?\n\n"
            "👉 Develop mental adaptability, tactical poise, and focus under pressure. "
            "Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#CoachabilityWins #CricketTactics #SurvivalSkillsForAthletes #OlympicMindset #AdaptOrDecline #LornetteDaye"
        )
    },
    {
        "id": 7,
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": (
            "YOUNG TALENT. BRIGHTER TOMORROWS: NAVIGATING SUDDEN ACCLAIM. 🌟🏏\n\n"
            "Handling failure is hard; handling overnight acclaim without losing your head is even harder.\n\n"
            "When a young player scores record-breaking hundreds, media praise and lucrative sponsorship contracts arrive instantly. "
            "The challenge for young men is keeping their circle grounded, their routines sacred, and their focus locked on the game. "
            "Do not let the noise outside enter your preparation sanctuary.\n\n"
            "Men: How are you guarding your personal routines against the distractions of external attention?\n\n"
            "👉 Build steady habits, emotional discipline, and balanced perspective through seasons of growth. "
            "Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #GroundedLeadership #HandlingSuccess #CricketEngland #MenWhoLead #CoachLornette"
        )
    },
    {
        "id": 8,
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "18 HUNDREDS. 18 HUNDREDS. ONE NEW STANDARD. 🇿🇦🇮🇳👑\n\n"
            "When women raise the bar, the entire sporting world moves forward.\n\n"
            "Laura Wolvaardt of South Africa and Smriti Mandhana of India: two masterclasses in batting elegance and power. "
            "Wolvaardt drawing level with Mandhana for the most international hundreds in women's cricket history. "
            "Two distinct nations, two extraordinary batting journeys, united by an unyielding commitment to world-class precision.\n\n"
            "In Olympic athletics, we celebrate pioneers who do not simply break records; they expand what future generations believe is possible.\n\n"
            "Women: What boundary in your industry are you tearing down through your daily excellence?\n\n"
            "👉 Build unshakable confidence, identity, and resilience across every stage of your journey. "
            "Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#LauraWolvaardt #SmritiMandhana #WomensCricket #18Hundreds #SurvivalSkillsForWomen #OlympicStandard #GlobalExcellence #LornetteDaye"
        )
    },
    {
        "id": 9,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE BEAUTY OF THE COVER DRIVE: TECHNICAL PURITY UNDER PRESSURE. 🏏✨\n\n"
            "Few sights in global sport rival the cover drive of Laura Wolvaardt or Smriti Mandhana.\n\n"
            "High elbow, head balanced directly over the ball, smooth follow-through, and effortless placement through the covers. "
            "That purity of stroke play is not accidental. It is the mathematical reward of tens of thousands of throwdowns "
            "in batting nets from Potchefstroom to Mumbai. Technical perfection delivers its own protection under pressure.\n\n"
            "When your technique is sound, you do not need frantic effort. You let the ball meet the sweet spot.\n\n"
            "Professionals: Are you polishing the fundamentals of your craft until they shine effortlessly?\n\n"
            "👉 Master the discipline of technical excellence and learn how to finish strong. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#CoverDrive #TechnicalPurity #SmritiMandhana #LauraWolvaardt #FinishStrong #OlympicDiscipline #LornetteDaye"
        )
    },
    {
        "id": 10,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "GLOBAL EXPANSION: WOMEN'S SPORT REWRITING ECONOMIC REALITY. 🌍📈\n\n"
            "The explosion of the Women's Premier League (WPL) and international women's cricket is an economic revolution.\n\n"
            "Record television viewership, sold-out stadiums across India, and historic commercial partnerships. "
            "Athletes like Mandhana and Wolvaardt are proving that when you deliver elite athletic performance, "
            "global audiences and corporate capital will respond in massive numbers.\n\n"
            "Executive leadership teams that champion women's excellence build stronger, more resilient global organizations.\n\n"
            "Executives: Are you investing in the transformative power of women's leadership in your sector?\n\n"
            "👉 Inspire your executive organization with high-performance keynote strategies from an Olympic champion coach. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#WomensSportEconomy #WPL #GlobalLeadership #ExecutiveStrategy #CoachLornette #EconomicEmpowerment"
        )
    },
    {
        "id": 11,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "EXCELLENCE HAS NO BORDERS: FROM SOUTH AFRICA TO INDIA. 🇿🇦🇮🇳\n\n"
            "Sport is the universal bridge that connects diverse cultures through shared respect.\n\n"
            "Despite different backgrounds, different pitches, and different languages, Laura Wolvaardt and Smriti Mandhana "
            "share the same heartbeat: the relentless pursuit of mastery with a bat in hand. "
            "When opponents respect each other's work, competition elevates everyone.\n\n"
            "Readers: How can you build bridges of mutual respect with colleagues across different backgrounds today?\n\n"
            "👉 Discover encouragement, renewed hope, and perspective for navigating life with grace. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ExcellenceHasNoBorders #CricketUnites #SurvivingLife #MutualRespect #OlympicSpirit #LornetteDaye"
        )
    },
    {
        "id": 12,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "BATTING THROUGH THE NERVOUS NINETIES: MENTAL POISE AT THE THRESHOLD. 🎯🏏\n\n"
            "Every cricketer knows the psychological terror of batting on ninety-five.\n\n"
            "Your century is five runs away. The stadium is on its feet. Your pulse quickens. "
            "This is where ordinary players play a reckless shot and throw away hours of disciplined labor. "
            "To reach eighteen international hundreds, you must treat ninety-nine with the exact same calm process as zero.\n\n"
            "Athletes: Can you maintain your emotional discipline when you are right on the verge of a breakthrough?\n\n"
            "👉 Learn how to regulate pressure and finish your achievements with champion calm. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#NervousNineties #CenturyMakers #MentalPoise #SurvivalSkillsForAthletes #OlympicMentalToughness #LornetteDaye"
        )
    },
    {
        "id": 13,
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "MORE WOMEN. HIGHER POSSIBILITIES: INSPIRING A CONTINENT. 🌏👑\n\n"
            "When Smriti Mandhana drives through extra cover or Laura Wolvaardt cuts backward of point, "
            "millions of girls in Delhi, Cape Town, and beyond see proof that their ambitions are valid.\n\n"
            "Visibility is the catalyst of aspiration. When women see women excelling on global stages, "
            "the mental limits of what is possible vanish.\n\n"
            "Women: Never underestimate the quiet impact your courage and competence have on those watching you from afar.\n\n"
            "👉 Step boldly into your purpose with practical tools for resilience and leadership. "
            "Read Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#MoreWomenHigherPossibilities #WomensCricket #InspireTheNext #SurvivalSkillsForWomen #OlympicLegacy #CoachLornette"
        )
    },
    {
        "id": 14,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE ENDURING HERITAGE OF CRICKET: FINISHING STRONG ACROSS INNINGS. 🏆🏏\n\n"
            "Whether it is Harry Brook's fearless stroke play or Wolvaardt and Mandhana rewriting the century record books, "
            "international cricket reminds us of a timeless truth: talent gets you into the stadium, "
            "but patience, humility, and disciplined preparation decide how you finish.\n\n"
            "Step up to your crease today with purpose. Respect the delivery. Trust your training. Finish strong.\n\n"
            "👉 Master the habits of elite athletes who turn pressure into enduring legacy. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#CricketHeritage #FinishStrong #GlobalAthletes #OlympicMindset #PlayYourBest #LornetteDaye #ExcellenceInSport"
        )
    }
]

# ==========================================
# CAMPAIGN 7: SITAYA FAGAN (10 Posts) - slots 82 to 91
# ==========================================
sitaya_posts = [
    {
        "id": 1,
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "USC SITAYA HAS ARRIVED: FROM MELBOURNE TO LOS ANGELES. ✌️🏀🇦🇺\n\n"
            "USC's 6 foot 4 freshman forward brings international pedigree and major upside.\n\n"
            "Crossing the Pacific Ocean from Australia to join the elite women's basketball program at USC "
            "is a massive athletic transition. Sitaya Fagan brings size, mobility, court vision, and Australian national team grit "
            "to the Galen Center. She arrives ready to contribute to a championship culture.\n\n"
            "In four decades coaching Olympic athletes, international transitions test two things: "
            "your cultural adaptability and the depth of your personal foundation.\n\n"
            "Young athletes: Are you prepared to carry your talent across borders and make your presence felt?\n\n"
            "👉 Build grounded identity, resilience, and confidence through major life transitions. "
            "Read Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SitayaFagan #USCWBB #FightOn #MelbourneToLA #AussieHoops #SurvivalSkillsForWomen #OlympicCoach #LornetteDaye"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "THE 6'4\" FORWARD: COMBINING LENGTH, SPEED, AND RIM PROTECTION. 🛡️🏀\n\n"
            "Modern basketball demands versatile size that can switch on the perimeter and protect the rim.\n\n"
            "Sitaya Fagan's ability to run the floor in transition, contest shots without fouling, "
            "and rebound out of her area provides USC with an extraordinary tactical advantage. "
            "Length is a physical gift; rim-protection timing is a product of disciplined film study and footwork.\n\n"
            "Athletes: Are you relying purely on natural physical attributes, or sharpening your tactical positioning?\n\n"
            "👉 Build champion focus, discipline systems, and high performance habits. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#RimProtection #SitayaFagan #USCFreshman #SurvivalSkillsForAthletes #DefensiveMastery #OlympicStandard #LornetteDaye"
        )
    },
    {
        "id": 3,
        "cta": "Survival Skills for Students ($14.99 CAD)",
        "text": (
            "STUDENT-ATHLETE MATURITY: NAVIGATING LIFE TWELVE THOUSAND MILES FROM HOME. ✈️📚\n\n"
            "Moving twelve thousand miles away from family at age eighteen to pursue collegiate athletics demands profound maturity.\n\n"
            "Adjusting to American college life, rigorous Big Ten athletic travel, and high academic expectations "
            "requires emotional self-reliance. Sitaya Fagan is proving that with proper structure and supportive community, "
            "distance becomes the crucible where independent leaders are forged.\n\n"
            "Students and parents: Are you building systems to help young people thrive when away from home?\n\n"
            "👉 Practical strategies for student focus, healthy habits, and academic-athletic balance. "
            "Read Survival Skills for Students ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForStudents #InternationalStudentAthlete #SitayaFagan #BigTenHoops #EmotionalIndependence #LornetteDaye"
        )
    },
    {
        "id": 4,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "LOS ANGELES BUILDS DIFFERENT: THE ELITE PRESSURE OF TROJAN TRADITION. ✌️🌟\n\n"
            "Wearing number 1 for USC Women's Basketball is an honor that demands a daily standard.\n\n"
            "From Cheryl Miller and Lisa Leslie to modern Trojan stars, the legacy of greatness in Los Angeles is everywhere. "
            "Sitaya Fagan does not run from that standard; she embraces it. "
            "Great athletes understand that pressure from legendary predecessors is an invitation to rise.\n\n"
            "Leaders: Do you see historical standards as an intimidating burden or an inspiring benchmark?\n\n"
            "👉 Discover how Olympic-level competitors embrace legacy and finish strong. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#USCLegacy #TrojanHeritage #SitayaFagan #FinishStrong #HighStandards #OlympicMindset #CoachLornette"
        )
    },
    {
        "id": 5,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "MORE THAN A GAME: A BRIGHTER TOMORROW BUILDS TODAY. 🌅🤝\n\n"
            "Basketball is what you play; it is never who you are.\n\n"
            "Sitaya Fagan's journey from junior leagues in Victoria, Australia to collegiate basketball in the United States "
            "is driven by family support, faith, and a deep appreciation for the opportunities sport provides. "
            "When young athletes keep their identity anchored in character, on-court setbacks cannot shake their inner peace.\n\n"
            "Readers: How does keeping perspective on what matters most protect your joy during stressful seasons?\n\n"
            "👉 Find encouragement, strength in transition, and renewed hope for your path. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#IdentityBeyondSport #SurvivingLife #SitayaFagan #AussieAthletes #PerspectiveInPressure #LornetteDaye"
        )
    },
    {
        "id": 6,
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "WOMEN BUILD BRIGHTER: THE RISE OF AUSTRALIAN BASKETBALL TALENT. 🇦🇺🏀\n\n"
            "Australia has long produced world-class basketball talent, and the next wave of female stars is exceptional.\n\n"
            "From the WNBL to the Opals and now NCAA Division I, young Australian women are demonstrating physical poise, "
            "unselfish team play, and tough defensive identity on global courts. Sitaya Fagan represents that fierce Aussie pedigree.\n\n"
            "Women: Celebrate the unique strengths your heritage brings to your professional arena.\n\n"
            "👉 Rebuild confidence, thrive with purpose, and discover practical tools for personal growth. "
            "Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#WomenBuildBrighter #AustralianBasketball #SitayaFagan #OpalsFuture #SurvivalSkillsForWomen #CoachLornette"
        )
    },
    {
        "id": 7,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "THE POWER OF FOOTWORK: MASTERING LOW-POST POSITIONING. 👣🏀\n\n"
            "Size creates potential, but footwork creates points.\n\n"
            "Sitaya Fagan's ability to seal defenders, drop step, and establish deep post position before the entry pass arrives "
            "is the mark of high-level coaching. When a post player wins the positioning battle early, the finish becomes simple.\n\n"
            "In athletics and business, win the position before the play develops, and the outcome will take care of itself.\n\n"
            "Athletes: Are you winning the preliminary positioning battle before trying to make the play?\n\n"
            "👉 Strengthen your fundamental athletic habits and mental poise. "
            "Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#PostFootwork #SitayaFagan #FundamentalSkills #SurvivalSkillsForAthletes #OlympicCoaching #LornetteDaye"
        )
    },
    {
        "id": 8,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "FIGHT ON: RESILIENCE IN THE CRUCIBLE OF BIG TEN PLAY. ✌️⚔️\n\n"
            "The Big Ten conference is physical, grinding, and relentlessly competitive on the glass.\n\n"
            "Freshman forwards must adjust to relentless physical contact on every rebound and box out. "
            "Sitaya Fagan's willingness to fight for inside position and battle through contact reveals an athlete "
            "who does not back down from physical challenge. Trojan resilience is forged in the paint.\n\n"
            "Leaders: Does your team back away from intense competition, or lean into the contact?\n\n"
            "👉 Master the mindset of championship competitors who embrace the struggle and finish strong. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FightOn #BigTenBasketball #SitayaFagan #ResilienceInSport #FinishStrong #OlympicMindset #LornetteDaye"
        )
    },
    {
        "id": 9,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "GLOBAL TALENT PIPELINES: LESSONS FROM INTERNATIONAL RECRUITING. 🌏🏢\n\n"
            "Modern elite sports organizations scout worldwide to find unique talent that complements their domestic roster.\n\n"
            "USC bringing Sitaya Fagan from Melbourne illustrates the global nature of modern talent identification. "
            "Organizations that expand their scouting horizons beyond geographic borders assemble richer, more versatile teams.\n\n"
            "Executives: Are your recruiting strategies discovering global perspective, or confined to traditional local pools?\n\n"
            "👉 Transform your organizational talent acquisition and leadership culture with Olympic principles. "
            "Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n"
            "#GlobalTalent #InternationalScouting #ExecutiveLeadership #CrossBorderExcellence #CoachLornette"
        )
    },
    {
        "id": 10,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE ARRIVAL IS JUST THE START: BUILDING A FOUR-YEAR TROJAN LEGACY. 👑✌️\n\n"
            "Arriving at USC is an incredible milestone, but the destination is four years of championship building.\n\n"
            "Sitaya Fagan has the size, the skill, and the international foundation to become a cornerstone of USC basketball. "
            "Those who build enduring legacies are the ones who treat freshman arrival not as a celebration, "
            "but as the opening rep of an exhaustive four-year masterclass.\n\n"
            "Stay humble. Stay hungry. Honor the work. Finish strong.\n\n"
            "👉 Master the habits of elite athletes who transform raw potential into lasting legacy. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SitayaFagan #TrojanFamily #USCForward #FinishStrong #OlympicStandards #LornetteDaye #MasteryInAction"
        )
    }
]

# ==========================================
# CAMPAIGN 8: TYRESE GIBSON (12 Posts) - slots 92 to 103
# ==========================================
tyrese_posts = [
    {
        "id": 1,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "THE BOY ON THE BUS KEPT GOING: DON'T LET ONE CHAPTER CONVINCE YOU THE BOOK IS FINISHED. 🚌📖\n\n"
            "Watts. Coca-Cola commercial. R&B chart-toppers. Hollywood blockbuster franchises. Fatherhood. Loss. Reinvention.\n\n"
            "More than three decades after singing on that city bus in Watts, Tyrese Gibson is still here. "
            "Still creating. Still fighting. Still standing. He has walked through seasons of intense public praise "
            "and seasons of devastating personal heartbreak. Through every chapter, he refused to close the book.\n\n"
            "In forty years of coaching elite performers, I know that resilience is not the absence of tears. "
            "It is the stubborn refusal to surrender your pen when life writes a painful sentence.\n\n"
            "Readers: What difficult chapter are you living through right now that needs a courageous next page?\n\n"
            "👉 Find renewed strength, emotional perspective, and hope through life's hardest transitions. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TyreseGibson #TheBoyOnTheBus #DontGiveUp #SurvivingLife #CreativeResilience #HopeAfterLoss #LornetteDaye"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": (
            "VULNERABILITY IS NOT WEAKNESS: THE COURAGE OF EMOTIONAL HONESTY. 🛡️💔\n\n"
            "Men are frequently taught that emotional suppression is strength. In truth, buried pain poisons the soul.\n\n"
            "Tyrese Gibson has stood in front of global audiences and spoken with raw honesty about grief, depression, "
            "fatherhood battles, and the ache of losing brothers like John Singleton and Paul Walker. "
            "Speaking your pain out loud takes far more courage than pretending you are unbreakable.\n\n"
            "When men learn to acknowledge their wounds without losing their dignity, true healing and leadership begin.\n\n"
            "Men: Are you carrying grief in silence, or seeking the brotherhood that helps you bear the weight?\n\n"
            "👉 Build emotional resilience, personal clarity, and steady balance in demanding seasons. "
            "Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #Tyrese #EmotionalResilience #MenAndGrief #AuthenticLeadership #CoachLornette"
        )
    },
    {
        "id": 3,
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": (
            "WATTS ROOTS: SURVIVING TO THRIVING ACROSS THREE DECADES. 🏙️🔥\n\n"
            "You cannot choose where you start, but you can choose what you do with your opportunity.\n\n"
            "Growing up in Watts, Los Angeles during an era of extreme systemic violence, survival was a daily assignment. "
            "Tyrese channeled his pain into melodies, his drive into auditions, and his survival instincts into a multi-decade Hollywood career. "
            "He moved beyond survival mode and built a life of creative momentum.\n\n"
            "Professionals: Are you still trapped in survival instincts, or intentionally building a foundation to thrive?\n\n"
            "👉 Identify what is holding you back and step into purpose-driven growth. "
            "Read Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n"
            "#WattsToHollywood #SurvivingToThriving #TyreseGibson #OvercomingEnvironment #PurposeDrivenMomentum #LornetteDaye"
        )
    },
    {
        "id": 4,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE FAST FRANCHISE ENDURANCE: TWENTY YEARS OF BLOCKBUSTER EXECUTION. 🎬🏎️\n\n"
            "A hit film is an achievement; sustaining a role in a multi-billion-dollar franchise over twenty years is endurance.\n\n"
            "From 2 Fast 2 Furious in 2003 through ten installments, Tyrese has been a central pillar of global cinema. "
            "Long production schedules, intense physical demands, and global promotional tours require high physical stamina "
            "and unwavering professional reliability on set.\n\n"
            "In Olympic athletics, we celebrate those who do not just run one fast lap, but hold their pace over marathon distances.\n\n"
            "Leaders: Is your professional stamina built for a two-decade marathon?\n\n"
            "👉 Master the stamina and mindset of world-class finishers. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FastAndFurious #TyreseGibson #ProfessionalEndurance #FinishStrong #OlympicPacing #LornetteDaye #LongevityInFilm"
        )
    },
    {
        "id": 5,
        "cta": "Survival Skills for Believers ($14.99 CAD)",
        "text": (
            "FAITH IN THE VALLEY: ANCHORING YOUR SOUL WHEN STORMS RAGE. ⚓🙏\n\n"
            "It is easy to give praise on the mountain peak. The measure of your faith is whether you worship in the valley.\n\n"
            "Through every court battle, every public misunderstanding, and every season of sorrow, Tyrese has consistently "
            "testified to the grace and mercy of God. He knows that external fame cannot heal an aching spirit; only an anchor in Christ "
            "provides peace that surpasses human understanding.\n\n"
            "Believers: When your life's circumstances seem dark, where is your anchor dropped?\n\n"
            "👉 Navigate life's hardest chapters with scripture-backed wisdom, grace, and unshakable faith. "
            "Explore Survival Skills for Believers ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SurvivalSkillsForBelievers #TyreseFaith #FaithInTheValley #AnchorOfHope #PeaceInTheStorm #LornetteDaye"
        )
    },
    {
        "id": 6,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "FATHERHOOD AS SACRED CALLING: LEAVING A LEGACY OF LOVE. 👨‍👧❤️\n\n"
            "The red carpets will eventually roll up. The most important title you will ever hold is Father.\n\n"
            "Watch Tyrese talk about his daughters and you see a man whose fierce devotion to fatherhood transcends all Hollywood glamour. "
            "He fights for their presence, their security, and their joy. Great leadership begins in the living room, "
            "not the boardroom.\n\n"
            "Men and parents: Are you investing your deepest presence in the children who look up to you?\n\n"
            "👉 Build lasting family foundations, emotional warmth, and perspective that endures. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FatherhoodFirst #TyreseGibson #FamilyLegacy #SurvivingLife #ProtectingTheNextGeneration #LornetteDaye"
        )
    },
    {
        "id": 7,
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": (
            "THE DISCIPLINE OF REINVENTION: NEVER LETTING CRITICS FREEZE YOUR GROWTH. 🔄🎤\n\n"
            "When critics attempt to pigeonhole you into a single lane, keep expanding your canvas.\n\n"
            "From billboard-topping soul music to comedy, action cinema, authoring New York Times bestsellers, and producing films, "
            "Tyrese has refused to let outside opinions define his boundaries. Reinvention is not fleeing yourself; "
            "it is unlocking the multifaceted gifts God placed inside you.\n\n"
            "Men: What dormant gift have you neglected because you feared what critics might say?\n\n"
            "👉 Reclaim your focus, balance, and creative courage in every season of life. "
            "Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n"
            "#Reinvention #Tyrese #MultifacetedCreativity #SurvivalSkillsForMen #MenWhoLead #OlympicCourage #LornetteDaye"
        )
    },
    {
        "id": 8,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "AUTHENTIC STORYTELLING: BUILDING EMOTIONAL BRIDGES WITH AUDIENCES. 🎙️🌟\n\n"
            "In an era of generic corporate scripts, authenticity is the rarest and most valuable currency.\n\n"
            "Whether Tyrese is singing a ballad or speaking to an auditorium, people connect because they feel his humanity. "
            "He does not hide his flaws behind polished public relations veneers. "
            "Leaders who dare to be authentic generate immediate trust and fierce loyalty.\n\n"
            "Executives: Does your corporate communication feel manufactured, or does it resonate with genuine human authority?\n\n"
            "👉 Train your leadership team to communicate with authentic emotional resonance and executive poise. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#AuthenticCommunication #ExecutiveResonance #TyreseStyle #HumanLeadership #CoachLornette"
        )
    },
    {
        "id": 9,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "GRIEF AND RECOVERY: HONORING BROTHERS GONE TOO SOON. 🕊️🖤\n\n"
            "Losing beloved friends leaves hollow places that time alone cannot fill.\n\n"
            "Tyrese has openly mourned Paul Walker, John Singleton, and his dear mother Priscilla Murray. "
            "Yet his tribute to them has not been surrender; it has been continuing their legacy of generosity, passion, "
            "and unrelenting creative commitment. The greatest honor you can give to the departed is to live fully.\n\n"
            "Readers: If you are walking through the shadow of loss, know that your life still holds profound purpose.\n\n"
            "👉 Find comfort, rebuilding tools, and practical encouragement for seasons of heavy grief. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#GriefAndHealing #PaulWalkerLegacy #JohnSingleton #SurvivingLife #HonoringThoseWeLost #LornetteDaye"
        )
    },
    {
        "id": 10,
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": (
            "CREATIVE INDEPENDENCE: OWNING YOUR MASTERS AND YOUR FUTURE. 💼🎶\n\n"
            "Do not spend your entire life building another person's empire while leaving your own barren.\n\n"
            "Tyrese's transition into independent music distribution and film production demonstrates an artist "
            "who understands intellectual property. When you own your masters, your creative vision remains uncompromised "
            "and your economic legacy is secured for your children.\n\n"
            "Professionals: Are you building true ownership and equity in your craft, or simply renting your labor?\n\n"
            "👉 Move beyond survival mode and construct lasting economic and creative independence. "
            "Explore Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n"
            "#OwnershipOverRenting #CreativeIndependence #Tyrese #SurvivingToThriving #BuildingEquity #LornetteDaye"
        )
    },
    {
        "id": 11,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE GRIND NEVER SLEEPS: RETURNING TO THE STUDIO AFTER MIDNIGHT. 🎹🌙\n\n"
            "When other people are sleeping, true artists are searching for the chord that moves the soul.\n\n"
            "Watch Tyrese in the recording studio at 2:00 AM, working vocal harmonies with live musicians, "
            "refusing to settle for autotune shortcuts. Soul music requires soul investment. "
            "When you put genuine craftsmanship into your product, it never goes out of style.\n\n"
            "Leaders: Are you taking shortcuts in your deliverables, or sweating the craftsmanship?\n\n"
            "👉 Build the obsessive work ethic of champions who take pride in every detail. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#Craftsmanship #StudioGrind #TyreseMusic #FinishStrong #OlympicStandards #NoShortcuts #CoachLornette"
        )
    },
    {
        "id": 12,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "MORE THAN THREE DECADES LATER: THE STORY IS STILL BEING WRITTEN. 🌅👑\n\n"
            "Never let the world write your obituary while breath is still in your lungs.\n\n"
            "Tyrese Gibson's journey is a testament to the stubborn resilience of the human spirit. "
            "From an impoverished bus seat in South Central Los Angeles to international movie premieres and Grammy nominations, "
            "he proves that when you refuse to quit, God writes chapters you never could have planned.\n\n"
            "Whatever chapter you find yourself in today, take heart: pick up your pen, hold your head high, and finish strong.\n\n"
            "👉 Discover how to finish your race with purpose, faith, and enduring legacy. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TheStoryContinues #TyreseGibson #NeverGiveUp #FinishStrong #OlympicSpirit #FaithAndEndurance #LornetteDaye"
        )
    }
]

# ==========================================
# CAMPAIGN 9: YAROSLAVA MAHUCHIKH (8 Posts) - slots 104 to 111
# ==========================================
yaroslava_posts = [
    {
        "id": 1,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE BAR KEEPS MOVING. SO DOES SHE. 🇺🇦🥇\n\n"
            "Yaroslava Mahuchikh: Olympic Champion. World Record Holder. 2.10 Meters.\n\n"
            "For thirty-seven years, Stefka Kostadinova's legendary women's high jump world record of 2.09 meters "
            "stood as an unreachable summit in track and field. Experts claimed human biomechanics had met their limit. "
            "Then, on a sunlit afternoon in Paris, twenty-two-year-old Yaroslava Mahuchikh cleared 2.10 meters with millimeter perfection.\n\n"
            "In four decades coaching Olympic athletes, I know that human limits exist only until someone with extraordinary technical discipline "
            "and emotional poise dares to raise the bar.\n\n"
            "Leaders: What 'impossible' ceiling in your field are you ready to shatter?\n\n"
            "👉 Discover how world-class competitors break barriers and finish strong. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#YaroslavaMahuchikh #WorldRecord210 #HighJumpQueen #OlympicChampion #FinishStrong #UkraineStrong #LornetteDaye"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "SLEEPING BETWEEN JUMPS: THE ULTIMATE LESSON IN ATHLETIC RECOVERY. 🛌🧘‍♀️\n\n"
            "While rivals pace nervously, bite their nails, and burn vital adrenaline, Yaroslava climbs into a green sleeping bag.\n\n"
            "She lies flat on her back next to the high jump mat, puts a jacket over her eyes, and sleeps between competition heights. "
            "That is not theatrical indifference. It is world-class autonomic nervous system regulation. "
            "She brings her heart rate down to resting levels, conserves energy, and wakes up only when the bar is raised.\n\n"
            "Athletes: Can you switch off competition stress between attempts to conserve your explosive power?\n\n"
            "👉 Master physiological regulation, visualization, and recovery routines. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SleepingBagRoutine #HighJumpPoise #Mahuchikh #SurvivalSkillsForAthletes #ParasympatheticReset #OlympicCoach #LornetteDaye"
        )
    },
    {
        "id": 3,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "JUMPING UNDER WAR: COMPETING WHEN YOUR HOMELAND IS UNDER FIRE. 🇺🇦🕊️\n\n"
            "Competing on the world stage is hard. Competing while your family endures missile strikes in Dnipro is heroic.\n\n"
            "Yaroslava Mahuchikh fled Russian artillery in a car, traveled three days across Europe, and won the World Indoor Championship "
            "within weeks. She jumps not for personal glory, but to remind the world of Ukraine's unbreakable spirit. "
            "When your purpose is bigger than personal vanity, pain transforms into fuel.\n\n"
            "Readers: What weight in your personal life can you transform into purposeful resolve today?\n\n"
            "👉 Find strength in times of crisis, renewed perspective, and hope in dark seasons. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#UkraineStrength #Mahuchikh #CourageUnderFire #SurvivingLife #PurposeOverFear #OlympicResilience #LornetteDaye"
        )
    },
    {
        "id": 4,
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": (
            "GRACE UNDER PRESSURE: COMBINING ELEGANCE AND EXPLOSIVE FORCE. 🌟👟\n\n"
            "High jump is poetry combined with violent physics.\n\n"
            "The approach run must build centripetal force along a precise curved arc. "
            "The plant foot must withstand five times body weight in ground reaction force. "
            "The back must arch into an effortless crescent over the bar. "
            "Yaroslava executes this terrifying kinetic collision with the smile and calm grace of a dancer.\n\n"
            "Women in leadership often confront harsh environments. You do not need to mimic harshness to command respect. "
            "Poise and supreme technical competence are your greatest weapons.\n\n"
            "Women: Are you leading with grounded poise and unshakeable mastery?\n\n"
            "👉 Build lasting confidence, emotional balance, and identity in high-pressure arenas. "
            "Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n"
            "#GraceUnderPressure #Yaroslava #WomenInSport #SurvivalSkillsForWomen #KineticPoetry #OlympicStandards #CoachLornette"
        )
    },
    {
        "id": 5,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "PARIS GOLD: FULFILLING DESTINY ON THE WORLD'S GREATEST STAGE. 🥇🇫🇷\n\n"
            "Olympic gold is the dream of millions; it is claimed only by those whose nerve remains ironclad when the bar is at 2.00 meters.\n\n"
            "In the Stade de France, in front of eighty thousand roaring fans, Yaroslava Mahuchikh cleared the winning height on her first attempt. "
            "First-attempt clearances break the psychological will of your competitors. "
            "When you execute cleanly on the first try, you impose insurmountable pressure on everyone else.\n\n"
            "Leaders: Is your team prepared to deliver on the first attempt when the championship is on the line?\n\n"
            "👉 Master the habits of Olympic champions who execute flawlessly when it matters most. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#OlympicGold #Paris2024 #Mahuchikh #FirstAttemptExecution #FinishStrong #OlympicMindset #LornetteDaye"
        )
    },
    {
        "id": 6,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE ARCHITECTURE OF HIGH PERFORMANCE: ROUTINE OVER ADRENALINE. 📐🎯\n\n"
            "Amateurs rely on hype and adrenaline; Olympic champions rely on repeatable architecture.\n\n"
            "Watch Yaroslava's pre-jump ritual: four steps measured with a tape, two deep diaphragmatic breaths, "
            "a gentle tap of the spikes, visual mapping of the crossbar, and then the approach. "
            "She repeats that identical sequence whether jumping 1.90m in May or 2.10m for a world record. "
            "Consistency in routine produces consistency in execution.\n\n"
            "Executives: Does your organization possess repeatable operational routines that function flawlessly under pressure?\n\n"
            "👉 Transform your leadership execution with Olympic routine frameworks. "
            "Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n"
            "#RoutineOverAdrenaline #HighPerformanceArchitecture #ExecutiveDiscipline #CoachLornette #OperationalMastery"
        )
    },
    {
        "id": 7,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "FLIGHT MECHANICS: OVERCOMING THE FEAR OF GRAVITY. 🕊️⚡\n\n"
            "To jump 2.10 meters, an athlete must throw her body backward over a thin fiberglass bar seven feet off the ground.\n\n"
            "Any hesitation in the final two strides kills horizontal speed and causes failure. "
            "You must run toward the bar with total commitment, trust your plant, and allow physics to launch you into the air. "
            "Faith in your preparation conquers the fear of falling.\n\n"
            "Athletes: Where in your competitive execution are you tapping the brakes right before takeoff?\n\n"
            "👉 Eliminate hesitation and build fearless competitive commitment. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FearlessTakeoff #HighJumpMechanics #SurvivalSkillsForAthletes #CommitmentWins #OlympicCoach #LornetteDaye"
        )
    },
    {
        "id": 8,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE SKY IS NOT THE LIMIT: INSPIRING A NATION'S TOMORROWS. 🇺🇦🌅\n\n"
            "Yaroslava Mahuchikh's legacy will be measured not just in centimeters, but in the light she shone into a nation's dark night.\n\n"
            "She proved that Ukrainian youth can face war, displacement, and grief, and still rise to the very top of human achievement. "
            "True champions lift more than themselves over the bar; they lift their people.\n\n"
            "Set your bar high. Honor your people. Finish strong.\n\n"
            "👉 Discover how to finish your race with purpose, courage, and lasting legacy. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HigherBrighterFurther #YaroslavaMahuchikh #UkrainianPride #FinishStrong #OlympicLegacy #LornetteDaye #MasteryInAction"
        )
    }
]

# ==========================================
# CAMPAIGN 10: SAQUON BARKLEY (10 Posts) - slots 112 to 121
# ==========================================
saquon_posts = [
    {
        "id": 1,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "WHAT DO YOU DO AFTER GREATNESS? SAQUON BARKLEY IN PHILADELPHIA. 🦅🏈\n\n"
            "The work does not end at the top. A higher kind of greatness begins when you start fresh.\n\n"
            "After six seasons battling through injuries, franchise instability, and intense scrutiny in New York, "
            "Saquon Barkley arrived in Philadelphia with clear intent. In his opening games in midnight green, "
            "he exploded for three touchdowns, hurdled defenders backward, and established the Eagles as title contenders. "
            "He did not rest on his past reputation; he brought an elevated standard of workhorse excellence.\n\n"
            "In four decades coaching Olympic champions, I remind athletes: greatness is not a trophy on your shelf. "
            "It is the standard of sweat you bring to today's practice.\n\n"
            "Leaders: When entering a new chapter, do you rely on your resume, or prove your value on day one?\n\n"
            "👉 Master the habits of elite performers who finish strong in every arena. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#SaquonBarkley #FlyEaglesFly #AfterGreatness #FinishStrong #WorkhorseDiscipline #OlympicMindset #LornetteDaye"
        )
    },
    {
        "id": 2,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "THE BACKWARD HURDLE: ATHLETIC AUDACITY BACKED BY PHYSICAL SCIENCE. 🦅⚡\n\n"
            "When Saquon Barkley leaped backward over an NFL cornerback in live combat, the sports world gasped.\n\n"
            "Spectators called it a miracle. Biomechanists called it an unprecedented display of quad force, hip flexion, "
            "and spatial proprioception. You cannot execute that maneuver without thousands of squats, plyometric box jumps, "
            "and unyielding trust in your knee ligaments. Audacity on the field is earned in the weight room.\n\n"
            "Athletes: Are you putting in the structural conditioning necessary to support creative brilliance under contact?\n\n"
            "👉 Build elite physical resilience, rotational power, and explosive balance. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BackwardHurdle #Saquon #PhysicalGenius #SurvivalSkillsForAthletes #OlympicBiomechanics #LornetteDaye"
        )
    },
    {
        "id": 3,
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": (
            "RECOVERING FROM THE TORN ACL: THE PSYCHOLOGY OF THE REBUILD. 🛡️🦵\n\n"
            "When Saquon's ACL tore on the turf at Soldier Field in 2020, critics declared his elite burst was gone forever.\n\n"
            "The darkest hours of an athlete's life are spent in physical therapy clinics, relearning how to bend the knee, "
            "enduring scar-tissue breakdown, and fighting off feelings of obsolescence. Saquon embraced that lonely crucible. "
            "He rebuilt his body from the ground up and returned faster, stronger, and more durable than before.\n\n"
            "Men: When an unexpected injury or financial setback knocks you down, do you complain, or begin the quiet rebuild?\n\n"
            "👉 Build mental toughness, emotional resilience, and steady habits through seasons of physical repair. "
            "Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ACLRecovery #SaquonRebuild #PhysicalResilience #SurvivalSkillsForMen #MenWhoLead #OvercomingAdversity #CoachLornette"
        )
    },
    {
        "id": 4,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "THE RUNNING BACK STANDARD: CONFRONTING THE POSITION DISRESPECT. 🏈💪\n\n"
            "Modern NFL analytics claim running backs are disposable commodities that should not receive second contracts.\n\n"
            "Saquon Barkley rejected that narrative. He demonstrated that an elite running back who catches out of the backfield, "
            "protects in pass block, and punishes linebackers in the fourth quarter alters the entire geometry of an offense. "
            "When the industry devalues your role, the solution is not resentment; it is making yourself completely irreplaceable.\n\n"
            "Professionals: Has your industry attempted to commoditize your expertise? How are you making yourself indispensable?\n\n"
            "👉 Learn how to rise above industry averages and finish what you started with undeniable impact. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#RunningBackValue #SaquonBarkley #IndispensableTalent #FinishStrong #OlympicStandards #LornetteDaye"
        )
    },
    {
        "id": 5,
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE EAGLES CULTURE: EXECUTING IN A FOOTBALL CITY THAT DEMANDS PERFECTION. 🔔🦅\n\n"
            "Philadelphia is not a city for the faint of heart. The fans are knowledgeable, passionate, and relentlessly demanding.\n\n"
            "Saquon stepped into that passionate environment and embraced the standard immediately. "
            "He ran with violent purpose, celebrated with his offensive line, and spoke with authentic humility. "
            "When high-profile acquisitions honor the local community's passion, team chemistry explodes.\n\n"
            "Executives: How well does your executive leadership integrate with the unique culture of your organization?\n\n"
            "👉 Build a culture of fierce accountability and high performance with Olympic keynote frameworks. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#PhillyEagles #Saquon #HighExpectations #ExecutiveLeadership #TeamChemistry #CoachLornette"
        )
    },
    {
        "id": 6,
        "cta": "Surviving Life ($14.99 CAD)",
        "text": (
            "PEOPLE. PURPOSE. PERFORMANCE: A BRIGHTER TOMORROW BUILDS TODAY. 🌅🤝\n\n"
            "Beyond the sixty-yard touchdown runs and highlight clips, Saquon Barkley is a devoted father and philanthropist.\n\n"
            "His Michael Ann & Saquon Barkley Hope Foundation empowers underprivileged youth with educational scholarships, "
            "athletic camps, and food security. He knows that scoring touchdowns without uplifting others is an empty triumph. "
            "Greatness is defined by how much light you leave in the lives of those around you.\n\n"
            "Readers: How are you using your personal success to uplift those who cannot repay you?\n\n"
            "👉 Find deep meaning, perspective, and joy through service to others. "
            "Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HopeFoundation #SaquonCares #PurposeLivesHigher #SurvivingLife #LegacyOfGiving #LornetteDaye"
        )
    },
    {
        "id": 7,
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": (
            "THE POWER OF BALANCE: STAYING UPRIGHT THROUGH THE COLLISION. ⚖️🏈\n\n"
            "Saquon's legendary thigh development is not for aesthetics; it is a human suspension system.\n\n"
            "When safeties dive at his ankles, his core activates, his base widens, and he absorbs the blow while maintaining forward momentum. "
            "Contact balance is the defining difference between a two-yard gain and an explosive fifty-yard breakaway.\n\n"
            "Athletes: Are you training your stabilization muscles to keep your balance when hits arrive off-center?\n\n"
            "👉 Develop elite balance, joint integrity, and contact recovery systems. "
            "Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ContactBalance #SaquonBarkley #RunningBackBiomechanics #SurvivalSkillsForAthletes #OlympicTraining #LornetteDaye"
        )
    },
    {
        "id": 8,
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": (
            "BETTING ON YOURSELF: CHOOSING THE CHALLENGE OVER THE COMFORTABLE. 🎲🦅\n\n"
            "Staying in familiar circumstances is safe, but it rarely produces personal transformation.\n\n"
            "Leaving New York for Philadelphia meant facing intense divisional rivalry, learning a new offensive scheme, "
            "and playing under immense championship pressure. Saquon bet on his health, his work ethic, and his ability "
            "to thrive in a competitive system. Bet on yourself when you know your preparation is real.\n\n"
            "Men: What bold decision have you been postponing because staying comfortable felt safer?\n\n"
            "👉 Rebuild confidence, clarify purpose, and step into decisive leadership. "
            "Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BetOnYourself #SaquonMove #DecisiveLeadership #SurvivalSkillsForMen #MenWhoLead #CoachLornette"
        )
    },
    {
        "id": 9,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "FOURTH QUARTER WEAR-DOWN: PUNISHING SECONDARIES IN THE DYING MINUTES. ⏱️🧱\n\n"
            "In the first quarter, every defense is fast and energetic. "
            "By the fourth quarter, after tackling Saquon Barkley twenty times, defenders take wider angles, "
            "hesitate at the hole, and look to avoid contact. Great backs don't just gain yards; they break the defensive spirit.\n\n"
            "In your professional battles, stay relentless through the early friction. The fourth quarter is where you pull away.\n\n"
            "Leaders: Is your team built to outlast competitors in the final quarter of the fiscal year?\n\n"
            "👉 Master the habits of elite athletes who conquer fatigue and finish strong. "
            "Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FourthQuarterFinish #SaquonBarkley #RelentlessPressure #FinishStrong #OlympicStandards #LornetteDaye"
        )
    },
    {
        "id": 10,
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": (
            "FLY EAGLES FLY: THE QUEST FOR THE ULTIMATE PRIZE. 🏆🦅\n\n"
            "Individual accolades mean nothing compared to lifting the Lombardi Trophy.\n\n"
            "Saquon Barkley's career has featured Pro Bowls, Offensive Rookie of the Year awards, and viral highlights. "
            "Yet what burns in his chest is the championship ring. He joined the Eagles to play for the title, "
            "knowing that championship glory is the only achievement that never tarnishes.\n\n"
            "Keep your eyes fixed on the ultimate prize. Honor the daily grind. Finish strong.\n\n"
            "👉 Discover the championship mindset that carries elite performers to the summit. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n"
            "#FlyEaglesFly #SaquonBarkley #ChampionshipQuest #FinishStrong #OlympicGlory #LornetteDaye #MasteryInSport"
        )
    }
]

# Generate scripts 5 through 10
generate_script("CAMPAIGN 5: NBA - PRO BASKETBALL LEADERSHIP & EXECUTION", "nba", nba_posts, 65, "schedule-nba-campaign.py", "nba-scheduled-report.json")
generate_script("CAMPAIGN 6: CRICKET - INTERNATIONAL HERITAGE & PRECISION", "cricket", cricket_posts, 68, "schedule-cricket-campaign.py", "cricket-scheduled-report.json")
generate_script("CAMPAIGN 7: SITAYA FAGAN - YOUTH ATHLETICS & EMERGING STARS", "sitaya-fagan", sitaya_posts, 82, "schedule-sitaya-fagan-campaign.py", "sitaya-fagan-scheduled-report.json")
generate_script("CAMPAIGN 8: TYRESE GIBSON - ENTERTAINMENT & CREATIVE RESILIENCE", "tyrese-gibson", tyrese_posts, 92, "schedule-tyrese-gibson-campaign.py", "tyrese-gibson-scheduled-report.json")
generate_script("CAMPAIGN 9: YAROSLAVA MAHUCHIKH - WORLD RECORD HIGH JUMP & POISE", "yaroslava-mahuchikh", yaroslava_posts, 104, "schedule-yaroslava-mahuchikh-campaign.py", "yaroslava-mahuchikh-scheduled-report.json")
generate_script("CAMPAIGN 10: SAQUON BARKLEY - NFL POWER, RECOVERY & RESILIENCE", "saquon-barkley", saquon_posts, 112, "schedule-saquon-barkley-campaign.py", "saquon-barkley-scheduled-report.json")

print("\nALL 6 BUILDERS GENERATED WITH 100% VERIFICATION!")
