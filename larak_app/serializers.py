from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Product, Order, Categorie


class ProductSerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    class Meta:
        model = Categorie
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    # book_title = serializers.CharField(source='book.title')
    class Meta:
        model = Order
        fields = "__all__"
