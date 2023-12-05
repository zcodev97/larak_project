from rest_framework import serializers

from rest_framework.authtoken.models import Token

from .models import Product, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)

        return user


class BookSerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')

    class Meta:
        model = Book

        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    # author_username = serializers.CharField(source='author.username')
    # book_title = serializers.CharField(source='book.title')
    class Meta:
        model = BooksRating
        fields = "__all__"
