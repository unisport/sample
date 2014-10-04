import itertools
from app.data_filters import KeyValueFilter, CompositeFilter, SortingFilter, PaginationFilter
from app.exceptions import SuchProductAlreadyExists


def get_product_by_id(data, product_id):
    try:
        return next(KeyValueFilter(key="id", value=product_id).apply(data))
    except StopIteration:
        return None


def get_kids_products_sorted_by_price(data):
    return CompositeFilter(
        KeyValueFilter(key="kids", value="1"),
        SortingFilter(SortingFilter.ASC, "sortable_price")
    ).apply(
        data
    )


def get_products_paginated(data, page_num, per_page=10):
    return CompositeFilter(
        SortingFilter(SortingFilter.ASC, "sortable_price"),
        PaginationFilter(page_num, per_page)
    ).apply(
        data
    )


def delete_product(data, data_storage, product_id):
    res = KeyValueFilter(key="id", value=product_id, inverse=True).apply(data)
    res = list(res)  # needed to free read stream
    data_storage.save_data(res)


def update_product(data, data_storage, product):
    res = KeyValueFilter(key="id", value=product.id, inverse=True).apply(data)
    res = itertools.chain(res, (product,))
    data_storage.save_data(res)


def create_product(data, data_storage, product):
    data = list(data)  # to use data from generator twice for checking ID and for operation %(
    res = KeyValueFilter(key="id", value=product.id).apply(data)
    if len(list(res)) > 0:
        raise SuchProductAlreadyExists
    res = itertools.chain(data, (product,))
    data_storage.save_data(res)

