import fs from 'node:fs';
import path from 'node:path';

const SRC_DIR = 'C:\\Users\\Zhane\\Documents\\Website stuff\\lornetteig\\Career Circle Posts\\november\\injury';
const DEST_DIR = path.resolve('public/campaigns/nba-injury');

if (!fs.existsSync(DEST_DIR)) {
  fs.mkdirSync(DEST_DIR, { recursive: true });
}

// 8 Unique Master Editorial Plates
const INJURY_PLATES = [
  {
    index: 1,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_02 PM-1.png",
    destSlug: "01-the-season-just-started",
    scheduledDate: "2026-11-02",
    scheduledAt: "2026-11-02T13:30:00.000Z", // 8:30 AM EST
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "NBA INJURY CRISIS & EARLY SEASON REALITY",
    headline: "The Season Just Started. And Already, Too Many Conversations Are About Injuries Instead of Basketball.",
    body: `Opening week in the NBA should be a celebration of pure athletic artistry, tactical innovation, and rising superstars commanding the hardwood.

Instead, within days of tip-off, fans, front offices, and commentators find themselves dissecting MRI results, torn obliques, and loaded injury reports. The conversation has shifted from the joy of the game to the vulnerability of the human body.

When an athlete goes down in November, it is not just a tactical blow to a team's win-loss column. It is an immediate psychological shock to a young player who spent six months conditioning for this exact moment.

Olympic-level coach Lornette Daye has spent over four decades preparing elite performers for the mental reality of sport. Her foundational principle: true athletic greatness requires protecting the athlete first and respecting the game second. When organizations treat recovery with the same reverence they bring to competition, athletes build sustainable, multi-decade careers.

Protect the player. Respect the game.`,
    hashtags: "#NBA #NBAInjuries #AthleteWellbeing #SportsMedicine #LornettesFoundations #CareerCircle #BetterPeopleBetterPlayers"
  },
  {
    index: 2,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_03 PM-2.png",
    destSlug: "02-jalen-williams-road-back",
    scheduledDate: "2026-11-06",
    scheduledAt: "2026-11-06T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "RECOVERY ARCHITECTURE & PATIENCE",
    headline: "Jalen Williams: One Moment Can Change a Season. The Road Back Matters More Than the Race Back.",
    body: `In the modern high-velocity NBA, a single awkward landing or hyperextension can alter an entire franchise trajectory in less than a second.

For emerging stars like Oklahoma City's Jalen Williams, an early-season setback tests emotional maturity far more than physical pain. The natural instinct of every fierce competitor is to rush back, beat the medical timeline, and prove their toughness.

Lornette Daye coaches athletes through Foundation Four: Resilience After Setback. The road back matters infinitely more than the race back. Rushing a rehabilitation protocol to satisfy short-term game-day urgency almost always results in compensatory injuries that compromise long-term career ceilings.

Recovery deserves the exact same focus, discipline, and emotional respect that an athlete brings to game seven of the playoffs.

Patience during rehab is not weakness. It is the highest form of professional discipline.`,
    hashtags: "#JalenWilliams #OKCThunder #RehabMindset #AthleteRecovery #LornettesFoundations #CareerCircle"
  },
  {
    index: 3,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_03 PM-3.png",
    destSlug: "03-kawhi-leonard-longevity",
    scheduledDate: "2026-11-10",
    scheduledAt: "2026-11-10T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "CAREER LONGEVITY & LOAD PRESERVATION",
    headline: "Kawhi Leonard: Longevity Is a Different Kind of Greatness. Protecting Tomorrow Matters.",
    body: `Few athletes in professional basketball history have faced as much public scrutiny over load management and recovery protocols as two-time Finals MVP Kawhi Leonard.

Critics demand eighty-two games of relentless physical output. But Kawhi and his medical team understand a deeper reality: championship banners are raised in June, not November. Protecting an athlete's physical tomorrow matters just as much as competing today.

In Lornette's Foundations, Lornette Daye teaches Foundation Five: Pressure, Emotional Regulation and Recovery. Elite performance is not about exhausting your biological reserves until your joints give out. It is about calculated pacing, biological intelligence, and knowing when to protect your primary asset.

Experience, leadership, and lasting impact outlive any single regular-season box score.

Redefine your standards of greatness from reckless exhaustion to sustainable mastery.`,
    hashtags: "#KawhiLeonard #Clippers #LoadManagement #AthleteLongevity #LornettesFoundations #CareerCircle"
  },
  {
    index: 4,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_04 PM-4.png",
    destSlug: "04-every-name-is-a-person",
    scheduledDate: "2026-11-14",
    scheduledAt: "2026-11-14T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "HUMAN IDENTITY BEHIND THE JERSEY",
    headline: "Every Name on the Injury Report Is a Person: Real People, Real Families, Real Lives Beyond the Game.",
    body: `To the casual sports fan or fantasy league manager, an injury report is a list of names, positions, and projected return dates.

To the athlete sitting in a quiet training room with ice strapped to their knee, that report represents sleepless nights, anxiety about contract security, and the haunting fear that their body might fail them again.

Behind every jersey number is a son, a father, a family, and a human being who has poured twenty years of identity into a sport that can vanish in a heartbeat.

Lornette Daye built Lornette's Foundations around Foundation One: Identity Beyond Sport. When an athlete knows who they are without the sneakers and the cheering crowds, an injury ceases to be an existential catastrophe. It becomes a temporary obstacle to be navigated with poise and clarity.

See the human being first. The athlete second.`,
    hashtags: "#HumanFirst #AthleteMentalHealth #IdentityBeyondSport #WholeAthlete #LornettesFoundations #CareerCircle"
  },
  {
    index: 5,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_05 PM-5.png",
    destSlug: "05-back-to-back-again",
    scheduledDate: "2026-11-18",
    scheduledAt: "2026-11-18T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "PROFESSIONAL SCHEDULING & PHYSIOLOGY",
    headline: "Back-to-Back. Again. Should Recovery Time Have a Greater Place in Professional Scheduling?",
    body: `Flying from Denver to Minneapolis at two in the morning, arriving at the hotel at four, and stepping onto the court fourteen hours later to sprint four miles against elite athletes is not high performance. It is biological survival.

Back-to-back games remain one of the primary drivers of soft-tissue strains, hamstring tears, and cognitive fatigue across professional basketball.

Lornette Daye's background in Olympic sprinting and biomechanics emphasizes the scientific reality of the central nervous system. When the nervous system is chronically depleted, reaction times drop by milliseconds, joints lose neuromuscular protection, and catastrophic non-contact injuries skyrocket.

More recovery does not weaken the game. More recovery creates a faster, cleaner, more explosive product that protects the athletes fans pay to see.

Respect the science of human recovery.`,
    hashtags: "#NBAArchitecture #BackToBack #SportsScience #Biomechanics #LornettesFoundations #CareerCircle"
  },
  {
    index: 6,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_06 PM-6.png",
    destSlug: "06-82-games-one-body",
    scheduledDate: "2026-11-22",
    scheduledAt: "2026-11-22T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "THE 82-GAME TOLL",
    headline: "82 Games. One Body. Is the Modern NBA Regular Season Asking Too Much of Its Athletes?",
    body: `The eighty-two-game regular season schedule was established in 1967. But the game played today bears zero physical resemblance to the game played sixty years ago.

Today's players cover more court area at higher velocities, experience harder decelerations, and execute complex defensive switches that place unprecedented torque on tendons and ligaments.

Yet the calendar remains unchanged.

Lornette Daye advocates for institutional courage in sports governance. The athlete is more important than the broadcast schedule. When leagues prioritize commercial volume over human biological sustainability, the fans end up watching depleted rosters in playoff games.

A schedule must serve the athlete, not the other way around.`,
    hashtags: "#82Games #NBALogistics #AthletePreservation #SportsGovernance #LornettesFoundations #CareerCircle"
  },
  {
    index: 7,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_06 PM-7.png",
    destSlug: "07-athletes-are-not-machines",
    scheduledDate: "2026-11-26",
    scheduledAt: "2026-11-26T13:30:00.000Z", // Thanksgiving morning
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "THE PHILOSOPHY OF RECOVERY",
    headline: "Athletes Are Not Machines: Great Performance Requires Preparation, Recovery, and a Life Beyond the Game.",
    body: `Modern sports culture often glorifies the 'grind' to an unhealthy extreme. Athletes are told to ignore pain, play through structural damage, and treat their bodies like disposable machinery.

Machinery breaks down. Human beings heal, adapt, and grow stronger when given the proper emotional and physical environment.

Lornette Daye has spent forty years demonstrating that recovery is an active discipline of excellence, not a passive absence of work. Nutrition, sleep architecture, mental decompression, and emotional balance are the four pillars that allow an athlete to compete at the world-class level for fifteen years instead of five.

If you treat yourself like a machine, you will rust. If you honor your humanity, your potential has no ceiling.

Recovery is part of excellence. Live it with intention.`,
    hashtags: "#AthletesAreNotMachines #RecoveryPhilosophy #HighPerformanceLiving #LornettesFoundations #CareerCircle"
  },
  {
    index: 8,
    sourceFile: "ChatGPT Image Oct 28, 2026, 11_51_07 PM-8.png",
    destSlug: "08-paolo-banchero-bright-tomorrow",
    scheduledDate: "2026-11-30",
    scheduledAt: "2026-11-30T13:30:00.000Z",
    slotType: "Morning Sports Debate (8:30 AM EST)",
    eyebrow: "FUTURE-PROOFING TALENT",
    headline: "Paolo Banchero: Great Potential Deserves a Long Future. One Injury Should Never Define an Athlete's Journey.",
    body: `When twenty-one-year-old Orlando Magic superstar Paolo Banchero erupted for fifty points and followed it with a torn oblique just days later, the sports world held its collective breath.

Watching a transcendent young talent sidelined at the peak of his early ascension is a reminder of the fragility of professional sport.

The critical lesson for Paolo and every young leader watching is this: your setback is not your finish line. A six-week rehabilitation window is a microscopic blip in what should be a fifteen-year Hall of Fame journey.

Lornette Daye's work with young champions centers on emotional poise through adversity. Use the rehabilitation window to study the game from the sideline, refine your leadership voice, and strengthen your mental resilience.

Talent today. A bright, unshakeable tomorrow.`,
    hashtags: "#PaoloBanchero #OrlandoMagic #NextGenGreatness #ResilienceAfterSetback #LornettesFoundations #CareerCircle"
  }
];

// Standardized 4-link ecosystem footer
const ECOSYSTEM_FOOTER = `ATHLETE FOUNDATIONS & RECOVERY:
Explore Lornette's Foundations: https://lornettedaye.com/foundations

VENTURE & ENTERPRISE:
Build business and NIL infrastructure: https://umattr.ca/business

DIGITAL IDENTITY:
Architect your executive web presence: https://umattr.ca/website

CAREER MOBILITY:
Step into post-athletic career pathways: https://careercircle.app`;

console.log("Staging 8 unique NBA Injury master plates...");
const masterQueue = [];

for (const p of INJURY_PLATES) {
  const src = path.join(SRC_DIR, p.sourceFile);
  const destFile = `${p.destSlug}.png`;
  const dest = path.join(DEST_DIR, destFile);
  
  if (!fs.existsSync(src)) {
    throw new Error(`Missing source file: ${src}`);
  }
  
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
    localPath: `/campaigns/nba-injury/${destFile}`,
    cdnUrl: `https://lornettedaye.com/campaigns/nba-injury/${destFile}`,
    eyebrow: p.eyebrow,
    headline: p.headline,
    caption: fullCaption,
    hashtags: p.hashtags
  });
}

// Write master queue JSON
const QUEUE_PATH = path.resolve('scripts/master-nba-injury-queue.json');
fs.writeFileSync(QUEUE_PATH, JSON.stringify(masterQueue, null, 2), 'utf-8');
console.log(`Saved master queue with 8 posts to ${QUEUE_PATH}`);

// Generate HTML Review Gallery
const htmlGallery = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Campaign Review: NBA Injury & Athlete Recovery (8 Posts)</title>
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
    <h1>NBA Injuries & Athlete Recovery</h1>
    <p style="color: var(--muted); max-width: 700px; margin: 0 auto;">
      8 Unique Master Editorial Plates &bull; Spaced Across November 2026 &bull; Morning Sports Debate Window (8:30 AM EST)<br>
      High-Impact Analysis Featuring Paolo Banchero, Kawhi Leonard, Jalen Williams & Lornette Daye
    </p>
    <div class="stats">
      <div class="stat-item"><div class="stat-val">8</div><div class="stat-lbl">Master Posts</div></div>
      <div class="stat-item"><div class="stat-val">Nov 2 - 30</div><div class="stat-lbl">Pacing Window</div></div>
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

const HTML_PATH = path.resolve('public/campaigns/nba-injury/review.html');
fs.writeFileSync(HTML_PATH, htmlGallery, 'utf-8');
console.log(`Generated HTML gallery at ${HTML_PATH}`);
