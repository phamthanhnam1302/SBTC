from django.test import Client, TestCase


class CoreErrorTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_urls_are_available_for_guest(self):
        """The 404 page renders a custom template"""
        response = self.guest_client.get('/unexisting_page/')
        self.assertTemplateUsed(
            response,
            'core/404.html',
            '404 page not using custom template'
        )
