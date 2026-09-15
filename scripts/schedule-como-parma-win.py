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

CDN_URL = 'https://lornettedaye.com/campaigns/como-win/como-parma-2-1.jpg'

post_data = {
    "title": "MORE THAN A MATCH. A HIGHER STANDARD. COMO 1907 TAKES THE POINTS!",
    "dueAt": "2026-09-16T18:00:00.000Z", # Wednesday, September 16, 2026 at 12:00 PM MDT
    "displayTime": "Wednesday, Sep 16, 2026 - 12:00 PM MDT",
    "assetUrl": CDN_URL,
    "text": """MORE THAN A MATCH. A HIGHER STANDARD. COMO 1907 TAKES THE POINTS! 🔵⚪🔥

Stadio Giuseppe Sinigaglia erupted as Como 1907 secured a hard-fought 2–1 victory over Parma in Serie A!

Look closely at the embrace between Nico Paz and his teammates. In high-stakes competition, talent might ignite a spark, but collective trust and tactical discipline seal the result. Nico Paz commanded the pitch with elite poise, vision, and fearless ball progression, embodying the relentless hunger driving Como’s resurgence.

In over 40 years coaching Olympic champions and advising elite sports organizations, I have observed one undeniable truth:
Anyone can look dominant when the scoreline is easy. True championship caliber is forged in the grueling minutes when the opponent pushes back, momentum wavers, and you have to execute under maximum pressure.

That isn't just football—that is a higher standard of leadership.

Coaches, athletes, and executives: When you hold a slim lead in a high-pressure environment, do you retreat into safe preservation mode, or do you double down on your foundational standard? Let’s hear your perspective in the comments! 👇

👉 Bring 40+ years of Olympic championship culture to your team or organization: https://lornettedaye.com/speaking
👉 Master the mental game on and off the field with "Survival Skills for Athletes" ($14.99 CAD): https://lornettedaye.com/books

#Como1907 #Calcio #SerieA #NicoPaz #ComoParma #StadioSinigaglia #FootballElevated #LDFootball #ChampionMindset #TeamCulture #HighPerformance #LeadershipExcellence #LornetteDaye #FinishStrong #SurvivalSkillsForAthletes"""
}

mutation = """
mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
            post {
                id
                dueAt
                status
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

def buffer_request(query, variables=None):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({"query": query, "variables": variables or {}}).encode('utf-8')
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        body = json.loads(resp.read().decode('utf-8'))
        if "errors" in body:
            print(f"   ❌ GraphQL Errors: {body['errors']}")
        return body.get("data", {})

def probe_asset(url):
    print("🔍 Probing production asset URL...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
    try:
        with urllib.request.urlopen(req, context=ctx) as r:
            if r.status == 200:
                cl = r.headers.get("Content-Length", "unknown")
                print(f"   ✅ [200 OK] {url} ({cl} bytes)")
                return True
            else:
                print(f"   ❌ [{r.status}] {url}")
                return False
    except Exception as e:
        print(f"   ❌ [ERROR] {url}: {e}")
        return False

def main():
    print("======================================================")
    print("🇮🇹 Como 1907 vs. Parma 2-1 Victory: Scheduling Post")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print(f"Target Time: {post_data['displayTime']} ({post_data['dueAt']})")
    print("======================================================\n")

    if not probe_asset(post_data["assetUrl"]):
        print("🛑 Pre-flight verification failed! Asset is not live with HTTP 200 on production custom domain.")
        sys.exit(1)

    input_data = {
        "channelId": CHANNEL_ID,
        "text": post_data["text"],
        "mode": "customScheduled",
        "dueAt": post_data["dueAt"],
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "assets": [{"image": {"url": post_data["assetUrl"]}}]
    }

    try:
        data = buffer_request(mutation, {"input": input_data})
        create_post = data.get("createPost", {})
        typename = create_post.get("__typename")

        if typename == "PostActionSuccess" and "post" in create_post:
            post_obj = create_post["post"]
            print(f"   ✅ Success! Buffer Post ID: {post_obj['id']} | Due: {post_obj['dueAt']}\n")
            post_data["bufferPostId"] = post_obj["id"]
            post_data["status"] = "scheduled"
            post_data["scheduledAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        elif typename == "LimitReachedError":
            msg = create_post.get("message", "Rate limit reached")
            print(f"   ⚠️ Limit reached: {msg}\n")
            post_data["status"] = "limit_reached"
            post_data["error"] = msg
            sys.exit(2)
        else:
            print(f"   ⚠️ Failed response: {json.dumps(create_post, indent=2)}\n")
            post_data["status"] = "failed"
            post_data["error"] = create_post
            sys.exit(3)
    except Exception as e:
        print(f"   ❌ Exception: {e}\n")
        post_data["status"] = "error"
        post_data["error"] = str(e)
        sys.exit(4)

    report_path = os.path.join(os.path.dirname(__file__), "como-parma-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, indent=2, ensure_ascii=False)

    print(f"🎉 Report saved to {report_path}")

if __name__ == "__main__":
    main()
