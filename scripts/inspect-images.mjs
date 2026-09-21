import fs from 'fs';

const files = [
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
  const tagRegex = /<Image\b[^>]*\/>/gs;
  let match;
  while ((match = tagRegex.exec(content)) !== null) {
    const tag = match[0];
    const srcMatch = tag.match(/src="([^"]+)"/);
    const posMatch = tag.match(/objectPosition:\s*"([^"]+)"/);
    const altMatch = tag.match(/alt="([^"]+)"/);
    console.log({
      src: srcMatch ? srcMatch[1] : 'unknown',
      objectPosition: posMatch ? posMatch[1] : 'default',
      alt: altMatch ? altMatch[1].slice(0, 40) + '...' : 'none'
    });
  }
}
