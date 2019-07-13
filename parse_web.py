
from bs4 import BeautifulSoup

path = 'backup/foundation.html'
soup = BeautifulSoup(path, 'html.parser')


# get all brands on the page, it results in a <class 'bs4.element.ResultSet'> iterable
all_brands = soup.find_all(attrs= {"data-at" : "sku_item_brand"})


# print(all_brands.prettify())
print(type(all_brands))

brands = []
for brand in all_brands:
    brand_name = brand.get_text()
    print(brand_name)
    brands.append(brand_name)
