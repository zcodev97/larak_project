from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from core.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.conf import settings
from .models import User


class ClientsList(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.filter(userType__title__in=['supervisor', 'subuser'])
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
