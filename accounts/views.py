
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@api_view(['POST'])
def RegisterView(request):
    username = request.data['username']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    user = User(username=username, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            'success': 'You are authenticated',
            'user Id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'refresh': str(refresh),
            'access': str(refresh.access_token)}
    )
