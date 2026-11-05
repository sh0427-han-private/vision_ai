import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import assert from 'node:assert/strict';

const BASE = 'http://127.0.0.1:8000';
const PAGE_SLUGS = [
  ['scalar', 'scalar'], ['vector', 'vector'], ['matrix', 'matrix'],
  ['tensor', 'tensor'], ['shape', 'shape'],
  ['dot-product', 'dot-product'], ['function', 'function'],
  ['cnn', 'kernel'], ['pixels', 'layout'],
];
const dir = 'p4-browser-evidence';
await mkdir(dir, { recursive: true });
const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
const failures = [];

async function check(name, run) {
  try {
    await run();
    console.log('PASS', name);
  } catch (error) {
    failures.push({ name, message: error.message });
    console.error('FAIL', name, error.message);
  }
}

async function changeValue(page, selector, wanted, eventType = 'input') {
  const element = page.locator(selector);
  await element.evaluate((node, args) => {
    node.value = args.wanted;
    node.dispatchEvent(new Event(args.eventType, { bubbles: true }));
  }, { wanted: String(wanted), eventType });
}

for (const width of [1440, 390]) {
  const page = await browser.newPage({ viewport: { width, height: 900 } });
  for (const [slug, anchor] of PAGE_SLUGS) {
    await check(width + ' render ' + slug, async () => {
      const response = await page.goto(BASE + '/notes/' + slug + '.html', {
        waitUntil: 'domcontentloaded',
      });
      assert.equal(response.status(), 200);
      assert.equal(await page.locator('h1').count(), 1);
      assert.equal(await page.locator('#' + anchor).count(), 1);
      assert.ok(await page.locator('a[href*="#"]').count() > 0);
      assert.ok(await page.locator('figure').count() > 0);
      if (await page.locator('.math-display').count() > 0) {
        await page.waitForFunction(
          () => [...document.querySelectorAll('.math-display')].every(
            element => element.querySelector('mjx-container') !== null,
          ),
          null,
          { timeout: 20000 },
        );
      }
      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth > innerWidth + 1,
      );
      assert.equal(overflow, false, 'unintended page-level horizontal overflow');
      await page.screenshot({
        path: dir + '/' + width + '-' + slug + '.png',
        fullPage: true,
        animations: 'disabled',
      });
      if (slug === 'cnn') {
        for (const anchorName of ['kernel', 'pooling']) {
          await page.goto(BASE + '/notes/cnn.html#' + anchorName, {
            waitUntil: 'domcontentloaded',
          });
          await page.waitForFunction(
            () => [...document.querySelectorAll('.math-display')].every(
              element => element.querySelector('mjx-container') !== null,
            ),
            null,
            { timeout: 20000 },
          );
          const section = page.locator('#' + anchorName);
          assert.ok(
            (await section.locator('h2').innerText()).includes(
              anchorName === 'kernel' ? 'Kernel' : 'Pooling',
            ),
          );
          await section.evaluate(element => {
            window.scrollTo({
              top: Math.max(0, element.getBoundingClientRect().top + window.scrollY - 30),
              behavior: 'instant',
            });
          });
          const headingTop = await section.locator('h2').evaluate(
            element => element.getBoundingClientRect().top,
          );
          assert.ok(
            headingTop >= 0 && headingTop < 250,
            'Section heading must be visible: ' + anchorName + ' top=' + headingTop,
          );
          const target = dir + '/' + width + '-cnn-' + anchorName + '.png';
          let bytes;
          for (let attempt = 0; attempt < 3; attempt++) {
            // Chromium may capture an unpainted frame after a large scroll.
            await page.waitForTimeout(250);
            await page.evaluate(() => new Promise(resolve => {
              requestAnimationFrame(() => requestAnimationFrame(resolve));
            }));
            bytes = await page.screenshot({
              path: target,
              animations: 'disabled',
            });
            if (bytes.byteLength > 12000) break;
            await section.evaluate(element => {
              element.scrollIntoView({ block: 'start', behavior: 'instant' });
            });
          }
          assert.ok(
            bytes.byteLength > 12000,
            'Screenshot remains blank after repaint retries: '
              + width + '/' + anchorName,
          );
        }
      }
    });
  }
  await check(width + ' P4 prerequisite/next-topic deep link', async () => {
    await page.goto(BASE + '/notes/scalar.html', { waitUntil: 'domcontentloaded' });
    await page.locator('a[href="vector.html#vector"]').first().click();
    await page.waitForURL('**/notes/vector.html#vector');
    assert.equal(await page.locator('#vector').count(), 1);
    await page.goto(BASE + '/notes/cnn.html#pooling', { waitUntil: 'domcontentloaded' });
    assert.equal(await page.locator('#pooling h2').count(), 1);
    await page.goto(BASE + '/notes/cnn.html#kernel', { waitUntil: 'domcontentloaded' });
    assert.equal(await page.locator('#kernel h2').count(), 1);
  });
  await check(width + ' Shape and GELU two-line stdout display', async () => {
    for (const [slug, section, expected] of [
      ['shape', 'python', '(3, 2, 3)\n[0, 3, 6] 18'],
      ['cnn', 'nonlinear', '[0.0, 0.5, 3]\n0.3457'],
    ]) {
      await page.goto(BASE + '/notes/' + slug + '.html', { waitUntil: 'domcontentloaded' });
      const output = page.locator('#' + section + ' p:has-text("예상 출력:") + pre > code');
      assert.equal(await output.count(), 1);
      assert.equal(await output.textContent(), expected);
      assert.equal(await output.evaluate(el => getComputedStyle(el.parentElement).whiteSpace), 'pre');
      await output.scrollIntoViewIfNeeded();
      await page.screenshot({
        path: dir + '/' + width + '-' + slug + '-stdout.png',
        animations: 'disabled',
      });
    }
  });
  await check(width + ' Function equation CHTML and contained width', async () => {
    await page.goto(BASE + '/notes/function.html', { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(
      () => document.querySelector('#example .equation mjx-container') !== null,
      null, { timeout: 20000 },
    );
    const metrics = await page.locator('#example .equation').evaluate(el => ({
      clientWidth: el.clientWidth,
      scrollWidth: el.scrollWidth,
      mathWidth: el.querySelector('mjx-container').getBoundingClientRect().width,
      pageWidth: document.documentElement.scrollWidth,
      viewportWidth: innerWidth,
    }));
    console.log('FUNCTION_EQUATION_METRICS', width, JSON.stringify(metrics));
    assert.ok(metrics.clientWidth > 100);
    assert.ok(metrics.scrollWidth <= metrics.clientWidth + 2,
      'Function equation must fit without sideways scrolling: ' + JSON.stringify(metrics));
    assert.ok(metrics.pageWidth <= metrics.viewportWidth + 1, 'Function equation causes page overflow');
    await page.locator('#example .equation').scrollIntoViewIfNeeded();
    await page.screenshot({
      path: dir + '/' + width + '-function-equation.png',
      animations: 'disabled',
    });
  });
  await check(width + ' MathJax actual CHTML typesetting', async () => {
    await page.goto(BASE + '/notes/dot-product.html', { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(
      () => document.querySelector('.math-display mjx-container') !== null,
      { timeout: 20000 },
    );
    const texRaw = await page.locator('.equation-fallback').count();
    assert.equal(texRaw, 0);
    assert.ok(await page.locator('.math-display mjx-container').count() > 0);
  });
  await check(width + ' kernel/pooling math fits equation panel', async () => {
    for (const anchor of ['kernel', 'pooling']) {
      await page.goto(BASE + '/notes/cnn.html#' + anchor, {
        waitUntil: 'domcontentloaded',
      });
      await page.waitForFunction(
        selector => document.querySelector(selector + ' mjx-container') !== null,
        '#' + anchor + ' .math-display',
        { timeout: 20000 },
      );
      const widthCheck = await page.locator('#' + anchor + ' .equation').evaluate(
        container => ({
          available: container.clientWidth,
          content: container.scrollWidth,
        }),
      );
      assert.ok(
        widthCheck.content <= widthCheck.available + 2,
        anchor + ' equation still overflows: ' + JSON.stringify(widthCheck),
      );
    }
  });
  await check(width + ' topic fallback + back/forward', async () => {
    await page.goto(BASE + '/index.html?topic=semiconductor');
    assert.equal(await page.locator('[data-topic-panel="overview"]').getAttribute('hidden'), null);
    assert.equal(await page.locator('[data-topic-tab="semiconductor"]').count(), 0);
    await page.goto(BASE + '/index.html?topic=ai');
    assert.equal(await page.locator('[data-topic-panel="ai"]').getAttribute('hidden'), null);
    await page.locator('[data-topic-tab="vision"]').click();
    assert.equal(await page.locator('[data-topic-panel="vision"]').getAttribute('hidden'), null);
    await page.goBack();
    assert.equal(await page.locator('[data-topic-panel="ai"]').getAttribute('hidden'), null);
    await page.goForward();
    assert.equal(await page.locator('[data-topic-panel="vision"]').getAttribute('hidden'), null);
  });
  await check(width + ' legacy JS brightness lab', async () => {
    await page.goto(BASE + '/notes/pixels.html');
    const before = await page.locator('#pixel-matrix').innerText();
    await changeValue(page, '#brightness', 175);
    const after = await page.locator('#pixel-matrix').innerText();
    assert.notEqual(after, before);
    assert.ok(await page.locator('#pixel-matrix span').count() === 64);
  });
  await check(width + ' legacy JS convolution lab', async () => {
    await page.goto(BASE + '/notes/cnn.html');
    const before = await page.locator('#conv-value').innerText();
    await changeValue(page, '#conv-position', 4);
    const after = await page.locator('#conv-value').innerText();
    assert.notEqual(after, before);
    assert.ok(after.includes('위치 (1, 1)'));
  });
  await check(width + ' legacy JS patch lab', async () => {
    await page.goto(BASE + '/notes/vit.html');
    const before = await page.locator('#patch-result').innerText();
    const nextValue = await page.locator('#patch-size').evaluate(node => {
      if (node.options) return [...node.options].map(x => x.value).find(x => x !== node.value);
      return node.value === '16' ? '32' : '16';
    });
    assert.ok(nextValue);
    await changeValue(page, '#patch-size', nextValue, 'change');
    const after = await page.locator('#patch-result').innerText();
    assert.notEqual(after, before);
  });
  await check(width + ' legacy JS threshold lab', async () => {
    await page.goto(BASE + '/notes/training.html');
    const before = await page.locator('#threshold-value').innerText();
    await changeValue(page, '#threshold', 90);
    const after = await page.locator('#threshold-value').innerText();
    assert.notEqual(after, before);
  });
  if (width === 390) {
    await check('mobile sidebar open, Escape and focus', async () => {
      await page.goto(BASE + '/notes/scalar.html');
      const menu = page.locator('.menu');
      await menu.click();
      assert.ok(await page.locator('.sidebar').evaluate(n => n.classList.contains('open')));
      assert.equal(await menu.getAttribute('aria-expanded'), 'true');
      await page.keyboard.press('Escape');
      assert.equal(await menu.getAttribute('aria-expanded'), 'false');
    });
  }
  await page.close();
}
await browser.close();
console.log('BROWSER CHECKS', failures.length === 0 ? 'ALL PASS' : 'FAILED', failures.length);
if (failures.length) process.exitCode = 1;
