import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com/feed/history")
time.sleep(20)  

for _ in range(20): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

video_links = []
videos = driver.find_elements(By.XPATH, "//ytd-video-renderer//a[contains(@href, '/watch')]")


for video in videos:
    link = video.get_attribute("href")
    print(f"Found Link: {link}")  
    if link and "watch" in link:
        video_links.append(link)


with open("watch_history.json", "w") as f:
    json.dump(video_links, f, indent=4)

print(f"✅ Saved {len(video_links)} video links to watch_history.json")

driver.quit()
