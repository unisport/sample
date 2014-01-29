# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.utils.http import urlencode

register = template.Library()


@register.inclusion_tag('products/templatetags/sort_widget.html',takes_context = True)
def sort_widget(context, sort_params, sort_key, sort_dir, view_name, extra_args):
    request = context.get('request')
    if request:
        get_params = dict(request.GET)
    else:
        get_params = {}
    buff_get_params = {}
    for key, value in get_params.items():
        if value:
            buff_get_params[key] = value[0]
    get_params = buff_get_params
    sort_menu = []
    for item in sort_params:
        if item["sort"]:
            if item["sort"]["key"] == sort_key:
                item["sort"]["active"] = sort_dir
                this_sort_dir = "asc" if sort_dir == "desc" else "desc"
            else:
                this_sort_dir = "asc"
            get_params["sort_key"] = item["sort"]["key"]
            get_params["sort_dir"] = this_sort_dir
            item["url"] = reverse(view_name, args=extra_args) + "?" + urlencode(get_params)
        sort_menu.append(item)
    return locals()