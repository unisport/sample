from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import urllib2
import json

SOURCE = 'https://www.unisport.dk/api/sample/'

class BaseView(View):
    def __init__(self, *args, **kwargs):
        data = urllib2.urlopen(SOURCE)
        data = json.load(data)
        self.data = sorted(data['products'], key=lambda prod: float(prod.get('price').replace(',', '.')))
        return super(BaseView, self).__init__(*args, **kwargs)

    def pagination(self, request):
        page = request.GET.get('page')
        paginator = Paginator(self.data, 10)
        data = None
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        return data


class ProductsView(BaseView):
    template_name = 'products.html'

    def get(self, request):
        data = self.pagination(request)
        context = {'products': data}
        return render_to_response(self.template_name, context)


class ProductsKidsView(BaseView):
    template_name = 'products.html'

    def get(self, request):
        self.data = [data for data in self.data if int(data.get('kids'))]
        data = self.pagination(request)
        context = {'products': data}
        return render_to_response(self.template_name, context)


class ProductsByIdView(BaseView):
    template_name = 'products.html'

    def get(self, request, id=None):
        data = [data for data in self.data if int(data.get('id')) == int(id)]
        context = {'products': data}
        return render_to_response(self.template_name, context)