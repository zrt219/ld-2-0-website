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
BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/lewis-hamilton'

lewis_posts = [
    # FRIDAY SEP 4, 2026 (Practice Day & Telemetry Setup)
    {
        "id": 1,
        "title": "LIGHTS OUT IN THE MIND BEFORE THE TRACK",
        "session": "Pre-FP1 Morning Momentum",
        "dueAt": "2026-09-04T12:30:00.000Z", # Friday Sep 4, 6:30 AM MDT
        "displayTime": "Friday, Sep 4, 2026 - 6:30 AM MDT",
        "assetFile": "lh-01.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-01.png",
        "isVideo": False,
        "text": "LIGHTS OUT IN THE MIND BEFORE THE WHEELS HIT THE TRACK.\n\nBefore FP1 begins on an F1 race weekend, the preparation has already consumed hundreds of hours in the simulator, biometric conditioning, and tactical visualization.\n\nLewis Hamilton doesn't show up on Friday morning hoping for a good setup. He arrives with complete cognitive alignment and an appetite to hunt down every thousandth of a second.\n\nIn 40+ years of coaching Olympians and elite executives, the lesson is universal: peak performance is never an accident of race day—it is built in the silent, disciplined hours of pre-session preparation.\n\nLock in your mindset before you step into the arena today.\n\n🏁 F1 FANS & TEAM LH: What are your FP1 predictions for Lewis this weekend? Drop your thoughts below! 👇\n\n👉 Book championship keynote leadership: lornettedaye.com/speaking\n\n#LewisHamilton #TeamLH #LH44 #F1 #Formula1 #ItalianGP #Monza #MercedesAMGF1 #ScuderiaFerrari #StillWeRise #LornetteDaye #HighPerformance #ChampionshipMindset #MotorsportLeadership #PreparationIsKey #FinishStrong"
    },
    {
        "id": 2,
        "title": "TELEMETRY MASTERY: THE MILLISECOND DISCIPLINE",
        "session": "Post-FP1 / Pre-FP2 Debrief",
        "dueAt": "2026-09-04T16:00:00.000Z", # Friday Sep 4, 10:00 AM MDT
        "displayTime": "Friday, Sep 4, 2026 - 10:00 AM MDT",
        "assetFile": "lh-02.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-02.png",
        "isVideo": False,
        "text": "TELEMETRY MASTERY: THE MILLISECOND DISCIPLINE.\n\nIn Formula 1, the difference between pole position and P6 is often less than three tenths of a second—a single blink of an eye.\n\nBetween practice sessions, Lewis Hamilton sits with his race engineers dissecting micro-sectors: entry speeds, brake pressures, apex rotation, and differential settings. He welcomes critical telemetry because ego has no place in the pursuit of perfection.\n\nGreat leaders don't shy away from cold, objective data. They use feedback as fuel to refine their mechanics.\n\nDissect your data. Refine your execution. Shave off the waste.\n\n🏎️ F1 TECH TALK: How critical is driver feedback vs raw engineering data in dialing in race pace? Let's debate in the comments! 💬\n\n👉 Elevate your executive team's precision: lornettedaye.com/programs\n\n#LewisHamilton #TeamLH #F1Telemetry #EngineeringExcellence #Formula1 #HighPerformance #LornetteDaye #ContinuousImprovement #DataDrivenLeadership #LH44 #PrecisionExecution #FinishStrong #F1Debrief"
    },
    {
        "id": 3,
        "title": "TURNING SETUP STRUGGLES INTO RACE PACE",
        "session": "Post-Practice Session Analysis",
        "dueAt": "2026-09-04T19:00:00.000Z", # Friday Sep 4, 1:00 PM MDT
        "displayTime": "Friday, Sep 4, 2026 - 1:00 PM MDT",
        "assetFile": "lh-03.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-03.png",
        "isVideo": False,
        "text": "TURNING SETUP STRUGGLES INTO CHAMPIONSHIP PACE.\n\nFriday practice isn't always smooth. Oversteer on corner exit, tire graining on high-fuel runs, and unexpected balance shifts can make the car feel nearly undriveable.\n\nWhat makes a 7-time World Champion legendary is not panicking when the Friday timesheet looks daunting. Lewis stays composed, communicates crystal-clear feedback to the garage, and trusts the overnight engineering turnaround.\n\nWhen your business or project hits friction early on, don't abort the mission. Adjust the balance and stay the course.\n\nResilience is the ultimate setup advantage.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#LewisHamilton #TeamLH #F1 #ResilienceInSport #OvercomingAdversity #LornetteDaye #LeadershipPoise #Formula1 #GrandPrixWeekend #LH44 #PatienceAndFocus #FinishStrong"
    },
    {
        "id": 4,
        "title": "THE ART OF THE OVERTAKE: SURGICAL BRAVERY",
        "session": "Friday Highlight & Fan Debate",
        "dueAt": "2026-09-04T22:30:00.000Z", # Friday Sep 4, 4:30 PM MDT
        "displayTime": "Friday, Sep 4, 2026 - 4:30 PM MDT",
        "assetFile": "lh-04.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-04.png",
        "isVideo": False,
        "text": "THE ART OF THE OVERTAKE: SURGICAL BRAVERY AT 200 MPH.\n\nExecuting a late-braking maneuver into Turn 1 requires more than raw courage—it demands surgical spatial awareness, complete trust in your machinery, and the audacity to claim space.\n\nLewis Hamilton has delivered some of the cleanest, most electrifying overtakes in modern Grand Prix history because he balances fierce aggression with immaculate control.\n\nIn business negotiations and career breakthroughs, knowing exactly when to make your move without overshooting the apex is the hallmark of mastery.\n\nBe bold. Be calculated. Seize your gap.\n\n🔥 F1 HIGHLIGHT MOMENT: What is the greatest Lewis Hamilton overtake in F1 history? Silverstone 2008? Brazil 2021? Monza 2018? Sound off below! 👇\n\n👉 Keynote speaking on decisive leadership: lornettedaye.com/speaking\n\n#LewisHamilton #LH44 #F1Overtake #TeamLH #Formula1 #RacingLegends #DecisiveLeadership #HighPerformance #LornetteDaye #BraveryUnderPressure #GrandPrixHistory #FinishStrong"
    },
    {
        "id": 5,
        "title": "STILL WE RISE: DEFYING THE CRITICS AND BARRIERS",
        "session": "Friday Primetime Championship Wisdom",
        "dueAt": "2026-09-05T01:30:00.000Z", # Friday Sep 4, 7:30 PM MDT
        "displayTime": "Friday, Sep 4, 2026 - 7:30 PM MDT",
        "assetFile": "lh-05.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-05.png",
        "isVideo": False,
        "text": "\"STILL I RISE\" IS NOT A SLOGAN—IT IS AN UNBREAKABLE STANDARD.\n\nFrom karting tracks in Stevenage where people said he didn't belong, to standing alone at the pinnacle of motorsport with 100+ wins and 100+ poles.\n\nLewis Hamilton was told he was \"too unconventional,\" \"too outspoken,\" and that he \"should just focus on driving.\" He responded by breaking every historic barrier and championing diversity, equity, and STEM education for the next generation.\n\nWhen you walk into spaces where no one looks like you, don't shrink to fit the room. Elevate the room to meet your standard.\n\nNever apologize for your excellence.\n\n👉 Discover youth empowerment & leadership impact: lornettedaye.com/impact\n\n#LewisHamilton #StillWeRise #TeamLH #LH44 #DiversityInSport #Mission44 #LornetteDaye #BlackExcellence #Trailblazer #HighPerformance #LeadershipIntegrity #FinishStrong #F1"
    },

    # SATURDAY SEP 5, 2026 (Qualifying Day & The Quest for Pole)
    {
        "id": 6,
        "title": "THE SATURDAY FOCUS: TUNING OUT THE NOISE",
        "session": "Pre-FP3 / Saturday Morning Build-up",
        "dueAt": "2026-09-05T12:30:00.000Z", # Saturday Sep 5, 6:30 AM MDT
        "displayTime": "Saturday, Sep 5, 2026 - 6:30 AM MDT",
        "assetFile": "lh-06.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-06.png",
        "isVideo": False,
        "text": "SATURDAY MORNING IN THE PADDOCK: THE INNER FORTRESS.\n\nSaturday at a Grand Prix is when the tension ramps up to maximum volume. Media speculation, rival lap times, and the relentless ticking clock before Qualifying.\n\nWatch Lewis Hamilton put on his helmet: his shoulders drop, his breathing slows, and he enters a state of deep cognitive flow. The noise of the world outside disappears.\n\nIn high-stakes corporate summits and athletic championships alike, your ability to silence external distractions determines whether you crumble or conquer.\n\nBuild your inner fortress before the battle begins.\n\n👉 Master mental toughness & focus: lornettedaye.com/programs\n\n#LewisHamilton #QualifyingDay #F1Saturday #TeamLH #MentalToughness #HighPerformanceMindset #LornetteDaye #FocusUnderFire #Formula1 #LH44 #InnerCalm #FinishStrong"
    },
    {
        "id": 7,
        "title": "Q3 EXECUTION: PEAK PRESSURE ON FRESH SOFTS",
        "session": "Pre-Qualifying Showdown",
        "dueAt": "2026-09-05T16:00:00.000Z", # Saturday Sep 5, 10:00 AM MDT
        "displayTime": "Saturday, Sep 5, 2026 - 10:00 AM MDT",
        "assetFile": "lh-07.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-07.png",
        "isVideo": False,
        "text": "Q3 SHOOTOUT: ONE OUT LAP. ONE FLYER. ZERO ROOM FOR ERROR.\n\nQualifying in Formula 1 is the purest expression of raw speed on earth. You have one set of fresh soft tires, optimal track temperature, and 90 seconds to extract every single ounce of mechanical grip.\n\nLewis Hamilton holds the all-time record with 104+ Pole Positions not because he is reckless, but because he can touch the absolute knife-edge of grip without falling off.\n\nPressure isn't a weight when you trust your mechanics and commit completely to the line.\n\nCommit with zero hesitation.\n\n⏱️ POLE PREDICTION: Will Lewis secure a front-row start today? Drop your pole time predictions in the comments! 🏁\n\n👉 Book Olympian Coach Lornette Daye for your keynote: lornettedaye.com/speaking\n\n#LewisHamilton #PolePosition #Q3Shootout #F1Qualifying #TeamLH #SpeedAndPrecision #HighPerformance #LornetteDaye #MasteryInMotion #LH44 #Formula1 #FinishStrong"
    },
    {
        "id": 8,
        "title": "STARTING POSITION VS RACE CRAFT: CHAMPIONSHIP POSTURE",
        "session": "Post-Qualifying Strategic Analysis",
        "dueAt": "2026-09-05T19:00:00.000Z", # Saturday Sep 5, 1:00 PM MDT
        "displayTime": "Saturday, Sep 5, 2026 - 1:00 PM MDT",
        "assetFile": "lh-08.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-08.png",
        "isVideo": False,
        "text": "QUALIFYING DETERMINES THE GRID. RACE CRAFT WINS THE TROPHY.\n\nWhether Lewis Hamilton lines up on the front row or starts from deep in the pack, his posture never falters. Points and podiums are awarded on Sunday, not Saturday.\n\nIn 40+ years of coaching championship athletes, I have seen too many leaders give up after a disappointing Saturday qualification. But true champions view an unfavorable starting grid as simply a more dramatic canvas for victory.\n\nIt is not where you start—it is how fiercely you execute on race day.\n\nRecalibrate your strategy and get ready to fight tomorrow.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#LewisHamilton #F1Debrief #RaceCraft #TeamLH #ChampionshipPosture #LornetteDaye #NeverGiveUp #SundayPoints #Formula1 #LH44 #Resilience #FinishStrong"
    },
    {
        "id": 9,
        "title": "THE QUALIFYING MASTERCLASS & RAW AGILITY",
        "session": "Saturday Evening Fan Debate",
        "dueAt": "2026-09-05T22:30:00.000Z", # Saturday Sep 5, 4:30 PM MDT
        "displayTime": "Saturday, Sep 5, 2026 - 4:30 PM MDT",
        "assetFile": "lh-09.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-09.png",
        "isVideo": False,
        "text": "THE RAIN MASTER: SINGAPORE 2018, STYRIA 2020, SILVERSTONE 2008.\n\nWhen the heavens open and the track turns into a mirror of standing water, raw horsepower means nothing. Only feel, throttle delicacy, and superhuman courage prevail.\n\nLewis Hamilton's wet-weather masterclasses are legendary because he finds grip where other drivers only see walls. He dances on the razor's edge with effortless grace.\n\nWhen the operating environment in your industry turns chaotic and unpredictable, those who master adaptability don't just survive—they dominate.\n\nThrive in the rain.\n\n🌧️ TEAM LH DEBATE: What is Lewis's greatest wet-weather drive of all time? Silverstone 2008 (winning by over a minute) or Turkey 2020 (clinching Title #7)? Share below! 💬\n\n👉 Executive agility and leadership coaching: lornettedaye.com/programs\n\n#LewisHamilton #RainMaster #WetWeatherDriving #Formula1 #TeamLH #HighPerformanceCoaching #LornetteDaye #Adaptability #MotorsportGreatness #LH44 #FinishStrong"
    },
    {
        "id": 10,
        "title": "TEAM DYNAMICS & UNWAVERING LOYALTY IN THE GARAGE",
        "session": "Saturday Primetime Leadership Reflection",
        "dueAt": "2026-09-06T01:30:00.000Z", # Saturday Sep 5, 7:30 PM MDT
        "displayTime": "Saturday, Sep 5, 2026 - 7:30 PM MDT",
        "assetFile": "lh-10.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-10.png",
        "isVideo": False,
        "text": "\"WE WIN AND WE LOSE TOGETHER.\"\n\nAcross 18+ seasons at the pinnacle of motorsport, Lewis Hamilton has never publicly scapegoated his mechanics or engineers. When pit stops go wrong or engines blow, he stands side-by-side with his crew.\n\n\"We win as a team, and we lose as a team.\"\n\nIn elite corporate culture, nothing destroys momentum faster than leaders who claim the glory in good times and blame their subordinates when storms hit.\n\nTrue leadership is taking the blame in public and sharing the credit in private.\n\nStand by your team with unwavering loyalty.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#LewisHamilton #TeamCulture #LeadershipExcellence #WeWinAndWeLoseTogether #LornetteDaye #ExecutiveLeadership #TeamLH #MercedesAMGF1 #ScuderiaFerrari #LH44 #IntegrityInLeadership"
    },

    # SUNDAY SEP 6, 2026 (Grand Prix Race Day & The 53 Laps of Grit)
    {
        "id": 11,
        "title": "RACE DAY PSYCHOLOGY: THE INNER CALM ON THE GRID",
        "session": "Sunday Morning Pre-Race Briefing",
        "dueAt": "2026-09-06T12:30:00.000Z", # Sunday Sep 6, 6:30 AM MDT
        "displayTime": "Sunday, Sep 6, 2026 - 6:30 AM MDT",
        "assetFile": "lh-11.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-11.jpg",
        "isVideo": False,
        "text": "RACE DAY: THE CALM BEFORE THE 53-LAP STORM.\n\nStanding on the starting grid surrounded by hundreds of cameras, roaring mechanics, and the national anthem, the sensory overload is immense.\n\nLewis Hamilton closes his eyes, checks his heart rate variability, and connects with his purpose. When the 5 red lights illuminate, his mind is as calm as still water.\n\nChampionship execution requires regulating your central nervous system when everything around you screams for panic.\n\nMaster your inner pulse, and the outcome will take care of itself.\n\n🏁 RACE DAY PREDICTIONS: Where will Lewis finish today? Podium? P1? Drop your predictions below! 🏎️👇\n\n👉 Book championship keynote leadership: lornettedaye.com/speaking\n\n#LewisHamilton #RaceDay #F1Sunday #ItalianGP #Monza #TeamLH #GrandPrix #HighPerformance #LornetteDaye #EmotionalRegulation #ChampionMindset #LH44 #FinishStrong"
    },
    {
        "id": 12,
        "title": "THE TIRE WHISPERER: THE SUBTLE ART OF WINNING SLOWLY",
        "session": "Mid-Race Telemetry & Strategy",
        "dueAt": "2026-09-06T16:00:00.000Z", # Sunday Sep 6, 10:00 AM MDT
        "displayTime": "Sunday, Sep 6, 2026 - 10:00 AM MDT",
        "assetFile": "lh-12.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-12.jpg",
        "isVideo": False,
        "text": "\"BONO, MY TIRES ARE DEAD...\" (SETS FASTEST LAP).\n\nLewis Hamilton's tire management is the stuff of Formula 1 legend. He can nurse a set of degraded Pirelli mediums 15 laps longer than any rival, all while matching front-running lap times.\n\nIn business and life, aggressive sprinting without resource management leads directly to burnout and mechanical failure. True masters know when to preserve their energy and when to unleash maximum pace in the final stint.\n\nProtect your resources so you have ammunition when the race is decided.\n\nManage your energy like a 7-time World Champion.\n\n👉 Learn strategic pacing and executive resilience: lornettedaye.com/programs\n\n#LewisHamilton #TireWhisperer #HammerTime #F1Strategy #TeamLH #LornetteDaye #SustainableLeadership #ResourceManagement #HighPerformance #LH44 #FinishStrong"
    },
    {
        "id": 13,
        "title": "THE CHECKERED FLAG: VALOR, PODIUM, AND THE ETHOS OF EXCELLENCE",
        "session": "Post-Race Grand Prix Debrief",
        "dueAt": "2026-09-06T19:00:00.000Z", # Sunday Sep 6, 1:00 PM MDT
        "displayTime": "Sunday, Sep 6, 1:00 PM MDT",
        "assetFile": "lh-13.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-13.jpg",
        "isVideo": False,
        "text": "THE CHECKERED FLAG FALLS: VALOR ON THE TEMPLE OF SPEED.\n\nAfter 300+ kilometers of sustained 5G forces, blistering temperatures in the cockpit, and relentless tactical chess, the race is won.\n\nStanding on the podium receiving the cheers of thousands of passionate fans is the physical manifestation of hundreds of team members working in flawless unison.\n\nCelebrate your milestones, but never forget the collective effort that made the podium possible.\n\nHumility on the podium honors the people who built the machine.\n\n🏆 POST-RACE REACTION: How would you rate Lewis's drive today out of 10? Share your race rating below! 💬👇\n\n👉 Connect with Lornette Daye: lornettedaye.com\n\n#LewisHamilton #PodiumFinish #F1Debrief #TeamLH #Formula1 #LornetteDaye #HighPerformanceLeadership #ItalianGP #Monza #LH44 #FinishStrong #ExcellenceInMotion"
    },
    {
        "id": 14,
        "title": "THE LEGACY OF A 7-TIME CHAMPION: RELENTLESS REINVENTION",
        "session": "Sunday Evening Highlight & Debrief",
        "dueAt": "2026-09-06T22:30:00.000Z", # Sunday Sep 6, 4:30 PM MDT
        "displayTime": "Sunday, Sep 6 - 4:30 PM MDT",
        "assetFile": "lh-14.jpg",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-14.jpg",
        "isVideo": False,
        "text": "CONTINUOUS REINVENTION: THE SECRET TO TWO DECADES AT THE PINNACLE.\n\nDrivers come and go. Eras rise and fall. But Lewis Hamilton has stood at the summit of world motorsport across V8s, hybrid V6s, ground effect eras, and team transitions.\n\nWhy? Because he refuses to be nostalgic about past trophies. He tests new fitness regimens, investigates vegan plant-based nutrition, adapts to new steering geometries, and studies younger rivals with genuine curiosity.\n\nIf you want multi-decade longevity in your career, never believe you have arrived. Remain a perpetual student of your craft.\n\nReinvent yourself before the competition forces you to.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#LewisHamilton #CareerLongevity #PerpetualStudent #ContinuousReinvention #LornetteDaye #HighPerformance #TeamLH #Formula1 #LH44 #GOAT #FinishStrong"
    },
    {
        "id": 15,
        "title": "BEYOND THE PODIUM: PURPOSE, PLATFORM, AND HUMAN ELEVATION",
        "session": "Sunday Primetime Race Weekend Grand Finale",
        "dueAt": "2026-09-07T01:30:00.000Z", # Sunday Sep 6, 7:30 PM MDT
        "displayTime": "Sunday, Sep 6 - 7:30 PM MDT",
        "assetFile": "lh-01.png",
        "assetUrl": f"{BASE_IMAGE_URL}/lh-01.png",
        "isVideo": False,
        "text": "BEYOND THE TROPHIES: WHAT WILL YOUR PLATFORM STAND FOR?\n\n\"Winning races is great, but creating opportunities for young people who were told they couldn't make it—that is what I want to be remembered for.\"\n\nLewis Hamilton's ultimate greatness will not be measured by the silverware in his trophy room, but by Mission 44, the Hamilton Commission, and the doors he kicked open for marginalized voices across world sport.\n\nAs the curtain falls on another thrilling Grand Prix weekend, ask yourself:\nWhat are you doing with the influence, revenue, and platform your success has built?\n\nPour your greatness back into the world.\n\n👉 Join Olympian Coach Lornette Daye in building generational leadership: lornettedaye.com\n\n#LewisHamilton #PurposeDrivenLeadership #Mission44 #StillWeRise #TeamLH #LornetteDaye #GenerationalImpact #HumanitarianLegacy #LH44 #Formula1 #HighPerformance #FinishStrong"
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

def schedule_lewis_campaign():
    print("======================================================")
    print("🏎️ Scheduling Lewis Hamilton F1 Race Weekend Campaign (15 Posts)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Friday Sep 4 - Sunday Sep 6, 2026 | 5x Daily (6:30A, 10:00A, 1:00P, 4:30P, 7:30P MDT)")
    print("======================================================\n")

    results = []

    for idx, p in enumerate(lewis_posts):
        print(f"[{idx + 1}/{len(lewis_posts)}] Scheduling Post #{p['id']} ({p['session']}): \"{p['title']}\"")
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

    report_path = os.path.join(os.getcwd(), "scripts", "lewis-f1-weekend-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"🎉 Scheduled Report saved to {report_path}")

    scheduled_count = len([r for r in results if r.get("status") == "scheduled"])
    print(f"Summary: {scheduled_count}/{len(lewis_posts)} posts successfully scheduled directly in Buffer.\n")

if __name__ == "__main__":
    schedule_lewis_campaign()


posts = [
    {
        "id": 1,
        "title": "START WHERE YOU ARE, USE WHAT YOU HAVE",
        "dueAt": "2026-09-04T19:30:00.000Z",
        "displayTime": "Friday, Sep 4, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-01.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-01.png",
        "text": "START WHERE YOU ARE. USE WHAT YOU HAVE. DO WHAT YOU CAN.\n\nArthur Ashe didn't wait for ideal conditions to build a legendary legacy. In an era of segregation and steep barriers, he walked onto the court with immaculate precision, unshakable dignity, and absolute mastery over his craft.\n\nIn 40+ years of coaching Olympians and executive leaders, the greatest trap I see is waiting for the \"perfect moment\" to execute.\n\nChampionship performance begins with the resources you possess today.\n\nMaster the fundamentals in front of you, and momentum will take care of the rest.\n\n👉 Book championship keynote speaking: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #HighPerformance #LeadershipPoise #LornetteDaye #GrandSlam #BlackExcellence #FinishStrong #CourageUnderPressure #TennisHistory"
    },
    {
        "id": 2,
        "title": "QUIET INTENSITY: THE POWER OF UNDERSTATED EXCELLENCE",
        "dueAt": "2026-09-05T02:00:00.000Z",
        "displayTime": "Friday, Sep 4, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-02.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-02.png",
        "text": "QUIET INTENSITY: THE POWER OF UNDERSTATED EXCELLENCE.\n\nArthur Ashe never had to shout to command the room or the court. His composure was disarming, his tactical patience was lethal, and his dignity was impenetrable.\n\nIn high-stakes arenas, noise is often mistaken for authority. But true power is silent, deliberate, and grounded in emotional control.\n\nWhen the arena gets loud, drop your internal noise and let your execution speak.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#ArthurAshe #USOpen #LeadershipPoise #HighPerformance #LornetteDaye #InnerCalm #DignityInSport #ExecutiveLeadership #EmotionalMastery #FinishStrong"
    },
    {
        "id": 3,
        "title": "TACTICAL PATIENCE OVER RAW AGGRESSION",
        "dueAt": "2026-09-05T19:30:00.000Z",
        "displayTime": "Saturday, Sep 5, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-03.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-03.png",
        "text": "TACTICAL PATIENCE OVER RAW AGGRESSION.\n\nWhen Arthur Ashe dismantled Jimmy Connors in the 1975 Wimbledon final, he didn't try to out-hit him. He changed speeds, sliced, chipped, and used tactical genius to neutralize overwhelming power.\n\nAthletic greatness and business dominance aren't always about brute force—they are about strategic adaptation under fire.\n\nOut-think the competition before you try to out-muscle them.\n\n👉 Elevate your executive mindset: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #TacticalExcellence #StrategicLeadership #LornetteDaye #ChampionshipMindset #TennisWisdom #HighPerformance #CoachingExcellence"
    },
    {
        "id": 4,
        "title": "CIVIC COURAGE BEYOND THE BASELINE",
        "dueAt": "2026-09-06T02:00:00.000Z",
        "displayTime": "Saturday, Sep 5, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-04.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-04.png",
        "text": "CIVIC COURAGE BEYOND THE BASELINE.\n\n\"I know I could never forgive myself if I elected to live without humane purpose, without trying to help the poor and unfortunate, without recognizing that perhaps the purest joy in life comes with trying to help others.\"\n\nArthur Ashe understood that trophies tarnish, but generational impact endures. From fighting South African apartheid to establishing youth tennis foundations, his life stood for human elevation.\n\nWhat are you doing with the platform your success has built?\n\n👉 Discover our youth & community impact: lornettedaye.com/impact\n\n#ArthurAshe #USOpen #CivilRights #PurposeDrivenLeadership #LornetteDaye #HumanitarianLegacy #BlackExcellence #CommunityImpact #LeadershipIntegrity"
    },
    {
        "id": 5,
        "title": "TURNING ADVERSITY INTO A MORAL MANDATE",
        "dueAt": "2026-09-06T19:30:00.000Z",
        "displayTime": "Sunday, Sep 6, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-05.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-05.png",
        "text": "TURNING ADVERSITY INTO A MORAL MANDATE.\n\nWhen faced with life-altering health challenges, Arthur Ashe refused victimhood. He channeled his visibility into global education, public health awareness, and breaking down stigmas.\n\nAs a coach for four decades, I have learned that the measure of a champion isn't how they handle victory—it's how they pivot through unexpected storms.\n\nAdversity doesn't define you; your response writes the ultimate chapter.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#ArthurAshe #USOpen #Resilience #CourageInAdversity #LornetteDaye #LeadershipWisdom #OvercomingObstacles #FaithAndFocus #FinishStrong"
    },
    {
        "id": 6,
        "title": "PREPARATION IS THE MOTHER OF CONFIDENCE",
        "dueAt": "2026-09-07T02:00:00.000Z",
        "displayTime": "Sunday, Sep 6, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-06.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-06.png",
        "text": "PREPARATION IS THE MOTHER OF CONFIDENCE.\n\nArthur Ashe said: \"One important key to success is self-confidence. An important key to self-confidence is preparation.\"\n\nYou cannot improvise championship poise when the pressure peaks. Poise is the natural byproduct of thousands of unseen hours spent sharpening your mind, body, and emotional discipline.\n\nDo the heavy lifting in private so you can stand fearless in public.\n\n👉 Book Lornette Daye for your next corporate summit: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #Preparation #SelfConfidence #LornetteDaye #HighPerformanceCoaching #ChampionshipPoise #ExecutiveTraining #MentalToughness"
    },
    {
        "id": 7,
        "title": "THE SACRED DUTY OF MENTORSHIP",
        "dueAt": "2026-09-07T19:30:00.000Z",
        "displayTime": "Monday, Sep 7, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-07.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-07.png",
        "text": "THE SACRED DUTY OF MENTORSHIP.\n\nArthur Ashe didn't just break barriers—he turned around and built bridges. He founded the National Junior Tennis League (NJTL) to ensure underserved youth had access to education, sport, and opportunity.\n\nIn elite sports and corporate boardrooms, true leaders measure their greatness not by how many people serve them, but by how many people they elevate.\n\nWho are you pulling up behind you today?\n\n👉 Learn more about high-performance mentorship: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #MentorshipMatters #YouthEmpowerment #LornetteDaye #LeadershipLegacy #NJTL #CommunityExcellence #FinishStrong"
    },
    {
        "id": 8,
        "title": "GRACE UNDER MAXIMUM SCRUTINY",
        "dueAt": "2026-09-08T02:00:00.000Z",
        "displayTime": "Monday, Sep 7, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-08.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-08.png",
        "text": "GRACE UNDER MAXIMUM SCRUTINY.\n\nAs the first Black man to win the US Open, Wimbledon, and the Australian Open, Arthur Ashe carried the weight of history every time he stepped on the court.\n\nHe met hostility with intellect. He met prejudice with unmatched athletic majesty.\n\nWhen the spotlight is harsh, let your grace be your armor and your standard of excellence your shield.\n\n👉 Equip your leadership team with unwavering poise: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #GraceUnderPressure #PioneersInSport #LornetteDaye #LeadershipUnderFire #HistoricalExcellence #TennisLegends #UnshakableFocus"
    },
    {
        "id": 9,
        "title": "THE SCHOLAR-ATHLETE PHILOSOPHY",
        "dueAt": "2026-09-08T19:30:00.000Z",
        "displayTime": "Tuesday, Sep 8, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-09.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-09.png",
        "text": "THE SCHOLAR-ATHLETE PHILOSOPHY.\n\nArthur Ashe was an avid reader, historian, and author of *A Hard Road to Glory*, a definitive three-volume history of African American athletes. He believed mental development must always match physical conditioning.\n\nSpeed and strength can win a match. But intellectual curiosity, discipline, and emotional wisdom build a lifetime of triumph.\n\nFeed your mind with the same relentless rigor you give your business.\n\n👉 Discover Lornette Daye's life lessons & books: lornettedaye.com/books\n\n#ArthurAshe #USOpen #ScholarAthlete #ContinuousLearning #LornetteDaye #KnowledgeIsPower #LifelongMastery #HighPerformanceWisdom #HardRoadToGlory"
    },
    {
        "id": 10,
        "title": "PLAYING THE LONG GAME IN HIGH-STAKES ARENAS",
        "dueAt": "2026-09-09T02:00:00.000Z",
        "displayTime": "Tuesday, Sep 8, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-10.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-10.png",
        "text": "PLAYING THE LONG GAME IN HIGH-STAKES ARENAS.\n\nArthur Ashe understood that championships are won over sets, matches, seasons, and decades—not single points.\n\nWhen you face an unexpected break of serve or a sudden quarterly downturn, panic is your greatest enemy. Recalibrate your posture, trust your system, and stay committed to the marathon.\n\nLong-term consistency will always defeat short-term hype.\n\n👉 Book custom performance coaching: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #LongGame #StrategicFocus #LornetteDaye #HighPerformanceMindset #ConsistencyWins #ExecutiveCoaching #GrandSlamLeadership"
    },
    {
        "id": 11,
        "title": "THE POWER OF RADICAL INTEGRITY",
        "dueAt": "2026-09-09T19:30:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-11.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-11.png",
        "text": "THE POWER OF RADICAL INTEGRITY.\n\nOn and off the court, Arthur Ashe was the gold standard of ethical conduct. He called lines honestly, treated ball kids and royalty with equal respect, and never compromised his principles for convenience.\n\nIn modern leadership, integrity isn't an optional perk—it is the bedrock of trust, team loyalty, and sustainable victory.\n\nStand on principle, even when you stand alone.\n\n👉 Explore keynote topics on ethical high performance: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #IntegrityInAction #LeadershipCharacter #LornetteDaye #EthicsInSports #TrustAndLeadership #ExecutiveIntegrity #FinishStrong"
    },
    {
        "id": 12,
        "title": "HONORING THE STADIUM: WHERE LEGENDS ARE BORN",
        "dueAt": "2026-09-10T02:00:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-12.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-12.png",
        "text": "HONORING THE STADIUM: WHERE LEGENDS ARE BORN.\n\nEvery September, the greatest athletes on earth walk under the arch of Arthur Ashe Stadium in Flushing Meadows. Etched in steel is his timeless charge to humanity:\n\n\"From what we get, we can make a living; what we give, however, makes a life.\"\n\nAs the US Open enters its championship stretch, remember that your ultimate legacy is what you pour back into the world.\n\n👉 Connect with Lornette Daye: lornettedaye.com\n\n#ArthurAshe #USOpen #ArthurAsheStadium #FlushingMeadows #LornetteDaye #TennisChampionships #GenerationalImpact #LifeLegacy #ChampionMindset"
    },
    {
        "id": 13,
        "title": "QUARTERFINAL POISE: DELIVERING UNDER PRESSURE",
        "dueAt": "2026-09-10T19:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-01.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-01.png",
        "text": "QUARTERFINAL POISE: DELIVERING UNDER PRESSURE.\n\nAs the US Open rounds into the critical stages, the margin of error evaporates. Every unforced error is punished; every moment of hesitation is magnified.\n\nArthur Ashe thrived in these moments because his internal pulse was slower than the chaos around him.\n\nIn your business and life, high stakes don't require frantic effort. They require radical calm, sharp clarity, and flawless execution.\n\n👉 Learn executive resilience with Lornette Daye: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #HighPerformance #PressureIntoPower #LornetteDaye #ExecutivePoise #ChampionshipMindset #TennisExcellence #FocusUnderFire"
    },
    {
        "id": 14,
        "title": "SERVICE OVER STATUS",
        "dueAt": "2026-09-11T02:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-02.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-02.png",
        "text": "SERVICE OVER STATUS.\n\nArthur Ashe never allowed the adulation of fame to inflate his ego. When asked about his greatest achievements, he spoke about community tennis centers, AIDS awareness, and educational reform.\n\nTrue champions understand that prestige without purpose is hollow.\n\nUse your position of influence to serve those who cannot repay you.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#ArthurAshe #USOpen #ServantLeadership #LornetteDaye #PurposeOverPride #FaithInAction #CommunityFirst #LegacyBuilding #FinishStrong"
    },
    {
        "id": 15,
        "title": "SEMIFINAL FRIDAY: THE MASTERY OF FOCUS",
        "dueAt": "2026-09-11T19:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-03.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-03.png",
        "text": "SEMIFINAL FRIDAY: THE MASTERY OF FOCUS.\n\nSemifinal tennis at Arthur Ashe Stadium tests the absolute limits of human endurance and mental fortitude.\n\nArthur Ashe knew that when your physical stamina is tested, your mind must step forward and command the body.\n\nNever surrender your focus to exhaustion. Train your mind to be strongest when your body feels the weakest.\n\n👉 Elevate your team's mental toughness: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #Semifinals #MentalFortitude #LornetteDaye #HighPerformanceMindset #OvercomingFatigue #FocusAndDiscipline #ChampionshipHabits"
    },
    {
        "id": 16,
        "title": "COURAGE IS CONTAGIOUS",
        "dueAt": "2026-09-12T02:00:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-04.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-04.png",
        "text": "COURAGE IS CONTAGIOUS.\n\nWhen Arthur Ashe stepped forward on global issues, he gave permission for generations of athletes after him—from Venus and Serena Williams to Coco Gauff and Naomi Osaka—to stand boldly in their truth.\n\nLeadership is about demonstrating courage so clearly that those around you find their own backbone.\n\nBe the catalyst of courage in your organization today.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#ArthurAshe #USOpen #LeadershipCourage #InspiringGenerations #LornetteDaye #Trailblazers #CourageIsContagious #PioneersInAction #GrandSlamImpact"
    },
    {
        "id": 17,
        "title": "WOMEN'S FINAL SATURDAY: GLORY UNDER THE LIGHTS",
        "dueAt": "2026-09-12T19:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-05.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-05.png",
        "text": "WOMEN'S FINAL SATURDAY: GLORY UNDER THE LIGHTS.\n\nTonight, champions write their names into tennis immortality inside Arthur Ashe Stadium.\n\nThe trophy ceremony is only the final 10 minutes of a lifetime of relentless sacrifice, early morning conditioning, and unbroken belief.\n\nCelebrate the process as much as you celebrate the coronation.\n\n👉 Work directly with Olympian Coach Lornette Daye: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #WomensFinal #ChampionshipSaturday #LornetteDaye #AthleticExcellence #GrandSlamGlory #ProcessOverOutcome #FinishStrong"
    },
    {
        "id": 18,
        "title": "THE ANATOMY OF A CHAMPION'S MINDSET",
        "dueAt": "2026-09-13T02:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-06.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-06.png",
        "text": "THE ANATOMY OF A CHAMPION'S MINDSET.\n\nArthur Ashe proved that true power does not reside in physical muscle alone, but in intellectual mastery, emotional restraint, and moral conviction.\n\nWhen you align your skills with purpose and discipline, no opponent or circumstance can take your crown.\n\nAnchor yourself in purpose, and execute with precision.\n\n👉 Discover leadership insights & keynotes: lornettedaye.com/speaking\n\n#ArthurAshe #USOpen #ChampionsMindset #PurposeAndDiscipline #LornetteDaye #ExecutiveCoaching #PeakPerformance #MentalMastery #TennisLegacy"
    },
    {
        "id": 19,
        "title": "MEN'S FINAL SUNDAY: THE PINNACLE OF COMPETITION",
        "dueAt": "2026-09-13T19:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 1:30 PM MDT",
        "imageFile": "ashe-07.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-07.png",
        "text": "MEN'S FINAL SUNDAY: THE PINNACLE OF COMPETITION.\n\n58 years ago, Arthur Ashe became the first champion of the US Open era in 1968. Today, the world's best compete on the court bearing his name.\n\nChampionships are decided by who holds their nerve when everything is on the line.\n\nTrust your training. Silence the doubts. Seize your moment.\n\n👉 Schedule your breakthrough session: lornettedaye.com/programs\n\n#ArthurAshe #USOpen #MensFinal #ChampionshipSunday #LornetteDaye #HighPerformance #GrandSlamFinal #HoldYourNerve #TennisHistory"
    },
    {
        "id": 20,
        "title": "US OPEN 2026 FINALE: THE TIMELESS LEGACY OF ARTHUR ASHE",
        "dueAt": "2026-09-14T02:00:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 8:00 PM MDT",
        "imageFile": "ashe-08.png",
        "imageUrl": f"{BASE_IMAGE_URL}/ashe-08.png",
        "text": "US OPEN 2026 FINALE: THE TIMELESS LEGACY OF ARTHUR ASHE.\n\nAs the curtain falls on the 2026 US Open, we honor the man whose courage and grace built the foundation for modern sport.\n\n\"Success is a journey, not a destination. The doing is often more important than the outcome.\"\n\nTake Arthur Ashe's wisdom with you into every boardroom, classroom, and arena: walk with dignity, play with honor, and leave the world better than you found it.\n\n👉 Join the high-performance journey: lornettedaye.com\n\n#ArthurAshe #USOpen #GrandFinale #ArthurAsheLegacy #LornetteDaye #HighPerformance #DignityAndHonor #LifeJourney #FinishStrong"
    }
]

import ssl

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

def schedule_campaign():
    print("======================================================")
    print("🚀 Scheduling Arthur Ashe US Open Campaign (20 Posts)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Sep 4 - Sep 13, 2026 | 2x Daily (1:30 PM & 8:00 PM MDT)")
    print("======================================================\n")

    results = []
    import time

    for idx, p in enumerate(posts):
        print(f"[{idx + 1}/{len(posts)}] Scheduling Post #{p['id']}: \"{p['title']}\"")
        print(f"   Slot: {p['displayTime']} ({p['dueAt']})")
        print(f"   Image: {p['imageUrl']}")

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
                        "url": p["imageUrl"]
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

    report_path = os.path.join(os.getcwd(), "scripts", "arthur-ashe-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"🎉 Scheduled Report saved to {report_path}")

    scheduled_count = len([r for r in results if r.get("status") == "scheduled"])
    print(f"Summary: {scheduled_count}/{len(posts)} posts successfully scheduled directly in Buffer.\n")

if __name__ == "__main__":
    schedule_campaign()


