# -*- coding: utf-8 -*-
"""
Automated Buffer Scheduler for Campaign 1: Vintage NFL (24 Posts)
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
        "slot": "Tuesday (08:30 AM MDT)",
        "dueAt": "2026-10-06T14:30:00.000Z",
        "assetFile": "vintage-nfl-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-01.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "BEFORE PERSONAL BRANDS HAD A NAME, THERE WAS PRIME TIME. ⚡🏈\n\nStyle without substance is an illusion. Substance backed by undeniable mastery changes an entire culture.\n\nLong before modern social media algorithms existed, Deion Sanders walked onto the field with absolute clarity about who he was. The bandana, the gold chains, the high stepping into the end zone. Critics debated the swagger, but opponents feared the preparation. Deion was not an entertainer trying to play corner; he was an elite technician whose preparation allowed him to shut down half the field.\n\nIn four decades of coaching Olympic athletes and champions, I have observed that true confidence never originates from external hype. It is born in the quiet hours when your physical conditioning and technical discipline remove all doubt.\n\nLeaders and athletes: Are you waiting for permission to step into your presence, or is your preparation commanding the room?\n\n👉 Discover how Olympic-level clarity transforms your execution. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#DeionSanders #PrimeTime #HistoricLegends #NFLHeritage #FinishStrong #OlympicDiscipline #LornetteDaye #UnapologeticExcellence"
    },
    {
        "id": 2,
        "slot": "Tuesday (05:45 PM MDT)",
        "dueAt": "2026-10-06T23:45:00.000Z",
        "assetFile": "vintage-nfl-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE DUAL-SPORT STANDARD: MASTERING MULTIPLE ARENAS. ⚾🏈\n\nPlaying NFL football on Sunday and stepping onto a Major League Baseball diamond in the same week requires more than gifted genetics. It requires mental compartmentalization of the highest order.\n\nDeion Sanders did not merely dabble; he competed at the summit of two distinct global sports. To hit a ninety-five mile per hour fastball and tackle world-class receivers demands an athlete whose focus resets to zero on every single play. Your previous error cannot enter the batter's box, just as your previous strikeout cannot follow you onto the football field.\n\nIn my coaching philosophy, we call this the ultimate athletic reset. What happened ten seconds ago has zero power over the next execution.\n\nAthletes: Can your focus transition cleanly between different high-pressure demands without carrying residue?\n\n👉 Strengthen your focus and build a repeatable champion routine on and off the field. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#DualSportExcellence #PrimeTime #MentalReset #FocusUnderPressure #SurvivalSkillsForAthletes #OlympicMindset #LornetteDaye"
    },
    {
        "id": 3,
        "slot": "Wednesday (08:30 AM MDT)",
        "dueAt": "2026-10-07T14:30:00.000Z",
        "assetFile": "vintage-nfl-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "WHEN FOOTBALL FELT DIFFERENT: THE PSYCHOLOGY OF AVOIDANCE. 🛡️🔥\n\nThe greatest statistical mark of an elite shutdown cornerback is not how many interceptions he caught. It is how many times the quarterback looked to his side of the field and refused to throw the ball.\n\nDeion Sanders altered defensive strategy by turning his side of the gridiron into an unoccupied island. Offensive coordinators spent entire game-planning weeks designing plays away from him. That is psychological authority. He eliminated half the opponent's playbook before the opening whistle was blown.\n\nIn executive leadership, when your organization operates with flawless execution and strategic reputation, competitors concede territory before the contest even starts.\n\nExecutives: Is your operational standard dictating the terms of your industry, or are you reacting to market pressure?\n\n👉 Equip your leadership team to command high-stakes arenas with Olympic composure. Book Lornette Daye for executive keynotes: lornettedaye.com/speaking\n\n#TheLegendsSeries #DeionSanders #CornerbackRoyalty #StrategicAuthority #ExecutiveLeadership #CoachLornette #CommandTheRoom"
    },
    {
        "id": 4,
        "slot": "Wednesday (05:45 PM MDT)",
        "dueAt": "2026-10-07T23:45:00.000Z",
        "assetFile": "vintage-nfl-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-04.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "AUTHENTICITY IS A COMPETITIVE ADVANTAGE. 💎🎯\n\nConformity is comfortable, but greatness rarely asks for consensus.\n\nWhen Deion Sanders arrived in professional football, traditionalists urged him to tone down his personality, wear muted colors, and behave like every other player who came before him. Deion understood an essential truth: suppressing your authentic identity to appease the insecure drains your vital energy.\n\nHe poured that energy into his teammates, his preparation, and his performance. He proved that you can be charismatic and disciplined, magnetic and relentless, expressive and profoundly prepared.\n\nMen often struggle with the tension between societal expectations and their authentic drive. When you anchor your self-worth in disciplined preparation, external judgment loses its sting.\n\nMen: Are you shrinking yourself to fit traditional boxes, or owning your God-given presence?\n\n👉 Build emotional resilience, personal clarity, and steady balance in every season of demand. Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #DeionSanders #AuthenticLeadership #Resilience #MenWhoLead #OlympicStandard #LornetteDaye"
    },
    {
        "id": 5,
        "slot": "Thursday (08:30 AM MDT)",
        "dueAt": "2026-10-08T14:30:00.000Z",
        "assetFile": "vintage-nfl-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-05.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "EVERYBODY KNEW 22 WAS GETTING THE BALL. THEY STILL COULDN'T STOP HIM. 🏈🛡️\n\nThere is no deception when your execution is absolute.\n\nIn the 1990s, when the Dallas Cowboys stepped onto the line of scrimmage, every defender, coach, and fan in the stadium knew the football was going to number 22. Emmitt Smith did not rely on trick plays. He lined up seven yards deep, took the handoff, read the crease with surgical vision, and gained five punishing yards.\n\nPlay after play. Game after game. Year after year. Dominance is not about surprising people once; it is about establishing a standard so profound that even when the world knows your strategy, they cannot stop your execution.\n\nLeaders: Is your team relying on gimmicks, or is your fundamental execution so disciplined that results are inevitable?\n\n👉 Learn how to sustain relentless momentum until the finish line is crossed. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#EmmittSmith #Number22 #DallasCowboys #RelentlessStandard #FinishStrong #AllTimeRushingKing #WorkEthic #LornetteDaye"
    },
    {
        "id": 6,
        "slot": "Thursday (05:45 PM MDT)",
        "dueAt": "2026-10-08T23:45:00.000Z",
        "assetFile": "vintage-nfl-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-06.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "18,355 RUSHING YARDS: THE TRIUMPH OF PHYSICAL AND MENTAL DURABILITY. 📈🏔️\n\nThe ultimate athletic metric is availability over decades.\n\nRunning back in the NFL is arguably the most physically punishing position in modern sports. The collisions are violent, the career averages short, and the physical wear immediate. Yet Emmitt Smith accumulated 18,355 rushing yards and 164 touchdowns over fifteen grueling seasons. He accomplished this not by avoiding contact, but by mastering the subtle art of balance, pad level, and year-round recovery.\n\nIn coaching elite sprinters and athletes, I always emphasize that longevity is not luck. It is the daily commitment to sleep, nutrition, mobility, and emotional poise between competitions.\n\nAthletes: Are you prioritizing your recovery as intensely as your competition?\n\n👉 Build the physical resilience and mental systems required for long-term championship execution. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#EmmittSmith #AllTimeRecord #LongevityInSport #PhysicalDurability #SurvivalSkillsForAthletes #OlympicCoach #ConsistencyWins"
    },
    {
        "id": 7,
        "slot": "Friday (08:30 AM MDT)",
        "dueAt": "2026-10-09T14:30:00.000Z",
        "assetFile": "vintage-nfl-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-07.png",
        "cta": "Surviving Life ($14.99 CAD)",
        "text": "THE POWER OF WILL: WHEN THE BODY WANTS TO SURRENDER. ⚔️🏆\n\nJanuary 2, 1994. Giants Stadium. Emmitt Smith suffered a third-degree separated shoulder in the first half of a divisional title clash. Every time his arm was touched, pain shot through his body. Most human beings would have headed straight to the locker room.\n\nEmmitt taped the shoulder, returned to the huddle, and carried the football thirty-two times for 168 yards and caught ten passes. He literally dragged his team to victory with one functional arm.\n\nWe all face chapters in life where our circumstances are painful and our resources feel depleted. In those moments, you do not look at the scoreboard; you look at your purpose and keep taking the next step.\n\nReaders: What weight are you carrying today that requires you to tap into your deepest well of courage?\n\n👉 Find strength, practical encouragement, and perspective when seasons test your resolve. Explore Surviving Life ($14.99 CAD): lornettedaye.com/books\n\n#EmmittSmith #UnstoppableWill #Perseverance #SurvivingLife #OvercomingPain #CourageUnderPressure #LornetteDaye"
    },
    {
        "id": 8,
        "slot": "Friday (05:45 PM MDT)",
        "dueAt": "2026-10-09T23:45:00.000Z",
        "assetFile": "vintage-nfl-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "CONSISTENCY WINS: SAME NUMBER. A HIGHER STANDARD. 🏛️🌟\n\nBrilliance sparkles, but consistency builds empires.\n\nEleven consecutive seasons with over 1,000 rushing yards. Three Super Bowl rings. One Super Bowl MVP. Emmitt Smith never chased viral attention or unnecessary theatrics. He arrived at the facility before sunrise, studied defensive fronts with his offensive linemen, and executed his assignment.\n\nIn business as in sports, the companies that dominate over decades are not the ones with one lucky quarter. They are the organizations that deliver repeatable excellence day after day, regardless of weather or fatigue.\n\nExecutives: Have you built a culture where consistency is celebrated as the highest virtue?\n\n👉 Transform your leadership culture with Olympic principles of operational stamina and team accountability. Book Lornette Daye: lornettedaye.com/speaking\n\n#ConsistencyWins #Emmitt22 #CowboysDynasty #ExecutivePerformance #HighStandards #CoachLornette #OperationalExcellence"
    },
    {
        "id": 9,
        "slot": "Saturday (08:30 AM MDT)",
        "dueAt": "2026-10-10T14:30:00.000Z",
        "assetFile": "vintage-nfl-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-09.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE STANDARD DIDN'T NEED TO SHOUT. GREATNESS SPOKE THROUGH RESULTS. 🤫🏈\n\nThe loudest person in the room is rarely the most prepared.\n\nJerry Rice did not conduct himself with theatrical boasts. He did not need to. When you hold the records for 1,549 receptions, 22,895 receiving yards, and 208 total touchdowns, your work speaks with deafening volume. Every pattern he ran was drawn with mathematical precision. Every catch tucked smoothly into his frame. Every block downfield executed as if the championship depended on it.\n\nIn Olympic athletics, we teach that quiet competence commands greater long-term respect than loud posturing. Let your discipline be your loudest statement.\n\nAthletes and professionals: Are you spending energy broadcasting your intentions, or proving your standard through performance?\n\n👉 Master the mindset of elite finishers who let results define their legacy. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#JerryRice #SanFrancisco49ers #TheStandard #FinishStrong #QuietConfidence #OlympicMindset #ResultsSpeak #CoachLornette"
    },
    {
        "id": 10,
        "slot": "Saturday (03:45 PM MDT)",
        "dueAt": "2026-10-10T21:45:00.000Z",
        "assetFile": "vintage-nfl-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-10.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "THE LEGEND OF 'THE HILL': OUTWORKING THE WORLD IN THE OFFSEASON. ⛰️🏃‍♂️\n\nSuper Bowls are celebrated under stadium lights, but they are won on remote dirt trails in July.\n\nEvery summer, Jerry Rice retreated to the punishing hills of San Carlos, California. A grueling two-and-a-half-mile trail with a steep forty-five-degree incline at the summit. Dozens of elite NFL players attempted to train with him over the years. Most vomited and quit before reaching the top. Rice ran it repeatedly, sprint after sprint, until his lungs burned and his legs shook.\n\nHe ran the hill because he knew that in the fourth quarter of a January playoff game, no defensive back on earth could match his cardiovascular conditioning.\n\nAthletes: What is your personal 'Hill' that gives you an unshakeable edge when competition gets fierce?\n\n👉 Build relentless conditioning and the mental toughness of an elite champion. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#JerryRice #TheHill #Conditioning #NoShortcuts #SurvivalSkillsForAthletes #OlympicDiscipline #LornetteDaye"
    },
    {
        "id": 11,
        "slot": "Saturday (05:45 PM MDT)",
        "dueAt": "2026-10-10T23:45:00.000Z",
        "assetFile": "vintage-nfl-11.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-11.png",
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": "ROUTE-RUNNING PRECISION: TURNING FOOTBALL INTO GEOMETRY. 📐🎯\n\nSpeed is an asset, but precision is lethal.\n\nJerry Rice did not run a 4.3 forty-yard dash at the NFL combine. He ran a 4.6. Yet cornerbacks who ran 4.2 could never keep up with him out of his breaks. Why? Because Rice eliminated every fraction of wasted motion. His stem was identical on every play. His head didn't drop before a cut. His footwork hit the exact blade of grass dictated by the play call.\n\nWhen you master technical precision, you do not need raw physical advantages to dominate your field. You create separation through superior discipline and economy of movement.\n\nProfessionals: Where in your daily work are you relying on frantic hustle instead of surgical precision?\n\n👉 Move beyond just getting by and step into a life of purpose-driven mastery. Read Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n#PrecisionCraft #JerryRice #RouteRunning #Mastery #SurvivingToThriving #HighPerformance #LornetteDaye"
    },
    {
        "id": 12,
        "slot": "Sunday (08:30 AM MDT)",
        "dueAt": "2026-10-11T14:30:00.000Z",
        "assetFile": "vintage-nfl-12.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-12.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "PLAYING AT AGE 40: REJECTING THE EXPIRATION DATE. ⏳🔥\n\nAt age 40, Jerry Rice caught 92 passes for 1,211 yards and seven touchdowns with the Oakland Raiders. Wide receivers in their twenties were marveling at his body fat percentage, his burst off the line, and his relentless motor.\n\nRice proved that when an athlete treats his body like a high-performance instrument, the biological clock bends. He did not drink alcohol during the season. He maintained strict hydration and flexibility routines before physical therapy was an industry buzzword.\n\nMen: Aging is inevitable, but decay is largely a choice of discipline. What habits are you protecting today to ensure you thrive twenty years from now?\n\n👉 Rebuild your foundation, sustain physical vitality, and balance pressure across every stage of manhood. Explore Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #JerryRice #Longevity #DisciplineOverDecay #MenWhoLead #OlympicCoaching #CoachLornette"
    },
    {
        "id": 13,
        "slot": "Sunday (03:45 PM MDT)",
        "dueAt": "2026-10-11T21:45:00.000Z",
        "assetFile": "vintage-nfl-13.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-13.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE HANDS OF A BRICKLAYER'S SON: ROOTS OF PERFECTION. 🧱🤲\n\nLong before catching passes from Joe Montana and Steve Young, young Jerry Rice spent scorching Mississippi summers working for his father as a bricklayer. His brother would stand on the scaffolding and throw red clay bricks from twenty feet away. Jerry had to catch them barehanded. If you drop a brick, it shatters, or it breaks your nose.\n\nThat pressure taught Rice to look every ball into his fingertips with intense concentration. By the time a football was thrown his way in the fourth quarter of the Super Bowl, it felt as soft as a pillow.\n\nYour early hardships are not your handicap; they are your secret training ground for greatness.\n\nLeaders: What past obstacle gave you the resilience that now sets you apart?\n\n👉 Harness your history and learn how to finish with undeniable purpose. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#JerryRice #BricklayersSon #OriginStory #FinishStrong #HardshipBuildsResilience #OlympicMindset #LornetteDaye"
    },
    {
        "id": 14,
        "slot": "Sunday (05:45 PM MDT)",
        "dueAt": "2026-10-11T23:45:00.000Z",
        "assetFile": "vintage-nfl-14.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-14.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "SOME PLAYED THE GAME. HE DEFINED IT. 🏆✨\n\nA standard is not something you achieve; it is something you inhabit.\n\nJerry Rice did not take plays off during Tuesday morning walkthroughs. Whenever he caught a pass in practice, even if the whistle blew twenty yards back, he sprinted sixty yards all the way to the end zone and touched the goalpost. Every single rep.\n\nTeammates joked at first, but soon they realized: Rice was conditioning his subconscious brain that the only acceptable conclusion to touching a football was crossing the goal line.\n\nIn your organization, do your employees complete their tasks half-heartedly, or do they finish every repetition through the goal line?\n\n👉 Elevate your team's operational habits to championship standards with Olympic-level executive coaching. Book Lornette Daye: lornettedaye.com/speaking\n\n#JerryRice #ChampionshipHabits #FinishTheRep #ExecutiveCoaching #OlympicStandards #LornetteDaye #LeadershipExcellence"
    },
    {
        "id": 15,
        "slot": "Monday (08:30 AM MDT)",
        "dueAt": "2026-10-12T14:30:00.000Z",
        "assetFile": "vintage-nfl-15.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-15.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "PRESSURE DISAPPEARS WHEN YOUR PREPARATION IS INEVITABLE. 🌪️🎯\n\nPressure is merely the shadow cast by unpreparedness.\n\nJerry Rice caught 11 passes for 215 yards in Super Bowl XXIII, earning MVP honors in one of the most pressurized sporting events on earth. When reporters asked him how he handled the nerve-shredding anxiety of the Super Bowl stage, his response was simple: 'I've already run these routes three thousand times this year alone. Today was just the test.'\n\nWhen you repeat your craft with obsessive discipline in the dark, the lights of the championship stage cannot blind you.\n\nAthletes: Are you relying on emotional adrenaline on game day, or an iron foundation of reps?\n\n👉 Build the unshakable mental routines that keep you calm when the stakes are highest. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#PressureIsAPrivilege #JerryRice #SuperBowlMVP #PreparationIsEverything #SurvivalSkillsForAthletes #OlympicCoach #LornetteDaye"
    },
    {
        "id": 16,
        "slot": "Monday (03:45 PM MDT)",
        "dueAt": "2026-10-12T21:45:00.000Z",
        "assetFile": "vintage-nfl-16.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-16.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "A HIGHER FORM OF CONSISTENCY: 20 SEASONS OF SUPREMACY. 🌟🏈\n\nIt is relatively easy to be great for one season. Anyone with talent and fresh legs can produce a memorable campaign.\n\nThe true test of human mastery is whether you can return year after year, with a target on your back, facing younger, faster defenders designed specifically to stop you, and still lead the league in receiving. Jerry Rice was first-team All-Pro in three different decades: the 1980s, the 1990s, and the 2000s.\n\nThat is not athletic luck. That is an Olympic commitment to physical preservation and mental hunger.\n\nLeaders: Is your vision designed for a brief sprint, or built for multi-decade relevance?\n\n👉 Discover how to sustain endurance across long career horizons. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#JerryRice #ThreeDecadesOfGreatness #EnduringLegacy #FinishStrong #OlympicStandards #LornetteDaye #ConsistencyOverHype"
    },
    {
        "id": 17,
        "slot": "Monday (05:45 PM MDT)",
        "dueAt": "2026-10-12T23:45:00.000Z",
        "assetFile": "vintage-nfl-17.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-17.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THEY CALLED HIM THE PLAYMAKER. THEN HE KEPT PROVING WHY. 💥⭐\n\nSome players make plays. Others manufacture moments that shift the emotional tide of a franchise.\n\nMichael Irvin was the fiery heartbeat of the 1990s Dallas Cowboys dynasty. When the offense faced third down and twelve in freezing weather with a defender draped all over his back, number 88 looked at Troy Aikman, tapped his chest, and demanded the ball. He did not shy away from the spotlight; he welcomed the burden of victory.\n\nIn four decades coaching Canadian national champions, I know that championship teams require at least one leader who genuinely craves the responsibility of the decisive moment.\n\nLeaders: When the outcome is on the line, does your team look for excuses, or demand the ball?\n\n👉 Learn how to cultivate unwavering clutch confidence under extreme pressure. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#MichaelIrvin #ThePlaymaker #DallasCowboys #88Club #FinishStrong #ClutchPerformance #OlympicMindset #LornetteDaye"
    },
    {
        "id": 18,
        "slot": "Tuesday (08:30 AM MDT)",
        "dueAt": "2026-10-13T14:30:00.000Z",
        "assetFile": "vintage-nfl-18.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-18.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "ENERGY IS CONTAGIOUS: IGNITING A LOCKER ROOM. 🔥🏟️\n\nTactical schemes don't win championships unless they are fueled by genuine emotional conviction.\n\nMichael Irvin practiced with the exact same ferocious intensity he displayed on Sunday afternoon. He celebrated routine completions in August training camp as if they were Super Bowl touchdowns. He challenged cornerbacks in practice until tempers flared, and then embraced them afterward. He set the emotional thermostat of the entire building. You could not be around Michael Irvin and remain lukewarm.\n\nAthletes: Are you draining energy from your teammates, or supplying the competitive fire that lifts the standard?\n\n👉 Build champion communication, presence, and emotional fire on and off the field. Read Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#MichaelIrvin #EmotionalLeadership #CompetitiveFire #TeamCulture #SurvivalSkillsForAthletes #OlympicCoach #LornetteDaye"
    },
    {
        "id": 19,
        "slot": "Tuesday (11:00 AM MDT)",
        "dueAt": "2026-10-13T17:00:00.000Z",
        "assetFile": "vintage-nfl-19.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-19.png",
        "cta": "Survival Skills for Men ($14.99 CAD)",
        "text": "IMPOSING YOUR WILL AT THE CATCH POINT. 💪🏈\n\nIn elite sport, space is rarely given. It must be claimed with physical authority.\n\nAt 6 foot 2 and 210 pounds, Michael Irvin revolutionized the wide receiver position by introducing physical ferocity to route running. He used his body to box out cornerbacks like a rebounder on the hardwood. He attacked 50-50 balls with violent hands and complete conviction that every ball in the air belonged to him.\n\nMen often hesitate when confronted with aggressive resistance in their careers or personal challenges. When you hesitate, you surrender leverage. When you commit fully, obstacles move.\n\nMen: Are you hesitating at the point of contact in your life, or stepping forward with decisive authority?\n\n👉 Strengthen your emotional resilience and decisive leadership habits. Read Survival Skills for Men ($14.99 CAD): lornettedaye.com/books\n\n#SurvivalSkillsForMen #MichaelIrvin #DecisiveAction #PhysicalAuthority #MenWhoLead #OlympicStandard #LornetteDaye"
    },
    {
        "id": 20,
        "slot": "Tuesday (01:15 PM MDT)",
        "dueAt": "2026-10-13T19:15:00.000Z",
        "assetFile": "vintage-nfl-20.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-20.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": "GREATNESS LOOKED GOOD IN SILVER AND BLUE. 🏆⭐\n\nThree Super Bowl championships in four years was not an accident of talent. It was the product of ruthless accountability.\n\nJimmy Johnson and Michael Irvin established a culture in Dallas where mistakes were not brushed aside. Stars were held to a higher standard than rookies. Irvin demanded perfection from Aikman, and Aikman demanded perfection from Irvin. They loved each other enough to confront each other with honesty.\n\nIn high-performance organizations, harmony is not the absence of tension. Harmony is the shared commitment to winning that makes constructive confrontation productive.\n\nExecutives: Does your culture encourage radical accountability, or polite mediocrity?\n\n👉 Coach your executive team to build a dynasty of accountability and high execution. Book Lornette Daye for keynotes and executive strategy: lornettedaye.com/speaking\n\n#DallasDynasty #MichaelIrvin #ChampionshipCulture #ExecutiveLeadership #Accountability #CoachLornette #CommandTheField"
    },
    {
        "id": 21,
        "slot": "Tuesday (03:45 PM MDT)",
        "dueAt": "2026-10-13T21:45:00.000Z",
        "assetFile": "vintage-nfl-21.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-21.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE LEGENDS SERIES: WHY WE MUST REMEMBER THE GIANTS. 🏛️🏈\n\nA generation that forgets its heritage will inevitably lower its standard.\n\nWhen we study Deion Sanders, Emmitt Smith, Jerry Rice, and Michael Irvin, we are not simply admiring vintage highlights. We are studying the foundational architecture of modern athletic greatness. These legends competed before high-tech recovery chambers and multi-million-dollar training apps existed. They dominated through sheer willpower, relentless tape study, and an unshakeable pride in their craft.\n\nIn my coaching work with Olympic champions, I remind young athletes that their opportunity was bought by the sweat of those who ran before them.\n\nAthletes and leaders: Are you honoring the standard set by the pioneers of your field?\n\n👉 Anchor your ambitions in timeless principles of grit, purpose, and legacy. Explore Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#TheLegendsSeries #GridironHeritage #NFLHistory #FinishStrong #TimelessExcellence #OlympicCoach #LornetteDaye"
    },
    {
        "id": 22,
        "slot": "Tuesday (05:45 PM MDT)",
        "dueAt": "2026-10-13T23:45:00.000Z",
        "assetFile": "vintage-nfl-22.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-22.png",
        "cta": "Survival Skills: Surviving to Thriving ($14.99 CAD)",
        "text": "THE RIVALRY OF GIANTS: WHEN EXCELLENCE PUSHED EXCELLENCE. ⚔️🏆\n\nYou cannot become your absolute best without an opponent who pushes you to the brink.\n\nThe NFC Championship battles between the San Francisco 49ers and the Dallas Cowboys in the 1990s were more than football games. They were masterclasses in competitive pressure. Jerry Rice on one sideline, Michael Irvin and Emmitt Smith on the other, and Deion Sanders switching sides to chase another ring. Neither team could afford a single mental lapse, because the opponent was flawless.\n\nStop complaining about fierce competition in your industry. Thank your rivals for forcing you to eliminate your weaknesses.\n\nLeaders: Is your competition exposing your vulnerabilities, or sharpening your execution?\n\n👉 Move beyond survival mode and turn market pressure into fuel for long-term growth. Read Survival Skills: Surviving to Thriving ($14.99 CAD): lornettedaye.com/books\n\n#49ersVsCowboys #EpicRivalries #IronSharpensIron #SurvivingToThriving #HighStakesCompetition #LornetteDaye"
    },
    {
        "id": 23,
        "slot": "Wednesday (08:30 AM MDT)",
        "dueAt": "2026-10-14T14:30:00.000Z",
        "assetFile": "vintage-nfl-23.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-23.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD)",
        "text": "LEGACY LIVES ON: DEFINING YOUR IDENTITY BEYOND THE UNIFORM. 🌟🏈\n\nThe uniform comes off for every athlete eventually. What remains is your character.\n\nWhat makes Deion Sanders, Emmitt Smith, Jerry Rice, and Michael Irvin immortal is not just their hall of fame rings. It is how they transitioned their athletic discipline into business, coaching, broadcasting, and community leadership. They proved that the mental fortitude forged on the gridiron is transferable to every arena of life.\n\nAt Lornette Daye Athletics, our first Foundation is 'Identity Beyond Sport.' When you know who you are without the jersey, you play with total freedom on the field and total poise off it.\n\nAthletes: Have you built a foundation that will stand long after your competitive career concludes?\n\n👉 Build a champion mindset and lifelong identity that transcends the game. Explore Survival Skills for Athletes ($14.99 CAD): lornettedaye.com/books\n\n#IdentityBeyondSport #LifeAfterFootball #TheLegendsSeries #SurvivalSkillsForAthletes #OlympicPhilosophy #LornetteDaye"
    },
    {
        "id": 24,
        "slot": "Wednesday (11:00 AM MDT)",
        "dueAt": "2026-10-14T17:00:00.000Z",
        "assetFile": "vintage-nfl-24.png",
        "assetUrl": "https://lornettedaye.com/campaigns/vintage-nfl/vintage-nfl-24.png",
        "cta": "Finish Strong Book ($14.99 CAD)",
        "text": "THE VINTAGE STANDARD: UNCOMPROMISING WORK OVER TIME. 🏛️👑\n\nEras change. Rules evolve. Technology advances. But the fundamental law of greatness remains unyielding.\n\nYou cannot fake twenty years of dominance like Jerry Rice. You cannot fake eighteen thousand yards of punishment like Emmitt Smith. You cannot fake two-sport swagger like Deion Sanders. You cannot fake third-down heart like Michael Irvin.\n\nThey stood the test of time because they honored the unglamorous details of the daily grind. They showed up when nobody was watching, worked when they didn't feel like it, and finished what they started.\n\nWhatever your arena is today, take a page from the legends: raise your standard, silence the noise, and finish strong.\n\n👉 Step into your greatness with Olympic principles of perseverance and purpose. Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): lornettedaye.com/books\n\n#VintageNFL #HistoricLegends #FinishStrong #GridironHeritage #NoExcuses #OlympicMindset #LornetteDaye #MasteryInAction"
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
    print("CAMPAIGN 1: VINTAGE NFL - HISTORIC GRIDIRON LEGENDS & HERITAGE (24 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    report_path = os.path.join(os.path.dirname(__file__), "vintage-nfl-scheduled-report.json")
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

    for idx, post in enumerate(posts_data[:1], 1):
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
    print(f"Summary: {success_count}/24 posts scheduled successfully.")
    print("=" * 75)

if __name__ == "__main__":
    main()
