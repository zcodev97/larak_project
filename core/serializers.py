import datetime
from django.conf import settings
from rest_framework import serializers
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='user_type.title')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'user_type', 'supervisor',
                  'date_joined']
