from rest_framework import serializers

from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'title', 'details', 'slug', 'image', 'active', 'experience_data']


class HomeToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['active']


class HomeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['experience_data']