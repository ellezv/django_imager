"""Imagersite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from imager_images.views import library_view, photos_view, albums_view, photo_id_view, album_id_view


urlpatterns = [
    url(r'^library/$', library_view, name="library"),
    url(r'^photos/$', photos_view, name="photos"),
    url(r'^albums/$', albums_view, name="albums"),
    url(r'^photos/(?P<pk>\d+)/$', photo_id_view, name="individual_photo"),
    url(r'^albums/(?P<pk>\d+)/$', album_id_view, name="individual_album")
]
