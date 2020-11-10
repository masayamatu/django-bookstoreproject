from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='kobayashi',
            email='kobayashi@email.com',
            password='testkobayashi'
        )
        self.assertEqual(user.username,'kobayashi')
        self.assertEqual(user.email,'kobayashi@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    def test_create_superudser(self):
        User=get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superkobayashi',
            email='superkobayashi@email.com',
            password = 'testsuperkobayashi'
        )
        self.assertEqual(admin_user.username,'superkobayashi')
        self.assertEqual(admin_user.email,'superkobayashi@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
# Create your tests here.
