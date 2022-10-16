from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import Group
from rest_framework.response import Response
from .serializers import *
# from django.contrib.auth.decorators import login_required
from .decorator import permission_required
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import views


# Create your views here.
# @permission_classes([IsAuthenticated])


@api_view(['GET'])
# @permission_required(['view_group'])
# @permission_classes([IsAuthenticated])
def group_list(request):
    group = Group.objects.all()
    serializer = GroupSerializer(group, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_required(['add_group'])
# @permission_classes([IsAuthenticated])
def create_group(request):
    name = request.data['name']
    group = Group(name=name)
    group.save()
    return Response(
        {
            'success': 'New Group Added',
            'group Id': group.id,
            'group name': group.name
        }
    )


@api_view(['PATCH'])
# @permission_required(['change_group'])
# @permission_classes([IsAuthenticated])
def update_group(request, pk):
    group_data = request.data
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(group, data=group_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_required(['delete_group'])
# @permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return Response('Deleted')


# Permission view funtions

@api_view(['GET'])
def permission_list(request):
    permissions = Permission.objects.all()
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data)
