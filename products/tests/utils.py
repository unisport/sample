from products.models import Product


def create_fake_product(**custom_params):
    params = dict(
        name='',
        price=0,
        price_old=0,
        currency='DKK',
        sizes='One size',
        delivery='1-2 dage',
        url='http://abc.def',
        image='http://abc.def',
        img_url='http://abc.def',
    )
    params.update(custom_params)
    return Product.objects.create(**params)
