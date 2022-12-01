from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from .models import User

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testemail',
            'first_name': 'testfirst',
            'last_name': 'testlast',
            'bio': 'testbio',
            'profile_pic': 'testpic',
            'created_at': 'testcreated'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
