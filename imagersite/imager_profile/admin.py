from django.contrib import admin
from imager_images.models import Image
from imager_profile.models import ImagerProfile


# Register your models here.
admin.site.register(Image)
admin.site.register(ImagerProfile)