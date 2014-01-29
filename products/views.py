from sample.utils import render_to
from django.http import HttpResponseRedirect, HttpResponse
import json
import urllib2
from django.core.urlresolvers import reverse
from models import Product, ProductSize
from forms import ProductForm, ProductSizeForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Opens Unisport URL, loads the JSON response and returns the "latest" list of products
def get_json():
    opener = urllib2.build_opener()
    req = urllib2.Request("http://www.unisport.dk/api/sample/")
    f = opener.open(req)
    product_json = json.load(f)
    return product_json["latest"]


# Returns original JSON data, ordered and paginated - with or without a category given
def main_page(request, category=None):
    json_to_process = get_json()
    # Get page parameter, default is 1 and try and turn it into integer
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        return HttpResponse("Page must be an integer", content_type="text/plain")
    # Get items parameter, default is 10 and try and turn it into integer
    try:
        items = int(request.GET.get("items", 10))
    except ValueError:
        return HttpResponse("Items per page must be an integer", content_type="text/plain")
    if category:
        # If category is present, filter the JSON object where given category is true (1).
        # Throws an error if given category is not a key in the JSON object
        try:
            json_to_process = [x for x in json_to_process if x[category] == "1"]
            if not category in ["kids", "kid_adult", "women", "free_porto"]:
                return HttpResponse("Cannot filter JSON by %s" % category, content_type="text/plain")
        except KeyError:
            return HttpResponse("%s is not a key in the JSON object" % category, content_type="text/plain")
    # Since there are problems sorting numbers in strings, replace , with . in the string, and then convert value to float before sorting
    sorted_json = sorted(json_to_process, key=lambda x: float(x["price"].replace(",", ".")))
    # Sets low range to be equal to items per page * (number of pages - 1). The -1 is to insure that the first page will always start on index 0
    low_range = items * (page - 1)
    # High range should always be page * items (not subtracted by 1), because of the way slicing works.
    # list[0:10] will return the first 10 items (0-9) and so forth.
    high_range = page * items
    paginated_json = sorted_json[low_range:high_range]
    result = {"latest": paginated_json}
    return HttpResponse(json.dumps(result), content_type="application/json")


def view_product(request, product_id):
    json_to_process = get_json()
    # Try to get the first object of JSON, where ID is equal to the product_id parameter
    try:
        result = [x for x in json_to_process if x["id"] == product_id][0]
    except IndexError:
        return HttpResponse("Product with id %s does not exist" % product_id, content_type="text/plain")
    return HttpResponse(json.dumps(result), content_type="application/json")


# Page for list of products
@render_to("products/products_list.html")
def products_list(request, page=1, items=10):
    page = int(page)
    items = int(items)
    products = Product.objects.filter(deleted=False).order_by("price")

    # Table headers
    sort_params = [
            {"title": "Product name", "width": "", "sort":{"active": None, "key": "name"}},
            {"title": "Price", "width": "", "sort":{"active": None, "key": "price"}},
            {"title": "Sizes", "width": "", "sort": None},
            {"title": "Actions", "width": "", "sort": None, "colspan": "3"},
    ]
    extra_args = [page, items]

    # Get sort key and direction, and sort appropiatly if present
    sort_key = request.REQUEST.get("sort_key", "price")
    sort_dir = request.REQUEST.get("sort_dir", "asc")
    if products and request.REQUEST.get("sort_key"):
        if sort_key in ["name", "price"]:
            order_key = sort_key
            if sort_dir == "desc":
                order_key = "-%s" % order_key
            products = products.order_by(order_key)

    # Use Django built-in pagination
    paginator = Paginator(products, items)
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        return HttpResponseRedirect(reverse("products.views.products_list", args=[paginator.num_pages, items]))
    return locals()


# Page for list of sizes
@render_to("products/sizes_list.html")
def sizes_list(request, page=1, items=10):
    page = int(page)
    items = int(items)
    sizes = ProductSize.objects.all().order_by("title")
    # Table headers
    sort_params = [
            {"title": "Size title", "width": "650", "sort": {"active": None, "key": "title"}},
            {"title": "Actions", "width": "", "sort": None, "colspan": "2"},
    ]
    extra_args = [page, items]

    # Get sort key and direction, and sort appropiatly if present
    sort_key = request.REQUEST.get("sort_key", "title")
    sort_dir = request.REQUEST.get("sort_dir", "asc")
    if sizes and request.REQUEST.get("sort_key"):
        if sort_key in ["title"]:
            order_key = sort_key
            if sort_dir == "desc":
                order_key = "-%s" % order_key
            sizes = sizes.order_by(order_key)

    # Use Django built-in pagination
    paginator = Paginator(sizes, items)
    try:
        sizes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        return HttpResponseRedirect(reverse("products.views.sizes_list", args=[paginator.num_pages, items]))
    return locals()


@render_to("products/edit_product.html")
def edit_product(request, product_id=0):
    # Sets the form of product creation. If product_id is present, will use the product as form instance
    if product_id:
        try:
            product = Product.objects.get(pk=product_id)
            form = ProductForm(request.POST or None, instance=product)
        except Product.DoesNotExist:
            form = ProductForm(request.POST or None)
    else:
        form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save()
        return HttpResponseRedirect(reverse("products.views.products_list"))
    return locals()


@render_to("products/edit_size.html")
def edit_size(request, size_id=0):
    # Sets the form of size creation. If size_id is present, will use the size as form instance
    if size_id:
        try:
            size = ProductSize.objects.get(pk=size_id)
            form = ProductSizeForm(request.POST or None, instance=size)
        except ProductSize.DoesNotExist:
            form = ProductSizeForm(request.POST or None)
    else:
        form = ProductSizeForm(request.POST or None)
    return locals()


def delete_product(request, product_id):
    # Simple delete of product. Uses a delete column, as some other tables might be affected by a "real" delete
    try:
        product = Product.objects.get(pk=product_id)
        product.deleted = True
        product.save()
    except Product.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse("products.views.products_list"))


def delete_size(request, size_id):
    # A "real" delete function for product sizes
    try:
        size = ProductSize.objects.get(pk=size_id)
        size.delete()
    except Size.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse("products.views.sizes_list"))