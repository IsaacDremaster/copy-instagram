from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


from .serializers import (
    PublicationSerializer,
    AuthTokenSerializer,
    ProfileSerializer
)

from .models import User


class SignUpUserView(generics.CreateAPIView):
    serializer_class = PublicationSerializer
    queryset = User.objects.all()


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permissions_classes = (IsAuthenticated, )
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
