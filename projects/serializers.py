from rest_framework import serializers

from campaign.serializers import CampaignsSerializer
from .models import Projects
from areaofwork.serializers import *
from areaofwork.models import *


class ProjectsSerializer(serializers.ModelSerializer):
    campaigns = CampaignsSerializer(many=True, read_only=True)

    # areaofwork = serializers.SerializerMethodField('areaofwork_detail', read_only = True)

    # def areaofwork_detail(self, obj): 
    #     instance = Areaofwork.objects.get(id=obj.id)

    #     return AreaofworkReadSerializer(instance).data

    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image', 'date', 'areaofwork', 'campaigns', 'featured']


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image']
