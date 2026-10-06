import { chromium } from '@playwright/test';

async function measure() {
  const browser = await chromium.launch();
  for (const width of [1280, 1440, 1536]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    await page.goto('http://localhost:3000/', { waitUntil: 'domcontentloaded' });
    await page.waitForSelector("header[data-hydrated='true']");

    const data = await page.evaluate(() => {
      const nav = document.querySelector("header nav");
      const ul = nav.querySelector("ul");
      const ulStyle = window.getComputedStyle(ul);
      const items = Array.from(ul.children).map((li, idx) => {
        const link = li.querySelector("a");
        const btn = li.querySelector("button");
        const chevron = btn ? btn.querySelector("svg") : null;
        const liRect = li.getBoundingClientRect();
        const linkRect = link ? link.getBoundingClientRect() : null;
        const btnRect = btn ? btn.getBoundingClientRect() : null;
        const chevronRect = chevron ? chevron.getBoundingClientRect() : null;
        return {
          idx,
          text: link ? link.innerText.trim() : li.innerText.trim(),
          li: { left: liRect.left, right: liRect.right, width: liRect.width },
          link: linkRect ? { left: linkRect.left, right: linkRect.right, width: linkRect.width } : null,
          btn: btnRect ? { left: btnRect.left, right: btnRect.right, width: btnRect.width } : null,
          chevron: chevronRect ? { left: chevronRect.left, right: chevronRect.right, width: chevronRect.width } : null,
        };
      });

      return {
        gap: ulStyle.gap,
        items,
      };
    });

    console.log(`\n=== VIEWPORT ${width}px ===`);
    console.log(`ul computed gap: ${data.gap}`);
    for (let i = 0; i < data.items.length - 1; i++) {
      const curr = data.items[i];
      const next = data.items[i + 1];
      const liGap = (next.li.left - curr.li.right).toFixed(1);
      const textToText = (next.link ? next.link.left - curr.link.right : next.li.left - curr.link.right).toFixed(1);
      let extra = '';
      if (curr.chevron) {
        const chevronToNext = (next.link ? next.link.left - curr.chevron.right : next.li.left - curr.chevron.right).toFixed(1);
        const linkToChevron = (curr.chevron.left - curr.link.right).toFixed(1);
        extra = ` [chevron: link->chev=${linkToChevron}px, chev->next=${chevronToNext}px, btn.right-li.right=${(curr.btn.right - curr.li.right).toFixed(1)}px]`;
      }
      console.log(`  ${curr.text.padEnd(12)} -> ${next.text.padEnd(12)}: liGap=${liGap}px, textToText=${textToText}px${extra}`);
    }
  }
  await browser.close();
}

measure().catch(console.error);
