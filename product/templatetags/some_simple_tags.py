from django import template

register = template.Library()

# Check if the current page is Add a product or Update a product
@register.simple_tag()
def add_or_update(aURL, checkActive):
    if 'add' in aURL:
        if checkActive == '1':
            return 'active'
        else:
            return 'Add'
    else:
        if checkActive == '1':
            return ''
        else:
            return 'Update'


#   Printing the detail of a product
@register.simple_tag()
def boolStringCheck(aString):
    if aString == '1':
        return 'Yes'
    elif aString == '0':
        return 'No'
    else:
        return aString
