from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from products.models import Product

class ProductListTest(TestCase):

	def setUp(self):
		#create products

		#instance of test browsr
		self.client = Client()

		#Create test data (products items)
		#set value only for mandatory fields (fields without 'default=' and 'null=True' params)
		Product.objects.get_or_create(
			name='Test name1',
			currency='DKK',
			delivery='1-2 days',
			price='1',
			price_old='10')
		
		Product.objects.get_or_create(
			name='Test name2',
			currency='DKK',
			delivery='1-2 days',
			price='2',
			price_old='20')
		Product.objects.get_or_create(
			name='Test name3',
			currency='DKK',
			delivery='1-2 days',
			price='3',
			price_old='30')

		#url to products page 
		self.url = reverse('products_list')

	def test_products_list(self):
		"Test corect rendering of product_list"
		#make request to url with products list and get response
		response = self.client.get(self.url)

		#checking server answer code (OK)
		self.assertEqual(response.status_code, 200)

		#checking that our page(content) show items
		self.assertIn('Test name1', response.content)

		#check that our page(content) show all creted items
		self.assertEqual(len(response.context['products']), 3)

		#check corect data in one product (price) 
		self.assertEqual(response.context['products'][1].price, 2)

class ProductsListPaginationTest(TestCase):

    def setUp(self):
        self.products = []
        for i in range(15):
            product = Product.objects.create(
            	name='Test name %d' % i,
				currency='DKK %d' % i,
				delivery='1-2 days %d' % i,
				price='1%d' % i,
				price_old='10%d' % i)
                
            
            self.products.append(product)

        self.client = Client()
        self.url = reverse('products_list')

    def test_pagination(self):
    	"Test pagination"

    	response = self.client.get(self.url)
    	self.assertEqual(response.status_code, 200)

    	self.url =  '%s?page=2' % reverse('products_list')
    	self.assertEqual(len(response.context['products']), 5)