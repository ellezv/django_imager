from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, TemplateView):
    """Class based view for user's own profile view."""

    template_name = "imager_profile/detail.html"
    login_url = reverse_lazy("login")

    def get_context_data(self):
        """Extend get_context_data method to our data."""
        if self.request.user.is_authenticated():
            public_images = self.request.user.profile.images.filter(
                published='public').count()
            private_images = self.request.user.profile.images.filter(
                published='private').count()
            profile = self.request.user.profile
            return {'profile': profile,
                    'public_images': public_images,
                    'private_images': private_images}

        else:
            return {'error': "You're not signed in."}


class UserProfileView(TemplateView):
    """Class based view for other user's profile view."""

    template_name = "imager_profile/detail.html"

    def get_context_data(self, username):
        """Extend get_context_data method to our data."""
        user = get_object_or_404(User, username=username)
        profile = user.profile
        public_images = profile.images.filter(published='public').count()
        private_images = profile.images.filter(published='private').count()
        return {'profile': profile,
                'public_images': public_images,
                'private_images': private_images}
