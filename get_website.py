
import pause
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--kiosk")

driver = webdriver.Chrome(options=options, executable_path=r'/Users/jbaripatti/Development/chromedriver')

PAGE = 'https://www.sephora.com/ca/en/shop/foundation-makeup'

driver.get(PAGE)
pause.seconds(1)

icon_cross_ele = driver.find_element_by_css_selector('svg.css-1bpyffv').click()
pause.seconds(1)

page_source = driver.page_source

print(f"fetching {PAGE} from the internet")

# saving html source to disk

with open("/Users/jbaripatti/PycharmProjects/webscrapper_spark/backup/foundation.html", "w") as f:
    f.write(page_source)
    print('writing cached foundations.html')

driver.close()
driver.quit()



