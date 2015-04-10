from django.views.generic import View
from django.core import serializers
from unisample.api.product.helpers import StatusResponse
from unisample.api.product.services.product_service import ProductService


class ProductListAjaxView(View):
    product_service = ProductService()

    def get(self, request, *args, **kwargs):
        products = self.product_service.get_cheapest()
        products = serializers.serialize('json', products)
        return StatusResponse.ok(products=products)

product_list_ajax = ProductListAjaxView.as_view()
