#!/usr/bin/env python3
"""
Screenshot script to capture demo pages of the Car Price Predictor application.
"""
import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshots():
    # Create screenshots directory
    os.makedirs("screenshots", exist_ok=True)

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--disable-software-rasterizer']
        )
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})

        # Base URL
        base_url = "http://127.0.0.1:5000"

        # Pages to screenshot
        pages = [
            ("/", "home_page.png", "Home Page - Car Price Prediction Form"),
            ("/about-us", "about_page.png", "About Us Page"),
            ("/contact-us", "contact_page.png", "Contact Us Page"),
            ("/login", "login_page.png", "Login Page"),
            ("/register", "register_page.png", "Register Page"),
        ]

        for route, filename, description in pages:
            try:
                print(f"Taking screenshot of {description}...")
                await page.goto(f"{base_url}{route}")
                await page.wait_for_load_state("networkidle")
                await asyncio.sleep(0.5)  # Extra wait for any animations
                await page.screenshot(path=f"screenshots/{filename}", full_page=True)
                print(f"  ✓ Saved: screenshots/{filename}")
            except Exception as e:
                print(f"  ✗ Error capturing {description}: {e}")

        # Take a screenshot of prediction result
        print("Taking screenshot of prediction result...")
        try:
            await page.goto(f"{base_url}/")
            await page.wait_for_load_state("networkidle")

            # Fill in the form with sample data
            # Select state first
            await page.select_option("#state", "ca")
            await asyncio.sleep(0.3)

            # Wait for city dropdown to populate and select
            await page.wait_for_selector("#city option:not([value=''])")
            await page.select_option("#city", "los angeles")

            # Select make
            await page.select_option("#make", "toyota")
            await asyncio.sleep(0.3)

            # Wait for model dropdown to populate and select
            await page.wait_for_selector("#model option:not([value=''])")
            await page.select_option("#model", "camry")

            # Fill year and mileage
            await page.fill('input[name="year"]', "2018")
            await page.fill('input[name="mileage"]', "35000")

            # Take screenshot of filled form
            await page.screenshot(path="screenshots/filled_form.png", full_page=True)
            print("  ✓ Saved: screenshots/filled_form.png")

            # Submit the form
            await page.click('button[type="submit"]')
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(0.5)

            # Screenshot the result
            await page.screenshot(path="screenshots/prediction_result.png", full_page=True)
            print("  ✓ Saved: screenshots/prediction_result.png")

        except Exception as e:
            print(f"  ✗ Error capturing prediction result: {e}")

        await browser.close()
        print("\nAll screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(take_screenshots())
