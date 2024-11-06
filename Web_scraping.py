from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.headless = False  # Set to True for headless mode


driver = webdriver.Chrome(options=options)
query = "laptop"
file =0
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&qid=1730633414&ref=sr_pg_2")
    time.sleep(2)
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"Page={i}: {len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w" ,encoding="utf-8") as f:
            f.write(d)
            file += 1
time.sleep(2)
    
driver.quit()  # Move this outside the loop
