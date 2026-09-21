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
BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/osaka-fourth-round'

osaka_posts = [
    {
        "id": 1,
        "title": "A Beautiful Return / Most Elegant LD Tone",
        "slot": "Tuesday Morning Gold Artwork (10:00 AM MDT)",
        "dueAt": "2026-09-08T16:00:00.000Z", # Tue Sep 8, 10:00 AM MDT
        "displayTime": "Tuesday, Sep 8, 2026 - 10:00 AM MDT",
        "assetFile": "osaka-01.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-01.jpg",
        "text": "A beautiful return. A powerful new chapter. 🤍\n\nOutstanding performance from Naomi Osaka throughout this comeback after becoming a mom. The courage to return, the discipline to rebuild and the belief to compete again at this level deserve recognition.\n\nThis is only the beginning of even greater performances ahead.\n\nStrength. Grace. Belief. And much more still to come.\n\n— Lornette Daye\n\n👉 Discover executive leadership & high performance: lornettedaye.com/speaking\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 2,
        "title": "Strength & Inspiration / Closest to LD Original",
        "slot": "Tuesday Evening Action Post (6:30 PM MDT)",
        "dueAt": "2026-09-09T00:30:00.000Z", # Tue Sep 8, 6:30 PM MDT
        "displayTime": "Tuesday, Sep 8, 2026 - 6:30 PM MDT",
        "assetFile": "osaka-02.png",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-02.png",
        "text": "Outstanding performance from Naomi Osaka. 🤍🎾\n\nWatching her comeback after becoming a mom has been truly inspiring. To return to this level, compete on the biggest stages and continue pushing forward takes tremendous strength.\n\nThis is only the beginning of even greater performances ahead.\n\nKeep going, Naomi. There is so much more to come. ✨\n\n— Lornette Daye\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 3,
        "title": "Three Grand Slam Round of 16 Runs in 2026",
        "slot": "Wednesday Morning Gold Artwork (10:00 AM MDT)",
        "dueAt": "2026-09-09T16:00:00.000Z", # Wed Sep 9, 10:00 AM MDT
        "displayTime": "Wednesday, Sep 9, 2026 - 10:00 AM MDT",
        "assetFile": "osaka-03.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-03.jpg",
        "text": "THREE GRAND SLAM ROUND OF 16 RUNS IN HER FIRST FULL COMEBACK SEASON. 🎾✨\n\nWhile her 2026 US Open ended in the fourth round against Elena Rybakina, this season marked the first time in Naomi Osaka’s entire storied career that she reached at least the fourth round at three of the four Grand Slams.\n\nConsistency on the biggest stages is the true foundation of Grand Slam championships.\n\nThis is only the beginning of even greater performances ahead. Keep building.\n\n— Lornette Daye\n\n👉 Learn championship performance coaching: lornettedaye.com/programs\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 4,
        "title": "More Personal & Heartfelt Message",
        "slot": "Wednesday Evening Action Post (6:30 PM MDT)",
        "dueAt": "2026-09-10T00:30:00.000Z", # Wed Sep 9, 6:30 PM MDT
        "displayTime": "Wednesday, Sep 9, 2026 - 6:30 PM MDT",
        "assetFile": "osaka-04.png",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-04.png",
        "text": "Naomi, what an outstanding performance and what a beautiful comeback. 🤍\n\nComing back after becoming a mom and competing at this level again is something special to watch. The strength, determination and belief behind the journey mean just as much as the results.\n\nI truly believe this is only the beginning of greater performances ahead.\n\nKeep believing. Keep building. Keep going. 🎾✨\n\n— Lornette Daye\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 5,
        "title": "Motherhood + High Performance",
        "slot": "Thursday Morning Gold Artwork (10:00 AM MDT)",
        "dueAt": "2026-09-10T16:00:00.000Z", # Thu Sep 10, 10:00 AM MDT
        "displayTime": "Thursday, Sep 10, 2026 - 10:00 AM MDT",
        "assetFile": "osaka-05.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-05.jpg",
        "text": "Mother. Champion. Still writing her story. 🎾✨\n\nOutstanding performance from Naomi Osaka. Watching her return after becoming a mom and continue competing on the biggest stages has been inspiring.\n\nMotherhood did not end the story—it became part of a new chapter.\n\nThis is only the beginning of greater performances ahead.\n\n— Lornette Daye\n\n👉 Keynote speaking on purpose & resilience: lornettedaye.com/speaking\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 6,
        "title": "Stronger Athlete-Development Angle",
        "slot": "Thursday Evening Action Post (6:30 PM MDT)",
        "dueAt": "2026-09-11T00:30:00.000Z", # Thu Sep 10, 6:30 PM MDT
        "displayTime": "Thursday, Sep 10, 2026 - 6:30 PM MDT",
        "assetFile": "osaka-06.png",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-06.png",
        "text": "Outstanding performance from Naomi Osaka. 🎾\n\nHer comeback after becoming a mom is another reminder that an athlete’s journey does not have to follow one straight path. New chapters can bring new strength, new perspective and new possibilities.\n\nThis is only the beginning of greater performances ahead.\n\nI’m excited to see where this next chapter takes her.\n\n— Lornette Daye\n\n👉 Explore athlete development and mentorship: lornettedaye.com/programs\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 7,
        "title": "Walk In Greatness & Unshakable Standard",
        "slot": "Friday Morning Gold Artwork (10:00 AM MDT)",
        "dueAt": "2026-09-11T16:00:00.000Z", # Fri Sep 11, 10:00 AM MDT
        "displayTime": "Friday, Sep 11, 2026 - 10:00 AM MDT",
        "assetFile": "osaka-07.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-07.jpg",
        "text": "WALK IN GREATNESS. A BIGGER, BRIGHTER, BRAVER CHAPTER. ✨\n\nWhen Naomi Osaka walks onto Arthur Ashe Stadium, it is more than a tennis match—it is an undeniable statement of style, strength, and motherhood.\n\nTrue greatness isn't measured by never facing a setback; it is defined by walking back into the arena with your head held high, rooted in purpose and self-belief.\n\nThis is only the beginning of greater performances ahead.\n\n— Lornette Daye\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 8,
        "title": "Shorter + Stronger for LinkedIn Engagement",
        "slot": "Friday Evening Action Post (6:30 PM MDT)",
        "dueAt": "2026-09-12T00:30:00.000Z", # Fri Sep 11, 6:30 PM MDT
        "displayTime": "Friday, Sep 11, 2026 - 6:30 PM MDT",
        "assetFile": "osaka-08.png",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-08.png",
        "text": "Outstanding performance from Naomi Osaka. 🤍\n\nFrom becoming a mom to returning to compete among the very best in the world, her journey continues to show resilience, belief and determination.\n\nThis is only the beginning of even greater performances ahead.\n\nWhat has impressed you most about Naomi’s comeback? 🎾\n\n— Lornette Daye\n\n👉 Connect with Lornette Daye: lornettedaye.com\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 9,
        "title": "More Than A Comeback / Bigger Possibilities",
        "slot": "Saturday Morning Gold Artwork (10:00 AM MDT)",
        "dueAt": "2026-09-12T16:00:00.000Z", # Sat Sep 12, 10:00 AM MDT
        "displayTime": "Saturday, Sep 12, 2026 - 10:00 AM MDT",
        "assetFile": "osaka-09.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-09.jpg",
        "text": "This feels like more than a comeback.\n\nOutstanding performance from Naomi Osaka as she continues this new chapter after becoming a mom. There is strength in returning, but there is even greater strength in continuing to believe that your best can still be ahead of you.\n\nThis is only the beginning of greater performances ahead. 🤍✨\n\n— Lornette Daye\n\n👉 Book championship speaking & leadership keynotes: lornettedaye.com/speaking\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    },
    {
        "id": 10,
        "title": "Motherhood, Daughter Shai & The Grand Slam Road Ahead",
        "slot": "Saturday Evening Action Post (6:30 PM MDT)",
        "dueAt": "2026-09-13T00:30:00.000Z", # Sat Sep 12, 6:30 PM MDT
        "displayTime": "Saturday, Sep 12, 2026 - 6:30 PM MDT",
        "assetFile": "osaka-10.png",
        "assetUrl": f"{BASE_IMAGE_URL}/osaka-10.png",
        "text": "MOTHERHOOD AS THE ULTIMATE ANCHOR: THE ROAD AHEAD FOR NAOMI. 🤍🎾\n\nWith daughter Shai now three, Naomi has shared how motherhood has given her a profound sense of grounding and clarity. Tennis is no longer her sole identity—it is her passion, her craft, and her joy.\n\nWhen an elite champion plays with freedom and unburdened joy, their ceiling is limitless.\n\nWe celebrate your fourth-round run in New York, Naomi. We know the best is yet to come.\n\n— Lornette Daye\n\n👉 Explore programs and high-performance coaching: lornettedaye.com/programs\n\n#NaomiOsaka #USOpen #Tennis #WTA #WomensTennis #WomenInSports #Motherhood #AthleteMom #Comeback #Resilience #HighPerformance #AthleteDevelopment #SportsInspiration #WomenAthletes #LornetteDaye #LD"
    }
]

def buffer_request(query, variables=None):
    url = "https://api.buffer.com"
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        if "errors" in res and res["errors"]:
            raise Exception(f"Buffer GraphQL Error: {json.dumps(res['errors'], indent=2)}")
        return res.get("data")

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        text
        status
        shareMode
        dueAt
      }
    }
    ... on LimitReachedError {
      message
    }
    ... on InvalidInputError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on UnexpectedError {
      message
    }
  }
}
"""

def schedule_osaka_campaign():
    print("======================================================")
    print("🎾 Scheduling Naomi Osaka Fourth Round Campaign (10 Posts)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Tuesday Sep 8 - Saturday Sep 12, 2026 | 2x Daily (10:00 AM & 6:30 PM MDT)")
    print("======================================================\n")

    results = []

    for idx, p in enumerate(osaka_posts):
        print(f"[{idx + 1}/{len(osaka_posts)}] Scheduling Post #{p['id']} ({p['slot']}): \"{p['title']}\"")
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
            "assets": [
                {
                    "image": {
                        "url": p["assetUrl"]
                    }
                }
            ]
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
                results.append(p)
            else:
                print(f"   ⚠️ Failed response: {json.dumps(create_post, indent=2)}\n")
                p["status"] = "failed"
                p["error"] = create_post
                results.append(p)
        except Exception as e:
            print(f"   ❌ Error: {str(e)}\n")
            p["status"] = "error"
            p["error"] = str(e)
            results.append(p)

        time.sleep(0.4)

    report_path = os.path.join(os.getcwd(), "scripts", "osaka-fourth-round-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"🎉 Scheduled Report saved to {report_path}")

    scheduled_count = len([r for r in results if r.get("status") == "scheduled"])
    print(f"Summary: {scheduled_count}/{len(osaka_posts)} posts successfully scheduled directly in Buffer.\n")

if __name__ == "__main__":
    schedule_osaka_campaign()
