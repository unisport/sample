"""
utilities.py - Unisport Sample webservice
"""

from re import match
from collections import OrderedDict
from money import Money

# def paginate(items, size):
#     """
#     Paginates a list.

#     :param items: the items to paginate.
#     :param page_size: the size of each page.
#     :returns: the paginated items-list, where each page is size of page_size.
#     """
#     # pages = []
#     # start = 0
#     # end = 0
#     # for i in range(len(items)):
#     #     end = i + page_size
#     #     if i % page_size == 0:
#     #         page = items[start:end]
#     #         pages.append(page)
#     #         start = end
#     # return pages
#     return [items[i:i+size] for i in range(len(items)) if i % size == 0]

paginate = lambda items, size: [items[i:i+size] for i in range(len(items)) if i % size == 0]

def parse_money(value, currency):
    """
    Parses a money-amount based on its value and currency-type.

    :param value: the value of the money-amount
    :param currency: the currency-type of the money
    :returns: Money(value, currency)
    """
    if match(".+,[0-9]+$", value):
        return Money(
            value.replace(".", "").replace(",", "."),
            currency
        )
    return Money(value.replace(",", ""), currency)

def order_dict(dictionary, order):
    od = OrderedDict([(o, dictionary[o]) for o in order if o in dictionary.keys()])
    return od
