from django.core.paginator import Paginator
from django.shortcuts import render

from api.models import Product
from api.forms import ProductForm


def index(request):
    form = ProductForm()

    if request.POST:

        # If a "Delete" button was pressed
        if request.POST.get('delete'):
            product = Product.objects.get(pk=request.POST['id'])
            product.delete()

        # If the "Create" button was pressed
        elif request.POST.get('create'):
            # Create a Product in the database using the POST parameters
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()

    # Page is optionally passed in GET
    page = request.GET.get('page') or 1

    # Test if it is an integer. It is user input so it could be anything.
    try:
        page = int(page)
    except ValueError:
        page = 1

    paginator = Paginator(Product.objects.order_by('price'), 10)

    # .get_page() instead of .page() because this is a sample and handling out of bound pages right
    # here feels a bit outside the scope of the exercise.
    products = paginator.get_page(page)

    return render(request, 'index.html', {
        'form': form,
        'page': page,
        'prev_page': page - 1,
        'next_page': page + 1,
        'products': products,
    })