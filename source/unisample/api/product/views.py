from django.views.generic import View
from unisample.api.product.serializers import ProductSerializer
from unisample.api.product.helpers import StatusResponse
from unisample.api.product.services.product_service import ProductService


class ProductListAjaxView(View):
    product_service = ProductService()

    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer()
        products = self.product_service.get_cheapest()
        products = serializer.serialize(products)
        return StatusResponse.ok(products=products)

product_list_ajax = ProductListAjaxView.as_view()
