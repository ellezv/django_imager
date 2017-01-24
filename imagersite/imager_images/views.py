"""Views for ou imager_images app."""
from django.shortcuts import render
from imager_images.models import Image, Album
# Create your views here.


def library_view(request):
    """View for the user's own library."""
    if request.user.is_authenticated():
        albums = request.user.profile.albums.all()
        images = request.user.profile.images.all()
        # import pdb; pdb.set_trace()
        return render(request, "imager_images/library.html", {
            'albums': albums,
            'images': images})


def photos_view(request):
    """View for all public photos."""
    photos = Image.objects.filter(published='public').all()
    return render(request, "imager_images/photos.html", {
        'photos': photos})


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
