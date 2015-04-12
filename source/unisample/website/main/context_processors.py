from django.utils import formats

def add_formats(request):
    return {
        'JS_DATE_FORMAT':  formats.get_format("JS_DATE_FORMAT"),
        'JS_DATETIME_FORMAT':  formats.get_format("JS_DATETIME_FORMAT"),
    }
