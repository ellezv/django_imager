"""Views for our imager_images app."""
from django.views.generic import TemplateView, CreateView, UpdateView
from django.utils import timezone
<<<<<<< HEAD
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from imager_images.models import Image, Album
from imager_images.forms import PhotoForm, AlbumForm
from django.urls import reverse_lazy
=======
from imager_images.forms import PhotoForm, AlbumForm
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
>>>>>>> 7cd90ad7d62cc8faeb291f2d33fbb65188f15e55


# class LibraryView(TemplateView):
#     """A class based view for Library view."""

#     template_name = "imager_images/library.html"

#     def get_context_data(self):
#         """Extending get_context_data method."""
#         if self.request.user.is_authenticated():
#             albums = self.request.user.profile.albums.all()
#             images = self.request.user.profile.images.all()
#         else:
#             albums = images = None
#         return {'albums': albums, 'images': images}

def library_view(request):
    """View for the user's own library."""
    if request.user.is_authenticated():
        all_albums = request.user.profile.albums.all()
        album_page = request.GET.get("album", 1)
        all_images = request.user.profile.images.all()
        image_page = request.GET.get("image", 1)

        album_pages = Paginator(all_albums, 4)
        image_pages = Paginator(all_images, 4)

        images = image_pages.page(image_page)
        albums = album_pages.page(album_page)

        # import pdb; pdb.set_trace()
        return render(request, "imager_images/library.html", {
            'albums': albums,
            'images': images})


class PhotoView(TemplateView):
    """A class based view for Photo view."""

    template_name = "imager_images/photos.html"

    def get_context_data(self):
        """Extending get_context_data method to add our data."""
        photos = Image.objects.filter(published='public').all()
        return {'photos': photos}


class PhotoTagView(TemplateView):
    """A class based view for Photo view."""

    template_name = "imager_images/photos.html"

    def get_context_data(self, slug):
        """Extending get_context_data method to add our data."""
        photos = Image.objects.filter(tags__slug=slug).all()
        return {'photos': photos}


class AlbumView(TemplateView):
    """Class based view for Album view."""

    template_name = "imager_images/albums.html"

    def get_context_data(self):
        """Extending get_context_data method."""
        albums = Album.objects.filter(published='public').all()
        return {'albums': albums}


class PhotoIdView(TemplateView):
    """Class based view for individual photo view."""

    template_name = "imager_images/photo_id.html"

    def get_context_data(self, pk):
        """Extending get_context_data method for our data."""
        photo = Image.objects.get(pk=pk)
        # import pdb; pdb.set_trace()
        if photo.published == 'public' or photo.owner.user == self.request.user:
            return {"photo": photo}
        else:
            error = "I'm sorry, that photo is not available."
            return {"error": error}


class AlbumIdView(TemplateView):
    """A class based view for individual album view."""

    template_name = "imager_images/album_id.html"

    def get_context_data(self, pk):
        """Extend get_context_data method for our data to render."""
        album = Album.objects.get(pk=pk)
        if album.published == 'public' or album.owner.user == self.request.user:
            images = album.images.all()
            return {"album": album, "images": images}
        else:
            error = "I'm sorry, that album is not available."
            return {"error": error}


class AddPhotoView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """A class based view to add a picture."""

    model = Image
    form_class = PhotoForm
    template_name = 'imager_images/add_photo.html'
    login_url = reverse_lazy("login")
    permission_required = "images.add_image"

    def form_valid(self, form):
        """Execute if form is valid."""
        photo = form.save()
        photo.owner = self.request.user.profile
        photo.date_uploaded = timezone.now()
        photo.date_modified = timezone.now()
        if photo.published == "public":
            photo.published_date = timezone.now()
        photo.save()
        return redirect('library')


class AddAlbumView(LoginRequiredMixin, CreateView):
    """A class based view to add an Album."""

    model = Album
    form_class = AlbumForm
    template_name = 'imager_images/add_album.html'
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """Execute if form is valid."""
        album = form.save()
        album.owner = self.request.user.profile
        album.date_created = timezone.now()
        album.save()
        return redirect('library')


class PhotoEditView(LoginRequiredMixin, UpdateView):
    """A class based view to edit an image."""

    model = Image
    form_class = PhotoForm
    template_name = 'imager_images/add_photo.html'
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """Execute if form is valid."""
        photo = form.save()
        photo.date_modified = timezone.now()
        if photo.published == "public":# This needs to be fixed. only update if changed
            photo.published_date = timezone.now()
        photo.save()
        return redirect('library')


class AlbumEditView(LoginRequiredMixin, UpdateView):
    """A class based view to edit an album."""

    model = Album
    form_class = AlbumForm
    template_name = 'imager_images/add_album.html'
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        """Execute if form is valid."""
        album = form.save()
        album.date_modified = timezone.now()
        if album.published == "public":# This needs to be fixed. only update if changed
            album.published_date = timezone.now()
        album.save()
        return redirect('library')
