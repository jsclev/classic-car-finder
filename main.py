import requests
from bs4 import BeautifulSoup


# https://www.streetsideclassics.com/vehicles/new_arrivals?q%5Bmake_eq%5D=Plymouth&q%5Bmodel_eq%5D=Road+Runner&q%5Byear_gteq%5D=1969&q%5Byear_lteq%5D=1969
URL = "https://www.streetsideclassics.com/vehicles/new_arrivals"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.contents)
