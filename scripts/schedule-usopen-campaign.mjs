/**
 * US Open 7-Day Fast & Engaging Fan Debate Campaign Scheduler
 * Direct Buffer GraphQL API Integration (NO Vercel)
 * 
 * Schedule: 10 posts across 7 days starting tomorrow evening
 * Channel: Lornette Daye LinkedIn (ID: 6a39d30c5ab6d2f1065f5301)
 */

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/usopen';

export const usOpenPosts = [
  // Day 1 - Aug 30, 2026
  {
    day: 1,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-08-30T23:30:00.000Z', // 5:30 PM MDT Aug 30 -> 23:30 UTC Aug 30
    imageFile: 'usopen-01.png',
    headline: "NEW YORK. IT'S TIME. THE US OPEN BEGINS.",
    text: `New York under the lights hits completely different. 

The unmatched energy, the electric Arthur Ashe night crowd, and two weeks of high-stakes tennis drama are officially here!

Who is your dark horse to make a deep run into the second week? Drop your tournament predictions below! 👇🎾

#USOpen #USOpen2026 #Tennis #GrandSlam #ArthurAshe #NewYorkSports #TennisTalk #LornetteDaye #SportsDebate #TennisCommunity #WTA #ATP`,
  },
  {
    day: 1,
    timeMDT: '7:15 PM MDT',
    dueAt: '2026-08-31T01:15:00.000Z', // 7:15 PM MDT Aug 30 -> 01:15 UTC Aug 31
    imageFile: 'usopen-02.png',
    headline: 'CAN SABALENKA MAKE IT THREE?',
    text: `Aryna Sabalenka is on a historic mission in Queens.

Three consecutive US Open titles would put her in truly legendary company. Her raw baseline power and aggressive serving are built for these courts—but can anyone disrupt her rhythm?

Can Sabalenka complete the three-peat, or does the field have an answer? Let's hear your take! 🎾👇

#Sabalenka #USOpen #WTA #TennisDebate #ThreePeat #GrandSlamTennis #WomensTennis #SportsDiscussion #LornetteDaye #TennisFans #ArthurAshe`,
  },

  // Day 2 - Aug 31, 2026
  {
    day: 2,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-08-31T23:30:00.000Z',
    imageFile: 'usopen-03.png',
    headline: 'COCO GAUFF. NEW YORK. HOME CROWD. CAN SHE DO IT AGAIN?',
    text: `Nothing compares to Coco Gauff playing with 24,000 New Yorkers screaming behind her.

When Coco gets the Arthur Ashe crowd rocking, momentum shifts in an instant. Defending a home Grand Slam comes with immense pressure—can she capture magic again?

Is Coco hoisting the trophy this year? Yes or No? Drop your verdict below! 🏆🇺🇸

#CocoGauff #USOpen #ArthurAsheStadium #TeamUSA #WTATour #TennisLovers #HomeCrowdAdvantage #LornetteDaye #USOpenTennis #GrandSlam #ChampionMindset`,
  },
  {
    day: 2,
    timeMDT: '7:15 PM MDT',
    dueAt: '2026-09-01T01:15:00.000Z',
    imageFile: 'usopen-04.png',
    headline: 'ALCARAZ IS BACK.',
    text: `Five months away from top-tier competition. Now one of tennis's grandest stages awaits Carlos Alcaraz.

His electric shot-making, drop shots, and superhuman court coverage make him must-watch tennis every single time. 

Can Alcaraz conquer New York once again? Drop your predictions below! 🔥👇

#CarlosAlcaraz #Alcaraz #USOpen #ATP #GrandSlam #TennisComeback #ArthurAshe #TennisFever #LornetteDaye #SportsDebate #TennisExcellence`,
  },

  // Day 3 - Sept 1, 2026
  {
    day: 3,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-09-01T23:30:00.000Z',
    imageFile: 'usopen-05.png',
    headline: 'SINNER IS OUT. THE DRAW JUST CHANGED. WHO BENEFITS MOST?',
    text: `Jannik Sinner is OUT of the US Open. 

A massive shockwave just ripped through the men's draw. The entire championship bracket is wide open.

Who capitalizes most on this vacancy—Alcaraz, Zverev, Djokovic, or a surprise dark horse?

Tell us who has the easiest path to the final now! 📊👇

#JannikSinner #USOpenDraw #TennisNews #ATPWorldTour #GrandSlamDrama #TennisCommunity #USOpen2026 #LornetteDaye #SportsUpdate #BracketBuster`,
  },

  // Day 4 - Sept 2, 2026
  {
    day: 4,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-09-02T23:30:00.000Z',
    imageFile: 'usopen-06.png',
    headline: 'ZVEREV HAS THE NO. 1 SEED.',
    text: `Alexander Zverev enters New York holding the No. 1 seed.

He has the weapons, the booming serve, and the big-stage experience. But can he finally break through the final barrier and claim that elusive Grand Slam title?

Is this Zverev's moment, or will the pressure catch up? Cast your vote in the comments! 🎾👇

#AlexanderZverev #No1Seed #USOpen #ATPTour #GrandSlamHunt #TennisDebate #ArthurAshe #LornetteDaye #TennisChampionship #FlushingMeadows`,
  },

  // Day 5 - Sept 3, 2026
  {
    day: 5,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-09-03T23:30:00.000Z',
    imageFile: 'usopen-07.png',
    headline: 'VENUS WILLIAMS. 46 YEARS OLD. STILL COMPETING.',
    text: `46 years old. Still stepping onto the court at the US Open.

Venus Williams doesn't have anything left to prove to anyone—she plays purely for the love of the game and the relentless spirit of competition. Longevity is its own form of greatness.

How much respect do you have for Venus's legendary career? Show some love in the comments! 👑❤️

#VenusWilliams #TennisLegend #Longevity #USOpen #IconicAthlete #WTAHistory #BlackExcellence #LornetteDaye #InspiringAthletes #ArthurAshe #FinishStrong`,
  },
  {
    day: 5,
    timeMDT: '7:15 PM MDT',
    dueAt: '2026-09-04T01:15:00.000Z',
    imageFile: 'usopen-08.png',
    headline: "SEVEN DIFFERENT WOMEN'S GRAND SLAM CHAMPIONS SINCE 2025.",
    text: `Seven different women's Grand Slam champions across the last major tournaments.

Predicting the WTA side of the draw is the ultimate challenge for any tennis fan right now. The depth, parity, and competitive fire in women's tennis has never been higher.

Who is walking away with the trophy this time? Name your champion below! 🏆⚡

#WomensTennis #WTA #GrandSlamParity #USOpen #TennisPredictions #CompetitiveDepth #TennisDebate #LornetteDaye #SportsDiscussion #WomenInSport`,
  },

  // Day 6 - Sept 4, 2026
  {
    day: 6,
    timeMDT: '5:30 PM MDT',
    dueAt: '2026-09-04T23:30:00.000Z',
    imageFile: 'usopen-09.png',
    headline: 'WHO OWNS NEW YORK?',
    text: `Arthur Ashe Stadium crowns true legends under the Friday night lights.

Alcaraz? Djokovic? Zverev? Or a brand new first-time Grand Slam champion?

Who owns New York in 2026? Drop your final four and champion picks right here! 🗽🎾

#WhoOwnsNewYork #USOpenFinals #ATPTennis #Djokovic #Alcaraz #Zverev #TennisTalk #GrandSlamShowdown #LornetteDaye #SportsDebate #ArthurAsheStadium`,
  },

  // Day 7 - Sept 5, 2026
  {
    day: 7,
    timeMDT: '6:00 PM MDT',
    dueAt: '2026-09-06T00:00:00.000Z',
    imageFile: 'usopen-10.png',
    headline: 'PUT THEM ON RECORD: YOUR US OPEN CHAMPIONS.',
    text: `Time to lock it in and put your predictions on the permanent record!

🏆 Men's Champion: ____________________
🏆 Women's Champion: __________________

Leave your picks in the comments now before the finals begin! Let's see who gets both right! 👇🔥

#USOpenPredictions #FinalPicks #TennisChampions #GrandSlamFinals #LockItIn #TennisCommunity #LornetteDaye #SportsFanatics #ArthurAshe #ChampionshipWeekend`,
  },
];

async function main() {
  console.log('======================================================');
  console.log('Scheduling 10 US Open Posts across 7 Days into Buffer');
  console.log(`Channel ID: ${CHANNEL_ID}`);
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

  let successCount = 0;
  let errorCount = 0;

  for (let i = 0; i < usOpenPosts.length; i++) {
    const p = usOpenPosts[i];
    const fullImageUrl = `${BASE_IMAGE_URL}/${p.imageFile}`;
    console.log(`[Post ${i + 1}/${usOpenPosts.length}] Day ${p.day} (${p.timeMDT}) -> Image: ${fullImageUrl}`);

    const variables = {
      input: {
        channelId: CHANNEL_ID,
        mode: 'customScheduled',
        schedulingType: 'automatic',
        needsApproval: false,
        saveToDraft: false,
        dueAt: p.dueAt,
        text: p.text,
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
        errorCount++;
      } else if (result.data?.createPost?.post?.id) {
        const post = result.data.createPost.post;
        console.log(`   ✅ Scheduled in Buffer! ID: ${post.id} | Due: ${post.dueAt}`);
        p.bufferPostId = post.id;
        p.status = 'scheduled';
        successCount++;
      } else {
        console.error(`   ⚠️ Buffer API Response:`, JSON.stringify(result.data?.createPost));
        errorCount++;
      }
    } catch (err) {
      console.error(`   ❌ Fetch Exception:`, err.message);
      errorCount++;
    }

    await new Promise(r => setTimeout(r, 600));
  }

  console.log('\n======================================================');
  console.log(`Summary: ${successCount} Posts Scheduled | ${errorCount} Errors`);
  console.log('======================================================');
}

main().catch(console.error);
