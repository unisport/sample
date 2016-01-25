from django.test import TestCase
from mock import MagicMock
from views import *


class ProductsViewTestCase(TestCase):
    def setUp(self):
        self.request = MagicMock()
        self.request.method = 'GET'
        
    def test_pagination(self):
        view = ProductsView()
        self.request.GET = {'page':1}
        response1 = view.get(self.request)
        self.request.GET = {'page': 'unexpected'}
        response2 = view.get(self.request)
        self.assertEqual(response1.content, response2.content)
        self.request.GET = {'page': u'99999'}
        response1 = view.get(self.request)
        num_pages = view.pagination(self.request).paginator.num_pages
        self.request.GET = {'page': num_pages}
        response2 = view.get(self.request)
        self.assertEqual(response1.content, response2.content)

