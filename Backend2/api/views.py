from django.shortcuts import render
from .models import UserProfile

# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserRegisterSerializer, UserProfileSerializer
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile


# Se puede introducir tanto username como email para loguearse
class LoginApiView(APIView):

    # Por ahora el inicio de sesion se maneja con sesiones, pero para mejor escalabilidad, usar Tokens
    def post(self, request, *args, **kwargs):
        # Al hacer el post ponle este nombre al input para que lo detecte bien
        username_or_email = request.data.get('username-email')
        password = request.data.get('password')

        if '@' in username_or_email:
            user = User.objects.get(email=username_or_email)
        else:
            user = authenticate(username=username_or_email, password=password)

        if user is not None and user.is_active:
            # token, created = Token.objects.get_or_create(user)
            user_profile = user.userprofile
            user_profile_serializer = UserProfileSerializer(user_profile)
            login(request, user)
            return Response({"user": user_profile_serializer.data}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterApiView(APIView):

    def post(self, request):
        serializer_user = UserRegisterSerializer(data=request.data)

        if serializer_user.is_valid(raise_exception=True):
            username = serializer_user.validated_data['email'].split('@')[0]
            user = User.objects.create(
                username=username,
                email=serializer_user.validated_data['email'],
                password=serializer_user.validated_data['password']
            )

            user_profile = UserProfile.objects.create(user_id=user.id)
            return Response("User registered without errors", status=status.HTTP_200_OK)


class CreateUserProfile(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


class UpdateUserProfile(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        user = profile.user

        if user.username != request.data['user.username']:
            user.username = request.data['user.username']
            user.save()

        profile.name = request.data['name']
        profile.bio = request.data['bio']
        profile.save()

        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view(['GET'])
def allowed_urls(request):
    urls = [
        {
            "POST": ["http://127.0.0.1:8000/api/login",
                     "http://127.0.0.1:8000/api/register",
                     "http://127.0.0.1:8000/api/logout",
                     ]
        },
        {
            "GET": ["http://127.0.0.1:8000/api/users",
                    "http://127.0.0.1:8000/api/users/<str:pk>",
                    ]
        },
        {
            "PUT": "http://127.0.0.1:8000/api/update-user/<str:pk>"
        }
    ]
    return Response(urls)
