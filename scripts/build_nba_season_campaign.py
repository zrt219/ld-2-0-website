import json
import os
from datetime import datetime, timezone, timedelta

# Production Base URL
BASE_IMG_URL = "https://lornettedaye.com/campaigns/nba-season-start"

# 21-Day Schedule Matrix
# Day 1: Oct 23, 2026 at 10:00 PM MDT (UTC-6) -> 04:00 UTC Oct 24
# Days 2-21: Oct 24 - Nov 13, 2026 at 6:30 PM EDT (UTC-4) -> 22:30 UTC same day
# Note: Daylight saving time ends on Sunday Nov 1, 2026!
# From Nov 1 onwards, standard time is EST (UTC-5), so 6:30 PM EST -> 23:30 UTC.
# Let's ensure accurate UTC timestamps for 6:30 PM Eastern Time.

posts_data = [
    {
        "day": 1,
        "date_str": "2026-10-23T22:00:00-06:00", # 10:00 PM MDT
        "image": "01_week_one_championships.png",
        "title": "WEEK ONE: AND WE ARE ALREADY TALKING CHAMPIONSHIPS",
        "caption": """WEEK ONE: AND WE ARE ALREADY TALKING CHAMPIONSHIPS.

The NBA season has barely tipped off, and the national conversation has already jumped straight to June.

We see Anthony Edwards setting an electric tone in Minnesota. We see LaMelo Ball creating immediate chemistry. We see Giannis beginning an intense new chapter in Miami, and Kawhi Leonard once again wearing Toronto across his chest.

As an Olympic-level coach and former national champion, I have seen this phenomenon across every elite discipline. Opening week brings raw adrenaline and headline hype. But championships are never won on opening night.

Championship teams are built in the untelevised hours. They are forged through communication when sets break down, mutual trust when shots do not fall, and emotional poise through November and January road trips.

Talent opens the door. Repeatable habits, emotional regulation, and locker room trust determine who is still standing when the trophy enters the arena.

Which team or player has made the strongest opening statement so far?

Explore how elite athletes and high-performing organizations build championship foundations that endure pressure:
https://lornettedaye.com/foundations

#NBA #NBATipOff #HEATCulture #WolvesBack #WeTheNorth #BetterPeopleBetterPlayers #LornettesFoundations #ExecutiveLeadership #AthleteDevelopment"""
    },
    {
        "day": 2,
        "date_str": "2026-10-24T18:30:00-04:00", # 6:30 PM EDT
        "image": "raptors_01_vince_carter.png",
        "title": "LEGEND SPOTLIGHT: VINCE CARTER AND THE POWER OF BELIEF",
        "caption": """LEGEND SPOTLIGHT: VINCE CARTER AND THE POWER OF BELIEF.

Before a franchise can win, it has to believe it belongs on the map.

In the late 1990s, Canadian basketball needed a cultural earthquake. Vince Carter did not just provide world-class athleticism and highlight-reel dunks. He gave an entire country permission to believe that world-class basketball excellence lived north of the border.

In high-performance coaching, we call this the catalyst phase. One individual with transcendent courage and undeniable belief can alter the psychological ceiling of an entire organization.

Carter proved that Canadian arenas could roar with the loudest in the league. That belief inspired a generation of Canadian youth who now dominate rosters across the NBA.

Belief is contagious. When an elite performer steps into their authentic power, they expand what everyone around them believes is possible.

What was your favorite Vince Carter memory in Toronto?

Learn how we train athletes to build unshakable self-belief and cultural leadership:
https://lornettedaye.com/foundations

#WeTheNorth #VinceCarter #HalfManHalfAmazing #TorontoRaptors #NBALegends #BetterPeopleBetterPlayers #LornettesFoundations #AthleteDevelopment #ChampionMindset"""
    },
    {
        "day": 3,
        "date_str": "2026-10-25T18:30:00-04:00", # 6:30 PM EDT
        "image": "02_miami_heat_starting_five.png",
        "title": "FIVE NAMES. ONE BIG EXPECTATION. MIAMI HEAT STARTING FIVE",
        "caption": """FIVE NAMES. ONE BIG EXPECTATION. MIAMI HEAT STARTING FIVE.

Giannis. Bam Adebayo. Klay Thompson. Andrew Wiggins. Donovan Mitchell.

On paper, this lineup looks like an all-star roster constructed in a basketball simulator. But in the NBA, names on a whiteboard do not win basketball games. Shared execution and role clarity do.

When elite competitors assemble in Miami, they enter a system defined by conditioning, defensive discipline, and complete accountability. Having five prolific scorers means nothing if players do not accept the invisible work: boxing out, making the extra pass, rotating on defense, and communicating through fatigue.

In my 40-plus years coaching elite athletes, I have watched super-teams fracture when individual egos refused to yield. And I have watched championship units thrive when star athletes embraced being world-class in their defensive habits and unselfish in the clutch.

Can this Miami group merge their individual greatness into championship execution?

Discover the systems behind team cohesion and elite performance under pressure:
https://lornettedaye.com/foundations

#HEATCulture #MiamiHEAT #Giannis #BamAdebayo #KlayThompson #DonovanMitchell #NBA #TeamCohesion #LornettesFoundations #BetterPeopleBetterPlayers"""
    },
    {
        "day": 4,
        "date_str": "2026-10-26T18:30:00-04:00", # 6:30 PM EDT
        "image": "raptors_02_kyle_lowry.png",
        "title": "LEGEND SPOTLIGHT: KYLE LOWRY AND THE HEART OF A CHAMPION",
        "caption": """LEGEND SPOTLIGHT: KYLE LOWRY AND THE HEART OF A CHAMPION.

The stat sheet will never tell you the full truth about Kyle Lowry.

Lowry is the undisputed heartbeat of Toronto Raptors history not because of scoring averages, but because of his willingness to do everything other players avoid. Taking charges with five seconds on the clock, diving onto hardwood for loose balls, directing traffic, and absorbing pressure for his teammates.

In elite sports, every championship roster requires an emotional anchor. Someone whose standard of effort is so high and uncompromising that no teammate dares to take a play off.

Lowry demonstrated that true leadership is demonstrated through sacrifice. You earn your locker room respect not by what you say in press conferences, but by the physical and mental battles you fight for your team when nobody is cheering.

That relentless will is what brought the Larry O'Brien trophy to Toronto in 2019.

What made Kyle Lowry the quintessential leader of the Raptors franchise?

Explore how to develop leadership presence and relentless competitive character:
https://lornettedaye.com/foundations

#WeTheNorth #KyleLowry #NorthOverEverything #RaptorsNation #LeadershipInAction #BetterPeopleBetterPlayers #LornettesFoundations #EmotionalPoise #ChampionStandards"""
    },
    {
        "day": 5,
        "date_str": "2026-10-27T18:30:00-04:00", # 6:30 PM EDT
        "image": "03_minnesota_wolves_starting_five.png",
        "title": "MINNESOTA MEANS BUSINESS: SPEED, LENGTH, AND RELENTLESS ENERGY",
        "caption": """MINNESOTA MEANS BUSINESS: SPEED, LENGTH, AND RELENTLESS ENERGY.

Anthony Edwards. LaMelo Ball. Jaden McDaniels. Jonathan Kuminga. Rudy Gobert.

The Minnesota Timberwolves have assembled one of the most explosive, versatile, and athletically imposing starting units in modern basketball. Speed on the perimeter, elite rim protection, and relentless transition firepower.

Yet physical superiority only carries a team so far in a demanding 82-game schedule.

The true test for this Minnesota group is emotional consistency. When young, dynamic talents play with freedom and joy, they are nearly impossible to guard. But championship teams must also master the slow, gritty, half-court execution required in fourth quarters when defensive intensity peaks.

As a coach, when you have this level of talent, the secret is teaching them to love the process of defense as much as they love the highlight reels.

How far can this Minnesota lineup go if their chemistry matches their athletic ceiling?

Discover our high-performance frameworks for maintaining competitive focus:
https://lornettedaye.com/foundations

#WolvesBack #Timberwolves #AnthonyEdwards #LaMeloBall #RudyGobert #NBA #AthleticExcellence #LornettesFoundations #BetterPeopleBetterPlayers #FocusUnderPressure"""
    },
    {
        "day": 6,
        "date_str": "2026-10-28T18:30:00-04:00", # 6:30 PM EDT
        "image": "raptors_03_demar_derozan.png",
        "title": "LEGEND SPOTLIGHT: DEMAR DEROZAN AND RELENTLESS CRAFTSMANSHIP",
        "caption": """LEGEND SPOTLIGHT: DEMAR DEROZAN AND RELENTLESS CRAFTSMANSHIP.

"Don't worry, I got us."

When Chris Bosh departed in 2010, DeMar DeRozan sent a single message that defined a decade of Toronto basketball. And then, he went to work.

Every single summer, DeRozan returned to Toronto with a new weapon. Better footwork, an unguardable mid-range pull-up, improved playmaking, and tighter handles. He did not rely on shortcuts or trends. He honored the timeless craftsmanship of the game.

Equally powerful was his courage off the court. DeMar was one of the first global superstars to speak openly about mental health and vulnerability, showing that being strong does not mean suppressing your humanity.

Loyalty, work ethic, and authentic courage. That is how legacy is built.

What lesson from DeMar DeRozan's journey in Toronto has stayed with you most?

Learn how we help elite performers master their craft and emotional resilience:
https://lornettedaye.com/foundations

#WeTheNorth #DeMarDeRozan #CompeteEveryDay #Mastery #MentalHealthInSports #BetterPeopleBetterPlayers #LornettesFoundations #ResilienceAfterSetback #WorkEthic"""
    },
    {
        "day": 7,
        "date_str": "2026-10-29T18:30:00-04:00", # 6:30 PM EDT
        "image": "04_timberwolves_brotherhood.png",
        "title": "THAT IS MY BROTHER: TWO STARS, ONE TEAM, AND UNBREAKABLE TRUST",
        "caption": """THAT IS MY BROTHER: TWO STARS, ONE TEAM, AND UNBREAKABLE TRUST.

Anthony Edwards and LaMelo Ball. Two generational guards sharing one backcourt.

In sports media, people often wonder if two dominant personalities can coexist. Will there be jealousy over shots? Who takes the final shot? Who commands the spotlight?

True greatness answers those questions before they are even asked. When mutual respect and authentic brotherhood exist between teammates, competition turns inward toward opponents, not sideways against each other.

As an Olympic-level coach, I have seen partnerships achieve immortality only when both competitors realize that their partner's success amplifies their own. When Edwards celebrates LaMelo's vision, and LaMelo sets up Edwards in transition, the entire locker room feels that unity.

Locker room trust is not an accident. It is built through daily conversations, shared laughter, and holding each other to championship standards.

What makes an elite backcourt partnership truly unguardable?

Learn how we cultivate trust, cohesion, and elite team dynamics:
https://lornettedaye.com/foundations

#WolvesBack #AnthonyEdwards #LaMeloBall #Brotherhood #TeamDynamics #NBA #LockerRoomCulture #BetterPeopleBetterPlayers #LornettesFoundations #CommunicationAndPresence"""
    },
    {
        "day": 8,
        "date_str": "2026-10-30T18:30:00-04:00", # 6:30 PM EDT
        "image": "raptors_04_kawhi_leonard.png",
        "title": "LEGEND SPOTLIGHT: KAWHI LEONARD AND PEAK EMOTIONAL POISE",
        "caption": """LEGEND SPOTLIGHT: KAWHI LEONARD AND PEAK EMOTIONAL POISE.

One season. One mission. One historic championship.

In 2019, Kawhi Leonard gave the sports world a masterclass in emotional poise and high-stakes execution. Regardless of whether the Raptors were up by twenty or down by ten, his demeanor remained entirely undisturbed.

His famous Game 7 game-winner against Philadelphia was the culmination of thousands of hours of mental preparation. In that split second when the ball bounced four times on the rim, the entire continent held its breath. Kawhi stood crouched, centered in complete presence.

In the Performance Edge Framework, we teach that your previous shot cannot hit your next shot. When you disconnect your identity from past mistakes or future anxiety, you unlock your highest level of performance under extreme pressure.

Kawhi brought championship calm to Toronto, and the city will never forget it.

How did Kawhi Leonard's quiet composure impact your view of athletic leadership?

Discover how we train athletes and executives in emotional regulation and reset routines:
https://lornettedaye.com/foundations

#WeTheNorth #KawhiLeonard #TheShot #NBAChampions2019 #EmotionalPoise #ExecutionUnderPressure #BetterPeopleBetterPlayers #LornettesFoundations #PeakPerformance"""
    },
    {
        "day": 9,
        "date_str": "2026-10-31T18:30:00-04:00", # 6:30 PM EDT
        "image": "05_toronto_raptors_return.png",
        "title": "THE RETURN. THE EXPECTATIONS. THE FUTURE. TORONTO RAPTORS",
        "caption": """THE RETURN. THE EXPECTATIONS. THE FUTURE. TORONTO RAPTORS.

Immanuel Quickley. RJ Barrett. Kawhi Leonard. Scottie Barnes. Jakob Poeltl.

The energy inside Scotiabank Arena is unmistakable. The reunion of championship pedigree with hungry Canadian talent and modern two-way versatility has ignited Toronto once again.

This lineup brings an exceptional blend of experiences. Kawhi provides proven championship calm. RJ Barrett brings Canadian pride and attacking rim pressure. Scottie Barnes represents the multi-dimensional future of positionless basketball, while Quickley and Poeltl provide floor spacing and defensive rim integrity.

The challenge for Toronto this season is connecting these generational timelines. Veterans must mentor without stifling young initiative. Young stars must lead with humility while asserting their competitive will.

When youth embraces veteran wisdom, special seasons happen.

What is the ceiling for this Toronto Raptors starting five this season?

Learn more about bridging veteran leadership with emerging talent:
https://lornettedaye.com/foundations

#WeTheNorth #TorontoRaptors #ScottieBarnes #RJBarrett #KawhiLeonard #NBATipOff #RaptorsNation #BetterPeopleBetterPlayers #LornettesFoundations #TeamLeadership"""
    },
    {
        "day": 10,
        "date_str": "2026-11-01T18:30:00-05:00", # 6:30 PM EST (UTC-5)
        "image": "raptors_05_chris_bosh.png",
        "title": "LEGEND SPOTLIGHT: CHRIS BOSH AND ANCHORING A FRANCHISE",
        "caption": """LEGEND SPOTLIGHT: CHRIS BOSH AND ANCHORING A FRANCHISE.

Carrying the weight of a franchise as a young big man requires extraordinary maturity.

When Chris Bosh became the focal point of the Toronto Raptors, he brought grace, relentless rebounding, and an ahead-of-his-time face-up game that paved the way for modern stretch bigs. Night after night, he showed up and competed against the league's fiercest frontcourts.

In elite athletic development, we evaluate athletes not only on their talent, but on their professional dependability. Can your coaching staff and teammates count on your effort every single evening, regardless of circumstances?

Bosh answered that call with five consecutive All-Star selections in Toronto, playing with dignity, intelligence, and an unwavering commitment to his teammates.

He laid a foundation of professionalism that helped the Raptors establish permanent respect across the NBA.

What is your defining memory of Chris Bosh leading the Toronto frontcourt?

Explore our frameworks for building athlete consistency and professional habits:
https://lornettedaye.com/foundations

#WeTheNorth #ChrisBosh #CB4 #TorontoRaptors #HallOfFame #Consistency #BetterPeopleBetterPlayers #LornettesFoundations #AthleteDevelopment #ProfessionalStandards"""
    },
    {
        "day": 11,
        "date_str": "2026-11-02T18:30:00-05:00", # 6:30 PM EST
        "image": "06_talent_wins_trust_builds.png",
        "title": "TALENT WINS GAMES. TRUST BUILDS TEAMS",
        "caption": """TALENT WINS GAMES. TRUST BUILDS TEAMS.

Anthony Edwards and LaMelo Ball have started their partnership with an unmistakable statement.

Highlight plays fill social media feeds and ignite home crowds. But championship teams are built through thousands of moments that never appear in the box score:
- Communication on defensive switches.
- Immediate encouragement after a missed shot.
- Shared accountability when the whistle does not blow.
- Willingness to celebrate another man's scoring run.

In my four decades coaching Olympic athletes, the biggest differentiator between podium finishers and early exits has never been physical ability. It is trust.

When athletes trust their coach, their system, and their teammates, hesitation vanishes. They play fast, decisive, and fearless.

What matters more for a championship backcourt: individual talent or mutual chemistry?

Learn how we train teams to build unbreakable locker room trust and alignment:
https://lornettedaye.com/foundations

#NBATipOff #WolvesBack #TeamChemistry #AnthonyEdwards #LaMeloBall #HighPerformance #BetterPeopleBetterPlayers #LornettesFoundations #LeadershipExcellence"""
    },
    {
        "day": 12,
        "date_str": "2026-11-03T18:30:00-05:00", # 6:30 PM EST
        "image": "raptors_06_pascal_siakam.png",
        "title": "LEGEND SPOTLIGHT: PASCAL SIAKAM AND THE RELENTLESS ASCENT",
        "caption": """LEGEND SPOTLIGHT: PASCAL SIAKAM AND THE RELENTLESS ASCENT.

Pascal Siakam's journey from Cameroon to NBA Champion is one of the greatest developmental stories in sports history.

He did not touch a basketball until his late teens. He spent time in the G-League developing his game with Raptors 905. He earned the Most Improved Player award, became an All-NBA forward, and scored 32 points on 14-of-17 shooting in Game 1 of the 2019 NBA Finals.

How does an athlete make that quantum leap?

Unmatched motor and complete coachability. Pascal never negotiated with his conditioning. He sprinted in transition every possession, embraced coaching feedback without defense, and trusted the development process every day.

In our Athlete Development programs, we teach that your starting point does not define your summit. Relentless effort, humbleness to learn, and supreme conditioning will outwork raw talent every single time.

What part of Pascal Siakam's evolution inspired you the most?

Discover how we coach athletes to unlock extraordinary developmental breakthroughs:
https://lornettedaye.com/foundations

#WeTheNorth #PascalSiakam #SpicyP #DevelopmentalStory #WorkEthicWins #BetterPeopleBetterPlayers #LornettesFoundations #AthleteDevelopment #Resilience"""
    },
    {
        "day": 13,
        "date_str": "2026-11-04T18:30:00-05:00", # 6:30 PM EST
        "image": "07_three_teams_one_question.png",
        "title": "THREE TEAMS. FIFTEEN PLAYERS. ONE QUESTION: WHO CONTROLS THE PACE?",
        "caption": """THREE TEAMS. FIFTEEN PLAYERS. ONE QUESTION: WHO CONTROLS THE PACE?

Miami. Minnesota. Toronto.

Three distinct philosophies competing for Eastern and Western supremacy:
- Miami relies on defensive suffocation, physical conditioning, and veteran playoff poise.
- Minnesota thrives on speed, open-court athleticism, and explosive backcourt creation.
- Toronto leans into long-limbed defensive switching, Canadian grit, and calculated half-court execution.

When elite systems clash, the winner is rarely the team with the highest-scoring individual. The winner is the team that dictates pace and imposes its identity on the game.

If Minnesota forces a track meet, they are dangerous. If Miami turns the fourth quarter into a half-court grind, they hold the upper hand. If Toronto controls the glass and transition tempo, their versatility shines.

In athletics and in corporate leadership, winning begins with knowing exactly who you are and refusing to let your competitor change your rhythm.

Which of these three teams has the most sustainable identity over 82 games?

Explore how to develop and protect your competitive identity:
https://lornettedaye.com/foundations

#HEATCulture #WolvesBack #WeTheNorth #NBA #TacticalBreakdown #PaceAndSpace #BetterPeopleBetterPlayers #LornettesFoundations #IdentityBeyondSport"""
    },
    {
        "day": 14,
        "date_str": "2026-11-05T18:30:00-05:00", # 6:30 PM EST
        "image": "raptors_07_fred_vanvleet.png",
        "title": "LEGEND SPOTLIGHT: FRED VANVLEET AND BETTING ON YOURSELF",
        "caption": """LEGEND SPOTLIGHT: FRED VANVLEET AND BETTING ON YOURSELF.

Undrafted out of Wichita State. Sent to the G-League.

Fred VanVleet could have accepted the world's ceiling on his career. Instead, he coined a phrase that became an international rallying cry: "Bet on Yourself."

In the 2019 Eastern Conference Finals and NBA Finals, VanVleet hit clutch three after clutch three while face-guarding Stephen Curry with relentless tenacity. He played with a bandaged eye and chipped tooth, refusing to yield an inch of hardwood.

Self-belief is not arrogance. Authentic self-belief is backed by obsessive preparation. When you know you have outworked your competition in empty gyms at 5:00 AM, you step into high-pressure moments without fear.

VanVleet proved to every young athlete that where you start in the draft means nothing compared to how you prepare every single day.

How has the "Bet on Yourself" mindset influenced your own career and journey?

Learn how we help competitors build unshakable mental discipline and preparation systems:
https://lornettedaye.com/foundations

#WeTheNorth #FredVanVleet #BetOnYourself #SteadyFreddy #DisciplineSystems #BetterPeopleBetterPlayers #LornettesFoundations #Resilience #ChampionMindset"""
    },
    {
        "day": 15,
        "date_str": "2026-11-06T18:30:00-05:00", # 6:30 PM EST
        "image": "04_timberwolves_brotherhood.png",
        "title": "BACKCOURT DYNAMICS: HOW TWO ALPHA GUARDS LEARN TO ELEVATE EACH OTHER",
        "caption": """BACKCOURT DYNAMICS: HOW TWO ALPHA GUARDS LEARN TO ELEVATE EACH OTHER.

When Anthony Edwards attacks the rim with ferocity, defenses collapse. When LaMelo Ball reads the floor three steps ahead, shooters find open space.

The hardest transition for elite scoring guards is learning when to take over and when to empower.

In high-performance coaching, we focus heavily on communication and presence. Great backcourts do not need spoken play-calls on every possession. They communicate through eye contact, spatial awareness, and mutual trust.

Edwards and Ball are showing that when young leaders prioritize winning over personal accolades, their entire team rises to meet their energy.

Championship chemistry is not born overnight. It is tested through November slumps and December road stretches. Keep watching this dynamic.

What is the biggest key for Edwards and Ball maintaining this momentum all winter?

Discover our principles for elite sports leadership and backcourt synergy:
https://lornettedaye.com/foundations

#WolvesBack #AnthonyEdwards #LaMeloBall #Timberwolves #BackcourtSynergy #BetterPeopleBetterPlayers #LornettesFoundations #LeadershipInAction"""
    },
    {
        "day": 16,
        "date_str": "2026-11-07T18:30:00-05:00", # 6:30 PM EST
        "image": "raptors_08_damon_stoudamire.png",
        "title": "LEGEND SPOTLIGHT: DAMON STOUDAMIRE AND LAYING THE FIRST BRICK",
        "caption": """LEGEND SPOTLIGHT: DAMON STOUDAMIRE AND LAYING THE FIRST BRICK.

Every great building starts with a foundation in the dirt.

In 1995, the Toronto Raptors were an expansion franchise playing inside the cavernous SkyDome. Damon "Mighty Mouse" Stoudamire was the first draft pick in franchise history, standing 5-foot-10 in a league of giants.

He played with ferocious speed, poise, and heart, capturing the 1996 NBA Rookie of the Year award and delivering unforgettable upsets against Michael Jordan's 72-win Chicago Bulls.

In leadership, the pioneer's role is often the hardest. You do not inherit a winning culture; you have to generate it through sheer willpower when nobody expects you to win.

Stoudamire proved that Toronto belonged in professional basketball from day one.

Do you remember watching Damon Stoudamire lead the early Raptors at the SkyDome?

Learn how we teach athletes and organizations to lay unshakable cultural foundations:
https://lornettedaye.com/foundations

#WeTheNorth #DamonStoudamire #MightyMouse #RaptorsOriginal #FoundationBuilders #BetterPeopleBetterPlayers #LornettesFoundations #LegacyAndImpact"""
    },
    {
        "day": 17,
        "date_str": "2026-11-08T18:30:00-05:00", # 6:30 PM EST
        "image": "02_miami_heat_starting_five.png",
        "title": "THE COST OF EXPECTATION: WHY MIAMI HEAT CULTURE DEMANDS SACRIFICE",
        "caption": """THE COST OF EXPECTATION: WHY MIAMI HEAT CULTURE DEMANDS SACRIFICE.

When you assemble superstars, expectation becomes the default currency.

In Miami, the standard has never been about making the playoffs. The standard is championship contention every single season. That level of expectation breaks players who rely solely on talent, but refines competitors who thrive on discipline.

In our Olympic coaching work, we emphasize emotional regulation and recovery. High-pressure environments create chronic physical and mental fatigue. Athletes who thrive in pressure-cooker organizations are those who develop daily reset habits:
- Focusing exclusively on what they can control today.
- Leaving yesterday's performance in the past.
- Holding themselves accountable before coaches have to speak.

The Miami Heat starting five has the star power. The real question is whether they possess the daily emotional endurance to sustain championship intensity.

How do you manage high expectations in your own competitive environment?

Explore our frameworks for performing under extreme organizational pressure:
https://lornettedaye.com/foundations

#HEATCulture #MiamiHEAT #HighExpectations #EmotionalRegulation #DisciplineSystems #BetterPeopleBetterPlayers #LornettesFoundations #ExecutiveExcellence"""
    },
    {
        "day": 18,
        "date_str": "2026-11-09T18:30:00-05:00", # 6:30 PM EST
        "image": "raptors_09_jose_calderon.png",
        "title": "LEGEND SPOTLIGHT: JOSE CALDERON AND THE UNSELFISH FLOOR GENERAL",
        "caption": """LEGEND SPOTLIGHT: JOSE CALDERON AND THE UNSELFISH FLOOR GENERAL.

In an era of highlight-heavy basketball, Jose Calderon was a masterclass in efficiency and unselfish leadership.

His historic 2008-09 free-throw record (98.1%) still stands as a testament to surgical focus. Even more impressive was his assist-to-turnover ratio, consistently leading the entire NBA by making the correct pass time after time.

Calderon never sought the personal spotlight. He took pride in making his teammates look extraordinary, organizing the offense, and communicating with warmth and professionalism.

In elite sport and high-performing business, the unselfish floor general is often the glue that holds everything together. When you elevate others, you make the entire organization resilient.

What did Jose Calderon teach us about the art of selfless point guard play?

Learn how we train communicators and floor generals to elevate their teams:
https://lornettedaye.com/foundations

#WeTheNorth #JoseCalderon #FloorGeneral #UnselfishPlay #TorontoRaptors #Efficiency #BetterPeopleBetterPlayers #LornettesFoundations #CommunicationAndPresence"""
    },
    {
        "day": 19,
        "date_str": "2026-11-10T18:30:00-05:00", # 6:30 PM EST
        "image": "05_toronto_raptors_return.png",
        "title": "BUILDING THE NEXT ERA: HOW RECENT HISTORY INFORMS TORONTO'S HORIZON",
        "caption": """BUILDING THE NEXT ERA: HOW RECENT HISTORY INFORMS TORONTO'S HORIZON.

As the Toronto Raptors move through November, every game serves as a data point for growth.

With Scottie Barnes asserting himself as an all-around playmaker, RJ Barrett attacking downhill, and veterans providing steady poise, Toronto is writing its next chapter.

The lesson from 30 years of Raptors basketball is simple: sustained success in Canada is never handed out. It is earned through defensive identity, unselfish ball movement, and pride in representing the North.

As Coach Lornette Daye, watching Canadian basketball talent compete at the pinnacle of world sport is deeply gratifying. But the goal is never just participation. The goal is building a culture capable of competing for championships year after year.

What has impressed you most about the Raptors' identity early in this campaign?

Discover how we help organizations build enduring cultures of athletic excellence:
https://lornettedaye.com/foundations

#WeTheNorth #TorontoRaptors #ScottieBarnes #RJBarrett #CultureBuilding #BetterPeopleBetterPlayers #LornettesFoundations #IdentityBeyondSport"""
    },
    {
        "day": 20,
        "date_str": "2026-11-11T18:30:00-05:00", # 6:30 PM EST
        "image": "raptors_10_scottie_barnes.png",
        "title": "LEGEND SPOTLIGHT: SCOTTIE BARNES AND THE TORCH OF LEADERSHIP",
        "caption": """LEGEND SPOTLIGHT: SCOTTIE BARNES AND THE TORCH OF LEADERSHIP.

From Rookie of the Year to NBA All-Star, Scottie Barnes represents both the present and the future of the Toronto Raptors franchise.

He possesses the joyous energy of Vince Carter, the physical motor of Pascal Siakam, and the unselfish court vision of Kyle Lowry. But what sets Scottie apart is his authentic personality and genuine love for connecting with teammates and fans alike.

In our athlete development programs, we teach that leadership is not about trying to be someone else. It is about bringing your authentic self to the court every single day, playing with relentless energy, and inspiring those around you to elevate their standard.

Scottie holds the torch for Canadian basketball. And the future is in exceptional hands.

What excites you most about Scottie Barnes leading this franchise into the next decade?

Learn how we guide emerging stars into mature, high-impact leaders:
https://lornettedaye.com/foundations

#WeTheNorth #ScottieBarnes #RaptorsNation #NextGenerationLeader #AllStar #BetterPeopleBetterPlayers #LornettesFoundations #ChampionMindset #AthleteDevelopment"""
    },
    {
        "day": 21,
        "date_str": "2026-11-12T18:30:00-05:00", # 6:30 PM EST
        "image": "01_week_one_championships.png",
        "title": "THREE WEEKS IN: WHAT SEPARATES CONTENDERS FROM NOISE",
        "caption": """THREE WEEKS IN: WHAT SEPARATES CONTENDERS FROM NOISE.

Three weeks into the NBA season, the initial adrenaline of opening night has settled into the reality of the daily grind.

Teams that relied solely on raw shooting and emotion have begun to regress. Teams that invested in defensive communication, roster depth, and locker room trust are finding their rhythm.

This is the greatest lesson sport offers to any competitive endeavor:
- Flashy beginnings are easy. Sustained excellence requires discipline systems.
- Highlight plays attract attention. Unselfish defense wins playoff rounds.
- Great individuals win quarters. Unified cultures win championships.

Whether on the court or in executive leadership, the standard never changes: Better People, Better Players.

Which team has proven their identity to you over these opening three weeks?

Explore Lornette Daye's Complete Athlete Development System:
https://lornettedaye.com/foundations

#NBA #NBATipOff #BetterPeopleBetterPlayers #LornettesFoundations #ExecutiveLeadership #HighPerformance #ChampionMindset #ChampionshipCulture"""
    }
]

# Validation assertions
for idx, p in enumerate(posts_data):
    # Zero asterisk invariant
    assert "*" not in p["caption"], f"Asterisk detected in caption day {p['day']}"
    assert "*" not in p["title"], f"Asterisk detected in title day {p['day']}"
    # Zero em-dash invariant
    assert "—" not in p["caption"], f"Em-dash detected in caption day {p['day']}"
    assert "—" not in p["title"], f"Em-dash detected in title day {p['day']}"
    # Media asset exists locally
    local_path = os.path.join(r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\nba-season-start", p["image"])
    assert os.path.isfile(local_path), f"Asset missing: {local_path}"

# Format full JSON queue
queue = []
for p in posts_data:
    dt = datetime.fromisoformat(p["date_str"])
    due_at = dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    queue.append({
        "day": p["day"],
        "date": dt.strftime("%Y-%m-%d"),
        "dueAt": due_at,
        "title": p["title"],
        "caption": p["caption"],
        "image": f"{BASE_IMG_URL}/{p['image']}",
        "local_image": p["image"]
    })

out_path = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\scripts\master-nba-season-queue.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(queue)} campaign posts in {out_path}!")
for q in queue:
    print(f"Day {q['day']:02d} | {q['dueAt']} | {q['image']} | {q['title'][:40]}")
