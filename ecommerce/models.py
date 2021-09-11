from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title



class Book(models.Model):
	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
	author = models.CharField(max_length=100, null=True)
	isbn = models.CharField(max_length=13)
	pages = models.IntegerField()
	price = models.IntegerField()
	stock = models.IntegerField()
	description = models.TextField()
	imageURL = models.URLField()
	status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title



class Product(models.Model):
	product_tag = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	price = models.IntegerField()
	stock = models.IntegerField()
	imageURL = models.URLField()
	status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.product_tag} {self.name}"

class Cart(models.Model):
	cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	books = models.ManyToManyField(Book)
	products = models.ManyToManyField(Product)

	class Meta:
		ordering = ['cart_id']

	def __str__(self):
		return f"{self.cart_id}"

