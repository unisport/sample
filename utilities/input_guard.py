allowed_fields =set(['kids', 'name', 'package', 'kid_adult', 'free_porto', 'price', 'sizes', 'delivery', 'url', 'price_old', 'img_url', 'women'])

def guard_products_failed(fields):
    input_filelds = set(fields)
    result = input_filelds.difference(allowed_fields)
    if len(result) == 0 :
        return False
    for item in result:
        if item not in allowed_fields:
            return True
    return False