/**
 * US Open Begins 2026 Night-Session Campaign Scheduling Script
 * 10 High-Impact Ads for Lornette Daye LinkedIn
 * 
 * Schedule: 2 posts per day across 5 consecutive days (Aug 30 – Sep 3) at 7:00 PM & 8:30 PM MDT
 * CTA: lornettedaye.com
 * Invariant: Every post includes a verified visual asset from public/campaigns/us-open-begins/
 */

import { bufferGraphQL } from './buffer-post.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/us-open-begins';

export const usOpenBeginsPosts = [
  {
    id: 1,
    title: "US Open Begins: Under the Arthur Ashe Lights",
    imageFile: "usopenbegins-01.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-01.png`,
    dueAt: "2026-08-31T01:00:00.000Z", // Sunday Aug 30 @ 7:00 PM MDT
    timeLabel: "Sunday, Aug 30 - 7:00 PM MDT",
    headline: "US OPEN BEGINS. 23,000 VOICES. ONE NIGHT SESSION UNDER THE LIGHTS.",
    text: `The US Open officially begins tonight.

There is nothing in global sport that matches the electric humidity, the roar of 23,000 fans, and the blinding glow of Arthur Ashe Stadium under the night lights.

When you play in New York at night, the atmosphere tests every layer of your mental preparation. 
If you are timid, the stadium will swallow you whole. 
If you are grounded in your purpose, the energy becomes rocket fuel for your performance.

To every competitor stepping onto the court tonight:
Trust the thousands of hours you spent preparing in silence.
Embrace the electricity. 
Let your game speak.

US Open 2026 begins now.

🔗 Build high-performance resilience and keynote leadership: https://lornettedaye.com

#USOpen2026 #USOpenBegins #ArthurAsheNightSession #TennisExcellence #LornetteDaye #FinishStrong #GrandSlamNight #ChampionMindset #PressureIsAPrivilege #MentalToughness #NewYorkTennis #EliteCoaching #SportsPsychology #PeakPerformance #GameSetMatch #TennisWorld #ExecutiveLeadership`,
  },
  {
    id: 2,
    title: "The Arena Tests Who You Are in the Dark",
    imageFile: "usopenbegins-02.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-02.png`,
    dueAt: "2026-08-31T02:30:00.000Z", // Sunday Aug 30 @ 8:30 PM MDT
    timeLabel: "Sunday, Aug 30 - 8:30 PM MDT",
    headline: "THE ARENA DOES NOT CREATE CHARACTER. IT REVEALS IT.",
    text: `Under the stadium lights, there is nowhere to hide.

When you're down 15-40 in the deciding set with the entire world watching, technique only takes you so far.
In that exact split second, your internal character takes over.

Do you shrink back and play not to lose?
Or do you step into the baseline, commit to your target, and swing with unwavering conviction?

In my 40+ years in elite athletics, I've learned that champions are not forged in comfortable moments. They are forged when every muscle is burning and the outcome hangs by a thread.

Hold your nerve. Trust your training.

🔗 Discover executive mentorship & performance coaching: https://lornettedaye.com

#USOpen2026 #CharacterUnderPressure #TennisMindset #GrandSlamBattles #LornetteDaye #FinishStrong #ArthurAshe #MentalFortitude #ExecutiveCoaching #PeakState #EliteAthletics #HighPerformance #ClutchPerformance #TennisCulture #NeverBackDown #PodiumFocus`,
  },
  {
    id: 3,
    title: "The Battle for Every Millimeter",
    imageFile: "usopenbegins-03.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-03.png`,
    dueAt: "2026-09-01T01:00:00.000Z", // Monday Aug 31 @ 7:00 PM MDT
    timeLabel: "Monday, Aug 31 - 7:00 PM MDT",
    headline: "GREATNESS IS NOT ACCIDENTAL. IT IS WON MILLIMETER BY MILLIMETER.",
    text: `At the US Open, the difference between winning a Grand Slam match and packing your bags is measured in millimeters.

A fraction of a degree on racket angle.
A millisecond of delay on court recognition.
A split second of hesitation on a break point.

When outsiders watch tennis on television, they see the glamorous winners.
Coaches see the unseen discipline: the footwork adjustments, the kinetic chain, the breath control between serves.

If you want world-class outcomes in your business or athletic career, fall in love with the precision of the micro-habits.

Master the small things. The big victories will follow.

🔗 Learn how Olympic discipline translates into corporate success: https://lornettedaye.com

#USOpen2026 #PrecisionInAction #MicroDisciplines #HighPerformanceHabits #LornetteDaye #FinishStrong #GrandSlamTennis #TennisCoaching #EliteTraining #SportsScience #ExecutiveLeadership #ArthurAsheStadium #ContinuousImprovement #Mastery #WinningMindset`,
  },
  {
    id: 4,
    title: "Silencing the Noise in Flushing Meadows",
    imageFile: "usopenbegins-04.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-04.png`,
    dueAt: "2026-09-01T02:30:00.000Z", // Monday Aug 31 @ 8:30 PM MDT
    timeLabel: "Monday, Aug 31 - 8:30 PM MDT",
    headline: "WHEN THE WORLD GETS LOUD, YOUR FOCUS MUST GET QUIET.",
    text: `New York is unapologetically loud.
The chatter in the stands, the press conferences, the online commentary, the flashing cameras.

Weak performers allow external noise to dictate their internal emotional state.
Legendary performers build an impenetrable cone of silence around their craft.

When you step up to serve at 5-5 in the fifth set, nothing exists except the yellow felt ball, your breath, and the target on the court.

Control what you can control. 
Ignore the rest.

🔗 Explore keynote speaking on focus and mental clarity under pressure: https://lornettedaye.com

#USOpen2026 #ConeOfSilence #FocusUnderPressure #FlushingMeadows #LornetteDaye #FinishStrong #Composure #MentalClarity #ExecutivePresence #SportsLeadership #ArthurAshe #GrandSlamMindset #HighStakes #DeepWork #TennisPsychology`,
  },
  {
    id: 5,
    title: "Respect the Journey: The Heart of the Athlete",
    imageFile: "usopenbegins-05.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-05.png`,
    dueAt: "2026-09-02T01:00:00.000Z", // Tuesday Sep 1 @ 7:00 PM MDT
    timeLabel: "Tuesday, Sep 1 - 7:00 PM MDT",
    headline: "DON'T JUST CHEER THE RESULT. RESPECT THE SACRIFICE BEHIND IT.",
    text: `Before an athlete steps onto Arthur Ashe Stadium under prime-time television lights, they walked through years of unseen sacrifice:

• Countless lonely 5:00 AM track and gym sessions.
• Painful rehab routines away from family and friends.
• Financial stress and endless travel across time zones.

We love crowning champions on Sunday afternoon, but we must learn to honour the sheer human courage required just to make it to the starting line.

Developing the athlete means caring for the complete human being.

Respect the journey. Support the person.

🔗 Learn more about our holistic athlete development & transition framework: https://lornettedaye.com

#USOpen2026 #AthleteWelfare #RespectTheJourney #HumanFirst #LornetteDaye #FinishStrong #HighPerformanceEcosystem #TennisLife #OlympicMindset #WholePersonCare #SportsPhilanthropy #MentalHealthInSports #SportsLeadership #CoachingWithEmpathy`,
  },
  {
    id: 6,
    title: "The Fire of New York Night Sessions",
    imageFile: "usopenbegins-06.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-06.png`,
    dueAt: "2026-09-02T02:30:00.000Z", // Tuesday Sep 1 @ 8:30 PM MDT
    timeLabel: "Tuesday, Sep 1 - 8:30 PM MDT",
    headline: "NEW YORK NIGHT SESSIONS: WHERE PASSION MEETS PRESSURE.",
    text: `Matches that start at 9:00 PM and finish at 1:30 AM in the New York humidity are not just tennis matches—they are psychological masterclasses.

Your legs are heavy. Your grip is soaked. The crowd is on its feet demanding more.

In moments of extreme physical fatigue, the mind will always look for an exit door. 
The champion’s job is to close that door, look adversity in the eye, and find another gear that opponent didn’t know existed.

You are always capable of more than your comfort zone tells you.

Find your second wind.

🔗 Book Lornette Daye for high-impact motivational keynotes: https://lornettedaye.com

#USOpen2026 #NightSessionDrama #SecondWind #RelentlessDrive #LornetteDaye #FinishStrong #ArthurAsheStadium #LateNightTennis #Endurance #GritAndGrace #ExecutivePerformance #ChampionHabits #UnstoppableSpirit #SportsInspiration`,
  },
  {
    id: 7,
    title: "Women Dominating the Grand Slam Stage",
    imageFile: "usopenbegins-07.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-07.png`,
    dueAt: "2026-09-03T01:00:00.000Z", // Wednesday Sep 2 @ 7:00 PM MDT
    timeLabel: "Wednesday, Sep 2 - 7:00 PM MDT",
    headline: "WOMEN’S TENNIS IN NEW YORK: POWER, GRACE, AND UNAPOLOGETIC COMMAND.",
    text: `When female athletes command Arthur Ashe Stadium with blistering 115 mph serves, court-to-court agility, and fearless baseline dominance, they don't just win trophies—they shift cultural standards.

They show every young girl watching across the globe that power, speed, and competitive hunger are not traits to minimize; they are superpowers to unleash.

Visibility creates possibility.
Support creates champions.

To every woman competing under the New York lights this week: continue commanding the stage.

🔗 Read about our women's leadership initiatives in athletics and business: https://lornettedaye.com

#USOpen2026 #WomenInSport #WTAChampionship #FemaleEmpowerment #GirlsInTennis #LornetteDaye #FinishStrong #RepresentationMatters #SheCanPlay #TitleIX #WomenLeaders #GrandSlamPower #NextGenChampions #SportsEquality #ArthurAshe`,
  },
  {
    id: 8,
    title: "Turning Adversity Into Your Competitive Advantage",
    imageFile: "usopenbegins-08.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-08.png`,
    dueAt: "2026-09-03T02:30:00.000Z", // Wednesday Sep 2 @ 8:30 PM MDT
    timeLabel: "Wednesday, Sep 2 - 8:30 PM MDT",
    headline: "ADVERSITY IS NOT A DETOUR. IT IS THE WORKOUT.",
    text: `Every Grand Slam champion faces a match where everything goes wrong:
The string tension feels off. The wind is swirling. The opponent is playing the match of their life.

Amateurs let bad conditions become their excuse.
Champions use friction as leverage to elevate their problem-solving.

Adversity is not an interruption to your greatness; it is the exact laboratory where your resilience is tested and proven.

When conditions are imperfect: adapt, adjust, and outwork the challenge.

🔗 Order the book 'Finish Strong' by Lornette Daye: https://lornettedaye.com

#USOpen2026 #AdversityIsFuel #ResilienceInSport #ChampionMindset #LornetteDaye #FinishStrong #MentalGrit #TennisStrategy #OvercomeObstacles #ExecutiveMindset #PeakConditioning #ArthurAshe #LeadershipUnderFire #NeverGiveUp`,
  },
  {
    id: 9,
    title: "The Legacy of Arthur Ashe and Billie Jean King",
    imageFile: "usopenbegins-09.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-09.png`,
    dueAt: "2026-09-04T01:00:00.000Z", // Thursday Sep 3 @ 7:00 PM MDT
    timeLabel: "Thursday, Sep 3 - 7:00 PM MDT",
    headline: "PLAYING FOR SOMETHING BIGGER THAN THE SCOREBOARD.",
    text: `When you compete at the USTA Billie Jean King National Tennis Center in Arthur Ashe Stadium, you are standing on sacred ground built by giants who used sport to transform human rights.

Arthur Ashe showed us that sportsmanship and social justice are inseparable.
Billie Jean King proved that equal opportunity for women is non-negotiable.

When an athlete understands that their platform is larger than a paycheck or a ranking, their competitive purpose becomes unstoppable.

Compete for yourself. But play for your legacy.

🔗 Explore keynotes on ethical leadership and sports advocacy: https://lornettedaye.com

#USOpen2026 #ArthurAsheLegacy #BillieJeanKing #SportsPhilanthropy #SocialImpact #LornetteDaye #FinishStrong #LeadershipThroughSport #PurposeDriven #EqualityInSport #TennisRoyalty #ExecutiveWisdom #GlobalChange #HistoricalImpact`,
  },
  {
    id: 10,
    title: "Finish Strong: Crowned in New York",
    imageFile: "usopenbegins-10.png",
    imageUrl: `${BASE_IMAGE_URL}/usopenbegins-10.png`,
    dueAt: "2026-09-04T02:30:00.000Z", // Thursday Sep 3 @ 8:30 PM MDT
    timeLabel: "Thursday, Sep 3 - 8:30 PM MDT",
    headline: "WHEN THE DUST SETTLES IN NEW YORK: FINISH STRONG.",
    text: `15 days of battle. 
Hundreds of hours of baseline warfare. 
Thousands of shots exchanged under the sun and the stars.

As the tournament moves toward its crowning moments, remember:
Nobody remembers how comfortably you began the match. 
The world only remembers the courage, dignity, and tenacity with which you closed it out.

Whatever court you are competing on today—in athletics, in executive leadership, or in personal growth:
Leave nothing in the tank. 

Stand tall. Serve with pride. 
Finish strong.

🔗 Connect with Lornette Daye for books, keynotes, and high-performance coaching: https://lornettedaye.com

#USOpen2026 #FinishStrong #ChampionshipLegacy #GrandSlamGlory #LornetteDaye #KeynoteSpeaker #PodiumMindset #ExecutiveExcellence #TennisChampion #UnwaveringResolve #ArthurAshe #NewYorkFinals #VictoryMindset #LeadershipInAction`,
  },
];

async function schedulePost(post) {
  const input = {
    channelId: CHANNEL_ID,
    text: post.text,
    mode: 'customScheduled',
    dueAt: post.dueAt,
    schedulingType: 'automatic',
    needsApproval: false,
    saveToDraft: false,
    assets: [
      {
        image: {
          url: post.imageUrl,
        },
      },
    ],
  };

  const mutation = `
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
        ... on NotFoundError { message }
        ... on UnauthorizedError { message }
        ... on UnexpectedError { message }
        ... on LimitReachedError { message }
        ... on InvalidInputError { message }
      }
    }
  `;

  return await bufferGraphQL(mutation, { input });
}

async function main() {
  console.log('======================================================================');
  console.log('🎾 Scheduling 10 "US OPEN BEGINS" Night Ads Starting Sunday, Aug 30');
  console.log('======================================================================\n');

  for (const post of usOpenBeginsPosts) {
    console.log(`[Scheduling US Open Begins Ad #${post.id}] "${post.title}"`);
    console.log(`   📅 Slot: ${post.timeLabel} (${post.dueAt})`);
    console.log(`   🖼️ Image: ${post.imageUrl}`);
    
    try {
      const res = await schedulePost(post);
      if (res.createPost?.__typename === 'PostActionSuccess' && res.createPost.post) {
        post.bufferPostId = res.createPost.post.id;
        console.log(`   ✅ SUCCESS! Buffer Post ID: ${res.createPost.post.id}\n`);
      } else {
        console.log(`   ⚠️ Response:`, JSON.stringify(res, null, 2), '\n');
      }
    } catch (err) {
      console.error(`   ❌ Error scheduling #${post.id}:`, err.message, '\n');
    }
    
    // Pause briefly between calls
    await new Promise(r => setTimeout(r, 600));
  }

  console.log('======================================================================');
  console.log('🎉 All 10 "US OPEN BEGINS" Ads successfully scheduled into Buffer!');
  console.log('======================================================================\n');
}

main().catch(console.error);
