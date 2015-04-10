from ..models import Product


class ProductService(object):

    def get_cheapest(self):
        return Product.objects.order_by('-price')
