# -*- coding: utf-8 -*-
"""
Immediate LinkedIn Publisher for Edmonton Oilers Shootout Winner & UCF Historic Upset
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Mode: shareNow (Immediate Publication)
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

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

OILERS_VIDEO_URL = "https://lornettedaye.com/campaigns/oilers/rnh-shootout-winner.mp4"
UCF_IMAGE_URL = "https://lornettedaye.com/campaigns/ucf-byu/ucf_byu_upset_plate_01.png"

OILERS_TEXT = """THE SHOOTOUT WINNER: RYAN NUGENT-HOPKINS CALLS GAME IN EDMONTON.

Turn your sound all the way up for this one.

October 22 at Rogers Place. A 6-5 double-overtime thriller against the Carolina Hurricanes came down to one single puck, twenty-five meters of ice, and complete optical calm.

Ryan Nugent-Hopkins stepped onto the ice for his very first game of the season after missing nine straight games with injury. The entire arena was standing on its feet.

Watch the patience on this shootout approach. He glides in, delays his commitment until the goaltender bites, and buries the only successful shootout goal of the entire contest while Devon Levi shuts the door at the other end.

Connor McDavid and Leon Draisaitl each put up five points in regulation, but when the game hung on a single shot, it was Nuge who delivered.

In over four decades coaching Olympic champions, I tell my athletes that calm under pressure is not an accident. It is forged during the silent hours of rehabilitation. When your mental preparation is complete, your pulse stays steady when the game is on your stick.

Fan Question for Oil Country: Where were you when Nuge buried this shootout winner? Drop your memory below.

Discover how elite athletes train mental stillness and clutch execution under pressure:
https://lornettedaye.com/foundations

#EdmontonOilers #Oilers #LetsGoOilers #OilCountry #RyanNugentHopkins #ConnorMcDavid #LeonDraisaitl #DevonLevi #NHL #ClutchPerformance #LornettesFoundations #BetterPeopleBetterPlayers #ChampionMindset"""

UCF_TEXT = """HISTORIC UPSET: UCF SHOCKS NO. 2 BYU 39-31 IN DOUBLE OVERTIME.

In one of the wildest, most electric finishes of the entire college football season, the UCF Knights have defeated the undefeated No. 2-ranked BYU Cougars in Orlando.

Final score: UCF 39, No. 2 BYU 31 in double overtime.

This is not just another win on the schedule. This is the first victory over a top-5 team in UCF football program history.

When you step onto the field against the second-ranked team in the nation, every spectator expects you to blink. But in elite sport, national rankings do not make tackles, and reputations do not convert fourth downs.

Look at how UCF executed when everything was on the line:
- Overcoming a blocked field goal at the end of regulation to reset for overtime.
- Keyone Jenkins throwing a surgical 2-yard touchdown pass to Grayson Brousseau in double overtime.
- Converting a high-difficulty 2-point conversion pass to push the lead to eight.
- Locking down the goal line at the 4-yard line on 4th down to ignite an unforgettable field storming.

As an Olympic-level coach and former national champion, I always remind competitors: An upset is never luck. It is the predictable outcome of an underdog that refuses to be intimidated by a number beside an opponent's name.

Fan Question for College Football Fans: Where does this rank among the most shocking upsets you have seen this season?

Explore how elite athletes and high-performing organizations build championship composure under pressure:
https://lornettedaye.com/foundations

#UCF #UCFKnights #ChargeOn #Big12 #BYU #CollegeFootball #CFBUpset #HistoricWin #BetterPeopleBetterPlayers #LornettesFoundations #ChampionMindset"""

# Assertions
assert "*" not in OILERS_TEXT, "Asterisk found in OILERS_TEXT"
assert "—" not in OILERS_TEXT, "Em-dash found in OILERS_TEXT"
assert "*" not in UCF_TEXT, "Asterisk found in UCF_TEXT"
assert "—" not in UCF_TEXT, "Em-dash found in UCF_TEXT"

MUTATION = '''
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

def probe_url(url):
    print(f"Probing {url}...")
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            print(f"  [200 OK] {resp.headers.get('Content-Type')}")
            return True
    except Exception as e:
        print(f"  [FAIL] {e}")
        return False

def publish_share_now(title, text, asset_url, is_video=False):
    print(f"\nPublishing Now: {title}")
    print(f"  Asset: {asset_url} ({'VIDEO' if is_video else 'IMAGE'})")

    if is_video:
        assets = [{"video": {"url": asset_url}}]
    else:
        assets = [{"image": {"url": asset_url}}]

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": text,
            "mode": "shareNow",
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": assets
        }
    }

    payload = json.dumps({"query": MUTATION, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            create_post = data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            post_obj = create_post.get("post")
            if typename == "PostActionSuccess" and post_obj:
                print(f"  >>> SUCCESS: Post ID {post_obj.get('id')} published! Status: {post_obj.get('status')}")
                return {"status": "success", "postId": post_obj.get("id"), "details": post_obj}
            else:
                print(f"  >>> FAILED: {create_post}")
                return {"status": "failed", "error": create_post}
    except Exception as e:
        print(f"  >>> EXCEPTION: {e}")
        return {"status": "error", "error": str(e)}

def main():
    print("=" * 80)
    print("IMMEDIATE LINKEDIN PUBLISHER: OILERS SHOOTOUT & UCF HISTORIC UPSET")
    print(f"Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # 1. Probe both assets
    assert probe_url(OILERS_VIDEO_URL), "Oilers video failed probe"
    assert probe_url(UCF_IMAGE_URL), "UCF image failed probe"

    results = []

    # 2. Publish Oilers video now
    res_oilers = publish_share_now(
        title="Oilers Shootout Winner",
        text=OILERS_TEXT,
        asset_url=OILERS_VIDEO_URL,
        is_video=True
    )
    results.append({"topic": "Edmonton Oilers", "result": res_oilers})

    # Wait 3 seconds
    time.sleep(3.0)

    # 3. Publish UCF image plate now
    res_ucf = publish_share_now(
        title="UCF Historic Upset over No. 2 BYU",
        text=UCF_TEXT,
        asset_url=UCF_IMAGE_URL,
        is_video=False
    )
    results.append({"topic": "UCF Knights Upset", "result": res_ucf})

    report_path = os.path.join(os.path.dirname(__file__), "published-now-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print(f"Execution complete. Report saved to {report_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()
