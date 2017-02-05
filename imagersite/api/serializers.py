from rest_framework import serializers
from imager_images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = (
            'id',
            'title',
            'description',
            'date_published',
            'date_modified',
            'date_uploaded',
            'published',
            'owner',
            'image'
        )
