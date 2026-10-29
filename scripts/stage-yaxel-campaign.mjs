import fs from 'node:fs';
import path from 'node:path';

const SRC_DIR = 'C:\\Users\\Zhane\\Documents\\Website stuff\\lornetteig\\Career Circle Posts\\november\\yaxel';
const DEST_DIR = path.resolve('public/campaigns/yaxel');

if (!fs.existsSync(DEST_DIR)) {
  fs.mkdirSync(DEST_DIR, { recursive: true });
}

// 10 Unique Master Editorial Plates for Yaxel Lendeborg Campaign
const YAXEL_PLATES = [
  {
    index: 1,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_55_57 PM-1.png",
    destSlug: "01-more-than-the-game",
    scheduledDate: "2026-11-03",
    scheduledAt: "2026-11-04T00:30:00.000Z", // 7:30 PM EST / 00:30 UTC next day
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "IDENTITY BEYOND SPORT & ATHLETIC PURPOSE",
    headline: "More Than the Game: The World Sees the Basketball Player. Behind Every Jersey Is a Son, a Family, and a Story.",
    body: `When an athlete steps onto an NBA hardwood under bright arena lights, the world sees statistics, physical presence, and game execution.

Fans cheer the rebounds, the defensive stops, and the tenacity in the paint. But every elite performer carries an entire world inside their chest. Behind the uniform is a young man with real responsibilities, a devoted family, and an uphill climb that started long before anyone knew his name.

Olympic-level mentor Lornette Daye has coached national champions and Olympians for over forty years. Her foundational rule for long-term greatness begins with Foundation One: Identity Beyond Sport. When an athlete knows who they are off the court, their game becomes grounded in unwavering clarity rather than external validation.

Yaxel Lendeborg embodies this standard. Competing with fierce intensity while keeping his heart anchored to the people who raised him is what true leadership looks like.

Play with purpose. Live in the moment. Celebrate the journey.`,
    hashtags: "#YaxelLendeborg #Warriors #IdentityBeyondSport #MoreThanAnAthlete #FamilyFirst #LornettesFoundations #CareerCircle #BetterPeopleBetterPlayers"
  },
  {
    index: 2,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_55_58 PM-2.png",
    destSlug: "02-yaxel-what-a-journey",
    scheduledDate: "2026-11-09",
    scheduledAt: "2026-11-10T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "THE POWER OF GRIT & PERSEVERANCE",
    headline: "Yaxel, What a Journey: From Michigan and Junior College to the Golden State Warriors.",
    body: `The path to professional basketball is rarely a straight line. For Yaxel Lendeborg, it was built day by day, gym by gym, through relentless dedication and unshakeable humility.

From his early roots in Michigan, through the demanding junior college trenches, to dominating the collegiate boards, and now putting on jersey number thirty-two for Golden State, every step was earned. Nothing was handed to him.

Lornette Daye teaches Foundation Three: Discipline Systems. Talent opens doors, but daily discipline and silent sacrifice keep you inside the room. Reaching this stage is proof of what happens when preparation meets quiet conviction.

Take time to honor how far you have come. Your hard work deserves to be celebrated, and this new chapter is only the beginning of your legacy.

Enjoy every moment of this hard-earned milestone.`,
    hashtags: "#YaxelLendeborg #GoldenStateWarriors #NBAJourney #JuniorCollegeToNBA #DisciplineSystems #LornettesFoundations #CareerCircle"
  },
  {
    index: 3,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_55_59 PM-3.png",
    destSlug: "03-some-battles-are-personal",
    scheduledDate: "2026-11-15",
    scheduledAt: "2026-11-16T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "UNSEEN COURAGE & FAMILY DEVOTION",
    headline: "Some Battles Are Personal: Showing Up to Compete While Carrying the Weight of Those You Love.",
    body: `The hardest battles an athlete fights never appear on the box score.

Showing up to compete at the highest level of professional sport while carrying personal worries for a family member facing health challenges demands an extraordinary level of emotional courage. It requires compartmentalizing pressure while holding deep compassion in your heart.

In Lornette's Foundations, Foundation Seven centers on Family and Community Support. The strength of an athlete does not come from cold isolation. It comes from the love, gratitude, and purpose rooted in family bonds.

Yaxel, your poise in navigating both professional demands and personal family devotion commands profound respect. When you play for something bigger than yourself, you tap into a reserve of strength that pressure cannot shake.

True strength is playing with heart while honoring the people who matter most.`,
    hashtags: "#UnseenCourage #FamilyDevotion #EmotionalRegulation #LornettesFoundations #AthleteSupport #CareerCircle #BetterPeopleBetterPlayers"
  },
  {
    index: 4,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_00 PM-4.png",
    destSlug: "04-a-mothers-love",
    scheduledDate: "2026-11-21",
    scheduledAt: "2026-11-22T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "FOUNDATION OF UNCONDITIONAL SUPPORT",
    headline: "A Mother's Love: Long Before the Arena Lights, There Was Someone Who Believed in You First.",
    body: `Long before the NBA Draft, the packed arenas, and the national broadcasts, there was a mother who saw the greatness in her son before the world ever noticed.

She was there through the late-night practices, the quiet doubts, the sacrifices, and the endless miles traveled to keep a dream alive. That unconditional love is the unseen engine behind every great athletic achievement.

Lornette Daye often reflects with elite athletes on the sacred value of family anchors. When sports try to reduce you to your latest performance, a mother's voice reminds you of your true worth. Everything Yaxel pours onto the court is an echo of the love and guidance poured into him.

To every athlete playing with a loved one in their heart: let that love be your peace, your fuel, and your anchor.

That love is an unbreakable part of your story.`,
    hashtags: "#MothersLove #FamilyAnchor #SacrificeAndLove #LornettesFoundations #FamilySupport #CareerCircle #BetterPeopleBetterPlayers"
  },
  {
    index: 5,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_02 PM-5.png",
    destSlug: "05-stay-focused-on-your-dream",
    scheduledDate: "2026-11-27",
    scheduledAt: "2026-11-28T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "EXECUTION & EMOTIONAL EQUANIMITY",
    headline: "Stay Focused on Your Dream: Dedication, Preparation, and Belief When Life Becomes Complex.",
    body: `When life outside the court becomes complicated and heavy, keeping your professional focus sharp is one of the greatest tests of character.

It is easy to stay locked in when everything is smooth. But true champions develop the ability to honor their emotions without losing control of their daily execution. Preparation, dedication, and self-belief remain your compass through stormy seasons.

Lornette Daye coaches athletes through Foundation Two: Champion Mindset. Focus is not about ignoring life's realities. Focus is about bringing your total presence to the task right in front of you, one possession, one drill, and one moment at a time.

Take each opportunity as it comes. Protect your peace, trust your preparation, and know that you were built to handle this moment.

One step at a time. One breath at a time.`,
    hashtags: "#StayFocused #ChampionMindset #EmotionalPoise #MentalToughness #LornettesFoundations #CareerCircle"
  },
  {
    index: 6,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_02 PM-6.png",
    destSlug: "06-you-are-human-first",
    scheduledDate: "2026-12-03",
    scheduledAt: "2026-12-04T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "WHOLE ATHLETE WELLBEING",
    headline: "You Are Human First: Being Strong Does Not Mean You Cannot Feel Emotion.",
    body: `Sports culture often tells young men and elite athletes that vulnerability is weakness. We praise them for playing through physical pain and expect them to remain emotionless robots off the court.

The reality is far more profound: an athlete can be fierce, physically dominant, and completely locked into the game, while still feeling worried, emotional, or overwhelmed about family circumstances.

Lornette Daye has championed the Whole Athlete framework for decades. Acknowledging your feelings does not diminish your competitive edge. It actually protects your mental longevity and deepens your resilience.

Being human first is what gives your athletic journey genuine meaning. Give yourself permission to feel, to lean on your support network, and to breathe.

You do not have to carry everything alone.`,
    hashtags: "#HumanFirst #WholeAthlete #MentalHealthInSports #VulnerabilityIsStrength #LornettesFoundations #CareerCircle"
  },
  {
    index: 7,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_04 PM-7.png",
    destSlug: "07-enjoy-this-moment",
    scheduledDate: "2026-12-09",
    scheduledAt: "2026-12-10T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "GRATITUDE & PRESENT MOMENT AWARENESS",
    headline: "Enjoy This Moment: You Have Worked Too Hard to Reach This Stage Not to Appreciate It.",
    body: `When you are constantly grinding for the next contract, the next defensive stop, and the next win, it is easy to forget to look up and realize where you are standing.

You have sacrificed years of sleep, pushed through grueling conditioning sessions, and weathered setbacks that would have caused others to quit. Reaching the pinnacle of professional sport is a rare privilege that only a tiny fraction of athletes ever achieve.

Lornette Daye reminds every competitor she coaches: do not let the urgency of tomorrow steal the beauty of today. Celebrate the small victories. Savor the feeling of running out of the tunnel. Appreciate the camaraderie in the locker room.

You have earned your seat at this table. Let yourself feel the joy of the game you fell in love with as a boy.

Live in this moment fully.`,
    hashtags: "#EnjoyTheMoment #GratitudeInSports #Presence #AthleticAchievement #LornettesFoundations #CareerCircle"
  },
  {
    index: 8,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_05 PM-8.png",
    destSlug: "08-let-your-love-of-the-game-show",
    scheduledDate: "2026-12-15",
    scheduledAt: "2026-12-16T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "PASSION, HEART & INTENSITY",
    headline: "Let Your Love of the Game Show: Play With Heart, Trust Your Work, and Remember Why You Started.",
    body: `Under the weight of professional expectations, media scrutiny, and contract pressures, sport can easily feel like a heavy job.

The secret to playing your best when the stakes are highest is returning to your original joy. Remember the cracked asphalt courts, the sound of the ball bouncing in an empty schoolyard, and the pure excitement of dreaming about this life.

Lornette Daye coaches Foundation Two and Foundation Five: when you connect to your original passion, fear disappears. Trust the thousands of hours you spent putting up shots when no cameras were around. Play with an open heart and let your natural joy illuminate the floor.

When you play with authentic love for the game, everyone watching can feel it.

Trust your preparation. Play free.`,
    hashtags: "#LoveOfTheGame #PurePassion #PlayFree #TrustTheProcess #LornettesFoundations #CareerCircle #BetterPeopleBetterPlayers"
  },
  {
    index: 9,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_06 PM-9.png",
    destSlug: "09-every-athlete-has-a-story",
    scheduledDate: "2026-12-21",
    scheduledAt: "2026-12-22T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "MULTIDIMENSIONAL EXCELLENCE",
    headline: "Every Athlete Has a Story: Beyond Every Statistic Is a Legacy in the Making.",
    body: `Modern sports analytics can measure an athlete's jump height, lateral quickness, and shooting efficiency down to decimal points.

What analytics can never quantify is heart, loyalty to family, and the quiet dignity of a young leader determined to uplift his community. Beyond the box scores is a person building a life, creating generational security, and establishing an enduring legacy.

Lornette Daye founded Lornette's Foundations to equip athletes for the entirety of their journey: Foundation Nine (Personal Brand and Story) and Foundation Ten (Legacy and Community Impact). Your sport is your platform, but your character is your true legacy.

Yaxel Lendeborg's journey is inspiring thousands of young athletes who started with long odds and big dreams. Keep writing your story with poise and integrity.

Your story is touching lives far beyond the hardwood.`,
    hashtags: "#EveryAthleteHasAStory #AthleteLegacy #CommunityImpact #WholeAthlete #LornettesFoundations #CareerCircle"
  },
  {
    index: 10,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_56_07 PM-10.png",
    destSlug: "10-a-personal-message-from-lornette-daye",
    scheduledDate: "2026-12-27",
    scheduledAt: "2026-12-28T00:30:00.000Z",
    slotType: "Evening Family Reflection (7:30 PM EST)",
    eyebrow: "A PERSONAL MESSAGE FROM LORNETTE DAYE",
    headline: "To Yaxel Lendeborg: Admiration for Your Play, Your Strength for Your Mother, and Your Family Heart.",
    body: `A personal note from Olympic-level coach Lornette Daye:

Yaxel,

I admire how exceptionally well you are playing while your family is navigating a deeply difficult season. As a former elite athlete and coach of over forty years, I understand that the battles outside sport can be far more demanding than anything you face between the lines.

Your ability to compete with excellence, maintain your humility, and stand as a rock for your mother reflects the highest standard of character. When you play with love as your primary motive, you inspire everyone who crosses your path.

Keep believing in your abilities. Stay focused on what you can control. Above all, take time to enjoy the moments you have worked so hard to create.

Wishing you, your mother, and your entire family strength, peace, and many beautiful moments together.

Sincerely,
Lornette Daye
Olympic-Level Coach and Canadian National Sprint Champion`,
    hashtags: "#LornetteDaye #YaxelLendeborg #GoldenStateWarriors #FamilyStrength #BetterPeopleBetterPlayers #LornettesFoundations #CareerCircle"
  }
];

const ECOSYSTEM_FOOTER = `ATHLETE FOUNDATIONS & FAMILY SYSTEMS:
Explore Lornette's Foundations: https://lornettedaye.com/foundations

VENTURE & ENTERPRISE:
Build business and NIL infrastructure: https://umattr.ca/business

DIGITAL IDENTITY:
Architect your executive web presence: https://umattr.ca/website

CAREER MOBILITY:
Step into post-athletic career pathways: https://careercircle.app`;

console.log(`Staging ${YAXEL_PLATES.length} master editorial plates for Yaxel Lendeborg campaign...`);

const masterQueue = [];

for (const p of YAXEL_PLATES) {
  const src = path.join(SRC_DIR, p.sourceFile);
  if (!fs.existsSync(src)) {
    throw new Error(`Source file missing: ${src}`);
  }

  const destFile = `${p.destSlug}.png`;
  const dest = path.join(DEST_DIR, destFile);

  fs.copyFileSync(src, dest);
  console.log(`Copied: ${destFile}`);

  const fullCaption = `${p.eyebrow}

${p.headline}

${p.body}

${ECOSYSTEM_FOOTER}

${p.hashtags}`;

  // Pre-flight assertion guards
  if (fullCaption.includes('*')) {
    throw new Error(`Post #${p.index} contains asterisks!`);
  }
  if (fullCaption.includes('—')) {
    throw new Error(`Post #${p.index} contains em dashes!`);
  }
  if (!fullCaption.includes('https://lornettedaye.com/foundations') ||
      !fullCaption.includes('https://umattr.ca/business') ||
      !fullCaption.includes('https://umattr.ca/website') ||
      !fullCaption.includes('https://careercircle.app')) {
    throw new Error(`Post #${p.index} is missing an ecosystem URL!`);
  }
  if (fullCaption.includes('Coach Lornette')) {
    throw new Error(`Post #${p.index} contains prohibited 'Coach Lornette'!`);
  }

  masterQueue.push({
    postIndex: p.index,
    scheduledAt: p.scheduledAt,
    scheduledDate: p.scheduledDate,
    slotType: p.slotType,
    imageFilename: destFile,
    localPath: `/campaigns/yaxel/${destFile}`,
    cdnUrl: `https://lornettedaye.com/campaigns/yaxel/${destFile}`,
    eyebrow: p.eyebrow,
    headline: p.headline,
    caption: fullCaption,
    hashtags: p.hashtags
  });
}

// Write master queue JSON
const QUEUE_PATH = path.resolve('scripts/master-yaxel-queue.json');
fs.writeFileSync(QUEUE_PATH, JSON.stringify(masterQueue, null, 2), 'utf-8');
console.log(`Saved master queue with ${masterQueue.length} posts to ${QUEUE_PATH}`);

// Generate HTML Review Gallery
const htmlGallery = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Campaign Review: Yaxel Lendeborg (10 Milestone Posts)</title>
  <style>
    :root {
      --bg: #0d0c0a;
      --card-bg: #171513;
      --border: rgba(198, 165, 92, 0.3);
      --gold: #c6a55c;
      --text: #e6e4df;
      --muted: #a39e93;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      padding: 40px 20px;
    }
    header {
      max-width: 1200px;
      margin: 0 auto 40px auto;
      text-align: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 30px;
    }
    h1 {
      font-size: 2.2rem;
      color: #fff;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 8px;
    }
    .badge {
      display: inline-block;
      background: rgba(198, 165, 92, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold);
      padding: 4px 14px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      border-radius: 9999px;
      margin-bottom: 16px;
    }
    .stats {
      display: flex;
      justify-content: center;
      gap: 30px;
      margin-top: 20px;
      flex-wrap: wrap;
    }
    .stat-item {
      background: rgba(255,255,255,0.03);
      padding: 12px 24px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.08);
    }
    .stat-val { font-size: 1.4rem; font-weight: 700; color: var(--gold); }
    .stat-lbl { font-size: 0.75rem; text-transform: uppercase; color: var(--muted); }
    
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 30px;
      max-width: 1300px;
      margin: 0 auto;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .img-wrap {
      width: 100%;
      aspect-ratio: 1/1;
      background: #000;
      position: relative;
      overflow: hidden;
    }
    .img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .card-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .post-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--gold);
      margin-bottom: 12px;
    }
    .post-num {
      background: var(--gold);
      color: #000;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .eyebrow {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--gold);
      font-weight: 700;
      margin-bottom: 6px;
    }
    .headline {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 16px;
      line-height: 1.35;
    }
    .caption-box {
      background: rgba(0,0,0,0.4);
      padding: 16px;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.06);
      font-size: 0.85rem;
      color: var(--muted);
      white-space: pre-wrap;
      max-height: 220px;
      overflow-y: auto;
      font-family: inherit;
      line-height: 1.5;
    }
    .links-badge {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 14px;
    }
    .link-tag {
      font-size: 0.65rem;
      background: rgba(198, 165, 92, 0.1);
      border: 1px solid rgba(198, 165, 92, 0.3);
      color: #e6e4df;
      padding: 3px 8px;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <header>
    <div class="badge">Master Campaign Pre-Flight Review</div>
    <h1>Yaxel Lendeborg: 60-Day Milestone Journey</h1>
    <p style="color: var(--muted); max-width: 700px; margin: 0 auto;">
      10 Unique Master Editorial Plates &bull; Paced Every 6 Days Across November & December 2026 &bull; Evening Family Reflection (7:30 PM EST)<br>
      Warm Mentorship, Unwavering Family Devotion, and Lornette Daye's Foundations
    </p>
    <div class="stats">
      <div class="stat-item"><div class="stat-val">10</div><div class="stat-lbl">Milestone Drops</div></div>
      <div class="stat-item"><div class="stat-val">Nov 3 - Dec 27</div><div class="stat-lbl">60-Day Pacing</div></div>
      <div class="stat-item"><div class="stat-val">4 Links</div><div class="stat-lbl">Foundations &bull; Business &bull; Website &bull; CareerCircle</div></div>
      <div class="stat-item"><div class="stat-val">100%</div><div class="stat-lbl">Zero-Asterisk Compliant</div></div>
    </div>
  </header>

  <main class="grid">
    ${masterQueue.map(item => `
      <div class="card">
        <div class="img-wrap">
          <img src="${item.localPath}" alt="${item.headline}" loading="lazy">
        </div>
        <div class="card-body">
          <div class="post-meta">
            <span class="post-num">Post #${item.postIndex}</span>
            <span>${item.scheduledDate} &bull; ${item.slotType}</span>
          </div>
          <div class="eyebrow">${item.eyebrow}</div>
          <div class="headline">${item.headline}</div>
          <div class="caption-box">${item.caption}</div>
          <div class="links-badge">
            <span class="link-tag">&check; lornettedaye.com/foundations</span>
            <span class="link-tag">&check; umattr.ca/business</span>
            <span class="link-tag">&check; umattr.ca/website</span>
            <span class="link-tag">&check; careercircle.app</span>
          </div>
        </div>
      </div>
    `).join('')}
  </main>
</body>
</html>`;

const HTML_PATH = path.resolve('public/campaigns/yaxel/review.html');
fs.writeFileSync(HTML_PATH, htmlGallery, 'utf-8');
console.log(`Generated HTML gallery at ${HTML_PATH}`);
