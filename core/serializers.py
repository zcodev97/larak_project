import datetime

from django.conf import settings
# from .models import User
from rest_framework import serializers
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    userType = serializers.CharField(source='userType.title')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'userType']
