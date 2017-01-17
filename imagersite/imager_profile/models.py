from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save
from django.dispath import receiver


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
    photography_type = models.Choices(
        ('LA', 'Landscape'),
        ('WD', 'Weddings'),
        ('AN', 'Animals'),
        ('PT', 'Portraits'),
        ('UR', 'Urban'),
        ('FA', 'Fashion'),
        ('TR', 'Travel'),
        ('WA', 'Water')
    )