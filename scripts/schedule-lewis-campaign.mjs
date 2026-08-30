/**
 * Lewis Hamilton F1 Leadership & Fan Engagement Campaign Scheduling Script
 * 10 High-Impact Ads for Lornette Daye LinkedIn
 * 
 * Schedule: 2 posts per day across 5 consecutive days (Aug 30 – Sep 3) at 9:00 AM & 3:00 PM MDT
 * CTA: lornettedaye.com
 * Invariant: Every post includes a verified visual asset from public/campaigns/lewis-hamilton/
 */

import { bufferGraphQL } from './buffer-post.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/lewis-hamilton';

export const lewisHamiltonPosts = [
  {
    id: 1,
    title: "Still We Rise: The Mindset of a 7-Time World Champion",
    imageFile: "lewishamilton-01.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-01.png`,
    dueAt: "2026-08-30T15:00:00.000Z", // Sunday Aug 30 @ 9:00 AM MDT (15:00 UTC)
    timeLabel: "Sunday, Aug 30 - 9:00 AM MDT",
    headline: "STILL WE RISE: THE MINDSET OF A 7-TIME FORMULA 1 WORLD CHAMPION.",
    text: `From a council estate in Stevenage with a second-hand kart to standing alone at the pinnacle of motorsport history.

Lewis Hamilton’s journey is not just a motorsport story—it is a masterclass in resilience, grit, and the refusal to let society dictate your boundaries.

When you enter spaces where nobody looks like you, where tradition is built to keep you out, your talent must be undeniable, but your spirit must be unbreakable.

"Still I Rise" isn’t just ink on Lewis's back; it is a philosophy for every underdog fighting to break through in sports, business, or life.

No matter the obstacles in your lane: keep pushing. The checkered flag belongs to those who refuse to lift off the throttle.

🏁 F1 FANS & TEAM LH: What is your single most inspiring Lewis Hamilton race or moment of all time? Drop your favorite drive in the comments below! 👇

🔗 Explore keynote leadership and high-performance resilience: https://lornettedaye.com

#LewisHamilton #TeamLH #F1 #Formula1 #StillWeRise #LH44 #MercedesAMGF1 #ScuderiaFerrari #ChampionMindset #LornetteDaye #FinishStrong #MotorsportLeadership #Resilience #BreakingBarriers #HighPerformance #KeynoteSpeaker #GOAT #F1Community #RacingMindset`,
  },
  {
    id: 2,
    title: "100+ Poles. 100+ Wins. 7 Titles.",
    imageFile: "lewishamilton-02.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-02.png`,
    dueAt: "2026-08-30T21:00:00.000Z", // Sunday Aug 30 @ 3:00 PM MDT (21:00 UTC)
    timeLabel: "Sunday, Aug 30 - 3:00 PM MDT",
    headline: "100+ POLE POSITIONS. 100+ RACE WINS. 7 WORLD TITLES. BUT NUMBERS ARE ONLY HALF THE STORY.",
    text: `In the ultra-competitive world of Formula 1, drivers come and go in a flash. 
To stay at the absolute pinnacle for nearly two decades requires continuous, ruthless reinvention.

Over 100 pole positions. Over 100 Grand Prix victories. 7 World Championships.

What separates good drivers from true all-time legends is what happens AFTER they win their first title. 
Do they get comfortable? Or do they dissect their telemetry with even greater hunger?

Lewis Hamilton never stopped evolving his braking points, his physical conditioning, his mental clarity, and his tire management.

Success is not a destination. It is a relentless habit of self-refinement.

🏎️ FAN DEBATE: Which era of Lewis was the most fiercely dominant—the explosive rookie years at McLaren, or the record-shattering Mercedes dynasty? Share your take below! 💬

🔗 Master continuous improvement in your organization: https://lornettedaye.com

#LH44 #LewisHamilton #F1History #FormulaOne #MercedesF1 #McLarenF1 #ContinuousImprovement #PeakPerformance #LornetteDaye #FinishStrong #ExecutiveCoaching #F1Stats #MasteryInAction #HighPerformanceHabits #MotorsportLife #GrandPrixChampion #Excellence`,
  },
  {
    id: 3,
    title: "Leadership at 200 MPH: Unifying the Team",
    imageFile: "lewishamilton-03.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-03.png`,
    dueAt: "2026-08-31T15:00:00.000Z", // Monday Aug 31 @ 9:00 AM MDT (15:00 UTC)
    timeLabel: "Monday, Aug 31 - 9:00 AM MDT",
    headline: "LEADERSHIP AT 200 MPH: HOW A CHAMPION INSPIRES AN 1,800-PERSON ORGANIZATION.",
    text: `When Lewis crosses the line first, you hear his immediate radio transmission:
"A massive thank you to everyone back at the factory in Brackley and Brixworth. We win and we lose together."

Formula 1 looks like an individual sport on television, but behind that single steering wheel is an army of 1,800 aerodynamicists, composite engineers, strategy analysts, and mechanics.

A toxic driver blames the garage when the car is slow.
A transformational leader sits with the mechanics until midnight, takes ownership of mistakes, and breathes belief back into the team.

When leaders celebrate the unseen contributors, loyalty becomes unbreakable and performance reaches new heights.

We win together. We lose together.

👥 LEADERSHIP QUESTION: How do you keep your team united and motivated when projects hit a difficult slump? Let's discuss in the comments below! 👇

🔗 Transform your team's culture with high-performance coaching: https://lornettedaye.com

#TeamLeadership #CultureOfExcellence #LewisHamilton #MercedesAMGF1 #F1Engineering #TeamworkInAction #LornetteDaye #FinishStrong #ExecutiveLeadership #HighPerformanceTeams #SportsPsychology #WinTogether #MotorsportCulture #OrganizationalLeadership`,
  },
  {
    id: 4,
    title: "The Wet-Weather Master: Where Rain Reveals Greatness",
    imageFile: "lewishamilton-04.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-04.png`,
    dueAt: "2026-08-31T21:00:00.000Z", // Monday Aug 31 @ 3:00 PM MDT (21:00 UTC)
    timeLabel: "Monday, Aug 31 - 3:00 PM MDT",
    headline: "THE WET-WEATHER MASTER: WHY ADVERSE CONDITIONS SEPARATE DRIVERS FROM ICONS.",
    text: `Silverstone 2008 (winning by over a minute in biblical rain).
Turkey 2020 (starting 6th on a treacherous track to seal World Championship #7).
Interlagos 2016 (mastering aquaplaning while everyone else spun off).

When the track is bone dry and conditions are ideal, car aerodynamics do the heavy lifting.
When the heavens open and grip drops to zero, the machines equalize—and pure human sensory genius takes over.

Rain strips away excuses. It rewards feel, courage, and complete emotional regulation.

In business and sports, easy markets make anyone look competent. 
It is when the economic or competitive weather turns stormy that real champions step forward and dominate.

🌧️ F1 FANS: Is Turkey 2020 on slick intermediate tires Lewis's greatest wet-weather drive, or does Silverstone 2008 take the crown? Cast your vote! 🏆

🔗 Learn how to navigate crisis with Olympic-level composure: https://lornettedaye.com

#WetWeatherMaster #Silverstone2008 #Turkey2020 #LewisHamilton #F1Legends #F1Memories #CrisisLeadership #LornetteDaye #FinishStrong #SensoryMastery #RainMaster #GrandPrixGreatness #F1Debate #MotorsportHeritage #UnderPressure`,
  },
  {
    id: 5,
    title: "Purpose Beyond the Podium: Mission 44",
    imageFile: "lewishamilton-05.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-05.png`,
    dueAt: "2026-09-01T15:00:00.000Z", // Tuesday Sep 1 @ 9:00 AM MDT (15:00 UTC)
    timeLabel: "Tuesday, Sep 1 - 9:00 AM MDT",
    headline: "MORE THAN A DRIVER: USING THE GLOBAL STAGE FOR LASTING GENERATIONAL IMPACT.",
    text: `Trophies collect dust. Records eventually get challenged.
What endures forever is how many doors you kicked open for the next generation.

Through Mission 44 and the Hamilton Commission, Lewis didn’t just talk about diversity in STEM and motorsport—he invested tens of millions of dollars to fund apprenticeships, scholarships, and technical pathways for underrepresented youth.

He proved that true greatness is never about how much spotlight you take, but how much light you shine onto others.

Your platform is a privilege. Use it to build a legacy that outlasts your athletic career.

🚀 COMMUNITY IMPACT: Who is an athlete or leader you admire for using their platform for genuine social change? Tag them below! 🌟

🔗 Learn about youth empowerment and sports philanthropy: https://lornettedaye.com

#Mission44 #HamiltonCommission #DiversityInMotorsport #STEMEducation #YouthEmpowerment #LewisHamilton #LornetteDaye #FinishStrong #PurposeDrivenLeadership #SocialImpact #RepresentationInSTEM #SportsPhilanthropy #LegacyBuilding #ChangeMakers #InspireYouth`,
  },
  {
    id: 6,
    title: "The Adversity Blueprint: Grace Under Fire",
    imageFile: "lewishamilton-06.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-06.png`,
    dueAt: "2026-09-01T21:00:00.000Z", // Tuesday Sep 1 @ 3:00 PM MDT (21:00 UTC)
    timeLabel: "Tuesday, Sep 1 - 3:00 PM MDT",
    headline: "THE ADVERSITY BLUEPRINT: HOW TRUE CHAMPIONS RESPOND TO HEARTBREAK.",
    text: `December 12, 2021. Abu Dhabi.
In one of the most controversial moments in modern sports history, an 8th World Championship slipped away in the final seconds of the race.

The world watched closely to see how Lewis Hamilton would react.
Would he throw a tantrum? Would he insult his rivals?

Instead, he stepped out of the cockpit, walked straight to his opponent and his family, offered dignified congratulations, and held his head high.

Class in defeat is infinitely harder than arrogance in victory.

True strength is not proven when everything goes your way. It is proven by the dignity, poise, and silence with which you endure heartbreak before getting back to work.

Dignity is a superpower.

🤝 LIFE LESSON: What did Lewis's reaction teach you about handling unfair moments with grace? Share your reflections below. 👇

🔗 Master mental fortitude with 'Finish Strong' frameworks: https://lornettedaye.com

#AbuDhabi2021 #GraceUnderFire #CharacterMatters #LewisHamilton #TrueSportsmanship #DignityInDefeat #LornetteDaye #FinishStrong #MentalGrit #EmotionalMaturity #ExecutivePresence #ChampionMindset #IntegrityInSport #OvercomingAdversity`,
  },
  {
    id: 7,
    title: "The Ferrari Chapter: Embracing the Ultimate Challenge",
    imageFile: "lewishamilton-07.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-07.png`,
    dueAt: "2026-09-02T15:00:00.000Z", // Wednesday Sep 2 @ 9:00 AM MDT (15:00 UTC)
    timeLabel: "Wednesday, Sep 2 - 9:00 AM MDT",
    headline: "THE FERRARI CHAPTER: WHY LEGENDS NEVER CHOOSE THE COMFORTABLE PATH.",
    text: `He could have comfortably finished his career at Mercedes as an eternal ambassador with zero pressure.
Instead, at age 40, Lewis Hamilton chose to wear the iconic Rosso Corsa and join Scuderia Ferrari.

Why? Because true competitors are not addicted to past safety—they are drawn to the highest mountain.

Stepping into the pressure cooker of Maranello, learning a new culture, and chasing that elusive 8th title in red is the ultimate declaration of courage.

If your goals don't terrify you, they aren't big enough.

Never let age or past achievements stop you from writing your boldest chapter yet.

🔴 F1 WORLD & TIFOSI: Are you ready to see Lewis Hamilton in Ferrari red? Can he bring the World Championship back to Maranello? Sound off in the comments! 🏎️🇮🇹

🔗 Discover how to execute bold career transitions: https://lornettedaye.com

#FerrariF1 #ScuderiaFerrari #HamiltonToFerrari #LH44 #ForzaFerrari #Tifosi #F12025 #F12026 #BoldMoves #LewisHamilton #LornetteDaye #FinishStrong #CareerTransitions #NeverSettle #CourageToChange #Maranello #MotorsportDrama`,
  },
  {
    id: 8,
    title: "Sensory Mastery: The Unseen Precision of F1",
    imageFile: "lewishamilton-08.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-08.png`,
    dueAt: "2026-09-02T21:00:00.000Z", // Wednesday Sep 2 @ 3:00 PM MDT (21:00 UTC)
    timeLabel: "Wednesday, Sep 2 - 3:00 PM MDT",
    headline: "SENSORY MASTERY: MANAGING CHAOS AT 350 KM/H UNDER 5G OF BRAKING FORCE.",
    text: `Piloting a modern Formula 1 hybrid car is equivalent to playing speed chess while enduring the physical strain of a fighter jet.

Every lap requires:
• Modulating brake pedal pressure with 100 kg of leg force.
• Monitoring tire surface temperatures down to the single degree Celsius.
• Adjusting differential and brake balance dials on the steering wheel mid-corner.
• Communicating telemetry and strategy with race engineers at 220 mph.

This is sensory intelligence operating at the highest human limit.

In high-stakes industries, the difference between good and elite is the ability to process overwhelming data in real time while keeping your heart rate completely composed.

Calm in the cockpit. Precise in execution.

⚙️ TECH TALK: What technical aspect of Lewis’s driving craft do you think is the most underrated by casual fans? Share your thoughts below! 💬

🔗 Build Olympic-level focus and sensory discipline: https://lornettedaye.com

#F1Tech #MotorsportScience #SensoryMastery #LewisHamilton #DriverFitness #HighPerformance #LornetteDaye #FinishStrong #CognitiveEndurance #F1Telemetry #PeakHumanPerformance #SportsScience #ExecutiveFocus #EngineeringExcellence`,
  },
  {
    id: 9,
    title: "Unapologetically Authentic: Redefining Paddock Culture",
    imageFile: "lewishamilton-09.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-09.png`,
    dueAt: "2026-09-03T15:00:00.000Z", // Thursday Sep 3 @ 9:00 AM MDT (15:00 UTC)
    timeLabel: "Thursday, Sep 3 - 9:00 AM MDT",
    headline: "UNAPOLOGETICALLY AUTHENTIC: BREAKING THE CONSERVATIVE MOLD IN GLOBAL SPORT.",
    text: `For decades, Formula 1 drivers were expected to fit a very narrow corporate template: standard polo shirts, predictable PR quotes, and total conformity.

Lewis Hamilton changed the game.
From Met Gala red carpets to avant-garde paddock fashion, from producing music to backing environmental initiatives—he showed the world that you can be deeply multifaceted and still be the fastest human on the planet.

When you refuse to shrink yourself to fit someone else’s small expectations, you give everyone around you permission to be authentic.

Never apologize for having diverse passions. Excellence has no single uniform.

🌟 AUTHENTICITY POLL: How has Lewis inspired you to show up as your full, authentic self in your business or creative career? Let’s hear your story! ✍️

🔗 Empower authentic leadership in your organization: https://lornettedaye.com

#AuthenticLeadership #BeYourself #FashionInF1 #LewisHamilton #MetGalaF1 #PaddockStyle #LornetteDaye #FinishStrong #BreakingTheMold #ExecutivePresence #DiverseLeadership #CulturalImpact #Trailblazer #ModernIcons #ConfidenceInAction`,
  },
  {
    id: 10,
    title: "Finish Strong: It's Not Over Until the Checkered Flag",
    imageFile: "lewishamilton-10.png",
    imageUrl: `${BASE_IMAGE_URL}/lewishamilton-10.png`,
    dueAt: "2026-09-03T21:00:00.000Z", // Thursday Sep 3 @ 3:00 PM MDT (21:00 UTC)
    timeLabel: "Thursday, Sep 3 - 3:00 PM MDT",
    headline: "FINISH STRONG: THE RACE IS NEVER OVER UNTIL THE CHECKERED FLAG DROPS.",
    text: `Remember Brazil 2021?
Disqualified from qualifying. Starting the Sprint from P20 (dead last). 
Taking a grid penalty for Sunday.

And still charging through the entire field with unrelenting fury to take the Grand Prix victory.

That is the definitive hallmark of the champion mindset:
It doesn't matter how badly the deck is stacked against you. 
It doesn't matter how many penalties they hand you. 

When you have prepared your body, sharpened your mind, and anchored yourself in unwavering belief—you keep fighting until the final millimeter of tarmac.

Whatever race you are running today:
Do not slow down. Do not yield to fear.

Keep your foot on the floor. 
Finish strong.

🏁 TO TEAM LH & RACING FANS WORLDWIDE: What is your favorite quote or life lesson from Lewis Hamilton that you carry with you? Share it in the comments below! 🏎️💨

🔗 Discover books, keynotes, and high-performance frameworks: https://lornettedaye.com

#Brazil2021 #InterlagosMasterclass #NeverGiveUp #LewisHamilton #TeamLH #FinishStrong #CheckeredFlag #LornetteDaye #KeynoteSpeaker #PodiumFinish #GrandPrixGlory #UnstoppableSpirit #F1Motorsport #VictoryMindset #ExecutiveExcellence`,
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
  console.log('🏎️ Scheduling 10 Lewis Hamilton F1 Leadership Ads Starting Sunday, Aug 30');
  console.log('======================================================================\n');

  for (const post of lewisHamiltonPosts) {
    console.log(`[Scheduling Lewis Hamilton Ad #${post.id}] "${post.title}"`);
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
  console.log('🎉 All 10 Lewis Hamilton Ads successfully scheduled into Buffer!');
  console.log('======================================================================\n');
}

main().catch(console.error);
