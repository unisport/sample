from json import JSONEncoder
from Product import Product

class ProductJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return dict(
                 name=obj.name,
                 kids=obj.kids,
                 sizes=obj.sizes,
                 url=obj.url,
                 free_porto=obj.free_porto,
                 price=obj.price,
                 package=obj.package,
                 delivery=obj.delivery,
                 kid_adult=obj.kid_adult,
                 price_old=obj.price_old,
                 img_url=obj.img_url,
                 id=obj.id,
                 women=obj.women)
                 
        return JSONEncoder.default(self, obj)
