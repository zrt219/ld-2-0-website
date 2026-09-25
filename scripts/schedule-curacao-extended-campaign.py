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

VIDEO_URL = 'https://lornettedaye.com/campaigns/curacao/curacao-extended.mp4'

posts_data = [
    {
        "id": 1,
        "type": "video",
        "slot": "Friday 7:00 AM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T13:00:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "WHERE WERE YOU WHEN THE 4TH GOAL HIT THE BACK OF THE NET? 🇨🇼🌊\n\n"
            "Down 0-3 on the road against Costa Rica at halftime. "
            "Down on the scoreboard, but never broken in spirit.\n\n"
            "Then the second half unfolded:\n"
            "• Kenji Gorré cuts the deficit.\n"
            "• Tahith Chong levels the psychological momentum.\n"
            "• Kenji Gorré strikes again to make it 3-3.\n"
            "• Jordi Paulina seals the 4-3 triumph in the closing minutes.\n\n"
            "In four decades coaching Olympic athletes, I have witnessed many comebacks, "
            "but what Curaçao executed here was pure competitive conviction. "
            "They refused damage limitation. They stepped onto the pitch and altered history.\n\n"
            "To every supporter watching across Willemstad, the Netherlands, and around the world: "
            "How loud did you celebrate when that final whistle blew? Tell us your match story below!\n\n"
            "Ban Kòrsou!\n\n"
            "Build unshakeable belief when the odds look impossible. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Olympic-caliber mental toughness to your team or keynote: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 2,
        "type": "video",
        "slot": "Friday 12:00 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T18:00:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "REWATCH THIS SEQUENCE CLOSELY. WHAT HAPPENS WHEN A SQUAD REFUSES TO FOLD? 🌊🇨🇼\n\n"
            "Costa Rica 3, Curaçao 0 at the interval.\n\n"
            "Most teams would have dropped into a passive defensive shape to avoid further embarrassment. "
            "Instead, Team Curaçao recognized that pressure is merely information. "
            "They adjusted their pressing angles, accelerated ball circulation, and attacked with supreme poise.\n\n"
            "Four unanswered goals away from home against a regional giant.\n\n"
            "Who was the player on this pitch that inspired you the most during this historic 4-3 comeback? "
            "Drop your vote and favorite moment in the comments.\n\n"
            "Dushi Kòrsou stood tall.\n\n"
            "Develop championship focus, tactical discipline, and mental resilience. "
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and corporate workshops: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 3,
        "type": "video",
        "slot": "Friday 2:30 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-25T20:30:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Official Championship Library ($14.99 CAD) & Speaking",
        "text": (
            "THE FULL EXTENDED SEQUENCE: PURE HEART AND RELENTLESS STAMINA 🇨🇼⚡\n\n"
            "Watch the closing 15 minutes of this match tape. "
            "Every sprint carries the energy of the entire island. "
            "Every 50-50 challenge represents decades of ambition and Caribbean pride.\n\n"
            "When the final goal crossed the line to complete the 4-3 comeback, "
            "it proved once and for all that geographic size never defines competitive ceiling.\n\n"
            "How did your household react when the comeback was complete? Did you wake up the neighbors? "
            "Let us hear the stories from Bandabou to Banda'riba and across the global diaspora!\n\n"
            "Ban Kòrsou!\n\n"
            "Equip your mind for high-pressure execution. "
            "Explore Coach Lornette Daye's complete digital book catalog ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive coaching and keynote speaking: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 4,
        "type": "video",
        "slot": "Friday 8:00 PM MDT (Sep 25, 2026)",
        "dueAt": "2026-09-26T02:00:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "FRIDAY NIGHT REPLAY: THE BLUE WAVE THAT SHOCKED CONCACAF 🇨🇼🌊\n\n"
            "Nothing unites a culture quite like an impossible victory delivered on the international stage.\n\n"
            "Costa Rica 3, Curaçao 4.\n\n"
            "Look at the poise in transition, the collective composure in the penalty area, "
            "and the relentless spirit of a team that simply refused to lose. "
            "This is what athletic legacy is made of.\n\n"
            "Share this replay with someone who needs an injection of belief heading into the weekend. "
            "What was your personal favorite goal from this masterclass?\n\n"
            "Ban Kòrsou!\n\n"
            "Learn how elite performers turn extreme adversity into career-defining triumph. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Olympic-caliber leadership principles to your organization: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 5,
        "type": "video",
        "slot": "Saturday 9:30 AM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-26T15:30:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "SATURDAY MORNING FILM STUDY: BELIEF IN MOTION 🇨🇼⚽\n\n"
            "Study this extended match footage from a tactical and psychological standpoint.\n\n"
            "When you trail 0-3 at halftime against a tournament favorite, chaos is easy. "
            "Panic is easy. Frustration is easy.\n\n"
            "What is difficult, and what separates champions from everyone else, is emotional regulation. "
            "Team Curaçao stayed within their structural foundation, trusted their preparation, "
            "and executed one possession at a time until the scoreline read 4-3 in their favor.\n\n"
            "What was the exact turning point in your opinion? Which play shifted the psychological momentum? "
            "Break down the match with us in the comments.\n\n"
            "Master emotional poise and focus under tournament pressure. "
            "Discover Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote presentations and athletic mindset workshops: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 6,
        "type": "video",
        "slot": "Saturday 2:30 PM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-26T20:30:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "FROM 0-3 DOWN TO A 4-3 VICTORY: CULTURE OVER CIRCUMSTANCE 🌊🇨🇼\n\n"
            "This extended match tape will be studied for decades across the Caribbean region.\n\n"
            "It proves that when a locker room shares collective trust, clarity of vision, "
            "and unrelenting courage, no deficit is permanent. "
            "Curaçao came into hostile territory, absorbed early adversity, and delivered a masterclass in modern football.\n\n"
            "Drop a blue heart or Curaçao flag in the comments if you stand proud with Team Curaçao wherever you are in the world! "
            "The Blue Wave is only beginning.\n\n"
            "Ban Kòrsou!\n\n"
            "Turn setbacks into your greatest springboard. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive coaching and corporate leadership seminars: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 7,
        "type": "video",
        "slot": "Saturday 8:00 PM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-27T02:00:00.000Z",
        "assetFile": "curacao-extended.mp4",
        "assetUrl": VIDEO_URL,
        "cta": "Official Digital Book Library ($14.99 CAD) & Speaking",
        "text": (
            "WEEKEND FINALE: THE HISTORIC 4-3 COMEBACK REWATCH 🇨🇼🏆\n\n"
            "Over 170 seconds of pure heart, clinical finishing, and unwavering national dignity.\n\n"
            "When the scoreboard was 3-0 against them, Team Curaçao decided that their story was far from over. "
            "Four goals later, the entire CONCACAF region took notice of what island pride can achieve.\n\n"
            "Tag a friend, teammate, or family member who was watching this match live. "
            "Let us make sure this generation never forgets what is possible when you refuse to quit.\n\n"
            "Ban Kòrsou!\n\n"
            "Explore Coach Lornette Daye's full library of championship guides ($14.99 CAD each): https://lornettedaye.com/books\n\n"
            "Keynote bookings and high-performance leadership consulting: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #IslandPride #SmallIslandBigDreams #CaribbeanToTheWorld #LornetteDaye"
        )
    }
]

def check_for_em_dashes():
    errors = []
    for p in posts_data:
        t = p["text"]
        if "—" in t or "&mdash;" in t or "\u2014" in t:
            errors.append(f"Post {p['id']} contains an em dash!")
    if errors:
        for err in errors:
            print("ERROR:", err)
        sys.exit(1)
    print("EM DASH CHECK: PASS (Zero em dashes found across all 7 posts).")

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
                    "video": {
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

def main():
    print("=" * 70)
    print("STARTING CURAÇAO EXTENDED VIDEO CAMPAIGN SCHEDULING (7 POSTS)")
    print("=" * 70)

    check_for_em_dashes()

    report_path = os.path.join(os.path.dirname(__file__), "curacao-extended-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]

        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/7] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/7] Scheduling Post #{p_id} ({post['slot']}) - Due: {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {wait_sec + 5}s...")
                time.sleep(wait_sec + 5)
                continue

            create_post_data = res.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                st = post_obj.get("status")
                due = post_obj.get("dueAt")
                print(f"  >>> SUCCESS: Post ID {b_id} scheduled for {due} (status: {st})")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetFile": post["assetFile"],
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "assetFile": post["assetFile"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/7 posts scheduled successfully.")

if __name__ == "__main__":
    main()
