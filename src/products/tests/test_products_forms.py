from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from products.models import Product
from products.forms import ProductModelForm


class ProductUpdateFormTest(TestCase):

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

		self.url = reverse('update_product', kwargs={'pk': 1})

	def test_form_rendering(self):
		"Test rendering page elements (fields, buttons, urls) in update_product form"

		#make request to url with products list and get response
		response = self.client.get(self.url)

		#checking server answer code (OK)
		self.assertEqual(response.status_code, 200)

		# check necessary page elements existing 
		self.assertIn('Create Product', response.content)
		self.assertIn('Name', response.content)
		self.assertIn('Price', response.content)
		self.assertIn('name="add_button"', response.content)
		self.assertIn('action="%s"' % self.url, response.content)
		self.assertIn(str(reverse('products_list')), response.content)



	def test_updating_product(self):
		"Test updating product data via update_product form"


		response = self.client.get(self.url)

		self.assertEqual(response.status_code, 200)

		#fill up the form with new data
		#need to set all fields, because request.POST it is a dictonary of all {field_name:value}
		#and default fealds do not adding to it automaticaly 
		response = self.client.post(self.url, {
			'name': 'Updated Name',
            'currency': 'Updated Currency', 
            'delivery': 'Updated Delivery',
            'price': '777', 
            'price_old': '888',
            'kid_adult':'0',
			'women':'0', 
			'kids':'0', 
			'package':'0'}, follow=True)




		# check response status after updeting
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('product_detail', kwargs={'pk': 1}))

		self.assertEqual(response.status_code, 200)

		product = Product.objects.get(pk=1)


		self.assertEqual(product.name, 'Updated Name')
		self.assertEqual(product.currency, 'Updated Currency')
		self.assertEqual(product.delivery, 'Updated Delivery')
		# self.assertEqual(product.)

	


class ProductUpdateFormDataTest(TestCase):

	def setUp(self):
		#create products

		#instance of test browsr
		self.client = Client()

		#Create test data (products items)
		#set value only for mandatory fields (fields without 'default=' and 'null=True' params)
		self.url = reverse('update_product', kwargs={'pk': 1})


	def test_valid_form(self):
		"Test form with valid fields values"

		p = Product.objects.create(
			name='One', 
			currency='Two', 
			delivery='Three', 
			price='5',
			price_old='6',
			kid_adult='7',
			women='8',
			kids='9',
			package='10')

		data = {'name':p.name,'currency':p.currency,'delivery':p.delivery, 
			'price':p.price, 
			'price_old':p.price_old,
			'kid_adult':p.kid_adult,
			'women':p.women, 
			'kids':p.kids, 
			'package':p.package}
		form = ProductModelForm(data=data)

		# if you got fail, try to look at form.errors output
		print (form.errors)
		self.assertTrue(form.is_valid())

        
	def test_invalid_form(self):
		"Test form with invalid or empty required fields values. Forms errors:"

		data = {
			'name':'TestName',
			'currency':'', 
			'delivery':'1-2 days', 
			}
		form = ProductModelForm(data=data)
		# send to output errors from form
		print (form.errors.as_data())
		self.assertFalse(form.is_valid(),)






		
       