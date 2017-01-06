def convert_prices_from_danish_notation(data):
    # change danish number notation to a pythonic representation, e.g.
    # 1.099,00 becomes 1099.00

    if data.get('price') is not None and ',' in data['price']:
        data.update(price=data['price'].replace('.', '').replace(',', '.'))

    if data.get('price_old') is not None and ',' in data['price_old']:
        data.update(price_old=data['price_old'].replace('.', '').replace(',', '.'))
