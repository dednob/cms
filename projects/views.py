from django.shortcuts import render
from .models import Projects
from .serializers import ProjectsSerializer, ProjectsListSerializer, ProjectsReadSerializer
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
def list(request):
    try:
        project = Projects.objects.all()
        serializer = ProjectsListSerializer(project, many=True)
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


@api_view(['GET'])
def project_detail(request, slug):
    try:
        slug = slug
        if id is not None:
            project = Projects.objects.get(slug=slug)
            serializer = ProjectsReadSerializer(project)
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


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def projects_by_aow(request, slug):
    try:
        project = Projects.objects.filter(areaofwork__slug=slug)
        serializer = ProjectsReadSerializer(project, many=True)
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
        project_data = request.data
        if 'image' in project_data and project_data['image'] != None:
            fmt, img_str = str(project_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            project_data['image'] = img_file

        slug = slugify(project_data['title'])
        suffix = 1
        if Projects.objects.filter(title__exact=project_data['title']).exists():
            count = Projects.objects.filter(title__exact=project_data['title']).count()
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
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Created Data Successfully",
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
        project_data = request.data
        project = Projects.objects.get(slug=slugkey)

        if ('image' in project_data and project_data['image']==None) and project.image!=None:
            
            project_data.pop('image')

        if 'image' in project_data and project_data['image'] != None:
            fmt, img_str = str(project_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            project_data['image'] = img_file

        # slug = slugify(project_data['title'])
        suffix = 1
        if Projects.objects.filter(title__exact=project_data['title']).exists():
            count = Projects.objects.filter(title__exact=project_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(project_data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(project_data['title']), suffix)

        project_data['slug'] = slug

        
        serializer = ProjectsSerializer(project, data=project_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Updated Data Successfully",
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
        project = Projects.objects.get(slug=slug)
        project.delete()
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


@api_view(['GET'])
def featured_project(request):
    try:
        project = Projects.objects.filter(featured=True)
        serializer = ProjectsListSerializer(project, many=True)
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