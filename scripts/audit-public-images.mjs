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

console.log(`Found ${publicImages.length} images in public/`);

// Read all code and script files
const searchDirs = ['src', 'scripts', 'tests', 'docs', 'content'].map(d => path.resolve(d));
let allCodeFiles = [];
searchDirs.forEach(d => {
  allCodeFiles = allCodeFiles.concat(getFiles(d));
});

// Also check root files like package.json, AGENTS.md, etc.
const rootFiles = ['AGENTS.md', 'README.md', 'next.config.mjs', 'next.config.js', 'package.json'].map(f => path.resolve(f)).filter(fs.existsSync);
allCodeFiles = allCodeFiles.concat(rootFiles);

const codeContents = allCodeFiles
  .filter(f => {
    const ext = path.extname(f).toLowerCase();
    return ['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.json', '.md', '.css', '.html', '.py'].includes(ext);
  })
  .map(f => ({
    file: path.relative(process.cwd(), f).replace(/\\/g, '/'),
    content: fs.readFileSync(f, 'utf8')
  }));

console.log(`Searching across ${codeContents.length} files...`);

const report = [];

publicImages.forEach(img => {
  const filename = path.basename(img);
  const withoutExt = path.basename(img, path.extname(img));
  const publicPath = '/' + img;
  
  const matchedIn = [];
  
  codeContents.forEach(({ file, content }) => {
    // Check for exact path, filename, or withoutExt
    if (content.includes(img) || content.includes(publicPath) || content.includes(filename)) {
      matchedIn.push(file);
    }
  });

  report.push({
    image: img,
    matchedCount: matchedIn.length,
    matchedIn: matchedIn.slice(0, 5)
  });
});

const unused = report.filter(r => r.matchedCount === 0);
console.log(`\nTotal images: ${report.length}`);
console.log(`Used images count: ${report.length - unused.length}`);
console.log(`Unused images count: ${unused.length}`);

const byDir = {};
unused.forEach(u => {
  const dir = path.dirname(u.image);
  byDir[dir] = (byDir[dir] || 0) + 1;
});
console.log('\nUnused images by directory:');
console.log(JSON.stringify(byDir, null, 2));

