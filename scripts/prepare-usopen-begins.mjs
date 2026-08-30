import fs from 'fs';
import path from 'path';

const srcDir = 'C:\\Users\\Zhane\\Documents\\Website stuff\\lornetteig\\Career Circle Posts\\August linkinedads\\us open #2\\New folder';
const destDir = path.join(process.cwd(), 'public', 'campaigns', 'us-open-begins');

if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.png') || f.endsWith('.jpg') || f.endsWith('.jpeg'));
console.log('Source files found:', files.length);

files.sort((a, b) => {
  const numA = parseInt(a.match(/\((\d+)\)/)?.[1] || '0', 10);
  const numB = parseInt(b.match(/\((\d+)\)/)?.[1] || '0', 10);
  return numA - numB;
});

files.forEach((f, i) => {
  const numStr = String(i + 1).padStart(2, '0');
  const targetName = `usopenbegins-${numStr}.png`;
  fs.copyFileSync(path.join(srcDir, f), path.join(destDir, targetName));
  console.log(`Copied ${f} -> ${targetName}`);
});

console.log('All 10 images copied successfully to public/campaigns/us-open-begins/');
