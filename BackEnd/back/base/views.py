from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout


# Se puede introducir tanto username como email para loguearse
class LoginApiView(APIView):

    def post(self, request):
        # Al hacer el post ponle este nombre al input para que lo detecte bien
        username_or_email = request.data.get('username-email')
        password = request.data.get('password')

        if '@' in username_or_email:
            user = authenticate(email=username_or_email, password=password)
        else:
            user = authenticate(username=username_or_email, password=password)
            print(user)

        if user is not None and user.is_active:
            login(request, user)
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutApiView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UsersApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def allowed_urls(request, *args, **kwargs):
    urls = [
        {"POST": ["http://127.0.0.1:8000/api/login",
                  "http://127.0.0.1:8000/api/register",
                  "http://127.0.0.1:8000/api/users/"]
         },
        {"GET": ["http://127.0.0.1:8000/api/users",
                 "http://127.0.0.1:8000/api/users/<str:pk>"]},
    ]
    return Response(urls)
