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

CDN_BASE = 'https://lornettedaye.com/campaigns/sleep-ads'

sleep_posts = [
    {
        "id": 1,
        "title": "SLEEP CAN WAIT: ARTHUR ASHE STADIUM AT 3:33 A.M.",
        "phase": "Tonight Kickoff (Late Night Primetime)",
        "slot": "Thursday Night (9:30 PM MDT)",
        "dueAt": "2026-09-11T03:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 9:30 PM MDT",
        "assetFile": "sleep-01.png",
        "assetUrl": f"{CDN_BASE}/sleep-01.png",
        "text": """SLEEP CAN WAIT. WHEN THE MATCH IS THIS GOOD. 🎾☕✨

Arthur Ashe Stadium. 3:33 A.M. Pillows. Blankets. Fifth set fuel.

There is a special, unwritten contract between the US Open and the die-hard fans who refuse to leave until the final ball is struck. When the night bleeds into morning and the rest of New York is fast asleep, 23,000 strangers become family under the floodlights.

In over 40 years of coaching Olympic champions, I have witnessed countless moments of athletic majesty—but nothing compares to the raw human passion of fans huddled under fleece blankets, nursing lukewarm coffee, completely captivated by two warriors trading 30-shot rallies in the fifth set.

Tennis keeps us human. Different generations. Same magic.

For the ones who stay.

👉 Discover athlete mentorship & high-performance leadership: lornettedaye.com/athlete-coaching
👉 Read *Survival Skills for Believers*: lornettedaye.com/books

#USOpen #ArthurAsheStadium #SleepCanWait #Tennis #GrandSlam #NightSession #FifthSet #TennisCommunity #TennisCulture #LornetteDaye #HighPerformance #ForTheOnesWhoStay #FlushingMeadows #NewYorkTennis"""
    },
    {
        "id": 2,
        "title": "THE FIFTH SET HAD OTHER PLANS",
        "phase": "Friday Afternoon Feature",
        "slot": "Friday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-09-11T19:00:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 1:00 PM MDT",
        "assetFile": "sleep-02.png",
        "assetUrl": f"{CDN_BASE}/sleep-02.png",
        "text": """THE FIFTH SET HAD OTHER PLANS. 🎾⚡🌙

You told yourself you would leave after the third set. You told yourself you had an 8:00 AM meeting. But then the match leveled at two sets all, the momentum swung, and leaving was no longer an option.

That is the spell of Grand Slam night tennis. It suspends time. It demands everything from the players on the court, and it pulls every ounce of emotion from the fans in the upper decks.

True greatness doesn't follow a tidy schedule. The most defining moments in sport—and in life—arrive when you are tired, cold, and tested, but you choose to stay in the arena anyway.

Respect the grind. Savor the battle.

👉 Keynote speaking on athletic resilience & mental toughness: lornettedaye.com/speaking
👉 Explore executive leadership programs: lornettedaye.com/programs

#USOpen #SleepCanWait #ArthurAsheStadium #NightSession #GrandSlam #TennisLife #TennisLovers #FifthSetDrama #LornetteDaye #HighPerformance #MentalFortitude #ChampionMindset #FinishStrong #TennisVibes"""
    },
    {
        "id": 3,
        "title": "BLANKETS, COFFEE & UNFILTERED PASSION",
        "phase": "Friday Midnight Primetime",
        "slot": "Friday Night (10:30 PM MDT)",
        "dueAt": "2026-09-12T04:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 10:30 PM MDT",
        "assetFile": "sleep-03.png",
        "assetUrl": f"{CDN_BASE}/sleep-03.png",
        "text": """BLANKETS. COFFEE. TENNIS. 3:33 A.M. ☕🧥🎾

Look around Arthur Ashe Stadium at 2:00 in the morning. You don’t see casual spectators. You see believers.

You see fans wrapped in stadium blankets, clutching hot cups of coffee, roaring on every breakpoint like their own lives depend on it. That collective heartbeat is what elevates tennis from a sport into a cultural phenomenon.

In four decades of elite athletic development, I tell every competitor: The crowd isn’t cheering for perfection; they are cheering for your refusal to quit. When fans see an athlete leaving their heart on the blue hardcourt, they will stay all night to bear witness.

Never underestimate the power of shared human energy.

👉 Learn more about high-performance culture & community impact: lornettedaye.com/impact
👉 Book Olympic coach keynote speaking: lornettedaye.com/speaking

#USOpen #ArthurAsheStadium #SleepCanWait #TennisFans #NightSession #GrandSlamTennis #FanCulture #FlushingMeadows #LornetteDaye #HighPerformance #PassionOverComfort #TennisCommunity #ForTheOnesWhoStay"""
    },
    {
        "id": 4,
        "title": "TENNIS KEEPS US HUMAN: THE MIDNIGHT LESSON",
        "phase": "Saturday Afternoon Feature",
        "slot": "Saturday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-09-12T19:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 1:00 PM MDT",
        "assetFile": "sleep-04.png",
        "assetUrl": f"{CDN_BASE}/sleep-04.png",
        "text": """TENNIS KEEPS US HUMAN. 🤍🎾🏟️

In a world increasingly dominated by digital feeds and short attention spans, what else can hold 23,000 people spellbound in freezing stadium air at 3:00 in the morning?

Grand Slam night sessions are an antidote to cynicism. They remind us of the beauty of human struggle, the tension of razor-thin margins, and the raw courage it takes to stand alone on a court and serve for the match.

Sport at this level is not about the scoreline—it is about the human spirit refusing to fold.

When was the last time you were so fully absorbed in a pursuit that time completely vanished?

Find what makes you stay until 3:33 A.M.

👉 Read *Survival Skills for Leaders*: lornettedaye.com/books
👉 Leadership consulting with Olympian Coach Lornette Daye: lornettedaye.com

#USOpen #SleepCanWait #ArthurAsheStadium #TennisKeepsUsHuman #GrandSlam #HumanExcellence #LornetteDaye #HighPerformance #MindsetMatters #TennisHeritage #CourageUnderPressure #FinishStrong"""
    },
    {
        "id": 5,
        "title": "FOR THE ONES WHO STAY",
        "phase": "Saturday Midnight Primetime",
        "slot": "Saturday Night (10:30 PM MDT)",
        "dueAt": "2026-09-13T04:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 10:30 PM MDT",
        "assetFile": "sleep-05.png",
        "assetUrl": f"{CDN_BASE}/sleep-05.png",
        "text": """FOR THE ONES WHO STAY. 🌙✨🎾

When the clock ticks past midnight and the stadium announcers remind everyone that the subways are running on late schedules, a quiet transformation occurs.

The stadium empties of the faint of heart, leaving only the purists. The sound of the ball hitting the strings reverberates louder. Every gasp from the crowd feels amplified.

Championship culture in athletics and business works the exact same way. Anyone can show up when the sun is out and the stakes are low. But legacy belongs to the ones who stay when the temperature drops, the exhaustion sets in, and the outcome hangs by a thread.

Stand firm. Stay late. Finish strong.

👉 Executive leadership coaching & keynote speaking: lornettedaye.com/speaking
👉 Athlete transition & mental performance: lornettedaye.com/athlete-coaching

#USOpen #SleepCanWait #ArthurAsheStadium #NightSession #GrandSlam #TennisFamily #LornetteDaye #HighPerformance #MentalToughness #Resilience #Endurance #FinishStrong #ATP #WTA"""
    },
    {
        "id": 6,
        "title": "DIFFERENT GENERATIONS. SAME MAGIC.",
        "phase": "Sunday Afternoon Feature",
        "slot": "Sunday Afternoon (1:00 PM MDT)",
        "dueAt": "2026-09-13T19:00:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 1:00 PM MDT",
        "assetFile": "sleep-06.png",
        "assetUrl": f"{CDN_BASE}/sleep-06.png",
        "text": """DIFFERENT GENERATIONS. SAME MAGIC. 🎾🤝💫

Look closely at the crowd in the wee hours of a US Open marathon: A grandfather sharing a blanket with his grandson. College students leaning over the rail next to corporate executives who took off their ties six hours ago.

There are no titles or resumes in Arthur Ashe Stadium at 3:33 A.M. There is only the shared reverence for two athletes pushing past the limits of human endurance.

Throughout my 40+ years coaching across global sports, the most powerful lesson has always been this: True excellence breaks down every demographic divide and unifies people around a common standard.

Protect the spaces that bring us together.

👉 Learn about youth development & sports mentorship: lornettedaye.com/impact
👉 Explore leadership programs: lornettedaye.com/programs

#USOpen #ArthurAsheStadium #TennisMagic #GenerationsOfTennis #SleepCanWait #GrandSlam #SportsUnite #CommunityExcellence #LornetteDaye #HighPerformance #TennisCulture #FinishStrong"""
    },
    {
        "id": 7,
        "title": "SLEEP CAN WAIT: WHEN HISTORY IS BEING WRITTEN",
        "phase": "Sunday Midnight Finale",
        "slot": "Sunday Night (10:30 PM MDT)",
        "dueAt": "2026-09-14T04:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 10:30 PM MDT",
        "assetFile": "sleep-07.png",
        "assetUrl": f"{CDN_BASE}/sleep-07.png",
        "text": """SLEEP CAN WAIT. WHEN HISTORY IS BEING WRITTEN. 🏆🔥🎾

As another unforgettable US Open closes its final night session chapter, we carry forward the memories of matches that refused to end and performances that defied fatigue.

You can always catch up on sleep tomorrow. But you can never replay the feeling of being present when history is etched into the court.

To every player who battled through cramps and self-doubt, and to every fan who stayed until the lights were dimmed: Thank you for keeping the soul of sport alive.

When greatness calls, answer without hesitation.

Lornette Daye | 40+ Years in Olympic Athletics & Leadership Mastery

👉 Book corporate keynote speaking: lornettedaye.com/speaking
👉 Explore executive coaching: lornettedaye.com/athlete-coaching

#USOpen #ArthurAsheStadium #SleepCanWait #TennisHistory #GrandSlam #NightSession #TennisLegacy #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #TennisKeepsUsHuman #FlushingMeadows"""
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
    for p in sleep_posts:
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
    print("🎾 'Sleep Can Wait' US Open Campaign: 7-Post Cadence")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Tonight (Sep 10) + Fri/Sat/Sun (Sep 11-13, 2026)")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(sleep_posts):
        print(f"[{idx + 1}/{len(sleep_posts)}] Scheduling Post #{p['id']} ({p['phase']}): \"{p['title']}\"")
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

    report_path = os.path.join(os.path.dirname(__file__), "sleep-campaign-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Sleep Can Wait Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(sleep_posts)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
