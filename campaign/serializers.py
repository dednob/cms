from rest_framework import serializers
from .models import Campaigns


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ['id', 'title', 'details', 'slug', 'image', 'date','projects']