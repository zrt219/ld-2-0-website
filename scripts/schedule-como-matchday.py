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

CDN_BASE = 'https://lornettedaye.com/campaigns/como-matchday'

como_matchday_posts = [
    {
        "id": 1,
        "title": "COMO OLD TOWN: TRADITION, STYLE, AND FOOTBALL BY THE LAKE",
        "phase": "Pre-Game (Morning Buildup)",
        "slot": "Thursday Morning (9:00 AM MDT)",
        "dueAt": "2026-09-10T15:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 9:00 AM MDT",
        "assetFile": "como-01-old-town.jpg",
        "assetUrl": f"{CDN_BASE}/como-01-old-town.jpg",
        "text": """COMO OLD TOWN: TRADITION, STYLE, AND FOOTBALL BY THE LAKE. 🇮🇹⚽✨

Before the floodlights illuminate Stadio Giuseppe Sinigaglia, the soul of Como 1907 breathes through the narrow cobblestone streets of Old Town.

Football in Italy is never just 90 minutes on grass. It is centuries of civic pride, architectural majesty, and generational devotion woven into the fabric of daily life.

In 40+ years coaching Olympic champions and advising executive boards, I have learned that long-term institutional greatness cannot be manufactured overnight with capital alone—it requires honoring the heritage and people who built the foundation.

When you respect your roots, the ascent becomes unbreakable.

Matchday is here. Forza Como.

👉 Discover sports governance & high-performance culture programs: lornettedaye.com/programs
👉 Book Olympic coach keynote speaking: lornettedaye.com/speaking

#Como1907 #Calcio #SerieA #StadioSinigaglia #LakeComo #ItalianFootball #SportsGovernance #ExecutivePresence #LornetteDaye #HighPerformance #ChampionMindset #CultureFirst #FinishStrong #Lombardia #Matchday"""
    },
    {
        "id": 2,
        "title": "BARADELLO CASTLE: HISTORY ABOVE THE CITY. AMBITION ON THE PITCH",
        "phase": "Pre-Game (Midday Strategic Focus)",
        "slot": "Thursday Midday (11:00 AM MDT)",
        "dueAt": "2026-09-10T17:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 11:00 AM MDT",
        "assetFile": "como-02-baradello-castle.jpg",
        "assetUrl": f"{CDN_BASE}/como-02-baradello-castle.jpg",
        "text": """HISTORY ABOVE THE CITY. AMBITION ON THE PITCH. 🏰⚽🔥

High above Lake Como, the stone towers of Castello Baradello have stood watch since the 12th century. Today, that enduring vantage point mirrors the audacious ambition driving Como 1907.

From bankruptcy in the lower divisions to the top echelon of Italian football, Como's transformation is a textbook masterclass in visionary sports architecture.

True leadership isn't about scrambling for short-term fixes; it is about establishing a high-altitude strategic perspective, building modern data infrastructure, and executing with disciplined patience.

When your vision is anchored higher than your circumstances, obstacles become stepping stones.

Aim high. Execute with conviction. Finish strong.

👉 Keynote speaking on strategic vision & organizational resilience: lornettedaye.com/speaking
👉 Read *Survival Skills for Believers*: lornettedaye.com/books

#Como1907 #Baradello #SerieA #Calcio #StadioSinigaglia #ItalianFootball #HighPerformance #SportsInvestment #ClubArchitecture #LornetteDaye #StrategicLeadership #ExecutiveVision #FinishStrong #LakeComo"""
    },
    {
        "id": 3,
        "title": "THE STADIUM BY THE LAKE: 30 MINUTES TO KICKOFF",
        "phase": "Pre-Game (Countdown to Kickoff)",
        "slot": "Thursday Pre-Kickoff (12:30 PM MDT)",
        "dueAt": "2026-09-10T18:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 12:30 PM MDT",
        "assetFile": "como-03-stadium-by-the-lake.jpg",
        "assetUrl": f"{CDN_BASE}/como-03-stadium-by-the-lake.jpg",
        "text": """THE STADIUM BY THE LAKE: 30 MINUTES TO KICKOFF. 🌊🏟️⚽

Stadio Giuseppe Sinigaglia sits right at the water’s edge—one of the most breathtaking sporting stages on earth. But once the whistle blows, aesthetic beauty gives way to ruthless competitive intensity.

Kickoff is at 1:00 PM MDT.

In elite sport, preparation ends when you step onto the pitch. In these final 30 minutes, tactical clarity and emotional poise must lock in together.

When the stadium roars and the pressure spikes, champions don't look around—they look inward and trust their standard.

Game on. Drop the noise, command your space, and dictate the tempo.

👉 High-performance athlete & executive coaching: lornettedaye.com/athlete-coaching
👉 Leadership consulting with Olympian Coach Lornette Daye: lornettedaye.com

#Como1907 #StadioSinigaglia #Kickoff #SerieA #Calcio #LakeComo #MatchdayFocus #HighPerformance #LornetteDaye #TacticalMastery #PressureIsAPrivilege #ItalianFootball #FinishStrong"""
    },
    {
        "id": 4,
        "title": "WELCOME TO LAKE COMO: BEAUTY, ATMOSPHERE, AND FOOTBALL WITH SOUL",
        "phase": "Post-Game (Full-Time Reflection)",
        "slot": "Thursday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-10T22:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 4:00 PM MDT",
        "assetFile": "como-04-welcome-lake-como.jpg",
        "assetUrl": f"{CDN_BASE}/como-04-welcome-lake-como.jpg",
        "text": """BEAUTY, ATMOSPHERE, AND FOOTBALL WITH SOUL. 🌅⚽🤍

As the sun dips behind the Alps and the dusk settles over the water, matchday in Como reveals something profound about competitive athletics.

Tactical battles are won with feet and lungs, but club legacies are sustained through soul. Whether celebrating victory or dissecting the margins of defeat, elite competitors treat every full-time whistle not as an ending, but as data for tomorrow’s standard.

In 40+ years in Olympic athletics, I have seen that the teams who dominate long-term are the ones who reflect with honesty, recover with discipline, and protect their collective culture.

Football with soul. Ambition with purpose.

👉 Explore transformational executive culture programs: lornettedaye.com/programs
👉 Read Lornette Daye's leadership insights: lornettedaye.com/blog

#Como1907 #LakeComo #FullTime #Calcio #SerieA #StadioSinigaglia #FootballCulture #SportsLeadership #LornetteDaye #HighPerformance #Resilience #PostMatch #FinishStrong #ItalianFootball"""
    },
    {
        "id": 5,
        "title": "COMO 1907: EUROPEAN NIGHT — WHERE FOOTBALL MEETS BEAUTY",
        "phase": "Post-Game (Primetime Evening Finale)",
        "slot": "Thursday Evening (7:00 PM MDT)",
        "dueAt": "2026-09-11T01:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 7:00 PM MDT",
        "assetFile": "como-05-european-night.jpg",
        "assetUrl": f"{CDN_BASE}/como-05-european-night.jpg",
        "text": """COMO 1907: EUROPEAN NIGHT — WHERE FOOTBALL MEETS BEAUTY. 🌌🏟️✨

Under the brilliant floodlights on the shores of Lake Como, the modern dream of Como 1907 shines brightest.

Competing on European nights requires more than talent; it demands psychological immunity to fear, seamless collective cohesion, and the audacity to belong on the biggest stages in world sport.

From grassroots recovery to global executive presence, Como has demonstrated that when world-class investment respects community pride, magic happens.

Never shrink your ambition. Own your arena. Build something that outlasts the final whistle.

Finish strong.

👉 Book Lornette Daye for your international corporate summit: lornettedaye.com/speaking
👉 Athlete transition & high-performance mentorship: lornettedaye.com/mentorship

#Como1907 #EuropeanNight #SerieA #Calcio #StadioSinigaglia #LakeComo #ChampionsLeague #SportsGovernance #ExecutivePresence #LornetteDaye #HighPerformance #GlobalAmbition #FinishStrong #FootballArt"""
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
    for p in como_matchday_posts:
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
    print("🇮🇹 Como 1907 Matchday Campaign: 5-Post Cadence")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Date: Thursday, September 10, 2026 (Game at 1:00 PM MDT)")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(como_matchday_posts):
        print(f"[{idx + 1}/{len(como_matchday_posts)}] Scheduling Post #{p['id']} ({p['phase']}): \"{p['title']}\"")
        print(f"   Slot: {p['displayTime']} ({p['dueAt']})")
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

    report_path = os.path.join(os.path.dirname(__file__), "como-matchday-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Como 1907 Matchday Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(como_matchday_posts)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
