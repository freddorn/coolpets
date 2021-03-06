from django.test import TestCase
from products.models import Product


class ProductEntryTest(TestCase):
    """ Test Product model returns product title """

    def test_string_representation(self):
        product = Product(title="Test Product")
        self.assertEqual(str(product), product.title)

    def test_get_absolute_url(self):
        pk = 99
        title = "Test Product"
        expected_result = '/products/listing/' + str(pk) + '/'

        product = Product(pk=pk, title=title)
        result = Product.get_absolute_url(product)

        self.assertEqual(result, expected_result)
