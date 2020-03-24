import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


class JumiaKeProductList:

    def __init__(self):
        self.link = 'https://www.jumia.co.ke/'
        self.product_list = []

    def getHTMLContent(self):
        try:
            html = requests.get(url=self.link)
            if html.status_code == 200:
                soup = BeautifulSoup(html.text, 'html.parser')
                return soup
            else:
                return False
        except requests.exceptions.ConnectionError:
            return False

    def getProductNamesAndPrices(self):
        soup_object = self.getHTMLContent()
        if not soup_object:
            return 'Could not connect to {} please retry later'.format(self.link)
        df = pd.DataFrame(columns=["PRODUCT NAME", "PRICE"])
        all_item_divs = soup_object.find_all('div', {'class': ['itm col']})
        all_item_links = soup_object.find_all('a', {'class': ['prd _box col']})
        div_loop = all_item_divs + all_item_links
        for div in div_loop:
            product_name = div.find('div', {'class': ['name']}).text
            jumia_product_price = div.find('div', {'class': ['prc']}).text
            product_price = jumia_product_price.split(' ')[1]
            product = {
                "name": str(product_name.replace("\\", " ").replace("\"", " inches")),
                "price": str(product_price)
            }
            row = [y for x, y in json.loads(json.dumps(product)).items()]
            df.loc[len(df)] = row
            self.product_list.append(json.loads(json.dumps(product)))
        df.to_csv("jumia-ke-product-list.csv")
        return product_list


if __name__ == '__main__':
    product_list = JumiaKeProductList()
    product_list.getProductNamesAndPrices()
    print("Done executing function")
