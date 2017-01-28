from products.models import Product


def get_products_page(page, limit, for_kids=False):
    """Get a list of products for a page.

    :param page: The number of the page to get the products for.
    :param limit: A number of products per page.
    :param for_kids: Determines whether the returned products should be are
        marked with `kids=1`.
    :return: The list of products.
    """
    assert page > 0

    qs = Product.objects.order_by('price')
    if for_kids:
        qs = qs.filter(kids=True)

    page_of_results = qs[(page - 1) * limit:(page - 1) * limit + limit]
    return list(page_of_results)


def get_product_by_id(product_id):
    """Get product by id.

    `DoesNotExist` exception will be raised if an object with the given id does
    not exist.

    :param product_id: The id of the product to get.
    """
    return Product.objects.get(id=product_id)
