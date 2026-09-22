# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for CAMPAIGN 8: TYRESE GIBSON - ENTERTAINMENT & CREATIVE RESILIENCE (12 Posts)
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
        "slot": "Saturday (01:15 PM MDT)",
        "dueAt": "2026-10-24T19:15:00.000Z",
        "assetFile": "tyrese-gibson-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-01.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "THE BOY ON THE BUS KEPT GOING: DON'T LET ONE CHAPTER CONVINCE YOU THE BOOK IS FINISHED. 🚌📖\n\nWatts. Coca-Cola commercial. R&B chart-toppers. Hollywood blockbuster franchises. Fatherhood. Loss. Reinvention.\n\nMore than three decades after singing on that city bus in Watts, Tyrese Gibson is still here. Still creating. Still fighting. Still standing. He has walked through seasons of intense public praise and seasons of devastating personal heartbreak. Through every chapter, he refused to close the book.\n\nIn forty years of coaching elite performers, I know that resilience is not the absence of tears. It is the stubborn refusal to surrender your pen when life writes a painful sentence.\n\nReaders: What difficult chapter are you living through right now that needs a courageous next page?\n\n👉 Find renewed strength, emotional perspective, and hope through life's hardest transitions. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#TyreseGibson #TheBoyOnTheBus #DontGiveUp #SurvivingLife #CreativeResilience #HopeAfterLoss #LornetteDaye"
    },
    {
        "id": 2,
        "slot": "Saturday (03:45 PM MDT)",
        "dueAt": "2026-10-24T21:45:00.000Z",
        "assetFile": "tyrese-gibson-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-02.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "VULNERABILITY IS NOT WEAKNESS: THE COURAGE OF EMOTIONAL HONESTY. 🛡️💔\n\nMen are frequently taught that emotional suppression is strength. In truth, buried pain poisons the soul.\n\nTyrese Gibson has stood in front of global audiences and spoken with raw honesty about grief, depression, fatherhood battles, and the ache of losing brothers like John Singleton and Paul Walker. Speaking your pain out loud takes far more courage than pretending you are unbreakable.\n\nWhen men learn to acknowledge their wounds without losing their dignity, true healing and leadership begin.\n\nMen: Are you carrying grief in silence, or seeking the brotherhood that helps you bear the weight?\n\n👉 Build emotional resilience, personal clarity, and steady balance in demanding seasons. Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #Tyrese #EmotionalResilience #MenAndGrief #AuthenticLeadership #CoachLornette"
    },
    {
        "id": 3,
        "slot": "Saturday (05:45 PM MDT)",
        "dueAt": "2026-10-24T23:45:00.000Z",
        "assetFile": "tyrese-gibson-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-03.png",
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": "WATTS ROOTS: SURVIVING TO THRIVING ACROSS THREE DECADES. 🏙️🔥\n\nYou cannot choose where you start, but you can choose what you do with your opportunity.\n\nGrowing up in Watts, Los Angeles during an era of extreme systemic violence, survival was a daily assignment. Tyrese channeled his pain into melodies, his drive into auditions, and his survival instincts into a multi-decade Hollywood career. He moved beyond survival mode and built a life of creative momentum.\n\nProfessionals: Are you still trapped in survival instincts, or intentionally building a foundation to thrive?\n\n👉 Identify what is holding you back and step into purpose-driven growth. Read Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n#WattsToHollywood #SurvivingToThriving #TyreseGibson #OvercomingEnvironment #PurposeDrivenMomentum #LornetteDaye"
    },
    {
        "id": 4,
        "slot": "Sunday (08:30 AM MDT)",
        "dueAt": "2026-10-25T14:30:00.000Z",
        "assetFile": "tyrese-gibson-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-04.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE FAST FRANCHISE ENDURANCE: TWENTY YEARS OF BLOCKBUSTER EXECUTION. 🎬🏎️\n\nA hit film is an achievement; sustaining a role in a multi-billion-dollar franchise over twenty years is endurance.\n\nFrom 2 Fast 2 Furious in 2003 through ten installments, Tyrese has been a central pillar of global cinema. Long production schedules, intense physical demands, and global promotional tours require high physical stamina and unwavering professional reliability on set.\n\nIn Olympic athletics, we celebrate those who do not just run one fast lap, but hold their pace over marathon distances.\n\nLeaders: Is your professional stamina built for a two-decade marathon?\n\n👉 Master the stamina and mindset of world-class finishers. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#FastAndFurious #TyreseGibson #ProfessionalEndurance #FinishStrong #OlympicPacing #LornetteDaye #LongevityInFilm"
    },
    {
        "id": 5,
        "slot": "Sunday (11:00 AM MDT)",
        "dueAt": "2026-10-25T17:00:00.000Z",
        "assetFile": "tyrese-gibson-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-05.png",
        "cta": "Survival Skills for Believers ($14.99 CAD)",
        "text": "FAITH IN THE VALLEY: ANCHORING YOUR SOUL WHEN STORMS RAGE. ⚓🙏\n\nIt is easy to give praise on the mountain peak. The measure of your faith is whether you worship in the valley.\n\nThrough every court battle, every public misunderstanding, and every season of sorrow, Tyrese has consistently testified to the grace and mercy of God. He knows that external fame cannot heal an aching spirit; only an anchor in Christ provides peace that surpasses human understanding.\n\nBelievers: When your life's circumstances seem dark, where is your anchor dropped?\n\n👉 Navigate life's hardest chapters with scripture-backed wisdom, grace, and unshakable faith. Explore Survival Skills for Believers ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForBelievers #TyreseFaith #FaithInTheValley #AnchorOfHope #PeaceInTheStorm #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Sunday (01:15 PM MDT)",
        "dueAt": "2026-10-25T19:15:00.000Z",
        "assetFile": "tyrese-gibson-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-06.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "FATHERHOOD AS SACRED CALLING: LEAVING A LEGACY OF LOVE. 👨‍👧❤️\n\nThe red carpets will eventually roll up. The most important title you will ever hold is Father.\n\nWatch Tyrese talk about his daughters and you see a man whose fierce devotion to fatherhood transcends all Hollywood glamour. He fights for their presence, their security, and their joy. Great leadership begins in the living room, not the boardroom.\n\nMen and parents: Are you investing your deepest presence in the children who look up to you?\n\n👉 Build lasting family foundations, emotional warmth, and perspective that endures. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#FatherhoodFirst #TyreseGibson #FamilyLegacy #SurvivingLife #ProtectingTheNextGeneration #LornetteDaye"
    },
    {
        "id": 7,
        "slot": "Sunday (03:45 PM MDT)",
        "dueAt": "2026-10-25T21:45:00.000Z",
        "assetFile": "tyrese-gibson-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-07.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "THE DISCIPLINE OF REINVENTION: NEVER LETTING CRITICS FREEZE YOUR GROWTH. 🔄🎤\n\nWhen critics attempt to pigeonhole you into a single lane, keep expanding your canvas.\n\nFrom billboard-topping soul music to comedy, action cinema, authoring New York Times bestsellers, and producing films, Tyrese has refused to let outside opinions define his boundaries. Reinvention is not fleeing yourself; it is unlocking the multifaceted gifts God placed inside you.\n\nMen: What dormant gift have you neglected because you feared what critics might say?\n\n👉 Reclaim your focus, balance, and creative courage in every season of life. Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#Reinvention #Tyrese #MultifacetedCreativity #SurvivalSkillsForMen #MenWhoLead #OlympicCourage #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Sunday (05:45 PM MDT)",
        "dueAt": "2026-10-25T23:45:00.000Z",
        "assetFile": "tyrese-gibson-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "AUTHENTIC STORYTELLING: BUILDING EMOTIONAL BRIDGES WITH AUDIENCES. 🎙️🌟\n\nIn an era of generic corporate scripts, authenticity is the rarest and most valuable currency.\n\nWhether Tyrese is singing a ballad or speaking to an auditorium, people connect because they feel his humanity. He does not hide his flaws behind polished public relations veneers. Leaders who dare to be authentic generate immediate trust and fierce loyalty.\n\nExecutives: Does your corporate communication feel manufactured, or does it resonate with genuine human authority?\n\n👉 Train your leadership team to communicate with authentic emotional resonance and executive poise. Book Lornette Daye: lornettedaye.com/speaking\n\n#AuthenticCommunication #ExecutiveResonance #TyreseStyle #HumanLeadership #CoachLornette"
    },
    {
        "id": 9,
        "slot": "Monday (08:30 AM MDT)",
        "dueAt": "2026-10-26T14:30:00.000Z",
        "assetFile": "tyrese-gibson-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-09.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "GRIEF AND RECOVERY: HONORING BROTHERS GONE TOO SOON. 🕊️🖤\n\nLosing beloved friends leaves hollow places that time alone cannot fill.\n\nTyrese has openly mourned Paul Walker, John Singleton, and his dear mother Priscilla Murray. Yet his tribute to them has not been surrender; it has been continuing their legacy of generosity, passion, and unrelenting creative commitment. The greatest honor you can give to the departed is to live fully.\n\nReaders: If you are walking through the shadow of loss, know that your life still holds profound purpose.\n\n👉 Find comfort, rebuilding tools, and practical encouragement for seasons of heavy grief. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#GriefAndHealing #PaulWalkerLegacy #JohnSingleton #SurvivingLife #HonoringThoseWeLost #LornetteDaye"
    },
    {
        "id": 10,
        "slot": "Monday (11:00 AM MDT)",
        "dueAt": "2026-10-26T17:00:00.000Z",
        "assetFile": "tyrese-gibson-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-10.png",
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": "CREATIVE INDEPENDENCE: OWNING YOUR MASTERS AND YOUR FUTURE. 💼🎶\n\nDo not spend your entire life building another person's empire while leaving your own barren.\n\nTyrese's transition into independent music distribution and film production demonstrates an artist who understands intellectual property. When you own your masters, your creative vision remains uncompromised and your economic legacy is secured for your children.\n\nProfessionals: Are you building true ownership and equity in your craft, or simply renting your labor?\n\n👉 Move beyond survival mode and construct lasting economic and creative independence. Explore Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n#OwnershipOverRenting #CreativeIndependence #Tyrese #SurvivingToThriving #BuildingEquity #LornetteDaye"
    },
    {
        "id": 11,
        "slot": "Monday (01:15 PM MDT)",
        "dueAt": "2026-10-26T19:15:00.000Z",
        "assetFile": "tyrese-gibson-11.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-11.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE GRIND NEVER SLEEPS: RETURNING TO THE STUDIO AFTER MIDNIGHT. 🎹🌙\n\nWhen other people are sleeping, true artists are searching for the chord that moves the soul.\n\nWatch Tyrese in the recording studio at 2:00 AM, working vocal harmonies with live musicians, refusing to settle for autotune shortcuts. Soul music requires soul investment. When you put genuine craftsmanship into your product, it never goes out of style.\n\nLeaders: Are you taking shortcuts in your deliverables, or sweating the craftsmanship?\n\n👉 Build the obsessive work ethic of champions who take pride in every detail. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#Craftsmanship #StudioGrind #TyreseMusic #FinishStrong #OlympicStandards #NoShortcuts #CoachLornette"
    },
    {
        "id": 12,
        "slot": "Monday (03:45 PM MDT)",
        "dueAt": "2026-10-26T21:45:00.000Z",
        "assetFile": "tyrese-gibson-12.png",
        "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-12.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "MORE THAN THREE DECADES LATER: THE STORY IS STILL BEING WRITTEN. 🌅👑\n\nNever let the world write your obituary while breath is still in your lungs.\n\nTyrese Gibson's journey is a testament to the stubborn resilience of the human spirit. From an impoverished bus seat in South Central Los Angeles to international movie premieres and Grammy nominations, he proves that when you refuse to quit, God writes chapters you never could have planned.\n\nWhatever chapter you find yourself in today, take heart: pick up your pen, hold your head high, and finish strong.\n\n👉 Discover how to finish your race with purpose, faith, and enduring legacy. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#TheStoryContinues #TyreseGibson #NeverGiveUp #FinishStrong #OlympicSpirit #FaithAndEndurance #LornetteDaye"
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
    print("CAMPAIGN 8: TYRESE GIBSON - ENTERTAINMENT & CREATIVE RESILIENCE (12 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "tyrese-gibson-scheduled-report.json")
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

        rate_limit_halt = False
        while True:
            print(f"\n[{idx}/{len(posts_data)}] Scheduling: Post #{p_id} ({post['slot']}) - {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                if wait_sec > 120:
                    print(f"  [RATE LIMIT] HTTP 429: Window locked for {wait_sec}s. Exiting for background scheduler.")
                    rate_limit_halt = True
                    break
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

        if rate_limit_halt:
            break

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/12 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
