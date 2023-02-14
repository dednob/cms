from rest_framework import serializers
from .models import Aboutus, Team


class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = ['id', 'title', 'details', 'slug', 'image']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'