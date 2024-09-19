import time
from playwright.sync_api import sync_playwright

def scrape_tiktok_profile(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Visit Tiktok profile
        page.goto(f'https://www.tiktok.com/@{username}')

        #Wait for JS to load
        time.sleep(5)
        # Extract data (videos, views, likes, etc.)
