from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def profile_view(request):
    """View for the user's own profile."""
    # username = "You're not signed in, dummy"
    if request.user.is_authenticated():
        public_images = request.user.profile.images.filter(published='public').count()
        private_images = request.user.profile.images.filter(published='private').count()
        profile = request.user.profile
        # import pdb; pdb.set_trace()

        return render(request, "imager_profile/detail.html",
                               {'profile': profile,
                                'public_images': public_images,
                                'private_images': private_images
                                })
    else:
        error_message = "Yout're not signed in."
        return render(request, "imager_profile/detail.html",
                               {'error': error_message
                                })


def user_profile_view(request, username):
    """View for other user's profile."""
    user = User.objects.get(username=username)
    profile = user.profile
    public_images = profile.images.filter(published='public').count()
    private_images = profile.images.filter(published='private').count()
    return render(request, "imager_profile/detail.html",
                           {'profile': profile,
                            'public_images': public_images,
                            'private_images': private_images
                            })
