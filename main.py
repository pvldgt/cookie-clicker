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
driver.implicitly_wait(10)

import time
# Click on the cookie
# make the while loop work for 5 minutes
end_time = time.time() + 60 * 5

check_time = time.time() + 20

# list_of_prices = []

# Find the cookie element
cookie = driver.find_element(By.ID, "bigCookie")

while time.time() < end_time:

    # Click on it
    cookie.click()
    # Delay of 1 sec between clicks for ease of development
    # time.sleep(1)

    if time.time() > check_time:

        # Create a list of prices of available items
        list_of_prices = []
        # try:
        prices_available = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled div.content span.price")
        for price in prices_available:
            if int(price.text.replace(",","")) not in list_of_prices:
                list_of_prices.append(int(price.text.replace(",","")))
        # except NoSuchElementException:
        #     print("no such element")

        # Print the prices of available items
        print(list_of_prices)

        #TODO Every 5 seconds check what upgrades are available and buy the most expensive one

        # Find the most expensive element

        most_expensive = 0
        for price in list_of_prices:
            if price > most_expensive:
                most_expensive = price
        print(most_expensive)
        # Click that element
        for price in prices_available:
            if int(price.text.replace(",","")) == most_expensive:
                # Get the ID of the most important element
                element_id = price.get_attribute("id")
                replace_id = element_id.replace("Price", "")
                expensive_element = driver.find_element(By.ID, replace_id)
                try:
                    expensive_element.click()
                except:
                    print("oopsie")

        check_time += 18


# After 5 minutes stop the bot and print "cookies/second"

driver.implicitly_wait(5)
find_result = driver.find_element(By.ID, "cookiesPerSecond")
pre_result = find_result.text
# Split on the space, grab the last element and convert to a float
result = float(pre_result.split(" ")[-1])
print(f"Your final result is {result} cookies per second")

driver.quit()
