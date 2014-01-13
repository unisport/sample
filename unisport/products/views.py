from django.shortcuts import (render, get_object_or_404, Http404)
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from products.models import Item
from products.forms import ContactForm

class ContactView(FormView):
    template_name = 'form.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)

def getitem(request, id):
    """
    Gets a specific item, or returns a 404 error
    """
    item = get_object_or_404(Item, id = id)
    return render(request, 'products/product.html', {'item': item} )

def kids(request):
    """
    Returns the list of products for kids.
    """
    items = Item.objects.filter(kids=True)
    return render(request, 'products/products.html', {'items': items})

def paginate(request):
    """
    Paginates the products.  Each page contains ten products, ordered by price
    in ascending order.  If page argument is not numeric, Http404 will be
    raised, and also in case that there are no items on the page.  If there is
    no query string provided, the first ten products are shown.  
    """
    try:
        if len(request.GET) == 0:
            page = 1
        else:
            page = int(request.GET.get('page'))
        total = Item.objects.count()
        start = (page-1) * 10
        end = start + 10
        products = Item.objects.all()[start:min(total,end)]
        if products.count() == 0:
            raise Http404 # just a plain 
        return render(request, 'products/products.html', {'items': products})
    except (ValueError, NameError):
        raise Http404
