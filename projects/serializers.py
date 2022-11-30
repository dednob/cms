from rest_framework import serializers

# from campaign.serializers import CampaignsSerializer
from areaofwork.serializers import *
from areaofwork.models import *
from .models import Projects


class ProjectsReadSerializer(serializers.ModelSerializer):
    # campaigns = CampaignsSerializer(many=True, read_only=True)

    # areaofwork = serializers.SerializerMethodField('areaofwork_detail', read_only = True)

    # def areaofwork_detail(self, obj): 
    #     instance = Areaofwork.objects.get(id=obj.id)

    #     return AreaofworkReadSerializer(instance).data
    areaofwork = AreaofworkProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image', 'date', 'areaofwork', 'campaigns', 'featured']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image', 'date', 'areaofwork', 'featured']


class ProjectsListSerializer(serializers.ModelSerializer):
    areaofwork = AreaofworkProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ['id', 'title', 'details', 'slug', 'image', 'featured', 'areaofwork']



class ProjectsCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'slug']
