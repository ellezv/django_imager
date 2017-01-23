"""Views for Imager Site."""

from django.shortcuts import render
from imager_images.models import Image, Album


def home_view(request):
    """Home view for the imager site."""
    import random
    img_lst = Image.objects.all()
    img = random.choice(img_lst)
    return render(
        request,
        'imagersite/home.html',
        {'static_background': img.image.url}
    )
# note: when our database has images, we can query it and return a random path
# as the static background.
