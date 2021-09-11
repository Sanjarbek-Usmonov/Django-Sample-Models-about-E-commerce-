from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, CartSerializer, UserSerializer
from .models import Category, Product, Book, Cart
from rest_framework import permissions
from django.contrib.auth.models import User

class CategoryListView(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ListBookView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = BookSerializer
	queryset = Book.objects.all()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class ListProductView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class DetailProductView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class UserListView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CartListView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

