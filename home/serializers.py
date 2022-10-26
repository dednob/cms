from rest_framework import serializers

from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'title', 'details', 'slug', 'image', 'active']

class HomeToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['active']

