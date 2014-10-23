__author__ = 'azhukov'

from django.core.urlresolvers import reverse
from rest_framework.test import APIClient, APITestCase

from models import Item
import settings


class ItemListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('products')
        self.all_items = Item.objects.all().order_by('price')

    def test_get_items_list(self):
        response = self.client.get(reverse('products'))
        items = response.data['results']
        self.assertEqual(len(items), settings.REST_FRAMEWORK['PAGINATE_BY'])
        self.assertEqual(list(sorted(items, key=lambda item: item['price'])), items)

    def test_pagination(self):
        response = self.client.get(reverse('products'), data={'page': 2})
        items = response.data['results']
        print self.all_items
        self.assertEqual(
            [item['id'] for item in items],
            [item.id for item in self.all_items[10:20]]
        )

    def test_create_item(self):
        data = dict(id='1', name='Test item', sizes='test')
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.data['name'], data['name'])


class ItemSingleViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.item_id = "93590"

    def test_get_item(self):
        response = self.client.get(reverse('item_single', args=(self.item_id,)))
        self.assertEqual(response.data['id'], self.item_id)

    def test_update_item(self):
        data = dict(name='Updated name')
        response = self.client.patch(reverse('item_single', args=(self.item_id,)), data=data)
        self.assertEqual(response.data['name'], data['name'])


class ItemKidsListTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_items(self):
        response = self.client.get(reverse('products_kids'))
        self.assertTrue(all([item['kids'] is True] for item in response.data['results']))



