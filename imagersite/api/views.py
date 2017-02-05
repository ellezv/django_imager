from imager_images.models import Image
from api.serializers import ImageSerializer
from rest_framework import mixins
from rest_framework import generics


class ImageList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)