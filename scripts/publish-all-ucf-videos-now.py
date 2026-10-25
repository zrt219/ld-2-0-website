# -*- coding: utf-8 -*-
"""
Immediate LinkedIn Publisher for All 4 UCF Highlight Videos
Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
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
BASE_URL = "https://lornettedaye.com/campaigns/ucf-byu"

videos_to_publish = [
    {
        "id": 1,
        "title": "ONE PLAY. ONE TOUCHDOWN: KEYONE JENKINS TO GRAYSON BROUSSEAU IN 2OT",
        "asset": "ucf_byu_touchdown_2ot.mp4",
        "caption": """ONE PLAY. ONE TOUCHDOWN. DOUBLE OVERTIME EXECUTION.

Watch the composure in this sequence.

Second overtime in Orlando. The physical fatigue is total. Legs are heavy, breath is shallow, and the entire stadium is on edge.

Quarterback Keyone Jenkins takes the snap, stands tall in the pocket, and delivers a surgical 2-yard strike to tight end Grayson Brousseau in the back of the end zone.

In high-performance athletics, the red zone in overtime is where technique either breaks down or solidifies legacy. Most athletes rush their reads when the clock is tight and the stakes are immense. Great athletes slow their heart rate, trust their muscle memory, and deliver with calm precision.

Repetition in empty practice facilities creates calm in sold-out stadiums.

Fan Question: What was your immediate reaction when Jenkins found Brousseau for this score?

Discover how we train competitors in emotional regulation and fourth-quarter execution:
https://lornettedaye.com/foundations

#UCF #ChargeOn #KeyoneJenkins #DoubleOvertime #Touchdown #ClutchPerformance #CollegeFootball #LornettesFoundations #BetterPeopleBetterPlayers #ExecutionUnderPressure"""
    },
    {
        "id": 2,
        "title": "THE MAGICAL 2-POINT CONVERSION: CALCULATED AGGRESSION UNDER PRESSURE",
        "asset": "ucf_byu_magical_2pt_conversion.mp4",
        "caption": """THE MAGICAL 2-POINT CONVERSION: CALCULATED AGGRESSION UNDER PRESSURE.

Leading 37-31 in double overtime, UCF faced a critical tactical decision. Kick the extra point for a seven-point lead, or go for two to make it a full eight-point cushion.

They did not play not to lose. They attacked to win.

Watch Keyone Jenkins escape heavy pressure, keep his eyes downfield, and thread a magnificent conversion pass to seize complete control of the contest at 39-31.

In my four decades coaching Olympic athletes, the biggest difference between competitors who almost win and champions who finish the job is courage in pivotal moments. When you have momentum, you do not pull back. You press the advantage.

Fortune favors the team that stays on the offensive when fear would suggest caution.

Fan Question: How brilliant was the play-call and execution on this crucial 2-point conversion?

Learn how we train teams and executive leaders to make courageous, high-stakes decisions:
https://lornettedaye.com/foundations

#UCFKnights #ChargeOn #TwoPointConversion #CalculatedRisk #BoldLeadership #Big12Football #LornettesFoundations #BetterPeopleBetterPlayers #ChampionMindset"""
    },
    {
        "id": 3,
        "title": "THE 4TH-AND-GOAL STAND: DEFENSE SEALS THE FIELD STORMING",
        "asset": "ucf_byu_goal_line_stand_win.mp4",
        "caption": """THE 4TH-AND-GOAL STAND: WHEN DEFENSE SEALS IMMORTALITY.

Turn your volume all the way up and witness Orlando erupt.

BYU drove all the way down to the UCF 4-yard line in second overtime. Fourth down. The entire game, the undefeated season for BYU, and the biggest upset in UCF history came down to four yards.

The UCF secondary played disciplined, lock-down coverage. Bear Bachmeier's fourth-down pass fell incomplete on the turf, and instantly, thousands of roaring students and fans stormed the field.

Defense wins championships because defense is built entirely on desire, communication, and refusing to yield an inch of ground. When your offense gives you an eight-point lead, the defense has to anchor the result.

That defensive stand will be talked about in Orlando for the next thirty years.

Fan Question: Rate the intensity of this goal-line stand from 1 to 10!

Learn how to build resilient team defense and unbreakable culture under pressure:
https://lornettedaye.com/foundations

#UCF #FieldStorming #GoalLineStand #DefenseWins #CollegeFootballUpset #ChargeOn #LornettesFoundations #BetterPeopleBetterPlayers #ResilienceAfterSetback"""
    },
    {
        "id": 4,
        "title": "POISE AMID CHAOS: CAPITALIZING ON OPPONENT MISTAKES",
        "asset": "ucf_byu_capitalize_penalty.mp4",
        "caption": """POISE AMID CHAOS: HOW TO CAPITALIZE ON OPPONENT MISTAKES.

Watch how UCF responded when the game seemed on the verge of slipping away.

Late in the fourth quarter, an initial sack and fumble call threatened to end the contest. But UCF did not panic. The coaching staff and players remained composed while officials reviewed the play, successfully overturning it to an incomplete pass. Then, when BYU was flagged for an unsportsmanlike conduct penalty, UCF immediately seized the momentum.

In elite sport, chaos is guaranteed. Referees make controversial calls. Reviews take minutes. Opponents lose their discipline.

The team that regulates its emotions and immediately shifts into attack mode will always punish the opponent's lapse in composure.

Emotional poise is a competitive superpower. When everyone around you is losing their heads, your calm becomes your weapon.

Fan Question: How important is emotional discipline when officiating drama strikes in a close game?

Discover our Olympic frameworks for emotional regulation and poise:
https://lornettedaye.com/foundations

#UCFKnights #ChargeOn #EmotionalRegulation #DisciplineSystems #GameManagement #CollegeFootball #LornettesFoundations #BetterPeopleBetterPlayers #FocusUnderPressure"""
    }
]

# Assertions
for v in videos_to_publish:
    assert "*" not in v["caption"], f"Asterisk in caption {v['id']}"
    assert "—" not in v["caption"], f"Em-dash in caption {v['id']}"
    assert "*" not in v["title"], f"Asterisk in title {v['id']}"
    assert "—" not in v["title"], f"Em-dash in title {v['id']}"

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

def publish_video_now(item):
    url = f"{BASE_URL}/{item['asset']}"
    print(f"\nPublishing Now Video #{item['id']}: {item['title']}")
    print(f"  Video URL: {url}")

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": item["caption"],
            "mode": "shareNow",
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": [{"video": {"url": url}}]
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
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            create_post = data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            post_obj = create_post.get("post")
            if typename == "PostActionSuccess" and post_obj:
                print(f"  >>> SUCCESS: Video #{item['id']} Post ID {post_obj.get('id')} published! Status: {post_obj.get('status')}")
                return {"status": "success", "postId": post_obj.get("id"), "details": post_obj}
            else:
                print(f"  >>> FAILED: {create_post}")
                return {"status": "failed", "error": create_post}
    except Exception as e:
        print(f"  >>> EXCEPTION: {e}")
        return {"status": "error", "error": str(e)}

def main():
    print("=" * 80)
    print("IMMEDIATE LINKEDIN PUBLISHER: ALL 4 UCF HIGHLIGHT VIDEOS")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Pre-flight probe
    for v in videos_to_publish:
        assert probe_url(f"{BASE_URL}/{v['asset']}"), f"Failed to probe {v['asset']}"

    results = []
    for idx, v in enumerate(videos_to_publish, 1):
        res = publish_video_now(v)
        results.append({
            "id": v["id"],
            "title": v["title"],
            "asset": v["asset"],
            "result": res
        })
        if idx < len(videos_to_publish):
            print("Waiting 4 seconds before publishing next video...")
            time.sleep(4.0)

    report_path = os.path.join(os.path.dirname(__file__), "published-all-ucf-videos-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print(f"Execution complete. Report saved to {report_path}")
    success_count = sum(1 for r in results if r["result"].get("status") == "success")
    print(f"Summary: {success_count}/{len(videos_to_publish)} UCF videos published immediately!")
    print("=" * 80)

if __name__ == "__main__":
    main()
