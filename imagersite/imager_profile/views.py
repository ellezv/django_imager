from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def profile_view(request):
    """View for the profile."""
    return render(request, "imager_profile/detail.html", {})