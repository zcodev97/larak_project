from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.db.models import Q
from core.models import User
from core.serializers import CustomUserSerializer
from .models import Order, Product, Category, EmployeeOrders
from .serializers import (OrderSerializer, CategorySerializer,
                          ProductSerializer, AddProductSerializer,
                          ClientProductSerializer,
                          ClientOrdersSerializer, AddOrderSerializer,
                          OrderUpdateSerializer, AddEmployeeOrderSerializer,
                          GetEmployeeOrdersSerializer, UpdateEmployeeOrderSerializer
                          )
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination


# class UserInfoFromToken(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         # Assuming you have a serializer for your user mouserdel
#         user_serializer = CustomUserSerializer(request.user).data
#         return Response({'user': user_serializer}, status=status.HTTP_200_OK)


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


class OrdersListAPI(generics.ListCreateAPIView):
    serializer_class = ClientOrdersSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Get the current user from the request
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()

        return Order.objects.filter(client=user).order_by('created_at')


class AdminOrdersListAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        biker_username = self.request.user.username
        return Order.objects.filter(
            Q(status__contains={"biker_status": {"title": "delivered"}}) |
            Q(status__contains={"biker_status": {"title": "rejected"}}) | Q(
                status__contains={"biker_status": {"title": "accepted"}}),
        ).order_by('-created_at')


class AdminCurrentOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        biker_username = self.request.user.username
        return Order.objects.filter(

            Q(
                status__contains={"biker_status": None},
            )
        )


class EmployeeOrderListAPI(generics.ListCreateAPIView):
    serializer_class = ClientOrdersSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        username = self.kwargs['client']
        user = User.objects.get(username=username)
        return Order.objects.filter(client=user)


class AddOrderAPI(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddOrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class UpdateOrderAPI(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


# biker apis

class BikerOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        biker_username = self.request.user.username
        return Order.objects.filter(
            Q(status__contains={"biker_status": {"biker": biker_username},"arrived_status": True}) | Q(status__contains={"biker_status": {"biker": biker_username},"arrived_status": False})
        ).order_by('-created_at')


class BikerCurrentOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        biker_username = self.request.user.username
        return Order.objects.filter(
            Q(status__contains={"biker_status": {"biker": biker_username, }, "arrived_status": None}, )
        ).order_by('-created_at')


class CompletedOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        biker_username = self.request.user.username
        return Order.objects.filter(
            Q(status__contains={"arrived_status": True}, )
        ).order_by('-created_at')


class AddEmployeeOrderAPI(generics.CreateAPIView):
    queryset = EmployeeOrders.objects.all()
    serializer_class = AddEmployeeOrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class UpdateEmployeeOrderAPI(generics.UpdateAPIView):
    queryset = EmployeeOrders.objects.all()
    serializer_class = UpdateEmployeeOrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GetEmployeeOrdersAPI(generics.ListAPIView):
    serializer_class = GetEmployeeOrdersSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        user = self.request.user
        return EmployeeOrders.objects.filter(
            # Q(status__contains={"manager_action": {"title": None}}) |
            # Q(status__contains={"manager_action": {"title": "accepted"}}),
            employee=user
        ).order_by('created_at')


class GetEmployeeOrdersForSupervisorAPI(generics.ListAPIView):
    serializer_class = GetEmployeeOrdersSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        user = self.request.user
        employee = self.request.query_params.get('employee')
        return EmployeeOrders.objects.filter(
            Q(
                status__contains={"manager_action": None},
            ), employee__username=employee, manager__username=user)
