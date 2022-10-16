from django.shortcuts import render
from .models import Donate
from .serializers import DonateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def details(request):
    donate = Donate.objects.all()
    serializer = DonateSerializer(donate, many=True)
    return Response(serializer.data)




@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

    slug = slugify(data['title'])
    suffix = 1

    if Donate.objects.filter(title__exact=slug).exists():
        print("yes")
        count = Donate.objects.filter(title__exact=slug).count()
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
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def update(request, pk):
    data = request.data
    if 'image' in data:
        fmt, img_str = str(data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        data['image'] = img_file

    slug = slugify(data['title'])
    suffix = 1

    if Donate.objects.filter(title__exact=slug).exists():
        print("yes")
        count = Donate.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(data['title']), suffix)

    data['slug'] = slug

    donate = Donate.objects.get(id=pk)
    serializer = Donate(donate, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete(request, pk):
    donate = Donate.objects.get(id=pk)
    donate.delete()
    return Response('Deleted')
