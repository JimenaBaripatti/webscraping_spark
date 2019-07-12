
import pause
from selenium import webdriver
from bs4 import BeautifulSoup
import pprint as pp


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

#all_text = content.get_text()


# get all brands on the page, it results in a <class 'bs4.element.ResultSet'> iterable
all_brands = content.find_all(attrs= {"data-at" : "sku_item_brand"})


# print(all_brands.prettify())
print(type(all_brands))

brands = []
for brand in all_brands:
    brand_name = brand.get_text()
    print(brand_name)
    brands.append(brand_name)






driver.close()
driver.quit()