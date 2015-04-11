# -*- coding: utf-8 -*-

class ProductData(object):

    def __init__(self,
         name=None, pk=None, permanent_id=None,
         price=None, price_old=None,
         kids=None, kid_adult=None, women=None,
         delivery=None, free_porto=None, package=None, sizes=None,
         url=None, img_url=None,
         **kwargs # Ignore other arguments
    ):
        self.name = name
        self.pk = pk
        self.permanent_id = permanent_id

        self.price = price
        self.price_old = price_old

        self.kids = kids
        self.kid_adult = kid_adult
        self.women = women

        self.delivery = delivery
        self.free_porto = free_porto
        self.package = package
        self.sizes = sizes

        self.url = url
        self.img_url = img_url
