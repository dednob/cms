from django.shortcuts import render
from .models import *
from .serializers import *
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
        aboutus = Aboutus.objects.all()
        serializer = AboutusSerializer(aboutus, many=True)
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
def about_view(request):
    try:
        about = Aboutus.objects.last()
        serializer = AboutusSerializer(about)
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
def about_details(request, pk):
    try:
        about = Aboutus.objects.get(id = pk)
        serializer = AboutusSerializer(about)
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
def update_aboutus(request):
    try:
        aboutus_data = request.data
        print(aboutus_data)
        aboutus = Aboutus.objects.last()
        
        if aboutus == None:
            print(aboutus_data)

            if 'image' in aboutus_data:
                fmt, img_str = str(aboutus_data['image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                aboutus_data['image'] = img_file


            slug = slugify(aboutus_data['title'])
            suffix = 1
            if Aboutus.objects.filter(title__exact=aboutus_data['title']).exists():
                count = Aboutus.objects.filter(title__exact=aboutus_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(aboutus_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(aboutus_data['title']), suffix)

            aboutus_data['slug'] = slug
            serializer = AboutusSerializer(data=aboutus_data)

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

        else:
            print("Ami Running")

            if ('image' in aboutus_data and aboutus_data['image'] == None) and aboutus.image != None:
                aboutus_data.pop('image')

            if 'image' in aboutus_data:
                fmt, img_str = str(aboutus_data['image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                aboutus_data['image'] = img_file

            suffix = 1
            if Aboutus.objects.filter(title__exact=aboutus_data['title']).exists():
                count = Aboutus.objects.filter(title__exact=aboutus_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(aboutus_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(aboutus_data['title']), suffix)

            aboutus_data['slug'] = slug

            serializer = AboutusSerializer(aboutus, data = aboutus_data, partial = True)
            if serializer.is_valid():
                serializer.save()    
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Data updated successfully",
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






# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create(request):
#     try:
#         data = request.data
#         if 'image' in data:
#             fmt, img_str = str(data['image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['image'] = img_file

#         slug = slugify(data['title'])
#         suffix = 1
#         if Aboutus.objects.filter(title__exact=data['title']).exists():
#             count = Aboutus.objects.filter(title__exact=data['title']).count()
#             print(count)
#             suffix += count
#             print("yes")
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         else:
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         data['slug'] = slug
#         serializer = AboutusSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'code': status.HTTP_200_OK,
#                 'response': "Received Data Successfully",
#                 "data": serializer.data
#             })
#         else:
#             return Response({
#                 'code': status.HTTP_400_BAD_REQUEST,
#                 'response': "Data not Valid",
#                 'error': serializer.errors
#             })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def update(request, pk):
#     try:
#         data = request.data
#         aboutus = Aboutus.objects.get(id=pk)
#         if ('image' in data and data['image'] == None) and aboutus.image != None:
#             data.pop('image')

#         if 'image' in data:
#             fmt, img_str = str(data['image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['image'] = img_file

#         # slug = slugify(data['title'])
#         suffix = 1
#         if Aboutus.objects.filter(title__exact=data['title']).exists():
#             count = Aboutus.objects.filter(title__exact=data['title']).count()
#             print(count)
#             suffix += count
#             print("yes")
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         else:
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         data['slug'] = slug

        
#         serializer = AboutusSerializer(aboutus, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'code': status.HTTP_200_OK,
#                 'response': "Received Data Successfully",
#                 "data": serializer.data
#             })
#         else:
#             return Response({
#                 'code': status.HTTP_400_BAD_REQUEST,
#                 'response': "Data not Valid",
#                 'error': serializer.errors
#             })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def partial_update(request, pk=None):
#     id = pk
#     aboutus = Aboutus.objects.get(pk=id)
#     serializer = AboutusSerializer(aboutus, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'msg': 'Partial Data Updated'})
#     return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    try:
        aboutus = Aboutus.objects.get(id=pk)
        aboutus.delete()
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
def toggle_aboutus_active_status(request, pk):
    try:
        about = Aboutus.objects.get(id=pk)
        about.active = True
        about.save()
        about_list = Aboutus.objects.exclude(id=pk)
        for about in about_list:
            about.active = False
            about.save()

        about = Aboutus.objects.get(active=True)
        serializer = AboutusSerializer(about)

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







#Team

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def team_list(request):
    try:
        team = Team.objects.all().order_by('priority')
        serializer = TeamSerializer(team, many=True)
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
def team_create(request):
    try:
        data = request.data
        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        
        serializer = TeamSerializer(data=data)
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
def team_update(request, pk):
    try:
        data = request.data
        team = Team.objects.get(id=pk)
        
        if ('image' in data and data['image'] == None) and team.image != None:
            data.pop('image')

        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        
        serializer = TeamSerializer(team, data=data, partial=True)
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

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def partial_update(request, pk=None):
#     id = pk
#     aboutus = Aboutus.objects.get(pk=id)
#     serializer = AboutusSerializer(aboutus, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'msg': 'Partial Data Updated'})
#     return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def team_delete(request, pk):
    try:
        team = Team.objects.get(id=pk)
        team.delete()
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