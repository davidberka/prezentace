import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# CONFIGURATION
PRESENTATION_ID = "1pFZMHBbIthUYMSvgbEr4xa_UnOxjqyASdXXtzLiz6oM"  # Replace this
NUM_SLIDES = 6  # Set this to your actual number of slides
OUTPUT_DIR = "screenshots/8"

# Set up Chrome options (headless optional)
options = Options()
options.add_argument("--headless")  # Uncomment to run in background (no visible window)
options.add_argument("--start-maximized")

# Launch Chrome with driver manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the presentation in "present" mode
slides_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}/present"
driver.get(slides_url)
time.sleep(5)  # Wait for presentation to load

# Create output folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Screenshot loop
for i in range(NUM_SLIDES):
    time.sleep(1.5)  # Wait for slide to render fully
    screenshot_path = os.path.join(OUTPUT_DIR, f"slide_{i + 1}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Captured: {screenshot_path}")
    driver.find_element("tag name", "body").send_keys(Keys.ARROW_RIGHT)

# Finish
driver.quit()
print(f"\n✅ All {NUM_SLIDES} slides captured to '{OUTPUT_DIR}/'")