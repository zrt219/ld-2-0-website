/**
 * Schedule Buffer Athlete & Leadership Group Posts Starting Sunday, August 30, 2026
 * Channel: Lornette D LinkedIn (6a39d30c5ab6d2f1065f5301)
 */

import { bufferGraphQL, getChannels } from './buffer-post.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';

export const athletePosts = [
  {
    id: 1,
    title: "It Matters Where You Finish",
    ideaId: "6a8bdb7d954ab88f3a2c434a",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bdb7a5572ff74dc0c4ae7/7ba355320fb2ca8a59e8e6c28c39b04b.original.png",
    dueAt: "2026-08-30T18:00:00.000Z", // Sunday Aug 30 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Sunday, Aug 30 - 12:00 PM MDT",
    text: `Your first chapter is not your final chapter.
Your postal code is not your ceiling.
Your family circumstances are not a life sentence.
Your age is not a verdict.

And someone else’s narrow expectations do not get to hold the pen to your future.

In my 40+ years of coaching world-class athletes and mentoring young leaders, I’ve seen time and again that history is made by people whose beginnings gave no hint of the greatness they would achieve.

We do our youth a profound disservice when we tell them to "be realistic."
What they need is permission to imagine boldly.
What they need is the systemic opportunity to prepare relentlessly.
What they need is the courage to keep running their race when the road gets steep.

Where you start matters because it builds your grit.
But it does NOT define where you finish.

Your story is still being written. Dream big.

🔗 Explore mentorship & keynote speaking: lornettedaye.com/speaking

#YourStoryMatters #FinishStrong #DreamBig #Leadership #FutureLeaders #YouthLeadership #NextGeneration #YouthEmpowerment #RepresentationMatters #BelieveInYourself #Purpose #Potential #PersonalGrowth #LeadershipDevelopment #Resilience #Perseverance #BreakingBarriers #Inspiration #Motivation #KeynoteSpeaker #ExecutiveLeadership #GrowthMindset #Courage #KeepGoing #GlobalAthletics`,
  },
  {
    id: 2,
    title: "Before They Can Become It (Women in Sport)",
    ideaId: "6a8bd5caaf3a71402dc1815a",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bd5c7fb6e0a524508fc46/c7c73c92bcc3335a4bbacf0a05f59b4c.original.png",
    dueAt: "2026-08-31T00:00:00.000Z", // Sunday Aug 30 @ 6:00 PM MDT (00:00 UTC Aug 31)
    timeLabel: "Sunday, Aug 30 - 6:00 PM MDT",
    text: `You cannot be what you cannot see.

Sometimes inspiration isn’t a grand keynote speech.
Sometimes it is a 10-year-old girl in the stands watching a woman wear her nation's colours on the international stage and whispering to herself:
"That could be me."

That is what intentional investment in women’s athletics truly creates.
It doesn't just build stronger competitors. It ignites generational belief.

When female athletes receive equal funding, premier broadcast slots, and institutional backing, we reshape the neurological blueprint of what young girls believe is possible for their lives.

The athlete competing today may never meet the child she inspires.
But that child will carry that spark for the rest of her life.

Role models matter. Support systems matter. Belief changes futures.

🔗 Learn about our athlete coaching & female leadership initiatives: lornettedaye.com/about

#WomenInSport #InvestInWomen #FemaleAthletes #GirlsInSport #RepresentationMatters #WomenInLeadership #AthleteDevelopment #RoleModelsMatter #NextGenLeaders #OlympicHopefuls #HighPerformance #SheCanPlay #YouthDevelopment #LornetteDaye #FinishStrong #SportsEquity #TitleIX #GlobalSport #Empowerment #SportsLeadership`,
  },
  {
    id: 3,
    title: "The IOC Grants & The Timeline of Progress",
    ideaId: "6a8bcc2b657d38df4bc0af03",
    imageUrl: "https://lornettedaye.com/campaigns/turkey/turkey-08.png",
    dueAt: "2026-08-31T18:00:00.000Z", // Monday Aug 31 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Monday, Aug 31 - 12:00 PM MDT",
    text: `This is not an attack on progress. It is an urgent reminder of how long progress can take.

The IOC’s strategic decision in 2026 to provide direct grants to Olympic competitors is a milestone that deserves genuine praise.

But the words "for the first time" should give every sports leader pause.

For over a century, generations of elite athletes sacrificed their bodies, depleted their savings, and built the multi-billion-dollar global sports economy without receiving direct equity from the spectacle they created.

We must celebrate the progress—while fearlessly asking:
Why did it take disruption from outside organizations and athlete advocacy to make compensation non-negotiable?

Who creates the value? The athletes.
Who absorbs the lifelong physical toll? The athletes.
Who deserves meaningful equity in the sports business? The athletes.

The needle is finally moving. Now, let’s ensure it doesn’t stop until every world-class competitor has a sustainable economic foundation.

🔗 Read my latest analysis on sports governance & athlete advocacy: lornettedaye.com/blog

#PayTheAthletes #AthleteEquity #SportsBusiness #SportsEconomics #OlympicMovement #AthleteRights #AthleteWelfare #SportsGovernance #EliteAthletes #FutureOfSport #SportsLeadership #AthleteFirst #SportsLaw #SportsManagement #HighPerformance #LornetteDaye #FinishStrong #OlympicGames #GlobalAthletics`,
  },
  {
    id: 4,
    title: "Market Disruption & Athlete Value",
    ideaId: "6a8bcc0f0bbbc27299e55540",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bcbceab1fe8806a0538be/31f2c743e808b75a90c2393d5c7b7308.original.png",
    dueAt: "2026-09-01T00:00:00.000Z", // Monday Aug 31 @ 6:00 PM MDT (00:00 UTC Sep 1)
    timeLabel: "Monday, Aug 31 - 6:00 PM MDT",
    text: `Competition doesn't just improve performance on the track—it forces institutions to re-evaluate athlete worth.

Look at the trajectory of the past few years:
• In 2024, World Athletics broke century-old precedent by awarding $50,000 to Olympic gold medalists in Paris.
• In 2026, the IOC approved direct grants for all Olympic athletes.
• Meanwhile, disruptive new leagues emerged with multi-million-dollar event purses, direct appearance fees, and historic record bonuses.

Regardless of where you stand on specific new commercial formats, one truth is undeniable:
Market competition forces sports federations to answer questions they previously avoided.

How much of the revenue generated by broadcast rights, merchandise, and sponsorships actually reaches the human beings inside the jersey?

When athletes have options, sports systems are forced to modernize. That is a massive win for the future of global sport.

🔗 Book Lornette Daye for executive keynotes on leadership & disruption: lornettedaye.com/speaking

#AthleteEconomy #PayTheAthletes #SportsBusiness #SportsDisruption #SportsEconomics #AthleteRights #AthleteCompensation #FutureOfSport #SportsInnovation #SportsLeadership #OlympicAthletes #EliteSport #TrackAndField #SportsMarketing #AthleteAdvocacy #FinishStrong #LornetteDaye #SportsIndustry`,
  },
  {
    id: 5,
    title: "Extraordinary Performance Deserves Extraordinary Compensation",
    ideaId: "6a8bcbb5954ab88f3a2c0716",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bcbaf40dc50163c0fc617/219cef6021154b9aa22c63fee075177e.original.png",
    dueAt: "2026-09-01T18:00:00.000Z", // Tuesday Sep 1 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Tuesday, Sep 1 - 12:00 PM MDT",
    text: `Think about what it takes to break a world record.

Thousands of grueling training sessions in the dark.
Years of relentless physical rehabilitation.
Decades of missed family milestones, financial strain, and unseen sacrifice.

Then, in a fraction of a second, history is rewritten. Millions of people around the world watch in awe, and broadcast networks generate record ratings.

Why should that extraordinary moment transform the bottom line of corporations and broadcast networks—while leaving the athlete struggling to pay for their coaching staff?

Extraordinary performance deserves extraordinary compensation.
When an athlete elevates their sport to unprecedented heights, they should participate directly in the wealth they create.

Transforming a sport should transform the athlete's life.

🔗 Discover high-performance coaching & transition programs: lornettedaye.com/athlete-coaching

#WorldRecord #ElitePerformance #PayTheAthletes #AthleteCompensation #SportsExcellence #HighPerformanceCulture #SportsBusiness #SportsEconomics #TrackAndField #Swimming #OlympicAthletes #SportsScience #HumanPerformance #AthleteFirst #SportsLeadership #FinishStrong #LornetteDaye #KeynoteSpeaker`,
  },
  {
    id: 6,
    title: "The Grocery Store Test (Human Reality of Sport)",
    ideaId: "6a8bcba3af3a71402dc15588",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bcb9af407f17426080495/4b838062272a08ac7f049c2f3c6e16d2.original.png",
    dueAt: "2026-09-02T00:00:00.000Z", // Tuesday Sep 1 @ 6:00 PM MDT (00:00 UTC Sep 2)
    timeLabel: "Tuesday, Sep 1 - 6:00 PM MDT",
    text: `The most powerful argument for athlete compensation isn't made in a boardroom or a stadium.
It happens in the grocery store aisle.

Elite athletes don't live on medals. They need rent, clean nutrition, physiotherapy, equipment, transportation, and family security.

We applaud their patriotism on international television, but too often forget that their athletic prime is an extremely narrow window.
One torn ligament or one administrative selection decision can end a decade of work in a heartbeat.

Athletes should not arrive at retirement with a collection of ribbons, worn-out joints, and zero financial security for the next 50 years of their lives.

Recent prize money expansions and athlete stipends are crucial steps forward. But the conversation cannot stop there.

Bills are monthly. Careers are short. Let’s fund athletes accordingly.

🔗 Read Lornette Daye’s athlete life transition & welfare frameworks: lornettedaye.com/impact

#AthleteWelfare #AthletePay #FinancialSecurity #LifeAfterSport #SportsEconomics #SportsBusiness #EliteAthletes #OlympicHopefuls #AthleteRights #SportsGovernance #AthleteSupport #MentalHealthInSports #SportsManagement #FinishStrong #LornetteDaye #AdvocacyInSport #CareerTransition`,
  },
  {
    id: 7,
    title: "If the Body Takes the Risk, the Athlete Must Share the Reward",
    ideaId: "6a8bc853954ab88f3a2bfcdf",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bc845c91ccb61700ade9e/f49c9af4df37a309b402cdc4da89615e.original.png",
    dueAt: "2026-09-02T18:00:00.000Z", // Wednesday Sep 2 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Wednesday, Sep 2 - 12:00 PM MDT",
    text: `The spectator sees a 10-second sprint or a flawless routine.
The athlete lives with everything that happens afterward:

The torn meniscus. The chronic achilles tendinopathy. The spinal disc compression.
The months of physiotherapy, MRI scans, cold tubs, and sleepless nights.

Elite athletics requires human beings to operate at the absolute brink of physiological limits.
Physical risk creates long-term health and financial consequences. And the athlete carries 100% of that burden.

That’s why telling athletes to "just be grateful for the opportunity" is an outdated and unacceptable philosophy.

If the global entertainment economy thrives on the physical risks taken by athletes, those athletes must receive equitable long-term compensation and healthcare protection.

If the body takes the risk, the athlete must share the reward.

🔗 Learn more about sustainable sports policies & athlete health advocacy: lornettedaye.com/speaking

#AthleteHealth #SportsMedicine #AthleteRecovery #PayTheAthletes #SportsScience #PhysicalToll #EliteSport #AthleteWelfare #HighPerformance #InjuryPrevention #SportsEthics #AthleteProtection #SportsLeadership #OlympicPreparation #LornetteDaye #FinishStrong #SportsBusiness`,
  },
  {
    id: 8,
    title: "The Hidden Invoices of World-Class Sport",
    ideaId: "6a8bc83cc76a3bfbb58d8794",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bc83334c92d90c7094cc1/dd7aced7676b372a0602116206736cbf.original.png",
    dueAt: "2026-09-03T00:00:00.000Z", // Wednesday Sep 2 @ 6:00 PM MDT (00:00 UTC Sep 3)
    timeLabel: "Wednesday, Sep 2 - 6:00 PM MDT",
    text: `The competition lasts one evening.
Getting there costs thousands of dollars before a single starting gun is fired.

International flights. Hotel stays. Baggage fees for specialized gear. Physio appointments. Coaching retainers. Entry fees. Lost work wages.

For the majority of aspiring world champions, these costs come directly out of their own pockets (or their families' savings) with zero guarantee of a return.

We cannot design a sports ecosystem that only works for athletes with wealthy benefactors or those who have already achieved superstar status.

Talent is distributed evenly across our communities, but capital is not.
If we want true excellence on the world stage, we must eliminate the operational financial barriers that choke the pipeline before an athlete can even emerge.

Let athletes earn. Remove the friction. Build sustainable pathways.

🔗 Partner with Lornette Daye on sports development initiatives: lornettedaye.com/programs

#GrassrootsSport #SportsFunding #AthleteExpenses #HighPerformance #SportsEquity #TrackAndField #OlympicAthletes #SportsInfrastructure #AthleteDevelopment #YouthInSport #SportsEconomics #SportsPhilanthropy #LornetteDaye #FinishStrong #SportsManagement #GlobalAthletics`,
  },
  {
    id: 9,
    title: "Two Careers to Afford One Dream",
    ideaId: "6a8bc82c0bbbc27299e548cb",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bc811a90788af4b084e79/6aa25c3be4a8c322a0abb707cd27c8bf.original.png",
    dueAt: "2026-09-03T18:00:00.000Z", // Thursday Sep 3 @ 12:00 PM MDT (18:00 UTC)
    timeLabel: "Thursday, Sep 3 - 12:00 PM MDT",
    text: `Imagine this daily routine:
5:00 AM: Track workout & sprint mechanics.
8:00 AM: Weight room & plyometrics.
10:30 AM: Physio, icing, and mobility.

Then, instead of recovering to let the muscular system rebuild, you put on a uniform and work an 8-hour shift in retail, warehousing, or hospitality just to pay rent.

Then wake up and do it all over again tomorrow.

We love romanticizing the "grind," but sleep deprivation and chronic financial stress are the fastest ways to destroy world-class athletic potential.

Recovery is not a luxury in elite sport; it is an absolute physiological requirement.

When we fail to properly compensate athletes, we force them to sacrifice the very recovery their bodies need to compete at the highest level.

World-class talent should never be cut short because an athlete couldn't afford to rest.

🔗 Explore keynote topics on sustainable high performance & resilience: lornettedaye.com/speaking

#EliteAthleteLife #AthleteStruggles #HighPerformance #SportsScience #RecoveryMatters #AthletePay #SportsBusiness #MentalToughness #CoachingExcellence #TrackAndField #OlympicTraining #WorkLifeBalance #SportsLeadership #LornetteDaye #FinishStrong #KeynoteSpeaker`,
  },
  {
    id: 10,
    title: "Yes We Can (Breaking Historic Barriers)",
    ideaId: "6a8bddef954ab88f3a2c470e",
    imageUrl: "https://buffer-media-uploads.s3.amazonaws.com/6a39d1c11bd2ec1bc407d874/6a8bdc32f9e42075f00c249e/827a848e7c2f2ec56f9bd23b9da2c480.original.png",
    dueAt: "2026-09-04T00:00:00.000Z", // Thursday Sep 3 @ 6:00 PM MDT (00:00 UTC Sep 4)
    timeLabel: "Thursday, Sep 3 - 6:00 PM MDT",
    text: `There will always be voices ready to tell you that the odds are insurmountable.
There will always be critics telling you the room isn't ready for your voice, the podium isn't ready for your face, or the ceiling is too low for your wings.

Then history breaks wide open.

When Barack Obama declared "Yes We Can," it wasn't just a political rallying cry—it was an enduring statement about what happens when people refuse to let history dictate their limitations.

Whenever you face a barrier that feels impenetrable in your sport, your business, or your community, remember this:
"Impossible" has a terrible track record.

Keep preparing in silence.
Keep sharpening your craft.
Keep building your table.

Sometimes history is simply waiting for someone brave enough to step forward and finish strong.

🔗 Order the book 'Finish Strong' by Lornette Daye: lornettedaye.com/books

#YesWeCan #BarackObama #LeadershipExcellence #BlackHistory #BreakingBarriers #HistoryMakers #NextGenLeaders #RepresentationMatters #YouthEmpowerment #ExecutiveLeadership #Resilience #Unstoppable #Inspiration #PurposeDriven #FinishStrong #LornetteDaye #KeynoteSpeaker #DreamBigger #SocialImpact #Courage`,
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
    assets: post.imageUrl ? [{ image: { url: post.imageUrl } }] : [],
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
  console.log('🚀 Scheduling 10 Athlete & Leadership Group Posts Starting Sunday, Aug 30');
  console.log('======================================================================\n');

  for (const post of athletePosts) {
    console.log(`[Scheduling Post #${post.id}] "${post.title}"`);
    console.log(`   📅 Slot: ${post.timeLabel} (${post.dueAt})`);
    console.log(`   🖼️ Image: ${post.imageUrl ? 'Attached' : 'Text-only'}`);
    
    try {
      const res = await schedulePost(post);
      if (res.createPost?.__typename === 'PostActionSuccess' && res.createPost.post) {
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
  console.log('🎉 All 10 posts processed! Checking final queue status...');
  console.log('======================================================================\n');
}

main().catch(console.error);
