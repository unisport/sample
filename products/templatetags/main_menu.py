from django import template

register = template.Library()


@register.inclusion_tag('products/templatetags/main_menu.html', takes_context=True)
def main_menu(context):
    request = context.get("request")
    return locals()