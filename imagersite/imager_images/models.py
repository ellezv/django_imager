from django.db import models

# Create your models here.


class Image(models.Model):
    """Image model for the Imager App."""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_published = models.DateTimeField()
    data_modified = models.DateTimeField()
    date_uploaded = models.DateTimeField()
    pub_choices = (
        ('private', 'Private'),
        ('shared', 'Shared'),
        ('public', 'Public'),
    )
    published = models.CharField(max_length=255, choices=pub_choices)
    image = models.ImageField(upload_to="")
