from django.core.urlresolvers import resolve, reverse
from django.http import Http404, HttpRequest
from django.test import TestCase
from django.core.serializers.json import DjangoJSONEncoder
from products.views import ProductView, kids, Product
import json


class TestProducts(TestCase):

    def setUp(self):
        Product.reload_data()

    def test_url_accordance(self):
        template = "{0}.{1}"
        urls = ['/products/', '/products/1/', '/products/999999/']
        view_path = template.format(ProductView.__module__, ProductView.__name__)

        for url in urls:
            func = resolve(url).func
            res_view_path = template.format(func.__module__, func.func_name)
            self.assertEqual(res_view_path, view_path)

        func = resolve('/products/kids/').func
        self.assertEqual(func, kids)

    def test_response_status(self):

        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('kids'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get('{0}?page=1'.format(reverse('products')))
        self.assertEqual(response.status_code, 200)

        random_id = Product.objects.order_by('?').values_list('pk',
                                                              flat=True).first()
        response = self.client.get('{0}{1}/'.format(reverse('products'), random_id))
        self.assertEqual(response.status_code, 200)

        Product.objects.filter(pk=random_id).delete()
        response = self.client.get('{0}{1}/'.format(reverse('products'), random_id))
        self.assertEqual(response.status_code, 404)

        response = self.client.get('{0}?page=helloWorld'.format(reverse('products')))
        self.assertEqual(response.status_code, 400)

    def test_wrong_id_exception_404(self):
        request = HttpRequest()
        request.method = 'GET'
        fake_id = random_id = Product.objects.order_by('?').values_list('pk',
                                                                        flat=True).first()
        Product.objects.filter(pk=random_id).delete()
        self.assertRaises(Http404, ProductView.as_view(), request, fake_id)

    def test_kids_response(self):
        if not Product.objects.filter(kids='1').exists():
            Product.objects.update(kids='1')

        response = self.client.get(reverse('kids'))
        raw_products = json.loads(response.content)
        for raw_product in raw_products:
            self.assertEqual(raw_product.get('kids', '0'), '1')

    def test_products_page_response(self):
        page = 2

        response = self.client.get('{0}?page={1}'.format(reverse('products'), page))
        raw_products = json.loads(response.content)
        self.assertTrue(len(raw_products) <= ProductView.products_on_page)

        end = page * ProductView.products_on_page
        begin = end - ProductView.products_on_page

        product_list = list(Product.objects.order_by('price').values()[begin:end])
        from_db = json.loads(json.dumps(product_list, cls=DjangoJSONEncoder))
        self.assertListEqual(raw_products, from_db)

    def test_products_response(self):
        response = self.client.get(reverse('products'))
        raw_products = json.loads(response.content)
        self.assertTrue(len(raw_products) <= ProductView.products_on_page)

        product_list = list(Product.objects.order_by('price').values()[:10])
        from_db = json.loads(json.dumps(product_list, cls=DjangoJSONEncoder))
        self.assertListEqual(raw_products, from_db)

    def test_products_id_response(self):
        random_id = Product.objects.order_by('?').values_list('pk',
                                                              flat=True).first()
        response = self.client.get('{0}{1}/'.format(reverse('products'), random_id))
        raw_products = json.loads(response.content)
        self.assertEqual(random_id, raw_products['id'])

        product = Product.objects.values().get(pk=random_id)
        from_db = json.loads(json.dumps(product, cls=DjangoJSONEncoder))
        self.assertDictEqual(raw_products, from_db)