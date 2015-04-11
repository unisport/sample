from unisample.api.product.models import Product


class ProductService(object):

    def get_cheapest(self):
        return Product.objects.order_by('price')

    def get_kids_products(self):
        return self.get_cheapest().filter(kids=1)

    def get_product_detail(self, product_id):
        product = Product.objects.filter(id=product_id)
        product = product[0] if product else None
        return product

    # -- -- -- --
    
    def create_product(self, user, product_data):
        product = Product()
        self._update_product(product, product_data)
        return product

    def update_product(self, user, product_data):
        product = Product.objects.get(pk=product_data.pk)
        self._update_product(product, product_data)
        return product

    def delete_product(self, user, product_pk):
        product = Product.objects.get(pk=product_pk)
        product.delete()

    def _update_product(self, product, product_data):
        product.name = product_data.name

        product.price = product_data.price
        product.price_old = product_data.price_old

        product.kids = product_data.kids
        product.kid_adult = product_data.kid_adult
        product.women = product_data.women

        product.delivery = product_data.delivery
        product.free_porto = product_data.free_porto
        product.package = product_data.package
        product.sizes = product_data.sizes

        product.url = product_data.url
        product.img_url = product_data.img_url

        product.save()

        return product
