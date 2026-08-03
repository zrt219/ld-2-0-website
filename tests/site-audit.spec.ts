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

test("mobile navigation opens and navigates", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/");

  const menuButton = page.getByRole("button", { name: /open navigation menu/i });
  await expect(menuButton).toBeVisible();
  await menuButton.click();

  await expect(page.locator("[data-mobile-menu]")).toBeVisible();
  await expect(page.locator("[data-mobile-menu] a")).toHaveCount(9);
  await page.locator("[data-mobile-menu]").getByRole("link", { name: /^Speaker$/i }).click();
  await expect(page).toHaveURL(/\/speaking$/);
});

test("media video modal opens and closes from the keyboard", async ({ page }) => {
  await page.goto("/media", { waitUntil: "domcontentloaded" });

  await page.getByRole("button", { name: /play speaker reel/i }).first().click();
  await expect(page.getByRole("dialog", { name: /speaker reel video/i })).toBeVisible();
  await expect(page.locator("video[controls]")).toBeVisible();

  await page.keyboard.press("Escape");
  await expect(page.getByRole("dialog", { name: /speaker reel video/i })).toBeHidden();
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

  await page.goto("/book", { waitUntil: "domcontentloaded" });
  const form = page.locator("form").first();

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
  await form.getByLabel(/public speaking/i).check();
  await form.getByLabel(/event goals/i).fill(
    "Audit submission checks that fallback booking email is available for delivery failures.",
  );
  await form.getByLabel(/I consent/i).check();
  await form.getByRole("button", { name: /inquire about availability/i }).click();

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
  await expect(downloads).toHaveCount(8);
  for (const item of speakerKitItems) {
    const response = await page.request.get(`/speaker-kit/${item}-sample.html`);
    expect(response.status(), `${item} sample download should resolve`).toBeLessThan(400);
  }

  await page.goto("/media", { waitUntil: "domcontentloaded" });
  const resourceLinks = page.locator("a[href^='/speaker-kit']");
  await expect.poll(async () => resourceLinks.count()).toBeGreaterThanOrEqual(4);
});
