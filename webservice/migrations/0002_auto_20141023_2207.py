# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

# this is to handle comma in price and price_old fields
# when converting them into float
from locale import atof, setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, '')

from django.db import models, migrations
import requests


def import_items(apps, schema_editor):
    Item = apps.get_model('webservice', 'Item')
    response = requests.get('http://www.unisport.dk/api/sample/')
    raw_data = json.loads(response.content)

    for item in raw_data['latest']:
        Item(
            id=item['id'],
            kids=bool(int(item['kids'])),
            name=item['name'].encode('ascii', 'replace'), # handle decoding errors
            sizes=item['sizes'],
            kid_adult=bool(int(item['kid_adult'])),
            free_porto=True if item['free_porto'] == 'True' else False,
            price=atof(item['price'].encode('ascii')), # handle a float with comma, also handle coding
            package=bool(int(item['package'])),
            delivery=item['delivery'],
            url=item['url'],
            price_old=atof(str(item['price_old']).encode('ascii')),
            img_url=item['img_url'],
            women=bool(int(item['women']))
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_items)
    ]
