from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class PublicIndexViewTests(TestCase):
    def test_index_page_loads(self):
        """Going to the index page shows me log in info."""
        response = self.client.get(reverse('public:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Built for Humans")

    def test_early_access_valid(self):
        """Entering valid email redirects to thank you page."""
        with patch('tasks.mail_task.send_email_task.delay') as mock_task:
            response = self.client.post(
                reverse('public:index'), {
                    'email_address': 'test@tester.com'
                }, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Thank you!")
            self.assertTrue(mock_task.called)
