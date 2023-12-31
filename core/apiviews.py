import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from core.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.conf import settings
from .models import User


class RecentRegisteredClients(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Get the current user from the request
        user = self.request.user

        # Calculate the start date of the recent month
        today = datetime.datetime.now()
        start_of_month = today.replace(day=1)
        User.objects.filter(userType__title__in=['supervisor', 'subuser'])
        # Filter the queryset to return records created by this user from this month
        return User.objects.filter(date_joined__gte=start_of_month)



