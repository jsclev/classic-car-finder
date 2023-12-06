import requests
from bs4 import BeautifulSoup


url = 'https://www.streetsideclassics.com/vehicles?q%5Bmake_eq%5D=Plymouth&q%5Bmodel_eq%5D=Road+Runner&q%5Byear_gteq%5D=1968&q%5Byear_lteq%5D=1970'
page = requests.get(url)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

inventory_items = soup.select('.inventory-item')

for inventory_item in inventory_items:
    inner_item = inventory_item.find("div", {"class": "inventory-name"})
    year = inner_item.select('span[itemprop="productionDate"]')[0].get_text(strip=True)
    make = inner_item.select('span[itemprop="manufacturer"]')[0].get_text(strip=True)
    price = inner_item.select('.inventory-price')[0].get_text(strip=True)
    model = inner_item.select('span[itemprop="model"]')[0].get_text(strip=True)
    description = inner_item.select('.inventory-description')[0].get_text(strip=True)

    print(year + ' ' + make + ' ' + model + ', ' + price + ', ' + description)

# https://www.streetsideclassics.com/vehicles/new_arrivals?q%5Bmake_eq%5D=Plymouth&q%5Bmodel_eq%5D=Road+Runner&q%5Byear_gteq%5D=1968&q%5Byear_lteq%5D=1970
# https://www.gatewayclassiccars.com/make/plymouth?max_year=1969&min_year=1969
