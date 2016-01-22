import json
from django.test import TestCase

from ..models import Product, Size


class ProductModelTest(TestCase):
    """
    Test model Product (CRUD and methods)
    """
    @staticmethod
    def create_example():
        obj = Product.objects.create(
            name='Example',
            url='http://example.com',
            kid_adult='0',
            kids='0',
            women='0',
            free_porto='0',
            price=100.15,
            price_old=100,
            package='0',
            delivery='1 day',
            img_url='http://example.com'
        )
        size = Size.objects.create(
            value='EU 34'
        )
        obj.sizes.add(size)
        obj.save()
        return obj

    def test_create_instance(self):
        self.assertEqual(Product.objects.count(), 0)
        obj = self.create_example()
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, obj.name)

    def test_edit_instance(self):
        obj = self.create_example()
        obj.name = "Boots"
        obj.save()
        self.assertEqual(Product.objects.first().name, "Boots")

    def test_delete_instance(self):
        obj = self.create_example()
        self.assertEqual(Product.objects.count(), 1)
        obj.delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_get_json_method(self):
        obj = self.create_example()
        self.assertEqual(json.loads(obj.get_json())['name'], 'Example')

    def test_get_size_method(self):
        obj = self.create_example()
        self.assertIn('EU', obj.get_sizes())


class SizeModelTest(TestCase):
    """
    Test model Size (CRUD and methods)
    """
    @staticmethod
    def create_example():
        return Size.objects.create(
            value='EU 34'
        )

    def test_create_instance(self):
        self.assertEqual(Size.objects.count(), 0)
        obj = self.create_example()
        self.assertEqual(Size.objects.count(), 1)
        self.assertEqual(Size.objects.first().value, obj.value)

    def test_edit_instance(self):
        obj = self.create_example()
        obj.value = "50"
        obj.save()
        self.assertEqual(Size.objects.first().value, "50")

    def test_delete_instance(self):
        obj = self.create_example()
        self.assertEqual(Size.objects.count(), 1)
        obj.delete()
        self.assertEqual(Size.objects.count(), 0)
