import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from core.serializers import (CustomUserSerializer, AddCustomUserSerializer,
                              GetUserInfoSerializer,
                              AddUserInfoSerializer, AddEmployeeSerializer, UpdatePasswordSerializer)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from django.conf import settings
from .models import User, UserInfo


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


class AddUserInfoAPI(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = AddUserInfoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            user_info = UserInfo.objects.get(user=user)
            serializer = self.get_serializer(user_info, data=request.data)
        except UserInfo.DoesNotExist:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserInfoAPI(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = GetUserInfoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        id = request.user
        try:
            user_info = UserInfo.objects.get(user_id=id)
            serializer = self.get_serializer(user_info)
            return Response(serializer.data)
        except UserInfo.DoesNotExist:
            return Response({'error': 'User information not found'}, status=status.HTTP_404_NOT_FOUND)


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


class UsersUnderManagerAPI(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        manager = self.request.user
        return User.objects.filter(supervisor=manager, user_type__title__in=['user'])
