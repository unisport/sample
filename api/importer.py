import requests
from api.serializers import ProductSerializer


def import_unisport_data():
    """Import unisport data from their api to the db."""

    unisport_api_uri = "https://www.unisport.dk/api/products/batch/"
    products_list_param = "?list=194742,193638,197237,188894,188896,189214,\
    194824,197250,194368,194477,194986,185253,197236,185117,187424,185866,\
    187743,194813,193639,187972,194923,194646,173445,193637,187744,200197,\
    193539,170478,194753,188893,181372,187477,193959,189188,197235,187812,\
    197242,168029,187425,194823"
    import_url = f"{unisport_api_uri}{products_list_param}"

    response = requests.get(
        url=import_url,
        timeout=5
    )
    products = response.json().get('products')

    return products[0]
