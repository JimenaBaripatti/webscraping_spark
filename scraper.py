
from bs4 import BeautifulSoup
import os
from itertools import chain
import csv


def extract_data(item):
    """Extract information of brand, name, price, rating and shades of an item block
    :param item:
    :return: a dictionary
    """
    item_brand = item.find(attrs={'data-at': 'sku_item_brand'}).text
    item_name = item.find(attrs={'data-at': 'sku_item_name'}).text
    item_price = item.find(attrs={'data-at': "sku_item_price_list"}).text

    try:
        item_shades = item.find('div', class_="css-rrjz1n").text

    except AttributeError:
        item_shades = ''

    item_rating = item.find('div', class_='css-1adflzz').attrs['aria-label']
    row = dict(brand=item_brand,
               name=item_name,
               price=item_price,
               n_shades=item_shades,
               rating=item_rating)
    return row


def process_item_block(soup):
    """Extract data of each item blocks
    param: soup element
    return: list of dictionaries
    """

    item_blocks = soup.find_all('div', class_="css-12egk0t")
    rows = []
    for item in item_blocks:
        row = extract_data(item)
        rows.append(row)

    return rows


def create_soup(file_path):
    with open(file_path)as fp:
        soup = BeautifulSoup(fp)
    return soup


def process_directory(directory):
    """Process .htm files

    :param directory: directory path
    :return: nested list
    """
    data = []

    for f_name in os.listdir(directory):
        if f_name.endswith('.htm'):
            path = directory + f_name
            soup = create_soup(path)
            data.append(process_item_block(soup))
    return data


if __name__ == '__main__':

    nested_list = process_directory('backup/')
    face_makeup = list(chain.from_iterable(nested_list))

    with open('face_makeup.csv', mode='w', encoding='utf-8-sig') as csv_file:
        fieldnames = ['brand', 'name', 'price', 'n_shades', 'rating']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in face_makeup:
            writer.writerow(item)

    print('The scraping was successful. Got data of {0} items!'.format(len(face_makeup)))

