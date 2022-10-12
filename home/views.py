from django.shortcuts import render
from .models import Home
from .serializers import HomeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile


@api_view(['GET'])
def home_list(request):
    home = Home.objects.all()
    serializer = HomeSerializer(home, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_home(request):
    home_data = request.data
    if 'home_image' in home_data:
        fmt, img_str = str(home_data['home_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        home_data['home_image'] = img_file

    serializer = HomeSerializer(data=home_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_home(request, pk):
    home_data = request.data
    if 'home_image' in home_data:
        fmt, img_str = str(home_data['home_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        home_data['home_image'] = img_file

    home = Home.objects.get(id=pk)
    serializer = HomeSerializer(home, data=home_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_home(request, pk):
    home = Home.objects.get(id=pk)
    home.delete()
    return Response('Deleted')
