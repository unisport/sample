from json import JSONEncoder
from products.models import Product


def decimal_to_string_with_comma(value):
    return str(value).replace('.', ',')


class ProductEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Product):
            return {
                'is_customizable': str(int(o.is_customizable)),
                'delivery': o.delivery,
                'kids': str(int(o.kids)),
                'name': o.name,
                'package': str(int(o.package)),
                'kid_adult': str(int(o.kid_adult)),
                'free_porto': str(int(o.free_porto)),
                'image': o.image,
                'sizes': o.sizes,
                'price': decimal_to_string_with_comma(o.price),
                'url': o.url,
                'online': str(int(o.online)),
                'price_old': decimal_to_string_with_comma(o.price_old),
                'currency': o.currency,
                'img_url': o.img_url,
                'id': str(o.id),
                'women': str(int(o.women)),
            }
        return super().default(o)
