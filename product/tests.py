from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import Product
import random




# Create your tests her
class ProductTest(TestCase):

    #####################
    #       SETUP
    def create_product(self,
                       _name='product_for_test1',
                       _price=50,
                       _price_old=70,
                       _currency='DKK',
                       _is_customizable=random.choice(['1', '0']),
                       _delivery=random.choice(['1', '0']),
                       _size='M',
                       _kids=random.choice(['1', '0']),
                       _kid_adult=random.choice(['1', '0']),
                       _free_porto=random.choice(['1', '0']),
                       _image='',
                       _package=random.choice(['1', '0']),
                       _url='',
                       _online=random.choice(['1', '0']),
                       _img_url='',
                       _women=random.choice(['1', '0'])):
        return Product.objects.create(name=_name,
                                      price=_price,
                                      price_old=_price_old,
                                      currency=_currency,
                                      is_customizable=_is_customizable,
                                      delivery=_delivery,
                                      size=_size,
                                      kids=_kids,
                                      kid_adult=_kid_adult,
                                      free_porto=_free_porto,
                                      image=_image,
                                      package=_package,
                                      url=_url,
                                      online=_online,
                                      img_url=_img_url,
                                      women=_women)

    #####################################################
    #                                                   #
    #                   Models test                     #
    #                                                   #
    #####################################################

    def test_product_creation(self):
        prod = self.create_product()

        # Test if the object is created
        self.assertTrue(isinstance(prod, Product))

        # Test if the field "name" is correctly created
        self.assertEqual(prod.name,'product_for_test1')

        # Test the function get_fields inside the model
        self.assertEqual(len(prod.get_fields()), 17)

        # Test the function get_absolute_url inside the model
        self.assertEqual(prod.get_absolute_url(), '/product/1/')


    #####################################################
    #                                                   #
    #                   Views  test                     #
    #                                                   #
    #####################################################

    """
    If no product exist, an appropriate message should be displayed.
    """
    def test_no_product_created(self):
        # SETUP
        client = Client()

        response = client.get(reverse('product:product'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No product is found. The list might be empty')
        self.assertQuerysetEqual(response.context['all_products'], [])

    """
    Test if any kid product is created
    """
    def test_product_list_view(self):
        # SETUP
        client = Client()
        prod = self.create_product()

        """
        If the list of product is not empty
        """
        response = client.get(reverse('product:product'))
        self.assertEqual(len(response.context['all_products']),1)

        # CREATE a kid product
        kids_prod = self.create_product(
                       _name='product_for_test_kids',
                       _price=150,
                       _price_old=70,
                       _currency='DKK',
                       _is_customizable='1',
                       _delivery='1',
                       _size='S',
                       _kids='1',
                       _kid_adult='1',
                       _free_porto=0,
                       _image='',
                       _package='1',
                       _url='',
                       _online='0',
                       _img_url='',
                       _women='0')

        """
        If the list of product now has 2 products
        """
        response = client.get(reverse('product:product'))
        self.assertEqual(len(response.context['all_products']), 2)

        """
        If the list of kid product now has maximum 2 products (because of the randomness)
        """
        kids_response = client.get(reverse('product:kidsView'))
        self.assertLessEqual(len(kids_response.context['kids_products']), 2)


    """
    Test if the list of product is sorted from cheapest
    This test is performed by 
        1) creating 10 product objects with random prices and putting in a list
        2) sorting this list after the price from smallest to highest (float data type)
        3) retrieving the price list above
        4) retrieving the raw list of the prices of 10 products displayed on the view
        5) comparing these 2 lists if they are identical
    """
    def test_list_of_product_sorted_from_cheapest(self):

        #SETUP for test
        client = Client()

        #SETUP of creation of product
        N = 10
        sample_prices_list = [round(random.uniform(1, 500), 2) for _ in range(N)]

        #Define main list to use
        list_of_10_products = []

        # Randomly create 10 products
        for i in range(N):
            prod_name = 'Test_product' + str(i)
            prod = self.create_product(_name=prod_name, _price=sample_prices_list[i])
            list_of_10_products.append(prod)

        sorted_list = sorted(list_of_10_products, key= lambda x: x.price)

        response = client.get(reverse('product:product'))
        self.assertEqual(response.status_code, 200)
        self.assertListEqual([float(p.price) for p in response.context['all_products']], [p1.price for p1 in sorted_list])
        #self.assertListEqual([p.price for p in response.context['all_products']], list_of_10_products.sort(key= lambda x: x.price))
        #self.assertListEqual(response.context['all_products'], list_of_10_products.sort(key=lambda x: x.price))


    """
    Test detail view
    """
    def test_detail_View(self):
        # SETUP
        client = Client()
        prod = self.create_product()

        response_detail = client.get(reverse('product:detail', args=(prod.id,)))
        self.assertEqual(response_detail.status_code, 200)


    """
    Test Add view
    """
    def test_add_view(self):
        # SETUP
        client = Client()

        response_add = client.get(reverse('product:product-add'))
        self.assertEqual(response_add.status_code, 200)


