from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Pip install Webdriver manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Import keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options


chrome_driver_path = "/Users/paveldegtyarev/Desktop/DATA/UDEMY/chromedriver"

# Add functionality to keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Import modules to wait for the language selection to appear
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Select English language
language = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div#langSelect-EN')))
language.click()

# Wait for 5 seconds just in case to load the cookie
driver.implicitly_wait(5)

import time
# Click on the cookie
# make the while loop work for 5 minutes
end_time = time.time() + 60 * 5
print(time.time())
print(end_time)
while time.time() < end_time:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()







# time.sleep(5)
# driver.quit()
