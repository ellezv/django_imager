from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class ProfileView(TemplateView):
    """Class based view for user's own profile view."""

    template_name = "imager_profile/detail.html"

    def get_context_data(self):
        """Extend get_context_data method to our data."""
        if self.request.user.is_authenticated():
            public_images = self.request.user.profile.images.filter(published='public').count()
            private_images = self.request.user.profile.images.filter(published='private').count()
            profile = self.request.user.profile
            return {'profile': profile,
                    'public_images': public_images,
                    'private_images': private_images}

        else:
            return {'error': "You're not signed in."}




# def profile_view(request):
#     """View for the user's own profile."""
#     # username = "You're not signed in, dummy"
#     if request.user.is_authenticated():
#         public_images = request.user.profile.images.filter(published='public').count()
#         private_images = request.user.profile.images.filter(published='private').count()
#         profile = request.user.profile
#         # import pdb; pdb.set_trace()

#         return render(request, "imager_profile/detail.html",
#                                {'profile': profile,
#                                 'public_images': public_images,
#                                 'private_images': private_images
#                                 })
#     else:
#         error_message = "Yout're not signed in."
#         return render(request, "imager_profile/detail.html",
#                                {'error': error_message
#                                 })


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
