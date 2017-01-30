import logging
from functools import wraps

from django.conf import settings
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def error_on_exception(view):
    """Returns a JsonResponse with an error message when exception happens.

    When in debug mode, exception will be reraised and a standard Django error
    page will be shown.
    """
    @wraps(view)
    def wrapper(*args, **kwargs):
        try:
            return view(*args, **kwargs)
        except Exception as exc:
            if settings.DEBUG:
                raise
            logger.exception('An error occurred when handling an API request.',
                             exc_info=exc)
            return JsonResponse({
                'error': {
                    'message': 'Unexpected error occurred.'
                }
            }, status=500)
    return wrapper
