from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect


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


class RegisterApiView(GenericAPIView):
    serializer_class = UserSerializer

    @method_decorator(csrf_protect)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

        except ValidationError as exc:
            return Response(exc.detail, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutApiView(APIView, LoginRequiredMixin):

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

