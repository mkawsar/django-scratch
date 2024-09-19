import time
from bs4 import BeautifulSoup
from selenium import webdriver

# Set up the Selenium Chrome driver
def setup_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run browser in headless mode
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

# Scrape TikTok data for a given username
def scrape_tiktok_profile(username):
    driver = setup_selenium()

    # Navigate to the TikTok user's profile page
    driver.get(f'https://www.tiktok.com/@{username}')
    time.sleep(5)  # Wait for page to fully load

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    videos = soup.find_all('div', {'class': 'eq741c50'})
    for video in videos:
        video_url = video.find('a', {'class': 'video-link'})['href']
        print(video_url)
