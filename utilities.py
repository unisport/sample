"""
utilities.py - Unisport Sample webservice

In general, the se utilities are made with functional programming in mind.
I emphasize the functional programming part, because it provides a streamlined
    way of bringing reproducibility which is good in general for any product,
    and for unit testing.

The pydoc style used is reST, because of a plugin I have for my editor,
    which uses said format.
"""

from re import match

# Ordinary dicts are unordered, and the unittest package
# had some problems comparing two dicts, even though they
# would logically be the exact same, and thus this would
# be used in order_dict() to keep the specified order.
from collections import OrderedDict

# This provides a nice, streamlined way of handling monetary value,
# instead of making one yourself.
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

# This is for paginating any list. This provides a functional way of paginating items.
# I used a lambda expression for shortening the whole definition.
paginate = lambda items, size: [items[i:i+size] for i in range(len(items)) if i % size == 0]

def parse_money(value, currency):
    """
    Parses a money-amount based on its value and currency-type.

    :param value: the value of the money-amount
    :param currency: the currency-type of the money
    :returns: Money(value, currency)
    """

    # I believe the specified regex pattern is flexible enough for our purposes.
    # This way also provides a way for the possibility to use other currencies,
    # and other decimal notation.
    if match(".+,[0-9]+$", value):
        return Money(
            # Money(value=...) doesn't take kindly to commas.
            # Thus the thousands-separators, if any, are removed.
            # The comma is replaced by a dot, which Money() can parse.
            value.replace(".", "").replace(",", "."),
            currency
        )
    return Money(value.replace(",", ""), currency)

# This was for reordering the key-value pairs in dicts,
# because the unittest package would act weird when asserting dicts.
order_dict = lambda dictionary, order: OrderedDict(
    [(o, dictionary[o]) for o in order if o in dictionary.keys()]
)
