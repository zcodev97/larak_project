from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from core.serializers import CustomUserSerializer
from .models import Order, Product, Category
from .serializers import (OrderSerializer, CategorySerializer, ProductSerializer, AddProductSerializer,
                          ClientProductSerializer, ClientOrdersSerializer, AddOrderSerializer)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken


class UserInfoFromToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Assuming you have a serializer for your user mouserdel
        user_serializer = CustomUserSerializer(request.user).data
        return Response({'user': user_serializer}, status=status.HTTP_200_OK)


class CategoriesList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class SingleCategory(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ClientProductsListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ClientProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class AddProductAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ClientOrdersListAPI(generics.ListCreateAPIView):
    serializer_class = ClientOrdersSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Get the current user from the request
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()

        return Order.objects.filter(client=user)[:100]


class AddOrderAPI(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddOrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class UpdateOrderAPI(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
