// Visual QA: screenshot every tab of the built Module Hub, plus the other apps.
//
//   npm install playwright        (once; uses its bundled Chromium)
//   node tools/qa/screenshot_tabs.js
//
// Output: qa-screenshots/*.png — reviewed by eye before each publish.
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..', '..');
const OUT = path.join(ROOT, 'qa-screenshots');
const url = (app) => 'file://' + path.join(ROOT, 'dist', app, 'index.html');

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch(
    process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}
  );
  const page = await browser.newPage({ viewport: { width: 1400, height: 1000 } });

  await page.goto(url('module-hub'));
  await page.waitForTimeout(800);
  for (const tab of ['m1', 'm2', 'm3', 'm4']) {
    await page.click(`.nav-item[data-target="${tab}"]`);
    await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(OUT, `hub-${tab}.png`), fullPage: true });
    console.log('captured hub', tab);
  }
  for (const app of ['competitor-radar', 'pr-analytics-dashboard', 'architecture']) {
    await page.goto(url(app));
    await page.waitForTimeout(800);
    await page.screenshot({ path: path.join(OUT, `${app}.png`), fullPage: true });
    console.log('captured', app);
  }
  await browser.close();
})();
