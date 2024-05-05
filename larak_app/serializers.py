from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Product, Order, Category, EmployeeOrders
from core.models import User
from core.serializers import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    class Meta:
        model = Category
        fields = "__all__"


class GetEmployeeOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOrders
        fields = "__all__"


class AddEmployeeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOrders
        fields = ['employee', 'manager', 'cart', 'status']


class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    def get_client_name(self, obj):
        # Check if account_manager is set, handle potential None values
        if obj.client:
            return obj.client.username + obj.client.first_name  # Access the username attribute
        else:
            return None  # Return None or a default value if account_manager is missing

    class Meta:
        model = Order
        fields = ['order_id', 'client_name', 'created_at', 'status', 'cart']


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = "__all__"


class ClientProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'description', 'category', 'discount', 'price', 'on_home_screen', 'on_banner',
                  'active']


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ClientOrdersSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.username')

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'client', 'cart', 'status', 'created_at']


class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'client', 'cart', 'status', 'created_at']
