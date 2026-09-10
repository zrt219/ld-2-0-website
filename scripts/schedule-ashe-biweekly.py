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

ASSET_URL = 'https://lornettedaye.com/campaigns/spotlight-sept11/arthur-ashe-1968-champion.jpg'

drops = [
    {
        "id": 1,
        "title": "A Champion Changes More Than a Game: Arthur Ashe 1968 (Drop 1)",
        "slot": "Friday Morning Peak (8:30 AM MDT)",
        "dueAt": "2026-09-11T14:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:30 AM MDT",
        "assetUrl": ASSET_URL,
        "text": """A CHAMPION CHANGES MORE THAN A GAME. 🏆✨

In September 1968, Arthur Ashe didn't just win the inaugural US Open—he shattered barriers as the first Black man to win a Grand Slam in the Open Era. He carried the weight of history not with anger, but with quiet majesty, intellectual brilliance, and moral fortitude.

In 40+ years of coaching Olympians, national champions, and executive leaders, I have learned that trophies collect dust, but character builds generational pathways.

Arthur Ashe showed us that sport is not merely an arena for athletic conquest—it is a platform to elevate humanity, champion equality, and build a brighter tomorrow.

When you enter your arena today, ask yourself: Are you playing for the scoreboard, or are you executing for a higher purpose?

Stand tall. Lead with dignity. Finish strong.

👉 Book keynote speaking on ethical leadership & champion mindset: lornettedaye.com/speaking
👉 Read *Survival Skills for Believers*: lornettedaye.com/books

#ArthurAshe #USOpen #TennisHistory #GrandSlam #BlackExcellence #CivilRights #LeadershipPoise #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #ATP #TennisHeritage #CourageUnderPressure""",
        "bufferPostId": "6aa25728c11e8719057a7447",
        "status": "scheduled",
        "scheduledAt": "2026-09-10T07:06:54Z"
    },
    {
        "id": 2,
        "title": "A Champion Changes More Than a Game: Arthur Ashe 1968 (Drop 2)",
        "slot": "Tuesday Morning Peak (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 AM MDT",
        "assetUrl": ASSET_URL,
        "text": """A CHAMPION CHANGES MORE THAN A GAME: ARTHUR ASHE 1968 🏆✨

In September 1968, Arthur Ashe shattered barriers as the first Black man to win a Grand Slam in the Open Era. He carried the weight of history not with bitterness or noise, but with quiet majesty, moral fortitude, and leadership dignity.

In 40+ years of coaching Olympians, national champions, and executive leaders, I have seen that athletic greatness alone does not create timeless leaders. True greatness comes when your character and purpose transcend the arena.

Arthur Ashe proved that a champion doesn't just play to win games—they elevate humanity and open doors for generations that follow.

When you step into your arena this week, are you executing merely for the scoreboard, or are you leading for a higher purpose?

Stand tall. Lead with dignity. Finish strong.

👉 Book championship keynote speaking & leadership mastery: lornettedaye.com/speaking
👉 Read *Survival Skills for Believers*: lornettedaye.com/books

#ArthurAshe #USOpen #TennisHistory #GrandSlam #BlackExcellence #LeadershipDignity #MoralFortitude #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #ATP #TennisHeritage #CourageUnderPressure"""
    },
    {
        "id": 3,
        "title": "A Champion Changes More Than a Game: Arthur Ashe 1968 (Drop 3)",
        "slot": "Friday Morning Peak (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:30 AM MDT",
        "assetUrl": ASSET_URL,
        "text": """A CHAMPION CHANGES MORE THAN A GAME: ELEVATING HUMANITY BEYOND THE SCOREBOARD 🏆✨

When Arthur Ashe captured the 1968 US Open title, he showed the entire world what moral fortitude and intellectual discipline look like under maximum pressure.

As the first Black man to win a Grand Slam in the Open Era, he stood in an arena filled with tension and prejudice, answering every challenge with immaculate precision and unyielding grace.

Trophies will inevitably collect dust, but elevating humanity leaves a legacy that time cannot erase.

In elite sports and corporate boardrooms, true leaders measure their greatness not by how many trophies they accumulate, but by how many people they elevate along the way.

Lead with purpose. Command your standard. Finish strong.

👉 Executive leadership coaching & keynote speaking: lornettedaye.com/speaking
👉 Explore high-performance programs: lornettedaye.com/programs

#ArthurAshe #USOpen #TennisHistory #GrandSlam #MoralFortitude #BlackExcellence #CivilRights #LeadershipPoise #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #ArthurAsheStadium #TennisWisdom"""
    },
    {
        "id": 4,
        "title": "A Champion Changes More Than a Game: Arthur Ashe 1968 (Drop 4)",
        "slot": "Tuesday Morning Peak (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 8:30 AM MDT",
        "assetUrl": ASSET_URL,
        "text": """"Start where you are. Use what you have. Do what you can."

In September 1968, Arthur Ashe did not wait for the world to become fair before choosing to be great. By claiming the inaugural US Open title as the first Black man in the Open Era, he anchored a standard of moral fortitude, calm authority, and leadership dignity that continues to inspire millions.

A champion changes more than a game—they elevate humanity beyond the scoreboard.

In my 40+ years coaching Olympic champions, the lesson is universal: When the arena gets chaotic, champions anchor themselves in their core values and let their execution speak.

Don't let external circumstances dictate your character. Elevate your standard and lead from the front.

👉 Book Lornette Daye for your corporate keynote or summit: lornettedaye.com/speaking
👉 High-performance leadership coaching: lornettedaye.com/athlete-coaching

#ArthurAshe #USOpen #GrandSlam #TennisHistory #BlackExcellence #LeadershipDignity #MoralFortitude #LornetteDaye #HighPerformance #ChampionMindset #FinishStrong #ATP #CharacterMatters #PeakPerformance"""
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

def main():
    print("======================================================")
    print("🎾 Arthur Ashe 1968: Bi-Weekly 2-Week Campaign (4 Drops)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Slot: Morning Peak (8:30 AM MDT / 14:30 UTC)")
    print("Asset: " + ASSET_URL)
    print("======================================================\n")

    results = []

    for idx, p in enumerate(drops):
        if p.get("status") == "scheduled" and p.get("bufferPostId"):
            print(f"[{idx + 1}/{len(drops)}] Post #{p['id']} already scheduled in Buffer (ID: {p['bufferPostId']})")
            print(f"   Slot: {p['displayTime']} ({p['dueAt']})\n")
            results.append(p)
            continue

        print(f"[{idx + 1}/{len(drops)}] Scheduling Post #{p['id']} ({p['slot']}): \"{p['title']}\"")
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
                msg = create_post.get("message", "Rate or daily limit reached")
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

    report_path = os.path.join(os.path.dirname(__file__), "ashe-biweekly-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Arthur Ashe Bi-Weekly Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(drops)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
