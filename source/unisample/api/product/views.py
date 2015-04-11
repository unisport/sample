from django.views.generic import View
from unisample.api.product.serializers import ProductSerializer
from unisample.api.product.helpers import StatusResponse
from unisample.api.product.services.product_service import ProductService


#-----------------------------------------------------------------------------------------------------------------------
class AbstractProductAjaxView(View):
    product_service = ProductService()

    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer()
        products = self.get_list()
        products = serializer.serialize(products)
        return StatusResponse.ok(products=products)

    def get_list(self):
        return []


#-----------------------------------------------------------------------------------------------------------------------
class ProductListAjaxView(AbstractProductAjaxView):

    def get_list(self):
        return self.product_service.get_cheapest()

product_list_ajax = ProductListAjaxView.as_view()


#-----------------------------------------------------------------------------------------------------------------------
class ProductKidsAjaxView(AbstractProductAjaxView):

    def get_list(self):
        return self.product_service.get_kids_products()

product_kids_ajax = ProductKidsAjaxView.as_view()
