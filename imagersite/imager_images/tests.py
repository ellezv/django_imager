from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import ImagerProfile
from imager_images.models import Image, Album
from django.utils import timezone
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "Imgr User {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@datsite.com".format(x.username.replace(" ", ""))
    )


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image
    title = factory.Sequence(lambda n: "Image {}".format(n))


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    title = factory.Sequence(lambda n: "Album {}".format(n))


class ImageTestCase(TestCase):
    """The Image App Test Runner."""

    def setUp(self):
        """User setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]
        self.images = [ImageFactory.create() for i in range(10)]
        self.album = [AlbumFactory.create() for i in range(10)]

    def test_image_title(self):
        """Test that the image has a title."""
        # import pdb;pdb.set_trace()
        self.assertTrue("Image" in Image.objects.first().title)

    def test_image_has_description(self):
        """Test that the Image description field can be assigned."""
        image = Image.objects.first()
        image.description = "This is a good image."
        image.save()
        self.assertTrue(Image.objects.first().description == "This is a good image.")

    def test_image_has_published(self):
        """Test the image published field."""
        image = Image.objects.first()
        image.published = 'public'
        image.save()
        self.assertTrue(Image.objects.first().published == "public")

    def test_image_date_modified(self):
        """Test that the image has a date modified default."""
        image = Image.objects.first()
        # import pdb;pdb.set_trace()
        self.assertTrue(image.date_modified)

    def test_image_date_uploaded(self):
        """Test that the image has a date uploaded default."""
        image = Image.objects.first()
        # import pdb;pdb.set_trace()
        self.assertTrue(image.date_uploaded)

    def test_image_no_date_date_published(self):
        """Test that the image does not have a date published before assignment."""
        image = Image.objects.first()
        self.assertFalse(image.date_published)

    def test_image_date_date_published(self):
        """Test that the image has a date published after assignment."""
        image = Image.objects.first()
        image.date_published = timezone.now
        self.assertTrue(image.date_published)

    def test_image_has_no_owner(self):
        """Test that image has no owner."""
        image = Image.objects.first()
        self.assertFalse(image.owner)

    def test_image_has_owner(self):
        """Test that image has an owner after assignment."""
        image = Image.objects.first()
        user1 = User.objects.first()
        image.owner = user1.profile
        self.assertTrue(image.owner)

    def test_owner_has_image(self):
        """Test that the owner has the image."""
        image = Image.objects.first()
        user1 = User.objects.first()
        image.owner = user1.profile
        image.save()
        # import pdb; pdb.set_trace()
        self.assertTrue(user1.profile.images.count() == 1)

    def test_two_images_have_owner(self):
        """Test two images have the same owner."""
        image1 = Image.objects.all()[0]
        image2 = Image.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.assertTrue(image1.owner == user1.profile)
        self.assertTrue(image2.owner == user1.profile)

    def test_owner_has_two_images(self):
        """Test that owner has two image."""
        image1 = Image.objects.all()[0]
        image2 = Image.objects.all()[1]
        user1 = User.objects.first()
        image1.owner = user1.profile
        image2.owner = user1.profile
        image1.save()
        image2.save()
        self.assertTrue(user1.profile.images.count() == 2)

    def test_image_has_no_album(self):
        """Test that the image is in an album."""
        image = Image.objects.first()
        self.assertTrue(image.albums.count() == 0)

    def test_image_has_album(self):
        """Test that the image is in an album."""
        image = Image.objects.first()
        album1 = Album.objects.first()
        image.albums.add(album1)
        self.assertTrue(image.albums.count() == 1)

    def test_album_has_no_image(self):
        """Test that an album has no image before assignemnt."""
        album1 = Album.objects.first()
        self.assertTrue(album1.images.count() == 0)

    def test_album_has_image(self):
        """Test that an album has an image after assignemnt."""
        image = Image.objects.first()
        album1 = Album.objects.first()
        image.albums.add(album1)
        self.assertTrue(image.albums.count() == 1)

    def test_two_images_have_album(self):
        """Test that two images have same album."""
        image1 = Image.objects.all()[0]
        image2 = Image.objects.all()[1]
        album1 = Album.objects.first()
        image1.albums.add(album1)
        image2.albums.add(album1)
        image1.save()
        image2.save()
        self.assertTrue(image1.albums.all()[0] == album1)
        self.assertTrue(image2.albums.all()[0] == album1)

    def test_album_has_two_images(self):
        image1 = Image.objects.all()[0]
        image2 = Image.objects.all()[1]
        album1 = Album.objects.first()
        image1.albums.add(album1)
        image2.albums.add(album1)
        image1.save()
        image2.save()
        self.assertTrue(album1.images.count() == 2)

    def test_image_has_two_albums(self):
        """Test that an image has two albums."""
        image1 = Image.objects.first()
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        image1.albums.add(album1)
        image1.albums.add(album2)
        image1.save()
        self.assertTrue(image1.albums.count() == 2)

    def test_album_title(self):
        """Test that the album has a title."""
        self.assertTrue("Album" in Album.objects.first().title)

    def test_album_has_description(self):
        """Test that the album description field can be assigned."""
        album = Album.objects.first()
        album.description = "This is a good album."
        album.save()
        self.assertTrue(Album.objects.first().description == "This is a good album.")

    def test_album_has_published(self):
        """Test the album publisalbumhed field."""
        album = Album.objects.first()
        album.published = 'public'
        album.save()
        self.assertTrue(Album.objects.first().published == "public")

    def test_album_date_modified(self):
        """Test that the album has a date modified default."""
        album = Album.objects.first()
        self.assertTrue(album.date_modified)

    def test_album_date_created(self):
        """Test that the album has a date uploaded default."""
        album = Album.objects.first()
        self.assertTrue(album.date_created)

    def test_album_no_date_date_published(self):
        """Test that the album does not have a date published before assignment."""
        album = Album.objects.first()
        self.assertFalse(album.date_published)

    def test_album_date_date_published(self):
        """Test that the album has a date published after assignment."""
        album = Album.objects.first()
        album.date_published = timezone.now
        self.assertTrue(album.date_published)

    def test_album_has_no_owner(self):
        """Test that album has no owner."""
        album = Album.objects.first()
        self.assertFalse(album.owner)

    def test_album_has_owner(self):
        """Test that album has an owner after assignment."""
        album = Album.objects.first()
        user1 = User.objects.first()
        album.owner = user1.profile
        self.assertTrue(album.owner)

    def test_owner_has_album(self):
        """Test that the owner has the album."""
        album = Album.objects.first()
        user1 = User.objects.first()
        album.owner = user1.profile
        album.save()
        # import pdb; pdb.set_trace()
        self.assertTrue(user1.profile.albums.count() == 1)

    def test_two_albums_have_owner(self):
        """Test two albums have the same owner."""
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        user1 = User.objects.first()
        album1.owner = user1.profile
        album2.owner = user1.profile
        album1.save()
        album2.save()
        self.assertTrue(album1.owner == user1.profile)
        self.assertTrue(album2.owner == user1.profile)

    def test_owner_has_two_albums(self):
        """Test that owner has two albums."""
        album1 = Album.objects.all()[0]
        album2 = Album.objects.all()[1]
        user1 = User.objects.first()
        album1.owner = user1.profile
        album2.owner = user1.profile
        album1.save()
        album2.save()
        self.assertTrue(user1.profile.albums.count() == 2)
