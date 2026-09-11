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

CDN_BASE = 'https://lornettedaye.com/campaigns/shelton-333am'

HASHTAGS = "#BenShelton #CarlosAlcaraz #USOpen #ArthurAsheStadium #Tennis #GrandSlam #333AM #FifthSet #TennisCommunity #TennisCulture #ATP #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #TennisFans #SleepCanWait #FlushingMeadows #NewYorkTennis"

posts_data = [
    # --- DAY 1: Friday, Sep 11, 2026 ---
    {
        "id": 1,
        "theme_arc": "Faceoff Drama",
        "slot": "Friday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-11T16:00:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-01.png",
        "assetUrl": f"{CDN_BASE}/shelton-01.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of this 3:33 AM battle, and honestly... I'm still sleep deprived haha! 🎾🔥☕

Who else was up watching when Ben Shelton and Carlos Alcaraz pushed each other across 4 hours and 28 minutes of pure fifth-set theater?

Fan Question: Where were you watching from when the final point was played, and how many cups of coffee did it take to survive the morning after? Drop your city below! 👇

This was the final for me. In over 40 years of coaching Olympic champions, you rarely see two young athletes trade heavy artillery with that level of fearless joy. New York never sleeps on greatness.

👉 When your career goes to the fifth set, preparation carries you through. Order *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 2,
        "theme_arc": "Faceoff Drama",
        "slot": "Friday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-11T20:15:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-07.png",
        "assetUrl": f"{CDN_BASE}/shelton-07.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of the Shelton vs. Alcaraz marathon, and my adrenaline is still buzzing! ⚡🏟️

Who else was up watching with their eyes glued to the screen when everyone in your house was asleep?

Fan Question: Ben Shelton's electric roar or Carlos Alcaraz's impossible get—what was THE shot of the match that made you jump off your couch? Tell me below!

Some matches belong to more than a tournament; they become cultural milestones that define a new generation. When you witness athletes refusing to back down under the lights of Arthur Ashe Stadium, it recharges your belief in human potential.

👉 Book Olympian Coach Lornette Daye for your corporate summit on high-performance execution: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 3,
        "theme_arc": "Faceoff Drama",
        "slot": "Friday Night (11:15 PM MDT)",
        "dueAt": "2026-09-12T05:15:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-03.png",
        "assetUrl": f"{CDN_BASE}/shelton-03.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM at Arthur Ashe Stadium, wrapped in blankets with good tennis and zero regrets. 🌙☕🎾

Who else was up watching into the early hours of Friday morning?

Fan Question: Be totally honest: Did you promise yourself you'd turn the TV off after the 3rd set, but the 5th set completely ruined your bedtime?

When the match is this good, sleep can wait. That is the magic of Grand Slam tennis—it turns millions of fans across the globe into one united late-night family.

👉 Master the mental discipline required for life's marathon moments. Read Lornette Daye's books: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 2: Saturday, Sep 12, 2026 ---
    {
        "id": 4,
        "theme_arc": "Faceoff Drama",
        "slot": "Saturday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-12T16:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-01.png",
        "assetUrl": f"{CDN_BASE}/shelton-01.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM, and Saturday morning tennis talk has never been more electric! 🎾💥

Who else was up watching Ben Shelton announce himself to the entire tennis world on the biggest stage in sport?

Fan Question: Between Shelton's 149 MPH missile serve and Alcaraz's touch at the net, which skill would you rather have in your own game?

True athletic majesty is born when supreme power meets emotional composure. When young champions embrace pressure as an invitation, they rewrite history before our eyes.

👉 Inspire your leadership team to command their arena. Book keynote speaking: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 5,
        "theme_arc": "Faceoff Drama",
        "slot": "Saturday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-12T20:15:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-07.png",
        "assetUrl": f"{CDN_BASE}/shelton-07.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of the fifth set, and I still say: This was the final for me! 🏆🤍

Who else was up watching two gladiators leave every single ounce of sweat on the blue hardcourt?

Fan Question: On a scale of 1 to 10, how loud did you scream during that 5th set tiebreak?

In 40+ years coaching Olympic athletes, the champions who stay etched in our memory aren't just the ones who win trophies—they're the ones who give everything they have until 3:33 in the morning.

👉 Build endurance for your own high-stakes challenges. Explore *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 6,
        "theme_arc": "Faceoff Drama",
        "slot": "Saturday Night (11:15 PM MDT)",
        "dueAt": "2026-09-13T05:15:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-03.png",
        "assetUrl": f"{CDN_BASE}/shelton-03.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of the night session, and I'd do it all over again tonight without hesitation! 🌌🎾☕

Who else was up watching Arthur Ashe Stadium stay packed with diehards until 3:33 AM?

Fan Question: If you could attend any night session match in tennis history in person, which one are you picking?

Great tennis people stay. When you are part of a shared moment bigger than yourself, fatigue disappears.

👉 Bring championship poise and culture to your corporate organization: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # --- DAY 3: Sunday, Sep 13, 2026 ---
    {
        "id": 7,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Sunday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-13T16:00:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-02.png",
        "assetUrl": f"{CDN_BASE}/shelton-02.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM under the glowing moon of New York City, and nobody wanted it to end. 🌕🗽🎾

Who else was up watching as the Manhattan skyline lit up the background of a quarterfinal epic?

Fan Question: What is it about New York City and Arthur Ashe Stadium that brings out this kind of unhinged athletic drama?

New York doesn't just host tennis; New York challenges you to prove who you really are when the lights are brightest.

👉 Arm your mindset with timeless wisdom. Get Lornette Daye's life-mastery books: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 8,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Sunday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-13T20:15:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-09.png",
        "assetUrl": f"{CDN_BASE}/shelton-09.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of the greatest late-night quarterfinal in US Open history. 🏟️✨

Who else was up watching Arthur Ashe Stadium glowing like a cathedral in the middle of Queens at 3:33 AM?

Fan Question: How many times during the 5th set did you think: "There's no way he gets that ball back"—and then he did?

Sport at this level is poetry written at 130 miles per hour. It shows us what happens when mental limits are shattered.

👉 Transform your leadership team’s performance standard. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 9,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Sunday Night (11:15 PM MDT)",
        "dueAt": "2026-09-14T05:15:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-05.png",
        "assetUrl": f"{CDN_BASE}/shelton-05.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of the match that wouldn't end in the city that never sleeps. 🚖🌙🎾

Who else was up watching when the yellow cabs were still rolling and the 7 train was packed with fans in tennis hats at 4:00 AM?

Fan Question: Have you ever taken the 7 train out of Flushing Meadows after 2:00 AM? Share your wildest US Open travel story!

A greater game lives here. When passion outlasts convenience, that's when memories are forged.

👉 Discover the fortitude to finish strong in every season of life: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 4: Monday, Sep 14, 2026 ---
    {
        "id": 10,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Monday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-14T16:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-10.png",
        "assetUrl": f"{CDN_BASE}/shelton-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM, and as Monday morning kicks off, the lessons of that night still ring true! 🎾🏙️🔥

Who else was up watching Ben Shelton and Carlos Alcaraz redefine prime-time resilience?

Fan Question: How do you bring that same "5th set at 3:33 AM" intensity into your work week on Monday morning?

Monday demands the same mindset as a tiebreak: Drop the mental distractions, lock into your routine, and own every single point.

👉 Book Olympic coach keynote speaking for your corporate kickoff: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 11,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Monday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-14T20:15:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-02.png",
        "assetUrl": f"{CDN_BASE}/shelton-02.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM, and that golden moon over Arthur Ashe Stadium will stay with me forever. 🌕🎾

Who else was up watching until the bitter, glorious end?

Fan Question: What other sports moment in your lifetime felt like time completely stopped?

When athletes push each other to their absolute limits, the outcome becomes secondary to the honor of competing. That is what sport is supposed to teach us.

👉 Learn how to navigate high-stakes pressure with grace: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 12,
        "theme_arc": "Midnight NYC Skyline",
        "slot": "Monday Night (11:15 PM MDT)",
        "dueAt": "2026-09-15T05:15:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-05.png",
        "assetUrl": f"{CDN_BASE}/shelton-05.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of the match that refused to yield to the clock. ⏰🌃🎾

Who else was up watching when 3:33 AM felt like 7:00 PM because the energy in Queens was vibrating so high?

Fan Question: Who did you text at 3:00 AM while watching this match? Did they actually text you back?

Authentic human connection doesn't check the clock. When excellence is on display, we stay.

👉 Equip your leaders to execute with composure when the stakes are highest: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # --- DAY 5: Tuesday, Sep 15, 2026 ---
    {
        "id": 13,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Tuesday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-15T16:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-04.png",
        "assetUrl": f"{CDN_BASE}/shelton-04.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM, because in the fifth set: It’s just. one. more. point. Then another. Then another. 🎾⏰🔥

Who else was up watching when neither player would surrender a single inch of baseline?

Fan Question: When you are totally exhausted in life or sports, what is the internal thought that pushes you to take one more step?

Greatness waits a little longer for those who refuse to quit. Discipline creates freedom.

👉 Read *Survival Skills for Believers* for deep mental toughness: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 14,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Tuesday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-15T20:15:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-08.png",
        "assetUrl": f"{CDN_BASE}/shelton-08.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of the fifth set, watching sweat fly off the strings at 3:33 AM! 💦🎾⚡

Who else was up watching Ben Shelton dig deeper into his reserve tank than he ever had before?

Fan Question: What is your favorite quote about resilience under maximum pressure?

In elite coaching, I tell athletes: You don't discover who you are when things are easy. You find out when you're 4 hours in, legs burning, and the crowd is screaming.

👉 Book keynote speaking on ethical leadership & champion poise: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 15,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Tuesday Night (11:15 PM MDT)",
        "dueAt": "2026-09-16T05:15:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-06.png",
        "assetUrl": f"{CDN_BASE}/shelton-06.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM. Four hours. Twenty-eight minutes. Five sets. ⏳✨

Who else was up watching history be made while the rest of the world slept?

Fan Question: If you had to describe this match in just ONE word, what word are you choosing?

Some matches live forever. Not because of who hoisted the cup, but because of how deeply both fighters respected the arena.

👉 Build the mental architecture of a champion. Visit: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 6: Wednesday, Sep 16, 2026 ---
    {
        "id": 16,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Wednesday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-16T16:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-11.png",
        "assetUrl": f"{CDN_BASE}/shelton-11.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM, and Wednesday morning is a great reminder that true grit is timeless. 🎾🏆

Who else was up watching when every single service game felt like match point?

Fan Question: What was the most clutch shot you saw Ben Shelton hit during the entire tournament?

When you train your mind to stay calm when the arena is loud, no challenge can knock you off balance.

👉 Keynote speaking with Olympian Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 17,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Wednesday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-16T20:15:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-04.png",
        "assetUrl": f"{CDN_BASE}/shelton-04.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM, watching two 20-somethings play like seasoned warriors. ⚔️🎾

Who else was up watching the sheer physical courage on display in Arthur Ashe Stadium?

Fan Question: How do you reset your mind after losing a crucial point so you can win the next one?

The secret of elite competitors is simple: They don't carry the baggage of the last point into the next swing. Reset. Refocus. Execute.

👉 Equip your mindset with *Survival Skills for Women* & *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 18,
        "theme_arc": "Fifth-Set Grind",
        "slot": "Wednesday Night (11:15 PM MDT)",
        "dueAt": "2026-09-17T05:15:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-08.png",
        "assetUrl": f"{CDN_BASE}/shelton-08.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM, and the magic of that night still hasn't faded. 🌙🎾✨

Who else was up watching when Carlos and Ben met at the net and shared that unforgettable embrace?

Fan Question: How important is sportsmanship to you when watching your favorite athletes compete?

True champions fight with ferocious intensity between the lines, but honor their opponent the second the battle concludes. Dignity always wins.

👉 Elevate your organization's culture with executive leadership programs: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # --- DAY 7: Thursday, Sep 17, 2026 ---
    {
        "id": 19,
        "theme_arc": "Typographic Grand Finale",
        "slot": "Thursday Morning (10:00 AM MDT)",
        "dueAt": "2026-09-17T16:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 10:00 AM MDT",
        "assetFile": "shelton-06.png",
        "assetUrl": f"{CDN_BASE}/shelton-06.png",
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""I stayed up until the end of 3:33 AM. Four hours. Twenty-eight minutes. Five sets. 💛🎾

Who else was up watching the match that redefined what an American tennis night session can be?

Fan Question: As we wrap up this historic week, what was your single favorite memory from this US Open?

Some matches live forever. For every fan who stayed up and every young player who watched in awe: Keep swinging with full conviction.

👉 Master the blueprint of high-performance fortitude: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 20,
        "theme_arc": "Typographic Grand Finale",
        "slot": "Thursday Afternoon (2:15 PM MDT)",
        "dueAt": "2026-09-17T20:15:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 2:15 PM MDT",
        "assetFile": "shelton-11.png",
        "assetUrl": f"{CDN_BASE}/shelton-11.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM, and I will never forget the feeling in that stadium. 🌟🎾

Who else was up watching with chills down their spine on match point?

Fan Question: Who is your pick to win the next Grand Slam title between Ben Shelton and Carlos Alcaraz?

When talent is matched by indomitable will, there is no ceiling to what can be achieved.

👉 Book Lornette Daye for your corporate keynote or annual summit: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 21,
        "theme_arc": "Typographic Grand Finale",
        "slot": "Thursday Night (11:15 PM MDT)",
        "dueAt": "2026-09-18T05:15:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 11:15 PM MDT",
        "assetFile": "shelton-01.png",
        "assetUrl": f"{CDN_BASE}/shelton-01.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""I stayed up until the end of 3:33 AM. And I would stay up all over again tomorrow. 🎾✨🤍

Who else was up watching when history was made under the New York sky?

Final Question: To all the night owls, the tennis lovers, and the believers: What match should we break down next? Leave your suggestions below!

This was the final for me. Own your arena. Lead with dignity. Finish strong.

Lornette Daye | 40+ Years in Olympic Athletics & Leadership Mastery

👉 Book corporate keynote speaking & executive coaching: lornettedaye.com/speaking
👉 High-performance books & life lessons: lornettedaye.com/books

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
    unique_assets = list(dict.fromkeys(p["assetUrl"] for p in posts_data))
    all_ok = True
    for url in unique_assets:
        file_name = url.split('/')[-1]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        try:
            with urllib.request.urlopen(req, context=ctx) as r:
                if r.status == 200:
                    cl = r.headers.get("Content-Length", "unknown")
                    print(f"   ✅ [200 OK] {file_name} ({cl} bytes)")
                else:
                    print(f"   ❌ [{r.status}] {file_name}")
                    all_ok = False
        except Exception as e:
            print(f"   ❌ [ERROR] {file_name}: {e}")
            all_ok = False
    print("======================================================\n")
    return all_ok

def main():
    print("======================================================")
    print("🎾 Ben Shelton 3:33 AM US Open Campaign: 21-Post Cadence")
    print("Window: Friday, Sep 11 to Thursday, Sep 17, 2026 (7 Days)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(posts_data):
        print(f"[{idx + 1}/{len(posts_data)}] Scheduling Post #{p['id']} ({p['theme_arc']}): \"{p['slot']}\"")
        print(f"   Due: {p['dueAt']} | CTA: {p['cta']}")
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

    report_path = os.path.join(os.path.dirname(__file__), "shelton-campaign-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Shelton Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
