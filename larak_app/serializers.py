from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Product, Order, Category
from core.models import User
from core.serializers import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    class Meta:
        model = Category
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    # book_title = serializers.CharField(source='book.title')
    class Meta:
        model = Order
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = "__all__"


class ClientProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ['id', 'image', 'title', 'description', 'category', 'discount', 'price', 'on_home_screen','on_banner',]


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ClientOrdersSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.username')


    class Meta:
        model = Order
        fields = ['id','order_id', 'client','cart','status','created_at']


class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [ 'order_id', 'client','cart','status','created_at']
