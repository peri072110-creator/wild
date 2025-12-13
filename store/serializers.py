from .models import (
                     UserProfile, Category, SubCategory,
                     Product, ProductImage, Review,
                     Cart, CartItem)
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'username',  'phone_number',  'password', 'email', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class  UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_image', 'category_name']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image']

class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    created_date = serializers.DateTimeField(format='%d/%m/%Y', read_only=True)
    sub_category_name = CategoryListSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'images', 'price',
                  'product_type', 'created_date', 'get_avg_rating', 'sub_category_name']
    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

class SubCategoryListSerializer(serializers.ModelSerializer):
            class Meta:
                model = SubCategory
                fields = ['id', 'sub_category_name']

class SubCategorySimpleSerializer(serializers.ModelSerializer):
           class Meta:
                model = SubCategory
                fields = ['sub_category_name']

class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products =  ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['sub_category_name', 'products']

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryListSerializer(many=True, read_only=True)
    image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'sub_category', 'image',]

class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', read_only=True)
    user = UserProfileSimpleSerializer(read_only=True)
    class Meta:
        model = Review
        fields =  ['user', 'stars', 'comment', 'created_date']

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', read_only=True)
    sub_category = SubCategorySimpleSerializer(read_only=True)

    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['sub_category', 'product_name', 'images','price', 'product_type',
                  'description','video','created_date','reviews']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'