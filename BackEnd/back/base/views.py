import hashlib
import secrets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout


# Se puede introducir tanto username como email para loguearse
class LoginApiView(APIView):

    # Por ahora el inicio de sesion se maneja con sesiones, pero para mejor escalabilidad, usar Tokens
    def post(self, request):
        # Al hacer el post ponle este nombre al input para que lo detecte bien
        username_or_email = request.data.get('username-email')
        password = request.data.get('password')

        if '@' in username_or_email:
            user = authenticate(email=username_or_email, password=password)
        else:
            user = authenticate(username=username_or_email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # token = self.generate_token(user)
            data = {
                'id': user.id,
                'username': user.username,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

    # def generate_token(self, user):
    #     token = secrets.token_hex(32)
    #     hash_token = hashlib.sha256(token.encode('utf-8')).hexdigest()
    #     return token


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def logout_user(request):
    logout(request)


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
                  "http://127.0.0.1:8000/api/register"
                  ]
         },
        {"GET": ["http://127.0.0.1:8000/api/users",
                 "http://127.0.0.1:8000/api/users/<str:pk>"]},
    ]
    return Response(urls)
