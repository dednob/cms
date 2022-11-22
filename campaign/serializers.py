from rest_framework import serializers
from .models import Campaigns

from projects.serializers import *
from projects.models import *



class CampaignsSerializer(serializers.ModelSerializer):
    
    
    projects = ProjectsCampaignSerializer(many=True, read_only=True)

    class Meta:
        model = Campaigns
        
        fields = ['id', 'title', 'details','description', 'slug', 'image', 'date','projects']


class CampaignsPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campaigns
        fields = ['id', 'title', 'details','description', 'slug', 'image', 'date','projects']

# class CampaignsReadSerializer(serializers.ModelSerializer):
    
#     gallery = GallerySerializer(many=True, read_only=True)
#     projects = ProjectsSerializer(many=True, read_only=True)

#     def projects_detail(self, obj): 
#         print(list(obj))
#         project_instance = Projects.objects.get(id=obj.projects.id)
#         return ProjectsListSerializer(project_instance).data

#     class Meta:
#         model = Campaigns
#         fields = ['id', 'title', 'details','description', 'slug', 'image', 'date', 'projects', 'gallery']

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep["projects"] = ProjectsSerializer(instance.projects.all(), many=True).data
    #     return rep


class CampaignsListSerializer(serializers.ModelSerializer):
    projects = ProjectsCampaignSerializer(many=True, read_only=True)
    class Meta:
        model = Campaigns
        fields = ['id', 'title', 'details', 'slug', 'image', 'date','projects' ]

class CampaignsGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaigns
        fields = ['id', 'title', 'slug']