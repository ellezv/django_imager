"""Views for Imager Site."""

from django.shortcuts import render
from imager_images.models import Image, Album


def home_view(request):
    """Home view for the imager site."""
    ps_rand_image = Image.objects.all()[4].image.url
    return render(request,
                  'imagersite/home.html',
                  {'static_background': ps_rand_image})
# note: when our database has images, we can query it and return a random path
# as the static background.
