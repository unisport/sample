# -*- coding: utf-8 -*-
from decimal import Decimal


def encoder(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))