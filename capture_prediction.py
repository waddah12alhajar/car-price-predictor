#!/usr/bin/env python3
"""
Capture the ML prediction result using Playwright
"""
import asyncio
from playwright.async_api import async_playwright
import os

async def capture_prediction():
    os.makedirs("screenshots", exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer']
        )

        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        try:
            print("Loading home page...")
            await page.goto("http://127.0.0.1:5000/", wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(3000)  # Wait for JS to load

            # Take full-page screenshot of the form
            print("Taking full-page screenshot of prediction form...")
            await page.screenshot(path="screenshots/06_full_form.png", full_page=True)
            print("  ✓ Saved: screenshots/06_full_form.png")

            # Fill in the form
            print("Filling form with sample data...")

            # Select California
            await page.select_option("#state", "ca")
            await page.wait_for_timeout(500)

            # Select Los Angeles
            await page.select_option("#city", "los angeles")
            await page.wait_for_timeout(300)

            # Select Toyota
            await page.select_option("#make", "toyota")
            await page.wait_for_timeout(500)

            # Select Camry
            await page.select_option("#model", "camry")
            await page.wait_for_timeout(300)

            # Fill year
            await page.fill('input[name="year"]', "2018")

            # Fill mileage
            await page.fill('input[name="mileage"]', "35000")

            # Screenshot the filled form
            print("Taking screenshot of filled form...")
            await page.screenshot(path="screenshots/07_filled_form.png", full_page=True)
            print("  ✓ Saved: screenshots/07_filled_form.png")

            # Submit the form
            print("Submitting form for ML prediction...")
            await page.click('button[type="submit"]')
            await page.wait_for_load_state("networkidle", timeout=30000)
            await page.wait_for_timeout(2000)

            # Screenshot the result
            print("Taking screenshot of ML prediction result...")
            await page.screenshot(path="screenshots/08_prediction_result.png", full_page=True)
            print("  ✓ Saved: screenshots/08_prediction_result.png")

        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_prediction())
