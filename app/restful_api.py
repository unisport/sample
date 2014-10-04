from data_source import StreamDataSource
from flask import request, jsonify
from usecases import get_kids_products_sorted_by_price, get_products_paginated, get_product_by_id
from flask_app import app
from flask.ext import restful

rest = restful.Api(app)


def data_to_json(data):
    return jsonify(
        {
            "latest": [document.__dict__ for document in data]
        }
    )


class Kids(restful.Resource):

    def get(self):
        data_source = StreamDataSource.file_stream_factory()

        res = get_kids_products_sorted_by_price(
            data_source.get_data()
        )

        return data_to_json(res)


class Products(restful.Resource):

    def get(self):
        data_source = StreamDataSource.file_stream_factory()

        page = int(request.args.get("page", 1))

        res = get_products_paginated(
            data_source.get_data(),
            page_num=page - 1,
            per_page=10,
        )

        return data_to_json(res)


class ProductId(restful.Resource):

    def get(self, product_id):
        data_source = StreamDataSource.file_stream_factory()

        res = get_product_by_id(
            data_source.get_data(),
            product_id
        )

        if res is None:
            return {
                "status": "Not document with such ID"
            }

        return jsonify(res.__dict__)


rest.add_resource(Products, '/products/')
rest.add_resource(ProductId, '/products/<product_id>/')
rest.add_resource(Kids, '/products/kids/')
