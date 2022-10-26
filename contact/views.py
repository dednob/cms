from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def message_details(request, pk):
    contact = Contact.objects.get(id = pk)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    data = request.data 
    serializer = ContactSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response('Deleted')


