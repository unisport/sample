from datetime import datetime
from random import randint


def generate_item_permanent_id(max_length=14):
    assert max_length >= 12, 'max length must be greater than 12'
    from unisample.api.product.models import Product

    cur_date = datetime.now()
    id_start = '%04d%02d%02d' % (cur_date.year, cur_date.month, cur_date.day)
    id_end_length = max_length - len(id_start)
    id_end_template = '{:0>' + str(id_end_length) + '}'

    is_id_exists = True
    while is_id_exists:

        id_end = randint(0, 10**id_end_length - 1)
        id_end = id_end_template.format(id_end)
        permanent_id = id_start + id_end

        if Product.objects.filter(_permanent_id=permanent_id).count() == 0:
            return permanent_id
