from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse


class RegistrationRegisterViewTest(TestCase):
    def test_registration(self):
        """Going to the registration page shows a registration form."""
        response = self.client.get(reverse('registration:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign up for Rolorex")

    def test_valid_registration(self):
        """Entering valid input to the registration form redirects me to the index."""
        response = self.client.post(reverse('registration:register'), {
            'username': 'tester',
            'email': 'test@tester.com',
            'password': 'super-security'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Built for Humans")

        new_user = User.objects.get(username='tester')
        self.assertEqual(new_user.email, 'test@tester.com')

    def test_invalid_registration(self):
        """Entering invalid input to the registration form returns an error."""
        response = self.client.post(reverse('registration:register'), {
            'username': 'tester',
            'email': 'notanemail',
            'password': 'super-security'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")

        with self.assertRaises(ObjectDoesNotExist):
            new_user = User.objects.get(username='tester')

        response = self.client.post(reverse('registration:register'), {
            'username': '',
            'email': 'notanemail',
            'password': 'super-security'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")

        with self.assertRaises(ObjectDoesNotExist):
            new_user = User.objects.get(username='tester')
