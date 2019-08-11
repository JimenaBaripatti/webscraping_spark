from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
# options.add_argument("--kiosk")

driver = webdriver.Chrome(options=options, executable_path=r'/Users/jbaripatti/Development/chromedriver')

PAGE = 'https://www.sephora.com/ca/en/shop/foundation-makeup'

driver.get(PAGE)
pause.seconds(1)

# close pop-up
icon_cross_ele = driver.find_element_by_css_selector('svg.css-1bpyffv').click()
pause.seconds(2)

# select view all items
icon_select_all = Select(driver.find_element_by_css_selector("select.css-bpk111"))
icon_select_all.select_by_value('300')
pause.seconds(5)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait 30 seconds for page to load and extract the element after it loads
timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.css-2gkpw0")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

# footer = driver.find_element_by_tag_name('footer')

# footer.location_once_scrolled_into_view
pause.seconds(5)

page_source = driver.page_source
print(f"fetching {PAGE} from the internet")

soup = BeautifulSoup(page_source, 'html.parser')
driver.close()
driver.quit()

print('Done!')