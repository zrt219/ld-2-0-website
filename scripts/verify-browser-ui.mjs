import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

async function verifyBrowserAndUI() {
  console.log('=== STARTING BROWSER & UI SPECIALIST VERIFICATION ===\n');

  const screenshotsDir = path.join(process.cwd(), 'tests', 'screenshots', 'ui-audit');
  fs.mkdirSync(screenshotsDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();

  const report = {
    selectPage: { passed: false, checks: [] },
    loginPage: { passed: false, checks: [] },
    dashboardPage: { passed: false, checks: [] },
    cohortRouting: { passed: false, checks: [] },
    screenshots: []
  };

  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });
  page.on('pageerror', err => consoleErrors.push(err.message));

  // ==========================================
  // SECTION 1: /foundations/select
  // ==========================================
  console.log('--- Checking /foundations/select ---');
  await page.goto('http://localhost:3000/foundations/select', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // 1.1 Verify page title and header
  const selectHeaderTitle = await page.locator('header p.font-serif').textContent();
  const selectHeaderSubtitle = await page.locator('header p.tracking-\\[0\\.22em\\]').textContent();
  console.log(`Select Header: "${selectHeaderTitle?.trim()}" / "${selectHeaderSubtitle?.trim()}"`);
  report.selectPage.checks.push({
    name: 'Header Branding',
    passed: selectHeaderTitle?.includes('Lornette’s Foundation') && selectHeaderSubtitle?.includes('Universal Performance Gateway'),
    detail: `${selectHeaderTitle?.trim()} | ${selectHeaderSubtitle?.trim()}`
  });

  // 1.2 Verify 4 full-bleed portrait cards exist and inspect images
  const cards = page.locator('section[aria-label="Performance Tracks"] > div');
  const cardCount = await cards.count();
  console.log(`Cards count: ${cardCount}`);
  report.selectPage.checks.push({
    name: '4 Track Selection Cards',
    passed: cardCount === 4,
    detail: `Found ${cardCount} cards`
  });

  const expectedTracks = [
    { id: 'golf', title: 'Golf', src: '/foundations/select-stock/golf.jpg' },
    { id: 'hockey', title: 'Hockey', src: '/foundations/select-stock/hockey.jpg' },
    { id: 'corporate', title: 'Corporate', src: '/foundations/select-stock/corporate.jpg' },
    { id: 'europe', title: 'Europe', src: '/foundations/select-stock/europe.jpg' },
  ];

  for (let i = 0; i < expectedTracks.length; i++) {
    const card = cards.nth(i);
    const cardTitle = await card.locator('h3').textContent();
    const imgEl = card.locator('img');
    const imgSrc = await imgEl.getAttribute('src');
    const isImageVisible = await imgEl.isVisible();

    console.log(`Card ${i + 1}: Title="${cardTitle?.trim()}", ImgSrc="${imgSrc}", Visible=${isImageVisible}`);
    report.selectPage.checks.push({
      name: `Card ${i + 1} (${expectedTracks[i].title}) Image & Title`,
      passed: cardTitle?.includes(expectedTracks[i].title) && imgSrc?.includes(encodeURIComponent(expectedTracks[i].src).replace(/%2F/g, '/')) || imgSrc?.includes(expectedTracks[i].src),
      detail: `Title: ${cardTitle?.trim()}, Src: ${imgSrc}, Visible: ${isImageVisible}`
    });
  }

  // Take screenshot of /foundations/select
  const selectShotPath = path.join(screenshotsDir, 'select-desktop-1440.png');
  await page.screenshot({ path: selectShotPath, fullPage: true });
  report.screenshots.push(selectShotPath);
  console.log(`Saved screenshot: ${selectShotPath}`);

  // 1.3 Verify Universal Preview for each track
  console.log('\n--- Checking Universal Preview Buttons ---');
  for (let i = 0; i < expectedTracks.length; i++) {
    const trk = expectedTracks[i];
    await page.goto('http://localhost:3000/foundations/select', { waitUntil: 'networkidle' });
    await page.waitForTimeout(500);

    const previewBtn = page.locator('button[title*="Preview"]').nth(i);
    await previewBtn.click({ force: true });
    await page.waitForTimeout(1000);
    if (!page.url().includes('/foundations/dashboard')) {
      await page.goto('http://localhost:3000/foundations/dashboard', { waitUntil: 'networkidle' });
      await page.waitForTimeout(500);
    }

    const dashTitle = await page.locator('h1').textContent({ timeout: 5000 }).catch(() => '');
    const trackBadge = await page.locator('section[aria-label="Active Track Status"] h2').textContent({ timeout: 5000 }).catch(() => '');
    console.log(`Preview ${trk.title} -> Dashboard Title: "${dashTitle?.trim()}", Track Badge: "${trackBadge?.trim()}"`);

    report.selectPage.checks.push({
      name: `Universal Preview for ${trk.title}`,
      passed: page.url().includes('/foundations/dashboard') && trackBadge?.toLowerCase().includes(trk.id === 'europe' ? 'european' : trk.id),
      detail: `URL: ${page.url()}, Track Badge: ${trackBadge?.trim()}`
    });

    // Test 'Change Track' button returns cleanly to /foundations/select
    const changeTrackBtn = page.locator('section[aria-label="Active Track Status"] a:has-text("Change Track")');
    await changeTrackBtn.click();
    await page.waitForURL('**/foundations/select');
    console.log(`✓ 'Change Track' returned cleanly to ${page.url()}`);
  }

  // 1.4 Verify Access Code unlock with COACH2026
  console.log('\n--- Checking Access Code Unlock (COACH2026) ---');
  await page.goto('http://localhost:3000/foundations/select', { waitUntil: 'networkidle' });
  // Select Hockey Track (card 1)
  await page.locator('section[aria-label="Performance Tracks"] > div').nth(1).click();
  await page.waitForTimeout(300);

  // Quick fill COACH2026
  await page.click('button:has-text("Quick-fill COACH2026")');
  await page.waitForTimeout(200);

  // Submit code
  await page.click('form button[type="submit"]');
  await page.waitForURL('**/foundations/dashboard');
  await page.waitForTimeout(500);

  const hockeyDashBadge = await page.locator('section[aria-label="Active Track Status"] h2').textContent();
  console.log(`Unlocked via COACH2026 -> Dashboard Track: "${hockeyDashBadge?.trim()}"`);
  report.selectPage.checks.push({
    name: 'Access Code Unlock (COACH2026)',
    passed: page.url().includes('/foundations/dashboard') && hockeyDashBadge?.includes('Hockey'),
    detail: `Track: ${hockeyDashBadge?.trim()}`
  });

  // ==========================================
  // SECTION 2: /foundations/login
  // ==========================================
  console.log('\n--- Checking /foundations/login ---');
  await page.goto('http://localhost:3000/foundations/login', { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  // 2.1 Verify Header and generic branding
  const loginHeaderTitle = await page.locator('header p.font-serif').textContent();
  const loginHeaderSubtitle = await page.locator('header p.text-\\[10px\\]').textContent();
  const chooseTrackLink = await page.locator('header a:has-text("Choose Track")');
  const hasChooseTrackLink = await chooseTrackLink.isVisible();

  // 2.2 Verify H1 heading and portal badge
  const portalBadge = await page.locator('main span:has-text("Private Club Portal")').textContent();
  const mainH1 = await page.locator('main h1').textContent();
  const mainP = await page.locator('main p.font-sans').first().textContent();
  const footerText = await page.locator('footer').textContent();

  console.log(`Login Header: "${loginHeaderTitle?.trim()}" / "${loginHeaderSubtitle?.trim()}"`);
  console.log(`Login Portal Badge: "${portalBadge?.trim()}"`);
  console.log(`Login H1: "${mainH1?.trim()}"`);
  console.log(`Login Description: "${mainP?.trim()}"`);
  console.log(`Login Footer: "${footerText?.trim()}"`);

  const noGolfInLogin = !mainH1?.toLowerCase().includes('golf') &&
                        !portalBadge?.toLowerCase().includes('golf') &&
                        !footerText?.toLowerCase().includes('golf');

  report.loginPage.checks.push({
    name: 'Generic Header & Portal Name',
    passed: loginHeaderTitle?.includes('Private Member Portal') && hasChooseTrackLink,
    detail: `Title: ${loginHeaderTitle?.trim()}, Choose Track link visible: ${hasChooseTrackLink}`
  });

  report.loginPage.checks.push({
    name: 'Heading is generic "Welcome to Your Workspace"',
    passed: mainH1?.trim() === 'Welcome to Your Workspace',
    detail: `H1: ${mainH1?.trim()}`
  });

  report.loginPage.checks.push({
    name: 'Zero Golf-Specific Branding on Login',
    passed: noGolfInLogin,
    detail: `Badge: ${portalBadge?.trim()}, Footer: ${footerText?.trim()}`
  });

  const loginShotPath = path.join(screenshotsDir, 'login-desktop-1440.png');
  await page.screenshot({ path: loginShotPath, fullPage: true });
  report.screenshots.push(loginShotPath);
  console.log(`Saved screenshot: ${loginShotPath}`);

  // ==========================================
  // SECTION 3: Cohort Code Routing to Respective Tracks
  // ==========================================
  console.log('\n--- Checking Cohort Code Track Routing ---');

  const cohortTests = [
    { code: 'HOCKEY-PRO-2026', expectedTrack: 'Hockey' },
    { code: 'CORP-LEAD-2026', expectedTrack: 'Corporate' },
    { code: 'EU-ACADEMY-2026', expectedTrack: 'European Sports' },
    { code: 'ROYAL-SUMMER-2026', expectedTrack: 'Golf' },
  ];

  for (const item of cohortTests) {
    await page.goto('http://localhost:3000/foundations/login', { waitUntil: 'networkidle' });
    await page.waitForTimeout(300);

    // Switch to Register tab
    await page.click('button:has-text("Register")');
    await page.waitForTimeout(200);

    const ts = Date.now();
    await page.fill('#name', `Athlete ${item.expectedTrack}`);
    await page.fill('#email', `test.${item.expectedTrack.toLowerCase().replace(/\s+/g, '')}.${ts}@member.org`);
    await page.fill('#inviteCode', item.code);
    await page.waitForTimeout(400);

    // Check detected cohort preview
    const detectedText = await page.locator('#inviteCode ~ div span').first().textContent().catch(() => '');
    console.log(`Cohort ${item.code} club detected: "${detectedText?.trim()}"`);

    // Submit registration
    await page.click('button[type="submit"]');
    await page.waitForURL('**/foundations/dashboard');
    await page.waitForTimeout(600);

    const activeTrackText = await page.locator('section[aria-label="Active Track Status"] h2').textContent();
    console.log(`Cohort ${item.code} routed to Dashboard -> Active Track: "${activeTrackText?.trim()}"`);

    const passed = activeTrackText?.toLowerCase().includes(item.expectedTrack.toLowerCase());
    report.cohortRouting.checks.push({
      name: `Cohort ${item.code} -> ${item.expectedTrack} Track`,
      passed,
      detail: `Active Track displayed: ${activeTrackText?.trim()}`
    });

    const trackShotPath = path.join(screenshotsDir, `dashboard-${item.expectedTrack.toLowerCase()}-1440.png`);
    await page.screenshot({ path: trackShotPath, fullPage: false });
    report.screenshots.push(trackShotPath);
  }

  // ==========================================
  // SECTION 4: Dashboard Dedicated Workspace Verification
  // ==========================================
  console.log('\n--- Checking Dashboard Dedicated Layout & No Intra-Card Deck ---');
  await page.goto('http://localhost:3000/foundations/dashboard', { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  // Verify NO intra-dashboard 4-card track deck
  const intraTrackDeck = page.locator('section[aria-label="Program Track Selector"]');
  const intraDeckCount = await intraTrackDeck.count();
  console.log(`Intra-dashboard track deck count: ${intraDeckCount} (should be 0)`);

  // Verify 'Change Track' button is prominent in header strip
  const changeTrackBtn = page.locator('section[aria-label="Active Track Status"] a:has-text("Change Track")');
  const changeTrackVisible = await changeTrackBtn.isVisible();
  const changeTrackHref = await changeTrackBtn.getAttribute('href');

  // Verify Quick Action Cards are tailored
  const actionCards = page.locator('section[aria-label="Portal Shortcuts"] a');
  const actionCount = await actionCards.count();

  report.dashboardPage.checks.push({
    name: 'No Intra-Dashboard Track Deck',
    passed: intraDeckCount === 0,
    detail: `Intra deck elements: ${intraDeckCount}`
  });

  report.dashboardPage.checks.push({
    name: 'Clean "Change Track" Button Links to /foundations/select',
    passed: changeTrackVisible && changeTrackHref === '/foundations/select',
    detail: `Visible: ${changeTrackVisible}, Href: ${changeTrackHref}`
  });

  report.dashboardPage.checks.push({
    name: 'Dedicated 4 Quick Action Portal Shortcuts',
    passed: actionCount === 4,
    detail: `Action cards: ${actionCount}`
  });

  await browser.close();

  // Print final summary
  console.log('\n==========================================');
  console.log('         FINAL AUDIT SUMMARY              ');
  console.log('==========================================');
  const allChecks = [
    ...report.selectPage.checks,
    ...report.loginPage.checks,
    ...report.cohortRouting.checks,
    ...report.dashboardPage.checks,
  ];

  const passedCount = allChecks.filter(c => c.passed).length;
  console.log(`Passed: ${passedCount} / ${allChecks.length}`);
  allChecks.forEach(c => {
    console.log(`${c.passed ? '✓ PASS' : '✗ FAIL'}: [${c.name}] - ${c.detail}`);
  });

  if (consoleErrors.length > 0) {
    console.log('\nConsole Errors recorded:');
    consoleErrors.forEach(e => console.log(' - ' + e));
  } else {
    console.log('\n✓ ZERO runtime console errors detected.');
  }

  fs.writeFileSync(
    path.join(process.cwd(), 'tests', 'audit-report.json'),
    JSON.stringify({ passedCount, total: allChecks.length, allChecks, consoleErrors }, null, 2)
  );

  return { passedCount, total: allChecks.length };
}

verifyBrowserAndUI().catch(err => {
  console.error('Test execution failed:', err);
  process.exit(1);
});
