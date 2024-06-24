from rest_framework import serializers
from sights.models import Sights, CITY_CHOICES, CATEGORY_CHOICES
from django.contrib.auth.models import User


class SightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sights
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    sights = serializers.PrimaryKeyRelatedField(many=True, queryset=Sights.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'sights']
