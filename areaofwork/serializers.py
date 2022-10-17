from rest_framework import serializers

from projects.serializers import ProjectsSerializer
from .models import Areaofwork


class AreaofworkSerializer(serializers.ModelSerializer):
    projects = ProjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Areaofwork
        fields = ['id', 'title', 'details', 'slug', 'image', 'projects']