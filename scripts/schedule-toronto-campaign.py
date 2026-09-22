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

CDN_BASE = 'https://lornettedaye.com/campaigns/toronto'

posts_data = [
    {
        "id": 1,
        "slot": "Tuesday Morning (10:30 AM MDT)",
        "dueAt": "2026-09-22T16:30:00.000Z",
        "assetFile": "toronto-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "LEGACY LOOKS GOOD IN EVERY ERA. 🦖🇨🇦🏆\n\n"
            "Take a close look at this photograph. When champions gather in tailored tuxedos, "
            "it is not about the clothing. It is about the shared sweat, the silent sacrifices, "
            "and the unshakeable bond forged through relentless discipline.\n\n"
            "In 2019, the Toronto Raptors proved to the entire world that Canadian sports culture "
            "belongs on the summit. They did not just win a Larry O'Brien trophy. They changed the "
            "mindset of an entire country. They showed millions of young Canadian athletes that "
            "world-class excellence can live and thrive right here at home.\n\n"
            "In 40+ years of coaching Olympic athletes and national champions, I have witnessed "
            "many talented rosters. But true championship teams possess something deeper: brotherhood, "
            "uncompromising standards, and absolute trust under pressure.\n\n"
            "Toronto fans: What was the exact moment in 2019 when you knew the Raptors were taking the crown?\n\n"
            "👉 Bring Olympic-level championship culture and elite team cohesion to your corporate conference or athletic program. "
            "Book Coach Lornette Daye for keynotes and executive summits: lornettedaye.com/speaking\n\n"
            "#WeTheNorth #TorontoRaptors #RaptorsNation #KyleLowry #NorthOverEverything #ChampionshipCulture #CanadianSports #Brotherhood #ExecutiveLeadership #TeamCulture #OlympicMindset #LornetteDaye #KeynoteSpeaker #TorontoBasketball #6ix"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-01.png"
    },
    {
        "id": 2,
        "slot": "Thursday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-24T22:30:00.000Z",
        "assetFile": "toronto-02.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "WHEN THE STANDARD IS REAL, GENERATIONS SHOW UP. 🤝🍁\n\n"
            "DeMar DeRozan laying the foundation stone by stone. Kyle Lowry anchoring the heartbeat. "
            "Fred VanVleet betting on himself every single night. Pascal Siakam running the floor with tireless motor. "
            "Serge Ibaka bringing championship poise.\n\n"
            "Great cultures are not built overnight. They are passed down like an heirloom from one leader "
            "to the next. Before Toronto lifted the banner in June 2019, there were years of heartbreak, "
            "grueling early-morning shootarounds, and relentless commitment to building a winning identity.\n\n"
            "When high standards become the organizational norm, players do not just show up to play. "
            "They show up for each other. That is why this brotherhood remains unshakeable years after the final buzzer.\n\n"
            "Leaders & Coaches: Which teammate in Raptors franchise history had the deepest impact on your own view of leadership?\n\n"
            "👉 Equip your leadership team with the tools to build sustainable championship culture. "
            "Invite Lornette Daye to headline your next summit: lornettedaye.com/speaking\n\n"
            "#WeTheNorth #RaptorsBrotherhood #TorontoRaptors #DeMarDeRozan #KyleLowry #FredVanVleet #PascalSiakam #LeadershipExcellence #HighPerformanceCulture #CanadianExcellence #TeamBuilding #CoachLornette #KeynoteSpeaker #ChampionshipMindset"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-02.png"
    },
    {
        "id": 3,
        "slot": "Saturday Morning (11:00 AM MDT)",
        "dueAt": "2026-09-26T17:00:00.000Z",
        "assetFile": "toronto-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "A NIGHT FOR 7. SOME NUMBERS BECOME IDENTITY. 7️⃣✨\n\n"
            "In sports, you wear a jersey number. But every once in a generation, an athlete turns a number into a symbol "
            "of resilience, heart, and pride for an entire nation.\n\n"
            "For Toronto, number 7 will forever mean Kyle Lowry. The charges taken on hardwood floors with bodies flying. "
            "The timely pull-up three-pointers in hostile arenas. The quiet leadership inside the huddle when the season hung in the balance.\n\n"
            "Kyle did not just play point guard for Toronto. He became the living heartbeat of the city. He proved that grit, emotional poise, "
            "and relentless will matter far more than flash or hype.\n\n"
            "What is your all-time favorite Kyle Lowry highlight in a Raptors jersey? Drop your memories below!\n\n"
            "👉 Inspire your organization with the timeless principles of elite resilience and championship leadership. "
            "Keynotes and masterclasses by Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#KyleLowry #Number7 #GROAT #TorontoRaptors #WeTheNorth #RaptorsNation #HeartOverHype #CanadianBasketball #GrindAndResilience #OlympicMindset #LornetteDaye #LeadershipSummit #SportsExcellence"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-03.png"
    },
    {
        "id": 4,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-28T14:30:00.000Z",
        "assetFile": "toronto-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "PRESENCE IS PART OF PERFORMANCE. 👔🔥\n\n"
            "How you enter the arena sets the tone for how you compete. Dignity, poise, and sharp execution do not start "
            "at tip-off. They begin the moment you step out of the tunnel.\n\n"
            "Throughout my career preparing athletes for international competition, I always reminded them: "
            "Body language is a competitive weapon. When opponents see your composure, your laser focus, and your unity before the game even begins, "
            "you have already won the first round of the mental battle.\n\n"
            "These men brought that exact swagger and executive calm to Toronto basketball. They carried the weight of a nation with effortless grace.\n\n"
            "Executives & Leaders: How does your executive team carry itself when the spotlight turns on and the pressure peaks?\n\n"
            "👉 Cultivate executive presence, mental toughness, and focus under pressure. "
            "Book Coach Lornette Daye for your leadership conference: lornettedaye.com/speaking\n\n"
            "#ExecutivePresence #ComposureUnderPressure #TorontoRaptors #WeTheNorth #CorporateLeadership #ChampionshipHabits #OlympicCaliber #CanadianSports #BodyLanguage #PeakPerformance #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-04.png"
    },
    {
        "id": 5,
        "slot": "Wednesday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-09-30T19:00:00.000Z",
        "assetFile": "toronto-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "CHAMPIONSHIP ENERGY DOES NOT EXPIRE. IT MULTIPLIES. ⚡️🏀\n\n"
            "The greatest gift a championship roster gives an organization is not the banner in the rafters. "
            "It is the blueprint left behind for the next generation.\n\n"
            "When young players step into the locker room in Toronto, they look up and see what is possible. "
            "They know that Canadian teams can beat anyone on the planet when they stay disciplined and united. "
            "The energy of 2019 still circulates through the veins of Canadian basketball, powering youth clubs, prep academies, and college programs nationwide.\n\n"
            "True mentors do not hoard their knowledge. They pour everything into the rising talent coming behind them.\n\n"
            "Who represents the future of Canadian basketball excellence to you today? Tag them or name them below!\n\n"
            "👉 Develop long-term talent succession and mentorship systems in your company or athletic program. "
            "Book Lornette Daye: lornettedaye.com/speaking\n\n"
            "#NextGeneration #CanadianBasketball #WeTheNorth #TorontoRaptors #TalentDevelopment #MentorshipInAction #YouthSports #CanadaBasketball #ChampionshipLegacy #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-05.png"
    },
    {
        "id": 6,
        "slot": "Friday Afternoon (5:00 PM MDT)",
        "dueAt": "2026-10-02T23:00:00.000Z",
        "assetFile": "toronto-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "MORE THAN A CITY. AN ENTIRE NATION UNITED. 🇨🇦🦖\n\n"
            "Remember Jurassic Park in June 2019? But not just outside Scotiabank Arena in Toronto.\n\n"
            "Think of Halifax. Montreal. Regina. Calgary. Edmonton. Vancouver. Thousands standing shoulder-to-shoulder in the rain, "
            "cheering on every possession. An entire country rallying around one common dream.\n\n"
            "Sport has a unique, unmatched power: it bridges divisions, unites communities, and creates shared memories that last for lifetimes. "
            "When a team represents an entire nation with pride and integrity, people feel that connection in their bones.\n\n"
            "Raptors faithful: Which city or Jurassic Park watch party did you experience the 2019 Finals from?\n\n"
            "👉 Harness the power of shared purpose to unite your teams and departments. "
            "Schedule Lornette Daye for your company-wide keynote: lornettedaye.com/speaking\n\n"
            "#WeTheNorth #JurassicPark #CoastToCoast #CanadaSports #TorontoRaptors #NationalPride #SharedVision #UnityThroughSport #CommunityCulture #LornetteDaye #KeynoteSpeaker #ChampionshipVibes"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-06.png"
    },
    {
        "id": 7,
        "slot": "Sunday Mid-day (11:30 AM MDT)",
        "dueAt": "2026-10-04T17:30:00.000Z",
        "assetFile": "toronto-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "SACRIFICE OVER STATS: THE KYLE LOWRY CHARGE BLUEPRINT. 🛡️💥\n\n"
            "Taking a charge in basketball is the most unglamorous play in sports. It does not make the top-ten highlight reels. "
            "It does not boost your scoring average. It hurts every single time.\n\n"
            "Yet Kyle Lowry led the NBA in charges taken year after year. Why? Because winning organizations are built on the dirty work "
            "that most people refuse to do.\n\n"
            "In business, in athletics, and in life: championships are won by the teammates who dive on the floor for loose balls, "
            "who accept tough assignments without complaining, and who put the team mission ahead of personal accolades.\n\n"
            "Leaders: What is your organization's version of 'taking a charge' to protect the mission?\n\n"
            "👉 Transform individual contributors into selfless, mission-driven team leaders. "
            "Bring Lornette Daye to your leadership retreat: lornettedaye.com/speaking\n\n"
            "#SelflessLeadership #TakingTheCharge #KyleLowry #WorkEthic #TorontoRaptors #WeTheNorth #CultureOfExcellence #TeamFirst #OlympicStandard #LornetteDaye #KeynoteSpeaking"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-07.png"
    },
    {
        "id": 8,
        "slot": "Tuesday Morning (10:30 AM MDT)",
        "dueAt": "2026-10-06T16:30:00.000Z",
        "assetFile": "toronto-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "CULTURE THAT OUTLASTS CONTRACTS. 🏆🫂\n\n"
            "Contracts expire. Rosters turn over. Trades happen. But genuine brotherhood never dissolves.\n\n"
            "Look at the way these Raptors champions greet each other whenever they cross paths, regardless of what jersey they wear today. "
            "The mutual respect is immediate. The love is genuine. That only happens when people go to war together, endure hardship, "
            "and emerge victorious on the other side.\n\n"
            "If your workplace culture only lasts as long as the bonus check clears, you do not have culture. You just have payroll. "
            "Real culture creates relationships and standards that people carry with pride for the rest of their lives.\n\n"
            "Tag a former teammate or colleague who still feels like family today!\n\n"
            "👉 Build lasting culture and deep organizational loyalty. "
            "Book Coach Lornette Daye for your team leadership workshops: lornettedaye.com/speaking\n\n"
            "#OrganizationalCulture #LifelongBrotherhood #TorontoRaptors #WeTheNorth #WorkplaceExcellence #AuthenticLeadership #LoyaltyInAction #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-08.png"
    },
    {
        "id": 9,
        "slot": "Thursday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-10-08T22:00:00.000Z",
        "assetFile": "toronto-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "FROM UNDRAFTED TO UNSTOPPABLE: THE TORONTO BLUEPRINT. 📈🔥\n\n"
            "Fred VanVleet: Undrafted out of Wichita State. "
            "Pascal Siakam: Drafted 27th overall out of New Mexico State. "
            "Norman Powell: Second round pick, 46th overall.\n\n"
            "The Toronto Raptors did not win in 2019 by buying superstar shortcuts. They built the most formidable player development "
            "system in professional basketball. They sent players to Raptors 905 in Mississauga to grind, to fail, to adapt, and to build grit.\n\n"
            "Potential is everywhere. Development systems are rare. When you build an organization where work ethic is rewarded and every player "
            "is coached with high standards and high love, diamonds emerge from the rough.\n\n"
            "Raptors fans: What went through your mind when Fred VanVleet started burying dagger threes in the fourth quarter of the Finals?\n\n"
            "👉 Build elite development pipelines and cultivate hidden talent in your workforce. "
            "Keynotes and coaching seminars by Lornette Daye: lornettedaye.com/speaking\n\n"
            "#BetOnYourself #FredVanVleet #PascalSiakam #PlayerDevelopment #TorontoRaptors #WeTheNorth #TalentPipeline #GritAndGrind #OlympicDevelopment #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-09.png"
    },
    {
        "id": 10,
        "slot": "Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-10-10T16:00:00.000Z",
        "assetFile": "toronto-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "SATURDAY MEMORIES: JUNE 2019 ON YONGE STREET. 🚌🍁\n\n"
            "Over 2 million people filled the streets of downtown Toronto. People perched on highway overpasses, climbing trees, "
            "and standing in sea of red, black, and gold from morning until night.\n\n"
            "It was the celebration of a generation. It showed the entire globe what Canadian passion looks like.\n\n"
            "When you put in the unglamorous work in quiet, empty gyms for years, the celebration at the end is sweet beyond words. "
            "Never despise the small beginnings or the grueling days when nobody is clapping. The parade is built in the dark.\n\n"
            "Drop your best memory, video, or photo from the 2019 championship parade in the comments below!\n\n"
            "👉 Inspire your teams to stay committed through the hardest phases of growth. "
            "Book Coach Lornette Daye for your next company convention: lornettedaye.com/speaking\n\n"
            "#ChampionshipParade #TorontoParade #June2019 #WeTheNorth #TorontoRaptors #CanadianPride #HardWorkPaysOff #OlympicExcellence #LornetteDaye #KeynoteSpeaker #TorontoLife"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-10.png"
    },
    {
        "id": 11,
        "slot": "Monday Mid-day (12:00 PM MDT)",
        "dueAt": "2026-10-12T18:00:00.000Z",
        "assetFile": "toronto-11.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "CANADIAN THANKSGIVING FINALE: FOREVER GRATEFUL FOR 7. 🦃🍁❤️\n\n"
            "Today across Canada, families gather around dinner tables to give thanks for blessings, resilience, and community.\n\n"
            "On this special Thanksgiving Day, Canadian basketball fans everywhere take a moment to reflect on gratitude. "
            "We are grateful for the relentless heart of Kyle Lowry, who gave everything he had to this franchise for nine unforgettable seasons. "
            "We are grateful for the memories that brought parents and kids closer together around television screens across ten provinces and three territories.\n\n"
            "Championships are historic. But the gratitude, unity, and lasting inspiration they leave behind are eternal.\n\n"
            "Happy Canadian Thanksgiving to all our friends, athletes, and leaders across Canada and around the world! "
            "What are you most grateful for this season?\n\n"
            "👉 Celebrate Canadian excellence and bring champion-level inspiration to your organization in the year ahead. "
            "Connect with Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#HappyThanksgivingCanada #CanadianThanksgiving #Gratitude #KyleLowry #WeTheNorth #TorontoRaptors #CanadianExcellence #ChampionshipLegacy #OlympicMindset #LornetteDaye #KeynoteSpeaker #ThankYou7"
        ),
        "assetUrl": f"{CDN_BASE}/toronto-11.png"
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
    print("Starting Buffer queue scheduling for Toronto Raptors Legacy & Kyle Lowry #7 Campaign...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "toronto-scheduled-report.json")
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
                "campaign": "Toronto Raptors Legacy & Kyle Lowry #7 Gala",
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
    print(f"Toronto Campaign Scheduling Complete: {successful_count}/{len(posts_data)} posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")


if __name__ == "__main__":
    main()
