import fs from 'node:fs';
import path from 'node:path';

const ROOT_DIR = 'C:\\Users\\Zhane\\Documents\\Website stuff\\lornetteig\\FOUNDATIONS';
const CARTOON_DIR = path.join(ROOT_DIR, 'cartoon');
const CSV_PATH = path.join(CARTOON_DIR, 'linkedin_lornette_umattr_90_day_schedule.csv');

const DEST_DIR = path.resolve('public/campaigns/foundations-umattr');
if (!fs.existsSync(DEST_DIR)) {
  fs.mkdirSync(DEST_DIR, { recursive: true });
}

function normalizeKey(str) {
  return str.toLowerCase().replace(/[^a-z0-9]/g, '');
}

// Map all available source files
const sourceFilesMap = new Map();

function indexDir(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const ent of entries) {
    if (ent.isFile() && ent.name.toLowerCase().endsWith('.png')) {
      const fullPath = path.join(dir, ent.name);
      sourceFilesMap.set(normalizeKey(ent.name), fullPath);
    }
  }
}

indexDir(ROOT_DIR);
indexDir(CARTOON_DIR);

console.log(`Found ${sourceFilesMap.size} unique source images indexed.`);

// Read and parse CSV
const rawCsv = fs.readFileSync(CSV_PATH, 'utf-8');
const lines = rawCsv.split(/\r?\n/).filter(l => l.trim().length > 0);

function parseCsvLine(text) {
  const result = [];
  let cur = '';
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      if (inQuotes && text[i + 1] === '"') {
        cur += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (c === ',' && !inQuotes) {
      result.push(cur);
      cur = '';
    } else {
      cur += c;
    }
  }
  result.push(cur);
  return result;
}

const headerCols = parseCsvLine(lines[0]).map(h => h.replace(/^\uFEFF/, '').trim());
console.log('CSV Headers:', headerCols);

const rows = [];
for (let i = 1; i < lines.length; i++) {
  const cols = parseCsvLine(lines[i]);
  if (cols.length < headerCols.length) continue;
  const row = {};
  for (let j = 0; j < headerCols.length; j++) {
    row[headerCols[j]] = cols[j];
  }
  rows.push(row);
}

console.log(`Parsed ${rows.length} CSV rows.`);

// Copy unique images to public/campaigns/foundations-umattr/
const uniqueImages = new Set(rows.map(r => r.Image_File));
console.log(`Unique images in CSV: ${uniqueImages.size}`);

for (const imgName of uniqueImages) {
  const norm = normalizeKey(imgName);
  const srcPath = sourceFilesMap.get(norm);
  if (!srcPath) {
    throw new Error(`Could not find source image on disk for: ${imgName} (norm: ${norm})`);
  }
  const destPath = path.join(DEST_DIR, imgName);
  if (!fs.existsSync(destPath) || fs.statSync(destPath).size !== fs.statSync(srcPath).size) {
    fs.copyFileSync(srcPath, destPath);
    console.log(`  Copied: ${imgName}`);
  }
}

console.log('All unique images verified and copied into destination directory.');

// Pillar metadata definitions
const PILLARS_CONFIG = {
  'Pillar 1': {
    name: 'Personal Mentorship & Leadership',
    eyebrow: 'PERSONAL MENTORSHIP & LEADERSHIP',
    primaryCtaLabel: 'Work with Lornette to clarify goals, strengthen confidence, and build a practical path forward:',
    primaryUrl: 'https://lornettedaye.com/mentorship'
  },
  'Pillar 2': {
    name: "Lornette's Foundations",
    eyebrow: "LORNETTE'S FOUNDATIONS",
    primaryCtaLabel: 'Build athletic excellence, emotional resilience, and sustainable performance systems:',
    primaryUrl: 'https://lornettedaye.com/foundations'
  },
  'Pillar 3': {
    name: 'UMATTR Academy',
    eyebrow: 'UMATTR ACADEMY',
    primaryCtaLabel: 'Master applied AI skills, prompt engineering, and career intelligence in practical labs:',
    primaryUrl: 'https://www.umattr.ca/academy'
  },
  'Pillar 4': {
    name: 'Business Management & AI Consulting',
    eyebrow: 'BUSINESS MANAGEMENT & AI CONSULTING',
    primaryCtaLabel: 'Align organizational workflows, scale operations, and implement practical AI strategies:',
    primaryUrl: 'https://www.umattr.ca/business/consulting'
  },
  'Pillar 5': {
    name: 'Website Design & Business Growth',
    eyebrow: 'WEBSITE DESIGN & BUSINESS GROWTH',
    primaryCtaLabel: 'Architect an executive digital identity, conversion-focused web presence, and growth engine:',
    primaryUrl: 'https://www.umattr.ca/website'
  }
};

function getPillarKey(pillarStr) {
  for (const k of Object.keys(PILLARS_CONFIG)) {
    if (pillarStr.startsWith(k)) return k;
  }
  return 'Pillar 1';
}

function buildFivePillarStack(activePillarKey) {
  const cfg = PILLARS_CONFIG[activePillarKey];

  return `FIVE CONNECTED OPPORTUNITIES WITH LORNETTE DAYE & UMATTR:

FEATURED OPPORTUNITY:
${cfg.name.toUpperCase()}:
${cfg.primaryCtaLabel}
${cfg.primaryUrl}

EXPLORE THE COMPLETE ECOSYSTEM:
1. Personal Mentorship: https://lornettedaye.com/mentorship
2. Lornette's Foundations: https://lornettedaye.com/foundations
3. UMATTR Academy: https://www.umattr.ca/academy
4. Business & AI Consulting: https://www.umattr.ca/business
5. Website Design & Growth: https://www.umattr.ca/website`;
}

const masterQueue = [];

for (let idx = 0; idx < rows.length; idx++) {
  const r = rows[idx];
  const postIndex = idx + 1;
  const pillarKey = getPillarKey(r.Pillar);
  const pillarCfg = PILLARS_CONFIG[pillarKey];

  // Clean raw copy
  let cleanedBody = r.Full_LinkedIn_Post_Text
    // Remove em dashes
    .replace(/—/g, ' - ')
    .replace(/\u2014/g, ' - ')
    // Remove asterisks
    .replace(/\*/g, '')
    // Replace Coach Lornette
    .replace(/Coach Lornette/g, 'Lornette Daye')
    // Remove any trailing CTA lines that might duplicate the stack
    .replace(/👉[^\n]+/g, '')
    .replace(/🔗[^\n]+/g, '')
    .trim();

  // Extract hashtags from bottom
  const hashtagMatches = cleanedBody.match(/(#[A-Za-z0-9_]+\s*)+$/);
  let hashtags = '#LornetteDaye #UMATTR #Mentorship #Foundations #BusinessGrowth #BetterPeopleBetterPlayers';
  if (hashtagMatches) {
    hashtags = hashtagMatches[0].trim();
    cleanedBody = cleanedBody.substring(0, hashtagMatches.index).trim();
  }

  // Remove old raw single CTA URLs from body
  cleanedBody = cleanedBody.replace(/https?:\/\/[^\s]+/g, '').trim();

  const cdnUrl = `https://lornettedaye.com/campaigns/foundations-umattr/${r.Image_File}`;
  const fivePillarStack = buildFivePillarStack(pillarKey);

  const fullCaption = `${pillarCfg.eyebrow}

${cleanedBody}

${fivePillarStack}

${hashtags}`;

  // Assertions
  if (fullCaption.includes('*')) {
    throw new Error(`Post #${postIndex} contains asterisks!`);
  }
  if (fullCaption.includes('—') || fullCaption.includes('\u2014')) {
    throw new Error(`Post #${postIndex} contains em dashes!`);
  }
  if (fullCaption.includes('Coach Lornette')) {
    throw new Error(`Post #${postIndex} contains Coach Lornette!`);
  }
  if (!fullCaption.includes('https://lornettedaye.com/mentorship') ||
      !fullCaption.includes('https://lornettedaye.com/foundations') ||
      !fullCaption.includes('https://www.umattr.ca/academy') ||
      !fullCaption.includes('https://www.umattr.ca/business') ||
      !fullCaption.includes('https://www.umattr.ca/website')) {
    throw new Error(`Post #${postIndex} is missing one of the 5 ecosystem links!`);
  }

  masterQueue.push({
    postIndex,
    postId: r.Post_ID,
    dayNumber: parseInt(r.Day_Number, 10),
    slot: r.Slot,
    scheduledDate: r.Date,
    dayOfWeek: r.Day_Of_Week,
    timeSlot: r.Time_Slot,
    scheduledAt: r.Due_At_UTC,
    pillar: r.Pillar,
    theme: r.Theme,
    imageFilename: r.Image_File,
    localPath: `/campaigns/foundations-umattr/${r.Image_File}`,
    cdnUrl,
    assetDescription: r.Asset_Description,
    eyebrow: pillarCfg.eyebrow,
    caption: fullCaption,
    hashtags
  });
}

// Write master queue JSON
const QUEUE_PATH = path.resolve('scripts/master-foundations-umattr-queue.json');
fs.writeFileSync(QUEUE_PATH, JSON.stringify(masterQueue, null, 2), 'utf-8');
console.log(`Saved master queue with ${masterQueue.length} posts to ${QUEUE_PATH}`);

// Generate HTML Review Gallery
const htmlGallery = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Campaign Review: Lornette Daye × UMATTR (180 Posts)</title>
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
      max-width: 1400px;
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
    .theme {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 14px;
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
    <h1>Lornette Daye × UMATTR: 90-Day Goals & Mentorship Campaign</h1>
    <p style="color: var(--muted); max-width: 800px; margin: 0 auto;">
      180 Master Editorial Posts &bull; Oct 30, 2026 – Jan 27, 2027 (90 Consecutive Days) &bull; 2 Posts Daily (8:00 AM & 1:00 PM)<br>
      The 5 Connected Opportunities: Mentorship, Foundations, UMATTR Academy, Business & AI Consulting, Website Design
    </p>
    <div class="stats">
      <div class="stat-item"><div class="stat-val">180</div><div class="stat-lbl">Master Posts</div></div>
      <div class="stat-item"><div class="stat-val">90 Days</div><div class="stat-lbl">Duration</div></div>
      <div class="stat-item"><div class="stat-val">5 Pillars</div><div class="stat-lbl">Connected Ecosystem</div></div>
      <div class="stat-item"><div class="stat-val">100%</div><div class="stat-lbl">Zero-Asterisk & Zero-Em-Dash Compliant</div></div>
    </div>
  </header>

  <main class="grid">
    ${masterQueue.map(item => `
      <div class="card">
        <div class="img-wrap">
          <img src="${item.localPath}" alt="${item.theme}" loading="lazy">
        </div>
        <div class="card-body">
          <div class="post-meta">
            <span class="post-num">Post #${item.postIndex} (${item.postId})</span>
            <span>Day ${item.dayNumber} &bull; ${item.slot}</span>
          </div>
          <div class="eyebrow">${item.pillar}</div>
          <div class="theme">${item.theme}</div>
          <div class="caption-box">${item.caption}</div>
          <div class="links-badge">
            <span class="link-tag">&check; Mentorship</span>
            <span class="link-tag">&check; Foundations</span>
            <span class="link-tag">&check; Academy</span>
            <span class="link-tag">&check; Business</span>
            <span class="link-tag">&check; Website</span>
          </div>
        </div>
      </div>
    `).join('')}
  </main>
</body>
</html>`;

const HTML_PATH = path.resolve('public/campaigns/foundations-umattr/review.html');
fs.writeFileSync(HTML_PATH, htmlGallery, 'utf-8');
console.log(`Generated HTML gallery at ${HTML_PATH}`);
