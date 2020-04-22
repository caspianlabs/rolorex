from django.test import TestCase
from django.urls import reverse


class PublicIndexViewTests(TestCase):
    def test_index_page_loads(self):
        """Going to the index page shows me log in info."""
        response = self.client.get(reverse('public:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Rolorex")

