"""Views for Imager Site."""

from django.shortcuts import render


def home_view(request):
    """Home view for the imager site."""
    return render(request,
                  'imagersite/home.html',
                  {'static_background': "/static/images/banff.jpg"})
# note: when our database has images, we can query it and return a random path
# as the static background.
