# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 7: SITAYA FAGAN - YOUTH ATHLETICS & EMERGING STARS (10 Posts)
Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
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

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'

posts_data = [
    {
        "id": 1,
        "slot": "Thursday (01:15 PM MDT)",
        "dueAt": "2026-10-22T19:15:00.000Z",
        "assetFile": "sitaya-fagan-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-01.png",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": "USC SITAYA HAS ARRIVED: FROM MELBOURNE TO LOS ANGELES. ✌️🏀🇦🇺\n\nUSC's 6 foot 4 freshman forward brings international pedigree and major upside.\n\nCrossing the Pacific Ocean from Australia to join the elite women's basketball program at USC is a massive athletic transition. Sitaya Fagan brings size, mobility, court vision, and Australian national team grit to the Galen Center. She arrives ready to contribute to a championship culture.\n\nIn four decades coaching Olympic athletes, international transitions test two things: your cultural adaptability and the depth of your personal foundation.\n\nYoung athletes: Are you prepared to carry your talent across borders and make your presence felt?\n\n👉 Build grounded identity, resilience, and confidence through major life transitions. Read Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n#SitayaFagan #USCWBB #FightOn #MelbourneToLA #AussieHoops #SurvivalSkillsForWomen #OlympicCoach #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Thursday (03:45 PM MDT)",
        "dueAt": "2026-10-22T21:45:00.000Z",
        "assetFile": "sitaya-fagan-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE 6'4\" FORWARD: COMBINING LENGTH, SPEED, AND RIM PROTECTION. 🛡️🏀\n\nModern basketball demands versatile size that can switch on the perimeter and protect the rim.\n\nSitaya Fagan's ability to run the floor in transition, contest shots without fouling, and rebound out of her area provides USC with an extraordinary tactical advantage. Length is a physical gift; rim-protection timing is a product of disciplined film study and footwork.\n\nAthletes: Are you relying purely on natural physical attributes, or sharpening your tactical positioning?\n\n👉 Build champion focus, discipline systems, and high performance habits. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#RimProtection #SitayaFagan #USCFreshman #SurvivalSkillsForAthletes #DefensiveMastery #OlympicStandard #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Thursday (05:45 PM MDT)",
        "dueAt": "2026-10-22T23:45:00.000Z",
        "assetFile": "sitaya-fagan-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-03.png",
        "cta": "Survival Skills for Students ($14.99 CAD)",
        "text": "STUDENT-ATHLETE MATURITY: NAVIGATING LIFE TWELVE THOUSAND MILES FROM HOME. ✈️📚\n\nMoving twelve thousand miles away from family at age eighteen to pursue collegiate athletics demands profound maturity.\n\nAdjusting to American college life, rigorous Big Ten athletic travel, and high academic expectations requires emotional self-reliance. Sitaya Fagan is proving that with proper structure and supportive community, distance becomes the crucible where independent leaders are forged.\n\nStudents and parents: Are you building systems to help young people thrive when away from home?\n\n👉 Practical strategies for student focus, healthy habits, and academic-athletic balance. Read Survival Skills for Students ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForStudents #InternationalStudentAthlete #SitayaFagan #BigTenHoops #EmotionalIndependence #LornetteDaye"
    },
    {
        "id": 4,
        "slot": "Friday (08:30 AM MDT)",
        "dueAt": "2026-10-23T14:30:00.000Z",
        "assetFile": "sitaya-fagan-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-04.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "LOS ANGELES BUILDS DIFFERENT: THE ELITE PRESSURE OF TROJAN TRADITION. ✌️🌟\n\nWearing number 1 for USC Women's Basketball is an honor that demands a daily standard.\n\nFrom Cheryl Miller and Lisa Leslie to modern Trojan stars, the legacy of greatness in Los Angeles is everywhere. Sitaya Fagan does not run from that standard; she embraces it. Great athletes understand that pressure from legendary predecessors is an invitation to rise.\n\nLeaders: Do you see historical standards as an intimidating burden or an inspiring benchmark?\n\n👉 Discover how Olympic-level competitors embrace legacy and finish strong. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#USCLegacy #TrojanHeritage #SitayaFagan #FinishStrong #HighStandards #OlympicMindset #CoachLornette"
    },
    {
        "id": 5,
        "slot": "Friday (11:00 AM MDT)",
        "dueAt": "2026-10-23T17:00:00.000Z",
        "assetFile": "sitaya-fagan-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-05.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "MORE THAN A GAME: A BRIGHTER TOMORROW BUILDS TODAY. 🌅🤝\n\nBasketball is what you play; it is never who you are.\n\nSitaya Fagan's journey from junior leagues in Victoria, Australia to collegiate basketball in the United States is driven by family support, faith, and a deep appreciation for the opportunities sport provides. When young athletes keep their identity anchored in character, on-court setbacks cannot shake their inner peace.\n\nReaders: How does keeping perspective on what matters most protect your joy during stressful seasons?\n\n👉 Find encouragement, strength in transition, and renewed hope for your path. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#IdentityBeyondSport #SurvivingLife #SitayaFagan #AussieAthletes #PerspectiveInPressure #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Friday (01:15 PM MDT)",
        "dueAt": "2026-10-23T19:15:00.000Z",
        "assetFile": "sitaya-fagan-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-06.png",
        "cta": "Survival Skills for Women ($14.99 CAD)",
        "text": "WOMEN BUILD BRIGHTER: THE RISE OF AUSTRALIAN BASKETBALL TALENT. 🇦🇺🏀\n\nAustralia has long produced world-class basketball talent, and the next wave of female stars is exceptional.\n\nFrom the WNBL to the Opals and now NCAA Division I, young Australian women are demonstrating physical poise, unselfish team play, and tough defensive identity on global courts. Sitaya Fagan represents that fierce Aussie pedigree.\n\nWomen: Celebrate the unique strengths your heritage brings to your professional arena.\n\n👉 Rebuild confidence, thrive with purpose, and discover practical tools for personal growth. Explore Survival Skills for Women ($14.99 CAD): lornettedaye.com/books\n\n#WomenBuildBrighter #AustralianBasketball #SitayaFagan #OpalsFuture #SurvivalSkillsForWomen #CoachLornette"
    },
    {
        "id": 7,
        "slot": "Friday (03:45 PM MDT)",
        "dueAt": "2026-10-23T21:45:00.000Z",
        "assetFile": "sitaya-fagan-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-07.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE POWER OF FOOTWORK: MASTERING LOW-POST POSITIONING. 👣🏀\n\nSize creates potential, but footwork creates points.\n\nSitaya Fagan's ability to seal defenders, drop step, and establish deep post position before the entry pass arrives is the mark of high-level coaching. When a post player wins the positioning battle early, the finish becomes simple.\n\nIn athletics and business, win the position before the play develops, and the outcome will take care of itself.\n\nAthletes: Are you winning the preliminary positioning battle before trying to make the play?\n\n👉 Strengthen your fundamental athletic habits and mental poise. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#PostFootwork #SitayaFagan #FundamentalSkills #SurvivalSkillsForAthletes #OlympicCoaching #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Friday (05:45 PM MDT)",
        "dueAt": "2026-10-23T23:45:00.000Z",
        "assetFile": "sitaya-fagan-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-08.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "FIGHT ON: RESILIENCE IN THE CRUCIBLE OF BIG TEN PLAY. ✌️⚔️\n\nThe Big Ten conference is physical, grinding, and relentlessly competitive on the glass.\n\nFreshman forwards must adjust to relentless physical contact on every rebound and box out. Sitaya Fagan's willingness to fight for inside position and battle through contact reveals an athlete who does not back down from physical challenge. Trojan resilience is forged in the paint.\n\nLeaders: Does your team back away from intense competition, or lean into the contact?\n\n👉 Master the mindset of championship competitors who embrace the struggle and finish strong. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#FightOn #BigTenBasketball #SitayaFagan #ResilienceInSport #FinishStrong #OlympicMindset #LornetteDaye"
    },
    {
        "id": 9,
        "slot": "Saturday (08:30 AM MDT)",
        "dueAt": "2026-10-24T14:30:00.000Z",
        "assetFile": "sitaya-fagan-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "GLOBAL TALENT PIPELINES: LESSONS FROM INTERNATIONAL RECRUITING. 🌏🏢\n\nModern elite sports organizations scout worldwide to find unique talent that complements their domestic roster.\n\nUSC bringing Sitaya Fagan from Melbourne illustrates the global nature of modern talent identification. Organizations that expand their scouting horizons beyond geographic borders assemble richer, more versatile teams.\n\nExecutives: Are your recruiting strategies discovering global perspective, or confined to traditional local pools?\n\n👉 Transform your organizational talent acquisition and leadership culture with Olympic principles. Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n#GlobalTalent #InternationalScouting #ExecutiveLeadership #CrossBorderExcellence #CoachLornette"
    },
    {
        "id": 10,
        "slot": "Saturday (11:00 AM MDT)",
        "dueAt": "2026-10-24T17:00:00.000Z",
        "assetFile": "sitaya-fagan-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/sitaya-fagan/sitaya-fagan-10.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE ARRIVAL IS JUST THE START: BUILDING A FOUR-YEAR TROJAN LEGACY. 👑✌️\n\nArriving at USC is an incredible milestone, but the destination is four years of championship building.\n\nSitaya Fagan has the size, the skill, and the international foundation to become a cornerstone of USC basketball. Those who build enduring legacies are the ones who treat freshman arrival not as a celebration, but as the opening rep of an exhaustive four-year masterclass.\n\nStay humble. Stay hungry. Honor the work. Finish strong.\n\n👉 Master the habits of elite athletes who transform raw potential into lasting legacy. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#SitayaFagan #TrojanFamily #USCForward #FinishStrong #OlympicStandards #LornetteDaye #MasteryInAction"
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

def main():
    print("=" * 75)
    print("CAMPAIGN 7: SITAYA FAGAN - YOUTH ATHLETICS & EMERGING STARS (10 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "sitaya-fagan-scheduled-report.json")
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
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/{len(posts_data)}] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/{len(posts_data)}] Scheduling: Post #{p_id} ({post['slot']}) - {post['dueAt']}...")
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
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "slot": post["slot"],
                    "assetUrl": post["assetUrl"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

            time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/10 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
