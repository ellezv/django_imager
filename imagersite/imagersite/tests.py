"""Tests for Imager Site."""
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile

import factory


class FrontEndTests(TestCase):
    """Tests for our front-end."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()

    def test_home_view_status(self):
        """."""
        from imagersite.views import home_view
        req = self.request.get("/home")
        response = home_view(req)
        self.assertEqual(response.status_code, 200)

    def test_login_view_status(self):
        """."""
        from django.contrib.auth.views import login
        req = self.request.get("/")
        response = login(req)
        self.assertEqual(response.status_code, 200)

    def test_register_view_status(self):
        from registration.backends.hmac.views import RegistrationView
        req = self.request.get("/")
        response = RegistrationView.as_view()(req)
        self.assertEqual(response.status_code, 200)
