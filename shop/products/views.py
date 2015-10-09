# -*- encoding: UTF-8 -*-
"""
Propose: Implemented REST API
Author: 'yac'
"""

import json
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from models import Product


FIELD_REQUIRED = {'success': False, 'errorMessage': 'Field <name> is required or empty'}


def product(request):
    """ Get list of products ordered with the cheapest first.
    Create product if method `POST`
    """

    if request.method == 'GET':

        sql = 'SELECT * FROM products_product order by CAST(price AS DECIMAL(6,2))'

        arg = QueryDict(request.GET.urlencode()).dict()
        slc = int(arg.get('page', 1)) * 10

        inst_list = Product.objects.raw(sql)[slc - 10: slc]

        return json_response({'result': [to_dict(ins) for ins in inst_list]})

    # create product
    elif request.method == 'POST':
        data = json.loads(request.body)
        if not data.get('name'):
            return json_response(FIELD_REQUIRED)

        p = Product(**data)
        p.save()
        return json_response({'id': p.id})


def detail(request, product_id):
    """ Get detail by product ID or Update/delete if method `POST`
     @param product_id: product ID in DataBase
    """
    if request.method == 'GET':
        instance = get_object_or_404(Product, id=product_id)
        return json_response({'result': to_dict(instance)})

    elif request.method == 'POST':
        data = json.loads(request.body)

        # update
        if data:
            if not data.get('name'):
                return json_response(FIELD_REQUIRED)

            Product(id=product_id, **data).save()
        else:  # delete
            get_object_or_404(Product, id=product_id).delete()

        return json_response({'success': True})

def kids(request):
    """ Get list of products ordered with the cheapest first for kids """
    sql = 'SELECT * FROM products_product where kids=1 order by CAST(price AS DECIMAL(6,2))'
    inst_list = Product.objects.raw(sql)

    return json_response({'result': [to_dict(ins) for ins in inst_list]})

def json_response(data):
    """ Response json format """
    return HttpResponse(json.dumps(data), content_type="application/json")

def to_dict(instance):
    """ Convert model instance to dict """
    return model_to_dict(instance, fields=[field.name for field in instance._meta.fields])