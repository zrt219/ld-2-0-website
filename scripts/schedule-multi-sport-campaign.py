# -*- coding: utf-8 -*-
"""
Multi-Sport Campaign Scheduler: Football, Grant Fuhr & Hockey (Oct 30 - Nov 8, 2026)
Total: 30 posts (10 Football, 10 Grant Fuhr, 10 Hockey)
Cadence: 3 posts / day
  - Slot 1 (Morning 08:15 AM MDT / 14:15 UTC): Canadian NFL Football Star
  - Slot 2 (Mid-Day 01:00 PM MDT / 19:00 UTC): Grant Fuhr Goaltending Legend Tribute
  - Slot 3 (Late Afternoon 04:30 PM MDT / 22:30 UTC): Canadian Hockey Trailblazer / Star
Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
Destination: Lornette's Foundations (https://lornettedaye.com/foundations)

Invariants:
- Zero em dashes (—, \u2014)
- Zero "Coach Lornette" prefixes in copy (use "Lornette Daye" or "Olympic-level coach Lornette Daye")
- Strict plural "Lornette’s Foundations"
- High-visibility hashtag stacks
"""

import sys
import os
import json
import ssl
import urllib.request
import urllib.error
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

POSTS = [
    # ==========================================
    # DAY 1: Thursday, October 30, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_001",
        "sport": "Football",
        "title": "Chase & Sydney Brown",
        "slot": "Day 1 Morning (08:15 AM MDT)",
        "dueAt": "2026-10-30T14:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-01-chase-sydney-brown.png",
        "text": """SAME ROOTS. DIFFERENT SIDELINES. 🇨🇦🏈

From London, Ontario to the highest level of professional football, Chase Brown and Sydney Brown represent what happens when relentless work ethic meets uncompromising brotherhood.

In my four decades coaching Olympic-level athletes and national champions, I have observed that elite athletic development is never an accident. It is built in the cold early mornings, through family sacrifice, and in an unwavering refusal to be outworked. When twin brothers reach Sunday lights on opposite sidelines in the NFL, it speaks volumes about the foundation laid long before the stadium lights turned on.

Raw athletic talent opens the door. But character, emotional regulation, and discipline keep you in the room.

To every young athlete striving in grassroots programs across Canada: your postal code never defines your ceiling. Your preparation does.

Are you building habits that withstand the test of the highest level?

If you are an athlete, parent, or sports organization committed to elite development on and off the field:

👉 Explore Lornette's Foundations, our complete athlete development system: https://lornettedaye.com/foundations
💬 Or send me a direct message right here on LinkedIn to discuss mentorship and high-performance athlete workshops.

#ChaseBrown #SydneyBrown #Bengals #Eagles #CanadianFootball #NFLCanada #AthleteDevelopment #ChampionMindset #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_002",
        "sport": "Grant Fuhr",
        "title": "Golden Goaltender Tribute",
        "slot": "Day 1 Mid-Day (01:00 PM MDT)",
        "dueAt": "2026-10-30T19:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-01-golden-goaltender.png",
        "text": """THE GREATEST GOALTENDER EVER? WAYNE GRETZKY THOUGHT SO. 🏒🏆

In 1987, Wayne Gretzky was asked about the cornerstone of Edmonton's dynasty. His answer was definitive: "Grant Fuhr is the best goaltender who ever played the game, there's no question of that."

Grant Fuhr did not just win games. He absorbed immense pressure so his teammates could play with absolute freedom. When a game was tied 5-5 in the third period of a Stanley Cup Final, Fuhr made the one save that changed history. That is not just technical skill. That is supreme emotional regulation and ice in the veins.

In my 40+ years coaching Olympic-level performers, I teach that true mastery is revealed when the noise is at its peak. The best do not panic. They get calmer.

Grant Fuhr proved that poise in the crease can carry a championship dynasty.

How do you respond when the stakes are highest and everyone is looking at you?

To develop the mental resilience and composure of a champion:

👉 Discover Lornette's Foundations, the complete athlete development program: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to connect on executive performance and athlete development programs.

#GrantFuhr #EdmontonOilers #StanleyCup #HockeyLegend #GoalieMindset #PressurePoise #HallOfFame #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_003",
        "sport": "Hockey",
        "title": "Willie O'Ree: The Man Who Opened The Door",
        "slot": "Day 1 Late Afternoon (04:30 PM MDT)",
        "dueAt": "2026-10-30T22:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-01-willie-oree.png",
        "text": """THE MAN WHO OPENED THE DOOR. 🏒🚪

On January 18, 1958, Willie O'Ree stepped onto the ice for the Boston Bruins and changed hockey forever.

What makes Willie's legacy even more staggering is what he endured in silence: playing through racial hostility while secretly blind in his right eye from a puck strike years earlier. He never made an excuse. He never let circumstances dictate his standard. He simply showed up, competed with dignity, and paved the road for generations that followed.

As a Canadian Olympian coach, I remind our athletes daily: trailblazers do not carry light loads. They carry the responsibility of opening doors for others.

Every young Black hockey player who laces up skates today stands on the shoulders of Willie O'Ree's courage and poise.

When adversity confronts your journey, what foundation keeps you standing tall?

Equip yourself or your team with the discipline and resilience of a champion:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message here on LinkedIn to schedule a leadership workshop or team keynote.

#WillieORee #BostonBruins #HockeyPioneer #Trailblazer #Resilience #BlackHockeyHistory #BetterPeopleBetterPlayers #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 2: Friday, October 31, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_004",
        "sport": "Football",
        "title": "Chase Brown: London Raised. NFL Proven.",
        "slot": "Day 2 Morning (08:15 AM MDT)",
        "dueAt": "2026-10-31T14:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-02-chase-brown.png",
        "text": """LONDON RAISED. NFL PROVEN. 🇨🇦⚡

When Chase Brown takes the field for the Cincinnati Bengals, every explosive cut and downhill run is fueled by years of silent dedication in southwestern Ontario.

The transition from Canadian youth football to an NFL starter demands extraordinary adaptability. The speed of the game multiplies. The margin for error shrinks to inches. Those who thrive are not just physically gifted. They possess the mental discipline to study schemes, protect the quarterback, and execute under pressure.

In my four decades mentoring elite performers, one rule never changes: you do not rise to the occasion. You sink to the level of your preparation.

Chase Brown proves that Canadian athletes possess the grit to compete with anyone on the planet.

Are you preparing today for the opportunity tomorrow will demand?

Build the championship mindset required to compete at your highest standard:

👉 Learn more about Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss athlete development and high-performance coaching.

#ChaseBrown #CincinnatiBengals #NFLCanada #LondonOntario #RunningBack #Preparation #Discipline #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_005",
        "sport": "Grant Fuhr",
        "title": "Greatest Goaltender: 5 Stanley Cups",
        "slot": "Day 2 Mid-Day (01:00 PM MDT)",
        "dueAt": "2026-10-31T19:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-02-greatest-goaltender.png",
        "text": """5 STANLEY CUPS. 403 WINS. UNMATCHED CLUTCH EXCELLENCE. 🏆🧤

There are goaltenders who put up impressive statistics in low-risk environments. And then there is Grant Fuhr, who stood in the crease for the highest-scoring, highest-risk offensive machine in hockey history.

Playing behind the 1980s Edmonton Oilers required an entirely different mental framework. Opponents received odd-man rushes constantly. Fuhr had to stay sharp while seeing only three shots in ten minutes, then face a breakaway with the championship on the line.

That requires laser-like focus and supreme emotional control.

In high-performance athletics and executive leadership alike, the hardest discipline is sustaining focus when the environment is unpredictable.

Do you have the focus systems in place to deliver when the spotlight suddenly turns to you?

Master the mental disciplines of repeatable elite execution:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for performance consulting and keynotes.

#GrantFuhr #GoaltendingLegend #EdmontonOilers #ClutchPerformance #MentalFocus #HockeyHistory #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_006",
        "sport": "Hockey",
        "title": "Jarome Iginla: 625 Goals. A Legacy.",
        "slot": "Day 2 Late Afternoon (04:30 PM MDT)",
        "dueAt": "2026-10-31T22:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-02-jarome-iginla.png",
        "text": """625 GOALS. 1,300 POINTS. A LEGACY BUILT ON POWER AND INTEGRITY. 🇨🇦🔥

Jarome Iginla redefined what it meant to be an elite NHL captain.

He could score a hat trick, throw a game-turning check, defend a teammate, and then address the media with absolute humility and class. That combination of ferocity in competition and dignity off the ice is the true hallmark of an Olympic champion.

Having coached Olympians across multiple sports, I have seen many skilled players. But the ones who leave an immortal legacy are leaders like Jarome, whose character elevates the standard of everyone in the locker room.

True leadership is not proclaimed through words. It is demonstrated through relentless standard and respect for the game.

What example are you setting for those who follow your lead?

Build character-driven leadership in your athletes, team, or organization:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect with me via direct message on LinkedIn to discuss athlete development workshops.

#JaromeIginla #CalgaryFlames #HockeyHallOfFame #TeamCanada #Leadership #CaptainMindset #OlympicExcellence #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 3: Saturday, November 01, 2026
    # (DST: 08:15 MST -> 15:15 UTC, 13:00 MST -> 20:00 UTC, 16:30 MST -> 23:30 UTC)
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_007",
        "sport": "Football",
        "title": "Chuba Hubbard: Sherwood Park to Sunday Lights",
        "slot": "Day 3 Morning (08:15 AM MST)",
        "dueAt": "2026-11-01T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-03-chuba-hubbard.png",
        "text": """SHERWOOD PARK TO SUNDAY LIGHTS. 🇨🇦🍁

From the frozen fields of Alberta to carrying the workload in the Carolina Panthers' backfield, Chuba Hubbard's journey is an anthem of steady perseverance.

In the modern NFL, running backs face relentless physical pressure, shifting depth charts, and intense scrutiny. Chuba didn't just survive in that environment. He earned his extension and earned the absolute trust of his coaching staff through physical toughness and professional discipline.

In 40+ years in elite sports, I remind athletes: perseverance is not passive waiting. It is doing the fundamental work with excellence every single day, especially when the spotlight is elsewhere.

When you do the unglamorous work in private, you will always be ready for the lights in public.

Are you executing your daily fundamentals with championship consistency?

Equip your athletes or corporate team with durable resilience systems:

👉 Learn about Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to start an athlete development conversation.

#ChubaHubbard #CarolinaPanthers #SherwoodPark #AlbertaProud #NFLRunningBack #Perseverance #DisciplineSystems #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_008",
        "sport": "Grant Fuhr",
        "title": "Golden Goaltending Legacy: Spruce Grove Roots",
        "slot": "Day 3 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-01T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-03-golden-legacy.png",
        "text": """FROM SPRUCE GROVE TO HOCKEY IMMORTALITY. 🇨🇦🌲

Long before he was lifting five Stanley Cups or entering the Hockey Hall of Fame, Grant Fuhr was an Alberta kid stopping pucks on neighborhood rinks in Spruce Grove.

He wasn't manufactured in a high-tech academy. He was forged through thousands of hours of instinct, vision, athleticism, and the unshakeable self-belief that he could stop anything thrown his way.

In my coaching career, I have seen that world-class athletes never lose touch with their roots. Your beginning grounds you. It reminds you of why you play when the business of professional sport becomes overwhelming.

Do you remember the love for the craft that started your journey?

Reconnecting with your core purpose is one of the ten pillars of athletic excellence:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for performance mentorship and athlete development inquiries.

#GrantFuhr #SpruceGrove #AlbertaHockey #OilersDynasty #PurposeDriven #RootsOfExcellence #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_009",
        "sport": "Hockey",
        "title": "Wayne Simmonds: Every Shift",
        "slot": "Day 3 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-01T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-03-wayne-simmonds.png",
        "text": """1,037 NHL GAMES. ZERO EASY NIGHTS. 🏒💪

When Wayne Simmonds laced up his skates, teammates walked taller and opponents took note.

Over 15 rugged seasons in the National Hockey League, Simmonds embodied the concept of competitive presence. He scored tough goals in the blue paint, fought through severe injuries, and stood up for his squad with absolute loyalty. He earned every single second of ice time through honest, uncompromising effort.

As an Olympic-level coach, I teach that presence is not about intimidation. It is about an aura of unshakable reliability. Your team knows that no matter how difficult the battle becomes, you will never yield an inch.

Are you bringing that level of dependability to your team every single day?

Cultivate presence, accountability, and grit across your sports organization:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss team culture and athlete performance workshops.

#WayneSimmonds #WayneTrain #Flyers #MapleLeafs #NHLGrind #PresenceAndAccountability #WorkEthic #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 4: Sunday, November 02, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_010",
        "sport": "Football",
        "title": "Jevon Holland: Coquitlam to the Big Stage",
        "slot": "Day 4 Morning (08:15 AM MST)",
        "dueAt": "2026-11-02T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-04-jevon-holland.png",
        "text": """FROM COQUITLAM TO THE BIG STAGE. 🇨🇦🌊

Playing safety in the National Football League requires elite physical speed paired with a chess master's mind. Jevon Holland brings both every single snap.

Born in Coquitlam, British Columbia, Holland has established himself as one of the premier defensive backs in football. He diagnoses route concepts before the ball is thrown, communicates coverages across the secondary, and plays with an infectious joy that lifts the entire defense.

In 40+ years coaching Olympic champions, I emphasize that emotional energy is a competitive advantage. When an athlete plays with joy anchored in intense preparation, pressure dissolves.

Do you play and lead with joy, or are you weighed down by external expectations?

Master emotional regulation and competitive poise:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message here on LinkedIn to schedule a performance assessment or speaking engagement.

#JevonHolland #NFLDefense #CoquitlamBC #SafetyPlay #EmotionalPoise #GamePreparation #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_011",
        "sport": "Grant Fuhr",
        "title": "Edmonton's Golden Legend: Poise Defined an Era",
        "slot": "Day 4 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-02T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-04-edmontons-golden-legend.png",
        "text": """CHAMPIONSHIP POISE DEFINED AN ERA. 🏒✨

Look closely at any photograph of Grant Fuhr during a high-stakes playoff game. You will never see frantic movement. You will never see tension in his posture.

You see balance. Stillness. Absolute readiness.

While fans held their breath and tension threatened to paralyze the building, Fuhr looked as though he was playing shinny on an empty pond. That quiet confidence radiated through the entire Edmonton bench, allowing legends like Messier, Gretzky, Kurri, and Coffey to attack without hesitation.

In high-performance sport, your emotional frequency is contagious. A calm leader settles an entire organization.

What energy are you projecting to those who rely on your leadership?

Develop the poise and internal anchor of a world-class champion:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect via direct message on LinkedIn for executive coaching and high-performance programs.

#GrantFuhr #OilersDynasty #ChampionshipPoise #EmotionalRegulation #LeadershipPresence #HockeyRoyalty #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_012",
        "sport": "Hockey",
        "title": "P.K. Subban: He Changed The Game His Way",
        "slot": "Day 4 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-02T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-04-pk-subban.png",
        "text": """HE CHANGED THE GAME HIS WAY. 🏒💥

When P.K. Subban stepped onto NHL ice, he brought dynamic electric energy, booming slapshots, bone-crushing open-ice hits, and an unmistakable personal brand.

Winning the 2013 Norris Trophy as the league's top defenseman proved his elite hockey caliber. But his 10-million-dollar pledge to Montreal Children's Hospital proved something much greater: his commitment to using his platform to transform lives.

In my four decades coaching high-performance athletes, I teach that identity must extend far beyond your sport. When an athlete knows who they are away from competition, their performance inside the arena reaches new heights because they compete without fear.

Who are you when the jersey comes off?

Anchor your identity, personal brand, and legacy with our athlete development curriculum:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me here on LinkedIn to learn how we coach athletes to build enduring impact.

#PKSubban #NorrisTrophy #MontrealCanadiens #PersonalBrand #Philanthropy #IdentityBeyondSport #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 5: Monday, November 03, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_013",
        "sport": "Football",
        "title": "Elic Ayomanor: Medicine Hat, Big League Dreams",
        "slot": "Day 5 Morning (08:15 AM MST)",
        "dueAt": "2026-11-03T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-05-elic-ayomanor.png",
        "text": """MEDICINE HAT. BIG LEAGUE DREAMS. 🇨🇦🎯

From Medicine Hat, Alberta to dominating Saturdays in college football and stepping into the NFL spotlight, Elic Ayomanor is proof of the power of self-belief.

His legendary performance, catching 13 passes for 294 yards and three touchdowns in a historic comeback, did not happen by chance. It happened because when the game demanded greatness against top-ranked competition, his physical preparation and focus met the moment without flinching.

In 40+ years coaching Olympic athletes, I teach that signature moments are prepared long before anyone is watching. You don't hope you will perform when the spotlight turns on. You know you will, because the standard was locked into your muscle memory months earlier.

Are you training your mind and body for your signature breakthrough?

Master repeatable execution under pressure:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss athlete development cohorts.

#ElicAyomanor #TennesseeTitans #MedicineHat #AlbertaAthlete #WideReceiver #BigMoments #AthletePreparation #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_014",
        "sport": "Grant Fuhr",
        "title": "The Greatest: Legacy Built Save By Save",
        "slot": "Day 5 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-03T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-05-the-greatest.png",
        "text": """A LEGACY BUILT SAVE BY SAVE. 🧱🏒

In the 1988 season, Grant Fuhr played 75 regular-season games for the Edmonton Oilers, leading the NHL in wins and capturing the Vezina Trophy as the league's top goaltender.

Think about the sheer physical and mental endurance required to face elite shooters night after night in an era before modern goalie equipment ergonomics. Fuhr never complained of fatigue. He strapped on his pads and delivered excellence repeatedly.

Durability is one of the most underrated attributes of a world champion. Anyone can have a great week. Very few possess the discipline systems to perform at a world-class level across an entire career.

What daily recovery and mental wellness systems protect your durability?

Learn how our athlete development framework builds long-term athletic sustainability:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss performance wellness programs.

#GrantFuhr #VezinaTrophy #GoalieGreatness #Durability #DisciplineSystems #Endurance #HockeyLegends #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_015",
        "sport": "Hockey",
        "title": "Quinton Byfield: The Next Era Is His To Shape",
        "slot": "Day 5 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-03T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-05-quinton-byfield.png",
        "text": """THE NEXT ERA IS HIS TO SHAPE. 👑🏒

Selected second overall in the 2020 NHL Draft, Newmarket, Ontario native Quinton Byfield entered professional hockey with immense expectations on his young shoulders.

What impressed me most about Quinton is his patient maturity. He didn't rush the process. He went to the AHL, worked relentlessly on his two-way game, developed his 6-foot-5 frame, and evolved into a foundational powerhouse for the Los Angeles Kings.

In my four decades coaching high-performance competitors, I emphasize this crucial principle: player development is never a straight line. The athletes who achieve enduring greatness are those who trust the process, embrace developmental adversity, and keep building day by day.

Are you giving your own growth the patience and rigor it deserves?

Build long-term developmental pathways for young athletes and emerging talent:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Reach out via direct message on LinkedIn for youth athlete development consulting.

#QuintonByfield #LAKings #OntarioHockey #NextGeneration #PatienceAndProcess #YouthDevelopment #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 6: Tuesday, November 04, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_016",
        "sport": "Football",
        "title": "Joshua Palmer: Brampton Built. Buffalo Ready.",
        "slot": "Day 6 Morning (08:15 AM MST)",
        "dueAt": "2026-11-04T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-06-joshua-palmer.png",
        "text": """BRAMPTON BUILT. BUFFALO READY. 🇨🇦⚡

Brampton, Ontario has become one of the premier hotbeds of world-class athletic talent in North America. And Joshua Palmer is a prime example of why.

Palmer plays the wide receiver position with surgical precision: clean route running, strong hands in traffic, and an exceptional understanding of defensive leverage. When an NFL quarterback needs a critical third-down conversion, they look to the receiver who runs the exact depth and makes the tough catch in traffic.

Reliability is the currency of champions.

In my Olympic coaching experience, flash sells tickets, but reliability wins championships. Coaches build game plans around athletes they can trust on every single rep.

Are you the teammate your coach or leader can trust implicitly when the game is on the line?

Develop elite reliability and competitive discipline:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss athlete development frameworks.

#JoshuaPalmer #BuffaloBills #BramptonProud #NFLWideReceiver #Reliability #RouteRunning #OlympicStandard #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_017",
        "sport": "Grant Fuhr",
        "title": "Goaltending Greatness: Hall of Fame History",
        "slot": "Day 6 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-04T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-06-goaltending-greatness.png",
        "text": """HISTORY IN THE CREASE: HOCKEY HALL OF FAME 2003. 🏛️🏒

In 2003, Grant Fuhr became the first Black player inducted into the Hockey Hall of Fame.

He did not achieve that historic milestone by following an established blueprint. He created his own. With his hybrid stand-up and butterfly style, lightning-fast glove hand, and unmatched anticipation, Fuhr altered the way an entire generation of goaltenders played the position.

True greatness does not seek to imitate. It masters the fundamentals, then expands the boundaries of what is possible.

As an Olympic coach, I encourage every athlete to find their unique edge. The game does not need a carbon copy of yesterday's star. It needs you performing at your absolute authentic best.

Have you discovered and unlocked your personal performance edge?

Identify and sharpen your competitive advantage with our athlete development curriculum:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me on LinkedIn for athlete and executive high-performance consulting.

#GrantFuhr #HockeyHallOfFame #Pioneer #BlackHistory #GoaltendingExcellence #AuthenticGreatness #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_018",
        "sport": "Hockey",
        "title": "Jet Greaves: From Cambridge to the Crease",
        "slot": "Day 6 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-04T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-06-jet-greaves.png",
        "text": """FROM CAMBRIDGE TO THE NHL CREASE. 🇨🇦🧤

Jet Greaves was never handed an easy route to the National Hockey League.

Passed over in the NHL Draft, the Cambridge, Ontario native refused to let outside opinions define his ceiling. He grinded through junior hockey, earned an AHL contract through sheer performance, and when the Columbus Blue Jackets gave him an opportunity, he stopped 46 of 49 shots in an unforgettable debut.

That is the definition of staying ready so you never have to get ready.

In 40+ years coaching athletes to national titles, I remind competitors: the draft status is just a number on draft day. What you do with the next day determines your life.

Are you letting past setbacks or snubs dictate your current effort?

Turn adversity into your competitive springboard:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for athlete resilience coaching and team keynotes.

#JetGreaves #ColumbusBlueJackets #CambridgeOntario #Undrafted #Resilience #GoalieLife #PreparationMeetsOpportunity #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 7: Wednesday, November 05, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_019",
        "sport": "Football",
        "title": "John Metchie III: Bigger Than Football",
        "slot": "Day 7 Morning (08:15 AM MST)",
        "dueAt": "2026-11-05T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-07-john-metchie.png",
        "text": """THE JOURNEY IS BIGGER THAN FOOTBALL. 🇨🇦❤️

When John Metchie III caught passes at Alabama and entered the NFL Draft, his talent was undeniable. But his greatest victory came off the field, overcoming acute promyelocytic leukemia to return to the NFL gridiron with the Carolina Panthers.

Standing on an NFL sideline after beating cancer is the ultimate testament to human spirit, faith, and medical courage. It puts every dropped pass, tough loss, and minor setback into crystal-clear perspective.

In my four decades coaching elite performers, I teach that sport is a laboratory for life. We build resilience, discipline, and character on the track and on the field so that when life's hardest tests arrive, your foundation does not shake.

What inner anchor sustains you through your darkest seasons?

Build resilience that endures far beyond the boundary lines:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Connect via direct message on LinkedIn to discuss resilience keynotes and athlete mentorship.

#JohnMetchie #CarolinaPanthers #BramptonOntario #Perseverance #CancerSurvivor #TrueResilience #InspirationInSport #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_020",
        "sport": "Grant Fuhr",
        "title": "Legendary Goaltender: When The Game Got Loud",
        "slot": "Day 7 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-05T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-07-legendary-goaltender.png",
        "text": """WHEN THE GAME GOT LOUD, FUHR GOT CALMER. 🏒🤫

Stanley Cup playoffs produce an environment of pure sensory overload: 18,000 screaming fans, flying bodies, deflected pucks, and the weight of an entire city's expectations.

Most athletes experience an elevated heart rate that leads to rushed decisions. Grant Fuhr did the opposite. His breathing slowed. His movements became more economical. He controlled the tempo of the entire arena from his crease.

In high-performance coaching, we call this the reset protocol. You cannot prevent the world from getting noisy. But you can train your autonomic nervous system to find stillness in the storm.

How quickly can you reset your emotions when a crisis erupts in your environment?

Train your emotional regulation and pressure recovery systems:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me on LinkedIn for high-performance leadership and athlete training programs.

#GrantFuhr #PressureRegulation #ResetProtocol #Composure #HighPerformance #MentalToughness #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_021",
        "sport": "Hockey",
        "title": "Anthony Duclair: Speed. Skill. Purpose.",
        "slot": "Day 7 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-05T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-07-anthony-duclair.png",
        "text": """SPEED. SKILL. PURPOSE. 🏒💨

Pointe-Claire, Quebec's Anthony Duclair plays the game with electrifying speed. But his most significant impact is his leadership with the Hockey Diversity Alliance, working to make hockey welcoming and accessible for kids of every background.

When an athlete pairs elite speed on the ice with a clear sense of purpose away from it, their performance deepens. They are no longer playing just for statistics or contracts. They are playing for legacy and community impact.

In my coaching career, purpose is the greatest fuel an athlete can possess. Goals wear out. Passion can waver. But purpose endures every season.

What is the deeper mission driving your daily effort?

Discover how Lornette's Foundations connects athletic excellence with enduring community impact:

👉 Learn more at: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss athlete development and social impact partnerships.

#AnthonyDuclair #NYIslanders #QuebecHockey #HockeyDiversityAlliance #CommunityImpact #PurposeDriven #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 8: Thursday, November 06, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_022",
        "sport": "Football",
        "title": "Theo Johnson: Windsor to New York",
        "slot": "Day 8 Morning (08:15 AM MST)",
        "dueAt": "2026-11-06T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-08-theo-johnson.png",
        "text": """WINDSOR TO NEW YORK. 🇨🇦🗽

At 6-foot-6 and 260 pounds with elite 4.5 speed, Windsor, Ontario's Theo Johnson is built like a prototype modern NFL tight end.

Selected by the New York Giants, Johnson represents the new wave of Canadian athletes who combine rare size with world-class athletic testing. But raw measurable numbers only earn you an evaluation. Turning physical potential into on-field dominance requires blocking technique, playbook mastery, and mental toughness.

As an Olympic-level coach, I remind young athletes: potential is just unrealized promise. Execution is what builds a career.

Are you converting your potential into repeatable excellence every day?

Build the discipline and technical systems to unlock your full athletic ceiling:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for performance consultation and athlete development cohorts.

#TheoJohnson #NYGiants #WindsorOntario #TightEnd #NFLDraft #AthleticPotential #DisciplineInExecution #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_023",
        "sport": "Grant Fuhr",
        "title": "Canadian Hockey Legend: Number 31 Retired",
        "slot": "Day 8 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-06T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-08-canadian-hockey-legend.png",
        "text": """NUMBER 31: RETIRED TO THE RAFTERS. REMEMBERED FOREVER. 🏒3️⃣1️⃣

When a franchise retires your jersey number, they are not just honoring the saves you made. They are acknowledging that the standard you set defined the soul of the organization.

Grant Fuhr's number 31 hangs in Edmonton because he represented the heartbeat of five Stanley Cup championship teams. He showed up when it mattered most, embraced accountability, and earned the absolute reverence of hockey legends.

True athletic legacy outlasts any single contract or championship parade. It lives in the culture you leave behind.

What standard are you leaving for the next generation in your sport or business?

Build an enduring culture of excellence with Lornette's Foundations:

👉 Explore the curriculum: https://lornettedaye.com/foundations
💬 Connect with me via direct message on LinkedIn for culture and leadership workshops.

#GrantFuhr #Number31 #EdmontonOilers #JerseyRetirement #CultureOfExcellence #Legacy #AthleteDevelopment #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_024",
        "sport": "Hockey",
        "title": "K'Andre Miller: The Ring Tells Part of the Story",
        "slot": "Day 8 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-06T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-08-kandre-miller.png",
        "text": """THE RING TELLS ONLY PART OF THE STORY. 🏒💍

Standing 6-foot-5 on the blue line, K'Andre Miller's smooth skating stride and exceptional defensive reach make him a nightmare for opposing forwards.

Having already captured a Stanley Cup ring in 2026 with the Carolina Hurricanes, Miller's trajectory represents the pinnacle of modern defensemen. Yet the championship ring is only the visible outcome. The real story is the thousands of unseen hours learning backward crossovers, film study, and mental preparation required to dominate at 25 minutes a night.

In my coaching career, championships are won in the private months of preparation, not the final seconds of celebration.

Are you falling in love with the unglamorous daily process that leads to victory?

Build daily process discipline into your athletic journey:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to discuss athlete development and high-performance training.

#KAndreMiller #CarolinaHurricanes #StanleyCupChampion #Defenseman #DailyProcess #UnseenWork #ChampionMindset #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 9: Friday, November 07, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_025",
        "sport": "Football",
        "title": "Akheem Mesidor: Ottawa Produced an NFL Pass Rusher",
        "slot": "Day 9 Morning (08:15 AM MST)",
        "dueAt": "2026-11-07T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-09-akheem-mesidor.png",
        "text": """OTTAWA PRODUCED AN NFL PASS RUSHER. 🇨🇦⚡

Dominating the line of scrimmage in the NFL requires explosive first-step quickness, relentless leverage, and relentless violent hand fighting. Akheem Mesidor brings all three.

From Canada's capital in Ottawa to tearing up collegiate backfields and landing with the Los Angeles Chargers, Mesidor's relentless motor is his signature trademark. He refuses to take a snap off. Even when a play runs away from his side, he hunts down the ball carrier with unyielding intensity.

In 40+ years coaching Olympic champions, motor is not something you turn on and off on game day. It is an internal standard of effort that you train on every single repetition.

Is your motor running at full capacity when nobody is grading you?

Train the championship motor that separates good athletes from elite professionals:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Reach out via direct message on LinkedIn for performance coaching and athletic workshops.

#AkheemMesidor #LAChargers #OttawaOntario #DefensiveLine #PassRusher #RelentlessMotor #HighEffort #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_026",
        "sport": "Grant Fuhr",
        "title": "Canadian Goaltending Excellence: World-Class Game",
        "slot": "Day 9 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-07T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-09-goaltending-excellence.png",
        "text": """CANADIAN ROOTS. WORLD-CLASS GAME. 🇨🇦🌎

Grant Fuhr did not just capture Stanley Cups in the NHL. He represented Canada on the international stage, backstopping Team Canada to Canada Cup victories against the finest hockey powers in the world.

When you put on the maple leaf or step onto a global stage, the pressure elevates exponentially. You are no longer playing for a city. You are carrying the athletic heritage of an entire nation. Fuhr welcomed that burden with a calm smile and delivered when history called.

In my four decades coaching Olympians, international competition tests character more than any domestic league. You must navigate travel, foreign environments, and elevated stakes while staying true to your core preparation.

How well does your performance travel under foreign pressure?

Prepare your athletes for the national and international stage:

👉 Learn more about Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for Olympic-level athlete mentorship.

#GrantFuhr #TeamCanada #CanadaCup #InternationalHockey #OlympicMindset #NationalPride #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_027",
        "sport": "Hockey",
        "title": "Darnell Nurse: New Colours. Determination.",
        "slot": "Day 9 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-07T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-09-darnell-nurse.png",
        "text": """NEW COLOURS. UNWAVERING DETERMINATION. 🦈🏒

Hamilton, Ontario's Darnell Nurse has always been built on athletic pedigree, fierce competitiveness, and physical pride.

Stepping into a new chapter in 2026 with the San Jose Sharks, Nurse brings over a decade of NHL leadership, playoff battles, and minute-munching defense to a young dressing room hungry to establish a winning identity. Transitioning teams requires adaptability, humbleness, and a clear standard of daily work.

In high-performance sport and corporate leadership, the test of a veteran is how effectively you mentor the next wave of talent while maintaining your own sharp competitive edge.

Are you investing in the teammates who will carry your organization's future?

Master athlete leadership, mentorship, and career transitions:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Direct message me on LinkedIn to explore team development and executive leadership programs.

#DarnellNurse #SanJoseSharks #HamiltonProud #NHLDefense #VeteranLeadership #CareerTransitions #BetterPeopleBetterPlayers #LornettesFoundations #LornetteDaye"""
    },

    # ==========================================
    # DAY 10: Saturday, November 08, 2026
    # ==========================================
    {
        "id": "CAMPAIGN_MULTI_028",
        "sport": "Football",
        "title": "Matthew Bergeron: Quebec Roots. Atlanta Stage.",
        "slot": "Day 10 Morning (08:15 AM MST)",
        "dueAt": "2026-11-08T15:15:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/football/football-10-matthew-bergeron.png",
        "text": """QUEBEC ROOTS. ATLANTA STAGE. 🇨🇦⚜️

From Victoriaville, Quebec to anchoring the offensive line for the Atlanta Falcons, Matthew Bergeron is paving the way for French Canadian athletes in the NFL.

Offensive line play is the ultimate team-first position in sports. You don't get individual fantasy points or flashy highlight reels. You succeed only when five athletes move with one unified heartbeat, executing complex communication against 300-pound world-class defenders in fractions of a second.

In my four decades coaching championship squads, true team cohesion begins with shared discipline and trust. When each member protects the person beside them, victory is inevitable.

How strongly is your team unified around a shared standard of trust?

Build team cohesion and communication systems that win:

👉 Discover Lornette's Foundations: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn for organizational coaching and sports team workshops.

#MatthewBergeron #AtlantaFalcons #QuebecSports #Victoriaville #OffensiveLine #TeamCohesion #UnsungHeroes #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_029",
        "sport": "Grant Fuhr",
        "title": "A Canadian Legend: 100 Greatest Players",
        "slot": "Day 10 Mid-Day (01:00 PM MST)",
        "dueAt": "2026-11-08T20:00:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/fuhr/fuhr-10-a-canadian-legend.png",
        "text": """ONE OF THE NHL'S 100 GREATEST PLAYERS: GRANT FUHR. 🏆🇨🇦

When the NHL celebrated its centennial in 2017, Grant Fuhr was formally enshrined among the 100 Greatest NHL Players in history.

Decades after his final save, his impact on the sport remains undiminished. He inspired generations of minority athletes to strap on goalie pads, proved that composure is the ultimate weapon under pressure, and proved that a kid from Spruce Grove, Alberta could reach the highest summit of global hockey.

As an Olympic-level coach, that is what real legacy looks like. It is not just the trophies in the cabinet. It is the dreams you ignited in people you will never meet.

What dream are you igniting in the people who watch your journey?

Create a legacy that endures across generations with our 10-Foundation athlete development system:

👉 Explore Lornette's Foundations: https://lornettedaye.com/foundations
💬 Reach out via direct message on LinkedIn to connect on speaking, executive coaching, or athlete mentorship.

#GrantFuhr #NHL100 #CanadianLegend #HockeyRoyalty #LegacyAndImpact #EnduringExcellence #LornettesFoundations #LornetteDaye"""
    },
    {
        "id": "CAMPAIGN_MULTI_030",
        "sport": "Hockey",
        "title": "Willie O'Ree: A Pioneer. A Trailblazer. A Lasting Legacy.",
        "slot": "Day 10 Late Afternoon (04:30 PM MST)",
        "dueAt": "2026-11-08T23:30:00.000Z",
        "asset_url": "https://lornettedaye.com/campaigns/hockey/hockey-10-willie-oree-legacy.png",
        "text": """A PIONEER. A TRAILBLAZER. A LASTING LEGACY. 🏒🚪

To close our multi-sport tribute to Canadian excellence, we return to the man who made it all possible: Willie O'Ree.

Willie's journey was not easy. He took racial taunts in hostile barns, endured physical cheap shots, and played with vision in only one eye. Yet throughout his entire life, Willie never harbored bitterness. He answered ignorance with dignified excellence, relentless warmth, and an unwavering commitment to youth inclusion.

At Lornette's Foundations, our core motto is simple: BETTER PEOPLE · BETTER PLAYERS.

Willie O'Ree proved that when you are grounded as a human being of integrity, no external barrier can ever keep you from your destiny.

To every athlete, coach, and leader: let your standard be defined by your character, your work ethic, and your love for those who follow in your footsteps.

👉 Join us in building better people and better players: https://lornettedaye.com/foundations
💬 Send me a direct message on LinkedIn to partner on high-performance athlete and leadership development.

#WillieORee #HockeyPioneer #Trailblazer #BetterPeopleBetterPlayers #HockeyDiversity #Inspiration #OlympicCoach #LornettesFoundations #LornetteDaye"""
    }
]

CREATE_POST_MUTATION = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
        text
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

def verify_assets_on_production():
    print("--- Verifying all 30 assets on production (https://lornettedaye.com) ---")
    ctx = ssl._create_unverified_context()
    missing = []
    for item in POSTS:
        url = item["asset_url"]
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                if resp.status != 200:
                    missing.append((url, resp.status))
        except urllib.error.HTTPError as e:
            missing.append((url, e.code))
        except Exception as e:
            missing.append((url, str(e)))
    
    if missing:
        print(f"⚠️ {len(missing)} assets NOT accessible on production yet:")
        for m in missing[:5]:
            print(f"   {m[0]} -> {m[1]}")
        return False
    print("✅ All 30 production assets return HTTP 200 OK!")
    return True

def schedule_single_post(post_item):
    ctx = ssl._create_unverified_context()
    asset_payload = [{"image": {"url": post_item["asset_url"]}}]
    input_data = {
        "channelId": CHANNEL_ID,
        "text": post_item["text"],
        "mode": "customScheduled",
        "schedulingType": "automatic",
        "needsApproval": False,
        "saveToDraft": False,
        "dueAt": post_item["dueAt"],
        "assets": asset_payload
    }
    
    payload = json.dumps({"query": CREATE_POST_MUTATION, "variables": {"input": input_data}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            create_post = data.get("data", {}).get("createPost", {})
            typename = create_post.get("__typename")
            if typename == "PostActionSuccess" and "post" in create_post:
                p = create_post["post"]
                return True, p.get("id"), p.get("status")
            else:
                msg = create_post.get("message") or json.dumps(create_post)
                return False, typename, msg
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get("Retry-After")
        body = e.read().decode("utf-8", errors="ignore")
        return False, f"HTTP_{e.code}", f"Retry-After: {retry_after} | Body: {body}"
    except Exception as e:
        return False, "NetworkError", str(e)

def main():
    print("================================================================")
    print("🚀 MULTI-SPORT LINKEDIN CAMPAIGN SCHEDULER")
    print("Categories: Football, Grant Fuhr & Hockey Trailblazers")
    print("Dates: Oct 30, 2026 - Nov 08, 2026 (10 Days x 3 Posts = 30 Posts)")
    print("Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)")
    print("================================================================\n")
    
    # Save master queue to json
    queue_path = "scripts/master-multi-sport-queue.json"
    with open(queue_path, "w", encoding="utf-8") as f:
        json.dump(POSTS, f, indent=2)
    print(f"Master multi-sport queue saved: {queue_path} ({len(POSTS)} items)")

    # Check assets
    assets_ready = verify_assets_on_production()
    if not assets_ready:
        print("\nHALTING: Assets not yet 200 OK on production. Deployment in progress.")
        return

    report_path = "scripts/multi-sport-scheduled-report.json"
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            scheduled_report = json.load(f)
    else:
        scheduled_report = {}

    print(f"\nAlready scheduled: {len(scheduled_report)} / {len(POSTS)} posts.")

    for idx, item in enumerate(POSTS):
        post_id = item["id"]
        if post_id in scheduled_report:
            continue

        print(f"[{idx+1}/30] Scheduling {post_id} | {item['sport']}: {item['title']} | Slot: {item['slot']}")
        ok, res_id, res_status = schedule_single_post(item)
        if ok:
            print(f"   ✅ SUCCESS: Post ID {res_id} ({res_status})")
            scheduled_report[post_id] = {
                "postId": res_id,
                "status": res_status,
                "dueAt": item["dueAt"],
                "sport": item["sport"],
                "title": item["title"],
                "slot": item["slot"],
                "asset_url": item["asset_url"]
            }
            with open(report_path, "w", encoding="utf-8") as f:
                json.dump(scheduled_report, f, indent=2)
            time.sleep(2)  # Polite pacing between API requests
        else:
            print(f"   ⚠️ STOP / ERROR: {res_id} - {res_status}")
            break

    print("\n================================================================")
    print(f"📊 SUMMARY: {len(scheduled_report)} / {len(POSTS)} posts scheduled in Buffer.")
    print(f"Execution report: {report_path}")
    print("================================================================")

if __name__ == "__main__":
    main()
