from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import about_view, contact_view
from django.test import Client, TestCase
from pages.forms import ContactForm


class TestUrls(SimpleTestCase):

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact_view)


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('index.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))


class TestAboutView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/about/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('about.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))


class TestContactView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/pages/contact/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/pages/contact/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('contact.html', str(names))
        self.assertIn('components/navbar.html', str(names))
        self.assertIn('components/footer.html', str(names))

    def test_contact_form_in_context(self):
        response = self.client.get('/pages/contact/')
        form = response.context['form']

        self.assertEqual(type(form), ContactForm)


# Helper functions


def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names
