import logging
from contextlib import contextmanager
from unittest import TestCase

from django.http import JsonResponse

from products.decorators import error_on_exception


class ErrorOnExceptionTest(TestCase):
    def test_preserves_return_value_on_success(self):
        def original_function():
            return 97

        decorated = error_on_exception(original_function)

        self.assertEqual(decorated(), 97)

    def test_returns_json_response_on_error(self):
        def original_function():
            raise Exception('Exception message')

        decorated = error_on_exception(original_function)
        with _suppress_logger('products.decorators'):
            response = decorated()

        self.assertEqual(response.status_code, 500)
        self.assertIsInstance(response, JsonResponse)

    def test_error_response_contains_message(self):
        def original_function():
            raise Exception('Exception message')

        decorated = error_on_exception(original_function)
        with _suppress_logger('products.decorators'):
            response = decorated()

        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Unexpected error', response.content)


@contextmanager
def _suppress_logger(logger_name):
    def _reject_all_records(record):
        return False

    logger = logging.getLogger(logger_name)
    logger.addFilter(_reject_all_records)
    try:
        yield
    finally:
        logger.removeFilter(_reject_all_records)
