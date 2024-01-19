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
    # author_username = serializers.CharField(source='author.username')
    # category = CategorySerializer()
    # user = CustomUserSerializer()
    # def create(self, validated_data):
    #     # Extract the specialty data
    #     category_data = validated_data.pop('category', None)
    #     category_data = validated_data.pop('created_by', None)
    #     # Create or update the Specialty object
    #     category_instance, created = Categorie.objects.get_or_create(**category_data)
    #     # Set the specialty_instance on the InsideCoursesRecord instance
    #     validated_data['category'] = category_instance
    #     # Create the InsideCoursesRecord instance
    #     instance = Categorie.objects.create(**validated_data)
    #
    #     return instance
    class Meta:
        model = Product
        fields = "__all__"
