"""Views for Imager Site."""

from django.shortcuts import render
from imager_images.models import Image
from django.conf import settings


def home_view(request):
    """Home view for the imager site."""
    import random
    img_lst = Image.objects.all()
    if not len(img_lst):
        img_url = settings.STATIC_URL + "banff.jpg"
    else:
        img_url = random.choice(img_lst).image.url
    return render(
        request,
        'imagersite/home.html',
        {'static_background': img_url}
    )
