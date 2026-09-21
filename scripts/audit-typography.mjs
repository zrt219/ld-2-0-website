import fs from 'fs';

const files = [
  'src/app/foundations/page.tsx',
  'src/app/foundations/golf/page.tsx',
  'src/app/foundations/golf/keynote/page.tsx',
  'src/app/foundations/golf/workshop/page.tsx',
  'src/app/foundations/golf/program/page.tsx',
  'src/app/foundations/golf/club-partnership/page.tsx',
  'src/app/foundations/clubs/page.tsx',
  'src/app/foundations/performance-edge/page.tsx'
];

for (const f of files) {
  const content = fs.readFileSync(f, 'utf8');
  console.log('===', f, '===');
  
  // Find h1
  const h1Match = content.match(/<h1[^>]*>(.*?)<\/h1>/s);
  if (h1Match) {
    console.log('  H1:', h1Match[1].replace(/\s+/g, ' ').trim());
  }

  // Find kickers/badges
  const kickerMatches = [...content.matchAll(/<(?:span|p)[^>]*tracking-\[[^\]]+\][^>]*>(.*?)<\/(?:span|p)>/gs)];
  for (const km of kickerMatches.slice(0, 4)) {
    const text = km[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
    if (text) console.log('  Kicker/Eyebrow:', text);
  }

  // Find h2s
  const h2Matches = [...content.matchAll(/<h2[^>]*>(.*?)<\/h2>/gs)];
  for (const h2 of h2Matches) {
    console.log('  H2:', h2[1].replace(/\s+/g, ' ').trim());
  }
}
