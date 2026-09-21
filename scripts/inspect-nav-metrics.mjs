import { chromium } from "playwright";

async function run() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });

  console.log("Navigating to http://localhost:3000/ ...");
  await page.goto("http://localhost:3000/", { waitUntil: "networkidle" });

  const nav = page.getByLabel("Primary navigation");
  const headerBox = await page.locator("header").boundingBox();
  console.log("Header bounding box:", headerBox);

  // Test Foundations dropdown trigger
  const foundationsBtn = nav.getByRole("button", { name: /foundations menu/i });
  const foundationsBtnBox = await foundationsBtn.boundingBox();
  const foundationsLinkBox = await nav.getByRole("link", { name: /^Foundations$/i }).boundingBox();
  console.log("Foundations text link bottom:", foundationsLinkBox.y + foundationsLinkBox.height);
  console.log("Foundations chevron btn box:", foundationsBtnBox);
  console.log("Chevron vertical center:", foundationsBtnBox.y + foundationsBtnBox.height / 2);
  console.log("Text link vertical center:", foundationsLinkBox.y + foundationsLinkBox.height / 2);

  // Measure before opening flyout
  const bodyHeightBefore = await page.evaluate(() => document.body.scrollHeight);

  // Open Foundations flyout
  await foundationsBtn.click();
  await page.waitForSelector("#foundations-submenu");
  await page.waitForTimeout(300);

  const flyoutBox = await page.locator("#foundations-submenu ul").boundingBox();
  console.log("Foundations flyout box:", flyoutBox);
  console.log("Distance from Foundations link bottom (underline) to flyout top:", flyoutBox.y - (foundationsLinkBox.y + foundationsLinkBox.height));
  console.log("Distance from header bottom to flyout top:", flyoutBox.y - (headerBox.y + headerBox.height));

  const bodyHeightAfter = await page.evaluate(() => document.body.scrollHeight);
  console.log("Body height shift:", bodyHeightAfter - bodyHeightBefore);

  // Take screenshot of Foundations flyout open
  await page.screenshot({ path: "tests/screenshots/foundations-dropdown-1440.png" });
  console.log("Saved tests/screenshots/foundations-dropdown-1440.png");

  // Close Foundations flyout
  await foundationsBtn.click();
  await page.locator("#foundations-submenu").waitFor({ state: "hidden" });
  await page.waitForTimeout(150);

  // Test Books dropdown
  const booksBtn = nav.getByRole("button", { name: /books menu/i });
  const booksBtnBox = await booksBtn.boundingBox();
  const booksLinkBox = await nav.getByRole("link", { name: /^Books$/i }).boundingBox();
  console.log("Books text link bottom:", booksLinkBox.y + booksLinkBox.height);
  console.log("Books chevron btn box:", booksBtnBox);
  console.log("Books chevron vertical center:", booksBtnBox.y + booksBtnBox.height / 2);
  console.log("Books text link vertical center:", booksLinkBox.y + booksLinkBox.height / 2);

  await booksBtn.click();
  await page.waitForSelector("#books-submenu");
  await page.waitForTimeout(300);

  const booksFlyoutBox = await page.locator("#books-submenu ul").boundingBox();
  console.log("Books flyout box:", booksFlyoutBox);
  console.log("Distance from Books link bottom (underline) to flyout top:", booksFlyoutBox.y - (booksLinkBox.y + booksLinkBox.height));
  console.log("Distance from header bottom to flyout top:", booksFlyoutBox.y - (headerBox.y + headerBox.height));

  // Verify Books items
  const booksItems = await page.locator("#books-submenu a").allInnerTexts();
  console.log("Books flyout items:", booksItems);

  // Take screenshot of Books flyout open
  await page.screenshot({ path: "tests/screenshots/books-dropdown-1440.png" });
  console.log("Saved tests/screenshots/books-dropdown-1440.png");

  // Now test on /foundations page with secondary nav
  console.log("\nNavigating to /foundations ...");
  await page.goto("http://localhost:3000/foundations", { waitUntil: "networkidle" });
  const subnav = page.getByLabel("Foundations section navigation");
  const subnavBox = await subnav.boundingBox();
  const headerBoxFoundations = await page.locator("header").boundingBox();
  console.log("Header on /foundations:", headerBoxFoundations);
  console.log("Subnav on /foundations:", subnavBox);
  console.log("Gap between header bottom and subnav top:", subnavBox.y - (headerBoxFoundations.y + headerBoxFoundations.height));

  // Open Foundations dropdown on /foundations
  const foundationsBtnOnF = page.getByLabel("Primary navigation").getByRole("button", { name: /foundations menu/i });
  await foundationsBtnOnF.click();
  await page.waitForSelector("#foundations-submenu");
  await page.waitForTimeout(300);
  const flyoutOnF = await page.locator("#foundations-submenu ul").boundingBox();
  console.log("Flyout on /foundations box:", flyoutOnF);
  console.log("Flyout top vs subnav top:", flyoutOnF.y, "vs", subnavBox.y);
  console.log("Does flyout overlay subnav?", flyoutOnF.y < subnavBox.y + subnavBox.height && flyoutOnF.y + flyoutOnF.height > subnavBox.y);

  await page.screenshot({ path: "tests/screenshots/foundations-page-dropdown-1440.png" });
  console.log("Saved tests/screenshots/foundations-page-dropdown-1440.png");

  await page.screenshot({ path: "tests/screenshots/foundations-page-dropdown-1440.png" });
  console.log("Saved tests/screenshots/foundations-page-dropdown-1440.png");

  await browser.close();
}

run().catch(console.error);
