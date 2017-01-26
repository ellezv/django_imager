"""Views for our imager_images app."""
from django.views.generic import TemplateView, CreateView
from imager_images.models import Image, Album
from django.utils import timezone
from imager_images.forms import PhotoForm
from django.shortcuts import redirect


class LibraryView(TemplateView):
    """A class based view for Library view."""

    template_name = "imager_images/library.html"

    def get_context_data(self):
        """Extending get_context_data method."""
        if self.request.user.is_authenticated():
            albums = self.request.user.profile.albums.all()
            images = self.request.user.profile.images.all()
        else:
            albums = images = None
        return {'albums': albums, 'images': images}


class PhotoView(TemplateView):
    """A class based view for Photo view."""

    template_name = "imager_images/photos.html"

    def get_context_data(self):
        """Extending get_context_data method to add our data."""
        photos = Image.objects.filter(published='public').all()
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


class AddPhotoView(CreateView):
    """A class based view to add a picture."""

    template_name = 'imager_images/add_photo.html'
    form_class = PhotoForm

    # def get_queryset(self):
    #     queryset = Image.objects.all()
    #     return queryset

    # def get_context_data(self):
    #     """Extend get_context_data method for our data."""
    #     # import pdb; pdb.set_trace()
    #     if self.request.method == "POST":
    #         import pdb; pdb.set_trace()
    #         form = PhotoForm(self.request.POST)
    #         if form.is_valid():
    #             photo = form.save(commit=False)
    #             photo.owner = self.request.user.profile
    #             photo.published_date = timezone.now()
    #             photo.save()
    #             return redirect('individual_photo', pk=photo.pk)
    #     else:
    #         return {}

class AddPhotoView(CreateView):
    """A class based view to add a picture."""

    model = Image
    form_class = PhotoForm
    template_name = 'imager_images/add_photo.html'
    success_url = 'library'

    # def get_context_data(self):
    #     """Extend get_context_data method for our data."""
    #     # import pdb; pdb.set_trace()
    #     if self.request.method == "POST":
    #         import pdb; pdb.set_trace()
    #         form = PhotoForm(self.request.POST)
    #         if form.is_valid():
    #             photo = form.save(commit=False)
    #             photo.owner = self.request.user.profile
    #             photo.published_date = timezone.now()
    #             photo.save()
    #             return redirect('individual_photo', pk=photo.pk)
    #     else:
    #         return {}

    def form_valid(self, form):
        photo = form.save()
        photo.owner = self.request.user.profile
        photo.published_date = timezone.now()
        photo.save()
        return redirect('individual_photo', pk=photo.pk)
