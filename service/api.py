import requests
from service.constants import URL


class Unisport:
    def __init__(self):
        self.url = URL
        self.products = []

    def fetch_products(self):
        """
            Will fetch all products from API given in URL.
            Will only fetch products once.
        """
        # We do not want to spam the api to much!
        if not self.products:
            response = requests.get(self.url)
            self.products = response.json().get('products')

    def sort_products(self, reverse=False):
        """
            Sort products by price.
        Args:
            reverse (bool, optional): sort ascending/decending.
                Defaults to False.
        """
        # Convert price to int, to make sort work as expected!
        self.products.sort(
            reverse=reverse,
            key=lambda product: int(product['price'])
        )

    def get_products(self, page=1):
        """
            Should return the first 10 objects
            ordered with the cheapest first.
            Support for pagination.

        Args:
            page (int, optional): Support for pagination.
                1 to 4 will return 10 products.
                5 will return nothing.
                Defaults to 1.

        Returns:
            list: Will return a list of products, if inside supported pages.
        """

        self.fetch_products()
        self.sort_products()

        page_size = 10
        # Page 1 = 0, Page 2 = 10, etc.
        start_slice = page_size * (page - 1)
        # Page 1 = 10, Page 2 = 20, etc.
        end_slice = page_size * page
        return self.products[start_slice:end_slice]

    def get_kids_products(self):
        """
            Should return the products where kids=1
            ordered with the cheapest first.
        """
        # kids=1 does not exist in current version of API or data returned!
        raise NotImplementedError

    def get_product(self, product_id):
        """
        Should return the individual product.

        Args:
            product_id (int): id of a product

        Returns:
            product or None: Detail of product if found.
                If not found, None is returned.
        """

        self.fetch_products()

        result = list(
            filter(
                lambda p: p['id'] == str(product_id),
                self.products
            )
        )
        if len(result) == 1:
            return result[0]
        else:
            return None
