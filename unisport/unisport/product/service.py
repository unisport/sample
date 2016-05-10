from decimal import Decimal


def get_price_from_unicode(price):
    return Decimal(price.replace('.', '').replace(',', '.'))

