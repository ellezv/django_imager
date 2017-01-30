"""Models for the Imager Images."""

from django.db import models
from django.utils import timezone
from imager_profile.models import ImagerProfile

# Create your models here.


class Image(models.Model):
    """Image model for the Imager App."""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(default=timezone.now)
    date_uploaded = models.DateTimeField(default=timezone.now)
    pub_choices = (
        ('private', 'Private'),
        ('shared', 'Shared'),
        ('public', 'Public'),
    )
    published = models.CharField(max_length=255,
                                 choices=pub_choices,
                                 blank=True,
                                 null=True)
    image = models.ImageField(upload_to="")
    owner = models.ForeignKey(ImagerProfile,
                              related_name='images',
                              blank=True,
                              null=True
                              )

    def __str__(self):
        """Return title as string."""
        return self.title


class Album(models.Model):
    """Album model for the Imager App."""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    pub_choices = (
        ('private', 'Private'),
        ('shared', 'Shared'),
        ('public', 'Public'),
    )
    published = models.CharField(max_length=255,
                                 choices=pub_choices,
                                 blank=True,
                                 null=True
                                 )
    cover_image = models.ImageField(upload_to="")
    owner = models.ForeignKey(ImagerProfile, related_name='albums',
                              # default=1,
                              blank=True,
                              null=True
                              )
    images = models.ManyToManyField(Image, related_name='albums', blank=True, null=True)

    def __str__(self):
        """Return title as string."""
        return self.title
