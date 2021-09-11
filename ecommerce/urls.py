from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='singlecategory'),
    path('books', ListBookView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='singlebook'),

    path('products', ListProductView.as_view(), name='products'),
    path('products/<int:pk>', DetailProductView.as_view(), name='singleproduct'),

    path('users', UserListView.as_view(), name='users'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user'),

    path('cart', CartListView.as_view(), name='carts'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cart_detail'),
]