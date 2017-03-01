from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from ..models import Product


User = get_user_model()

class ProductAPITest(APITestCase):

    fixtures = ['products.json']

    put_product_info = {
        "is_customizable": "0",
        "delivery": "None",
        "kids": "0",
        "name": "API product",
        "sizes": "One Size",
        "kid_adult": "0",
        "free_porto": "0",
        "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
        "package": "True",
        "price": "200.00",
        "url": "https://www.unisport.dk/gavekort/",
        "price_old": "300.00",
        "currency": "DKK",
        "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
        "id": "3",
        "women": "0",
        "online": "0"
    }

    def setUp(self):

        admin_user = User.objects.create_superuser(
            username='testuser', email='test@test.com', 
            password='test12345')

    def tearDown(self):
        admin_user = User.objects.get(email='test@test.com')
        admin_user.delete()

    def test_product_create(self):

        url = reverse('create_product')

        admin_user = User.objects.get(email='test@test.com')

        self.client.force_authenticate(user=admin_user)

        product_info = {
            "is_customizable": "0",
            "delivery": "None",
            "kids": "0",
            "name": "API product",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
            "package": "True",
            "price": "200.00",
            "url": "https://www.unisport.dk/gavekort/",
            "price_old": "300.00",
            "currency": "DKK",
            "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
            "id": "3",
            "women": "0",
            "online": "0"
        }

        response = self.client.post(url, data=product_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_update(self):

        admin_user = User.objects.get(email='test@test.com')

        self.client.force_authenticate(user=admin_user)

        put_data = {
            "is_customizable": "0",
            "delivery": "None",
            "kids": "0",
            "name": "New name",
            "sizes": "One Size",
            "kid_adult": "0",
            "free_porto": "0",
            "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
            "package": "True",
            "price": "200.00",
            "url": "https://www.unisport.dk/gavekort/",
            "price_old": "300.00",
            "currency": "DKK",
            "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
            "id": "3",
            "women": "0",
            "online": "0"
        }

        url = reverse('update_product', kwargs={'product_id': 23})

        response = self.client.put(url, data=put_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product_errors(self):

        url = reverse('create_product')

        admin_user = User.objects.get(email='test@test.com')

        self.client.force_authenticate(user=admin_user)

        invalid_data_dicts = [
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "",
                    "kids": "0",
                    "name": "",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "",
                    "currency": "",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "delivery": [
                        "This field may not be blank."
                    ],
                    "price_old": [
                        "A valid number is required."
                    ],
                    "price": [
                        "A valid number is required."
                    ],
                    "name": [
                        "This field may not be blank."
                    ],
                    "currency": [
                        "This field may not be blank."
                    ]
                }
            },
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "None",
                    "kids": "0",
                    "name": "",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "200.00",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "300.00",
                    "currency": "DKK",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "name": [
                        "This field may not be blank."
                    ]
                }
            },
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "",
                    "kids": "0",
                    "name": "Some Name",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "200.00",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "300.00",
                    "currency": "DKK",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "delivery": [
                        "This field may not be blank."
                    ]
                }
            },
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "1-2 days",
                    "kids": "0",
                    "name": "Some Name",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "200.00",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "",
                    "currency": "DKK",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "price_old": [
                        "A valid number is required."
                    ]
                }
            },
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "1-2 days",
                    "kids": "0",
                    "name": "Some Name",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "300.00",
                    "currency": "DKK",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "price": [
                        "A valid number is required."
                    ]
                }
            },
            {'data':
                {
                    "is_customizable": "0",
                    "delivery": "1-2 days",
                    "kids": "0",
                    "name": "Some Name",
                    "sizes": "One Size",
                    "kid_adult": "0",
                    "free_porto": "0",
                    "image": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "package": "True",
                    "price": "200.00",
                    "url": "https://www.unisport.dk/gavekort/",
                    "price_old": "300.00",
                    "currency": "",
                    "img_url": "https://dxjm75mafwy8p.cloudfront.net/product/1/e1daa14a0ea9.jpg",
                    "id": "3",
                    "women": "0",
                    "online": "0"
                },
            'errors':
                {
                    "currency": [
                        "This field may not be blank."
                    ]
                }
            }
        ]

        for invalid_dict in invalid_data_dicts:
            response = self.client.post(url, data=invalid_dict['data'], format='json')
            self.assertNotEqual(response.data, status.HTTP_201_CREATED)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(response.data, invalid_dict['errors'])


    def test_get_all_products(self):

        url = reverse('get_products')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 24)
        self.assertEqual(response.data["products"], 10)

    def test_get_all_products(self):

        url = reverse('get_kids_products')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 11)
        self.assertEqual(len(response.data["products"]), 10)

