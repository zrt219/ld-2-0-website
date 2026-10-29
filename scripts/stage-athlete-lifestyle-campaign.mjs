import fs from 'node:fs';
import path from 'node:path';

const SRC_DIR = 'C:\\Users\\Zhane\\Documents\\Website stuff\\lornetteig\\Career Circle Posts\\november\\main gold november campaign';
const DEST_DIR = path.resolve('public/campaigns/athlete-lifestyle');

if (!fs.existsSync(DEST_DIR)) {
  fs.mkdirSync(DEST_DIR, { recursive: true });
}

// 71 Canonical Images
const CANONICAL_FILES = [
  { file: "2026 College Football NIL Valuations-6.png", slug: "01-cfb-nil-valuations", title: "College Football NIL Valuations and the Reality of Modern Player Equity" },
  { file: "A Million-Dollar Women’s Football Moment.png", slug: "02-million-dollar-womens-football", title: "A Million Dollar Women's Football Moment: Rewriting the Commercial Ceiling" },
  { file: "A'ja Wilson inspires the next generation.png", slug: "03-aja-wilson-next-gen", title: "A'ja Wilson: Inspiring the Next Generation Beyond the Championship Trophy" },
  { file: "A'ja Wilson_ Greatness, Season After Season-16.png", slug: "04-aja-wilson-greatness-season", title: "A'ja Wilson: Season-Built Greatness and Repeatable Standards" },
  { file: "A'ja Wilson_ The Work and Impact-18.png", slug: "05-aja-wilson-work-and-impact", title: "A'ja Wilson: The Unseen Work and Long-Term Cultural Impact" },
  { file: "A'ja Wilson’s season-built greatness.png", slug: "06-aja-wilson-season-built", title: "Building a Legacy That Outlasts the Season" },
  { file: "Andraya Carter_ From Court to Conversation-17.png", slug: "07-andraya-carter-court-to-conversation", title: "Andraya Carter: From Hardwood Intensity to Broadcasting Authority" },
  { file: "Andraya Carter_ Gold-Edged Game Insight-14.png", slug: "08-andraya-carter-game-insight", title: "Deep Analytical Acumen: The Transition from Player to Premier Analyst" },
  { file: "Andraya Carter_ She Knows the Game.png", slug: "09-andraya-carter-she-knows-game", title: "Commanding the Room: Expertise That Commands Respect" },
  { file: "Andraya Carter_ The next generation’s voice-19.png", slug: "10-andraya-carter-next-gen-voice", title: "A Voice for the Next Generation of Sports Storytellers" },
  { file: "A’ja Wilson_ More than a player-21.png", slug: "11-aja-wilson-more-than-player", title: "The Athlete Beyond the Jersey: Developing Complete Human Excellence" },
  { file: "A’ja Wilson_ Work, achievement, and impact.png", slug: "12-aja-wilson-achievement-impact", title: "Achievement Without Emotional Balance Is Just Noise" },
  { file: "Bahamas 400m runner on a world stage.png", slug: "13-bahamas-400m-world-stage", title: "Standing on the World Stage: The Weight of National Pride" },
  { file: "Bahamas athlete behind the performance.png", slug: "14-bahamas-behind-performance", title: "The Mind Behind the Stride: Olympic Focus in Solitude" },
  { file: "Bahamas athlete_ one lap, years of commitment.png", slug: "15-bahamas-one-lap-commitment", title: "One Lap, Years of Discipline: The Architecture of True Commitment" },
  { file: "Behind the headset_ Ryan Day-3.png", slug: "16-ryan-day-behind-headset-3", title: "Behind the Headset: Executive Presence in High-Pressure Arenas" },
  { file: "Beyond the contract_ athlete futures-13.png", slug: "17-beyond-contract-athlete-futures", title: "Beyond the Contract: Architecting the Post-Athletic Career Blueprint" },
  { file: "Carr family football legacy.png", slug: "18-carr-family-legacy", title: "The Carr Family Legacy: Navigating Expectations Across Generations" },
  { file: "Carr family sports legacy.png", slug: "19-carr-family-sports-legacy", title: "Passing the Torch: Building Multigenerational Athletic Character" },
  { file: "CFL 2026 Top Five Paid Players-2.png", slug: "20-cfl-top-paid-players", title: "CFL 2026 Financial Realities: Smart Wealth Systems for Pro Athletes" },
  { file: "CFL career pathways, wellbeing, and transition-1.png", slug: "21-cfl-career-pathways-wellbeing", title: "CFL Pathways: Health, Career Transition, and Life Beyond the Goalposts" },
  { file: "CFL_ Canadian game, real business-3.png", slug: "22-cfl-canadian-game-real-business", title: "The Business Behind the Gridiron: Preparing Canadian Athletes for Boardrooms" },
  { file: "Chas Nimrod, Ready for the Moment-2.png", slug: "23-chas-nimrod-ready-moment-2", title: "Chas Nimrod: Preparing When Nobody Is Watching for When Everyone Is" },
  { file: "Chas Nimrod, ready for the moment.png", slug: "24-chas-nimrod-ready-moment", title: "When Opportunity Knocks, Only Prior Preparation Answers" },
  { file: "Chas Nimrod_ Every Opportunity-8.png", slug: "25-chas-nimrod-every-opportunity", title: "Every Opportunity Carries a Responsibility to Execute" },
  { file: "Chas Nimrod_ The unseen work.png", slug: "26-chas-nimrod-unseen-work", title: "The Solitary Work That Breeds Public Poise" },
  { file: "Chas Nimrod_ The Work Unseen-5.png", slug: "27-chas-nimrod-work-unseen-5", title: "Refining the Micro-Habits of Championship Readiness" },
  { file: "CJ Carr practices at Notre Dame-3.png", slug: "28-cj-carr-notre-dame-practice", title: "Under the Golden Dome: Establishing Personal Identity in Storied Programs" },
  { file: "CJ Carr_ Football family, his own path-1.png", slug: "29-cj-carr-his-own-path", title: "Football Royalty, Personal Blueprint: Carving an Independent Trajectory" },
  { file: "College football beyond the lights-7.png", slug: "30-college-football-beyond-lights", title: "Beyond the Stadium Lights: The Mental Health Reality of Modern Athletes" },
  { file: "College football's $8 billion business-4.png", slug: "31-college-football-8-billion-business", title: "College Football's 8 Billion Dollar Landscape: Protecting the Human Asset" },
  { file: "Edmonton Oilers with Ryan Nugent-Hopkins-22.png", slug: "32-edmonton-oilers-nugent-hopkins", title: "Longevity on the Ice: Ryan Nugent-Hopkins and the Power of Consistency" },
  { file: "EPL top five salary rankings-16.png", slug: "33-epl-top-five-salary-rankings", title: "Global Football Compensation: Financial Longevity for International Pros" },
  { file: "Every opportunity has a story.png", slug: "34-every-opportunity-story", title: "Every Opportunity Carries an Untold Story of Sacrifice" },
  { file: "Finally_ women's football, elevated.png", slug: "35-finally-womens-football-elevated", title: "The Elevation of Women's Football: Valuing Performance and Equity" },
  { file: "From Hawaiʻi to the stadium-2.png", slug: "36-hawaii-to-stadium-2", title: "Roots and Heritage: Carrying Island Culture to the Biggest Stages" },
  { file: "From Hawaiʻi, built for the moment-1.png", slug: "37-hawaii-built-for-moment-1", title: "Resilience Forged in Community: Grounded Leadership Under Fire" },
  { file: "Generations of the game-2.png", slug: "38-generations-of-the-game", title: "Generational Lessons: What Veteran Athletes Must Pass to Emerging Talent" },
  { file: "Golden football moment_ Girma and Smith-11.png", slug: "39-golden-moment-girma-smith", title: "Naomi Girma and Olivia Smith: Championship Chemistry and Cultural Impact" },
  { file: "Jayden Maiava_ Leadership Beyond the Field-3.png", slug: "40-jayden-maiava-leadership-field", title: "Jayden Maiava: Leading the Huddle with Humility and Decisive Poise" },
  { file: "Manning Family Football Legacy-24.png", slug: "41-manning-family-legacy-24", title: "The Manning Playbook: Building Family Governance in Pro Sports" },
  { file: "Manning family football legacy-25.png", slug: "42-manning-family-legacy-25", title: "Navigating Surnames and Pressure: Developing the Individual First" },
  { file: "Michael Irvin Miami Hurricanes editorial-12.png", slug: "43-michael-irvin-miami-editorial", title: "Michael Irvin: Passion, Intensity, and Channeling Energy for Growth" },
  { file: "Michael Irvin_ Miami to the world stage.png", slug: "44-michael-irvin-world-stage", title: "From Coral Gables to Global Prominence: The Evolution of Athletic Identity" },
  { file: "Michael Irvin_ The U Stays With You-9.png", slug: "45-michael-irvin-u-stays-9", title: "The Brotherhood of Sport: Leveraging Lifelong Networks in Business" },
  { file: "Michael Irvin_ The U stays with you.png", slug: "46-michael-irvin-u-stays", title: "The Bonds of Locker Room Culture: Replicating Team Chemistry in Corporate Life" },
  { file: "Michael Irvin’s Miami Hurricanes Legacy-15.png", slug: "47-michael-irvin-legacy-15", title: "Legacy Beyond the Field: Redefining What It Means to Be a Playmaker" },
  { file: "Naomi Girma and Olivia Smith_ Finally-6.png", slug: "48-naomi-girma-olivia-smith-finally", title: "Market Recognition Arrives: When Preparation Meets Inevitable Value" },
  { file: "NBA's Top Five Salaries, 2026–27-11.png", slug: "49-nba-top-salaries-2026-27", title: "NBA Contract Realities: Wealth Creation vs Long-Term Stewardship" },
  { file: "NFL after the game_ next chapters-20.png", slug: "50-nfl-after-the-game-next-chapters", title: "Life After the Final Whistle: Navigating the NFL Career Transition" },
  { file: "NFL Sundays_ a massive business-12.png", slug: "51-nfl-sundays-massive-business", title: "NFL Sundays as an Economic Engine: Athletes as Strategic Stakeholders" },
  { file: "NFL’s Biggest Contracts_ 2026 Annual Averages-15.png", slug: "52-nfl-biggest-contracts-2026", title: "Navigating High-Stakes Contracts: Financial Poise and Advisory Circles" },
  { file: "NHL revenue behind the ice-8.png", slug: "53-nhl-revenue-behind-ice", title: "Behind the Ice: Understanding Commercial Growth in Professional Hockey" },
  { file: "NHL's 2026–27 top five paid players-5.png", slug: "54-nhl-top-five-paid-players", title: "Hockey Longevity: Sustainable Performance and Post-Skating Portfolios" },
  { file: "Oilers home ice with Nugent-Hopkins-26.png", slug: "55-oilers-home-ice-nugent-hopkins", title: "Home Ice Leadership: How Veteran Presence Anchors Team Culture" },
  { file: "Premier League 2026–27 top earners-17.png", slug: "56-premier-league-top-earners", title: "Premier League Financial Velocity: Grounding Global Icons in Real Life" },
  { file: "Premier League career pathways-19.png", slug: "57-premier-league-career-pathways", title: "International Career Pathways: Preparing Global Athletes for Modern Enterprise" },
  { file: "Premier League dreams, real-life revenue-14.png", slug: "58-premier-league-dreams-revenue", title: "Beyond the Pitch: Building Sustainable Business Models for Footballers" },
  { file: "Ryan Day champions strong leadership.png", slug: "59-ryan-day-champions-leadership", title: "Ryan Day: Constructing High-Accountability Cultural Foundations" },
  { file: "Ryan Day leads with strength-4.png", slug: "60-ryan-day-leads-with-strength", title: "Quiet Strength Under Intense Spotlight: The Coach's Emotional Anchor" },
  { file: "Ryan Day_ Behind the Headset.png", slug: "61-ryan-day-behind-headset-portrait", title: "Behind the Headset: Calm Decisions in the Chaos of Big Ten Football" },
  { file: "Ryan Day_ Leadership Through Listening-1.png", slug: "62-ryan-day-leadership-listening-1", title: "Leadership Through Listening: Cultivating the Modern Athlete Voice" },
  { file: "Ryan Day’s Leadership in Listening.png", slug: "63-ryan-day-leadership-listening", title: "Empathetic Command: Why Listening Is the Ultimate Competitive Advantage" },
  { file: "Ryan Nugent-Hopkins in Oilers Gold-20.png", slug: "64-ryan-nugent-hopkins-oilers-gold", title: "Quiet Discipline: The 82-Game Grind and Year-Round Lifestyle Mastery" },
  { file: "Shaunae Miller-Uibo in gold and ivory-10.png", slug: "65-shaunae-miller-uibo-gold-ivory", title: "Shaunae Miller-Uibo: Olympic Grace and Regal Executive Presence" },
  { file: "Shaunae Miller-Uibo on the world stage-7.png", slug: "66-shaunae-miller-uibo-world-stage", title: "Commanding the Global Stage: When Athletic Mastery Meets Poise" },
  { file: "Shaunae Miller-Uibo_ One lap, years of commitment-23.png", slug: "67-shaunae-one-lap-commitment-23", title: "The 400-Meter Metaphor: Sustaining Velocity Through the Final Curve of Life" },
  { file: "The Premier League’s £6.8 Billion Price Tag-10.png", slug: "68-premier-league-price-tag", title: "The 6.8 Billion Pound Broadcast Reality: Athletes as Cultural Assets" },
  { file: "The value was always there-13.png", slug: "69-value-was-always-there", title: "The Value Was Always There: Recognizing Intrinsic Worth Before the World Catches Up" },
  { file: "What Players Negotiate Matters-9.png", slug: "70-what-players-negotiate-matters", title: "What Players Negotiate Matters: Moving from Short-Term Cash to Long-Term Ownership" },
  { file: "Who shares in the game’s success_-18.png", slug: "71-who-shares-in-game-success", title: "Who Shares in the Game's Success: Building Fair Systems for the Next Generation" }
];

console.log(`Checking ${CANONICAL_FILES.length} canonical files...`);
let copied = 0;
for (const item of CANONICAL_FILES) {
  const srcPath = path.join(SRC_DIR, item.file);
  const destPath = path.join(DEST_DIR, `${item.slug}.png`);
  if (!fs.existsSync(srcPath)) {
    console.error(`Missing file: ${srcPath}`);
  } else {
    fs.copyFileSync(srcPath, destPath);
    copied++;
  }
}
console.log(`Copied ${copied} files to ${DEST_DIR}`);
