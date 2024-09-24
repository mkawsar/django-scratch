from playwright.sync_api import sync_playwright
import time

def scrape_tiktok_videos(username):
    u = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    with sync_playwright() as p:
        # Launch browser in non-headless mode to avoid bot detection
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=u)
        page = context.new_page()

        # Set a user agent to avoid bot detection
        
        # Navigate to the TikTok user's page
        page.goto(f'https://www.tiktok.com/@{username}')
        
        # Wait for the page to finish loading
        page.wait_for_load_state('networkidle')

        # Wait for the post item list to appear, with increased timeout
        try:
            page.wait_for_selector("div[data-e2e='user-post-item-list']", timeout=30000)
        except Exception as e:
            print(f"Error: {e}")
            browser.close()
            return []

        # Optionally wait for a few seconds to ensure all videos are loaded
        time.sleep(10)  # Adjust this delay as needed
        
        # Locate all video items
        videos = page.query_selector_all("div[data-e2e='user-post-item-list']")
        video_data = []

        # Extract video details
        for video in videos:
            try:
                video_url = video.query_selector("a").get_attribute('href')
                text_content = page.evaluate('(element) => element.textContent', video_url)
                print(text_content)
                likes = video.query_selector("strong").inner_text()

                video_data.append({
                    'username': username,
                    'video_url': video_url,
                    'likes': int(likes.replace('K', '000').replace('M', '000000'))
                })
            except Exception as e:
                print(f"Error scraping video: {e}")

        browser.close()
        print(video_data)
        return video_data
    