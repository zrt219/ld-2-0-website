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
BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/frances-tiafoe'



tiafoe_posts = [
    # WEDNESDAY SEP 9, 2026 (Day 1: JTCC Roots & Immigrant Grit)
    {
        "id": 1,
        "title": "FROM JTCC NIGHT SHIFTS TO ARTHUR ASHE STADIUM",
        "slot": "Wednesday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-09T14:00:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 8:00 AM MDT",
        "assetFile": "tiafoe-01.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-01.png",
        "text": "FROM SLEEPING ON JTCC MASSAGE TABLES TO LIGHTING UP ARTHUR ASHE STADIUM. 🎾⚡\n\nFrances Tiafoe’s story is the epitome of the immigrant hustle. His father, an immigrant from Sierra Leone, worked as the head of maintenance at the Junior Tennis Champions Center in Maryland. Frances and his brother slept on spare folding tables while practicing every spare minute of daylight.\n\nIn 40+ years of coaching Olympic champions and executive leaders, the greatest competitive advantage I have ever seen is hunger born from humble beginnings.\n\nYou cannot teach someone who was born on third base the grit of someone who had to build the ballpark.\n\nHonor your roots. Use your background as your greatest fuel.\n\n👉 Book keynote leadership on high-performance grit: lornettedaye.com/speaking\n\n#FrancesTiafoe #BigFoe #USOpen #Tennis #ArthurAshe #ImmigrantGrit #BlackExcellence #HighPerformance #LornetteDaye #ChampionMindset #JTCC #FinishStrong #ATP"
    },
    {
        "id": 2,
        "title": "ELECTRIC ENERGY: UNMATCHED COURT PRESENCE",
        "slot": "Wednesday Midday Highlight (11:30 AM MDT)",
        "dueAt": "2026-09-09T17:30:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 11:30 AM MDT",
        "assetFile": "tiafoe-02.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-02.png",
        "text": "BRINGING THE STADIUM TO ITS FEET: THE POWER OF AUTHENTIC CHARISMA. 🔥🎾\n\nWhen Big Foe steps onto the court, the entire atmosphere shifts. He doesn't just play tennis; he commands the room, hypes up the crowd, and turns high-pressure athletics into pure theater.\n\nIn corporate boardrooms and athletic arenas, leaders often try to suppress their natural personality to fit an outdated mold. But true magnetic leadership comes from having the courage to be fully, unapologetically yourself.\n\nNever shrink your magnitude to make others comfortable.\n\nBring your full energy to everything you do today.\n\n👉 Explore executive presence & leadership programs: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoeEnergy #USOpen #ArthurAsheStadium #Tennis #LeadershipPresence #LornetteDaye #AuthenticLeadership #HighPerformance #CharismaInSport #FinishStrong"
    },
    {
        "id": 3,
        "title": "JOY AS A COMPETITIVE WEAPON",
        "slot": "Wednesday Afternoon (2:30 PM MDT)",
        "dueAt": "2026-09-09T20:30:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 2:30 PM MDT",
        "assetFile": "tiafoe-03.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-03.png",
        "text": "JOY IS NOT A WEAKNESS—IT IS A CHAMPIONSHIP WEAPON. 🤍✨\n\nWatch Frances Tiafoe in a brutal 5th set tiebreak: he is smiling, nodding with the crowd, and genuinely relishing the fight. While opponents tighten up with anxiety, Frances plays with the freedom of someone who knows he is living his dream.\n\nWhen you love the battle more than you fear the outcome, pressure loses all power over you.\n\nFind the joy in your grind, and exhaustion will never catch you.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#FrancesTiafoe #BigFoe #JoyUnderPressure #USOpen #Tennis #HighPerformanceMindset #LornetteDaye #Resilience #MentalFortitude #ChampionSpirit #FinishStrong"
    },
    {
        "id": 4,
        "title": "CLUTCH 5-SET RESILIENCE & SHOTMAKING",
        "slot": "Wednesday Evening Highlight (5:30 PM MDT)",
        "dueAt": "2026-09-09T23:30:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 5:30 PM MDT",
        "assetFile": "tiafoe-04.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-04.png",
        "text": "CLUTCH EXECUTION IN THE 5TH SET: DIGGING DEEPER THAN YOUR OPPONENT. 🎾💪\n\nAt 2 sets all, 4 hours in, legs burning and lungs screaming for air—technique alone won't save you. What wins Grand Slam matches is the emotional willingness to suffer longer than the person across the net.\n\nFrances Tiafoe's record in US Open 5-set matches is legendary because he thrives when the stakes are raw and unforgiving.\n\nWhen your back is against the wall, don't look for an exit. Lean into the fire.\n\n👉 Discover coaching with Olympian Coach Lornette Daye: lornettedaye.com/athlete-coaching\n\n#FrancesTiafoe #BigFoe #ClutchPerformance #5SetThriller #USOpen #Tennis #LornetteDaye #HighPerformanceCoaching #GritAndGlory #NeverGiveUp #FinishStrong"
    },
    {
        "id": 5,
        "title": "THE POWER OF PURPOSE OVER PEDIGREE",
        "slot": "Wednesday Primetime (8:00 PM MDT)",
        "dueAt": "2026-09-10T02:00:00.000Z",
        "displayTime": "Wednesday, Sep 9, 2026 - 8:00 PM MDT",
        "assetFile": "tiafoe-05.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-05.png",
        "text": "PURPOSE OVER PEDIGREE: REWRITING THE SCRIPT OF ELITE SPORT. 🏆✨\n\nTennis historically belonged to country clubs and generational wealth. Frances Tiafoe shattered that ceiling with raw talent, family sacrifice, and an unshakable work ethic.\n\nNever let where you start determine where you finish. Your pedigree doesn't dictate your future—your daily commitment does.\n\nStep into spaces you weren't \"supposed\" to be in and own them.\n\n👉 Book Lornette Daye for your corporate summit: lornettedaye.com/speaking\n\n#FrancesTiafoe #BigFoe #BreakingBarriers #PurposeOverPedigree #BlackExcellence #LornetteDaye #Trailblazers #InclusionInSport #HighPerformance #FinishStrong"
    },

    # THURSDAY SEP 10, 2026 (Day 2: Crowd Synergy & Big Foe Energy)
    {
        "id": 6,
        "title": "WHEN 24,000 NEW YORKERS STAND ON THEIR FEET",
        "slot": "Thursday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-10T14:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 8:00 AM MDT",
        "assetFile": "tiafoe-06.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-06.png",
        "text": "24,000 FANS UNDER THE NIGHT LIGHTS: THE ART OF CROWD SYNERGY. 🗽🎾\n\nSome players shrink when the crowd gets loud. Frances Tiafoe conducts the Arthur Ashe crowd like a symphony. He channels every cheer, every gasp, and every chant into raw kinetic velocity on court.\n\nGreat leaders don't just speak to their audience—they build emotional bridges that turn passive spectators into committed teammates.\n\nConnect with your community and let their belief elevate your game.\n\n👉 Explore leadership dynamics and team building: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #ArthurAshe #USOpenNights #TennisCommunity #LornetteDaye #LeadershipSynergy #AudienceConnection #HighPerformance #FinishStrong"
    },
    {
        "id": 7,
        "title": "THE FOREHAND EXPLOSION & ATHLETIC REACH",
        "slot": "Thursday Midday Highlight (11:30 AM MDT)",
        "dueAt": "2026-09-10T17:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 11:30 AM MDT",
        "assetFile": "tiafoe-07.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-07.png",
        "text": "BIOMECHANICAL POWER: WEAPONIZING ATHLETICISM AT THE NET. ⚡🎾\n\nFrances Tiafoe's unique open-stance forehand and lightning-fast footwork allow him to retrieve balls that seem physically impossible to reach.\n\nWhen you master your physical mechanics and trust your instincts, you can innovate your own style rather than copying someone else's playbook.\n\nOwn your unique competitive advantage.\n\n👉 Elevate your biomechanics and mental agility: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #TennisTechnique #AthleticGreatness #LornetteDaye #HighPerformance #Biomechanics #PlayYourGame #FinishStrong #ATP"
    },
    {
        "id": 8,
        "title": "PRESSURE IS A PRIVILEGE: EMBRACING THE MARQUEE STAGE",
        "slot": "Thursday Afternoon (2:30 PM MDT)",
        "dueAt": "2026-09-10T20:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 2:30 PM MDT",
        "assetFile": "tiafoe-08.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-08.png",
        "text": "\"PRESSURE IS A PRIVILEGE.\" — BILLIE JEAN KING. 🎾✨\n\nPlaying in the second week of a Grand Slam brings global scrutiny. Every unforced error is replayed; every celebration is analyzed. Frances Tiafoe welcomes that pressure because he knows few people on earth ever earn the right to feel it.\n\nWhen high-stakes moments arrive in your career: don't complain about the pressure. Celebrate that you have earned a seat at the championship table.\n\nStep up and deliver.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#FrancesTiafoe #PressureIsAPrivilege #BigFoe #USOpen #Tennis #LornetteDaye #ExecutivePoise #ChampionshipMindset #HighPerformance #FinishStrong"
    },
    {
        "id": 9,
        "title": "TURNING DEFENSE INTO EXPLOSIVE WINNERS",
        "slot": "Thursday Evening Highlight (5:30 PM MDT)",
        "dueAt": "2026-09-10T23:30:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 5:30 PM MDT",
        "assetFile": "tiafoe-09.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-09.png",
        "text": "FROM ON THE ROPES TO WINNING THE POINT: THE COUNTER-ATTACK MINDSET. 💥🎾\n\nWhen opponents think they have Frances cornered behind the baseline, his explosive counter-punching turns a desperate defensive scramble into a baseline winner.\n\nIn business and life, defending your position is only half the battle. True resilience is turning your competitor's attack into your greatest opportunity to strike.\n\nTurn defense into dominance.\n\n👉 Discover high-performance leadership coaching: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #CounterAttack #TennisMastery #USOpen #LornetteDaye #StrategicExecution #HighPerformance #LeadershipWisdom #FinishStrong"
    },
    {
        "id": 10,
        "title": "STANDING IN AUTHENTICITY: NEVER DIMMING YOUR LIGHT",
        "slot": "Thursday Primetime (8:00 PM MDT)",
        "dueAt": "2026-09-11T02:00:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 8:00 PM MDT",
        "assetFile": "tiafoe-10.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-10.png",
        "text": "NEVER DIM YOUR LIGHT TO FIT SOMEONE ELSE'S COMFORT ZONE. 🌟✨\n\nFrances Tiafoe wears his heart on his sleeve. His raw emotion, his broad smile, his fist pumps, and his respect for opponents make him one of the most beloved figures in global sport.\n\nAuthenticity builds trust that sterile perfection never could. Be bold enough to show the world who you truly are.\n\nLead with courage and authenticity.\n\n👉 Book keynote speaking with Lornette Daye: lornettedaye.com/speaking\n\n#FrancesTiafoe #BigFoe #AuthenticLeadership #BeYourself #LornetteDaye #BlackExcellence #SportsInspiration #LeadershipCharacter #FinishStrong"
    },

    # FRIDAY SEP 11, 2026 (Day 3: Semifinal Fortitude & Tactical Growth)
    {
        "id": 11,
        "title": "THE EVOLUTION OF A GRAND SLAM CONTENDER",
        "slot": "Friday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-11T14:00:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:00 AM MDT",
        "assetFile": "tiafoe-01.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-01.png",
        "text": "CONTINUOUS REFINEMENT: EVOLVING FROM PHENOM TO GRAND SLAM REGULAR. 🎾📈\n\nReaching the semifinals of the US Open multiple times is not luck—it is the result of systematic tactical upgrades: improving second-serve percentages, shortening points, and conserving energy across two grueling weeks.\n\nGreatness is never static. If you want multi-year success in your field, continually upgrade your operating system.\n\nSharpen your fundamentals every single day.\n\n👉 Connect with Lornette Daye: lornettedaye.com\n\n#FrancesTiafoe #BigFoe #ContinuousImprovement #GrandSlamConsistency #LornetteDaye #HighPerformance #TennisDevelopment #FinishStrong"
    },
    {
        "id": 12,
        "title": "SERVE & VOLLEY AUDACITY UNDER FIRE",
        "slot": "Friday Midday Highlight (11:30 AM MDT)",
        "dueAt": "2026-09-11T17:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 11:30 AM MDT",
        "assetFile": "tiafoe-02.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-02.png",
        "text": "AUDACITY ON BREAK POINT: ATTACKING THE NET WHEN OTHERS HESITATE. ⚡🎾\n\nWhen facing break points in high-stakes matches, the conventional play is to stay safe behind the baseline. Frances Tiafoe dares to serve and volley, closing down angles and forcing opponents to make impossible passing shots.\n\nCalculated risk-taking when everything is on the line separates champions from contenders.\n\nTrust your training and take the initiative.\n\n👉 Elevate your strategic risk-taking: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #ServeAndVolley #ClutchTactics #USOpen #Tennis #LornetteDaye #StrategicRisk #HighPerformance #FinishStrong"
    },
    {
        "id": 13,
        "title": "OVERCOMING THE FIVE-SET MENTAL WALL",
        "slot": "Friday Afternoon (2:30 PM MDT)",
        "dueAt": "2026-09-11T20:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 2:30 PM MDT",
        "assetFile": "tiafoe-03.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-03.png",
        "text": "BREAKING THROUGH THE MENTAL WALL AT 3 HOURS 45 MINUTES. 🧠🔥\n\nEvery elite athlete hits the wall—that moment when lactic acid floods the muscles and self-doubt whispers that surrender is easier. Frances Tiafoe trains his mind to override physical fatigue and find another gear.\n\nYour mind commands your body, not the other way around. Train your thoughts to be strongest when your body feels weakest.\n\nBreak through your wall.\n\n👉 Read *Survival Skills for Believers*: lornettedaye.com/books\n\n#FrancesTiafoe #MentalToughness #OvercomingFatigue #BigFoe #LornetteDaye #HighPerformanceMindset #TennisPsychology #FinishStrong"
    },
    {
        "id": 14,
        "title": "MATCH POINT POISE & EMOTIONAL RELEASE",
        "slot": "Friday Evening Highlight (5:30 PM MDT)",
        "dueAt": "2026-09-11T23:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 5:30 PM MDT",
        "assetFile": "tiafoe-04.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-04.png",
        "text": "THE MOMENT OF TRIUMPH: EARNING YOUR STRIPES ON THE WORLD STAGE. 🏆🙌\n\nWhen match point is won and the racquet flies into the air, that roar from Frances Tiafoe represents every early morning, every doubter silenced, and every sacrifice his family made to give him this chance.\n\nCelebrate your victories with deep gratitude for the journey that built you.\n\nFinish Strong and celebrate your milestones.\n\n👉 Learn more about high-performance coaching: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #MatchPoint #TriumphInSport #LornetteDaye #GratitudeAndGlory #USOpen #TennisCelebration #FinishStrong"
    },
    {
        "id": 15,
        "title": "GIVING BACK: THE FRANCES TIAFOE FUND & YOUTH ACCESS",
        "slot": "Friday Primetime (8:00 PM MDT)",
        "dueAt": "2026-09-12T02:00:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:00 PM MDT",
        "assetFile": "tiafoe-05.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-05.png",
        "text": "PULLING UP THE NEXT GENERATION: THE FRANCES TIAFOE FUND. 🤝🎾\n\nFrances didn't just climb the mountain—he built an elevator. Through the Frances Tiafoe Fund and USTA Foundation, he provides tennis equipment, academic tutoring, and coaching grants to kids from underrepresented communities.\n\nTrue greatness is measured by what you leave behind. Use your success to build bridges for those coming next.\n\nBuild generational impact today.\n\n👉 Discover our community & youth initiatives: lornettedaye.com/impact\n\n#FrancesTiafoe #GivingBack #FrancesTiafoeFund #USTAFoundation #YouthEmpowerment #LornetteDaye #GenerationalImpact #CommunityLeadership #FinishStrong"
    },

    # SATURDAY SEP 12, 2026 (Day 4: Championship Horizon & Legacy)
    {
        "id": 16,
        "title": "BIG FOE ENERGY: INSPIRING THE NEXT GENERATION",
        "slot": "Saturday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-12T14:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:00 AM MDT",
        "assetFile": "tiafoe-06.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-06.png",
        "text": "BIG FOE ENERGY: REIMAGINING WHAT A TENNIS CHAMPION LOOKS LIKE. 🎾👑\n\nFor young kids in Maryland, Washington D.C., and across the world who never saw someone like themselves holding a tennis racquet, Frances Tiafoe is proof that the dream is real.\n\nRepresentation isn't just about visibility—it is about expanding the boundaries of what is possible in the minds of the next generation.\n\nBe the proof that it can be done.\n\n👉 Book championship speaking & mentorship: lornettedaye.com/speaking\n\n#FrancesTiafoe #BigFoe #RepresentationMatters #YouthInspiration #LornetteDaye #BlackExcellence #TennisLegends #FinishStrong"
    },
    {
        "id": 17,
        "title": "THE UNFILTERED PASSION OF CHAMPIONSHIP SPORT",
        "slot": "Saturday Midday Highlight (11:30 AM MDT)",
        "dueAt": "2026-09-12T17:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 11:30 AM MDT",
        "assetFile": "tiafoe-07.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-07.png",
        "text": "PASSION IS CONTAGIOUS: LEAVING EVERYTHING ON THE COURT. 🔥🎾\n\nYou will never hear anyone say Frances Tiafoe held back. He dives for volleys, hypes the crowd between games, and leaves every single drop of sweat on the baseline.\n\nIf you want extraordinary outcomes in business and life, don't hold back in reserve. Put everything you have on the line.\n\nGive 100% of your heart to your craft.\n\n👉 Read *Survival Skills for Women*: lornettedaye.com/books\n\n#FrancesTiafoe #BigFoe #UnfilteredPassion #HighPerformance #LornetteDaye #PassionInAction #AllHeart #FinishStrong"
    },
    {
        "id": 18,
        "title": "CONSISTENCY OVER CHAOS: REACHING THE ELITE TIER",
        "slot": "Saturday Afternoon (2:30 PM MDT)",
        "dueAt": "2026-09-12T20:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 2:30 PM MDT",
        "assetFile": "tiafoe-08.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-08.png",
        "text": "CHAMPIONSHIP MATURITY: TURNING FLASHES OF BRILLIANCE INTO SUSTAINED EXCELLENCE. 📈🏆\n\nFlashy highlight reels get views, but disciplined daily consistency wins Grand Slam titles. Frances Tiafoe's evolution into a perennial top-10 contender is proof of his maturing mental stamina and daily discipline.\n\nFall in love with the mundane daily fundamentals that create extraordinary milestones.\n\nConsistency will always defeat short-term hype.\n\n👉 Learn executive discipline & coaching: lornettedaye.com/programs\n\n#FrancesTiafoe #BigFoe #DailyDiscipline #ConsistencyWins #LornetteDaye #HighPerformance #TennisExcellence #FinishStrong"
    },
    {
        "id": 19,
        "title": "ARTHUR ASHE STADIUM: WHERE MAGIC HAPPENS",
        "slot": "Saturday Evening Highlight (5:30 PM MDT)",
        "dueAt": "2026-09-12T23:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 5:30 PM MDT",
        "assetFile": "tiafoe-09.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-09.png",
        "text": "ARTHUR ASHE STADIUM: THE TEMPLE OF HEROES AND HEART. 🗽✨\n\nThere is no arena in global sport quite like Arthur Ashe Stadium on a warm September evening. When Frances Tiafoe plays under these lights, history and modern excellence collide.\n\nHonor the pioneers who built the ground you stand on, and play with a spirit worthy of their legacy.\n\nStand on the shoulders of giants and reach higher.\n\n👉 Connect with Lornette Daye: lornettedaye.com\n\n#FrancesTiafoe #ArthurAshe #USOpen #TennisHistory #LornetteDaye #BlackExcellence #ArthurAsheStadium #FinishStrong"
    },
    {
        "id": 20,
        "title": "THE JOURNEY IS THE TROPHY: PURPOSE, PRIDE, AND FINISH STRONG",
        "slot": "Saturday Primetime Grand Finale (8:00 PM MDT)",
        "dueAt": "2026-09-13T02:00:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:00 PM MDT",
        "assetFile": "tiafoe-10.png",
        "assetUrl": f"{BASE_IMAGE_URL}/tiafoe-10.png",
        "text": "THE JOURNEY IS THE TRUE TROPHY: WALKING WITH PRIDE AND FINISHING STRONG. 🏆✨\n\nWin or lose, Frances Tiafoe walks off the court with his head held high, knowing that the kid from Hyattsville who started with a dream has inspired millions around the globe.\n\nYour worth is never defined by a single scoreboard. It is defined by the heart, dignity, and courage you bring to the arena.\n\nKeep pushing. Keep inspiring. Finish Strong.\n\n— Lornette Daye\n\n👉 Join Olympian Coach Lornette Daye in building championship resilience: lornettedaye.com\n\n#FrancesTiafoe #BigFoe #TheJourneyIsTheTrophy #FinishStrong #LornetteDaye #HighPerformance #Tennis #BlackExcellence #ChampionHeart #USOpen"
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

def schedule_tiafoe_campaign():
    print("======================================================")
    print("🎾 Scheduling Frances Tiafoe 4-Day Sprint Campaign (20 Posts)")
    print(f"Channel: Lornette Daye LinkedIn ({CHANNEL_ID})")
    print("Window: Wednesday Sep 9 - Saturday Sep 12, 2026 | 5x Daily (8:00A, 11:30A, 2:30P, 5:30P, 8:00P MDT)")
    print("======================================================\n")

    results = []

    for idx, p in enumerate(tiafoe_posts):
        print(f"[{idx + 1}/{len(tiafoe_posts)}] Scheduling Post #{p['id']} ({p['slot']}): \"{p['title']}\"")
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

    report_path = os.path.join(os.getcwd(), "scripts", "tiafoe-sprint-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"🎉 Scheduled Report saved to {report_path}")

    scheduled_count = len([r for r in results if r.get("status") == "scheduled"])
    print(f"Summary: {scheduled_count}/{len(tiafoe_posts)} posts successfully scheduled directly in Buffer.\n")

if __name__ == "__main__":
    schedule_tiafoe_campaign()
