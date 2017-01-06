import requests

# fetch data from the endpoint
def fetch_data():
    try:
        import requests
        r = requests.get('http://www.unisport.dk/api/sample/')
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    return r.json()

# seed Product model
def seed_db(session, Product):
    data = fetch_data()
    for product in data['products']:
        pro = Product(
            delivery = product['delivery'],
            free_porto = product['free_porto'],
            img_url = product['img_url'],
            kid_adult = product['kid_adult'],
            kids = product['kids'],
            name = product['name'],
            package = product['package'],
            price = product['price'],
            price_old = product['price_old'],
            sizes = product['sizes'],
            url = product['url'],
            women = product['women']
        )
        session.add(pro)
        session.commit()
    session.query(Product).all()


