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
