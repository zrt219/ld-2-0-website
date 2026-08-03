import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";
import { chromium } from "playwright";

const baseUrl = process.env.AUDIT_BASE_URL || "http://localhost:3000";
const outputDir = path.join(process.cwd(), "output", "playwright");
const artifactPath = path.join(outputDir, "audit-results.json");

const checks = [];
const consoleMessages = [];
const pageErrors = [];
let devServerProcess;

const requiredRoutes = [
  "/",
  "/speaking",
  "/leadership",
  "/inclusion",
  "/mentorship",
  "/athlete-coaching",
  "/about",
  "/media",
  "/recognition",
  "/books",
  "/impact",
  "/programs",
  "/events",
  "/blog",
  "/blog/embrace-new-beginnings",
  "/speaker-kit",
  "/book",
];

const speakerKitItems = [
  "short-bio",
  "long-bio",
  "speaker-one-sheet",
  "headshots",
  "topic-sheet",
  "intro-script",
  "av-requirements",
  "logo-pack",
];

function record(id, status, message, details = {}) {
  checks.push({
    id,
    status,
    message,
    ...details,
  });
}

function isSameOriginUrl(value) {
  try {
    return new URL(value, baseUrl).origin === new URL(baseUrl).origin;
  } catch {
    return false;
  }
}

async function canReach(url) {
  try {
    await fetch(url, { method: "HEAD" });
    return true;
  } catch {
    return false;
  }
}

async function ensureServer() {
  if (await canReach(baseUrl)) {
    return;
  }

  if (process.env.AUDIT_BASE_URL) {
    throw new Error(`AUDIT_BASE_URL is not reachable: ${baseUrl}`);
  }

  const url = new URL(baseUrl);
  const command = `npm run dev -- --hostname ${url.hostname} --port ${url.port || "3000"}`;
  devServerProcess = spawn(command, {
    cwd: process.cwd(),
    env: { ...process.env, NEXT_TELEMETRY_DISABLED: "1" },
    shell: true,
    stdio: ["ignore", "ignore", "ignore"],
  });

  const startedAt = Date.now();
  while (Date.now() - startedAt < 120_000) {
    if (await canReach(baseUrl)) {
      return;
    }
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }

  throw new Error(`Timed out waiting for dev server at ${baseUrl}`);
}

async function visibleText(locator) {
  try {
    return (await locator.innerText({ timeout: 1000 })).trim();
  } catch {
    return "";
  }
}

async function collectOverflow(page) {
  return page.evaluate(() => {
    const viewport = window.innerWidth;
    const offenders = Array.from(document.querySelectorAll("body *"))
      .map((element) => {
        const rect = element.getBoundingClientRect();
        return {
          tag: element.tagName.toLowerCase(),
          id: element.id || "",
          className:
            typeof element.className === "string"
              ? element.className
              : "",
          text: (element.textContent || "").trim().slice(0, 80),
          left: Math.round(rect.left),
          right: Math.round(rect.right),
          width: Math.round(rect.width),
        };
      })
      .filter((item) => item.width > 0 && (item.left < -1 || item.right > viewport + 1))
      .slice(0, 8);

    return {
      viewport,
      doc: document.documentElement.scrollWidth,
      body: document.body.scrollWidth,
      offenders,
    };
  });
}

async function checkRoute(page, routePath) {
  const response = await page.goto(new URL(routePath, baseUrl).href, {
    waitUntil: "networkidle",
  });

  record(
    `route:${routePath}`,
    response && response.status() < 400 ? "pass" : "fail",
    response
      ? `${routePath} returned HTTP ${response.status()}`
      : `${routePath} did not return a browser response`,
  );

  const bodyText = await visibleText(page.locator("body"));
  record(
    `content:${routePath}`,
    /Lornette\s+Daye/i.test(bodyText) ? "pass" : "fail",
    /Lornette\s+Daye/i.test(bodyText)
      ? "Lornette Daye brand content is present"
      : "Lornette Daye brand content is missing from the page",
  );

  const overflow = await collectOverflow(page);
  record(
    `overflow:${routePath}:${page.viewportSize().width}`,
    overflow.doc <= overflow.viewport + 1 && overflow.body <= overflow.viewport + 1
      ? "pass"
      : "fail",
    `Horizontal overflow check: viewport=${overflow.viewport}, document=${overflow.doc}, body=${overflow.body}`,
    { overflow },
  );
}

async function checkRoutes(page) {
  for (const routePath of requiredRoutes) {
    await page.setViewportSize({ width: 1280, height: 900 });
    await checkRoute(page, routePath);

    await page.setViewportSize({ width: 390, height: 844 });
    await checkRoute(page, routePath);
  }
}

async function checkNav(page) {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(baseUrl, { waitUntil: "networkidle" });

  const navLinks = await page
    .locator("header a, nav a")
    .evaluateAll((links) =>
      links.map((link) => ({
        text: link.textContent.trim(),
        href: link.getAttribute("href"),
      })),
    )
    .catch(() => []);

  record(
    "nav:present",
    navLinks.length >= 4 ? "pass" : "fail",
    navLinks.length
      ? `Found ${navLinks.length} header/nav links`
      : "No header or nav links found",
    { navLinks },
  );

  for (const label of [
    "Home",
    "Speaker",
    "Leadership",
    "Books",
    "Mentorship",
    "About",
    "Media",
    "Blog",
    "Book Lornette",
  ]) {
    const found = navLinks.some((link) => new RegExp(label, "i").test(link.text));
    record(
      `nav:item:${label.toLowerCase()}`,
      found ? "pass" : "fail",
      found ? `Navigation includes ${label}` : `Navigation is missing ${label}`,
    );
  }

  for (const link of navLinks) {
    if (!link.href || !isSameOriginUrl(link.href)) {
      continue;
    }

    const url = new URL(link.href, baseUrl);
    if (url.hash && url.pathname === new URL(baseUrl).pathname) {
      const targetExists = await page.locator(url.hash).count().catch(() => 0);
      record(
        `nav:anchor:${url.hash}`,
        targetExists > 0 ? "pass" : "fail",
        targetExists > 0
          ? `Anchor target ${url.hash} exists`
          : `Anchor target ${url.hash} is missing`,
      );
      continue;
    }

    if (!url.hash) {
      const response = await page.request.get(url.href, { maxRedirects: 3 });
      record(
        `nav:path:${url.pathname}`,
        response.status() < 400 ? "pass" : "fail",
        `${url.pathname} returned HTTP ${response.status()}`,
      );
    }
  }
}

async function checkMobileMenu(page) {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(baseUrl, { waitUntil: "networkidle" });

  const menuButton = page
    .locator("header button, nav button, header summary, nav summary, [data-mobile-menu-trigger]")
    .filter({ hasText: /menu|navigation|open/i })
    .or(
      page.locator(
        "header button[aria-label*='menu' i], nav button[aria-label*='menu' i], header summary[aria-label*='menu' i], nav summary[aria-label*='menu' i], header button[aria-controls*='menu' i], nav button[aria-controls*='menu' i]",
      ),
    )
    .first();
  const hasMenuButton = (await menuButton.count()) > 0;
  record(
    "mobile-menu:button",
    hasMenuButton ? "pass" : "fail",
    hasMenuButton ? "Mobile menu button is present" : "Mobile menu button is missing",
  );

  if (!hasMenuButton) {
    return;
  }

  try {
    await menuButton.click({ timeout: 5000 });
  } catch (error) {
    record(
      "mobile-menu:click",
      "fail",
      `Mobile menu button could not be clicked: ${error.message}`,
    );
    return;
  }
  const visibleNavItems = await page
    .locator("nav a:visible, [role='dialog'] a:visible, [data-mobile-menu] a:visible")
    .count();
  record(
    "mobile-menu:opens",
    visibleNavItems >= 3 ? "pass" : "fail",
    visibleNavItems >= 3
      ? `Mobile menu opened with ${visibleNavItems} visible links`
      : "Mobile menu did not reveal expected navigation links",
  );

  const mobileMenuLinks = page.locator("[data-mobile-menu] a:visible");
  const mobileMenuLinkCount = await mobileMenuLinks.count().catch(() => 0);
  record(
    "mobile-menu:link-count",
    mobileMenuLinkCount === 9 ? "pass" : "fail",
    mobileMenuLinkCount === 9
      ? "Mobile menu exposes 9 navigation links"
      : `Expected 9 mobile navigation links, found ${mobileMenuLinkCount}`,
  );

  const speakerLink = page.getByRole("link", { name: /^Speaker$/i }).first();
  if ((await speakerLink.count()) > 0) {
    await speakerLink.click();
    await page.waitForURL(new RegExp("/speaking$"), { timeout: 5000 }).catch(() => {});
    record(
      "mobile-menu:navigate",
      page.url().endsWith("/speaking") ? "pass" : "fail",
      page.url().endsWith("/speaking")
        ? "Mobile menu link navigates to /speaking"
        : `Mobile menu link did not navigate as expected; current URL is ${page.url()}`,
    );
  } else {
    record(
      "mobile-menu:navigate",
      "fail",
      "Mobile menu is missing the Speaker link",
    );
  }

  await page.keyboard.press("Escape");
}

async function checkVideoModal(page) {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(new URL("/media", baseUrl).href, { waitUntil: "networkidle" });

  const trigger = page
    .getByRole("button", { name: /watch|video|reel|play/i })
    .or(page.getByRole("link", { name: /watch|video|reel|play/i }))
    .first();
  const hasTrigger = (await trigger.count()) > 0;
  record(
    "video:trigger",
    hasTrigger ? "pass" : "fail",
    hasTrigger ? "Video/reel trigger is present" : "Video/reel trigger is missing",
  );

  if (!hasTrigger) {
    return;
  }

  await trigger.click();
  const modalSurface = page.locator("[role='dialog'], video:visible, iframe:visible");
  const modalVisible = (await modalSurface.count()) > 0;
  record(
    "video:modal",
    modalVisible ? "pass" : "fail",
    modalVisible
      ? "Video modal or player is visible after trigger"
      : "Video trigger did not open a visible modal/player",
  );

  await page.keyboard.press("Escape");
  const dialogRemaining = await page.locator("[role='dialog']:visible").count();
  record(
    "video:escape-closes",
    dialogRemaining === 0 ? "pass" : "fail",
    dialogRemaining === 0
      ? "Escape closes the visible video modal"
      : "Video modal remained visible after Escape",
  );
}

async function checkBooking(page) {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.route("**/api/inquiry", async (route) => {
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        ok: false,
        fallbackRequired: true,
        message: "Email delivery is not configured. Please use the prepared mailto fallback.",
      }),
    });
  });
  await page.goto(new URL("/book", baseUrl).href, { waitUntil: "networkidle" });

  const forms = page.locator("form");
  const formCount = await forms.count();
  const fallbackLinks = await page
    .locator("a[href^='mailto:'], a[href^='tel:'], a[href*='calendly'], a[href*='booking']")
    .evaluateAll((links) => links.map((link) => link.getAttribute("href")))
    .catch(() => []);

  record(
    "booking:surface",
    formCount > 0 || fallbackLinks.length > 0 ? "pass" : "fail",
    formCount > 0
      ? `Found ${formCount} booking/contact form(s)`
      : fallbackLinks.length > 0
        ? `Found ${fallbackLinks.length} booking fallback link(s)`
        : "No booking form or fallback contact link found",
    { fallbackLinks },
  );

  if (formCount === 0) {
    return;
  }

  const form = forms.first();
  const submit = form
    .locator("button[type='submit'], input[type='submit'], button:not([type])")
    .first();
  await submit.click();
  await page.waitForTimeout(500);

  const invalidFields = await form.locator(":invalid").count().catch(() => 0);
  const validationText = await visibleText(
    page
      .locator("[role='alert'], [aria-live], .error, .field-error")
      .filter({ hasText: /.+/ })
      .first(),
  );
  record(
    "booking:validation",
    invalidFields > 0 || validationText.length > 0 ? "pass" : "fail",
    invalidFields > 0 || validationText.length > 0
      ? "Empty booking form exposes validation feedback"
      : "Empty booking form submission did not expose validation feedback",
    { invalidFields, validationText },
  );

  await form.getByLabel(/full name/i).fill("Audit Tester");
  await form.getByLabel(/^email$/i).fill("audit@example.com");
  await form.getByLabel(/organization/i).fill("Audit Organization");
  await form.getByLabel(/event type/i).selectOption({ label: "Keynote" });
  await form.getByLabel(/event location/i).selectOption({ label: "Virtual" });
  await form.getByLabel(/audience size/i).fill("150");
  await form.getByLabel(/keynotes & speaking/i).check();
  await form.getByLabel(/event goals/i).fill(
    "Audit submission checks that the booking form falls back to a prepared email.",
  );
  await form.getByLabel(/I consent/i).check();
  await submit.click();

  const fallbackLink = form.locator("a[href^='mailto:']").first();
  await fallbackLink.waitFor({ state: "visible", timeout: 5000 }).catch(() => {});
  const fallbackHref = (await fallbackLink.getAttribute("href").catch(() => "")) ?? "";
  record(
    "booking:fallback",
    fallbackHref.includes("mailto:") && fallbackHref.includes("audit%40example.com")
      ? "pass"
      : "fail",
    fallbackHref
      ? "Valid booking submission exposes a prepared mailto fallback when delivery is unavailable"
      : "Valid booking submission did not expose the mailto fallback",
    { fallbackHref },
  );
  await page.unroute("**/api/inquiry");
}

async function checkDownloads(page) {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(new URL("/speaker-kit", baseUrl).href, { waitUntil: "networkidle" });

  for (const id of speakerKitItems) {
    const anchorCount = await page.locator(`#${id}`).count();
    record(
      `speaker-kit:anchor:${id}`,
      anchorCount === 1 ? "pass" : "fail",
      anchorCount === 1
        ? `Speaker kit section #${id} exists`
        : `Speaker kit section #${id} is missing or duplicated`,
    );
  }

  const downloads = await page
    .locator(
      "a[download], a[href$='.pdf'], a[href$='.doc'], a[href$='.docx'], a[href$='.zip'], a[href$='.html']",
    )
    .evaluateAll((links) =>
      links.map((link) => ({
        text: link.textContent.trim(),
        href: link.href,
        download: link.getAttribute("download"),
      })),
    )
    .catch(() => []);

  record(
    "downloads:present",
    downloads.length >= speakerKitItems.length ? "pass" : "fail",
    downloads.length >= speakerKitItems.length
      ? `Found ${downloads.length} sample downloadable speaker-kit asset(s)`
      : `Expected at least ${speakerKitItems.length} sample downloads, found ${downloads.length}`,
    { downloads },
  );

  for (const download of downloads) {
    if (!download.href || !isSameOriginUrl(download.href)) {
      continue;
    }

    const response = await page.request.head(download.href, { maxRedirects: 3 });
    record(
      `downloads:asset:${path.basename(new URL(download.href).pathname)}`,
      response.status() < 400 ? "pass" : "fail",
      `${download.href} returned HTTP ${response.status()}`,
    );
  }

  await page.goto(new URL("/media", baseUrl).href, { waitUntil: "networkidle" });
  const kitLinks = await page
    .locator("a[href^='/speaker-kit']")
    .evaluateAll((links) =>
      links.map((link) => ({
        text: link.textContent.trim(),
        href: link.getAttribute("href"),
      })),
    )
    .catch(() => []);

  record(
    "speaker-kit:media-links",
    kitLinks.length >= 4 ? "pass" : "fail",
    kitLinks.length >= 4
      ? `Media page exposes ${kitLinks.length} speaker-kit resource links`
      : "Media page does not expose the expected speaker-kit resource links",
    { kitLinks },
  );

}

async function main() {
  await ensureServer();
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on("console", (msg) => {
    if (msg.type() === "error") {
      consoleMessages.push(msg.text());
    }
  });
  page.on("pageerror", (error) => pageErrors.push(error.message));

  try {
    await checkRoutes(page);
    await checkNav(page);
    await checkMobileMenu(page);
    await checkVideoModal(page);
    await checkBooking(page);
    await checkDownloads(page);

    record(
      "console:errors",
      consoleMessages.length === 0 && pageErrors.length === 0 ? "pass" : "fail",
      consoleMessages.length === 0 && pageErrors.length === 0
        ? "No console errors or page errors captured"
        : "Console errors or page errors were captured",
      { consoleMessages, pageErrors },
    );
  } finally {
    await browser.close();
  }

  fs.mkdirSync(outputDir, { recursive: true });
  const summary = {
    baseUrl,
    generatedAt: new Date().toISOString(),
    counts: {
      pass: checks.filter((check) => check.status === "pass").length,
      fail: checks.filter((check) => check.status === "fail").length,
      warn: checks.filter((check) => check.status === "warn").length,
    },
    checks,
  };
  fs.writeFileSync(artifactPath, `${JSON.stringify(summary, null, 2)}\n`);

  for (const check of checks) {
    const marker = check.status === "pass" ? "PASS" : check.status === "warn" ? "WARN" : "FAIL";
    console.log(`${marker} ${check.id}: ${check.message}`);
  }
  console.log(`\nWrote ${artifactPath}`);

  if (summary.counts.fail > 0) {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
}).finally(() => {
  if (devServerProcess && !devServerProcess.killed) {
    devServerProcess.kill();
  }
});
