from django.shortcuts import render
from .models import Areaofwork
from .serializers import AreaofworkSerializer, AreaofworkReadSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from rest_framework import status


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def aow_list(request):
    areaofwork = Areaofwork.objects.all()
    serializer = AreaofworkReadSerializer(areaofwork, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def aow_detail(request, slug):
    if slug is not None:
        aow = Areaofwork.objects.get(slug=slug)
        serializer = AreaofworkSerializer(aow)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    try:
        data = request.data
        
        if 'image' in data and data['image'] != None:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        # slug = slugify(data['title'])
        suffix = 1
        print(data['title'])
        

        if Areaofwork.objects.filter(title__exact=data['title']).exists():
            print("yes")
            count = Areaofwork.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            print("No")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug
        serializer = AreaofworkSerializer(data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data created successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
                'error': serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):

    areaofwork = Areaofwork.objects.get(slug=slugkey)
    data = request.data
    if('image' in data and data['image']== None) and areaofwork.image != None:
            data.pop('image')

    if 'image' in data and data['image'] != None:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

    # slug = slugify(data['title'])
    suffix = 1

    if Areaofwork.objects.filter(title__exact=data['title']).exists():
        print("yes")
        count = Areaofwork.objects.filter(title__exact=data['title']).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(data['title']), suffix)

    data['slug'] = slug

    
    serializer = AreaofworkSerializer(areaofwork, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, slug):
    areaofwork = Areaofwork.objects.get(slug=slug)
    areaofwork.delete()
    return Response('Deleted')
