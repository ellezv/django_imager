"""Views for Imager Site."""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def home_view(request):
    """Home view for the imager site."""
    data = "Nothing right now"
    return render(request,
                  'imagersite/home.html',
                  {'data': data})
    # return HttpResponse('This is the Home Page!')
