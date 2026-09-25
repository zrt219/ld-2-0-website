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

VIDEO_URL = 'https://lornettedaye.com/campaigns/curacao/curacao-fullmatch.mp4'

post_data = {
    "id": 1,
    "type": "video",
    "slot": "Immediate Breaking Drop: Friday 3:50 AM MDT (Sep 25, 2026)",
    "dueAt": "2026-09-25T09:50:00.000Z",
    "assetFile": "curacao-fullmatch.mp4",
    "assetUrl": VIDEO_URL,
    "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
    "text": (
        "THE FULL 1080P MATCH TAPE IS HERE: COSTA RICA 3, CURAÇAO 4 🇨🇼🌊\n\n"
        "Down 0-3 on the road in San José at the interval. "
        "Most teams pack it in. Most teams look for damage limitation. "
        "Team Curaçao decided to make history instead.\n\n"
        "Watch every second of the Blue Wave comeback in full 1080p broadcast quality right now:\n"
        "• Kenji Gorré cuts the lead in half.\n"
        "• Tahith Chong unleashes pure class to level the momentum.\n"
        "• Gorré strikes again for the brace.\n"
        "• Jordi Paulina finishes the masterpiece in the 88th minute.\n\n"
        "To everyone watching across Willemstad, the Netherlands, and the entire diaspora: "
        "Turn your speakers all the way up and celebrate this moment!\n\n"
        "Ban Kòrsou!\n\n"
        "Discover how to build unbreakable resilience when the odds look impossible. "
        "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
        "Bring Olympic-caliber mental toughness to your next conference or keynote: https://lornettedaye.com/speaking\n\n"
        "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #FootballComeback #HistoricComeback #FinishStrong #LornetteDaye"
    )
}

def check_for_em_dashes():
    t = post_data["text"]
    if "—" in t or "&mdash;" in t or "\u2014" in t:
        print("ERROR: Post contains an em dash!")
        sys.exit(1)
    print("EM DASH CHECK: PASS (Zero em dashes found in post text).")

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
    print("SCHEDULING RAW FULL MATCH VIDEO IMMEDIATE POST NOW (1080P)")
    print("=" * 70)

    check_for_em_dashes()

    print(f"\nScheduling Immediate Post ({post_data['slot']}) - Due: {post_data['dueAt']}...")
    print(f"  Asset: {post_data['assetUrl']}")
    res = schedule_post(post_data)

    create_post_data = res.get("data", {}).get("createPost", {})
    typename = create_post_data.get("__typename")
    post_obj = create_post_data.get("post")

    if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
        b_id = post_obj["id"]
        st = post_obj.get("status")
        due = post_obj.get("dueAt")
        print(f"  >>> SUCCESS: Immediate Post ID {b_id} scheduled for {due} (status: {st})")
        report = [{
            "id": 1,
            "type": post_data["type"],
            "slot": post_data["slot"],
            "dueAt": due,
            "postId": b_id,
            "status": st,
            "assetFile": post_data["assetFile"],
            "assetUrl": post_data["assetUrl"],
            "cta": post_data["cta"]
        }]
        out_path = os.path.join(os.path.dirname(__file__), "curacao-fullmatch-now-report.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Report saved to {out_path}")
    else:
        err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
        print(f"  >>> ERROR: {err_msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()
