# -*- coding: utf-8 -*-
import os
import json

output_file = os.path.join(os.path.dirname(__file__), "schedule-mondo-campaign.py")

script_content = '''# -*- coding: utf-8 -*-
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

CDN_BASE = 'https://lornettedaye.com/campaigns/mondo'

HASHTAGS = "#MondoDuplantis #Duplantis #TrackAndField #PoleVault #OlympicChampion #AthleticDirector #CoachingExcellence #HighPerformance #NCAATrack #WorldAthletics #SportsLeadership #OlympicMindset #LornetteDaye #RaisingTheBar"

posts_data = [
    # =========================================================================
    # WAVE 1: REDEFINING HUMAN LIMITS & THE PHYSICS OF OUTLIERS (Sep 14 - Sep 17)
    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026
    {
        "id": 1,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "assetFile": "mondo-1.png",
        "assetUrl": f"{CDN_BASE}/mondo-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""HOW HIGH CAN MONDO ACTUALLY GO? 🇸🇪🥇🚀

Armand "Mondo" Duplantis just pushed the World Record to 6.31 meters. Let that sink in: 20 feet, 8.5 inches above the earth on a flexible fiberglass pole.

In my 40+ years coaching Olympic athletes and national champions, I have studied generational phenoms across disciplines. Most athletes stop expanding when they run out of rivals. But Mondo isn't racing a competitor in the next lane—he is negotiating with gravity itself.

Track fans and biomechanics experts: Given current pole vault physics and takeoff velocities, what do you believe is the ultimate human ceiling—6.35m? 6.40m? Or is 6.31m already nudging against the physical barrier?

Coaches and Athletic Directors: Building an athlete who thrives when they are alone at the top requires an entirely different psychological playbook.

👉 Bring Olympic high-performance coaching to your athletic department, coaching symposium, or leadership team: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 2,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-14T19:00:00.000Z",
        "assetFile": "mondo-2.png",
        "assetUrl": f"{CDN_BASE}/mondo-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""HE ISN'T CHASING THE COMPETITION ANYMORE. HE'S CHASING THE CEILING. 📈⚡

When you are 20 centimeters clear of the silver medalist, who do you look at on the runway?

Most athletes crack when they no longer have a rabbit to chase. Without external benchmarks, urgency fades, complacency creeps in, and performance plateaus. Mondo Duplantis has achieved what only the rarest outliers do: complete internal benchmarking.

Every millimeter is an internal dialogue between preparation and fearlessness.

Athletes & Competitors: When you find yourself far ahead of your peers, how do you sustain the hunger to keep pushing your standards higher?

👉 Train the inner discipline required to dominate your sport from within. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 3,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-15T00:00:00.000Z",
        "assetFile": "mondo-3.png",
        "assetUrl": f"{CDN_BASE}/mondo-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE BAR KEEPS RISING. SO DOES HE. 👑🇸🇪

Look at the height of that bar. To anyone else, it looks like an impossible obstacle. To Mondo, it’s just the next checkpoint.

In Olympic sport, you don't rise to the occasion under pressure; you sink to the level of your training foundation. What the world sees for six seconds on the runway is the mathematical culmination of millions of unglamorous reps in an empty stadium.

Athletic Directors & Collegiate Coaches: How do you build an athletic culture where your athletes view pressure as a privilege rather than an emotional threat?

I work directly with collegiate athletic programs and sports leadership summits to instill the psychological resilience of champions.

👉 Book Lornette Daye for your athletic department’s keynotes and coaching workshops: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 2: Tuesday, Sep 15, 2026
    {
        "id": 4,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "assetFile": "mondo-4.png",
        "assetUrl": f"{CDN_BASE}/mondo-4.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""6.31M IS THE RECORD. NOT THE LIMIT. 🏟️✨

Sergey Bubka broke the pole vault world record 35 times. Mondo Duplantis has already broken it more than 10 times—one centimeter at a time.

Why one centimeter? Because elite mastery understands the power of progressive overload. When you jump 1cm higher each time, you don't just protect bonuses—you systematically stretch the human nervous system's perception of what is possible without inducing cognitive panic.

Track Coaches: Is resetting the record 1cm at a time the smartest psychological strategy in modern sports history, or would you want him to attempt 6.35m straight away?

👉 Learn the Olympic mindset of sustained, incremental greatness. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 5,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-15T19:00:00.000Z",
        "assetFile": "mondo-5.png",
        "assetUrl": f"{CDN_BASE}/mondo-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BUDAPEST. 6.20M. ANOTHER TITLE. 🇭🇺🥇

Before he broke 6.31m, there was Budapest. World championship pressure. Scorching heat. The entire stadium holding its breath.

Outsiders think championship moments are about hype. As an Olympic coach, I know they are about emotional regulation. When your pulse is pounding in your ears, can you execute the identical takeoff mechanics you practiced at 7:00 AM on a rainy Tuesday?

Coaches & Performance Directors: What is your team’s protocol when high-stakes emotional anxiety threatens to hijack technical mechanics?

I train teams, coaches, and sports executives to master high-stakes competitive poise.

👉 Book an Olympic performance clinic or keynote for your athletic program: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 6,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-16T00:00:00.000Z",
        "assetFile": "mondo-6.png",
        "assetUrl": f"{CDN_BASE}/mondo-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""SWEDEN'S GOLD STANDARD: WHAT MAKES A GENERATIONAL ICON? 🇸🇪🏅

Look at Mondo's focus in this shot. There is no tension in his jaw. No hurried desperation. Just quiet, centered authority.

In track and field, raw speed and power are common. What makes someone Sweden’s gold standard—and a global phenomenon—is the synchronicity between mind, breath, and spatial discipline.

Coaches & University Leaders: Are your development programs spending 90% of their time on conditioning and only 10% on the mental architecture that governs performance?

Let's flip the script.

👉 Schedule Lornette Daye to address your coaching staff and student-athletes: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 3: Wednesday, Sep 16, 2026
    {
        "id": 7,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "assetFile": "mondo-7.png",
        "assetUrl": f"{CDN_BASE}/mondo-7.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""ELEVATION IS A MINDSET. 🧠📏

You cannot clear a bar your mind hasn't already made peace with.

Before Mondo plants that pole in the box, his nervous system has already rehearsed the inversion, the hip clearance, and the release hundreds of times in microscopic detail. If there is a single sliver of doubt, the pole flexes differently, the drive knee stalls, and the bar crashes down.

Athletes: When you are standing before your biggest test, do you visualize the victory or are you secretly guarding against failure?

👉 Master the mental routines that transform fear into execution. Read *Survival Skills for Athletes* by Olympic coach Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 8,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-16T19:00:00.000Z",
        "assetFile": "mondo-8.png",
        "assetUrl": f"{CDN_BASE}/mondo-8.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""WORLD NO. 1. STILL LOOKING UP. ☝️✨

The most dangerous moment in any athletic career is the day you reach #1.

When you're chasing, the target is clear. But when you become the world standard, the mountain has no trail ahead. You have to blaze it yourself. Mondo Duplantis has been World No. 1 for years, yet every time he steps onto the runway, his finger points upward.

Athletic Administrators & Head Coaches: How do you keep an undefeated team or decorated champion hungry when everyone around them is telling them they've already won?

👉 Bring Lornette Daye to your campus to challenge your athletes and leadership to redefine their ceiling: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 9,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-17T00:00:00.000Z",
        "assetFile": "mondo-9.png",
        "assetUrl": f"{CDN_BASE}/mondo-9.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""SOME ATHLETES WIN. OTHERS REDEFINE POSSIBLE. 🚀🔥

Winning a gold medal means you beat the field on that specific day. Redefining what is possible means everyone who comes after you must rethink the laws of the sport.

Mondo Duplantis didn't just win Olympic gold; he altered the visual imagination of what human beings can accomplish with a pole and a runway.

Track Community: Who in sports history belongs in the same category as Mondo in completely redefining their event? (Carl Lewis, Usain Bolt, Dick Fosbury, Bob Beamon?)

Drop your pick in the comments.

👉 Discover the true story of Olympic perseverance and legacy. *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 4: Thursday, Sep 17, 2026
    {
        "id": 10,
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "assetFile": "mondo-10.png",
        "assetUrl": f"{CDN_BASE}/mondo-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""RAISE THE BAR. THEN CLEAR IT. 📈🛡️

It’s easy to talk about raising standards. It’s another thing entirely to walk up to the official, ask for the bar to be moved higher than any human has ever soared, and execute under the glare of millions of screens.

In collegiate and Olympic athletics, talk is cheap. Standards are verified only by execution under maximum resistance.

Coaches: What is one standard in your program right now that needs to be raised—and what is holding your team back from clearing it?

👉 Book Lornette Daye for your annual athletic banquet, coaching clinic, or leadership summit: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # =========================================================================
    # WAVE 2: THE PSYCHOLOGY OF SELF-COMPETITION & REPEAT EXCELLENCE (Sep 17 - Sep 21)
    # =========================================================================
    {
        "id": 11,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-18T00:00:00.000Z",
        "assetFile": "mondo-1.png",
        "assetUrl": f"{CDN_BASE}/mondo-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""IS SELF-COMPETITION HARDER THAN RACING A RIVAL? 🤔🇸🇪

Think about this: When you have a fierce rival breathing down your neck, your adrenaline spikes automatically. Survival instincts take over.

But when you are Mondo Duplantis, everyone else has packed up their poles and gone to the stands. The stadium is silent. The officials adjust the bar just for you. You have to generate every ounce of competitive electricity entirely from within your own soul.

Athletes & Coaches: Do you perform better when someone is challenging you, or when you are challenged only by your own standard?

In 40+ years of high-performance coaching, I've found self-competition is the highest form of athletic maturity.

👉 Empower your sports organization with championship mental toughness: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 5: Friday, Sep 18, 2026
    {
        "id": 12,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "assetFile": "mondo-2.png",
        "assetUrl": f"{CDN_BASE}/mondo-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""THE SPEED-POWER EQUATION: WHY MONDO OUT-JUMPS GIANTS ⚡📐

Mondo Duplantis is not the tallest vaulter in history. Nor does he have the heaviest frame.

What he possesses is lethal runway speed—clocking sprint times comparable to world-class 100m sprinters. When you transfer world-class kinetic speed directly into energy stored in a carbon-fiber pole, you don't need brute muscle to clear 6.30m+; you need flawless technical timing.

Coaches: How often do you see athletes trying to muscle through problems that actually require speed, rhythm, and leverage?

👉 Learn how to optimize athletic efficiency, recovery, and discipline. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 13,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-18T19:00:00.000Z",
        "assetFile": "mondo-3.png",
        "assetUrl": f"{CDN_BASE}/mondo-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""COACHING PHENOMS: THE PARENT-COACH DYNAMIC BEHIND MONDO 👨‍👦🇸🇪

Behind Mondo’s world records is one of the most successful family-coach partnerships in modern sports: his father Greg Duplantis (an elite pole vaulter himself) and his mother Helena (a Swedish heptathlete and volleyball player).

Navigating the line between parent and coach is one of the most perilous tightropes in athletics. Do it wrong, and you cause burnout and resentment. Do it right, and you create an unshakable foundation of trust and technical brilliance.

Parents & Coaches: How do you balance pushing for greatness while safeguarding an athlete’s emotional joy and human identity?

👉 Book Lornette Daye to speak on parenting champions and sustainable athletic leadership: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 14,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-19T00:00:00.000Z",
        "assetFile": "mondo-4.png",
        "assetUrl": f"{CDN_BASE}/mondo-4.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""THE 6-SECOND CRUCIBLE: WHERE TITLES ARE WON OR LOST ⏱️💥

From the moment Mondo initiates his first stride to the moment he clears the bar is approximately 6 seconds.

Six seconds. In those six seconds, thousands of hours of training, diet, mental therapy, and physical therapy are compressed into one explosive release. There is no room for conscious thought. If you think on the runway, you miss.

You have to trust the subconscious programming you built in the dark.

Athletes: What mental cue do you use right before you begin your competitive routine to silence mental noise?

👉 Develop deep, subconscious confidence under Olympic-level pressure. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 6: Saturday, Sep 19, 2026
    {
        "id": 15,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "assetFile": "mondo-5.png",
        "assetUrl": f"{CDN_BASE}/mondo-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""WHY THE WORLD STOPS TO WATCH POLE VAULT AGAIN 🌍🏟️

Before Mondo Duplantis, pole vault was considered a niche technical event hidden in track meet schedules. Today, entire Diamond League stadiums refuse to leave their seats until Mondo takes his final attempts at world record heights.

One athlete, through charismatic mastery and fearless ambition, transformed the cultural reach of an entire discipline.

Sports Directors & Event Leaders: That is the power of authentic star power rooted in athletic substance. How is your organization cultivating athletes who inspire beyond the scoresheet?

👉 Book Lornette Daye for your sports leadership summit or athletic convention: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 16,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-19T19:00:00.000Z",
        "assetFile": "mondo-6.png",
        "assetUrl": f"{CDN_BASE}/mondo-6.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""RESILIENCE AFTER A FAILED ATTEMPT: THE 2-MINUTE WINDOW 🔄⏳

At world record heights, Mondo misses frequently on his first and second attempts. The bar rattles. The crowd groans. The camera zooms in on his face.

Notice what he does: He doesn't kick the mat. He doesn't yell at officials. He sits on the bench, drinks water, visualizes the hip tuck, and resets his posture. In two minutes, his heart rate returns to baseline.

Competitors: When you fail publicly on attempt #1, how quickly can you wipe your emotional slate clean for attempt #2?

👉 Build rapid reset routines that keep you dominant under pressure. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 17,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-20T00:00:00.000Z",
        "assetFile": "mondo-7.png",
        "assetUrl": f"{CDN_BASE}/mondo-7.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE DANGER OF 'GOOD ENOUGH': LESSONS FROM MONDO DUPLANTIS ⚠️🏅

At 6.00m, Mondo had already won the competition. The gold was secured. The check was signed.

He could have waved to the crowd, put on his warmups, and celebrated. Instead, he told the officials: "Move the bar to 6.25m." Then "Move it to 6.31m."

Average programs celebrate when they beat the opponent. Championship programs don't stop until they test their absolute limits.

Coaches & Athletic Leaders: Does your culture celebrate just winning, or do you demand true personal excellence?

👉 Bring Olympic high-performance coaching to your university or sports organization: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 7: Sunday, Sep 20, 2026
    {
        "id": 18,
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "assetFile": "mondo-8.png",
        "assetUrl": f"{CDN_BASE}/mondo-8.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""THE LONELINESS OF BEING UNRIVALED 🏔️🇸🇪

When you operate at the outer boundary of human performance, there is no peer group to turn to for advice. Nobody else knows what 6.30m feels like at the top of the bend.

That isolation can break an athlete if their identity is built solely on trophies.

As an Olympic coach for over 40 years, I tell athletes: You must ground your worth in who you are as a human being, not just what height you clear.

Athletic Mentors: How do you protect your top performers from the emotional isolation of extreme success?

👉 Explore identity, purpose, and rising through pressure. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 19,
        "slot": "Sunday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-20T19:00:00.000Z",
        "assetFile": "mondo-9.png",
        "assetUrl": f"{CDN_BASE}/mondo-9.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""PRECISION OVER POWER: THE BIOMECHANICS OF ELEVATION 📐🔬

Watch Mondo Duplantis invert on the pole. His body traces a flawless C-curve around the crossbar, clearing it by millimeters without wasting an ounce of kinetic energy.

Many athletes believe that jumping higher requires more aggressive straining. In reality, elevation is about release and timing—knowing exactly when to stop pulling and allow physics to whip you upward.

Coaches: Where in your training are your athletes over-exerting because they lack technical refinement?

👉 Book Lornette Daye for high-performance athletic coaching workshops: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 20,
        "slot": "Sunday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-21T00:00:00.000Z",
        "assetFile": "mondo-10.png",
        "assetUrl": f"{CDN_BASE}/mondo-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""HALFWAY THROUGH THE CEILING: WHAT CAN YOUR TEAM CLEAR THIS WEEK? 🎯💥

We have completed Week 1 of our analysis of Mondo Duplantis's record-shattering journey.

Whether you coach a collegiate track squad, manage an athletic department, or lead an organization: The bar in front of you this week will not lower itself. You have to run faster, plant deeper, and commit to the jump.

What is the single biggest standard your team needs to clear before the month ends?

Share your target below.

👉 Transform your team's competitive culture with an Olympic keynote from Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # =========================================================================
    # WAVE 3: CHAMPIONSHIP COACHING STANDARDS & MENTAL RE-PROGRAMMING (Sep 21 - Sep 24)
    # =========================================================================
    # DAY 8: Monday, Sep 21, 2026
    {
        "id": 21,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "assetFile": "mondo-1.png",
        "assetUrl": f"{CDN_BASE}/mondo-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""COACHING THE UNPRECEDENTED: HOW DO YOU TRAIN AN OUTLIER? 🏅🇸🇪

When an athlete has surpassed every existing training manual in your sport, what does a coach do?

You can’t pull up old film to see how someone else did it. You are charting unexplored territory. The best coaches of generational phenoms don’t micromanage—they create an environment of psychological safety, physical recovery, and ruthless curiosity.

Athletic Directors: Does your coaching staff have the tools and mentorship to guide generational talent without holding them back?

👉 Elevate your coaching staff with Lornette Daye's Olympic leadership masterclass: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 22,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-21T19:00:00.000Z",
        "assetFile": "mondo-2.png",
        "assetUrl": f"{CDN_BASE}/mondo-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""CHASING THE CEILING: WHY COMFORT IS THE ENEMY OF CHAMPIONS 🚫🛋️

It is comfortable to rest on your laurels. Once you are Olympic champion and world record holder, the world will happily pay you appearance fees just to show up.

Mondo Duplantis refuses that comfort. Every season, he changes pole stiffness, refines his approach steps, and experiments with grip height. He risks failing on global TV in order to touch heights no human has ever breathed at.

Athletes: Are you currently protecting your past accomplishments or aggressively hunting your next level?

👉 Break through athletic comfort zones. Read *Survival Skills for Athletes* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 23,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-22T00:00:00.000Z",
        "assetFile": "mondo-3.png",
        "assetUrl": f"{CDN_BASE}/mondo-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""WHEN THE STADIUM HOLDS ITS BREATH: THE MENTAL CALM OF MONDO 🤫🏟️

60,000 spectators fall completely silent. The slow clap begins.

Many athletes tense up when the entire focus of an arena narrows onto them. Mondo uses that energy as wind beneath his wings. He harmonizes the stadium's rhythm with his approach strides.

Coaches: How do you train your athletes to absorb crowd energy instead of letting it paralyze their motor skills?

This is a trainable psychological skill.

👉 Book Lornette Daye for your sports leadership clinics and athletic department keynotes: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 9: Tuesday, Sep 22, 2026
    {
        "id": 24,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "assetFile": "mondo-4.png",
        "assetUrl": f"{CDN_BASE}/mondo-4.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""RECORDS ARE WRITTEN IN PENCIL. LEGACY IS ETCHED IN STONE. 🏛️✨

A record lasts until someone jumps 1cm higher. But the legacy of *how* you competed—your humility, your respect for the craft, your sportsmanship toward fellow competitors—endures forever.

Watch Mondo cheer for his rivals when they attempt personal bests. True champions don't need their competitors to fail to validate their own greatness.

Track Fans: Does Mondo's joy and sportsmanship make him even more compelling than his world record marks?

👉 Learn the deeper meaning of Olympic legacy. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 25,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-22T19:00:00.000Z",
        "assetFile": "mondo-5.png",
        "assetUrl": f"{CDN_BASE}/mondo-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BUDAPEST TO PARIS TO LA 2028: SUSTAINING EXCELLENCE ACROSS OLYMPIADS 🔄🏅

Winning one Olympic gold medal can happen on a lucky day. Winning multiple golds across multiple Olympic cycles requires an institutional standard of excellence.

Mondo Duplantis has dominated world pole vaulting since his teenage years, staying healthy, engaged, and motivated across changing Olympic quadrants.

Athletic Directors: How is your athletic department building sustainable development pipelines that keep athletes competing at the highest level year after year?

👉 Partner with Lornette Daye for high-performance athletic consulting: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 26,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-23T00:00:00.000Z",
        "assetFile": "mondo-6.png",
        "assetUrl": f"{CDN_BASE}/mondo-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""CULTURE DICTATES HEIGHT: LESSONS FROM SWEDISH ATHLETICS 🇸🇪🌟

Sweden produces outsized numbers of world-class champions across track, skiing, hockey, and swimming. Why?

Because their athletic system balances technical rigor with psychological autonomy. Athletes are encouraged to love the game, think for themselves, and take ownership of their training.

Coaches: Does your team culture encourage athletic ownership, or are your athletes merely following orders?

👉 Book Olympic coach Lornette Daye to consult on elite team culture and coaching dynamics: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 10: Wednesday, Sep 23, 2026
    {
        "id": 27,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "assetFile": "mondo-7.png",
        "assetUrl": f"{CDN_BASE}/mondo-7.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""THE ANATOMY OF FEAR: PLANTING AT 35 KM/H 🏃💨

Imagine sprinting full speed with a 17-foot carbon pole, aiming a 3-inch tip into a steel box sunk into the ground, knowing you will be propelled 20 feet in the air.

If you hesitate for one microsecond, the vault collapses. Pole vaulting requires total cognitive surrender to physics.

Competitors: How do you teach an athlete to run straight toward something that naturally triggers human fear instincts?

👉 Build fearless mental conditioning. Order *Survival Skills for Athletes* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 28,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-23T19:00:00.000Z",
        "assetFile": "mondo-8.png",
        "assetUrl": f"{CDN_BASE}/mondo-8.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""STILL LOOKING UP: THE ANCHOR OF HUMILITY ⚓🙌

Notice that when Mondo clears a world record, he doesn't belittle the sport. He bows to the bar. He hugs his parents. He thanks the fans.

Humility is not weakness; it is the ultimate shield against competitive fragility. When you know you are a student of your craft, you never stop learning.

Coaches & Leaders: What practices are in place in your program to keep your most successful athletes grounded and coachable?

👉 Schedule Lornette Daye for your school, conference, or athletic leadership retreat: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 29,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-24T00:00:00.000Z",
        "assetFile": "mondo-9.png",
        "assetUrl": f"{CDN_BASE}/mondo-9.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""REDEFINING POSSIBLE: LESSONS FOR EVERY STUDENT-ATHLETE 🎓🏃

You might not be aiming for 6.31 meters on a pole vault runway.

Maybe your ceiling is a college degree, making the varsity roster, or overcoming an ACL tear. The principles remain identical: break the daunting goal down centimeter by centimeter, refuse to accept external limits, and show up every morning with relentless consistency.

What "impossible" standard are you working to redefine this year?

👉 Read *Finish Strong: Chasing the Olympic Dream* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 11: Thursday, Sep 24, 2026
    {
        "id": 30,
        "slot": "Thursday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-24T19:00:00.000Z",
        "assetFile": "mondo-10.png",
        "assetUrl": f"{CDN_BASE}/mondo-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""RAISING THE CEILING IN COLLEGIATE ATHLETICS 🏫🏛️

Before Mondo conquered the Diamond League, he jumped for LSU in the NCAA. He learned how to handle team pressure, travel schedules, and collegiate expectations.

NCAA Track & Field remains the world's premier crucible for athletic development. But collegiate athletes face unprecedented pressures today—from NIL and transfer portals to 24/7 social media scrutiny.

Collegiate Athletic Directors & Coaches: Are you giving your athletes the inner resilience required to thrive under modern pressure?

👉 Book Lornette Daye for your collegiate athletic department's fall/spring keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # =========================================================================
    # WAVE 4: BUILDING ENDURING ATHLETIC LEGACY & THE OLYMPIC HORIZON (Sep 24 - Sep 27)
    # =========================================================================
    {
        "id": 31,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-25T00:00:00.000Z",
        "assetFile": "mondo-1.png",
        "assetUrl": f"{CDN_BASE}/mondo-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE 6.31M BLUEPRINT: HOW GENERATIONAL STANDARDS SPREAD 🌍📐

When Roger Bannister broke the 4-minute mile, several runners did it shortly after. Why? Because the psychological barrier was demolished.

Mondo Duplantis clearing 6.30m+ will do the exact same thing for track and field. High school and college vaulters today look at 6 meters not as a miraculous myth, but as an achievable benchmark.

Athletic Leaders: When you raise the ceiling for one athlete, you raise the belief system of an entire generation.

👉 Bring Lornette Daye to inspire your program's leaders to set generational standards: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 12: Friday, Sep 25, 2026
    {
        "id": 32,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "assetFile": "mondo-2.png",
        "assetUrl": f"{CDN_BASE}/mondo-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""THE CEILING IS AN ILLUSION: DECODING MENTAL BARRIERS 🧩⚡

In athletics, we often talk about "ceilings." We say an athlete has reached their peak, or that their physical frame has hit its limit.

In over four decades of coaching Olympic competitors, I have learned that 90% of physical ceilings are actually cognitive boundaries. When you rewire the athlete’s self-concept, the body suddenly finds another gear.

Athletes: Where in your life are you treating a temporary plateau as a permanent ceiling?

👉 Rewire your mental limits. Order *Survival Skills for Athletes* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 33,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-25T19:00:00.000Z",
        "assetFile": "mondo-3.png",
        "assetUrl": f"{CDN_BASE}/mondo-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""WHAT ATHLETIC DIRECTORS CAN LEARN FROM THE DUPLANTIS MASTERY 📋🏛️

To produce a world-record breaker, an athletic organization needs three aligned pillars:
1. World-class technical coaching
2. Unflinching mental resilience training
3. A culture that protects the athlete’s joy and humanity

If any of these three pillars is missing, the athlete burns out before they reach their prime.

Athletic Directors & Sports Executives: How strong are the three pillars in your program?

👉 Book Lornette Daye to conduct an Olympic High-Performance Audit & Keynote for your department: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 34,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-26T00:00:00.000Z",
        "assetFile": "mondo-4.png",
        "assetUrl": f"{CDN_BASE}/mondo-4.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""BEHIND THE 6.31M SMILE: WHAT FANS NEVER SEE 📸🌧️

The stadium cameras catch the celebratory backflips and the victory lap draped in the Swedish flag.

What they don’t show are the cold November mornings in Lafayette, Louisiana, where a 10-year-old Mondo jumped in his backyard until his hands were bleeding. The torn hand blisters. The missed flights. The moments of deep frustration.

Greatness is never bought in the spotlight. It is financed in the dark.

👉 Discover what it really takes to reach the Olympic summit. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 13: Saturday, Sep 26, 2026
    {
        "id": 35,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "assetFile": "mondo-5.png",
        "assetUrl": f"{CDN_BASE}/mondo-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE COMPETITOR’S PARADOX: PLAYFULNESS UNDER MAXIMUM STAKES 🎭🔥

Notice Mondo’s body language before a world record attempt: He jokes with the camera. He bounces on his toes. He smiles.

Most competitors become stiff and grim when the stakes are highest. But stiffness destroys the elasticity required for explosive jumping. By keeping his demeanor playful, Mondo preserves muscular fluidity and mental freedom.

Coaches: Are your athletes competing with joyful freedom, or are they paralyzed by fear of making a mistake?

👉 Invite Lornette Daye to speak to your coaches and teams about competing with freedom: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 36,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-26T19:00:00.000Z",
        "assetFile": "mondo-6.png",
        "assetUrl": f"{CDN_BASE}/mondo-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE GOLD STANDARD ACROSS GENERATIONS 🇸🇪👑

In sports history, we rarely get to witness an athlete who is so far ahead of their contemporaries that they define the era entirely.

Wayne Gretzky in hockey. Michael Jordan in basketball. Usain Bolt in sprinting. Mondo Duplantis in pole vault.

Studying these athletes is not just for track fans; it is essential study for anyone leading teams, managing talent, and driving human excellence.

👉 Book Lornette Daye for your sports leadership event, university commencement, or corporate keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 37,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-27T00:00:00.000Z",
        "assetFile": "mondo-7.png",
        "assetUrl": f"{CDN_BASE}/mondo-7.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""ELEVATION AS A DAILY HABIT: SMALL WINS, EXPONENTIAL HEIGHTS 📈🌱

You don't wake up one morning and decide to clear 6.31 meters.

You wake up and decide to execute your warm-up perfectly. You choose sleep over scrolling. You hydrate properly. You honor your recovery. Elevation is not an event—it is the compound interest of thousands of daily micro-decisions.

Athletes: What is one small daily habit you can upgrade starting tomorrow morning?

👉 Build the championship habits that sustain a career. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 14: Sunday, Sep 27, 2026 (Grand Finale Drops)
    {
        "id": 38,
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "assetFile": "mondo-8.png",
        "assetUrl": f"{CDN_BASE}/mondo-8.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""STILL LOOKING UP: THE COUNTDOWN TO LA 2028 🇺🇸⏳

The Los Angeles 2028 Olympic Games will take place on Mondo Duplantis's home continent. The energy in that stadium will be electric.

Every training cycle between now and 2028 is calculated to ensure that when he steps onto that runway in Los Angeles, he isn't just competing for gold—he is competing to elevate humanity's understanding of what is possible.

Sports Fans: Can Mondo clear 6.35m or 6.40m at LA 2028?

Tell me your prediction below.

👉 Prepare your mind and soul for ambitious goals. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 39,
        "slot": "Sunday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-27T19:00:00.000Z",
        "assetFile": "mondo-9.png",
        "assetUrl": f"{CDN_BASE}/mondo-9.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEYOND MEDALS: WHAT ATHLETES TEACH THE WORLD 🌍✨

Medals tarnish. World records are eventually eclipsed.

What never fades is the human inspiration of watching someone conquer their fear, trust their preparation, and fly without hesitation. Mondo Duplantis reminds every young kid in a gym, every coach on a track, and every leader in a boardroom that our biggest limits exist only in our minds.

Coaches & Athletic Leaders: Thank you for dedicating your lives to mentoring the next generation of champions.

👉 Connect with Olympic coach Lornette Daye for keynotes and consulting: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 40,
        "slot": "Sunday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-28T00:00:00.000Z",
        "assetFile": "mondo-10.png",
        "assetUrl": f"{CDN_BASE}/mondo-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""RAISE THE BAR. THEN CLEAR IT: THE 2-WEEK MONDO CAMPAIGN FINALE 🏁🇸🇪

Over the past 14 days, we have examined the mechanics, psychology, and standards of Armand "Mondo" Duplantis.

Here is the central lesson from four decades of Olympic coaching:
The bar will always feel intimidating. The runway will always demand courage. But when your foundation is built on discipline, family, and purpose, elevation is inevitable.

To every athletic director, head coach, and sports organization: Keep raising your standards.

👉 Bring Lornette Daye’s Olympic Masterclass to your campus or conference: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 41,
        "slot": "Sunday Evening Encore (7:30 PM MDT)",
        "dueAt": "2026-09-28T01:30:00.000Z",
        "assetFile": "mondo-1.png",
        "assetUrl": f"{CDN_BASE}/mondo-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE FINAL QUESTION: WHAT IS YOUR PERSONAL 6.31M? ❓🚀

We close our 2-week campaign with the question that matters most:

What is the standard in your life, your career, or your athletic program that you have been treating as an impossible barrier?

Is it leading with bolder authority? Demanding higher accountability from your team? Stepping into a national arena?

Whatever your crossbar is: Stop waiting for conditions to be perfect. Trust your preparation and take the runway.

👉 Book Lornette Daye to ignite your team with the Olympic mindset: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 42,
        "slot": "Sunday Night Grand Finale (9:00 PM MDT)",
        "dueAt": "2026-09-28T03:00:00.000Z",
        "assetFile": "mondo-4.png",
        "assetUrl": f"{CDN_BASE}/mondo-4.png",
        "cta": "Complete Catalog & Speaking (lornettedaye.com)",
        "text": f"""GRAND FINALE: THE CEILING IS AN ILLUSION. 👑✨

6.31 meters is a number in the record books. But the spirit of Mondo Duplantis—the relentless pursuit of incremental mastery, joyful courage under fire, and humble sportsmanship—belongs to all of us.

Thank you to the global track & field community, collegiate coaches, and athletic leaders who joined this discussion over the past 2 weeks.

Explore Lornette Daye’s complete Olympic high-performance library and keynote offerings:
👉 Keynote Speaking: lornettedaye.com/speaking
👉 Published Books ($14.99 CAD each): lornettedaye.com/books

Higher, further, together.

{HASHTAGS}"""
    }
]

def schedule_post(post):
    query = """
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            ... on PostActionSuccess {
                post {
                    id
                    status
                    scheduledAt
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

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "customScheduled",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "assets": {
                "images": [
                    {
                        "url": post["assetUrl"]
                    }
                ]
            }
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
            body = json.loads(resp.read().decode('utf-8'))
            return body
    except Exception as e:
        return {"error": str(e)}

def main():
    print(f"Starting Buffer queue scheduling for Mondo Duplantis Campaign (42 posts)...")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    results = []
    success_count = 0

    for idx, post in enumerate(posts_data, 1):
        print(f"[{idx}/42] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
        resp = schedule_post(post)

        create_post_data = resp.get("data", {}).get("createPost", {})
        post_obj = create_post_data.get("post")

        if post_obj and post_obj.get("id"):
            post_id = post_obj["id"]
            status = post_obj.get("status")
            sched_at = post_obj.get("scheduledAt")
            print(f"   --> SUCCESS! Post ID: {post_id} | Status: {status} | Scheduled: {sched_at}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "bufferPostId": post_id,
                "status": status,
                "assetUrl": post["assetUrl"],
                "cta": post["cta"],
                "success": True
            })
            success_count += 1
        else:
            err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
            print(f"   --> FAILED: {err_msg}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "error": err_msg,
                "success": False
            })

        time.sleep(0.5)

    print("-" * 60)
    print(f"Mondo Campaign Scheduling Complete: {success_count}/42 posts successfully placed into Buffer Scheduled Queue.")

    report_path = os.path.join(os.path.dirname(__file__), "mondo-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({
            "campaign": "Mondo Duplantis - The Ceiling is an Illusion",
            "total_posts": len(posts_data),
            "successful_posts": success_count,
            "channelId": CHANNEL_ID,
            "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "results": results
        }, f, indent=2)
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
'''

with open(output_file, "w", encoding="utf-8") as f:
    f.write(script_content)

print(f"Successfully generated {output_file} ({len(script_content)} bytes)")
