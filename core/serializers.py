import datetime
from django.conf import settings
from rest_framework import serializers
from .models import User,UserInfo
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
            supervisor=validated_data.get('supervisor')
        )
        user.groups.set([2])  # Set the default group
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='user_type.title')
    supervisor = serializers.CharField(source='supervisor.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'supervisor', 'is_superuser',
                  'date_joined']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'lon', 'lat']

#  2 manager
#  5 admin
