from django.http.response import Http404
from django.views.generic import View
from unisample.api.api_common.helpers import StatusResponse
from unisample.api.api_common.views import PaginatingMixin
from unisample.api.product.serializers import ProductSerializer
from unisample.api.product.services.product_service import ProductService


#-----------------------------------------------------------------------------------------------------------------------
class AbstractProducListtAjaxView(View, PaginatingMixin):
    product_service = ProductService()
    product_serializer = ProductSerializer()

    def get(self, request, *args, **kwargs):
        products = self.get_list()
        products = self.paginate(products)

        try:
            products = self.product_serializer.serialize(products)
        except:
            return StatusResponse.fail('Was unable to serialize objects')

        return StatusResponse.ok(products=products)

    def get_list(self):
        return []


#-----------------------------------------------------------------------------------------------------------------------
class ProductListAjaxView(AbstractProducListtAjaxView):

    def get_list(self):
        return self.product_service.get_cheapest()

product_list_ajax = ProductListAjaxView.as_view()


#-----------------------------------------------------------------------------------------------------------------------
class ProductKidsAjaxView(AbstractProducListtAjaxView):

    def get_list(self):
        return self.product_service.get_kids_products()

product_kids_ajax = ProductKidsAjaxView.as_view()


#-----------------------------------------------------------------------------------------------------------------------
class ProductDetailAjaxView(View):
    product_service = ProductService()
    product_serializer = ProductSerializer()

    def get(self, request, *args, **kwargs):
        product_pk = kwargs['product_pk']
        product = self.product_service.get_product_detail(product_pk)

        if not product:
            raise Http404

        try:
            product = self.product_serializer.serialize([product])[0]
        except:
            return StatusResponse.fail('Was unable to serialize object')

        return StatusResponse.ok(product=product)

product_detail_ajax = ProductDetailAjaxView.as_view()
