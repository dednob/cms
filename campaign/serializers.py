from rest_framework import serializers
from .models import Campaigns
from gallery.serializers import GallerySerializer


class CampaignsSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Campaigns
        fields = ['id', 'title', 'details', 'slug', 'image', 'date','projects', 'gallery']