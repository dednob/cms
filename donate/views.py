from django.shortcuts import render
from .models import Donate
from .serializers import DonateSerializer
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
def details(request):
    try:
        donate = Donate.objects.all()
        serializer = DonateSerializer(donate, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    try:
        data = request.data
        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Donate.objects.filter(title__exact=data['title']).exists():
            print("yes")
            count = Donate.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug
        serializer = Donate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):
    try:
        data = request.data
        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Donate.objects.filter(title__exact=data['title']).exists():
            print("yes")
            count = Donate.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug

        donate = Donate.objects.get(slug=slugkey)
        serializer = Donate(donate, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, slug):
    try:
        donate = Donate.objects.get(slug=slug)
        donate.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data Deleted"
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

