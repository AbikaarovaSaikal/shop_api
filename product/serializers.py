from rest_framework import serializers
from .models import Product, Category, Review
from django.db.models import Avg
# from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ReviewValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price category'.split()

class ProductValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category', 'reviews', 'rating']

    def get_category(self, product):
        return product.category.name if product.category else None

    def get_rating(self, product):
        return product.reviews.aggregate(
            avg=Avg('stars')
        )['avg']


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, category):
        return category.products.count()

class CategoryValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


    
# class CategoryListSerializer(serializers.ModelSerializer):
#     products_count = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Category
#         fields = ['name', 'products_count']

#     def get_products_count(self, category):
#         return category.products.count()

# class CategoryDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class ProductListSerializer(serializers.ModelSerializer):
#     reviews = serializers.SerializerMethodField()
#     rating = serializers.SerializerMethodField()
#     category = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = 'title price reviews category rating'.split()

#     def get_reviews(self, product):
#         return ReviewSerializer(product.reviews.all(), many=True).data
    
#     def get_category(self, product):
#         return product.category.name if product.category else None
    
#     def get_rating(self, product):
#         return product.reviews.aggregate(
#             avg=Avg('stars')
#         )['avg']

# class ProductDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class ReviewListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['text']

# class ReviewDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


# class CategoryValidateSerializer(serializers.Serializer):
#     name = serializers.CharField(min_length=3, max_length=255)
    

# class ProductValidateSerializer(serializers.Serializer):
#     title = serializers.CharField(min_length=3, max_length=255)
#     description = serializers.CharField(required=False, default='Not description')
#     price = serializers.IntegerField(default=0)
#     category_id = serializers.IntegerField()
    
#     def validate_category_id(self, category_id):
#         try:
#             Category.objects.get(id=category_id)
#         except Category.DoesNotExist:
#             raise ValidationError('Category does not exist!')
#         return category_id


# class ReviewValidateSerializer(serializers.Serializer):
#     text = serializers.CharField(required=False)
#     stars = serializers.FloatField(min_value=0, max_value=5)
#     product_id = serializers.IntegerField()

#     def validate_product_id(self, product_id):
#         try:
#             Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             raise ValidationError('Product does not exist!')
#         return product_id