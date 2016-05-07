import unittest
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from .views import CatalogView


class CatalogViewTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        request = self.factory.get(reverse('catalog'))
        response = CatalogView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class CatalogKidsViewTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        request = self.factory.get(reverse('kids'))
        response = CatalogView.as_view()(request)
        self.assertEqual(response.status_code, 200)
