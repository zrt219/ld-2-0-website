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

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', '')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/penix'

posts_data = [
    # Post 1 (Sat, Oct 03) - Asset: penix-01.png
    {
        "id": 1,
        "wave": "Wave 1: Preparation & Patience",
        "slot": "Day 1: Saturday, Oct 03, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-03T15:30:00.000Z",
        "assetFile": "penix-01.png",
        "assetUrl": f"{CDN_BASE}/penix-01.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "PATIENCE, POISE, AND PREPARATION: READY WHEN YOUR NUMBER IS CALLED. 🏈⚡\n\n"
            "In forty years of coaching Olympic athletes and champions, I have observed that the most critical season in an athlete's life "
            "is rarely the one spent in the spotlight. It is the quiet season spent preparing when nobody is watching.\n\n"
            "Look at Michael Penix Jr. When Atlanta selected him eighth overall, the external commentary was relentless. "
            "Critics debated the timeline, questioned the strategy, and created endless noise. "
            "Penix did what true professionals do: he kept his head down, absorbed the playbook, supported his teammates, "
            "and treated every backup rep with starter intensity.\n\n"
            "In enterprise leadership, high-potential executives often face a similar trial. "
            "You are ready to lead, but the timing asks you to wait. "
            "How you behave in that waiting room determines your authority when the door finally opens.\n\n"
            "Preparation is not passive. Preparation is active mastery.\n\n"
            "Stay ready,\n"
            "Lornette\n\n"
            "Bring this exact framework on high-stakes preparation and poise under pressure to your executive team. "
            "Book my keynote presentation for your leadership summit: https://lornettedaye.com/book\n\n"
            "#MichaelPenixJr #AtlantaFalcons #NFL #QB1 #PenixJr #PatienceAndPoise #ExecutiveLeadership #HighPerformance "
            "#OlympicMindset #PreparationEqualsConfidence #FinishStrong #LornetteDaye #LeadershipDevelopment #ReadyWhenCalled"
        )
    },
    # Post 2 (Sun, Oct 04 - NFL Sunday) - Asset: penix-golden-starter-poster.png
    {
        "id": 2,
        "wave": "Wave 1: Preparation & Patience",
        "slot": "Day 2: Sunday, Oct 04, 2026 at 09:30 AM MDT (NFL Game Day)",
        "dueAt": "2026-10-04T15:30:00.000Z",
        "assetFile": "penix-golden-starter-poster.png",
        "assetUrl": f"{CDN_BASE}/penix-golden-starter-poster.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE GOLDEN STANDARD: THE ATLANTA FALCONS STARTER ERA. 🔴⚫\n\n"
            "NFL Sundays do not care about excuses. When you step behind center as an NFL quarterback, "
            "you are commanding an entire franchise, eleven men in the huddle, and fifty thousand screaming fans in the stadium.\n\n"
            "What makes Michael Penix Jr. special is not just his generational left-handed arm talent. "
            "It is his composure. You cannot rush composure. It is forged through adversity, tested through delay, "
            "and anchored by an unwavering belief in your foundation.\n\n"
            "I teach corporate organizations that your team's culture under stress mirrors the demeanor of the person with the ball. "
            "When the leader breathes calmly, the huddle locks in.\n\n"
            "Lead with quiet conviction.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Elevate your organization's leadership poise and execution under fire. "
            "Inquire about executive retreats and keynote speaking: https://lornettedaye.com/book\n\n"
            "#AtlantaFalcons #RiseUp #MichaelPenixJr #FalconsNation #NFLSunday #QB1 #GoldenStandard #ExecutivePoise "
            "#LeadershipUnderPressure #OlympicExcellence #LornetteDaye #FinishStrong #SportsLeadership #GameDayMindset"
        )
    },
    # Post 3 (Mon, Oct 05) - Asset: penix-02.png
    {
        "id": 3,
        "wave": "Wave 1: Preparation & Patience",
        "slot": "Day 3: Monday, Oct 05, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-05T15:30:00.000Z",
        "assetFile": "penix-02.png",
        "assetUrl": f"{CDN_BASE}/penix-02.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "OVERCOMING TWO ACL TEARS: RESILIENCE AS A COMPETITIVE ADVANTAGE. 🛡️\n\n"
            "Before Michael Penix Jr. was a first-round NFL draft pick, he endured four season-ending injuries in college, "
            "including two torn ACLs. Most athletes would have walked away. The medical rehabilitation alone is agonizing.\n\n"
            "Penix did not surrender. He used each rehabilitation cycle to deepen his mental processing, study defensive tendencies, "
            "and reconstruct his mechanical efficiency.\n\n"
            "As an Olympic coach, I have seen careers made and broken on training tables. "
            "Physical talent opens the door, but resilience determines how long you stay in the room. "
            "Your scars are not evidence of weakness. They are proof that you survived the battle.\n\n"
            "Keep rebuilding your foundation.\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Book my keynote on resilience and bouncing back from setbacks for your company: "
            "https://lornettedaye.com/book\n\n"
            "#ResilienceInSport #MichaelPenixJr #OvercomingAdversity #InjuryComeback #MentalToughness #LeadershipResilience "
            "#OlympicMindset #LornetteDaye #FinishStrong #NFLQuarterback #CorporateKeynote #HighPerformanceCulture"
        )
    },
    # Post 4 (Tue, Oct 06) - Asset: penix-03.png
    {
        "id": 4,
        "wave": "Wave 1: Preparation & Patience",
        "slot": "Day 4: Tuesday, Oct 06, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-06T15:30:00.000Z",
        "assetFile": "penix-03.png",
        "assetUrl": f"{CDN_BASE}/penix-03.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "POCKET PRESENCE: PROCESSING SPEED IN HOSTILE ENVIRONMENTS. ⏱️\n\n"
            "An NFL quarterback has roughly 2.4 seconds to receive the snap, scan four downfield routes, identify a disguised safety blitz, "
            "and deliver a strike with 300-pound linemen bearing down on his chest.\n\n"
            "You cannot survive in the pocket if your mind is chaotic. Elite processing requires total emotional regulation.\n\n"
            "Michael Penix Jr. possesses rare stillness in the pocket. He does not flinch when the pocket collapses around him. "
            "In enterprise leadership, volatility is your pocket. Deadlines collapse, market dynamics shift, and competitors close in. "
            "The executives who win are the ones who cultivate internal stillness amidst external chaos.\n\n"
            "Quiet the noise. Trust your eyes.\n\n"
            "Stay steady,\n"
            "Lornette\n\n"
            "Empower your senior leaders to navigate hostile market environments with world-class composure. "
            "Book me for your next executive summit: https://lornettedaye.com/book\n\n"
            "#PocketPresence #ExecutivePresence #HighSpeedDecisionMaking #EmotionalRegulation #MichaelPenixJr #NFLQuarterback "
            "#LeadershipStrategy #PressureManagement #LornetteDaye #FinishStrong #CorporateKeynote"
        )
    },
    # Post 5 (Wed, Oct 07) - Asset: penix-04.png
    {
        "id": 5,
        "wave": "Wave 2: Pocket Presence & Precision",
        "slot": "Day 5: Wednesday, Oct 07, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-07T15:30:00.000Z",
        "assetFile": "penix-04.png",
        "assetUrl": f"{CDN_BASE}/penix-04.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE ART OF QUIET FILM STUDY: DOING THE UNSEEN WORK. 🎥🏈\n\n"
            "Championship games are not won on Sunday afternoons. They are won on Wednesday mornings at 6:00 AM in dark meeting rooms, "
            "watching the same third-down blitz disguise forty times until it becomes second nature.\n\n"
            "Michael Penix Jr. earned the trust of the Atlanta Falcons coaching staff by mastering the mental playbook. "
            "When young players obsess over physical gifts, true pros obsess over preparation.\n\n"
            "In forty years on track tracks around the globe, I told every athlete: the arena only showcases what you did in private. "
            "Never underestimate the compounding leverage of quiet, unglamorous preparation.\n\n"
            "Do the work in private.\n\n"
            "With purpose,\n"
            "Lornette\n\n"
            "Learn how to build elite preparation habits across your corporate teams. "
            "Book my keynote presentation today: https://lornettedaye.com/book\n\n"
            "#FilmStudy #PreparationIsKey #UnseenWork #MichaelPenixJr #AtlantaFalcons #WorkEthic #Professionalism "
            "#OlympicStandard #HighPerformanceHabits #FinishStrong #LornetteDaye #ExecutiveCoaching"
        )
    },
    # Post 6 (Thu, Oct 08) - Asset: penix-05.png
    {
        "id": 6,
        "wave": "Wave 2: Pocket Presence & Precision",
        "slot": "Day 6: Thursday, Oct 08, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-08T15:30:00.000Z",
        "assetFile": "penix-05.png",
        "assetUrl": f"{CDN_BASE}/penix-05.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "SILENCING THE NOISE: LETTING SUNDAYS ANSWER THE DOUBTERS. 🎯\n\n"
            "When Michael Penix Jr. was drafted, national pundits spent weeks debating the pick. "
            "They debated his age, his injury history, and the team's depth chart. "
            "Had Penix engaged in public debates or played the victim, he would have wasted vital energy.\n\n"
            "Instead, he smiled, thanked God for the opportunity, and went straight to the practice facility. "
            "Champions understand a simple principle: you do not defeat your critics with arguments. "
            "You defeat them with excellence.\n\n"
            "When your organization faces skepticism or market doubt, do not become defensive. "
            "Focus entirely on your execution. Results are the only argument that settles the score.\n\n"
            "Let your work speak.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Inquire about keynote bookings for your leadership conference: "
            "https://lornettedaye.com/book\n\n"
            "#SilenceTheNoise #MichaelPenixJr #FocusOnExecution #LeadershipExcellence #ResultsSpeak #NFLMindset "
            "#AtlantaFalcons #OlympicPoise #MentalClarity #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 7 (Fri, Oct 09) - Asset: penix-06.png
    {
        "id": 7,
        "wave": "Wave 2: Pocket Presence & Precision",
        "slot": "Day 7: Friday, Oct 09, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-09T15:30:00.000Z",
        "assetFile": "penix-06.png",
        "assetUrl": f"{CDN_BASE}/penix-06.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "COMMANDING THE HUDDLE: EARNING PEER RESPECT BEFORE THE SNAP. 🗣️🏈\n\n"
            "You cannot demand respect because of your draft status or your title. "
            "Respect in an NFL locker room is earned through daily consistency, genuine humility, and relentless preparation.\n\n"
            "When Michael Penix Jr. steps into the Atlanta Falcons huddle, veterans listen because he earned their trust through deeds, "
            "not words. He demonstrated that he was willing to learn, take hard coaching, and hold himself to the highest standard.\n\n"
            "In corporate management, young directors and newly appointed executives face this exact dynamic. "
            "You cannot demand allegiance through authority alone. You must earn it through competence, empathy, and poise under fire.\n\n"
            "Lead by example first.\n\n"
            "With conviction,\n"
            "Lornette\n\n"
            "Book my keynote address on executive presence and peer trust for your annual leadership event: "
            "https://lornettedaye.com/book\n\n"
            "#CommandTheHuddle #PeerLeadership #EarnedRespect #MichaelPenixJr #AtlantaFalcons #ExecutivePresence "
            "#LockerRoomCulture #TeamAccountability #OlympicLeadership #FinishStrong #LornetteDaye"
        )
    },
    # Post 8 (Sat, Oct 10) - Asset: penix-07.png
    {
        "id": 8,
        "wave": "Wave 2: Pocket Presence & Precision",
        "slot": "Day 8: Saturday, Oct 10, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-10T15:30:00.000Z",
        "assetFile": "penix-07.png",
        "assetUrl": f"{CDN_BASE}/penix-07.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "MECHANICAL PRECISION UNDER FATIGUE: DELIVERING IN THE FOURTH QUARTER. 💥\n\n"
            "Anyone can throw a beautiful pass in the first quarter when their legs are fresh and their adrenaline is high. "
            "The real test of an elite quarterback arrives with two minutes remaining in the fourth quarter, "
            "trailing by four points, with tired legs and a muddy pocket.\n\n"
            "Michael Penix Jr. has shown throughout his career that his mechanics remain repeatable regardless of exhaustion. "
            "His left-handed release is crisp, balanced, and decisive.\n\n"
            "Athletic greatness is not about performing well when conditions are ideal. "
            "It is about maintaining your standard when fatigue tempts you to compromise.\n\n"
            "Protect your standard.\n\n"
            "Stay disciplined,\n"
            "Lornette\n\n"
            "Equip your corporate teams to execute flawlessly through high-pressure fourth-quarter deadlines. "
            "Book me for your next executive retreat: https://lornettedaye.com/book\n\n"
            "#MechanicalPrecision #FourthQuarterClutch #ExecutionUnderFatigue #MichaelPenixJr #NFLQuarterback #AtlantaFalcons "
            "#HighPerformanceHabits #FinishStrong #LornetteDaye #LeadershipDiscipline"
        )
    },
    # Post 9 (Sun, Oct 11 - NFL Sunday) - Asset: penix-golden-starter-poster.png
    {
        "id": 9,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 9: Sunday, Oct 11, 2026 at 09:30 AM MDT (NFL Game Day)",
        "dueAt": "2026-10-11T15:30:00.000Z",
        "assetFile": "penix-golden-starter-poster.png",
        "assetUrl": f"{CDN_BASE}/penix-golden-starter-poster.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE MOMENT OF IMPACT: STEPPING ONTO THE BIGGEST STAGE. 🌟🔴⚫\n\n"
            "There comes a defining moment in every leader's journey where preparation meets opportunity. "
            "The backup headset comes off. The helmet goes on. You take the field as the starter.\n\n"
            "This golden Atlanta Falcons starter portrait represents more than one football player. "
            "It represents every professional who was counted out, told to wait, or doubted by critics, "
            "and who chose instead to dedicate their life to relentless, dignified craft mastery.\n\n"
            "When your moment arrives, you do not hope for success. You execute the blueprint you built in private.\n\n"
            "Rise up. Finish strong.\n\n"
            "Proudly,\n"
            "Lornette\n\n"
            "Bring Olympic-caliber inspiration and strategic clarity to your organization. "
            "Schedule a conversation to book my keynote: https://lornettedaye.com/book\n\n"
            "#AtlantaFalcons #RiseUp #MichaelPenixJr #NFLStarter #QB1 #GoldenLegacy #MomentOfImpact #SeizeTheMoment "
            "#OlympicStandard #FinishStrong #LornetteDaye #CorporateSpeaker #LeadershipInspiration"
        )
    },
    # Post 10 (Mon, Oct 12) - Asset: penix-08.png
    {
        "id": 10,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 10: Monday, Oct 12, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-12T15:30:00.000Z",
        "assetFile": "penix-08.png",
        "assetUrl": f"{CDN_BASE}/penix-08.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "NEXT-PLAY SPEED: ERASING MISTAKES FROM YOUR MINDSET. ⚡🧠\n\n"
            "One of the signature principles I teach athletes across golf, track, and football is this: "
            "your previous shot cannot hit your next shot. In football, your previous interception cannot throw your next touchdown.\n\n"
            "Young quarterbacks often struggle because they carry the ghost of past mistakes into the next drive. "
            "Michael Penix Jr. possesses rapid mental reset capability. If a drive stalls, he processes the breakdown on the tablet, "
            "takes a breath, and returns to the field with clean focus.\n\n"
            "How fast does your team recover from a failed pitch or a missed target? "
            "Speed of reset is the single greatest competitive advantage in high-stakes markets.\n\n"
            "Reset immediately. Finish strong.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Train your corporate team in high-speed mental resets and performance recovery. "
            "Book my keynote presentation: https://lornettedaye.com/book\n\n"
            "#NextPlaySpeed #MentalReset #HighPerformanceMindset #MichaelPenixJr #NFLStrategy #EmotionalPoise "
            "#LeadershipResilience #OvercomingMistakes #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 11 (Tue, Oct 13) - Asset: penix-09.png
    {
        "id": 11,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 11: Tuesday, Oct 13, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-13T15:30:00.000Z",
        "assetFile": "penix-09.png",
        "assetUrl": f"{CDN_BASE}/penix-09.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "FROM COLLEGE PHENOM TO PRO LEADER: NAVIGATING THE TRANSITION. 🎓🏈\n\n"
            "Dominating college football at Washington was an incredible feat, leading the nation in passing yards and reaching the National Championship. "
            "However, transitioning into the National Football League requires a complete elevation in preparation and maturity.\n\n"
            "Michael Penix Jr. handled the transition by embracing a humble, student-first mentality. "
            "He did not arrive in Atlanta acting like an established star. He arrived as a hungry craftsman eager to master the system.\n\n"
            "When high performers transition into new leadership roles or join larger organizations, ego is the greatest barrier to growth. "
            "The quickest way to earn authority is to show up with genuine curiosity and a relentless commitment to the team's standard.\n\n"
            "Stay humble. Stay hungry.\n\n"
            "With encouragement,\n"
            "Lornette\n\n"
            "Inquire about bringing me to speak to your emerging leaders and executive cohorts: "
            "https://lornettedaye.com/book\n\n"
            "#LeadershipTransition #StudentOfTheGame #MichaelPenixJr #CollegeToNFL #WashingtonHuskies #AtlantaFalcons "
            "#HumbleExcellence #OlympicMentorship #FinishStrong #LornetteDaye #ExecutiveDevelopment"
        )
    },
    # Post 12 (Wed, Oct 14) - Asset: penix-10.png
    {
        "id": 12,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 12: Wednesday, Oct 14, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-14T15:30:00.000Z",
        "assetFile": "penix-10.png",
        "assetUrl": f"{CDN_BASE}/penix-10.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "TRUSTING THE TIMELINE: WHY CHAMPIONS NEVER PANIC. ⏳\n\n"
            "In modern culture, everyone expects instant results. We want the promotion immediately. "
            "We want the market share overnight. We panic when things take longer than our planned calendar.\n\n"
            "Michael Penix Jr.'s journey is a masterclass in trusting the long game. "
            "From college injuries to transfer portals to draft-day surprises, nothing about his journey followed a smooth script. "
            "Yet, because he trusted his foundation, every delay ended up strengthening his character.\n\n"
            "Do not despise the season that requires patience. That is where your stamina is built.\n\n"
            "Trust your foundation.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Bring this transformative perspective on patience, stamina, and long-term execution to your corporate audience. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#TrustTheTimeline #PatienceInLeadership #LongTermVision #MichaelPenixJr #AtlantaFalcons #NoPanic "
            "#ResilientLeadership #OlympicWisdom #FinishStrong #LornetteDaye #CorporateSpeaker"
        )
    },
    # Post 13 (Thu, Oct 15) - Asset: penix-01.png
    {
        "id": 13,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 13: Thursday, Oct 15, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-15T15:30:00.000Z",
        "assetFile": "penix-01.png",
        "assetUrl": f"{CDN_BASE}/penix-01.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "CULTURE OVER CLICHÉ: BUILDING A WINNING STANDARD IN ATLANTA. 🏛️🔴⚫\n\n"
            "Culture is not a poster on the wall. Culture is how your team responds when you are down ten points on the road. "
            "Culture is whether your backup quarterback studies the opponent as if he is starting every single snap.\n\n"
            "Michael Penix Jr. is helping redefine the standard of Atlanta Falcons football through his poise, preparation, and selflessness. "
            "When your stars embody your culture, excellence becomes contagious.\n\n"
            "In my Olympic coaching career, I witnessed teams with average talent defeat world-record holders simply because "
            "their cultural alignment was unshakeable. Never underestimate the power of an aligned huddle.\n\n"
            "Build your culture daily.\n\n"
            "In partnership,\n"
            "Lornette\n\n"
            "Book my corporate keynote on building unshakeable championship culture: "
            "https://lornettedaye.com/book\n\n"
            "#ChampionshipCulture #AtlantaFalcons #MichaelPenixJr #TeamAlignment #HighPerformanceCulture #NFLQuarterback "
            "#OlympicCoaching #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 14 (Fri, Oct 16) - Asset: penix-golden-starter-poster.png
    {
        "id": 14,
        "wave": "Wave 3: The Starting Era & Legacy",
        "slot": "Day 14: Friday, Oct 16, 2026 at 09:30 AM MDT",
        "dueAt": "2026-10-16T15:30:00.000Z",
        "assetFile": "penix-golden-starter-poster.png",
        "assetUrl": f"{CDN_BASE}/penix-golden-starter-poster.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE CLIMAX: FINISH WHAT YOU STARTED. 🏆✨\n\n"
            "We conclude this two-week campaign with the golden image that embodies Michael Penix Jr.'s journey. "
            "He was questioned, delayed, tested, and challenged at every stage of his athletic career. "
            "Through it all, he remained anchored in his faith, his work ethic, and his unyielding commitment to his craft.\n\n"
            "To every leader, competitor, and builder reading these words: your journey may not look like anyone else's. "
            "You may have had to endure painful detours and seasons of waiting. "
            "Do not allow the delays to diminish your fire.\n\n"
            "Keep preparing. Keep stepping up. Always finish strong.\n\n"
            "Your coach and friend,\n"
            "Lornette\n\n"
            "Bring Lornette Daye to keynote your corporate summit, conference, or executive retreat: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #MichaelPenixJr #AtlantaFalcons #RiseUp #QB1 #GoldenLegacy #OlympicMindset "
            "#FinishWhatYouStarted #KeynoteSpeaker #CorporateKeynote #HighPerformance"
        )
    }
]

def check_invariants():
    for p in posts_data:
        t = p["text"]
        # Invariant 1: No em dashes
        for dash in ["\u2014", "&mdash;", "—"]:
            if dash in t:
                raise ValueError(f"Post #{p['id']} contains an em dash ({dash})!")
        # Invariant 2: Signed strictly Lornette
        if "Coach Lornette" in t:
            raise ValueError(f"Post #{p['id']} is signed 'Coach Lornette' instead of 'Lornette'!")
        if "Lornette" not in t:
            raise ValueError(f"Post #{p['id']} does not have Lornette signature!")
        # Invariant 3: 100% Keynote CTA
        if "lornettedaye.com/book" not in t:
            raise ValueError(f"Post #{p['id']} is missing keynote booking CTA!")

check_invariants()
print("INVARIANTS AUDIT PASSED: 0 em dashes, all signed strictly 'Lornette', 100% Keynote CTA.")

def schedule_posts():
    token = TOKEN or os.environ.get('BUFFER_ACCESS_TOKEN', '')
    if not token:
        print("BUFFER_ACCESS_TOKEN is not set. Saving staged schedule to report and queue files.")
        return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "BufferClient/1.0"
    }

    ctx = ssl._create_unverified_context()
    graphql_url = "https://api.buffer.com"
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            status
            dueAt
          }
        }
        ... on UserError {
          message
        }
      }
    }
    """

    results = []
    success_count = 0

    for i, p in enumerate(posts_data, 1):
        print(f"\n[{i}/14] Scheduling Post #{p['id']} ({p['slot']}) - Due: {p['dueAt']}...")
        print(f"  Asset: {p['assetUrl']}")

        payload = {
            "query": mutation,
            "variables": {
                "input": {
                    "channelId": CHANNEL_ID,
                    "text": p["text"],
                    "schedulingType": "automatic",
                    "mode": "customScheduled",
                    "dueAt": p["dueAt"],
                    "saveToDraft": False,
                    "needsApproval": False,
                    "assets": [
                        {
                            "image": {
                                "url": p["assetUrl"]
                            }
                        }
                    ]
                }
            }
        }

        req = urllib.request.Request(graphql_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                errors = res_data.get("errors")
                if errors:
                    print(f"  >>> GRAPHQL ERROR: {errors}")
                    p["status"] = "failed"
                    p["error"] = errors[0].get("message")
                else:
                    create_res = res_data.get("data", {}).get("createPost", {})
                    if "post" in create_res:
                        post_id = create_res["post"]["id"]
                        p["status"] = "scheduled"
                        p["postId"] = post_id
                        print(f"  >>> SUCCESS: Post ID: {post_id}")
                        success_count += 1
                    else:
                        err_msg = create_res.get("message", "Unknown error")
                        print(f"  >>> ERROR: {err_msg}")
                        p["status"] = "failed"
                        p["error"] = err_msg
        except urllib.error.HTTPError as he:
            err_body = he.read().decode("utf-8", errors="replace")
            print(f"  >>> HTTP ERROR {he.code}: {err_body}")
            p["status"] = "failed"
            p["error"] = f"HTTP {he.code}: {err_body}"
        except Exception as e:
            print(f"  >>> NETWORK ERROR: {e}")
            p["status"] = "failed"
            p["error"] = str(e)

        results.append(p)
        time.sleep(1.2)

    report_path = "scripts/penix-scheduled-report.json"
    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump(results, rf, indent=2, ensure_ascii=False)
    print(f"\nExecution complete. Saved {success_count}/14 successfully to {report_path}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
