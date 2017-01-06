from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from sample.views import index


class TestHomePage(TestCase):

    def test_url_resolves_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_url_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertTrue(b'<html>' in response.content)
        self.assertTrue(b'</html>' in response.content)



