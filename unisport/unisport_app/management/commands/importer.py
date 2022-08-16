import requests
import json
from unisport_app.models import Product
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://www.unisport.dk/api/products/batch/?list=200776,213591,200775,197250,213590,200780,209588,217706,205990,212703,197237,205989,211651,213626,217710,200783,213576,202483,200777,203860,198079,189052,205946,209125,200784,190711,201338,201440,206026,213587,172011,209592,193539,173432,200785,201442,203854,213577,200802,197362'

class Command(BaseCommand):
  def import_product(self, data):
    id = data.get('id', None)
    prices = data.get('prices', None)
    name = data.get('name', None)
    relative_url = data.get('relative_url', None)
    image = data.get('image', None)
    delivery = data.get('delivery', None)
    online = data.get('online', None)
    labels = data.get('labels', None)
    is_customizable = data.get('is_customizable', None)
    is_exclusive = data.get('is_exclusive', None)
    stock = data.get('stock', None)
    currency = data.get('currency', None)
    url = data.get('url', None)
    attributes = data.get('attributes', None)

    try:
        product, created = Product.objects.get_or_create(
            id = id,
            prices = prices,
            name = name,
            relative_url = relative_url,
            image = image,
            delivery = delivery,
            online = online,
            labels = labels,
            is_customizable = is_customizable,
            is_exclusive = is_exclusive,
            stock = stock,
            currency = currency,
            url = url,
            attributes = attributes
        ) 
        if created:
            product.save()
    except Exception as e:
        print(str(e))
        msg = "\n\nSomething went wrong saving this product: {}\n{}".format(id, str(e))
        print(msg)

  def handle(self, *args, **options):
  
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
    url=IMPORT_URL,
    headers=headers,
    )
    
    response.raise_for_status()
    data = json.loads(response.text)
    truedata = data.get('products')
    for data_object in truedata:  
      
      self.import_product(data_object)