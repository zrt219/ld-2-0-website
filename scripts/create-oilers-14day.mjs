import fs from 'fs';

const posts = [
  {
    day: 1,
    title: "Post 1 (Live Tonight): The Return of Ryan Nugent-Hopkins",
    date: "Saturday, Oct 24, 2026",
    scheduledAt: null, // live immediately
    isLiveNow: true,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png",
    caption: `NUGE IS BACK. ONE SHOT. ONE MOMENT.

When Ryan Nugent-Hopkins stepped onto the ice Thursday night against Carolina, he had missed nine consecutive games. 

No warm-up games. No margin for error in a wild 6-5 contest. 

And when the game went to a shootout, Coach put the puck on #93's stick.

One attempt. Decisive release. Goal. Devon Levi slammed the door, and the Edmonton Oilers secured two critical points in Rogers Place.

THE ATHLETIC REALITY:
Clutch execution is not an accident of emotion. It is the byproduct of internal emotional regulation, structured preparation, and an unshakeable identity that does not depend on immediate rhythm. When you are sidelined, your mind must stay inside the game so that when your moment arrives, your hands and feet already know what to do.

At Lornette's Foundations, we coach athletes across hockey, golf, and Olympic disciplines to develop this exact level of psychological poise:
https://lornettedaye.com/foundations

OIL COUNTRY: Where were you when Nuge buried the game-winner? Drop your reaction below.

#EdmontonOilers #LetsGoOilers #RyanNugentHopkins #OilersNation #RogersPlace #NHL #HockeyTwitter #ClutchPerformance #OilCountry #MentalToughness #SportsPsychology #LornettesFoundations #AthleteDevelopment`
  },
  {
    day: 2,
    title: "Post 2: Overcoming Injury and the Battle of Rhythm",
    date: "Sunday, Oct 25, 2026",
    scheduledAt: "2026-10-25T18:15:00.000Z", // 12:15 PM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png",
    caption: `THE RETURN FROM INJURY: THE MENTAL BATTLE NOBODY SEES.

Missing nine games in the NHL is not just physical recovery. It is a daily mental test.

While your teammates battle on the road, you are grinding through isolated rehab skates, conditioning drills, and watching from the press box. You question your timing. You wonder if your game speed will translate on night one.

Ryan Nugent-Hopkins answered every single question in his season debut:
- 19+ minutes of disciplined two-way responsibility
- Relentless special teams presence
- The lone shootout goal to seal the win

THE COACHING PERSPECTIVE:
True athletes do not wait for competition to find their confidence. They build their foundation in solitude so that adversity never dictates their standard.

Explore the complete athlete development framework at Lornette's Foundations:
https://lornettedaye.com/foundations

Hockey parents and coaches: How do you help your players maintain focus when sidelined by injury?

#EdmontonOilers #RyanNugentHopkins #InjuryComeback #AthleteMindset #HockeyCulture #NHLHighlights #SportsLeadership #Resilience #PlayerDevelopment #RogersPlace #OilCountry #LornettesFoundations`
  },
  {
    day: 3,
    title: "Post 3: The Shootout as a Solitary Pressure Chamber",
    date: "Monday, Oct 26, 2026",
    scheduledAt: "2026-10-26T17:30:00.000Z", // 11:30 AM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-shootout-hero-poster.png",
    caption: `THE LONELIEST 85 FEET IN HOCKEY.

A shootout attempt is not a skill drill. It is an isolated psychological duel.

18,000 screaming fans in Rogers Place. A goaltender challenging every inch of net. 65 minutes of exhausting hockey already in your legs. 

Ryan Nugent-Hopkins did not rush his approach. He controlled his glide speed, forced the goaltender into a subtle freeze, and buried the winner with precision.

KEY TAKEAWAY FOR ATHLETES:
Under extreme pressure, the body always defaults to the level of its baseline training. If your heart rate spikes and your breathing accelerates, your hands lock up. Master your breath, lock onto your visual target, and trust the thousands of repetitions you have banked.

Discover how Lornette's Foundations builds pressure-tested performers:
https://lornettedaye.com/foundations

Oilers fans: Rank your top three all-time Oilers shootout specialists in the comments below.

#EdmontonOilers #ShootoutWinner #NugentHopkins #HockeySkills #HockeyIQ #ClutchGene #HighPerformance #AthleteTraining #FocusUnderPressure #NHLNews #SportsMindset #LornettesFoundations`
  },
  {
    day: 4,
    title: "Post 4: McDavid and Draisaitl's 5-Point Nights",
    date: "Tuesday, Oct 27, 2026",
    scheduledAt: "2026-10-27T18:00:00.000Z", // 12:00 PM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png",
    caption: `WHEN SUPERSTARS CARRY THE LOAD: 10 COMBINED POINTS.

Connor McDavid: 5 points.
Leon Draisaitl: 5 points.

Thursday's 6-5 thriller against Carolina was a masterclass in offensive firepower from the two most dominant playmakers on the planet. Yet even with 10 combined points from #97 and #29, the game still came down to sudden-death execution.

THE LEADERSHIP LESSON:
Great teams do not rely exclusively on their brightest stars to close out victories. Championship culture is forged when your complementary pillars, your glue players like Ryan Nugent-Hopkins, step up in the defining moment to finish what the leaders started.

Learn how we teach team dynamics, peer leadership, and role excellence at Lornette's Foundations:
https://lornettedaye.com/foundations

Oil Country: Is this McDavid and Draisaitl's greatest dual performance of the young season? Let us know your thoughts.

#ConnorMcDavid #LeonDraisaitl #EdmontonOilers #OilersNation #SuperstarMindset #NHLStars #HockeyLeadership #TeamFirst #RogersPlace #HockeyExcellence #LornettesFoundations`
  },
  {
    day: 5,
    title: "Post 5: Devon Levi Slamming the Door",
    date: "Wednesday, Oct 28, 2026",
    scheduledAt: "2026-10-28T17:00:00.000Z", // 11:00 AM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-shootout-hero-poster.png",
    caption: `THE GOALIE PERSPECTIVE: DEVON LEVI CLOSES THE SHUTTER.

A shootout goal on the board means nothing if your goaltender cannot hold the crease.

After giving up five goals in a back-and-forth track meet, Devon Levi had to reset his mind completely before the shootout began. No frustration. No baggage from regulation. Pure presence.

He stopped every single Carolina shooter, sealing the victory the second Nuge scored.

THE NEXT SHOT MENTALITY:
In my four decades of Olympic-level coaching, one rule stands above all: Your previous play cannot stop your next play. Goaltenders who obsess over the goals they let in will always surrender the next one. Great stoppers compartmentalize instantly.

Master the mental reset mechanism through Lornette's Foundations:
https://lornettedaye.com/foundations

Goalies and coaches: What is your primary anchor routine after letting in a tough goal? Share below.

#DevonLevi #Goaltending #GoalieLife #EdmontonOilers #MentalReset #NextPlaySpeed #HockeyGoalie #PressureManagement #RogersPlace #SportsPerformance #LornettesFoundations`
  },
  {
    day: 6,
    title: "Post 6: Fourteen Years of Quiet Loyalty",
    date: "Thursday, Oct 29, 2026",
    scheduledAt: "2026-10-29T18:30:00.000Z", // 12:30 PM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png",
    caption: `FOURTEEN YEARS OF EDMONTON LOYALTY: THE RYAN NUGENT-HOPKINS STANDARD.

First overall pick in 2011. Over 900 regular season games. 700+ points.

Through rebuilds, coaching changes, playoff heartbreak, and Stanley Cup Final runs, Ryan Nugent-Hopkins has never wavered. He does not seek headlines. He does not complain about his minutes. He simply works.

THE IDENTITY PRINCIPLE:
In sports and in life, longevity belongs to those who build their identity on consistency rather than fanfare. Nugent-Hopkins embodies Foundation 1 of our curriculum: Identity Beyond Sport, paired with selfless team commitment.

Build lasting discipline and athletic character with Lornette's Foundations:
https://lornettedaye.com/foundations

Question for Edmonton: Where does Ryan Nugent-Hopkins rank among the most beloved Oilers of the modern era?

#RyanNugentHopkins #OilersHistory #EdmontonOilers #HockeyLoyalty #NHLMilestones #AthleteLongevity #CharacterMatters #OilCountry #EdmontonSports #LornettesFoundations`
  },
  {
    day: 7,
    title: "Post 7: The Micro-Habits of Winning Hockey",
    date: "Friday, Oct 30, 2026",
    scheduledAt: "2026-10-30T17:15:00.000Z", // 11:15 AM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png",
    caption: `WINNING HAPPENS IN THE INVISIBLE DETAILS.

Fans remember the game-winning shootout goal. Coaches study the micro-details that made it possible.

Notice Ryan Nugent-Hopkins on the backcheck in overtime:
- Stick on the ice cutting off passing lanes
- Shoulder checks before receiving pucks in traffic
- Positioning that denies Grade-A rush opportunities

THE SYSTEM CONTRACT:
Elite skill gets you to the NHL. Elite habits keep you there for 15 seasons. When pressure mounts, undisciplined players hunt for glory; disciplined athletes double down on the system.

Sharpen your technical and emotional discipline at Lornette's Foundations:
https://lornettedaye.com/foundations

Coaches: What is the one defensive habit you find hardest to instill in young offensive players?

#HockeyIQ #MicroHabits #EdmontonOilers #DefensiveDiscipline #HockeyCoaching #NHLStrategy #HighPerformance #SkillDevelopment #PlayerEvaluation #LornettesFoundations`
  },
  {
    day: 8,
    title: "Post 8: The Back-and-Forth Thriller Blueprint",
    date: "Saturday, Oct 31, 2026",
    scheduledAt: "2026-10-31T16:30:00.000Z", // 10:30 AM MDT
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-shootout-hero-poster.png",
    caption: `GAME MANAGEMENT IN CHAOS: 6-5 THRILLER BREAKDOWN.

When the scoreboard reads 6-5 and the game resembles a track meet, emotions run wild. 

Players start pinching unnecessarily. Defencemen gamble on pucks. The team that stabilizes first is the team that skates away with the victory.

THE PSYCHOLOGY OF STABILIZATION:
In track and field, when a race breaks down into a chaotic pack, the champion never matches the nervous frantic energy of the field. You maintain your stride length. You keep your shoulders loose. In hockey, Ryan Nugent-Hopkins provided that calming heartbeat for Edmonton on Thursday night.

Learn how to control emotional arousal in high-stakes competition with Lornette's Foundations:
https://lornettedaye.com/foundations

Fans: Do you prefer tight 2-1 defensive grinds or wild 6-5 shootouts? Debate below.

#HockeyAnalytics #GameManagement #EdmontonOilers #NHLRegularSeason #RogersPlace #SportsStrategy #MentalGame #Composure #GameBreakdown #LornettesFoundations`
  },
  {
    day: 9,
    title: "Post 9: Rogers Place Energy as a Competitive Advantage",
    date: "Sunday, Nov 01, 2026",
    scheduledAt: "2026-11-01T19:45:00.000Z", // 12:45 PM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png",
    caption: `THE SEVENTH SKATER: ROGERS PLACE AND THE OIL COUNTRY FAITHFUL.

There is no hockey environment in North America quite like Rogers Place when an Oilers game enters overtime.

The deafening roar when Ryan Nugent-Hopkins took his turn at center ice was an injection of pure adrenaline. But elite athletes know how to harness crowd energy without letting it distort their heart rate.

THE PERFORMANCE EDGE:
An untrained athlete lets external noise dictate internal tempo. A trained competitor channels the roar into razor-sharp focus. Nugent-Hopkins used the home ice wave to slow down the goaltender, not rush himself.

Develop your mental resilience and presence through Lornette's Foundations:
https://lornettedaye.com/foundations

Oil Country: What was the loudest moment you have ever personally experienced inside Rogers Place or Northlands Coliseum?

#OilCountry #RogersPlace #OilersNation #HomeIceAdvantage #HockeyCrowd #EdmontonCulture #NHLAtmosphere #PerformancePsychology #Focus #LornettesFoundations`
  },
  {
    day: 10,
    title: "Post 10: Champion Mindset in Athletic Development",
    date: "Monday, Nov 02, 2026",
    scheduledAt: "2026-11-02T18:45:00.000Z", // 11:45 AM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png",
    caption: `FOUNDATION 2: THE CHAMPION MINDSET UNDER SCRUTINY.

What separates good hockey players from franchise cornerstones?

It is not pure skating speed or wrist shot velocity. It is the refusal to accept complacency on ordinary days.

Ryan Nugent-Hopkins arrived in Edmonton as an 18-year-old phenom. Over 14 years, he evolved from a raw offensive talent into one of the most reliable complete centers in professional hockey. That evolution requires a growth mindset that embraces coaching, defensive responsibility, and physical sacrifice.

EXPLORE THE FOUNDATIONS:
Our 10 Athletic Foundations guide competitors through identity, mental poise, discipline systems, and career longevity. 

Start building your foundation today:
https://lornettedaye.com/foundations

Athletes and parents: What area of your mental game needs the most attention this season?

#ChampionMindset #AthleteDevelopment #HockeyTraining #YouthSports #SportsMentorship #LongTermDevelopment #EdmontonOilers #CharacterInSport #LornettesFoundations`
  },
  {
    day: 11,
    title: "Post 11: Tactical Breakdown of Nuge's Shootout Glide",
    date: "Tuesday, Nov 03, 2026",
    scheduledAt: "2026-11-03T19:15:00.000Z", // 12:15 PM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png",
    caption: `TACTICAL FILM STUDY: HOW NUGE FROZE THE HURRICANES GOALIE.

Watch the mechanics of Ryan Nugent-Hopkins' game-winning shootout attempt:

1. THE WIDE APPROACH: He enters the zone with speed, forcing the goaltender to honor both sides of the net.
2. THE SUDDEN DECELERATION: At the hash marks, he shifts his weight to a glide, reading the goalie's stance.
3. THE QUICK SNAP RELEASE: No wasted stickhandling. As soon as the five-hole opens slightly, the puck is off his blade.

THE DRILL PHILOSOPHY:
Clutch scoring is about deception, patience, and reading defensive micro-cues. In our athlete development sessions, we teach players to recognize opponent positioning before committing to an action.

Enhance your sports IQ and athletic execution with Lornette's Foundations:
https://lornettedaye.com/foundations

Hockey players: Do you prefer a quick wrist shot or an elaborate deke in a breakaway scenario? Why?

#FilmStudy #TacticalHockey #ShootoutGoal #HockeySkills #ScoringMechanics #OilersHockey #HockeyCoach #PlayerDevelopment #SkillWork #LornettesFoundations`
  },
  {
    day: 12,
    title: "Post 12: Mastering the Nervous System Under Pressure",
    date: "Wednesday, Nov 04, 2026",
    scheduledAt: "2026-11-04T18:00:00.000Z", // 11:00 AM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-shootout-hero-poster.png",
    caption: `TURNING COMPETITIVE ANXIETY INTO SHARP EXECUTION.

Every athlete feels the pit in their stomach before a game-deciding attempt. That is physiological arousal, not weakness.

The difference between elite performers and those who freeze is how they interpret that surge:
- Amateurs interpret a racing heart as fear.
- Champions interpret elevated adrenaline as biological readiness.

Ryan Nugent-Hopkins channeled his adrenaline into razor-focused puck protection and execution to beat Carolina.

THE POISE PLAYBOOK:
When pressure strikes:
1. Ground your feet.
2. Take three deliberate box breaths.
3. Lock into your immediate visual target.

Master physiological regulation and mental clarity with Lornette's Foundations:
https://lornettedaye.com/foundations

Coaches: How do you help your players normalize and manage pre-game nerves?

#NervousSystem #MentalPerformance #SportsPsychology #Breathwork #PoiseUnderPressure #EdmontonOilers #HighPerformanceHabits #AthleteHealth #LornettesFoundations`
  },
  {
    day: 13,
    title: "Post 13: Sustaining Excellence Across an 82-Game Campaign",
    date: "Thursday, Nov 05, 2026",
    scheduledAt: "2026-11-05T19:30:00.000Z", // 12:30 PM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png",
    caption: `THE MARATHON MINDSET: MANAGING THE 82-GAME NHL SEASON.

An NHL regular season is an endurance test of the highest order. Travel, back-to-backs, injuries, and emotional swings.

One great comeback win against Carolina in October does not make a season. But the resilience and trust built in tight games forms the bedrock for a deep playoff run in May and June.

THE SYSTEM ADVANTAGE:
Teams that survive the grueling regular season have established recovery routines, emotional balance, and unwavering trust in their depth players like Ryan Nugent-Hopkins.

Learn how Lornette's Foundations builds resilient athletes capable of sustaining peak output:
https://lornettedaye.com/foundations

Oil Country: What is the most critical area the Oilers need to maintain as the season moves into November?

#82GameMarathon #NHLSeason #EdmontonOilers #StanleyCupPursuit #TeamResilience #SportsRecovery #AthleticEndurance #LongTermSuccess #LornettesFoundations`
  },
  {
    day: 14,
    title: "Post 14: Better People, Better Players - The Lornette Daye Philosophy",
    date: "Friday, Nov 06, 2026",
    scheduledAt: "2026-11-06T18:15:00.000Z", // 11:15 AM MST
    isLiveNow: false,
    assetUrl: "https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png",
    caption: `BETTER PEOPLE MAKE BETTER PLAYERS.

In 40+ years of coaching Canadian national champions, Olympians, and elite competitors across hockey, golf, and track, one truth has never changed:

Athletic performance is an extension of human character.

When you observe Ryan Nugent-Hopkins, you see technical hockey mastery. But more importantly, you see humility, dedication to teammates, emotional balance in victory and defeat, and an unshakeable work ethic.

THAT IS THE LORNETTE DAYE STANDARD:
We do not just train athletes to win games. We prepare them to lead with dignity, thrive under pressure, and build a lasting legacy that outlives their sport.

Step into the complete athlete development journey with Lornette's Foundations:
https://lornettedaye.com/foundations

To Oil Country and sports communities everywhere: Thank you for standing behind athletes who lead with character and class.

#BetterPeopleBetterPlayers #LornettesFoundations #EdmontonOilers #RyanNugentHopkins #SportsLeadership #OlympicCoaching #CharacterDevelopment #YouthHockey #HighPerformance #OilCountry`
  }
];

// Validate invariants: zero asterisks, zero em dashes
let valid = true;
posts.forEach(p => {
  if (p.caption.includes('*')) {
    console.error(`ERROR: Post ${p.day} contains asterisks!`);
    valid = false;
  }
  if (p.caption.includes('—') || p.caption.includes('\u2014')) {
    console.error(`ERROR: Post ${p.day} contains em dashes!`);
    valid = false;
  }
});

if (!valid) {
  process.exit(1);
}

fs.writeFileSync('scripts/oilers-14day-data.json', JSON.stringify(posts, null, 2));
console.log('Successfully validated and generated scripts/oilers-14day-data.json with 14 posts!');
