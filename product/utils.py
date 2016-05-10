from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

'''
pagination handler, creates paginated object from queryset and params from settings,
optional params: items on page, list of pagination pages to show
'''
def paginate_objects(queryset, page):
    paginator = Paginator(queryset, settings.DEFAULT_ITEMS_PER_PAGE)
    if not page:
        page = 1
    index = int(page) - 1
    start_page = index-settings.PAGINATION_PAGES if index > settings.PAGINATION_PAGES else 0
    end_page = index+settings.PAGINATION_PAGES if index+settings.PAGINATION_PAGES < paginator.num_pages else paginator.num_pages
    short_page_range = paginator.page_range[start_page:end_page]
    setattr(paginator, 'short_page_range', short_page_range)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects


# price parser to make it float
def price_handler(price):
    return (price.replace('.', '')).replace(',', '.')
