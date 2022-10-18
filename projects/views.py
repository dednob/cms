from django.shortcuts import render
from .models import Projects
from .serializers import ProjectsSerializer, ProjectsListSerializer
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
    project = Projects.objects.all()
    serializer = ProjectsListSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, slug):
    slug = slug
    if id is not None:
        project = Projects.objects.get(slug=slug)
        serializer = ProjectsSerializer(project)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def projects_by_aow(request, slug):
    project = Projects.objects.filter(areaofwork__slug=slug)
    serializer = ProjectsSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request):
    project_data = request.data
    if 'image' in project_data:
        fmt, img_str = str(project_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        project_data['image'] = img_file

    slug = slugify(project_data['title'])
    suffix = 1
    if Projects.objects.filter(slug__exact=slug).exists():
        count = Projects.objects.filter(slug__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(project_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(project_data['title']), suffix)

    project_data['slug'] = slug
    serializer = ProjectsSerializer(data=project_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def update(request, slugkey):
    project_data = request.data
    if 'image' in project_data:
        fmt, img_str = str(project_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        project_data['image'] = img_file

    slug = slugify(project_data['title'])
    suffix = 1
    if Projects.objects.filter(slug__exact=slug).exists():
        count = Projects.objects.filter(slug__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(project_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(project_data['title']), suffix)

    project = Projects.objects.get(slug=slugkey)
    serializer = ProjectsSerializer(project, data=project_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete(request, slug):
    project = Projects.objects.get(slug=slug)
    project.delete()
    return Response('Deleted')


@api_view(['GET'])
def featured_project(request):
    project = Projects.objects.filter(featured=True)
    serializer = ProjectsListSerializer(project, many=True)
    return Response(serializer.data)
