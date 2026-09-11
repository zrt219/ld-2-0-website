import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301' # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/football-weekend'

football_posts = [
    {
        "id": 1,
        "team": "Colorado Buffaloes",
        "phase": "Friday Colorado Teaser",
        "slot": "Friday Afternoon (3:30 PM MDT)",
        "dueAt": "2026-09-11T21:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 3:30 PM MDT",
        "assetFile": "colorado-01.png",
        "assetUrl": f"{CDN_BASE}/colorado-01.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": """COLORADO KEEPS PEOPLE WATCHING. WHAT IS THEIR MARKETING SECRET? 🏈🦬✨

Access. Personality. Storytelling. Culture.

From opening day against Georgia Tech to sold-out stands under the Flatirons, Colorado football has rewritten the playbook on what it means to build an iconic sporting brand in the modern era.

It belongs to more than football. It is about creating an emotional connection so powerful that fans and creators rally together.

In 40+ years coaching Olympic champions and executive leaders, the greatest lesson is this: You cannot command attention until you dare to stand for something unmistakable.

When your team steps onto the field, what story are you telling the world?

👉 Equip your mind with championship fortitude — order *Survival Skills for Believers*: lornettedaye.com/books

#ColoradoFootball #CUBuffs #CoachPrime #SkoBuffs #WeComing #CollegeFootball #Big12 #PrimeEffect #LornetteDaye #HighPerformance #ChampionMindset #SportsBranding #FinishStrong #FootballCulture"""
    },
    {
        "id": 2,
        "team": "Colorado Buffaloes",
        "phase": "Saturday Colorado Gameday Morning",
        "slot": "Saturday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-12T14:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:00 AM MDT",
        "assetFile": "colorado-02.png",
        "assetUrl": f"{CDN_BASE}/colorado-02.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": """WIN THE GAME. WIN THE ATTENTION. THE PRIME EFFECT. 🏈🔥⚡

Story ➔ Attention ➔ Community ➔ Tickets ➔ Culture.

Saturday morning in Boulder hits different. When Coach Prime leads the Buffaloes out of the tunnel, it isn’t just a football game—it’s an electric masterclass in transformative leadership.

What can every corporate organization learn from Colorado?

When leadership communicates with unshakeable conviction, energy shifts. Doubt disappears. High standards become contagious.

Believe bigger. Walk into your arena today with total ownership of your craft.

👉 Book Lornette Daye for your corporate keynote on transformative leadership: lornettedaye.com/speaking

#CUBuffs #CoachPrime #WeComing #ColoradoBuffaloes #CollegeGameday #BelieveBigger #PrimeEffect #SportsGovernance #ExecutivePresence #LornetteDaye #HighPerformance #LeadershipWisdom #FinishStrong"""
    },
    {
        "id": 3,
        "team": "Colorado Buffaloes",
        "phase": "Saturday Colorado Tailgate & Storytelling",
        "slot": "Saturday Mid-Morning (10:30 AM MDT)",
        "dueAt": "2026-09-12T16:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 10:30 AM MDT",
        "assetFile": "colorado-03.png",
        "assetUrl": f"{CDN_BASE}/colorado-03.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": """MORE THAN FOOTBALL. GOOD PLAYERS, BETTER STORIES. 🦬🎥🏈

Tailgates are packed. The Rocky Mountain sun is shining. 3 hours until kickoff.

Colorado didn’t just rebuild a roster—they built a media powerhouse that empowers athletes, connects communities, and redefines student-athlete visibility.

In four decades of elite athlete development, I have always said: Athletes are not commodities; they are storytellers and leaders who shape culture for generations to come.

When you invest in the whole person—their mind, character, and vision—championship results follow naturally.

Study the playbook of enduring resilience.

👉 Grab your copy of Lornette Daye's life-mastery books: lornettedaye.com/books

#ColoradoFootball #CUBuffs #SkoBuffs #CoachPrime #WeComing #CollegeFootball #StudentAthletes #NIL #SportsMedia #LornetteDaye #HighPerformance #CharacterFirst #FinishStrong #Gameday"""
    },
    {
        "id": 4,
        "team": "Colorado Buffaloes",
        "phase": "Saturday Colorado Kickoff Lockdown (45m to 1:30 PM Kickoff)",
        "slot": "Saturday Pre-Kickoff (12:45 PM MDT)",
        "dueAt": "2026-09-12T18:45:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 12:45 PM MDT",
        "assetFile": "colorado-04.png",
        "assetUrl": f"{CDN_BASE}/colorado-04.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": """45 MINUTES TO KICKOFF: THE PRIME EFFECT IN FULL MOTION. ⏰🏈🔥

Folsom Field is rocking. Sanders #2. Hunter #12. The black and gold are locked in for the 1:30 PM MDT kickoff.

In sports and high-stakes business, the talk ends in the tunnel. When the cameras flash and the roar deafens, all that remains is your preparation and your poise.

Colorado changes lives not because they avoid pressure, but because they run directly toward it.

Pressure is a privilege. Stand tall, execute the details, and command your standard.

Sko Buffs!

👉 Elevate your executive team with high-performance coaching: lornettedaye.com/speaking

#CUBuffs #ColoradoFootball #CoachPrime #WeComing #SkoBuffs #CollegeGameday #Kickoff #FolsomField #ShedeurSanders #TravisHunter #LornetteDaye #HighPerformance #PressureIsAPrivilege #FinishStrong"""
    },
    {
        "id": 5,
        "team": "Seattle Seahawks",
        "phase": "Saturday Night Primetime",
        "slot": "Saturday Night (8:00 PM MDT)",
        "dueAt": "2026-09-13T02:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:00 PM MDT",
        "assetFile": "seahawks-01.png",
        "assetUrl": f"{CDN_BASE}/seahawks-01.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": """CHAMPIONS OPEN WITH A WIN: SEATTLE 13 • NEW ENGLAND 10. 🏆🌊🏈

As college football wraps up Saturday, the NFL spotlight turns north to Seattle.

Lumen Field. World Champions. Title defense underway.

Reaching the pinnacle of professional football is extraordinarily hard. But defending that standard—knowing every single team is circling your date on their calendar—demands a whole new level of mental conditioning.

In my 40+ years coaching Olympic champions, true titleholders never relax into complacency. They double down on the fundamentals that got them there.

Defend the standard. Stay hungry.

👉 Build unshakeable mental fortitude — read *Survival Skills for Believers*: lornettedaye.com/books

#Seahawks #12s #GoHawks #LumenField #NFL #TitleDefense #SuperBowlChampions #ChampionshipCulture #LornetteDaye #HighPerformance #MentalToughness #FinishStrong #NFLWeekend"""
    },
    {
        "id": 6,
        "team": "Seattle Seahawks",
        "phase": "Sunday Morning Kickoff",
        "slot": "Sunday Morning (9:00 AM MDT)",
        "dueAt": "2026-09-13T15:00:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 9:00 AM MDT",
        "assetFile": "seahawks-02.png",
        "assetUrl": f"{CDN_BASE}/seahawks-02.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": """68,000+ CAME TO SEE THE CHAMPIONS. AND SEATTLE GAVE THEM A WIN. 🏈🔊💚

Sunday gameday in Seattle is unlike anything in world sport.

The 12s don't just attend games; they actively tilt the field. Decibels vibrating the stadium concrete, seismic readings on third downs, and an unyielding connection between players and civic community.

What makes a championship brand bigger than the game itself?

People. Elevation. Possibility.

When leadership creates an authentic home advantage, your team becomes unstoppable.

👉 Keynote speaking with Olympian Coach Lornette Daye on building high-performance culture: lornettedaye.com/speaking

#Seahawks #12s #GoHawks #LumenField #NFL #SeattleSeahawks #HomeFieldAdvantage #ChampionshipCulture #LornetteDaye #HighPerformance #LeadershipExcellence #FinishStrong #NFLGameday"""
    },
    {
        "id": 7,
        "team": "Seattle Seahawks",
        "phase": "Sunday Midday Action",
        "slot": "Sunday Midday (2:00 PM MDT)",
        "dueAt": "2026-09-13T20:00:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 2:00 PM MDT",
        "assetFile": "seahawks-03.png",
        "assetUrl": f"{CDN_BASE}/seahawks-03.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": """BUILT BY BELIEVERS. FOREVER. 🏈🛡️🔥

Lynch #24. Wilson #3. Sherman #25. Thomas #29.

The Legion of Boom didn't just win football games—they redefined defensive dominance through supreme collective trust and an unapologetic, fearless identity.

Every great defense, every great enterprise, and every Olympic podium performance shares the same core DNA: Absolute accountability to the person standing next to you.

When teammates trust each other unconditionally, fear evaporates.

Master the standard of championship execution.

👉 Discover Lornette Daye's life lessons & books: lornettedaye.com/books

#Seahawks #LegionOfBoom #GoHawks #12s #LumenField #NFLHistory #ChampionshipDNA #TeamworkMastery #LornetteDaye #HighPerformance #SuperBowlXLVIII #FinishStrong #Accountability"""
    },
    {
        "id": 8,
        "team": "Seattle Seahawks",
        "phase": "Sunday Night Football Primetime",
        "slot": "Sunday Evening (6:30 PM MDT)",
        "dueAt": "2026-09-14T00:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 6:30 PM MDT",
        "assetFile": "seahawks-04.png",
        "assetUrl": f"{CDN_BASE}/seahawks-04.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": """WHAT MAKES A CHAMPIONSHIP BRAND BIGGER THAN THE GAME ITSELF? 🌃🏆✨

As the Sunday Night Football lights glow over Puget Sound and Lumen Field, we reflect on what truly endures.

Trophies sit in glass cases. But the culture of pride, collective resilience, and elevating possibilities lives forever in the people who believe.

From college football Saturdays in Boulder to Sunday championship battles in Seattle: Sport is our greatest teacher of perseverance, dignity, and grace under fire.

Rise up. Lead with authority. Finish strong.

Lornette Daye | 40+ Years in Olympic Athletics & Leadership Mastery

👉 Book corporate executive workshops & keynote speaking: lornettedaye.com/speaking

#Seahawks #12s #GoHawks #NFL #SundayNightFootball #LumenField #ChampionshipLegacy #SportsGovernance #ExecutivePresence #LornetteDaye #HighPerformance #LeadershipCulture #FinishStrong"""
    }
]

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        text
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

def buffer_request(query, variables):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode("utf-8")).get("data", {})

def probe_assets():
    print("======================================================")
    print("🔍 Probing Production Visual Assets (Zero-404 Guarantee)")
    print("======================================================")
    ctx = ssl._create_unverified_context()
    all_ok = True
    for p in football_posts:
        url = p["assetUrl"]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        try:
            with urllib.request.urlopen(req, context=ctx) as r:
                if r.status == 200:
                    cl = r.headers.get("Content-Length", "unknown")
                    print(f"   ✅ [200 OK] {p['assetFile']} ({cl} bytes)")
                else:
                    print(f"   ❌ [{r.status}] {p['assetFile']}")
                    all_ok = False
        except Exception as e:
            print(f"   ❌ [ERROR] {p['assetFile']}: {e}")
            all_ok = False
    print("======================================================\n")
    return all_ok

def main():
    print("======================================================")
    print("🏈 Football Weekend Campaign: 8-Post Cadence")
    print("Colorado Buffaloes (Fri-Sat) & Seattle Seahawks (Sat-Sun)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(football_posts):
        print(f"[{idx + 1}/{len(football_posts)}] Scheduling Post #{p['id']} ({p['phase']}): \"{p['team']}\"")
        print(f"   Slot: {p['displayTime']} ({p['dueAt']})")
        print(f"   CTA: {p['cta']}")
        print(f"   Asset: {p['assetUrl']}")

        input_data = {
            "channelId": CHANNEL_ID,
            "text": p["text"],
            "mode": "customScheduled",
            "dueAt": p["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": [{"image": {"url": p["assetUrl"]}}]
        }

        try:
            data = buffer_request(mutation, {"input": input_data})
            create_post = data.get("createPost", {})
            typename = create_post.get("__typename")

            if typename == "PostActionSuccess" and "post" in create_post:
                post_obj = create_post["post"]
                print(f"   ✅ Success! Buffer Post ID: {post_obj['id']} | Due: {post_obj['dueAt']}\n")
                p["bufferPostId"] = post_obj["id"]
                p["status"] = "scheduled"
                p["scheduledAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                results.append(p)
            elif typename == "LimitReachedError":
                msg = create_post.get("message", "Rate limit reached")
                print(f"   ⚠️ Limit reached: {msg}\n")
                p["status"] = "limit_reached"
                p["error"] = msg
                results.append(p)
            else:
                print(f"   ⚠️ Failed response: {json.dumps(create_post, indent=2)}\n")
                p["status"] = "failed"
                p["error"] = create_post
                results.append(p)
        except Exception as e:
            print(f"   ❌ Exception: {e}\n")
            p["status"] = "error"
            p["error"] = str(e)
            results.append(p)

        time.sleep(1.0)

    report_path = os.path.join(os.path.dirname(__file__), "football-weekend-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Football Weekend Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(football_posts)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
