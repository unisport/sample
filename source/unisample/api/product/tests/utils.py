# -*- coding: utf-8 -*-
from unisample.api.product.models import Product


def create_product(
    name, price=None, price_old=None, kids=None, kid_adult=None, women=None,
):
    product = Product()

    product.name = name

    product.price     = price or 100.0
    product.price_old = price_old or 90.0

    product.kids      = kids or 0
    product.kid_adult = kid_adult or 0
    product.women     = women or 0

    product.delivery   = 'delivery',
    product.free_porto = False,
    product.package    = 1

    product.sizes = 'sizes'

    product.url = 'http://test.url'
    product.img_url = 'http://test.url'

    product.save()

    return product
