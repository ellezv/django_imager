"""Views for Imager Site."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic import TemplateView

from imager_images.models import Image

import random


class HomeView(TemplateView):
    """A class based view for home page."""

    template_name = "imagersite/home.html"

    def get_context_data(self):
        """Extending get_context_data method to return the data we need."""
        img_lst = Image.objects.all()
        if not len(img_lst):
            static_background = settings.STATIC_URL + "banff.jpg"
        else:
            static_background = random.choice(img_lst).image.url
        return {"static_background": static_background}
