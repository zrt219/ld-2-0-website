# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for Campaign 4: Mendoza (20 Posts)
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
        "slot": "Sunday (03:45 PM MDT)",
        "dueAt": "2026-10-18T21:45:00.000Z",
        "assetFile": "mendoza-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE QUARTERBACK: LEADERSHIP UNDER PRESSURE. 🏈🎯\n\nEvery snap asks for clarity. Purpose. Pressure. Performance.\n\nNo position in team sports concentrates psychological weight like the quarterback. Eighty thousand screaming spectators. Twenty-two moving bodies on the turf. A rolling play clock ticking toward zero. In that cauldron, the quarterback cannot afford an anxious heartbeat. He must see the coverage before the snap, diagnose rotation at the drop, and deliver the football on time.\n\nIn four decades of Olympic coaching, I have found that high-pressure clarity is not an innate gift. It is a disciplined mental structure built through deliberate cognitive training.\n\nLeaders: When market chaos collapses around your organization, do you react frantically, or command the pocket with calm?\n\n👉 Master the poise of elite leaders who finish what they started. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#TheQuarterback #LeadershipUnderPressure #FernandoMendoza #CalFootball #FinishStrong #OlympicMindset #CoachLornette"
    },
    {
        "id": 2,
        "slot": "Sunday (05:45 PM MDT)",
        "dueAt": "2026-10-18T23:45:00.000Z",
        "assetFile": "mendoza-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-02.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "QB2 MAY BE THE HARDEST JOB: PREPARE EVERY WEEK. WAIT WITHOUT WASTING. 📋⏳\n\nDiscipline builds opportunity before anyone offers you the stage.\n\nThe backup quarterback takes zero starting reps in practice. He stands on the sideline holding a clipboard, enduring the cold wind, knowing he might not play a single snap. Yet on third down in the fourth quarter, when the starter's helmet comes off, he must step onto the turf and execute the two-minute drill without hesitation or warmup excuses.\n\nMen often find themselves in seasons of waiting where their potential is overlooked. The amateur wastes his waiting season in resentment. The champion uses his waiting season to master the playbook.\n\nMen: Are you wasting your current holding pattern, or obsessively preparing for your sudden promotion?\n\n👉 Build mental grit, steady balance, and emotional resilience through seasons of quiet demand. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#QB2 #StayReady #DisciplineBuildsOpportunity #SurvivalSkillsForMen #PatienceAndPower #MenWhoLead #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Monday (08:30 AM MDT)",
        "dueAt": "2026-10-19T14:30:00.000Z",
        "assetFile": "mendoza-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-03.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE STILL EYE IN THE STORM: POCKET PRESENCE AS A REFLEX. 🌪️👁️\n\nWhen three-hundred-pound defensive linemen are closing from your blind side, human biology screams to run away.\n\nElite quarterback play demands the opposite: stepping into the pocket, keeping your eyes downfield, and delivering the strike with a defender driving his shoulder into your sternum. That courage does not come from bravado; it comes from an unshakeable faith in your mechanics and your offensive line.\n\nAthletes must train their nervous system to override panic reflexes when physical collisions are imminent.\n\nAthletes: Can you keep your eyes locked on the objective while chaos swirls around your periphery?\n\n👉 Build ironclad focus and physiological recovery under heavy contact. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#PocketPresence #FocusUnderFire #QuarterbackMindset #SurvivalSkillsForAthletes #OlympicDiscipline #LornetteDaye"
    },
    {
        "id": 4,
        "slot": "Monday (11:00 AM MDT)",
        "dueAt": "2026-10-19T17:00:00.000Z",
        "assetFile": "mendoza-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "THE PRE-SNAP READ: WINNING THE PLAY BEFORE THE BALL IS SNAPPED. 🧠🏈\n\nBy the time the ball leaves the quarterback's fingers, the outcome was decided five seconds earlier.\n\nFernando Mendoza reads the defensive alignment: safety depth, cornerback leverage, linebacker tilt. He changes the protection, adjusts the hot route, and calls out the blitz disguise. Great quarterbacking is 90% intellectual diagnosis and 10% physical execution.\n\nIn enterprise strategy, the executive who anticipates regulatory shifts and market consolidation wins the quarter before competitors even realize the environment has changed.\n\nExecutives: Is your organization diagnosing market indicators, or merely reacting after disruption hits?\n\n👉 Equip your executive suite with Olympic-caliber strategic foresight and operational poise. Book Lornette Daye for keynotes: lornettedaye.com/speaking\n\n#PreSnapRead #StrategicForesight #ExecutiveLeadership #QuarterbackVision #CoachLornette #CommandTheArena"
    },
    {
        "id": 5,
        "slot": "Monday (01:15 PM MDT)",
        "dueAt": "2026-10-19T19:15:00.000Z",
        "assetFile": "mendoza-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-05.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "MORE THAN A GAME: A BRIGHTER TOMORROW BUILDS TODAY. 🌅🏟️\n\nFootball provides a platform, but character provides the legacy.\n\nWhen Fernando Mendoza leads his team through the tunnel into a stadium illuminated by golden California sunlight, he carries more than play designs. He carries the discipline of family, the heritage of sacrifice, and the realization that young athletes across the country are watching how he conducts himself. Great leaders embrace the mantle of positive example.\n\nWhen your daily labor is connected to a purpose greater than yourself, fatigue loses its power to derail you.\n\nReaders: What greater mission fuels your perseverance when daily demands feel overwhelming?\n\n👉 Discover encouragement, renewed purpose, and strength for difficult chapters. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#MoreThanAGame #PurposeLivesHigher #SurvivingLife #FernandoMendoza #LegacyInAction #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Monday (03:45 PM MDT)",
        "dueAt": "2026-10-19T21:45:00.000Z",
        "assetFile": "mendoza-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-06.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "2.4 SECONDS: THE RUTHLESS WINDOW OF DIVISION I PASSING. ⏱️⚡\n\nIn collegiate football, you do not have three seconds to admire the scenery. The ball must be out of your hand in 2.4 seconds, or you are on your back.\n\nTo process five route concepts against split-field coverages in under two and a half seconds requires complete elimination of mental friction. There is zero time for second-guessing. Decisiveness is the difference between a sixty-yard touchdown and a devastating turnover.\n\nIn high-performance competition, hesitation is always more dangerous than an aggressive mistake.\n\nAthletes: Have you trained your decision-making to fire cleanly without hesitation?\n\n👉 Build rapid mental processing and pre-shot routines for elite competition. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#ProcessingSpeed #DecisiveExecution #NoHesitation #SurvivalSkillsForAthletes #OlympicMindset #LornetteDaye"
    },
    {
        "id": 7,
        "slot": "Monday (05:45 PM MDT)",
        "dueAt": "2026-10-19T23:45:00.000Z",
        "assetFile": "mendoza-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-07.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE CAPTAIN'S PATCH: OWNING THE BLAME, SHARING THE GLORY. 🎖️🤝\n\nTrue leadership is an asymmetrical trade: you absorb the failure, and deflect the credit to the huddle.\n\nWhen an interception is thrown, the elite quarterback stands at the postgame microphone and takes full responsibility, even if the receiver ran the incorrect depth. When three touchdowns are scored, he brings his offensive line to the podium and talks about their protection. That is how loyalty and trust are forged in blood.\n\nTeammates will lay everything on the line for a leader who protects them in public and holds them to excellence in private.\n\nLeaders: Are you shielding your team from external criticism, or throwing them under the bus when results fall short?\n\n👉 Master the principles of selfless, high-accountability leadership. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#Captaincy #Accountability #SelflessLeadership #FinishStrong #TeamFirst #OlympicCoaching #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Tuesday (08:30 AM MDT)",
        "dueAt": "2026-10-20T14:30:00.000Z",
        "assetFile": "mendoza-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-08.png",
        "cta": "Survival Skills for Students ($14.99 CAD)",
        "text": "THE FILM ROOM HABIT: WHERE VICTORY IS REHEARSED IN SILENCE. 📼💡\n\nWhile peers are socializing on Friday evening, the committed quarterback is rewinding third-down pressures for the twentieth time. He notes the weak-side linebacker's foot alignment. He studies the nickelback's blitz cadence. When Saturday afternoon arrives, there are no surprises.\n\nFor collegiate student-athletes, balancing rigorous academic coursework with twenty hours of weekly film study demands ruthless daily scheduling and zero procrastination.\n\nStudents: Are you studying your material deeply, or skimming the surface hoping to get by?\n\n👉 Practical tools for focus, academic stamina, and purpose-driven habits for young leaders. Read Survival Skills for Students ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForStudents #FilmStudy #PreparationWins #FocusAndExcellence #StudentAthleteDiscipline #LornetteDaye"
    },
    {
        "id": 9,
        "slot": "Tuesday (11:00 AM MDT)",
        "dueAt": "2026-10-20T17:00:00.000Z",
        "assetFile": "mendoza-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-09.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE ZERO-SECOND MEMORY: RISING IMMEDIATELY AFTER A DISASTER. 🔄🛡️\n\nEvery great quarterback throws an interception that gets returned for a touchdown. The stadium boos. The momentum swings wildly. Your heart sinks into your cleats.\n\nIn that brutal moment, you have a stark choice: surrender to shame, or sit on the sideline bench, put on the headset, review the coverage sheet, and prepare for the next possession. The previous snap cannot hit the next throw. What matters is the drive that follows.\n\nIn Olympic competition, I teach athletes that resilient champions are defined by the speed of their mental reset.\n\nLeaders: How quickly does your organization reset after a catastrophic setback?\n\n👉 Build unshakeable emotional resilience and learn how to finish strong after failure. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#ZeroSecondMemory #ResilienceAfterSetback #ResetAndExecute #FinishStrong #OlympicMindset #LornetteDaye"
    },
    {
        "id": 10,
        "slot": "Tuesday (01:15 PM MDT)",
        "dueAt": "2026-10-20T19:15:00.000Z",
        "assetFile": "mendoza-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-10.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE KINETIC CHAIN: VELOCITY IS BORN IN THE HIPS AND FEET. 🦾⚙️\n\nAmateurs throw with their arm. Champions throw with their entire kinetic chain.\n\nA sixty-yard post pass against tight coverage originates in the back foot planted firmly in the turf, rotates through the hips, transfers through core torque, and releases smoothly off the fingertips. If your lower body is exhausted, your accuracy disintegrates.\n\nFernando Mendoza invests hours in rotational mobility, scapular stability, and core endurance. When your physical foundation is rock solid, precision remains effortless into the fourth quarter.\n\nAthletes: Are you training your complete kinetic foundation, or neglecting the supporting muscles?\n\n👉 Build champion physical systems and injury prevention habits. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#KineticChain #QuarterbackMechanics #ThrowingVelocity #SurvivalSkillsForAthletes #OlympicBiomechanics #LornetteDaye"
    },
    {
        "id": 11,
        "slot": "Tuesday (03:45 PM MDT)",
        "dueAt": "2026-10-20T21:45:00.000Z",
        "assetFile": "mendoza-11.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-11.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "GOLDEN STATE PRIDE: REPRESENTING SOMETHING BIGGER THAN YOURSELF. 🐻🏈\n\nPutting on the blue and gold jersey of California football carries over a century of academic and athletic tradition. From Memorial Stadium overlooking the San Francisco Bay to the halls of Berkeley, the expectations are massive. Fernando Mendoza represents that legacy with immense pride and personal dignity.\n\nWhen you understand that you stand on the shoulders of giants, personal vanity fades, and genuine stewardship takes over.\n\nReaders: How does honoring your family and institutional roots give you strength today?\n\n👉 Find deep meaning, renew perspective, and build a foundation of hope. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#CalBears #GoldenStatePride #Stewardship #SurvivingLife #LegacyAndHeritage #LornetteDaye"
    },
    {
        "id": 12,
        "slot": "Tuesday (05:45 PM MDT)",
        "dueAt": "2026-10-20T23:45:00.000Z",
        "assetFile": "mendoza-12.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-12.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "COMMANDING THE HUDDLE: THE PSYCHOLOGY OF EYE CONTACT. 👁️⚡\n\nWhen ten exhausted, bruised teammates lean into the huddle with ninety seconds remaining, they are not just listening to play numbers. They are looking into the quarterback's eyes.\n\nIf they see fear, they tighten up. If they see quiet conviction and calm certainty, their belief surges. Fernando Mendoza steps into the circle, makes direct eye contact with every lineman and receiver, and calls the play with unmistakable cadence. Presence is communicated before words are spoken.\n\nIn boardrooms, leaders who speak with grounded vocal resonance and calm posture inspire immediate organizational alignment.\n\nExecutives: Does your executive presence project calm authority in crisis situations?\n\n👉 Train your senior executives to command high-stakes meetings with Olympic presence. Book Lornette Daye: lornettedaye.com/speaking\n\n#HuddleLeadership #ExecutivePresence #EyeContact #CommandTheRoom #CoachLornette #LeadershipInCrisis"
    },
    {
        "id": 13,
        "slot": "Wednesday (08:30 AM MDT)",
        "dueAt": "2026-10-21T14:30:00.000Z",
        "assetFile": "mendoza-13.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-13.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE RED ZONE: WHERE MARGINS SHRINK TO INCHES. 🔴🎯\n\nBetween the twenty-yard line and the goal line, the football field shrinks drastically. Safeties compress down. Windows close in a fraction of a second. A throw that is six inches off target is batted away or intercepted.\n\nSuccess in the red zone requires extreme tactical discipline and ball placement. You cannot force passes into triple coverage hoping for miracles. You take what the defense yields, protect the possession, and strike ruthlessly when the seam opens.\n\nIn high-stakes corporate closings, the final mile demands surgical focus and zero emotional carelessness.\n\nLeaders: Can your team execute with heightened precision when space and time are severely limited?\n\n👉 Master the finishing mechanics that ensure victory at the goal line. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#RedZoneExecution #PrecisionPassing #FinishStrong #HighStakesCloser #OlympicMindset #LornetteDaye"
    },
    {
        "id": 14,
        "slot": "Wednesday (11:00 AM MDT)",
        "dueAt": "2026-10-21T17:00:00.000Z",
        "assetFile": "mendoza-14.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-14.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "BIOFEEDBACK UNDER THE HELMET: CONTROLLING YOUR AUTONOMIC NERVOUS SYSTEM. 🧘‍♂️🏈\n\nElite athletic performance is biological mastery.\n\nWhen adrenaline spikes to maximum levels during a hostile road contest, fine motor skills deteriorate. Your grip tightens too hard on the football leather. Your throws sail high over receivers' heads. The great quarterbacks practice box breathing between downs, consciously lowering their heart rate to eighty-five beats per minute so their arm release remains fluid and soft.\n\nIn sports and leadership, you must master your physiology before you can master your performance.\n\nAthletes: Do you know how to breathe down your anxiety in the middle of a high-stakes possession?\n\n👉 Master physiological regulation and competitive poise on and off the field. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#EmotionalPoise #BoxBreathing #HeartRateControl #SurvivalSkillsForAthletes #OlympicSportsScience #LornetteDaye"
    },
    {
        "id": 15,
        "slot": "Wednesday (01:15 PM MDT)",
        "dueAt": "2026-10-21T19:15:00.000Z",
        "assetFile": "mendoza-15.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-15.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "THE BROTHERHOOD IN THE TRENCHES: HONORING THE UNHERALDED WORK. 🛡️🤝\n\nA quarterback is only as clean as the five men battling in front of him.\n\nFernando Mendoza knows that without the left tackle anchoring against a speed rush, or the center snapping the ball in the driving rain, brilliant statistics are impossible. Great quarterbacks take their offensive linemen out to dinner, celebrate their blocks on tape, and acknowledge their bruising sacrifices every single day.\n\nMen: Who are the unheralded contributors in your life who protect your blind side while you receive the credit? Have you expressed your gratitude to them lately?\n\n👉 Build deeper relationships, humility, and steady teamwork across your personal and professional life. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#TheOffensiveLine #BrotherhoodInTheTrenches #GratitudeInLeadership #SurvivalSkillsForMen #MenWhoLead #CoachLornette"
    },
    {
        "id": 16,
        "slot": "Wednesday (03:45 PM MDT)",
        "dueAt": "2026-10-21T21:45:00.000Z",
        "assetFile": "mendoza-16.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-16.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "SCRAMBLING WITH PURPOSE: CREATING OFF-SCHEDULE BRILLIANCE. 🏃‍♂️💨\n\nWhen the called play breaks down, does your mind disintegrate or innovate?\n\nFernando Mendoza does not scramble to pad rushing statistics; he maneuvers within the pocket to buy an extra 1.5 seconds so a broken route can uncover. He keeps two hands on the football, stays balanced on the balls of his feet, and directs traffic downfield with his off-hand. Off-schedule greatness is not chaotic scramble; it is disciplined improvisation.\n\nIn dynamic business landscapes, when market conditions invalidate your business plan, you must improvise with strategic purpose.\n\nLeaders: Can your team pivot off-schedule without losing sight of the strategic target?\n\n👉 Learn how elite athletes adapt under sudden pressure and finish strong. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#OffScheduleGreatness #DisciplinedImprovisation #QuarterbackPlay #FinishStrong #Adaptability #LornetteDaye"
    },
    {
        "id": 17,
        "slot": "Wednesday (05:45 PM MDT)",
        "dueAt": "2026-10-21T23:45:00.000Z",
        "assetFile": "mendoza-17.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-17.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE FOURTH QUARTER TWO-MINUTE DRILL: SEPARATING CONTENDERS FROM PRETENDERS. ⏱️🏆\n\nEighty yards. One timeout. Fifty-eight seconds on the clock. Score or go home.\n\nIn that crucible, tired muscles plead for mercy. The quarterback's mind must remain crystal clear: clock management, sideline throws, taking intermediate yards, knowing when to spike the football, and delivering the walk-off strike in the back corner of the end zone. Games are won by those who preserve cognitive stamina into the dying seconds.\n\nEndurance is not just physical; it is the mental willpower to think clearly when your body is completely spent.\n\nProfessionals: Does your execution hold its crispness at the conclusion of demanding quarters?\n\n👉 Master the mindset of championship finishers who refuse to wilt when the clock winds down. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#TwoMinuteDrill #FourthQuarterFinish #CognitiveStamina #FinishStrong #OlympicStandards #LornetteDaye"
    },
    {
        "id": 18,
        "slot": "Thursday (08:30 AM MDT)",
        "dueAt": "2026-10-22T14:30:00.000Z",
        "assetFile": "mendoza-18.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-18.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "OVERCOMING THE BENCH: REBUILDING YOUR HOPE WHEN YOU ARE NOT CHOSEN. 🪑✨\n\nBeing benched or demoted is one of the most painful psychological wounds an athlete can suffer. You question your identity, your talent, and your worth.\n\nFernando Mendoza experienced chapters where he had to fight from the bottom of the depth chart, competing every day without guarantee of starting. He kept his faith intact, supported the starter, and threw extra passes after practice with student managers. When his opportunity finally arrived, he was undeniable.\n\nIf you feel sidelined in your career or personal journey right now, do not lose heart. Use the quiet season to build character that cannot be shaken.\n\nReaders: What hidden preparation can you invest in today while waiting for your next open door?\n\n👉 Rebuild confidence, find strength in hardship, and step into renewal. Read Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#SurvivingLife #OvercomingTheBench #FaithInTheProcess #PatienceAndResilience #HopeAfterHardship #LornetteDaye"
    },
    {
        "id": 19,
        "slot": "Thursday (11:00 AM MDT)",
        "dueAt": "2026-10-22T17:00:00.000Z",
        "assetFile": "mendoza-19.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-19.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "PURPOSE LIVES HIGHER: THE BLUEPRINT OF ELITE ATHLETIC COMMAND. 🏛️🏈\n\nGreatness is never accidental. It is a mathematical equation of disciplined reps executed with spiritual intentionality.\n\nWhen Fernando Mendoza takes the field, you see the convergence of athletic preparation, family values, and a deep personal sense of purpose. He is not playing for social media clips; he is playing to establish a legacy of excellence that inspires everyone around him.\n\nWhen leaders lead with moral clarity and high technical standards, organizations achieve generational longevity.\n\nExecutives: Is your organization guided by transient market hype, or a higher standard of authentic purpose?\n\n👉 Inspire your executive leadership with keynotes grounded in four decades of championship athletic wisdom. Book Lornette Daye: lornettedaye.com/speaking\n\n#PurposeLivesHigher #FernandoMendoza #EliteCommand #ExecutiveWisdom #HighPerformanceCulture #CoachLornette"
    },
    {
        "id": 20,
        "slot": "Thursday (01:15 PM MDT)",
        "dueAt": "2026-10-22T19:15:00.000Z",
        "assetFile": "mendoza-20.png",
        "assetUrl": "https://lornettedaye.com/campaigns/mendoza/mendoza-20.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE QUARTERBACK LEGACY: PLAYING YOUR BEST WHEN IT MATTERS MOST. 👑🌟\n\nSeasons come and go, but the standard you establish echoes for generations.\n\nFrom high school roots to Division I quarterbacking on national television, the lesson of Fernando Mendoza's journey is clear: stay ready, love your teammates, embrace the crucible of pressure, and never let external circumstances dictate your internal standard of excellence.\n\nIn sports as in life, you will be remembered not for how you started, but for how you finished. Step into the arena with conviction. Honor the reps. Finish strong.\n\n👉 Master the habits and mindset of world-class champions across every field of endeavor. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#TheQuarterbackSeries #FernandoMendoza #FinishStrong #PlayYourBest #OlympicExcellence #LornetteDaye #MasteryInSport"
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
    print("CAMPAIGN 4: MENDOZA - HIGH PERFORMANCE & ELITE FOCUS (20 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "mendoza-scheduled-report.json")
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
    print(f"Summary: {success_count}/20 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
