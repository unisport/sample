import json
import urllib2
from django.core.management.base import NoArgsCommand
from products.models import Product, ProductSize
from products.views import get_json

class Command(NoArgsCommand):
    help = "Gets json from Unisport and builds the database"

    def handle(self, **options):
        product_json = get_json()
        for item in product_json:
        # Try to find product - if it doesn't exist, create a new DB entry
            try:
                product = Product.objects.get(pk=item["id"])
            except Product.DoesNotExist:
                product = Product()
            for key, value in item.items():
                if not key in ["sizes"]:
                    if key in ["price", "price_old"]:
                        product.__dict__[key] = value.replace(",", ".")
                    elif key in ["kids", "kid_adult", "women", "free_porto"]:
                        product.__dict__[key] = int(value)
                    else:
                        product.__dict__[key] = value
            product.from_json = True
            product.save()
            # Create a list of product sizes from the json
            product_sizes = item["sizes"].split(",")
            # Create product sizes, and add the sizes to the product
            for item in product_sizes:
                size, created = ProductSize.objects.get_or_create(title=item)
                product.sizes.add(size)
        return None
