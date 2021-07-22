from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver = webdriver.Safari()
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
sleep (5)
driver.close()