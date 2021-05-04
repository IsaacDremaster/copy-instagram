from django.db.models import F
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import PublicationSerializer
from .models import Publications

class PublicationsView(ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publications.objects.prefetch_related('post_image').order_by('-date').annotate(
        owner_nickname = F('owner__username'),
        owner_avatar = F('owner__avatar')
    ).order_by('-date')
    lookup_field ='pk'

    def get_object(self):
        Publications.objects.prefetch_related