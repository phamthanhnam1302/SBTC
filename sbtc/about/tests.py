from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.user = User.objects.create_user(username='tester')
        self.authorized_client.force_login(self.user)

    def test_urls_are_available_for_guest(self):
        """ Checking access to pages without authorization """
        urls_loggedout = {
            '/about/tech/': HTTPStatus.OK,
            '/about/author/': HTTPStatus.OK,
            '/about/new': HTTPStatus.NOT_FOUND,
        }
        for url, status in urls_loggedout.items():
            with self.subTest(status=status):
                response = self.guest_client.get(url)
                self.assertEqual(
                    response.status_code,
                    status,
                    f'Error accessing {url} without authorization'
                )

    def test_urls_are_available_for_authorized(self):
        """ Authorized access check """
        urls_loggedin = {
            '/about/tech/': HTTPStatus.OK,
            '/about/author/': HTTPStatus.OK,
            '/about/new': HTTPStatus.NOT_FOUND,
        }
        for url, status in urls_loggedin.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(
                    response.status_code,
                    status,
                    f'Error accessing {url} with authorization'
                )

    def test_urls_use_correct_template(self):
        """The URL uses the appropriate pattern."""
        templates_url_names = {
            '/about/tech/': 'about/tech.html',
            '/about/author/': 'about/author.html',
        }
        for url, template in templates_url_names.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(
                    response,
                    template,
                    f'Error using template for {url}'
                )
