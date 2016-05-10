#coding: utf-8
from factory.django import DjangoModelFactory
from unisport.product import models


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = models.Product
        django_get_or_create = ('name',
                                'price',
                                'kids',
                                'currency',
                                'url',
                                'delivery',
                                'package',
                                'kid_adult',
                                'free_porto',
                                'image',
                                'size',
                                'online',
                                'price_old',
                                'img_url',
                                'women',
                                )
    name = 'Foo'
    price = 20
    kids = 0
    currency = 'DKK'
    url = u'http://google.com'
    delivery = u'1-2 days'
    package = 1
    kid_adult = 1
    free_porto = 'free'
    image = u'http://img.com/'
    size = ''
    online = 0
    price_old = 27.5
    img_url = u'http://img.com/'
    women = 0