from .models import Home
from .serializers import HomeSerializer, HomeExperienceSerializer, AchievmentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from areaofwork.models import Areaofwork
from campaign.models import Campaigns
from projects.models import Projects
from gallery.models import Gallery
from contact.models import Contact
from aboutus.models import *
from reviews.models import *

from home.models import Achievement
from rest_framework import status



@api_view(['GET'])
def home_view(request):
    try:
        home = Home.objects.get(active=True)
        serializer = HomeSerializer(home)
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
def home_details(request, pk):
    try:
        home = Home.objects.get(id = pk)
        serializer = HomeSerializer(home)
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
def home_list(request):
    try:
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
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
def toggle_active_status(request, pk):
    try:
        home = Home.objects.get(id=pk)
        home.active = True
        home.save()
        home_list = Home.objects.exclude(id=pk)
        for home in home_list:
            home.active = False
            home.save()

        home1 = Home.objects.get(active=True)
        serializer = HomeSerializer(home1)

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
def experience_details(request):
    try:
        home = Home.objects.get(active=True)
        serializer = HomeExperienceSerializer(home)
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
def create_home(request):
    try:
        data = request.data
        # if 'image' in data:
        #     fmt, img_str = str(data['image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['image'] = img_file

        if 'top_banner_image' in data:
            print("ami top banner")
            fmt, img_str = str(data['top_banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['top_banner_image'] = img_file
        
        if 'overview_banner_image' in data:
            print("ami top banner")
            fmt, img_str = str(data['overview_banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['overview_banner_image'] = img_file
        # if 'mid_banner_image' in data:
        #     print("ami mid_banner_image")
        #     fmt, img_str = str(data['mid_banner_image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['mid_banner_image'] = img_file
        
        # if 'mid_layer_image' in data:
        #     print("ami mid_layer_image")
        #     fmt, img_str = str(data['mid_layer_image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['mid_layer_image'] = img_file
        
        if 'footer_image' in data:
            print("ami footer_image")
            fmt, img_str = str(data['footer_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['footer_image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Home.objects.filter(title__exact=data['title']).exists():
            count = Home.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug
        serializer = HomeSerializer(data=data)
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
    # return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    try:
        data = request.data
        home = Home.objects.get(id=pk)

        # if ('image' in data and data['image'] == None) and home.image != None:
        #     data.pop('image')
        
        if ('top_banner_image' in data and data['top_banner_image'] == None):
            data.pop('top_banner_image')

        if ('overview_banner_image' in data and data['overview_banner_image'] == None):
            data.pop('overview_banner_image')
        
        # if ('mid_banner_image' in data and data['mid_banner_image'] == None) and home.image != None:
        #     data.pop('mid_banner_image')
        
        # if ('mid_layer_image' in data and data['mid_layer_image'] == None) and home.image != None:
        #     data.pop('mid_layer_image')
        
        if ('footer_image' in data and data['footer_image'] == None):
            data.pop('footer_image')


        # if 'image' in data:
        #     fmt, img_str = str(data['image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['image'] = img_file

        if 'top_banner_image' in data:
            fmt, img_str = str(data['top_banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['top_banner_image'] = img_file
            
        if 'overview_banner_image' in data:
            print("ami top banner")
            fmt, img_str = str(data['overview_banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['overview_banner_image'] = img_file
        
        # if 'mid_banner_image' in data:
        #     fmt, img_str = str(data['mid_banner_image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['mid_banner_image'] = img_file
        
        # if 'mid_layer_image' in data:
        #     fmt, img_str = str(data['mid_layer_image']).split(';base64,')
        #     ext = fmt.split('/')[-1]
        #     img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        #     data['mid_layer_image'] = img_file
        
        if 'footer_image' in data:
            fmt, img_str = str(data['footer_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['footer_image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Home.objects.filter(title__exact=data['title']).exists():
            print("yes")
            count = Home.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug

        
        serializer = HomeSerializer(home, data=data, partial=True)
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
# def partial_update_home(request, pk=None):
#     id = pk
#     home = Home.objects.get(pk=id)
#     serializer = HomeSerializer(home, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'msg': 'Partial Data Updated'})
#     return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_home(request, pk):
    try:
        home = Home.objects.get(id=pk)
        home.delete()
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


# Achievement

@api_view(['GET'])
def achievement_view(request):
    try:
        achievement = Achievement.objects.last()
        serializer = AchievmentSerializer(achievement)
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

# @api_view(['GET'])
# def achievement_details(request, pk):
#     try:
#         achievement = Achievement.objects.get(id = pk)
#         serializer = AchievmentSerializer(achievement)
#         return Response({
#             'code': status.HTTP_200_OK,
#             'response': "Received Data Successfully",
#             "data": serializer.data
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })


@api_view(['GET'])
def achievement_list(request):
    try:
        achievement = Achievement.objects.all()
        serializer = AchievmentSerializer(achievement, many=True)
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
def update_achievement(request):
    try:
        achievement_data = request.data
        print(achievement_data)
        achievement = Achievement.objects.last()
        
        if achievement == None:
            print(achievement_data)

            if 'image' in achievement_data:
                fmt, img_str = str(achievement_data['image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                achievement_data['image'] = img_file

            if 'background_image' in achievement_data:
                print("ami top banner")
                fmt, img_str = str(achievement_data['background_image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                achievement_data['background_image'] = img_file

            slug = slugify(achievement_data['title'])
            suffix = 1

            if Achievement.objects.filter(title__exact=achievement_data['title']).exists():
                count = Achievement.objects.filter(title__exact=achievement_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(achievement_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(achievement_data['title']), suffix)
            
            achievement_data['slug'] = slug

            serializer = AchievmentSerializer(data = achievement_data, partial = True)
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

            if ('image' in achievement_data and achievement_data['image'] == None) and achievement.image != None:
                achievement_data.pop('image')
        
            if ('background_image' in achievement_data and achievement_data['background_image'] == None) and achievement.background_image != None:
                achievement_data.pop('background_image')

            



            if 'image' in achievement_data:
                fmt, img_str = str(achievement_data['image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                achievement_data['image'] = img_file

            if 'background_image' in achievement_data:
                print("ami top banner")
                fmt, img_str = str(achievement_data['background_image']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                achievement_data['background_image'] = img_file

            slug = slugify(achievement_data['title'])
            suffix = 1

            if Achievement.objects.filter(title__exact=achievement_data['title']).exists():
                count = Achievement.objects.filter(title__exact=achievement_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(achievement_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(achievement_data['title']), suffix)

            achievement_data['slug'] = slug

            serializer = AchievmentSerializer(achievement, data = achievement_data, partial = True)
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
# def create_achievement(request):
#     try:
#         data = request.data
#         if 'image' in data:
#             fmt, img_str = str(data['image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['image'] = img_file

#         if 'background_image' in data:
#             print("ami top banner")
#             fmt, img_str = str(data['background_image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['background_image'] = img_file
        
        

#         slug = slugify(data['title'])
#         suffix = 1

#         if Achievement.objects.filter(title__exact=data['title']).exists():
#             count = Achievement.objects.filter(title__exact=data['title']).count()
#             print(count)
#             suffix += count
#             print("yes")
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         else:
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         data['slug'] = slug
#         serializer = AchievmentSerializer(data=data)
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
# def update_achievement(request, pk):
#     try:
#         data = request.data
#         achievement = Achievement.objects.get(id=pk)

#         if ('image' in data and data['image'] == None) and achievement.image != None:
#             data.pop('image')
        
#         if ('background_image' in data and data['background_image'] == None) and achievement.background_image != None:
#             data.pop('background_image')


#         if 'image' in data:
#             fmt, img_str = str(data['image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['image'] = img_file

#         if 'background_image' in data:
#             fmt, img_str = str(data['background_image']).split(';base64,')
#             ext = fmt.split('/')[-1]
#             img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
#             data['background_image'] = img_file
        
        
#         slug = slugify(data['title'])
#         suffix = 1

#         if Achievement.objects.filter(title__exact=data['title']).exists():
#             print("yes")
#             count = Home.objects.filter(title__exact=data['title']).count()
#             print(count)
#             suffix += count
#             print("yes")
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         else:
#             slug = "%s-%s" % (slugify(data['title']), suffix)

#         data['slug'] = slug

        
#         serializer = AchievmentSerializer(achievement, data=data, partial=True)
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

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_achievement(request, pk):
#     try:
#         achievement = Achievement.objects.get(id=pk)
#         achievement.delete()
#         return Response({
#             'code': status.HTTP_200_OK,
#             'response': "Data Deleted"
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })


# @api_view(['GET'])
# def toggle_achievement_active_status(request, pk):
#     try:
#         achievement = Achievement.objects.get(id=pk)
#         achievement.active = True
#         achievement.save()
#         achievement_list = Achievement.objects.exclude(id=pk)
#         for achievement in achievement_list:
#             achievement.active = False
#             achievement.save()

#         achv1 = Achievement.objects.get(active=True)
#         serializer = AchievmentSerializer(achv1)

#         return Response({
#             'code': status.HTTP_200_OK,
#             'response': "Received Data Successfully",
#             "data": serializer.data
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })


@api_view(['GET'])
def work_list_count(request):
    try:
        areaofwork_count = Areaofwork.objects.all().count()
        project_count = Projects.objects.all().count()
        gallery_count = Gallery.objects.all().count()
        contact_count = Contact.objects.all().count()
        home_count = Home.objects.all().count()
        campaign_count = Campaigns.objects.all().count()
        # employee_count = Team.objects.all().count()
        review_count = Review.objects.all().count()
        
        return Response({
            'Response': 'Count received successfully',
            'Areaofwork': areaofwork_count,
            'projects': project_count,
            'gallery': gallery_count,
            'contact': contact_count,
            'home': home_count,
            'campaign' : campaign_count,
            # 'employee': employee_count,
            'reviews' : review_count
            

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })