from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Campaigns
from .serializers import CampaignsSerializer, CampaignsListSerializer
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
    serializer = CampaignsListSerializer(campaigns, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def campaign_detail(request, slug):

    if slug is not None:
        campaigns = Campaigns.objects.get(slug=slug)
        serializer = CampaignsSerializer(campaigns)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def campaigns_by_projects(request, slug):

    campaigns = Campaigns.objects.filter(projects__slug=slug)
    serializer = CampaignsSerializer(campaigns, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def related_campaigns(request, slug):

    campaigns = Campaigns.objects.filter(projects__slug=slug)
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
def update(request, slugkey):
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

    project = Campaigns.objects.get(slug=slugkey)
    serializer = CampaignsSerializer(project, data=campaign_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete(request, slug):
    campaign = Campaigns.objects.get(slug=slug)
    campaign.delete()
    return Response('Deleted')
