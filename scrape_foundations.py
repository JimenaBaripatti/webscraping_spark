
import pause
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--kiosk")

driver = webdriver.Chrome(options=options, executable_path=r'/Users/jbaripatti/Development/chromedriver')

driver.get('https://www.sephora.com/ca/en/shop/foundation-makeup')
pause.seconds(1)

icon_cross_ele = driver.find_element_by_css_selector('svg.css-1bpyffv').click()
pause.seconds(2)

page_source = driver.page_source

content = BeautifulSoup(page_source, 'html.parser')
print(content)


driver.close()
driver.quit()