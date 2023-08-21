from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

    # def validate(self, attrs):
    #     email_exists = User.objects.filter(email=attrs['email']).exists()
    #
    #     if email_exists:
    #         raise ValidationError('Email already in use')
    #
    #     return super().validate(attrs)
    #
    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user
