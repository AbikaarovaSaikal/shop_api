from rest_framework import serializers
from .models import Product, Category, Review
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['name', 'products_count']

    def get_products_count(self, category):
        return category.products.count()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'title price reviews category rating'.split()

    def get_reviews(self, product):
        return ReviewSerializer(product.reviews.all(), many=True).data
    
    def get_category(self, product):
        return product.category.name if product.category else None
    
    def get_rating(self, product):
        return product.reviews.aggregate(
            avg=Avg('stars')
        )['avg']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'