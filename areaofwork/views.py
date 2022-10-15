from django.shortcuts import render
from .models import Areaofwork
from .serializers import AreaofworkSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list(request):
    areaofwork = Areaofwork.objects.all()
    serializer = AreaofworkSerializer(areaofwork, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

    slug = slugify(data['title'])
    suffix = 1
    if Areaofwork.objects.filter(title__exact=slug).exists():
        count = Areaofwork.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(data['title']), suffix)

    data['slug'] = slug
    serializer = AreaofworkSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

    areaofwork = Areaofwork.objects.get(id=pk)
    serializer = AreaofworkSerializer(areaofwork, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update(request, pk=None):
    id = pk
    areaofwork = Areaofwork.objects.get(pk=id)
    serializer = AreaofworkSerializer(areaofwork, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    areaofwork = Areaofwork.objects.get(id=pk)
    areaofwork.delete()
    return Response('Deleted')
