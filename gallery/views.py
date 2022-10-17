from django.shortcuts import render
from .models import Gallery
from .serializers import GallerySerializer
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
    gallery = Gallery.objects.all()
    serializer = GallerySerializer(gallery, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def gallery_detail(request, slug):
    if slug is not None:
        gallery = Gallery.objects.get(slug=slug)
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def gallery_by_camp(request, slug):
    # campaign_id = pk
    gallery = Gallery.objects.filter(campaign__slug=slug)
    serializer = GallerySerializer(gallery, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def projects_by_aow(request, pk):
#     id = pk
#     project = Projects.objects.filter(areaofwork__id = id)
#     serializer = ProjectsSerializer(project, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def upload(request):
    gallery_data = request.data
    if 'image' in gallery_data:
        fmt, img_str = str(gallery_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        gallery_data['image'] = img_file

    slug = slugify(gallery_data['title'])
    suffix = 1
    if Gallery.objects.filter(title__exact=slug).exists():
        count = Gallery.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

    gallery_data['slug'] = slug

    serializer = GallerySerializer(data=gallery_data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def update(request, slugkey):
    gallery_data = request.data
    if 'image' in gallery_data:
        fmt, img_str = str(gallery_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        gallery_data['image'] = img_file

    slug = slugify(gallery_data['title'])
    suffix = 1
    if Gallery.objects.filter(title__exact=slug).exists():
        count = Gallery.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

    project = Gallery.objects.get(slug=slugkey)
    serializer = GallerySerializer(project, data=gallery_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete(request, slug):
    project = Gallery.objects.get(slug=slug)
    project.delete()
    return Response('Deleted')
