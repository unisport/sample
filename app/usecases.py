from app.data_filters import KeyValueFilter, CompositeFilter, SortingFilter, PaginationFilter


def get_product_by_id(data, product_id):
    try:
        return next(KeyValueFilter(key='id', value=product_id).apply(data))
    except StopIteration:
        return None


def get_kids_products_sorted_by_price(data):
    return CompositeFilter(
        KeyValueFilter(key='kids', value="1"),
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


def delete_product(data_source, product_id):
    pass


