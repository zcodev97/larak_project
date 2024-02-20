import datetime
from django.conf import settings
from rest_framework import serializers
from .models import User


class AddCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone',
                  'user_type', 'supervisor']


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='user_type.title')
    supervisor = serializers.CharField(source='supervisor.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone',
                  'user_type', 'supervisor', 'is_superuser',
                  'date_joined','groups']

#  2 manager
#  5 admin
