from rest_framework import serializers
from .models import Category, Book, Product, Cart
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'title',
			)
		model = Category


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'title',
			'category',
			'author',
			'isbn',
			'pages',
			'price',
			'stock',
			'description',
			'imageURL',
			'status',
			'created_at',
			)
		model = Book

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Product

class UserSerializer(serializers.ModelSerializer):
	books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
	products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'email',
			'books',
			'products',
		)

class CartUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):
	cart_id = CartUserSerializer(read_only=True, many=False)
	books = BookSerializer(read_only=True, many=True)
	products = ProductSerializer(read_only=True, many=True)
	class Meta:
		model = Cart
		fields = '__all__'

