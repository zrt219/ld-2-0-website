/**
 * Leylah Fernandez September Campaign Scheduler
 * 3x Daily Posts (9:00 AM, 1:00 PM, 6:30 PM MDT) throughout September
 * 
 * Editorial Angle: Inspiring Storytelling & Canadian Heritage (immigrant work ethic, grassroots development, national pride)
 * Voice: Lornette Daye (Former Canadian National Sprint Champion, Olympian Coach, Keynote Speaker)
 * Image Assets: https://lornettedaye.com/campaigns/leylah/leylah-01.png to leylah-10.png
 */

import fs from 'fs';
import path from 'path';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/leylah';

export const leylahCaptions = [
  // 1. Still Standing / Work Ethic
  {
    imageIndex: 1,
    headline: "LEYLAH — STILL STANDING.",
    text: `As a former Canadian National Sprint Champion and Olympian coach, I know how brutal the international sports spotlight can be when results plateau.

People love to celebrate the breakthrough, but they disappear during the unseen grind of rebuilding.

What I respect most about Leylah Fernandez is that she never stopped doing the unglamorous work. She didn't complain about the ranking drops or media scrutiny. She laced up her shoes, hit the practice court, and trusted her foundation.

To every athlete, founder, and professional grinding through a difficult season: keep standing. Your comeback is already underway.

Discover high-performance mindset coaching: lornettedaye.com/athlete-coaching

#LeylahFernandez #StillStanding #CanadianTennis #TennisCanada #ResilienceInSport #LornetteDaye #NeverGiveUp #HighPerformanceMindset #WomenInSport #USOpen2026 #FinishStrong`,
  },

  // 2. Real Confidence / Immigrant Roots
  {
    imageIndex: 2,
    headline: "CONFIDENCE ISN'T JUST FOR THE GOOD DAYS.",
    text: `Confidence is easy when your serve is clicking, the crowd is cheering, and every shot lands on the line.

Real confidence—the kind forged in immigrant families who sacrificed everything to give their children a shot at a dream—is what keeps you standing when the scoreboard is against you.

Leylah learned her tenacity at the kitchen table from parents who taught her that no opponent is bigger than your heart.

True champions don't derive their worth from external rankings. They derive it from their internal standard.

Read more about resilience and mental toughness: lornettedaye.com/about

#RealConfidence #ImmigrantWorkEthic #FamilySacrifice #CanadianExcellence #LeylahFernandez #LornetteDaye #MentalGrit #TennisMindset #WomenInLeadership #USOpen`,
  },

  // 3. New York Remembers Her / Experience
  {
    imageIndex: 3,
    headline: "NEW YORK REMEMBERS HER.",
    text: `In 2021, an unseeded Canadian teenager took New York by storm, smiling through brutal 3-set battles against the best players on earth.

Five years later, Leylah Fernandez returns to Flushing Meadows not as a novelty, but as a seasoned, battle-tested competitor who understands what it truly takes to reach a Grand Slam final.

Experience doesn't remove pressure—it teaches you how to use pressure as fuel.

Never count out a fighter who knows the taste of the big stage.

Explore leadership and peak performance programs: lornettedaye.com/leadership

#NewYorkRemembers #USOpenFinalist #ExperienceMatters #LeylahFernandez #ArthurAsheStadium #LornetteDaye #UnderdogMindset #BigStageConfidence #TennisCanada #FinishStrong`,
  },

  // 4. Don't Count Leylah Out / Big Wins
  {
    imageIndex: 4,
    headline: "DON'T COUNT LEYLAH OUT.",
    text: `When Leylah took down World No. 5 Mirra Andreeva 6-1, 6-4 in Toronto, she sent a clear message to the tennis world:

When Leylah finds her rhythm and court positioning, she can dismantle anyone on tour.

Momentum in sport is not an accident. It is the sudden alignment of months of quiet preparation with a single moment of opportunity.

Always back the athlete who has ice in her veins when the pressure rises.

Connect with Lornette Daye for keynotes and team training: lornettedaye.com/speaking

#DontCountHerOut #GiantKiller #WTAExcellence #LeylahFernandez #NationalBankOpen #LornetteDaye #MomentumShift #CanadianAthletes #ClutchPerformance #TennisDebate`,
  },

  // 5. One Result Doesn't Define You / Athlete Welfare
  {
    imageIndex: 5,
    headline: "ONE RESULT DOESN'T DEFINE YOU.",
    text: `In my 40+ years in athletics, the biggest lie I see young competitors believe is that their human value is tied to their last match.

A loss doesn't erase your talent.
A slump doesn't erase your potential.
A ranking drop doesn't determine your dignity.

Developing the athlete means protecting the person inside the athlete. When you play with freedom instead of fear, excellence flows naturally.

Explore athlete mentorship & wellness coaching: lornettedaye.com/mentorship

#DevelopingTheAthlete #PreparingThePerson #BuildingTheFuture #AthleteWellbeing #LeylahFernandez #LornetteDaye #SafeSport #SelfWorth #MentalHealthInSports #FinishStrong`,
  },

  // 6. Canada, We Have Someone to Cheer For / National Pride
  {
    imageIndex: 6,
    headline: "CANADA, WE HAVE SOMEONE TO CHEER FOR. 🇨🇦",
    text: `From Montreal and Laval to the world's biggest arenas:

Every time Leylah Fernandez steps onto the court wearing that Maple Leaf spirit, she carries the hopes of millions of young Canadian athletes across every province.

Canadian sport is built on grit, humility, and the quiet refusal to back down from anyone.

Let's rally behind Leylah as she battles in New York! Drop your Canadian flags and cheers below! 🇨🇦🎾👇

#TeamCanada #TennisCanada #CanadianPride #GoCanada #LeylahFernandez #LornetteDaye #MapleLeafExcellence #MontrealSports #CanadianChampions #USOpen`,
  },

  // 7. Pressure Builds Champions / Elite Mentality
  {
    imageIndex: 7,
    headline: "PRESSURE BUILDS CHAMPIONS.",
    text: `The pressure to defend points and maintain expectations has broken many promising careers.

But as Billie Jean King famously said, 'Pressure is a privilege.'

When you look at Leylah Fernandez's eyes on return of serve, you see an athlete who doesn't shy away from confrontation. She steps into the baseline, takes the ball on the rise, and dictates the terms of engagement.

In life and business: don't back away from the heat. Step into it.

Book Lornette Daye for your next conference or executive summit: lornettedaye.com/book

#PressureIsAPrivilege #StepIntoTheFire #AggressiveMindset #LeylahFernandez #LornetteDaye #ExecutivePresence #HighPerformance #ChampionHabits #WTA #FinishStrong`,
  },

  // 8. When the Season Doesn't Go to Plan / Resilience
  {
    imageIndex: 8,
    headline: "WHEN THE SEASON DOESN'T GO TO PLAN...",
    text: `No championship journey is a straight line.

There are injury setbacks, tough draws, bad bounces, and nights where you question whether the sacrifices are worth it.

Resilience is not the absence of frustration; it is finding another reason to show up at 6:00 AM anyway.

Leylah Fernandez's career is a masterclass in staying the course when the noise gets loud.

Order Lornette's best-selling book 'Finish Strong': lornettedaye.com/books

#WhenThingsGoWrong #StayTheCourse #UnwaveringFocus #LeylahFernandez #LornetteDaye #FinishStrongBook #ResilienceMatters #SportsMotivation #TennisLife #KeynoteSpeaker`,
  },

  // 9. Comeback Starts With Belief / Grassroots Impact
  {
    imageIndex: 9,
    headline: "SOMETIMES THE COMEBACK STARTS WITH BELIEF.",
    text: `Long before the television cameras arrive, a champion must see the victory in the quiet theater of their own imagination.

When young girls across Canada see Leylah fighting for every single ball with relentless passion, they see proof that dedication and heart can conquer physical giants.

Grassroots sport thrives when our national heroes show us how to believe again.

Believe in your craft. Work in silence. Become unstoppable.

Discover grassroots sports initiatives: lornettedaye.com/programs

#ComebackMindset #BeliefFirst #InspireTheNextGeneration #LeylahFernandez #GrassrootsSport #LornetteDaye #BelieveWorkBecome #YouthEmpowerment #TennisInspiration #RoleModels`,
  },

  // 10. First Test / Matchday Focus
  {
    imageIndex: 10,
    headline: "FIRST TEST: NEW YORK STARTS HERE.",
    text: `Grand Slams are not won in the final; they are won in the grueling discipline of round one.

One point at a time.
One game at a time.
One set at a time.

When Leylah takes the court against top international competition, every detail of her preparation comes alive.

Are you backing Leylah to make a deep run this tournament? Drop your matchday predictions below! 🎾🔥🇨🇦

#MatchdayFocus #RoundOneReady #OnePointAtATime #LeylahFernandez #USOpen2026 #TennisCanada #LornetteDaye #SportsDebate #GrandSlamTennis #FinishStrong`,
  },
];

async function main() {
  console.log('======================================================');
  console.log('Scheduling Leylah Fernandez September Campaign');
  console.log(`Channel ID: ${CHANNEL_ID}`);
  console.log('Times: 9:00 AM, 1:00 PM, and 6:30 PM MDT daily');
  console.log('======================================================\n');

  const mutation = `
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
          post {
            id
            status
            shareMode
            dueAt
          }
        }
        ... on LimitReachedError {
          message
        }
        ... on InvalidInputError {
          message
        }
        ... on UnauthorizedError {
          message
        }
        ... on UnexpectedError {
          message
        }
      }
    }
  `;

  // September Schedule: Aug 30 to Sept 15 (initial wave)
  const daysCount = 15;
  const timeSlots = [
    { hour: 9, minute: 0, label: '9:00 AM MDT', utcOffset: 15 },
    { hour: 13, minute: 0, label: '1:00 PM MDT', utcOffset: 19 },
    { hour: 18, minute: 30, label: '6:30 PM MDT', utcOffset: 0.5 }, // next day 00:30 UTC
  ];

  let postCount = 0;
  let successCount = 0;
  let limitCount = 0;

  for (let day = 0; day < daysCount; day++) {
    const calendarDate = new Date(Date.UTC(2026, 7, 30 + day)); // Starting Aug 30
    const dateString = calendarDate.toISOString().split('T')[0];

    for (let slotIdx = 0; slotIdx < timeSlots.length; slotIdx++) {
      const slot = timeSlots[slotIdx];
      const captionObj = leylahCaptions[postCount % leylahCaptions.length];
      const imgFile = `leylah-${String(captionObj.imageIndex).padStart(2, '0')}.png`;
      const fullImageUrl = `${BASE_IMAGE_URL}/${imgFile}`;

      // Calculate dueAt timestamp
      let dueYear = 2026;
      let dueMonth = 7; // August
      let dueDay = 30 + day;
      let dueHour = slot.utcOffset;
      let dueMinute = slot.minute;

      if (slotIdx === 2) {
        // 6:30 PM MDT -> 00:30 UTC next day
        dueDay += 1;
        dueHour = 0;
        dueMinute = 30;
      }

      const dueAtDate = new Date(Date.UTC(dueYear, dueMonth, dueDay, dueHour, dueMinute, 0, 0));
      const dueAt = dueAtDate.toISOString();

      postCount++;
      console.log(`[Post #${postCount}] Day ${day + 1} (${dateString} @ ${slot.label}) -> Creative: ${imgFile}`);

      const variables = {
        input: {
          channelId: CHANNEL_ID,
          mode: 'customScheduled',
          schedulingType: 'automatic',
          needsApproval: false,
          saveToDraft: false,
          dueAt: dueAt,
          text: captionObj.text,
          assets: [
            {
              image: {
                url: fullImageUrl,
              },
            },
          ],
        },
      };

      try {
        const res = await fetch(GRAPHQL_ENDPOINT, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${BUFFER_TOKEN}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            query: mutation,
            variables,
          }),
        });

        const result = await res.json();

        if (result.errors) {
          console.error(`   ❌ GraphQL Error:`, JSON.stringify(result.errors));
        } else if (result.data?.createPost?.post?.id) {
          const post = result.data.createPost.post;
          console.log(`   ✅ Scheduled in Buffer! ID: ${post.id} | Due: ${post.dueAt}`);
          successCount++;
        } else if (result.data?.createPost?.__typename === 'LimitReachedError') {
          console.log(`   ⚠️ Buffer queue capacity reached: ${result.data.createPost.message}`);
          limitCount++;
          break; // Stop when queue is filled
        } else {
          console.error(`   ⚠️ Buffer API Response:`, JSON.stringify(result.data?.createPost));
        }
      } catch (err) {
        console.error(`   ❌ Fetch Exception:`, err.message);
      }

      await new Promise(r => setTimeout(r, 600));
    }

    if (limitCount > 0) break;
  }

  console.log('\n======================================================');
  console.log(`Summary: ${successCount} Posts Scheduled into Buffer Active Queue`);
  console.log('======================================================');
}

if (process.argv[1]?.includes('schedule-leylah-campaign')) {
  if (process.argv[1]?.includes('schedule-leylah-campaign.mjs')) {
  main().catch(console.error);
}
}
