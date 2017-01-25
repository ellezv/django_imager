"""Views for Imager Site."""

from django.shortcuts import render
from imager_images.models import Image
from django.conf import settings
from django.views.generic import TemplateView
import random


class HomeView(TemplateView):
    """A class based view for home page."""

    template_name = "imagersite/home.html"

    def get_context_data(self):
        """Extending get_context_data method."""
        img_lst = Image.objects.all()
        if not len(img_lst):
            static_background = settings.STATIC_URL + "banff.jpg"
        else:
            static_background = random.choice(img_lst).image.url
        return {"static_background": static_background}


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
