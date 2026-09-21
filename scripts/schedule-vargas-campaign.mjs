/**
 * Melissa Vargas 3-Week Campaign (21 Days / 63 Posts)
 * 3x Daily Posts (9:00 AM, 1:00 PM, 6:30 PM MDT)
 * 
 * Narrative Lens: Reflective Storytelling & Human Resilience (Cuba to exile, injury rehab, finding a home in Türkiye)
 * Voice: Lornette Daye (40+ years Olympian coach, Canadian National Sprint Champion)
 * Image Assets: https://lornettedaye.com/campaigns/vargas/vargas-01.png through vargas-20.png
 */

import fs from 'fs';
import path from 'path';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/vargas';

export const vargasCaptions = [
  {
    imageIndex: 1,
    headline: "THE WORLD KNOWS HER NAME. MELISSA VARGAS.",
    text: `When you watch Melissa Vargas soar above the net and drive a volleyball at 112 km/h, it is easy to see only the superhuman athleticism.

What the highlight reels don't show is the quiet resilience of a young woman who had to leave everything she knew in Cuba at just 18, navigate international bans, and rebuild her entire life in a foreign land.

In 40+ years of coaching, I have learned that true power is never purely physical. Real power comes from surviving the seasons when the world tries to count you out.

Melissa didn't break. She grew roots in new soil and bloomed.

Discover high-performance resilience coaching: https://lornettedaye.com/athlete-coaching

#MelissaVargas #VargasPower #ResilienceInSport #CubanExcellence #TurkiyeVolleyball #LornetteDaye #OvercomingAdversity #FileninSultanlari #WomenInSport #ImmigrantGrit #FinishStrong #TrueGreatness #MentalFortitude #ChampionSpirit #VolleyballLegend #NeverGiveUp #HighPerformanceMindset #SportsStorytelling #VNLChampion #EuroVolley`,
  },

  {
    imageIndex: 2,
    headline: "33 POINTS. ONE FINAL. ONE RECORD.",
    text: `33 points in a single championship final. The highest-scoring performance in VNL Final history.

When the gold medal was on the line and the pressure reached boiling point, Melissa Vargas didn't look for someone else to step up. She took the ball, owned the moment, and delivered under fire.

Clutch execution isn't luck. It is the result of thousands of hours spent mastering self-regulation when your heart is pounding and 15,000 fans are screaming.

When your moment comes in business or life: don't hesitate. Step forward.

Explore executive leadership keynotes: https://lornettedaye.com/speaking

#33Points #RecordBreaker #ClutchPerformance #MelissaVargas #LornetteDaye #ExecutivePresence #HighPressureExecution #ChampionHabits #VolleyballHistory #VNLLeadership #VargasExcellence #OwnTheMoment #TurkiyePride #SportsPsychology #FinishStrong #PeakPerformance #LeadershipExcellence #DeliverUnderFire #PodiumExecution #MasteryInMotion`,
  },

  {
    imageIndex: 3,
    headline: "FROM EXILE TO EMPRESS: THE REBUILDING OF A CHAMPION.",
    text: `At 18 years old, Melissa Vargas was banned from international competition for seeking proper shoulder surgery. She was isolated from her national team, stripped of her platform, and forced to start over from scratch.

Most people would have walked away from the sport with bitterness.

Melissa chose another path. She rehabilitated her shoulder in silence, learned a new culture, and earned the respect of an entire nation through her humility and undeniable work ethic.

A setback is never your finish line—it is the setup for your true masterpiece.

Read 'Finish Strong' by Lornette Daye: https://lornettedaye.com/books

#FromExileToEmpress #RebuildingAChampion #SetbackToComeback #MelissaVargas #LornetteDaye #FinishStrongBook #ResilienceMatters #ShoulderRehab #SecondChances #NeverBreak #TriumphOverAdversity #QuietDignity #VolleyballInspiration #TurkiyeHero #HumanSpirit #OvercomeAnything #ChampionJourney #LifeLessonsThroughSport #InspireTheWorld #TrueStrength`,
  },

  {
    imageIndex: 4,
    headline: "THE JOY BEHIND THE EXPLOSIVE POWER.",
    text: `Look at Melissa Vargas's face after an ace or a thunderous kill block.

The radiant smile, the playful tongue-out celebration, the infectious energy that lifts every teammate on the floor.

In elite sports, too many athletes carry tension like a cage. Melissa plays with untamed joy. She loves the battle so much that fear has no room to breathe.

Joy is not the enemy of discipline; joy is the fuel that makes impossible workloads feel light.

Bring passion back into your craft.

Discover holistic mentorship & leadership programs: https://lornettedaye.com/programs

#JoyInCompetition #PlayWithPassion #MelissaVargas #InfectiousEnergy #LornetteDaye #TeamChemistry #LeadershipThroughJoy #VolleyballLove #FileninSultanlari #TurkiyeVolley #AthleteMindset #PositiveCulture #HighPerformanceJoy #NoFearJustJoy #ChampionSmiles #VargasEnergy #UnleashYourGreatness #CourtPresence #FinishStrong #LoveTheGame`,
  },

  {
    imageIndex: 5,
    headline: "BELONGING IS EARNED, NOT INHERITED.",
    text: `When Melissa Vargas stepped onto Turkish soil and put on the national jersey, she wasn't just joining a volleyball roster—she was embracing a people who embraced her back.

National pride isn't just about where your birth certificate was signed. It is about where you pour your sweat, your tears, and your deepest commitment.

Türkiye gave Melissa a home when she needed one most. In return, Melissa gave Türkiye its first-ever European and Nations League championships.

When leaders create a culture of unconditional belonging, extraordinary loyalty and historic performance follow.

Learn about inclusive leadership frameworks: https://lornettedaye.com/inclusion

#CultureOfBelonging #TurkiyeHome #MelissaVargas #InclusiveLeadership #LornetteDaye #LoyaltyAndMerit #EmbraceTheOutsider #NationalUnity #SportsDiplomacy #OneFlagOneJourney #EuroVolleyChampions #FileninSultanlari #BelongingMatters #LeadershipCulture #GlobalCitizens #HeartOverBorders #ChampionshipBond #TrueInclusion #FinishStrong #EmpoweredWomen`,
  },

  {
    imageIndex: 6,
    headline: "112 KM/H: THE MECHANICS OF FEARLESS COMMITMENT.",
    text: `A 112 km/h spike does not happen through brute strength alone.

It requires perfect approach timing, an explosive vertical coil from the hips, full thoracic extension, and absolute, fearless commitment on the swing.

If you hesitate for 0.05 seconds, the block closes and the attack is neutralized.

Hesitation kills high performance. Once you analyze the court and choose your lane: accelerate through the ball.

Commit fully to your vision.

Explore athletic biomechanics and coaching: https://lornettedaye.com/athlete-coaching

#112KMH #FearlessCommitment #SpikeMechanics #MelissaVargas #LornetteDaye #BiomechanicsInSport #VolleyballScience #AccelerateThroughTheBall #NoHesitation #ClutchAttack #HighPerformanceBiomechanics #OlympicStandard #PhysicalMastery #PowerAndPrecision #FinishStrong #CoachingWisdom #FlawlessExecution #AttackTheMoment #VolleyballWorld #PowerHitter`,
  },

  {
    imageIndex: 7,
    headline: "HOW CHAMPIONS CARRY THE WEIGHT OF A NATION.",
    text: `85 million people in Türkiye live and breathe every point when the national women's volleyball team takes the court.

Carrying that level of expectation can crush an unprepared athlete.

Melissa Vargas handles that weight not by trying to shoulder it alone, but by feeding off the love of the supporters and channeling the collective heartbeat of the nation into her game.

Great leaders don't buckle under expectation; they transform pressure into a privilege and an honor.

Discover executive resilience coaching: https://lornettedaye.com/leadership

#WeightOfANation #PressureAsPrivilege #MelissaVargas #TurkiyeLove #LornetteDaye #ExecutiveEndurance #LeadingUnderPressure #FileninSultanlari #NationalHeroes #VolleyballPassion #MindsetOfAChampion #MentalStamina #HandleTheExpectation #ChampionshipCharacter #FinishStrong #LeadershipFrameworks #GraceUnderPressure #InspiringNations #SportsLeadership #TrueIcon`,
  },

  {
    imageIndex: 8,
    headline: "REBUILDING IN SILENCE: THE YEARS NOBODY TALKS ABOUT.",
    text: `Between 2016 and 2021, while international headlines were talking about other players, Melissa Vargas was grinding in club gyms across Switzerland, China, and Istanbul.

No national team spotlight. No global television broadcasts. Just the relentless, daily repetition of sharpening her tools.

Never underestimate someone who was forced to rebuild in the shadows. When they finally step into the light, nothing can stop them because they have already survived the darkness.

Trust your quiet season. It is preparing you for your biggest stage.

Read 'Surviving Life' by Lornette Daye: https://lornettedaye.com/book

#QuietSeason #RebuildInSilence #MelissaVargas #GrindInTheDark #LornetteDaye #SurvivingLifeBook #UnseenWork #PatienceAndPower #PreparationPays #VolleyballJourney #ComebackStory #UnstoppableForce #FaithInTheProcess #TrustTheGrind #FinishStrong #ResilienceInLife #SportsMotivation #LifeLessons #NeverDoubtYourself #ChampionMindset`,
  },

  {
    imageIndex: 9,
    headline: "WHEN YOU PLAY FOR SOMETHING BIGGER THAN YOURSELF.",
    text: `Why does Melissa Vargas dive across hardwood floors and throw her body into the stands for a ball that seems impossible to save?

Because she is not playing for individual statistics. She is playing for her teammates, her family, and the millions of young girls across Türkiye and Latin America watching her prove that boundaries are made to be broken.

When your purpose extends beyond your own ego, you unlock a reservoir of energy that ordinary competitors simply cannot access.

Find your 'Why'. It will carry you through every fourth-set deficit.

Explore youth empowerment & sports programs: https://lornettedaye.com/programs

#BiggerThanMyself #PurposeDrivenSport #MelissaVargas #DiveForEveryBall #LornetteDaye #YouthEmpowerment #UnselfishExcellence #TeamFirst #InspireTheNextGeneration #FileninSultanlari #VolleyballHeart #TruePurpose #UnstoppableDrive #FinishStrong #LeadershipPurpose #GirlPowerInSport #SportsRoleModel #OvercomeLimits #ChampionshipPurpose #ExcellenceInAction`,
  },

  {
    imageIndex: 10,
    headline: "FINISH STRONG: THE VARGAS STANDARD.",
    text: `In the fifth set of the European Championship final against Serbia, with the score tied and tension suffocating the arena:

Melissa Vargas demanded the ball on every crucial rotation. Down the line. Cross court. Off the block.

She finished strong because her entire life had trained her for that exact moment.

Whatever arena you find yourself competing in today—whether it's on the volleyball court, in the boardroom, or in the quiet battles of everyday life:

Don't back down.
Demand the ball.
Finish Strong.

Discover Lornette Daye's full coaching & keynote offerings: https://lornettedaye.com

#FinishStrong #TheVargasStandard #FifthSetMentality #MelissaVargas #LornetteDaye #ClutchExecution #EuroVolleyMVP #DemandingTheBall #ChampionSpirit #40YearsOfCoaching #OlympicExcellence #HighPerformanceLife #UnshakeableConfidence #LeadershipMastery #KeynoteSpeaker #AuthorFinishStrong #TrueEmpowerment #SportsWisdom #VolleyballQueen #NeverQuit`,
  },
  // Repeat narrative cycle for items 11-20 with fresh perspectives
  {
    imageIndex: 11,
    headline: "MELISSA VARGAS: THE ART OF REDEFINING IMPOSSIBLE.",
    text: `They told her that her shoulder would never hold up to world-class hitting again.
They told her that leaving her home country meant the end of her international career.

Today, Melissa Vargas is a European Champion, Nations League MVP, and the most feared outside hitter on the planet.

Never let someone else's limited imagination dictate your ceiling.

Discover coaching for barrier-breakers: https://lornettedaye.com/athlete-coaching

#RedefineImpossible #BreakAllCeilings #MelissaVargas #LornetteDaye #OvercomeTheOdds #VolleyballPower #FileninSultanlari #SportsInspiration #FinishStrong #TrueGreatness #ImmigrantExcellence #ChampionHeart #FearlessJourney #DefyTheDoubters #HighPerformanceLife`,
  },
  {
    imageIndex: 12,
    headline: "TACTICAL EXCELLENCE MEETS RAW ATHLETICISM.",
    text: `Power without tactical intelligence is wasted energy.

Watch how Melissa Vargas reads the setter's hands, identifies the seam in the opposing block, and alters her hitting angle in mid-air.

True mastery is where explosive physical power meets calm tactical discernment.

Sharpen both your mind and your body: https://lornettedaye.com/about

#TacticalMastery #MindAndBody #MelissaVargas #VolleyballTactics #LornetteDaye #AthleticIntelligence #CourtVision #SmartPower #EliteCoaching #FinishStrong #VolleyballExcellence #HighPerformance #StrategyInMotion #ChampionMindset #WomensVolleyball`,
  },
  {
    imageIndex: 13,
    headline: "THE POWER OF AN UNCONDITIONAL SUPPORT SYSTEM.",
    text: `No athlete survives exile and multi-year recovery without coaches, mentors, and teammates who believe in them when the scoreboard is blank.

Melissa's triumph is a testament to the Turkish Volleyball Federation's vision and her teammates' unconditional embrace.

Build ecosystems where human beings feel safe to take big risks and grow.

Explore team culture consulting: https://lornettedaye.com/leadership

#SupportSystems #TeamCulture #PsychologicalSafety #MelissaVargas #LornetteDaye #TurkiyeVolley #LeadershipCulture #ChampionEcosystem #FileninSultanlari #FinishStrong #SafeSport #MentorshipMatters #UnconditionalSupport #BuildGreatTeams #SportsGovernance`,
  },
  {
    imageIndex: 14,
    headline: "HUMILITY IN VICTORY: THE TRADEMARK OF A TRUE LEADER.",
    text: `Even after breaking scoring records and receiving tournament MVP trophies, Melissa Vargas's first instinct is always to point to her setter, celebrate her libero, and thank the fans.

Arrogance repels; humble greatness inspires a generation.

Lead with humility. Perform with ferocity.

Book Lornette Daye for your executive summit: https://lornettedaye.com/speaking

#HumbleGreatness #LeadWithHumility #MelissaVargas #TrueLeadership #LornetteDaye #ExecutiveWisdom #VolleyballCulture #TeamFirst #InspireGenerations #FileninSultanlari #FinishStrong #KeynoteSpeaker #ChampionCharacter #GraceInVictory #SportsLegacy`,
  },
  {
    imageIndex: 15,
    headline: "RESILIENCE IS A DAILY MUSCLE, NOT A ONE-TIME ACT.",
    text: `People think resilience is something you summon only during a crisis.

In reality, resilience is built in the daily, unrecorded discipline of sleeping properly, eating clean, showing up for rehab on rainy mornings, and protecting your mental peace.

Melissa Vargas is resilient because she practices resilience every single day.

Strengthen your foundation: https://lornettedaye.com/programs

#DailyResilience #DisciplineOverMotivation #MelissaVargas #HabitsOfChampions #LornetteDaye #FinishStrongBook #ConsistentWork #VolleyballGrit #AthleteRoutine #SelfMastery #MindsetMatters #HighPerformanceHabits #SustainableSuccess #TurkiyePride #SportsPsychology`,
  },
  {
    imageIndex: 16,
    headline: "THE SPEED OF TRANSFORMATION: TRUSTING THE TIMELINE.",
    text: `When you are in the middle of a career transition or personal wilderness, days feel like months.

Melissa spent years waiting for citizenship and international clearance. She didn't waste that time complaining—she used it to get stronger.

When your time comes, make sure you are ready.

Read more about career transitions: https://lornettedaye.com/blog

#TrustTheTimeline #CareerTransition #MelissaVargas #PrepareInSilence #LornetteDaye #VolleyballJourney #PatienceAndPreparation #DivineTiming #AthleteTransition #FinishStrong #MentalEndurance #StayReady #OpportunityMeetsPreparation #TurkiyeVolley #LeadershipJourney`,
  },
  {
    imageIndex: 17,
    headline: "DEFENSE WINS CHAMPIONSHIPS: THE UNSEEN VARGAS IMPACT.",
    text: `Everyone talks about her 112 km/h spikes.

But watch Melissa Vargas sprint to cover behind the block, dig balls out of the net, and communicate on transition defense.

Superstars who commit to defense are the ones who hang championship banners.

Never be too big to do the dirty work.

Explore sports performance frameworks: https://lornettedaye.com/athlete-coaching

#DoTheDirtyWork #TransitionDefense #ChampionshipDefense #MelissaVargas #LornetteDaye #UnsungEffort #VolleyballDefense #TotalAthlete #FileninSultanlari #FinishStrong #TeamWorkEthic #HumilityInAction #HighPerformanceStandard #VolleyballWorld #ChampionWork`,
  },
  {
    imageIndex: 18,
    headline: "THE GLOBAL SISTERHOOD OF WOMEN'S SPORT.",
    text: `From Cuban youth courts to European arenas: Melissa Vargas represents the unstoppable rise of women's sports across the globe.

Sold-out arenas. Millions of television viewers. Young girls wearing #4 jerseys in every Turkish city.

Women's sports is not an alternative; it is the premier sports phenomenon of our time.

Invest in female athletics: https://lornettedaye.com/impact

#WomensSportsRise #GlobalSisterhood #MelissaVargas #InvestInWomen #LornetteDaye #WomenInVolleyball #FileninSultanlari #EmpoweringGirls #SportsPhenomenon #FinishStrong #NextGenerationLeaders #EqualPlay #InspireTheWorld #SportsImpact #Trailblazer`,
  },
  {
    imageIndex: 19,
    headline: "STANDING TALL IN THE ARENA: OWNING YOUR POWER.",
    text: `Standing 6'4", tattooed, vibrant, and unapologetically herself:

Melissa Vargas refuses to shrink so that others feel comfortable. She owns every inch of her height, every decibel of her power, and every piece of her identity.

Never apologize for your magnitude. Take up space.

Discover personal empowerment with Lornette Daye: https://lornettedaye.com/about

#OwnYourPower #TakeUpSpace #UnapologeticallyYou #MelissaVargas #LornetteDaye #AuthenticConfidence #StandTall #EmpoweredWomen #VolleyballQueen #FileninSultanlari #FinishStrong #SelfBelief #MagnificentExcellence #BeBold #LeadershipPresence`,
  },
  {
    imageIndex: 20,
    headline: "YOUR FINISH LINE IS WAITING: RUN TOWARD IT.",
    text: `In 40+ years of coaching, I have never seen a champion who didn't have to fight through a season of doubt.

Melissa Vargas fought through exile, injury, and uncertainty—and emerged as a global icon and European champion.

Your past does not define you. Your obstacles do not define you. Your response defines you.

Fight through. Believe. Finish Strong.

Connect with Lornette Daye: https://lornettedaye.com

#YourFinishLine #RunTowardIt #FinishStrong #MelissaVargas #LornetteDaye #40YearsOfExcellence #OlympicCoach #TurkiyeHero #VolleyballLegend #NeverGiveUp #ChampionMindset #LifeBeyondLimits #KeynoteSpeaker #HighPerformanceCoach #TriumphInSport`,
  },
];

async function main() {
  console.log('======================================================');
  console.log('Melissa Vargas 3-Week Campaign: 63 Posts / 21 Days');
  console.log('Times: 9:00 AM, 1:00 PM, and 6:30 PM MDT');
  console.log('======================================================\n');

  const manifestPath = path.join(process.cwd(), 'scripts', 'campaign-manifest.json');
  let manifest = [];
  if (fs.existsSync(manifestPath)) {
    manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  }

  const timeSlots = [
    { label: '9:00 AM MDT', utcOffset: 15, hour: 9, minute: 0 },
    { label: '1:00 PM MDT', utcOffset: 19, hour: 13, minute: 0 },
    { label: '6:30 PM MDT', utcOffset: 0.5, hour: 18, minute: 30 },
  ];

  let idCounter = manifest.length > 0 ? Math.max(...manifest.map(m => m.id)) : 0;
  const daysCount = 21;
  let postCount = 0;

  for (let day = 1; day <= daysCount; day++) {
    timeSlots.forEach((slot, slotIdx) => {
      const captionObj = vargasCaptions[postCount % vargasCaptions.length];
      const imgFile = `vargas-${String(captionObj.imageIndex).padStart(2, '0')}.png`;
      const fullImageUrl = `${BASE_IMAGE_URL}/${imgFile}`;

      let dueYear = 2026;
      let dueMonth = 7; // August
      let dueDay = 30 + (day - 1);
      let dueHour = slot.utcOffset;
      let dueMinute = 0;

      if (slotIdx === 2) {
        dueDay += 1;
        dueHour = 0;
        dueMinute = 30;
      }

      const targetDate = new Date(Date.UTC(dueYear, dueMonth, dueDay, dueHour, dueMinute, 0, 0));
      idCounter++;
      postCount++;

      manifest.push({
        id: idCounter,
        campaign: 'melissa-vargas-3week',
        day: day,
        timeMDT: slot.label,
        dueAt: targetDate.toISOString(),
        imageIndex: captionObj.imageIndex,
        imageFile: imgFile,
        imageUrl: fullImageUrl,
        headline: captionObj.headline,
        text: captionObj.text,
        status: 'pending',
        bufferPostId: null,
      });
    });
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
  console.log(`🎉 Successfully saved 63 Melissa Vargas posts! Total posts in master manifest: ${manifest.length}`);
}

if (process.argv[1]?.includes('schedule-vargas-campaign.mjs')) {
  main().catch(console.error);
}
