from django.shortcuts import render
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
