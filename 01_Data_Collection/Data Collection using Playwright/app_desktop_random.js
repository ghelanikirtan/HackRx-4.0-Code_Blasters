const { chromium } = require('playwright');
const fs = require('fs');

const outputFile = 'urls.txt'; // Name of the input text file containing URLs
const screenshotsFolder = 'screenshots'; // Folder to store the screenshots

// Randomize CSS properties
function randomizeCSS() {
  const randomMargin = Math.floor(Math.random() * 50) + 10;
  const randomPadding = Math.floor(Math.random() * 50) + 10;
  const randomFontSize = Math.floor(Math.random() * 20) + 12;
  const randomFontStyle = Math.random() < 0.5 ? 'normal' : 'italic';
  const randomColor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;

  return `
    margin: ${randomMargin}px;
    padding: ${randomPadding}px;
    font-size: ${randomFontSize}px;
    font-style: ${randomFontStyle};
    color: ${randomColor};
  `;
}

// Read URLs from the text file
function readUrlsFromFile() {
  const data = fs.readFileSync(outputFile, 'utf-8');
  return data.split('\n').filter((url) => url.trim() !== '');
}

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  try {
    // Create the screenshots folder if it doesn't exist
    if (!fs.existsSync(screenshotsFolder)) {
      fs.mkdirSync(screenshotsFolder);
    }

    const urls = readUrlsFromFile();

    for (const url of urls) {
      try {
        await page.goto(url);

        // Randomize CSS properties and apply to the body element
        const randomStyle = randomizeCSS();
        await page.addStyleTag({ content: `body { ${randomStyle} }` });

        // Take a screenshot
        const timestamp = new Date().getTime();
        const screenshotPath = `${screenshotsFolder}/screenshot_${timestamp}.png`;
        await page.screenshot({ path: screenshotPath });

        console.log(`Screenshot taken for ${url}`);
      } catch (error) {
        console.error(`Error capturing screenshot for ${url}: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  } finally {
    await browser.close();
    console.log('Screenshot process completed.');
  }
})();
