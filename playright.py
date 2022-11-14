import time

from playwright.async_api import async_playwright
import asyncio
from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    # go to url
    page.goto("https://e-katanalotis.gov.gr/householdBasket")
    await page.waitForTimeout(5000)
    # get HTML



