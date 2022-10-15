from rest_framework import serializers
from .models import Areaofwork


class AreaofworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areaofwork
        fields = ['id', 'title', 'details', 'slug', 'image']