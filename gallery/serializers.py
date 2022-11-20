from rest_framework import serializers
from .models import Gallery
from campaign.serializers import *

class GallerySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Gallery
        fields = '__all__'



