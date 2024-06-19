"""teste for models """

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """test models"""

    def test_create_user_wth_email_successful(self):
        """test creating user with email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email, password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@Example.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],]

        for email , expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_witout_email(self):
        """test creating user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')