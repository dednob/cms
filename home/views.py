from .models import Home
from .serializers import HomeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from areaofwork .models import Areaofwork
from campaign .models import Campaigns
from projects .models import Projects

@api_view(['GET'])
def home_details(request):
    home = Home.objects.all()
    serializer = HomeSerializer(home, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def experience_details(request):
    return Response({
        'Establish year': "1900",
        "AreaofWork": Areaofwork.objects.all().count(),
        "Campaigns": Campaigns.objects.all().count(),
        "Projects": Projects.objects.all().count()

    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_home(request):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

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
        return Response(serializer.data)
    return Response(serializer.errors)
<<<<<<< HEAD
=======

>>>>>>> eed35fcefab2e15f90b688a8e945612f55ac7a25

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

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

    home = Home.objects.get(slug=slugkey)
    serializer = HomeSerializer(home, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


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
def delete_home(request, slug):
    home = Home.objects.get(slug=slug)
    home.delete()
    return Response('Deleted')
