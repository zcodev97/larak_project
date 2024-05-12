import datetime

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from core.serializers import (CustomUserSerializer, AddCustomUserSerializer, AddEmployeeSerializer,
                              UpdatePasswordSerializer, AddUserInfoSerializer, CustomClientsSerializer)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from django.conf import settings
from .models import User


class UpdatePasswordAPI(generics.GenericAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddUserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AddCustomUserSerializer
    permission_classes = [AllowAny]


class AddEmployeeAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AddEmployeeSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GetUserInfoAPI(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).first()


class AddUserInfoAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AddUserInfoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class UsersListAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return User.objects.filter(user_type__title__in=['manager', 'user'])


class BikersListAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    paginator = PageNumberPagination()
    paginator.page_size = None

    def get_queryset(self):
        return User.objects.filter(user_type__title__in=['biker'])


class UsersUnderManagerAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(supervisor=manager, user_type__title__in=['user'])


class UsersUnderManagersAPI(generics.ListCreateAPIView):
    serializer_class = CustomClientsSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(user_type__title__in=['user'])


class UsersManagersAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(user_type__title__in=['manager'])


class UsersBikersAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(user_type__title__in=['biker'])


class SystemUsersAPI(generics.ListCreateAPIView):
    serializer_class = CustomClientsSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        excluded_types = ['biker', 'manager', 'user']  # User types to exclude
        return User.objects.exclude(user_type__title__in=excluded_types)
