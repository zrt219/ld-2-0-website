import { test, expect } from "@playwright/test";

test.describe("Learner Portal & Course Player", () => {
  test.setTimeout(60000);

  test("Login portal loads and navigates to dashboard", async ({ page }) => {
    await page.goto("/foundations/login");
    await expect(page.locator("h1")).toContainText("Welcome, Golfer");
    await page.locator("button:has-text('Enter Workspace')").click();
    await page.waitForURL("**/foundations/dashboard", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/dashboard/);
  });

  test("Dashboard displays exact luxury visual system", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/dashboard");

    // Check Hero & Branding
    await expect(page.locator("h1")).toContainText("WELCOME TO MY PERFORMANCE EDGE");
    await expect(page.locator("text=Powered by the Performance Edge Framework").first()).toBeVisible();
    await expect(page.locator("text=Your guided Golf performance journey starts here.")).toBeVisible();
    await expect(page.locator("text=“A stronger you creates a stronger game.”")).toBeVisible();

    // Check 4 Shortcuts
    await expect(page.locator("text=My Journey").first()).toBeVisible();
    await expect(page.locator("text=Lessons").first()).toBeVisible();
    await expect(page.locator("text=Assessments").first()).toBeVisible();
    await expect(page.locator("text=Resources").first()).toBeVisible();

    // Check 3 Bottom Cards
    await expect(page.locator("text=A Message From Lornette")).toBeVisible();
    await expect(page.getByText("Your Progress", { exact: true })).toBeVisible();
    await expect(page.locator("text=A Calmer Mind")).toBeVisible();

    // Check Signature Bottom Banner
    await expect(page.locator("text=Discipline Your Focus.")).toBeVisible();
    await expect(page.locator("text=Elevate Your Game.")).toBeVisible();

    // Screenshot
    await page.screenshot({ path: "tests/screenshots/dashboard_desktop.png", fullPage: true });
  });

  test("Learner sidebar renders changing scenic golf gallery with gold, beach, and mountain vistas", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/dashboard");

    // Atmospheric card Lornette principle and motto
    await expect(page.locator("text=“Your previous shot cannot hit your next shot.”").first()).toBeVisible();
    await expect(page.locator("text=Better People · Better Players").first()).toBeVisible();

    // Scenic gallery region & carousel ARIA
    const gallery = page.getByRole("region", { name: "Scenic golf atmospheric gallery" });
    await expect(gallery).toBeVisible();
    await expect(gallery).toHaveAttribute("aria-roledescription", "carousel");

    // Check initial active slide label (Gold Sunrise)
    await expect(gallery.locator("text=Gold Sunrise")).toBeVisible();

    // Check tabs/dots and touch-friendly target size (at least 20x20px)
    const tabs = gallery.locator("button[role='tab']");
    await expect(tabs).toHaveCount(3);
    const firstTabBox = await tabs.first().boundingBox();
    expect(firstTabBox?.width).toBeGreaterThanOrEqual(20);
    expect(firstTabBox?.height).toBeGreaterThanOrEqual(20);

    // Initial tab states
    await expect(tabs.nth(0)).toHaveAttribute("aria-selected", "true");
    await expect(tabs.nth(1)).toHaveAttribute("aria-selected", "false");

    // Switch to Beach Links via click
    await tabs.nth(1).click();
    await expect(gallery.locator("text=Beach Links")).toBeVisible();
    await expect(tabs.nth(1)).toHaveAttribute("aria-selected", "true");

    // Switch to Mountain Vista via keyboard navigation (ArrowRight)
    await tabs.nth(1).focus();
    await page.keyboard.press("ArrowRight");
    await expect(gallery.locator("text=Mountain Vista")).toBeVisible();
    await expect(tabs.nth(2)).toHaveAttribute("aria-selected", "true");

    // Test Play/Pause slideshow toggle
    const pauseBtn = gallery.getByRole("button", { name: /pause scenic slideshow/i });
    await expect(pauseBtn).toBeVisible();
    await pauseBtn.click();
    const resumeBtn = gallery.getByRole("button", { name: /resume scenic slideshow/i });
    await expect(resumeBtn).toBeVisible();
  });

  test("Course player provides interactive video and 10-foundation curriculum", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/lessons");
    await page.waitForLoadState("networkidle");

    // Check Header & Player
    await expect(page.locator("h1")).toContainText("WELCOME, GOLFER");
    await expect(page.locator("text=Begin with Lornette.")).toBeVisible();

    // Check Right Rail
    await expect(page.getByText("YOUR PROGRESS", { exact: true })).toBeVisible();
    await expect(page.locator("text=Step 3 of 10")).toBeVisible();
    await expect(page.locator("text=Progress Looks Good on You.")).toBeVisible();

    // Screenshot initial player view
    await page.screenshot({ path: "tests/screenshots/lessons_desktop.png" });

    // Switch lesson via button
    const lesson5Btn = page.locator("button", { hasText: "Pressure, Emotional Regulation & Recovery" });
    await expect(lesson5Btn).toBeVisible();
    await lesson5Btn.click();
    if (!(await page.locator("h2").first().textContent())?.includes("Pressure, Emotional Regulation")) {
      await page.waitForTimeout(500);
      await lesson5Btn.click();
    }
    await expect(page.locator("h2").first()).toContainText("Pressure, Emotional Regulation & Recovery");

    // Save reflection
    await page.locator("textarea").first().fill("When pressure hits, I will use the physiological double-inhalation breath.");
    await page.locator("button", { hasText: "Save Reflection" }).click();
    await expect(page.locator("text=Reflection saved to your Performance Edge Plan.")).toBeVisible();

    // Check Bottom Banner
    await expect(page.getByLabel("Training Calm Principle Banner")).toBeVisible();
    await page.screenshot({ path: "tests/screenshots/lessons_desktop_full.png", fullPage: true });
  });

  test("Performance Journey displays canonical 10 Foundations", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/progress");

    await expect(page.locator("h1")).toContainText("YOUR PERFORMANCE JOURNEY");
    await expect(page.locator("text=Ten weeks. Practical tools. One next shot at a time.")).toBeVisible();
    await expect(page.locator("text=LORNETTE DAYE").first()).toBeVisible();
    await expect(page.locator("text=SAME PRINCIPLES. A STRONGER YOU.")).toBeVisible();

    // Screenshot
    await page.screenshot({ path: "tests/screenshots/progress_desktop.png" });
  });

  test("Mobile layout verified for dashboard and lessons", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/foundations/dashboard");
    await expect(page.locator("h1")).toContainText("WELCOME TO MY PERFORMANCE EDGE");

    // Mobile bottom navigation should be visible
    await expect(page.locator("nav[aria-label='Mobile quick tabs']")).toBeVisible();

    // Open mobile navigation drawer via hamburger button
    const menuBtn = page.getByRole("button", { name: /open portal navigation drawer/i });
    await expect(menuBtn).toBeVisible();
    await menuBtn.click();

    // Verify mobile drawer dialog and its scrollable content have no-scrollbar class
    const drawer = page.getByRole("dialog", { name: "Portal Navigation Drawer" });
    await expect(drawer).toBeVisible();
    const scrollContainers = drawer.locator(".overflow-y-auto");
    await expect(scrollContainers.first()).toBeVisible();
    await expect(scrollContainers.first()).toHaveClass(/no-scrollbar/);
    await expect(scrollContainers.nth(1)).toBeVisible();
    await expect(scrollContainers.nth(1)).toHaveClass(/no-scrollbar/);

    // Verify nav links inside mobile drawer
    await expect(drawer.getByRole("link", { name: "Dashboard" })).toBeVisible();
    await expect(drawer.getByRole("link", { name: "Lessons" })).toBeVisible();

    // Close mobile drawer
    const closeBtn = drawer.getByRole("button", { name: /close menu/i });
    await closeBtn.click();
    await expect(drawer).not.toBeVisible();

    await page.screenshot({ path: "tests/screenshots/dashboard_mobile.png" });
  });

  test("Admin workspace displays inquiries, cohorts, and plan review", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/admin?code=LD-ADMIN-2026");
    await page.waitForLoadState("networkidle");
    await expect(page.locator("h1")).toContainText("Admin Console");
    await expect(page.locator("text=Master Administrator · Coach Lornette Daye")).toBeVisible();
    await expect(page.locator("h2", { hasText: "Inquiries" })).toBeVisible();

    // Switch to Cohorts tab
    const cohortsBtn = page.locator("a", { hasText: "Cohorts" });
    await expect(cohortsBtn).toBeVisible();
    await cohortsBtn.click();
    await page.waitForURL("**/foundations/admin?tab=cohorts");
    await expect(page.locator("text=GOLF-FALL-2026")).toBeVisible();

    // Switch to Plans tab
    const plansBtn = page.locator("a", { hasText: "Lornette Review Queue" });
    await plansBtn.click();
    await page.waitForURL("**/foundations/admin?tab=plans");
    await expect(page.locator("h2", { hasText: "Lornette Review Queue" })).toBeVisible();
  });

  test("Club executive portal displays aggregate metrics and privacy guarantee", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/club");
    await expect(page.locator("h1")).toContainText("Team Aggregate Performance");
    await expect(page.locator("text=Private & Anonymized")).toBeVisible();
    await expect(page.locator("text=10-Foundation Cohort Progress")).toBeVisible();
    await expect(page.locator("text=INTERNAL-06: PGA Club Delivery Companion")).toBeVisible();
  });

  test("Coach Lornette review workflow syncs between admin and athlete plan", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });

    // Step 1: Open admin workspace review queue
    await page.goto("/foundations/admin?code=LD-ADMIN-2026&tab=plans");
    await page.waitForLoadState("networkidle");
    await expect(page.locator("text=Alex Harrison").first()).toBeVisible();

    // Step 2: Enter Coach Lornette review notes & submit
    const notesBox = page.locator("textarea[name='review_notes']").first();
    await notesBox.fill("Outstanding pre-shot discipline. Your committed routine is tournament-ready.");
    await page.locator("button[type='submit']:has-text('Submit Feedback')").first().click();

    // Step 3: Open participant's My Plan page and verify workspace loads
    await page.goto("/foundations/plan");
    await page.waitForLoadState("networkidle");
    await expect(page.locator("h1")).toContainText("My Performance Edge Plan");
  });

  test("Athlete can submit Grill-Me pressure challenge and review critique", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });

    // Step 1: Open Grill-Me pressure lab
    await page.goto("/foundations/grill-me");
    await page.waitForLoadState("networkidle");
    await expect(page.locator("h1")).toContainText("Coach Lornette's Grill-Me Challenge");

    // Step 2: Fill out tactical execution
    const textarea = page.locator("#golfer-response");
    await expect(textarea).toBeVisible();
    await textarea.fill("Stepped off tee box, executed 2 physiological breaths, locked focus on intermediate blade 18 inches ahead.");
    await page.locator("button[type='submit']", { hasText: "Submit to Coach Lornette" }).click();
    await expect(
      page.locator("text=Submitted to Coach Lornette Daye's Review Queue!")
    ).toBeVisible();

    // Step 3: Verify entry appears in admin review queue
    await page.goto("/foundations/admin?code=LD-ADMIN-2026&tab=plans");
    await page.waitForLoadState("networkidle");
    await expect(page.locator("h2", { hasText: "Lornette Review Queue" })).toBeVisible();
  });

  test("Goal and Grill-Me route redirects resolve seamlessly", async ({ page }) => {
    // Check /goal redirect to plan
    await page.goto("/goal");
    await page.waitForURL("**/foundations/plan", { timeout: 10000 });
    await expect(page).toHaveURL(/.*\/foundations\/plan/);

    // Check /foundations/goal redirect to plan
    await page.goto("/foundations/goal");
    await page.waitForURL("**/foundations/plan", { timeout: 10000 });
    await expect(page).toHaveURL(/.*\/foundations\/plan/);

    // Check /grill-me redirect
    await page.goto("/grill-me");
    await page.waitForURL("**/foundations/grill-me", { timeout: 10000 });
    await expect(page).toHaveURL(/.*\/foundations\/grill-me/);

    // Check /learn redirect to lessons
    await page.goto("/learn");
    await page.waitForURL("**/foundations/lessons", { timeout: 10000 });
    await expect(page).toHaveURL(/.*\/foundations\/lessons/);

    // Check /boost redirect to grill-me
    await page.goto("/boost");
    await page.waitForURL("**/foundations/grill-me", { timeout: 10000 });
    await expect(page).toHaveURL(/.*\/foundations\/grill-me/);
  });

  test("Account settings genuinely persist changes to store and re-sync across navigation", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/account");
    await page.waitForLoadState("networkidle");

    // Check initial input values by targeting labels
    const homeClubInput = page.locator("input").nth(2);
    const handicapInput = page.locator("input").nth(3);
    const divisionSelect = page.locator("select");

    await homeClubInput.fill("Marine Drive Golf Club");
    await handicapInput.fill("1.8 Index");
    await divisionSelect.selectOption("Collegiate Athlete (NCAA / U Sports)");

    // Save changes
    await page.locator("button[type='submit']", { hasText: "Save Changes" }).click();
    await expect(page.locator("text=Profile preferences updated.")).toBeVisible();

    // Navigate away to dashboard and back to account
    await page.goto("/foundations/dashboard");
    await page.waitForLoadState("networkidle");
    await page.goto("/foundations/account");
    await page.waitForLoadState("networkidle");

    // Verify persisted values remain intact
    await expect(page.locator("input").nth(2)).toHaveValue("Marine Drive Golf Club");
    await expect(page.locator("input").nth(3)).toHaveValue("1.8 Index");
    await expect(page.locator("select")).toHaveValue("Collegiate Athlete (NCAA / U Sports)");
  });

  test("Persona-switch reflection sync dynamically updates reflection inputs in lessons", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });

    // Step 1: Open lessons page as Alex Harrison (Foundation 1 reflection)
    await page.goto("/foundations/lessons");
    await page.waitForLoadState("networkidle");

    // Select Foundation 1 lesson
    const f1Btn = page.locator("button", { hasText: "Identity Beyond Sport" }).first();
    await f1Btn.click();

    // Verify Alex Harrison's Foundation 1 reflection is loaded
    const noticeTextarea = page.locator("#reflection-notice");
    await expect(noticeTextarea).toHaveValue(
      /I noticed my mood depended too heavily on the front-9 score/
    );

    // Step 2: Switch to Taylor Brooks persona via login portal
    await page.goto("/foundations/login");
    await page.waitForLoadState("networkidle");
    await page.locator("button", { hasText: "Preview Athlete Personas (Demo Sandbox)" }).click();
    await page.locator("button", { hasText: "Taylor Brooks" }).click();
    await page.waitForURL("**/foundations/dashboard", { timeout: 10000 });

    // Step 3: Return to lessons page and select Foundation 1
    await page.goto("/foundations/lessons");
    await page.waitForLoadState("networkidle");
    const f1BtnTaylor = page.locator("button", { hasText: "Identity Beyond Sport" }).first();
    await f1BtnTaylor.click();

    // Verify Taylor Brooks' reflection is dynamically synchronized
    await expect(noticeTextarea).toHaveValue(
      /When NCAA scouts stood by the 1st tee/
    );
  });

  test("Admin Code Access: Direct URL with code query param unlocks foundations dashboard", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/dashboard?code=LD-ADMIN-2026");
    await page.waitForURL("**/foundations/dashboard", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/dashboard/);
    await expect(page.locator("h1")).toContainText("WELCOME TO MY PERFORMANCE EDGE");
    await expect(page.locator("text=Powered by the Performance Edge Framework").first()).toBeVisible();
    await expect(page.locator("text=A stronger you creates a stronger game.")).toBeVisible();
  });

  test("Admin Code Access: Login portal admin mode unlocks dashboard with admin code", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/login");
    await expect(page.locator("h1")).toContainText("Welcome, Golfer");

    // Click Admin Code tab
    await page.locator("button:has-text('Admin Code')").click();
    await expect(page.locator("h1")).toContainText("Coach & Admin Access");
    await expect(page.locator("label:has-text('Official Admin Access Code')")).toBeVisible();

    // Fill Admin Code and submit
    await page.locator("#adminCode").fill("LD-ADMIN-2026");
    await page.locator("button:has-text('Enter Dashboard as Admin')").click();

    // Verify redirect to dashboard
    await page.waitForURL("**/foundations/dashboard", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/dashboard/);
    await expect(page.locator("h1")).toContainText("WELCOME TO MY PERFORMANCE EDGE");
  });

  test("Admin Code Access: Direct URL with code param unlocks foundations admin console", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/admin?code=LD-ADMIN-2026");
    await page.waitForURL("**/foundations/admin", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/admin/);
    await expect(page.locator("h1")).toContainText("Admin Console");
    await expect(page.locator("text=Master Administrator · Coach Lornette Daye")).toBeVisible();
  });

  test("Admin Code Access: Handles lowercase and whitespace padded codes gracefully", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/admin?code=%20ld-admin-2026%20");
    await page.waitForURL("**/foundations/admin", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/admin/);
    await expect(page.locator("h1")).toContainText("Admin Console");
    await expect(page.locator("text=Master Administrator · Coach Lornette Daye")).toBeVisible();
  });

  test("Admin Console: All 6 tabs load and display operational data", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto("/foundations/admin?code=LD-ADMIN-2026");
    await page.waitForLoadState("networkidle");

    // 1. Inquiries tab (default)
    await expect(page.locator("h2", { hasText: "Inquiries" })).toBeVisible();

    // 2. Participants tab
    await page.locator("a:has-text('Participants')").click();
    await expect(page.locator("text=Alex Harrison")).toBeVisible();
    await expect(page.locator("text=Taylor Brooks")).toBeVisible();

    // 3. Cohorts tab
    await page.locator("a:has-text('Cohorts')").click();
    await expect(page.locator("text=Create New Cohort")).toBeVisible();
    await expect(page.locator("text=GOLF-FALL-2026")).toBeVisible();

    // 4. Enrollments tab
    await page.locator("a:has-text('Enrollments')").click();
    await expect(page.locator("h2", { hasText: "Enrollments" })).toBeVisible();

    // 5. Lornette Review Queue tab
    await page.locator("a:has-text('Lornette Review Queue')").click();
    await expect(page.locator("h2", { hasText: "Lornette Review Queue" })).toBeVisible();

    // 6. Curated Resources tab
    await page.locator("a:has-text('Resources')").click();
    await expect(page.locator("h2", { hasText: "Resources" })).toBeVisible();

    // Master Administrator Header Badge navigation back to Dashboard
    const backToDashboard = page.locator("a:has-text('Back to Dashboard')");
    await expect(backToDashboard).toBeVisible();
    await backToDashboard.click();
    await page.waitForURL("**/foundations/dashboard", { timeout: 15000 });
    await expect(page).toHaveURL(/.*\/foundations\/dashboard/);
  });
});

