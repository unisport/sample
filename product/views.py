from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Product
from .utils import paginate_objects


# all products view to show all products
class CatalogView(TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        product_queryset = Product.objects.all().order_by('price').prefetch_related('sizes')
        if kwargs.get('kids', False):
            product_queryset = product_queryset.filter(kids=1)
        context['products'] = paginate_objects(product_queryset, self.request.GET.get('page'))
        return context


# single product detail view
class ProductView(DetailView):
    template_name = 'product.html'
    model = Product
