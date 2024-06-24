from sights.models import Sights
from sights.serializers import SightsSerializer
from sights.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from sights.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SightsList(generics.ListCreateAPIView):
    queryset = Sights.objects.all()
    serializer_class = SightsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['title', 'description']
    ordering_fields = ('title', 'owner')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sights.objects.all()
    serializer_class = SightsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
