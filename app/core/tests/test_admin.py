"""
test for the django admin modifications.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    """test for django admin."""

    def setUp(self):
        """create user and client """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123', )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='test user', )

    def test_users_list(self):
        """tests that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """test the edit userspace works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test the create userpage works."""
        url = url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
