import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/zverev-usopen'

HASHTAGS = "#AlexanderZverev #Zverev #BenShelton #USOpen #USOpen2026 #ArthurAsheStadium #GrandSlam #Champion #Tennis #Redemption #Greatness #Sportsmanship #Resilience #Discipline #HighPerformance #ChampionMindset #OlympicCoach #LornetteDaye #Leadership"

posts_data = [
    # =========================================================================
    # LAUNCH POST: TONIGHT (Sunday Night, Sep 13, 2026)
    # =========================================================================
    {
        "id": 1,
        "theme_arc": "The Disbelief Moment",
        "slot": "Tonight (11:55 PM MDT)",
        "dueAt": "2026-09-14T05:55:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 11:55 PM MDT",
        "assetFile": "zverev-img-01-he-didnt-realize.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-01-he-didnt-realize.png",
        "isVideo": False,
        "cta": "Books (Survival Skills for Athletes - lornettedaye.com/books)",
        "text": f"""HE DIDN'T REALIZE HE'D WON. 🏆🎾✨

On championship point inside Arthur Ashe Stadium, Alexander Zverev struck the winning ball, turned around, and walked back to the baseline preparing for the next rally. It wasn't until Ben Shelton smiled and walked toward the net with arms open that reality crashed through:

*He had just won the 2026 US Open.* 6-3, 7-6, 5-7, 6-2.

That level of hyper-focus only comes when an athlete eliminates all outcome obsession and locks entirely into the process. Six years after his agonizing 2020 final loss, Sascha Zverev exorcised every demon on that court.

Fan Question: Did you catch Zverev's stunned reaction at match point? What went through your mind when he finally dropped his racket in tears?

👉 When your career faces heartbreak, focus is your only salvation. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026
    # =========================================================================
    {
        "id": 2,
        "theme_arc": "Exorcising the Demons",
        "slot": "Monday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-14T14:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-02-heartbreak-to-history.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-02-heartbreak-to-history.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""FROM HEARTBREAK TO HISTORY. 🌅🎾🥇

In 2020, Alexander Zverev stood two points away from his dream on Arthur Ashe, only to watch it slip away in a fifth-set tiebreak. In 2022, a devastating torn ligament threatened to end his elite career. 

Most people allow crushing setbacks to become their epitaph. Champions allow them to become their curriculum.

Yesterday, Zverev lifted the 2026 US Open trophy as a completely remodeled human being. More than a match—it was a masterclass in psychological rebirth.

Fan Question: How do you respond when life tests your resolve with heartbreaking defeat?

👉 Inspire your corporate teams to turn agonizing setbacks into breakthrough victories. Book Olympic Coach Lornette Daye for your executive summit: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 3,
        "theme_arc": "The Winning Point",
        "slot": "Monday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-14T18:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""CHAMPIONSHIP POINT REPLAY: Watch the exact moment disbelief turns into history! 🎥🔥🎾

Look closely at Zverev's body language after the return sails long. No celebration. No fist pump. Just pure, unadulterated flow state. He was so completely dialed in that his brain hadn't caught up with what his body had accomplished.

And look at Ben Shelton's class at the net—smiling, pointing, and embracing his rival with total dignity.

Fan Question: Is this the most surreal championship point finish in Grand Slam tennis history?

👉 Master the flow-state psychology that allows elite performers to deliver under maximum pressure. Read *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 4,
        "theme_arc": "Sportsmanship & Character",
        "slot": "Monday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-14T22:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-03-greatness-respects.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-03-greatness-respects.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""A CHAMPION. A FIGHTER. A MOMENT. 🤝👑

Look at the warmth between Alexander Zverev and Ben Shelton at the net. Shelton pushed Zverev to the brink with 140+ MPH artillery, but when the battle was done, there was nothing but mutual reverence.

*Respecting rivals elevates the sport.*

In four decades of coaching Olympic champions, I have witnessed that true greatness never diminishes its opponent. It honors the competitor that forced them to dig deeper into their soul.

Fan Question: What made Ben Shelton's run to the 2026 US Open final so special to you?

👉 Cultivate a workplace culture of radical respect and fierce, ethical competition. Book Lornette Daye for your leadership team: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 5,
        "theme_arc": "Trophy Glory",
        "slot": "Monday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-15T02:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""THE SILVER IS FINALLY HIS! 🏆✨🗽

Watch Alexander Zverev hoist the US Open Championship Trophy into the New York night sky! 

That smile represents thousands of hours of rehab, solitary gym sessions, tears behind closed doors, and the unshakeable decision never to give up on his calling.

*Discipline creates freedom. Endurance creates legacy.*

Fan Question: If you had to describe Zverev's six-year redemption arc in just ONE word, what word do you choose?

👉 Build the mental resilience needed to finish your marathon. Explore Lornette Daye's library of high-performance books: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 2: Tuesday, Sep 15, 2026
    # =========================================================================
    {
        "id": 6,
        "theme_arc": "The Score That Changed Everything",
        "slot": "Tuesday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-15T14:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-04-score-that-changed.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-04-score-that-changed.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""6-3, 7-6, 5-7, 6-2. The numbers that rewritten a legacy. 📊⚡

When Ben Shelton captured the third set 7-5, every spectator in Arthur Ashe held their breath. Was 2020 repeating itself? Would Zverev let doubt creep into his baseline rhythm?

His response in set four—breaking Shelton early, serving with 82% first-serve precision, and shutting the door—was the hallmark of emotional maturity.

Fan Question: What was the critical turning point in the final that sealed the championship for Zverev?

👉 Empower your leaders to execute flawlessly when momentum swings against them. Book Olympian Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 7,
        "theme_arc": "Flow State Video",
        "slot": "Tuesday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-15T18:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Midday video breakdown: The mechanics of championship composure! 🎾👀

Notice Zverev’s serve placement on match point—deep, kicking into the body, neutralising Shelton's explosive return. No overhitting. No panic. Just ruthless adherence to the game plan.

When you trust your fundamentals, you don't need miracles under pressure.

Fan Question: How do you stay calm and composed when everything is on the line?

👉 Fortify your mental foundation with practical lessons from 40+ years in Olympic athletics: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 8,
        "theme_arc": "He Came Back For This",
        "slot": "Tuesday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-15T22:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-05-he-came-back.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-05-he-came-back.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""HE CAME BACK FOR THIS. 💥🗽

*Harder roads lead to brighter days.*

When Zverev left Roland Garros in a wheelchair in 2022, critics asked if he would ever move the same way on hard courts. When he lost tight matches in 2024, critics questioned his mental fortitude.

Yesterday proved what every champion knows: Doubt from the outside is irrelevant when conviction from the inside is unbreakable.

Fan Question: What is the biggest doubt you had to conquer in your own journey to success?

👉 Bring world-class resilience training to your company. Schedule a keynote with Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 9,
        "theme_arc": "Trophy Roar Video",
        "slot": "Tuesday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-16T02:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""The sound of 24,000 fans celebrating human perseverance! 🔊🏆

When Alexander Zverev hoisted that silver cup, he wasn't just holding a trophy; he was holding the physical manifestation of six years of unbroken faith.

*Some comebacks change everything.*

Fan Question: Which comeback story in world sports inspires you the most?

👉 Read *Survival Skills for Believers* to cultivate champion-level endurance: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 3: Wednesday, Sep 16, 2026
    # =========================================================================
    {
        "id": 10,
        "theme_arc": "First At Last",
        "slot": "Wednesday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-16T14:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-06-first-at-last.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-06-first-at-last.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""FIRST AT LAST. 🥇✨

Alexander Zverev joins the pantheon of Grand Slam champions. 

In modern professional sports, the label "best player without a major" is a heavy anchor to carry. It breaks many athletes. Zverev chose to let it sharpen his hunger.

*Champions live differently.* They don't run from their labels; they dismantle them on the biggest court in the world.

Fan Question: Which active tennis player do you think will be next to break through for their first Grand Slam title?

👉 Teach your organization how to shed limiting labels and unlock their highest potential. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 11,
        "theme_arc": "Pure Joy Reel",
        "slot": "Wednesday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-16T18:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""That smile says it all. 😃🎾🏆

Watch how Sascha looks at the trophy before lifting it above his head. In that single moment, every 5:00 AM sprint, every ice bath, and every painful headline became worth it.

*A higher standard in sport.*

Fan Question: When did you last experience the pure joy of accomplishing something you fought years to achieve?

👉 Discover how to navigate the emotional peaks and valleys of elite ambition. Order Lornette Daye's books: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 12,
        "theme_arc": "The Wait is Over",
        "slot": "Wednesday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-16T22:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-07-the-wait-is-over.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-07-the-wait-is-over.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE WAIT IS OVER. ⏳👑

*Discipline drives destiny.*

The journey to the summit is rarely a straight line. It is a zigzag of setbacks, plateaus, and micro-adjustments. Those who quit on the plateaus never see the sunrise from the peak.

Zverev stayed on the mountain. And on Sunday, Arthur Ashe Stadium crowned him champion.

Fan Question: How do you maintain daily discipline when the results take months or years to show?

👉 Equip your executive leadership with the long-horizon stamina needed to win. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 13,
        "theme_arc": "Championship Point Breakdown",
        "slot": "Wednesday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-17T02:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Wednesday evening film study: Look at the sportsmanship between Zverev and Shelton! 🎥🤝

In an era where sports entertainment often defaults to manufactured drama, these two gladiators gave us pure athletic nobility. 

Fierce competition during the point. Unconditional brotherhood the second the point ends.

Fan Question: Does mutual respect between rivals make a championship match even more memorable?

👉 Learn the moral and mental principles that define enduring champions: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 4: Thursday, Sep 17, 2026
    # =========================================================================
    {
        "id": 14,
        "theme_arc": "Redemption at Arthur Ashe",
        "slot": "Thursday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-17T14:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-08-champion-magazine.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-08-champion-magazine.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""CHAMPION: REDEMPTION AT ARTHUR ASHE. 📰🏆

Thursday leadership editorial:
What does it take to walk onto the exact same court where you experienced the most painful failure of your life, in front of 24,000 spectators and millions watching globally, and rewrite your story?

It requires confronting the ghost of your past and refusing to let it dictate your future.

*Discipline. Resilience. Belongs here.*

Fan Question: Have you ever had to return to a place where you previously failed and try again? Tell me your story below!

👉 Book Olympian Coach Lornette Daye to empower your organization to face difficult challenges with fearless poise: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 15,
        "theme_arc": "Flow State Masterclass",
        "slot": "Thursday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-17T18:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""“He didn't realize he'd won.” 🤯🎾

Why did Zverev walk back to the baseline? Because in true peak performance, you don't calculate scorecards—you execute the micro-task in front of you. 

When you stay in the micro, the macro takes care of itself.

Fan Question: How do you prevent your brain from getting ahead of itself when you're close to a major goal?

👉 Master the high-performance mental conditioning used by Olympic medalists. Read Lornette Daye: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 16,
        "theme_arc": "Arthur Ashe Belongs to Him",
        "slot": "Thursday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-17T22:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-09-arthur-ashe-belongs.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-09-arthur-ashe-belongs.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""ARTHUR ASHE BELONGS TO HIM NOW. 🏟️✨

*2020: Pain builds better champions.*
*2026: Alexander Zverev wins the US Open.*

The court that once witnessed his deepest sorrow now stands as the cathedral of his triumph. When you outwork your doubt and honor the arena, greatness is inevitable.

Fan Question: What is your favorite stadium or arena in world sports?

👉 Elevate your team's mental toughness to handle high-stakes corporate arenas. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 17,
        "theme_arc": "Lifting the Cup",
        "slot": "Thursday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-18T02:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Thursday night reel: The culmination of a 15-year tennis journey! 🏆💫

From prodigy to contender, from heartbreak to injury, to Grand Slam champion. There are no shortcuts on the road to mastery.

*A brighter chapter ahead.*

Fan Question: Where does this US Open victory rank among the best sports moments of 2026?

👉 Build an unbreakable mental blueprint for your life and career. Order *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 5: Friday, Sep 18, 2026
    # =========================================================================
    {
        "id": 18,
        "theme_arc": "The Crown is His",
        "slot": "Friday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-18T14:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-10-crown-is-his.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-10-crown-is-his.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE CROWN IS HIS. 👑🗽🎾

Friday morning leadership insight:
*Discipline drives bigger destinies.*

Talent opens doors, but character keeps you in the room. When the pressure reached boiling point against Ben Shelton's electric power, Zverev didn't flinch. He let discipline steer the wheel.

Fan Question: What role has personal discipline played in your greatest achievements?

👉 Inspire your workforce to cultivate championship-level discipline. Book Olympic Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 19,
        "theme_arc": "Friday Trophy Energy",
        "slot": "Friday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-18T18:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Friday midday energy booster! ⚡🏆

Revisit the electric atmosphere inside Arthur Ashe Stadium as Alexander Zverev hoisted his first Grand Slam cup! Let this serve as your reminder heading into the weekend: 

No matter how far away your goal feels, persistent work compounds.

Fan Question: What goal are you currently chipping away at that you refuse to quit on?

👉 Discover practical mental frameworks for long-term compounding success: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 20,
        "theme_arc": "The Disbelief Flashback",
        "slot": "Friday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-18T22:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-01-he-didnt-realize.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-01-he-didnt-realize.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""PRESSURE BUILDS GREATNESS. SAME PAST. STRONGER TOMORROW. 💫🎾

When you face intense scrutiny, pressure can either crush your spirit or crystallize your talent into a diamond. Alexander Zverev allowed 6 years of pressure to forge him into a US Open champion.

Fan Question: How do you convert high-stakes pressure into focused energy?

👉 Equip your executive leadership with tools to thrive under immense corporate pressure. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 21,
        "theme_arc": "Friday Night Reel",
        "slot": "Friday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-19T02:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""The match point that will be studied for decades. 📽️✨

Watch how Ben Shelton congratulates Zverev before Zverev even realizes the match is done. True sportsmanship honors the human being across the net.

*Tennis elevates the spirit.*

Fan Question: What has tennis taught you about life and resilience?

👉 Learn the psychology of elite athletic and executive performance: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 6: Saturday, Sep 19, 2026
    # =========================================================================
    {
        "id": 22,
        "theme_arc": "Saturday Reflection",
        "slot": "Saturday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-19T14:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-02-heartbreak-to-history.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-02-heartbreak-to-history.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""Saturday morning sports masterclass:
Five years after the heartbreak of 2020, Alexander Zverev became a Grand Slam champion.

The greatest lesson of this US Open is simple:
Your past only defines you if you stop evolving. If you keep improving your craft, your past becomes the foundation of your triumph.

Fan Question: What past failure are you most grateful for today because of what it taught you?

👉 Book Olympian Coach Lornette Daye for inspiring keynote speeches on overcoming adversity: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 23,
        "theme_arc": "Saturday Action Reel",
        "slot": "Saturday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-19T18:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Relive the final ball. 🎾💥

Look at the silence across Arthur Ashe right before the serve, and the explosive eruption seconds later. Moments like this are why we fall in love with sports.

Fan Question: Were you watching live when Zverev won? What was the energy like in your living room?

👉 Develop the mental toughness required for life's biggest points. Read *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 24,
        "theme_arc": "Resilience Creates Beauty",
        "slot": "Saturday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-19T22:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-05-he-came-back.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-05-he-came-back.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*RESILIENCE CREATES BEAUTY.* 🎨✨

Saturday afternoon reflection:
True beauty in sport does not come from easy, unblemished dominance. It comes from the scars of battle, the surgeries, the tears, and the relentless decision to return.

Alexander Zverev def. Ben Shelton 6-3, 7-6, 5-7, 6-2. Arthur Ashe Stadium.

Fan Question: Which athlete's comeback story moves you the most?

👉 Bring authentic, high-impact leadership inspiration to your organization. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 25,
        "theme_arc": "Saturday Night Trophy Glow",
        "slot": "Saturday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-20T02:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Saturday night celebration! 🥂🏆

Under the bright stadium lights, Sascha Zverev lifts the Tiffany trophy. A victory for patience, for relentless work ethic, and for the belief that destiny belongs to those who refuse to stay down.

Fan Question: What celebration will you have when you reach your next big milestone?

👉 Equip yourself with the mindset of a champion: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # DAY 7: Sunday, Sep 20, 2026
    # =========================================================================
    {
        "id": 26,
        "theme_arc": "Rivalry & Brotherhood",
        "slot": "Sunday Morning (8:00 AM MDT)",
        "dueAt": "2026-09-20T14:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 8:00 AM MDT",
        "assetFile": "zverev-img-03-greatness-respects.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-03-greatness-respects.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""GREATNESS RESPECTS GREATNESS. 🤝💫

Sunday morning thought:
Ben Shelton is only getting started. To reach the US Open final and push a veteran champion to four grueling sets proves that American tennis is in brilliant hands.

When two champions respect each other, the entire sport rises.

Fan Question: How many Grand Slam titles do you predict Ben Shelton will win in his career?

👉 Build collaborative, high-trust leadership dynamics across competitive teams. Book Olympian Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 27,
        "theme_arc": "Sunday Midday Reel",
        "slot": "Sunday Midday (12:00 PM MDT)",
        "dueAt": "2026-09-20T18:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 12:00 PM MDT",
        "assetFile": "zverev-vid-02-trophy-lift.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-02-trophy-lift.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Sunday spotlight: One week after history was made! 🏆⭐

The 2026 US Open will go down as the tournament where redemption conquered doubt. Let this victory be your fuel for the week ahead.

*Character builds champions.*

Fan Question: What is the main takeaway you took from the 2026 US Open?

👉 Master the mental disciplines of elite athletes. Explore Lornette Daye's books: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 28,
        "theme_arc": "Arthur Ashe Special Issue",
        "slot": "Sunday Afternoon (4:00 PM MDT)",
        "dueAt": "2026-09-20T22:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 4:00 PM MDT",
        "assetFile": "zverev-img-08-champion-magazine.png",
        "assetUrl": f"{CDN_BASE}/zverev-img-08-champion-magazine.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""MORE THAN A MATCH. A HIGHER STANDARD IN SPORT. 🎾📰

As the US Open chapter closes, the standard has been raised. Alexander Zverev proved that the measure of a champion is not how gracefully they start, but how courageously they endure.

*Tennis lives bigger here.*

Fan Question: Who was your MVP of the entire 2026 US Open tournament?

👉 Bring Olympic wisdom, resilience frameworks, and high-performance poise to your organization. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 29,
        "theme_arc": "Grand Finale Championship Point",
        "slot": "Sunday Evening (8:00 PM MDT)",
        "dueAt": "2026-09-21T02:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 8:00 PM MDT",
        "assetFile": "zverev-vid-01-championship-point.mp4",
        "assetUrl": f"{CDN_BASE}/zverev-vid-01-championship-point.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""GRAND FINALE: THE MOMENT THAT CHANGED EVERYTHING. 🎾👑🔥

One final look at championship point: The ball strikes, the crowd rises, and Alexander Zverev stands frozen in disbelief before Ben Shelton embraces him.

To every dreamer, every athlete, and every leader who has suffered heartbreak: Keep stepping up to the baseline. Your moment is coming.

Own your arena. Lead with dignity. Finish strong.

Lornette Daye | 40+ Years in Olympic Athletics & Leadership Mastery

👉 Read *Survival Skills for Believers*: lornettedaye.com/books
👉 Keynote Speaking & Executive Coaching: lornettedaye.com/speaking

{HASHTAGS}"""
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
    with urllib.request.urlopen(req, context=ctx) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        if "errors" in body:
            print(f"   ❌ GraphQL Errors: {body['errors']}")
        return body.get("data", {})

def probe_assets():
    ctx = ssl._create_unverified_context()
    unique_urls = sorted(list(set(p["assetUrl"] for p in posts_data)))
    print(f"🔍 Pre-flight checking {len(unique_urls)} unique production URLs on https://lornettedaye.com...")
    all_ok = True
    for url in unique_urls:
        file_name = url.split('/')[-1]
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx) as resp:
                status = resp.status
                cl = resp.headers.get("Content-Length", "unknown")
                if status == 200:
                    print(f"  ✅ [200 OK] {file_name} ({cl} bytes)")
                else:
                    print(f"  ❌ [{status}] {file_name}")
                    all_ok = False
        except Exception as e:
            print(f"  ❌ [ERROR] {file_name} -> {e}")
            all_ok = False
    return all_ok

def main():
    print("======================================================")
    print("  Alexander Zverev US Open Champion Campaign: 29 Posts")
    print(f"  Channel: {CHANNEL_ID}")
    print(f"  Total posts to schedule: {len(posts_data)}")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(posts_data):
        print(f"[{idx + 1}/{len(posts_data)}] Scheduling Post #{p['id']} ({p['theme_arc']}): \"{p['slot']}\"")
        print(f"   Due: {p['dueAt']} | CTA: {p['cta']}")
        print(f"   Asset: {p['assetUrl']} (Video: {p['isVideo']})")

        if p.get("isVideo", False):
            asset_payload = [{"video": {"url": p["assetUrl"]}}]
        else:
            asset_payload = [{"image": {"url": p["assetUrl"]}}]

        input_data = {
            "channelId": CHANNEL_ID,
            "text": p["text"],
            "mode": "customScheduled",
            "dueAt": p["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": asset_payload
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
                msg = create_post.get("message", "Rate limit reached")
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

    report_path = os.path.join(os.path.dirname(__file__), "zverev-campaign-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Zverev Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
