from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from api.models import Product
import urllib2
import json

# use this command to import data from the provided endpoint
class Command(BaseCommand):

    def handle(self, *args, **options):
        # get the provided json data
        data_url = 'http://www.unisport.dk/api/sample/'
        try:
            page = urllib2.urlopen(data_url)
        except Exception, e:
            print e
            return

        content = page.read()
        data = json.loads(content)

        # import data to the database
        for product in data['products']:
            # change danish number notation to a pythonic representation, e.g.
            # 1.099,00 becomes 1099.00
            product.update(price=product['price'].replace('.', '').replace(',', '.'))
            product.update(price_old=product['price_old'].replace('.', '').replace(',', '.'))

            # perform model validation on the provided data before saving
            # if there are no exception save the model
            #
            # full_clean() validates the model fields and uniqueness
            # it also returns a clean value for each field by converting it to proper python type
            # this means that, e.g.
            # for BooleanField we can use 0, 1, True, False, 't', 'True', '1', 'f' 'False', '0'
            try:
                product = Product(**product)
                product.full_clean()
                product.save()
            except ValidationError as e:
                print e.message_dict
