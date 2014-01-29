# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('products/templatetags/paginator_widget.html', takes_context=True)
def paginator_widget(context, view_name, page_number, pages_total, items_per_page, qty_selector_enabled=False, delta=3):
    if pages_total > 1:
        qty_options = [5, 10, 20, 30, 50]
        qty_selector = []
        request = context.get('request')
        if request:
            get_params = request.GET.urlencode()
            get_params = "?" + get_params if get_params else ""
        else:
            get_params = ""
        if qty_selector_enabled:
            for item in qty_options:
                qty_selector.append((item, reverse(view_name, args=[page_number, item]) + get_params, True if item == items_per_page else False))

            if not items_per_page in qty_options:
                qty_selector.append((items_per_page, reverse(view_name, args=[page_number, items_per_page]) + get_params, True))
                qty_selector.sort(key=lambda x: x[0])

        paginator = []
        if 1 <= page_number <= delta + 1:
            pages_range = range(1, page_number + delta + 1,1) if pages_total > page_number + delta else range(1, pages_total+1,1)
            for item in pages_range:
                paginator.append((item, reverse(view_name, args=[item, items_per_page]) + get_params, True if item == page_number else False))
            if pages_total > page_number + delta+1:
                paginator.append(("...", None, False))
            if not pages_total in pages_range:
                paginator.append((pages_total, reverse(view_name, args=[pages_total, items_per_page]) + get_params, False))
        elif delta + 1 < page_number <= pages_total - delta - 1:
            paginator.append((1, reverse(view_name, args=[1, items_per_page]) + get_params, False))
            if page_number - delta !=2:
                paginator.append(("...", None, False))
            pages_range = range(page_number - delta, page_number + delta + 1,1)
            for item in pages_range:
                paginator.append((item, reverse(view_name, args=[item, items_per_page]) + get_params, True if item == page_number else False))
            if page_number + delta + 1 != pages_total:
                paginator.append(("...", None, False))
            paginator.append((pages_total, reverse(view_name, args=[pages_total, items_per_page]) + get_params, False))
        elif pages_total - delta - 1 < page_number:
            paginator.append((1, reverse(view_name, args=[1, items_per_page]) + get_params, False))
            if page_number - delta > 2:
                paginator.append(("...", None, False))
            pages_range = range(page_number - delta, pages_total + 1,1)
            for item in pages_range:
                paginator.append((item, reverse(view_name, args=[item, items_per_page]) + get_params, True if item == page_number else False))
        else:
    #        Error?
            pages_range = range(1, pages_total + 1,1)
            for item in pages_range:
                paginator.append((item, reverse(view_name, args=[item, items_per_page]) + get_params, True if item == page_number else False))

        first = reverse(view_name, args=[1, items_per_page]) + get_params
        last = reverse(view_name, args=[pages_total, items_per_page]) + get_params
        prev = next = None
        try:
            page_position = range(1, pages_total+1,1).index(page_number)
            if page_position > 0:
                prev = page_position
            if page_position + 1 < pages_total:
                next = page_position + 2
        except ValueError:
            pass
        prev = reverse(view_name, args=[prev, items_per_page]) + get_params if prev else None
        next = reverse(view_name, args=[next, items_per_page]) + get_params if next else None

    return locals()