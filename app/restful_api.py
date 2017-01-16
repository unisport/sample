from app.data_storage import StreamDataStorage
from app.exceptions import SuchProductAlreadyExists
from app.models import Product
from data_source import StreamDataSource
from flask import request, jsonify
import os
from usecases import get_kids_products_sorted_by_price, get_products_paginated, get_product_by_id, delete_product, \
    update_product, create_product
from flask_app import app
from flask.ext import restful

rest = restful.Api(app)


DATA_URL = "http://www.unisport.dk/api/sample/"
DATA_FILE_PATH = "{path}/data.json".format(
    path=os.path.dirname(os.path.realpath(__file__))
)


def data_to_json(data):
    return jsonify(
        {
            "latest": [document.__dict__ for document in data]
        }
    )


class Kids(restful.Resource):

    def get(self):

        with open(DATA_FILE_PATH) as stream:

            data_source = StreamDataSource(stream)

            res = get_kids_products_sorted_by_price(
                data_source.get_data()
            )

            return data_to_json(res)


class Products(restful.Resource):

    def get(self):

        with open(DATA_FILE_PATH) as stream:

            data_source = StreamDataSource(stream)

            page = int(request.args.get("page", 1))

            res = get_products_paginated(
                data_source.get_data(),
                page_num=page - 1,
                per_page=10,
            )

            return data_to_json(res)


class ProductId(restful.Resource):

    def get(self, product_id):
        # data_source = StreamDataSource.url_stream_factory(DATA_URL)
        with open(DATA_FILE_PATH) as stream:

            data_source = StreamDataSource(stream)

            res = get_product_by_id(
                data_source.get_data(),
                product_id
            )

            if res is None:
                return {
                    "status": "No product with such ID"
                }

            return jsonify(res.__dict__)

    def delete(self, product_id):
        """remove"""
        with open(DATA_FILE_PATH, "r+") as stream:

            data_source = StreamDataSource(stream)
            data_storage = StreamDataStorage(stream)

            delete_product(data_source.get_data(), data_storage, product_id)

            return {
                "status": "DELETED"
            }

    def put(self, product_id):
        """create"""
        with open(DATA_FILE_PATH, "r+") as stream:

            data_source = StreamDataSource(stream)
            data_storage = StreamDataStorage(stream)

            product = Product(id=product_id, **dict(request.args.items()))

            try:
                create_product(data_source.get_data(), data_storage, product)
            except SuchProductAlreadyExists:
                return {
                    "status": "Product with such ID already exists"
                }
            else:
                return {
                    "status": "CREATED"
                }

    def post(self, product_id):
        """update"""
        with open(DATA_FILE_PATH, "r+") as stream:

            data_source = StreamDataSource(stream)
            data_storage = StreamDataStorage(stream)

            # For some reason request.args unzipping properly only this way
            product = Product(id=product_id, **dict(request.args.items()))

            update_product(data_source.get_data(), data_storage, product)

            return {
                "status": "UPDATED"
            }


rest.add_resource(Products, '/products/')
rest.add_resource(ProductId, '/products/<product_id>/')
rest.add_resource(Kids, '/products/kids/')
