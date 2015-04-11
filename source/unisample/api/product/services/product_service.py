from ..models import Product


class ProductService(object):

    def get_cheapest(self):
        return Product.objects.order_by('-price')

    def get_kids_products(self):
        return self.get_cheapest().filter(kids=1)

    def get_product_detail(self, product_id):
        product = Product.objects.filter(id=product_id)
        product = product[0] if product else None
        return product
