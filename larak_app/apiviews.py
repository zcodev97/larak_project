from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Order, Product, Categorie
from .serializers import OrderSerializer, CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class SingleCategory(generics.RetrieveDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class SingleProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
