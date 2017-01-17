from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class ImagerProfile(models.Model):
    """Profile class for all imager users."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    hireable = models.BooleanField(default=True)
    travel_radius = models.IntegerField(default=100)
    phone_number = models.CharField(max_length=10)
    camera_type = models.CharField(max_length=255, blank=True, null=True)
    photography_type_choices = (
        ('LA', 'Landscape'),
        ('WD', 'Weddings'),
        ('AN', 'Animals'),
        ('PT', 'Portraits'),
        ('UR', 'Urban'),
        ('FA', 'Fashion'),
        ('TR', 'Travel'),
        ('WA', 'Water')
    )
    photography_type = models.CharField(
        max_length=2,
        choices=photography_type_choices,
        blank=True,
        null=True)

    def is_active(self):
        """Return True if user is active, False if not."""
        return self.user.is_active

    def __str__(self):
        """Return a string representation of the imager profile instance."""
        profile = {
            'address': self.address,
            'bio': self.bio,
            'website': self.website,
            'hireable': self.hireable,
            'travel_radius': self.travel_radius,
            'phone number': self.phone_number,
            'camera type': self.camera_type,
            'type of photography': self.photography_type
        }
        return str(profile)


class ActiveUsersManager(models.Manager):
    """Active user manager."""

    def get_query_set(self):
        """Get the full query of active users."""
        return super(ActiveUsersManager, self).get_queryset().filter(user__is_active=True)


@receiver(post_save, sender=User)
def make_profile_for_user(sender, instance, **kwargs):
    """When a user is created, it gets a profile."""
    new_profile = ImagerProfile(user=instance)
    new_profile.save()
