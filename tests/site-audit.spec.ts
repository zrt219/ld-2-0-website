import { expect, test, type Locator, type Page } from "@playwright/test";

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
  "/collection",
  "/impact",
  "/programs",
  "/events",
  "/blog",
  "/blog/embrace-new-beginnings",
  "/speaker-kit",
  "/book",
  "/foundations",
  "/foundations/golf",
  "/foundations/golf/keynote",
  "/foundations/golf/workshop",
  "/foundations/golf/program",
  "/foundations/golf/club-partnership",
  "/foundations/golf/register",
  "/foundations/clubs",
  "/foundations/performance-edge",
  "/foundations/login",
  "/foundations/dashboard",
  "/foundations/lessons",
  "/foundations/progress",
  "/foundations/resources",
  "/foundations/plan",
  "/foundations/account",
  "/foundations/admin",
  "/foundations/club",
];

const speakerKitItems = [
  "short-bio",
  "long-bio",
  "speaker-one-sheet",
  "av-requirements",
];

async function expectNoHorizontalOverflow(page: Page) {
  const overflow = await page.evaluate(() => ({
    viewport: window.innerWidth,
    doc: document.documentElement.scrollWidth,
    body: document.body.scrollWidth,
  }));

  expect(overflow.doc, `document overflows viewport: ${JSON.stringify(overflow)}`).toBeLessThanOrEqual(
    overflow.viewport + 1,
  );
  expect(overflow.body, `body overflows viewport: ${JSON.stringify(overflow)}`).toBeLessThanOrEqual(
    overflow.viewport + 1,
  );
}

async function submitEmptyForm(form: Locator) {
  await form.locator("button[type='submit'], input[type='submit'], button:not([type])").first().click();
}

test.describe("site route audit", () => {
  for (const route of requiredRoutes) {
    test(`${route} loads and avoids horizontal overflow`, async ({ page }) => {
      for (const viewport of [
        { width: 1280, height: 900 },
        { width: 390, height: 844 },
      ]) {
        await page.setViewportSize(viewport);
        const response = await page.goto(route, { waitUntil: "domcontentloaded" });

        expect(response?.status(), `${route} returned an unhealthy status`).toBeLessThan(400);
        await expect(page.locator("body")).toContainText(/Lornette\s+Daye/i);
        await expectNoHorizontalOverflow(page);
      }
    });
  }
});

test("mobile navigation opens, expands submenus, and navigates", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/");
  await page.locator("header[data-hydrated='true']").waitFor();

  const menuButton = page.getByRole("button", { name: /open navigation menu/i });
  await expect(menuButton).toBeVisible();
  await menuButton.click();
  await page.waitForTimeout(350);

  await expect(page.locator("[data-mobile-menu]")).toBeVisible();
  await expect(page.locator("[data-mobile-menu] a")).toHaveCount(13);

  // Check Foundations sub-links in mobile menu (only true child destinations, no redundant root link)
  await expect(page.locator("[data-mobile-menu]").getByRole("link", { name: /^Lornette’s Foundation$/i })).toHaveCount(0);
  await expect(page.locator("[data-mobile-menu]").getByRole("link", { name: /^Golf$/i })).toBeVisible();
  await expect(page.locator("[data-mobile-menu]").getByRole("link", { name: /^For Clubs & Teams$/i })).toBeVisible();
  await expect(page.locator("[data-mobile-menu]").getByRole("link", { name: /^Performance Edge Framework$/i })).toBeVisible();

  // Check Books sub-links in mobile menu (only true child destinations, no redundant root link)
  await expect(page.locator("#mobile-books-submenu").getByRole("link", { name: /^Books$/i })).toHaveCount(0);
  await expect(page.locator("[data-mobile-menu]").getByRole("link", { name: /^Collection$/i })).toBeVisible();

  // Test navigation
  await page.locator("[data-mobile-menu]").getByRole("link", { name: /^Speaker$/i }).click();
  await expect(page).toHaveURL(/\/speaking$/, { timeout: 10000 });

  // Test Escape key closes mobile menu and restores focus
  const speakerMenuBtn = page.getByRole("button", { name: /open navigation menu/i });
  await speakerMenuBtn.click();
  await expect(page.locator("[data-mobile-menu]")).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(page.locator("[data-mobile-menu]")).toBeHidden();
  await expect(speakerMenuBtn).toBeFocused();
});

test("desktop split navigation opens submenu with disclosure button and keyboard", async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto("/");
  await page.locator("header[data-hydrated='true']").waitFor();

  const nav = page.getByLabel("Primary navigation");
  const foundationsLink = nav.getByRole("link", { name: /^Foundations$/i });
  await expect(foundationsLink).toBeVisible();

  const foundationsMenuBtn = nav.getByRole("button", { name: /foundations menu/i });
  await expect(foundationsMenuBtn).toBeVisible();
  await expect(foundationsMenuBtn).toHaveAttribute("aria-expanded", "false");

  // Measure layout before opening
  const bodyHeightBefore = await page.evaluate(() => document.body.scrollHeight);
  const foundationsLinkBox = await foundationsLink.boundingBox();
  const foundationsMenuBtnBox = await foundationsMenuBtn.boundingBox();
  expect(foundationsLinkBox).not.toBeNull();
  expect(foundationsMenuBtnBox).not.toBeNull();
  // Verify chevron is optically aligned with text link vertical center
  expect(Math.abs((foundationsMenuBtnBox!.y + foundationsMenuBtnBox!.height / 2) - (foundationsLinkBox!.y + foundationsLinkBox!.height / 2))).toBeLessThanOrEqual(1);

  // Click disclosure button to open submenu
  await foundationsMenuBtn.click();
  await expect(foundationsMenuBtn).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#foundations-submenu")).toBeVisible();
  await page.waitForTimeout(200); // allow motion transition to settle

  const flyoutUl = page.locator("#foundations-submenu ul");
  const flyoutBox = await flyoutUl.boundingBox();
  expect(flyoutBox).not.toBeNull();
  // Verify dropdown width is compact (220-245px)
  expect(flyoutBox!.width).toBeGreaterThanOrEqual(220);
  expect(flyoutBox!.width).toBeLessThanOrEqual(245);

  // Verify dropdown begins 12-16px below the trigger/underline
  const gapUnderline = flyoutBox!.y - (foundationsLinkBox!.y + foundationsLinkBox!.height);
  expect(gapUnderline).toBeGreaterThanOrEqual(12);
  expect(gapUnderline).toBeLessThanOrEqual(16);

  // Verify row heights are between 40-44px
  const foundationsRows = page.locator("#foundations-submenu li");
  const rowCount = await foundationsRows.count();
  expect(rowCount).toBe(3);
  for (let i = 0; i < rowCount; i++) {
    const rowBox = await foundationsRows.nth(i).boundingBox();
    expect(rowBox!.height).toBeGreaterThanOrEqual(40);
    expect(rowBox!.height).toBeLessThanOrEqual(44);
  }

  // Verify zero layout shift
  const bodyHeightAfter = await page.evaluate(() => document.body.scrollHeight);
  expect(bodyHeightAfter - bodyHeightBefore).toBe(0);

  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^Golf$/i })).toBeVisible();
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^For Clubs & Teams$/i })).toBeVisible();
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^Performance Edge Framework$/i })).toBeVisible();
  // Ensure redundant parent link is NOT present in submenu
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^Lornette’s Foundation$/i })).toHaveCount(0);

  // Test keyboard escape closes submenu
  await page.keyboard.press("Escape");
  await expect(foundationsMenuBtn).toHaveAttribute("aria-expanded", "false");
  await expect(page.locator("#foundations-submenu")).toBeHidden();

  // Test Books split navigation
  const booksLink = nav.getByRole("link", { name: /^Books$/i });
  await expect(booksLink).toBeVisible();
  const booksLinkBox = await booksLink.boundingBox();

  const booksMenuBtn = nav.getByRole("button", { name: /books menu/i });
  await expect(booksMenuBtn).toBeVisible();
  await expect(booksMenuBtn).toHaveAttribute("aria-expanded", "false");

  // Click disclosure button to open Books submenu
  await booksMenuBtn.click();
  await expect(booksMenuBtn).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#books-submenu")).toBeVisible();
  await page.waitForTimeout(200);

  const booksFlyoutBox = await page.locator("#books-submenu ul").boundingBox();
  expect(booksFlyoutBox).not.toBeNull();
  expect(booksFlyoutBox!.width).toBeGreaterThanOrEqual(220);
  expect(booksFlyoutBox!.width).toBeLessThanOrEqual(245);
  const booksGapUnderline = booksFlyoutBox!.y - (booksLinkBox!.y + booksLinkBox!.height);
  expect(booksGapUnderline).toBeGreaterThanOrEqual(12);
  expect(booksGapUnderline).toBeLessThanOrEqual(16);

  await expect(page.locator("#books-submenu").getByRole("link", { name: /^Collection$/i })).toBeVisible();
  // Ensure redundant parent link is NOT present in Books submenu
  await expect(page.locator("#books-submenu").getByRole("link", { name: /^Books$/i })).toHaveCount(0);

  // Test keyboard escape closes Books submenu
  await page.keyboard.press("Escape");
  await expect(booksMenuBtn).toHaveAttribute("aria-expanded", "false");
  await expect(page.locator("#books-submenu")).toBeHidden();

  // Test focus leaving submenu (onBlur/focusout) closes flyout
  await foundationsMenuBtn.click();
  await expect(foundationsMenuBtn).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#foundations-submenu")).toBeVisible();
  // Tab into Golf
  await page.keyboard.press("Tab");
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^Golf$/i })).toBeFocused();
  // Tab into For Clubs & Teams
  await page.keyboard.press("Tab");
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^For Clubs & Teams$/i })).toBeFocused();
  // Tab into Performance Edge Framework
  await page.keyboard.press("Tab");
  await expect(page.locator("#foundations-submenu").getByRole("link", { name: /^Performance Edge Framework$/i })).toBeFocused();
  // Tab past last item into Leadership (next top-level item)
  await page.keyboard.press("Tab");
  await expect(nav.getByRole("link", { name: /^Leadership$/i })).toBeFocused();
  await expect(foundationsMenuBtn).toHaveAttribute("aria-expanded", "false");
  await expect(page.locator("#foundations-submenu")).toBeHidden();
});

test("WCAG 2.2 AA split-link navigation and accessibility audit", async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto("/");
  await page.locator("header[data-hydrated='true']").waitFor();

  const nav = page.getByLabel("Primary navigation");

  // Verify Foundations parent link routes to /foundations
  const foundationsLink = nav.getByRole("link", { name: /^Foundations$/i });
  await expect(foundationsLink).toHaveAttribute("href", "/foundations");

  // Verify disclosure button has valid WCAG 2.2 minimum target size (>= 24x24 px per SC 2.5.8)
  const foundationsBtn = nav.getByRole("button", { name: /foundations menu/i });
  const btnBox = await foundationsBtn.boundingBox();
  expect(btnBox).not.toBeNull();
  expect(btnBox!.width).toBeGreaterThanOrEqual(24);
  expect(btnBox!.height).toBeGreaterThanOrEqual(24);

  // Verify aria-controls references the submenu id
  const controlsId = await foundationsBtn.getAttribute("aria-controls");
  expect(controlsId).toBe("foundations-submenu");

  // Open submenu
  await foundationsBtn.click();
  await expect(foundationsBtn).toHaveAttribute("aria-expanded", "true");
  const submenu = page.locator(`#${controlsId}`);
  await expect(submenu).toBeVisible();

  // Verify Foundations submenu contains ONLY Golf, For Clubs & Teams, Performance Edge Framework
  const submenuLinks = submenu.getByRole("link");
  await expect(submenuLinks).toHaveCount(3);
  await expect(submenuLinks.nth(0)).toHaveText("Golf");
  await expect(submenuLinks.nth(0)).toHaveAttribute("href", "/foundations/golf");
  await expect(submenuLinks.nth(1)).toHaveText("For Clubs & Teams");
  await expect(submenuLinks.nth(1)).toHaveAttribute("href", "/foundations/clubs");
  await expect(submenuLinks.nth(2)).toHaveText("Performance Edge Framework");
  await expect(submenuLinks.nth(2)).toHaveAttribute("href", "/foundations/performance-edge");

  // Verify Books parent link and submenu
  const booksBtn = nav.getByRole("button", { name: /books menu/i });
  const booksControlsId = await booksBtn.getAttribute("aria-controls");
  expect(booksControlsId).toBe("books-submenu");

  const booksBtnBox = await booksBtn.boundingBox();
  expect(booksBtnBox).not.toBeNull();
  expect(booksBtnBox!.width).toBeGreaterThanOrEqual(24);
  expect(booksBtnBox!.height).toBeGreaterThanOrEqual(24);

  await booksBtn.click();
  await expect(booksBtn).toHaveAttribute("aria-expanded", "true");
  const booksSubmenu = page.locator(`#${booksControlsId}`);
  await expect(booksSubmenu).toBeVisible();

  // Verify Books submenu contains ONLY Collection
  const booksSubLinks = booksSubmenu.getByRole("link");
  await expect(booksSubLinks).toHaveCount(1);
  await expect(booksSubLinks.first()).toHaveText("Collection");
  await expect(booksSubLinks.first()).toHaveAttribute("href", "/collection");

  // Verify clicking parent link directly navigates to /foundations
  await foundationsLink.click();
  await expect(page).toHaveURL(/\/foundations$/, { timeout: 10000 });
});

test("foundations submenu active states correctly isolate active subpath", async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto("/foundations/golf");
  await page.locator("header[data-hydrated='true']").waitFor();

  const nav = page.getByLabel("Primary navigation");
  const foundationsLink = nav.getByRole("link", { name: /^Foundations$/i });
  await expect(foundationsLink).toHaveAttribute("aria-current", "page");

  const foundationsMenuBtn = nav.getByRole("button", { name: /foundations menu/i });
  await foundationsMenuBtn.click();
  await expect(page.locator("#foundations-submenu")).toBeVisible();

  // "Golf" must be active
  const golfSubLink = page.locator("#foundations-submenu").getByRole("link", { name: /^Golf$/i });
  await expect(golfSubLink).toHaveAttribute("aria-current", "page");

  // Siblings must not be active
  const clubsSubLink = page.locator("#foundations-submenu").getByRole("link", { name: /^For Clubs & Teams$/i });
  await expect(clubsSubLink).not.toHaveAttribute("aria-current", "page");
});

test("foundations secondary subnav collapses and expands on mobile", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/foundations");
  await page.locator("nav[data-hydrated='true']").waitFor();

  const subNav = page.getByLabel("Foundations section navigation");
  await expect(subNav).toBeVisible();

  // On mobile, the subnav displays active section label
  await expect(subNav.getByText(/Foundations \//i)).toBeVisible();
  await expect(subNav.locator("span", { hasText: /^Overview$/i })).toBeVisible();

  // Expand mobile subnav
  const toggleBtn = subNav.getByRole("button", { name: /foundations section menu/i });
  await expect(toggleBtn).toBeVisible();
  await expect(toggleBtn).toHaveAttribute("aria-expanded", "false");

  await toggleBtn.click();
  await expect(toggleBtn).toHaveAttribute("aria-expanded", "true");
  await expect(subNav.locator("#foundations-mobile-subnav")).toBeVisible();

  // Navigate to Golf via mobile subnav
  await subNav.locator("#foundations-mobile-subnav").getByRole("link", { name: /^Golf$/i }).click();
  await expect(page).toHaveURL(/\/foundations\/golf$/, { timeout: 10000 });
  await page.locator("nav[data-hydrated='true']").waitFor();
  await expect(subNav.locator("span", { hasText: /^Golf$/i })).toBeVisible();

  // Test Escape key closes mobile subnav and restores focus
  const golfToggleBtn = subNav.getByRole("button", { name: /foundations section menu/i });
  await golfToggleBtn.click();
  await expect(golfToggleBtn).toHaveAttribute("aria-expanded", "true");
  await expect(subNav.locator("#foundations-mobile-subnav")).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(golfToggleBtn).toHaveAttribute("aria-expanded", "false");
  await expect(subNav.locator("#foundations-mobile-subnav")).toBeHidden();
  await expect(golfToggleBtn).toBeFocused();
});

test("foundations secondary subnav desktop golf dropdown opens and navigates", async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto("/foundations");
  await page.locator("nav[data-hydrated='true']").waitFor();

  const subNav = page.getByLabel("Foundations section navigation");
  const golfDisclosureBtn = subNav.getByRole("button", { name: /golf subpages menu/i });
  await expect(golfDisclosureBtn).toBeVisible();
  await expect(golfDisclosureBtn).toHaveAttribute("aria-expanded", "false");

  // Click disclosure to open dropdown
  await golfDisclosureBtn.click();
  await expect(golfDisclosureBtn).toHaveAttribute("aria-expanded", "true");
  const dropdown = subNav.locator("#foundations-golf-submenu");
  await expect(dropdown).toBeVisible();

  // Verify links inside dropdown
  await expect(dropdown.getByRole("link", { name: /keynote experience/i })).toHaveAttribute(
    "href",
    "/foundations/golf/keynote",
  );
  await expect(dropdown.getByRole("link", { name: /member clinic & workshop/i })).toHaveAttribute(
    "href",
    "/foundations/golf/workshop",
  );
  await expect(dropdown.getByRole("link", { name: /10-week guided program/i })).toHaveAttribute(
    "href",
    "/foundations/golf/program",
  );
  await expect(dropdown.getByRole("link", { name: /club partnership/i })).toHaveAttribute(
    "href",
    "/foundations/golf/club-partnership",
  );

  // Press Escape to close dropdown and restore focus
  await page.keyboard.press("Escape");
  await expect(golfDisclosureBtn).toHaveAttribute("aria-expanded", "false");
  await expect(dropdown).toBeHidden();
  await expect(golfDisclosureBtn).toBeFocused();
});

test("media video modal opens and closes from the keyboard", async ({ page }) => {
  await page.goto("/media");
  await page.locator("article[data-hydrated='true']").first().waitFor();

  await page.getByRole("button", { name: /play speaker reel/i }).first().click();
  await expect(page.getByRole("dialog", { name: /speaker reel/i })).toBeVisible();
  await expect(page.locator("video[controls]")).toBeVisible();

  await page.keyboard.press("Escape");
  await expect(page.getByRole("dialog", { name: /speaker reel/i })).toBeHidden();
});

test("booking form validates empty submission and exposes mailto fallback", async ({ page }) => {
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

  await page.goto("/book");
  const form = page.locator("form[data-hydrated='true']");
  await form.waitFor();

  await submitEmptyForm(form);
  await expect(page.locator("[aria-live]").filter({ hasText: /correct the highlighted fields/i })).toBeVisible();
  await expect(page.getByText(/Please enter your full name/i)).toBeVisible();
  await expect(page.getByText(/Please select at least one topic/i)).toBeVisible();

  await form.getByLabel(/full name/i).fill("Audit Tester");
  await form.getByLabel(/^email$/i).fill("audit@example.com");
  await form.getByLabel(/organization/i).fill("Audit Organization");
  await form.getByLabel(/event type/i).selectOption({ label: "Keynote" });
  await form.getByLabel(/event location/i).selectOption({ label: "Virtual" });
  await form.getByLabel(/audience size/i).fill("150");
  await form.getByLabel(/keynotes & speaking/i).check();
  await form.getByLabel(/event goals/i).fill(
    "Audit submission checks that fallback booking email is available for delivery failures.",
  );
  await form.getByLabel(/I consent/i).check();
  await form.getByRole("button", { name: /^inquire$/i }).click();

  const fallback = page.getByRole("link", { name: /open prepared email/i });
  await expect(fallback).toBeVisible();
  await expect(fallback).toHaveAttribute("href", /mailto:.*audit%40example\.com/);
});

test("speaker kit resources are addressable from kit and media pages", async ({ page }) => {
  await page.goto("/speaker-kit", { waitUntil: "domcontentloaded" });

  for (const id of speakerKitItems) {
    await expect(page.locator(`#${id}`), `missing speaker kit anchor #${id}`).toHaveCount(1);
  }

  const downloads = page.locator("a[download]");
  await expect(downloads).toHaveCount(3);
  for (const item of ["lornette-short-bio.pdf", "lornette-long-bio.pdf", "av-requirements-sample.html"]) {
    const response = await page.request.get(`/speaker-kit/${item}`);
    expect(response.status(), `${item} download should resolve`).toBeLessThan(400);
  }

  await page.goto("/media", { waitUntil: "domcontentloaded" });
  const resourceLinks = page.locator("a[href^='/speaker-kit']");
  await expect.poll(async () => resourceLinks.count()).toBeGreaterThanOrEqual(4);
});

test.describe("foundations visual assets verification", () => {
  test("/foundations loads all 4 editorial and showcase images with verified hydration", async ({ page }) => {
    await page.goto("/foundations");
    
    // Check that Turkey sports poster is NOT in DOM
    const turkeyImg = page.locator("img[src*='one-flag-one-journey-vision-for-sport.jpg']");
    await expect(turkeyImg).toHaveCount(0);

    const editorialImages = [
      "lornette-foundations-grand-staircase.png",
      "lornette-foundations-stadium-tunnel.png",
      "lornette-golf-fairway-mountain-sunset.png",
      "lornette-foundations-academy-hallway.png",
      "lornette-foundations-outdoor-track-sunrise.png",
    ];

    for (const imgName of editorialImages) {
      const locator = page.locator(`img[src*='${imgName}']`);
      await expect(locator).toHaveCount(1);
      await locator.scrollIntoViewIfNeeded();
      await expect.poll(async () => {
        return locator.evaluate((img: HTMLImageElement) => img.complete && img.naturalWidth > 0);
      }, { timeout: 10000 }).toBe(true);
    }
  });

  test("/foundations satisfies all 7 editorial sections, semantic headings, and valid routes", async ({ page }) => {
    await page.goto("/foundations");

    // 1. Hero section
    await expect(page.locator("h1")).toHaveText("Lornette’s Foundation");
    await expect(page.getByRole("link", { name: /explore the athlete program/i })).toHaveAttribute("href", "/foundations/golf");
    await expect(page.getByRole("link", { name: /for clubs & teams/i })).toHaveAttribute("href", "/foundations/clubs");

    // 2. Credibility strip
    const credibilitySection = page.locator("section[aria-label='Foundations credibility statistics']");
    await expect(credibilitySection).toBeVisible();
    await expect(credibilitySection).toContainText("40+");
    await expect(credibilitySection).toContainText("500+");
    await expect(credibilitySection).toContainText("150+");

    // 3. Philosophy section
    await expect(page.getByRole("heading", { name: /develop the athlete\. prepare the person\./i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /stepping into the arena with conviction/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("link", { name: /explore the performance edge framework/i })).toHaveAttribute("href", "/foundations/performance-edge");

    // 4. Flagship Golf Pathway card
    await expect(page.getByRole("heading", { name: /foundation pathways/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /golf performance program/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("link", { name: /explore golf pathway/i }).first()).toHaveAttribute("href", "/foundations/golf");

    // 5. The Performance Edge Framework section
    await expect(page.getByRole("heading", { name: /the performance edge framework/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /eight practical performance tools/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("link", { name: /learn the performance edge framework/i }).first()).toHaveAttribute("href", "/foundations/performance-edge");

    // 6. Clubs & Organizations partnership section
    await expect(page.getByRole("heading", { name: /bring lornette’s foundation to your organization/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("link", { name: /explore club & team partnerships/i })).toHaveAttribute("href", "/foundations/clubs");
    await expect(page.getByRole("heading", { name: /cultivating resilience across the entire roster/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("link", { name: /learn about institutional programs/i })).toHaveAttribute("href", "/foundations/clubs");

    // 7. Closing CTA
    await expect(page.getByRole("heading", { name: /build a stronger athlete\. build a stronger future\./i, level: 2 })).toBeVisible();
    await expect(page.getByRole("link", { name: /explore lornette’s foundation/i })).toHaveAttribute("href", "/foundations/golf");
    await expect(page.getByRole("link", { name: /work with lornette/i })).toHaveAttribute("href", "/book");
  });

  test("/foundations maintains internal card containment without clipping on mobile viewports", async ({ page }) => {
    for (const width of [390, 375]) {
      await page.setViewportSize({ width, height: 844 });
      await page.goto("/foundations");

      // Verify no h3 or article element exceeds viewport bounds
      const violations = await page.evaluate((vpWidth) => {
        const elements = Array.from(document.querySelectorAll("h1, h2, h3, article, .grid > div"));
        return elements
          .map((el) => {
            const rect = el.getBoundingClientRect();
            return { tag: el.tagName, text: el.textContent?.slice(0, 30), right: rect.right, width: rect.width };
          })
          .filter((item) => item.right > vpWidth + 1);
      }, width);

      expect(violations, `elements overflowing viewport on ${width}px: ${JSON.stringify(violations)}`).toHaveLength(0);
    }
  });

  test("/foundations/clubs loads executive desk runner hero and playbook images", async ({ page }) => {
    await page.goto("/foundations/clubs");
    const heroImg = page.locator("img[src*='lornette-foundations-executive-desk-runner.png']");
    await expect(heroImg).toHaveCount(1);
    const playbookImg = page.locator("img[src*='lornette-foundations-tactical-playbook-board.png']");
    await expect(playbookImg).toHaveCount(1);
  });

  test("/foundations/performance-edge loads armchair study hero and curved track images", async ({ page }) => {
    await page.goto("/foundations/performance-edge");
    const heroImg = page.locator("img[src*='lornette-foundations-armchair-study.png']");
    await expect(heroImg).toHaveCount(1);
    const trackImg = page.locator("img[src*='lornette-foundations-curved-track-athletes.png']");
    await expect(trackImg).toHaveCount(1);
  });

  test("/foundations/golf pages load all curated hero and editorial images", async ({ page }) => {
    test.slow();
    await page.goto("/foundations/golf");
    await expect(page.locator("img[src*='lornette-golf-putting-green-sunrise.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='sunlight-golf-dew-flag.jpg']")).toHaveCount(1);
    await expect(page.locator("img[src*='sunlight-golf-fairway-sunrise.jpg']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-simulator-studio-tablet.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-coastal-links-sunrise.jpg']")).toHaveCount(1);

    await page.goto("/foundations/golf/keynote");
    await expect(page.locator("img[src*='lornette-golf-keynote-podium.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-terrace-skyline-view.png']")).toHaveCount(1);

    await page.goto("/foundations/golf/workshop");
    await expect(page.locator("img[src*='lornette-golf-indoor-studio.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-fairway-composure-sunset.jpg']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-indoor-green-notebook.png']")).toHaveCount(1);

    await page.goto("/foundations/golf/program");
    await expect(page.locator("img[src*='lornette-golf-tournament-prep.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-executive-desk.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-fairway-mountain-sunset.png']")).toHaveCount(1);

    await page.goto("/foundations/golf/club-partnership");
    await expect(page.locator("img[src*='lornette-golf-coastal-links.png']")).toHaveCount(1);
    await expect(page.locator("img[src*='lornette-golf-clubhouse-lounge-putter.png']")).toHaveCount(1);
  });

  test("/foundations/golf satisfies CRO, 3-Phase curriculum, and progressive disclosure contracts", async ({ page }) => {
    await page.goto("/foundations/golf");

    // 1. Hero Section & Outcome-Led Headline
    await expect(page.getByRole("heading", { name: /play your best when it matters/i, level: 1 })).toBeVisible();
    await expect(page.getByText(/10-week guided program/i).first()).toBeVisible();
    await expect(page.getByRole("link", { name: /explore the 10-week program/i })).toHaveAttribute("href", "/foundations/golf/program");
    await expect(page.getByRole("link", { name: /for clubs & teams/i }).first()).toHaveAttribute("href", "/foundations/clubs");

    // 2. Credibility Strip
    const credibilitySection = page.locator("section[aria-label='Verified athletic credentials']");
    await expect(credibilitySection).toBeVisible();
    await expect(credibilitySection).toContainText("40+");
    await expect(credibilitySection).toContainText("500+");
    await expect(credibilitySection).toContainText("150+");
    await expect(credibilitySection).toContainText("10");

    // 3. Core Outcomes Section
    await expect(page.getByRole("heading", { name: /what this program helps you build/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /composure under pressure/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /automated pre-shot cadence/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /five-second mistake recovery/i, level: 3 })).toBeVisible();

    // 4. 3-Phase Curriculum Presentation
    await expect(page.getByRole("heading", { name: /the 10-week athlete development journey/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /build your foundation/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /perform & respond/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /build what comes next/i, level: 3 })).toBeVisible();

    // 5. Accessible Progressive Disclosure for All 10 Weeks
    const fullJourneyDetails = page.locator("details", { hasText: /see the full 10-week journey/i });
    await expect(fullJourneyDetails).toBeVisible();
    await expect(fullJourneyDetails).not.toHaveAttribute("open", "");
    await fullJourneyDetails.locator("summary").click();
    await expect(fullJourneyDetails).toHaveAttribute("open", "");
    await expect(fullJourneyDetails.getByRole("heading", { name: /identity beyond sport/i, level: 4 })).toBeVisible();
    await expect(fullJourneyDetails.getByRole("heading", { name: /legacy & community impact/i, level: 4 })).toBeVisible();

    // 6. One Foundation at a Time Rhythm Section
    await expect(page.getByRole("heading", { name: /one foundation at a time/i, level: 2 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /lornette guidance/i, level: 3 })).toBeVisible();
    await expect(page.getByRole("heading", { name: /practical performance tool/i, level: 3 })).toBeVisible();

    // 7. Frequently Asked Questions
    await expect(page.getByRole("heading", { name: /frequently asked questions/i, level: 2 })).toBeVisible();
    const firstFaq = page.locator("details", { hasText: /who is lornette’s foundation.*golf designed for/i });
    await expect(firstFaq).toBeVisible();
    await firstFaq.locator("summary").click();
    await expect(firstFaq).toHaveAttribute("open", "");
    await expect(firstFaq).toContainText(/dedicated competitive golfers/i);
  });

  test("/foundations/golf/register loads fairway image and handles registration submission", async ({ page }) => {
    await page.goto("/foundations/golf/register");
    await expect(page.locator("img[src*='lornette-golf-fairway-composure-sunset.jpg']")).toHaveCount(1);
    await expect(page.getByRole("heading", { name: /join the 10-week guided program/i })).toBeVisible();

    // Fill registration form
    await page.getByPlaceholder(/e\.g\. Taylor/i).fill("Jordan");
    await page.getByPlaceholder(/e\.g\. Morgan/i).fill("Spieth");
    await page.getByPlaceholder(/you@email\.com/i).fill("jordan@example.com");
    await page.getByPlaceholder(/\(555\) 123-4567/i).fill("555-987-6543");
    await page.getByPlaceholder(/e\.g\. Atlanta, GA/i).fill("Dallas, TX");
    await page.locator("select").selectOption("PGA Coach / Pro Recommendation");

    // Submit form
    await page.getByRole("button", { name: /register for the program/i }).click();

    // Verify submission success state and recipient email display
    await expect(page.getByRole("heading", { name: /registration received/i })).toBeVisible({ timeout: 10000 });
    await expect(page.getByText(/lornettedayespeaking@umattr\.ca/i)).toBeVisible();
  });
});

