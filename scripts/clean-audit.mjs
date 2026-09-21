import fs from 'fs';
import path from 'path';

function getFiles(dir) {
  let results = [];
  if (!fs.existsSync(dir)) return results;
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getFiles(fullPath));
    } else {
      results.push(fullPath);
    }
  });
  return results;
}

const publicDir = path.resolve('public');
const allPublicFiles = getFiles(publicDir);
const imageExtensions = new Set(['.png', '.jpg', '.jpeg', '.webp', '.svg', '.avif', '.gif']);

const publicImages = allPublicFiles
  .filter(f => imageExtensions.has(path.extname(f).toLowerCase()))
  .map(f => path.relative(publicDir, f).replace(/\\/g, '/'));

// Scan code files across src, content, tests, docs, and scripts (excluding audit/report files)
const searchDirs = ['src', 'scripts', 'tests', 'docs', 'content'].map(d => path.resolve(d));
let allCodeFiles = [];
searchDirs.forEach(d => {
  allCodeFiles = allCodeFiles.concat(getFiles(d));
});
const rootFiles = ['AGENTS.md', 'README.md', 'next.config.mjs', 'next.config.js', 'package.json'].map(f => path.resolve(f)).filter(fs.existsSync);
allCodeFiles = allCodeFiles.concat(rootFiles);

const codeContents = allCodeFiles
  .filter(f => {
    const rel = path.relative(process.cwd(), f).replace(/\\/g, '/');
    if (rel.includes('unused-report') || rel.includes('non-campaign-unused') || rel.includes('audit-') || rel.includes('inspect-')) return false;
    const ext = path.extname(f).toLowerCase();
    return ['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.json', '.md', '.css', '.html', '.py'].includes(ext);
  })
  .map(f => ({
    file: path.relative(process.cwd(), f).replace(/\\/g, '/'),
    content: fs.readFileSync(f, 'utf8')
  }));

const unused = [];
const used = [];

publicImages.forEach(img => {
  const filename = path.basename(img);
  const publicPath = '/' + img;
  const matched = codeContents.some(({ content }) => content.includes(img) || content.includes(publicPath) || content.includes(filename));
  const fullPath = path.join(publicDir, img);
  const stat = fs.statSync(fullPath);
  const item = {
    path: img,
    sizeKB: (stat.size / 1024).toFixed(1),
    bytes: stat.size
  };
  if (matched) {
    used.push(item);
  } else {
    unused.push(item);
  }
});

console.log(`Total images: ${publicImages.length}`);
console.log(`Used: ${used.length}`);
console.log(`Unused: ${unused.length}`);

const byDir = {};
unused.forEach(u => {
  const dir = path.dirname(u.path);
  if (!byDir[dir]) byDir[dir] = [];
  byDir[dir].push(u);
});

console.log('\n--- Summary by directory ---');
for (const dir of Object.keys(byDir).sort()) {
  const files = byDir[dir];
  const mb = (files.reduce((a, b) => a + b.bytes, 0) / (1024 * 1024)).toFixed(2);
  console.log(`${dir.padEnd(30)} : ${String(files.length).padStart(3)} files (${mb.padStart(6)} MB)`);
}

