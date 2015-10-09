import json

from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.views.generic import View

from models import Product
from django.core.serializers.json import DjangoJSONEncoder


class ProductView(View):
    """
    The best way to make view - multi functional is create Class based views
        to separate functionality
    """
    products_on_page = 10

    def get(self, request, product_id=None):
        if product_id is not None:
            return self.get_by_id(product_id)

        return self.get_by_page(request.GET.get('page', '1'))

    def get_by_id(self, product_id):
        try:
            response = Product.objects.values().get(pk=product_id)
            return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder),
                                content_type='application/json')
        except Product.DoesNotExist:
            raise Http404("Product with id '{}' does not exist".format(product_id))

    def get_by_page(self, page):
        try:
            page = int(page)
            assert page > 0
        except (ValueError, AssertionError):
            return HttpResponseBadRequest("Wrong 'page' format. Number > 0 require, got {}".format(page))

        end = page * self.products_on_page
        begin = end - self.products_on_page

        product_list = list(Product.objects.order_by('price').values()[begin:end])
        response = json.dumps(product_list, cls=DjangoJSONEncoder)

        return HttpResponse(response, content_type='application/json')


def kids(request):
    product_list = list(Product.objects.filter(kids='1').order_by('price').values())
    response = json.dumps(product_list, cls=DjangoJSONEncoder)
    return HttpResponse(response, content_type='application/json')
