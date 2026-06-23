import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Create a large viewport for cinematic feel
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        # Load the local index.html
        abs_path = os.path.abspath("index.html")
        await page.goto(f"file://{abs_path}")

        # 1. Splash Screen
        await page.screenshot(path="01_splash.png")

        # 2. Enter App
        await page.click("#enter-btn")
        await page.wait_for_timeout(2000) # Wait for transition
        await page.screenshot(path="02_app_main.png")

        # 3. Scroll to Megalodon (Era 6 - Miocene)
        # Total height is 8 * 100vh = 8 * 1080
        await page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.7)")
        await page.wait_for_timeout(2000) # Wait for camera to catch up (lerp)
        await page.screenshot(path="07_megalodon_view.png")

        # 4. Open Tectonics at this depth
        await page.keyboard.press("g")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="08_globe_miocene.png")
        await page.keyboard.press("Escape")

        # 5. Evolution Tree
        await page.keyboard.press("t")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="04_tree.png")
        await page.keyboard.press("Escape")

        # 6. Quiz/Research
        await page.keyboard.press("q")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="05_quiz.png")

        # 7. Interact with Quiz
        await page.click(".quiz-opt:first-child") # Might be wrong depending on active zone, but let's see
        await page.wait_for_timeout(1000)
        await page.screenshot(path="06_quiz_feedback.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
