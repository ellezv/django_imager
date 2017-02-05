from imager_images.models import Image
from api.serializers import ImageSerializer
from rest_framework import viewsets, permissions


# class ImageList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class ImageViewSet(viewsets.ModelViewSet):

    serializer_class = ImageSerializer

    def get_queryset(self):
        """Get queryset for photographer."""
        return Image.objects.filter(owner=self.request.user.profile)
