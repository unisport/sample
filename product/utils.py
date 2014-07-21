# coding=utf-8

import requests

from product.models import Product, Size


UNISPORT_API = 'http://www.unisport.dk/api/sample/'


def fetch_json_data():
    """
    Fetchs JSON product information from Unisport
    """
    r = requests.get(UNISPORT_API)
    return r.json()


def import_json_data(j_data):
    """
    Imports Product one by one from JSON
    """
    res = {'created': [], 'updated': []}
    for p_data in j_data['latest']:
        p, created = json_to_product(p_data)

        if created:
            res['created'].append(p)
        else:
            res['updated'].append(p)
    
    return res


def json_to_product(j_data):
    """
    Import single Product
    """
    j_data = j_data.copy()

    sizes = j_data.pop('sizes', '')
    delivery = j_data.pop('delivery', '')

    if delivery:
        # prepare delivery information
        try:
            days, _ = delivery.split(' ')
            min_day, max_day = days.split('-')
            j_data['min_delivery_day'] = int(min_day)
            j_data['max_delivery_day'] = int(max_day)
        except:
            pass

    def _convert_price(price):
        return price.replace('.', '').replace(',', '.')
    j_data['price'] = _convert_price(j_data['price'])
    j_data['price_old'] = _convert_price(j_data['price_old'])

    # import product
    p, created = Product.objects.get_or_create(pid=j_data['id'], defaults=j_data)

    # to update product if it exists
    if not created:
        for key in j_data:
            setattr(p, key, j_data[key])
        p.save()

    # Complete Product -- Size relation
    if sizes:
        sizes = sizes.split(',')

        # create non exist Size first
        map(lambda s: Size.objects.get_or_create(name=s), sizes)

        if not created:
            p_sizes = p.sizes.all().values_list('name', flat=True)
        else:
            p_sizes = []

        sizes = set(sizes)
        p_sizes = set(p_sizes)

        new_sizes = sizes - p_sizes
        old_sizes = p_sizes - sizes

        p.sizes.remove(*list(old_sizes))

        new_sizes = list(Size.objects.filter(name__in=list(new_sizes)))
        p.sizes.add(*new_sizes)

    return p, created
