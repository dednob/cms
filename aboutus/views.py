from django.shortcuts import render
from .models import Aboutus
from .serializers import AboutusSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def About_list(request):
    aboutus = Aboutus.objects.all()
    serializer = AboutusSerializer(aboutus, many = True)
    return Response(serializer.data)

