import datetime
from abc import ABC
from django.conf import settings
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class AddCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'user_type', 'supervisor', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type'),
            supervisor=validated_data.get('supervisor'),
            is_active=False
        )
        user.groups.set([2])  # Set the default group
        return user


class UpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class AddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'user_type', 'supervisor', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type'),
            supervisor=validated_data.get('supervisor')
        )
        user.groups.set([1])  # Set the default group
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='user_type.title')
    supervisor = serializers.CharField(source='supervisor.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'supervisor', 'is_superuser',
                  'date_joined']

