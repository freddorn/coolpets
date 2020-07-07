from django.test import TestCase
from django.contrib.auth.models import User
from cart.models import ShippingDestination, Order, OrderItem
from products.models import Product
from django.test import Client, RequestFactory


class ShippingDestinationEntryTest(TestCase):

    def test_string_representation(self):

        sd = ShippingDestination(country="Test")
        self.assertEqual(str(sd), sd.country)

    def test_default_shipping_time(self):

        sd = ShippingDestination(country="Test")
        self.assertEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_time(self):

        sd = ShippingDestination(country="Test", shipping_time="42 years")
        self.assertNotEqual(sd.shipping_time, "1 to 2 weeks")

    def test_add_shipping_price(self):

        sd = ShippingDestination(country="Test", shipping_price=42)
        self.assertEqual(sd.shipping_price, 42)
        self.assertNotEqual(sd.shipping_price, 99.99)


class OrderItemEntryTest(TestCase):

    def test_string_representation(self):

        product = Product(title="Test Product")
        order = Order(full_name="John Wayne")
        order_item = OrderItem(order=order, product=product, quantity=3)

        expected_result = '3 x Test Product'

        self.assertEqual(str(order_item), expected_result)

    def test_order_id_on_order_item(self):

        product = Product(title="Test Product")
        order = Order(id=42, full_name="John Wayne")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.order.id, 42)

    def test_product_id_in_order_item(self):

        product = Product(id=99, title="Test Product")
        order = Order(id=42, full_name="John Wayne")
        order_item = OrderItem(order=order, product=product, quantity=3)

        self.assertEqual(order_item.product.id, 99)


class OrderEntryTest(TestCase):

    def test_string_representation(self):

        user = User(username="Longmire")
        order = Order(id=42, date_ordered='2020-07-06', customer=user)

        expected_result = '42-2020-07-06-Longmire'

        self.assertEqual(str(order), expected_result)

    def test_default_values(self):

        user = User(username="Longmire")
        order = Order(id=42, date_ordered='2020-07-06', customer=user)

        self.assertEqual(order.paid, False)
        self.assertEqual(order.shipped, False)


class TestCartViewLoggedOut(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):

        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/")


class TestCartViewLoggedIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )

    def test_response_status_200(self):

        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_load_page_with_no_cart_contents(self):

        client = Client()
        client.login(username='testuser', password="testing321")

        response = client.get('/cart/')
        context = response.context
        self.assertTrue(context['nothing_in_cart'])


class TestCheckoutInfoViewLoggedPut(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response_redirect(self):

        response = self.client.get('/cart/checkout/info/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, "/accounts/login/?next=/cart/checkout/info/")


class TestCheckoutInfoViewLoggedIn(TestCase):
    """ Test for checkout info view when user is logged out """

    def setUp(self):

        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testing321"
        )

    def test_user_logged_in_but_nothing_in_cart_redirect(self):

        # logs user in
        client = Client()
        client.login(username='testuser', password="testing321")

        # gets response
        response = client.get('/cart/checkout/info/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/cart/")

    def test_post_new_order_form_correct(self):

        # create client and log them in
        client = Client()
        client.login(username='testuser', password="testing321")

        # create product in database
        product = Product()
        product.id = 3
        product.price = 20
        product.num_in_stock = 10
        product.description = "description"
        product.tags = "tags"
        product.save()

        country = ShippingDestination.objects.create(
            country="US", shipping_price=10)
        Order.objects.create(customer=self.user)

        # create session data for product
        session = client.session
        session['cart'] = {'orderItems': [
            {'listingId': 3, 'quantity': 1}], 'total': 20, 'count': 1}
        session.save()

        client.post(
            '/cart/checkout/info/',
            {
                'full_name': 'John Wayne',
                'address_line_1': '1234 Test',
                'town_or_city': 'City',
                'state': 'State',
                'postcode': '12345',
                'country': country.id,
            }
        )

        order = Order.objects.filter(customer=self.user).first()
        self.assertEqual(order.full_name, "John Wayne")
        self.assertEqual(order.state, "State")
        self.assertEqual(order.country, country)
        self.assertIsInstance(order, Order)
