/**
 * Destiny Spurlock Track & Field Leadership Campaign
 * 10 High-Impact Posts for Lornette Daye LinkedIn
 * 
 * Schedule: Every 3 days across September (Sep 2, 5, 8, 11, 14, 17, 20, 23, 26, 29 at 1:00 PM MDT)
 * CTA: lornettedaye.com
 * Invariant: Every post includes a verified visual asset from public/campaigns/destiny-spurlock/
 */

import { bufferGraphQL } from './buffer-post.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/destiny-spurlock';

export const destinySpurlockPosts = [
  {
    id: 1,
    title: "Developing the Athlete, Preparing the Person",
    imageFile: "destinyspurlock-01.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-01.png`,
    dueAt: "2026-09-02T19:00:00.000Z", // Wednesday Sep 2 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Wednesday, Sep 2 - 1:00 PM MDT",
    headline: "DEVELOPING THE ATHLETE. PREPARING THE PERSON. EMPOWERING DESTINY SPURLOCK.",
    text: `Coaching an athlete is never just about the digits on a stopwatch.

In 40+ years of high-performance coaching, I have seen fast runners break under pressure because their identity was tied solely to their race results.
And I have seen resilient athletes like Destiny Spurlock transform into unstoppable forces because their foundation was built on character, purpose, and self-worth.

When we invest in the human being inside the jersey:
• Confidence replaces fear.
• Preparation replaces anxiety.
• The podium takes care of itself.

Developing the athlete. Preparing the person. Building the future.

🔗 Explore athlete mentorship & high-performance coaching: https://lornettedaye.com

#DestinySpurlock #TrackAndField #AthleteMentorship #StudentAthlete #SprintCoach #LornetteDaye #FinishStrong #HighPerformance #WomenInSport #NCAATrack #YouthEmpowerment #CharacterInSport #HolisticCoaching #AthleteDevelopment #FutureLeaders #SpeedAndPower`,
  },
  {
    id: 2,
    title: "Explosive Speed Starts in the Mind",
    imageFile: "destinyspurlock-02.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-02.png`,
    dueAt: "2026-09-05T19:00:00.000Z", // Saturday Sep 5 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Saturday, Sep 5 - 1:00 PM MDT",
    headline: "EXPLOSIVE SPEED STARTS IN THE MIND: THE ANATOMY OF A SPRINT CHAMPION.",
    text: `A 100-meter sprint is won before the starter's gun ever fires.

In the starting blocks, your heart is pounding at 160 BPM. The stadium is silent. 
If your mind is tense, your shoulders tighten, your hips drop, and your stride locks up.
If your mind is tranquil and razor-sharp, your nervous system fires with maximum kinetic force.

Destiny Spurlock demonstrates the rare combination of explosive physical power and absolute mental composure under pressure.

Speed is not just muscle; speed is neurological stillness.

Control your mind. Release your power.

🔗 Learn Olympic-level mental conditioning and executive focus: https://lornettedaye.com

#SprintMechanics #StartingBlocks #SpeedTraining #MindsetMatters #LornetteDaye #DestinySpurlock #FinishStrong #TrackNation #SprintTraining #MentalToughness #SportsScience #PeakPerformance #AthleticExcellence #HighPerformanceMindset #FastTwitch`,
  },
  {
    id: 3,
    title: "Balancing Academics and Athletics",
    imageFile: "destinyspurlock-03.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-03.png`,
    dueAt: "2026-09-08T19:00:00.000Z", // Tuesday Sep 8 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Tuesday, Sep 8 - 1:00 PM MDT",
    headline: "BALANCING ACADEMICS AND ATHLETICS: THE UNSEEN REALITY OF THE STUDENT-ATHLETE.",
    text: `6:00 AM: Weight room and plyometrics.
9:00 AM: University lectures and lab coursework.
2:30 PM: Track session, sprint intervals, and video review.
5:30 PM: Physio treatment and recovery cold tubs.
7:30 PM: Study hall and exam preparation until midnight.

Then wake up and do it all over again.

Collegiate student-athletes like Destiny Spurlock manage schedules that would exhaust full-time corporate executives.
They learn time management, emotional grit, and hyper-accountability long before they enter the professional workforce.

Hire student-athletes. They already know how to deliver world-class results under relentless pressure.

🔗 Connect with Lornette Daye for leadership keynotes and corporate summits: https://lornettedaye.com

#StudentAthlete #NCAALife #AcademicExcellence #DualCareer #DestinySpurlock #LornetteDaye #FinishStrong #ExecutiveDiscipline #TimeManagement #YouthLeadership #WorkEthic #NextGenTalent #CollegeTrack #FutureExecutives`,
  },
  {
    id: 4,
    title: "When You Back Young Women in Sport",
    imageFile: "destinyspurlock-04.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-04.png`,
    dueAt: "2026-09-11T19:00:00.000Z", // Friday Sep 11 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Friday, Sep 11 - 1:00 PM MDT",
    headline: "WHEN YOU BACK YOUNG WOMEN IN SPORT, YOU CHANGE GENERATIONS.",
    text: `When a young woman steps onto the track and discovers her physical strength, something permanent shifts in her identity.

She learns that taking up space is not a disruption; it is her right.
She learns that speed and power belong to her.
She learns that she can stare down fierce competition and hold her line with pride.

Destiny Spurlock represents the future of women in athletics: unapologetically ambitious, technically disciplined, and deeply committed to lifting others as she climbs.

Invest in female athletics. The returns ripple through families, communities, and boardrooms for decades.

🔗 Learn about our women's sports leadership and youth empowerment initiatives: https://lornettedaye.com

#WomenInSport #InvestInWomen #GirlsInTrack #DestinySpurlock #LornetteDaye #FinishStrong #RepresentationMatters #FemaleAthletes #EmpowermentThroughSport #TitleIXLegacy #WomenInLeadership #NextGenChampions #SheCanFly`,
  },
  {
    id: 5,
    title: "Overcoming the Injury Wall",
    imageFile: "destinyspurlock-05.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-05.png`,
    dueAt: "2026-09-14T19:00:00.000Z", // Monday Sep 14 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Monday, Sep 14 - 1:00 PM MDT",
    headline: "OVERCOMING THE INJURY WALL: PATIENCE, REHABILITATION & FAITH.",
    text: `Every serious sprinter knows the heartbreak of the hamstring tweak, the ankle sprain, or the uncooperative tendon.

When you're forced to watch from the sidelines while your competitors are racing, doubt will test every corner of your soul.
"Will I get my top-end speed back?"
"Did I lose my edge?"

The athletes who emerge stronger are those who treat the rehabilitation room with the exact same work ethic as the track.
They build mental toughness in the dark.
They sharpen their nutrition, mobility, and biomechanics.

A setback is never your finish line. It is the setup for your strongest season yet.

Keep the faith. Trust the process.

🔗 Order 'Finish Strong' by Lornette Daye and conquer life's setbacks: https://lornettedaye.com

#InjuryComeback #AthleteRehab #ResilienceInSport #DestinySpurlock #LornetteDaye #FinishStrong #OvercomingSetbacks #PatienceAndFaith #MentalGrit #TrackAndField #SportsMedicine #ComebackStronger #UnwaveringBelief`,
  },
  {
    id: 6,
    title: "From Grassroots Dreams to Collegiate Excellence",
    imageFile: "destinyspurlock-06.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-06.png`,
    dueAt: "2026-09-17T19:00:00.000Z", // Thursday Sep 17 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Thursday, Sep 17 - 1:00 PM MDT",
    headline: "FROM GRASSROOTS DREAMS TO COLLEGIATE EXCELLENCE.",
    text: `Look at any collegiate athlete standing on the podium.
Behind that medal is a municipal track with cracked rubber, parents who drove through snowstorms to weekend qualifiers, and volunteer coaches who gave up their Saturday mornings for years.

Destiny Spurlock’s rise is a testament to what happens when raw talent meets relentless work and intentional community support.

We cannot wait until athletes are world champions to support them.
We must invest in them while they are still in the grassroots pipeline.

Potential is everywhere. Opportunity is what unlocks it.

🔗 Discover our grassroots youth athletics & mentorship programs: https://lornettedaye.com

#GrassrootsAthletics #YouthDevelopment #PathwayToPodium #DestinySpurlock #LornetteDaye #FinishStrong #CommunityImpact #AccessToSport #TrackCoach #SportsPhilanthropy #YouthEmpowerment #CollegiateAthletics #OlympicJourney`,
  },
  {
    id: 7,
    title: "The Value of Athlete Mentorship",
    imageFile: "destinyspurlock-07.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-07.png`,
    dueAt: "2026-09-20T19:00:00.000Z", // Sunday Sep 20 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Sunday, Sep 20 - 1:00 PM MDT",
    headline: "THE VALUE OF ATHLETE MENTORSHIP: WALKING ALONGSIDE THE NEXT GENERATION.",
    text: `When I was competing as a Canadian National Sprint Champion and Olympian coach, the greatest asset I had was not a pair of spikes—it was a mentor who believed in me when I couldn't see the road ahead.

Mentorship is the difference between a talented athlete who burns out from stress, and a resilient leader who turns obstacles into stepping stones.

Walking alongside rising stars like Destiny Spurlock is my life's greatest joy. 
Passing down four decades of track wisdom, psychological regulation, and life preparation ensures the torch burns even brighter for the next generation.

Never underestimate the power of speaking belief into a young person's life.

🔗 Explore executive mentorship & athlete guidance programs: https://lornettedaye.com

#AthleteMentorship #CoachingWisdom #GenerationalImpact #DestinySpurlock #LornetteDaye #FinishStrong #PassTheTorch #LeadershipDevelopment #MentorshipMatters #TrackAndField #NextGeneration #InspireYouth #LifeCoaching`,
  },
  {
    id: 8,
    title: "The 100M & 200M Dash: Where Grit Meets the Curve",
    imageFile: "destinyspurlock-08.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-08.png`,
    dueAt: "2026-09-23T19:00:00.000Z", // Wednesday Sep 23 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Wednesday, Sep 23 - 1:00 PM MDT",
    headline: "THE 100M & 200M DASH: WHERE TECHNIQUE MEETS RELENTLESS GRIT.",
    text: `The 200-meter dash is a masterclass in controlled violence.

You explode out of the blocks, slingshot off the bend against immense centrifugal force, and then face the final 80-meter straightaway where your legs feel like lead and oxygen is scarce.

Casual spectators think sprinting is about straining and clenching teeth.
Elite sprinters like Destiny Spurlock know the secret:
The one who stays relaxed, keeps their knee drive high, and maintains posture in the final 30 meters is the one who crosses the line first.

When fatigue hits: do not panic. Stay tall. Execute your form.

🔗 Master high-performance execution under intense pressure: https://lornettedaye.com

#SprintMechanics #200mDash #TrackAndField #SpeedTechnique #DestinySpurlock #LornetteDaye #FinishStrong #PostureUnderPressure #SpeedKillz #SprintForm #HighPerformance #AthleticsCanada #NCAASprints`,
  },
  {
    id: 9,
    title: "Preparing for Life Beyond the Track",
    imageFile: "destinyspurlock-09.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-09.png`,
    dueAt: "2026-09-26T19:00:00.000Z", // Saturday Sep 26 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Saturday, Sep 26 - 1:00 PM MDT",
    headline: "THE COMPLETE ATHLETE: PREPARING FOR THE LIFE THAT COMES AFTER SPORT.",
    text: `One day, every athlete runs their final race and hangs up their competition spikes.

What happens to your identity when the cheering stops?

That is why my coaching philosophy has always focused on building the complete human being.
The discipline, integrity, resilience, and strategic thinking developed on the track are not just for winning races—they are your superpower for building businesses, leading teams, and serving communities for the next 50 years.

Destiny Spurlock is building a foundation that transcends sport.

Run fast. But lead even faster.

🔗 Discover athlete transition and career leadership coaching: https://lornettedaye.com

#LifeAfterSport #CompleteAthlete #AthleteTransition #DestinySpurlock #LornetteDaye #FinishStrong #ExecutiveLeadership #CareerAfterAthletics #IdentityBeyondSport #LifelongSuccess #LeadershipFramework`,
  },
  {
    id: 10,
    title: "Finish Strong: Destiny Spurlock Writes Her Legacy",
    imageFile: "destinyspurlock-10.png",
    imageUrl: `${BASE_IMAGE_URL}/destinyspurlock-10.png`,
    dueAt: "2026-09-29T19:00:00.000Z", // Tuesday Sep 29 @ 1:00 PM MDT (19:00 UTC)
    timeLabel: "Tuesday, Sep 29 - 1:00 PM MDT",
    headline: "YOUR STORY IS STILL BEING WRITTEN: FINISH STRONG.",
    text: `To Destiny Spurlock and every rising athlete striving for greatness:

You will face doubters. You will face bad weather, difficult selections, and moments of exhaustion.
None of that defines where you finish.

What defines you is the fire in your belly, the consistency of your daily habits, and the courage to step onto the track with complete belief in your preparation.

Run your race. Own your lane. 
Finish strong.

🔗 Connect with Lornette Daye for books, keynote speaking, and mentorship: https://lornettedaye.com

#DestinySpurlock #FinishStrong #OwnYourLane #TrackAndField #LornetteDaye #KeynoteSpeaker #InspirationalLeadership #YouthEmpowerment #ChampionshipMindset #PodiumFinish #SprintNation #LegacyInAction #UnstoppableSpirit`,
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
  console.log('🏃 Scheduling 10 Destiny Spurlock Ads Across September (Sep 2 – Sep 29)');
  console.log('======================================================================\n');

  for (const post of destinySpurlockPosts) {
    console.log(`[Scheduling Destiny Spurlock Ad #${post.id}] "${post.title}"`);
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
  console.log('🎉 All 10 Destiny Spurlock Ads successfully scheduled into Buffer!');
  console.log('======================================================================\n');
}

main().catch(console.error);
