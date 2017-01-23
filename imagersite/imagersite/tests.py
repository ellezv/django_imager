"""Tests for Imager Site."""
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile

from imager_images.tests import UserFactory, ImageFactory, AlbumFactory


class FrontEndTests(TestCase):
    """Tests for our front-end."""

    def setUp(self):
        """Set up the tests."""
        self.client = Client()
        self.request = RequestFactory()
        # self.user = [UserFactory.create() for i in range(10)]
        self.images = [ImageFactory.create() for i in range(10)]
        self.album = [AlbumFactory.create() for i in range(10)]

    def test_profile_view(self):
        """Test profile view status code."""
        from imager_profile.views import profile_view
        req = self.request.get("/profile")
        some_user = UserFactory.create()
        req.user = some_user
        response = profile_view(req)
        self.assertEqual(response.status_code, 200)

    def test_profile_route_uses_right_template(self):
        """Test profile view renders correct template."""
        response = self.client.get("/profile")
        self.assertTemplateUsed(response, 'imager_profile/detail.html')

    def test_home_view_status(self):
        """Test home view is accessible."""
        from imagersite.views import home_view
        req = self.request.get("/")
        response = home_view(req)
        self.assertEqual(response.status_code, 200)

    def test_home_route_uses_right_template(self):
        """Test that home route uses the expected template."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'imagersite/home.html')

    def test_login_view_status(self):
        """Test login view is accessible."""
        from django.contrib.auth.views import login
        req = self.request.get("/")
        response = login(req)
        self.assertEqual(response.status_code, 200)

    def test_login_route_uses_right_template(self):
        """Test that the login route uses the expected template."""
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_register_view_status(self):
        """Test register view status code is 200."""
        from registration.backends.hmac.views import RegistrationView
        req = self.request.get("/")
        response = RegistrationView.as_view()(req)
        self.assertEqual(response.status_code, 200)

    def test_login_view_redirects(self):
        """Test successful redirect once logged-in."""
        new_user = UserFactory.create()
        new_user.username = "test_user"
        new_user.set_password("test_password")
        new_user.save()
        response = self.client.post('/login/', {
            "username": new_user.username,
            "password": "test_password"}, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)

    def test_can_register_new_user(self):
        """Test a new user can register."""
        user_count = User.objects.count()
        self.client.post('/registration/register/', {
            "username": "test_user",
            "email": "test@user.com",
            "password1": "testpassword",
            "password2": "testpassword"
        })
        self.assertTrue(User.objects.count() == user_count + 1)
        self.assertTrue(User.objects.first().username == "test_user")

    def test_register_user_is_inactive(self):
        """Test that a newly registered user is inactive."""
        user_count = User.objects.count()
        self.client.post('/registration/register/', {
            "username": "test_user",
            "email": "test@user.com",
            "password1": "testpassword",
            "password2": "testpassword"
        })
        self.assertTrue(User.objects.count() == user_count + 1)
        self.assertTrue(ImagerProfile.active.count() == user_count)
