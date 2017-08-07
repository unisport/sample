"""
Did no use model function because there was no need to use a database to solve the assignment
"""


class Product:
    is_customizable = 0
    delivery = ""
    kids = 0
    name = ""
    sizes = ""
    kid_adult = 0
    free_porto = 0
    image = ""
    package = 0
    price = 0
    url = ""
    online = 0
    price_old = 0
    currency = ""
    img_url = ""
    id = 0
    women = 0

    def __init__(self, id, name, price, currency, kids):
        self.id = id
        self.name = name
        self.price = price
        self.currency = currency
        self.kids = kids

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "%s (%s)" % (self.name, self.price)






