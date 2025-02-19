from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class signUp(TestCase):
    def test_signup_password_mismatch(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password': 'Legitplug',
            'password2': 'Legitplug'
        })
        self.assertEqual(response.status_code, 200)  # Should not redirect
        self.assertFalse(User.objects.filter(username='testuser2').exists())  # User should NOT be created
        self.assertContains(response, "The two password fields didn’t match")  # Error message
