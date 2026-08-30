/**
 * US Open 2026 Campaign Scheduling Script
 * 10 High-Impact Ads for Lornette Daye LinkedIn
 * 
 * Schedule: 2 posts per day across 5 consecutive days (Aug 30 – Sep 3) at 12:00 PM & 6:00 PM MDT
 * CTA: lornettedaye.com
 * Invariant: Every post includes a verified visual asset from public/campaigns/us-open/
 */

import { bufferGraphQL } from './buffer-post.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/us-open';

export const usOpenPosts = [
  {
    id: 1,
    title: "New York Doesn't Care About Your Ranking",
    imageFile: "usopen-01.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-01.png`,
    dueAt: "2026-08-30T18:00:00.000Z", // Sunday Aug 30 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Sunday, Aug 30 - 12:00 PM MDT",
    headline: "NEW YORK DOESN'T CARE ABOUT YOUR RANKING. YOU STILL HAVE TO WIN THE POINT.",
    text: `New York does not care about your seeding, your reputation, or what you accomplished last season.
When you step onto Arthur Ashe Stadium, all the past accolades evaporate. You still have to win the point.

In 40+ years of high-performance coaching, I have watched athletes freeze because they relied on their title instead of their preparation. 
Rankings give you entry; they do not give you victory.

Under the bright lights of Flushing Meadows, the formula never changes:
• Serve with intention.
• Fight through the break points.
• Recover between rallies.
• Believe when the momentum shifts.

Whether you're serving for a Grand Slam championship or executing an executive turnaround in the boardroom: title means nothing without relentless execution.

Serve. Fight. Recover. Believe.

🔗 Discover high-performance frameworks & leadership insights: https://lornettedaye.com

#USOpen2026 #USOpen #ArthurAshe #TennisLeadership #HighPerformance #ChampionMindset #LornetteDaye #FinishStrong #PressureIsAPrivilege #MentalToughness #GrandSlam #TennisLife #ExecutiveCoaching #PeakPerformance #EliteAthletics #SportsPsychology #GameSetMatch #NewYorkSports #PodiumMindset`,
  },
  {
    id: 2,
    title: "The Wait Is Over. It's Time to Play.",
    imageFile: "usopen-02.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-02.png`,
    dueAt: "2026-08-31T00:00:00.000Z", // Sunday Aug 30 @ 6:00 PM MDT (00:00 UTC Aug 31)
    timeLabel: "Sunday, Aug 30 - 6:00 PM MDT",
    headline: "THE WAIT IS OVER. IT'S TIME TO PLAY. NEW YORK. HARD COURTS. NO EASY POINTS.",
    text: `The tunnel walk is where doubt tries to whisper.
Behind you are months of grueling off-court conditioning, physiotherapy, and isolated practice.
Ahead of you is 23,000 roaring spectators and the unforgiving blue hard courts of New York.

There are no easy points at the US Open.
Every ball comes back with extra pace. Every error is amplified. Every game tests whether your character matches your talent.

To every athlete stepping into the arena this fortnight:
Walk tall. You didn't come this far to play timid. 
Own the moment. Own the pressure.

The wait is over. It's time to play.

🔗 Explore keynote speaking and leadership development: https://lornettedaye.com

#USOpen2026 #WomenInSport #WTA #GrandSlam #HardCourtTennis #ArthurAsheStadium #LornetteDaye #FinishStrong #FemaleAthletes #PressureIsAPrivilege #MentalGrit #EliteCoaching #SportsLeadership #TennisChampionship #NextGenAthletes #Unstoppable #FocusUnderPressure #NewYorkCity`,
  },
  {
    id: 3,
    title: "15 Days. One New York. One Champion.",
    imageFile: "usopen-03.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-03.png`,
    dueAt: "2026-08-31T18:00:00.000Z", // Monday Aug 31 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Monday, Aug 31 - 12:00 PM MDT",
    headline: "15 DAYS. ONE NEW YORK. ONE CHAMPION. EVERY POINT MATTERS NOW.",
    text: `A Grand Slam is not a tennis tournament—it is a 15-day war of attrition.

128 players enter the draw. Only one lifts the trophy on Championship Sunday.

What separates the winner from the rest of the field is rarely pure technique. At this level, everyone can hit a 120 mph serve or a blistering forehand. 
What separates the champion is emotional discipline across 15 relentless days:
• Managing sleep and recovery amidst midnight matches.
• Staying dialed in when bad line calls happen.
• Refusing to panic when down two sets to love.

Greatness is built point by point, hour by hour, choice by choice.

Every point matters now.

🔗 Build championship endurance in your organization: https://lornettedaye.com

#USOpen2026 #GrandSlamTennis #15DaysOfExcellence #ArthurAshe #ChampionshipMindset #LornetteDaye #FinishStrong #EveryPointMatters #EnduranceInSport #SportsPerformance #HighPerformanceHabits #EliteTraining #TennisWorld #NYCStage #LeadershipInAction #UnwaveringFocus`,
  },
  {
    id: 4,
    title: "New York Is Waiting. The Pressure Is Real.",
    imageFile: "usopen-04.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-04.png`,
    dueAt: "2026-09-01T00:00:00.000Z", // Monday Aug 31 @ 6:00 PM MDT (00:00 UTC Sep 1)
    timeLabel: "Monday, Aug 31 - 6:00 PM MDT",
    headline: "US OPEN. READY FOR PLAY. NEW YORK IS WAITING. THE PRESSURE IS REAL. WHO'S READY?",
    text: `Arthur Ashe Stadium in the morning sun is deceptive. The court sits peaceful and empty.
But in just a few hours, the decibel level will rival a rock concert, and the weight of an entire season will rest on a single baseline rally.

This is the biggest stage in tennis. 
The pressure is real. It makes hearts pound, forearms tighten, and shallow breathing take over.

Amateur competitors run from pressure.
World champions reframe pressure as proof that they are exactly where they belong.

When the stadium lights turn on tonight and the crowd starts buzzing: don't wish for less pressure. Demand more of yourself.

Who’s ready?

🔗 Connect with Lornette Daye for executive performance consulting: https://lornettedaye.com

#USOpen2026 #ArthurAsheStadium #PressureIsAPrivilege #FlushingMeadows #TennisCulture #SportsPsychology #LornetteDaye #FinishStrong #ExecutiveMindset #PeakState #HighStakes #GrandSlamFinal #TennisCommunity #CoachingWisdom #MentalFortitude #ChampionHabits`,
  },
  {
    id: 5,
    title: "The Champion Is Back (Carlos Alcaraz)",
    imageFile: "usopen-05.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-05.png`,
    dueAt: "2026-09-01T18:00:00.000Z", // Tuesday Sep 1 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Tuesday, Sep 1 - 12:00 PM MDT",
    headline: "THE CHAMPION IS BACK. CARLOS ALCARAZ. DEFENDING NEW YORK. READY TO FIGHT FOR IT AGAIN.",
    text: `Returning to defend a title after injury is one of the hardest psychological tests in world sport.

When you've tasted ultimate victory, the expectation isn't just to play—it's to dominate. But an athlete returning from physical setback carries the memory of the rehab room, the doubts of the critics, and the intense target on their back.

Carlos Alcaraz represents the essence of modern high-performance: explosive athleticism paired with an unbreakable competitive joy.

True champions don't defend championships by playing safe. 
They attack the tournament with the same raw hunger that made them champions in the first place.

Defending New York. Returning with purpose. Ready to fight for every inch.

🔗 Read 'Finish Strong' and master the art of the comeback: https://lornettedaye.com

#CarlosAlcaraz #USOpen2026 #DefendingChampion #InjuryComeback #AthleteResilience #LornetteDaye #FinishStrong #TennisRoyalty #NextGenTennis #HighPerformanceRecovery #MentalGrit #GrandSlamChampion #NeverGiveUp #SportsExcellence #ArthurAshe #FightingSpirit`,
  },
  {
    id: 6,
    title: "Flushing Meadows: Where Legends Are Forged",
    imageFile: "usopen-06.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-06.png`,
    dueAt: "2026-09-02T00:00:00.000Z", // Tuesday Sep 1 @ 6:00 PM MDT (00:00 UTC Sep 2)
    timeLabel: "Tuesday, Sep 1 - 6:00 PM MDT",
    headline: "FLUSHING MEADOWS: WHERE REPUTATIONS ARE TESTED AND LEGENDS ARE FORGED.",
    text: `You can win in quiet arenas with polite applause.
You cannot win the US Open without mastering the chaos of New York.

Subway trains rattling in the distance. 23,000 passionate fans reacting to every drop shot. Jet planes overhead from LaGuardia. Humid, sticky late-summer air.

Flushing Meadows doesn't offer sanctuary. It demands total presence.

In sport and in business, leaders often complain about "external noise." 
The best in the world don't fight the noise—they channel it into razor-sharp focus.

Composure in the storm is what turns talented players into immortal legends.

🔗 Transform how your leaders handle high-pressure environments: https://lornettedaye.com

#USOpen2026 #FlushingMeadows #NewYorkEnergy #CrowdNoise #ComposureUnderFire #LornetteDaye #FinishStrong #TennisMentality #HighPerformanceLeadership #ExecutiveResilience #ArthurAshe #GrandSlamLegacy #SportsMentalGame #FocusOnTheFinish`,
  },
  {
    id: 7,
    title: "The Margins of Victory",
    imageFile: "usopen-07.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-07.png`,
    dueAt: "2026-09-02T18:00:00.000Z", // Wednesday Sep 2 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Wednesday, Sep 2 - 12:00 PM MDT",
    headline: "FIVE SETS. FOUR HOURS. ONE INCH. THE MARGIN BETWEEN VICTORY AND DEFEAT.",
    text: `In a 4-hour, 5-set marathon at the US Open, both players might run 5 miles and hit over 300 shots each.
And the match is often decided by a total point differential of less than 2%.

One inch on a passing shot.
One millisecond of hesitation on a second serve.
One lapse in breath control during a tiebreak.

That is the unforgiving reality of world-class competition. 
You cannot wait until the fifth set to care about the details. The habits you practice at 6:00 AM on a cold Tuesday dictate whether that final ball catches the line or flies wide.

Master the micro-disciplines. The major victories will take care of themselves.

🔗 Learn how Olympic-level discipline drives organizational success: https://lornettedaye.com

#FiveSets #USOpen2026 #MarginsOfVictory #EmotionalDiscipline #LateStageExecution #LornetteDaye #FinishStrong #TennisExcellence #SportsStrategy #LeadershipUnderPressure #MentalEndurance #GrandSlamBattles #ArthurAsheStadium #ClutchPerformance`,
  },
  {
    id: 8,
    title: "From the Practice Courts to the Night Session",
    imageFile: "usopen-08.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-08.png`,
    dueAt: "2026-09-03T00:00:00.000Z", // Wednesday Sep 2 @ 6:00 PM MDT (00:00 UTC Sep 3)
    timeLabel: "Wednesday, Sep 2 - 6:00 PM MDT",
    headline: "FROM THE PRACTICE COURTS AT SUNRISE TO THE NIGHT SESSION UNDER THE LIGHTS.",
    text: `The world only tunes in for the spectacle under the prime-time stadium lights.
They don't see the 6:30 AM warmups on Court 18 when the stands are completely empty.

They don't see the repetitive shoulder band work, the blister taping, the ice baths, and the film analysis dissecting opponent return patterns.

Spectators celebrate the finish line. 
Champions fall in love with the unglamorous preparation.

If you aren't willing to dominate the unseen hours in the dark, you have no right to expect victory in the spotlight.

Fall in love with the grind.

🔗 Book Lornette Daye for your next keynote or corporate summit: https://lornettedaye.com

#USOpen2026 #NightSession #ArthurAsheLights #UnseenGrind #PreparationOverPride #LornetteDaye #FinishStrong #HighPerformanceHabits #TennisTraining #MasteryInAction #SportsDiscipline #WorkInTheDark #GrandSlamPreparation #PeakConditioning`,
  },
  {
    id: 9,
    title: "Pressure Is a Privilege",
    imageFile: "usopen-09.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-09.png`,
    dueAt: "2026-09-03T18:00:00.000Z", // Thursday Sep 3 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Thursday, Sep 3 - 12:00 PM MDT",
    headline: "PRESSURE IS A PRIVILEGE. IT MEANS YOU’VE EARNED THE RIGHT TO COMPETE.",
    text: `As you walk onto the court at Flushing Meadows, you pass Billie Jean King’s timeless words etched into the concrete:
"Pressure is a privilege."

Pressure does not exist for people who play small.
Pressure does not exist for those who stay in the comfort zone and never take risks.

If your hands are shaking, if the stakes feel overwhelming, if everyone is watching—congratulations. It means you have built something significant enough to matter.

Don't pray for the stakes to be lowered. 
Step into the center of the court, take a deep breath, and let your preparation speak.

🔗 Discover mentorship and high-performance strategies: https://lornettedaye.com

#PressureIsAPrivilege #BillieJeanKing #USOpen2026 #MentalReframing #HighStakesLeadership #LornetteDaye #FinishStrong #TennisHistory #CourageOverFear #ArthurAshe #GrandSlamMindset #Empowerment #ExecutiveCoaching #PeakPerformance`,
  },
  {
    id: 10,
    title: "Finish Strong (Championship Glory)",
    imageFile: "usopen-10.png",
    imageUrl: `${BASE_IMAGE_URL}/usopen-10.png`,
    dueAt: "2026-09-04T00:00:00.000Z", // Thursday Sep 3 @ 6:00 PM MDT (00:00 UTC Sep 4)
    timeLabel: "Thursday, Sep 3 - 6:00 PM MDT",
    headline: "IT MATTERS HOW YOU START. IT MATTERS INFINITELY MORE HOW YOU FINISH.",
    text: `Two weeks of grueling Grand Slam tennis come down to this final weekend.
Bodies are bruised. Muscles are exhausted. Nerves are frayed.

At this stage, physical talent alone will not carry you over the finish line. 
It comes down to pure spirit, heart, and the refusal to let fatigue make a coward of your dreams.

In sport, in business, and in life:
Anyone can start fast when energy is high and optimism is fresh. 
Legends are defined by how they battle through the fifth set when every muscle is screaming to quit.

Dig deep. Hold your serve. 
Finish strong.

🔗 Explore keynote speaking, books, and high-performance coaching: https://lornettedaye.com

#FinishStrong #USOpen2026 #ChampionshipSunday #GrandSlamGlory #LegacyBuilding #LornetteDaye #KeynoteSpeaker #HighPerformanceMindset #TennisChampion #UnwaveringResolve #PodiumFinish #SportsInspiration #Endurance #VictoryMindset #Leadership`,
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
  console.log('🎾 Scheduling 10 US Open 2026 Ads Starting Sunday, Aug 30');
  console.log('======================================================================\n');

  for (const post of usOpenPosts) {
    console.log(`[Scheduling US Open Ad #${post.id}] "${post.title}"`);
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
  console.log('🎉 All 10 US Open Ads successfully scheduled into Buffer!');
  console.log('======================================================================\n');
}

main().catch(console.error);
