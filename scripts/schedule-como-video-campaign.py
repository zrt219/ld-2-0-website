import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_VIDEO = 'https://lornettedaye.com/campaigns/como-win/como-sinigaglia-win.mp4'
HASHTAGS = "#Como1907 #SemmCumasch #Lariani #NelNomeDiComo #StadioSinigaglia #SerieA #Calcio #CescFabregas #NicoPaz #FootballElevated #LDFootball #ChampionMindset #TeamCulture #HighPerformance #LeadershipExcellence #LornetteDaye #FinishStrong #SurvivalSkillsForAthletes"

video_posts = [
    {
        "id": 1,
        "title": "THE SOUND OF VICTORY AT SINIGAGLIA",
        "theme": "Matchday Evening Passion & Pure Joy",
        "slot": "Wednesday Evening (4:30 PM MDT)",
        "dueAt": "2026-09-16T22:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 4:30 PM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""LISTEN TO THE ROAR OF STADIO GIUSEPPE SINIGAGLIA! 🔵⚪🇮🇹🔊

Turn your volume all the way up for this one.

When the final whistle blew and Como 1907 sealed another massive Serie A victory, the energy didn't just stay on the pitch—it echoed across the waters of Lake Como!

Watch the players, the coaching staff, and the supporters erupt as one single heartbeat. In sports, you can buy expensive contracts, but you cannot buy genuine passion. You cannot buy the electrifying hunger of a squad that fights for every square inch of grass and every single fan in the stands.

In over 40 years coaching Olympic champions, I have seen every kind of celebration. But nothing compares to the raw, unscripted triumph of a team that knows exactly what they sacrificed to get here.

Question for football fans and leaders: What was the most electrifying sports celebration you ever witnessed live in person? Drop your memory below! 👇

👉 Elevate your team's culture to championship standards: https://lornettedaye.com/speaking
👉 Read "Survival Skills for Athletes" ($14.99 CAD) for mental toughness & focus: https://lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 2,
        "title": "CULTURE OVER CAPITAL: THE COMO 1907 BLUEPRINT",
        "theme": "Strategic Leadership & Institutional Architecture",
        "slot": "Thursday Midday (11:30 AM MDT)",
        "dueAt": "2026-09-17T17:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 11:30 AM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""CULTURE OVER CAPITAL: WHY COMO 1907 IS WINNING ON AND OFF THE PITCH. ⚽📊✨

Look past the celebration in this video for a moment. Look at the foundation beneath it.

A few short years ago, Como 1907 was mired in bankruptcy and the lower tiers of Italian football. Today, they are commanding Serie A fixtures with tactical swagger, data-driven methodology, and global respect.

How do you engineer a turnaround like that?
1. Strategic Clarity: You don't chase quick fixes; you hire visionary leadership (Cesc Fàbregas) who instill a relentless tactical identity.
2. Humble Discipline: No ego is larger than the club badge.
3. Total Community Buy-in: You build an environment where players run through walls because the entire city believes in them.

Whether you manage an elite soccer club, an Olympic national team, or a Fortune 500 company, the rule remains: Culture eats strategy for breakfast, but disciplined culture turns vision into trophies.

Leaders: When turning around an organization, what is the very first standard you establish? Let's discuss in the comments. 👇

👉 Book Lornette Daye for your executive summit or sports leadership retreat: https://lornettedaye.com/speaking
👉 Grab your digital edition of "Survival Skills for Men" ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00

{HASHTAGS}"""
    },
    {
        "id": 3,
        "title": "THE MAGIC OF SHARED PURPOSE",
        "theme": "Community Devotion & Authentic Belonging",
        "slot": "Friday Afternoon (2:00 PM MDT)",
        "dueAt": "2026-09-18T20:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 2:00 PM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""WHEN A TEAM REPRESENTS A COMMUNITY, WINNING BECOMES SACRED. 💙🏟️

Watch how Cesc Fàbregas and the squad celebrate right in front of the Curva at Stadio Sinigaglia. 

There is no barrier between the athletes and the people. The victory belongs to the baker, the barista, the boat captain on the lake, and the generations of supporters who wore the blue scarf through every heartbreak and relegation.

That is the power of shared purpose. When athletes understand that their performance is a platform of inspiration for an entire community, they find an extra 10% reserve of stamina when their legs are burning in the 88th minute.

Whatever arena you compete in today—sports, business, or community service—never forget who you are fighting for.

Supporters: Which club in world football has the most unbreakable bond with its fans? Tag your club! 👇

👉 Learn how to anchor your organization in authentic purpose: https://lornettedaye.com/programs
👉 Rebuild your foundation with "Surviving Life" by Lornette Daye ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02

{HASHTAGS}"""
    },
    {
        "id": 4,
        "title": "WEEKEND FUEL: STANDARDS THAT NEVER DROP",
        "theme": "Resilience & Relentless Execution",
        "slot": "Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-19T16:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 10:00 AM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""WEEKEND INSPIRATION: CHAMPIONS CELEBRATE HARD BECAUSE THEY WORK HARDER. 🔥🏆

Nothing in top-flight football is handed to you on a silver platter. Every clean sheet, every counter-attack, every slide tackle in the mud at Stadio Sinigaglia was paid for on the training ground on cold Tuesday mornings.

When you watch Como 1907 celebrate this victory, remember that joy is the byproduct of discipline. 

If you want to feel the exhilarating high of winning on matchday, you have to fall in love with the unglamorous grind of preparation. You have to commit to standards that don't fluctuate with your mood.

What goal are you putting in the work for this weekend? Share your focus below and let’s keep each other accountable! 👇

👉 Transform your athletic mindset with "Survival Skills for Athletes" ($14.99 CAD): https://lornettedaye.com/books
👉 Explore high-performance coaching and mentorship: https://lornettedaye.com/programs

{HASHTAGS}"""
    },
    {
        "id": 5,
        "title": "MONDAY MOTIVATION: THE UNDERDOG MENTALITY",
        "theme": "Defying Doubters & Stepping into Greatness",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 8:30 AM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""START YOUR WEEK LIKE COMO 1907: REFUSE TO ACCEPT LIMITATIONS! 💥⚡

When Como arrived in Serie A, critics and pundits doubted whether they could compete against storied football institutions. 

This video is their answer.

Underdog status is not a curse—it is your greatest competitive advantage. When people underestimate you:
- You have no burden of unearned entitlement.
- You play with total freedom and ferocious intensity.
- You catch complacent giants looking in the rearview mirror.

As you step into your workweek, take that Como spirit with you. Let doubters talk while you put your head down and execute your game plan.

What is one challenge on your calendar this week that calls for an underdog mindset? Drop it below! 👇

👉 Inspire your company or athletic department with Olympic coach Lornette Daye: https://lornettedaye.com/speaking
👉 Read "Finish Strong: Chasing the Olympic Dream" ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A

{HASHTAGS}"""
    },
    {
        "id": 6,
        "title": "TACTICAL DISCIPLINE UNDER PRESSURE",
        "theme": "Executing the Game Plan Under Fire",
        "slot": "Tuesday Midday (1:00 PM MDT)",
        "dueAt": "2026-09-22T19:00:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 1:00 PM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""THE ART OF CLOSING OUT THE MATCH. ⚽⏱️🛡️

Watch the passion in this celebration. What you are witnessing is the payoff of tactical composure.

In Serie A, holding onto a lead against relentless opponents requires ice in your veins. It means midfielders pressing in tight coordination, center-backs winning aerial duels, and attackers sacrificing their personal stats to track back and defend.

In 40+ years coaching world-class athletes, I have always taught: "Emotion will get you started, but execution will get you over the line."

When the pressure spikes in your field of work, do you default to panic or do you trust your preparation? 

Coaches & directors: How do you train your players to stay calm in the final 5 minutes of a tight match? Let's trade insights! 👇

👉 Equip your coaches with elite mental performance tools: https://lornettedaye.com/programs
👉 Order "Survival Skills for Athletes" ($14.99 CAD): https://lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 7,
        "title": "WHAT 40 YEARS OF OLYMPIC COACHING TAUGHT ME ABOUT CHEMISTRY",
        "theme": "Unselfish Camaraderie & Brotherhood",
        "slot": "Thursday Morning (10:30 AM MDT)",
        "dueAt": "2026-09-24T16:30:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 10:30 AM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""CHEMISTRY CANNOT BE FAKED. 🤝💙🔥

Look at the hugs, the smiles, and the mutual respect between every player on the pitch in this video.

You cannot manufacture team chemistry in a press release. It is forged through:
- Shared sweat in preseason training
- Honest, constructive locker-room conversations
- Mutual accountability where every teammate holds the same high standard
- Celebrating each other's successes without jealousy

When you build an environment where everyone genuinely wants their teammate to win, you become unbeatable.

Tag a teammate, coach, or colleague who always brings unselfish energy to your locker room or office! 👇

👉 Book keynote speaker Lornette Daye for your next conference: https://lornettedaye.com/speaking
👉 Explore the complete Lornette Daye Book Catalog: https://lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 8,
        "title": "THE HIGHER STANDARD: COMO 1907 ALWAYS FORWARD",
        "theme": "Legacy & Continuous Evolution",
        "slot": "Saturday Morning (11:00 AM MDT)",
        "dueAt": "2026-09-26T17:00:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 11:00 AM MDT",
        "assetUrl": CDN_VIDEO,
        "isVideo": True,
        "text": f"""MORE THAN A MATCH. A HIGHER STANDARD. 🔵⚪🇮🇹

As the cheers fade into the evening over Lake Como, the work does not stop. 

True champions enjoy the victory, savor the moment with the fans, and then immediately reset their focus on the next standard. Because greatness is not a destination you reach once—it is a continuous habit of demanding more from yourself tomorrow than you did today.

Como 1907 is proving to the world that when visionary ownership, brilliant coaching, elite young talent, and passionate supporters align, magic happens.

Forza Como. Always forward. Sempre avanti.

What higher standard are you setting for your life and career this month? Drop it below! 👇

👉 Partner with Olympic coach Lornette Daye: https://lornettedaye.com
👉 Keynote Speaking: https://lornettedaye.com/speaking
👉 Digital Books Catalog ($14.99 CAD each): https://lornettedaye.com/books

{HASHTAGS}"""
    }
]

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        dueAt
        state
        channelId
      }
    }
    ... on UserError {
      message
    }
    ... on LimitReachedError {
      message
    }
    ... on RestProxyError {
      message
    }
  }
}
"""

def buffer_request(query, variables=None):
    url = "https://publish.buffer.com/graphql"
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode("utf-8")).get("data", {})

def probe_asset(url):
    print(f"🔍 Probing production asset URL: {url}")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
    try:
        with urllib.request.urlopen(req, context=ctx) as r:
            if r.status == 200:
                cl = r.headers.get("Content-Length", "unknown")
                print(f"   ✅ [200 OK] ({cl} bytes)")
                return True
            else:
                print(f"   ❌ [{r.status}] {url}")
                return False
    except Exception as e:
        print(f"   ❌ [ERROR] {url}: {e}")
        return False

def main():
    print("======================================================")
    print("🇮🇹 Como 1907 Sinigaglia Victory Video: 8-Post Campaign")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("======================================================\n")

    if not probe_asset(CDN_VIDEO):
        print("🛑 Pre-flight verification failed! Video asset is not live with HTTP 200 on production custom domain.")
        sys.exit(1)

    results = []
    for idx, p in enumerate(video_posts):
        print(f"[{idx + 1}/{len(video_posts)}] Scheduling: \"{p['title']}\"")
        print(f"   Due: {p['displayTime']} ({p['dueAt']})")

        input_data = {
            "channelId": CHANNEL_ID,
            "text": p["text"],
            "mode": "customScheduled",
            "dueAt": p["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": [{"video": {"url": p["assetUrl"]}}]
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

    report_path = os.path.join(os.path.dirname(__file__), "como-video-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(video_posts)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
