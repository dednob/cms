from django.shortcuts import render
from .models import Campaigns
from .serializers import CampaignsSerializer
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
    campaigns = Campaigns.objects.all()
    serializer = CampaignsSerializer(campaigns, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def campaign_detail(request, pk):
    id = pk
    if id is not None:
        campaigns = Campaigns.objects.get(id=id)
        serializer = CampaignsSerializer(campaigns)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def campaigns_by_projects(request, pk):
    id = pk
    campaigns = Campaigns.objects.filter(projects__id = id)
    serializer = CampaignsSerializer(campaigns, many=True)
    return Response(serializer.data)



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request):
    campaign_data = request.data
    if 'image' in campaign_data:
        fmt, img_str = str(campaign_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        campaign_data['image'] = img_file

    slug = slugify(campaign_data['title'])
    suffix = 1
    if Campaigns.objects.filter(title__exact=slug).exists():
        count = Campaigns.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

    campaign_data['slug'] = slug
    serializer = CampaignsSerializer(data=campaign_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    campaign_data = request.data
    if 'image' in campaign_data:
        fmt, img_str = str(campaign_data['image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        campaign_data['image'] = img_file

    slug = slugify(campaign_data['title'])
    suffix = 1
    if Campaigns.objects.filter(title__exact=slug).exists():
        count = Campaigns.objects.filter(title__exact=slug).count()
        print(count)
        suffix += count
        print("yes")
        slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

    else:
        slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

    project = Campaigns.objects.get(id=pk)
    serializer = CampaignsSerializer(project, data=campaign_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete(request, pk):
    campaign = Campaigns.objects.get(id=pk)
    campaign.delete()
    return Response('Deleted')
