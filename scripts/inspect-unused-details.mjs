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
    if (rel.startsWith('scripts/unused-report') || rel.startsWith('scripts/inspect-') || rel.startsWith('scripts/audit-')) return false;
    const ext = path.extname(f).toLowerCase();
    return ['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.json', '.md', '.css', '.html', '.py'].includes(ext);
  })
  .map(f => ({
    file: path.relative(process.cwd(), f).replace(/\\/g, '/'),
    content: fs.readFileSync(f, 'utf8')
  }));


const unused = [];
publicImages.forEach(img => {
  const filename = path.basename(img);
  const publicPath = '/' + img;
  const matched = codeContents.some(({ content }) => content.includes(img) || content.includes(publicPath) || content.includes(filename));
  if (!matched) {
    const fullPath = path.join(publicDir, img);
    const stat = fs.statSync(fullPath);
    unused.push({
      path: img,
      size: (stat.size / 1024).toFixed(1) + ' KB',
      bytes: stat.size
    });
  }
});

fs.writeFileSync('scripts/unused-report.json', JSON.stringify(unused, null, 2));
console.log('Saved ' + unused.length + ' unused files to scripts/unused-report.json');

const nonCampaign = unused.filter(x => !x.path.startsWith('campaigns/'));
const byFolder = {};
nonCampaign.forEach(x => {
  const f = path.dirname(x.path);
  if (!byFolder[f]) byFolder[f] = [];
  byFolder[f].push(x);
});

fs.writeFileSync('scripts/non-campaign-unused.json', JSON.stringify(byFolder, null, 2));
console.log('Saved non-campaign unused summary to scripts/non-campaign-unused.json');
for (const folder of Object.keys(byFolder)) {
  const files = byFolder[folder];
  const totalMB = (files.reduce((acc, f) => acc + f.bytes, 0) / (1024*1024)).toFixed(2);
  console.log('FOLDER: ' + folder + ' -> ' + files.length + ' files (' + totalMB + ' MB)');
}



