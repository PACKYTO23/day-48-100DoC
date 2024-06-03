from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# price_peso = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is {price_peso.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")

# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")

# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# print(bug_link.text)

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

final_dates = dates
final_events = events
python_events_data = {}

for n in range(len(final_dates)):
    python_events_data[n] = {
        "time": dates[n].text,
        "name": events[n].text,
    }

print(python_events_data)

driver.close()
# driver.quit()
