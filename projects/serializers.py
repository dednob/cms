from rest_framework import serializers

from campaign.serializers import CampaignsSerializer
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    campaigns = CampaignsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image', 'date', 'areaofwork', 'campaigns']

