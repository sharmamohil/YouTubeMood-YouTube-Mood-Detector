import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument(r"user-data-dir=C:\Users\ASUSSSS\AppData\Local\Google\Chrome\SeleniumProfile")  
options.add_argument("--profile-directory=Default")
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")  # Fix 1

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com/feed/history")
time.sleep(5)

for _ in range(3):  
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

videos = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
video_data = [{"title": v.text, "link": v.get_attribute("href")} for v in videos if v.get_attribute("href")]

with open("youtube_history.json", "w", encoding="utf-8") as f:
    json.dump(video_data, f, indent=4, ensure_ascii=False)

print(" YouTube history saved to youtube_history.json")

input("Press Enter to exit...")
driver.quit()
