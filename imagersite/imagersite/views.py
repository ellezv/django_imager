"""Views for Imager Site."""

from django.shortcuts import render
from django.http import HttpResponse 

def home_view(request):
    """Home view for the imager site."""
    # return render(request,
    #               'base.html',
    #               {'data': data})
    return HttpResponse('This is the Home Page!')