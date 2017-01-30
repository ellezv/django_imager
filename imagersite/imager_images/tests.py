
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy

from imager_images.models import Image, Album
from imager_images.views import LibraryView, PhotoView, AlbumView, PhotoIdView, AlbumIdView

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
    image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images.jpg', 'rb').read(), content_type='image/jpeg')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
    title = factory.Sequence(lambda n: "Album {}".format(n))
    cover_image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images.jpg', 'rb').read(), content_type='image/jpeg')
    description = "Calvin and hobbes album"


class ImageTestCase(TestCase):
    """The Image App Test Runner."""

    def setUp(self):
        """User setup for tests."""
        self.client = Client()
        self.request = RequestFactory()
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
        """Test that an album has two images."""
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

    def test_libary_view_returns_200(self):
        """Test Library View returns a 200."""
        user = UserFactory.create()
        user.save()
        view = LibraryView.as_view()
        req = self.request.get(reverse_lazy('library'))
        req.user = user
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_logged_in_user_has_library(self):
        """A logged in user gets a 200 resposne."""
        user = UserFactory.create()
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(response.status_code == 200)

    def test_logged_in_user_sees_their_albums(self):
        """Test that a logged in user can see their images in library."""
        user = UserFactory.create()
        album1 = Album.objects.first()
        album2 = Album.objects.all()[1]
        user.profile.albums.add(album1)
        user.profile.albums.add(album2)
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(album1.description in str(response.content))

    def test_photo_view_returns_200(self):
        """Test that the photo view returns a 200."""
        req = self.request.get(reverse_lazy('photos'))
        view = PhotoView.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_photo_view_returns_public_photos(self):
        """Test that the photo view returns public photos."""
        image = ImageFactory()
        image.published = 'public'
        image.save()
        req = self.request.get(reverse_lazy('photos'))
        view = PhotoView.as_view()
        response = view(req)
        self.assertTrue(response.context_data['photos'].count() == 1)

    def test_photo_view_doesnt_return_private_photos(self):
        """Test that the photo view doesnt return private photos."""
        image = ImageFactory()
        image.published = 'private'
        image.save()
        req = self.request.get(reverse_lazy('photos'))
        view = PhotoView.as_view()
        response = view(req)
        self.assertTrue(response.context_data['photos'].count() == 0)

    def test_album_view_returns_200(self):
        """Test that the album view returns a 200."""
        req = self.request.get(reverse_lazy('albums'))
        view = AlbumView.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_album_view_returns_public_albums(self):
        """Test that the album view returns public albums."""
        album = AlbumFactory()
        album.published = 'public'
        album.save()
        req = self.request.get(reverse_lazy('albums'))
        view = AlbumView.as_view()
        response = view(req)
        self.assertTrue(response.context_data['albums'].count() == 1)

    def test_album_view_doesnt_return_private_albums(self):
        """Test that the album view doesnt return private albums."""
        album = AlbumFactory()
        album.published = 'private'
        album.save()
        req = self.request.get(reverse_lazy('albums'))
        view = AlbumView.as_view()
        response = view(req)
        self.assertTrue(response.context_data['albums'].count() == 0)

    def test_photoid_view_returns_200(self):
        """Test that the photo id view returns a 200."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        self.client.force_login(user)
        photo = ImageFactory()
        photo.owner = user.profile
        photo.save()
        response = self.client.get(reverse_lazy('individual_photo',
                                                kwargs={'pk': photo.id}))
        self.assertTrue(response.status_code == 200)

    def test_photoid_view_returns_public_photo(self):
        """Test that a user can view a public photo of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        photo = ImageFactory()
        photo.published = 'public'
        photo.owner = user.profile
        photo.save()
        response = self.client.get(reverse_lazy('individual_photo',
                                                kwargs={'pk': photo.id}))
        # import pdb; pdb.set_trace()
        self.assertTrue(response.context_data['photo'])

    def test_photoid_view_doesnt_return_private_photo(self):
        """Test that a user cannot view a private photo of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        photo = ImageFactory()
        photo.published = 'private'
        photo.owner = user.profile
        photo.save()
        response = self.client.get(reverse_lazy('individual_photo',
                                                kwargs={'pk': photo.id}))
        with self.assertRaises(KeyError):
            response.context_data['photo']

    def test_photoid_view_returns_error_private_photo(self):
        """Test that a user cannot view a private photo of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        photo = ImageFactory()
        photo.published = 'private'
        photo.owner = user.profile
        photo.save()
        response = self.client.get(reverse_lazy('individual_photo',
                                                kwargs={'pk': photo.id}))
        self.assertTrue(response.context_data['error'])

    def test_photoid_user_views_own_private_photo(self):
        """Test that a user can view their own private photo."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        self.client.force_login(user)
        photo = ImageFactory()
        photo.published = 'private'
        photo.owner = user.profile
        photo.save()
        response = self.client.get(reverse_lazy('individual_photo',
                                                kwargs={'pk': photo.id}))
        # import pdb; pdb.set_trace()
        self.assertTrue(response.context_data['photo'])

    def test_albumid_view_returns_200(self):
        """Test that the album id view returns a 200."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        self.client.force_login(user)
        album = AlbumFactory()
        album.owner = user.profile
        album.save()
        response = self.client.get(reverse_lazy('individual_album',
                                                kwargs={'pk': album.id}))
        self.assertTrue(response.status_code == 200)

    def test_albumid_view_returns_public_album(self):
        """Test that a user can view a public album of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        album = AlbumFactory()
        album.published = 'public'
        album.owner = user.profile
        album.save()
        response = self.client.get(reverse_lazy('individual_album',
                                                kwargs={'pk': album.id}))
        self.assertTrue(response.context_data['album'])

    def test_albumid_view_doesnt_return_private_album(self):
        """Test that a user cannot view a private album of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        album = AlbumFactory()
        album.published = 'private'
        album.owner = user.profile
        album.save()
        response = self.client.get(reverse_lazy('individual_album',
                                                kwargs={'pk': album.id}))
        with self.assertRaises(KeyError):
            response.context_data['album']

    def test_albumid_view_returns_error_private_album(self):
        """Test that a user cannot view a private album of another user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        user2 = User()
        user2.username = "maxrebo"
        user2.set_password('itsaband')
        user2.save()
        self.client.force_login(user2)
        album = AlbumFactory()
        album.published = 'private'
        album.owner = user.profile
        album.save()
        response = self.client.get(reverse_lazy('individual_album',
                                                kwargs={'pk': album.id}))
        self.assertTrue(response.context_data['error'])

    def test_albumid_user_views_own_private_album(self):
        """Test that a user can view their own private album."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        self.client.force_login(user)
        album = AlbumFactory()
        album.published = 'private'
        album.owner = user.profile
        album.save()
        response = self.client.get(reverse_lazy('individual_album',
                                                kwargs={'pk': album.id}))
        self.assertTrue(response.context_data['album'])

    def new_user_signed_in(self):
        """Make and sign in new user."""
        user = User()
        user.username = "jabba"
        user.set_password('itspizza')
        user.save()
        self.client.force_login(user)
        return user

    def submit_add_image_form(self):
        """Submit a form to test."""
        image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post(reverse_lazy('add_photos'),
                                    {'title': 'itsatitle',
                                     'description': 'his greatness jabba',
                                     'published': 'public',
                                     'image': image})
        return response

    def test_add_an_image_count(self):
        """Test that adding an image increases the model count."""
        self.new_user_signed_in()
        images = Image.objects.count()
        self.submit_add_image_form()
        assert Image.objects.count() == images + 1

    def test_add_an_image_correct_owner(self):
        """Test that a new added image is owned by the user."""
        user = self.new_user_signed_in()
        users_images = user.profile.images.count()
        self.submit_add_image_form()
        assert user.profile.images.count() == users_images + 1

    def test_add_two_images_correct_owner(self):
        """Test that a new added images are owned by the user."""
        user = self.new_user_signed_in()
        users_images = user.profile.images.count()
        self.submit_add_image_form()
        self.submit_add_image_form()
        assert user.profile.images.count() == users_images + 2

    def test_add_an_image_correct_published(self):
        """Test that a new added image has the right published type."""
        user = self.new_user_signed_in()
        self.submit_add_image_form()
        assert user.profile.images.first().published == 'public'

    def test_add_an_image_correct_decription(self):
        """Test that a new added image has the right description."""
        user = self.new_user_signed_in()
        self.submit_add_image_form()
        assert user.profile.images.first().description == 'his greatness jabba'

    def test_new_image_in_users_library(self):
        """Test that a new added image's description shows up in the library page."""
        user = self.new_user_signed_in()
        self.submit_add_image_form()
        response = self.client.get(reverse_lazy('library'))
        assert user.profile.images.first().description in str(response.content)

    def submit_add_album_form(self):
        """Submit a form to test add album."""
        image = SimpleUploadedFile(name='test_image.jpg', content=open('imagersite/static/images.jpg', 'rb').read(), content_type='image/jpeg')
        response = self.client.post(reverse_lazy('add_albums'),
                                    {'title': 'itsanalbum',
                                     'description': 'mostly hosting pod races',
                                     'published': 'public',
                                     'cover_image': image
                                     })
        return response

    def test_add_an_album_count(self):
        """Test that adding an album increases the model count."""
        self.new_user_signed_in()
        albums = Album.objects.count()
        self.submit_add_album_form()
        assert Album.objects.count() == albums + 1

    def test_add_an_album_correct_owner(self):
        """Test that a new added album is owned by the user."""
        user = self.new_user_signed_in()
        users_albums = user.profile.albums.count()
        self.submit_add_album_form()
        assert user.profile.albums.count() == users_albums + 1

    def test_add_two_albums_correct_owner(self):
        """Test that a new added albums are owned by the user."""
        user = self.new_user_signed_in()
        users_albums = user.profile.albums.count()
        self.submit_add_album_form()
        self.submit_add_album_form()
        assert user.profile.albums.count() == users_albums + 2

    def test_add_an_album_correct_published(self):
        """Test that a new added album has the right published type."""
        user = self.new_user_signed_in()
        self.submit_add_album_form()
        assert user.profile.albums.first().published == 'public'

    def test_add_an_album_correct_decription(self):
        """Test that a new added album has the right description."""
        user = self.new_user_signed_in()
        self.submit_add_album_form()
        assert user.profile.albums.first().description == 'mostly hosting pod races'

    def test_new_album_in_users_library(self):
        """Test that a new added album's description shows up in the library page."""
        user = self.new_user_signed_in()
        self.submit_add_album_form()
        response = self.client.get(reverse_lazy('library'))
        assert user.profile.albums.first().description in str(response.content)
