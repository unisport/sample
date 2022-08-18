from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView

from unisport.unisport_data.models import Product


class ProductDeleteView(DeleteView):
    model = Product

    success_url = reverse_lazy("web:products")

    template_name = "unisport_web/product_confirm_delete.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "unisport_web/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        return context


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    template_name = "unisport_web/products_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product_list = Product.objects.all()
        paginator = Paginator(product_list, self.paginate_by)

        page = self.request.GET.get("page")

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context["object_list"] = products

        return context
