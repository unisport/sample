import urllib
import json
from models import Product


# fetches sample data
def fetch_data():
    response = urllib.urlopen("https://www.unisport.dk/api/sample/")
    data = json.loads(response.read())

    return data["products"]


# convert string based bit value to boolean value
# for data filtering
def string_bit_to_boolean(bit):
    try:
        if bit == '1':
            return True
        else:
            return False
    except KeyError:
        return False


# convert price string to float value
# for better sortability
def format_price(price):
    try:
        price = price.replace('.', '')
        price = price.replace(',', '.')
        return float(price)
    except KeyError:
        return float("0.00")


# populates database with seed data
def run(db):
    data = fetch_data()
    for item in data:
        product = Product(
            id=int(item["id"]),
            is_customizable=string_bit_to_boolean(item["is_customizable"]),
            delivery=string_bit_to_boolean(item["delivery"]),
            kids=string_bit_to_boolean(item["kids"]),
            name=item["name"],
            sizes=item["sizes"],
            free_porto=string_bit_to_boolean(item["free_porto"]),
            kid_adult=string_bit_to_boolean(item["kid_adult"]),
            image=item["image"],
            package=string_bit_to_boolean(item["package"]),
            price=format_price(item["price"]),
            url=item["url"],
            online=string_bit_to_boolean(item["online"]),
            price_old=string_bit_to_boolean(item["price_old"]),
            img_url=item["img_url"],
            women=string_bit_to_boolean(item["women"])
        )
        db.session.add(product)
        db.session.commit()
