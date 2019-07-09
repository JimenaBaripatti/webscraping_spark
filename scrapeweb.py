#! /usr/bin/env python3

import pause
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--kiosk")

driver = webdriver.Chrome(options=options, executable_path=r'/Users/jbaripatti/Development/chromedriver')

driver.get('https://www.sephora.com')

icon_cross_ele = driver.find_element_by_css_selector('svg.css-1bpyffv')
icon_cross_ele.click()

search_ele = driver.find_element_by_name("keyword")
time.sleep(1)
search_ele.clear()
search_ele.send_keys("foundation")
search_ele.send_keys(Keys.RETURN)
time.sleep(3)

driver.quit()