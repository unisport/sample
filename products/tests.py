from django.core.urlresolvers import resolve, reverse
from django.http import Http404, HttpRequest
from django.test import TestCase
from products.views import products, product, kids


class TestProducts(TestCase):

    def test_url_resolves_products(self):
        url = resolve('/products/')
        self.assertEqual(url.func, products)

    def test_products_status(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_product(self):
        url = reverse('product', args=[51536])
        self.assertEqual(url, '/products/51536/')

    def test_wrong_id_raises_404(self):
        request = HttpRequest()
        fake_id = 000
        self.assertRaises(Http404, product, request, fake_id)

    def test_url_resolves_kids(self):
        url = resolve('/products/kids/')
        self.assertEqual(url.func, kids)

    def test_kids_status(self):
        response = self.client.get(reverse('kids'))
        self.assertEqual(response.status_code, 200)

    def test_kids_returns_data(self):
        response = self.client.get(reverse('kids'))
        prod = response.context['products'][0]
        self.assertTrue('kids' in prod)
        self.assertEqual(prod.get('kids'), '1')

    def test_products_page(self):
        page = 2
        response = self.client.get('/products/?page={0}'.format(page))
        prod = response.context['products']
        self.assertEqual(prod[10:20], prod[(page*10)-10:10*page])













