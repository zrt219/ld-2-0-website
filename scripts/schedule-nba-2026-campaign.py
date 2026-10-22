# -*- coding: utf-8 -*-
"""
Automated Buffer Campaign Scheduler: NBA 2026 Season Launch Campaign
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Destination: Lornette's Foundations (https://lornettedaye.com/foundations)
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

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN')
if not TOKEN:
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('BUFFER_ACCESS_TOKEN='):
                    TOKEN = line.strip().split('=', 1)[1].strip()
                    break
if not TOKEN:
    TOKEN = 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0'
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

CAMPAIGN_POSTS = [
    {
        "id": 1,
        "athlete": "Anthony Edwards (Hero - Personal Favorite)",
        "slot": "Thursday Oct 22 (08:30 AM MDT)",
        "dueAt": "2026-10-22T14:30:00.000Z",
        "assetFile": "nba-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-01.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """ANTHONY EDWARDS: THE NEXT LEVEL ALWAYS DEMANDS MORE. 🐺🏀

When people ask me who my personal favorite player in today's NBA is, my answer is immediate: Anthony Edwards.

It is not just the explosive first step, the rim-rattling finishes, or the sheer joy he brings to the court. It is his absolute hunger to grow into every room he enters. When Anthony arrived in Minnesota, he possessed world-class raw athletic tools. But what separates exciting young talent from true championship contenders is the willingness to confront weaknesses. Edwards committed to lockdown perimeter defense, rebuilt his decision-making in the clutch, and embraced the responsibility of carrying a franchise.

In my four decades coaching Olympic-level athletes and national champions, I teach one unbreakable truth: arriving at the next level is only the beginning. The real test is meeting the elevated standard the new level demands.

Whether you are an aspiring pro athlete or an executive leading a high-stakes enterprise, you cannot rely on yesterday's habits to conquer tomorrow's arena.

Are you preparing your game for where you are, or where you want to lead?

If you are an elite athlete, parent of an emerging competitor, or sports organization looking to master the mental, physical, and emotional disciplines that create enduring excellence:

👉 Explore Lornette's Foundations, our complete athlete development system: https://lornettedaye.com/foundations
💬 Or send me a direct message right here on LinkedIn to start a conversation about our athlete development cohorts.

#AnthonyEdwards #MinnesotaTimberwolves #NBAPrep #OlympicMindset #AthleteDevelopment #ChampionMindset #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 2,
        "athlete": "Shai Gilgeous-Alexander",
        "slot": "Thursday Oct 22 (01:00 PM MDT)",
        "dueAt": "2026-10-22T19:00:00.000Z",
        "assetFile": "nba-canadian-01-sga.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-01-sga.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """SHAI GILGEOUS-ALEXANDER: CALM PRECISION AND CANADIAN GREATNESS. 🇨🇦⚡

There is a quiet majesty in watching Shai Gilgeous-Alexander dismantle an opposing defense.

He never rushes. He never panics. Regardless of the crowd noise, the shot clock, or the physical pressure thrown his way, Shai dictates the tempo of the entire arena. Coming out of Hamilton, Ontario, Shai built his game on kinetic balance, deceptive deceleration, and an unshakable inner stillness. That composure is not accidental: it is the hallmark of an athlete who has mastered his emotional regulation.

In our work with elite competitors, we emphasize Foundation 2: Champion Mindset, and Foundation 5: Pressure, Emotional Regulation, and Recovery. When you control your internal state, external chaos cannot touch you.

Canadian basketball is standing on the world stage because players like Shai prove that poise and relentless preparation will always outlast emotional volatility.

Leaders and athletes: When the game speeds up around you, do you rush, or do you command your own pace?

👉 Ready to build unyielding mental poise and competitive mastery? Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss guided coaching for your athletes.

#ShaiGilgeousAlexander #ThunderUp #CanadaBasketball #ChampionMindset #EmotionalRegulation #EliteAthletes #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 3,
        "athlete": "Jamal Murray",
        "slot": "Friday Oct 23 (08:30 AM MDT)",
        "dueAt": "2026-10-23T14:30:00.000Z",
        "assetFile": "nba-canadian-02-murray.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-02-murray.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """JAMAL MURRAY: BUILT FOR THE BIG MOMENTS. 🏹🏔️

Championships are won in the clutch, but clutch players are forged in the dark.

From his childhood training in Kitchener, Ontario, doing push-ups in the snow and practicing meditation drills with his father, Jamal Murray was conditioned to welcome pressure rather than dread it. When the Denver Nuggets need a season-defining bucket with two seconds remaining, everyone in the building knows where the ball is going, yet Jamal's heart rate stays level.

Even more inspiring is how he responded to a catastrophic knee injury: turning a devastating setback into fuel that powered an NBA championship run. In Lornette's Foundations, Foundation 4 is Resilience After Setback. True resilience is not merely bouncing back; it is returning stronger, sharper, and more purpose-driven than before.

Pressure is a privilege reserved for those who have put in the work.

How do you train your mind to stay steady when the lights are brightest?

👉 Master the mental routines and pressure-management frameworks of champions. Learn about Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss private athlete and team mentorship.

#JamalMurray #DenverNuggets #MileHighBasketball #ClutchPerformance #ResilienceAfterSetback #CanadaBasketball #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 4,
        "athlete": "RJ Barrett",
        "slot": "Friday Oct 23 (01:00 PM MDT)",
        "dueAt": "2026-10-23T19:00:00.000Z",
        "assetFile": "nba-canadian-03-barrett.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-03-barrett.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """RJ BARRETT: REPRESENTING HOME AND CARRYING EXPECTATIONS. 🦖🍁

Wearing your country's name or your hometown jersey on your chest carries a unique weight.

Mississauga's RJ Barrett has carried immense expectations since his teenage years as the top high school player in the world. Now back home leading the Toronto Raptors, RJ approaches every single night with blue-collar professionalism, transition aggression, and deep pride in representing his community.

In my coaching career spanning four decades with national teams and Olympians, I have seen high expectations break athletes who lack an anchored identity. That is why Foundation 1 in Lornette's Foundations is Identity Beyond Sport, complemented by Foundation 7: Family and Community Support. When an athlete knows who they are off the court, public scrutiny cannot erode their self-worth.

When you stay grounded in your values and community, the weight of expectation becomes fuel for excellence.

How do you protect your inner identity while performing under intense external eyes?

👉 Empower your athlete with the character and resilience to thrive at the next level. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect directly with me via LinkedIn DM to learn more about our athlete development programs.

#RJBarrett #WeTheNorth #TorontoRaptors #CanadaBasketball #IdentityBeyondSport #YouthAthleteDevelopment #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 5,
        "athlete": "Luguentz Dort",
        "slot": "Saturday Oct 24 (09:30 AM MDT)",
        "dueAt": "2026-10-24T15:30:00.000Z",
        "assetFile": "nba-canadian-05-dort.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-05-dort.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """LUGUENTZ DORT: UNCOMPROMISING EFFORT AND BLUE-COLLAR GRIT. 🔒🛡️

Offense sells tickets. Relentless, brick-wall defense wins playoff series.

Luguentz Dort's journey from Montreal North to becoming the most feared perimeter lockdown defender in the NBA is a masterclass in professional purpose. Undrafted in 2019, Lu did not pout or search for excuses. He found a skill that every championship roster desperately needs, mastered it with obsessive physical conditioning, and made the "Dorture Chamber" legendary.

In Lornette's Foundations, Foundation 3 is Discipline Systems: the daily, non-negotiable habits that turn potential into undeniable impact. Dort proves that when you commit 100% to your role, respect your craft, and bring unyielding physical effort every night, the world has no choice but to recognize your greatness.

Are you waiting for the perfect opportunity, or are you making yourself indispensable through sheer discipline?

👉 Build the mental grit and discipline systems that separate contenders from pretenders. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to inquire about athlete coaching and team workshops.

#LuguentzDort #LockdownDefense #MontrealMade #DisciplineSystems #UnderdogMindset #CanadaBasketball #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 6,
        "athlete": "Nickeil Alexander-Walker",
        "slot": "Sunday Oct 25 (10:00 AM MDT)",
        "dueAt": "2026-10-25T16:00:00.000Z",
        "assetFile": "nba-canadian-04-alexander-walker.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-04-alexander-walker.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """NICKEIL ALEXANDER-WALKER: THE POWER OF REINVENTION AND PATIENCE. 🐺📈

Overnight success in elite athletics is almost always an illusion.

When Toronto native Nickeil Alexander-Walker entered the league, finding his permanent footing took time, trades, and deep soul-searching. Instead of resisting change, Nickeil reinvented his game: transforming from a high-usage ball-handler into one of the league's most devastating point-of-attack defenders and reliable corner-three marksmen.

That transition requires humility and an ego-free dedication to team victory. In Lornette's Foundations, Foundation 4 is Resilience After Setback and Foundation 6 is Communication and Presence. When an athlete learns to accept coaching, adapt their skill set, and embrace their authentic role, their true breakthrough begins.

Growth requires you to let go of who you used to be so you can become who your team needs you to be.

What part of your approach are you willing to adapt to unlock your next level of performance?

👉 Discover the Olympic-level mental frameworks that help athletes adapt and excel through transitions. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me on LinkedIn to explore cohort openings.

#NickeilAlexanderWalker #Timberwolves #CanadaBasketball #Resilience #AthleteGrowth #Adaptability #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 7,
        "athlete": "Andrew Nembhard",
        "slot": "Monday Oct 26 (08:15 AM MDT)",
        "dueAt": "2026-10-26T14:15:00.000Z",
        "assetFile": "nba-canadian-09-nembhard.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-09-nembhard.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """ANDREW NEMBHARD: COMMANDING THE ARENA WITH BASKETBALL IQ. 🧠⚡

True leadership on the floor is not loud: it is decisive, prepared, and composed.

Aurora, Ontario's Andrew Nembhard slipped into the second round of the NBA Draft, but anyone who watched him navigate the playoffs with the Indiana Pacers saw a master technician at work. Facing the highest-pressure moments in Madison Square Garden and Boston, Nembhard controlled the offense, hit game-winners, and guarded the opposing team's best perimeter scorer with icy confidence.

His superpower is preparation. He reads defenses three steps ahead because he studies the game with monastic discipline. In Lornette's Foundations, Foundation 2 is Champion Mindset and Foundation 8 is Career Readiness. High basketball IQ is not an innate gift: it is the direct dividend of deliberate, analytical study.

The scoreboard rewards the execution you see, but the outcome was decided by the preparation nobody witnessed.

How deeply are you studying your competition before you step onto the floor?

👉 Elevate your athlete's tactical intelligence and decision-making under pressure. Learn about Lornette's Foundations: https://lornettedaye.com/foundations
💬 Inquire today via LinkedIn DM to discuss our athlete development curriculum.

#AndrewNembhard #PacersBasketball #IndianaPacers #BasketballIQ #MentalPreparation #CanadaBasketball #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 8,
        "athlete": "Bennedict Mathurin",
        "slot": "Monday Oct 26 (01:30 PM MDT)",
        "dueAt": "2026-10-26T19:30:00.000Z",
        "assetFile": "nba-canadian-07-mathurin.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-07-mathurin.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """BENNEDICT MATHURIN: PLAYING WITH UNAPOLOGETIC FEARLESSNESS. ⚜️🔥

You cannot coach an athlete to play timidly and expect them to win championships.

From the courts of Montreal, Quebec, Bennedict Mathurin brought a fierce, uncompromising edge to the NBA. He attacks the paint without hesitation, invites physical contact, and plays every single possession as if he has everything to prove. Behind that intensity is a deep emotional anchor: playing in honor of his family and the memories that shape his relentless drive.

In Lornette's Foundations, Foundation 1 is Identity Beyond Sport and Foundation 9 is Personal Brand and Story. When an athlete connects their athletic effort to a purpose larger than themselves, fear evaporates. They play with pure freedom because they are fueled by something deeper than a stat sheet.

When your purpose is rooted in family, legacy, and gratitude, pressure turns into passion.

What is the deeper "why" that fuels your competitive fire?

👉 Help your athletes discover their deeper purpose and build unstoppable confidence on the court. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Message me directly on LinkedIn to discuss program enrollment.

#BennedictMathurin #MontrealBasketball #FearlessMindset #PurposeDrivenAthlete #CanadaBasketball #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 9,
        "athlete": "Zach Edey",
        "slot": "Tuesday Oct 27 (08:30 AM MDT)",
        "dueAt": "2026-10-27T14:30:00.000Z",
        "assetFile": "nba-canadian-08-edey.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-08-edey.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """ZACH EDEY: OWNING YOUR SIZE, SILENCING SKEPTICS. 🐻🇨🇦

Greatness often begins where others see limitations.

Throughout his rise from Toronto to back-to-back National College Player of the Year honors at Purdue, and now stepping into the paint for the Memphis Grizzlies, Zach Edey was constantly told the modern game had passed traditional big men by. Instead of shrinking to fit other people's narratives, Zach worked relentlessly on his conditioning, footwork, and rim deterrence.

He embraced who he is with complete conviction. In Lornette's Foundations, Foundation 1 is Identity Beyond Sport and Foundation 6 is Communication and Presence. An athlete must learn to dominate their unique physical and mental profile rather than imitating someone else's style.

When you master your authentic strengths with relentless discipline, the game adjusts to you.

Are you trying to fit someone else's mold, or are you mastering your unique advantage?

👉 Equip emerging athletes to build authentic physical presence and mental toughness. Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect via LinkedIn DM to explore mentorship options.

#ZachEdey #MemphisGrizzlies #CanadaBasketball #PurdueAlum #PhysicalPresence #AthleteResilience #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 10,
        "athlete": "Shaedon Sharpe",
        "slot": "Wednesday Oct 28 (08:30 AM MDT)",
        "dueAt": "2026-10-28T14:30:00.000Z",
        "assetFile": "nba-canadian-06-sharpe.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-06-sharpe.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """SHAEDON SHARPE: TURNING RARE GIFT INTO CRAFT MASTERY. 🌹✈️

Natural athletic talent can open the door, but craft mastery determines how long you stay in the room.

London, Ontario's Shaedon Sharpe possesses vertical explosion and aerial grace that few humans on earth will ever experience. Yet the most exciting development in his young NBA career in Portland is not the highlight dunks: it is his growth as a playmaker, his defensive focus, and his expanding shot creation.

In my four decades coaching Olympic champions, I remind athletes that God-given gifts are merely raw materials. In Lornette's Foundations, Foundation 3 is Discipline Systems and Foundation 10 is Legacy and Community Impact. When an athlete pairs world-class physical tools with dedicated study and daily consistency, they do not just make highlights: they leave an indelible legacy.

Talent is your starting line. Relentless refinement is your finish line.

How are you developing the fundamentals behind your greatest natural strengths?

👉 Help your athletes turn raw ability into sustainable athletic excellence. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me on LinkedIn to start the conversation.

#ShaedonSharpe #RipCity #TrailBlazers #CanadaBasketball #AthleteExcellence #DisciplineSystems #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": 11,
        "athlete": "Dillon Brooks",
        "slot": "Thursday Oct 29 (08:30 AM MDT)",
        "dueAt": "2026-10-29T14:30:00.000Z",
        "assetFile": "nba-canadian-10-brooks.png",
        "assetUrl": "https://lornettedaye.com/campaigns/nba/nba-canadian-10-brooks.png",
        "cta": "Lornette's Foundations (lornettedaye.com/foundations)",
        "text": """DILLON BROOKS: COMPETING WITH UNAPOLOGETIC CONVICTION. ☀️🛡️

Every championship contender needs a tone-setter who does not blink in the face of conflict.

Mississauga's Dillon Brooks plays with a competitive conviction that electrifies his teammates and disrupts opponents. Whether anchoring Canada's perimeter defense to historic international victories or setting a physical culture in the NBA, Dillon brings an unwavering belief in his preparation and an unmatched competitive heart.

In Lornette's Foundations, Foundation 6 is Communication and Presence and Foundation 2 is Champion Mindset. Elite sport is not for the faint of heart: it requires athletes to stand tall under pressure, accept the villain narrative if necessary, and compete for every inch of hardwood without hesitation.

Conviction is contagious. When your leader refuses to back down, the entire team stands taller.

Do your athletes bring quiet confidence or undeniable competitive fire to the arena?

👉 Instill unyielding mental toughness, presence, and competitive poise in your players. Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Message me directly here on LinkedIn to learn about team and individual athlete development.

#DillonBrooks #PhoenixSuns #Rockets #CanadaBasketball #CompetitiveConviction #DefensiveEdge #LornettesFoundations #LornetteDaye"""
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
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }
    except Exception as e:
        return {"error": str(e)}

def verify_all_assets_live():
    print("Pre-Flight Zero-404 Invariant Check:")
    ctx = ssl._create_unverified_context()
    all_ok = True
    for p in CAMPAIGN_POSTS:
        url = p["assetUrl"]
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status == 200:
                    print(f"  [HTTP 200 OK] {p['assetFile']}")
                else:
                    print(f"  [FAILED {resp.status}] {url}")
                    all_ok = False
        except Exception as e:
            print(f"  [FAILED {e}] {url}")
            all_ok = False
    return all_ok

def main():
    print("=" * 80)
    print("AUTOMATED BUFFER CAMPAIGN: NBA 2026 SEASON LAUNCH (11 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Invariant Check: Verify NO em dashes in any post copy
    for p in CAMPAIGN_POSTS:
        if "—" in p["text"] or "&mdash;" in p["text"] or "\u2014" in p["text"]:
            raise ValueError(f"EM DASH INVARIANT VIOLATION in Post {p['id']} ({p['athlete']})")
        if "Coach Lornette" in p["text"]:
            raise ValueError(f"COACH LORNETTE INVARIANT VIOLATION in Post {p['id']} ({p['athlete']})")

    # Step 1: Pre-flight Live Asset Verification
    if not verify_all_assets_live():
        print("\nHalted: Not all assets returned HTTP 200 on production. Aborting Buffer schedule.")
        sys.exit(1)

    print("\nAll 11 production assets verified HTTP 200 OK! Proceeding to Buffer API...")

    report_path = os.path.join(os.path.dirname(__file__), "nba-campaign-master-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("results", [])
                for item in items:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Warning reading existing report: {e}")

    for post in CAMPAIGN_POSTS:
        pid = post["id"]
        if pid in results:
            print(f"Post {pid} ({post['athlete']}) already scheduled -> ID: {results[pid]['postId']}. Skipping.")
            continue

        print(f"\nScheduling Post {pid}/11: {post['athlete']}...")
        print(f"  Slot: {post['slot']} | DueAt: {post['dueAt']}")
        print(f"  Asset: {post['assetUrl']}")

        res = schedule_post(post)

        if "error" in res:
            print(f"  -> HTTP Error: {res['error']}")
            results[pid] = {
                "id": pid,
                "athlete": post["athlete"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "status": "error",
                "error": res["error"],
                "assetUrl": post["assetUrl"]
            }
            continue

        data = res.get("data", {}).get("createPost", {})
        typename = data.get("__typename")

        if typename == "PostActionSuccess":
            created_post = data.get("post", {})
            post_id = created_post.get("id")
            print(f"  -> SUCCESS! Scheduled Post ID: {post_id}")
            results[pid] = {
                "id": pid,
                "athlete": post["athlete"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "postId": post_id,
                "status": "scheduled",
                "assetUrl": post["assetUrl"],
                "cta": post["cta"]
            }
        else:
            msg = data.get("message", "Unknown error")
            print(f"  -> FAILED ({typename}): {msg}")
            results[pid] = {
                "id": pid,
                "athlete": post["athlete"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "status": "failed",
                "errorType": typename,
                "message": msg,
                "assetUrl": post["assetUrl"]
            }

        # Polite delay between Buffer API requests
        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print("SCHEDULING RUN COMPLETE")
    print(f"Report saved to: {report_path}")
    print("=" * 80)

if __name__ == '__main__':
    main()
