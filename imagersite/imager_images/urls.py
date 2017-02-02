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
from imager_images.views import LibraryView, PhotoView, AlbumView, PhotoIdView, AlbumIdView, AddPhotoView, AddAlbumView, PhotoEditView, AlbumEditView, PhotoTagView

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name="library"),
    url(r'^photos/$', PhotoView.as_view(), name="photos"),
    url(r'^albums/$', AlbumView.as_view(), name="albums"),
    url(r'^photos/(?P<pk>\d+)/$', PhotoIdView.as_view(), name="individual_photo"),
    url(r'^albums/(?P<pk>\d+)/$', AlbumIdView.as_view(), name="individual_album"),
    url(r'^albums/add/$', AddAlbumView.as_view(), name="add_albums"),
    url(r'^photos/add/$', AddPhotoView.as_view(), name="add_photos"),
    url(r'^photos/(?P<pk>\d+)/edit/$', PhotoEditView.as_view(), name="edit_photo"),
    url(r'^albums/(?P<pk>\d+)/edit/$', AlbumEditView.as_view(), name="edit_album"),
    url(r'^tagged/(?P<slug>[-\w]+)/$', PhotoTagView.as_view(), name="tagged_photos"),
]
