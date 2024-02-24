import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from core.serializers import CustomUserSerializer, AddCustomUserSerializer, UserInfoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from django.conf import settings
from .models import User, UserInfo


class AddUserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AddCustomUserSerializer
    permission_classes = [AllowAny]


class AddUserInfoAPI(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GetUserInfoAPI(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class UsersListAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return User.objects.filter(user_type__title__in=['manager', 'user'])


class BikersListAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return User.objects.filter(user_type__title__in=['biker'])
