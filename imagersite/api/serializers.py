from rest_framework import serializers
from imager_images.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'title',
            'code',
            'description',
            'date_published',
            'date_modified',
            'date_uploaded',
            'published',
            'image',
            'owner',
            'tags'
        )
