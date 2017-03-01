import requests
import json
from django.conf import settings


class UnisportAPI(object):

    def get_all(self):
        return self.request(None)   

    def request(
        self, path, args=None, post_args=None, method=None):
        """
        Perform request to 'https://www.unisport.dk/api/sample/'
        and retrieve all available data.

        Args:
            path (str): A sub path appended to the base url.
            post_args (dict): Data to be posted to the resouce
                requested.
            method (str): The HTTP method to be performed.
        Returns:
            response: The json content in the request to the
                sample end point.
            status_code (int): The status code of the response to
                the request
        """

        if args is None:
            args = dict()
        if post_args is not None:
            method = "POST"

        if path is None:
            path = ''

        try:
            response = requests.request(
                method or "GET",
                settings.UNISPORT_ENDPOINT + path,
                params=args,
                data=post_args)
        except requests.HTTPError as e:
            response = json.loads(e.read())
            raise UnisportAPIError(response)

        status_code = response.status_code or None
        headers = response.headers
        if 'json' in headers['content-type']:
            result = response.json()
        else:
            raise UnisportAPIError('Response not in json')


        if result and isinstance(result, dict) and result.get("error"):
            raise UnisportAPIError(result)
        return result, status_code

class UnisportAPIError(Exception):

    def __init__(self, result):
        self.result = result

        Exception.__init__(self, self.result)


class UniposortEndPoint(object):
    """ Helper class to retrieve and procces data from
    'UnisportAPI' class.
    """

    def __init__(self):

        self.unisprotapi = UnisportAPI()

    def get_all_products(self):
        """ Retreive all product items from unisport resource.
        Returns:
            dict: Containing all product items.
        """
        return self._get_all()

    def get_all_kids_products(self):
        """ Retreive all kids product items from unisport resource.
        Returns:
            dict: Containing all kids product items.
        """

        data = self._get_all()
        result = [item for item in data if item["kids"] == "1"]

        return result

    def get_product(self, product_id):

        """ A single item from the unisport resource by the product
        id.
        Args:
            product_id (int): The product id of the item to be
                returned.
        Returns:
            object: the object to be retrieved.
        """

        data = self._get_all()

        result = [item for item in data if item["id"] == str(product_id)][0]
        
        return result



    def _get_all(self):
        """ A private method to retrieve and sort all data
        obtained fron the unisport end point.

        Returns:
            ordered_data: Ordered dictionary of product items.
        """
        data, status = self.unisprotapi.get_all()

        ordered_data = sorted(data["products"], key=lambda k: k["price"].replace(",", "."))
        return ordered_data
