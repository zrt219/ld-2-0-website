import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const routes = [
  '/foundations',
  '/foundations/golf',
  '/foundations/clubs',
  '/foundations/performance-edge',
  '/book',
];

const viewports = [
  { name: '360', width: 360, height: 780 },
  { name: '390', width: 390, height: 844 },
  { name: '430', width: 430, height: 932 },
  { name: '768', width: 768, height: 1024 },
  { name: '1024', width: 1024, height: 768 },
  { name: '1440', width: 1440, height: 900 },
];

const brainDir = 'C:/Users/Zhane/.gemini/antigravity/brain/572e6bbe-0ffe-40d2-bf56-4c4f57ec28eb/baseline_audit';
if (!fs.existsSync(brainDir)) {
  fs.mkdirSync(brainDir, { recursive: true });
}

async function runAudit() {
  const browser = await chromium.launch({ headless: true });
  const report = [];

  for (const route of routes) {
    console.log(`Auditing route: ${route}`);
    for (const vp of viewports) {
      const page = await browser.newPage({
        viewport: { width: vp.width, height: vp.height },
      });

      try {
        await page.goto(`http://localhost:3000${route}`, { waitUntil: 'domcontentloaded' });
        await page.waitForTimeout(500);

        const overflow = await page.evaluate(() => {
          const docEl = document.documentElement;
          const body = document.body;
          const vpWidth = window.innerWidth;
          return {
            vpWidth,
            docScrollWidth: docEl.scrollWidth,
            bodyScrollWidth: body.scrollWidth,
            hasOverflow: docEl.scrollWidth > vpWidth + 1 || body.scrollWidth > vpWidth + 1,
          };
        });

        const slug = route.replace(/\//g, '_').replace(/^_/, '');
        const filename = `${slug || 'home'}_${vp.name}.png`;
        await page.screenshot({ path: path.join(brainDir, filename), fullPage: false });

        report.push({
          route,
          viewport: vp.name,
          overflow,
          screenshot: filename,
        });
      } catch (err) {
        console.error(`Error on ${route} (${vp.name}):`, err.message);
      } finally {
        await page.close();
      }
    }
  }

  await browser.close();
  fs.writeFileSync(path.join(brainDir, 'audit-report.json'), JSON.stringify(report, null, 2));
  console.log('Baseline audit and screenshots complete.');
}

runAudit().catch(console.error);
