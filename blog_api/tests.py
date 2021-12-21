from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.urls import reverse

class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse('blog_api:listcreate_api')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create_user(username='test_user1', password='test_user1')
        data ={'title':'new', 'author':1, 'content':'new'}
        url = reverse('blog_api:listcreate_api')
        response = self.client.post(url, data, formate='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        