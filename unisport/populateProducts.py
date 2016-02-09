import os
import django
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'main.settings')
import requests

django.setup()
from products_app.models import Products
from products_app.serializers import ProductSerializer


FIXTURE_URL = 'https://www.unisport.dk/api/sample/'

def formatFloat(product):
    def prepareAttr(attr):
        if isinstance(attr, str):
            attr = float(attr.replace('.', '').replace(',', '.'))
        return attr
    for attr in ('price', 'price_old'):
        product[attr] = prepareAttr(product[attr])
    return product   


def saveProduct(products):
    for product in products:
        product = formatFloat(product)
        serializer = ProductSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
        else:
            print('Produst name %s error: %s' %(product['name'],dict(serializer.errors.items())))


def download_json(url=FIXTURE_URL):
    response = requests.get(url)
    data = response.json()
    productsData = data.get('products')
    saveProduct(productsData)

if __name__ == '__main__':
    download_json()
