/**
 * Master Publishing Engine & Multi-Tier Campaign Generator (Anti-Duplicate Edition)
 * Every post generated with unique copy, bespoke hashtags, and staggered non-colliding time slots.
 */

import fs from 'fs';
import path from 'path';

const BASE_URL = 'https://lornettedaye.com/campaigns';

const uniqueStoryAngles = [
  "In 40+ years of high-performance coaching, I have watched athletes freeze because they relied on their title instead of their daily preparation.",
  "When you step onto Arthur Ashe Stadium, past accolades evaporate. You still have to win the point in front of you.",
  "Great leaders and elite athletes master the ability to flip the internal switch from quiet introspection to ruthless execution.",
  "True confidence isn't derived from external rankings or applause; it is forged when the results aren't going your way.",
  "Pressure is not a burden to be avoided; it is proof that what you are doing matters to the world.",
  "The biggest lesson I have learned on the international stage is that technique is only 50%—mental self-regulation is the other 50%.",
  "Momentum in high-stakes competition is not an accident; it is the sudden alignment of quiet preparation with a single opening.",
  "Talent should never have to choose between surviving and competing. Great institutions invest before the podium.",
  "Authenticity is the ultimate competitive advantage. Never shrink your magnitude to fit into someone else's comfort zone.",
  "Whatever arena you find yourself competing in today: don't hesitate, commit fully, and Finish Strong."
];

export function getCaptionsForFolder(folder, index, dayNumber) {
  const pad = String(index).padStart(2, '0');
  const imgUrl = `${BASE_URL}/${folder}/${folder}-${pad}.png`;
  const angle = uniqueStoryAngles[(index + dayNumber) % uniqueStoryAngles.length];

  switch (folder) {
    case 'lewishamilton':
      return {
        headline: `MONZA SPOTLIGHT [Day ${dayNumber}]: LEWIS HAMILTON IN SCARLET RED 🇮🇹🏎️`,
        text: `At 350 km/h through the Curva Grande, there is zero margin for hesitation.

${angle}

When Lewis Hamilton pilots the Ferrari through Monza, the passion of the Tifosi reaches fever pitch. True athletic mastery requires biomechanical precision and total emotional regulation under extreme national expectation.

Can Lewis deliver the dream podium at Monza? Drop your predictions below! 🏎️👇

🔗 High-Performance Frameworks: https://lornettedaye.com/athlete-coaching

#ItalianGP #Monza #LewisHamilton #ScuderiaFerrari #Tifosi #Formula1 #LornetteDaye #SpeedAndPrecision #ChampionMindset #HighPerformance #FinishStrong #AutodromoMonza #FerrariLife #Motorsport`,
        imgUrl
      };

    case 'como':
      return {
        headline: `SERIE A LEADERSHIP [Day ${dayNumber}]: THE COMO 1907 BLUEPRINT 🇮🇹⚽`,
        text: `From the shores of Lake Como to the pinnacle of Serie A football:

${angle}

Como 1907 is demonstrating what visionary sports governance looks like—building long-term infrastructure, respecting community heritage, and developing human potential before chasing instant trophies.

How high can this ambitious Italian project climb this season? Share your thoughts below! ⚽👇

🔗 Leadership & Organizational Programs: https://lornettedaye.com/leadership

#Como1907 #SerieA #ItalianFootball #Calcio #SustainableSport #SportsGovernance #LornetteDaye #LakeComo #ClubCulture #BuildingTheFuture #DevelopingTheAthlete #FinishStrong`,
        imgUrl
      };

    case 'carlos':
      return {
        headline: `US OPEN CONTENDER [Day ${dayNumber}]: CARLOS ALCARAZ'S FEARLESS ATTACK ⚡🇪🇸`,
        text: `Sliding defense, drop-shot disguise, and 100-mph forehands on the run.

${angle}

Carlos Alcaraz plays with an untamed joy that disarms opponents and electrifies Arthur Ashe Stadium. He does not wait for mistakes—he imposes his will from the first ball.

Are you backing Alcaraz to lift the trophy in New York? Let's hear your take! 🏆👇

🔗 Mindset Coaching with Lornette Daye: https://lornettedaye.com/athlete-coaching

#CarlosAlcaraz #USOpen #ATPWorldTour #FearlessExecution #TennisMastery #LornetteDaye #MentalToughness #GrandSlamTennis #ArthurAshe #PlayToWin #FinishStrong #TennisTalk`,
        imgUrl
      };

    case 'coco':
    case 'coco2':
      return {
        headline: `US OPEN HOME CROWD [Day ${dayNumber}]: COCO GAUFF'S CLUTCH POISE 🇺🇸👑`,
        text: `Defending a Grand Slam championship in front of 24,000 screaming New Yorkers is the ultimate test of athletic maturity.

${angle}

Coco Gauff embraces the pressure, feeds off the electric home energy, and delivers when everything is on the line.

Can Coco go back-to-back in Queens? Cast your vote in the comments! 🏆🇺🇸👇

🔗 Keynotes & Mentorship: https://lornettedaye.com/speaking

#CocoGauff #USOpenChampion #ArthurAsheStadium #TeamUSA #WTATennis #ChampionPoise #LornetteDaye #BlackExcellence #WomenInSport #TennisCommunity #GrandSlam2026 #FinishStrong`,
        imgUrl
      };

    case 'leylah':
      return {
        headline: `CANADIAN PRIDE [Day ${dayNumber}]: LEYLAH FERNANDEZ BACK IN NEW YORK 🇨🇦🎾`,
        text: `As a Canadian National Champion, I know the pride and grit that Leylah Fernandez carries every time she steps onto the hard courts.

${angle}

From Montreal grassroots to a Grand Slam final, Leylah's immigrant family work ethic and relentless fighting spirit prove that dedication conquers giants.

Let's rally behind Leylah in New York! Drop your Canadian flags below! 🇨🇦👇

🔗 Discover Canadian High-Performance Mentorship: https://lornettedaye.com/mentorship

#LeylahFernandez #TeamCanada #TennisCanada #CanadianPride #USOpen #LornetteDaye #ResilienceInSport #GrassrootsToGold #FinishStrong #MontrealSports #WTA`,
        imgUrl
      };

    case 'osaka':
    case 'osaka_court':
      return {
        headline: `ICONIC SPOTLIGHT [Day ${dayNumber}]: NAOMI OSAKA — GRACE, POWER & IDENTITY 👑🇯🇵`,
        text: `Athlete. Mother. Creator. Champion.

${angle}

Naomi Osaka refuses to be placed in a narrow box. She seamlessly fuses haute couture elegance with explosive 120-mph power on the world's most demanding sports canvas.

Never apologize for your magnitude. Take up space and own your court.

🔗 Explore Whole-Person Leadership: https://lornettedaye.com/about

#NaomiOsaka #USOpen #HauteCouture #PowerAndGrace #WTA #LornetteDaye #MulticulturalExcellence #AuthenticLeadership #ArthurAshe #WomenWhoLead #FinishStrong #ChampionMindset`,
        imgUrl
      };

    case 'ellis':
      return {
        headline: `NEXT-GEN POWER [Day ${dayNumber}]: ARTHUR FILS BREAKS THROUGH 🇫🇷🎾`,
        text: `Explosive first-step quickness and raw baseline power.

${angle}

Arthur Fils embodies the modern evolution of elite athletic tennis. He plays with the conviction that no opponent is invincible.

Watch out for Fils on the Arthur Ashe night session! Are you backing the young star? 🇫🇷👇

🔗 Book Lornette Daye for Keynotes: https://lornettedaye.com/speaking

#ArthurFils #NextGenATP #FrenchTennis #USOpen #PowerTennis #LornetteDaye #AthleticExcellence #DreamBig #FinishStrong #TennisFuture #GrandSlamDrama`,
        imgUrl
      };

    case 'turkey':
      return {
        headline: `SPORTS GOVERNANCE [Day ${dayNumber}]: TÜRKIYE'S ATHLETE INVESTMENT REVOLUTION 🇹🇷👏`,
        text: `Direct monthly stipends. Universal travel, lodging, and nutrition. Equal funding across Olympic, Paralympic, and Deaflympic disciplines.

${angle}

Türkiye's athlete-first investment model is a global blueprint for how modern nations should nurture human talent.

Great nations invest before the medal.

🔗 Read Lornette Daye's Sports Policy Insights: https://lornettedaye.com/impact

#TurkiyeSports #AthleteWelfare #HolisticAthlete #OlympicDevelopment #ParalympicEquity #Deaflympics #SportsPolicy #LornetteDaye #AthleteFirst #DevelopingTheAthlete #FinishStrong`,
        imgUrl
      };

    case 'vargas':
      return {
        headline: `CHAMPION RESOLVE [Day ${dayNumber}]: MELISSA VARGAS — 112 KM/H POWER 🏐🇹🇷`,
        text: `From overcoming exile at 18 to European Champion and 33-point VNL Finals record-holder:

${angle}

Melissa Vargas is living proof that a setback is never your finish line. When you play with joyful ferocity and purpose, you become unstoppable.

Demand the ball. Finish Strong.

🔗 Order Lornette Daye's 'Finish Strong': https://lornettedaye.com/books

#MelissaVargas #VargasPower #ResilienceInSport #TurkiyeVolleyball #FileninSultanlari #LornetteDaye #112KMH #ClutchPerformance #EuroVolleyMVP #FinishStrongBook #TrueGreatness`,
        imgUrl
      };

    default:
      return {
        headline: `HIGH PERFORMANCE [Day ${dayNumber}]: THE PURSUIT OF MASTERY 🗽🎾`,
        text: `Arthur Ashe Stadium crowns true legends under the Friday night lights.

${angle}

Whether you are competing for a Grand Slam or navigating an executive transformation: championship habits remain constant.

Step onto your court with conviction.

🔗 Visit: https://lornettedaye.com

#USOpen #ArthurAshe #GrandSlam #HighPerformance #LornetteDaye #ChampionHabits #MentalToughness #LeadershipExcellence #FinishStrong`,
        imgUrl
      };
  }
}

async function buildMasterManifest() {
  console.log('Generating Master Manifest with anti-duplicate copy and unique staggered times...');

  const masterManifest = [];
  let idCounter = 1;

  // 10 Staggered times with varied minutes
  const timeSlots = [
    { label: '8:14 AM MDT', utcHour: 14, utcMin: 14 },
    { label: '9:42 AM MDT', utcHour: 15, utcMin: 42 },
    { label: '11:18 AM MDT', utcHour: 17, utcMin: 18 },
    { label: '12:37 PM MDT', utcHour: 18, utcMin: 37 },
    { label: '2:11 PM MDT', utcHour: 20, utcMin: 11 },
    { label: '3:48 PM MDT', utcHour: 21, utcMin: 48 },
    { label: '5:22 PM MDT', utcHour: 23, utcMin: 22 },
    { label: '6:49 PM MDT', utcHour: 0, utcMin: 49, nextDay: true },
    { label: '8:16 PM MDT', utcHour: 2, utcMin: 16, nextDay: true },
    { label: '9:31 PM MDT', utcHour: 3, utcMin: 31, nextDay: true },
  ];

  const tennisFolders = ['usopen', 'usopen2', 'carlos', 'coco', 'coco2', 'leylah', 'osaka', 'osaka_court', 'ellis'];
  const turkeyFolders = ['turkey', 'vargas'];
  const italianFolders = ['lewishamilton', 'como'];
  const individualFolders = ['osaka', 'ellis', 'leylah', 'destiny'];

  let tennisIdx = 0;
  let turkeyIdx = 0;
  let indIdx = 0;

  for (let dayOffset = 0; dayOffset < 32; dayOffset++) {
    const calendarDate = new Date(Date.UTC(2026, 7, 30 + dayOffset));
    const dateStr = calendarDate.toISOString().split('T')[0];
    const isMonzaWeekend = (dayOffset >= 4 && dayOffset <= 8);

    for (let slotIdx = 0; slotIdx < timeSlots.length; slotIdx++) {
      const slot = timeSlots[slotIdx];
      let selectedFolder = 'usopen';

      if (isMonzaWeekend && (slotIdx === 2 || slotIdx === 6)) {
        selectedFolder = 'lewishamilton';
      } else if (slotIdx === 0 || slotIdx === 1 || slotIdx === 3 || slotIdx === 4 || slotIdx === 5 || slotIdx === 7 || slotIdx === 8) {
        selectedFolder = tennisFolders[tennisIdx % tennisFolders.length];
        tennisIdx++;
      } else if (slotIdx === 2) {
        selectedFolder = (dayOffset % 2 === 0) ? 'como' : turkeyFolders[turkeyIdx % turkeyFolders.length];
        if (dayOffset % 2 !== 0) turkeyIdx++;
      } else if (slotIdx === 6) {
        selectedFolder = turkeyFolders[turkeyIdx % turkeyFolders.length];
        turkeyIdx++;
      } else {
        selectedFolder = individualFolders[indIdx % individualFolders.length];
        indIdx++;
      }

      const maxFiles = (selectedFolder === 'osaka_court' || selectedFolder === 'turkey' || selectedFolder === 'vargas') ? 20 : 10;
      const assetNum = (idCounter % maxFiles) + 1;
      const caption = getCaptionsForFolder(selectedFolder, assetNum, dayOffset + 1);

      let dueYear = 2026;
      let dueMonth = 7;
      let dueDay = 30 + dayOffset;
      let dueHour = slot.utcHour;
      let dueMinute = slot.utcMin;

      if (slot.nextDay) {
        dueDay += 1;
      }

      const dueAtDate = new Date(Date.UTC(dueYear, dueMonth, dueDay, dueHour, dueMinute, 0, 0));

      masterManifest.push({
        id: idCounter,
        dayNumber: dayOffset + 1,
        date: dateStr,
        timeSlot: slot.label,
        dueAt: dueAtDate.toISOString(),
        campaign: selectedFolder,
        headline: caption.headline,
        text: caption.text,
        imageFile: `${selectedFolder}-${String(assetNum).padStart(2, '0')}.png`,
        imageUrl: caption.imgUrl,
        status: 'staged',
        bufferPostId: null,
      });

      idCounter++;
    }
  }

  const manifestPath = path.join(process.cwd(), 'scripts', 'campaign-manifest.json');
  const queuePath = path.join(process.cwd(), 'scripts', 'master-campaign-queue.json');

  fs.writeFileSync(manifestPath, JSON.stringify(masterManifest, null, 2));
  fs.writeFileSync(queuePath, JSON.stringify(masterManifest, null, 2));

  console.log(`✅ Anti-Duplicate Master Campaign Generated: ${masterManifest.length} unique posts staged.`);
}

buildMasterManifest().catch(console.error);
