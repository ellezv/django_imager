"""Tests for Imager Site."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "Imgr User {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@datsite.com".format(x.username.replace(" ", ""))
    )


class ImagerProfileCase(TestCase):
    """The Profile Model Test Runner."""

    def setUp(self):
        """DB setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]

    def test_profile_made_when_user_saved(self):
        """Test that making a user also makes a profile."""
        self.assertTrue(ImagerProfile.objects.count() == 10)

    def test_profile_same_data_as_user(self):
        uid = User.objects.first().id
        self.assertTrue(ImagerProfile.objects.filter(id=uid).first().user.username == User.objects.first().username)

    def test_delete_user_cascades(self):
        """Test that deleting a User deletes the Profile."""
        uid = User.objects.first().id
        test_user = User.objects.filter(id=uid).first()
        test_user.delete()
        self.assertTrue(len(ImagerProfile.objects.filter(id=uid)) == 0)

    def test_delete_user_cascades_model_len(self):
        """Test that deleting a User deletes the Profile in the model length."""
        uid = User.objects.first().id
        test_user = User.objects.filter(id=uid).first()
        test_user.delete()
        self.assertTrue(len(ImagerProfile.objects.all()) == 9)

    def test_profile_model_is_active(self):
        """Test that the profile isactive param is true."""
        self.assertTrue(ImagerProfile.objects.first().is_active)

