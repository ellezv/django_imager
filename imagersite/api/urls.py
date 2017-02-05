from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ImageViewSet

urlpatterns = [
    url(r'^images/$', ImageViewSet.as_view({'get': 'list'}), name='api_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)