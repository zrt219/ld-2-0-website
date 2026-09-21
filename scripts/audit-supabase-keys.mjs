import fs from 'fs';
import path from 'path';

const SRC_DIR = path.join(process.cwd(), 'src');

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(f => {
    let dirPath = path.join(dir, f);
    let isDirectory = fs.statSync(dirPath).isDirectory();
    isDirectory ? walkDir(dirPath, callback) : callback(dirPath);
  });
}

let leaked = false;
walkDir(SRC_DIR, (filePath) => {
  if (filePath.endsWith('.ts') || filePath.endsWith('.tsx') || filePath.endsWith('.js')) {
    const content = fs.readFileSync(filePath, 'utf8');
    if (content.includes('NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY')) {
      console.error('[AUDIT FAILED] Accidental exposure of NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY in ' + filePath);
      leaked = true;
    }
  }
});

if (leaked) {
  process.exit(1);
} else {
  console.log('[AUDIT PASSED] No NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY found in src files.');
}
