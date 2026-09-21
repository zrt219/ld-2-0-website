/**
 * Naomi Osaka Fashion & Power Series - 10-Day Campaign (3x Daily = 30 Posts)
 * Maximum Hashtag Stack | Couture Visuals | Lornette Daye Voice
 * 
 * Image Assets: https://lornettedaye.com/campaigns/osaka/osaka-01.png through osaka-10.png
 * Times: 9:00 AM, 1:00 PM, and 6:30 PM MDT
 */

import fs from 'fs';
import path from 'path';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/osaka';

export const osakaCaptions = [
  // 1. The Moment / Ritual & Focus
  {
    imageIndex: 1,
    headline: "BEFORE THE MATCH, THERE IS THE MOMENT.",
    text: `Before the first serve is struck. Before the applause erupts. Before the scoreboard flickers to life.

There is the quiet corridor walk.

In 40+ years of training elite Olympians and national champions, I have learned that peak performance is decided long before you step into the light. It is decided in the sacred ritual of preparation—where tradition, transformation, and relentless focus converge into a single moment of absolute clarity.

Naomi Osaka doesn't just enter an arena; she brings an entire universe of intentionality with her.

How do you prepare your mind before entering your highest-stakes arena?

Discover executive & high-performance mindset coaching: lornettedaye.com/athlete-coaching

#NaomiOsaka #PeakPerformance #MentalPreparation #HighPerformanceMindset #RitualOfExcellence #LornetteDaye #AthleteMindset #USOpen #GrandSlamTennis #WTA #FinishStrong #LeadershipExcellence #ArthurAshe #FocusAndDiscipline #ChampionshipMindset #WomenInSport #FashionInSport #CenterCourt #SportsPsychology #OlympicStandard`,
  },

  // 2. Roots & Heritage / Superpower
  {
    imageIndex: 2,
    headline: "HER ROOTS DON'T STAY OFF COURT. FROM JAPAN TO THE WORLD.",
    text: `Your heritage is not something you leave in the locker room. It is the soil from which your strength grows.

From Osaka to Port-au-Prince, from Tokyo to New York: Naomi Osaka brings every thread of her ancestry onto the court. The discipline of Japanese craftsmanship, the fiery resilience of Haitian spirit, and the bold ambition of a modern global icon.

When you know who you are and where you come from, no opponent's intimidation tactics can shake your foundation.

Authenticity is the ultimate competitive advantage. Never water down who you are to fit into someone else's comfort zone.

Explore diversity, equity, and authentic leadership programs: lornettedaye.com/inclusion

#NaomiOsaka #HeritageIsPower #MulticulturalExcellence #AuthenticLeadership #LornetteDaye #RepresentationMatters #JapaneseHeritage #HaitianPride #WomenOfImpact #USOpen2026 #CultureAndSport #GlobalCitizenship #BlackAndAsianExcellence #TennisIcon #LeadershipPresence #IdentityInSport #FinishStrong #SelfWorth #OwnYourStory #InclusiveLeadership`,
  },

  // 3. Transformation / Stepping into Greatness
  {
    imageIndex: 3,
    headline: "SHE WALKS IN ONE PERSON. SHE STEPS ON COURT TRANSFORMED.",
    text: `Off the court, she is soft-spoken, thoughtful, and deeply introspective.

On the court, she is a 4-time Grand Slam champion who strikes the ball with surgical violence and unyielding authority.

This is the art of psychological transformation.

Great leaders and elite athletes master the ability to flip the internal switch. You can be gentle in spirit while being ferocious in execution. You do not need to be loud to command absolute respect; your work will deliver the message.

Step onto your court with undeniable conviction.

Book Lornette Daye for your next keynote or executive masterclass: lornettedaye.com/speaking

#Transformation #TheSwitch #QuietConfidence #NaomiOsaka #LornetteDaye #ExecutivePresence #HighPerformance #KeynoteSpeaker #MasteryInMotion #WomenWhoLead #ChampionshipExecution #MentalFortitude #TennisCommunity #GrandSlamChampion #UnapologeticExcellence #PowerAndGrace #InnerStrength #ArthurAsheStadium #FinishStrong #SportsLeadership`,
  },

  // 4. Power Has No Single Look / Shattering Stereotypes
  {
    imageIndex: 4,
    headline: "WHO SAID POWER HAS ONE LOOK?",
    text: `Bows. Pearls. Ruffles. And a devastating 120-mph first serve.

For decades, women in sports were told to tone down their femininity if they wanted to be taken seriously as fierce competitors. Naomi Osaka shattered that outdated playbook into a million pieces.

You can love haute couture, celebrate delicate beauty, and simultaneously dominate the most grueling physical contests in the world.

Power isn't defined by rigid conformity; it is defined by the courage to show up as your complete, multifaceted self.

Break the mold. Redefine the standard.

Learn about women's leadership & youth empowerment: lornettedaye.com/programs

#WhoSaidPowerHasOneLook #NaomiOsaka #FashionAndSport #RedefiningPower #HauteCouture #WTAFashion #LornetteDaye #WomenEmpowerment #BreakTheMold #ShatterStereotypes #FemininePower #TennisChic #CourtsideStyle #FierceAndFeminine #ModernChampion #InnovativeAthletics #StyleIcon #BoldLeadership #Trailblazers #FinishStrong`,
  },

  // 5. Beautiful Doesn't Mean Fragile
  {
    imageIndex: 5,
    headline: "BEAUTIFUL DOESN'T MEAN FRAGILE.",
    text: `Grace can move. Power can float. Both can strike with lethal precision.

In track & field and world-class tennis alike, novice observers often mistake fluid elegance for a lack of toughness. But true biomechanical efficiency looks effortless precisely because immense power is channeled without wasted energy.

Do not mistake kindness for weakness.
Do not mistake elegance for fragility.

A silk dress can carry steel underneath.

Discover athlete wellness and sustainable performance coaching: lornettedaye.com/mentorship

#BeautifulNotFragile #GraceAndGrit #FluidPower #NaomiOsaka #LornetteDaye #EliteBiomechanics #AthleticMastery #PowerInGrace #StrengthWithin #TennisWisdom #MentalEndurance #ResilienceInMotion #FinishStrong #IronWill #ElegantExecution #WomenInSport #HighPerformanceMindset #SportsPsychology #AthleteMentorship #TrueStrength`,
  },

  // 6. Centre Court / The Ultimate Runway
  {
    imageIndex: 6,
    headline: "SOME WALK THE RUNWAY. SHE WALKS TO CENTRE COURT.",
    text: `Paris and Milan have fashion runways. But Arthur Ashe Stadium has 24,000 spectators and millions watching across every continent.

When Naomi Osaka steps into the spotlight, the world stops. She uses global sport not just as a venue for competition, but as a dynamic cultural canvas for self-expression, social commentary, and artistic innovation.

Your career is your stage. Every single day you decide what statement you are making to the world.

Make it bold. Make it memorable. Make it authentic.

Explore personal branding & keynote topics with Lornette: lornettedaye.com/media

#CentreCourt #GlobalRunway #CulturalIcon #NaomiOsaka #LornetteDaye #PersonalBrand #BoldStatements #GrandSlamFashion #ArthurAshe #CourtsideCulture #GameChanger #TennisArt #IconicMoments #ImpactBeyondSport #TrailblazingWomen #MediaPresence #HighImpactLeadership #ModernAthlete #FinishStrong #CreativeVision`,
  },

  // 7. Origami & Precision / Design as Athletic Language
  {
    imageIndex: 7,
    headline: "FOLD. FORM. MOVE. DESIGN CAN BE AN ATHLETIC LANGUAGE.",
    text: `Watch the precision of an origami fold. Crisp lines. Intentional geometry. Perfect balance.

Now watch Naomi Osaka's service motion: the kinetic coil of the legs, the extension through the torso, the explosive pronation at contact.

Sport is art in motion. When an athlete aligns technical precision with artistic passion, sport transcends winning and losing—it becomes mastery.

What is the craft you are perfecting every day?

Read Lornette Daye's bestselling book on mastery and endurance 'Finish Strong': lornettedaye.com/book

#DesignInMotion #AthleticArtistry #KineticPrecision #NaomiOsaka #OrigamiArt #Biomechanics #MasteryInSport #LornetteDaye #FinishStrongBook #TennisTechnique #Craftsmanship #PursuitOfExcellence #AestheticPower #KineticEnergy #AthleticGenius #WTAElite #FlushingMeadows #SportsScience #TechnicalMastery #GrandSlamArt`,
  },

  // 8. Heritage in Motion / Never Static
  {
    imageIndex: 8,
    headline: "WHERE YOU COME FROM CAN MOVE WITH YOU.",
    text: `Heritage is not a static museum piece behind glass; it is a living, breathing compass that moves with you across oceans and generations.

Naomi honors ancient traditions while rewriting modern history. She respects the legacy of the legends who paved the way while refusing to be constrained by their past limitations.

Honoring your roots doesn't mean standing still—it means using your heritage as a launchpad to go where no one has gone before.

Where is your foundation taking you next?

Explore Lornette's leadership and legacy frameworks: lornettedaye.com/impact

#HeritageInMotion #RootsAndWings #LegacyBuilding #NaomiOsaka #LornetteDaye #GenerationalImpact #AncestralStrength #CulturalPride #ForwardMotion #USOpenChampionship #ModernLegacy #GlobalInspiration #BreakthroughMoments #SportsAndCulture #InspireGenerations #EnduringExcellence #FearlessJourney #PioneerMindset #FinishStrong #CourageToLead`,
  },

  // 9. Honour the Past, Don't Live in It
  {
    imageIndex: 9,
    headline: "HONOUR THE PAST. DON'T LIVE IN IT.",
    text: `Tradition provides wisdom, but evolution creates champions.

The greatest athletes and industry disruptors never ask for permission to innovate. They study the fundamentals, respect the heritage, and then fearlessly build the future.

If tennis had stayed frozen in its past, we would never have witnessed the cultural revolution, technical evolution, and boundary-pushing fashion that Naomi Osaka brings to modern sports.

Respect your history. But build your tomorrow.

Connect with Lornette Daye for organizational transformation: lornettedaye.com/programs

#HonourThePast #BuildTheFuture #TraditionAndEvolution #NaomiOsaka #LornetteDaye #InnovationInSports #CultureShifter #ModernLeadership #PioneeringSpirit #TennisEvolution #DisruptTheGame #GameChangers #FutureOfSport #UnstoppableVision #BoldLeadership #LeadershipTransformation #FinishStrong #HighImpactExcellence #WTACommunity #Trailblazers`,
  },

  // 10. The Whole Person / Refusing the Box
  {
    imageIndex: 10,
    headline: "ATHLETE. MOTHER. JAPANESE. HAITIAN. CREATOR. CHAMPION. WHY SHOULD SHE CHOOSE?",
    text: `Society loves to place high-achieving women in narrow boxes:
'Just focus on tennis.'
'Just stick to fashion.'
'Just be a mother.'

Naomi Osaka's answer? I will be all of it.

You do not have to diminish any dimension of your identity to succeed at the highest level. You can be a devoted mother, a visionary creator, a champion of cultural heritage, and a world-class competitor simultaneously.

The world doesn't need a watered-down version of you. It needs all of you.

Show up fully. Compete fearlessly. Finish Strong.

Discover Lornette Daye's full coaching & keynote offerings: https://lornettedaye.com

#WhyChoose #MultifacetedWomen #AthleteMotherCreator #WholePersonExcellence #NaomiOsaka #LornetteDaye #UnapologeticallyYou #WorkingMothersInSport #WomenInLeadership #ChampionMindset #LimitlessPotential #MotherhoodAndCareer #IdentityAndPurpose #FullExpression #USOpen2026 #GlobalImpact #FinishStrong #LornetteDayeKeynotes #EmpowermentJourney #BreakAllBoxes`,
  },
];

async function main() {
  console.log('======================================================');
  console.log('Naomi Osaka Fashion & Power Campaign: 30 Posts / 10 Days');
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
  let postCount = 0;
  const daysCount = 10;

  for (let day = 1; day <= daysCount; day++) {
    timeSlots.forEach((slot, slotIdx) => {
      const captionObj = osakaCaptions[postCount % osakaCaptions.length];
      const imgFile = `osaka-${String(captionObj.imageIndex).padStart(2, '0')}.png`;
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
        campaign: 'naomi-osaka-fashion-power',
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
  console.log(`🎉 Successfully saved 30 Naomi Osaka Fashion posts! Total posts in master manifest: ${manifest.length}`);
}

export const osakaPosts = osakaCaptions;

if (process.argv[1]?.includes('schedule-osaka-campaign.mjs') || process.argv[1]?.endsWith('schedule-osaka-campaign')) {
  main().catch(console.error);
}
