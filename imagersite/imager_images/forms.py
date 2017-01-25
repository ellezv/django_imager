"""Forms."""

from django import forms

from imager_images.models import Image


class PhotoForm(forms.ModelForm):
    """This makes a form. Yay."""

    class Meta:
        model = Image
        exclude = ['owner', 'date_modified', 'date_published', 'date_uploaded']
