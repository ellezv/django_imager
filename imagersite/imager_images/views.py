"""Views for our imager_images app."""
from django.views.generic import TemplateView
from django.shortcuts import render
from imager_images.models import Image, Album


class LibraryView(TemplateView):
    """A class based view for Library view."""

    template_name = "imager_images/library.html"

    def get_context_data(self):
        """Extending get_context_data method."""
        if self.request.user.is_authenticated():
            albums = self.request.user.profile.albums.all()
            images = self.request.user.profile.images.all()

        return {'albums': albums, 'images': images}


class PhotoView(TemplateView):
    """A class based view for Photo view."""

    template_name = "imager_images/photos.html"

    def get_context_data(self):
        """Extending get_context_data method to add our data."""
        photos = Image.objects.filter(published='public').all()
        return {'photos': photos}

# def photos_view(request):
#     """View for all public photos."""
#     photos = Image.objects.filter(published='public').all()
#     return render(request, "imager_images/photos.html", {
#         'photos': photos})


def albums_view(request):
    """View for all public albums."""
    albums = Album.objects.filter(published='public').all()
    return render(request, "imager_images/albums.html", {
        'albums': albums})


def photo_id_view(request, pk):
    """View for an individual photo."""
    photo = Image.objects.get(pk=pk)
    return render(request, 'imager_images/photo_id.html', {
        "photo": photo})


def album_id_view(request, pk):
    """View for an individual album."""
    album = Album.objects.get(pk=pk)
    images = album.images.all()
    return render(request, 'imager_images/album_id.html', {
        "album": album,
        "images": images})
