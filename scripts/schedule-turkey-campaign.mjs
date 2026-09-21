/**
 * Türkiye Athlete Investment & Holistic Well-Being Campaign
 * 20 High-Impact Pain-Point Captions | Maximum Hashtag Stack | Lornette Daye Voice
 * 
 * Schedule: 7-Day High-Frequency Sprint (3x Daily at 9:00 AM, 1:00 PM, and 6:30 PM MDT)
 * Creatives: https://lornettedaye.com/campaigns/turkey/turkey-01.png to turkey-20.png
 */

import fs from 'fs';
import path from 'path';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/turkey';

export const turkeyCaptions = [
  {
    imageIndex: 1,
    headline: "CONGRATULATIONS, TÜRKIYE. YOU'RE INVESTING IN ATHLETES, NOT JUST MEDALS.",
    text: `For over 40 years as an Olympian coach and Canadian National Champion, I have witnessed the same heartbreak repeatedly:

Nations love waving flags when an athlete wins gold, but they vanish when that same athlete is working three jobs just to buy groceries and cover physiotherapy.

Türkiye's comprehensive athlete support model—providing direct monthly stipends, accommodation, travel, nutrition, and equal backing across Olympic, Paralympic, and Deaflympic disciplines—is what true sports leadership looks like.

The athlete is a human being before they are a medal count.

Developing the athlete. Preparing the person. Building the future.

Learn about athlete development frameworks: https://lornettedaye.com/athlete-coaching

#TurkiyeSports #AthleteWelfare #HolisticAthlete #OlympicDevelopment #ParalympicPride #Deaflympics #SportsPolicy #LornetteDaye #AthleteFirst #DevelopingTheAthlete #SportsGovernance #DirectAthleteSupport #HighPerformance #HumanRightsInSport #EquitableFunding #SportsReform #PodiumFunding #AthleteAdvocacy #OlympicStandard #FinishStrong`,
  },

  {
    imageIndex: 2,
    headline: "DON'T JUST CELEBRATE THE MEDAL. SUPPORT THE JOURNEY.",
    text: `Talent should never have to choose between surviving and competing.

When young athletes are forced to quit because they cannot afford travel to international qualifiers or basic sports nutrition, that is not a failure of their talent—it is a systemic failure of leadership.

Greatness is not manufactured on the podium. It is forged in empty training halls at 5:00 AM during years of untelevised sacrifice.

If a society wants the glory of champions, it must shoulder the burden of their development.

Discover athlete mentorship & well-being programs: https://lornettedaye.com/mentorship

#SupportTheJourney #TalentWithoutBarrier #GrassrootsSport #AthleteSurvival #HighPerformanceFunding #LornetteDaye #SportsPhilanthropy #SafeSport #AthleteDignity #OlympicDream #ParalympicAthletes #DeaflympicExcellence #SportsEconomics #SustainableAthletics #CoachingMatters #NextGenAthletes #SportsPolicyReform #FinishStrong #ChampionMindset #AthleteDevelopment`,
  },

  {
    imageIndex: 3,
    headline: "AN ATHLETE'S DIGNITY IS NOT NEGOTIABLE.",
    text: `When funding is tied exclusively to a podium finish, it creates a toxic culture of fear, burnout, and premature retirement.

What happens when an elite athlete suffers an injury?
What happens when they finish fourth by 0.01 seconds?
Does their years of dedication suddenly lose all value?

Basic monthly living security allows competitors to train with psychological safety, innovate in their craft, and perform without crippling existential anxiety.

Treat athletes with the dignity they deserve.

Explore organizational wellness and leadership keynotes: https://lornettedaye.com/leadership

#AthleteDignity #PsychologicalSafety #MentalHealthInSports #PodiumPressure #LornetteDaye #SportsIntegrity #AthleteWellbeing #HighPerformanceCulture #DutyOfCare #OlympicGovernance #ParalympicMovement #DeaflympicsLeadership #CoachingEthics #SustainablePerformance #SportsReform #ExecutiveLeadership #WholePersonCare #HumanFirst #FinishStrong #SafeSport`,
  },

  {
    imageIndex: 4,
    headline: "PARALYMPIC & DEAFLYMPIC EQUALITY IS NON-NEGOTIABLE.",
    text: `True sports equity is not about token PR statements—it is about equal checks, equal medical access, and equal institutional respect.

Paralympians and Deaflympians train with the exact same relentless intensity, sacrifice, and tactical discipline as any Olympic champion.

Türkiye setting a global benchmark by ensuring equal developmental resources across Olympic, Paralympic, and Deaflympic pipelines is a powerful message to every sports federation worldwide.

Inclusion is an active investment, not passive sympathy.

Read about inclusion and equity in sports: https://lornettedaye.com/inclusion

#ParalympicEquity #DeaflympicsVisibility #AdaptiveSports #TrueInclusion #EqualFunding #LornetteDaye #DisabilityAdvocacy #SportsForEveryone #AccessibleAthletics #GlobalInclusion #ParalympicChampion #DeafSport #HighPerformanceEquity #InstitutionalReform #LeadByExample #EmpowerAllAthletes #SportsPolicy #UniversalDesign #FinishStrong #OneFlagOneJourney`,
  },

  {
    imageIndex: 5,
    headline: "BEYOND THE PODIUM: PREPARING FOR LIFE AFTER SPORT.",
    text: `What happens when the national anthem fades and the career comes to an end?

Too many retired athletes face identity crises, financial instability, and emotional isolation because their entire worth was reduced to physical metrics.

Developing the athlete must include preparing the person:
• Dual-career education
• Financial literacy
• Mental health counseling
• Executive transition mentorship

When we invest in their mind and character, we build leaders who transform society long after their spikes are hung up.

Discover Lornette's dual-career transition programs: https://lornettedaye.com/programs

#LifeAfterSport #AthleteTransition #DualCareer #CareerTransition #MentalHealthMatters #LornetteDaye #DevelopingTheAthlete #PreparingThePerson #BuildingTheFuture #AthleteAdvocacy #SportsEducation #LeadershipDevelopment #LifeSkillsThroughSport #PostAthleticCareer #HolisticDevelopment #FinishStrong #EmpoweringAthletes #FutureLeaders #TransformativeSport #AthleteWellbeing`,
  },

  {
    imageIndex: 6,
    headline: "GRASSROOTS TO GOLD: WHY EARLY INVESTMENT MATTERS.",
    text: `You cannot harvest a championship crop without planting seeds and nourishing the soil for a decade.

Too many corporate sponsors and sports bodies wait until an athlete is already famous before offering support. By then, hundreds of equally gifted athletes have already fallen through the cracks due to poverty.

Early monthly stipends, access to quality coaching, and covered travel costs are what turn raw potential into world-class excellence.

Invest early. Invest consistently. Watch human greatness flourish.

Book Lornette Daye for your keynote summit: https://lornettedaye.com/speaking

#GrassrootsToGold #EarlyInvestment #TalentIdentification #YouthSportsDevelopment #LornetteDaye #SportsFunding #CorporateSponsorship #SocialImpactInSport #BuildingChampions #OlympicPipeline #ParalympicTalent #DeaflympicsDevelopment #LongTermAthleteDevelopment #SportsInfrastructure #PatienceInExcellence #HighPerformanceLeadership #KeynoteSpeaker #FinishStrong #GlobalAthletics #Empowerment`,
  },

  {
    imageIndex: 7,
    headline: "THE REAL COST OF ELITE ATHLETICS.",
    text: `Let's talk about the numbers nobody likes to discuss:

• International airfare and baggage fees for adaptive equipment.
• Specialized physio, osteopathy, and injury rehab.
• Clean, calorie-dense nutrition and supplements.
• High-performance coaching and facility access.

When federations leave these expenses to athletes and their families, only the wealthy survive. True democracy in sport requires institutional funding that levels the playing field for everyone.

Level the field. Lift the athlete.

Explore sports consulting with Lornette Daye: https://lornettedaye.com/about

#RealCostOfSport #LevelThePlayingField #SocioeconomicEquityInSport #SportsEconomics #LornetteDaye #HighPerformanceInfrastructure #AthleteAdvocacy #SportsNutrition #PhysiotherapyAccess #DemocratizeSport #OlympicCost #ParalympicFunding #GrassrootsAdvocacy #InstitutionalResponsibility #SportsReform #FinishStrong #AthleticsCanada #GlobalSportsGovernance #SafeSport #LeadershipVision`,
  },

  {
    imageIndex: 8,
    headline: "DEVELOPING THE ATHLETE. PREPARING THE PERSON. BUILDING THE FUTURE.",
    text: `This is not just my personal coaching philosophy—it is the moral imperative for 21st-century sport.

When coaches and federations treat athletes as disposable tools for medals, they break spirits. When we nurture their emotional intelligence, leadership, and personal dignity, they perform at heights they never dreamed possible.

Great champions are built from the inside out.

Let's build a sporting world where athletes thrive before, during, and long after competition.

Order 'Finish Strong' by Lornette Daye: https://lornettedaye.com/books

#DevelopingTheAthlete #PreparingThePerson #BuildingTheFuture #LornetteDaye #FinishStrongBook #HolisticCoaching #HumanCenteredSport #CoachingPhilosophy #40YearsOfExcellence #ChampionBuilder #OlympicCoach #ParalympicDevelopment #AthleteEmpowerment #TransformationalCoaching #SportsPsychology #MindBodySpirit #PodiumSuccess #SustainableGreatness #LeadershipWisdom #LegacyInSport`,
  },

  {
    imageIndex: 9,
    headline: "ENDING THE ERA OF DISPOSABLE ATHLETES.",
    text: `How many promising juniors have you seen disappear after a single ACL tear?

When nations only fund athletes who are currently winning, they encourage risky overtraining, concealing injuries, and irreversible physical damage.

Direct monthly safety nets guarantee that an injured athlete can take the necessary 12 months of rehab without fearing homelessness or losing their career.

Sustainable sports systems protect their most vulnerable assets: their people.

Discover athlete health & longevity strategies: https://lornettedaye.com/athlete-coaching

#EndDisposableSport #InjuryRehab #AthleteSafety #DutyOfCareInSports #LornetteDaye #SustainableAthletics #SportsLongevity #PreventBurnout #SafeSportMovement #AthleteFirst #OlympicHealth #ParalympicCare #MentalResilience #LongTermCare #SportsGovernanceReform #CoachingEthics #FinishStrong #HumanFirstAthleteSecond #TrueLeadership #SportsCare`,
  },

  {
    imageIndex: 10,
    headline: "TÜRKIYE: SETTING THE BLUEPRINT FOR GLOBAL SPORT GOVERNANCE.",
    text: `When a nation commits to direct monthly athlete stipends, universal lodging, nutritional support, and equal development across Olympic, Paralympic, and Deaflympic sports, it sets a gold standard that every international federation should emulate.

Sport is one of the greatest vehicles for national unity, youth health, and global prestige.

Investing directly into the living conditions of athletes is the highest-return investment a country can make.

Bravo, Türkiye. The sporting world is taking notice. 🇹🇷👏

Connect with Lornette Daye: https://lornettedaye.com

#TurkiyeModel #GlobalBlueprint #SportsGovernance #NationalPride #TurkiyeAthletes #LornetteDaye #OlympicInvestment #ParalympicSupport #DeaflympicsLeadership #SportsDiplomacy #FutureOfSport #HighPerformanceEcosystem #InternationalAthletics #NationalSportsReform #ChampionNations #InvestInPeople #SportsLeadership #PolicyMakers #FinishStrong #ExcellenceInAction`,
  },

  {
    imageIndex: 11,
    headline: "DON'T JUST CHEER THE WINNER. SUPPORT HER WHILE SHE IS BECOMING.",
    text: `It takes zero courage to jump on the bandwagon when a young woman stands on top of the world with gold around her neck.

Real leadership is believing in her, funding her travel, securing her nutrition, and shielding her from exploitation when she is still ranked outside the top 100.

Nurture the process. Protect the dreamers. Great nations invest before the medal.

Learn about women's leadership initiatives: https://lornettedaye.com/programs

#WhileSheIsBecoming #WomenInSport #NurturePotential #InvestBeforeTheMedal #LornetteDaye #FemaleAthletics #GrassrootsEmpowerment #NextGenWomen #OlympicWomen #ParalympicWomen #DeaflympicWomen #SheCanLead #SportsEquity #SupportHerJourney #FinishStrong #HighPerformanceMindset #SafeSport #ChampionTheFuture #GirlPowerInSport #LegacyBuilders`,
  },

  {
    imageIndex: 12,
    headline: "FEMALE ATHLETES DESERVE FINANCIAL INDEPENDENCE.",
    text: `When female competitors lack direct financial stipends, they become vulnerable to predatory sponsorships, toxic power dynamics, and premature career abandonment.

Direct athlete funding provides autonomy.
Direct athlete funding provides security.
Direct athlete funding provides leverage.

When women in sports are financially empowered, they lead with authority on and off the court.

Explore executive coaching & female athlete advocacy: https://lornettedaye.com/leadership

#FinancialIndependenceInSport #WomenAthletes #EmpowerWomenInSport #EqualPayInSports #LornetteDaye #AthleteAutonomy #SafeSport #FemaleLeadership #SportsEquity #FinancialLiteracy #WomensSportsMatter #ProtectFemaleAthletes #OlympicEquality #ParalympicEquality #DeaflympicEquality #FinishStrong #ExecutivePresence #WomenWhoLead #SportsBusiness #FairPlay`,
  },

  {
    imageIndex: 13,
    headline: "THE SILENT CRISIS: MENTAL HEALTH UNDER THE NATIONAL FLAG.",
    text: `Carrying the expectations of an entire nation on your shoulders is a heavy burden for a 20-year-old athlete.

When fear of losing funding is added to the pressure of global competition, mental health collapses.

Comprehensive athlete support must include professional sports psychologists, confidential counseling, and unconditional institutional backing.

A healthy mind produces an enduring champion.

Read about mental performance frameworks: https://lornettedaye.com/blog

#MentalHealthInSports #AthleteMindset #SilentCrises #PsychologicalSupport #LornetteDaye #MindHealthMatters #OlympicPressure #BreakTheStigma #SportsPsychology #MentalFortitude #HealthyAthletes #AthleteWellbeing #InnerPeaceOuterPower #WholeAthlete #FinishStrong #SafeSportEnvironment #CoachingCompassion #DutyOfCare #SportsMedicine #ChampionHealth`,
  },

  {
    imageIndex: 14,
    headline: "40 YEARS ON THE FRONTLINES OF COACHING EXCELLENCE.",
    text: `Over four decades in international track & field and high-performance coaching, I have coached athletes to national titles, Olympic qualifications, and podium finishes.

The single biggest lesson I have learned?

Coaching is not about imposing your ego on an athlete; it is about creating an ecosystem where their unique genius can safely emerge.

Support systems matter more than drills.

Book Lornette Daye for high-performance team coaching: https://lornettedaye.com/athlete-coaching

#40YearsOfCoaching #FrontlinesOfExcellence #OlympicCoach #HighPerformanceEcosystem #LornetteDaye #TrackAndField #MasteryInSport #CoachingExcellence #ChampionMaker #MentorshipMatters #LeadershipPhilosophy #SportsLegacy #CanadianTrack #InternationalAthletics #FinishStrong #DevelopingChampions #TrueGreatness #AthleteFirst #ExperienceCounts #TransformationalLeadership`,
  },

  {
    imageIndex: 15,
    headline: "SUSTAINABLE ATHLETIC PATHWAYS: FROM DISCOVERY TO RETIREMENT.",
    text: `A world-class sports system is not a lottery where 99% of participants are discarded.

It is a well-structured pipeline that:
1. Discovers talent in every region and socioeconomic background.
2. Nurtures fundamental athletic literacy without early burnout.
3. Provides full living, nutritional, and medical support at the elite level.
4. Transitions athletes seamlessly into coaching, governance, or enterprise careers.

Build systems that last generations.

Discover sports governance consulting: https://lornettedaye.com/about

#SustainableSport #AthleticPathways #TalentPipeline #SystemicSportsDesign #LornetteDaye #LongTermDevelopment #GrassrootsInfrastructure #SportsGovernance #NoAthleteLeftBehind #OlympicLegacy #ParalympicPipeline #DeaflympicPathways #SportsManagement #BuildForGenerations #HighPerformanceStrategy #FinishStrong #SportsEcosystem #PolicyDesign #GlobalAthletics #TransformSport`,
  },

  {
    imageIndex: 16,
    headline: "PARALYMPIC CHAMPIONS ARE HIGH-PERFORMANCE ICONS.",
    text: `Let's stop treating adaptive athletics as a charity project.

The engineering, physiological adaptations, and mental fortitude required to master wheelchair racing, blind sprinting, and seated throws are among the highest feats of human performance on earth.

Paralympic athletes deserve prime-time broadcast coverage, equal corporate sponsorships, and equal national funding.

Recognize excellence for what it is.

Explore inclusion and diversity programs with Lornette: https://lornettedaye.com/inclusion

#ParalympicIcons #HighPerformanceAdaptive #WheelchairAthletics #BlindSprinting #LornetteDaye #EliteAdaptiveSport #EqualCoverage #ParalympicPride #UnstoppableAthletes #SportsEngineering #ExtremeHumanPerformance #DisabilityIsPower #AdaptiveExcellence #FinishStrong #InclusionInAction #OneFlagOneJourney #InspireTheWorld #UniversalSports #ParalympicStandard #BreakAllBarriers`,
  },

  {
    imageIndex: 17,
    headline: "SAFEGUARDING SPORT: RESPECT, DIGNITY, AND EQUAL ACCESS.",
    text: `Every athlete has the fundamental human right to train and compete in an environment free from abuse, harassment, financial exploitation, and neglect.

Safe sport is not an optional add-on—it is the non-negotiable bedrock of all ethical athletic governance.

When nations institute direct, transparent monthly support, they strip away the corrupt leverage that abusers have traditionally held over vulnerable athletes.

Transparency builds trust. Trust creates champions.

Learn about Lornette's Safe Sport advocacy: https://lornettedaye.com/impact

#SafeSport #AthleteSafeguarding #TransparencyInSport #HumanRightsInAthletics #LornetteDaye #EthicalGovernance #ProtectOurAthletes #ZeroTolerance #DignityInSport #SportsPolicy #AthleteProtection #TrustAndIntegrity #SafeTrainingEnvironments #OlympicValues #ParalympicIntegrity #DeaflympicSafety #FinishStrong #SpeakUpForSport #TrueLeadership #DutyOfCare`,
  },

  {
    imageIndex: 18,
    headline: "THE UNSUNG HEROES: OLYMPIC FAMILIES.",
    text: `Behind every athlete you see on television is a mother who worked overtime shifts, a father who drove hundreds of miles to weekend meets, and siblings who sacrificed vacations so travel fees could be paid.

When sports systems fail to fund athletes, the burden falls squarely on working-class families.

Universal sports stipends take the financial stranglehold off families and allow athletes to compete on pure merit.

To every sports parent and family member: we see you, we honor you, and we fight for systemic change on your behalf.

Read 'Finish Strong' by Lornette Daye: https://lornettedaye.com/book

#UnsungHeroes #SportsParents #OlympicFamilies #SacrificeForGreatness #LornetteDaye #FamilySupportInSport #GrassrootsRealities #WorkingClassChampions #CommunityImpact #ParentalDedication #SupportOurAthletes #FinishStrongBook #SystemicRelief #TrueChampions #FamilySacrifice #SportsMoments #HeartOfSport #BehindTheGold #SportsCommunity #LegacyOfLove`,
  },

  {
    imageIndex: 19,
    headline: "GLOBAL SPORTS POLICY: LESSONS FROM THE FRONTLINES.",
    text: `Sports ministers and federation presidents frequently ask: 'How do we win more international medals?'

The answer is surprisingly simple:
Stop spending 80% of your budget on executive travel and administrative bureaucracy. Redirect the resources directly into the bank accounts, dinner plates, and physical therapy rooms of the athletes and coaches doing the actual work.

Cut bureaucracy. Fund athletes. Win medals.

Connect with Lornette Daye for organizational audits: https://lornettedaye.com/programs

#SportsPolicyAudit #DirectAthleteFunding #CutTheBureaucracy #SportsGovernance #LornetteDaye #HighPerformanceReform #AthleteFirstPolicy #OlympicPolicy #ParalympicGovernance #DeaflympicSupport #SportsAdministration #CleanSport #ResultsDrivenPolicy #GlobalSportsStrategy #EfficiencyInSport #FinishStrong #ExecutiveAuditing #LeadFromFront #InvestInTalent #TransformationalPolicy`,
  },

  {
    imageIndex: 20,
    headline: "FINISH STRONG: THE ATHLETE'S JOURNEY BEYOND THE FINAL WHISTLE.",
    text: `Your career as an active competitor may span 10 or 15 years.
Your life as a human being spans 80.

When we develop the whole person—equipping them with unshakeable self-worth, academic credentials, and ethical leadership tools—we ensure that their greatest victory is not a gold medal won at age 24, but the lasting impact they create for the rest of their lives.

Developing the Athlete.
Preparing the Person.
Building the Future.

Finish Strong. Always.

Explore Lornette Daye's full body of work: https://lornettedaye.com

#FinishStrong #DevelopingTheAthlete #PreparingThePerson #BuildingTheFuture #LornetteDaye #40YearsOfImpact #OlympicLegacy #ParalympicExcellence #DeaflympicsLeadership #WholePersonGreatness #LifeBeyondSport #ChampionMentality #KeynoteSpeaker #HighPerformanceCoach #AuthorFinishStrong #GenerationalImpact #HumanFirst #ExcellenceInLife #SportsInspiration #TheFinalFinish`,
  },
];

async function main() {
  console.log('======================================================');
  console.log('Türkiye Athlete Well-Being Sprint: 20 Posts / 7 Days');
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

  for (let i = 0; i < turkeyCaptions.length; i++) {
    const captionObj = turkeyCaptions[i];
    const day = Math.floor(i / 3) + 1;
    const slotIdx = i % 3;
    const slot = timeSlots[slotIdx];
    const imgFile = `turkey-${String(captionObj.imageIndex).padStart(2, '0')}.png`;
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

    manifest.push({
      id: idCounter,
      campaign: 'turkey-athlete-wellbeing',
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
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
  console.log(`🎉 Successfully saved 20 Türkiye Athlete Welfare posts! Total posts in master manifest: ${manifest.length}`);
}

export const turkeyPosts = turkeyCaptions;

if (process.argv[1]?.includes('schedule-turkey-campaign.mjs') || process.argv[1]?.endsWith('schedule-turkey-campaign')) {
  main().catch(console.error);
}
